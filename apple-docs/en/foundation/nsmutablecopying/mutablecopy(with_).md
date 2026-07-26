---
title: 'mutableCopy(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablecopying/mutablecopy(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablecopying/mutablecopy(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablecopying/mutablecopy%28with%3A%29.json'
content_hash: 'sha256:3fb1bf2163f9f516'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableCopying](../nsmutablecopying.md)

# mutableCopy(with:)

<sub>Instance Method</sub>

Returns a new instance that’s a mutable copy of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mutableCopy(with zone: NSZone? = nil) -> Any
```

## Parameters

- `zone` — This parameter is ignored. Memory zones are no longer used by Objective-C.

## Discussion

The returned object is implicitly retained by the sender, which is responsible for releasing it. The copy returned is mutable whether the original is mutable or not.

## See Also

### Related Documentation

- [- copyWithZone:](<../nscopying/copy(with_).md>) — Returns a new instance that’s a copy of the receiver.
- [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i)
- [mutableCopy()](<../../objectivec/nsobject-swift.class/mutablecopy().md>) — Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
