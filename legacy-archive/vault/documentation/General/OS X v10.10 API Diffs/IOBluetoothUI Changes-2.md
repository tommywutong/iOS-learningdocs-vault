---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/IOBluetoothUI.html
archived_at: '2026-07-15T07:34:55.500809Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# IOBluetoothUI Changes

## IOBluetoothUI (Added)

Added BluetoothKeyboardReturnType [struct]Added BluetoothKeyboardReturnType.init(_: UInt32)Added BluetoothKeyboardReturnType.valueAdded IOBluetoothAccessibilityIgnoredImageCellAdded IOBluetoothAccessibilityIgnoredTextFieldCellAdded IOBluetoothDeviceSelectorControllerAdded IOBluetoothDeviceSelectorController.addAllowedUUID(IOBluetoothSDPUUID!)Added IOBluetoothDeviceSelectorController.addAllowedUUIDArray([AnyObject]!)Added IOBluetoothDeviceSelectorController.beginSheetModalForWindow(NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>) -> IOReturnAdded IOBluetoothDeviceSelectorController.clearAllowedUUIDs()Added IOBluetoothDeviceSelectorController.deviceSelector() -> IOBluetoothDeviceSelectorController! [class]Added IOBluetoothDeviceSelectorController.getCancel() -> String!Added IOBluetoothDeviceSelectorController.getDescriptionText() -> String!Added IOBluetoothDeviceSelectorController.getHeader() -> String!Added IOBluetoothDeviceSelectorController.getOptions() -> IOBluetoothServiceBrowserControllerOptionsAdded IOBluetoothDeviceSelectorController.getPrompt() -> String!Added IOBluetoothDeviceSelectorController.getResults() -> [AnyObject]!Added IOBluetoothDeviceSelectorController.getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>Added IOBluetoothDeviceSelectorController.getTitle() -> String!Added IOBluetoothDeviceSelectorController.runModal() -> Int32Added IOBluetoothDeviceSelectorController.setCancel(String!)Added IOBluetoothDeviceSelectorController.setDescriptionText(String!)Added IOBluetoothDeviceSelectorController.setHeader(String!)Added IOBluetoothDeviceSelectorController.setOptions(IOBluetoothServiceBrowserControllerOptions)Added IOBluetoothDeviceSelectorController.setPrompt(String!)Added IOBluetoothDeviceSelectorController.setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>)Added IOBluetoothDeviceSelectorController.setTitle(String!)Added IOBluetoothObjectPushUIControllerAdded IOBluetoothObjectPushUIController.beginSheetModalForWindow(NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>) -> IOReturnAdded IOBluetoothObjectPushUIController.getDevice() -> IOBluetoothDevice!Added IOBluetoothObjectPushUIController.getTitle() -> String!Added IOBluetoothObjectPushUIController.isTransferInProgress() -> BoolAdded IOBluetoothObjectPushUIController.init(objectPushWithBluetoothDevice: IOBluetoothDevice!, withFiles:[AnyObject]!, delegate: AnyObject!)Added IOBluetoothObjectPushUIController.runModal()Added IOBluetoothObjectPushUIController.runPanel()Added IOBluetoothObjectPushUIController.setIconImage(NSImage!)Added IOBluetoothObjectPushUIController.setTitle(String!)Added IOBluetoothObjectPushUIController.stop()Added IOBluetoothPairingControllerAdded IOBluetoothPairingController.addAllowedUUID(IOBluetoothSDPUUID!)Added IOBluetoothPairingController.addAllowedUUIDArray([AnyObject]!)Added IOBluetoothPairingController.clearAllowedUUIDs()Added IOBluetoothPairingController.getDescriptionText() -> String!Added IOBluetoothPairingController.getOptions() -> IOBluetoothServiceBrowserControllerOptionsAdded IOBluetoothPairingController.getPrompt() -> String!Added IOBluetoothPairingController.getResults() -> [AnyObject]!Added IOBluetoothPairingController.getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>Added IOBluetoothPairingController.getTitle() -> String!Added IOBluetoothPairingController.runModal() -> Int32Added IOBluetoothPairingController.setDescriptionText(String!)Added IOBluetoothPairingController.setOptions(IOBluetoothServiceBrowserControllerOptions)Added IOBluetoothPairingController.setPrompt(String!)Added IOBluetoothPairingController.setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>)Added IOBluetoothPairingController.setTitle(String!)Added IOBluetoothPasskeyDisplayAdded IOBluetoothPasskeyDisplay.advancePasskeyIndicator()Added IOBluetoothPasskeyDisplay.backgroundImageConstraintAdded IOBluetoothPasskeyDisplay.centeredViewAdded IOBluetoothPasskeyDisplay.isIncomingRequestAdded IOBluetoothPasskeyDisplay.passkeyAdded IOBluetoothPasskeyDisplay.resetPasskeyIndicator()Added IOBluetoothPasskeyDisplay.retreatPasskeyIndicator()Added IOBluetoothPasskeyDisplay.returnHighlightImageAdded IOBluetoothPasskeyDisplay.returnImageAdded IOBluetoothPasskeyDisplay.setPasskey(String!, forDevice: IOBluetoothDevice!, usingSSP: Bool)Added IOBluetoothPasskeyDisplay.sharedDisplayView() -> IOBluetoothPasskeyDisplay! [class]Added IOBluetoothPasskeyDisplay.usePasskeyNotificaitonsAdded IOBluetoothServiceBrowserControllerAdded IOBluetoothServiceBrowserController.init(_: IOBluetoothServiceBrowserControllerOptions)Added IOBluetoothServiceBrowserController.addAllowedUUID(IOBluetoothSDPUUID!)Added IOBluetoothServiceBrowserController.addAllowedUUIDArray([AnyObject]!)Added IOBluetoothServiceBrowserController.beginSheetModalForWindow(NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>) -> IOReturnAdded IOBluetoothServiceBrowserController.clearAllowedUUIDs()Added IOBluetoothServiceBrowserController.getDescriptionText() -> String!Added IOBluetoothServiceBrowserController.getOptions() -> IOBluetoothServiceBrowserControllerOptionsAdded IOBluetoothServiceBrowserController.getPrompt() -> String!Added IOBluetoothServiceBrowserController.getResults() -> [AnyObject]!Added IOBluetoothServiceBrowserController.getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>Added IOBluetoothServiceBrowserController.getServiceBrowserControllerRef() -> Unmanaged<IOBluetoothServiceBrowserController>!Added IOBluetoothServiceBrowserController.getTitle() -> String!Added IOBluetoothServiceBrowserController.runModal() -> Int32Added IOBluetoothServiceBrowserController.setDescriptionText(String!)Added IOBluetoothServiceBrowserController.setOptions(IOBluetoothServiceBrowserControllerOptions)Added IOBluetoothServiceBrowserController.setPrompt(String!)Added IOBluetoothServiceBrowserController.setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>)Added IOBluetoothServiceBrowserController.setTitle(String!)Added IOBluetoothServiceBrowserController.withServiceBrowserControllerRef(IOBluetoothServiceBrowserController!) -> IOBluetoothServiceBrowserController! [class]Added IOBluetoothDeviceSelectorControllerRefAdded IOBluetoothGetDeviceSelectorController() -> Unmanaged<IOBluetoothDeviceSelectorController>!Added IOBluetoothGetPairingController() -> Unmanaged<IOBluetoothPairingController>!Added IOBluetoothPairingControllerRefAdded IOBluetoothServiceBrowserControllerOptionsAdded IOBluetoothServiceBrowserControllerRefAdded IOBluetoothValidateHardwareWithDescription(CFString!, CFString!) -> IOReturnAdded kBluetoothKeyboardANSIReturnAdded kBluetoothKeyboardISOReturnAdded kBluetoothKeyboardJISReturnAdded kBluetoothKeyboardNoReturnAdded kIOBluetoothServiceBrowserControllerOptionsAutoStartInquiryAdded kIOBluetoothServiceBrowserControllerOptionsDisconnectWhenDoneAdded kIOBluetoothServiceBrowserControllerOptionsNoneAdded kIOBluetoothUISuccessAdded kIOBluetoothUIUserCanceledErr

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
