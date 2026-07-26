---
title: isLensStabilizationEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotobracketsettings/islensstabilizationenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings/islensstabilizationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotobracketsettings/islensstabilizationenabled.json'
content_hash: 'sha256:2b0f64efdf26b1bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoBracketSettings](../avcapturephotobracketsettings.md)

# isLensStabilizationEnabled

<sub>Instance Property</sub>

A Boolean value that specifies whether to stabilize the lens for the duration of the bracketed capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isLensStabilizationEnabled: Bool { get set }
```

## Discussion

When this setting is [true](../../swift/true.md), the photo output uses optical image stabilization to hold the lens steady for the duration of the bracketed capture, helping to counter hand shake and produce a sharper bracket of images. The default setting is [false](../../swift/false.md).

You can enable this setting only if the photo output’s [lensStabilizationDuringBracketedCaptureSupported](../avcapturephotooutput/islensstabilizationduringbracketedcapturesupported.md) property is [true](../../swift/true.md). The capture output validates this requirement when you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your settings and delegate do not meet this requirement, that method raises an exception.

## See Also

### Working with bracketed settings

- [bracketedSettings](bracketedsettings.md) — An array describing the number of and settings for images to produce in a bracketed capture.
