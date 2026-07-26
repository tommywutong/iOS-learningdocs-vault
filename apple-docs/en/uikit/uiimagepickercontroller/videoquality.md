---
title: videoQuality
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/videoquality
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/videoquality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/videoquality.json'
content_hash: 'sha256:fd3b061f7d9930e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# videoQuality

<sub>Instance Property</sub>

The video recording and transcoding quality.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var videoQuality: UIImagePickerController.QualityType { get set }
```

## Discussion

The video quality setting specified by this property is used during video recording. It is also used whenever picking a recorded movie. Specifically, if the video quality setting is lower than the video quality of an existing movie, displaying that movie in the picker results in transcoding the movie to the lower quality.

The various video qualities are listed in the [QualityType](qualitytype.md) enumeration. The default value is [UIImagePickerControllerQualityTypeMedium](qualitytype/typemedium.md). To capture or transcode a movie using a video quality other than the default value, you must set the quality explicitly.

This property is available only if the [mediaTypes](mediatypes.md) property’s value array includes the `kUTTypeMovie` media type.

## See Also

### Related Documentation

- [+ availableMediaTypesForSourceType:](<availablemediatypes(for_).md>) — Retrieves the available media types for the specified source type.
- [+ isSourceTypeAvailable:](<issourcetypeavailable(__).md>) — Queries whether the device supports picking media using the specified source type.

### Configuring the video capture options

- [QualityType](qualitytype.md) — Constants that describe video quality settings for movies that are recorded with the built-in camera, or that are transcoded when they’re displayed in the image picker.
- [videoMaximumDuration](videomaximumduration.md) — The maximum duration, in seconds, for a video recording.
