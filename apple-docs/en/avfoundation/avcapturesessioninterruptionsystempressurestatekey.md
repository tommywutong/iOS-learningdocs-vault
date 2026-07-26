---
title: AVCaptureSessionInterruptionSystemPressureStateKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesessioninterruptionsystempressurestatekey
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionsystempressurestatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesessioninterruptionsystempressurestatekey.json'
content_hash: 'sha256:374504b94b21a0b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSessionInterruptionSystemPressureStateKey

<sub>Global Variable</sub>

A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
let AVCaptureSessionInterruptionSystemPressureStateKey: String
```

## Discussion

If an interruption occurs and the value of [AVCaptureSessionInterruptionReasonKey](avcapturesessioninterruptionreasonkey.md) equals [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableDueToSystemPressure](avcapturesession/interruptionreason/videodevicenotavailableduetosystempressure.md), the [userInfo](../foundation/notification/userinfo.md) dictionary for the notification contains this key and a corresponding [SystemPressureState](avcapturedevice/systempressurestate-swift.class.md) value.

## See Also

### Monitoring system pressure

- [systemPressureState](avcapturedevice/systempressurestate-swift.property.md) — A value that indicates the capture device’s current system pressure state.
- [SystemPressureState](avcapturedevice/systempressurestate-swift.class.md) — An object that provides information about OS and hardware status affecting capture system performance and availability.
