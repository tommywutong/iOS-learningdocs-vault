---
title: videoMaximumDuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/videomaximumduration
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/videomaximumduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/videomaximumduration.json'
content_hash: 'sha256:1ffe86ce857ffb25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# videoMaximumDuration

<sub>Instance Property</sub>

The maximum duration, in seconds, for a video recording.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var videoMaximumDuration: TimeInterval { get set }
```

## Discussion

The default value for this property is 10 minutes (600 seconds). When a user taps the Share button to send a movie to MMS, MobileMe, YouTube, or another destination, an appropriate duration limit and an appropriate video quality are enforced.

This property is available only if the [mediaTypes](mediatypes.md) property’s value array includes the `kUTTypeMovie` media type.

## See Also

### Related Documentation

- [+ availableMediaTypesForSourceType:](<availablemediatypes(for_).md>) — Retrieves the available media types for the specified source type.
- [+ isSourceTypeAvailable:](<issourcetypeavailable(__).md>) — Queries whether the device supports picking media using the specified source type.

### Configuring the video capture options

- [videoQuality](videoquality.md) — The video recording and transcoding quality.
- [QualityType](qualitytype.md) — Constants that describe video quality settings for movies that are recorded with the built-in camera, or that are transcoded when they’re displayed in the image picker.
