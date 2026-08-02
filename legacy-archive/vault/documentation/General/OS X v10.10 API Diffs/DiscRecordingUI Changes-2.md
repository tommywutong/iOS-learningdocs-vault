---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/DiscRecordingUI.html
archived_at: '2026-07-15T07:34:54.189466Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# DiscRecordingUI Changes

## DiscRecordingUI (Added)

Added DRBurnProgressPanelAdded DRBurnProgressPanel.beginProgressPanelForBurn(DRBurn!, layout: AnyObject!)Added DRBurnProgressPanel.beginProgressSheetForBurn(DRBurn!, layout: AnyObject!, modalForWindow: NSWindow!)Added DRBurnProgressPanel.description() -> String!Added DRBurnProgressPanel.setDescription(String!)Added DRBurnProgressPanel.setVerboseProgressStatus(Bool)Added DRBurnProgressPanel.stopBurn(AnyObject!)Added DRBurnProgressPanel.verboseProgressStatus() -> BoolAdded DRBurnSessionProgressCallbacks [struct]Added DRBurnSessionProgressCallbacks.burnDidFinishAdded DRBurnSessionProgressCallbacks.progressDidFinishAdded DRBurnSessionProgressCallbacks.progressWillBeginAdded DRBurnSessionProgressCallbacks.versionAdded DRBurnSessionProgressDialogOptions [struct]Added DRBurnSessionProgressDialogOptions.descriptionAdded DRBurnSessionProgressDialogOptions.dialogOptionFlagsAdded DRBurnSessionProgressDialogOptions.versionAdded DRBurnSessionSetupCallbacks [struct]Added DRBurnSessionSetupCallbacks.containsSuitableMediaAdded DRBurnSessionSetupCallbacks.deviceSelectionChangedAdded DRBurnSessionSetupCallbacks.deviceShouldBeTargetAdded DRBurnSessionSetupCallbacks.versionAdded DRBurnSessionSetupDialogOptions [struct]Added DRBurnSessionSetupDialogOptions.defaultButtonTitleAdded DRBurnSessionSetupDialogOptions.dialogOptionFlagsAdded DRBurnSessionSetupDialogOptions.versionAdded DRBurnSetupPanelAdded DRBurnSetupPanel.appendable(AnyObject!)Added DRBurnSetupPanel.burnObject() -> DRBurn!Added DRBurnSetupPanel.burnSpeed(AnyObject!)Added DRBurnSetupPanel.completionAction(AnyObject!)Added DRBurnSetupPanel.expand(AnyObject!)Added DRBurnSetupPanel.setCanSelectAppendableMedia(Bool)Added DRBurnSetupPanel.setCanSelectTestBurn(Bool)Added DRBurnSetupPanel.setDefaultButtonTitle(String!)Added DRBurnSetupPanel.testBurn(AnyObject!)Added DRBurnSetupPanel.verifyBurn(AnyObject!)Added DREraseProgressPanelAdded DREraseProgressPanel.beginProgressPanelForErase(DRErase!)Added DREraseProgressPanel.beginProgressSheetForErase(DRErase!, modalForWindow: NSWindow!)Added DREraseProgressPanel.description() -> String!Added DREraseProgressPanel.setDescription(String!)Added DREraseSessionProgressCallbacks [struct]Added DREraseSessionProgressCallbacks.eraseDidFinishAdded DREraseSessionProgressCallbacks.progressDidFinishAdded DREraseSessionProgressCallbacks.progressWillBeginAdded DREraseSessionProgressCallbacks.versionAdded DREraseSessionProgressDialogOptions [struct]Added DREraseSessionProgressDialogOptions.descriptionAdded DREraseSessionProgressDialogOptions.dialogOptionFlagsAdded DREraseSessionProgressDialogOptions.versionAdded DREraseSessionSetupCallbacks [struct]Added DREraseSessionSetupCallbacks.containsSuitableMediaAdded DREraseSessionSetupCallbacks.deviceSelectionChangedAdded DREraseSessionSetupCallbacks.deviceShouldBeTargetAdded DREraseSessionSetupCallbacks.versionAdded DREraseSessionSetupDialogOptions [struct]Added DREraseSessionSetupDialogOptions.dialogOptionFlagsAdded DREraseSessionSetupDialogOptions.versionAdded DREraseSetupPanelAdded DREraseSetupPanel.eraseObject() -> DRErase!Added DREraseSetupPanel.eraseType(AnyObject!)Added DRSetupPanelAdded DRSetupPanel.beginSetupSheetForWindow(NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)Added DRSetupPanel.cancel(AnyObject!)Added DRSetupPanel.close(AnyObject!)Added DRSetupPanel.deviceSelectionChanged(DRDevice!)Added DRSetupPanel.eject(AnyObject!)Added DRSetupPanel.mediaStateChanged([NSObject: AnyObject]!) -> BoolAdded DRSetupPanel.init(nibName: String!)Added DRSetupPanel.ok(AnyObject!)Added DRSetupPanel.open(AnyObject!)Added DRSetupPanel.runSetupPanel() -> IntAdded DRSetupPanel.setupForDisplay()Added NSObject.burnProgressPanel(DRBurnProgressPanel!, burnDidFinish: DRBurn!) -> BoolAdded NSObject.burnProgressPanelDidFinish(NSNotification!)Added NSObject.burnProgressPanelWillBegin(NSNotification!)Added NSObject.eraseProgressPanel(DREraseProgressPanel!, eraseDidFinish: DRErase!) -> BoolAdded NSObject.eraseProgressPanelDidFinish(NSNotification!)Added NSObject.eraseProgressPanelWillBegin(NSNotification!)Added NSObject.setupPanel(DRSetupPanel!, determineBestDeviceOfA: DRDevice!, orB: DRDevice!) -> DRDevice!Added NSObject.setupPanel(DRSetupPanel!, deviceContainsSuitableMedia: DRDevice!, promptString: AutoreleasingUnsafeMutablePointer<NSString?>) -> BoolAdded NSObject.setupPanel(DRSetupPanel!, deviceCouldBeTarget: DRDevice!) -> BoolAdded NSObject.setupPanelDeviceSelectionChanged(NSNotification!)Added NSObject.setupPanelShouldHandleMediaReservations(DRSetupPanel!) -> BoolAdded DRBurnIconAdded DRBurnProgressPanelDidFinishNotificationAdded DRBurnProgressPanelWillBeginNotificationAdded DRBurnSessionBeginProgressDialog(DRBurnSession!, AnyObject!, UnsafeMutablePointer<DRBurnSessionProgressDialogOptions>, UnsafeMutablePointer<DRBurnSessionProgressCallbacks>)Added DRBurnSessionBurnCompleteProcPtrAdded DRBurnSessionCreate() -> Unmanaged<DRBurnSession>!Added DRBurnSessionDeviceCheckProcPtrAdded DRBurnSessionDeviceSelectionNotificationProcPtrAdded DRBurnSessionGetBurn(DRBurnSession!) -> Unmanaged<DRBurn>!Added DRBurnSessionGetTypeID() -> CFTypeIDAdded DRBurnSessionMediaCheckProcPtrAdded DRBurnSessionProgressBeginNotificationProcPtrAdded DRBurnSessionProgressDialogOptionFlagsAdded DRBurnSessionProgressFinishNotificationProcPtrAdded DRBurnSessionRefAdded DRBurnSessionSetBurn(DRBurnSession!, DRBurn!)Added DRBurnSessionSetupDialog(DRBurnSession!, UnsafeMutablePointer<DRBurnSessionSetupDialogOptions>, UnsafeMutablePointer<DRBurnSessionSetupCallbacks>) -> Int8Added DRBurnSessionSetupDialogOptionFlagsAdded DRBurnSetupPanelDefaultButtonDefaultTitleAdded DREraseIconAdded DREraseProgressPanelDidFinishNotificationAdded DREraseProgressPanelWillBeginNotificationAdded DREraseSessionBeginProgressDialog(DREraseSession!, UnsafeMutablePointer<DREraseSessionProgressDialogOptions>, UnsafeMutablePointer<DREraseSessionProgressCallbacks>)Added DREraseSessionCreate() -> Unmanaged<DREraseSession>!Added DREraseSessionDeviceCheckProcPtrAdded DREraseSessionDeviceSelectionNotificationProcPtrAdded DREraseSessionEraseCompleteProcPtrAdded DREraseSessionGetErase(DREraseSession!) -> Unmanaged<DRErase>!Added DREraseSessionGetTypeID() -> CFTypeIDAdded DREraseSessionMediaCheckProcPtrAdded DREraseSessionProgressBeginNotificationProcPtrAdded DREraseSessionProgressDialogOptionFlagsAdded DREraseSessionProgressFinishNotificationProcPtrAdded DREraseSessionRefAdded DREraseSessionSetErase(DREraseSession!, DRErase!)Added DREraseSessionSetupDialog(DREraseSession!, UnsafeMutablePointer<DREraseSessionSetupDialogOptions>, UnsafeMutablePointer<DREraseSessionSetupCallbacks>) -> Int8Added DREraseSessionSetupDialogOptionFlagsAdded DRSetupPanelDeviceSelectionChangedNotificationAdded DRSetupPanelSelectedDeviceKeyAdded kBurnSessionProgressDialogDefaultOptionsAdded kBurnSessionProgressDialogDisplayVerboseProgressAdded kBurnSessionProgressDialogOptionsCurrentVersionAdded kBurnSessionSetupDialogAllowTestBurnsAdded kBurnSessionSetupDialogDefaultOptionsAdded kBurnSessionSetupDialogDontHandleReservationsAdded kBurnSessionSetupDialogForceClosedDiscsAdded kBurnSessionSetupDialogOptionsCurrentVersionAdded kDRBurnProgressSetupCallbacksCurrentVersionAdded kDRBurnSessionCancelAdded kDRBurnSessionOKAdded kDRBurnSessionSetupCallbacksCurrentVersionAdded kDREraseProgressSetupCallbacksCurrentVersionAdded kDREraseSessionCancelAdded kDREraseSessionOKAdded kDREraseSessionSetupCallbacksCurrentVersionAdded kEraseSessionProgressDialogDefaultOptionsAdded kEraseSessionProgressDialogOptionsCurrentVersionAdded kEraseSessionSetupDialogDefaultOptionsAdded kEraseSessionSetupDialogDontHandleReservationsAdded kEraseSessionSetupDialogOptionsCurrentVersion

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
