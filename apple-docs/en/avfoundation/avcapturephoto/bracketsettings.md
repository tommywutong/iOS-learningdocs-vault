---
title: bracketSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/bracketsettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/bracketsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/bracketsettings.json'
content_hash: 'sha256:63d1a1c4aa3cfb02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# bracketSettings

<sub>Instance Property</sub>

The variations available for bracketed capture settings for this photo.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var bracketSettings: AVCaptureBracketedStillImageSettings? { get }
```

## Discussion

When you request a bracketed capture using the [AVCapturePhotoBracketSettings](../avcapturephotobracketsettings.md) class, you specify an array of [AVCaptureBracketedStillImageSettings](../avcapturebracketedstillimagesettings.md) objects indicating the capture setting variations (such as exposure compensation) to apply to each image in the bracket. This property indicates the settings associated with this particular photo, or `nil` if this photo is not part of a bracketed capture.

## See Also

### Examining bracketed capture information

- [sequenceCount](sequencecount.md) — The 1-based index of this photo in a bracketed capture sequence.
- [lensStabilizationStatus](lensstabilizationstatus.md) — Information about the use of lens stabilization during bracketed photo capture.
- [LensStabilizationStatus](../avcapturedevice/lensstabilizationstatus.md) — Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.
