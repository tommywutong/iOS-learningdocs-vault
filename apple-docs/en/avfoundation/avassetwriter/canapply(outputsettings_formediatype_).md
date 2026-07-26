---
title: 'canApply(outputSettings:forMediaType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/canapply(outputsettings:formediatype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/canapply(outputsettings:formediatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/canapply%28outputsettings%3Aformediatype%3A%29.json'
content_hash: 'sha256:d142a4e396096c07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# canApply(outputSettings:forMediaType:)

<sub>Instance Method</sub>

Determines whether the output file format supports the output settings for a specific media type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func canApply(outputSettings: [String : Any]?, forMediaType mediaType: AVMediaType) -> Bool
```

## Parameters

- `outputSettings` — The output settings to validate.

- `mediaType` — The media type to validate the output settings for.

## Return Value

[true](../../swift/true.md) if the format supports the output settings; otherwise, [false](../../swift/false.md).

## Discussion

Use this method to determine the compatibility of output settings for a particular media type. For example, video compression settings that specify H.264 compression aren’t compatible with file formats that don’t contain H.264-compressed video.

## See Also

### Configuring inputs

- [inputs](inputs.md) — The inputs an asset writer contains.
- [availableMediaTypes](availablemediatypes.md) — The media types the asset writer supports adding as inputs.
- [- canAddInput:](<canadd(__)-6al7j.md>) — Determines whether the asset writer supports adding the input.
- [- addInput:](<add(__)-4c4d0.md>) — Adds an input to an asset writer. _(deprecated)_
