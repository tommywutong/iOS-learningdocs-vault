---
title: previewImageHandler
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/previewimagehandler
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/previewimagehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/previewimagehandler.json'
content_hash: 'sha256:f36f6824081e0057'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# previewImageHandler

<sub>Instance Property</sub>

The custom preview image handler block for the item provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var previewImageHandler: NSItemProvider.LoadHandler? { get set }
```

## Discussion

In your image handler block, return an [NSURL](../nsurl.md) object that specifies a file, or return an [NSData](../nsdata.md) object.

## See Also

### Loading a preview image

- [- loadPreviewImageWithOptions:completionHandler:](<loadpreviewimage(options_completionhandler_).md>) — Loads the preview image for the item that the item provider represents.
