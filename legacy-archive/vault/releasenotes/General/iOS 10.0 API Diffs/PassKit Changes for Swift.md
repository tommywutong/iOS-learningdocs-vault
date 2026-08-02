---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/PassKit.html
archived_at: '2026-07-18T02:55:35.732305Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# PassKit Changes for Swift

### PassKit

Removed [PKAddressField.None](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldnone)Removed PKPaymentMethodType.init(rawValue: UInt)Added [PKEncryptionScheme [struct]](https://developer.apple.com/documentation/passkit/pkencryptionscheme)Added [PKEncryptionScheme.init(rawValue: String)](https://developer.apple.com/documentation/passkit/pkencryptionscheme/2092172-init)Added [PKEncryptionScheme.RSA_V2](https://developer.apple.com/documentation/passkit/pkencryptionschemersa_v2)Added [PKPassKitError [struct]](https://developer.apple.com/documentation/passkit/pkpasskiterror)Added PKPassKitError.init(_nsError: NSError)Added [PKPassKitError.invalidDataError](https://developer.apple.com/documentation/passkit/pkpasskiterror/2320681-invaliddataerror)Added [PKPassKitError.invalidSignature](https://developer.apple.com/documentation/passkit/pkpasskiterror/2320680-invalidsignature)Added [PKPassKitError.notEntitledError](https://developer.apple.com/documentation/passkit/pkpasskiterror/2320679-notentitlederror)Added [PKPassKitError.unknownError](https://developer.apple.com/documentation/passkit/pkpasskiterror/2320682-unknownerror)Added [PKPassKitError.unsupportedVersionError](https://developer.apple.com/documentation/passkit/pkpasskiterror/2320678-unsupportedversionerror)Added [PKPassLibrary.present(_: PKPaymentPass)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1649554-presentpaymentpass)Added [PKPassLibraryNotificationKey [struct]](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey)Added [PKPassLibraryNotificationKey.init(rawValue: String)](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/2092173-init)Added [PKPassLibraryNotificationName [struct]](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname)Added [PKPassLibraryNotificationName.init(_: String)](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname/2092171-init)Added [PKPassLibraryNotificationName.init(rawValue: String)](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname/2092170-init)Added [PKPaymentAuthorizationController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller)Added [PKPaymentAuthorizationController.canMakePayments() -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649461-canmakepayments)Added [PKPaymentAuthorizationController.canMakePayments(usingNetworks: [PKPaymentNetwork]) -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649457-canmakepaymentsusingnetworks)Added [PKPaymentAuthorizationController.canMakePayments(usingNetworks: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649455-canmakepaymentsusingnetworks)Added [PKPaymentAuthorizationController.delegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649453-delegate)Added [PKPaymentAuthorizationController.dismiss(completion: ( () -> Swift.Void)?)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1771696-dismiss)Added [PKPaymentAuthorizationController.init(paymentRequest: PKPaymentRequest)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649462-init)Added [PKPaymentAuthorizationController.present(completion: ( (Bool) -> Swift.Void)?)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/1649463-presentwithcompletion)Added [PKPaymentAuthorizationControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationController(_: PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649454-paymentauthorizationcontroller)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationController(_: PKPaymentAuthorizationController, didSelectPaymentMethod: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649460-paymentauthorizationcontroller)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationController(_: PKPaymentAuthorizationController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649458-paymentauthorizationcontroller)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationController(_: PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649465-paymentauthorizationcontroller)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationControllerDidFinish(_: PKPaymentAuthorizationController)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649456-paymentauthorizationcontrollerdi)Added [PKPaymentAuthorizationControllerDelegate.paymentAuthorizationControllerWillAuthorizePayment(_: PKPaymentAuthorizationController)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/1649464-paymentauthorizationcontrollerwi)Added [PKPaymentButtonType.inStore](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/instore)Added [PKPaymentNetwork [struct]](https://developer.apple.com/documentation/passkit/pkpaymentnetwork)Added [PKPaymentNetwork.init(_: String)](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/2092169-init)Added [PKPaymentNetwork.init(rawValue: String)](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/2092174-init)Added [PKPaymentRequest.availableNetworks() -> [PKPaymentNetwork] [class]](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1833288-availablenetworks)Modified [PKAddPassButton](https://developer.apple.com/documentation/passkit/pkaddpassbutton)

|  | Declaration |
| --- | --- |
| From | ``` class PKAddPassButton : UIButton {     convenience init(style addPassButtonStyle: PKAddPassButtonStyle)     class func addPassButtonWithStyle(_ addPassButtonStyle: PKAddPassButtonStyle) -> Self     init(addPassButtonStyle style: PKAddPassButtonStyle)     var addPassButtonStyle: PKAddPassButtonStyle } ``` |
| To | ``` class PKAddPassButton : UIButton {     convenience init(style addPassButtonStyle: PKAddPassButtonStyle)     class func withStyle(_ addPassButtonStyle: PKAddPassButtonStyle) -> Self     init(addPassButtonStyle style: PKAddPassButtonStyle)     var addPassButtonStyle: PKAddPassButtonStyle     var font: UIFont     var lineBreakMode: NSLineBreakMode     var titleShadowOffset: CGSize } ``` |

Modified [PKAddPassButtonStyle [enum]](https://developer.apple.com/documentation/passkit/pkaddpassbuttonstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum PKAddPassButtonStyle : Int {     case Black     case BlackOutline } ``` |
| To | ``` enum PKAddPassButtonStyle : Int {     case black     case blackOutline } ``` |

Modified [PKAddPassButtonStyle.black](https://developer.apple.com/documentation/passkit/pkaddpassbuttonstyle/black)

|  | Declaration |
| --- | --- |
| From | ``` case Black ``` |
| To | ``` case black ``` |

Modified [PKAddPassButtonStyle.blackOutline](https://developer.apple.com/documentation/passkit/pkaddpassbuttonstyle/pkaddpassbuttonstyleblackoutline)

|  | Declaration |
| --- | --- |
| From | ``` case BlackOutline ``` |
| To | ``` case blackOutline ``` |

Modified [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKAddPassesViewController : UIViewController {     init(pass pass: PKPass)     init(passes passes: [PKPass])     class func canAddPasses() -> Bool     unowned(unsafe) var delegate: PKAddPassesViewControllerDelegate? } ``` | -- |
| To | ``` class PKAddPassesViewController : UIViewController {     init(pass pass: PKPass)     init(passes passes: [PKPass])     class func canAddPasses() -> Bool     unowned(unsafe) var delegate: PKAddPassesViewControllerDelegate?     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get }     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)     func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?     var transitionCoordinator: UIViewControllerTransitionCoordinator? { get }     var isModalInPopover: Bool     var contentSizeForViewInPopover: CGSize     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool)     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get }     var previewActionItems: [UIPreviewActionItem] { get }     func registerForPreviewing(with delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewing(withContext previewing: UIViewControllerPreviewing)     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get }     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand)     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get }     weak var transitioningDelegate: UIViewControllerTransitioningDelegate?     func updateViewConstraints()     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     var shouldAutomaticallyForwardAppearanceMethods: Bool { get }     func willMove(toParentViewController parent: UIViewController?)     func didMove(toParentViewController parent: UIViewController?)     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     var childViewControllerForStatusBarStyle: UIViewController? { get }     var childViewControllerForStatusBarHidden: UIViewController? { get }     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollection(forChildViewController childViewController: UIViewController) -> UITraitCollection?     var searchDisplayController: UISearchDisplayController? { get }     var isEditing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var editButtonItem: UIBarButtonItem { get }     class func attemptRotationToDeviceOrientation()     func shouldAutorotate(to toInterfaceOrientation: UIInterfaceOrientation) -> Bool     var shouldAutorotate: Bool { get }     var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }     var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotate(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didRotate(from fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func willAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotation(from fromInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKAddPassesViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension PKAddPassesViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: UIViewControllerRestoration.Type?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func applicationFinishedRestoringState() } extension PKAddPassesViewController : CVarArg { } extension PKAddPassesViewController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSExtensionRequestHandling, UIStateRestoring |

Modified [PKAddPaymentPassError [enum]](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror)

|  | Declaration |
| --- | --- |
| From | ``` enum PKAddPaymentPassError : Int {     case Unsupported     case UserCancelled     case SystemCancelled } ``` |
| To | ``` enum PKAddPaymentPassError : Int {     case unsupported     case userCancelled     case systemCancelled } ``` |

Modified [PKAddPaymentPassError.systemCancelled](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror/pkaddpaymentpasserrorsystemcancelled)

|  | Declaration |
| --- | --- |
| From | ``` case SystemCancelled ``` |
| To | ``` case systemCancelled ``` |

Modified [PKAddPaymentPassError.unsupported](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror/unsupported)

|  | Declaration |
| --- | --- |
| From | ``` case Unsupported ``` |
| To | ``` case unsupported ``` |

Modified [PKAddPaymentPassError.userCancelled](https://developer.apple.com/documentation/passkit/pkaddpaymentpasserror/usercancelled)

|  | Declaration |
| --- | --- |
| From | ``` case UserCancelled ``` |
| To | ``` case userCancelled ``` |

Modified [PKAddPaymentPassRequest](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKAddPaymentPassRequest : NSObject {     init()     @NSCopying var encryptedPassData: NSData?     @NSCopying var activationData: NSData?     @NSCopying var ephemeralPublicKey: NSData?     @NSCopying var wrappedKey: NSData? } ``` | -- |
| To | ``` class PKAddPaymentPassRequest : NSObject {     init()     var encryptedPassData: Data?     var activationData: Data?     var ephemeralPublicKey: Data?     var wrappedKey: Data?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKAddPaymentPassRequest : CVarArg { } extension PKAddPaymentPassRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKAddPaymentPassRequest.activationData](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615914-activationdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var activationData: NSData? ``` |
| To | ``` var activationData: Data? ``` |

Modified [PKAddPaymentPassRequest.encryptedPassData](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615926-encryptedpassdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var encryptedPassData: NSData? ``` |
| To | ``` var encryptedPassData: Data? ``` |

Modified [PKAddPaymentPassRequest.ephemeralPublicKey](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615952-ephemeralpublickey)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var ephemeralPublicKey: NSData? ``` |
| To | ``` var ephemeralPublicKey: Data? ``` |

Modified [PKAddPaymentPassRequest.wrappedKey](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest/1615950-wrappedkey)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var wrappedKey: NSData? ``` |
| To | ``` var wrappedKey: Data? ``` |

Modified [PKAddPaymentPassRequestConfiguration](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKAddPaymentPassRequestConfiguration : NSObject {     init?(encryptionScheme encryptionScheme: String)     var encryptionScheme: String { get }     var cardholderName: String?     var primaryAccountSuffix: String?     var localizedDescription: String?     var primaryAccountIdentifier: String?     var paymentNetwork: String? } ``` | -- |
| To | ``` class PKAddPaymentPassRequestConfiguration : NSObject {     init?(encryptionScheme encryptionScheme: PKEncryptionScheme)     var encryptionScheme: PKEncryptionScheme { get }     var cardholderName: String?     var primaryAccountSuffix: String?     var localizedDescription: String?     var primaryAccountIdentifier: String?     var paymentNetwork: PKPaymentNetwork?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKAddPaymentPassRequestConfiguration : CVarArg { } extension PKAddPaymentPassRequestConfiguration : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKAddPaymentPassRequestConfiguration.encryptionScheme](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615946-encryptionscheme)

|  | Declaration |
| --- | --- |
| From | ``` var encryptionScheme: String { get } ``` |
| To | ``` var encryptionScheme: PKEncryptionScheme { get } ``` |

Modified [PKAddPaymentPassRequestConfiguration.init(encryptionScheme: PKEncryptionScheme)](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615930-initwithencryptionscheme)

|  | Declaration |
| --- | --- |
| From | ``` init?(encryptionScheme encryptionScheme: String) ``` |
| To | ``` init?(encryptionScheme encryptionScheme: PKEncryptionScheme) ``` |

Modified [PKAddPaymentPassRequestConfiguration.paymentNetwork](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/1615948-paymentnetwork)

|  | Declaration |
| --- | --- |
| From | ``` var paymentNetwork: String? ``` |
| To | ``` var paymentNetwork: PKPaymentNetwork? ``` |

Modified [PKAddPaymentPassViewController](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKAddPaymentPassViewController : UIViewController {     class func canAddPaymentPass() -> Bool     init?(requestConfiguration configuration: PKAddPaymentPassRequestConfiguration, delegate delegate: PKAddPaymentPassViewControllerDelegate?)     weak var delegate: PKAddPaymentPassViewControllerDelegate? } ``` | -- |
| To | ``` class PKAddPaymentPassViewController : UIViewController {     class func canAddPaymentPass() -> Bool     init?(requestConfiguration configuration: PKAddPaymentPassRequestConfiguration, delegate delegate: PKAddPaymentPassViewControllerDelegate?)     weak var delegate: PKAddPaymentPassViewControllerDelegate?     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get }     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)     func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?     var transitionCoordinator: UIViewControllerTransitionCoordinator? { get }     var isModalInPopover: Bool     var contentSizeForViewInPopover: CGSize     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool)     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get }     var previewActionItems: [UIPreviewActionItem] { get }     func registerForPreviewing(with delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewing(withContext previewing: UIViewControllerPreviewing)     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get }     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand)     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get }     weak var transitioningDelegate: UIViewControllerTransitioningDelegate?     func updateViewConstraints()     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     var shouldAutomaticallyForwardAppearanceMethods: Bool { get }     func willMove(toParentViewController parent: UIViewController?)     func didMove(toParentViewController parent: UIViewController?)     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     var childViewControllerForStatusBarStyle: UIViewController? { get }     var childViewControllerForStatusBarHidden: UIViewController? { get }     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollection(forChildViewController childViewController: UIViewController) -> UITraitCollection?     var searchDisplayController: UISearchDisplayController? { get }     var isEditing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var editButtonItem: UIBarButtonItem { get }     class func attemptRotationToDeviceOrientation()     func shouldAutorotate(to toInterfaceOrientation: UIInterfaceOrientation) -> Bool     var shouldAutorotate: Bool { get }     var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }     var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotate(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didRotate(from fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func willAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotation(from fromInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKAddPaymentPassViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension PKAddPaymentPassViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: UIViewControllerRestoration.Type?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func applicationFinishedRestoringState() } extension PKAddPaymentPassViewController : CVarArg { } extension PKAddPaymentPassViewController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSExtensionRequestHandling, UIStateRestoring |

Modified [PKAddPaymentPassViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol PKAddPaymentPassViewControllerDelegate : NSObjectProtocol {     func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, generateRequestWithCertificateChain certificates: [NSData], nonce nonce: NSData, nonceSignature nonceSignature: NSData, completionHandler handler: (PKAddPaymentPassRequest) -> Void)     func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, didFinishAddingPaymentPass pass: PKPaymentPass?, error error: NSError?) } ``` |
| To | ``` protocol PKAddPaymentPassViewControllerDelegate : NSObjectProtocol {     func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, generateRequestWithCertificateChain certificates: [Data], nonce nonce: Data, nonceSignature nonceSignature: Data, completionHandler handler: @escaping (PKAddPaymentPassRequest) -> Swift.Void)     func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, didFinishAdding pass: PKPaymentPass?, error error: Error?) } ``` |

Modified [PKAddPaymentPassViewControllerDelegate.addPaymentPassViewController(_: PKAddPaymentPassViewController, didFinishAdding: PKPaymentPass?, error: Error?)](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate/1615942-addpaymentpassviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, didFinishAddingPaymentPass pass: PKPaymentPass?, error error: NSError?) ``` |
| To | ``` func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, didFinishAdding pass: PKPaymentPass?, error error: Error?) ``` |

Modified [PKAddPaymentPassViewControllerDelegate.addPaymentPassViewController(_: PKAddPaymentPassViewController, generateRequestWithCertificateChain: [Data], nonce: Data, nonceSignature: Data, completionHandler: (PKAddPaymentPassRequest) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate/1615915-addpaymentpassviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, generateRequestWithCertificateChain certificates: [NSData], nonce nonce: NSData, nonceSignature nonceSignature: NSData, completionHandler handler: (PKAddPaymentPassRequest) -> Void) ``` |
| To | ``` func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, generateRequestWithCertificateChain certificates: [Data], nonce nonce: Data, nonceSignature nonceSignature: Data, completionHandler handler: @escaping (PKAddPaymentPassRequest) -> Swift.Void) ``` |

Modified [PKAddressField [struct]](https://developer.apple.com/documentation/passkit/pkaddressfield)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PKAddressField : OptionSetType {     init(rawValue rawValue: UInt)     static var None: PKAddressField { get }     static var PostalAddress: PKAddressField { get }     static var Phone: PKAddressField { get }     static var Email: PKAddressField { get }     static var Name: PKAddressField { get }     static var All: PKAddressField { get } } ``` | OptionSetType |
| To | ``` struct PKAddressField : OptionSet {     init(rawValue rawValue: UInt)     static var none: PKAddressField { get }     static var postalAddress: PKAddressField { get }     static var phone: PKAddressField { get }     static var email: PKAddressField { get }     static var name: PKAddressField { get }     static var all: PKAddressField { get }     func intersect(_ other: PKAddressField) -> PKAddressField     func exclusiveOr(_ other: PKAddressField) -> PKAddressField     mutating func unionInPlace(_ other: PKAddressField)     mutating func intersectInPlace(_ other: PKAddressField)     mutating func exclusiveOrInPlace(_ other: PKAddressField)     func isSubsetOf(_ other: PKAddressField) -> Bool     func isDisjointWith(_ other: PKAddressField) -> Bool     func isSupersetOf(_ other: PKAddressField) -> Bool     mutating func subtractInPlace(_ other: PKAddressField)     func isStrictSupersetOf(_ other: PKAddressField) -> Bool     func isStrictSubsetOf(_ other: PKAddressField) -> Bool } extension PKAddressField {     func union(_ other: PKAddressField) -> PKAddressField     func intersection(_ other: PKAddressField) -> PKAddressField     func symmetricDifference(_ other: PKAddressField) -> PKAddressField } extension PKAddressField {     func contains(_ member: PKAddressField) -> Bool     mutating func insert(_ newMember: PKAddressField) -> (inserted: Bool, memberAfterInsert: PKAddressField)     mutating func remove(_ member: PKAddressField) -> PKAddressField?     mutating func update(with newMember: PKAddressField) -> PKAddressField? } extension PKAddressField {     convenience init()     mutating func formUnion(_ other: PKAddressField)     mutating func formIntersection(_ other: PKAddressField)     mutating func formSymmetricDifference(_ other: PKAddressField) } extension PKAddressField {     convenience init<S : Sequence where S.Iterator.Element == PKAddressField>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: PKAddressField...)     mutating func subtract(_ other: PKAddressField)     func isSubset(of other: PKAddressField) -> Bool     func isSuperset(of other: PKAddressField) -> Bool     func isDisjoint(with other: PKAddressField) -> Bool     func subtracting(_ other: PKAddressField) -> PKAddressField     var isEmpty: Bool { get }     func isStrictSuperset(of other: PKAddressField) -> Bool     func isStrictSubset(of other: PKAddressField) -> Bool } ``` | OptionSet |

Modified [PKAddressField.all](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldall)

|  | Declaration |
| --- | --- |
| From | ``` static var All: PKAddressField { get } ``` |
| To | ``` static var all: PKAddressField { get } ``` |

Modified [PKAddressField.email](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldemail)

|  | Declaration |
| --- | --- |
| From | ``` static var Email: PKAddressField { get } ``` |
| To | ``` static var email: PKAddressField { get } ``` |

Modified [PKAddressField.name](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldname)

|  | Declaration |
| --- | --- |
| From | ``` static var Name: PKAddressField { get } ``` |
| To | ``` static var name: PKAddressField { get } ``` |

Modified [PKAddressField.phone](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldphone)

|  | Declaration |
| --- | --- |
| From | ``` static var Phone: PKAddressField { get } ``` |
| To | ``` static var phone: PKAddressField { get } ``` |

Modified [PKAddressField.postalAddress](https://developer.apple.com/documentation/passkit/pkaddressfield/pkaddressfieldpostaladdress)

|  | Declaration |
| --- | --- |
| From | ``` static var PostalAddress: PKAddressField { get } ``` |
| To | ``` static var postalAddress: PKAddressField { get } ``` |

Modified [PKAutomaticPassPresentationSuppressionResult [enum]](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult)

|  | Declaration |
| --- | --- |
| From | ``` enum PKAutomaticPassPresentationSuppressionResult : UInt {     case NotSupported     case AlreadyPresenting     case Denied     case Cancelled     case Success } ``` |
| To | ``` enum PKAutomaticPassPresentationSuppressionResult : UInt {     case notSupported     case alreadyPresenting     case denied     case cancelled     case success } ``` |

Modified [PKAutomaticPassPresentationSuppressionResult.alreadyPresenting](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/alreadypresenting)

|  | Declaration |
| --- | --- |
| From | ``` case AlreadyPresenting ``` |
| To | ``` case alreadyPresenting ``` |

Modified [PKAutomaticPassPresentationSuppressionResult.cancelled](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/cancelled)

|  | Declaration |
| --- | --- |
| From | ``` case Cancelled ``` |
| To | ``` case cancelled ``` |

Modified [PKAutomaticPassPresentationSuppressionResult.denied](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/denied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [PKAutomaticPassPresentationSuppressionResult.notSupported](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/pkautomaticpasspresentationsuppressionresultnotsupported)

|  | Declaration |
| --- | --- |
| From | ``` case NotSupported ``` |
| To | ``` case notSupported ``` |

Modified [PKAutomaticPassPresentationSuppressionResult.success](https://developer.apple.com/documentation/passkit/pkautomaticpasspresentationsuppressionresult/success)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [PKContact](https://developer.apple.com/documentation/passkit/pkcontact)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKContact : NSObject {     var name: NSPersonNameComponents?     var postalAddress: CNPostalAddress?     var emailAddress: String?     var phoneNumber: CNPhoneNumber?     var supplementarySubLocality: String? } ``` | -- |
| To | ``` class PKContact : NSObject {     var name: PersonNameComponents?     var postalAddress: CNPostalAddress?     var emailAddress: String?     var phoneNumber: CNPhoneNumber?     var supplementarySubLocality: String?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKContact : CVarArg { } extension PKContact : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKContact.name](https://developer.apple.com/documentation/passkit/pkcontact/1619318-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: NSPersonNameComponents? ``` |
| To | ``` var name: PersonNameComponents? ``` |

Modified [PKEncryptionScheme.ECC_V2](https://developer.apple.com/documentation/passkit/pkencryptionscheme/1618637-ecc_v2)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKEncryptionSchemeECC_V2 | ``` let PKEncryptionSchemeECC_V2: String ``` |
| To | ECC_V2 | ``` static let ECC_V2: PKEncryptionScheme ``` |

Modified [PKMerchantCapability [struct]](https://developer.apple.com/documentation/passkit/pkmerchantcapability)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PKMerchantCapability : OptionSetType {     init(rawValue rawValue: UInt)     static var Capability3DS: PKMerchantCapability { get }     static var CapabilityEMV: PKMerchantCapability { get }     static var CapabilityCredit: PKMerchantCapability { get }     static var CapabilityDebit: PKMerchantCapability { get } } ``` | OptionSetType |
| To | ``` struct PKMerchantCapability : OptionSet {     init(rawValue rawValue: UInt)     static var capability3DS: PKMerchantCapability { get }     static var capabilityEMV: PKMerchantCapability { get }     static var capabilityCredit: PKMerchantCapability { get }     static var capabilityDebit: PKMerchantCapability { get }     func intersect(_ other: PKMerchantCapability) -> PKMerchantCapability     func exclusiveOr(_ other: PKMerchantCapability) -> PKMerchantCapability     mutating func unionInPlace(_ other: PKMerchantCapability)     mutating func intersectInPlace(_ other: PKMerchantCapability)     mutating func exclusiveOrInPlace(_ other: PKMerchantCapability)     func isSubsetOf(_ other: PKMerchantCapability) -> Bool     func isDisjointWith(_ other: PKMerchantCapability) -> Bool     func isSupersetOf(_ other: PKMerchantCapability) -> Bool     mutating func subtractInPlace(_ other: PKMerchantCapability)     func isStrictSupersetOf(_ other: PKMerchantCapability) -> Bool     func isStrictSubsetOf(_ other: PKMerchantCapability) -> Bool } extension PKMerchantCapability {     func union(_ other: PKMerchantCapability) -> PKMerchantCapability     func intersection(_ other: PKMerchantCapability) -> PKMerchantCapability     func symmetricDifference(_ other: PKMerchantCapability) -> PKMerchantCapability } extension PKMerchantCapability {     func contains(_ member: PKMerchantCapability) -> Bool     mutating func insert(_ newMember: PKMerchantCapability) -> (inserted: Bool, memberAfterInsert: PKMerchantCapability)     mutating func remove(_ member: PKMerchantCapability) -> PKMerchantCapability?     mutating func update(with newMember: PKMerchantCapability) -> PKMerchantCapability? } extension PKMerchantCapability {     convenience init()     mutating func formUnion(_ other: PKMerchantCapability)     mutating func formIntersection(_ other: PKMerchantCapability)     mutating func formSymmetricDifference(_ other: PKMerchantCapability) } extension PKMerchantCapability {     convenience init<S : Sequence where S.Iterator.Element == PKMerchantCapability>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: PKMerchantCapability...)     mutating func subtract(_ other: PKMerchantCapability)     func isSubset(of other: PKMerchantCapability) -> Bool     func isSuperset(of other: PKMerchantCapability) -> Bool     func isDisjoint(with other: PKMerchantCapability) -> Bool     func subtracting(_ other: PKMerchantCapability) -> PKMerchantCapability     var isEmpty: Bool { get }     func isStrictSuperset(of other: PKMerchantCapability) -> Bool     func isStrictSubset(of other: PKMerchantCapability) -> Bool } ``` | OptionSet |

Modified [PKMerchantCapability.capability3DS](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapability3ds)

|  | Declaration |
| --- | --- |
| From | ``` static var Capability3DS: PKMerchantCapability { get } ``` |
| To | ``` static var capability3DS: PKMerchantCapability { get } ``` |

Modified [PKMerchantCapability.capabilityCredit](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapabilitycredit)

|  | Declaration |
| --- | --- |
| From | ``` static var CapabilityCredit: PKMerchantCapability { get } ``` |
| To | ``` static var capabilityCredit: PKMerchantCapability { get } ``` |

Modified [PKMerchantCapability.capabilityDebit](https://developer.apple.com/documentation/passkit/pkmerchantcapability/pkmerchantcapabilitydebit)

|  | Declaration |
| --- | --- |
| From | ``` static var CapabilityDebit: PKMerchantCapability { get } ``` |
| To | ``` static var capabilityDebit: PKMerchantCapability { get } ``` |

Modified [PKMerchantCapability.capabilityEMV](https://developer.apple.com/documentation/passkit/pkmerchantcapability/1619224-capabilityemv)

|  | Declaration |
| --- | --- |
| From | ``` static var CapabilityEMV: PKMerchantCapability { get } ``` |
| To | ``` static var capabilityEMV: PKMerchantCapability { get } ``` |

Modified [PKObject](https://developer.apple.com/documentation/passkit/pkobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKObject : NSObject { } ``` | -- |
| To | ``` class PKObject : NSObject {     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKObject : CVarArg { } extension PKObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPass](https://developer.apple.com/documentation/passkit/pkpass)

|  | Declaration |
| --- | --- |
| From | ``` class PKPass : PKObject {     init(data data: NSData, error error: NSErrorPointer)     var passType: PKPassType { get }     unowned(unsafe) var paymentPass: PKPaymentPass? { get }     var serialNumber: String { get }     var passTypeIdentifier: String { get }     @NSCopying var webServiceURL: NSURL? { get }     var authenticationToken: String? { get }     @NSCopying var icon: UIImage { get }     var localizedName: String { get }     var localizedDescription: String { get }     var organizationName: String { get }     @NSCopying var relevantDate: NSDate? { get }     var userInfo: [NSObject : AnyObject]? { get }     @NSCopying var passURL: NSURL { get }     var remotePass: Bool { get }     var deviceName: String { get }     func localizedValueForFieldKey(_ key: String) -> AnyObject? } ``` |
| To | ``` class PKPass : PKObject {     init(data data: Data, error error: NSErrorPointer)     var passType: PKPassType { get }     var paymentPass: PKPaymentPass? { get }     var serialNumber: String { get }     var passTypeIdentifier: String { get }     var webServiceURL: URL? { get }     var authenticationToken: String? { get }     @NSCopying var icon: UIImage { get }     var localizedName: String { get }     var localizedDescription: String { get }     var organizationName: String { get }     var relevantDate: Date? { get }     var userInfo: [AnyHashable : Any]? { get }     var passURL: URL? { get }     var isRemotePass: Bool { get }     var deviceName: String { get }     func localizedValue(forFieldKey key: String) -> Any? } ``` |

Modified [PKPass.init(data: Data, error: NSErrorPointer)](https://developer.apple.com/documentation/passkit/pkpass/1618792-init)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData, error error: NSErrorPointer) ``` |
| To | ``` init(data data: Data, error error: NSErrorPointer) ``` |

Modified [PKPass.isRemotePass](https://developer.apple.com/documentation/passkit/pkpass/1618786-remotepass)

|  | Declaration |
| --- | --- |
| From | ``` var remotePass: Bool { get } ``` |
| To | ``` var isRemotePass: Bool { get } ``` |

Modified [PKPass.localizedValue(forFieldKey: String) -> Any?](https://developer.apple.com/documentation/passkit/pkpass/1618798-localizedvalueforfieldkey)

|  | Declaration |
| --- | --- |
| From | ``` func localizedValueForFieldKey(_ key: String) -> AnyObject? ``` |
| To | ``` func localizedValue(forFieldKey key: String) -> Any? ``` |

Modified [PKPass.passURL](https://developer.apple.com/documentation/passkit/pkpass/1618781-passurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var passURL: NSURL { get } ``` |
| To | ``` var passURL: URL? { get } ``` |

Modified [PKPass.paymentPass](https://developer.apple.com/documentation/passkit/pkpass/1618784-paymentpass)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var paymentPass: PKPaymentPass? { get } ``` |
| To | ``` var paymentPass: PKPaymentPass? { get } ``` |

Modified [PKPass.relevantDate](https://developer.apple.com/documentation/passkit/pkpass/1618776-relevantdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var relevantDate: NSDate? { get } ``` |
| To | ``` var relevantDate: Date? { get } ``` |

Modified [PKPass.userInfo](https://developer.apple.com/documentation/passkit/pkpass/1618794-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? { get } ``` |
| To | ``` var userInfo: [AnyHashable : Any]? { get } ``` |

Modified [PKPass.webServiceURL](https://developer.apple.com/documentation/passkit/pkpass/1618772-webserviceurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var webServiceURL: NSURL? { get } ``` |
| To | ``` var webServiceURL: URL? { get } ``` |

Modified [PKPassKitError.Code [enum]](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPassKitErrorCode : Int {     case UnknownError     case InvalidDataError     case UnsupportedVersionError     case InvalidSignature     case NotEntitledError } extension PKPassKitErrorCode : _BridgedNSError { } extension PKPassKitErrorCode : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = PKPassKitError         case unknownError         case invalidDataError         case unsupportedVersionError         case invalidSignature         case notEntitledError     } ``` |

Modified [PKPassKitError.Code.invalidDataError](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/invaliddataerror)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidDataError ``` |
| To | ``` case invalidDataError ``` |

Modified [PKPassKitError.Code.invalidSignature](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/invalidsignature)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidSignature ``` |
| To | ``` case invalidSignature ``` |

Modified [PKPassKitError.Code.notEntitledError](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/notentitlederror)

|  | Declaration |
| --- | --- |
| From | ``` case NotEntitledError ``` |
| To | ``` case notEntitledError ``` |

Modified [PKPassKitError.Code.unknownError](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode/pkunknownerror)

|  | Declaration |
| --- | --- |
| From | ``` case UnknownError ``` |
| To | ``` case unknownError ``` |

Modified [PKPassKitError.Code.unsupportedVersionError](https://developer.apple.com/documentation/passkit/pkpasskiterrorcode/pkunsupportedversionerror)

|  | Declaration |
| --- | --- |
| From | ``` case UnsupportedVersionError ``` |
| To | ``` case unsupportedVersionError ``` |

Modified [PKPassLibrary](https://developer.apple.com/documentation/passkit/pkpasslibrary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPassLibrary : NSObject {     class func isPassLibraryAvailable() -> Bool     class func requestAutomaticPassPresentationSuppressionWithResponseHandler(_ responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken     class func endAutomaticPassPresentationSuppressionWithRequestToken(_ requestToken: PKSuppressionRequestToken)     class func isSuppressingAutomaticPassPresentation() -> Bool     class func isPaymentPassActivationAvailable() -> Bool     func isPaymentPassActivationAvailable() -> Bool     func passes() -> [PKPass]     func passWithPassTypeIdentifier(_ identifier: String, serialNumber serialNumber: String) -> PKPass?     func passesOfType(_ passType: PKPassType) -> [PKPass]     func remotePaymentPasses() -> [PKPaymentPass]     func removePass(_ pass: PKPass)     func containsPass(_ pass: PKPass) -> Bool     func replacePassWithPass(_ pass: PKPass) -> Bool     func addPasses(_ passes: [PKPass], withCompletionHandler completion: ((PKPassLibraryAddPassesStatus) -> Void)?)     func openPaymentSetup()     func canAddPaymentPassWithPrimaryAccountIdentifier(_ primaryAccountIdentifier: String) -> Bool     func activatePaymentPass(_ paymentPass: PKPaymentPass, withActivationData activationData: NSData, completion completion: ((Bool, NSError) -> Void)?)     func activatePaymentPass(_ paymentPass: PKPaymentPass, withActivationCode activationCode: String, completion completion: ((Bool, NSError) -> Void)?) } ``` | -- |
| To | ``` class PKPassLibrary : NSObject {     class func isPassLibraryAvailable() -> Bool     class func requestAutomaticPassPresentationSuppression(responseHandler responseHandler: @escaping (PKAutomaticPassPresentationSuppressionResult) -> Swift.Void) -> PKSuppressionRequestToken     class func endAutomaticPassPresentationSuppression(withRequestToken requestToken: PKSuppressionRequestToken)     class func isSuppressingAutomaticPassPresentation() -> Bool     class func isPaymentPassActivationAvailable() -> Bool     func isPaymentPassActivationAvailable() -> Bool     func passes() -> [PKPass]     func pass(withPassTypeIdentifier identifier: String, serialNumber serialNumber: String) -> PKPass?     func passes(of passType: PKPassType) -> [PKPass]     func remotePaymentPasses() -> [PKPaymentPass]     func removePass(_ pass: PKPass)     func containsPass(_ pass: PKPass) -> Bool     func replacePass(with pass: PKPass) -> Bool     func addPasses(_ passes: [PKPass], withCompletionHandler completion: (@escaping (PKPassLibraryAddPassesStatus) -> Swift.Void)? = nil)     func openPaymentSetup()     func present(_ pass: PKPaymentPass)     func canAddPaymentPass(withPrimaryAccountIdentifier primaryAccountIdentifier: String) -> Bool     func activate(_ paymentPass: PKPaymentPass, withActivationData activationData: Data, completion completion: (@escaping (Bool, Error) -> Swift.Void)? = nil)     func activate(_ paymentPass: PKPaymentPass, withActivationCode activationCode: String, completion completion: (@escaping (Bool, Error) -> Swift.Void)? = nil)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKPassLibrary : CVarArg { } extension PKPassLibrary : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPassLibrary.activate(_: PKPaymentPass, withActivationCode: String, completion: ( (Bool, Error) -> Swift.Void)?)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617079-activate)

|  | Declaration |
| --- | --- |
| From | ``` func activatePaymentPass(_ paymentPass: PKPaymentPass, withActivationCode activationCode: String, completion completion: ((Bool, NSError) -> Void)?) ``` |
| To | ``` func activate(_ paymentPass: PKPaymentPass, withActivationCode activationCode: String, completion completion: (@escaping (Bool, Error) -> Swift.Void)? = nil) ``` |

Modified [PKPassLibrary.activate(_: PKPaymentPass, withActivationData: Data, completion: ( (Bool, Error) -> Swift.Void)?)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617088-activate)

|  | Declaration |
| --- | --- |
| From | ``` func activatePaymentPass(_ paymentPass: PKPaymentPass, withActivationData activationData: NSData, completion completion: ((Bool, NSError) -> Void)?) ``` |
| To | ``` func activate(_ paymentPass: PKPaymentPass, withActivationData activationData: Data, completion completion: (@escaping (Bool, Error) -> Swift.Void)? = nil) ``` |

Modified [PKPassLibrary.addPasses(_: [PKPass], withCompletionHandler: ( (PKPassLibraryAddPassesStatus) -> Swift.Void)?)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617093-addpasses)

|  | Declaration |
| --- | --- |
| From | ``` func addPasses(_ passes: [PKPass], withCompletionHandler completion: ((PKPassLibraryAddPassesStatus) -> Void)?) ``` |
| To | ``` func addPasses(_ passes: [PKPass], withCompletionHandler completion: (@escaping (PKPassLibraryAddPassesStatus) -> Swift.Void)? = nil) ``` |

Modified [PKPassLibrary.canAddPaymentPass(withPrimaryAccountIdentifier: String) -> Bool](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617081-canaddpaymentpasswithprimaryacco)

|  | Declaration |
| --- | --- |
| From | ``` func canAddPaymentPassWithPrimaryAccountIdentifier(_ primaryAccountIdentifier: String) -> Bool ``` |
| To | ``` func canAddPaymentPass(withPrimaryAccountIdentifier primaryAccountIdentifier: String) -> Bool ``` |

Modified [PKPassLibrary.endAutomaticPassPresentationSuppression(withRequestToken: PKSuppressionRequestToken) [class]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617097-endautomaticpasspresentationsupp)

|  | Declaration |
| --- | --- |
| From | ``` class func endAutomaticPassPresentationSuppressionWithRequestToken(_ requestToken: PKSuppressionRequestToken) ``` |
| To | ``` class func endAutomaticPassPresentationSuppression(withRequestToken requestToken: PKSuppressionRequestToken) ``` |

Modified [PKPassLibrary.pass(withPassTypeIdentifier: String, serialNumber: String) -> PKPass?](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617104-passwithpasstypeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func passWithPassTypeIdentifier(_ identifier: String, serialNumber serialNumber: String) -> PKPass? ``` |
| To | ``` func pass(withPassTypeIdentifier identifier: String, serialNumber serialNumber: String) -> PKPass? ``` |

Modified [PKPassLibrary.passes(of: PKPassType) -> [PKPass]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617074-passes)

|  | Declaration |
| --- | --- |
| From | ``` func passesOfType(_ passType: PKPassType) -> [PKPass] ``` |
| To | ``` func passes(of passType: PKPassType) -> [PKPass] ``` |

Modified [PKPassLibrary.replacePass(with: PKPass) -> Bool](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617082-replacepasswithpass)

|  | Declaration |
| --- | --- |
| From | ``` func replacePassWithPass(_ pass: PKPass) -> Bool ``` |
| To | ``` func replacePass(with pass: PKPass) -> Bool ``` |

Modified [PKPassLibrary.requestAutomaticPassPresentationSuppression(responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Swift.Void) -> PKSuppressionRequestToken [class]](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617078-requestautomaticpasspresentation)

|  | Declaration |
| --- | --- |
| From | ``` class func requestAutomaticPassPresentationSuppressionWithResponseHandler(_ responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken ``` |
| To | ``` class func requestAutomaticPassPresentationSuppression(responseHandler responseHandler: @escaping (PKAutomaticPassPresentationSuppressionResult) -> Swift.Void) -> PKSuppressionRequestToken ``` |

Modified [PKPassLibraryAddPassesStatus [enum]](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPassLibraryAddPassesStatus : Int {     case DidAddPasses     case ShouldReviewPasses     case DidCancelAddPasses } ``` |
| To | ``` enum PKPassLibraryAddPassesStatus : Int {     case didAddPasses     case shouldReviewPasses     case didCancelAddPasses } ``` |

Modified [PKPassLibraryAddPassesStatus.didAddPasses](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus/pkpasslibrarydidaddpasses)

|  | Declaration |
| --- | --- |
| From | ``` case DidAddPasses ``` |
| To | ``` case didAddPasses ``` |

Modified [PKPassLibraryAddPassesStatus.didCancelAddPasses](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus/pkpasslibrarydidcanceladdpasses)

|  | Declaration |
| --- | --- |
| From | ``` case DidCancelAddPasses ``` |
| To | ``` case didCancelAddPasses ``` |

Modified [PKPassLibraryAddPassesStatus.shouldReviewPasses](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus/shouldreviewpasses)

|  | Declaration |
| --- | --- |
| From | ``` case ShouldReviewPasses ``` |
| To | ``` case shouldReviewPasses ``` |

Modified [PKPassLibraryNotificationKey.addedPassesUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibraryaddedpassesuserinfokey)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryAddedPassesUserInfoKey | ``` let PKPassLibraryAddedPassesUserInfoKey: String ``` |
| To | addedPassesUserInfoKey | ``` static let addedPassesUserInfoKey: PKPassLibraryNotificationKey ``` |

Modified [PKPassLibraryNotificationKey.passTypeIdentifierUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/1617094-passtypeidentifieruserinfokey)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryPassTypeIdentifierUserInfoKey | ``` let PKPassLibraryPassTypeIdentifierUserInfoKey: String ``` |
| To | passTypeIdentifierUserInfoKey | ``` static let passTypeIdentifierUserInfoKey: PKPassLibraryNotificationKey ``` |

Modified [PKPassLibraryNotificationKey.removedPassInfosUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibraryremovedpassinfosuserinfokey)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryRemovedPassInfosUserInfoKey | ``` let PKPassLibraryRemovedPassInfosUserInfoKey: String ``` |
| To | removedPassInfosUserInfoKey | ``` static let removedPassInfosUserInfoKey: PKPassLibraryNotificationKey ``` |

Modified [PKPassLibraryNotificationKey.replacementPassesUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationkey/1617077-replacementpassesuserinfokey)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryReplacementPassesUserInfoKey | ``` let PKPassLibraryReplacementPassesUserInfoKey: String ``` |
| To | replacementPassesUserInfoKey | ``` static let replacementPassesUserInfoKey: PKPassLibraryNotificationKey ``` |

Modified [PKPassLibraryNotificationKey.serialNumberUserInfoKey](https://developer.apple.com/documentation/passkit/pkpasslibraryserialnumberuserinfokey)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibrarySerialNumberUserInfoKey | ``` let PKPassLibrarySerialNumberUserInfoKey: String ``` |
| To | serialNumberUserInfoKey | ``` static let serialNumberUserInfoKey: PKPassLibraryNotificationKey ``` |

Modified [PKPassLibraryNotificationName.PKPassLibraryDidChange](https://developer.apple.com/documentation/passkit/pkpasslibrarydidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryDidChangeNotification | ``` let PKPassLibraryDidChangeNotification: String ``` |
| To | PKPassLibraryDidChange | ``` static let PKPassLibraryDidChange: PKPassLibraryNotificationName ``` |

Modified [PKPassLibraryNotificationName.PKPassLibraryRemotePaymentPassesDidChange](https://developer.apple.com/documentation/passkit/pkpasslibraryremotepaymentpassesdidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPassLibraryRemotePaymentPassesDidChangeNotification | ``` let PKPassLibraryRemotePaymentPassesDidChangeNotification: String ``` |
| To | PKPassLibraryRemotePaymentPassesDidChange | ``` static let PKPassLibraryRemotePaymentPassesDidChange: PKPassLibraryNotificationName ``` |

Modified [PKPassType [enum]](https://developer.apple.com/documentation/passkit/pkpasstype)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPassType : UInt {     case Barcode     case Payment     case Any } ``` |
| To | ``` enum PKPassType : UInt {     case barcode     case payment     case any } ``` |

Modified [PKPassType.any](https://developer.apple.com/documentation/passkit/pkpasstype/pkpasstypeany)

|  | Declaration |
| --- | --- |
| From | ``` case Any ``` |
| To | ``` case any ``` |

Modified [PKPassType.barcode](https://developer.apple.com/documentation/passkit/pkpasstype/barcode)

|  | Declaration |
| --- | --- |
| From | ``` case Barcode ``` |
| To | ``` case barcode ``` |

Modified [PKPassType.payment](https://developer.apple.com/documentation/passkit/pkpasstype/pkpasstypepayment)

|  | Declaration |
| --- | --- |
| From | ``` case Payment ``` |
| To | ``` case payment ``` |

Modified [PKPayment](https://developer.apple.com/documentation/passkit/pkpayment)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPayment : NSObject {     var token: PKPaymentToken { get }     var billingAddress: ABRecord? { get }     var billingContact: PKContact? { get }     var shippingAddress: ABRecord? { get }     var shippingContact: PKContact? { get }     var shippingMethod: PKShippingMethod? { get } } ``` | -- |
| To | ``` class PKPayment : NSObject {     var token: PKPaymentToken { get }     var billingContact: PKContact? { get }     unowned(unsafe) var billingAddress: ABRecord? { get }     var shippingContact: PKContact? { get }     unowned(unsafe) var shippingAddress: ABRecord? { get }     var shippingMethod: PKShippingMethod? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKPayment : CVarArg { } extension PKPayment : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPayment.billingAddress](https://developer.apple.com/documentation/passkit/pkpayment/1619307-billingaddress)

|  | Declaration |
| --- | --- |
| From | ``` var billingAddress: ABRecord? { get } ``` |
| To | ``` unowned(unsafe) var billingAddress: ABRecord? { get } ``` |

Modified [PKPayment.shippingAddress](https://developer.apple.com/documentation/passkit/pkpayment/1619271-shippingaddress)

|  | Declaration |
| --- | --- |
| From | ``` var shippingAddress: ABRecord? { get } ``` |
| To | ``` unowned(unsafe) var shippingAddress: ABRecord? { get } ``` |

Modified [PKPaymentAuthorizationStatus [enum]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPaymentAuthorizationStatus : Int {     case Success     case Failure     case InvalidBillingPostalAddress     case InvalidShippingPostalAddress     case InvalidShippingContact     case PINRequired     case PINIncorrect     case PINLockout } ``` |
| To | ``` enum PKPaymentAuthorizationStatus : Int {     case success     case failure     case invalidBillingPostalAddress     case invalidShippingPostalAddress     case invalidShippingContact     case pinRequired     case pinIncorrect     case pinLockout } ``` |

Modified [PKPaymentAuthorizationStatus.failure](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/failure)

|  | Declaration |
| --- | --- |
| From | ``` case Failure ``` |
| To | ``` case failure ``` |

Modified [PKPaymentAuthorizationStatus.invalidBillingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidbillingpostaladdress)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidBillingPostalAddress ``` |
| To | ``` case invalidBillingPostalAddress ``` |

Modified [PKPaymentAuthorizationStatus.invalidShippingContact](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/invalidshippingcontact)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidShippingContact ``` |
| To | ``` case invalidShippingContact ``` |

Modified [PKPaymentAuthorizationStatus.invalidShippingPostalAddress](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatusinvalidshippingpostaladdress)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidShippingPostalAddress ``` |
| To | ``` case invalidShippingPostalAddress ``` |

Modified [PKPaymentAuthorizationStatus.pinIncorrect](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinincorrect)

|  | Declaration |
| --- | --- |
| From | ``` case PINIncorrect ``` |
| To | ``` case pinIncorrect ``` |

Modified [PKPaymentAuthorizationStatus.pinLockout](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinlockout)

|  | Declaration |
| --- | --- |
| From | ``` case PINLockout ``` |
| To | ``` case pinLockout ``` |

Modified [PKPaymentAuthorizationStatus.pinRequired](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pkpaymentauthorizationstatuspinrequired)

|  | Declaration |
| --- | --- |
| From | ``` case PINRequired ``` |
| To | ``` case pinRequired ``` |

Modified [PKPaymentAuthorizationStatus.success](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/success)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [PKPaymentAuthorizationViewController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPaymentAuthorizationViewController : UIViewController {     class func canMakePayments() -> Bool     class func canMakePaymentsUsingNetworks(_ supportedNetworks: [String]) -> Bool     class func canMakePaymentsUsingNetworks(_ supportedNetworks: [String], capabilities capabilties: PKMerchantCapability) -> Bool     unowned(unsafe) var delegate: PKPaymentAuthorizationViewControllerDelegate?     init(paymentRequest request: PKPaymentRequest) } ``` | -- |
| To | ``` class PKPaymentAuthorizationViewController : UIViewController {     class func canMakePayments() -> Bool     class func canMakePayments(usingNetworks supportedNetworks: [PKPaymentNetwork]) -> Bool     class func canMakePayments(usingNetworks supportedNetworks: [PKPaymentNetwork], capabilities capabilties: PKMerchantCapability) -> Bool     unowned(unsafe) var delegate: PKPaymentAuthorizationViewControllerDelegate?     init(paymentRequest request: PKPaymentRequest)     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get }     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)     func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?     var transitionCoordinator: UIViewControllerTransitionCoordinator? { get }     var isModalInPopover: Bool     var contentSizeForViewInPopover: CGSize     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool)     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get }     var previewActionItems: [UIPreviewActionItem] { get }     func registerForPreviewing(with delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewing(withContext previewing: UIViewControllerPreviewing)     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get }     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand)     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get }     weak var transitioningDelegate: UIViewControllerTransitioningDelegate?     func updateViewConstraints()     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     var shouldAutomaticallyForwardAppearanceMethods: Bool { get }     func willMove(toParentViewController parent: UIViewController?)     func didMove(toParentViewController parent: UIViewController?)     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     var childViewControllerForStatusBarStyle: UIViewController? { get }     var childViewControllerForStatusBarHidden: UIViewController? { get }     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollection(forChildViewController childViewController: UIViewController) -> UITraitCollection?     var searchDisplayController: UISearchDisplayController? { get }     var isEditing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var editButtonItem: UIBarButtonItem { get }     class func attemptRotationToDeviceOrientation()     func shouldAutorotate(to toInterfaceOrientation: UIInterfaceOrientation) -> Bool     var shouldAutorotate: Bool { get }     var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }     var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotate(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didRotate(from fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func willAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotation(from fromInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKPaymentAuthorizationViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension PKPaymentAuthorizationViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: UIViewControllerRestoration.Type?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func applicationFinishedRestoringState() } extension PKPaymentAuthorizationViewController : CVarArg { } extension PKPaymentAuthorizationViewController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSExtensionRequestHandling, UIStateRestoring |

Modified [PKPaymentAuthorizationViewController.canMakePayments(usingNetworks: [PKPaymentNetwork]) -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616187-canmakepaymentsusingnetworks)

|  | Declaration |
| --- | --- |
| From | ``` class func canMakePaymentsUsingNetworks(_ supportedNetworks: [String]) -> Bool ``` |
| To | ``` class func canMakePayments(usingNetworks supportedNetworks: [PKPaymentNetwork]) -> Bool ``` |

Modified [PKPaymentAuthorizationViewController.canMakePayments(usingNetworks: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool [class]](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/1616181-canmakepaymentsusingnetworks)

|  | Declaration |
| --- | --- |
| From | ``` class func canMakePaymentsUsingNetworks(_ supportedNetworks: [String], capabilities capabilties: PKMerchantCapability) -> Bool ``` |
| To | ``` class func canMakePayments(usingNetworks supportedNetworks: [PKPaymentNetwork], capabilities capabilties: PKMerchantCapability) -> Bool ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol PKPaymentAuthorizationViewControllerDelegate : NSObjectProtocol {     func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment, completion completion: (PKPaymentAuthorizationStatus) -> Void)     func paymentAuthorizationViewControllerDidFinish(_ controller: PKPaymentAuthorizationViewController)     optional func paymentAuthorizationViewControllerWillAuthorizePayment(_ controller: PKPaymentAuthorizationViewController)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingMethod shippingMethod: PKShippingMethod, completion completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingAddress address: ABRecord, completion completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingContact contact: PKContact, completion completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectPaymentMethod paymentMethod: PKPaymentMethod, completion completion: ([PKPaymentSummaryItem]) -> Void) } ``` |
| To | ``` protocol PKPaymentAuthorizationViewControllerDelegate : NSObjectProtocol {     func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment, completion completion: @escaping (PKPaymentAuthorizationStatus) -> Swift.Void)     func paymentAuthorizationViewControllerDidFinish(_ controller: PKPaymentAuthorizationViewController)     optional func paymentAuthorizationViewControllerWillAuthorizePayment(_ controller: PKPaymentAuthorizationViewController)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect shippingMethod: PKShippingMethod, completion completion: @escaping (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Swift.Void)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingAddress address: ABRecord, completion completion: @escaping (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Swift.Void)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingContact contact: PKContact, completion completion: @escaping (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Swift.Void)     optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect paymentMethod: PKPaymentMethod, completion completion: @escaping ([PKPaymentSummaryItem]) -> Swift.Void) } ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewController(_: PKPaymentAuthorizationViewController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616195-paymentauthorizationviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment, completion completion: (PKPaymentAuthorizationStatus) -> Void) ``` |
| To | ``` func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment, completion completion: @escaping (PKPaymentAuthorizationStatus) -> Swift.Void) ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewController(_: PKPaymentAuthorizationViewController, didSelect: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616184-paymentauthorizationviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectPaymentMethod paymentMethod: PKPaymentMethod, completion completion: ([PKPaymentSummaryItem]) -> Void) ``` |
| To | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect paymentMethod: PKPaymentMethod, completion completion: @escaping ([PKPaymentSummaryItem]) -> Swift.Void) ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewController(_: PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616186-paymentauthorizationviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingMethod shippingMethod: PKShippingMethod, completion completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void) ``` |
| To | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect shippingMethod: PKShippingMethod, completion completion: @escaping (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Swift.Void) ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewController(_: PKPaymentAuthorizationViewController, didSelectShippingAddress: ABRecord, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616196-paymentauthorizationviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingAddress address: ABRecord, completion completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void) ``` |
| To | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingAddress address: ABRecord, completion completion: @escaping (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Swift.Void) ``` |

Modified [PKPaymentAuthorizationViewControllerDelegate.paymentAuthorizationViewController(_: PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Swift.Void)](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/1616198-paymentauthorizationviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingContact contact: PKContact, completion completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void) ``` |
| To | ``` optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingContact contact: PKContact, completion completion: @escaping (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Swift.Void) ``` |

Modified [PKPaymentButton](https://developer.apple.com/documentation/passkit/pkpaymentbutton)

|  | Declaration |
| --- | --- |
| From | ``` class PKPaymentButton : UIButton {     convenience init(type buttonType: PKPaymentButtonType, style buttonStyle: PKPaymentButtonStyle)     class func buttonWithType(_ buttonType: PKPaymentButtonType, style buttonStyle: PKPaymentButtonStyle) -> Self     init(paymentButtonType type: PKPaymentButtonType, paymentButtonStyle style: PKPaymentButtonStyle) } ``` |
| To | ``` class PKPaymentButton : UIButton {     convenience init(type buttonType: PKPaymentButtonType, style buttonStyle: PKPaymentButtonStyle)     class func withType(_ buttonType: PKPaymentButtonType, style buttonStyle: PKPaymentButtonStyle) -> Self     init(paymentButtonType type: PKPaymentButtonType, paymentButtonStyle style: PKPaymentButtonStyle)     var font: UIFont     var lineBreakMode: NSLineBreakMode     var titleShadowOffset: CGSize } ``` |

Modified [PKPaymentButtonStyle [enum]](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPaymentButtonStyle : Int {     case White     case WhiteOutline     case Black } ``` |
| To | ``` enum PKPaymentButtonStyle : Int {     case white     case whiteOutline     case black } ``` |

Modified [PKPaymentButtonStyle.black](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle/pkpaymentbuttonstyleblack)

|  | Declaration |
| --- | --- |
| From | ``` case Black ``` |
| To | ``` case black ``` |

Modified [PKPaymentButtonStyle.white](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle/white)

|  | Declaration |
| --- | --- |
| From | ``` case White ``` |
| To | ``` case white ``` |

Modified [PKPaymentButtonStyle.whiteOutline](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle/whiteoutline)

|  | Declaration |
| --- | --- |
| From | ``` case WhiteOutline ``` |
| To | ``` case whiteOutline ``` |

Modified [PKPaymentButtonType [enum]](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPaymentButtonType : Int {     case Plain     case Buy     case SetUp } ``` |
| To | ``` enum PKPaymentButtonType : Int {     case plain     case buy     case setUp     case inStore } ``` |

Modified [PKPaymentButtonType.buy](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/buy)

|  | Declaration |
| --- | --- |
| From | ``` case Buy ``` |
| To | ``` case buy ``` |

Modified [PKPaymentButtonType.plain](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/plain)

|  | Declaration |
| --- | --- |
| From | ``` case Plain ``` |
| To | ``` case plain ``` |

Modified [PKPaymentButtonType.setUp](https://developer.apple.com/documentation/passkit/pkpaymentbuttontype/setup)

|  | Declaration |
| --- | --- |
| From | ``` case SetUp ``` |
| To | ``` case setUp ``` |

Modified [PKPaymentMethod](https://developer.apple.com/documentation/passkit/pkpaymentmethod)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPaymentMethod : NSObject {     var displayName: String? { get }     var network: String? { get }     var type: PKPaymentMethodType { get }     var paymentPass: PKPaymentPass? { get } } ``` | -- |
| To | ``` class PKPaymentMethod : NSObject {     var displayName: String? { get }     var network: PKPaymentNetwork? { get }     var type: PKPaymentMethodType { get }     @NSCopying var paymentPass: PKPaymentPass? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKPaymentMethod : CVarArg { } extension PKPaymentMethod : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPaymentMethod.network](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619209-network)

|  | Declaration |
| --- | --- |
| From | ``` var network: String? { get } ``` |
| To | ``` var network: PKPaymentNetwork? { get } ``` |

Modified [PKPaymentMethod.paymentPass](https://developer.apple.com/documentation/passkit/pkpaymentmethod/1619269-paymentpass)

|  | Declaration |
| --- | --- |
| From | ``` var paymentPass: PKPaymentPass? { get } ``` |
| To | ``` @NSCopying var paymentPass: PKPaymentPass? { get } ``` |

Modified [PKPaymentMethodType [enum]](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` struct PKPaymentMethodType : OptionSetType {     init(rawValue rawValue: UInt)     static var Unknown: PKPaymentMethodType { get }     static var Debit: PKPaymentMethodType { get }     static var Credit: PKPaymentMethodType { get }     static var Prepaid: PKPaymentMethodType { get }     static var Store: PKPaymentMethodType { get } } ``` | OptionSetType | -- |
| To | ``` enum PKPaymentMethodType : UInt {     case unknown     case debit     case credit     case prepaid     case store } ``` | -- | UInt |

Modified [PKPaymentMethodType.credit](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/credit)

|  | Declaration |
| --- | --- |
| From | ``` static var Credit: PKPaymentMethodType { get } ``` |
| To | ``` case credit ``` |

Modified [PKPaymentMethodType.debit](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/debit)

|  | Declaration |
| --- | --- |
| From | ``` static var Debit: PKPaymentMethodType { get } ``` |
| To | ``` case debit ``` |

Modified [PKPaymentMethodType.prepaid](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/prepaid)

|  | Declaration |
| --- | --- |
| From | ``` static var Prepaid: PKPaymentMethodType { get } ``` |
| To | ``` case prepaid ``` |

Modified [PKPaymentMethodType.store](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypestore)

|  | Declaration |
| --- | --- |
| From | ``` static var Store: PKPaymentMethodType { get } ``` |
| To | ``` case store ``` |

Modified [PKPaymentMethodType.unknown](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype/pkpaymentmethodtypeunknown)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | Unknown | ``` static var Unknown: PKPaymentMethodType { get } ``` | iOS 9.0 |
| To | unknown | ``` case unknown ``` | iOS 10.0 |

Modified [PKPaymentNetwork.amex](https://developer.apple.com/documentation/passkit/pkpaymentnetworkamex)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPaymentNetworkAmex | ``` let PKPaymentNetworkAmex: String ``` |
| To | amex | ``` static let amex: PKPaymentNetwork ``` |

Modified [PKPaymentNetwork.chinaUnionPay](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618644-chinaunionpay)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPaymentNetworkChinaUnionPay | ``` let PKPaymentNetworkChinaUnionPay: String ``` |
| To | chinaUnionPay | ``` static let chinaUnionPay: PKPaymentNetwork ``` |

Modified [PKPaymentNetwork.discover](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618641-discover)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPaymentNetworkDiscover | ``` let PKPaymentNetworkDiscover: String ``` |
| To | discover | ``` static let discover: PKPaymentNetwork ``` |

Modified [PKPaymentNetwork.interac](https://developer.apple.com/documentation/passkit/pkpaymentnetworkinterac)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPaymentNetworkInterac | ``` let PKPaymentNetworkInterac: String ``` |
| To | interac | ``` static let interac: PKPaymentNetwork ``` |

Modified [PKPaymentNetwork.masterCard](https://developer.apple.com/documentation/passkit/pkpaymentnetwork/1618643-mastercard)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPaymentNetworkMasterCard | ``` let PKPaymentNetworkMasterCard: String ``` |
| To | masterCard | ``` static let masterCard: PKPaymentNetwork ``` |

Modified [PKPaymentNetwork.privateLabel](https://developer.apple.com/documentation/passkit/pkpaymentnetworkprivatelabel)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPaymentNetworkPrivateLabel | ``` let PKPaymentNetworkPrivateLabel: String ``` |
| To | privateLabel | ``` static let privateLabel: PKPaymentNetwork ``` |

Modified [PKPaymentNetwork.visa](https://developer.apple.com/documentation/passkit/pkpaymentnetworkvisa)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPaymentNetworkVisa | ``` let PKPaymentNetworkVisa: String ``` |
| To | visa | ``` static let visa: PKPaymentNetwork ``` |

Modified [PKPaymentPass](https://developer.apple.com/documentation/passkit/pkpaymentpass)

|  | Declaration |
| --- | --- |
| From | ``` class PKPaymentPass : PKPass {     var primaryAccountIdentifier: String { get }     var primaryAccountNumberSuffix: String { get }     var deviceAccountIdentifier: String { get }     var deviceAccountNumberSuffix: String { get }     var activationState: PKPaymentPassActivationState { get } } ``` |
| To | ``` class PKPaymentPass : PKPass {     var primaryAccountIdentifier: String { get }     var primaryAccountNumberSuffix: String { get }     weak var deviceAccountIdentifier: NSString? { get }     weak var deviceAccountNumberSuffix: NSString? { get }     var activationState: PKPaymentPassActivationState { get } } ``` |

Modified [PKPaymentPass.deviceAccountIdentifier](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619074-deviceaccountidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var deviceAccountIdentifier: String { get } ``` |
| To | ``` weak var deviceAccountIdentifier: NSString? { get } ``` |

Modified [PKPaymentPass.deviceAccountNumberSuffix](https://developer.apple.com/documentation/passkit/pkpaymentpass/1619075-deviceaccountnumbersuffix)

|  | Declaration |
| --- | --- |
| From | ``` var deviceAccountNumberSuffix: String { get } ``` |
| To | ``` weak var deviceAccountNumberSuffix: NSString? { get } ``` |

Modified [PKPaymentPassActivationState [enum]](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPaymentPassActivationState : UInt {     case Activated     case RequiresActivation     case Activating     case Suspended     case Deactivated } ``` |
| To | ``` enum PKPaymentPassActivationState : UInt {     case activated     case requiresActivation     case activating     case suspended     case deactivated } ``` |

Modified [PKPaymentPassActivationState.activated](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/pkpaymentpassactivationstateactivated)

|  | Declaration |
| --- | --- |
| From | ``` case Activated ``` |
| To | ``` case activated ``` |

Modified [PKPaymentPassActivationState.activating](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/pkpaymentpassactivationstateactivating)

|  | Declaration |
| --- | --- |
| From | ``` case Activating ``` |
| To | ``` case activating ``` |

Modified [PKPaymentPassActivationState.deactivated](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/deactivated)

|  | Declaration |
| --- | --- |
| From | ``` case Deactivated ``` |
| To | ``` case deactivated ``` |

Modified [PKPaymentPassActivationState.requiresActivation](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/pkpaymentpassactivationstaterequiresactivation)

|  | Declaration |
| --- | --- |
| From | ``` case RequiresActivation ``` |
| To | ``` case requiresActivation ``` |

Modified [PKPaymentPassActivationState.suspended](https://developer.apple.com/documentation/passkit/pkpaymentpassactivationstate/suspended)

|  | Declaration |
| --- | --- |
| From | ``` case Suspended ``` |
| To | ``` case suspended ``` |

Modified [PKPaymentRequest](https://developer.apple.com/documentation/passkit/pkpaymentrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPaymentRequest : NSObject {     var merchantIdentifier: String     var countryCode: String     var supportedNetworks: [String]     var merchantCapabilities: PKMerchantCapability     var paymentSummaryItems: [PKPaymentSummaryItem]     var currencyCode: String     var requiredBillingAddressFields: PKAddressField     unowned(unsafe) var billingAddress: ABRecord?     var billingContact: PKContact?     var requiredShippingAddressFields: PKAddressField     unowned(unsafe) var shippingAddress: ABRecord?     var shippingContact: PKContact?     var shippingMethods: [PKShippingMethod]?     var shippingType: PKShippingType     @NSCopying var applicationData: NSData? } ``` | -- |
| To | ``` class PKPaymentRequest : NSObject {     class func availableNetworks() -> [PKPaymentNetwork]     var merchantIdentifier: String     var countryCode: String     var supportedNetworks: [PKPaymentNetwork]     var merchantCapabilities: PKMerchantCapability     var paymentSummaryItems: [PKPaymentSummaryItem]     var currencyCode: String     var requiredBillingAddressFields: PKAddressField     var billingContact: PKContact?     unowned(unsafe) var billingAddress: ABRecord?     var requiredShippingAddressFields: PKAddressField     var shippingContact: PKContact?     unowned(unsafe) var shippingAddress: ABRecord?     var shippingMethods: [PKShippingMethod]?     var shippingType: PKShippingType     var applicationData: Data?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKPaymentRequest : CVarArg { } extension PKPaymentRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPaymentRequest.applicationData](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619298-applicationdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var applicationData: NSData? ``` |
| To | ``` var applicationData: Data? ``` |

Modified [PKPaymentRequest.supportedNetworks](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619329-supportednetworks)

|  | Declaration |
| --- | --- |
| From | ``` var supportedNetworks: [String] ``` |
| To | ``` var supportedNetworks: [PKPaymentNetwork] ``` |

Modified [PKPaymentSummaryItem](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPaymentSummaryItem : NSObject {     convenience init(label label: String, amount amount: NSDecimalNumber)     class func summaryItemWithLabel(_ label: String, amount amount: NSDecimalNumber) -> Self     convenience init(label label: String, amount amount: NSDecimalNumber, type type: PKPaymentSummaryItemType)     class func summaryItemWithLabel(_ label: String, amount amount: NSDecimalNumber, type type: PKPaymentSummaryItemType) -> Self     var label: String     @NSCopying var amount: NSDecimalNumber     var type: PKPaymentSummaryItemType } ``` | -- |
| To | ``` class PKPaymentSummaryItem : NSObject {     convenience init(label label: String, amount amount: NSDecimalNumber)     class func withLabel(_ label: String, amount amount: NSDecimalNumber) -> Self     convenience init(label label: String, amount amount: NSDecimalNumber, type type: PKPaymentSummaryItemType)     class func withLabel(_ label: String, amount amount: NSDecimalNumber, type type: PKPaymentSummaryItemType) -> Self     var label: String     @NSCopying var amount: NSDecimalNumber     var type: PKPaymentSummaryItemType     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKPaymentSummaryItem : CVarArg { } extension PKPaymentSummaryItem : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPaymentSummaryItemType [enum]](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype)

|  | Declaration |
| --- | --- |
| From | ``` enum PKPaymentSummaryItemType : UInt {     case Final     case Pending } ``` |
| To | ``` enum PKPaymentSummaryItemType : UInt {     case final     case pending } ``` |

Modified [PKPaymentSummaryItemType.final](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/pkpaymentsummaryitemtypefinal)

|  | Declaration |
| --- | --- |
| From | ``` case Final ``` |
| To | ``` case final ``` |

Modified [PKPaymentSummaryItemType.pending](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype/pkpaymentsummaryitemtypepending)

|  | Declaration |
| --- | --- |
| From | ``` case Pending ``` |
| To | ``` case pending ``` |

Modified [PKPaymentToken](https://developer.apple.com/documentation/passkit/pkpaymenttoken)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPaymentToken : NSObject {     var paymentMethod: PKPaymentMethod { get }     var paymentInstrumentName: String { get }     var paymentNetwork: String { get }     var transactionIdentifier: String { get }     var paymentData: NSData { get } } ``` | -- |
| To | ``` class PKPaymentToken : NSObject {     var paymentMethod: PKPaymentMethod { get }     var paymentInstrumentName: String { get }     var paymentNetwork: String { get }     var transactionIdentifier: String { get }     var paymentData: Data { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PKPaymentToken : CVarArg { } extension PKPaymentToken : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPaymentToken.paymentData](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617000-paymentdata)

|  | Declaration |
| --- | --- |
| From | ``` var paymentData: NSData { get } ``` |
| To | ``` var paymentData: Data { get } ``` |

Modified [PKShippingType [enum]](https://developer.apple.com/documentation/passkit/pkshippingtype)

|  | Declaration |
| --- | --- |
| From | ``` enum PKShippingType : UInt {     case Shipping     case Delivery     case StorePickup     case ServicePickup } ``` |
| To | ``` enum PKShippingType : UInt {     case shipping     case delivery     case storePickup     case servicePickup } ``` |

Modified [PKShippingType.delivery](https://developer.apple.com/documentation/passkit/pkshippingtype/pkshippingtypedelivery)

|  | Declaration |
| --- | --- |
| From | ``` case Delivery ``` |
| To | ``` case delivery ``` |

Modified [PKShippingType.servicePickup](https://developer.apple.com/documentation/passkit/pkshippingtype/servicepickup)

|  | Declaration |
| --- | --- |
| From | ``` case ServicePickup ``` |
| To | ``` case servicePickup ``` |

Modified [PKShippingType.shipping](https://developer.apple.com/documentation/passkit/pkshippingtype/shipping)

|  | Declaration |
| --- | --- |
| From | ``` case Shipping ``` |
| To | ``` case shipping ``` |

Modified [PKShippingType.storePickup](https://developer.apple.com/documentation/passkit/pkshippingtype/storepickup)

|  | Declaration |
| --- | --- |
| From | ``` case StorePickup ``` |
| To | ``` case storePickup ``` |

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
