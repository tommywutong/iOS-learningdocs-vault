---
title: bracketedSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotobracketsettings/bracketedsettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings/bracketedsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotobracketsettings/bracketedsettings.json'
content_hash: 'sha256:572a3882b0842947'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoBracketSettings](../avcapturephotobracketsettings.md)

# bracketedSettings

<sub>Instance Property</sub>

An array describing the number of and settings for images to produce in a bracketed capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var bracketedSettings: [AVCaptureBracketedStillImageSettings] { get }
```

## Discussion

This array is read-only. You provide this array of bracket settings when creating a settings object with the `init(format:rawPixelFormatType:bracketedSettings:)` initializer.

## See Also

### Working with bracketed settings

- [lensStabilizationEnabled](islensstabilizationenabled.md) — A Boolean value that specifies whether to stabilize the lens for the duration of the bracketed capture.
