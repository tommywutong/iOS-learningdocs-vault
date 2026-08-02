---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/AVKit.html
archived_at: '2026-07-18T02:55:02.522769Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# AVKit Changes for Swift

### AVKit

Added [AVKitError [struct]](https://developer.apple.com/documentation/avkit/avkiterror)Added AVKitError.init(_nsError: NSError)Added [AVKitError.pictureInPictureStartFailed](https://developer.apple.com/documentation/avkit/avkiterror/2335363-pictureinpicturestartfailed)Added [AVKitError.unknown](https://developer.apple.com/documentation/avkit/avkiterror/2335355-unknown)Added [AVPlayerViewController.updatesNowPlayingInfoCenter](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1845194-updatesnowplayinginfocenter)Modified [AVKitError.Code [enum]](https://developer.apple.com/documentation/avkit/avkiterror)

|  | Declaration |
| --- | --- |
| From | ``` enum AVKitError : Int {     case Unknown     case PictureInPictureStartFailed } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = AVKitError         case unknown         case pictureInPictureStartFailed     } ``` |

Modified [AVKitError.Code.pictureInPictureStartFailed](https://developer.apple.com/documentation/avkit/avkiterror/avkiterrorpictureinpicturestartfailed)

|  | Declaration |
| --- | --- |
| From | ``` case PictureInPictureStartFailed ``` |
| To | ``` case pictureInPictureStartFailed ``` |

Modified [AVKitError.Code.unknown](https://developer.apple.com/documentation/avkit/avkiterror/code/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [AVPictureInPictureController](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPictureInPictureController : NSObject {     class func isPictureInPictureSupported() -> Bool     class func pictureInPictureButtonStartImageCompatibleWithTraitCollection(_ traitCollection: UITraitCollection?) -> UIImage     class func pictureInPictureButtonStopImageCompatibleWithTraitCollection(_ traitCollection: UITraitCollection?) -> UIImage     init?(playerLayer playerLayer: AVPlayerLayer)     var playerLayer: AVPlayerLayer { get }     weak var delegate: AVPictureInPictureControllerDelegate?     func startPictureInPicture()     func stopPictureInPicture()     var pictureInPicturePossible: Bool { get }     var pictureInPictureActive: Bool { get }     var pictureInPictureSuspended: Bool { get } } ``` | -- |
| To | ``` class AVPictureInPictureController : NSObject {     class func isPictureInPictureSupported() -> Bool     class func pictureInPictureButtonStartImage(compatibleWith traitCollection: UITraitCollection?) -> UIImage     class func pictureInPictureButtonStopImage(compatibleWith traitCollection: UITraitCollection?) -> UIImage     init?(playerLayer playerLayer: AVPlayerLayer)     var playerLayer: AVPlayerLayer { get }     weak var delegate: AVPictureInPictureControllerDelegate?     func startPictureInPicture()     func stopPictureInPicture()     var isPictureInPicturePossible: Bool { get }     var isPictureInPictureActive: Bool { get }     var isPictureInPictureSuspended: Bool { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension AVPictureInPictureController : CVarArg { } extension AVPictureInPictureController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AVPictureInPictureController.isPictureInPictureActive](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614720-ispictureinpictureactive)

|  | Declaration |
| --- | --- |
| From | ``` var pictureInPictureActive: Bool { get } ``` |
| To | ``` var isPictureInPictureActive: Bool { get } ``` |

Modified [AVPictureInPictureController.isPictureInPicturePossible](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614691-ispictureinpicturepossible)

|  | Declaration |
| --- | --- |
| From | ``` var pictureInPicturePossible: Bool { get } ``` |
| To | ``` var isPictureInPicturePossible: Bool { get } ``` |

Modified [AVPictureInPictureController.isPictureInPictureSuspended](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614689-pictureinpicturesuspended)

|  | Declaration |
| --- | --- |
| From | ``` var pictureInPictureSuspended: Bool { get } ``` |
| To | ``` var isPictureInPictureSuspended: Bool { get } ``` |

Modified [AVPictureInPictureController.pictureInPictureButtonStartImage(compatibleWith: UITraitCollection?) -> UIImage [class]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614699-pictureinpicturebuttonstartimage)

|  | Declaration |
| --- | --- |
| From | ``` class func pictureInPictureButtonStartImageCompatibleWithTraitCollection(_ traitCollection: UITraitCollection?) -> UIImage ``` |
| To | ``` class func pictureInPictureButtonStartImage(compatibleWith traitCollection: UITraitCollection?) -> UIImage ``` |

Modified [AVPictureInPictureController.pictureInPictureButtonStopImage(compatibleWith: UITraitCollection?) -> UIImage [class]](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/1614713-pictureinpicturebuttonstopimagec)

|  | Declaration |
| --- | --- |
| From | ``` class func pictureInPictureButtonStopImageCompatibleWithTraitCollection(_ traitCollection: UITraitCollection?) -> UIImage ``` |
| To | ``` class func pictureInPictureButtonStopImage(compatibleWith traitCollection: UITraitCollection?) -> UIImage ``` |

Modified [AVPictureInPictureControllerDelegate](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVPictureInPictureControllerDelegate : NSObjectProtocol {     optional func pictureInPictureControllerWillStartPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)     optional func pictureInPictureControllerDidStartPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)     optional func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, failedToStartPictureInPictureWithError error: NSError)     optional func pictureInPictureControllerWillStopPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)     optional func pictureInPictureControllerDidStopPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)     optional func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: (Bool) -> Void) } ``` |
| To | ``` protocol AVPictureInPictureControllerDelegate : NSObjectProtocol {     optional func pictureInPictureControllerWillStartPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)     optional func pictureInPictureControllerDidStartPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)     optional func picture(_ pictureInPictureController: AVPictureInPictureController, failedToStartPictureInPictureWithError error: Error)     optional func pictureInPictureControllerWillStopPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)     optional func pictureInPictureControllerDidStopPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)     optional func picture(_ pictureInPictureController: AVPictureInPictureController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: @escaping (Bool) -> Swift.Void) } ``` |

Modified [AVPictureInPictureControllerDelegate.picture(_: AVPictureInPictureController, failedToStartPictureInPictureWithError: Error)](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/1614697-picture)

|  | Declaration |
| --- | --- |
| From | ``` optional func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, failedToStartPictureInPictureWithError error: NSError) ``` |
| To | ``` optional func picture(_ pictureInPictureController: AVPictureInPictureController, failedToStartPictureInPictureWithError error: Error) ``` |

Modified [AVPictureInPictureControllerDelegate.picture(_: AVPictureInPictureController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Swift.Void)](https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/1614703-pictureinpicturecontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: (Bool) -> Void) ``` |
| To | ``` optional func picture(_ pictureInPictureController: AVPictureInPictureController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: @escaping (Bool) -> Swift.Void) ``` |

Modified [AVPlayerViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVPlayerViewController : UIViewController {     var player: AVPlayer?     var showsPlaybackControls: Bool     var videoGravity: String     var readyForDisplay: Bool { get }     var videoBounds: CGRect { get }     var contentOverlayView: UIView? { get }     var allowsPictureInPicturePlayback: Bool     weak var delegate: AVPlayerViewControllerDelegate? } extension AVPlayerViewController {     class func preparePrerollAds()     func playPrerollAdWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     func cancelPreroll() } ``` | -- |
| To | ``` class AVPlayerViewController : UIViewController {     var player: AVPlayer?     var showsPlaybackControls: Bool     var videoGravity: String     var isReadyForDisplay: Bool { get }     var videoBounds: CGRect { get }     var contentOverlayView: UIView? { get }     var allowsPictureInPicturePlayback: Bool     var updatesNowPlayingInfoCenter: Bool     weak var delegate: AVPlayerViewControllerDelegate?     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get }     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)     func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?     var transitionCoordinator: UIViewControllerTransitionCoordinator? { get }     var isModalInPopover: Bool     var contentSizeForViewInPopover: CGSize     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool)     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get }     var previewActionItems: [UIPreviewActionItem] { get }     func registerForPreviewing(with delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewing(withContext previewing: UIViewControllerPreviewing)     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get }     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand)     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get }     weak var transitioningDelegate: UIViewControllerTransitioningDelegate?     func updateViewConstraints()     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     var shouldAutomaticallyForwardAppearanceMethods: Bool { get }     func willMove(toParentViewController parent: UIViewController?)     func didMove(toParentViewController parent: UIViewController?)     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     var childViewControllerForStatusBarStyle: UIViewController? { get }     var childViewControllerForStatusBarHidden: UIViewController? { get }     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollection(forChildViewController childViewController: UIViewController) -> UITraitCollection?     var searchDisplayController: UISearchDisplayController? { get }     var isEditing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var editButtonItem: UIBarButtonItem { get }     class func attemptRotationToDeviceOrientation()     func shouldAutorotate(to toInterfaceOrientation: UIInterfaceOrientation) -> Bool     var shouldAutorotate: Bool { get }     var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }     var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotate(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didRotate(from fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func willAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotation(from fromInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension AVPlayerViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension AVPlayerViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: UIViewControllerRestoration.Type?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func applicationFinishedRestoringState() } extension AVPlayerViewController : CVarArg { } extension AVPlayerViewController : Equatable, Hashable {     var hashValue: Int { get } } extension AVPlayerViewController {     class func preparePrerollAds()     func playPrerollAd(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)!)     func cancelPreroll() } ``` | CVarArg, Equatable, Hashable, NSExtensionRequestHandling, UIStateRestoring |

Modified [AVPlayerViewController.isReadyForDisplay](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1615830-isreadyfordisplay)

|  | Declaration |
| --- | --- |
| From | ``` var readyForDisplay: Bool { get } ``` |
| To | ``` var isReadyForDisplay: Bool { get } ``` |

Modified [AVPlayerViewControllerDelegate](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVPlayerViewControllerDelegate : NSObjectProtocol {     optional func playerViewControllerWillStartPictureInPicture(_ playerViewController: AVPlayerViewController)     optional func playerViewControllerDidStartPictureInPicture(_ playerViewController: AVPlayerViewController)     optional func playerViewController(_ playerViewController: AVPlayerViewController, failedToStartPictureInPictureWithError error: NSError)     optional func playerViewControllerWillStopPictureInPicture(_ playerViewController: AVPlayerViewController)     optional func playerViewControllerDidStopPictureInPicture(_ playerViewController: AVPlayerViewController)     optional func playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(_ playerViewController: AVPlayerViewController) -> Bool     optional func playerViewController(_ playerViewController: AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: (Bool) -> Void) } ``` |
| To | ``` protocol AVPlayerViewControllerDelegate : NSObjectProtocol {     optional func playerViewControllerWillStartPictureInPicture(_ playerViewController: AVPlayerViewController)     optional func playerViewControllerDidStartPictureInPicture(_ playerViewController: AVPlayerViewController)     optional func playerViewController(_ playerViewController: AVPlayerViewController, failedToStartPictureInPictureWithError error: Error)     optional func playerViewControllerWillStopPictureInPicture(_ playerViewController: AVPlayerViewController)     optional func playerViewControllerDidStopPictureInPicture(_ playerViewController: AVPlayerViewController)     optional func playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(_ playerViewController: AVPlayerViewController) -> Bool     optional func playerViewController(_ playerViewController: AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: @escaping (Bool) -> Swift.Void) } ``` |

Modified [AVPlayerViewControllerDelegate.playerViewController(_: AVPlayerViewController, failedToStartPictureInPictureWithError: Error)](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1615822-playerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func playerViewController(_ playerViewController: AVPlayerViewController, failedToStartPictureInPictureWithError error: NSError) ``` |
| To | ``` optional func playerViewController(_ playerViewController: AVPlayerViewController, failedToStartPictureInPictureWithError error: Error) ``` |

Modified [AVPlayerViewControllerDelegate.playerViewController(_: AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler: (Bool) -> Swift.Void)](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/1615838-playerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func playerViewController(_ playerViewController: AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: (Bool) -> Void) ``` |
| To | ``` optional func playerViewController(_ playerViewController: AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: @escaping (Bool) -> Swift.Void) ``` |

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
