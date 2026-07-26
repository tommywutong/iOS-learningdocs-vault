---
title: adjustment
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversionwarning/adjustment
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversionwarning/adjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversionwarning/adjustment.json'
content_hash: 'sha256:f7e25081eeafe8e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionWarning](../avcaptionconversionwarning.md)

# adjustment

<sub>Instance Property</sub>

A correction the converter makes when it converts a caption to a specific format.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var adjustment: AVCaptionConversionAdjustment? { get }
```

## Discussion

If this value is `nil` and you perform the conversion without correcting the problem, the system doesn’t include captions that you indicate in the output media data.

## See Also

### Inspecting the warning

- [warningType](warningtype-swift.property.md) — A type that indicates the nature of the validation warning.
- [rangeOfCaptions](rangeofcaptions.md) — The range of the captions for which the system issued a warning.
- [AVCaptionConversionAdjustment](../avcaptionconversionadjustment.md) — An object that describes an adjustment to correct a problem found during validation of a caption conversion.
- [WarningType](warningtype-swift.struct.md) — The type of a caption conversion warning.
