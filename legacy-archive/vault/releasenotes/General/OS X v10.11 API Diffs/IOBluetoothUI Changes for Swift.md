---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/IOBluetoothUI.html
archived_at: '2026-07-18T02:53:36.346926Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# IOBluetoothUI Changes for Swift

### IOBluetoothUI

Removed BluetoothKeyboardReturnType.valueAdded BluetoothKeyboardReturnType.init(rawValue: UInt32)Added BluetoothKeyboardReturnType.rawValueModified [BluetoothKeyboardReturnType [struct]](https://developer.apple.com/documentation/iobluetoothui/bluetoothkeyboardreturntype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BluetoothKeyboardReturnType {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct BluetoothKeyboardReturnType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [IOBluetoothPairingController](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpairingcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothPairingController : NSWindowController {     init!() -> IOBluetoothPairingController     class func pairingController() -> IOBluetoothPairingController!     class func withPairingControllerRef(_ pairingControllerRef: IOBluetoothPairingController!) -> IOBluetoothPairingController!     func getPairingControllerRef() -> Unmanaged<IOBluetoothPairingController>!     func runModal() -> Int32     func getResults() -> [AnyObject]!     func setOptions(_ options: IOBluetoothServiceBrowserControllerOptions)     func getOptions() -> IOBluetoothServiceBrowserControllerOptions     func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>)     func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>     func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)     func addAllowedUUIDArray(_ allowedUUIDArray: [AnyObject]!)     func clearAllowedUUIDs()     func setTitle(_ windowTitle: String!)     func getTitle() -> String!     func setDescriptionText(_ descriptionText: String!)     func getDescriptionText() -> String!     func setPrompt(_ prompt: String!)     func getPrompt() -> String! } ``` |
| To | ``` class IOBluetoothPairingController : NSWindowController {      init!()     class func pairingController() -> IOBluetoothPairingController!     class func withPairingControllerRef(_ pairingControllerRef: IOBluetoothPairingController!) -> IOBluetoothPairingController!     func getPairingControllerRef() -> Unmanaged<IOBluetoothPairingController>!     func runModal() -> Int32     func getResults() -> [AnyObject]!     func setOptions(_ options: IOBluetoothServiceBrowserControllerOptions)     func getOptions() -> IOBluetoothServiceBrowserControllerOptions     func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>)     func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>     func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)     func addAllowedUUIDArray(_ allowedUUIDArray: [AnyObject]!)     func clearAllowedUUIDs()     func setTitle(_ windowTitle: String!)     func getTitle() -> String!     func setDescriptionText(_ descriptionText: String!)     func getDescriptionText() -> String!     func setPrompt(_ prompt: String!)     func getPrompt() -> String! } ``` |

Modified [IOBluetoothServiceBrowserController](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothServiceBrowserController : NSWindowController {     init!(_ inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOBluetoothServiceBrowserController     class func serviceBrowserController(_ inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOBluetoothServiceBrowserController!     class func browseDevices(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>, options inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOReturn     class func browseDevicesAsSheetForWindow(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>, options inOptions: IOBluetoothServiceBrowserControllerOptions, window inWindow: NSWindow!) -> IOReturn     class func withServiceBrowserControllerRef(_ serviceBrowserControllerRef: IOBluetoothServiceBrowserController!) -> IOBluetoothServiceBrowserController!     func getServiceBrowserControllerRef() -> Unmanaged<IOBluetoothServiceBrowserController>!     func discover(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func discoverAsSheetForWindow(_ sheetWindow: NSWindow!, withRecord outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func discoverWithDeviceAttributes(_ deviceAttributes: UnsafeMutablePointer<IOBluetoothDeviceSearchAttributes>, serviceList serviceArray: [AnyObject]!, serviceRecord outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func setOptions(_ inOptions: IOBluetoothServiceBrowserControllerOptions)     func runModal() -> Int32     func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) -> IOReturn     func getResults() -> [AnyObject]!     func getOptions() -> IOBluetoothServiceBrowserControllerOptions     func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>)     func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>     func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)     func addAllowedUUIDArray(_ allowedUUIDArray: [AnyObject]!)     func clearAllowedUUIDs()     func setTitle(_ windowTitle: String!)     func getTitle() -> String!     func setDescriptionText(_ descriptionText: String!)     func getDescriptionText() -> String!     func setPrompt(_ prompt: String!)     func getPrompt() -> String! } ``` |
| To | ``` class IOBluetoothServiceBrowserController : NSWindowController {      init!(_ inOptions: IOBluetoothServiceBrowserControllerOptions)     class func serviceBrowserController(_ inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOBluetoothServiceBrowserController!     class func browseDevices(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>, options inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOReturn     class func browseDevicesAsSheetForWindow(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>, options inOptions: IOBluetoothServiceBrowserControllerOptions, window inWindow: NSWindow!) -> IOReturn     class func withServiceBrowserControllerRef(_ serviceBrowserControllerRef: IOBluetoothServiceBrowserController!) -> IOBluetoothServiceBrowserController!     func getServiceBrowserControllerRef() -> Unmanaged<IOBluetoothServiceBrowserController>!     func discover(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func discoverAsSheetForWindow(_ sheetWindow: NSWindow!, withRecord outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func discoverWithDeviceAttributes(_ deviceAttributes: UnsafeMutablePointer<IOBluetoothDeviceSearchAttributes>, serviceList serviceArray: [AnyObject]!, serviceRecord outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func setOptions(_ inOptions: IOBluetoothServiceBrowserControllerOptions)     func runModal() -> Int32     func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) -> IOReturn     func getResults() -> [AnyObject]!     func getOptions() -> IOBluetoothServiceBrowserControllerOptions     func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>)     func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>     func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)     func addAllowedUUIDArray(_ allowedUUIDArray: [AnyObject]!)     func clearAllowedUUIDs()     func setTitle(_ windowTitle: String!)     func getTitle() -> String!     func setDescriptionText(_ descriptionText: String!)     func getDescriptionText() -> String!     func setPrompt(_ prompt: String!)     func getPrompt() -> String! } ``` |

Modified [IOBluetoothServiceBrowserController.init(_: IOBluetoothServiceBrowserControllerOptions)](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller/1516459-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(_ inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOBluetoothServiceBrowserController ``` |
| To | ``` init!(_ inOptions: IOBluetoothServiceBrowserControllerOptions) ``` |

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
