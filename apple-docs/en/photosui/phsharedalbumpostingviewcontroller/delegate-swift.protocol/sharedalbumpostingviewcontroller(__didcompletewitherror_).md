---
title: 'sharedAlbumPostingViewController(_:didCompleteWithError:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photosui/phsharedalbumpostingviewcontroller/delegate-swift.protocol/sharedalbumpostingviewcontroller(_:didcompletewitherror:)'
source_url: 'https://developer.apple.com/documentation/photosui/phsharedalbumpostingviewcontroller/delegate-swift.protocol/sharedalbumpostingviewcontroller(_:didcompletewitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phsharedalbumpostingviewcontroller/delegate-swift.protocol/sharedalbumpostingviewcontroller%28_%3Adidcompletewitherror%3A%29.json'
content_hash: 'sha256:f530ad740846e15c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [PhotosUI](../../../photosui.md) · [PHSharedAlbumPostingViewController](../../phsharedalbumpostingviewcontroller.md) · [Delegate](../delegate-swift.protocol.md)

# sharedAlbumPostingViewController(_:didCompleteWithError:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func sharedAlbumPostingViewController(_ postingViewController: PHSharedAlbumPostingViewController, didCompleteWithError error: (any Error)?)
```

## Discussion

Called when asset posting has completed.

`error` will be `nil` if asset posting was successful and non-`nil` if it was unsuccessful. The view controller won’t be dismissed automatically when this method is called.
