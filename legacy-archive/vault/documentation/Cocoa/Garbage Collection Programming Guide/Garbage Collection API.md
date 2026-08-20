---
title: Garbage Collection Programming Guide
apple_id: TP40002431
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/GarbageCollection/Articles/gcAPI.html
archived_at: '2026-07-15T07:15:55.487109Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Garbage Collection Programming Guide](Introduction%20to%20Garbage%20Collection.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Core%20Foundation%20with%20Garbage%20Collection.md)

# Garbage Collection API

This article summarizes the classes, methods, and functions associated with garbage collection.

Foundation provides several classes to help support design patterns associated with garbage collection, and the behavior of several methods in existing classes is changed when running under garbage collection.

`NSObject` adds the [finalize](https://developer.apple.com/documentation/objectivec/nsobject/1418513-finalize) method; other methods listed below are ignored completely or have changed semantics when used in a garbage collected environment.

__+allocWithZone:(NSZone \*)zone__: The _zone_ argument is ignored.

__- (id)autorelease__: This method is a no-op.

__-(void)dealloc__: This method is a no-op.

__-(void)finalize__: Conceptually similar to the traditional `dealloc`—for more details, see [Implementing a finalize Method](Implementing%20a%20finalize%20Method.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjtfvjvomi).

__- (oneway void)release__: This method is a no-op.

__- (id)retain__: This method is a no-op.

__- (NSUInteger)retainCount__: The return value is undefined.

`NSAutoreleasePool` adds the [drain](https://developer.apple.com/documentation/foundation/nsautoreleasepool/1520553-drain) method.

__-(void)drain__: Triggers garbage collection if memory allocated since last collection is greater than the current threshold. (This method ultimately calls `objc_collect_if_needed()`.)

[NSGarbageCollector](https://developer.apple.com/documentation/foundation/nsgarbagecollector) provides an object-oriented abstraction of the garbage collector. You use [defaultCollector](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431012-defaultcollector) to return the collector (this returns `nil` in a reference-counted environment).

You can use [disableCollectorForPointer:](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431013-disablecollectorforpointer) to ensure that memory at a given address will not be scanned—for example, to create new root objects. You balance this with [enableCollectorForPointer:](https://developer.apple.com/documentation/foundation/nsgarbagecollector/1431017-enablecollectorforpointer), which makes collectable memory that was previously marked as uncollectible.

[NSHashTable](https://developer.apple.com/documentation/foundation/nshashtable) is a collection class like [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) but which (amongst other features) provides the ability to create weak references to its contents.

[NSMapTable](https://developer.apple.com/documentation/foundation/nsmaptable) is a collection class like [NSMutableDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSMutableDictionary) but which (amongst other features) provides the ability to create weak references to its contents.

[NSPointerArray](https://developer.apple.com/documentation/foundation/nspointerarray) is a collection class like [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) but it can also hold `NULL` values, which can be inserted or extracted (and contribute to the object’s count). Also unlike traditional arrays, you can set the count of the array directly. Under Garbage Collection and using a zeroing weak memory configuration, `NULL` values appear when elements are collected. A pointer array uses an instance of [NSPointerFunctions](https://developer.apple.com/documentation/foundation/nspointerfunctions) to define callout functions appropriate for managing a pointer reference held somewhere else.

`NSValue` has a method to wrap a non-retained object, [valueWithNonretainedObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/clm/NSValue/valueWithNonretainedObject:).

__+(id)valueWithNonRetainedObject:(id)anObject__: Creates a new `NSValue` object containing a weak reference to `anObject`. If `anObject` is garbage collected, the reference is set to `nil`.

`NSThread` provides additional functionality for `currentThread`.

|  |  |
| --- | --- |
| [currentThread](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/clm/NSThread/currentThread) |  |

Various functions have been added.

__void \*NSAllocateCollectable(NSUInteger size, NSUInteger options)__: Allocates _size_ bytes of memory using the given option.

__id NSAllocateObject(Class aClass, NSUInteger extraBytes, NSZone \*zone);__: The zone parameter is ignored by `NSAllocateObject` in GC mode.

__id NSMakeCollectable(CFTypeRef cf)__: This function is a wrapper for [CFMakeCollectable](https://developer.apple.com/documentation/corefoundation/1521163-cfmakecollectable) (see [Core Foundation Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinrxfvjvomq)), but its return type is `id`, avoiding the need to cast if you assign the value to a Cocoa object.

This function may be useful when returning Core Foundation objects in code that must support both garbage-collected and non-garbage-collected environments, as illustrated in the following example.

```objc
- (NSString *)description
{
    CFStringRef myCFString = CFStringCreate...(...);
    return [NSMakeCollectable(myCFString) autorelease];
}
```


The behavior of several functions is different under garbage collection. The Core Foundation collection types (such as CFSet, CFMutableSet, CFDictionary, and CFArray) correctly support the standard “retaining” callbacks under GC in a way that allows cycles to be recovered, unlike non-GC behavior. Note also that `NULL` callbacks will weakly reference objects, but are not done with zeroing memory—you still need to remove objects from the collection. If you need zeroing weak object behavior, use [NSHashTable](https://developer.apple.com/documentation/foundation/nshashtable) or [NSMapTable](https://developer.apple.com/documentation/foundation/nsmaptable) instead.

Changed semantics when creating with `NULL` arguments.

__CFArrayCreateMutable(NULL, 0, NULL)__: References contents weakly, does _not_ zero. You must remove objects from the array.

Changed semantics when creating with `NULL` arguments.

__CFDictionaryCreateMutable(NULL, 0, NULL, NULL)__: References contents weakly, does _not_ zero. You must remove objects from the dictionary.

New and changed functions.

__CFTypeRef CFMakeCollectable(CFTypeRef anObject)__: Checks that anObject is a Core Foundation object allocated in the scanned memory zone and, in a garbage collected environment, releases it. This function is a no-op in a reference-counted environment.

__void CFRelease(CFTypeRef anObject)__: Decrements the retain count for `anObject`. If `anObject` was allocated in a garbage collected zone, then if its retain count is reduced to zero it is not actually deallocated until next collection. If `anObject` was allocated in a malloc zone, then if its retain count is reduced to zero it is deallocated immediately. Thus for GC objects, `CFRelease()` no longer has immediate side-effects.

Features and functions.

__`__strong`__: Specifies a reference that is visible to (followed by) the garbage collector (see [How the Garbage Collector Works](Garbage%20Collection%20for%20Cocoa%20Essentials.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjsfvjvomy)).

`__strong` modifies an instance variable or struct field declaration to inform the compiler to unconditionally issue a write-barrier to write to memory. `__strong` is implicitly part of any declaration of an Objective-C object reference type. You must use it explicitly if you need to use Core Foundation types, `void *`, or other non-object references (`__strong` modifies _pointer_ assignments, not scalar assignments).

`__strong` essentially modifies all levels of indirection of a pointer to use write-barriers, except when the final indirection produces a non-pointer l-value. When you declare a variable, you can put `__strong` on either side of the `*`; in the following example, all the variable declarations are equivalent:

```objc
@interface MyClass {
    __strong int *ptr1;
    int * __strong ptr2;
    int __strong * ptr3;
}
```

__`__weak`__: Specifies a reference that is _not_ visible to (followed by) the garbage collector (see [How the Garbage Collector Works](Garbage%20Collection%20for%20Cocoa%20Essentials.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjsfvjvomy)).

`__weak` informs the compiler to use a zeroing weak reference for a variable. All writes are done using a weak write-barrier, and all reads use a weak read-barrier. This allows you to reference a variable without preventing the variable from being garbage collected.

Weak references are set to zero (`nil`) if the destination is collected. If an object is collected, any weak instance variables are cleared _before_ being finalized. Thus, in a [finalize](https://developer.apple.com/documentation/objectivec/nsobject/1418513-finalize) method, you can guarantee that any `__weak` instance variables have been set to `nil`.

The runtime provides a number of functions to support different aspects of garbage collection, and an environment variable you can use to check whether GC is on or off for a process.

__`objc_allocate_object(cls, extra)`__: Allocates a new object.

__`id objc_msgSend(id theReceiver, SEL theSelector, ...)`__: Ignores these selectors: `retain`, `release`, `autorelease`, `retainCount`, `dealloc`. This is faster than messaging `nil`.

__`void objc_collect_if_needed(int options)`__: Triggers garbage collection if memory allocated since last collection is greater than the current threshold. Pass `OBJC_GENERATIONAL` to run generational collection.

This function must only be called from the main thread.

__`void objc_clear_stack(unsigned long options)`__: This function may be useful if you write your own event loop type mechanisms or code not using run loops—you need to clear the stack or risk unnecessarily extending the lifetime of objects.

Any uninitialized local variables will hold whatever values happen to be on the stack from previous function calls. Those values may be pointers to old objects which, while you don't consider the objects to still be live, the garbage collector will still see a reference to them on the stack and not collect them because of it. For example, if a function has a local variable which is a `char` array of `MAX_PATH` length, and you read a line and fill it with only a dozen characters, everything past the end of the dozen characters is left over from previous function calls and may be interpreted by the collector as pointers to objects.

__OBJC_PRINT_GC__: When debugging, you can perform a runtime check by setting the environment variable `OBJC_PRINT_GC=YES`. This prints the GC state of each Objective-C image, and whether GC is on or off for the process.

[Next](Document%20Revision%20History.md)[Previous](Using%20Core%20Foundation%20with%20Garbage%20Collection.md)

