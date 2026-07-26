---
title: AVCaptureBracketedStillImageSettings
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturebracketedstillimagesettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebracketedstillimagesettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebracketedstillimagesettings.json'
content_hash: 'sha256:81a983ea386c44b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureBracketedStillImageSettings

<sub>Class</sub>

The abstract superclass for bracketed photo capture settings.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class AVCaptureBracketedStillImageSettings
```

## Overview

> [!note] Note
> The `AVCaptureBracketedStillImageSettings` class must not be instantiated directly. You should create instances of the `AVCaptureManualExposureBracketedStillImageSettings` and `AVCaptureAutoExposureBracketedStillImageSettings` classes as appropriate.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVCaptureAutoExposureBracketedStillImageSettings](avcaptureautoexposurebracketedstillimagesettings.md), [AVCaptureManualExposureBracketedStillImageSettings](avcapturemanualexposurebracketedstillimagesettings.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Bracketed settings types

- [AVCaptureAutoExposureBracketedStillImageSettings](avcaptureautoexposurebracketedstillimagesettings.md) — A configuration for defining bracketed photo captures in terms of bias relative to automatic exposure.
- [AVCaptureManualExposureBracketedStillImageSettings](avcapturemanualexposurebracketedstillimagesettings.md) — A configuration for defining bracketed photo captures in terms of specific exposure and ISO values.
