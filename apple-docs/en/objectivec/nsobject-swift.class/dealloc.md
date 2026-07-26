---
title: dealloc
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/dealloc
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/dealloc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/dealloc.json'
content_hash: 'sha256:2a245632c7dad82d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# dealloc

<sub>Instance Method</sub>

Deallocates the memory occupied by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) dealloc;
```

## Discussion

Subsequent messages to the receiver may generate an error indicating that a message was sent to a deallocated object (provided the deallocated memory hasn’t been reused yet).

You override this method to dispose of resources other than the object’s instance variables, for example:

```objc
- (void)dealloc {
    free(myBigBlockOfMemory);
}
```

In an implementation of `dealloc`, do not invoke the superclass’s implementation. You should try to avoid managing the lifetime of limited resources such as file descriptors using `dealloc`.

You never send a [dealloc](dealloc.md) message directly. Instead, an object’s `dealloc` method is invoked by the runtime. See [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i) for more details.

### Special Considerations

When not using ARC, your implementation of `dealloc` must invoke the superclass’s implementation as its last instruction.

## See Also

### Creating, Copying, and Deallocating Objects

- [alloc](alloc.md) — Returns a new instance of the receiving class.
- [allocWithZone:](allocwithzone_.md) — Returns a new instance of the receiving class.
- [- init](<init().md>) — Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [- copy](<copy().md>) — Returns the object returned by `copy(with:)`.
- [copyWithZone:](copywithzone_.md) — Returns the receiver.
- [- mutableCopy](<mutablecopy().md>) — Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
- [mutableCopyWithZone:](mutablecopywithzone_.md) — Returns the receiver.
- [new](new.md) — Allocates a new instance of the receiving class, sends it an [- init](<init().md>) message, and returns the initialized object.
