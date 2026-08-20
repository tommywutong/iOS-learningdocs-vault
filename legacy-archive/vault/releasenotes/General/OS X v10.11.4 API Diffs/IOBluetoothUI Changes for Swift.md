---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/IOBluetoothUI.html
archived_at: '2026-07-18T02:53:52.283381Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# IOBluetoothUI Changes for Swift

### IOBluetoothUI

Modified [IOBluetoothDeviceSelectorController](https://developer.apple.com/documentation/iobluetoothui/iobluetoothdeviceselectorcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothDeviceSelectorController : NSWindowController {     class func deviceSelector() -> IOBluetoothDeviceSelectorController!     class func withDeviceSelectorControllerRef(_ deviceSelectorControllerRef: IOBluetoothDeviceSelectorController!) -> IOBluetoothDeviceSelectorController!     func getDeviceSelectorControllerRef() -> Unmanaged<IOBluetoothDeviceSelectorController>!     func runModal() -> Int32     func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) -> IOReturn     func getResults() -> [AnyObject]!     func setOptions(_ options: IOBluetoothServiceBrowserControllerOptions)     func getOptions() -> IOBluetoothServiceBrowserControllerOptions     func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>)     func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>     func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)     func addAllowedUUIDArray(_ allowedUUIDArray: [AnyObject]!)     func clearAllowedUUIDs()     func setTitle(_ windowTitle: String!)     func getTitle() -> String!     func setHeader(_ headerText: String!)     func getHeader() -> String!     func setDescriptionText(_ descriptionText: String!)     func getDescriptionText() -> String!     func setPrompt(_ prompt: String!)     func getPrompt() -> String!     func setCancel(_ prompt: String!)     func getCancel() -> String! } ``` |
| To | ``` class IOBluetoothDeviceSelectorController : NSWindowController {     class func deviceSelector() -> IOBluetoothDeviceSelectorController!     class func withDeviceSelectorControllerRef(_ deviceSelectorControllerRef: IOBluetoothDeviceSelectorControllerRef!) -> IOBluetoothDeviceSelectorController!     func getDeviceSelectorControllerRef() -> Unmanaged<IOBluetoothDeviceSelectorControllerRef>!     func runModal() -> Int32     func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) -> IOReturn     func getResults() -> [AnyObject]!     func setOptions(_ options: IOBluetoothServiceBrowserControllerOptions)     func getOptions() -> IOBluetoothServiceBrowserControllerOptions     func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>)     func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>     func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)     func addAllowedUUIDArray(_ allowedUUIDArray: [AnyObject]!)     func clearAllowedUUIDs()     func setTitle(_ windowTitle: String!)     func getTitle() -> String!     func setHeader(_ headerText: String!)     func getHeader() -> String!     func setDescriptionText(_ descriptionText: String!)     func getDescriptionText() -> String!     func setPrompt(_ prompt: String!)     func getPrompt() -> String!     func setCancel(_ prompt: String!)     func getCancel() -> String! } ``` |

Modified [IOBluetoothDeviceSelectorControllerRef](https://developer.apple.com/documentation/iobluetoothui/iobluetoothdeviceselectorcontrollerref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothDeviceSelectorControllerRef = IOBluetoothDeviceSelectorController ``` |
| To | ``` class IOBluetoothDeviceSelectorControllerRef { } ``` |

Modified [IOBluetoothPairingController](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpairingcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothPairingController : NSWindowController {      init!()     class func pairingController() -> IOBluetoothPairingController!     class func withPairingControllerRef(_ pairingControllerRef: IOBluetoothPairingController!) -> IOBluetoothPairingController!     func getPairingControllerRef() -> Unmanaged<IOBluetoothPairingController>!     func runModal() -> Int32     func getResults() -> [AnyObject]!     func setOptions(_ options: IOBluetoothServiceBrowserControllerOptions)     func getOptions() -> IOBluetoothServiceBrowserControllerOptions     func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>)     func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>     func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)     func addAllowedUUIDArray(_ allowedUUIDArray: [AnyObject]!)     func clearAllowedUUIDs()     func setTitle(_ windowTitle: String!)     func getTitle() -> String!     func setDescriptionText(_ descriptionText: String!)     func getDescriptionText() -> String!     func setPrompt(_ prompt: String!)     func getPrompt() -> String! } ``` |
| To | ``` class IOBluetoothPairingController : NSWindowController {      init!()     class func pairingController() -> IOBluetoothPairingController!     class func withPairingControllerRef(_ pairingControllerRef: IOBluetoothPairingControllerRef!) -> IOBluetoothPairingController!     func getPairingControllerRef() -> Unmanaged<IOBluetoothPairingControllerRef>!     func runModal() -> Int32     func getResults() -> [AnyObject]!     func setOptions(_ options: IOBluetoothServiceBrowserControllerOptions)     func getOptions() -> IOBluetoothServiceBrowserControllerOptions     func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>)     func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>     func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)     func addAllowedUUIDArray(_ allowedUUIDArray: [AnyObject]!)     func clearAllowedUUIDs()     func setTitle(_ windowTitle: String!)     func getTitle() -> String!     func setDescriptionText(_ descriptionText: String!)     func getDescriptionText() -> String!     func setPrompt(_ prompt: String!)     func getPrompt() -> String! } ``` |

Modified [IOBluetoothPairingControllerRef](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpairingcontrollerref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothPairingControllerRef = IOBluetoothPairingController ``` |
| To | ``` class IOBluetoothPairingControllerRef { } ``` |

Modified [IOBluetoothServiceBrowserController](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller)

|  | Declaration |
| --- | --- |
| From | ``` class IOBluetoothServiceBrowserController : NSWindowController {      init!(_ inOptions: IOBluetoothServiceBrowserControllerOptions)     class func serviceBrowserController(_ inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOBluetoothServiceBrowserController!     class func browseDevices(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>, options inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOReturn     class func browseDevicesAsSheetForWindow(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>, options inOptions: IOBluetoothServiceBrowserControllerOptions, window inWindow: NSWindow!) -> IOReturn     class func withServiceBrowserControllerRef(_ serviceBrowserControllerRef: IOBluetoothServiceBrowserController!) -> IOBluetoothServiceBrowserController!     func getServiceBrowserControllerRef() -> Unmanaged<IOBluetoothServiceBrowserController>!     func discover(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func discoverAsSheetForWindow(_ sheetWindow: NSWindow!, withRecord outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func discoverWithDeviceAttributes(_ deviceAttributes: UnsafeMutablePointer<IOBluetoothDeviceSearchAttributes>, serviceList serviceArray: [AnyObject]!, serviceRecord outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func setOptions(_ inOptions: IOBluetoothServiceBrowserControllerOptions)     func runModal() -> Int32     func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) -> IOReturn     func getResults() -> [AnyObject]!     func getOptions() -> IOBluetoothServiceBrowserControllerOptions     func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>)     func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>     func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)     func addAllowedUUIDArray(_ allowedUUIDArray: [AnyObject]!)     func clearAllowedUUIDs()     func setTitle(_ windowTitle: String!)     func getTitle() -> String!     func setDescriptionText(_ descriptionText: String!)     func getDescriptionText() -> String!     func setPrompt(_ prompt: String!)     func getPrompt() -> String! } ``` |
| To | ``` class IOBluetoothServiceBrowserController : NSWindowController {      init!(_ inOptions: IOBluetoothServiceBrowserControllerOptions)     class func serviceBrowserController(_ inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOBluetoothServiceBrowserController!     class func browseDevices(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>, options inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOReturn     class func browseDevicesAsSheetForWindow(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>, options inOptions: IOBluetoothServiceBrowserControllerOptions, window inWindow: NSWindow!) -> IOReturn     class func withServiceBrowserControllerRef(_ serviceBrowserControllerRef: IOBluetoothServiceBrowserControllerRef!) -> IOBluetoothServiceBrowserController!     func getServiceBrowserControllerRef() -> Unmanaged<IOBluetoothServiceBrowserControllerRef>!     func discover(_ outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func discoverAsSheetForWindow(_ sheetWindow: NSWindow!, withRecord outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func discoverWithDeviceAttributes(_ deviceAttributes: UnsafeMutablePointer<IOBluetoothDeviceSearchAttributes>, serviceList serviceArray: [AnyObject]!, serviceRecord outRecord: AutoreleasingUnsafeMutablePointer<IOBluetoothSDPServiceRecord?>) -> IOReturn     func setOptions(_ inOptions: IOBluetoothServiceBrowserControllerOptions)     func runModal() -> Int32     func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) -> IOReturn     func getResults() -> [AnyObject]!     func getOptions() -> IOBluetoothServiceBrowserControllerOptions     func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>)     func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>     func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)     func addAllowedUUIDArray(_ allowedUUIDArray: [AnyObject]!)     func clearAllowedUUIDs()     func setTitle(_ windowTitle: String!)     func getTitle() -> String!     func setDescriptionText(_ descriptionText: String!)     func getDescriptionText() -> String!     func setPrompt(_ prompt: String!)     func getPrompt() -> String! } ``` |

Modified [IOBluetoothServiceBrowserController.getServiceBrowserControllerRef() -> Unmanaged<IOBluetoothServiceBrowserControllerRef>!](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller/1516462-getservicebrowsercontrollerref)

|  | Declaration |
| --- | --- |
| From | ``` func getServiceBrowserControllerRef() -> Unmanaged<IOBluetoothServiceBrowserController>! ``` |
| To | ``` func getServiceBrowserControllerRef() -> Unmanaged<IOBluetoothServiceBrowserControllerRef>! ``` |

Modified [IOBluetoothServiceBrowserController.withServiceBrowserControllerRef(_: IOBluetoothServiceBrowserControllerRef!) -> IOBluetoothServiceBrowserController! [class]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller/1516498-withservicebrowsercontrollerref)

|  | Declaration |
| --- | --- |
| From | ``` class func withServiceBrowserControllerRef(_ serviceBrowserControllerRef: IOBluetoothServiceBrowserController!) -> IOBluetoothServiceBrowserController! ``` |
| To | ``` class func withServiceBrowserControllerRef(_ serviceBrowserControllerRef: IOBluetoothServiceBrowserControllerRef!) -> IOBluetoothServiceBrowserController! ``` |

Modified [IOBluetoothServiceBrowserControllerRef](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontrollerref)

|  | Declaration |
| --- | --- |
| From | ``` typealias IOBluetoothServiceBrowserControllerRef = IOBluetoothServiceBrowserController ``` |
| To | ``` class IOBluetoothServiceBrowserControllerRef { } ``` |

Modified [IOBluetoothGetDeviceSelectorController() -> Unmanaged<IOBluetoothDeviceSelectorControllerRef>!](https://developer.apple.com/documentation/iobluetoothui/1411895-iobluetoothgetdeviceselectorcont)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothGetDeviceSelectorController() -> Unmanaged<IOBluetoothDeviceSelectorController>! ``` |
| To | ``` func IOBluetoothGetDeviceSelectorController() -> Unmanaged<IOBluetoothDeviceSelectorControllerRef>! ``` |

Modified [IOBluetoothGetPairingController() -> Unmanaged<IOBluetoothPairingControllerRef>!](https://developer.apple.com/documentation/iobluetoothui/1411891-iobluetoothgetpairingcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func IOBluetoothGetPairingController() -> Unmanaged<IOBluetoothPairingController>! ``` |
| To | ``` func IOBluetoothGetPairingController() -> Unmanaged<IOBluetoothPairingControllerRef>! ``` |

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
