---
title: 'all(of:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phpickerfilter-swift.struct/all(of:)'
source_url: 'https://developer.apple.com/documentation/photosui/phpickerfilter-swift.struct/all(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerfilter-swift.struct/all%28of%3A%29.json'
content_hash: 'sha256:ad52d26a78fb9513'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerFilter](../phpickerfilter-swift.struct.md)

# all(of:)

<sub>Type Method</sub>

Creates a new filter that includes only the filters you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static func all(of subfilters: [PHPickerFilter]) -> PHPickerFilter
```

## Parameters

- `subfilters` — The array of filters to include.

## Return Value

A new filter that contains the list of filters you specify.

## See Also

### Creating Filters

- [playbackStyle(_:)](<playbackstyle(__).md>) — Creates a new filter by using the playback style you specify.
- [not(_:)](<not(__).md>) — Creates a new filter that excludes the filter you specify.
