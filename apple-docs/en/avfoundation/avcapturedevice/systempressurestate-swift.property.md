---
title: systemPressureState
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.property.json'
content_hash: 'sha256:d4f7c8a789804c89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# systemPressureState

<sub>Instance Property</sub>

A value that indicates the capture device’s current system pressure state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var systemPressureState: AVCaptureDevice.SystemPressureState { get }
```

## Discussion

This property indicates whether the capture device is currently in an elevated system pressure condition. When system pressure reaches a [AVCaptureSystemPressureLevelShutdown](systempressurestate-swift.class/level-swift.struct/shutdown.md) state, the capture device can’t continue to provide input, and the capture session becomes interrupted until the pressured state abates.

You can effectively mitigate system pressure by lowering the device’s [activeVideoMinFrameDuration](activevideominframeduration.md) in response to changes in the system pressure state. Implement frame rate throttling to bring system pressure down if your capture use case can tolerate a reduced frame rate.

## See Also

### Monitoring system pressure

- [SystemPressureState](systempressurestate-swift.class.md) — An object that provides information about OS and hardware status affecting capture system performance and availability.
- [AVCaptureSessionInterruptionSystemPressureStateKey](../avcapturesessioninterruptionsystempressurestatekey.md) — A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
