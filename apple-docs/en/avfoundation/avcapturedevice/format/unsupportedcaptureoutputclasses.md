---
title: unsupportedCaptureOutputClasses
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/unsupportedcaptureoutputclasses
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/unsupportedcaptureoutputclasses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/unsupportedcaptureoutputclasses.json'
content_hash: 'sha256:ed3ea21e8ef79c0e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# unsupportedCaptureOutputClasses

<sub>Instance Property</sub>

The list of capture output subclasses not allowed for capture with this format, if any.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var unsupportedCaptureOutputClasses: [AnyClass] { get }
```

## Discussion

As a rule, capture formats with a given [mediaType](mediatype.md) are available for use with all [AVCaptureOutput](../../avcaptureoutput.md) subclasses that accept that media type. However, this isn’t always the case. For example, formats for high-resolution photo capture may not support the [AVCaptureMovieFileOutput](../../avcapturemoviefileoutput.md) class due to bandwidth limitations.
