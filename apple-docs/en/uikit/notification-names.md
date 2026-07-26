---
title: Notification names
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/notification-names
source_url: 'https://developer.apple.com/documentation/uikit/notification-names'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/notification-names.json'
content_hash: 'sha256:4bf564bd10a90714'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Accessibility for UIKit](accessibility-for-uikit.md)

# Notification names

<sub>API Collection</sub>

The names of notifications that the accessibility system generates.

## Topics

### UI changes

- [UIAccessibilityScreenChangedNotification](uiaccessibility/notification/screenchanged.md) — A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [UIAccessibilityLayoutChangedNotification](uiaccessibility/notification/layoutchanged.md) — A notification that an app posts when the layout of a screen changes.
- [UIAccessibilityPageScrolledNotification](uiaccessibility/notification/pagescrolled.md) — A notification that an app posts when a scroll action completes.
- [UIAccessibilitySwitchControlStatusDidChangeNotification](uiaccessibility/switchcontrolstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Switch Control setting changes.
- [UIAccessibilityElementFocusedNotification](uiaccessibility/elementfocusednotification.md) — A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [UIAccessibilityReduceTransparencyStatusDidChangeNotification](uiaccessibility/reducetransparencystatusdidchangenotification.md) — A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [UIAccessibilityButtonShapesEnabledStatusDidChangeNotification](uiaccessibility/buttonshapesenabledstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Button Shapes setting changes. _(deprecated)_

### VoiceOver

- [UIAccessibilityAnnouncementNotification](uiaccessibility/notification/announcement.md) — A notification that an app posts when it needs to convey an announcement to the assistive app.
- [UIAccessibilityVoiceOverStatusDidChangeNotification](uiaccessibility/voiceoverstatusdidchangenotification.md) — A notification that UIKit posts when VoiceOver starts or stops.
- [UIAccessibilityAnnouncementDidFinishNotification](uiaccessibility/announcementdidfinishnotification.md) — A notification that UIKit posts when the system finishes reading an announcement.
- [UIAccessibilityVoiceOverStatusChanged](uiaccessibilityvoiceoverstatuschanged.md) — A notification that UIKit posts when VoiceOver starts or stops. _(deprecated)_

### Text

- [UIAccessibilityBoldTextStatusDidChangeNotification](uiaccessibility/boldtextstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Bold Text setting changes.
- [UIAccessibilityClosedCaptioningStatusDidChangeNotification](uiaccessibility/closedcaptioningstatusdidchangenotification.md) — A notification that UIKit posts when the setting for Closed Captions + SDH changes.

### Colors

- [UIAccessibilityDarkerSystemColorsStatusDidChangeNotification](uiaccessibility/darkersystemcolorsstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Increase Contrast setting changes.
- [UIAccessibilityGrayscaleStatusDidChangeNotification](uiaccessibility/grayscalestatusdidchangenotification.md) — A notification that UIKit posts when the system’s Grayscale setting changes.
- [UIAccessibilityInvertColorsStatusDidChangeNotification](uiaccessibility/invertcolorsstatusdidchangenotification.md) — A notification that UIKit posts when the settings for inverted colors change.

### Assistive apps

- [UIAccessibilityAssistiveTouchStatusDidChangeNotification](uiaccessibility/assistivetouchstatusdidchangenotification.md) — A notification that indicates a change in the status of AssistiveTouch.
- [UIAccessibilityGuidedAccessStatusDidChangeNotification](uiaccessibility/guidedaccessstatusdidchangenotification.md) — A notification that indicates when a Guided Access session starts or ends.
- [UIAccessibilityPauseAssistiveTechnologyNotification](uiaccessibility/notification/pauseassistivetechnology.md) — A notification that pauses an assistive app’s operations temporarily.
- [UIAccessibilityResumeAssistiveTechnologyNotification](uiaccessibility/notification/resumeassistivetechnology.md) — A notification that resumes an assistive app’s operations temporarily.
- [AssistiveTechnologyIdentifier](uiaccessibility/assistivetechnologyidentifier.md) — Identifiers for assistive apps.

### Audio and speech

- [UIAccessibilityMonoAudioStatusDidChangeNotification](uiaccessibility/monoaudiostatusdidchangenotification.md) — A notification that UIKit posts when system audio changes from stereo to mono.
- [UIAccessibilitySpeakScreenStatusDidChangeNotification](uiaccessibility/speakscreenstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Speak Screen setting changes.
- [UIAccessibilitySpeakSelectionStatusDidChangeNotification](uiaccessibility/speakselectionstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Speak Selection setting changes.
- [UIAccessibilityHearingDevicePairedEarDidChangeNotification](uiaccessibility/hearingdevicepairedeardidchangenotification.md) — A notification that UIKit posts when there’s a change to the currently paired hearing devices.

### Motion

- [UIAccessibilityReduceMotionStatusDidChangeNotification](uiaccessibility/reducemotionstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Reduce Motion setting changes.
- [UIAccessibilityShakeToUndoDidChangeNotification](uiaccessibility/shaketoundodidchangenotification.md) — A notification that UIKit posts when the system’s Shake to Undo setting changes.

## See Also

### Notifications

- [Notification dictionary keys](notification-dictionary-keys.md) — Handle notifications with keys in the user info dictionary.
- [UIAccessibilityPostNotification](<uiaccessibility/post(notification_argument_).md>) — Posts a notification to assistive apps.
