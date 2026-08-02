---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/DiscRecordingUI.html
archived_at: '2026-07-18T02:52:23.722219Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# DiscRecordingUI Changes

## DiscRecordingUI

Added DRBurnSessionProgressCallbacks.init()Added DRBurnSessionProgressCallbacks.init(version: UInt32, progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr, progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr, burnDidFinish: DRBurnSessionBurnCompleteProcPtr)Added DRBurnSessionProgressDialogOptions.init()Added DRBurnSessionProgressDialogOptions.init(version: UInt32, dialogOptionFlags: DRBurnSessionProgressDialogOptionFlags, description: Unmanaged<CFString>!)Added DRBurnSessionSetupCallbacks.init()Added DRBurnSessionSetupCallbacks.init(version: UInt32, deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr, containsSuitableMedia: DRBurnSessionMediaCheckProcPtr, deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr)Added DRBurnSessionSetupDialogOptions.init()Added DRBurnSessionSetupDialogOptions.init(version: UInt32, dialogOptionFlags: DRBurnSessionSetupDialogOptionFlags, defaultButtonTitle: Unmanaged<CFString>!)Added DREraseSessionProgressCallbacks.init()Added DREraseSessionProgressCallbacks.init(version: UInt32, progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr, progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr, eraseDidFinish: DREraseSessionEraseCompleteProcPtr)Added DREraseSessionProgressDialogOptions.init()Added DREraseSessionProgressDialogOptions.init(version: UInt32, dialogOptionFlags: DREraseSessionProgressDialogOptionFlags, description: Unmanaged<CFString>!)Added DREraseSessionSetupCallbacks.init()Added DREraseSessionSetupCallbacks.init(version: UInt32, deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr, containsSuitableMedia: DREraseSessionMediaCheckProcPtr, deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr)Added DREraseSessionSetupDialogOptions.init()Added DREraseSessionSetupDialogOptions.init(version: UInt32, dialogOptionFlags: DREraseSessionSetupDialogOptionFlags)Added NSObject.burnProgressPanel(DRBurnProgressPanel!, burnDidFinish: DRBurn!) -> BoolAdded NSObject.burnProgressPanelDidFinish(NSNotification!)Added NSObject.burnProgressPanelWillBegin(NSNotification!)Added NSObject.eraseProgressPanel(DREraseProgressPanel!, eraseDidFinish: DRErase!) -> BoolAdded NSObject.eraseProgressPanelDidFinish(NSNotification!)Added NSObject.eraseProgressPanelWillBegin(NSNotification!)Added NSObject.setupPanel(DRSetupPanel!, determineBestDeviceOfA: DRDevice!, orB: DRDevice!) -> DRDevice!Added NSObject.setupPanel(DRSetupPanel!, deviceContainsSuitableMedia: DRDevice!, promptString: AutoreleasingUnsafeMutablePointer<NSString?>) -> BoolAdded NSObject.setupPanel(DRSetupPanel!, deviceCouldBeTarget: DRDevice!) -> BoolAdded NSObject.setupPanelDeviceSelectionChanged(NSNotification!)Added NSObject.setupPanelShouldHandleMediaReservations(DRSetupPanel!) -> BoolModified DRBurnSessionProgressCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRBurnSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr     var progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr     var burnDidFinish: DRBurnSessionBurnCompleteProcPtr } ``` |
| To | ``` struct DRBurnSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr     var progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr     var burnDidFinish: DRBurnSessionBurnCompleteProcPtr     init()     init(version version: UInt32, progressWillBegin progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr, progressDidFinish progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr, burnDidFinish burnDidFinish: DRBurnSessionBurnCompleteProcPtr) } ``` |

Modified DRBurnSessionProgressDialogOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRBurnSessionProgressDialogOptions {     var version: UInt32     var dialogOptionFlags: DRBurnSessionProgressDialogOptionFlags     var description: Unmanaged<CFString>! } ``` |
| To | ``` struct DRBurnSessionProgressDialogOptions {     var version: UInt32     var dialogOptionFlags: DRBurnSessionProgressDialogOptionFlags     var description: Unmanaged<CFString>!     init()     init(version version: UInt32, dialogOptionFlags dialogOptionFlags: DRBurnSessionProgressDialogOptionFlags, description description: Unmanaged<CFString>!) } ``` |

Modified DRBurnSessionSetupCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRBurnSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr     var containsSuitableMedia: DRBurnSessionMediaCheckProcPtr     var deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr } ``` |
| To | ``` struct DRBurnSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr     var containsSuitableMedia: DRBurnSessionMediaCheckProcPtr     var deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr     init()     init(version version: UInt32, deviceShouldBeTarget deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr, containsSuitableMedia containsSuitableMedia: DRBurnSessionMediaCheckProcPtr, deviceSelectionChanged deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr) } ``` |

Modified DRBurnSessionSetupDialogOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRBurnSessionSetupDialogOptions {     var version: UInt32     var dialogOptionFlags: DRBurnSessionSetupDialogOptionFlags     var defaultButtonTitle: Unmanaged<CFString>! } ``` |
| To | ``` struct DRBurnSessionSetupDialogOptions {     var version: UInt32     var dialogOptionFlags: DRBurnSessionSetupDialogOptionFlags     var defaultButtonTitle: Unmanaged<CFString>!     init()     init(version version: UInt32, dialogOptionFlags dialogOptionFlags: DRBurnSessionSetupDialogOptionFlags, defaultButtonTitle defaultButtonTitle: Unmanaged<CFString>!) } ``` |

Modified DREraseSessionProgressCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DREraseSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr     var progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr     var eraseDidFinish: DREraseSessionEraseCompleteProcPtr } ``` |
| To | ``` struct DREraseSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr     var progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr     var eraseDidFinish: DREraseSessionEraseCompleteProcPtr     init()     init(version version: UInt32, progressWillBegin progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr, progressDidFinish progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr, eraseDidFinish eraseDidFinish: DREraseSessionEraseCompleteProcPtr) } ``` |

Modified DREraseSessionProgressDialogOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DREraseSessionProgressDialogOptions {     var version: UInt32     var dialogOptionFlags: DREraseSessionProgressDialogOptionFlags     var description: Unmanaged<CFString>! } ``` |
| To | ``` struct DREraseSessionProgressDialogOptions {     var version: UInt32     var dialogOptionFlags: DREraseSessionProgressDialogOptionFlags     var description: Unmanaged<CFString>!     init()     init(version version: UInt32, dialogOptionFlags dialogOptionFlags: DREraseSessionProgressDialogOptionFlags, description description: Unmanaged<CFString>!) } ``` |

Modified DREraseSessionSetupCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DREraseSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr     var containsSuitableMedia: DREraseSessionMediaCheckProcPtr     var deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr } ``` |
| To | ``` struct DREraseSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr     var containsSuitableMedia: DREraseSessionMediaCheckProcPtr     var deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr     init()     init(version version: UInt32, deviceShouldBeTarget deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr, containsSuitableMedia containsSuitableMedia: DREraseSessionMediaCheckProcPtr, deviceSelectionChanged deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr) } ``` |

Modified DREraseSessionSetupDialogOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DREraseSessionSetupDialogOptions {     var version: UInt32     var dialogOptionFlags: DREraseSessionSetupDialogOptionFlags } ``` |
| To | ``` struct DREraseSessionSetupDialogOptions {     var version: UInt32     var dialogOptionFlags: DREraseSessionSetupDialogOptionFlags     init()     init(version version: UInt32, dialogOptionFlags dialogOptionFlags: DREraseSessionSetupDialogOptionFlags) } ``` |

Modified DRSetupPanel.beginSetupSheetForWindow(NSWindow!, modalDelegate: AnyObject!, didEndSelector: Selector, contextInfo: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func beginSetupSheetForWindow(_ owner: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafePointer<()>) ``` |
| To | ``` func beginSetupSheetForWindow(_ owner: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified DRSetupPanel.init(nibName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(nibName nibName: String!) ``` |
| To | ``` init!(nibName nibName: String!) ``` |

Modified DRBurnIcon

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnIcon: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnIcon: String ``` | OS X 10.2 |

Modified DRBurnProgressPanelDidFinishNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnProgressPanelDidFinishNotification: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnProgressPanelDidFinishNotification: String ``` | OS X 10.2 |

Modified DRBurnProgressPanelWillBeginNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnProgressPanelWillBeginNotification: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnProgressPanelWillBeginNotification: String ``` | OS X 10.2 |

Modified DRBurnSessionBeginProgressDialog(DRBurnSession!, AnyObject!, UnsafeMutablePointer<DRBurnSessionProgressDialogOptions>, UnsafeMutablePointer<DRBurnSessionProgressCallbacks>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRBurnSessionBeginProgressDialog(_ burnSession: DRBurnSession!, _ layout: AnyObject!, _ options: UnsafePointer<DRBurnSessionProgressDialogOptions>, _ progressCallbacks: UnsafePointer<DRBurnSessionProgressCallbacks>) ``` | OS X 10.10 |
| To | ``` func DRBurnSessionBeginProgressDialog(_ burnSession: DRBurnSession!, _ layout: AnyObject!, _ options: UnsafeMutablePointer<DRBurnSessionProgressDialogOptions>, _ progressCallbacks: UnsafeMutablePointer<DRBurnSessionProgressCallbacks>) ``` | OS X 10.3 |

Modified DRBurnSessionCreate() -> Unmanaged<DRBurnSession>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DRBurnSessionGetBurn(DRBurnSession!) -> Unmanaged<DRBurn>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DRBurnSessionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DRBurnSessionMediaCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionMediaCheckProcPtr = CFunctionPointer<((DRBurnSession!, DRDevice!, UnsafePointer<Unmanaged<CFString>?>) -> Boolean)> ``` |
| To | ``` typealias DRBurnSessionMediaCheckProcPtr = CFunctionPointer<((DRBurnSession!, DRDevice!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Boolean)> ``` |

Modified DRBurnSessionSetBurn(DRBurnSession!, DRBurn!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DRBurnSessionSetupDialog(DRBurnSession!, UnsafeMutablePointer<DRBurnSessionSetupDialogOptions>, UnsafeMutablePointer<DRBurnSessionSetupCallbacks>) -> Int8

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DRBurnSessionSetupDialog(_ burnSession: DRBurnSession!, _ options: UnsafePointer<DRBurnSessionSetupDialogOptions>, _ setupCallbacks: UnsafePointer<DRBurnSessionSetupCallbacks>) -> Int8 ``` | OS X 10.10 |
| To | ``` func DRBurnSessionSetupDialog(_ burnSession: DRBurnSession!, _ options: UnsafeMutablePointer<DRBurnSessionSetupDialogOptions>, _ setupCallbacks: UnsafeMutablePointer<DRBurnSessionSetupCallbacks>) -> Int8 ``` | OS X 10.3 |

Modified DRBurnSetupPanelDefaultButtonDefaultTitle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRBurnSetupPanelDefaultButtonDefaultTitle: NSString! ``` | OS X 10.10 |
| To | ``` let DRBurnSetupPanelDefaultButtonDefaultTitle: String ``` | OS X 10.2 |

Modified DREraseIcon

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DREraseIcon: NSString! ``` | OS X 10.10 |
| To | ``` let DREraseIcon: String ``` | OS X 10.2 |

Modified DREraseProgressPanelDidFinishNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DREraseProgressPanelDidFinishNotification: NSString! ``` | OS X 10.10 |
| To | ``` let DREraseProgressPanelDidFinishNotification: String ``` | OS X 10.2 |

Modified DREraseProgressPanelWillBeginNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DREraseProgressPanelWillBeginNotification: NSString! ``` | OS X 10.10 |
| To | ``` let DREraseProgressPanelWillBeginNotification: String ``` | OS X 10.2 |

Modified DREraseSessionBeginProgressDialog(DREraseSession!, UnsafeMutablePointer<DREraseSessionProgressDialogOptions>, UnsafeMutablePointer<DREraseSessionProgressCallbacks>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DREraseSessionBeginProgressDialog(_ eraseSession: DREraseSession!, _ options: UnsafePointer<DREraseSessionProgressDialogOptions>, _ progressCallbacks: UnsafePointer<DREraseSessionProgressCallbacks>) ``` | OS X 10.10 |
| To | ``` func DREraseSessionBeginProgressDialog(_ eraseSession: DREraseSession!, _ options: UnsafeMutablePointer<DREraseSessionProgressDialogOptions>, _ progressCallbacks: UnsafeMutablePointer<DREraseSessionProgressCallbacks>) ``` | OS X 10.3 |

Modified DREraseSessionCreate() -> Unmanaged<DREraseSession>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DREraseSessionGetErase(DREraseSession!) -> Unmanaged<DRErase>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DREraseSessionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DREraseSessionMediaCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionMediaCheckProcPtr = CFunctionPointer<((DREraseSession!, DRDevice!, UnsafePointer<Unmanaged<CFString>?>) -> Boolean)> ``` |
| To | ``` typealias DREraseSessionMediaCheckProcPtr = CFunctionPointer<((DREraseSession!, DRDevice!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Boolean)> ``` |

Modified DREraseSessionSetErase(DREraseSession!, DRErase!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DREraseSessionSetupDialog(DREraseSession!, UnsafeMutablePointer<DREraseSessionSetupDialogOptions>, UnsafeMutablePointer<DREraseSessionSetupCallbacks>) -> Int8

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DREraseSessionSetupDialog(_ eraseSession: DREraseSession!, _ options: UnsafePointer<DREraseSessionSetupDialogOptions>, _ setupCallbacks: UnsafePointer<DREraseSessionSetupCallbacks>) -> Int8 ``` | OS X 10.10 |
| To | ``` func DREraseSessionSetupDialog(_ eraseSession: DREraseSession!, _ options: UnsafeMutablePointer<DREraseSessionSetupDialogOptions>, _ setupCallbacks: UnsafeMutablePointer<DREraseSessionSetupCallbacks>) -> Int8 ``` | OS X 10.3 |

Modified DRSetupPanelDeviceSelectionChangedNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSetupPanelDeviceSelectionChangedNotification: NSString! ``` | OS X 10.10 |
| To | ``` let DRSetupPanelDeviceSelectionChangedNotification: String ``` | OS X 10.2 |

Modified DRSetupPanelSelectedDeviceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let DRSetupPanelSelectedDeviceKey: NSString! ``` | OS X 10.10 |
| To | ``` let DRSetupPanelSelectedDeviceKey: String ``` | OS X 10.2 |

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
