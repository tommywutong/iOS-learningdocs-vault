---
title: 'postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+（27.0 起废弃）, iPadOS 26.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/posttophotossharedalbumsheet(ispresented:items:photolibrary:defaultalbumidentifier:completion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/posttophotossharedalbumsheet(ispresented:items:photolibrary:defaultalbumidentifier:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/posttophotossharedalbumsheet%28ispresented%3Aitems%3Aphotolibrary%3Adefaultalbumidentifier%3Acompletion%3A%29.json'
content_hash: 'sha256:dd4de2cd73f1a7a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)

<sub>Instance Method</sub>

Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.

> [!warning] Deprecated
> Use View.photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func postToPhotosSharedAlbumSheet(isPresented: Binding<Bool>, items: [PHPickerResult], photoLibrary: PHPhotoLibrary, defaultAlbumIdentifier: String? = nil, completion: ((Result<Void, any Error>) -> Void)? = nil) -> some View

```

## Parameters

- `isPresented` — The binding to whether the sheet should be shown.

- `items` — The items to be posted to the shared album.

- `photoLibrary` — Library to choose from.

- `defaultAlbumIdentifier` — Identifier for the shared album to be pre-selected. If none provided user can manually choose the shared album in UI.

- `completion` — Called with the result on completion of the request.

## See Also

### Technology-specific modifiers

- [offerCodeRedemption(isPresented:onCompletion:)](<offercoderedemption(ispresented_oncompletion_).md>) _(deprecated)_
- [subscriptionPromotionalOffer(offer:signature:)](<subscriptionpromotionaloffer(offer_signature_).md>) — Selects a promotional offer to apply to a purchase a customer makes from a subscription store view. _(deprecated)_
