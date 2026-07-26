---
title: 'Speed test: NSManagedObject ObjC-2.0 accessors | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/06/speed-test-nsmanagedobject-objc-20.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:2b6d577fe73b593b'
translated: false
---

> 原文：[Speed test: NSManagedObject ObjC-2.0 accessors | Cocoa with Love](https://www.cocoawithlove.com/2008/06/speed-test-nsmanagedobject-objc-20.html)　·　Cocoa with Love (Matt Gallagher)

A quick, relative-performance test of the 3 ways of accessing NSManagedObject properties in Leopard.

## Mac OS X Snow Leopard? I'm still not up-to-date with 10.5!

If you've been in a coma all week, you might not have noticed that Apple announced the next major update to Mac OS X on Monday, [Snow Leopard](http://www.apple.com/macosx/snowleopard). It's scheduled for "sometime next year" which means that I really should finish updating my code for the current version of Mac OS X.

As part of this, I've been assessing whether or not I should refactor some of my old pre-Leopard code to use the new NSManagedObject accessors introduced in Leopard.

If you don't know what I'm talking about, let me show you this...

```objc
// The old way to set an NSManagedObject string value
[object setValue:value forKey:@"stringValue"];

// The custom accessor way to set an NSManagedObject string value
[object setStringValue:value];

// The new alternate syntax for setting an NSManagedObject string value
object.stringValue = value;
```

In the "old" approach, NSManagedObject had to perform string comparisons to work out which property in the NSManagedObject's entity description corresponded to the provided "key". It also had to work out if custom "getter" and "setter" methods existed and might need to be invoked.

The "custom accessor" approach eliminates the string comparison and method lookups but prior to Leopard, you had to explicitly write these methods yourself — something time consuming enough to discourage use. In Leopard, you only need to declare these methods and you get the implementation for free.

The "new" approach really just uses Leopard's automatically generated custom accessor methods through Objective-C 2.0 properties but only requires "property" declaration (slightly less work again than method declaration).

With "custom accessor" methods requiring extra development work under Tiger, most of my pre-Leopard code uses the old KVC approach. Do I care? Should I update my code?

## Give me the numbers

The real question is: how much difference does it make? I have lots of code which uses the "old" approach. How much improvement will I see with one of the other two approaches?

Time for some test code:

```objc
    for (int i = 0; i < 10000; i++)
    {
        for (NSManagedObject *object in objects)
        {
            #if LEOPARD_OBJC_2_ACCESSORS
                NSString *value = object.stringValue;
                object.stringValue = value;
            #elif CUSTOM_METHOD_ACCESSORS
                NSString *value = [object stringValue];
                [object setStringValue:value];
            #else // Key Value Coding accessors
                NSString *value = [object valueForKey:@"stringValue"];
                [object setValue:value forKey:@"stringValue"];
            #endif
        }
    }
```

My test data is a set of 1000 entities with "stringValue" set to "Entity number %d" (where "%d" is 0001 to 1000). All data is prefaulted. All I'm doing is accessing a string value and setting it back again to the same value 10 million times.

Performance looks like this:

| Access approach | Time taken |
|---|---|
| Objective-C 2.0 Accessors | 16.6701 seconds |
| Custom Method Accessors | 16.7978 seconds |
| Key Value Coding Accessors | 31.6373 seconds |

* results generated on a Dual 2Ghz PPC G5 (Intel-only Snow Leopard makes him cry)

## Conclusion

The automatically generated Leopard accessors take half the time of the Key Value Coding approach — a substantial improvement. There is no practical difference between "Objective-C 2.0 Accessors" and "Custom Method Accessors" so that is merely a matter of stylistic preference and header declarations.

The old Key Value Coding approach still has its uses, particularly for runtime-selected key paths. It is also the only approach which requires no headers or declarations at all (although this can lead to runtime errors). But beyond that, I really should do some refactoring.
