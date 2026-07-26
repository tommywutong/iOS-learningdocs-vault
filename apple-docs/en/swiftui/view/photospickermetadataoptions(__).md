---
title: 'photosPickerMetadataOptions(_:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/photospickermetadataoptions(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/photospickermetadataoptions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/photospickermetadataoptions%28_%3A%29.json'
content_hash: 'sha256:3b378b4b6e870e6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# photosPickerMetadataOptions(_:)

<sub>Instance Method</sub>

Sets metadata options for the Photos picker.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func photosPickerMetadataOptions(_ metadataOptions: PHPickerMetadataOptions) -> some View

```

## Parameters

- `metadataOptions` — One or more of the available metadata options.

## Return Value

A Photos picker with specified metadata options.

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
- [photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)](<photossharedalbumcreationsheet(ispresented_defaulttitle_defaultsharingpolicy_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to create a new shared album. _(beta)_
- [photosSharedAlbumCustomizationSheet(isPresented:albumIdentifier:photoLibrary:onCompletion:)](<photossharedalbumcustomizationsheet(ispresented_albumidentifier_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to customize a specified shared album. _(beta)_
- [photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](<photossharedalbumpostingsheet(ispresented_items_defaultalbumidentifier_photolibrary_completion_).md>) — Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album. _(beta)_
