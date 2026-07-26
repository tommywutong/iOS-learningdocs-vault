---
title: new
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/new
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/new'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/new.json'
content_hash: 'sha256:c4ebb069ee75ad3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# new

<sub>Type Method</sub>

Allocates a new instance of the receiving class, sends it an [- init](<init().md>) message, and returns the initialized object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) new;
```

## Return Value

A new instance of the receiver.

## Discussion

This method is a combination of [alloc](alloc.md) and [- init](<init().md>). Like [alloc](alloc.md), it initializes the `isa` instance variable of the new object so it points to the class data structure. It then invokes the [- init](<init().md>) method to complete the initialization process.

## See Also

### Creating, Copying, and Deallocating Objects

- [alloc](alloc.md) — Returns a new instance of the receiving class.
- [allocWithZone:](allocwithzone_.md) — Returns a new instance of the receiving class.
- [- init](<init().md>) — Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [- copy](<copy().md>) — Returns the object returned by `copy(with:)`.
- [copyWithZone:](copywithzone_.md) — Returns the receiver.
- [- mutableCopy](<mutablecopy().md>) — Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
- [mutableCopyWithZone:](mutablecopywithzone_.md) — Returns the receiver.
- [dealloc](dealloc.md) — Deallocates the memory occupied by the receiver.
