---
title: 'sharedAlbumCustomizationViewController(_:didCompleteWithError:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photosui/phsharedalbumcustomizationviewcontroller/delegate-swift.protocol/sharedalbumcustomizationviewcontroller(_:didcompletewitherror:)'
source_url: 'https://developer.apple.com/documentation/photosui/phsharedalbumcustomizationviewcontroller/delegate-swift.protocol/sharedalbumcustomizationviewcontroller(_:didcompletewitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phsharedalbumcustomizationviewcontroller/delegate-swift.protocol/sharedalbumcustomizationviewcontroller%28_%3Adidcompletewitherror%3A%29.json'
content_hash: 'sha256:0743031535cdcbf6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [PhotosUI](../../../photosui.md) · [PHSharedAlbumCustomizationViewController](../../phsharedalbumcustomizationviewcontroller.md) · [Delegate](../delegate-swift.protocol.md)

# sharedAlbumCustomizationViewController(_:didCompleteWithError:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func sharedAlbumCustomizationViewController(_ customizationViewController: PHSharedAlbumCustomizationViewController, didCompleteWithError error: (any Error)?)
```

## Discussion

Called when shared album customization completes.

`error` will be `nil` if customization was successful and non-`nil` if it was unsuccessful. The view controller won’t be dismissed automatically when this method is called.
