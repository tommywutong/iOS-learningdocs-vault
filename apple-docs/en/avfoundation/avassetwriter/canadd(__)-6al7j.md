---
title: 'canAdd(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/canadd(_:)-6al7j'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/canadd(_:)-6al7j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/canadd%28_%3A%29-6al7j.json'
content_hash: 'sha256:8632f292b0878a3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# canAdd(_:)

<sub>Instance Method</sub>

Determines whether the asset writer supports adding the input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func canAdd(_ input: AVAssetWriterInput) -> Bool
```

## Parameters

- `input` — The asset writer input to add.

## Return Value

[true](../../swift/true.md) if you can add the input to the asset writer; otherwise [false](../../swift/false.md).

## See Also

### Configuring inputs

- [inputs](inputs.md) — The inputs an asset writer contains.
- [availableMediaTypes](availablemediatypes.md) — The media types the asset writer supports adding as inputs.
- [- canApplyOutputSettings:forMediaType:](<canapply(outputsettings_formediatype_).md>) — Determines whether the output file format supports the output settings for a specific media type.
- [- addInput:](<add(__)-4c4d0.md>) — Adds an input to an asset writer. _(deprecated)_
