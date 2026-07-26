---
title: 'photosPickerAccessoryVisibility(_:edges:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/photospickeraccessoryvisibility(_:edges:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/photospickeraccessoryvisibility(_:edges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/photospickeraccessoryvisibility%28_%3Aedges%3A%29.json'
content_hash: 'sha256:a6f4790f0b396201'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# photosPickerAccessoryVisibility(_:edges:)

<sub>Instance Method</sub>

Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func photosPickerAccessoryVisibility(_ visibility: Visibility, edges: Edge.Set = .all) -> some View

```

## Parameters

- `edges` — The accessory visibility to apply.

- `edges` — One or more of the available edges.

## Return Value

A Photos picker with the specified accessory visibility.

## See Also

### Selecting photos

- [PhotosPicker](../../photosui/photospicker.md) — A view that displays a Photos picker for choosing assets from the photo library.
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:)](<photospicker(ispresented_selection_matching_preferreditemencoding_).md>) — Presents a Photos picker that selects a `PhotosPickerItem`.
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)](<photospicker(ispresented_selection_matching_preferreditemencoding_photolibrary_).md>) — Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)](<photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_).md>) — Presents a Photos picker that selects a collection of `PhotosPickerItem`.
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_).md>) — Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library.
- [photosPickerDisabledCapabilities(_:)](<photospickerdisabledcapabilities(__).md>) — Disables capabilities of the Photos picker.
- [photosPickerSearchText(_:)](<photospickersearchtext(__).md>) — Sets search text of the Photos picker. _(beta)_
- [photosPickerStyle(_:)](<photospickerstyle(__).md>) — Sets the mode of the Photos picker.
- [photosPickerMetadataOptions(_:)](<photospickermetadataoptions(__).md>) — Sets metadata options for the Photos picker. _(beta)_
- [photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)](<photossharedalbumcreationsheet(ispresented_defaulttitle_defaultsharingpolicy_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to create a new shared album. _(beta)_
- [photosSharedAlbumCustomizationSheet(isPresented:albumIdentifier:photoLibrary:onCompletion:)](<photossharedalbumcustomizationsheet(ispresented_albumidentifier_photolibrary_oncompletion_).md>) — Presents a view for allowing the user to customize a specified shared album. _(beta)_
- [photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](<photossharedalbumpostingsheet(ispresented_items_defaultalbumidentifier_photolibrary_completion_).md>) — Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album. _(beta)_
