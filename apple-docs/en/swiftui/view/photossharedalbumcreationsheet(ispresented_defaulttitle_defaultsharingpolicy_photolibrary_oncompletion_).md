---
title: 'photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/photossharedalbumcreationsheet(ispresented:defaulttitle:defaultsharingpolicy:photolibrary:oncompletion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/photossharedalbumcreationsheet(ispresented:defaulttitle:defaultsharingpolicy:photolibrary:oncompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/photossharedalbumcreationsheet%28ispresented%3Adefaulttitle%3Adefaultsharingpolicy%3Aphotolibrary%3Aoncompletion%3A%29.json'
content_hash: 'sha256:76634054fe2a6a50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)

<sub>Instance Method</sub>

Presents a view for allowing the user to create a new shared album.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func photosSharedAlbumCreationSheet(isPresented: Binding<Bool>, defaultTitle: String? = nil, defaultSharingPolicy: PHSharedAlbumCreationSharingPolicy? = nil, photoLibrary: PHPhotoLibrary, onCompletion: ((PHSharedAlbumCreationResult?) -> Void)? = nil) -> some View

```

## Parameters

- `isPresented` — The binding for whether the shared album creation view should be shown.

- `defaultTitle` — The default title for the shared album. Useful for suggesting a relevant title to the user.

- `defaultSharingPolicy` — The default sharing policy of the shared album. If `nil`, this defaults to `.private`.

- `photoLibrary` — The photo library in which the shared album will be created.

- `onCompletion` — The callback that will be invoked when shared album creation has succeeded or failed. If successful, the `String` will be the album’s identifier.

## Discussion

> [!note] Remark
> When creation is finished, `onCompletion` will be called before`isPresented` is set to `false`. If the user cancels creation, `isPresented` will be set to `false` and `onCompletion` will not be called.

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
- [photosSharedAlbumCustomizationSheet(isPresented:albumIdentifier:photoLibrary:onCompletion:)](<photossharedalbumcustomizationsheet(ispresented_albumidentifier_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to customize a specified shared album. _(beta)_
- [photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](<photossharedalbumpostingsheet(ispresented_items_defaultalbumidentifier_photolibrary_completion_).md>) — Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album. _(beta)_
