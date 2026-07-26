---
title: 'conformedCaption(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptionformatconformer/conformedcaption(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionformatconformer/conformedcaption(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionformatconformer/conformedcaption%28for%3A%29.json'
content_hash: 'sha256:fe392d3398b9adcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionFormatConformer](../avcaptionformatconformer.md)

# conformedCaption(for:)

<sub>Instance Method</sub>

Creates a caption that conforms to a specific format.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func conformedCaption(for caption: AVCaption) throws -> AVCaption
```

## Parameters

- `caption` — The caption to conform.

## Return Value

A caption that conforms to the defined caption format.

## See Also

### Conforming captions

- [conformsCaptionsToTimeRange](conformscaptionstotimerange.md) — A Boolean value that indicates whether to conform the time range of a canonical caption.
