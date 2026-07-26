---
title: NotificationCenter.MessageIdentifier
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/messageidentifier
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier.json'
content_hash: 'sha256:21dee4c58ed44402'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# NotificationCenter.MessageIdentifier

<sub>Protocol</sub>

An optional identifier to associate a given message with a given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MessageIdentifier
```

## Overview

Implement a `MessageIdentifier` to provide a typed, ergonomic experience at the call point, as described in [SE-0299](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0299-extend-generic-static-member-lookup.md).

For example, given `ExampleMessage` with a `Subject` called `ExampleSubject`:

```swift
extension NotificationCenter.MessageIdentifier where Self == NotificationCenter.BaseMessageIdentifier<ExampleMessage> {
    static var eventDidOccur: Self { .init() }
}
```

This simplifies the call point for clients, as seen here:

```swift
let token = center.addObserver(of: exampleSubject, for: .eventDidOccur) { ... }
```

## Relationships

- **Conforming Types**: [BaseMessageIdentifier](basemessageidentifier.md)

## Topics

### Declaring the message type

- [MessageType](messageidentifier/messagetype.md)

### Identifying cookie storage messages

- [cookiesChanged](messageidentifier/cookieschanged.md) — An identifier for a message about a cookie storage instance’s cookies changing.

### Identifying undo manager messages

- [willUndoChange](messageidentifier/willundochange.md) — An identifier for a message about an undo manager preparing to perform an undo.
- [didUndoChange](messageidentifier/didundochange.md) — An identifier for a message about an undo manager having performed an undo.
- [willRedoChange](messageidentifier/willredochange.md) — An identifier for a message about an undo manager preparing to perform a redo.
- [didRedoChange](messageidentifier/didredochange.md) — An identifier for a message about an undo manager having performed a redo.
- [checkpoint](messageidentifier/checkpoint.md) — An identifier for a message about an undo manager reaching a checkpoint.
- [didOpenUndoGroup](messageidentifier/didopenundogroup.md) — An identifier for a message about an undo manager having opened an undo group.
- [willCloseUndoGroup](messageidentifier/willcloseundogroup.md) — An identifier for a message about an undo manager preparing to close an undo group.
- [didCloseUndoGroup](messageidentifier/didcloseundogroup.md) — An identifier for a message about an undo manager having closed an undo group.

### Identifying defaults messages

- [didChange](messageidentifier/didchange-187tw.md) — An identifier for a message about a change in a user defaults setting.
- [sizeLimitExceeded](messageidentifier/sizelimitexceeded.md) — An identifier for a message about a user defaults database exceeding its maximum size.

### Identifying metadata query messages

- [didStartGathering](messageidentifier/didstartgathering.md) — An identifier for a message about a metadata query that is starting its initial result gathering.
- [didFinishGathering](messageidentifier/didfinishgathering.md) — An identifier for a message about a metadata query that finished its initial result gathering.

### Identifying calendar, date, and time zone messages

- [calendarDayChanged](messageidentifier/calendardaychanged.md) — An identifier for a message about a change in calendar day.
- [systemClockDidChange](messageidentifier/systemclockdidchange.md) — An identifier for a message about a change in the system clock.
- [systemTimeZoneDidChange](messageidentifier/systemtimezonedidchange.md) — An identifier for a message about a change in the system time zone.

### Identifying locale messages

- [currentLocaleDidChange](messageidentifier/currentlocaledidchange.md) — An identifier for a message about a change in current locale.

### Identifying bundle messages

- [didLoad](messageidentifier/didload.md) — An identifier for a message about a bundle dynamically loading a class.

### Identifying process info messages

- [powerStateDidChange](messageidentifier/powerstatedidchange.md) — An identifier for a message about a power state change.
- [thermalStateDidChange](messageidentifier/thermalstatedidchange.md) — An identifier for a message about a thermal state change.
- [didTerminate](messageidentifier/didterminate.md) — An identifier for a message about a stopped task.

### Identifying file handle messages

- [connectionAccepted](messageidentifier/connectionaccepted.md) — An identifier for a message about a file handle accepting a connection.
- [dataAvailable](messageidentifier/dataavailable.md) — An identifier for a message about a file handle having data available for reading.
- [readToEndOfFileCompletion](messageidentifier/readtoendoffilecompletion.md) — An identifier for a message about a file handle having reached the end of a file or communication channel.
- [readCompletion](messageidentifier/readcompletion.md) — An identifier for a message about a file handle having read the currently available data from a file or communication channel.

### Identifying port messages

- [didBecomeInvalid](messageidentifier/didbecomeinvalid.md) — An identifier for a message about a port becoming invalid.

### Identifying file manager messages

- [ubiquityIdentityDidChange](messageidentifier/ubiquityidentitydidchange.md) — An identifier for a message about a file manager’s ubiquity identity changing.

### Identifying bundle resource request messages

- [lowDiskSpace](messageidentifier/lowdiskspace.md) — An identifier for a message about the available disk space getting low. _(deprecated)_

### Identifying extension messages

- [didBecomeActive](messageidentifier/didbecomeactive-79dvm.md) — An identifier for a message about a host app moving from the inactive to the active state.
- [willResignActive](messageidentifier/willresignactive-9z4xc.md) — An identifier for a message about a host app moving from the active to the inactive state.
- [didEnterBackground](messageidentifier/didenterbackground-5gdtk.md) — An identifier for a message about a host app beginning to run in the background.
- [willEnterForeground](messageidentifier/willenterforeground-p1og.md) — An identifier for a message about a host app preparing to run in the foreground.

### Identifying UIKit accessibility messages

- [switchControlStatusDidChange](messageidentifier/switchcontrolstatusdidchange.md)
- [elementFocused](messageidentifier/elementfocused.md)
- [reduceTransparencyStatusDidChange](messageidentifier/reducetransparencystatusdidchange.md)
- [announcementDidFinish](messageidentifier/announcementdidfinish.md)
- [boldTextStatusDidChange](messageidentifier/boldtextstatusdidchange.md)
- [closedCaptioningStatusDidChange](messageidentifier/closedcaptioningstatusdidchange.md)
- [darkerSystemColorsStatusDidChange](messageidentifier/darkersystemcolorsstatusdidchange.md)
- [grayscaleStatusDidChange](messageidentifier/grayscalestatusdidchange.md)
- [invertColorsStatusDidChange](messageidentifier/invertcolorsstatusdidchange.md)
- [assistiveTouchStatusDidChange](messageidentifier/assistivetouchstatusdidchange.md)
- [guidedAccessStatusDidChange](messageidentifier/guidedaccessstatusdidchange.md)
- [monoAudioStatusDidChange](messageidentifier/monoaudiostatusdidchange.md)
- [speakScreenStatusDidChange](messageidentifier/speakscreenstatusdidchange.md)
- [speakSelectionStatusDidChange](messageidentifier/speakselectionstatusdidchange.md)
- [hearingDevicePairedEarDidChange](messageidentifier/hearingdevicepairedeardidchange.md)
- [reduceMotionStatusDidChange](messageidentifier/reducemotionstatusdidchange.md)
- [shakeToUndoDidChange](messageidentifier/shaketoundodidchange.md)
- [voiceOverStatusDidChange](messageidentifier/voiceoverstatusdidchange.md)
- [buttonShapesEnabledStatusDidChange](messageidentifier/buttonshapesenabledstatusdidchange.md) _(deprecated)_

### Identifying UIKit app life cycle messages

- [didFinishLaunching](messageidentifier/didfinishlaunching.md)
- [didBecomeActive](messageidentifier/didbecomeactive-2hcfs.md)
- [didEnterBackground](messageidentifier/didenterbackground-1u5sm.md)
- [willEnterForeground](messageidentifier/willenterforeground-95zi8.md)
- [willResignActive](messageidentifier/willresignactive-4rf2p.md)
- [didReceiveMemoryWarning](messageidentifier/didreceivememorywarning.md)
- [significantTimeChange](messageidentifier/significanttimechange.md)
- [backgroundRefreshStatusDidChange](messageidentifier/backgroundrefreshstatusdidchange.md)
- [userDidTakeScreenshot](messageidentifier/userdidtakescreenshot.md)

### Identifying UIKit content size messages

- [contentSizeCategoryDidChange](messageidentifier/contentsizecategorydidchange.md)

### Identifying UIKIt device messages

- [batteryLevelDidChange](messageidentifier/batteryleveldidchange.md)
- [batteryStateDidChange](messageidentifier/batterystatedidchange.md)
- [orientationDidChange](messageidentifier/orientationdidchange.md)
- [proximityStateDidChange](messageidentifier/proximitystatedidchange.md)

### Identifying UIKit document messages

- [stateChanged](messageidentifier/statechanged.md)

### Identifying UIKit pasteboard messages

- [changed](messageidentifier/changed-28zxj.md)
- [removed](messageidentifier/removed.md)

### Identifying UIKit responder messages

- [keyboardWillChangeFrame](messageidentifier/keyboardwillchangeframe.md)
- [keyboardDidChangeFrame](messageidentifier/keyboarddidchangeframe.md)
- [keyboardWillHide](messageidentifier/keyboardwillhide.md)
- [keyboardDidHide](messageidentifier/keyboarddidhide.md)
- [keyboardWillShow](messageidentifier/keyboardwillshow.md)
- [keyboardDidShow](messageidentifier/keyboarddidshow.md)

### Identifying UIKit screen messages

- [brightnessDidChange](messageidentifier/brightnessdidchange.md)
- [modeDidChange](messageidentifier/modedidchange.md)
- [capturedDidChange](messageidentifier/captureddidchange.md)
- [referenceDisplayModeStatusDidChange](messageidentifier/referencedisplaymodestatusdidchange.md)

### Identifying UIKit text field messages

- [textDidBeginEditing](messageidentifier/textdidbeginediting-7lt1k.md)
- [textDidChange](messageidentifier/textdidchange-9363k.md)
- [textDidEndEditing](messageidentifier/textdidendediting-4r8fw.md)

### Identifying UIKit text input mode messages

- [currentInputModeDidChange](messageidentifier/currentinputmodedidchange.md)

### Identifying UIKit text view messages

- [textDidBeginEditing](messageidentifier/textdidbeginediting-9y8tn.md)
- [textDidChange](messageidentifier/textdidchange-8ns63.md)
- [textDidEndEditing](messageidentifier/textdidendediting-6cmke.md)

### Identifying UIKit view controller messages

- [didBecomeVisible](messageidentifier/didbecomevisible.md)
- [didBecomeHidden](messageidentifier/didbecomehidden.md)
- [showDetailTargetDidChange](messageidentifier/showdetailtargetdidchange.md)

### Identifying UIKit focus messages

- [movementDidFail](messageidentifier/movementdidfail.md)

### Identifying UIKit pointer lock state messages

- [didChange](messageidentifier/didchange-7wty5.md)

### Identifying UIKit scene messages

- [systemProtectionDidChange](messageidentifier/systemprotectiondidchange.md)
- [willConnect](messageidentifier/willconnect.md)
- [willEnterForeground](messageidentifier/willenterforeground-992xq.md)
- [didActivate](messageidentifier/didactivate.md)
- [willDeactivate](messageidentifier/willdeactivate.md)
- [didEnterBackground](messageidentifier/didenterbackground-5fqw0.md)

### Identifying AppKit workspace messages

- [didHideApplication](messageidentifier/didhideapplication.md)
- [didUnhideApplication](messageidentifier/didunhideapplication.md)
- [willLaunchApplication](messageidentifier/willlaunchapplication.md)
- [didLaunchApplication](messageidentifier/didlaunchapplication.md)
- [willSleep](messageidentifier/willsleep.md)
- [didWake](messageidentifier/didwake.md)
- [didTerminateApplication](messageidentifier/didterminateapplication.md)
- [didMountVolume](messageidentifier/didmountvolume.md)
- [willUnmountVolume](messageidentifier/willunmountvolume.md)
- [didUnmountVolume](messageidentifier/didunmountvolume.md)
- [didActivateApplication](messageidentifier/didactivateapplication.md)
- [didDeactivateApplication](messageidentifier/diddeactivateapplication.md)
- [didRenameVolume](messageidentifier/didrenamevolume.md)
- [sessionDidBecomeActive](messageidentifier/sessiondidbecomeactive.md)
- [sessionDidResignActive](messageidentifier/sessiondidresignactive.md)
- [didChangeFileLabels](messageidentifier/didchangefilelabels.md)
- [screensDidSleep](messageidentifier/screensdidsleep.md)
- [screensDidWake](messageidentifier/screensdidwake.md)
- [activeSpaceDidChange](messageidentifier/activespacedidchange.md)
- [accessibilityDisplayOptionsDidChange](messageidentifier/accessibilitydisplayoptionsdidchange.md)
- [shouldBeginSuppressingHighDynamicRangeContent](messageidentifier/shouldbeginsuppressinghighdynamicrangecontent.md)
- [shouldEndSuppressingHighDynamicRangeContent](messageidentifier/shouldendsuppressinghighdynamicrangecontent.md)

### Identifying EventKit messages

- [changed](messageidentifier/changed-50yz5.md) — A notification posted when changes are made to the Calendar or Reminders database.

### Identifying iTunes library messages

- [didChange](messageidentifier/didchange-1coqh.md)

### Type Properties

- [accessoryDidConnect](messageidentifier/accessorydidconnect.md) _(beta)_
- [accessoryDidDisconnect](messageidentifier/accessorydiddisconnect.md) _(beta)_
- [applicationAccessibilityEnabledDidChange](messageidentifier/applicationaccessibilityenableddidchange.md) — Shorthand identifier for `AccessibilitySettings/ApplicationAccessibilityEnabledDidChangeMessage`. _(beta)_
- [boundsDidChange](messageidentifier/boundsdidchange.md) _(beta)_
- [colorDidChange](messageidentifier/colordidchange.md) _(beta)_
- [colorSpaceDidChange](messageidentifier/colorspacedidchange.md) _(beta)_
- [columnConfigurationDidChange](messageidentifier/columnconfigurationdidchange.md) _(beta)_
- [columnDidMove](messageidentifier/columndidmove-78e2d.md) _(beta)_
- [columnDidMove](messageidentifier/columndidmove-9tkq6.md) _(beta)_
- [columnDidResize](messageidentifier/columndidresize-5pxs4.md) _(beta)_
- [columnDidResize](messageidentifier/columndidresize-7ktag.md) _(beta)_
- [contextHelpModeDidActivate](messageidentifier/contexthelpmodedidactivate.md) _(beta)_
- [contextHelpModeDidDeactivate](messageidentifier/contexthelpmodediddeactivate.md) _(beta)_
- [conversationHistoryDidUpdateMessage](messageidentifier/conversationhistorydidupdatemessage.md)
- [didAddItem](messageidentifier/didadditem.md) _(beta)_
- [didBecomeActive](messageidentifier/didbecomeactive-2y311.md) _(beta)_
- [didBecomeActive](messageidentifier/didbecomeactive-546kc.md) _(beta)_
- [didBecomeCurrent](messageidentifier/didbecomecurrent-9p0n4.md) — The identifier of the message that posts after a game controller becomes the most recently used controller.
- [didBecomeCurrent](messageidentifier/didbecomecurrent-9zfc.md) — The identifier of the message that posts after a mouse becomes the most recently used mouse.
- [didBecomeInactive](messageidentifier/didbecomeinactive.md) _(beta)_
- [didBecomeKey](messageidentifier/didbecomekey-3qijm.md) _(beta)_
- [didBecomeKey](messageidentifier/didbecomekey-6kgub.md)
- [didBecomeMain](messageidentifier/didbecomemain.md) _(beta)_
- [didBeginEditing](messageidentifier/didbeginediting.md) _(beta)_
- [didBeginTracking](messageidentifier/didbegintracking.md) _(beta)_
- [didChange](messageidentifier/didchange-1ebzb.md) _(beta)_
- [didChange](messageidentifier/didchange-96f1i.md) _(beta)_
- [didChange](messageidentifier/didchange-ywl6.md) _(beta)_
- [didChangeAutomaticCapitalization](messageidentifier/didchangeautomaticcapitalization.md) _(beta)_
- [didChangeAutomaticDashSubstitution](messageidentifier/didchangeautomaticdashsubstitution.md) _(beta)_
- [didChangeAutomaticInlinePrediction](messageidentifier/didchangeautomaticinlineprediction.md) _(beta)_
- [didChangeAutomaticPeriodSubstitution](messageidentifier/didchangeautomaticperiodsubstitution.md) _(beta)_
- [didChangeAutomaticQuoteSubstitution](messageidentifier/didchangeautomaticquotesubstitution.md) _(beta)_
- [didChangeAutomaticSpellingCorrection](messageidentifier/didchangeautomaticspellingcorrection.md) _(beta)_
- [didChangeAutomaticTextCompletion](messageidentifier/didchangeautomatictextcompletion.md) _(beta)_
- [didChangeAutomaticTextReplacement](messageidentifier/didchangeautomatictextreplacement.md) _(beta)_
- [didChangeBackingProperties](messageidentifier/didchangebackingproperties.md) _(beta)_
- [didChangeItem](messageidentifier/didchangeitem.md) _(beta)_
- [didChangeOcclusionState](messageidentifier/didchangeocclusionstate-5853a.md) _(beta)_
- [didChangeOcclusionState](messageidentifier/didchangeocclusionstate-99vn6.md) _(beta)_
- [didChangeScreen](messageidentifier/didchangescreen.md) _(beta)_
- [didChangeScreenParameters](messageidentifier/didchangescreenparameters.md) _(beta)_
- [didChangeScreenProfile](messageidentifier/didchangescreenprofile.md) _(beta)_
- [didChangeSelection](messageidentifier/didchangeselection.md) _(beta)_
- [didChangeTypingAttributes](messageidentifier/didchangetypingattributes.md) _(beta)_
- [didClose](messageidentifier/didclose.md) _(beta)_
- [didConnect](messageidentifier/didconnect-2pidr.md) — The identifier of the message that posts after a mouse accessory connects to the device.
- [didConnect](messageidentifier/didconnect-39qlx.md) — The identifier of the message that posts after a racing wheel accessory connects to the device.
- [didConnect](messageidentifier/didconnect-3d7x9.md) — The identifier of the message that posts after a game controller accessory connects to the device.
- [didConnect](messageidentifier/didconnect-6zuxs.md) — The identifier of the message that posts after a keyboard accessory connects to the device.
- [didConnect](messageidentifier/didconnect-oq29.md) — The identifier of the message that posts after a spatial accessory connects to the device. _(beta)_
- [didConnect](messageidentifier/didconnect-wf9.md) — The identifier of the message that posts after a stylus accessory connects to the device.
- [didDeminiaturize](messageidentifier/diddeminiaturize.md) _(beta)_
- [didDisconnect](messageidentifier/diddisconnect-127wj.md) — The identifier of the message that posts after a racing wheel accessory disconnects from the device.
- [didDisconnect](messageidentifier/diddisconnect-3p6qi.md) — The identifier of the message that posts after a stylus accessory disconnects from the device.
- [didDisconnect](messageidentifier/diddisconnect-5s9vw.md) — The identifier of the message that posts after a mouse accessory disconnects from the device.
- [didDisconnect](messageidentifier/diddisconnect-97jtl.md) — The identifier of the message that posts after a keyboard accessory disconnects from the device.
- [didDisconnect](messageidentifier/diddisconnect-9qi2f.md) — The identifier of the message that posts after a spatial accessory disconnects from the device. _(beta)_
- [didDisconnect](messageidentifier/diddisconnect-9ymbl.md) — The identifier of the message that posts after a game controller accessory disconnects from the device.
- [didEndEditing](messageidentifier/didendediting.md) _(beta)_
- [didEndLiveMagnify](messageidentifier/didendlivemagnify.md) _(beta)_
- [didEndLiveResize](messageidentifier/didendliveresize.md) _(beta)_
- [didEndLiveScroll](messageidentifier/didendlivescroll.md) _(beta)_
- [didEndSheet](messageidentifier/didendsheet.md) _(beta)_
- [didEndTracking](messageidentifier/didendtracking.md) _(beta)_
- [didEnterFullScreen](messageidentifier/didenterfullscreen.md) _(beta)_
- [didEnterVersionBrowser](messageidentifier/didenterversionbrowser.md) _(beta)_
- [didExitFullScreen](messageidentifier/didexitfullscreen.md) _(beta)_
- [didExitVersionBrowser](messageidentifier/didexitversionbrowser.md) _(beta)_
- [didExpose](messageidentifier/didexpose.md) _(beta)_
- [didFinishRestoringWindows](messageidentifier/didfinishrestoringwindows.md) _(beta)_
- [didHide](messageidentifier/didhide.md) _(beta)_
- [didLiveScroll](messageidentifier/didlivescroll.md) _(beta)_
- [didMergeChanges](messageidentifier/didmergechanges.md) _(beta)_
- [didMergeChangesAsync](messageidentifier/didmergechangesasync.md) _(beta)_
- [didMiniaturize](messageidentifier/didminiaturize.md) _(beta)_
- [didMove](messageidentifier/didmove.md) _(beta)_
- [didMoveToWritableLocation](messageidentifier/didmovetowritablelocation.md)
- [didRemoveItem](messageidentifier/didremoveitem-4hapv.md) _(beta)_
- [didRemoveItem](messageidentifier/didremoveitem-bimz.md) _(beta)_
- [didResignActive](messageidentifier/didresignactive.md) _(beta)_
- [didResignKey](messageidentifier/didresignkey-11hzh.md)
- [didResignKey](messageidentifier/didresignkey-2dgp0.md) _(beta)_
- [didResignMain](messageidentifier/didresignmain.md) _(beta)_
- [didResize](messageidentifier/didresize.md) _(beta)_
- [didResizeSubviews](messageidentifier/didresizesubviews.md) _(beta)_
- [didSave](messageidentifier/didsave.md) _(beta)_
- [didSaveObjectIDs](messageidentifier/didsaveobjectids.md) _(beta)_
- [didSaveObjectIDsAsync](messageidentifier/didsaveobjectidsasync.md) _(beta)_
- [didSendAction](messageidentifier/didsendaction.md) _(beta)_
- [didShow](messageidentifier/didshow.md) _(beta)_
- [didStopBeingCurrent](messageidentifier/didstopbeingcurrent-2sc31.md) — The identifier of the message that posts after a mouse stops being longer the most recently used mouse.
- [didStopBeingCurrent](messageidentifier/didstopbeingcurrent-9pdq9.md) — The identifier of the message that posts after a game controller stops being longer the most recently used controller.
- [didUnhide](messageidentifier/didunhide.md) _(beta)_
- [didUpdate](messageidentifier/didupdate-p3fm.md)
- [didUpdate](messageidentifier/didupdate-vu3m.md) _(beta)_
- [didUpdateWindows](messageidentifier/didupdatewindows.md) _(beta)_
- [eventChanged](messageidentifier/eventchanged.md) _(beta)_
- [fontSetChanged](messageidentifier/fontsetchanged.md) _(beta)_
- [frameDidChange](messageidentifier/framedidchange.md) _(beta)_
- [indexDidUpdate](messageidentifier/indexdidupdate.md)
- [itemDidCollapse](messageidentifier/itemdidcollapse.md) _(beta)_
- [itemDidExpand](messageidentifier/itemdidexpand.md) _(beta)_
- [itemWillCollapse](messageidentifier/itemwillcollapse.md) _(beta)_
- [itemWillExpand](messageidentifier/itemwillexpand.md) _(beta)_
- [keyboardSelectionDidChange](messageidentifier/keyboardselectiondidchange.md) _(beta)_
- [objectsDidChange](messageidentifier/objectsdidchange.md) _(beta)_
- [preferredScrollerStyleDidChange](messageidentifier/preferredscrollerstyledidchange.md) _(beta)_
- [protectedDataDidBecomeAvailable](messageidentifier/protecteddatadidbecomeavailable-3di2c.md) _(beta)_
- [protectedDataDidBecomeAvailable](messageidentifier/protecteddatadidbecomeavailable-6h44m.md)
- [protectedDataWillBecomeUnavailable](messageidentifier/protecteddatawillbecomeunavailable-1izcs.md) _(beta)_
- [protectedDataWillBecomeUnavailable](messageidentifier/protecteddatawillbecomeunavailable-3n08h.md)
- [radioAccessTechnologyDidChange](messageidentifier/radioaccesstechnologydidchange.md) _(beta)_
- [registrationsChanged](messageidentifier/registrationschanged.md) _(beta)_
- [registryDidChange](messageidentifier/registrydidchange.md) _(beta)_
- [remoteChange](messageidentifier/remotechange.md) _(beta)_
- [resumptionRecommendation](messageidentifier/resumptionrecommendation.md) _(beta)_
- [rowsDidChange](messageidentifier/rowsdidchange.md) _(beta)_
- [selectedAlternativeString](messageidentifier/selectedalternativestring.md) _(beta)_
- [selectionDidChange](messageidentifier/selectiondidchange-2akj4.md)
- [selectionDidChange](messageidentifier/selectiondidchange-676mh.md) _(beta)_
- [selectionDidChange](messageidentifier/selectiondidchange-72x2p.md) _(beta)_
- [selectionDidChange](messageidentifier/selectiondidchange-7qmnc.md) _(beta)_
- [selectionIsChanging](messageidentifier/selectionischanging-2i647.md) _(beta)_
- [selectionIsChanging](messageidentifier/selectionischanging-5u4tc.md) _(beta)_
- [selectionIsChanging](messageidentifier/selectionischanging-abh0.md) _(beta)_
- [storesDidChange](messageidentifier/storesdidchange.md) _(beta)_
- [storesDidChangeAsync](messageidentifier/storesdidchangeasync.md) _(beta)_
- [systemColorsDidChange](messageidentifier/systemcolorsdidchange.md) _(beta)_
- [systemPrefersReducedResourceUsageDidChange](messageidentifier/systemprefersreducedresourceusagedidchange.md) _(beta)_
- [tagsDidChange](messageidentifier/tagsdidchange.md) _(beta)_
- [textDidBeginEditing](messageidentifier/textdidbeginediting-45vc.md) _(beta)_
- [textDidChange](messageidentifier/textdidchange-5j4s4.md) _(beta)_
- [textDidEndEditing](messageidentifier/textdidendediting-5yxiy.md) _(beta)_
- [textMessageAvailabilityDidChange](messageidentifier/textmessageavailabilitydidchange.md) — Notification posted when text message availability changes. _(beta)_
- [tokensDidExpire](messageidentifier/tokensdidexpire.md)
- [userPreferencesDidChange](messageidentifier/userpreferencesdidchange.md)
- [willAddItem](messageidentifier/willadditem.md) _(beta)_
- [willBecomeActive](messageidentifier/willbecomeactive.md) _(beta)_
- [willBeginSheet](messageidentifier/willbeginsheet.md) _(beta)_
- [willChangeNotifyingTextView](messageidentifier/willchangenotifyingtextview.md) _(beta)_
- [willClose](messageidentifier/willclose-2wsvs.md) _(beta)_
- [willClose](messageidentifier/willclose-4565q.md) _(beta)_
- [willDismiss](messageidentifier/willdismiss.md) _(beta)_
- [willEnterFullScreen](messageidentifier/willenterfullscreen.md) _(beta)_
- [willEnterVersionBrowser](messageidentifier/willenterversionbrowser.md) _(beta)_
- [willExitFullScreen](messageidentifier/willexitfullscreen.md) _(beta)_
- [willExitVersionBrowser](messageidentifier/willexitversionbrowser.md) _(beta)_
- [willFinishLaunching](messageidentifier/willfinishlaunching.md) _(beta)_
- [willHide](messageidentifier/willhide.md) _(beta)_
- [willMiniaturize](messageidentifier/willminiaturize.md) _(beta)_
- [willMove](messageidentifier/willmove.md) _(beta)_
- [willPopUp](messageidentifier/willpopup-4czk2.md) _(beta)_
- [willPopUp](messageidentifier/willpopup-81zuu.md) _(beta)_
- [willPopUp](messageidentifier/willpopup-8ycpp.md) _(beta)_
- [willResignActive](messageidentifier/willresignactive-9aumz.md) _(beta)_
- [willResizeSubviews](messageidentifier/willresizesubviews.md) _(beta)_
- [willSave](messageidentifier/willsave.md) _(beta)_
- [willSendAction](messageidentifier/willsendaction.md) _(beta)_
- [willShow](messageidentifier/willshow.md) _(beta)_
- [willStartLiveMagnify](messageidentifier/willstartlivemagnify.md) _(beta)_
- [willStartLiveResize](messageidentifier/willstartliveresize.md) _(beta)_
- [willStartLiveScroll](messageidentifier/willstartlivescroll.md) _(beta)_
- [willTerminate](messageidentifier/willterminate-1u238.md)
- [willTerminate](messageidentifier/willterminate-7lu3s.md) _(beta)_
- [willUnhide](messageidentifier/willunhide.md) _(beta)_
- [willUpdateWindows](messageidentifier/willupdatewindows.md) _(beta)_

## See Also

### Using message identifiers

- [BaseMessageIdentifier](basemessageidentifier.md) — A type for use when defining optional Message identifiers.
