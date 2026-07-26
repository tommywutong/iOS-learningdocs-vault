---
title: selectionLimit
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfiguration-swift.struct/selectionlimit
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/selectionlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfiguration-swift.struct/selectionlimit.json'
content_hash: 'sha256:b36c2f8d6eabbc32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerConfiguration](../phpickerconfiguration-swift.struct.md)

# selectionLimit

<sub>Instance Property</sub>

The maximum number of selections the user can make.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var selectionLimit: Int
```

## Discussion

The default value is `1`. Setting the value to `0` sets the selection limit to the maximum that the system supports.

## See Also

### Setting the selection limit

- [selection](selection-swift.property.md) — The selection behavior for the picker.
- [PHPickerConfigurationSelection](../phpickerconfigurationselection.md) — Options that represent differing selection behavior.
- [Selection](selection-swift.enum.md) — Options that represent differing selection behavior.
