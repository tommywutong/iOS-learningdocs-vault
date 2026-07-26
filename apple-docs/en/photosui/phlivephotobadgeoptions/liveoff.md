---
title: liveOff
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phlivephotobadgeoptions/liveoff
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotobadgeoptions/liveoff'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotobadgeoptions/liveoff.json'
content_hash: 'sha256:12dd37dc73e92515'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoBadgeOptions](../phlivephotobadgeoptions.md)

# liveOff

<sub>Type Property</sub>

Return an icon for identifying assets whose additional Live Photo content is disabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var liveOff: PHLivePhotoBadgeOptions { get }
```

## Discussion

For example, when implementing a picker interface for sharing photos on a social network, you can use this icon to indicate when the user has chosen not to share the additional motion and sound content of a Live Photo.

## See Also

### Constants

- [PHLivePhotoBadgeOptionsOverContent](overcontent.md) — Return a variant icon for use on a variable background such as an animating Live Photo view.
