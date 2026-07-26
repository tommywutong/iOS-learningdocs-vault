---
title: PHPickerFilter
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 13.0+, visionOS, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerfilter-swift.struct
source_url: 'https://developer.apple.com/documentation/photosui/phpickerfilter-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerfilter-swift.struct.json'
content_hash: 'sha256:e13a158bf96c990d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHPickerFilter

<sub>Structure</sub>

A type that defines the filter to apply to the photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct PHPickerFilter
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Filters

- [playbackStyle(_:)](<phpickerfilter-swift.struct/playbackstyle(__).md>) — Creates a new filter by using the playback style you specify.
- [all(of:)](<phpickerfilter-swift.struct/all(of_).md>) — Creates a new filter that includes only the filters you specify.
- [not(_:)](<phpickerfilter-swift.struct/not(__).md>) — Creates a new filter that excludes the filter you specify.

### Getting Filter Types

- [bursts](phpickerfilter-swift.struct/bursts.md) — A filter that represents assets with multiple high-speed photos.
- [cinematicVideos](phpickerfilter-swift.struct/cinematicvideos.md) — A filter that represents videos with a shallow depth of field and focus transitions.
- [depthEffectPhotos](phpickerfilter-swift.struct/deptheffectphotos.md) — A filter that represents photos with depth information.
- [images](phpickerfilter-swift.struct/images.md) — The filter for images.
- [livePhotos](phpickerfilter-swift.struct/livephotos.md) — The filter for live photos.
- [panoramas](phpickerfilter-swift.struct/panoramas.md) — A filter that represents panorama photos.
- [screenRecordings](phpickerfilter-swift.struct/screenrecordings.md) — A filter that represents screen recordings.
- [screenshots](phpickerfilter-swift.struct/screenshots.md) — A filter that represents screenshots.
- [slomoVideos](phpickerfilter-swift.struct/slomovideos.md) — A filter that represents slow-motion videos.
- [timelapseVideos](phpickerfilter-swift.struct/timelapsevideos.md) — A filter that represents time-lapse videos.
- [videos](phpickerfilter-swift.struct/videos.md) — The filter for videos.
- [any(of:)](<phpickerfilter-swift.struct/any(of_).md>) — Returns a new filter formed by OR-ing the filters in a given array.

### Type Properties

- [spatialMedia](phpickerfilter-swift.struct/spatialmedia.md)

## See Also

### Photos picker for UIKit, AppKit

- [Selecting Photos and Videos in iOS](../photokit/selecting-photos-and-videos-in-ios.md) — Improve the user experience of finding and selecting assets by using the Photos picker.
- [PHPickerViewController](phpickerviewcontroller.md) — A view controller that provides the user interface for choosing assets from the photo library.
- [PHPickerViewControllerDelegate](phpickerviewcontrollerdelegate-5yntc.md) — A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [PHPickerConfiguration](phpickerconfiguration-swift.struct.md) — An object that contains information about how to configure a picker view controller.
- [PHPickerResult](phpickerresult-swift.struct.md) — Types that represent a selected asset from the user’s photo library.
