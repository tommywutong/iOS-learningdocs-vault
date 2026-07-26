---
title: PhotosPicker
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/photospicker
source_url: 'https://developer.apple.com/documentation/photosui/photospicker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/photospicker.json'
content_hash: 'sha256:486870f21e3d3bb5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PhotosPicker

<sub>Structure</sub>

A view that displays a Photos picker for choosing assets from the photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct PhotosPicker<Label> where Label : View
```

## Overview

Use the Photos picker view to browse and select images and videos from the photo library. The view contains methods for single selection and multiple selection. For example, the following code displays a button that — when pressed — shows a picker in multiple selection mode.

```swift
import SwiftUI
import PhotosUI

struct PhotosSelector: View {
    @State var selectedItems: [PhotosPickerItem] = []

    var body: some View {
        PhotosPicker(selection: $selectedItems,
                     matching: .images) {
            Text("Select Multiple Photos")
        }
    }
}
```

When displaying the picker, you can use [PHPickerFilter](phpickerfilter-swift.struct.md) options to customize what it displays. For example, the following code displays [images](phpickerfilter-swift.struct/images.md) and excludes [screenshots](phpickerfilter-swift.struct/screenshots.md).

```swift
PhotosPicker(selection: $selectedItems,
             matching: .any(of: [.images, .not(.screenshots)])) {
    Text("Select Photos")
}
```

The selection results you get are placeholder objects. A [PhotosPickerItem](photospickeritem.md) conforms to [Transferable](../coretransferable/transferable.md), and allows you to load a representation you request. To load a SwiftUI [Image](../swiftui/image.md) and track progress, use [loadTransferable(type:completionHandler:)](<photospickeritem/loadtransferable(type_completionhandler_).md>).

```swift
func loadTransferable(from imageSelection: PhotosPickerItem) -> Progress {
    return imageSelection.loadTransferable(type: Image.self) { result in
        DispatchQueue.main.async {
            guard imageSelection == self.imageSelection else { return }
            switch result {
            case .success(let image?):
                // Handle the success case with the image.
            case .success(nil):
                // Handle the success case with an empty value.
            case .failure(let error):
                // Handle the failure case with the provided error.
            }
        }
    }
}
```

A failure can occur when the system attempts to retrieve the data. For example, if the picker tries to download data from iCloud Photos without a network connection.

> [!important] Important
> [Image](../swiftui/image.md) only supports `PNG` file types through its [Transferable](../coretransferable/transferable.md) conformance, so you need to create a custom `Transferable` model to support other image types. See [Bringing Photos picker to your SwiftUI app](../photokit/bringing-photos-picker-to-your-swiftui-app.md) to learn more.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a picker

- [init(selection:matching:preferredItemEncoding:label:)](<photospicker/init(selection_matching_preferreditemencoding_label_).md>) — Creates a picker that selects an item and optionally configures the types of items to show, item encoding, and label behavior.
- [init(selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:label:)](<photospicker/init(selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_label_).md>) — Creates a picker that selects a collection of items and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(selection:matching:preferredItemEncoding:photoLibrary:label:)](<photospicker/init(selection_matching_preferreditemencoding_photolibrary_label_).md>) — Creates a picker that selects an item from the photo library you specify and optionally configures the types of items to show, item encoding, and label behavior.
- [init(selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:label:)](<photospicker/init(selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_label_).md>) — Creates a picker that selects a collection of items from the photo library you specify and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.

### Creating a picker with a title

- [init(_:selection:matching:preferredItemEncoding:)](<photospicker/init(__selection_matching_preferreditemencoding_)-7jbef.md>) — Creates a picker with a title key and selection, and optionally configures the types of items to show and item encoding behavior.
- [init(_:selection:matching:preferredItemEncoding:)](<photospicker/init(__selection_matching_preferreditemencoding_)-48f7l.md>) — Creates a picker with a title and selection, and optionally configures the types of items to show and item encoding behavior.
- [init(_:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)](<photospicker/init(__selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_)-8ac23.md>) — Creates a picker with a title key and selection, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(_:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)](<photospicker/init(__selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_)-6m11r.md>) — Creates a picker with a title and selection, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(_:selection:matching:preferredItemEncoding:photoLibrary:)](<photospicker/init(__selection_matching_preferreditemencoding_photolibrary_)-bu7c.md>) — Creates a picker with a title key and selection from the photo library you specify, and optionally configures the types of items to show, item encoding, and label behavior.
- [init(_:selection:matching:preferredItemEncoding:photoLibrary:)](<photospicker/init(__selection_matching_preferreditemencoding_photolibrary_)-6bm2n.md>) — Creates a picker with a title and selection from the photo library you specify, and optionally configures the types of items to show, item encoding, and label behavior.
- [init(_:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<photospicker/init(__selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_)-5tpfd.md>) — Creates a picker with a title key and selection from the photo library you specify, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(_:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<photospicker/init(__selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_)-6fwsc.md>) — Creates a picker with a title and selection from the photo library you specify, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.

## See Also

### Photos picker for SwiftUI

- [Bringing Photos picker to your SwiftUI app](../photokit/bringing-photos-picker-to-your-swiftui-app.md) — Select media assets by using a Photos picker view that SwiftUI provides.
- [Implementing an inline Photos picker](../photokit/implementing-an-inline-photos-picker.md) — Embed a system-provided, half-height Photos picker into your app’s view.
- [PhotosPickerItem](photospickeritem.md) — A type that represents an item you use with a Photos picker.
- [PhotosPickerSelectionBehavior](photospickerselectionbehavior.md) — A type that describes how the Photos picker handles user selection.
- [PhotosPickerStyle](photospickerstyle.md)
