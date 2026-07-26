---
title: AVCaptureExternalDisplayConfigurator
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfigurator
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfigurator.json'
content_hash: 'sha256:bda452d588d2c900'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureExternalDisplayConfigurator

<sub>Class</sub>

A configurator class allowing you to configure properties of an external display to match the camera’s active video format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureExternalDisplayConfigurator
```

## Overview

An [AVCaptureExternalDisplayConfigurator](avcaptureexternaldisplayconfigurator.md) allows you to configure a connected external display to output a clean feed using a `CALayer`. Using the configurator, you can opt into automatic adjustment of the external display’s color space and / or frame rate to match your device’s capture configuration. These adjustments are only applied to the external display, not to the device.

> [!note] Note
> Not all displays support the same configuration options as the device’s capture formats. Your adjustments to the external display are applied with utmost effort to accurately represent the capture device. When your capture device’s [activeFormat](avcapturedevice/activeformat.md) is unavailable on the external display, the configurator automatically chooses the closest available format.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Determining configuration support

- [shouldMatchFrameRateSupported](avcaptureexternaldisplayconfigurator/ismatchingframeratesupported.md) — Whether the external display supports matching frame rate to a capture device.
- [supportsPreferredResolution](avcaptureexternaldisplayconfigurator/ispreferredresolutionsupported.md) — Whether the external display supports configuration to your preferred resolution.
- [supportsBypassingColorSpaceConversion](avcaptureexternaldisplayconfigurator/isbypassingcolorspaceconversionsupported.md) — Whether the external display supports bypassing color space conversion.

### Creating an external display configurator

- [- initWithDevice:previewLayer:configuration:](<avcaptureexternaldisplayconfigurator/init(device_previewlayer_configuration_).md>) — An external display configurator instance that attempts to synchronize the preview layer configuration with the device capture configuration.

### Inspecting the configurator

- [activeExternalDisplayFrameRate](avcaptureexternaldisplayconfigurator/activeexternaldisplayframerate.md) — The currently configured frame rate on the external display that’s displaying the preview layer.
- [device](avcaptureexternaldisplayconfigurator/device.md) — The device for which the coordinator configures the preview layer.
- [active](avcaptureexternaldisplayconfigurator/isactive.md) — This property tells you whether the configurator is actively configuring the external display.
- [previewLayer](avcaptureexternaldisplayconfigurator/previewlayer.md) — The layer for which the configurator adjusts display properties to match the device’s state.

### Stopping configuration

- [- stop](<avcaptureexternaldisplayconfigurator/stop().md>) — Forces the external display configurator to asynchronously stop configuring the external display.

## See Also

### External display output

- [AVCaptureExternalDisplayConfiguration](avcaptureexternaldisplayconfiguration.md) — A class you use to specify a configuration to your external display configurator.
