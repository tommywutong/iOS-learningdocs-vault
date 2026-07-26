---
title: 'not(_:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phpickerfilter-swift.struct/not(_:)'
source_url: 'https://developer.apple.com/documentation/photosui/phpickerfilter-swift.struct/not(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerfilter-swift.struct/not%28_%3A%29.json'
content_hash: 'sha256:5cf7ac4b306330ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerFilter](../phpickerfilter-swift.struct.md)

# not(_:)

<sub>Type Method</sub>

Creates a new filter that excludes the filter you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static func not(_ filter: PHPickerFilter) -> PHPickerFilter
```

## Parameters

- `filter` — The filter to exclude from the new filter.

## Return Value

A new filter that excludes the filter you specify.

## See Also

### Creating Filters

- [playbackStyle(_:)](<playbackstyle(__).md>) — Creates a new filter by using the playback style you specify.
- [all(of:)](<all(of_).md>) — Creates a new filter that includes only the filters you specify.
