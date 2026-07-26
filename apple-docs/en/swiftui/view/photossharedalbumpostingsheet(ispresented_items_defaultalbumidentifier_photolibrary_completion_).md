---
title: 'photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/photossharedalbumpostingsheet(ispresented:items:defaultalbumidentifier:photolibrary:completion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/photossharedalbumpostingsheet(ispresented:items:defaultalbumidentifier:photolibrary:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/photossharedalbumpostingsheet%28ispresented%3Aitems%3Adefaultalbumidentifier%3Aphotolibrary%3Acompletion%3A%29.json'
content_hash: 'sha256:a3d7fd5d8607e466'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)

<sub>Instance Method</sub>

Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func photosSharedAlbumPostingSheet(isPresented: Binding<Bool>, items: [PHPickerResult], defaultAlbumIdentifier: String? = nil, photoLibrary: PHPhotoLibrary, completion: ((Result<String, any Error>) -> Void)? = nil) -> some View

```

## Parameters

- `isPresented` — The binding to whether the sheet should be shown.

- `items` — The items to be posted to the shared album.

- `defaultAlbumIdentifier` — Identifier for the shared album to be pre-selected. If none provided user can manually choose the shared album in UI.

- `photoLibrary` — Library to choose from.

- `completion` — Called with the result on completion of the request.

## See Also

### Selecting photos

- [PhotosPicker](../../photosui/photospicker.md) — A view that displays a Photos picker for choosing assets from the photo library.
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:)](<photospicker(ispresented_selection_matching_preferreditemencoding_).md>) — Presents a Photos picker that selects a `PhotosPickerItem`.
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)](<photospicker(ispresented_selection_matching_preferreditemencoding_photolibrary_).md>) — Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)](<photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_).md>) — Presents a Photos picker that selects a collection of `PhotosPickerItem`.
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_).md>) — Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library.
- [photosPickerAccessoryVisibility(_:edges:)](<photospickeraccessoryvisibility(__edges_).md>) — Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar.
- [photosPickerDisabledCapabilities(_:)](<photospickerdisabledcapabilities(__).md>) — Disables capabilities of the Photos picker.
- [photosPickerSearchText(_:)](<photospickersearchtext(__).md>) — Sets search text of the Photos picker. _(beta)_
- [photosPickerStyle(_:)](<photospickerstyle(__).md>) — Sets the mode of the Photos picker.
- [photosPickerMetadataOptions(_:)](<photospickermetadataoptions(__).md>) — Sets metadata options for the Photos picker. _(beta)_
- [photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)](<photossharedalbumcreationsheet(ispresented_defaulttitle_defaultsharingpolicy_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to create a new shared album. _(beta)_
- [photosSharedAlbumCustomizationSheet(isPresented:albumIdentifier:photoLibrary:onCompletion:)](<photossharedalbumcustomizationsheet(ispresented_albumidentifier_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to customize a specified shared album. _(beta)_
