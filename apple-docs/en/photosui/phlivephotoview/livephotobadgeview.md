---
title: livePhotoBadgeView
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.12+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phlivephotoview/livephotobadgeview
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoview/livephotobadgeview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoview/livephotobadgeview.json'
content_hash: 'sha256:40622856a3da014e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHLivePhotoView](../phlivephotoview.md)

# livePhotoBadgeView

<sub>Instance Property</sub>

A view for displaying Live Photo status.

<sub>macOS</sub>

```swift
var livePhotoBadgeView: NSView? { get }
```

## Discussion

The [PHLivePhotoView](../phlivephotoview.md) uses this subview to display icons indicating the existence or status of Live Photo content. Photos manages the content displayed in the badge view, so you don’t need to do anything with view’s content—instead, this property provides access to the badge view so you can change where it appears in your view hierarchy if needed. For example, if you display a Live Photo view within a scroll view, you can move the badge view so that its position remains constant while the scroll view scrolls.

## See Also

### Accessing User Interface Icons for Live Photos

- [+ livePhotoBadgeImageWithOptions:](<livephotobadgeimage(options_).md>) — Returns an icon image for the specified Live Photo semantic options.
