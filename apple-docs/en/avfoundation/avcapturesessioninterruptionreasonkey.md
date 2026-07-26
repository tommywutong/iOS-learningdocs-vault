---
title: AVCaptureSessionInterruptionReasonKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesessioninterruptionreasonkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesessioninterruptionreasonkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesessioninterruptionreasonkey.json'
content_hash: 'sha256:7939c2fee59449ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSessionInterruptionReasonKey

<sub>Global Variable</sub>

Key to retrieve information about a capture interruption from a [AVCaptureSessionWasInterruptedNotification](avcapturesession/wasinterruptednotification.md) user info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
let AVCaptureSessionInterruptionReasonKey: String
```

## Discussion

The value for this key is an [NSNumber](../foundation/nsnumber.md) object containing a [InterruptionReason](avcapturesession/interruptionreason.md) value.

## See Also

### User-infomation keys

- [AVCaptureSessionInterruptionSystemPressureStateKey](avcapturesessioninterruptionsystempressurestatekey.md) — A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
- [InterruptionReason](avcapturesession/interruptionreason.md) — Constants identifying the reason a capture session was interrupted, found in an [AVCaptureSessionWasInterruptedNotification](avcapturesession/wasinterruptednotification.md) user info dictionary.
