---
title: Garbage Collection Programming Guide
apple_id: TP40002431
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/GarbageCollection/Articles/gcCoreFoundation.html
archived_at: '2026-07-15T07:15:57.995727Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Garbage Collection Programming Guide](Introduction%20to%20Garbage%20Collection.md)


[Next](Garbage%20Collection%20API.md)[Previous](Inapplicable%20Patterns.md)

# Using Core Foundation with Garbage Collection

Sometimes you want to integrate Core Foundation objects into your application. If your application uses garbage collection, you must then ensure that you manage the memory for these objects correctly.

Core Foundation provides C-based opaque types for a number of data-types—including strings and dates and numbers and collections—that have counterparts in Cocoa Objective-C classes (for example, CFString corresponds to `NSString`). There are also Core Foundation opaque objects that don't have a direct Objective-C counterpart, yet also respond to basic Objective-C messages (such as `hash` and `isEqual:`). These opaque data types can be treated by Cocoa as objects—for example, they can be stored in collections. Since these objects are nearly indistinguishable from those created directly in Objective-C, they are also allocated and collected by the garbage collector, although they do require some special handling at time of creation.

The collection system supports multiple memory zones. When you create a Core Foundation object, you specify the zone using the allocator parameter. In a garbage collected environment, the standard default Core Foundation allocator (which normally points to the default malloc zone) is aimed at one that uses the garbage collector system—so by default all Core Foundation objects are allocated by the collector. The following list summarizes the behavior of the allocators in a garbage collected environment:

- `NULL`, `kCFAllocatorDefault`, and `kCFAllocatorSystemDefault` specify allocation from the garbage collection zone.

  By default, all Core Foundation objects are allocated in the garbage collection zone.
- `kCFAllocatorMallocZone` specifies allocation from default `malloc` zone.
- `kCFAllocatorMalloc` specifies allocation explicitly with `malloc()` and deallocation with `free()`.

Because you can use Core Foundation objects in applications that use garbage collection or reference counting, the Core Foundation memory management functions `CFRetain()` and `CFRelease()` are required to interoperate correctly in either environment. As a policy, they function in the same way in both—they respectively increment and decrement the reference counts of Core Foundation objects.

In a garbage collected environment, the `CFRetain` and `CFRelease` implementations are redirected to also use the garbage collectors reference counting mechanism. _The collector does not collect any object with a non-zero count_ (or any object reachable from such an object—Core Foundation objects with a retain count greater than zero act as root objects). Within C based code, therefore, `CFRetain` and `CFRelease` still perform the same logical functions that they always do—it’s just that the memory source and the location of the reference count bits is different.

By default, therefore, in a garbage-collected environment you manage Core Foundation objects exactly as you would in a reference-counted environment (as described in _[Memory Management Programming Guide for Core Foundation](../../Core%20Foundation/Memory%20Management%20Programming%20Guide%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdo2i)_ > [Ownership Policy](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148)). If you create or copy a Core Foundation object, you must subsequently release it when you’re finished with it. If you want to keep hold of a Core Foundation object, you must retain it and again subsequently release it when you’re finished with it.

The difference between the garbage-collected environment and reference-counted environment is in the timing of the object’s deallocation. In a reference counted environment, when the object’s retain count drops to 0 it is deallocated immediately; in a garbage-collected environment, what happens when a Core Foundation object's retain count transitions from 1 to 0 depends on where it resides in memory:

- If the object is in the malloc zone, it is deallocated immediately.
- If the object is in the garbage collected zone, the last `CFRelease()` does not immediately free the object, it simply makes it eligible to be reclaimed by the collector when it is discovered to be unreachable—that is, once all strong references to it are gone. Thus as long as the object is still referenced from an object-type instance variable (that hasn't been marked as`__weak`), a register, the stack, or a global variable, it will not be collected.

This behavioral difference gives you some additional flexibility in a garbage collected environment. In a non-garbage-collected application you call `CFRelease()` only when you want to relinquish ownership; in a garbage-collected application you may call `CFRelease()` immediately after allocation and the object will be collected when appropriate. Better still, though, you can use [CFMakeCollectable](https://developer.apple.com/documentation/corefoundation/1521163-cfmakecollectable) instead of `CFRelease`. `CFMakeCollectable` calls `CFRelease`, but has two supplementary features: first, it halts the program if the object wasn't allocated in the scanned zone; second, it’s a no-op in a reference counted environment. (In addition, it more clearly signals your intent.) For example:

```
CFStringRef myCFString = CFMakeCollectable(CFStringCreate...(...));
```

You can also use [NSMakeCollectable](https://developer.apple.com/documentation/foundation/1539822-nsmakecollectable). This is exactly the same as `CFMakeCollectable` except that it returns an `id`—you can use this to avoid the need for casting, as illustrated in the following example:

```
id myNSString = NSMakeCollectable(CFStringCreate...(...));
```

You could imagine the implementation of CFMakeCollectable as being similar to this:

```
id CFMakeCollectable(CFTypeRef object)
{
    CFAllocatorRef allocator = CFGetAllocator(object);
    if ((allocator != kCFAllocatorDefault) && (allocator != kCFAllocatorSystemDefault)) {
        // Register an error.
    }
    CFRelease([(id)object retain]);
    return object;
}
```

Similarly, you could define a hypothetical `MakeUncollectable()` function as follows:

```
id MakeUncollectable(id object)
{
    [CFRetain(object) release];
    return object;
}
```

This makes a currently collectable object uncollectable by giving it a retain count of 1.

There are three important corollaries here:

1. A single `CFMakeCollectable` (and hence `NSMakeCollectable`) balances a single `CFRetain`. For example, absent any additional memory management code, the following code fragment will result in `myCFString` “leaking”:

```
CFStringRef myCFString = CFMakeCollectable(CFStringCreate...(...));
CFRetain(myCFString);
```

   You must balance the `CFRetain` with a further `CFMakeCollectable`.
2. Because `CFMakeCollectable` is a no-op in a reference counted environment, if you use it with mixed mode code you do need to use `CFRelease` when running without garbage collection.

```
CFStringRef myCFString = CFMakeCollectable(CFStringCreate...(...));
// do interesting things with myCFString...
if ([NSGarbageCollector defaultCollector] == NULL) CFRelease(myCFString);
```
3. It is important to appreciate the asymmetry between Core Foundation and Cocoa—where `retain`, `release`, and `autorelease` are no-ops. If, for example, you have balanced a CFCreate… with `release` or `autorelease`, you will leak the object in a garbage collected environment:

```
NSString *myString = (NSString *)CFStringCreate...(...);
// Do interesting things with myString.
[myString release]; // **** Leaked in a garbage collected environment.
```

   Conversely, using `CFRelease` to release an object you have previously retained using `retain` will result in a reference count underflow error.

The garbage collector can only track a reference if it knows that it should be treated as an object. If you declare a Core Foundation structure as an instance variable, the compiler regards it only as an opaque structure pointer, not as an object. Assignments will not therefore by default generate the write-barriers required by the collector, the compiler needs some explicit information—this is also true for Core Foundation variables declared globally.

To indicate that a Core Foundation structure should be treated as a collectable object, you use the `__strong` keyword. This denotes that scanned memory references are to be stored into a given variable and that write-barriers should be issued.

```objc
@interface MyClass : NSObject {
    __strong CFDateRef myDate;
}
@end

@implementation MyClass

- (id)init
{
    self = [super init];
    if (self) {
        myDate = CFMakeCollectable(CFDateCreate(NULL, 0));
    }
    return self;
}

/*
There is no need for a finalize method here
*/
@end
```

If you want to see when write barriers are generated, you can ask the compiler to emit a warning at every point it issues a write-barrier by using the `Wassign-intercept` flag.

If you allocate a Core Foundation object locally, you can use `CFRetain` and `CFRelease` just as you would in a non-garbage collected application, for example:

```objc
- (void)doSomethingInterestingWithALocalCFDate
{
    CFDateRef epoch = CFDateCreate(NULL, 0);
    // ...
    CFRelease(epoch);
}
```

If you return the value, however, to ensure that the returned value is eligible for collection you must balance the Create with `NSMakeCollectable` (or `CFMakeCollectable`) as illustrated in the following example:

```objc
- (id)anInterestingDate
{
    CFDateRef epoch = CFDateCreate(NULL, 0);
    // ...
    return NSMakeCollectable(epoch);
}
```

If you are writing mixed-mode code (code that has to run in both a garbage-collected and reference-counted environments), you can use `NSMakeCollectable` (or `CFMakeCollectable`) to bring Core Foundation objects into the `NSObject` world as shown in this example (remember that `CFMakeCollectable` is a no-op in a reference-counted environment and `autorelease` is a no-op in a garbage collected environment):

```objc
- (NSString *)languageForString:(NSString *)string
{
    CFStringTokenizerRef tokenizer;
    // create and configure the tokenizer...
    CFStringRef language = CFStringTokenizerCopyCurrentTokenAttribute(tokenizer, kCFStringTokenizerAttributeLanguage);
    CFRelease(tokenizer);
    return [NSMakeCollectable(language) autorelease];
}
```


Collections (such as arrays and dictionaries) allocated in the scanned zone use strong references instead of reference counting (this is important for good garbage collection performance).

```
__strong CFMutableArrayRef myList;
```

Core Foundation collection objects such as dictionaries have different properties than their Objective-C Cocoa counterparts. In particular, they allow for non-retained entries which need not be objects but may be other pointers or even values of pointer size. This allows you, for example, to use integers as keys in a dictionary object. To accomplish this you pass `NULL` callbacks at collection object creation. This has the effect of just copying the pointer sized value into the collection object with no additional processing.

When the values are in fact objects they are stored as non-retained (weak) pointers, and if those objects are somehow reclaimed, what is stored becomes dangling references. Although unsafe, this practice is correctly supported when running under GC. Both the standard retaining as well as the non-retaining, weak (`NULL`) callbacks are supported correctly.

[Next](Garbage%20Collection%20API.md)[Previous](Inapplicable%20Patterns.md)

