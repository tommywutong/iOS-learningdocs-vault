---
title: mutableCopy()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/mutablecopy()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutablecopy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/mutablecopy%28%29.json'
content_hash: 'sha256:69f5342018b9500d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# mutableCopy()

<sub>Instance Method</sub>

Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mutableCopy() -> Any
```

## Return Value

The object returned by the [NSMutableCopying](../../foundation/nsmutablecopying.md) protocol method [mutableCopy(with:)](<../../foundation/nsmutablecopying/mutablecopy(with_).md>), where the zone is `nil`.

## Discussion

This is a convenience method for classes that adopt the [NSMutableCopying](../../foundation/nsmutablecopying.md) protocol. An exception is raised if there is no implementation for [mutableCopy(with:)](<../../foundation/nsmutablecopying/mutablecopy(with_).md>).

## See Also

### Creating, Copying, and Deallocating Objects

- [- init](<init().md>) — Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [- copy](<copy().md>) — Returns the object returned by `copy(with:)`.
