---
title: Garbage Collection Programming Guide
apple_id: TP40002431
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/GarbageCollection/Articles/gcFinalize.html
archived_at: '2026-07-15T07:15:59.998267Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Garbage Collection Programming Guide](Introduction%20to%20Garbage%20Collection.md)


[Next](Inapplicable%20Patterns.md)[Previous](Using%20Garbage%20Collection.md)

# Implementing a finalize Method

This article describes how to correctly and efficiently implement a `finalize` method.

Object finalization occurs at most once during the lifetime of an object—when it is collected. When more than one object is finalized, the order in which they are sent a `finalize` message is indeterminate, even if there are references between them. If you send messages between objects when they are being finalized, you must take extreme care to avoid anomalous behavior. To ease correctness concerns alone, it is best not to attempt any work in a finalizer. Moreover, however, time spent in object finalization incurs application overhead. Your design goal should therefore be to not have a finalizer at all. If you must use a finalizer, you should keep it as short as possible, and reference as few other objects as possible in its implementation.

Memory recovery time is typically _not_ the best time to reclaim resources or do clean-up work (such as releasing instance variables and closing resources). Your `finalize` code is part of the garbage collector’s critical path, and so should be kept to a minimum if not eliminated entirely. You should implement invalidation code that is distinct from your deallocation or finalization code and invoke it when appropriate.

To make your `finalize` method as efficient as possible, you should typically _not_ do any of the following:

- Disconnect object graphs
- Set instance variables to `nil`
- For view classes, remove `self` from the existing view hierarchy
- Remove `self` as an observer of a notification center (in a garbage collected environment, notification centers use zeroing weak references).

You should typically use `NSMakeCollectable()` on Core Foundation objects rather than relying on `CFRelease()` in `finalize`—this way collectable Core Foundation objects are actually collected sooner. (Collectable objects are collected with the source object whereas released objects are simply marked as being eligible for collection—these must wait for the next collection cycle to be collected.)

No objects are deallocated until all finalizers are complete (otherwise, no finalizer could use any other object anywhere, including objects like `NSString` that don’t have a finalizer) so you can access already-finalized objects—but only in other finalizers. Within a `finalize` method, therefore, you should reference as few other objects as possible. You can't necessarily know what other objects might have a reference to your instance, or whether they might message your instance from their finalizer, you must therefore code defensively to try to keep your instance as fully functional as is possible to support messages it might receive after finalization. Similarly, since you don't know in what order objects will be finalized, it may be that objects you message during a `finalize` method have themselves already been cleared.

For example, some objects use collection objects (arrays, dictionaries, or sets) to hold other related objects. Sometimes during finalization the collection is accessed and messages sent to each and every contained object. If the collection itself had been finalized and had discharged its objects, the algorithm would fail on that account alone. Similarly, if any of the objects in the collection can no longer respond correctly to the requested message after it is finalized, the algorithm again will fail.

Some Cocoa objects make assumptions about how many references are kept about themselves and where, for example by implementing the `release` method to trap the transition to a known value (typically of `0`) and then distributing cleanup work among their holders. In a garbage-collected environment, this pattern can lead to “resurrection” of an object—that is, it becomes valid again after having been finalized.

Resurrection occurs when a `finalize` method stores `self` in a non-garbage object. The resurrected object becomes a zombie. It logs all messages that are sent to it, but it is otherwise useless. It is eventually deallocated when it becomes garbage again (when its container is collected). You should consider resurrection to be a programming error.

The following example illustrates a trivial, albeit unlikely, case:

```objc
- (void)finalize
{
    [NSArray arrayWithObject:self];
}
```


The following example illustrates what happens if an object must manage an external resource—in this case, a Logger object is given a file descriptor to use for writing logging messages. File descriptors are not inexhaustible, and so the object provides a `close` method to relinquish the resource. In an ideal scenario, you should have closed the file descriptor before the `finalize` method is called. If, however—as is implied in this example—you have a shared or singleton object, it may not be possible to actively manage the object's resources, and you will have to rely on `finalize` to clean up. To ensure that the file descriptor is not kept beyond the object's lifetime, therefore, the `close` method is invoked in the `finalize` method.

```objc
@interface Logger : NSObject {
    int fileDescriptor;
}
- initWithFileDescriptor:(int)aFileDescriptor;
- (void)close;
- (void)log:(NSString *)message;
@end


@implementation Logger
- initWithFileDescriptor:(int)aFileDescriptor {
    self = [super init];
    if (self) {
        fileDescriptor = aFileDescriptor;
    }
    return self;
}

- (void)close {
    if (fileDescriptor != -1) close(fileDescriptor);
    fileDescriptor = -1;
}

- (void)finalize {
    [self close];
    [super finalize];
}

- (void)log:(NSString *)message {
    // Implementation continues ...
}
@end
```

The runtime invokes the `finalize` method after it determines that a logger object can no longer be reached. The message is sent once and it is an error for a finalizing object to have a new reference created to it in a reachable object. In other words, the object may not be revived (resurrected) once found to be unreachable.

A problem emerges even in this simple example. What would happen if a Logger object were created to track some other “larger” object, for example a window or a drawer or a network connection? This larger object might offer a logging API that enabled notations to be delivered to the file descriptor to mark progress. It might be natural to then have in this larger object one last message in its finalizer:

```objc
- (void)finalize {
    [logger log:@"saying goodbye!"];
    [logger close];
    [super finalize];
}
```

Unfortunately the results would not always match your expectation: the final message would sometimes appear and sometimes not. This is because:

- The larger object and the logger object would both be found to be garbage in the same collection cycle.
- For the file descriptor resource to still be open when the larger object sends the `log:` message, the logger must finalized after the larger object.
- The order in which the two objects are finalized, however, is non-deterministic.

[Next](Inapplicable%20Patterns.md)[Previous](Using%20Garbage%20Collection.md)

