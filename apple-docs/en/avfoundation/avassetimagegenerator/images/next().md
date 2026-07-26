---
title: next()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/images/next()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/images/next%28%29.json'
content_hash: 'sha256:1d61a4af9599712c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetImageGenerator](../../avassetimagegenerator.md) · [Images](../images.md)

# next()

<sub>Instance Method</sub>

Returns the next element in the sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
mutating func next() async -> AVAssetImageGenerator.Images.Element?
```

## Return Value

The next element, or `nil` if no more exist.

## See Also

### Iterating elements

- [Element](element.md) — An element that provides the result of an image generation request.
