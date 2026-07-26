---
title: monoAudioStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/monoaudiostatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/monoaudiostatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/monoaudiostatusdidchangenotification.json'
content_hash: 'sha256:bbce0b0e74d61364'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# monoAudioStatusDidChangeNotification

<sub>Type Property</sub>

A notification that UIKit posts when system audio changes from stereo to mono.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let monoAudioStatusDidChangeNotification: NSNotification.Name
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### Audio and speech

- [UIAccessibilitySpeakScreenStatusDidChangeNotification](speakscreenstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Speak Screen setting changes.
- [UIAccessibilitySpeakSelectionStatusDidChangeNotification](speakselectionstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Speak Selection setting changes.
- [UIAccessibilityHearingDevicePairedEarDidChangeNotification](hearingdevicepairedeardidchangenotification.md) — A notification that UIKit posts when there’s a change to the currently paired hearing devices.
