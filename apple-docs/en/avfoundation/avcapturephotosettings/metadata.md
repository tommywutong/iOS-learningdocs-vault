---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/metadata.json'
content_hash: 'sha256:7efbda1ad424423e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# metadata

<sub>Instance Property</sub>

A dictionary of metadata keys and values to embed in photo file output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var metadata: [String : Any] { get set }
```

## Discussion

The capture output automatically writes metadata including image orientation, EXIF camera properties, and Live Photo metadata, but you can override those values or specify additional metadata using the keys and values listed in `CGImageProperties`. (Setting this property with any other keys raises an exception.)
