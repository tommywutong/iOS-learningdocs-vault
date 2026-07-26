---
title: 'loadPreviewImage(options:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/loadpreviewimage(options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/loadpreviewimage(options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/loadpreviewimage%28options%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:1c6f10dfa0df76c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# loadPreviewImage(options:completionHandler:)

<sub>Instance Method</sub>

Loads the preview image for the item that the item provider represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadPreviewImage(options: [AnyHashable : Any]! = [:], completionHandler: NSItemProvider.CompletionHandler!)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadPreviewImage(options: [AnyHashable : Any]! = [:]) async throws -> any NSSecureCoding
```

## Parameters

- `options` — A dictionary of keys and values that provide information about the item, such as the size of an image. For a list of possible keys, see [Options Dictionary Key](../options-dictionary-key.md).

- `completionHandler` — A completion handler block to execute with the results. The first parameter of this block must be a parameter of type [NSData](../nsdata.md), [NSURL](../nsurl.md), [UIImage](../../uikit/uiimage.md) (in iOS), or [NSImage](../../appkit/nsimage.md) (in macOS) for receiving the image data. For more information about implementing the block, see [CompletionHandler](completionhandler.md).

## Discussion

To handle image preview yourself, provide a completion handler block that returns an [NSData](../nsdata.md) or [NSURL](../nsurl.md) object, or an instance of a platform-specific image class ([UIImage](../../uikit/uiimage.md) or [NSImage](../../appkit/nsimage.md)).

This method supports implicit type coercion for the item parameter of the completion block.

## See Also

### Loading a preview image

- [previewImageHandler](previewimagehandler.md) — The custom preview image handler block for the item provider.
