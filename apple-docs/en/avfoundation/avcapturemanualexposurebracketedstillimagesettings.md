---
title: AVCaptureManualExposureBracketedStillImageSettings
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings.json'
content_hash: 'sha256:cad1a8648effe4bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureManualExposureBracketedStillImageSettings

<sub>Class</sub>

A configuration for defining bracketed photo captures in terms of specific exposure and ISO values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class AVCaptureManualExposureBracketedStillImageSettings
```

## Overview

The `AVCaptureManualExposureBracketedStillImageSettings` class is a concrete subclass of the `AVCaptureBracketedStillImageSettings` class used when bracketing exposure duration and ISO.

An `AVCaptureManualExposureBracketedStillImageSettings` instance defines exposure duration and ISO settings that should be applied to one image in a bracket. An array of `AVCaptureManualExposureBracketedStillImageSettings` objects is passed to `captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:` to specify the bracketing.

You can query the minimum and maximum duration and ISO properties of the [AVCaptureDevice](avcapturedevice.md) instance supplying data to an [AVCaptureStillImageOutput](avcapturestillimageoutput.md) instance. If you wish to leave [exposureDuration](avcapturemanualexposurebracketedstillimagesettings/exposureduration.md) unchanged for this bracketed still image, you pass the value `AVCaptureExposureDurationCurrent` when creating the instance. To keep the ISO unchanged, you pass `AVCaptureISOCurrent` when creating the instance.

## Relationships

- **Inherits From**: [AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a manual bracketed exposure settings instance

- [+ manualExposureSettingsWithExposureDuration:ISO:](<avcapturemanualexposurebracketedstillimagesettings/manualexposuresettings(exposureduration_iso_).md>) — Creates a configuration of still image settings using the specified exposure duration and ISO.

### Getting manual exposure setting values

- [ISO](avcapturemanualexposurebracketedstillimagesettings/iso.md) — The ISO for the still image.
- [exposureDuration](avcapturemanualexposurebracketedstillimagesettings/exposureduration.md) — The exposure duration for the still image.

## See Also

### Bracketed settings types

- [AVCaptureAutoExposureBracketedStillImageSettings](avcaptureautoexposurebracketedstillimagesettings.md) — A configuration for defining bracketed photo captures in terms of bias relative to automatic exposure.
- [AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md) — The abstract superclass for bracketed photo capture settings.
