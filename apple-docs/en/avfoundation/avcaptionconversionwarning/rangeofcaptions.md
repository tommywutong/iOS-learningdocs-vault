---
title: rangeOfCaptions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversionwarning/rangeofcaptions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionwarning/rangeofcaptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionwarning/rangeofcaptions.json'
content_hash: 'sha256:d56da55a42ad74fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionWarning](../avcaptionconversionwarning.md)

# rangeOfCaptions

<sub>Instance Property</sub>

The range of the captions for which the system issued a warning.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var rangeOfCaptions: NSRange { get }
```

## Discussion

This object only references captions with the same time range. If captions with different start times and durations have similar problems, or if individual captions have multiple problems, the validator generates separate instances of this class for each problem case.

## See Also

### Inspecting the warning

- [warningType](warningtype-swift.property.md) — A type that indicates the nature of the validation warning.
- [adjustment](adjustment.md) — A correction the converter makes when it converts a caption to a specific format.
- [AVCaptionConversionAdjustment](../avcaptionconversionadjustment.md) — An object that describes an adjustment to correct a problem found during validation of a caption conversion.
- [WarningType](warningtype-swift.struct.md) — The type of a caption conversion warning.
