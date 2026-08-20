---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/PhotosUI.html
archived_at: '2026-07-18T02:55:36.621151Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# PhotosUI Changes for Swift

### PhotosUI

Modified [PHContentEditingController](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller)

|  | Declaration |
| --- | --- |
| From | ``` protocol PHContentEditingController : NSObjectProtocol {     func canHandleAdjustmentData(_ adjustmentData: PHAdjustmentData!) -> Bool     func startContentEditingWithInput(_ contentEditingInput: PHContentEditingInput!, placeholderImage placeholderImage: UIImage!)     func finishContentEditingWithCompletionHandler(_ completionHandler: ((PHContentEditingOutput!) -> Void)!)     func cancelContentEditing()     var shouldShowCancelConfirmation: Bool { get } } ``` |
| To | ``` protocol PHContentEditingController : NSObjectProtocol {     func canHandle(_ adjustmentData: PHAdjustmentData) -> Bool     func startContentEditing(with contentEditingInput: PHContentEditingInput, placeholderImage placeholderImage: UIImage)     func finishContentEditing(completionHandler completionHandler: @escaping (PHContentEditingOutput?) -> Swift.Void)     func cancelContentEditing()     var shouldShowCancelConfirmation: Bool { get } } ``` |

Modified [PHContentEditingController.canHandle(_: PHAdjustmentData) -> Bool](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller/1501739-canhandle)

|  | Declaration |
| --- | --- |
| From | ``` func canHandleAdjustmentData(_ adjustmentData: PHAdjustmentData!) -> Bool ``` |
| To | ``` func canHandle(_ adjustmentData: PHAdjustmentData) -> Bool ``` |

Modified [PHContentEditingController.finishContentEditing(completionHandler: (PHContentEditingOutput?) -> Swift.Void)](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller/1501741-finishcontentediting)

|  | Declaration |
| --- | --- |
| From | ``` func finishContentEditingWithCompletionHandler(_ completionHandler: ((PHContentEditingOutput!) -> Void)!) ``` |
| To | ``` func finishContentEditing(completionHandler completionHandler: @escaping (PHContentEditingOutput?) -> Swift.Void) ``` |

Modified [PHContentEditingController.startContentEditing(with: PHContentEditingInput, placeholderImage: UIImage)](https://developer.apple.com/documentation/photokit/phcontenteditingcontroller/1501738-startcontenteditingwithinput)

|  | Declaration |
| --- | --- |
| From | ``` func startContentEditingWithInput(_ contentEditingInput: PHContentEditingInput!, placeholderImage placeholderImage: UIImage!) ``` |
| To | ``` func startContentEditing(with contentEditingInput: PHContentEditingInput, placeholderImage placeholderImage: UIImage) ``` |

Modified [PHLivePhotoBadgeOptions [struct]](https://developer.apple.com/documentation/photokit/phlivephotobadgeoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PHLivePhotoBadgeOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var OverContent: PHLivePhotoBadgeOptions { get }     static var LiveOff: PHLivePhotoBadgeOptions { get } } ``` | OptionSetType |
| To | ``` struct PHLivePhotoBadgeOptions : OptionSet {     init(rawValue rawValue: UInt)     static var overContent: PHLivePhotoBadgeOptions { get }     static var liveOff: PHLivePhotoBadgeOptions { get }     func intersect(_ other: PHLivePhotoBadgeOptions) -> PHLivePhotoBadgeOptions     func exclusiveOr(_ other: PHLivePhotoBadgeOptions) -> PHLivePhotoBadgeOptions     mutating func unionInPlace(_ other: PHLivePhotoBadgeOptions)     mutating func intersectInPlace(_ other: PHLivePhotoBadgeOptions)     mutating func exclusiveOrInPlace(_ other: PHLivePhotoBadgeOptions)     func isSubsetOf(_ other: PHLivePhotoBadgeOptions) -> Bool     func isDisjointWith(_ other: PHLivePhotoBadgeOptions) -> Bool     func isSupersetOf(_ other: PHLivePhotoBadgeOptions) -> Bool     mutating func subtractInPlace(_ other: PHLivePhotoBadgeOptions)     func isStrictSupersetOf(_ other: PHLivePhotoBadgeOptions) -> Bool     func isStrictSubsetOf(_ other: PHLivePhotoBadgeOptions) -> Bool } extension PHLivePhotoBadgeOptions {     func union(_ other: PHLivePhotoBadgeOptions) -> PHLivePhotoBadgeOptions     func intersection(_ other: PHLivePhotoBadgeOptions) -> PHLivePhotoBadgeOptions     func symmetricDifference(_ other: PHLivePhotoBadgeOptions) -> PHLivePhotoBadgeOptions } extension PHLivePhotoBadgeOptions {     func contains(_ member: PHLivePhotoBadgeOptions) -> Bool     mutating func insert(_ newMember: PHLivePhotoBadgeOptions) -> (inserted: Bool, memberAfterInsert: PHLivePhotoBadgeOptions)     mutating func remove(_ member: PHLivePhotoBadgeOptions) -> PHLivePhotoBadgeOptions?     mutating func update(with newMember: PHLivePhotoBadgeOptions) -> PHLivePhotoBadgeOptions? } extension PHLivePhotoBadgeOptions {     convenience init()     mutating func formUnion(_ other: PHLivePhotoBadgeOptions)     mutating func formIntersection(_ other: PHLivePhotoBadgeOptions)     mutating func formSymmetricDifference(_ other: PHLivePhotoBadgeOptions) } extension PHLivePhotoBadgeOptions {     convenience init<S : Sequence where S.Iterator.Element == PHLivePhotoBadgeOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: PHLivePhotoBadgeOptions...)     mutating func subtract(_ other: PHLivePhotoBadgeOptions)     func isSubset(of other: PHLivePhotoBadgeOptions) -> Bool     func isSuperset(of other: PHLivePhotoBadgeOptions) -> Bool     func isDisjoint(with other: PHLivePhotoBadgeOptions) -> Bool     func subtracting(_ other: PHLivePhotoBadgeOptions) -> PHLivePhotoBadgeOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: PHLivePhotoBadgeOptions) -> Bool     func isStrictSubset(of other: PHLivePhotoBadgeOptions) -> Bool } ``` | OptionSet |

Modified [PHLivePhotoBadgeOptions.liveOff](https://developer.apple.com/documentation/photokit/phlivephotobadgeoptions/phlivephotobadgeoptionsliveoff)

|  | Declaration |
| --- | --- |
| From | ``` static var LiveOff: PHLivePhotoBadgeOptions { get } ``` |
| To | ``` static var liveOff: PHLivePhotoBadgeOptions { get } ``` |

Modified [PHLivePhotoBadgeOptions.overContent](https://developer.apple.com/documentation/photokit/phlivephotobadgeoptions/1623422-overcontent)

|  | Declaration |
| --- | --- |
| From | ``` static var OverContent: PHLivePhotoBadgeOptions { get } ``` |
| To | ``` static var overContent: PHLivePhotoBadgeOptions { get } ``` |

Modified [PHLivePhotoView](https://developer.apple.com/documentation/photokit/phlivephotoview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PHLivePhotoView : UIView {     class func livePhotoBadgeImageWithOptions(_ badgeOptions: PHLivePhotoBadgeOptions) -> UIImage     weak var delegate: PHLivePhotoViewDelegate?     var livePhoto: PHLivePhoto?     var muted: Bool     var playbackGestureRecognizer: UIGestureRecognizer { get }     func startPlaybackWithStyle(_ playbackStyle: PHLivePhotoViewPlaybackStyle)     func stopPlayback() } ``` | -- |
| To | ``` class PHLivePhotoView : UIView {     class func livePhotoBadgeImage(options badgeOptions: PHLivePhotoBadgeOptions = []) -> UIImage     weak var delegate: PHLivePhotoViewDelegate?     var livePhoto: PHLivePhoto?     var isMuted: Bool     var playbackGestureRecognizer: UIGestureRecognizer { get }     func startPlayback(with playbackStyle: PHLivePhotoViewPlaybackStyle)     func stopPlayback()     func viewPrintFormatter() -> UIViewPrintFormatter     func draw(_ rect: CGRect, for formatter: UIViewPrintFormatter)     func endEditing(_ force: Bool) -> Bool     func snapshotView(afterScreenUpdates afterUpdates: Bool) -> UIView?     func resizableSnapshotView(from rect: CGRect, afterScreenUpdates afterUpdates: Bool, withCapInsets capInsets: UIEdgeInsets) -> UIView?     func drawHierarchy(in rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool     var restorationIdentifier: String?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func constraintsAffectingLayout(for axis: UILayoutConstraintAxis) -> [NSLayoutConstraint]     var hasAmbiguousLayout: Bool { get }     func exerciseAmbiguityInLayout()     var leadingAnchor: NSLayoutXAxisAnchor { get }     var trailingAnchor: NSLayoutXAxisAnchor { get }     var leftAnchor: NSLayoutXAxisAnchor { get }     var rightAnchor: NSLayoutXAxisAnchor { get }     var topAnchor: NSLayoutYAxisAnchor { get }     var bottomAnchor: NSLayoutYAxisAnchor { get }     var widthAnchor: NSLayoutDimension { get }     var heightAnchor: NSLayoutDimension { get }     var centerXAnchor: NSLayoutXAxisAnchor { get }     var centerYAnchor: NSLayoutYAxisAnchor { get }     var firstBaselineAnchor: NSLayoutYAxisAnchor { get }     var lastBaselineAnchor: NSLayoutYAxisAnchor { get }     var layoutGuides: [UILayoutGuide] { get }     func addLayoutGuide(_ layoutGuide: UILayoutGuide)     func removeLayoutGuide(_ layoutGuide: UILayoutGuide)     func systemLayoutSizeFitting(_ targetSize: CGSize) -> CGSize     func systemLayoutSizeFitting(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority verticalFittingPriority: UILayoutPriority) -> CGSize     func alignmentRect(forFrame frame: CGRect) -> CGRect     func frame(forAlignmentRect alignmentRect: CGRect) -> CGRect     var alignmentRectInsets: UIEdgeInsets { get }     func forBaselineLayout() -> UIView     var forFirstBaselineLayout: UIView { get }     var forLastBaselineLayout: UIView { get }     var intrinsicContentSize: CGSize { get }     func invalidateIntrinsicContentSize()     func contentHuggingPriority(for axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentHuggingPriority(_ priority: UILayoutPriority, for axis: UILayoutConstraintAxis)     func contentCompressionResistancePriority(for axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentCompressionResistancePriority(_ priority: UILayoutPriority, for axis: UILayoutConstraintAxis)     var translatesAutoresizingMaskIntoConstraints: Bool     class var requiresConstraintBasedLayout: Bool { get }     func updateConstraintsIfNeeded()     func updateConstraints()     func needsUpdateConstraints() -> Bool     func setNeedsUpdateConstraints()     var constraints: [NSLayoutConstraint] { get }     func addConstraint(_ constraint: NSLayoutConstraint)     func addConstraints(_ constraints: [NSLayoutConstraint])     func removeConstraint(_ constraint: NSLayoutConstraint)     func removeConstraints(_ constraints: [NSLayoutConstraint])     func addMotionEffect(_ effect: UIMotionEffect)     func removeMotionEffect(_ effect: UIMotionEffect)     var motionEffects: [UIMotionEffect]     var gestureRecognizers: [UIGestureRecognizer]?     func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool     class func animateKeyframes(withDuration duration: TimeInterval, delay delay: TimeInterval, options options: UIViewKeyframeAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func addKeyframe(withRelativeStartTime frameStartTime: Double, relativeDuration frameDuration: Double, animations animations: @escaping () -> Void)     class func animate(withDuration duration: TimeInterval, delay delay: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Void)     class func animate(withDuration duration: TimeInterval, delay delay: TimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options options: UIViewAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func transition(with view: UIView, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     class func transition(from fromView: UIView, to toView: UIView, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], completion completion: (@escaping (Bool) -> Void)? = nil)     class func perform(_ animation: UISystemAnimation, on views: [UIView], options options: UIViewAnimationOptions = [], animations parallelAnimations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     class func beginAnimations(_ animationID: String?, context context: UnsafeMutableRawPointer?)     class func commitAnimations()     class func setAnimationDelegate(_ delegate: Any?)     class func setAnimationWillStart(_ selector: Selector?)     class func setAnimationDidStop(_ selector: Selector?)     class func setAnimationDuration(_ duration: TimeInterval)     class func setAnimationDelay(_ delay: TimeInterval)     class func setAnimationStart(_ startDate: Date)     class func setAnimationCurve(_ curve: UIViewAnimationCurve)     class func setAnimationRepeatCount(_ repeatCount: Float)     class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)     class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)     class func setAnimationTransition(_ transition: UIViewAnimationTransition, for view: UIView, cache cache: Bool)     class func setAnimationsEnabled(_ enabled: Bool)     class var areAnimationsEnabled: Bool { get }     class func performWithoutAnimation(_ actionsWithoutAnimation: () -> Void)     class var inheritedAnimationDuration: TimeInterval { get }     func draw(_ rect: CGRect)     func setNeedsDisplay()     func setNeedsDisplay(_ rect: CGRect)     var clipsToBounds: Bool     @NSCopying var backgroundColor: UIColor?     var alpha: CGFloat     var isOpaque: Bool     var clearsContextBeforeDrawing: Bool     var isHidden: Bool     var contentMode: UIViewContentMode     var contentStretch: CGRect     var mask: UIView?     var tintColor: UIColor!     var tintAdjustmentMode: UIViewTintAdjustmentMode     func tintColorDidChange()     var superview: UIView? { get }     var subviews: [UIView] { get }     var window: UIWindow? { get }     func removeFromSuperview()     func insertSubview(_ view: UIView, at index: Int)     func exchangeSubview(at index1: Int, withSubviewAt index2: Int)     func addSubview(_ view: UIView)     func insertSubview(_ view: UIView, belowSubview siblingSubview: UIView)     func insertSubview(_ view: UIView, aboveSubview siblingSubview: UIView)     func bringSubview(toFront view: UIView)     func sendSubview(toBack view: UIView)     func didAddSubview(_ subview: UIView)     func willRemoveSubview(_ subview: UIView)     func willMove(toSuperview newSuperview: UIView?)     func didMoveToSuperview()     func willMove(toWindow newWindow: UIWindow?)     func didMoveToWindow()     func isDescendant(of view: UIView) -> Bool     func viewWithTag(_ tag: Int) -> UIView?     func setNeedsLayout()     func layoutIfNeeded()     func layoutSubviews()     var layoutMargins: UIEdgeInsets     var preservesSuperviewLayoutMargins: Bool     func layoutMarginsDidChange()     var layoutMarginsGuide: UILayoutGuide { get }     var readableContentGuide: UILayoutGuide { get }     var frame: CGRect     var bounds: CGRect     var center: CGPoint     var transform: CGAffineTransform     var contentScaleFactor: CGFloat     var isMultipleTouchEnabled: Bool     var isExclusiveTouch: Bool     func hitTest(_ point: CGPoint, with event: UIEvent?) -> UIView?     func point(inside point: CGPoint, with event: UIEvent?) -> Bool     func convert(_ point: CGPoint, to view: UIView?) -> CGPoint     func convert(_ point: CGPoint, from view: UIView?) -> CGPoint     func convert(_ rect: CGRect, to view: UIView?) -> CGRect     func convert(_ rect: CGRect, from view: UIView?) -> CGRect     var autoresizesSubviews: Bool     var autoresizingMask: UIViewAutoresizing     func sizeThatFits(_ size: CGSize) -> CGSize     func sizeToFit()     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension PHLivePhotoView : UIAccessibilityIdentification { } extension PHLivePhotoView : CVarArg { } extension PHLivePhotoView : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, UIAccessibilityIdentification |

Modified [PHLivePhotoView.isMuted](https://developer.apple.com/documentation/photokit/phlivephotoview/1623430-muted)

|  | Declaration |
| --- | --- |
| From | ``` var muted: Bool ``` |
| To | ``` var isMuted: Bool ``` |

Modified [PHLivePhotoView.livePhotoBadgeImage(options: PHLivePhotoBadgeOptions) -> UIImage [class]](https://developer.apple.com/documentation/photokit/phlivephotoview/1623417-livephotobadgeimage)

|  | Declaration |
| --- | --- |
| From | ``` class func livePhotoBadgeImageWithOptions(_ badgeOptions: PHLivePhotoBadgeOptions) -> UIImage ``` |
| To | ``` class func livePhotoBadgeImage(options badgeOptions: PHLivePhotoBadgeOptions = []) -> UIImage ``` |

Modified [PHLivePhotoView.startPlayback(with: PHLivePhotoViewPlaybackStyle)](https://developer.apple.com/documentation/photokit/phlivephotoview/1623419-startplaybackwithstyle)

|  | Declaration |
| --- | --- |
| From | ``` func startPlaybackWithStyle(_ playbackStyle: PHLivePhotoViewPlaybackStyle) ``` |
| To | ``` func startPlayback(with playbackStyle: PHLivePhotoViewPlaybackStyle) ``` |

Modified [PHLivePhotoViewDelegate](https://developer.apple.com/documentation/photokit/phlivephotoviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol PHLivePhotoViewDelegate : NSObjectProtocol {     optional func livePhotoView(_ livePhotoView: PHLivePhotoView, willBeginPlaybackWithStyle playbackStyle: PHLivePhotoViewPlaybackStyle)     optional func livePhotoView(_ livePhotoView: PHLivePhotoView, didEndPlaybackWithStyle playbackStyle: PHLivePhotoViewPlaybackStyle) } ``` |
| To | ``` protocol PHLivePhotoViewDelegate : NSObjectProtocol {     optional func livePhotoView(_ livePhotoView: PHLivePhotoView, willBeginPlaybackWith playbackStyle: PHLivePhotoViewPlaybackStyle)     optional func livePhotoView(_ livePhotoView: PHLivePhotoView, didEndPlaybackWith playbackStyle: PHLivePhotoViewPlaybackStyle) } ``` |

Modified [PHLivePhotoViewDelegate.livePhotoView(_: PHLivePhotoView, didEndPlaybackWith: PHLivePhotoViewPlaybackStyle)](https://developer.apple.com/documentation/photokit/phlivephotoviewdelegate/1623431-livephotoview)

|  | Declaration |
| --- | --- |
| From | ``` optional func livePhotoView(_ livePhotoView: PHLivePhotoView, didEndPlaybackWithStyle playbackStyle: PHLivePhotoViewPlaybackStyle) ``` |
| To | ``` optional func livePhotoView(_ livePhotoView: PHLivePhotoView, didEndPlaybackWith playbackStyle: PHLivePhotoViewPlaybackStyle) ``` |

Modified [PHLivePhotoViewDelegate.livePhotoView(_: PHLivePhotoView, willBeginPlaybackWith: PHLivePhotoViewPlaybackStyle)](https://developer.apple.com/documentation/photokit/phlivephotoviewdelegate/1623421-livephotoview)

|  | Declaration |
| --- | --- |
| From | ``` optional func livePhotoView(_ livePhotoView: PHLivePhotoView, willBeginPlaybackWithStyle playbackStyle: PHLivePhotoViewPlaybackStyle) ``` |
| To | ``` optional func livePhotoView(_ livePhotoView: PHLivePhotoView, willBeginPlaybackWith playbackStyle: PHLivePhotoViewPlaybackStyle) ``` |

Modified [PHLivePhotoViewPlaybackStyle [enum]](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum PHLivePhotoViewPlaybackStyle : Int {     case Undefined     case Full     case Hint } ``` |
| To | ``` enum PHLivePhotoViewPlaybackStyle : Int {     case undefined     case full     case hint } ``` |

Modified [PHLivePhotoViewPlaybackStyle.full](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle/full)

|  | Declaration |
| --- | --- |
| From | ``` case Full ``` |
| To | ``` case full ``` |

Modified [PHLivePhotoViewPlaybackStyle.hint](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle/phlivephotoviewplaybackstylehint)

|  | Declaration |
| --- | --- |
| From | ``` case Hint ``` |
| To | ``` case hint ``` |

Modified [PHLivePhotoViewPlaybackStyle.undefined](https://developer.apple.com/documentation/photokit/phlivephotoviewplaybackstyle/phlivephotoviewplaybackstyleundefined)

|  | Declaration |
| --- | --- |
| From | ``` case Undefined ``` |
| To | ``` case undefined ``` |

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
