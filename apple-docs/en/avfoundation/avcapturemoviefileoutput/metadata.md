---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemoviefileoutput/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/metadata.json'
content_hash: 'sha256:d9bd1e456bbbfcc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# metadata

<sub>Instance Property</sub>

The metadata for the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var metadata: [AVMetadataItem]? { get set }
```

## Discussion

This array contains [AVMetadataItem](../avmetadataitem.md) objects. You use it to add metadata, such as copyright, creation date, and so on, to the recorded movie file.

## See Also

### Configuring movies

- [movieFragmentInterval](moviefragmentinterval.md) — The number of seconds of output that are written per fragment.
