---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/SafariServices.html
archived_at: '2026-07-18T02:55:37.281693Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# SafariServices Changes for Swift

### SafariServices

Added [SFContentBlockerManager.getStateOfContentBlocker(withIdentifier: String, completionHandler: (SFContentBlockerState?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/1639499-getstateofcontentblockerwithiden)Added [SFContentBlockerState](https://developer.apple.com/documentation/safariservices/sfcontentblockerstate)Added [SFContentBlockerState.isEnabled](https://developer.apple.com/documentation/safariservices/sfcontentblockerstate/1639520-isenabled)Added [SFErrorCode.loadingInterrupted](https://developer.apple.com/documentation/safariservices/sferror/code/loadinginterrupted)Added [SFErrorCode.noAttachmentFound](https://developer.apple.com/documentation/safariservices/sferror/code/noattachmentfound)Added [SFErrorCode.noExtensionFound](https://developer.apple.com/documentation/safariservices/sferrorcode/sferrornoextensionfound)Added [SFErrorDomain [enum]](https://developer.apple.com/documentation/safariservices/sferrorcode)Added [SFSafariViewController.preferredBarTintColor](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/2274394-preferredbartintcolor)Added [SFSafariViewController.preferredControlTintColor](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/2274393-preferredcontroltintcolor)Added [SFErrorDomain](https://developer.apple.com/documentation/safariservices/sferrordomain)Modified [SFContentBlockerErrorCode [enum]](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` enum SFContentBlockerErrorCode : Int {     case NoExtensionFound     case NoAttachmentFound     case LoadingInterrupted } ``` | -- |
| To | ``` enum SFContentBlockerErrorCode : Int {     case noExtensionFound     case noAttachmentFound     case loadingInterrupted } ``` | iOS 10.0 |

Modified [SFContentBlockerErrorCode.loadingInterrupted](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/sfcontentblockerloadinginterrupted)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` case LoadingInterrupted ``` | -- |
| To | ``` case loadingInterrupted ``` | iOS 10.0 |

Modified [SFContentBlockerErrorCode.noAttachmentFound](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/noattachmentfound)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` case NoAttachmentFound ``` | -- |
| To | ``` case noAttachmentFound ``` | iOS 10.0 |

Modified [SFContentBlockerErrorCode.noExtensionFound](https://developer.apple.com/documentation/safariservices/sfcontentblockererrorcode/sfcontentblockernoextensionfound)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` case NoExtensionFound ``` | -- |
| To | ``` case noExtensionFound ``` | iOS 10.0 |

Modified [SFContentBlockerManager](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SFContentBlockerManager : NSObject {     class func reloadContentBlockerWithIdentifier(_ identifier: String, completionHandler completionHandler: ((NSError?) -> Void)?) } ``` | -- |
| To | ``` class SFContentBlockerManager : NSObject {     class func reloadContentBlocker(withIdentifier identifier: String, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     class func getStateOfContentBlocker(withIdentifier identifier: String, completionHandler completionHandler: @escaping (SFContentBlockerState?, Error?) -> Swift.Void)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SFContentBlockerManager : CVarArg { } extension SFContentBlockerManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SFContentBlockerManager.reloadContentBlocker(withIdentifier: String, completionHandler: ( (Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/1620151-reloadcontentblocker)

|  | Declaration |
| --- | --- |
| From | ``` class func reloadContentBlockerWithIdentifier(_ identifier: String, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` class func reloadContentBlocker(withIdentifier identifier: String, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SFSafariViewController : UIViewController {     weak var delegate: SFSafariViewControllerDelegate?     convenience init()     convenience init(coder aDecoder: NSCoder)     convenience init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     init(URL URL: NSURL, entersReaderIfAvailable entersReaderIfAvailable: Bool)     convenience init(URL URL: NSURL) } ``` | -- |
| To | ``` class SFSafariViewController : UIViewController {     convenience init()     convenience init(coder aDecoder: NSCoder)     convenience init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?)     init(url URL: URL, entersReaderIfAvailable entersReaderIfAvailable: Bool)     convenience init(url URL: URL)     weak var delegate: SFSafariViewControllerDelegate?     var preferredBarTintColor: UIColor     var preferredControlTintColor: UIColor     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get }     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)     func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?     var transitionCoordinator: UIViewControllerTransitionCoordinator? { get }     var isModalInPopover: Bool     var contentSizeForViewInPopover: CGSize     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool)     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get }     var previewActionItems: [UIPreviewActionItem] { get }     func registerForPreviewing(with delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewing(withContext previewing: UIViewControllerPreviewing)     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get }     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand)     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get }     weak var transitioningDelegate: UIViewControllerTransitioningDelegate?     func updateViewConstraints()     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     var shouldAutomaticallyForwardAppearanceMethods: Bool { get }     func willMove(toParentViewController parent: UIViewController?)     func didMove(toParentViewController parent: UIViewController?)     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     var childViewControllerForStatusBarStyle: UIViewController? { get }     var childViewControllerForStatusBarHidden: UIViewController? { get }     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollection(forChildViewController childViewController: UIViewController) -> UITraitCollection?     var searchDisplayController: UISearchDisplayController? { get }     var isEditing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var editButtonItem: UIBarButtonItem { get }     class func attemptRotationToDeviceOrientation()     func shouldAutorotate(to toInterfaceOrientation: UIInterfaceOrientation) -> Bool     var shouldAutorotate: Bool { get }     var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }     var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotate(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didRotate(from fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func willAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotation(from fromInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SFSafariViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension SFSafariViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: UIViewControllerRestoration.Type?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func applicationFinishedRestoringState() } extension SFSafariViewController : CVarArg { } extension SFSafariViewController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSExtensionRequestHandling, UIStateRestoring |

Modified [SFSafariViewController.init(url: URL)](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/1621222-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(URL URL: NSURL) ``` |
| To | ``` convenience init(url URL: URL) ``` |

Modified [SFSafariViewController.init(url: URL, entersReaderIfAvailable: Bool)](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/1621221-init)

|  | Declaration |
| --- | --- |
| From | ``` init(URL URL: NSURL, entersReaderIfAvailable entersReaderIfAvailable: Bool) ``` |
| To | ``` init(url URL: URL, entersReaderIfAvailable entersReaderIfAvailable: Bool) ``` |

Modified [SFSafariViewControllerDelegate](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SFSafariViewControllerDelegate : NSObjectProtocol {     optional func safariViewController(_ controller: SFSafariViewController, activityItemsForURL URL: NSURL, title title: String?) -> [UIActivity]     optional func safariViewControllerDidFinish(_ controller: SFSafariViewController)     optional func safariViewController(_ controller: SFSafariViewController, didCompleteInitialLoad didLoadSuccessfully: Bool) } ``` |
| To | ``` protocol SFSafariViewControllerDelegate : NSObjectProtocol {     optional func safariViewController(_ controller: SFSafariViewController, activityItemsFor URL: URL, title title: String?) -> [UIActivity]     optional func safariViewControllerDidFinish(_ controller: SFSafariViewController)     optional func safariViewController(_ controller: SFSafariViewController, didCompleteInitialLoad didLoadSuccessfully: Bool) } ``` |

Modified [SFSafariViewControllerDelegate.safariViewController(_: SFSafariViewController, activityItemsFor: URL, title: String?) -> [UIActivity]](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/1621216-safariviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func safariViewController(_ controller: SFSafariViewController, activityItemsForURL URL: NSURL, title title: String?) -> [UIActivity] ``` |
| To | ``` optional func safariViewController(_ controller: SFSafariViewController, activityItemsFor URL: URL, title title: String?) -> [UIActivity] ``` |

Modified [SSReadingList](https://developer.apple.com/documentation/safariservices/ssreadinglist)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SSReadingList : NSObject {     class func defaultReadingList() -> SSReadingList?     init()     class func supportsURL(_ URL: NSURL) -> Bool     func addReadingListItemWithURL(_ URL: NSURL, title title: String?, previewText previewText: String?) throws } ``` | -- |
| To | ``` class SSReadingList : NSObject {     class func `default`() -> SSReadingList?     init()     class func supportsURL(_ URL: URL) -> Bool     func addItem(with URL: URL, title title: String?, previewText previewText: String?) throws     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SSReadingList : CVarArg { } extension SSReadingList : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SSReadingList.addItem(with: URL, title: String?, previewText: String?) throws](https://developer.apple.com/documentation/safariservices/ssreadinglist/1621226-additem)

|  | Declaration |
| --- | --- |
| From | ``` func addReadingListItemWithURL(_ URL: NSURL, title title: String?, previewText previewText: String?) throws ``` |
| To | ``` func addItem(with URL: URL, title title: String?, previewText previewText: String?) throws ``` |

Modified [SSReadingList.default() [class]](https://developer.apple.com/documentation/safariservices/ssreadinglist/1621220-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultReadingList() -> SSReadingList? ``` |
| To | ``` class func `default`() -> SSReadingList? ``` |

Modified [SSReadingList.supportsURL(_: URL) -> Bool [class]](https://developer.apple.com/documentation/safariservices/ssreadinglist/1621224-supportsurl)

|  | Declaration |
| --- | --- |
| From | ``` class func supportsURL(_ URL: NSURL) -> Bool ``` |
| To | ``` class func supportsURL(_ URL: URL) -> Bool ``` |

Modified [SSReadingListErrorCode [enum]](https://developer.apple.com/documentation/safariservices/ssreadinglisterror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum SSReadingListErrorCode : Int {     case URLSchemeNotAllowed } ``` |
| To | ``` enum SSReadingListErrorCode : Int {     case urlSchemeNotAllowed } ``` |

Modified [SSReadingListErrorCode.urlSchemeNotAllowed](https://developer.apple.com/documentation/safariservices/ssreadinglisterror/code/urlschemenotallowed)

|  | Declaration |
| --- | --- |
| From | ``` case URLSchemeNotAllowed ``` |
| To | ``` case urlSchemeNotAllowed ``` |

Modified [SFContentBlockerErrorDomain](https://developer.apple.com/documentation/safariservices/sfcontentblockererrordomain)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

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
