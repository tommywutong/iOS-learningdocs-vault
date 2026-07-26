---
title: 'allocWithZone:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/allocwithzone:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/allocwithzone:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/allocwithzone%3A.json'
content_hash: 'sha256:69c74d52cd7535ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# allocWithZone:

<sub>Type Method</sub>

Returns a new instance of the receiving class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) allocWithZone:(struct _NSZone *) zone;
```

## Parameters

- `zone` — This parameter is ignored.

## Return Value

A new instance of the receiver.

## Discussion

The `isa` instance variable of the new instance is initialized to a data structure that describes the class; memory for all other instance variables is set to `0`.

You must use an `init...` method to complete the initialization process. For example:

```objc
TheClass *newObject = [[TheClass allocWithZone:nil] init];
```

Do not override [allocWithZone:](allocwithzone_.md) to include any initialization code. Instead, class-specific versions of `init...` methods.

This method exists for historical reasons; memory zones are no longer used by Objective-C.

## See Also

### Creating, Copying, and Deallocating Objects

- [alloc](alloc.md) — Returns a new instance of the receiving class.
- [- init](<init().md>) — Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [- copy](<copy().md>) — Returns the object returned by `copy(with:)`.
- [copyWithZone:](copywithzone_.md) — Returns the receiver.
- [- mutableCopy](<mutablecopy().md>) — Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
- [mutableCopyWithZone:](mutablecopywithzone_.md) — Returns the receiver.
- [dealloc](dealloc.md) — Deallocates the memory occupied by the receiver.
- [new](new.md) — Allocates a new instance of the receiving class, sends it an [- init](<init().md>) message, and returns the initialized object.
