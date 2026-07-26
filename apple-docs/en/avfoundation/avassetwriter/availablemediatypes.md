---
title: availableMediaTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/availablemediatypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/availablemediatypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/availablemediatypes.json'
content_hash: 'sha256:4592184fadade691'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# availableMediaTypes

<sub>Instance Property</sub>

The media types the asset writer supports adding as inputs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var availableMediaTypes: [AVMediaType] { get }
```

## Discussion

Use this property to determine the acceptable media types for the container file that the asset writer outputs.

## See Also

### Configuring inputs

- [inputs](inputs.md) — The inputs an asset writer contains.
- [- canApplyOutputSettings:forMediaType:](<canapply(outputsettings_formediatype_).md>) — Determines whether the output file format supports the output settings for a specific media type.
- [- canAddInput:](<canadd(__)-6al7j.md>) — Determines whether the asset writer supports adding the input.
- [- addInput:](<add(__)-4c4d0.md>) — Adds an input to an asset writer. _(deprecated)_
