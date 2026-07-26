---
title: speakScreenStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/speakscreenstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/speakscreenstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/speakscreenstatusdidchangenotification.json'
content_hash: 'sha256:8ea6870916dcfd29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# speakScreenStatusDidChangeNotification

<sub>Type Property</sub>

A notification that UIKit posts when the system’s Speak Screen setting changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let speakScreenStatusDidChangeNotification: NSNotification.Name
```

## Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### Audio and speech

- [UIAccessibilityMonoAudioStatusDidChangeNotification](monoaudiostatusdidchangenotification.md) — A notification that UIKit posts when system audio changes from stereo to mono.
- [UIAccessibilitySpeakSelectionStatusDidChangeNotification](speakselectionstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Speak Selection setting changes.
- [UIAccessibilityHearingDevicePairedEarDidChangeNotification](hearingdevicepairedeardidchangenotification.md) — A notification that UIKit posts when there’s a change to the currently paired hearing devices.
