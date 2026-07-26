---
title: isProVideoStorageSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturemoviefileoutput/isprovideostoragesupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/isprovideostoragesupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/isprovideostoragesupported.json'
content_hash: 'sha256:34b2dc30aca75cb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# isProVideoStorageSupported

<sub>Instance Property</sub>

Whether this movie file output supports writing to Pro Video Storage in its current configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isProVideoStorageSupported: Bool { get }
```

## Discussion

A value of `YES` indicates that Pro Video Storage support is enabled for this output while `NO` indicates it is not. Check this value prior to setting property usesProVideoStorage to avoid exceptions when Pro Video Storage support is not enabled.
