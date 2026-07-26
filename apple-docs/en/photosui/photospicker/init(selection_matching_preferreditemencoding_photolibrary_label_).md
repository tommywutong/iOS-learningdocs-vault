---
title: 'init(selection:matching:preferredItemEncoding:photoLibrary:label:)'
framework: PhotosUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/photospicker/init(selection:matching:preferreditemencoding:photolibrary:label:)'
source_url: 'https://developer.apple.com/documentation/photosui/photospicker/init(selection:matching:preferreditemencoding:photolibrary:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/photospicker/init%28selection%3Amatching%3Apreferreditemencoding%3Aphotolibrary%3Alabel%3A%29.json'
content_hash: 'sha256:232cccc1530b82b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PhotosPicker](../photospicker.md)

# init(selection:matching:preferredItemEncoding:photoLibrary:label:)

<sub>Initializer</sub>

Creates a picker that selects an item from the photo library you specify and optionally configures the types of items to show, item encoding, and label behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@preconcurrency nonisolated init(selection: Binding<PhotosPickerItem?>, matching filter: PHPickerFilter? = nil, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic, photoLibrary: PHPhotoLibrary, @ViewBuilder label: @Sendable () -> Label)
```

## Parameters

- `selection` — The item the picker displays in a selected state.

- `filter` — The types of items that the picker shows.

- `preferredItemEncoding` — The encoding policy of the selection.

- `photoLibrary` — The photo library to select from.

- `label` — The view that describes the action of choosing an item.

## See Also

### Creating a picker

- [init(selection:matching:preferredItemEncoding:label:)](<init(selection_matching_preferreditemencoding_label_).md>) — Creates a picker that selects an item and optionally configures the types of items to show, item encoding, and label behavior.
- [init(selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:label:)](<init(selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_label_).md>) — Creates a picker that selects a collection of items and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:label:)](<init(selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_label_).md>) — Creates a picker that selects a collection of items from the photo library you specify and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
