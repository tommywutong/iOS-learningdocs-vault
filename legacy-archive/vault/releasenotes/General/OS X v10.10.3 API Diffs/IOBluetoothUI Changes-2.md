---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/IOBluetoothUI.html
archived_at: '2026-07-18T02:52:31.538786Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# IOBluetoothUI Changes

## IOBluetoothUI

Modified IOBluetoothDeviceSelectorController.beginSheetModalForWindow(NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafePointer<()>) -> IOReturn ``` |
| To | ``` func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) -> IOReturn ``` |

Modified IOBluetoothDeviceSelectorController.getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>

|  | Declaration |
| --- | --- |
| From | ``` func getSearchAttributes() -> ConstUnsafePointer<IOBluetoothDeviceSearchAttributes> ``` |
| To | ``` func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes> ``` |

Modified IOBluetoothDeviceSelectorController.setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>)

|  | Declaration |
| --- | --- |
| From | ``` func setSearchAttributes(_ searchAttributes: ConstUnsafePointer<IOBluetoothDeviceSearchAttributes>) ``` |
| To | ``` func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>) ``` |

Modified IOBluetoothObjectPushUIController.beginSheetModalForWindow(NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafePointer<()>) -> IOReturn ``` |
| To | ``` func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) -> IOReturn ``` |

Modified IOBluetoothObjectPushUIController.init(objectPushWithBluetoothDevice: IOBluetoothDevice!, withFiles:[AnyObject]!, delegate: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(objectPushWithBluetoothDevice inDevice: IOBluetoothDevice!, withFiles inFiles: [AnyObject]!, delegate inDelegate: AnyObject!) ``` |
| To | ``` init!(objectPushWithBluetoothDevice inDevice: IOBluetoothDevice!, withFiles inFiles: [AnyObject]!, delegate inDelegate: AnyObject!) ``` |

Modified IOBluetoothPairingController.getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>

|  | Declaration |
| --- | --- |
| From | ``` func getSearchAttributes() -> ConstUnsafePointer<IOBluetoothDeviceSearchAttributes> ``` |
| To | ``` func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes> ``` |

Modified IOBluetoothPairingController.setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>)

|  | Declaration |
| --- | --- |
| From | ``` func setSearchAttributes(_ searchAttributes: ConstUnsafePointer<IOBluetoothDeviceSearchAttributes>) ``` |
| To | ``` func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>) ``` |

Modified IOBluetoothPasskeyDisplay.backgroundImageConstraint

|  | Declaration |
| --- | --- |
| From | ``` @IBOutlet var backgroundImageConstraint: NSLayoutConstraint! ``` |
| To | ``` @IBOutlet unowned(unsafe) var backgroundImageConstraint: NSLayoutConstraint! ``` |

Modified IOBluetoothPasskeyDisplay.centeredView

|  | Declaration |
| --- | --- |
| From | ``` @IBOutlet var centeredView: NSView! ``` |
| To | ``` @IBOutlet unowned(unsafe) var centeredView: NSView! ``` |

Modified IOBluetoothServiceBrowserController.init(_: IOBluetoothServiceBrowserControllerOptions)

|  | Declaration |
| --- | --- |
| From | ``` init(_ inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOBluetoothServiceBrowserController ``` |
| To | ``` init!(_ inOptions: IOBluetoothServiceBrowserControllerOptions) -> IOBluetoothServiceBrowserController ``` |

Modified IOBluetoothServiceBrowserController.beginSheetModalForWindow(NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>) -> IOReturn

|  | Declaration |
| --- | --- |
| From | ``` func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafePointer<()>) -> IOReturn ``` |
| To | ``` func beginSheetModalForWindow(_ sheetWindow: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) -> IOReturn ``` |

Modified IOBluetoothServiceBrowserController.getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>

|  | Declaration |
| --- | --- |
| From | ``` func getSearchAttributes() -> ConstUnsafePointer<IOBluetoothDeviceSearchAttributes> ``` |
| To | ``` func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes> ``` |

Modified IOBluetoothServiceBrowserController.setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>)

|  | Declaration |
| --- | --- |
| From | ``` func setSearchAttributes(_ searchAttributes: ConstUnsafePointer<IOBluetoothDeviceSearchAttributes>) ``` |
| To | ``` func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>) ``` |

Modified IOBluetoothValidateHardwareWithDescription(CFString!, CFString!) -> IOReturn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

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
