---
title: UIImagePickerController.QualityType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/qualitytype
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/qualitytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/qualitytype.json'
content_hash: 'sha256:73f2eddcd802bc9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# UIImagePickerController.QualityType

<sub>Enumeration</sub>

Constants that describe video quality settings for movies that are recorded with the built-in camera, or that are transcoded when they’re displayed in the image picker.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum QualityType
```

## Overview

The constants in this enumeration are for use as values of the [videoQuality](videoquality.md) property.

The video quality setting applies to transcoding as well as to recording. Specifically, if the video quality setting is lower than the video quality of an existing movie, displaying that movie in the picker results in transcoding the movie to the lower quality.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIImagePickerControllerQualityTypeHigh](qualitytype/typehigh.md) — If recording, specifies that you want to use the highest-quality video recording supported for the active camera on the device.
- [UIImagePickerControllerQualityType640x480](qualitytype/type640x480.md) — If recording, specifies that you want to use VGA-quality video recording (pixel dimensions of 640x480).
- [UIImagePickerControllerQualityTypeMedium](qualitytype/typemedium.md) — If recording, specifies that you want to use medium-quality video recording.
- [UIImagePickerControllerQualityTypeLow](qualitytype/typelow.md) — If recording, specifies that you want to use low-quality video recording.
- [UIImagePickerControllerQualityTypeIFrame1280x720](qualitytype/typeiframe1280x720.md) — If recording, specifies that you want to use 1280x720 iFrame format.
- [UIImagePickerControllerQualityTypeIFrame960x540](qualitytype/typeiframe960x540.md) — If recording, specifies that you want to use 960x540 iFrame format.

### Initializers

- [init(rawValue:)](<qualitytype/init(rawvalue_).md>)

## See Also

### Configuring the video capture options

- [videoQuality](videoquality.md) — The video recording and transcoding quality.
- [videoMaximumDuration](videomaximumduration.md) — The maximum duration, in seconds, for a video recording.
