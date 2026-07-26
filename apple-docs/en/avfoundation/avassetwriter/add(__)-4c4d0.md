---
title: 'add(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriter/add(_:)-4c4d0'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/add(_:)-4c4d0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/add%28_%3A%29-4c4d0.json'
content_hash: 'sha256:75e2d0d92888a1ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# add(_:)

<sub>Instance Method</sub>

Adds an input to an asset writer.

> [!warning] Deprecated
> Use the appropriate AVAssetWriter.inputReceiver(for:...) overload for your input and optional adaptor instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func add(_ input: AVAssetWriterInput)
```

## Parameters

- `input` — A compatible asset writer input to add.

## Discussion

You can’t add inputs after asset writing begins.

## See Also

### Configuring inputs

- [inputs](inputs.md) — The inputs an asset writer contains.
- [availableMediaTypes](availablemediatypes.md) — The media types the asset writer supports adding as inputs.
- [- canApplyOutputSettings:forMediaType:](<canapply(outputsettings_formediatype_).md>) — Determines whether the output file format supports the output settings for a specific media type.
- [- canAddInput:](<canadd(__)-6al7j.md>) — Determines whether the asset writer supports adding the input.
