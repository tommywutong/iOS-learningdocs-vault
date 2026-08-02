---
title: Garbage Collection Programming Guide
apple_id: TP40002431
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/GarbageCollection/Articles/gcInapplicablePatterns.html
archived_at: '2026-07-15T07:16:00.504174Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Garbage Collection Programming Guide](Introduction%20to%20Garbage%20Collection.md)


[Next](Using%20Core%20Foundation%20with%20Garbage%20Collection.md)[Previous](Implementing%20a%20finalize%20Method.md)

# Inapplicable Patterns

The following sections discuss design patterns that are applicable in Cocoa applications that use reference counting but which do not translate well to a garbage collected environment.

If you use garbage collection, the methods that are used to implement the manual reference counting system (`retain`, `release`, `dealloc`, `autorelease`, and `retainCount`) have no effect—the Objective-C messenger short circuits their dispatch. As a result, overriding `release` and `dealloc` is not supported when garbage collection is enabled—this makes obsolete some object caching patterns.

Note, however, that `CFRetain` and `CFRelease` do still have an effect in Core Foundation objects. See also [Adopting Garbage Collection](Adopting%20Garbage%20Collection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjxfvjvomi).

When you use “classic” memory management, you typically implement a `dealloc` method that performs “clean-up” operations such as releasing instance variables, unregistering the object from a notification center, and closing resources. In a garbage-collected application, the analog of the `dealloc` method is [finalize](https://developer.apple.com/documentation/objectivec/nsobject/1418513-finalize).

In a garbage-collected application, there is obviously no need to release instance variables, however you should ideally ensure that other resources are closed prior to an object’s destruction. For more details, see [Implementing a finalize Method](Implementing%20a%20finalize%20Method.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjtfvjvomi).

Although there are conceptual similarities between `dealloc` and `finalize`, there are some constraints on the implementation of `finalize` that do not apply to `dealloc`. In particular, you must ensure that there are no ordering issues.

Occasionally, within a completely captive subgraph, significant work is done in `dealloc` methods as they do recursive releases and subsequent deallocations. Many applications that use reference counting make use of the deterministic ordering of object deallocation. If one object A retains another object B, A can guarantee that during its `dealloc` method the B is valid (object B’s `dealloc` method has not been called) and so send B messages and otherwise interact with it.

If you use garbage collection, it is possible for A and B to become invalid at the same time. Moreover, there is no ordering of the invocation of objects’ `finalize` methods. If object A has a strong reference to object B, and object A and object B are both reclaimed during a given collection cycle, then there is no guarantee that object A’s `finalize` method will be invoked first. Object A cannot therefore make any assumptions about the state of object B in its `finalize` method. Or, conversely, object B must be prepared to be messaged after its `finalize` method is invoked.

Since `finalize` messages may be sent in any order, existing code that relies on side effects during `dealloc` methods will need to introduce new methods to achieve a similar graph walking effect.

If you use weak collections, the count of the collection may change during an iteration loop. This will obviously lead to problems if you iterate over the contents of the collection directly using a `for` loop. On the other hand, enumeration objects can cause resurrection of the collection or its objects if all are found to be garbage at the same time—this is particularly likely to occur if you use a pattern where you have a collection of helper objects and on finalization they perform cleanup work (see [Avoiding Resurrection](Implementing%20a%20finalize%20Method.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjtfvjvomq)).

To avoid these problems, you should use the [NSFastEnumeration](https://developer.apple.com/documentation/foundation/nsfastenumeration) protocol (see [Fast Enumeration](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocFastEnumeration.html#//apple_ref/doc/uid/TP30001163-CH18)) to iterate over the contents of a collection.

A common pattern is to associate an object with an external resource—for example, a file descriptor—that needs "management" or other state that the object coordinates, often across several threads. The typical implementation is to use a non-retaining CFDictionary coupled with a global lock at the lookup and deallocation stages. This pattern does not work when you use garbage collection because there is a timing window during finalization where the object is no longer reachable from a root, yet is still in the dictionary and can be resurrected.

The solution is to use an `NSMapTable` object. A map table can hold keys, values, or both weakly, and when the objects are discovered unreachable the table is immediately cleared of such entries before any finalization is performed. This prevents resurrection of the object being finalized. For resources created and destroyed within the application, such as file descriptors, this is an adequate solution.

Cocoa used to have several classes of object (fonts and images) where a global table of strong keys held weak value references to the objects. The object would remove itself from the global table on `dealloc`. But it would also be the case that there would be some universally known objects that never went away, and the pattern was to allocate these at startup using `[[alloc ] init]` and simply place them in the weak table. The reference count for these objects would never decrease and so they would live indefinitely. Under garbage collection, in the absence of a strong reference these universal objects are collected. The solution is to use `[[NSGarbageCollector defaultCollector] disableCollectorForPointer:object]` on these objects before placing them in the weak table.

If you do not use garbage collection, references to delegates are typically “weak” (in that the delegate is not retained). This is to avoid retain cycle problems. With garbage collection, retain cycles do not pose a problem, so there is no need to declare references to delegates as `__weak`.

You cannot allocate objects in separate zones—all Cocoa objects must be allocated in a single managed heap. If your application is running in garbage collection mode, the zone parameter in `NSAllocateObject` is ignored. With garbage collection enabled, `[NSObject allocWithZone:zone]` calls `NSAllocateObject(cls, extra, zone)`, which in turn calls `objc_allocate_object(cls, extra)`.

You can allocate memory such that it is scanned using [NSAllocateCollectable](https://developer.apple.com/documentation/foundation/1539807-nsallocatecollectable) or [NSReallocateCollectable](https://developer.apple.com/documentation/foundation/1539802-nsreallocatecollectable).

[Next](Using%20Core%20Foundation%20with%20Garbage%20Collection.md)[Previous](Implementing%20a%20finalize%20Method.md)

