---
title: 'Friday Q&A 2013-09-13: A Library for Easier Property List Type Checking and Error Reporting'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-09-13-a-library-for-easier-property-list-type-checking-and-error-reporting.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ee7987e21436f82b'
translated: false
---

> 原文：[Friday Q&A 2013-09-13: A Library for Easier Property List Type Checking and Error Reporting](https://www.mikeash.com/pyblog/friday-qa-2013-09-13-a-library-for-easier-property-list-type-checking-and-error-reporting.html)　·　mikeash.com Friday Q&A

Posted at 2013-09-13 15:35 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-09-27: ARM64 and You](https://www.mikeash.com/pyblog/friday-qa-2013-09-27-arm64-and-you.html)  
Previous article: [Friday Q&A 2013-08-30: Model Serialization With Property Lists](https://www.mikeash.com/pyblog/friday-qa-2013-08-30-model-serialization-with-property-lists.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [plist](https://www.mikeash.com/pyblog/?tag=plist) [serialization](https://www.mikeash.com/pyblog/?tag=serialization)

Friday Q&A 2013-09-13: A Library for Easier Property List Type Checking and Error Reporting

by [Mike Ash](https://www.mikeash.com/)

**Inspiration**  
This will probably shock a lot of my readers, but I really like the [Java JSON library](http://json.org/java/) and its approach to type-checking.

It makes extensive use of exceptions and, while I often find exceptions to be overused for signaling errors in languages like Java, it works out extremely well here. There are methods to fetch optional and required objects of the various JSON types. If there's a type mismatch, or a required key is missing, the library throws an exception. The resulting code can put almost all of the error handling code in one place. For example:

```
    JSONObject obj = ...;
    try {
        JSONArray requiredArray = obj.getArray("array");
        long requiredLong = obj.getLong("number");
        String optionalString = obj.optString("string");
        ...use the values...
    } catch(JSONException e) {
        ...handle the error...
    }
```

This is much nicer than manually checking for errors with every value that comes out. There are some warts in the implementation (for example, `optString` will return the string representation of whatever object is there, even if it's not a string, which is absurd), but the concept is great.

Unfortunately, this design is not viable in Objective-C because exceptions are so poorly supported. Throwing exceptions for recoverable errors tends to enrage programmers trying to debug code, as a debugger breakpoint on thrown exceptions is a standard way to catch errors in Objective-C, and false positives are irritating to deal with. Further, since Objective-C doesn't check exceptions and Objective-C programmers aren't expecting to deal with them, it's far too easy to write code that doesn't `@catch` them, resulting in crashes or other misbehavior when they get thrown. Finally, code compiled with ARC is not exception-safe by default, so using a library like this _at all_ in ARC code would require nonstandard compiler flags in order to enable exception safety.

However, I think I've come up with an API that's similar in spirit to the ideal design I want, without requiring exceptions or other such nastiness.

**Code**  
The library is available on GitHub:

[https://github.com/mikeash/MAPlistTypeChecking](https://github.com/mikeash/MAPlistTypeChecking)

I will be walking through the basic operation and usage of the library here, but I won't actually be doing a thorough line-by-line walkthrough like I sometimes do, so if you're interested in details, check out the code there.

**Basic Design**  
The idea is to construct a tree of proxy objects. The top-level dictionary (or array) is wrapped in a proxy dictionary. When objects within that dictionary are requested, it fetches objects out of the original dictionary and wraps them in their own proxy objects.

I've termed these objects _error reporting objects_, which is vague and imprecise, but as they say, there are two hard problems in computer science: naming things, cache invalidation, and [fencepost errors](http://en.wikipedia.org/wiki/Fencepost_error#Fencepost_error).

Each error reporting object keeps track of its parent object and a list of reported errors:

```
    id _parent;
    NSMutableArray *_errors;
```

The errors are exposed through a method, and another method allows adding additional errors to the array:

```
    - (void)addError: (NSError *)error;
    - (NSArray *)errors;
```

The `addError:` method not only adds the error to the array, but it also calls the `addError:` method of its parent. The parent will then do the same thing, such that errors percolate up from whatever object is currently being worked on to the top-level object. Code reading from the property list can then set errors on individual objects within the property list, and the very top level of the code can then just check the top-level object for errors.

Manually setting errors on the property list objects is painful, of course, so there are helper methods that handle everything. `NSObject` gets two new class methods:

```
    + (instancetype)ma_castRequiredObject: (id)obj;
    + (instancetype)ma_castOptionalObject: (id)obj;
```

These take advantage of the new `instancetype` meta-type in Objective-C, such that an expression like `[NSString castRequiredObject: ...]` ends up with the type `NSString *` instead of just a generic `id`, allowing the compiler to better type-check the entire statement.

In addition to doing compile-time type casting, these methods also do runtime type checking. If the object is not of the correct type, _and_ it's an error reporting object, these methods generate an appropriate `NSError` object and set it on the object, which causes it to be reported up the chain. Additionally, dictionaries return a wrapper for `nil` values so that the `ma_castRequiredObject:` can report an error up the chain for missing values.

**Key Paths**  
Simply knowing that some object was missing or had the wrong type isn't very useful. For the error to have some value beyond "something went wrong", you need to know exactly which object caused the problem.

Each error reporting object also tracks the key it came from. For objects retrieved from dictionaries, this is the dictionary key. For objects retrieved from arrays, this is the array index as an `NSNumber`.

When an error is added to an error reporting object, it generates a new error object with the same information, but with the object's key added to it. The error's key path is kept in a user info key, `MAErrorReportingContainersKeyPathUserInfoKey`, and each successive object up the chain adds its own key to the path. The result is that the top-level object stores an error that contains complete key-path information for the object that caused the error.

**Examples**  
The way this works for the caller is best understood with an example. Here's an example deserialization method from the previous article:

```
    + (instancetype)pilotWithPropertyListRepresentation: (id)plist error: (NSError **)outError
    {
        Pilot *pilot = [[self alloc] init];

        id name = plist[@"name"];
        CHECK_NIL(name, @"name", outError);
        CHECK_TYPE(name, NSString, @"name", outError);
        [pilot setName: name];

        id airplanePlists = plist[@"airplanes"];
        CHECK_NIL(airplanePlists, @"airplanes", outError);
        CHECK_TYPE(airplanePlists, NSArray, @"airplanes", outError);

        NSMutableArray *airplanes = [NSMutableArray array];
        for(id plist in airplanePlists)
        {
            Airplane *airplane = [Airplane airplaneWithPropertyListRepresentation: plist error: outError];
            if(!airplane)
                return nil;
            [airplanes addObject: airplane];
        }

        [pilot setAirplanes: airplanes];

        return pilot;
    }
```

With this library, it becomes substantially simpler:

```
    + (instancetype)pilotWithPropertyListRepresentation: (id)plist
    {
        Pilot *pilot = [[self alloc] init];

        NSDictionary *dict = [NSDictionary ma_castRequiredObject: plist];

        [pilot setName: [NSString ma_castRequiredObject: dict[@"name"]];
        NSArray *airplanePlists = [NSArray ma_castRequiredObject: dict[@"airplanes"]];
        [pilot setAirplanes: MAP(airplanePlists, [Airplane airplaneWithPropertyListRepresentation: obj])];

        return pilot;
    }
```

The top-level code that deals with the property list then just needs to wrap it:

```
    id plist = [NSPropertyListSerialization propertyListWithData: plistData options: nil format: NULL error: &error];
    id wrapped = [MAErrorReportingObject wrapObject: plist];
    _airplane = [Airplane airplaneWithPropertyListRepresentation: wrapped];
    if([[wrapped errors] count] > 0)
    {
        // handle the errors
    }
```

**Caveats**  
This library isn't perfect, although I think it's _useful_. There are some things about it that are less than ideal, though:

1. tolerant even for required keys, since the

  methods return

  on error. For individual properties or instance variables, this is trivial, but it can cause some pain with collections.
2. methods. However, only types that are explicitly wrapped get transparent proxies, and values of types that aren't wrapped end up with a generic wrapper that must be passed through a

  method.
3. gets wrapped in a wrapper object, so naive code that expects to get

  directly out of a dictionary when the key is not present will be surprised.

Despite these problems, I think this library will make it much easier to write code that safely decodes property lists and JSON objects. Items 2 and 3 don't apply if you write the entire stack of code to use the `cast` methods, and item 1 is a fairly small price to pay compared to the type-checking code you'd need without this library.

**Conclusion**  
I apologize for not going into greater detail about how the library works, but I spent all of my time writing the code and not enough time writing the article. Fortunately, the basic concepts are simple: wrap each object in another object that tracks errors and knows about the parent object, and when setting an error on such an object, it also sets the error on its parent. Then write `cast` methods that set errors on cast failures, and errors from type checking percolate up to the top.

That's it for today. Come back next time for a discussion of the new 64-bit ARM processor in the iPhone 5S and what it _really_ means for us as users and developers. Friday Q&A is driven by reader suggestions, and while the topic for the next article is already decided, there will be plenty more to follow, so please [send in your topic suggestions](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
