---
title: 'photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/photospicker(ispresented:selection:maxselectioncount:selectionbehavior:matching:preferreditemencoding:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/photospicker(ispresented:selection:maxselectioncount:selectionbehavior:matching:preferreditemencoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/photospicker%28ispresented%3Aselection%3Amaxselectioncount%3Aselectionbehavior%3Amatching%3Apreferreditemencoding%3A%29.json'
content_hash: 'sha256:8a5f21027c357b27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)

<sub>Instance Method</sub>

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func photosPicker(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int? = nil, selectionBehavior: PhotosPickerSelectionBehavior = .default, matching filter: PHPickerFilter? = nil, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic) -> some View

```

## Parameters

- `isPresented` — The binding to whether the Photos picker should be shown.

- `selection` — All items being shown and selected in the Photos picker.

- `maxSelectionCount` — The maximum number of items that can be selected. Default is `nil`. Setting it to `nil` means maximum supported by the system.

- `selectionBehavior` — The selection behavior of the Photos picker. Default is `.default`.

- `filter` — Types of items that can be shown. Default is `nil`. Setting it to `nil` means all supported types can be shown.

- `preferredItemEncoding` — The encoding disambiguation policy of selected items. Default is `.automatic`. Setting it to `.automatic` means the best encoding determined by the system will be used.

## Discussion

The user explicitly grants access only to items they choose, so photo library access authorization is not needed.

## See Also

### Selecting photos

- [PhotosPicker](../../photosui/photospicker.md) — A view that displays a Photos picker for choosing assets from the photo library.
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:)](<photospicker(ispresented_selection_matching_preferreditemencoding_).md>) — Presents a Photos picker that selects a `PhotosPickerItem`.
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)](<photospicker(ispresented_selection_matching_preferreditemencoding_photolibrary_).md>) — Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_).md>) — Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library.
- [photosPickerAccessoryVisibility(_:edges:)](<photospickeraccessoryvisibility(__edges_).md>) — Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar.
- [photosPickerDisabledCapabilities(_:)](<photospickerdisabledcapabilities(__).md>) — Disables capabilities of the Photos picker.
- [photosPickerSearchText(_:)](<photospickersearchtext(__).md>) — Sets search text of the Photos picker. _(beta)_
- [photosPickerStyle(_:)](<photospickerstyle(__).md>) — Sets the mode of the Photos picker.
- [photosPickerMetadataOptions(_:)](<photospickermetadataoptions(__).md>) — Sets metadata options for the Photos picker. _(beta)_
- [photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)](<photossharedalbumcreationsheet(ispresented_defaulttitle_defaultsharingpolicy_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to create a new shared album. _(beta)_
- [photosSharedAlbumCustomizationSheet(isPresented:albumIdentifier:photoLibrary:onCompletion:)](<photossharedalbumcustomizationsheet(ispresented_albumidentifier_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to customize a specified shared album. _(beta)_
- [photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](<photossharedalbumpostingsheet(ispresented_items_defaultalbumidentifier_photolibrary_completion_).md>) — Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album. _(beta)_
