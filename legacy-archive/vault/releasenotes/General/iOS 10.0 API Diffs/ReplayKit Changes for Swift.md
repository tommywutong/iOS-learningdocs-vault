---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/ReplayKit.html
archived_at: '2026-07-18T02:55:37.163950Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# ReplayKit Changes for Swift

### ReplayKit

Added [NSExtensionContext.completeRequest(withBroadcast: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : NSCoding & NSObjectProtocol]?)](https://developer.apple.com/documentation/foundation/nsextensioncontext/2143167-completerequest)Added [NSExtensionContext.loadBroadcastingApplicationInfo(completion: (String, String, UIImage?) -> Swift.Void)](https://developer.apple.com/documentation/foundation/nsextensioncontext/1845240-loadbroadcastingapplicationinfow)Added [RPBroadcastActivityViewController](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller)Added [RPBroadcastActivityViewController.delegate](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/1771691-delegate)Added [RPBroadcastActivityViewController.load(handler: (RPBroadcastActivityViewController?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/1648331-loadbroadcastactivityviewcontrol)Added [RPBroadcastActivityViewControllerDelegate](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontrollerdelegate)Added [RPBroadcastActivityViewControllerDelegate.broadcastActivityViewController(_: RPBroadcastActivityViewController, didFinishWith: RPBroadcastController?, error: Error?)](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontrollerdelegate/1648323-broadcastactivityviewcontroller)Added [RPBroadcastConfiguration](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration)Added [RPBroadcastConfiguration.clipDuration](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration/1845249-clipduration)Added [RPBroadcastConfiguration.videoCompressionProperties](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration/1845248-videocompressionproperties)Added [RPBroadcastController](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller)Added [RPBroadcastController.broadcastExtensionBundleID](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143150-broadcastextensionbundleid)Added [RPBroadcastController.broadcastURL](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648337-broadcasturl)Added [RPBroadcastController.delegate](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143149-delegate)Added [RPBroadcastController.finishBroadcast(handler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648336-finishbroadcastwithhandler)Added [RPBroadcastController.isBroadcasting](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648332-broadcasting)Added [RPBroadcastController.isPaused](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143151-paused)Added [RPBroadcastController.pauseBroadcast()](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648333-pausebroadcast)Added [RPBroadcastController.resumeBroadcast()](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648335-resumebroadcast)Added [RPBroadcastController.serviceInfo](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/2143153-serviceinfo)Added [RPBroadcastController.startBroadcast(handler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/1648327-startbroadcastwithhandler)Added [RPBroadcastControllerDelegate](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate)Added [RPBroadcastControllerDelegate.broadcastController(_: RPBroadcastController, didFinishWithError: Error?)](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/1648328-broadcastcontroller)Added [RPBroadcastControllerDelegate.broadcastController(_: RPBroadcastController, didUpdateServiceInfo: [String : NSCoding & NSObjectProtocol])](https://developer.apple.com/documentation/replaykit/rpbroadcastcontrollerdelegate/2143152-broadcastcontroller)Added [RPBroadcastHandler](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler)Added [RPBroadcastHandler.updateServiceInfo(_: [String : NSCoding & NSObjectProtocol])](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler/2143171-updateserviceinfo)Added [RPBroadcastMP4ClipHandler](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler)Added [RPBroadcastMP4ClipHandler.finishedProcessingMP4Clip(withUpdatedBroadcastConfiguration: RPBroadcastConfiguration?, error: Error?)](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler/2097558-finishedprocessingmp4clipwithupd)Added [RPBroadcastMP4ClipHandler.processMP4Clip(with: URL?, setupInfo: [String : NSObject]?, finished: Bool)](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler/2143172-processmp4clip)Added [RPBroadcastSampleHandler](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler)Added [RPBroadcastSampleHandler.broadcastFinished()](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143169-broadcastfinished)Added [RPBroadcastSampleHandler.broadcastPaused()](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143174-broadcastpaused)Added [RPBroadcastSampleHandler.broadcastResumed()](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143168-broadcastresumed)Added [RPBroadcastSampleHandler.broadcastStarted(withSetupInfo: [String : NSObject]?)](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2143170-broadcaststarted)Added [RPBroadcastSampleHandler.processSampleBuffer(_: CMSampleBuffer, with: RPSampleBufferType)](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler/2123045-processsamplebuffer)Added [RPPreviewViewControllerMode [enum]](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollermode)Added [RPPreviewViewControllerMode.preview](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollermode/rppreviewviewcontrollermodepreview)Added [RPPreviewViewControllerMode.share](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollermode/share)Added [RPRecordingErrorCode.broadcastInvalidSession](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/broadcastinvalidsession)Added [RPRecordingErrorCode.systemDormancy](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorsystemdormancy)Added [RPSampleBufferType [enum]](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype)Added [RPSampleBufferType.audioApp](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype/rpsamplebuffertypeaudioapp)Added [RPSampleBufferType.audioMic](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype/audiomic)Added [RPSampleBufferType.video](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype/rpsamplebuffertypevideo)Added [RPScreenRecorder.cameraPreviewView](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1649023-camerapreviewview)Added [RPScreenRecorder.isCameraEnabled](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1649024-iscameraenabled)Added [RPScreenRecorder.startRecording(handler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1649019-startrecordingwithhandler)Modified [RPPreviewViewController](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class RPPreviewViewController : UIViewController {     weak var previewControllerDelegate: RPPreviewViewControllerDelegate? } ``` | -- |
| To | ``` class RPPreviewViewController : UIViewController {     weak var previewControllerDelegate: RPPreviewViewControllerDelegate?     var mode: RPPreviewViewControllerMode     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get }     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)     func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?     var transitionCoordinator: UIViewControllerTransitionCoordinator? { get }     var isModalInPopover: Bool     var contentSizeForViewInPopover: CGSize     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool)     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get }     var previewActionItems: [UIPreviewActionItem] { get }     func registerForPreviewing(with delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewing(withContext previewing: UIViewControllerPreviewing)     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get }     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand)     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get }     weak var transitioningDelegate: UIViewControllerTransitioningDelegate?     func updateViewConstraints()     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     var shouldAutomaticallyForwardAppearanceMethods: Bool { get }     func willMove(toParentViewController parent: UIViewController?)     func didMove(toParentViewController parent: UIViewController?)     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     var childViewControllerForStatusBarStyle: UIViewController? { get }     var childViewControllerForStatusBarHidden: UIViewController? { get }     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollection(forChildViewController childViewController: UIViewController) -> UITraitCollection?     var searchDisplayController: UISearchDisplayController? { get }     var isEditing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var editButtonItem: UIBarButtonItem { get }     class func attemptRotationToDeviceOrientation()     func shouldAutorotate(to toInterfaceOrientation: UIInterfaceOrientation) -> Bool     var shouldAutorotate: Bool { get }     var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }     var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotate(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didRotate(from fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func willAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotation(from fromInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension RPPreviewViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension RPPreviewViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: UIViewControllerRestoration.Type?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func applicationFinishedRestoringState() } extension RPPreviewViewController : CVarArg { } extension RPPreviewViewController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSExtensionRequestHandling, UIStateRestoring |

Modified [RPRecordingErrorCode [enum]](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum RPRecordingErrorCode : Int {     case Unknown     case UserDeclined     case Disabled     case FailedToStart     case Failed     case InsufficientStorage     case Interrupted     case ContentResize } ``` |
| To | ``` enum RPRecordingErrorCode : Int {     case unknown     case userDeclined     case disabled     case failedToStart     case failed     case insufficientStorage     case interrupted     case contentResize     case broadcastInvalidSession     case systemDormancy } ``` |

Modified [RPRecordingErrorCode.contentResize](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorcontentresize)

|  | Declaration |
| --- | --- |
| From | ``` case ContentResize ``` |
| To | ``` case contentResize ``` |

Modified [RPRecordingErrorCode.disabled](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrordisabled)

|  | Declaration |
| --- | --- |
| From | ``` case Disabled ``` |
| To | ``` case disabled ``` |

Modified [RPRecordingErrorCode.failed](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorfailed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [RPRecordingErrorCode.failedToStart](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorfailedtostart)

|  | Declaration |
| --- | --- |
| From | ``` case FailedToStart ``` |
| To | ``` case failedToStart ``` |

Modified [RPRecordingErrorCode.insufficientStorage](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/insufficientstorage)

|  | Declaration |
| --- | --- |
| From | ``` case InsufficientStorage ``` |
| To | ``` case insufficientStorage ``` |

Modified [RPRecordingErrorCode.interrupted](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorinterrupted)

|  | Declaration |
| --- | --- |
| From | ``` case Interrupted ``` |
| To | ``` case interrupted ``` |

Modified [RPRecordingErrorCode.unknown](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/rprecordingerrorunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [RPRecordingErrorCode.userDeclined](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode/userdeclined)

|  | Declaration |
| --- | --- |
| From | ``` case UserDeclined ``` |
| To | ``` case userDeclined ``` |

Modified [RPScreenRecorder](https://developer.apple.com/documentation/replaykit/rpscreenrecorder)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class RPScreenRecorder : NSObject {     class func sharedRecorder() -> RPScreenRecorder     init?()     class func new() -> Self?     func startRecordingWithMicrophoneEnabled(_ microphoneEnabled: Bool, handler handler: ((NSError?) -> Void)?)     func stopRecordingWithHandler(_ handler: ((RPPreviewViewController?, NSError?) -> Void)?)     func discardRecordingWithHandler(_ handler: () -> Void)     weak var delegate: RPScreenRecorderDelegate?     var recording: Bool { get }     var microphoneEnabled: Bool { get }     var available: Bool { get } } ``` | -- |
| To | ``` class RPScreenRecorder : NSObject {     class func shared() -> RPScreenRecorder     init()     func startRecording(withMicrophoneEnabled microphoneEnabled: Bool, handler handler: (@escaping (Error?) -> Swift.Void)? = nil)     func startRecording(handler handler: (@escaping (Error?) -> Swift.Void)? = nil)     func stopRecording(handler handler: (@escaping (RPPreviewViewController?, Error?) -> Swift.Void)? = nil)     func discardRecording(handler handler: @escaping () -> Swift.Void)     weak var delegate: RPScreenRecorderDelegate?     var isAvailable: Bool { get }     var isRecording: Bool { get }     var isMicrophoneEnabled: Bool     var isCameraEnabled: Bool     var cameraPreviewView: UIView? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension RPScreenRecorder : CVarArg { } extension RPScreenRecorder : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [RPScreenRecorder.discardRecording(handler: () -> Swift.Void)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620994-discardrecordingwithhandler)

|  | Declaration |
| --- | --- |
| From | ``` func discardRecordingWithHandler(_ handler: () -> Void) ``` |
| To | ``` func discardRecording(handler handler: @escaping () -> Swift.Void) ``` |

Modified [RPScreenRecorder.isAvailable](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620992-isavailable)

|  | Declaration |
| --- | --- |
| From | ``` var available: Bool { get } ``` |
| To | ``` var isAvailable: Bool { get } ``` |

Modified [RPScreenRecorder.isMicrophoneEnabled](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620987-ismicrophoneenabled)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` var microphoneEnabled: Bool { get } ``` | yes |
| To | ``` var isMicrophoneEnabled: Bool ``` | -- |

Modified [RPScreenRecorder.isRecording](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620981-recording)

|  | Declaration |
| --- | --- |
| From | ``` var recording: Bool { get } ``` |
| To | ``` var isRecording: Bool { get } ``` |

Modified [RPScreenRecorder.shared() -> RPScreenRecorder [class]](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620993-sharedrecorder)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedRecorder() -> RPScreenRecorder ``` |
| To | ``` class func shared() -> RPScreenRecorder ``` |

Modified [RPScreenRecorder.startRecording(withMicrophoneEnabled: Bool, handler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620979-startrecording)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func startRecordingWithMicrophoneEnabled(_ microphoneEnabled: Bool, handler handler: ((NSError?) -> Void)?) ``` | -- |
| To | ``` func startRecording(withMicrophoneEnabled microphoneEnabled: Bool, handler handler: (@escaping (Error?) -> Swift.Void)? = nil) ``` | iOS 10.0 |

Modified [RPScreenRecorder.stopRecording(handler: ( (RPPreviewViewController?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/1620990-stoprecordingwithhandler)

|  | Declaration |
| --- | --- |
| From | ``` func stopRecordingWithHandler(_ handler: ((RPPreviewViewController?, NSError?) -> Void)?) ``` |
| To | ``` func stopRecording(handler handler: (@escaping (RPPreviewViewController?, Error?) -> Swift.Void)? = nil) ``` |

Modified [RPScreenRecorderDelegate](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol RPScreenRecorderDelegate : NSObjectProtocol {     optional func screenRecorder(_ screenRecorder: RPScreenRecorder, didStopRecordingWithError error: NSError, previewViewController previewViewController: RPPreviewViewController?)     optional func screenRecorderDidChangeAvailability(_ screenRecorder: RPScreenRecorder) } ``` |
| To | ``` protocol RPScreenRecorderDelegate : NSObjectProtocol {     optional func screenRecorder(_ screenRecorder: RPScreenRecorder, didStopRecordingWithError error: Error, previewViewController previewViewController: RPPreviewViewController?)     optional func screenRecorderDidChangeAvailability(_ screenRecorder: RPScreenRecorder) } ``` |

Modified [RPScreenRecorderDelegate.screenRecorder(_: RPScreenRecorder, didStopRecordingWithError: Error, previewViewController: RPPreviewViewController?)](https://developer.apple.com/documentation/replaykit/rpscreenrecorderdelegate/1620983-screenrecorder)

|  | Declaration |
| --- | --- |
| From | ``` optional func screenRecorder(_ screenRecorder: RPScreenRecorder, didStopRecordingWithError error: NSError, previewViewController previewViewController: RPPreviewViewController?) ``` |
| To | ``` optional func screenRecorder(_ screenRecorder: RPScreenRecorder, didStopRecordingWithError error: Error, previewViewController previewViewController: RPPreviewViewController?) ``` |

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
