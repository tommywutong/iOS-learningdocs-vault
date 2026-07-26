---
title: UIAccessibility
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility.json'
content_hash: 'sha256:8c876a63d51759b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibility

<sub>Structure</sub>

A namespace for accessibility symbols for UIKit apps.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct UIAccessibility
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### System notifications

- [UIAccessibilityAnnouncementDidFinishNotification](uiaccessibility/announcementdidfinishnotification.md) — A notification that UIKit posts when the system finishes reading an announcement.
- [UIAccessibilityElementFocusedNotification](uiaccessibility/elementfocusednotification.md) — A notification that UIKit posts when an assistive app focuses on an accessibility element.

### App notifications

- [UIAccessibilityPostNotification](<uiaccessibility/post(notification_argument_).md>) — Posts a notification to assistive apps.
- [Notification](uiaccessibility/notification.md) — An accessibility notification that an app can send.

### Notification keys

- [UIAccessibilityAnnouncementKeyStringValue](uiaccessibility/announcementstringvalueuserinfokey.md) — The text of the announcement.
- [UIAccessibilityAnnouncementKeyWasSuccessful](uiaccessibility/announcementwassuccessfuluserinfokey.md) — A Boolean value that indicates whether the announcement is successful.
- [UIAccessibilityFocusedElementKey](uiaccessibility/focusedelementuserinfokey.md) — The element currently in focus by the assistive app.
- [UIAccessibilityUnfocusedElementKey](uiaccessibility/unfocusedelementuserinfokey.md) — The element previously in focus by the assistive app.
- [UIAccessibilityAssistiveTechnologyKey](uiaccessibility/assistivetechnologyuserinfokey.md) — The identifier of the assistive app.

### VoiceOver

- [UIAccessibilityIsVoiceOverRunning](uiaccessibility/isvoiceoverrunning.md) — A Boolean value that indicates whether VoiceOver is in an enabled state.
- [UIAccessibilityVoiceOverStatusDidChangeNotification](uiaccessibility/voiceoverstatusdidchangenotification.md) — A notification that UIKit posts when VoiceOver starts or stops.

### Switch Control

- [UIAccessibilityIsSwitchControlRunning](uiaccessibility/isswitchcontrolrunning.md) — A Boolean value that indicates whether the Switch Control setting is in an enabled state.
- [UIAccessibilitySwitchControlStatusDidChangeNotification](uiaccessibility/switchcontrolstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Switch Control setting changes.

### AssistiveTouch

- [UIAccessibilityIsAssistiveTouchRunning](uiaccessibility/isassistivetouchrunning.md) — A Boolean value that indicates whether AssistiveTouch is in an enabled state.
- [UIAccessibilityAssistiveTouchStatusDidChangeNotification](uiaccessibility/assistivetouchstatusdidchangenotification.md) — A notification that indicates a change in the status of AssistiveTouch.

### Autoplay videos

- [UIAccessibilityIsVideoAutoplayEnabled](uiaccessibility/isvideoautoplayenabled.md) — A Boolean value that indicates whether the Auto-Play Video Previews setting is in an enabled state.
- [UIAccessibilityVideoAutoplayStatusDidChangeNotification](uiaccessibility/videoautoplaystatusdidchangenotification.md) — A notification that UIKit posts when the system’s Auto-Play Video Previews setting changes.

### Bold text

- [UIAccessibilityIsBoldTextEnabled](uiaccessibility/isboldtextenabled.md) — A Boolean value that indicates whether the Bold Text setting is in an enabled state.
- [UIAccessibilityBoldTextStatusDidChangeNotification](uiaccessibility/boldtextstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Bold Text setting changes.

### Button shapes

- [UIAccessibilityButtonShapesEnabled](uiaccessibility/buttonshapesenabled.md) — A Boolean value that indicates whether the Button Shapes setting is in an enabled state. _(deprecated)_
- [UIAccessibilityButtonShapesEnabledStatusDidChangeNotification](uiaccessibility/buttonshapesenabledstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Button Shapes setting changes. _(deprecated)_

### Closed captions

- [UIAccessibilityIsClosedCaptioningEnabled](uiaccessibility/isclosedcaptioningenabled.md) — A Boolean value that indicates whether the Closed Captions + SDH setting is in an enabled state.
- [UIAccessibilityClosedCaptioningStatusDidChangeNotification](uiaccessibility/closedcaptioningstatusdidchangenotification.md) — A notification that UIKit posts when the setting for Closed Captions + SDH changes.

### Cross-fade transitions

- [UIAccessibilityPrefersCrossFadeTransitions](uiaccessibility/preferscrossfadetransitions.md) — A Boolean value that indicates whether the Reduce Motion and the Prefer Cross-Fade Transitions settings are in an enabled state.
- [UIAccessibilityPrefersCrossFadeTransitionsStatusDidChangeNotification](uiaccessibility/preferscrossfadetransitionsstatusdidchange.md) — A notification that UIKit posts when the system’s Prefer Cross-Fade Transitions setting changes.

### Differentiate without color

- [UIAccessibilityShouldDifferentiateWithoutColor](uiaccessibility/shoulddifferentiatewithoutcolor.md) — A Boolean value that indicates whether the Differentiate Without Color setting is in an enabled state.
- [UIAccessibilityShouldDifferentiateWithoutColorDidChangeNotification](uiaccessibility/differentiatewithoutcolordidchangenotification.md) — A notification that UIKit posts when the system’s Differentiate Without Color setting changes.

### Grayscale

- [UIAccessibilityIsGrayscaleEnabled](uiaccessibility/isgrayscaleenabled.md) — A Boolean value that indicates whether the Color Filters and the Grayscale settings are in an enabled state.
- [UIAccessibilityGrayscaleStatusDidChangeNotification](uiaccessibility/grayscalestatusdidchangenotification.md) — A notification that UIKit posts when the system’s Grayscale setting changes.

### Guided Access

- [UIAccessibilityIsGuidedAccessEnabled](uiaccessibility/isguidedaccessenabled.md) — A Boolean value that indicates whether the Guided Access setting is in an enabled state.
- [UIAccessibilityGuidedAccessStatusDidChangeNotification](uiaccessibility/guidedaccessstatusdidchangenotification.md) — A notification that indicates when a Guided Access session starts or ends.
- [UIAccessibilityRequestGuidedAccessSession](<uiaccessibility/requestguidedaccesssession(enabled_completionhandler_).md>) — Transitions the app to or from Single App mode asynchronously.
- [UIGuidedAccessConfigureAccessibilityFeatures](<uiaccessibility/configureforguidedaccess(features_enabled_completionhandler_).md>) — Enables or disables the specified accessibility features while using Guided Access.
- [UIGuidedAccessRestrictionStateForIdentifier](<uiaccessibility/guidedaccessrestrictionstate(foridentifier_).md>) — Returns the restriction state for the specified guided access restriction.
- [GuidedAccessRestrictionState](uiaccessibility/guidedaccessrestrictionstate.md) — Constants that describe the state of a restriction, either allow or deny.
- [UIGuidedAccessErrorDomain](uiaccessibility/guidedaccesserrordomain.md) — A string that identifies the Guided Access error domain.
- [GuidedAccessError](uiaccessibility/guidedaccesserror.md) — A Guided Access error.

### Hearing devices

- [UIAccessibilityHearingDevicePairedEar](uiaccessibility/hearingdevicepairedear.md) — The current pairing status of Made for iPhone hearing devices.
- [UIAccessibilityHearingDevicePairedEarDidChangeNotification](uiaccessibility/hearingdevicepairedeardidchangenotification.md) — A notification that UIKit posts when there’s a change to the currently paired hearing devices.

### Increase contrast

- [UIAccessibilityDarkerSystemColorsEnabled](uiaccessibility/isdarkersystemcolorsenabled.md) — A Boolean value that indicates whether the Increase Contrast setting is in an enabled state.
- [UIAccessibilityDarkerSystemColorsStatusDidChangeNotification](uiaccessibility/darkersystemcolorsstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Increase Contrast setting changes.

### Invert colors

- [UIAccessibilityIsInvertColorsEnabled](uiaccessibility/isinvertcolorsenabled.md) — A Boolean value that indicates whether the Classic Invert setting is in an enabled state.
- [UIAccessibilityInvertColorsStatusDidChangeNotification](uiaccessibility/invertcolorsstatusdidchangenotification.md) — A notification that UIKit posts when the settings for inverted colors change.

### Mono audio

- [UIAccessibilityIsMonoAudioEnabled](uiaccessibility/ismonoaudioenabled.md) — A Boolean value that indicates whether the Mono Audio setting is in an enabled state.
- [UIAccessibilityMonoAudioStatusDidChangeNotification](uiaccessibility/monoaudiostatusdidchangenotification.md) — A notification that UIKit posts when system audio changes from stereo to mono.

### On and off labels

- [UIAccessibilityIsOnOffSwitchLabelsEnabled](uiaccessibility/isonoffswitchlabelsenabled.md) — A Boolean value that indicates whether the On/Off Labels setting is in an enabled state.
- [UIAccessibilityOnOffSwitchLabelsDidChangeNotification](uiaccessibility/onoffswitchlabelsdidchangenotification.md) — A notification that UIKit posts when the system’s On/Off Labels setting changes.

### Reduce motion

- [UIAccessibilityIsReduceMotionEnabled](uiaccessibility/isreducemotionenabled.md) — A Boolean value that indicates whether the Reduce Motion setting is in an enabled state.
- [UIAccessibilityReduceMotionStatusDidChangeNotification](uiaccessibility/reducemotionstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Reduce Motion setting changes.

### Reduce transparency

- [UIAccessibilityIsReduceTransparencyEnabled](uiaccessibility/isreducetransparencyenabled.md) — A Boolean value that indicates whether the Reduce Transparency setting is in an enabled state.
- [UIAccessibilityReduceTransparencyStatusDidChangeNotification](uiaccessibility/reducetransparencystatusdidchangenotification.md) — A notification that UIKit posts when the system’s Reduce Transparency setting changes.

### Shake to undo

- [UIAccessibilityIsShakeToUndoEnabled](uiaccessibility/isshaketoundoenabled.md) — A Boolean value that indicates whether the Shake to Undo setting is in an enabled state.
- [UIAccessibilityShakeToUndoDidChangeNotification](uiaccessibility/shaketoundodidchangenotification.md) — A notification that UIKit posts when the system’s Shake to Undo setting changes.

### Spoken content

- [UIAccessibilityIsSpeakScreenEnabled](uiaccessibility/isspeakscreenenabled.md) — A Boolean value that indicates whether the Speak Screen setting is in an enabled state.
- [UIAccessibilitySpeakScreenStatusDidChangeNotification](uiaccessibility/speakscreenstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Speak Screen setting changes.
- [UIAccessibilityIsSpeakSelectionEnabled](uiaccessibility/isspeakselectionenabled.md) — A Boolean value that indicates whether the Speak Selection setting is in an enabled state.
- [UIAccessibilitySpeakSelectionStatusDidChangeNotification](uiaccessibility/speakselectionstatusdidchangenotification.md) — A notification that UIKit posts when the system’s Speak Selection setting changes.

### Conversions

- [UIAccessibilityConvertPathToScreenCoordinates](<uiaccessibility/converttoscreencoordinates(__in_)-6dx4a.md>) — Converts the specified path object to screen coordinates and returns a new path object with the results.
- [UIAccessibilityConvertFrameToScreenCoordinates](<uiaccessibility/converttoscreencoordinates(__in_)-9ziiu.md>) — Converts the specified rectangle from view coordinates to screen coordinates.

### Convenience functions

- [UIAccessibilityFocusedElement](<uiaccessibility/focusedelement(using_).md>) — Returns the accessibility element that’s currently in focus by the specified assistive app.
- [UIAccessibilityRegisterGestureConflictWithZoom](<uiaccessibility/registergestureconflictwithzoom().md>) — Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [UIAccessibilityZoomFocusChanged](<uiaccessibility/zoomfocuschanged(zoomtype_toframe_in_).md>) — Notifies the system when the app’s focus changes to a new location.

### Constants

- [UIAccessibilityTraits](uiaccessibilitytraits.md) — Constants that describe how an accessibility element behaves.
- [AssistiveTechnologyIdentifier](uiaccessibility/assistivetechnologyidentifier.md) — Identifiers for assistive apps.
- [HearingDeviceEar](uiaccessibility/hearingdeviceear.md) — Constants that specify how a person is using a hearing device.
- [UIAccessibilityContainerType](uiaccessibilitycontainertype.md) — Constants that indicate the type of content in a data-based container.
- [UIAccessibilityNavigationStyle](uiaccessibilitynavigationstyle.md) — Constants that describe how to navigate an object’s elements with an assistive app.
- [UIAccessibilityScrollDirection](uiaccessibilityscrolldirection.md) — The direction of a scrolling action.
- [ZoomType](uiaccessibility/zoomtype.md) — The types of system Zoom that can be in effect.
- [DirectTouchOptions](uiaccessibility/directtouchoptions.md) — Constants that configure how VoiceOver produces audio for direct touch areas.

### Structures

- [AnnouncementDidFinishMessage](uiaccessibility/announcementdidfinishmessage.md)
- [AssistiveTouchStatusDidChangeMessage](uiaccessibility/assistivetouchstatusdidchangemessage.md)
- [BoldTextStatusDidChangeMessage](uiaccessibility/boldtextstatusdidchangemessage.md)
- [ButtonShapesEnabledStatusDidChangeMessage](uiaccessibility/buttonshapesenabledstatusdidchangemessage.md) _(deprecated)_
- [ClosedCaptioningStatusDidChangeMessage](uiaccessibility/closedcaptioningstatusdidchangemessage.md)
- [DarkerSystemColorsStatusDidChangeMessage](uiaccessibility/darkersystemcolorsstatusdidchangemessage.md)
- [ElementFocusedMessage](uiaccessibility/elementfocusedmessage.md)
- [GrayscaleStatusDidChangeMessage](uiaccessibility/grayscalestatusdidchangemessage.md)
- [GuidedAccessStatusDidChangeMessage](uiaccessibility/guidedaccessstatusdidchangemessage.md)
- [HearingDevicePairedEarDidChangeMessage](uiaccessibility/hearingdevicepairedeardidchangemessage.md)
- [InvertColorsStatusDidChangeMessage](uiaccessibility/invertcolorsstatusdidchangemessage.md)
- [MonoAudioStatusDidChangeMessage](uiaccessibility/monoaudiostatusdidchangemessage.md)
- [ReduceMotionStatusDidChangeMessage](uiaccessibility/reducemotionstatusdidchangemessage.md)
- [ReduceTransparencyStatusDidChangeMessage](uiaccessibility/reducetransparencystatusdidchangemessage.md)
- [ShakeToUndoDidChangeMessage](uiaccessibility/shaketoundodidchangemessage.md)
- [SpeakScreenStatusDidChangeMessage](uiaccessibility/speakscreenstatusdidchangemessage.md)
- [SpeakSelectionStatusDidChangeMessage](uiaccessibility/speakselectionstatusdidchangemessage.md)
- [SwitchControlStatusDidChangeMessage](uiaccessibility/switchcontrolstatusdidchangemessage.md)
- [VoiceOverStatusDidChangeMessage](uiaccessibility/voiceoverstatusdidchangemessage.md)

## See Also

### Supporting types

- [AXArrayReturnBlock](axarrayreturnblock.md)
- [AXAttributedStringArrayReturnBlock](axattributedstringarrayreturnblock.md)
- [AXAttributedStringReturnBlock](axattributedstringreturnblock.md)
- [AXBoolReturnBlock](axboolreturnblock.md)
- [AXContainerTypeReturnBlock](axcontainertypereturnblock.md)
- [AXCustomActionsReturnBlock](axcustomactionsreturnblock.md)
- [AXCustomRotorsReturnBlock](axcustomrotorsreturnblock.md)
- [AXNavigationStyleReturnBlock](axnavigationstylereturnblock.md)
- [AXObjectReturnBlock](axobjectreturnblock.md)
- [AXPathReturnBlock](axpathreturnblock.md)
- [AXPointReturnBlock](axpointreturnblock.md)
- [AXRectReturnBlock](axrectreturnblock.md)
- [AXStringArrayReturnBlock](axstringarrayreturnblock.md)
- [AXStringReturnBlock](axstringreturnblock.md)
- [AXTextualContextReturnBlock](axtextualcontextreturnblock.md)
