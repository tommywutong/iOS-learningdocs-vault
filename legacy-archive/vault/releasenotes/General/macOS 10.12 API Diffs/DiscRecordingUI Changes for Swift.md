---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/DiscRecordingUI.html
archived_at: '2026-07-18T02:51:16.485357Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# DiscRecordingUI Changes for Swift

### DiscRecordingUI

Removed DRBurnSessionSetupCallbacks.init(version: UInt32, deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr!, containsSuitableMedia: DRBurnSessionMediaCheckProcPtr!, deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr!)Removed DREraseSessionSetupCallbacks.init(version: UInt32, deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr!, containsSuitableMedia: DREraseSessionMediaCheckProcPtr!, deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr!)Added DRBurnSessionSetupCallbacks.init(version: UInt32, deviceShouldBeTarget: DiscRecordingUI.DRBurnSessionDeviceCheckProcPtr!, containsSuitableMedia: DiscRecordingUI.DRBurnSessionMediaCheckProcPtr!, deviceSelectionChanged: DiscRecordingUI.DRBurnSessionDeviceSelectionNotificationProcPtr!)Added DREraseSessionSetupCallbacks.init(version: UInt32, deviceShouldBeTarget: DiscRecordingUI.DREraseSessionDeviceCheckProcPtr!, containsSuitableMedia: DiscRecordingUI.DREraseSessionMediaCheckProcPtr!, deviceSelectionChanged: DiscRecordingUI.DREraseSessionDeviceSelectionNotificationProcPtr!)Modified DRBurnProgressPanel

|  | Declaration |
| --- | --- |
| From | ``` class DRBurnProgressPanel : NSPanel {      init!()     class func progressPanel() -> DRBurnProgressPanel!     func beginProgressSheetForBurn(_ burn: DRBurn!, layout layout: AnyObject!, modalForWindow docWindow: NSWindow!)     func beginProgressPanelForBurn(_ burn: DRBurn!, layout layout: AnyObject!)     func setDescription(_ description: String!)     func description() -> String!     func setVerboseProgressStatus(_ verbose: Bool)     func verboseProgressStatus() -> Bool     @IBAction func stopBurn(_ sender: AnyObject!) } ``` |
| To | ``` class DRBurnProgressPanel : NSPanel {      init!()     class func progressPanel() -> DRBurnProgressPanel!     func beginProgressSheet(for burn: DRBurn!, layout layout: Any!, modalFor docWindow: NSWindow!)     func begin(for burn: DRBurn!, layout layout: Any!)     func setDescription(_ description: String!)     func description() -> String!     func setVerboseProgressStatus(_ verbose: Bool)     func verboseProgressStatus() -> Bool     @IBAction func stopBurn(_ sender: Any!) } ``` |

Modified DRBurnProgressPanel.begin(for: DRBurn!, layout: Any!)

|  | Declaration |
| --- | --- |
| From | ``` func beginProgressPanelForBurn(_ burn: DRBurn!, layout layout: AnyObject!) ``` |
| To | ``` func begin(for burn: DRBurn!, layout layout: Any!) ``` |

Modified DRBurnProgressPanel.beginProgressSheet(for: DRBurn!, layout: Any!, modalFor: NSWindow!)

|  | Declaration |
| --- | --- |
| From | ``` func beginProgressSheetForBurn(_ burn: DRBurn!, layout layout: AnyObject!, modalForWindow docWindow: NSWindow!) ``` |
| To | ``` func beginProgressSheet(for burn: DRBurn!, layout layout: Any!, modalFor docWindow: NSWindow!) ``` |

Modified DRBurnProgressPanel.stopBurn(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func stopBurn(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func stopBurn(_ sender: Any!) ``` |

Modified DRBurnSessionProgressCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRBurnSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr!     var progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr!     var burnDidFinish: DRBurnSessionBurnCompleteProcPtr!     init()     init(version version: UInt32, progressWillBegin progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr!, progressDidFinish progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr!, burnDidFinish burnDidFinish: DRBurnSessionBurnCompleteProcPtr!) } ``` |
| To | ``` struct DRBurnSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DiscRecordingUI.DRBurnSessionProgressBeginNotificationProcPtr!     var progressDidFinish: DiscRecordingUI.DRBurnSessionProgressFinishNotificationProcPtr!     var burnDidFinish: DiscRecordingUI.DRBurnSessionBurnCompleteProcPtr!     init()     init(version version: UInt32, progressWillBegin progressWillBegin: DiscRecordingUI.DRBurnSessionProgressBeginNotificationProcPtr!, progressDidFinish progressDidFinish: DiscRecordingUI.DRBurnSessionProgressFinishNotificationProcPtr!, burnDidFinish burnDidFinish: DiscRecordingUI.DRBurnSessionBurnCompleteProcPtr!) } ``` |

Modified DRBurnSessionProgressCallbacks.burnDidFinish

|  | Declaration |
| --- | --- |
| From | ``` var burnDidFinish: DRBurnSessionBurnCompleteProcPtr! ``` |
| To | ``` var burnDidFinish: DiscRecordingUI.DRBurnSessionBurnCompleteProcPtr! ``` |

Modified DRBurnSessionProgressCallbacks.init(version: UInt32, progressWillBegin: DiscRecordingUI.DRBurnSessionProgressBeginNotificationProcPtr!, progressDidFinish: DiscRecordingUI.DRBurnSessionProgressFinishNotificationProcPtr!, burnDidFinish: DiscRecordingUI.DRBurnSessionBurnCompleteProcPtr!)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: UInt32, progressWillBegin progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr!, progressDidFinish progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr!, burnDidFinish burnDidFinish: DRBurnSessionBurnCompleteProcPtr!) ``` |
| To | ``` init(version version: UInt32, progressWillBegin progressWillBegin: DiscRecordingUI.DRBurnSessionProgressBeginNotificationProcPtr!, progressDidFinish progressDidFinish: DiscRecordingUI.DRBurnSessionProgressFinishNotificationProcPtr!, burnDidFinish burnDidFinish: DiscRecordingUI.DRBurnSessionBurnCompleteProcPtr!) ``` |

Modified DRBurnSessionProgressCallbacks.progressDidFinish

|  | Declaration |
| --- | --- |
| From | ``` var progressDidFinish: DRBurnSessionProgressFinishNotificationProcPtr! ``` |
| To | ``` var progressDidFinish: DiscRecordingUI.DRBurnSessionProgressFinishNotificationProcPtr! ``` |

Modified DRBurnSessionProgressCallbacks.progressWillBegin

|  | Declaration |
| --- | --- |
| From | ``` var progressWillBegin: DRBurnSessionProgressBeginNotificationProcPtr! ``` |
| To | ``` var progressWillBegin: DiscRecordingUI.DRBurnSessionProgressBeginNotificationProcPtr! ``` |

Modified DRBurnSessionSetupCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRBurnSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr!     var containsSuitableMedia: DRBurnSessionMediaCheckProcPtr!     var deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr!     init()     init(version version: UInt32, deviceShouldBeTarget deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr!, containsSuitableMedia containsSuitableMedia: DRBurnSessionMediaCheckProcPtr!, deviceSelectionChanged deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr!) } ``` |
| To | ``` struct DRBurnSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DiscRecordingUI.DRBurnSessionDeviceCheckProcPtr!     var containsSuitableMedia: DiscRecordingUI.DRBurnSessionMediaCheckProcPtr!     var deviceSelectionChanged: DiscRecordingUI.DRBurnSessionDeviceSelectionNotificationProcPtr!     init()     init(version version: UInt32, deviceShouldBeTarget deviceShouldBeTarget: DiscRecordingUI.DRBurnSessionDeviceCheckProcPtr!, containsSuitableMedia containsSuitableMedia: DiscRecordingUI.DRBurnSessionMediaCheckProcPtr!, deviceSelectionChanged deviceSelectionChanged: DiscRecordingUI.DRBurnSessionDeviceSelectionNotificationProcPtr!) } ``` |

Modified DRBurnSessionSetupCallbacks.containsSuitableMedia

|  | Declaration |
| --- | --- |
| From | ``` var containsSuitableMedia: DRBurnSessionMediaCheckProcPtr! ``` |
| To | ``` var containsSuitableMedia: DiscRecordingUI.DRBurnSessionMediaCheckProcPtr! ``` |

Modified DRBurnSessionSetupCallbacks.deviceSelectionChanged

|  | Declaration |
| --- | --- |
| From | ``` var deviceSelectionChanged: DRBurnSessionDeviceSelectionNotificationProcPtr! ``` |
| To | ``` var deviceSelectionChanged: DiscRecordingUI.DRBurnSessionDeviceSelectionNotificationProcPtr! ``` |

Modified DRBurnSessionSetupCallbacks.deviceShouldBeTarget

|  | Declaration |
| --- | --- |
| From | ``` var deviceShouldBeTarget: DRBurnSessionDeviceCheckProcPtr! ``` |
| To | ``` var deviceShouldBeTarget: DiscRecordingUI.DRBurnSessionDeviceCheckProcPtr! ``` |

Modified DRBurnSetupPanel

|  | Declaration |
| --- | --- |
| From | ``` class DRBurnSetupPanel : DRSetupPanel {      init!()     class func setupPanel() -> DRBurnSetupPanel!     func setDefaultButtonTitle(_ title: String!)     func setCanSelectTestBurn(_ flag: Bool)     func setCanSelectAppendableMedia(_ flag: Bool)     func burnObject() -> DRBurn!     @IBAction func expand(_ sender: AnyObject!)     @IBAction func burnSpeed(_ sender: AnyObject!)     @IBAction func appendable(_ sender: AnyObject!)     @IBAction func completionAction(_ sender: AnyObject!)     @IBAction func testBurn(_ sender: AnyObject!)     @IBAction func verifyBurn(_ sender: AnyObject!) } ``` |
| To | ``` class DRBurnSetupPanel : DRSetupPanel {      init!()     class func setupPanel() -> DRBurnSetupPanel!     func setDefaultButtonTitle(_ title: String!)     func setCanSelectTestBurn(_ flag: Bool)     func setCanSelectAppendableMedia(_ flag: Bool)     func burnObject() -> DRBurn!     @IBAction func expand(_ sender: Any!)     @IBAction func burnSpeed(_ sender: Any!)     @IBAction func appendable(_ sender: Any!)     @IBAction func completionAction(_ sender: Any!)     @IBAction func testBurn(_ sender: Any!)     @IBAction func verifyBurn(_ sender: Any!) } ``` |

Modified DRBurnSetupPanel.appendable(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func appendable(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func appendable(_ sender: Any!) ``` |

Modified DRBurnSetupPanel.burnSpeed(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func burnSpeed(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func burnSpeed(_ sender: Any!) ``` |

Modified DRBurnSetupPanel.completionAction(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func completionAction(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func completionAction(_ sender: Any!) ``` |

Modified DRBurnSetupPanel.expand(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func expand(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func expand(_ sender: Any!) ``` |

Modified DRBurnSetupPanel.testBurn(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func testBurn(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func testBurn(_ sender: Any!) ``` |

Modified DRBurnSetupPanel.verifyBurn(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func verifyBurn(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func verifyBurn(_ sender: Any!) ``` |

Modified DREraseProgressPanel

|  | Declaration |
| --- | --- |
| From | ``` class DREraseProgressPanel : NSPanel {      init!()     class func progressPanel() -> DREraseProgressPanel!     func beginProgressSheetForErase(_ erase: DRErase!, modalForWindow docWindow: NSWindow!)     func beginProgressPanelForErase(_ erase: DRErase!)     func setDescription(_ description: String!)     func description() -> String! } ``` |
| To | ``` class DREraseProgressPanel : NSPanel {      init!()     class func progressPanel() -> DREraseProgressPanel!     func beginProgressSheet(for erase: DRErase!, modalFor docWindow: NSWindow!)     func begin(for erase: DRErase!)     func setDescription(_ description: String!)     func description() -> String! } ``` |

Modified DREraseProgressPanel.begin(for: DRErase!)

|  | Declaration |
| --- | --- |
| From | ``` func beginProgressPanelForErase(_ erase: DRErase!) ``` |
| To | ``` func begin(for erase: DRErase!) ``` |

Modified DREraseProgressPanel.beginProgressSheet(for: DRErase!, modalFor: NSWindow!)

|  | Declaration |
| --- | --- |
| From | ``` func beginProgressSheetForErase(_ erase: DRErase!, modalForWindow docWindow: NSWindow!) ``` |
| To | ``` func beginProgressSheet(for erase: DRErase!, modalFor docWindow: NSWindow!) ``` |

Modified DREraseSessionProgressCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DREraseSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr!     var progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr!     var eraseDidFinish: DREraseSessionEraseCompleteProcPtr!     init()     init(version version: UInt32, progressWillBegin progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr!, progressDidFinish progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr!, eraseDidFinish eraseDidFinish: DREraseSessionEraseCompleteProcPtr!) } ``` |
| To | ``` struct DREraseSessionProgressCallbacks {     var version: UInt32     var progressWillBegin: DiscRecordingUI.DREraseSessionProgressBeginNotificationProcPtr!     var progressDidFinish: DiscRecordingUI.DREraseSessionProgressFinishNotificationProcPtr!     var eraseDidFinish: DiscRecordingUI.DREraseSessionEraseCompleteProcPtr!     init()     init(version version: UInt32, progressWillBegin progressWillBegin: DiscRecordingUI.DREraseSessionProgressBeginNotificationProcPtr!, progressDidFinish progressDidFinish: DiscRecordingUI.DREraseSessionProgressFinishNotificationProcPtr!, eraseDidFinish eraseDidFinish: DiscRecordingUI.DREraseSessionEraseCompleteProcPtr!) } ``` |

Modified DREraseSessionProgressCallbacks.eraseDidFinish

|  | Declaration |
| --- | --- |
| From | ``` var eraseDidFinish: DREraseSessionEraseCompleteProcPtr! ``` |
| To | ``` var eraseDidFinish: DiscRecordingUI.DREraseSessionEraseCompleteProcPtr! ``` |

Modified DREraseSessionProgressCallbacks.init(version: UInt32, progressWillBegin: DiscRecordingUI.DREraseSessionProgressBeginNotificationProcPtr!, progressDidFinish: DiscRecordingUI.DREraseSessionProgressFinishNotificationProcPtr!, eraseDidFinish: DiscRecordingUI.DREraseSessionEraseCompleteProcPtr!)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: UInt32, progressWillBegin progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr!, progressDidFinish progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr!, eraseDidFinish eraseDidFinish: DREraseSessionEraseCompleteProcPtr!) ``` |
| To | ``` init(version version: UInt32, progressWillBegin progressWillBegin: DiscRecordingUI.DREraseSessionProgressBeginNotificationProcPtr!, progressDidFinish progressDidFinish: DiscRecordingUI.DREraseSessionProgressFinishNotificationProcPtr!, eraseDidFinish eraseDidFinish: DiscRecordingUI.DREraseSessionEraseCompleteProcPtr!) ``` |

Modified DREraseSessionProgressCallbacks.progressDidFinish

|  | Declaration |
| --- | --- |
| From | ``` var progressDidFinish: DREraseSessionProgressFinishNotificationProcPtr! ``` |
| To | ``` var progressDidFinish: DiscRecordingUI.DREraseSessionProgressFinishNotificationProcPtr! ``` |

Modified DREraseSessionProgressCallbacks.progressWillBegin

|  | Declaration |
| --- | --- |
| From | ``` var progressWillBegin: DREraseSessionProgressBeginNotificationProcPtr! ``` |
| To | ``` var progressWillBegin: DiscRecordingUI.DREraseSessionProgressBeginNotificationProcPtr! ``` |

Modified DREraseSessionSetupCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DREraseSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr!     var containsSuitableMedia: DREraseSessionMediaCheckProcPtr!     var deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr!     init()     init(version version: UInt32, deviceShouldBeTarget deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr!, containsSuitableMedia containsSuitableMedia: DREraseSessionMediaCheckProcPtr!, deviceSelectionChanged deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr!) } ``` |
| To | ``` struct DREraseSessionSetupCallbacks {     var version: UInt32     var deviceShouldBeTarget: DiscRecordingUI.DREraseSessionDeviceCheckProcPtr!     var containsSuitableMedia: DiscRecordingUI.DREraseSessionMediaCheckProcPtr!     var deviceSelectionChanged: DiscRecordingUI.DREraseSessionDeviceSelectionNotificationProcPtr!     init()     init(version version: UInt32, deviceShouldBeTarget deviceShouldBeTarget: DiscRecordingUI.DREraseSessionDeviceCheckProcPtr!, containsSuitableMedia containsSuitableMedia: DiscRecordingUI.DREraseSessionMediaCheckProcPtr!, deviceSelectionChanged deviceSelectionChanged: DiscRecordingUI.DREraseSessionDeviceSelectionNotificationProcPtr!) } ``` |

Modified DREraseSessionSetupCallbacks.containsSuitableMedia

|  | Declaration |
| --- | --- |
| From | ``` var containsSuitableMedia: DREraseSessionMediaCheckProcPtr! ``` |
| To | ``` var containsSuitableMedia: DiscRecordingUI.DREraseSessionMediaCheckProcPtr! ``` |

Modified DREraseSessionSetupCallbacks.deviceSelectionChanged

|  | Declaration |
| --- | --- |
| From | ``` var deviceSelectionChanged: DREraseSessionDeviceSelectionNotificationProcPtr! ``` |
| To | ``` var deviceSelectionChanged: DiscRecordingUI.DREraseSessionDeviceSelectionNotificationProcPtr! ``` |

Modified DREraseSessionSetupCallbacks.deviceShouldBeTarget

|  | Declaration |
| --- | --- |
| From | ``` var deviceShouldBeTarget: DREraseSessionDeviceCheckProcPtr! ``` |
| To | ``` var deviceShouldBeTarget: DiscRecordingUI.DREraseSessionDeviceCheckProcPtr! ``` |

Modified DREraseSetupPanel

|  | Declaration |
| --- | --- |
| From | ``` class DREraseSetupPanel : DRSetupPanel {      init!()     class func setupPanel() -> DREraseSetupPanel!     func eraseObject() -> DRErase!     @IBAction func eraseType(_ sender: AnyObject!) } ``` |
| To | ``` class DREraseSetupPanel : DRSetupPanel {      init!()     class func setupPanel() -> DREraseSetupPanel!     func eraseObject() -> DRErase!     @IBAction func eraseType(_ sender: Any!) } ``` |

Modified DREraseSetupPanel.eraseType(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func eraseType(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func eraseType(_ sender: Any!) ``` |

Modified DRSetupPanel

|  | Declaration |
| --- | --- |
| From | ``` class DRSetupPanel : NSPanel {     init!(nibName nibName: String!)     func runSetupPanel() -> Int     func beginSetupSheetForWindow(_ owner: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     @IBAction func ok(_ sender: AnyObject!)     @IBAction func cancel(_ sender: AnyObject!)     @IBAction func eject(_ sender: AnyObject!)     @IBAction func open(_ sender: AnyObject!)     @IBAction func close(_ sender: AnyObject!)     func deviceSelectionChanged(_ device: DRDevice!)     func mediaStateChanged(_ status: [NSObject : AnyObject]!) -> Bool     func setupForDisplay() } ``` |
| To | ``` class DRSetupPanel : NSPanel {     init!(nibName nibName: String!)     func run() -> Int     func beginSetupSheet(for owner: NSWindow!, modalDelegate modalDelegate: Any!, didEnd didEndSelector: Selector!, contextInfo contextInfo: UnsafeMutableRawPointer!)     @IBAction func ok(_ sender: Any!)     @IBAction func cancel(_ sender: Any!)     @IBAction func eject(_ sender: Any!)     @IBAction func open(_ sender: Any!)     @IBAction func close(_ sender: Any!)     func deviceSelectionChanged(_ device: DRDevice!)     func mediaStateChanged(_ status: [AnyHashable : Any]!) -> Bool     func setupForDisplay() } ``` |

Modified DRSetupPanel.beginSetupSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func beginSetupSheetForWindow(_ owner: NSWindow!, modalDelegate modalDelegate: AnyObject!, didEndSelector didEndSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func beginSetupSheet(for owner: NSWindow!, modalDelegate modalDelegate: Any!, didEnd didEndSelector: Selector!, contextInfo contextInfo: UnsafeMutableRawPointer!) ``` |

Modified DRSetupPanel.cancel(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func cancel(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func cancel(_ sender: Any!) ``` |

Modified DRSetupPanel.close(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func close(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func close(_ sender: Any!) ``` |

Modified DRSetupPanel.eject(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func eject(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func eject(_ sender: Any!) ``` |

Modified DRSetupPanel.mediaStateChanged(_: [AnyHashable : Any]!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func mediaStateChanged(_ status: [NSObject : AnyObject]!) -> Bool ``` |
| To | ``` func mediaStateChanged(_ status: [AnyHashable : Any]!) -> Bool ``` |

Modified DRSetupPanel.ok(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func ok(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func ok(_ sender: Any!) ``` |

Modified DRSetupPanel.open(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func open(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func open(_ sender: Any!) ``` |

Modified DRSetupPanel.run() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func runSetupPanel() -> Int ``` |
| To | ``` func run() -> Int ``` |

Modified NSNotification.Name.DRBurnProgressPanelDidFinish

|  | Name | Declaration |
| --- | --- | --- |
| From | DRBurnProgressPanelDidFinishNotification | ``` let DRBurnProgressPanelDidFinishNotification: String ``` |
| To | DRBurnProgressPanelDidFinish | ``` static let DRBurnProgressPanelDidFinish: NSNotification.Name ``` |

Modified NSNotification.Name.DRBurnProgressPanelWillBegin

|  | Name | Declaration |
| --- | --- | --- |
| From | DRBurnProgressPanelWillBeginNotification | ``` let DRBurnProgressPanelWillBeginNotification: String ``` |
| To | DRBurnProgressPanelWillBegin | ``` static let DRBurnProgressPanelWillBegin: NSNotification.Name ``` |

Modified NSNotification.Name.DREraseProgressPanelDidFinish

|  | Name | Declaration |
| --- | --- | --- |
| From | DREraseProgressPanelDidFinishNotification | ``` let DREraseProgressPanelDidFinishNotification: String ``` |
| To | DREraseProgressPanelDidFinish | ``` static let DREraseProgressPanelDidFinish: NSNotification.Name ``` |

Modified NSNotification.Name.DREraseProgressPanelWillBegin

|  | Name | Declaration |
| --- | --- | --- |
| From | DREraseProgressPanelWillBeginNotification | ``` let DREraseProgressPanelWillBeginNotification: String ``` |
| To | DREraseProgressPanelWillBegin | ``` static let DREraseProgressPanelWillBegin: NSNotification.Name ``` |

Modified NSNotification.Name.DRSetupPanelDeviceSelectionChanged

|  | Name | Declaration |
| --- | --- | --- |
| From | DRSetupPanelDeviceSelectionChangedNotification | ``` let DRSetupPanelDeviceSelectionChangedNotification: String ``` |
| To | DRSetupPanelDeviceSelectionChanged | ``` static let DRSetupPanelDeviceSelectionChanged: NSNotification.Name ``` |

Modified NSObject.burnProgressPanelDidFinish(_: Notification!)

|  | Declaration |
| --- | --- |
| From | ``` func burnProgressPanelDidFinish(_ aNotification: NSNotification!) ``` |
| To | ``` func burnProgressPanelDidFinish(_ aNotification: Notification!) ``` |

Modified NSObject.burnProgressPanelWillBegin(_: Notification!)

|  | Declaration |
| --- | --- |
| From | ``` func burnProgressPanelWillBegin(_ aNotification: NSNotification!) ``` |
| To | ``` func burnProgressPanelWillBegin(_ aNotification: Notification!) ``` |

Modified NSObject.eraseProgressPanelDidFinish(_: Notification!)

|  | Declaration |
| --- | --- |
| From | ``` func eraseProgressPanelDidFinish(_ aNotification: NSNotification!) ``` |
| To | ``` func eraseProgressPanelDidFinish(_ aNotification: Notification!) ``` |

Modified NSObject.eraseProgressPanelWillBegin(_: Notification!)

|  | Declaration |
| --- | --- |
| From | ``` func eraseProgressPanelWillBegin(_ aNotification: NSNotification!) ``` |
| To | ``` func eraseProgressPanelWillBegin(_ aNotification: Notification!) ``` |

Modified NSObject.setupPanel(_: DRSetupPanel!, deviceContainsSuitableMedia: DRDevice!, promptString: AutoreleasingUnsafeMutablePointer<NSString?>!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func setupPanel(_ aPanel: DRSetupPanel!, deviceContainsSuitableMedia device: DRDevice!, promptString prompt: AutoreleasingUnsafeMutablePointer<NSString?>) -> Bool ``` |
| To | ``` func setupPanel(_ aPanel: DRSetupPanel!, deviceContainsSuitableMedia device: DRDevice!, promptString prompt: AutoreleasingUnsafeMutablePointer<NSString?>!) -> Bool ``` |

Modified NSObject.setupPanelDeviceSelectionChanged(_: Notification!)

|  | Declaration |
| --- | --- |
| From | ``` func setupPanelDeviceSelectionChanged(_ aNotification: NSNotification!) ``` |
| To | ``` func setupPanelDeviceSelectionChanged(_ aNotification: Notification!) ``` |

Modified DRBurnSessionBeginProgressDialog(_: DRBurnSession!, _: CFTypeRef!, _: UnsafeMutablePointer<DRBurnSessionProgressDialogOptions>!, _: UnsafeMutablePointer<DRBurnSessionProgressCallbacks>!)

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnSessionBeginProgressDialog(_ burnSession: DRBurnSession!, _ layout: AnyObject!, _ options: UnsafeMutablePointer<DRBurnSessionProgressDialogOptions>, _ progressCallbacks: UnsafeMutablePointer<DRBurnSessionProgressCallbacks>) ``` |
| To | ``` func DRBurnSessionBeginProgressDialog(_ burnSession: DRBurnSession!, _ layout: CFTypeRef!, _ options: UnsafeMutablePointer<DRBurnSessionProgressDialogOptions>!, _ progressCallbacks: UnsafeMutablePointer<DRBurnSessionProgressCallbacks>!) ``` |

Modified DRBurnSessionBurnCompleteProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionBurnCompleteProcPtr = (DRBurnSession!, DRBurnRef!) -> DarwinBoolean ``` |
| To | ``` typealias DRBurnSessionBurnCompleteProcPtr = (DRBurnSession?, DRBurnRef?) -> DarwinBoolean ``` |

Modified DRBurnSessionDeviceCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionDeviceCheckProcPtr = (DRBurnSession!, DRDeviceRef!) -> DarwinBoolean ``` |
| To | ``` typealias DRBurnSessionDeviceCheckProcPtr = (DRBurnSession?, DRDeviceRef?) -> DarwinBoolean ``` |

Modified DRBurnSessionDeviceSelectionNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionDeviceSelectionNotificationProcPtr = (DRBurnSession!, DRDeviceRef!) -> Void ``` |
| To | ``` typealias DRBurnSessionDeviceSelectionNotificationProcPtr = (DRBurnSession?, DRDeviceRef?) -> Swift.Void ``` |

Modified DRBurnSessionMediaCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionMediaCheckProcPtr = (DRBurnSession!, DRDeviceRef!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> DarwinBoolean ``` |
| To | ``` typealias DRBurnSessionMediaCheckProcPtr = (DRBurnSession?, DRDeviceRef?, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> DarwinBoolean ``` |

Modified DRBurnSessionProgressBeginNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionProgressBeginNotificationProcPtr = (DRBurnSession!) -> Void ``` |
| To | ``` typealias DRBurnSessionProgressBeginNotificationProcPtr = (DRBurnSession?) -> Swift.Void ``` |

Modified DRBurnSessionProgressFinishNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionProgressFinishNotificationProcPtr = (DRBurnSession!) -> Void ``` |
| To | ``` typealias DRBurnSessionProgressFinishNotificationProcPtr = (DRBurnSession?) -> Swift.Void ``` |

Modified DRBurnSessionSetupDialog(_: DRBurnSession!, _: UnsafeMutablePointer<DRBurnSessionSetupDialogOptions>!, _: UnsafeMutablePointer<DRBurnSessionSetupCallbacks>!) -> Int8

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnSessionSetupDialog(_ burnSession: DRBurnSession!, _ options: UnsafeMutablePointer<DRBurnSessionSetupDialogOptions>, _ setupCallbacks: UnsafeMutablePointer<DRBurnSessionSetupCallbacks>) -> Int8 ``` |
| To | ``` func DRBurnSessionSetupDialog(_ burnSession: DRBurnSession!, _ options: UnsafeMutablePointer<DRBurnSessionSetupDialogOptions>!, _ setupCallbacks: UnsafeMutablePointer<DRBurnSessionSetupCallbacks>!) -> Int8 ``` |

Modified DREraseSessionBeginProgressDialog(_: DREraseSession!, _: UnsafeMutablePointer<DREraseSessionProgressDialogOptions>!, _: UnsafeMutablePointer<DREraseSessionProgressCallbacks>!)

|  | Declaration |
| --- | --- |
| From | ``` func DREraseSessionBeginProgressDialog(_ eraseSession: DREraseSession!, _ options: UnsafeMutablePointer<DREraseSessionProgressDialogOptions>, _ progressCallbacks: UnsafeMutablePointer<DREraseSessionProgressCallbacks>) ``` |
| To | ``` func DREraseSessionBeginProgressDialog(_ eraseSession: DREraseSession!, _ options: UnsafeMutablePointer<DREraseSessionProgressDialogOptions>!, _ progressCallbacks: UnsafeMutablePointer<DREraseSessionProgressCallbacks>!) ``` |

Modified DREraseSessionDeviceCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionDeviceCheckProcPtr = (DREraseSession!, DRDeviceRef!) -> DarwinBoolean ``` |
| To | ``` typealias DREraseSessionDeviceCheckProcPtr = (DREraseSession?, DRDeviceRef?) -> DarwinBoolean ``` |

Modified DREraseSessionDeviceSelectionNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionDeviceSelectionNotificationProcPtr = (DREraseSession!, DRDeviceRef!) -> Void ``` |
| To | ``` typealias DREraseSessionDeviceSelectionNotificationProcPtr = (DREraseSession?, DRDeviceRef?) -> Swift.Void ``` |

Modified DREraseSessionEraseCompleteProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionEraseCompleteProcPtr = (DREraseSession!, DREraseRef!) -> DarwinBoolean ``` |
| To | ``` typealias DREraseSessionEraseCompleteProcPtr = (DREraseSession?, DREraseRef?) -> DarwinBoolean ``` |

Modified DREraseSessionMediaCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionMediaCheckProcPtr = (DREraseSession!, DRDeviceRef!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> DarwinBoolean ``` |
| To | ``` typealias DREraseSessionMediaCheckProcPtr = (DREraseSession?, DRDeviceRef?, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> DarwinBoolean ``` |

Modified DREraseSessionProgressBeginNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionProgressBeginNotificationProcPtr = (DREraseSession!) -> Void ``` |
| To | ``` typealias DREraseSessionProgressBeginNotificationProcPtr = (DREraseSession?) -> Swift.Void ``` |

Modified DREraseSessionProgressFinishNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionProgressFinishNotificationProcPtr = (DREraseSession!) -> Void ``` |
| To | ``` typealias DREraseSessionProgressFinishNotificationProcPtr = (DREraseSession?) -> Swift.Void ``` |

Modified DREraseSessionSetupDialog(_: DREraseSession!, _: UnsafeMutablePointer<DREraseSessionSetupDialogOptions>!, _: UnsafeMutablePointer<DREraseSessionSetupCallbacks>!) -> Int8

|  | Declaration |
| --- | --- |
| From | ``` func DREraseSessionSetupDialog(_ eraseSession: DREraseSession!, _ options: UnsafeMutablePointer<DREraseSessionSetupDialogOptions>, _ setupCallbacks: UnsafeMutablePointer<DREraseSessionSetupCallbacks>) -> Int8 ``` |
| To | ``` func DREraseSessionSetupDialog(_ eraseSession: DREraseSession!, _ options: UnsafeMutablePointer<DREraseSessionSetupDialogOptions>!, _ setupCallbacks: UnsafeMutablePointer<DREraseSessionSetupCallbacks>!) -> Int8 ``` |

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
