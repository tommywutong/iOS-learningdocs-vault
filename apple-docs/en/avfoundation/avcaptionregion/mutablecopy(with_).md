---
title: 'mutableCopy(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptionregion/mutablecopy(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/mutablecopy(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/mutablecopy%28with%3A%29.json'
content_hash: 'sha256:569d48f010b7f87f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# mutableCopy(with:)

<sub>Instance Method</sub>

Creates a mutable copy of a caption region.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func mutableCopy(with zone: NSZone? = nil) -> Any
```

## Parameters

- `zone` — The system ignores this parameter. Objective-C doesn’t no longer supports memory zones.

## Return Value

A copy of the region.

## Discussion

This method throws an exception if the caption region contains an identifier.

## See Also

### Processing regions

- [- encodeWithCoder:](<encode(with_).md>) — Encodes the region using the specified encoder.
- [- isEqual:](<isequal(__).md>) — Returns a Boolean value that indicates whether an object equals another.
