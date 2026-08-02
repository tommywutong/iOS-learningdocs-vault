---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/iAd.html
archived_at: '2026-07-18T02:55:46.586866Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# iAd Changes for Swift

### iAd (Added)

Added ADClientError [struct]Added ADClientError.init(_nsError: NSError)Added ADClientError.limitAdTrackingAdded ADClientError.unknownAdded [ADClientError.Code.limitAdTracking](https://developer.apple.com/documentation/iad/adclienterror/adclienterrorlimitadtracking)Added [ADError [struct]](https://developer.apple.com/documentation/iad/aderror)Added [ADError.adUnloaded](https://developer.apple.com/documentation/iad/aderror/2339853-adunloaded)Added [ADError.applicationInactive](https://developer.apple.com/documentation/iad/aderror/2339857-applicationinactive)Added [ADError.assetLoadFailure](https://developer.apple.com/documentation/iad/aderror/2339854-assetloadfailure)Added [ADError.bannerVisibleWithoutContent](https://developer.apple.com/documentation/iad/aderror/2339849-bannervisiblewithoutcontent)Added [ADError.configurationError](https://developer.apple.com/documentation/iad/aderror/2339856-configurationerror)Added ADError.init(_nsError: NSError)Added [ADError.inventoryUnavailable](https://developer.apple.com/documentation/iad/aderror/2339850-inventoryunavailable)Added [ADError.loadingThrottled](https://developer.apple.com/documentation/iad/aderror/2339848-loadingthrottled)Added [ADError.serverFailure](https://developer.apple.com/documentation/iad/aderror/2339855-serverfailure)Added [ADError.unknown](https://developer.apple.com/documentation/iad/aderror/2339852-unknown)Added [ADError.Code.applicationInactive](https://developer.apple.com/documentation/iad/aderror/code/applicationinactive)Added [ADError.Code.assetLoadFailure](https://developer.apple.com/documentation/iad/aderror/code/assetloadfailure)Added [ADError.Code.bannerVisibleWithoutContent](https://developer.apple.com/documentation/iad/aderror/code/bannervisiblewithoutcontent)Added [ADError.Code.inventoryUnavailable](https://developer.apple.com/documentation/iad/aderror/aderrorinventoryunavailable)Added [ADError.Code.unknown](https://developer.apple.com/documentation/iad/aderror/code/unknown)Modified [ADAdType [enum]](https://developer.apple.com/documentation/iad/adadtype)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` enum ADAdType : Int {     case Banner     case MediumRectangle } ``` | -- | iAdJS |
| To | ``` enum ADAdType : Int {     case banner     case mediumRectangle } ``` | iOS 10.0 | iAd |

Modified [ADAdType.banner](https://developer.apple.com/documentation/iad/adadtype/adadtypebanner)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Banner ``` | iAdJS |
| To | ``` case banner ``` | iAd |

Modified [ADAdType.mediumRectangle](https://developer.apple.com/documentation/iad/adadtype/mediumrectangle)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case MediumRectangle ``` | iAdJS |
| To | ``` case mediumRectangle ``` | iAd |

Modified [ADBannerView](https://developer.apple.com/documentation/iad/adbannerview)

|  | Declaration | Protocols | Deprecation | Module |
| --- | --- | --- | --- | --- |
| From | ``` class ADBannerView : UIView {     init!(adType type: ADAdType)     var adType: ADAdType { get }     weak var delegate: ADBannerViewDelegate!     var bannerLoaded: Bool { get }     var bannerViewActionInProgress: Bool { get }     func cancelBannerViewAction()     var advertisingSection: String! } extension ADBannerView {     var requiredContentSizeIdentifiers: Set<NSObject>!     var currentContentSizeIdentifier: String!     class func sizeFromBannerContentSizeIdentifier(_ contentSizeIdentifier: String!) -> CGSize } ``` | -- | -- | iAdJS |
| To | ``` class ADBannerView : UIView {     init!(adType type: ADAdType)     var adType: ADAdType { get }     weak var delegate: ADBannerViewDelegate!     var isBannerLoaded: Bool { get }     var isBannerViewActionInProgress: Bool { get }     func cancelAction()     var advertisingSection: String!     var requiredContentSizeIdentifiers: Set<AnyHashable>!     var currentContentSizeIdentifier: String!     class func size(fromBannerContentSizeIdentifier contentSizeIdentifier: String!) -> CGSize     func viewPrintFormatter() -> UIViewPrintFormatter     func draw(_ rect: CGRect, for formatter: UIViewPrintFormatter)     func endEditing(_ force: Bool) -> Bool     func snapshotView(afterScreenUpdates afterUpdates: Bool) -> UIView?     func resizableSnapshotView(from rect: CGRect, afterScreenUpdates afterUpdates: Bool, withCapInsets capInsets: UIEdgeInsets) -> UIView?     func drawHierarchy(in rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool     var restorationIdentifier: String?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func constraintsAffectingLayout(for axis: UILayoutConstraintAxis) -> [NSLayoutConstraint]     var hasAmbiguousLayout: Bool { get }     func exerciseAmbiguityInLayout()     var leadingAnchor: NSLayoutXAxisAnchor { get }     var trailingAnchor: NSLayoutXAxisAnchor { get }     var leftAnchor: NSLayoutXAxisAnchor { get }     var rightAnchor: NSLayoutXAxisAnchor { get }     var topAnchor: NSLayoutYAxisAnchor { get }     var bottomAnchor: NSLayoutYAxisAnchor { get }     var widthAnchor: NSLayoutDimension { get }     var heightAnchor: NSLayoutDimension { get }     var centerXAnchor: NSLayoutXAxisAnchor { get }     var centerYAnchor: NSLayoutYAxisAnchor { get }     var firstBaselineAnchor: NSLayoutYAxisAnchor { get }     var lastBaselineAnchor: NSLayoutYAxisAnchor { get }     var layoutGuides: [UILayoutGuide] { get }     func addLayoutGuide(_ layoutGuide: UILayoutGuide)     func removeLayoutGuide(_ layoutGuide: UILayoutGuide)     func systemLayoutSizeFitting(_ targetSize: CGSize) -> CGSize     func systemLayoutSizeFitting(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority verticalFittingPriority: UILayoutPriority) -> CGSize     func alignmentRect(forFrame frame: CGRect) -> CGRect     func frame(forAlignmentRect alignmentRect: CGRect) -> CGRect     var alignmentRectInsets: UIEdgeInsets { get }     func forBaselineLayout() -> UIView     var forFirstBaselineLayout: UIView { get }     var forLastBaselineLayout: UIView { get }     var intrinsicContentSize: CGSize { get }     func invalidateIntrinsicContentSize()     func contentHuggingPriority(for axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentHuggingPriority(_ priority: UILayoutPriority, for axis: UILayoutConstraintAxis)     func contentCompressionResistancePriority(for axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentCompressionResistancePriority(_ priority: UILayoutPriority, for axis: UILayoutConstraintAxis)     var translatesAutoresizingMaskIntoConstraints: Bool     class var requiresConstraintBasedLayout: Bool { get }     func updateConstraintsIfNeeded()     func updateConstraints()     func needsUpdateConstraints() -> Bool     func setNeedsUpdateConstraints()     var constraints: [NSLayoutConstraint] { get }     func addConstraint(_ constraint: NSLayoutConstraint)     func addConstraints(_ constraints: [NSLayoutConstraint])     func removeConstraint(_ constraint: NSLayoutConstraint)     func removeConstraints(_ constraints: [NSLayoutConstraint])     func addMotionEffect(_ effect: UIMotionEffect)     func removeMotionEffect(_ effect: UIMotionEffect)     var motionEffects: [UIMotionEffect]     var gestureRecognizers: [UIGestureRecognizer]?     func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool     class func animateKeyframes(withDuration duration: TimeInterval, delay delay: TimeInterval, options options: UIViewKeyframeAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func addKeyframe(withRelativeStartTime frameStartTime: Double, relativeDuration frameDuration: Double, animations animations: @escaping () -> Void)     class func animate(withDuration duration: TimeInterval, delay delay: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Void)     class func animate(withDuration duration: TimeInterval, delay delay: TimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options options: UIViewAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func transition(with view: UIView, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     class func transition(from fromView: UIView, to toView: UIView, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], completion completion: (@escaping (Bool) -> Void)? = nil)     class func perform(_ animation: UISystemAnimation, on views: [UIView], options options: UIViewAnimationOptions = [], animations parallelAnimations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     class func beginAnimations(_ animationID: String?, context context: UnsafeMutableRawPointer?)     class func commitAnimations()     class func setAnimationDelegate(_ delegate: Any?)     class func setAnimationWillStart(_ selector: Selector?)     class func setAnimationDidStop(_ selector: Selector?)     class func setAnimationDuration(_ duration: TimeInterval)     class func setAnimationDelay(_ delay: TimeInterval)     class func setAnimationStart(_ startDate: Date)     class func setAnimationCurve(_ curve: UIViewAnimationCurve)     class func setAnimationRepeatCount(_ repeatCount: Float)     class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)     class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)     class func setAnimationTransition(_ transition: UIViewAnimationTransition, for view: UIView, cache cache: Bool)     class func setAnimationsEnabled(_ enabled: Bool)     class var areAnimationsEnabled: Bool { get }     class func performWithoutAnimation(_ actionsWithoutAnimation: () -> Void)     class var inheritedAnimationDuration: TimeInterval { get }     func draw(_ rect: CGRect)     func setNeedsDisplay()     func setNeedsDisplay(_ rect: CGRect)     var clipsToBounds: Bool     @NSCopying var backgroundColor: UIColor?     var alpha: CGFloat     var isOpaque: Bool     var clearsContextBeforeDrawing: Bool     var isHidden: Bool     var contentMode: UIViewContentMode     var contentStretch: CGRect     var mask: UIView?     var tintColor: UIColor!     var tintAdjustmentMode: UIViewTintAdjustmentMode     func tintColorDidChange()     var superview: UIView? { get }     var subviews: [UIView] { get }     var window: UIWindow? { get }     func removeFromSuperview()     func insertSubview(_ view: UIView, at index: Int)     func exchangeSubview(at index1: Int, withSubviewAt index2: Int)     func addSubview(_ view: UIView)     func insertSubview(_ view: UIView, belowSubview siblingSubview: UIView)     func insertSubview(_ view: UIView, aboveSubview siblingSubview: UIView)     func bringSubview(toFront view: UIView)     func sendSubview(toBack view: UIView)     func didAddSubview(_ subview: UIView)     func willRemoveSubview(_ subview: UIView)     func willMove(toSuperview newSuperview: UIView?)     func didMoveToSuperview()     func willMove(toWindow newWindow: UIWindow?)     func didMoveToWindow()     func isDescendant(of view: UIView) -> Bool     func viewWithTag(_ tag: Int) -> UIView?     func setNeedsLayout()     func layoutIfNeeded()     func layoutSubviews()     var layoutMargins: UIEdgeInsets     var preservesSuperviewLayoutMargins: Bool     func layoutMarginsDidChange()     var layoutMarginsGuide: UILayoutGuide { get }     var readableContentGuide: UILayoutGuide { get }     var frame: CGRect     var bounds: CGRect     var center: CGPoint     var transform: CGAffineTransform     var contentScaleFactor: CGFloat     var isMultipleTouchEnabled: Bool     var isExclusiveTouch: Bool     func hitTest(_ point: CGPoint, with event: UIEvent?) -> UIView?     func point(inside point: CGPoint, with event: UIEvent?) -> Bool     func convert(_ point: CGPoint, to view: UIView?) -> CGPoint     func convert(_ point: CGPoint, from view: UIView?) -> CGPoint     func convert(_ rect: CGRect, to view: UIView?) -> CGRect     func convert(_ rect: CGRect, from view: UIView?) -> CGRect     var autoresizesSubviews: Bool     var autoresizingMask: UIViewAutoresizing     func sizeThatFits(_ size: CGSize) -> CGSize     func sizeToFit()     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews() } extension ADBannerView : UIAccessibilityIdentification { } extension ADBannerView : CVarArg { } extension ADBannerView : Equatable, Hashable {     var hashValue: Int { get } } extension ADBannerView {     var requiredContentSizeIdentifiers: Set<AnyHashable>!     var currentContentSizeIdentifier: String!     class func size(fromBannerContentSizeIdentifier contentSizeIdentifier: String!) -> CGSize } ``` | CVarArg, Equatable, Hashable, UIAccessibilityIdentification | iOS 10.0 | iAd |

Modified [ADBannerView.adType](https://developer.apple.com/documentation/iad/adbannerview/1614621-adtype)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [ADBannerView.advertisingSection](https://developer.apple.com/documentation/iad/adbannerview/1614674-advertisingsection)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [ADBannerView.cancelAction()](https://developer.apple.com/documentation/iad/adbannerview/1614632-cancelaction)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` func cancelBannerViewAction() ``` | -- | iAdJS |
| To | ``` func cancelAction() ``` | iOS 10.0 | iAd |

Modified [ADBannerView.delegate](https://developer.apple.com/documentation/iad/adbannerview/1614649-delegate)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [ADBannerView.init(adType: ADAdType)](https://developer.apple.com/documentation/iad/adbannerview/1614692-initwithadtype)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [ADBannerView.isBannerLoaded](https://developer.apple.com/documentation/iad/adbannerview/1614635-isbannerloaded)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` var bannerLoaded: Bool { get } ``` | -- | iAdJS |
| To | ``` var isBannerLoaded: Bool { get } ``` | iOS 10.0 | iAd |

Modified [ADBannerView.isBannerViewActionInProgress](https://developer.apple.com/documentation/iad/adbannerview/1614656-isbannerviewactioninprogress)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` var bannerViewActionInProgress: Bool { get } ``` | -- | iAdJS |
| To | ``` var isBannerViewActionInProgress: Bool { get } ``` | iOS 10.0 | iAd |

Modified [ADBannerViewDelegate](https://developer.apple.com/documentation/iad/adbannerviewdelegate)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` protocol ADBannerViewDelegate : NSObjectProtocol {     optional func bannerViewWillLoadAd(_ banner: ADBannerView!)     optional func bannerViewDidLoadAd(_ banner: ADBannerView!)     optional func bannerView(_ banner: ADBannerView!, didFailToReceiveAdWithError error: NSError!)     optional func bannerViewActionShouldBegin(_ banner: ADBannerView!, willLeaveApplication willLeave: Bool) -> Bool     optional func bannerViewActionDidFinish(_ banner: ADBannerView!) } ``` | iAdJS |
| To | ``` protocol ADBannerViewDelegate : NSObjectProtocol {     optional func bannerViewWillLoadAd(_ banner: ADBannerView!)     optional func bannerViewDidLoadAd(_ banner: ADBannerView!)     optional func bannerView(_ banner: ADBannerView!, didFailToReceiveAdWithError error: Error!)     optional func bannerViewActionShouldBegin(_ banner: ADBannerView!, willLeaveApplication willLeave: Bool) -> Bool     optional func bannerViewActionDidFinish(_ banner: ADBannerView!) } ``` | iAd |

Modified [ADBannerViewDelegate.bannerView(_: ADBannerView!, didFailToReceiveAdWithError: Error!)](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614619-bannerview)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` optional func bannerView(_ banner: ADBannerView!, didFailToReceiveAdWithError error: NSError!) ``` | iAdJS |
| To | ``` optional func bannerView(_ banner: ADBannerView!, didFailToReceiveAdWithError error: Error!) ``` | iAd |

Modified [ADBannerViewDelegate.bannerViewActionDidFinish(_: ADBannerView!)](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614662-bannerviewactiondidfinish)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [ADBannerViewDelegate.bannerViewActionShouldBegin(_: ADBannerView!, willLeaveApplication: Bool) -> Bool](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614641-bannerviewactionshouldbegin)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [ADBannerViewDelegate.bannerViewDidLoadAd(_: ADBannerView!)](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614625-bannerviewdidloadad)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [ADBannerViewDelegate.bannerViewWillLoadAd(_: ADBannerView!)](https://developer.apple.com/documentation/iad/adbannerviewdelegate/1614636-bannerviewwillloadad)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [ADClient](https://developer.apple.com/documentation/iad/adclient)

|  | Declaration | Protocols | Module |
| --- | --- | --- | --- |
| From | ``` class ADClient : NSObject {     class func sharedClient() -> ADClient!     func determineAppInstallationAttributionWithCompletionHandler(_ completionHandler: ((Bool) -> Void)!)     func lookupAdConversionDetails(_ completionHandler: ((NSDate!, NSDate!) -> Void)!)     func requestAttributionDetailsWithBlock(_ completionHandler: (([NSObject : AnyObject]!, NSError!) -> Void)!)     func addClientToSegments(_ segmentIdentifiers: [AnyObject]!, replaceExisting replaceExisting: Bool) } ``` | -- | iAdJS |
| To | ``` class ADClient : NSObject {     class func shared() -> ADClient!     func determineAppInstallationAttribution(completionHandler completionHandler: (@escaping (Bool) -> Swift.Void)!)     func lookupAdConversionDetails(_ completionHandler: (@escaping (Date?, Date?) -> Swift.Void)!)     func requestAttributionDetails(_ completionHandler: (@escaping ([AnyHashable : Any]?, Error?) -> Swift.Void)!)     func add(toSegments segmentIdentifiers: [Any]!, replaceExisting replaceExisting: Bool)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension ADClient : CVarArg { } extension ADClient : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable | iAd |

Modified [ADClient.add(toSegments: [Any]!, replaceExisting: Bool)](https://developer.apple.com/documentation/iad/adclient/1614607-addclienttosegments)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func addClientToSegments(_ segmentIdentifiers: [AnyObject]!, replaceExisting replaceExisting: Bool) ``` | iAdJS |
| To | ``` func add(toSegments segmentIdentifiers: [Any]!, replaceExisting replaceExisting: Bool) ``` | iAd |

Modified [ADClient.determineAppInstallationAttribution(completionHandler: ( (Bool) -> Swift.Void)!)](https://developer.apple.com/documentation/iad/adclient/1614672-determineappinstallationattribut)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func determineAppInstallationAttributionWithCompletionHandler(_ completionHandler: ((Bool) -> Void)!) ``` | iAdJS |
| To | ``` func determineAppInstallationAttribution(completionHandler completionHandler: (@escaping (Bool) -> Swift.Void)!) ``` | iAd |

Modified [ADClient.lookupAdConversionDetails(_: ( (Date?, Date?) -> Swift.Void)!)](https://developer.apple.com/documentation/iad/adclient/1614612-lookupadconversiondetails)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func lookupAdConversionDetails(_ completionHandler: ((NSDate!, NSDate!) -> Void)!) ``` | iAdJS |
| To | ``` func lookupAdConversionDetails(_ completionHandler: (@escaping (Date?, Date?) -> Swift.Void)!) ``` | iAd |

Modified [ADClient.requestAttributionDetails(_: ( ([AnyHashable : Any]?, Error?) -> Swift.Void)!)](https://developer.apple.com/documentation/iad/adclient/1614620-requestattributiondetails)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func requestAttributionDetailsWithBlock(_ completionHandler: (([NSObject : AnyObject]!, NSError!) -> Void)!) ``` | iAdJS |
| To | ``` func requestAttributionDetails(_ completionHandler: (@escaping ([AnyHashable : Any]?, Error?) -> Swift.Void)!) ``` | iAd |

Modified [ADClient.shared() -> ADClient! [class]](https://developer.apple.com/documentation/iad/adclient/1614686-sharedclient)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func sharedClient() -> ADClient! ``` | iAdJS |
| To | ``` class func shared() -> ADClient! ``` | iAd |

Modified [ADClientError.Code [enum]](https://developer.apple.com/documentation/iad/adclienterror/code)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum ADClientError : Int {     case Unknown     case LimitAdTracking } ``` | iAdJS |
| To | ``` enum Code : Int {         typealias _ErrorType = ADClientError         case unknown         case limitAdTracking     } ``` | iAd |

Modified [ADClientError.Code.unknown](https://developer.apple.com/documentation/iad/adclienterror/code/unknown)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Unknown ``` | iAdJS |
| To | ``` case unknown ``` | iAd |

Modified [ADError.Code [enum]](https://developer.apple.com/documentation/iad/aderror/code)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` enum ADError : Int {     case Unknown     case ServerFailure     case LoadingThrottled     case InventoryUnavailable     case ConfigurationError     case BannerVisibleWithoutContent     case ApplicationInactive     case AdUnloaded     case AssetLoadFailure } ``` | iAdJS |
| To | ``` enum Code : Int {         typealias _ErrorType = ADError         case unknown         case serverFailure         case loadingThrottled         case inventoryUnavailable         case configurationError         case bannerVisibleWithoutContent         case applicationInactive         case adUnloaded         case assetLoadFailure     } ``` | iAd |

Modified [ADError.Code.adUnloaded](https://developer.apple.com/documentation/iad/aderror/aderroradunloaded)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case AdUnloaded ``` | iAdJS |
| To | ``` case adUnloaded ``` | iAd |

Modified [ADError.Code.configurationError](https://developer.apple.com/documentation/iad/aderror/code/configurationerror)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ConfigurationError ``` | iAdJS |
| To | ``` case configurationError ``` | iAd |

Modified [ADError.Code.loadingThrottled](https://developer.apple.com/documentation/iad/aderror/aderrorloadingthrottled)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case LoadingThrottled ``` | iAdJS |
| To | ``` case loadingThrottled ``` | iAd |

Modified [ADError.Code.serverFailure](https://developer.apple.com/documentation/iad/aderror/aderrorserverfailure)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case ServerFailure ``` | iAdJS |
| To | ``` case serverFailure ``` | iAd |

Modified [ADInterstitialAd](https://developer.apple.com/documentation/iad/adinterstitialad)

|  | Declaration | Protocols | Deprecation | Module |
| --- | --- | --- | --- | --- |
| From | ``` class ADInterstitialAd : NSObject {     weak var delegate: ADInterstitialAdDelegate!     var loaded: Bool { get }     var actionInProgress: Bool { get }     func cancelAction()     func presentInView(_ containerView: UIView!) -> Bool     func presentFromViewController(_ viewController: UIViewController!) } ``` | -- | -- | iAdJS |
| To | ``` class ADInterstitialAd : NSObject {     weak var delegate: ADInterstitialAdDelegate!     var isLoaded: Bool { get }     var isActionInProgress: Bool { get }     func cancelAction()     func present(in containerView: UIView!) -> Bool     func present(from viewController: UIViewController!)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension ADInterstitialAd : CVarArg { } extension ADInterstitialAd : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable | iOS 10.0 | iAd |

Modified [ADInterstitialAd.cancelAction()](https://developer.apple.com/documentation/iad/adinterstitialad/1614616-cancelaction)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [ADInterstitialAd.delegate](https://developer.apple.com/documentation/iad/adinterstitialad/1614647-delegate)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [ADInterstitialAd.isActionInProgress](https://developer.apple.com/documentation/iad/adinterstitialad/1614658-isactioninprogress)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` var actionInProgress: Bool { get } ``` | -- | iAdJS |
| To | ``` var isActionInProgress: Bool { get } ``` | iOS 10.0 | iAd |

Modified [ADInterstitialAd.isLoaded](https://developer.apple.com/documentation/iad/adinterstitialad/1614653-isloaded)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` var loaded: Bool { get } ``` | -- | iAdJS |
| To | ``` var isLoaded: Bool { get } ``` | iOS 10.0 | iAd |

Modified [ADInterstitialAd.present(in: UIView!) -> Bool](https://developer.apple.com/documentation/iad/adinterstitialad/1614646-present)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` func presentInView(_ containerView: UIView!) -> Bool ``` | -- | iAdJS |
| To | ``` func present(in containerView: UIView!) -> Bool ``` | iOS 10.0 | iAd |

Modified [ADInterstitialAdDelegate](https://developer.apple.com/documentation/iad/adinterstitialaddelegate)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` protocol ADInterstitialAdDelegate : NSObjectProtocol {     func interstitialAdDidUnload(_ interstitialAd: ADInterstitialAd!)     func interstitialAd(_ interstitialAd: ADInterstitialAd!, didFailWithError error: NSError!)     optional func interstitialAdWillLoad(_ interstitialAd: ADInterstitialAd!)     optional func interstitialAdDidLoad(_ interstitialAd: ADInterstitialAd!)     optional func interstitialAdActionShouldBegin(_ interstitialAd: ADInterstitialAd!, willLeaveApplication willLeave: Bool) -> Bool     optional func interstitialAdActionDidFinish(_ interstitialAd: ADInterstitialAd!) } ``` | iAdJS |
| To | ``` protocol ADInterstitialAdDelegate : NSObjectProtocol {     func interstitialAdDidUnload(_ interstitialAd: ADInterstitialAd!)     func interstitialAd(_ interstitialAd: ADInterstitialAd!, didFailWithError error: Error!)     optional func interstitialAdWillLoad(_ interstitialAd: ADInterstitialAd!)     optional func interstitialAdDidLoad(_ interstitialAd: ADInterstitialAd!)     optional func interstitialAdActionShouldBegin(_ interstitialAd: ADInterstitialAd!, willLeaveApplication willLeave: Bool) -> Bool     optional func interstitialAdActionDidFinish(_ interstitialAd: ADInterstitialAd!) } ``` | iAd |

Modified [ADInterstitialAdDelegate.interstitialAd(_: ADInterstitialAd!, didFailWithError: Error!)](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614645-interstitialad)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func interstitialAd(_ interstitialAd: ADInterstitialAd!, didFailWithError error: NSError!) ``` | iAdJS |
| To | ``` func interstitialAd(_ interstitialAd: ADInterstitialAd!, didFailWithError error: Error!) ``` | iAd |

Modified [ADInterstitialAdDelegate.interstitialAdActionDidFinish(_: ADInterstitialAd!)](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614637-interstitialadactiondidfinish)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [ADInterstitialAdDelegate.interstitialAdActionShouldBegin(_: ADInterstitialAd!, willLeaveApplication: Bool) -> Bool](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614652-interstitialadactionshouldbegin)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [ADInterstitialAdDelegate.interstitialAdDidLoad(_: ADInterstitialAd!)](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614609-interstitialaddidload)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [ADInterstitialAdDelegate.interstitialAdDidUnload(_: ADInterstitialAd!)](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614651-interstitialaddidunload)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [ADInterstitialAdDelegate.interstitialAdWillLoad(_: ADInterstitialAd!)](https://developer.apple.com/documentation/iad/adinterstitialaddelegate/1614688-interstitialadwillload)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [ADInterstitialPresentationPolicy [enum]](https://developer.apple.com/documentation/iad/adinterstitialpresentationpolicy)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` enum ADInterstitialPresentationPolicy : Int {     case None     case Automatic     case Manual } ``` | -- | iAdJS |
| To | ``` enum ADInterstitialPresentationPolicy : Int {     case none     case automatic     case manual } ``` | iOS 10.0 | iAd |

Modified [ADInterstitialPresentationPolicy.automatic](https://developer.apple.com/documentation/iad/adinterstitialpresentationpolicy/adinterstitialpresentationpolicyautomatic)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Automatic ``` | iAdJS |
| To | ``` case automatic ``` | iAd |

Modified [ADInterstitialPresentationPolicy.manual](https://developer.apple.com/documentation/iad/adinterstitialpresentationpolicy/manual)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case Manual ``` | iAdJS |
| To | ``` case manual ``` | iAd |

Modified [ADInterstitialPresentationPolicy.none](https://developer.apple.com/documentation/iad/adinterstitialpresentationpolicy/adinterstitialpresentationpolicynone)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` case None ``` | iAdJS |
| To | ``` case none ``` | iAd |

Modified [AVPlayerViewController.cancelPreroll()](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1614626-cancelpreroll)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [AVPlayerViewController.playPrerollAd(completionHandler: ( (Error?) -> Swift.Void)!)](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1614638-playprerolladwithcompletionhandl)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func playPrerollAdWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!) ``` | iAdJS |
| To | ``` func playPrerollAd(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)!) ``` | iAd |

Modified [AVPlayerViewController.preparePrerollAds() [class]](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/1614660-prepareprerollads)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [MPMoviePlayerController.cancelPreroll()](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1614613-cancelpreroll)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [MPMoviePlayerController.playPrerollAd(completionHandler: ( (Error?) -> Swift.Void)!)](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1614690-playprerolladwithcompletionhandl)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func playPrerollAdWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!) ``` | iAdJS |
| To | ``` func playPrerollAd(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)!) ``` | iAd |

Modified [MPMoviePlayerController.preparePrerollAds() [class]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1614610-prepareprerollads)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [UIViewController.canDisplayBannerAds](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614606-candisplaybannerads)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [UIViewController.interstitialPresentationPolicy](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614670-interstitialpresentationpolicy)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [UIViewController.isDisplayingBannerAd](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614640-displayingbannerad)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` var displayingBannerAd: Bool { get } ``` | -- | iAdJS |
| To | ``` var isDisplayingBannerAd: Bool { get } ``` | iOS 10.0 | iAd |

Modified [UIViewController.isPresentingFullScreenAd](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614630-ispresentingfullscreenad)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` var presentingFullScreenAd: Bool { get } ``` | -- | iAdJS |
| To | ``` var isPresentingFullScreenAd: Bool { get } ``` | iOS 10.0 | iAd |

Modified [UIViewController.originalContentView](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614605-originalcontentview)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [UIViewController.prepareInterstitialAds() [class]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614624-prepareinterstitialads)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [UIViewController.requestInterstitialAdPresentation() -> Bool](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614631-requestinterstitialadpresentatio)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [UIViewController.shouldPresentInterstitialAd](https://developer.apple.com/documentation/uikit/uiviewcontroller/1614627-shouldpresentinterstitialad)

|  | Deprecation | Module |
| --- | --- | --- |
| From | -- | iAdJS |
| To | iOS 10.0 | iAd |

Modified [ADClientErrorDomain](https://developer.apple.com/documentation/iad/adclienterrordomain)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

Modified [ADErrorDomain](https://developer.apple.com/documentation/iad/aderrordomain)

|  | Module |
| --- | --- |
| From | iAdJS |
| To | iAd |

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
