---
title: AVCaptureInput.Port
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureinput/port
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureinput/port'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureinput/port.json'
content_hash: 'sha256:92eb077725038b3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureInput](../avcaptureinput.md)

# AVCaptureInput.Port

<sub>Class</sub>

An object that represents a stream of data that a capture input provides.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class Port
```

## Overview

Instances of [AVCaptureInput](../avcaptureinput.md) have one or more input ports, one for each data stream they can produce. For example, an [AVCaptureDeviceInput](../avcapturedeviceinput.md) object presenting one video data stream has one port.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting an input port

- [enabled](port/isenabled.md) — A Boolean value that indicates whether the port is in an enabled state.
- [mediaType](port/mediatype.md) — The media type of the port.
- [formatDescription](port/formatdescription.md) — A description of the port format.
- [sourceDeviceType](port/sourcedevicetype.md) — The device type of the source camera that provides data to the port.
- [sourceDevicePosition](port/sourcedeviceposition.md) — The position of the source device providing input through this port.
- [clock](port/clock.md) — An object that represents the capture device’s clock.

### Observing format changes

- [AVCaptureInputPortFormatDescriptionDidChangeNotification](port/formatdescriptiondidchangenotification.md) — A notification the system posts when the capture input port’s format description changes.

### Accessing the input

- [input](port/input.md) — The input object that owns the port.

## See Also

### Accessing ports

- [ports](ports.md) — The ports available on a capture input.
