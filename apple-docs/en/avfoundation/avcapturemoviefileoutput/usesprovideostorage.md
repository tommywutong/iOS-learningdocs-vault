---
title: usesProVideoStorage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturemoviefileoutput/usesprovideostorage
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/usesprovideostorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/usesprovideostorage.json'
content_hash: 'sha256:b50fe88073c7cfed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# usesProVideoStorage

<sub>Instance Property</sub>

Whether this movie file output is configured to write to Pro Video Storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var usesProVideoStorage: Bool { get set }
```

## Discussion

Default is `NO`. Raises an exception if set to `YES` while proVideoStorageSupported is `NO`.
