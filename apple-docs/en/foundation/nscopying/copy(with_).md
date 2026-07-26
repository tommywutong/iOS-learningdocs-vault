---
title: 'copy(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscopying/copy(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscopying/copy(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscopying/copy%28with%3A%29.json'
content_hash: 'sha256:a20b555eea463467'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCopying](../nscopying.md)

# copy(with:)

<sub>Instance Method</sub>

Returns a new instance that’s a copy of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copy(with zone: NSZone? = nil) -> Any
```

## Parameters

- `zone` — This parameter is ignored. Memory zones are no longer used by Objective-C.

## Discussion

The returned object is implicitly retained by the sender, who is responsible for releasing it. The copy returned is immutable if the consideration “immutable vs. mutable” applies to the receiving object; otherwise the exact nature of the copy is determined by the class.

## See Also

### Related Documentation

- [- mutableCopyWithZone:](<../nsmutablecopying/mutablecopy(with_).md>) — Returns a new instance that’s a mutable copy of the receiver.
- [copy()](<../../objectivec/nsobject-swift.class/copy().md>) — Returns the object returned by `copy(with:)`.
- [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i)
