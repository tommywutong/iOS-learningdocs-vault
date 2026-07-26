---
title: faceID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.10+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatafaceobject/faceid
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/faceid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatafaceobject/faceid.json'
content_hash: 'sha256:d72b3312e067cee5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataFaceObject](../avmetadatafaceobject.md)

# faceID

<sub>Instance Property</sub>

The unique ID for this face metadata object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var faceID: Int { get }
```

## Discussion

Each time a face enters the picture, it is assigned a new unique identifier, which you can use to reference the face in your code. Face IDs are not reused, and the same face leaving and entering the picture again is assigned a new identifier.
