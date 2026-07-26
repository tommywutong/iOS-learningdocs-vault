---
title: conformsCaptionsToTimeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionformatconformer/conformscaptionstotimerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionformatconformer/conformscaptionstotimerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionformatconformer/conformscaptionstotimerange.json'
content_hash: 'sha256:f609ce58183a82ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionFormatConformer](../avcaptionformatconformer.md)

# conformsCaptionsToTimeRange

<sub>Instance Property</sub>

A Boolean value that indicates whether to conform the time range of a canonical caption.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var conformsCaptionsToTimeRange: Bool { get set }
```

## Discussion

By default, this property value is [false](../../swift/false.md). If you set the value to [true](../../swift/true.md), this object conforms the time range of captions to fit its encoded data.

When this object conforms captions to CAE608 format, it encodes them so that each CAE608 2-byte control code fits into one frame duration (1001/30000).

## See Also

### Conforming captions

- [- conformedCaptionForCaption:error:](<conformedcaption(for_).md>) — Creates a caption that conforms to a specific format.
