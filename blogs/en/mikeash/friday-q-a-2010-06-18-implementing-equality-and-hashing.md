---
title: 'Friday Q&A 2010-06-18: Implementing Equality and Hashing'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d146eb094026bbce'
translated: false
---

> 原文：[Friday Q&A 2010-06-18: Implementing Equality and Hashing](https://www.mikeash.com/pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html)　·　mikeash.com Friday Q&A

Posted at 2010-06-18 14:48 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Blocks and GCD in Russian](https://www.mikeash.com/pyblog/blocks-and-gcd-in-russian.html)  
Previous article: [Friday Q&A 2010-05-28: Leopard Collection Classes](https://www.mikeash.com/pyblog/friday-qa-2010-05-28-leopard-collection-classes.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hash](https://www.mikeash.com/pyblog/?tag=hash) [isequal](https://www.mikeash.com/pyblog/?tag=isequal) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-06-18: Implementing Equality and Hashing

by [Mike Ash](https://www.mikeash.com/)

**Equality**  
 Object equality is a fundamental concept that gets used all over the place. In Cocoa, it's implemented with the `isEqual:` method. Something as simple as `[array indexOfObject:]` will use it, so it's important that your objects support it.

It's so important that Cocoa actually gives us a default implementation of it on `NSObject`. The default implementation just compares pointers. In other words, an object is only equal to itself, and is never equal to another object. The implementation is functionally identical to:

```
    - (BOOL)isEqual: (id)other
    {
        return self == other;
    }
```

While oversimplified in many cases, this is actually good enough for a lot of objects. For example, an `NSView` is never considered equal to another `NSView`, only to itself. For `NSView`, and many other classes which behave that way, the default implementation is enough. That's good news, because it means that if your class has that same equality semantic, you don't have to do anything, and get the correct behavior for free.

**Implementing Custom Equality**  
 Sometimes you need a deeper implementation of equality. It's common for objects, typically what you might refer to as a "value object", to be distinct from another object but be logically equal to it. For example:

```
    // use mutable strings because that guarantees distinct objects
    NSMutableString *s1 = [NSMutableString stringWithString: @"Hello, world"];
    NSMutableString *s2 = [NSMutableString stringWithFormat: @"%@, %@", @"Hello", @"world"];
    BOOL equal = [s1 isEqual: s2]; // gives you YES!
```

Of course `NSMutableString` implements this for you in this case. But what if you have a custom object that you want to be able to do the same thing?

```
    MyClass *c1 = ...;
    MyClass *c2 = ...;
    BOOL equal = [c1 isEqual: c2];
```

In this case you need to implement your own version of `isEqual:`.

Testing for equality is fairly straightforward most of the time. Gather up the relevant properties of your class, and test them all for equality. If any of them are not equal, then return `NO`. Otherwise, return `YES`.

One subtle point with this is that the class of your object is an important property to test as well. It's perfectly valid to test a `MyClass` for equality with an `NSString`, but that comparison should never return `YES` (unless `MyClass` is a subclass of `NSString`, of course).

A somewhat less subtle point is to ensure that you only test properties that are actually important to equality. Things like caches that do not influence your object's externally-visible value should not be tested.

Let's say your class looks like this:

```
    @interface MyClass : NSObject
    {
        int _length;
        char *_data;
        NSString *_name;
        NSMutableDictionary *_cache;
    }
```

Your equality implementation would then look like this:

```
    - (BOOL)isEqual: (id)other
    {
        return ([other isKindOfClass: [MyClass class]] &&
                [other length] == _length &&
                memcmp([other data], _data, _length) == 0 &&
                [[other name] isEqual: _name])
                // note: no comparison of _cache
    }
```

**Hashing**  
 Hash tables are a commonly used data structure which are used to implement, among other things, `NSDictionary` and `NSSet`. They allow fast lookups of objects no matter how many objects you put in the container.

If you're familiar with how hash tables work, you may want to skip the next paragraph or two.

A hash table is basically a big array with special indexing. Objects are placed into an array with an index that corresponds to their hash. The hash is essentially a pseudorandom number generated from the object's properties. The idea is to make the index random enough to make it unlikely for two objects to have the same hash, but have it be fully reproducible. When an object is inserted, the hash is used to determine where it goes. When an object is looked up, its hash is used to determine where to look.

In more formal terms, the hash of an object is defined such that two objects have an identical hash if they are equal. Note that the reverse is not true, and can't be: two objects can have an identical hash and not be equal. You want to try to avoid this as much as possible, because when two unequal objects have the same hash (called a _collision_) then the hash table has to take special measures to handle this, which is slow. However, it's provably impossible to avoid it completely.

In Cocoa, hashing is implemented with the `hash` method, which has this signature:

```
    - (NSUInteger)hash;
```

As with equality, `NSObject` gives you a default implementation that just uses your object's identity. Roughly speaking, it does this:

```
    - (NSUInteger)hash
    {
        return (NSUInteger)self;
    }
```

The actual value may differ, but the essential point is that it's based on the actual pointer value of `self`. And just as with equality, if object identity equality is all you need, then the default implementation will do fine for you.

**Implementing Custom Hashing**  
 Because of the semantics of `hash`, if you override `isEqual:` then you _must_ override `hash`. If you don't, then you risk having two objects which are equal but which don't have the same hash. If you use these objects in a dictionary, set, or something else which uses a hash table, then hilarity will ensue.

Because the definition of the object's hash follows equality so closely, the implementation of `hash` likewise closely follows the implementation of `isEqual:`.

An exception to this is that there's no need to include your object's class in the definition of `hash`. That's basically a safeguard in `isEqual:` to ensure the rest of the check makes sense when used with a different object. Your hash is likely to be very different from the hash of a different class simply by virtue of hashing different properties and using different math to combine them.

**Generating Property Hashes**  
 Testing properties for equality is usually straightforward, but hashing them isn't always. How you hash a property depends on what kind of object it is.

For a numeric property, the hash can simply be the numeric value.

For an object property, you can send the object the `hash` method, and use what it returns.

For data-like properties, you'll want to use some sort of hash algorithm to generate the hash. You can use CRC32, or even something totally overkill like MD5. Another approach, somewhat less speedy but easy to use, is to wrap the data in an `NSData` and ask it for its hash, essentially offloading the work onto Cocoa. In the above example, you could compute the hash of `_data` like so:

```
    [[NSData dataWithBytes: _data length: _length] hash]
```

**Combining Property Hashes**  
 So you know how to generate a hash for each property, but how do you put them together?

The easiest way is to simply add them together, or use the bitwise xor property. However, this can hurt your hash's uniqueness, because these operations are symmetric, meaning that the separation between different properties gets lost. As an example, consider an object which contains a first and last name, with the following hash implementation:

```
    - (NSUInteger)hash
    {
        return [_firstName hash] ^ [_lastName hash];
    }
```

Now imagine you have two objects, one for "George Frederick" and one for "Frederick George". They will hash to the same value even though they're clearly not equal. And, although hash collisions can't be avoided completely, we should try to make them harder to obtain than this!

How to best combine hashes is a complicated subject without any single answer. However, any asymmetric way of combining the values is a good start. I like to use a bitwise rotation in addition to the xor to combine them:

```
    #define NSUINT_BIT (CHAR_BIT * sizeof(NSUInteger))
    #define NSUINTROTATE(val, howmuch) ((((NSUInteger)val) << howmuch) | (((NSUInteger)val) >> (NSUINT_BIT - howmuch)))
    
    - (NSUInteger)hash
    {
        return NSUINTROTATE([_firstName hash], NSUINT_BIT / 2) ^ [_lastName hash];
    }
```

**Custom Hash Example**  
 Now we can take all of the above and use it to produce a hash method for the example class. It follows the basic form of the equality method, and uses the above techniques to obtain and combine the hashes of the individual properties:

```
    - (NSUInteger)hash
    {
        NSUInteger dataHash = [[NSData dataWithBytes: _data length: _length] hash];
        return NSUINTROTATE(dataHash, NSUINT_BIT / 2) ^ [_name hash];
    }
```

If you have more properties, you can add more rotation and more xor operators, and it'll work out just the same. You'll want to adjust the amount of rotation for each property to make each one different.

**A Note on Subclassing**  
 You have to be careful when subclassing a class which implements custom equality and hashing. In particular, your subclass should not expose any new properties which equality is dependent upon. If it does, then it must not compare equal with any instances of the superclass.

To see why, consider a subclass of the first/last name class which includes a birthday, and includes that as part of its equality computation. It can't include it when comparing equality with an instance of the superclass, though, so its equality method would look like this:

```
    - (BOOL)isEqual: (id)other
    {
        // if the superclass doesn't like it then we're not equal
        if(![super isEqual: other])
            return NO;
        
        // if it's not an instance of the subclass, then trust the superclass
        // it's equal there, so we consider it equal here
        if(![other isKindOfClass: [MySubClass class]])
            return YES;
        
        // it's an instance of the subclass, the superclass properties are equal
        // so check the added subclass property
        return [[other birthday] isEqual: _birthday];
    }
```

Now you have an instance of the superclass for "John Smith", which I'll call `A`, and an instance of the subclass for "John Smith" with a birthday of 5/31/1982, which I'll call `B`. Because of the definition of equality above, `A` equals `B`, and `B` also equals itself, which is expected.

Now consider an instance of the subclass for "John Smith" with a birthday of 6/7/1994, which I'll call `C`. `C` is not equal to `B`, which is what we expect. `C` is equal to `A`, also expected. But now there's a problem. `A` equals both `B` and `C`, but `B` and `C` do not equal each other! This breaks the standard transitivity of the equality operator, and leads to extremely unexpected results.

In general this should not be a big problem. If your subclass adds properties which influence object equality, that's probably an indication of a design problem in your hierarchy anyway. Rather than working around it with weird implementations of `isEqual:`, consider redesigning your class hierarchy.

**A Note on Dictionaries**  
 If you want to use your object as a key in an `NSDictionary`, you need to implement hashing and equality, but you also need to implement `-copyWithZone:`. Techniques for doing that are beyond the scope of today's post, but you should be aware that you need to go a little bit further in that case.

**Conclusion**  
 Cocoa provides default implementations of equality and hashing which work for many objects, but if you want your objects to be considered equal even when they're distinct objects in memory, you have to do a bit of extra work. Fortunately, it's not difficult to do, and once you implement them, your class will work seamlessly with many Cocoa collection classes.

That's it for this week. Check back in two more weeks for another edition. Until then, keep sending me your requests for topics. Friday Q&A is driven by user submissions, so if you have an idea for a topic to cover here, please [send it in](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
