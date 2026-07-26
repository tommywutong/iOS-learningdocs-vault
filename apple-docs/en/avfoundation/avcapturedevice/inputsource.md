---
title: AVCaptureDevice.InputSource
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/inputsource
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/inputsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/inputsource.json'
content_hash: 'sha256:ad404a9ee8abe7be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.InputSource

<sub>Class</sub>

A distinct input source on a capture device.

<sub>macOS</sub>

```swift
class InputSource
```

## Overview

A capture device may optionally present an array of input sources that represent distinct mutually exclusive inputs to the device. For example, an audio capture device might have ADAT optical and analog input sources; a video capture device might have an HDMI or component input source.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Accessing properties

- [inputSourceID](inputsource/inputsourceid.md) — An identifier for an input source.
- [localizedName](inputsource/localizedname.md) — A localized, human-readable name for the input source.

## See Also

### Configuring input sources

- [inputSources](inputsources.md) — An array of input sources that the device supports.
- [activeInputSource](activeinputsource.md) — The currently active input source of the device.
