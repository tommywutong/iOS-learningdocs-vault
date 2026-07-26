---
title: promised last time
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-08-30-model-serialization-with-property-lists.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e98be43c92147fb7'
translated: false
---

> 原文：[promised last time](https://www.mikeash.com/pyblog/friday-qa-2013-08-30-model-serialization-with-property-lists.html)　·　mikeash.com Friday Q&A

Posted at 2013-08-30 13:35 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-09-13: A Library for Easier Property List Type Checking and Error Reporting](https://www.mikeash.com/pyblog/friday-qa-2013-09-13-a-library-for-easier-property-list-type-checking-and-error-reporting.html)  
Previous article: [Friday Q&A 2013-08-16: Let's Build Dispatch Groups](https://www.mikeash.com/pyblog/friday-qa-2013-08-16-lets-build-dispatch-groups.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [plist](https://www.mikeash.com/pyblog/?tag=plist) [serialization](https://www.mikeash.com/pyblog/?tag=serialization)

Friday Q&A 2013-08-30: Model Serialization With Property Lists

by [Mike Ash](https://www.mikeash.com/)

**Techniques**  
Serialization is the process of translating objects in memory to and from a stream of bytes. It's most commonly used for saving data to disk, and it's also useful for sending data over a network connection.

There are many ways to serialize data. Among the common ways on Apple platforms are:

1. Core Data
2. SQLite
3. `NSCoding`
4. Custom binary formats
5. Property lists

Of these, Core Data is probably the most popular, or at least the most hyped. Personally, I'm not a big fan. I find the API to be unwieldy and the framework itself to be painfully slow for anything more than a small amount of data.

SQLite is what Core Data usually works with, but it can also be used directly. This gives you a full SQL database with a local API and decent performance, but it's more work than other approaches, and is often unnecessary for small amounts of data.

`NSCoding` can be a nice middle ground, but it ties the serialized representation too closely to the in-memory representation for my tastes.

Custom binary formats can be great, but are usually a ton of work. You should avoid these when you can, but if you need them, there's no substitute.

Property lists provide a simple way to save small to moderate amounts of data easily and quickly. They're my technique of choice whenever I'm not storing enormous amounts of data.

**Property List Review**  
I assume that everyone reading this blog knows what property lists are and how they work, but just in case I'm wrong, here's a quick review.

Conceptually, a property list is a collection of objects of certain types:

1. Strings.
2. Numbers.
3. Raw data.
4. Dates.
5. Booleans.
6. Arrays.
7. Dictionaries with string keys.

It's similar to JSON, except that it has some types that JSON does not (dates and raw data), and property lists can't store `null`.

A property list can exist as objects in memory or as serialized data. As objects in memory, these types are represented by the Objective-C classes `NSString`, `NSNumber`, `NSData`, `NSDate`, `NSArray`, and `NSDictionary`. On disk, property lists can be stored as XML or in a compact, efficient binary format.

**Basic Property List Serialization**  
Let's take the following class as an example of something we want to serialize:

```
    @interface Airplane : NSObject

    @property (copy) NSString *model;
    @property (copy) NSString *registrationNumber
    @property unsigned long long airframeHours;

    @end
```

We'll add a pair of methods to this interface, one to serialize it to a property list, and one to deserialize it:

```
    - (id)propertyListRepresentation;
    + (instancetype)airplaneWithPropertyListRepresentation: (id)plist;
```

These will simply place the above fields into an `NSDictionary` and fetch them back out again:

```
    - (id)propertyListRepresentation
    {
        NSMutableDictionary *dict = [NSMutableDictionary dictionary];
        dict[@"model"] = _model;
        dict[@"registrationNumber"] = _registrationNumber;
        dict[@"airframeHours"] = @(_airframeHours);
        return dict;
    }

    + (instancetype)airplaneWithPropertyListRepresentation: (id)plist
    {
        Airplane *airplane = [[self alloc] init];
        [airplane setModel: plist[@"model"]];
        [airplane setRegistrationNumber: plist[@"registrationNumber"]];
        [airplane setAirframeHours: [plist[@"airframeHours"] unsignedLongLongValue]];
        return airplane;
    }
```

The code that owns the `Airplane` can then use these methods in conjunction with `NSPropertyListSerialization` to serialize the object:

```
    - (void)saveToURL: (NSURL *)url
    {
        id plist = [_airplane propertyListRepresentation];
        NSError *error;
        NSData *plistData = [NSPropertyListSerialization dataWithPropertyList: plist format: NSPropertyListBinaryFormat_v1_0 options: 0 error: &error];
        if(!plistData)
            NSLog(@"Unable to generate plist from Airplane: %@", error);
        BOOL success = [plistData writeToURL: url options: NSDataWritingAtomic error: &error];
        if(!success)
            NSLog(@"Unable to write plist data to disk: %@", error);
    }

    - (void)readFromURL: (NSURL *)url
    {
        NSError *error;
        NSData *plistData = [NSData dataWithContentsOfURL: url options: 0 error: &error];
        if(!plistData)
        {
            NSLog(@"Unable to read plist data from disk: %@", error);
            return;
        }
        id plist = [NSPropertyListSerialization propertyListWithData: plistData options: nil format: NULL error: &error];
        if(!plist)
        {
            NSLog(@"Unable to decode plist from data: %@", error);
            return;
        }
        _airplane = [Airplane airplaneWithPropertyListRepresentation: plist];
    }
```

**Collections**  
Let's add another model class and another layer to the serialization with this interface:

```
    @interface Pilot : NSObject

    @property (copy) NSString *name;
    @property (copy) NSArray *airplanes;

    @end
```

I'll make use of the helper macros from [MACollectionUtilities](https://github.com/mikeash/MACollectionUtilities), so beware, and check out that link if the code is confusing.

The serialization methods for this class will recursively call the ones on `Airplane` and build an array from the `Airplane` representations:

```
    - (id)propertyListRepresentation
    {
        NSMutableDictionary *dict = [NSMutableDictionary dictionary];
        dict[@"name"] = _name;
        dict[@"airplanes"] = MAP(_airplanes, [obj propertyListRepresentation]);
        return dict;
    }

    + (instancetype)pilotWithPropertyListRepresentation: (id)plist
    {
        Pilot *pilot = [[self alloc] init];
        [pilot setName: plist[@"name"]];
        [pilot setAirplanes: MAP(plist[@"airplanes"], [Airplane airplaneWithPropertyListRepresentation: obj])];
        return pilot;
    }
```

This technique can be extended to whatever depth you need, with property list representations containing other property list representations containing still others.

**Subclasses**  
We may have multiple subclasses of these model classes, at which point the property list serialization code has to get a bit smarter. Let's give `Airplane` some subclasses:

```
    @interface PoweredAirplane : Airplane

    @property int engineHorsepower;
    @property unsigned long long engineHours;

    @end

    @interface Glider : Airplane

    @property unsigned long long aerotowLaunchCount;
    @property unsigned long long winchLaunchCount;

    @end
```

The code for `-propertyListRepresentation` is easy: call `super`, then add more entries to the dictionary.

```
    // PoweredAirplane
    - (id)propertyListRepresentation
    {
        // We know that super returns a mutable dictionary
        // so stuff more entries into that.
        NSMutableDictionary *dict = [super propertyListRepresentation];
        dict[@"engineHorsepower"] = @(_engineHorsepower);
        dict[@"engineHours"] = @(_engineHours);
        return dict;
    }

    // Glider
    - (id)propertyListRepresentation
    {
        // We know that super returns a mutable dictionary
        // so stuff more entries into that.
        NSMutableDictionary *dict = [super propertyListRepresentation];
        dict[@"aerotowLaunchCount"] = @(_aerotowLaunchCount);
        dict[@"winchLaunchCount"] = @(_winchLaunchCount);
        return dict;
    }
```

However, `+airplaneWithPropertyListRepresentation:` needs support in the `Airplane` class. Simply implementing it in the subclasses like `-propertyListRepresentation` above won't do the job:

```
    // PoweredAirplane
    + (instancetype)airplaneWithPropertyListRepresentation: (id)plist
    {
        PoweredAirplane *airplane = [super airplaneWithPropertyListRepresentation: plist];
        [airplane setEngineHorsepower: [plist[@"engineHorsepower"] intValue];
        [airplane setEngineHours: [plist[@"engineHours"] unsignedLongLongValue];
        return airplane;
    }

    // Glider
    + (instancetype)airplaneWithPropertyListRepresentation: (id)plist
    {
        Glider *glider = [super airplaneWithPropertyListRepresentation: plist];
        [glider setAerotowLaunchCount: [plist[@"aerotowLaunchCount"] unsignedLongLongValue]];
        [glider setWinchLaunchCount: [plist[@"winchLaunchCount"] unsignedLongLongValue]];
        return glider;
    }
```

What's the problem? Let's look at the implementation of `Pilot` again, specifically this line:

```
    [pilot setAirplanes: MAP(plist[@"airplanes"], [Airplane airplaneWithPropertyListRepresentation: obj])];
```

The way `Airplane` implements `+airplaneWithPropertyListRepresentation:`, it has no idea about subclasses. By directly messaging `Airplane`, this code generates instances of `Airplane`, and not its subclasses. Because of this, information is lost when moving through serialization.

To fix this `Airplane` needs to be made aware of subclasses. We can use introspection to avoid having to hardcode knowledge of all subclasses in the code.

First, the implementation of `propertyListRepresentation` needs to save the class name into the property list along with the other data. We'll add a line to do that:

```
    - (id)propertyListRepresentation
    {
        NSMutableDictionary *dict = [NSMutableDictionary dictionary];
        dict[@"class"] = NSStringFromClass([self class]);
        dict[@"model"] = _model;
        dict[@"registrationNumber"] = _registrationNumber;
        dict[@"airframeHours"] = @(_airframeHours);
        return dict;
    }
```

Second, the implementation of `airplaneWithPropertyListRepresentation:` needs to retrieve the class and use it to instantiate the new object instead of simply calling `[self alloc]`:

```
    + (instancetype)airplaneWithPropertyListRepresentation: (id)plist
    {
        Class class = NSClassFromString(dict[@"class"]);
        Airplane *airplane = [[class alloc] init];
        [airplane setModel: plist[@"model"]];
        [airplane setRegistrationNumber: plist[@"registrationNumber"]];
        [airplane setAirframeHours: [plist[@"airframeHours"] unsignedLongLongValue]];
        return airplane;
    }
```

With these modifications in place, the subclass implementations of `+airplaneWithPropertyListRepresentation:` work as desired.

**`nil` Safety**  
It's common to have fields that can be `nil`, and you have to ensure that the code can deal with that. For example, if `name` can be nil, then blindly stuffing it into a dictionary won't work:

```
    dict[@"name"] = _name;
```

`NSMutableDictionary` refuses `nil` values, and will throw an exception if you attempt to add one.

In general, we can represent `nil` values through the simple absence of a key, so a quick `if` statement suffices to fix the problem:

```
    if(_name)
        dict[@"name"] = _name;
```

However, repeating `if` statements endlessly can get tedious. It's also easy to forget one. Another way to deal with the problem is to create an `NSMutableDictionary` subclass that does the check for us:

```
    @interface MANilToleratingDictionary : NSMutableDictionary
    @end

    @implementation MANilToleratingDictionary {
        NSMutableDictionary *_innerDictionary;
    }

    - (id)init
    {
        if((self = [super init]))
        {
            _innerDictionary = [NSMutableDictionary dictionary];
        }
    }

    - (NSUInteger)count
    {
        return [_innerDictionary count];
    }

    - (id)objectForKey: (id)key
    {
        return [_innerDictionary objectForKey: key];
    }

    - (NSEnumerator *)keyEnumerator
    {
        return [_innerDictionary keyEnumerator];
    }

    - (void)setObject: (id)obj forKey: (id <NSCopying>)key
    {
        // Don't pass nil objects into the underlying dictionary.
        if(obj)
            [_innerDictionary setObject: obj forKey: key];
    }

    - (void)removeObjectForKey: (id)key
    {
        [_innerDictionary removeObjectForKey: key];
    }

    @end
```

Now, this class can be used in place of a plain `NSMutableDictionary`, and attempts to set `nil` values will be ignored:

```
    - (id)propertyListRepresentation
    {
        NSMutableDictionary *dict = [[MANilToleratingDictionary alloc] init];
        dict[@"name"] = _name;
        dict[@"airplanes"] = MAP(_airplanes, [obj propertyListRepresentation]);
        return dict;
    }
```

If `_name` is `nil` here, the key will simply by absent from the dictionary.

**Error Checking**  
Because property lists are dynamically typed, you run the risk of getting an object of an unexpected type. You may expect an `NSString`, but the property list could contain an `NSNumber` for that key instead.

Cocoa and Objective-C implicitly perform a certain amount of checking for you, by virtue of the fact that sending messages to an object that it doesn't understand will throw an exception. Depending on your situation, this may be enough. For example, if you're saving data into Application Support and can reasonably expect no other app to be messing with the files, you can probably get away with just assuming that the property list contents are correct, and crashing if they're not. Even if you're creating user-accessible documents this way, you may not need to do anything special, depending on how robust you want to be against malformed documents.

For more detailed checking, you'll want to use the `isKindOfClass:` method. At the most basic, you can just bail out and return `nil` if it fails:

```
    id name = dict[@"name"];
    if(![name isKindOfClass: [NSString class]])
        return nil;
    _name = name;
```

Silent failures like this are generally bad, so you probably at least want to log an error:

```
    id name = dict[@"name"];
    if(![name isKindOfClass: [NSString class]])
    {
        NSLog(@"'name' field was not a string, can't load plist data. Actual 'name' value is: %@", dict[@"name"]);
        return nil;
    }
    _name = name;
```

In same cases, you really want to get information back to the user, like if you're loading a document file or made a request to a server and the property list contains bad data. In that case, you'll want to use the standard `NSError` mechanisms. For best results, you can use a custom domain, some custom codes, and a custom user info key. For example:

```
    NSString * const kPlistTypeErrorDomain = @"kPlistTypeErrorDomain";
    enum {
        kPlistBadTypeError,
        kPlistMissingKeyError
    };

    NSString * const kPlistTypeErrorKeyName = @"kPlistTypeErrorKeyName";
```

You could then add a parameter to the API to return an error, and use it to inform the caller of what went wrong:

```
    + (instancetype)pilotWithPropertyListRepresentation: (id)plist error: (NSError **)outError
    {
        Pilot *pilot = [[self alloc] init];

        id name = plist[@"name"];
        if(!name)
        {
            if(outError)
                *outError = [NSError errorWithDomain: kPlistTypeErrorDomain code: kPlistMissingKeyError userInfo: @{ kPlistTypeErrorKeyName : @"name" }];
            return nil;
        }
        if(![name isKindOfClass: [NSString class]])
        {
            if(outError)
                *outError = [NSError errorWithDomain: kPlistTypeErrorDomain code: kPlistBadTypeError userInfo: @{ kPlistTypeErrorKeyName : @"name" }];
            return nil;
        }

        [pilot setName: name];

        id airplanePlists = plist[@"airplanes"];
        if(!airplanePlists)
        {
            if(outError)
                *outError = [NSError errorWithDomain: kPlistTypeErrorDomain code: kPlistMissingKeyError userInfo: @{ kPlistTypeErrorKeyName : @"airplanes" }];
            return nil;
        }
        if(![airplanePlists isKindOfClass: [NSArray class]])
        {
            if(outError)
                *outError = [NSError errorWithDomain: kPlistTypeErrorDomain code: kPlistBadTypeError userInfo: @{ kPlistTypeErrorKeyName : @"airplanes" }];
            return nil;
        }

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

This works, but the amount of boilerplate is intense. We can clean it up with some macros:

```
    #define CHECK_NIL(variable, key, outError) \
        if(!(variable)) { \
            if((outError)) \
                outError = [NSError errorWithDomain: kPlistTypeErrorDomain code: kPlistMissingKeyError userInfo: @{ kPlistTypeErrorKeyName : (key) }]; \
            return nil; \
        }
    #define CHECK_TYPE(variable, type, key, outError) \
        if(![(variable) isKindOfClass: [(type) class]) { \
            if((outError)) \
                outError = [NSError errorWithDomain: kPlistTypeErrorDomain code: kPlistMissingKeyError userInfo: @{ kPlistTypeErrorKeyName : (key) }]; \
            return nil; \
        }
```

The code then becomes considerably nicer:

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

It's still not great, as there's a fair amount of repetition, but it's not too bad.

I'm working on a library that aims to make this even nicer, but this article is too narrow to contain it. Check back for a thorough writeup of it next time around.

**Top-Level Considerations**  
The top level of your property list requires some special consideration, especially if you're building a document format that needs to maintain compatibility across versions of your app. Some care needs to be taken to ensure that new data can be added and compatibility can be signaled.

To start with, make sure that the top level object in the property list is never, ever anything but an `NSDictionary`. If your data is just a big collection of objects, it can be tempting to just write out an `NSArray` containing the property list representations of the objects. _Don't do this!_ It works fine right up until the moment when you decide you want to add something else to the data, at which point you're stuck, because there's no way to add that data to the array without having old versions of the code attempting to interpret it.

If you do nothing else, wrap that array in a simple dictionary:

```
    id plist = @{ @"objects" : array };
```

Then, when you want to add something else, you can just add a second key:

```
    id plist = @{
        @"objects" : array,
        @"moreObjects" : otherArray
    };
```

The old code will simply ignore the additional key, and everything works fine.

This assumes that the additional data isn't essential to understanding the contents of the file, but is some sort of optional add-on. This can be true in many cases, but sometimes you'll want to add things which _must_ be understood, and old code shouldn't even attempt to understand. In that case, you can simply put both arrays under new keys:

```
    id plist = @{
        @"firstObjects" : array,
        @"moreObjects" : otherArray
    };
```

When doing this, you'll want to make sure your reader code checks for `@"objects"` as well so that it can read files written by older code. Users really hate it when they upgrade an app and all of their old data files become unreadable.

This may not be enough, or your property lists may be too complex for this to be feasible. I recommend adding some explicit version numbering to the top level property list.

The best way to handle this is to store both a major version number and a minor version number. Major version numbers indicate breaking changes. Code which was built to understand major version `X` must not attempt to read data with major version `X+1`. Minor version numbers indicate smaller changes which don't break compatibility, but which are still useful to signal. Code built to understand minor version `X` can still read data wiht minor version `X+1`. Later code can take advantage of the minor version number to alter how it reads data, if necessary.

With that, the top level property list would look something like this:

```
    const int kCurrentMajorVersion = 2;
    const int kCurrentMinorVersion = 1;

    const int kOldReleaseMajorVersion = 1;

    id plist = @{
        @"majorVersion" : @(kCurrentMajorVersion),
        @"minorVersion" : @(kCurrentMinorVersion),
        @"objects" : array
    };
```

When reading the property list, you'll want to make sure to check the major version number first thing:

```
    id majorVersion = plist[@"majorVersion"];
    CHECK_NIL(majorVersion, @"majorVersion", outError);
    CHECK_TYPE(majorVersion, NSNumber, @"majorVersion", outError);
    if([majorVersion intValue] == kCurrentMajorVersion)
        // read normally
    else if([majorVersion intValue] == kOldReleaseMajorVersion)
        // handle the old format
    else
        // error: can't read this version
```

If necessary, the minor version can be used to modify behavior slightly. It can usually be ignored, but it's nice to have the field in there just in case.

**XML Versus Binary**  
When generating the actual property list data, `NSPropertyListSerialization` provides two options: XML and binary. Which one should you use?

The advantage of XML is that it can be read, and to an extent edited, with a standard text editor. However, it's also large and slow, and in general I recommend avoiding it.

The binary format can't be read with a text editor, but the data is lean and it's fast to read and write. Xcode will display property lists in a nice graphical editor, so there's no problem inspecting or editing them by hand. The format is even [documented](http://opensource.apple.com/source/CF/CF-550/CFBinaryPList.c), even if just barely, so there's no problem with getting locked in to a proprietary format. If you find yourself with a binary plist that you absolutely must have in XML format, the `plutil` utility can convert it.

**Conclusion**  
There are many options for serialization, and property lists can fill a lot of roles well. It doesn't fit every situation, but if you have a reasonably simple object graph without a huge quantity of data, property lists provide a quick, easy, and straightforward way to serialize and deserialize those objects with a minimum of fuss. It requires writing a bit of code, but it can be well worth it for a simple file format over which you maintain full control.

That's it for today. Come back next time for a discussion of my experimental library for performing type checking and handling errors when deserializing objects from property lists. Until then, Friday Q&A is driven by reader suggestions, so please [send in your ideas for topics](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
