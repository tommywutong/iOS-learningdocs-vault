---
title: AVCaptureExternalDisplayConfiguration
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfiguration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfiguration.json'
content_hash: 'sha256:2dbba4a9247b91a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureExternalDisplayConfiguration

<sub>Class</sub>

A class you use to specify a configuration to your external display configurator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureExternalDisplayConfiguration
```

## Overview

Using an [AVCaptureExternalDisplayConfiguration](avcaptureexternaldisplayconfiguration.md), you direct your [AVCaptureExternalDisplayConfigurator](avcaptureexternaldisplayconfigurator.md) how to configure an external display to match your device’s active video format.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Modifying the configuration

- [bypassColorSpaceConversion](avcaptureexternaldisplayconfiguration/bypasscolorspaceconversion.md) — A property indicating whether the color space of the configurator’s preview layer should be preserved on the output display by avoiding color space conversions.
- [preferredResolution](avcaptureexternaldisplayconfiguration/preferredresolution.md) — Your preferred external display resolution.
- [shouldMatchFrameRate](avcaptureexternaldisplayconfiguration/shouldmatchframerate.md) — A property indicating whether the frame rate of the external display should be configured to match the camera’s frame rate.

## See Also

### External display output

- [AVCaptureExternalDisplayConfigurator](avcaptureexternaldisplayconfigurator.md) — A configurator class allowing you to configure properties of an external display to match the camera’s active video format.
