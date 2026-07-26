---
title: isConstantColorEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isconstantcolorenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isconstantcolorenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isconstantcolorenabled.json'
content_hash: 'sha256:2ee44071eb8f964f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isConstantColorEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the photo output configures the render pipeline to perform constant color capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isConstantColorEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). Set the value to [true](../../swift/true.md) to enable support for taking constant color photos. You can only enable constant color capture if the value of [constantColorSupported](isconstantcolorsupported.md) is [true](../../swift/true.md).

> [!note] Note
> Enabling constant color requires a lengthy reconfiguration of the capture pipeline. If you intend to capture constant color photos, set this property to [true](../../swift/true.md) before calling [- startRunning](<../avcapturesession/startrunning().md>), or within [- beginConfiguration](<../avcapturesession/beginconfiguration().md>) and [- commitConfiguration](<../avcapturesession/commitconfiguration().md>) calls on a running capture session.

## See Also

### Configuring constant color

- [constantColorSupported](isconstantcolorsupported.md) — A Boolean value that indicates whether a photo output supports constant color capture.
