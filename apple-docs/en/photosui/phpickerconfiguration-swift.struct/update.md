---
title: PHPickerConfiguration.Update
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfiguration-swift.struct/update
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/update'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfiguration-swift.struct/update.json'
content_hash: 'sha256:1f83e3f4bc807455'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerConfiguration](../phpickerconfiguration-swift.struct.md)

# PHPickerConfiguration.Update

<sub>Structure</sub>

An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct Update
```

## Overview

While a photos picker is visible, you can use an instance of this structure to change its [edgesWithoutContentMargins](edgeswithoutcontentmargins.md) or [selectionLimit](selectionlimit.md) properties. To do that, create and configure an instance of this object and pass it to the [PHPickerViewController](../phpickerviewcontroller.md) method [updatePicker(using:)](<../phpickerviewcontroller/updatepicker(using_).md>).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating an update object

- [init()](<update/init().md>)

### Adjusting selection limits

- [selectionLimit](update/selectionlimit.md) — The maximum number of selections the user can make.

### Adjusting content margins

- [edgesWithoutContentMargins](update/edgeswithoutcontentmargins.md) — The portions of a photo picker’s permiter that are borderless.

### Instance Properties

- [searchText](update/searchtext.md) — The search text for the picker. Default is `nil`.

## See Also

### Customizing picker appearance and behavior

- [mode](mode.md) — A layout type for the photos in the picker’s view.
- [PHPickerMode](../phpickermode-swift.struct.md) — Layout options that determine how the picker orders photos visually.
- [disabledCapabilities](disabledcapabilities.md) — The aspects of a photo picker’s default appearance that your app can disable.
- [PHPickerCapabilities](../phpickercapabilities.md) — Options that customize the look and behavior of the photos picker.
- [edgesWithoutContentMargins](edgeswithoutcontentmargins.md) — The portions of a photo picker’s perimeter that are borderless.
