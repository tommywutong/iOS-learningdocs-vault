---
title: PhotosPickerItem
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/photospickeritem
source_url: 'https://developer.apple.com/documentation/photosui/photospickeritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/photospickeritem.json'
content_hash: 'sha256:72d340fcafc8326e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PhotosPickerItem

<sub>Structure</sub>

A type that represents an item you use with a Photos picker.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct PhotosPickerItem
```

## Overview

The selection results you get from [PhotosPicker](photospicker.md) are placeholder objects. A [PhotosPickerItem](photospickeritem.md) conforms to [Transferable](../coretransferable/transferable.md), and allows you to load the representation you request. To load a SwiftUI [Image](../swiftui/image.md) and track progress, use [loadTransferable(type:completionHandler:)](<photospickeritem/loadtransferable(type_completionhandler_).md>).

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
> [Image](../swiftui/image.md) only supports `PNG` file types through its [Transferable](../coretransferable/transferable.md) conformance. For more information on creating a custom `Transferable` model to support other image types, see [Bringing Photos picker to your SwiftUI app](../photokit/bringing-photos-picker-to-your-swiftui-app.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a picker item

- [init(itemIdentifier:)](<photospickeritem/init(itemidentifier_).md>) — Creates a picker item with the identifier you specify, and without any representation.

### Inspecting a picker item

- [itemIdentifier](photospickeritem/itemidentifier.md) — The local identifier of the item.
- [supportedContentTypes](photospickeritem/supportedcontenttypes.md) — The content types the item supports in order of the most preferred to the least.

### Getting an encoding policy

- [EncodingDisambiguationPolicy](photospickeritem/encodingdisambiguationpolicy.md) — A type that determines the encoding to use when multiple encodings are available, based on the content type.

### Loading the provider’s contents

- [loadTransferable(type:)](<photospickeritem/loadtransferable(type_).md>) — Attempts to load an instance of the type you specify from the item provider.
- [loadTransferable(type:completionHandler:)](<photospickeritem/loadtransferable(type_completionhandler_).md>) — Attempts to load an instance of the type you specify from the item provider, with a completion handler.

## See Also

### Photos picker for SwiftUI

- [Bringing Photos picker to your SwiftUI app](../photokit/bringing-photos-picker-to-your-swiftui-app.md) — Select media assets by using a Photos picker view that SwiftUI provides.
- [Implementing an inline Photos picker](../photokit/implementing-an-inline-photos-picker.md) — Embed a system-provided, half-height Photos picker into your app’s view.
- [PhotosPicker](photospicker.md) — A view that displays a Photos picker for choosing assets from the photo library.
- [PhotosPickerSelectionBehavior](photospickerselectionbehavior.md) — A type that describes how the Photos picker handles user selection.
- [PhotosPickerStyle](photospickerstyle.md)
