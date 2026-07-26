---
title: 'playbackStyle(_:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phpickerfilter-swift.struct/playbackstyle(_:)'
source_url: 'https://developer.apple.com/documentation/photosui/phpickerfilter-swift.struct/playbackstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerfilter-swift.struct/playbackstyle%28_%3A%29.json'
content_hash: 'sha256:fc2af5e39da57d50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerFilter](../phpickerfilter-swift.struct.md)

# playbackStyle(_:)

<sub>Type Method</sub>

Creates a new filter by using the playback style you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static func playbackStyle(_ playbackStyle: PHAsset.PlaybackStyle) -> PHPickerFilter
```

## Parameters

- `playbackStyle` — The asset playback style.

## Return Value

A new filter with the playback style you specify.

## See Also

### Creating Filters

- [all(of:)](<all(of_).md>) — Creates a new filter that includes only the filters you specify.
- [not(_:)](<not(__).md>) — Creates a new filter that excludes the filter you specify.
