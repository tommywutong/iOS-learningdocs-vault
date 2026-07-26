---
title: AVCaptureDevice.SystemPressureState
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class.json'
content_hash: 'sha256:f6aa3ba632200af1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.SystemPressureState

<sub>Class</sub>

An object that provides information about OS and hardware status affecting capture system performance and availability.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class SystemPressureState
```

## Overview

The performance and availability of the camera capture system on an iOS device is subject to several external factors, such as power usage and device temperature. If during a capture session the total system pressure reaches excessive levels, the capture system automatically shuts down, causing a session interruption (see [AVCaptureSessionWasInterruptedNotification](../avcapturesession/wasinterruptednotification.md)). Under less heavy pressure, the system may automatically reduce capture quality.

Key-value observe the capture device’s [systemPressureState](systempressurestate-swift.property.md) property to monitor its state, and take action to reduce the performance impact of your capture session when system pressure increases—for example, by reducing the capture frame rate.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Overall level

- [level](systempressurestate-swift.class/level-swift.property.md) — The overall level of performance constraints on the capture system.
- [Level](systempressurestate-swift.class/level-swift.struct.md) — A structure that defines system pressure state levels.

### Contributing factors

- [factors](systempressurestate-swift.class/factors-swift.property.md) — The set of underlying causes for the system pressure level.
- [Factors](systempressurestate-swift.class/factors-swift.struct.md) — A structure that defines the factors affecting capture system performance.

## See Also

### Monitoring system pressure

- [systemPressureState](systempressurestate-swift.property.md) — A value that indicates the capture device’s current system pressure state.
- [AVCaptureSessionInterruptionSystemPressureStateKey](../avcapturesessioninterruptionsystempressurestatekey.md) — A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
