---
title: PHPickerMode
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickermode-swift.struct
source_url: 'https://developer.apple.com/documentation/photosui/phpickermode-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickermode-swift.struct.json'
content_hash: 'sha256:1a15c45370335b32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHPickerMode

<sub>Structure</sub>

Layout options that determine how the picker orders photos visually.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct PHPickerMode
```

## Overview

This structure defines the possible options for the photos picker configuration ([PHPickerConfiguration](phpickerconfiguration-c.class.md)) property [mode](phpickerconfiguration-swift.struct/mode.md). The option you choose determines the direction that its assets scroll in the view. In addition, the linear scrolling behavior of [compact](phpickermode-swift.struct/compact.md) mode offers the best user experience in a space-constrained layout.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Laying out photos

- [compact](phpickermode-swift.struct/compact.md) — A linear layout that’s conducive to a smaller area onscreen.
- [default](phpickermode-swift.struct/default.md) — A grid-based layout that’s conducive to a larger area onscreen.

## See Also

### Customizing picker appearance and behavior

- [mode](phpickerconfiguration-swift.struct/mode.md) — A layout type for the photos in the picker’s view.
- [disabledCapabilities](phpickerconfiguration-swift.struct/disabledcapabilities.md) — The aspects of a photo picker’s default appearance that your app can disable.
- [PHPickerCapabilities](phpickercapabilities.md) — Options that customize the look and behavior of the photos picker.
- [edgesWithoutContentMargins](phpickerconfiguration-swift.struct/edgeswithoutcontentmargins.md) — The portions of a photo picker’s perimeter that are borderless.
- [Update](phpickerconfiguration-swift.struct/update.md) — An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.
