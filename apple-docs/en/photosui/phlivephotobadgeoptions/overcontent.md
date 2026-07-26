---
title: overContent
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phlivephotobadgeoptions/overcontent
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotobadgeoptions/overcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotobadgeoptions/overcontent.json'
content_hash: 'sha256:3161059f42b3613f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoBadgeOptions](../phlivephotobadgeoptions.md)

# overContent

<sub>Type Property</sub>

Return a variant icon for use on a variable background such as an animating Live Photo view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var overContent: PHLivePhotoBadgeOptions { get }
```

## Discussion

By default, the [+ livePhotoBadgeImageWithOptions:](<../phlivephotoview/livephotobadgeimage(options_).md>) returns a solid-color image suitable for use as a template image, which you can then tint for appropriate display against a specific background. If the background content is busy, animated, or unknown, add this option to instead obtain an icon (not suitable for use as a template image) that provides extra contrast for better readability.

## See Also

### Constants

- [PHLivePhotoBadgeOptionsLiveOff](liveoff.md) — Return an icon for identifying assets whose additional Live Photo content is disabled.
