---
title: mode
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfiguration-swift.struct/mode
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/mode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfiguration-swift.struct/mode.json'
content_hash: 'sha256:99ca3abfdfbbe48a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerConfiguration](../phpickerconfiguration-swift.struct.md)

# mode

<sub>Instance Property</sub>

A layout type for the photos in the picker’s view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var mode: PHPickerMode
```

## Discussion

This property offers two ways that photos lay out in the picker:

- A linear mode ([compact](../phpickermode-swift.struct/compact.md)), in which photos form a line in a smaller area in the picker
- A two-dimensional mode ([default](../phpickermode-swift.struct/default.md)), in which photos form a grid in a larger area in the picker

## See Also

### Customizing picker appearance and behavior

- [PHPickerMode](../phpickermode-swift.struct.md) — Layout options that determine how the picker orders photos visually.
- [disabledCapabilities](disabledcapabilities.md) — The aspects of a photo picker’s default appearance that your app can disable.
- [PHPickerCapabilities](../phpickercapabilities.md) — Options that customize the look and behavior of the photos picker.
- [edgesWithoutContentMargins](edgeswithoutcontentmargins.md) — The portions of a photo picker’s perimeter that are borderless.
- [Update](update.md) — An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.
