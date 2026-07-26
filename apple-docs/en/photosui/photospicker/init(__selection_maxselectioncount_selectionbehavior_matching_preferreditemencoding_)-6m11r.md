---
title: 'init(_:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)'
framework: PhotosUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/photospicker/init(_:selection:maxselectioncount:selectionbehavior:matching:preferreditemencoding:)-6m11r'
source_url: 'https://developer.apple.com/documentation/photosui/photospicker/init(_:selection:maxselectioncount:selectionbehavior:matching:preferreditemencoding:)-6m11r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/photospicker/init%28_%3Aselection%3Amaxselectioncount%3Aselectionbehavior%3Amatching%3Apreferreditemencoding%3A%29-6m11r.json'
content_hash: 'sha256:1d2bd155ce8c2d77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PhotosPicker](../photospicker.md)

# init(_:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)

<sub>Initializer</sub>

Creates a picker with a title and selection, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init<S>(_ title: S, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int? = nil, selectionBehavior: PhotosPickerSelectionBehavior = .default, matching filter: PHPickerFilter? = nil, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic) where S : StringProtocol
```

## Parameters

- `title` — A string that describes the purpose of showing the picker.

- `selection` — The items the picker displays in a selected state.

- `maxSelectionCount` — The maximum number of items available to select.

- `selectionBehavior` — The selection behavior of the picker.

- `filter` — The types of items that the picker shows.

- `preferredItemEncoding` — The encoding policy of the selection.

## See Also

### Creating a picker with a title

- [init(_:selection:matching:preferredItemEncoding:)](<init(__selection_matching_preferreditemencoding_)-7jbef.md>) — Creates a picker with a title key and selection, and optionally configures the types of items to show and item encoding behavior.
- [init(_:selection:matching:preferredItemEncoding:)](<init(__selection_matching_preferreditemencoding_)-48f7l.md>) — Creates a picker with a title and selection, and optionally configures the types of items to show and item encoding behavior.
- [init(_:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)](<init(__selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_)-8ac23.md>) — Creates a picker with a title key and selection, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(_:selection:matching:preferredItemEncoding:photoLibrary:)](<init(__selection_matching_preferreditemencoding_photolibrary_)-bu7c.md>) — Creates a picker with a title key and selection from the photo library you specify, and optionally configures the types of items to show, item encoding, and label behavior.
- [init(_:selection:matching:preferredItemEncoding:photoLibrary:)](<init(__selection_matching_preferreditemencoding_photolibrary_)-6bm2n.md>) — Creates a picker with a title and selection from the photo library you specify, and optionally configures the types of items to show, item encoding, and label behavior.
- [init(_:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<init(__selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_)-5tpfd.md>) — Creates a picker with a title key and selection from the photo library you specify, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(_:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<init(__selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_)-6fwsc.md>) — Creates a picker with a title and selection from the photo library you specify, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
