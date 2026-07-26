---
title: 'mutableCopyWithZone:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/mutablecopywithzone:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutablecopywithzone:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/mutablecopywithzone%3A.json'
content_hash: 'sha256:27ce01ecccd17142'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# mutableCopyWithZone:

<sub>Type Method</sub>

Returns the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (id) mutableCopyWithZone:(struct _NSZone *) zone;
```

## Parameters

- `zone` — The memory zone in which to create the copy of the receiver.

## Return Value

The receiver.

## Discussion

This method exists so class objects can be used in situations where you need an object that conforms to the [NSMutableCopying](../../foundation/nsmutablecopying.md) protocol. For example, this method lets you use a class object as a key to an `NSDictionary` object. You should not override this method.

## See Also

### Creating, Copying, and Deallocating Objects

- [alloc](alloc.md) — Returns a new instance of the receiving class.
- [allocWithZone:](allocwithzone_.md) — Returns a new instance of the receiving class.
- [- init](<init().md>) — Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [- copy](<copy().md>) — Returns the object returned by `copy(with:)`.
- [copyWithZone:](copywithzone_.md) — Returns the receiver.
- [- mutableCopy](<mutablecopy().md>) — Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
- [dealloc](dealloc.md) — Deallocates the memory occupied by the receiver.
- [new](new.md) — Allocates a new instance of the receiving class, sends it an [- init](<init().md>) message, and returns the initialized object.
