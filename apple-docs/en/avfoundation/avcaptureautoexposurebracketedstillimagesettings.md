---
title: AVCaptureAutoExposureBracketedStillImageSettings
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings.json'
content_hash: 'sha256:d57037ff1c5667e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureAutoExposureBracketedStillImageSettings

<sub>Class</sub>

A configuration for defining bracketed photo captures in terms of bias relative to automatic exposure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class AVCaptureAutoExposureBracketedStillImageSettings
```

## Overview

An [AVCaptureAutoExposureBracketedStillImageSettings](avcaptureautoexposurebracketedstillimagesettings.md) instance defines the exposure target bias setting that should be applied to one image in a bracket. An array of `AVCaptureAutoExposureBracketedStillImageSettings` objects is passed to `captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:` to specify the bracketing.

The minimum and maximum exposure target bias are properties of the [AVCaptureDevice](avcapturedevice.md) instance supplying data to an [AVCaptureStillImageOutput](avcapturestillimageoutput.md) instance. If you wish to leave [exposureTargetBias](avcaptureautoexposurebracketedstillimagesettings/exposuretargetbias.md) unchanged for this bracketed still image, you may pass the value `AVCaptureExposureTargetBiasCurrent`.

## Relationships

- **Inherits From**: [AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an auto exposure settings instance

- [+ autoExposureSettingsWithExposureTargetBias:](<avcaptureautoexposurebracketedstillimagesettings/autoexposuresettings(exposuretargetbias_).md>) — Creates an `AVCaptureAutoExposureBracketedStillImageSettings` using the specified exposure target bias.

### Getting the exposure target bias

- [exposureTargetBias](avcaptureautoexposurebracketedstillimagesettings/exposuretargetbias.md) — The exposure bias for the auto exposure bracketed settings

## See Also

### Bracketed settings types

- [AVCaptureManualExposureBracketedStillImageSettings](avcapturemanualexposurebracketedstillimagesettings.md) — A configuration for defining bracketed photo captures in terms of specific exposure and ISO values.
- [AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md) — The abstract superclass for bracketed photo capture settings.
