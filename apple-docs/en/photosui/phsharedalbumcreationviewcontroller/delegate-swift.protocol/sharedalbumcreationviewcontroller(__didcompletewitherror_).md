---
title: 'sharedAlbumCreationViewController(_:didCompleteWithError:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photosui/phsharedalbumcreationviewcontroller/delegate-swift.protocol/sharedalbumcreationviewcontroller(_:didcompletewitherror:)'
source_url: 'https://developer.apple.com/documentation/photosui/phsharedalbumcreationviewcontroller/delegate-swift.protocol/sharedalbumcreationviewcontroller(_:didcompletewitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phsharedalbumcreationviewcontroller/delegate-swift.protocol/sharedalbumcreationviewcontroller%28_%3Adidcompletewitherror%3A%29.json'
content_hash: 'sha256:c7c43dfbc64213c4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [PhotosUI](../../../photosui.md) · [PHSharedAlbumCreationViewController](../../phsharedalbumcreationviewcontroller.md) · [Delegate](../delegate-swift.protocol.md)

# sharedAlbumCreationViewController(_:didCompleteWithError:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func sharedAlbumCreationViewController(_ creationViewController: PHSharedAlbumCreationViewController, didCompleteWithError error: (any Error)?)
```

## Discussion

Called when shared album creation completes.

If creation was successful, `-[PHSharedAlbumCreationViewController albumIdentifier]` will be non-`nil` and `error` will be `nil`. If creation was unsuccessful, `-[PHSharedAlbumCreationViewController albumIdentifier]` will be `nil` and `error` will be non-`nil`. The creation was cancelled by the user, both `-[PHSharedAlbumCreationViewController albumIdentifier]` and `error` will be `nil`. The view controller won’t be dismissed automatically when this method is called.
