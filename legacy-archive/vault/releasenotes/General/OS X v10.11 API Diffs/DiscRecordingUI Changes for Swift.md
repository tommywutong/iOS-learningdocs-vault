---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/DiscRecordingUI.html
archived_at: '2026-07-18T02:53:31.444255Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# DiscRecordingUI Changes for Swift

### DiscRecordingUI

Removed DRBurnSessionProgressCallbacks.init(version: UInt32, progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr, progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr, burnDidFinish: DRBurnSessionBurnCompleteProcPtr)Removed DRBurnSessionSetupCallbacks.init(version: UInt32, deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr, containsSuitableMedia: DRBurnSessionMediaCheckProcPtr, deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr)Removed DREraseSessionProgressCallbacks.init(version: UInt32, progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr, progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr, eraseDidFinish: DREraseSessionEraseCompleteProcPtr)Removed DREraseSessionSetupCallbacks.init(version: UInt32, deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr, containsSuitableMedia: DREraseSessionMediaCheckProcPtr, deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr)Added DRBurnSessionProgressCallbacks.init(version: UInt32, progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr!, progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr!, burnDidFinish: DRBurnSessionBurnCompleteProcPtr!)Added DRBurnSessionSetupCallbacks.init(version: UInt32, deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr!, containsSuitableMedia: DRBurnSessionMediaCheckProcPtr!, deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr!)Added DREraseSessionProgressCallbacks.init(version: UInt32, progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr!, progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr!, eraseDidFinish: DREraseSessionEraseCompleteProcPtr!)Added DREraseSessionSetupCallbacks.init(version: UInt32, deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr!, containsSuitableMedia: DREraseSessionMediaCheckProcPtr!, deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr!)Modified DRBurnProgressPanel

|  | Declaration |
| --- | --- |
| From | ``` class DRBurnProgressPanel : NSPanel {     init!() -> DRBurnProgressPanel     class func progressPanel() -> DRBurnProgressPanel!     func beginProgressSheetForBurn(_ burn: DRBurn!, layout layout: AnyObject!, modalForWindow docWindow: NSWindow!)     func beginProgressPanelForBurn(_ burn: DRBurn!, layout layout: AnyObject!)     func setDescription(_ description: String!)     func description() -> String!     func setVerboseProgressStatus(_ verbose: Bool)     func verboseProgressStatus() -> Bool     @IBAction func stopBurn(_ sender: AnyObject!) } ``` |
| To | ``` class DRBurnProgressPanel : NSPanel {      init!()     class func progressPanel() -> DRBurnProgressPanel!     func beginProgressSheetForBurn(_ burn: DRBurn!, layout layout: AnyObject!, modalForWindow docWindow: NSWindow!)     func beginProgressPanelForBurn(_ burn: DRBurn!, layout layout: AnyObject!)     func setDescription(_ description: String!)     func description() -> String!     func setVerboseProgressStatus(_ verbose: Bool)     func verboseProgressStatus() -> Bool     @IBAction func stopBurn(_ sender: AnyObject!) } ``` |

Modified DRBurnSessionProgressCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRBurnSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr     var progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr     var burnDidFinish: DRBurnSessionBurnCompleteProcPtr     init()     init(version version: UInt32, progressWillBegin progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr, progressDidFinish progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr, burnDidFinish burnDidFinish: DRBurnSessionBurnCompleteProcPtr) } ``` |
| To | ``` struct DRBurnSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr!     var progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr!     var burnDidFinish: DRBurnSessionBurnCompleteProcPtr!     init()     init(version version: UInt32, progressWillBegin progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr!, progressDidFinish progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr!, burnDidFinish burnDidFinish: DRBurnSessionBurnCompleteProcPtr!) } ``` |

Modified DRBurnSessionProgressCallbacks.burnDidFinish

|  | Declaration |
| --- | --- |
| From | ``` var burnDidFinish: DRBurnSessionBurnCompleteProcPtr ``` |
| To | ``` var burnDidFinish: DRBurnSessionBurnCompleteProcPtr! ``` |

Modified DRBurnSessionProgressCallbacks.progressDidFinish

|  | Declaration |
| --- | --- |
| From | ``` var progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr ``` |
| To | ``` var progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr! ``` |

Modified DRBurnSessionProgressCallbacks.progressWillBegin

|  | Declaration |
| --- | --- |
| From | ``` var progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr ``` |
| To | ``` var progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr! ``` |

Modified DRBurnSessionSetupCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRBurnSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr     var containsSuitableMedia: DRBurnSessionMediaCheckProcPtr     var deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr     init()     init(version version: UInt32, deviceShouldBeTarget deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr, containsSuitableMedia containsSuitableMedia: DRBurnSessionMediaCheckProcPtr, deviceSelectionChanged deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr) } ``` |
| To | ``` struct DRBurnSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr!     var containsSuitableMedia: DRBurnSessionMediaCheckProcPtr!     var deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr!     init()     init(version version: UInt32, deviceShouldBeTarget deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr!, containsSuitableMedia containsSuitableMedia: DRBurnSessionMediaCheckProcPtr!, deviceSelectionChanged deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr!) } ``` |

Modified DRBurnSessionSetupCallbacks.containsSuitableMedia

|  | Declaration |
| --- | --- |
| From | ``` var containsSuitableMedia: DRBurnSessionMediaCheckProcPtr ``` |
| To | ``` var containsSuitableMedia: DRBurnSessionMediaCheckProcPtr! ``` |

Modified DRBurnSessionSetupCallbacks.deviceSelectionChanged

|  | Declaration |
| --- | --- |
| From | ``` var deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr ``` |
| To | ``` var deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr! ``` |

Modified DRBurnSessionSetupCallbacks.deviceShouldBeTarget

|  | Declaration |
| --- | --- |
| From | ``` var deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr ``` |
| To | ``` var deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr! ``` |

Modified DRBurnSetupPanel

|  | Declaration |
| --- | --- |
| From | ``` class DRBurnSetupPanel : DRSetupPanel {     init!() -> DRBurnSetupPanel     class func setupPanel() -> DRBurnSetupPanel!     func setDefaultButtonTitle(_ title: String!)     func setCanSelectTestBurn(_ flag: Bool)     func setCanSelectAppendableMedia(_ flag: Bool)     func burnObject() -> DRBurn!     @IBAction func expand(_ sender: AnyObject!)     @IBAction func burnSpeed(_ sender: AnyObject!)     @IBAction func appendable(_ sender: AnyObject!)     @IBAction func completionAction(_ sender: AnyObject!)     @IBAction func testBurn(_ sender: AnyObject!)     @IBAction func verifyBurn(_ sender: AnyObject!) } ``` |
| To | ``` class DRBurnSetupPanel : DRSetupPanel {      init!()     class func setupPanel() -> DRBurnSetupPanel!     func setDefaultButtonTitle(_ title: String!)     func setCanSelectTestBurn(_ flag: Bool)     func setCanSelectAppendableMedia(_ flag: Bool)     func burnObject() -> DRBurn!     @IBAction func expand(_ sender: AnyObject!)     @IBAction func burnSpeed(_ sender: AnyObject!)     @IBAction func appendable(_ sender: AnyObject!)     @IBAction func completionAction(_ sender: AnyObject!)     @IBAction func testBurn(_ sender: AnyObject!)     @IBAction func verifyBurn(_ sender: AnyObject!) } ``` |

Modified DREraseProgressPanel

|  | Declaration |
| --- | --- |
| From | ``` class DREraseProgressPanel : NSPanel {     init!() -> DREraseProgressPanel     class func progressPanel() -> DREraseProgressPanel!     func beginProgressSheetForErase(_ erase: DRErase!, modalForWindow docWindow: NSWindow!)     func beginProgressPanelForErase(_ erase: DRErase!)     func setDescription(_ description: String!)     func description() -> String! } ``` |
| To | ``` class DREraseProgressPanel : NSPanel {      init!()     class func progressPanel() -> DREraseProgressPanel!     func beginProgressSheetForErase(_ erase: DRErase!, modalForWindow docWindow: NSWindow!)     func beginProgressPanelForErase(_ erase: DRErase!)     func setDescription(_ description: String!)     func description() -> String! } ``` |

Modified DREraseSessionProgressCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DREraseSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr     var progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr     var eraseDidFinish: DREraseSessionEraseCompleteProcPtr     init()     init(version version: UInt32, progressWillBegin progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr, progressDidFinish progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr, eraseDidFinish eraseDidFinish: DREraseSessionEraseCompleteProcPtr) } ``` |
| To | ``` struct DREraseSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr!     var progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr!     var eraseDidFinish: DREraseSessionEraseCompleteProcPtr!     init()     init(version version: UInt32, progressWillBegin progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr!, progressDidFinish progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr!, eraseDidFinish eraseDidFinish: DREraseSessionEraseCompleteProcPtr!) } ``` |

Modified DREraseSessionProgressCallbacks.eraseDidFinish

|  | Declaration |
| --- | --- |
| From | ``` var eraseDidFinish: DREraseSessionEraseCompleteProcPtr ``` |
| To | ``` var eraseDidFinish: DREraseSessionEraseCompleteProcPtr! ``` |

Modified DREraseSessionProgressCallbacks.progressDidFinish

|  | Declaration |
| --- | --- |
| From | ``` var progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr ``` |
| To | ``` var progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr! ``` |

Modified DREraseSessionProgressCallbacks.progressWillBegin

|  | Declaration |
| --- | --- |
| From | ``` var progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr ``` |
| To | ``` var progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr! ``` |

Modified DREraseSessionSetupCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DREraseSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr     var containsSuitableMedia: DREraseSessionMediaCheckProcPtr     var deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr     init()     init(version version: UInt32, deviceShouldBeTarget deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr, containsSuitableMedia containsSuitableMedia: DREraseSessionMediaCheckProcPtr, deviceSelectionChanged deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr) } ``` |
| To | ``` struct DREraseSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr!     var containsSuitableMedia: DREraseSessionMediaCheckProcPtr!     var deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr!     init()     init(version version: UInt32, deviceShouldBeTarget deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr!, containsSuitableMedia containsSuitableMedia: DREraseSessionMediaCheckProcPtr!, deviceSelectionChanged deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr!) } ``` |

Modified DREraseSessionSetupCallbacks.containsSuitableMedia

|  | Declaration |
| --- | --- |
| From | ``` var containsSuitableMedia: DREraseSessionMediaCheckProcPtr ``` |
| To | ``` var containsSuitableMedia: DREraseSessionMediaCheckProcPtr! ``` |

Modified DREraseSessionSetupCallbacks.deviceSelectionChanged

|  | Declaration |
| --- | --- |
| From | ``` var deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr ``` |
| To | ``` var deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr! ``` |

Modified DREraseSessionSetupCallbacks.deviceShouldBeTarget

|  | Declaration |
| --- | --- |
| From | ``` var deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr ``` |
| To | ``` var deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr! ``` |

Modified DREraseSetupPanel

|  | Declaration |
| --- | --- |
| From | ``` class DREraseSetupPanel : DRSetupPanel {     init!() -> DREraseSetupPanel     class func setupPanel() -> DREraseSetupPanel!     func eraseObject() -> DRErase!     @IBAction func eraseType(_ sender: AnyObject!) } ``` |
| To | ``` class DREraseSetupPanel : DRSetupPanel {      init!()     class func setupPanel() -> DREraseSetupPanel!     func eraseObject() -> DRErase!     @IBAction func eraseType(_ sender: AnyObject!) } ``` |

Modified DRBurnSessionBurnCompleteProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionBurnCompleteProcPtr = CFunctionPointer<((DRBurnSession!, DRBurn!) -> Boolean)> ``` |
| To | ``` typealias DRBurnSessionBurnCompleteProcPtr = (DRBurnSession!, DRBurn!) -> DarwinBoolean ``` |

Modified DRBurnSessionDeviceCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionDeviceCheckProcPtr = CFunctionPointer<((DRBurnSession!, DRDevice!) -> Boolean)> ``` |
| To | ``` typealias DRBurnSessionDeviceCheckProcPtr = (DRBurnSession!, DRDevice!) -> DarwinBoolean ``` |

Modified DRBurnSessionDeviceSelectionNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionDeviceSelectionNotificationProcPtr = CFunctionPointer<((DRBurnSession!, DRDevice!) -> Void)> ``` |
| To | ``` typealias DRBurnSessionDeviceSelectionNotificationProcPtr = (DRBurnSession!, DRDevice!) -> Void ``` |

Modified DRBurnSessionMediaCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionMediaCheckProcPtr = CFunctionPointer<((DRBurnSession!, DRDevice!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Boolean)> ``` |
| To | ``` typealias DRBurnSessionMediaCheckProcPtr = (DRBurnSession!, DRDevice!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> DarwinBoolean ``` |

Modified DRBurnSessionProgressBeginNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionProgressBeginNotificationProcPtr = CFunctionPointer<((DRBurnSession!) -> Void)> ``` |
| To | ``` typealias DRBurnSessionProgressBeginNotificationProcPtr = (DRBurnSession!) -> Void ``` |

Modified DRBurnSessionProgressFinishNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionProgressFinishNotificationProcPtr = CFunctionPointer<((DRBurnSession!) -> Void)> ``` |
| To | ``` typealias DRBurnSessionProgressFinishNotificationProcPtr = (DRBurnSession!) -> Void ``` |

Modified DREraseSessionDeviceCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionDeviceCheckProcPtr = CFunctionPointer<((DREraseSession!, DRDevice!) -> Boolean)> ``` |
| To | ``` typealias DREraseSessionDeviceCheckProcPtr = (DREraseSession!, DRDevice!) -> DarwinBoolean ``` |

Modified DREraseSessionDeviceSelectionNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionDeviceSelectionNotificationProcPtr = CFunctionPointer<((DREraseSession!, DRDevice!) -> Void)> ``` |
| To | ``` typealias DREraseSessionDeviceSelectionNotificationProcPtr = (DREraseSession!, DRDevice!) -> Void ``` |

Modified DREraseSessionEraseCompleteProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionEraseCompleteProcPtr = CFunctionPointer<((DREraseSession!, DRErase!) -> Boolean)> ``` |
| To | ``` typealias DREraseSessionEraseCompleteProcPtr = (DREraseSession!, DRErase!) -> DarwinBoolean ``` |

Modified DREraseSessionMediaCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionMediaCheckProcPtr = CFunctionPointer<((DREraseSession!, DRDevice!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> Boolean)> ``` |
| To | ``` typealias DREraseSessionMediaCheckProcPtr = (DREraseSession!, DRDevice!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> DarwinBoolean ``` |

Modified DREraseSessionProgressBeginNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionProgressBeginNotificationProcPtr = CFunctionPointer<((DREraseSession!) -> Void)> ``` |
| To | ``` typealias DREraseSessionProgressBeginNotificationProcPtr = (DREraseSession!) -> Void ``` |

Modified DREraseSessionProgressFinishNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionProgressFinishNotificationProcPtr = CFunctionPointer<((DREraseSession!) -> Void)> ``` |
| To | ``` typealias DREraseSessionProgressFinishNotificationProcPtr = (DREraseSession!) -> Void ``` |

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
