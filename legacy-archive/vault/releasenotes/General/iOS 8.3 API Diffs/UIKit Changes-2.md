---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/UIKit.html
archived_at: '2026-07-18T02:56:28.400049Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# UIKit Changes

## UIKit

Removed UIStatusBarStyle.BlackOpaqueAdded NSStringDrawingOptions.init(_: Int)Added NSStringDrawingOptions.init(rawValue: Int)Added UIAdaptivePresentationControllerDelegate.adaptivePresentationStyleForPresentationController(UIPresentationController!, traitCollection: UITraitCollection!) -> UIModalPresentationStyleAdded UIAdaptivePresentationControllerDelegate.presentationController(UIPresentationController!, willPresentWithAdaptiveStyle: UIModalPresentationStyle, transitionCoordinator: UIViewControllerTransitionCoordinator!)Added UIColor.init(CGColor: CGColor)Added UIEdgeInsets.init()Added UIEdgeInsets.init(top: CGFloat, left: CGFloat, bottom: CGFloat, right: CGFloat)Added UIOffset.init()Added UIOffset.init(horizontal: CGFloat, vertical: CGFloat)Added UIPresentationController.adaptivePresentationStyleForTraitCollection(UITraitCollection!) -> UIModalPresentationStyleAdded UIPrintInfo.printInfo() -> UIPrintInfo! [class]Added UITableViewController.init(coder: NSCoder!)Added UITableViewController.init(nibName: String!, bundle: NSBundle!)Added UIView.boundsAdded UIView.centerAdded UIView.transformAdded UI_USER_INTERFACE_IDIOM() -> UIUserInterfaceIdiomModified NSAttributedString.init(attachment: NSTextAttachment)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(attachment attachment: NSTextAttachment!) -> NSAttributedString ``` | iOS 8.1 |
| To | ``` init(attachment attachment: NSTextAttachment) -> NSAttributedString ``` | iOS 7.0 |

Modified NSAttributedString.dataFromRange(NSRange, documentAttributes:[NSObject: AnyObject], error: NSErrorPointer) -> NSData?

|  | Declaration |
| --- | --- |
| From | ``` func dataFromRange(_ range: NSRange, documentAttributes dict: [NSObject : AnyObject]!, error error: NSErrorPointer) -> NSData? ``` |
| To | ``` func dataFromRange(_ range: NSRange, documentAttributes dict: [NSObject : AnyObject], error error: NSErrorPointer) -> NSData? ``` |

Modified NSAttributedString.fileWrapperFromRange(NSRange, documentAttributes:[NSObject: AnyObject], error: NSErrorPointer) -> NSFileWrapper?

|  | Declaration |
| --- | --- |
| From | ``` func fileWrapperFromRange(_ range: NSRange, documentAttributes dict: [NSObject : AnyObject]!, error error: NSErrorPointer) -> NSFileWrapper? ``` |
| To | ``` func fileWrapperFromRange(_ range: NSRange, documentAttributes dict: [NSObject : AnyObject], error error: NSErrorPointer) -> NSFileWrapper? ``` |

Modified NSIndexPath.init(forItem: Int, inSection: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 6.0 |

Modified NSStringDrawingOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum NSStringDrawingOptions : Int {     case TruncatesLastVisibleLine     case UsesLineFragmentOrigin     case UsesFontLeading     case UsesDeviceMetrics } ``` | Equatable, Hashable, RawRepresentable |
| To | ``` struct NSStringDrawingOptions : RawOptionSetType {     init(_ rawValue: Int)     init(rawValue rawValue: Int)     static var TruncatesLastVisibleLine: NSStringDrawingOptions { get }     static var UsesLineFragmentOrigin: NSStringDrawingOptions { get }     static var UsesFontLeading: NSStringDrawingOptions { get }     static var UsesDeviceMetrics: NSStringDrawingOptions { get } } ``` | RawOptionSetType |

Modified NSStringDrawingOptions.TruncatesLastVisibleLine

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TruncatesLastVisibleLine ``` | iOS 8.0 |
| To | ``` static var TruncatesLastVisibleLine: NSStringDrawingOptions { get } ``` | iOS 8.3 |

Modified NSStringDrawingOptions.UsesDeviceMetrics

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UsesDeviceMetrics ``` | iOS 8.0 |
| To | ``` static var UsesDeviceMetrics: NSStringDrawingOptions { get } ``` | iOS 8.3 |

Modified NSStringDrawingOptions.UsesFontLeading

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UsesFontLeading ``` | iOS 8.0 |
| To | ``` static var UsesFontLeading: NSStringDrawingOptions { get } ``` | iOS 8.3 |

Modified NSStringDrawingOptions.UsesLineFragmentOrigin

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UsesLineFragmentOrigin ``` | iOS 8.0 |
| To | ``` static var UsesLineFragmentOrigin: NSStringDrawingOptions { get } ``` | iOS 8.3 |

Modified NSUnderlineStyle.ByWord

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUnderlineStyle.PatternDash

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUnderlineStyle.PatternDashDot

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUnderlineStyle.PatternDashDotDot

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUnderlineStyle.PatternDot

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUnderlineStyle.StyleDouble

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUnderlineStyle.StyleThick

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSValue.init(UIOffset: UIOffset)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 5.0 |

Modified UIAppearance.appearance() -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func appearance() -> Self! ``` | iOS 8.0 |
| To | ``` static func appearance() -> Self ``` | iOS 8.3 |

Modified UIAppearance.appearanceForTraitCollection(UITraitCollection) -> Self [class]

|  | Declaration |
| --- | --- |
| From | ``` class func appearanceForTraitCollection(_ trait: UITraitCollection) -> Self! ``` |
| To | ``` static func appearanceForTraitCollection(_ trait: UITraitCollection) -> Self ``` |

Modified UIApplicationDelegate.application(UIApplication, handleWatchKitExtensionRequest:[NSObject: AnyObject]?, reply:(([NSObject: AnyObject]!) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` optional func application(_ application: UIApplication!, handleWatchKitExtensionRequest userInfo: [NSObject : AnyObject]!, reply reply: (([NSObject : AnyObject]!) -> Void)!) ``` |
| To | ``` optional func application(_ application: UIApplication, handleWatchKitExtensionRequest userInfo: [NSObject : AnyObject]?, reply reply: (([NSObject : AnyObject]!) -> Void)!) ``` |

Modified UIBarButtonItem.possibleTitles

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var possibleTitles: NSSet? ``` |
| To | ``` var possibleTitles: Set<NSObject>? ``` |

Modified UIBarButtonItemStyle.Bordered

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified UIButtonType.System

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewController.init(collectionViewLayout: UICollectionViewLayout)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(collectionViewLayout layout: UICollectionViewLayout!) ``` | iOS 8.0 |
| To | ``` init(collectionViewLayout layout: UICollectionViewLayout) ``` | iOS 8.3 |

Modified UICollectionViewUpdateItem.indexPathAfterUpdate

|  | Declaration |
| --- | --- |
| From | ``` var indexPathAfterUpdate: NSIndexPath! { get } ``` |
| To | ``` var indexPathAfterUpdate: NSIndexPath? { get } ``` |

Modified UICollectionViewUpdateItem.indexPathBeforeUpdate

|  | Declaration |
| --- | --- |
| From | ``` var indexPathBeforeUpdate: NSIndexPath! { get } ``` |
| To | ``` var indexPathBeforeUpdate: NSIndexPath? { get } ``` |

Modified UIColor.init(CGColor: CGColor!)

|  | Declaration |
| --- | --- |
| From | ``` init(CGColor cgColor: CGColor!) ``` |
| To | ``` init!(CGColor cgColor: CGColor!) -> UIColor ``` |

Modified UIControl.allTargets() -> Set<NSObject>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func allTargets() -> NSSet ``` | iOS 8.0 |
| To | ``` func allTargets() -> Set<NSObject> ``` | iOS 8.3 |

Modified UIEdgeInsets [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIEdgeInsets {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat } ``` |
| To | ``` struct UIEdgeInsets {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat     init()     init(top top: CGFloat, left left: CGFloat, bottom bottom: CGFloat, right right: CGFloat) } ``` |

Modified UIEvent.allTouches() -> Set<NSObject>?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func allTouches() -> NSSet? ``` | iOS 8.0 |
| To | ``` func allTouches() -> Set<NSObject>? ``` | iOS 8.3 |

Modified UIEvent.touchesForGestureRecognizer(UIGestureRecognizer) -> Set<NSObject>?

|  | Declaration |
| --- | --- |
| From | ``` func touchesForGestureRecognizer(_ gesture: UIGestureRecognizer) -> NSSet? ``` |
| To | ``` func touchesForGestureRecognizer(_ gesture: UIGestureRecognizer) -> Set<NSObject>? ``` |

Modified UIEvent.touchesForView(UIView) -> Set<NSObject>?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func touchesForView(_ view: UIView) -> NSSet? ``` | iOS 8.0 |
| To | ``` func touchesForView(_ view: UIView) -> Set<NSObject>? ``` | iOS 8.3 |

Modified UIEvent.touchesForWindow(UIWindow) -> Set<NSObject>?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func touchesForWindow(_ window: UIWindow) -> NSSet? ``` | iOS 8.0 |
| To | ``` func touchesForWindow(_ window: UIWindow) -> Set<NSObject>? ``` | iOS 8.3 |

Modified UIFont.init(descriptor: UIFontDescriptor, size: CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptor.fontDescriptorWithSymbolicTraits(UIFontDescriptorSymbolicTraits) -> UIFontDescriptor?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor ``` | iOS 8.0 |
| To | ``` func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor? ``` | iOS 8.3 |

Modified UIFontDescriptor.matchingFontDescriptorsWithMandatoryKeys(Set<NSObject>?) -> [AnyObject]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: NSSet?) -> [AnyObject] ``` | iOS 8.0 |
| To | ``` func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<NSObject>?) -> [AnyObject] ``` | iOS 8.3 |

Modified UIKeyboardAppearance.Dark

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIKeyboardAppearance.Light

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIKeyboardType.DecimalPad

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified UIKeyboardType.Twitter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIKeyboardType.WebSearch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIModalPresentationStyle.CurrentContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIModalPresentationStyle.Custom

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIModalPresentationStyle.FormSheet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIModalPresentationStyle.None

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIModalPresentationStyle.PageSheet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIModalTransitionStyle.PartialCurl

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UINavigationController.init(navigationBarClass: AnyClass?, toolbarClass: AnyClass?)

|  | Declaration |
| --- | --- |
| From | ``` init(navigationBarClass navigationBarClass: AnyClass!, toolbarClass toolbarClass: AnyClass!) ``` |
| To | ``` init(navigationBarClass navigationBarClass: AnyClass?, toolbarClass toolbarClass: AnyClass?) ``` |

Modified UIObjectRestoration.objectWithRestorationIdentifierPath([AnyObject], coder: NSCoder) -> UIStateRestoring? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func objectWithRestorationIdentifierPath(_ identifierComponents: [AnyObject], coder coder: NSCoder) -> UIStateRestoring? ``` |
| To | ``` static func objectWithRestorationIdentifierPath(_ identifierComponents: [AnyObject], coder coder: NSCoder) -> UIStateRestoring? ``` |

Modified UIOffset [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIOffset {     var horizontal: CGFloat     var vertical: CGFloat } ``` |
| To | ``` struct UIOffset {     var horizontal: CGFloat     var vertical: CGFloat     init()     init(horizontal horizontal: CGFloat, vertical vertical: CGFloat) } ``` |

Modified UIPopoverBackgroundViewMethods.arrowBase() -> CGFloat [class]

|  | Declaration |
| --- | --- |
| From | ``` class func arrowBase() -> CGFloat ``` |
| To | ``` static func arrowBase() -> CGFloat ``` |

Modified UIPopoverBackgroundViewMethods.arrowHeight() -> CGFloat [class]

|  | Declaration |
| --- | --- |
| From | ``` class func arrowHeight() -> CGFloat ``` |
| To | ``` static func arrowHeight() -> CGFloat ``` |

Modified UIPopoverBackgroundViewMethods.contentViewInsets() -> UIEdgeInsets [class]

|  | Declaration |
| --- | --- |
| From | ``` class func contentViewInsets() -> UIEdgeInsets ``` |
| To | ``` static func contentViewInsets() -> UIEdgeInsets ``` |

Modified UIPrintInteractionController.printableUTIs() -> Set<NSObject> [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func printableUTIs() -> NSSet ``` | iOS 8.0 |
| To | ``` class func printableUTIs() -> Set<NSObject> ``` | iOS 8.3 |

Modified UIPrinter.init(URL: NSURL)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(URL url: NSURL!) -> UIPrinter ``` | iOS 8.0 |
| To | ``` init(URL url: NSURL) -> UIPrinter ``` | iOS 8.3 |

Modified UIResponder.touchesBegan(Set<NSObject>, withEvent: UIEvent)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func touchesBegan(_ touches: NSSet, withEvent event: UIEvent) ``` | iOS 8.0 |
| To | ``` func touchesBegan(_ touches: Set<NSObject>, withEvent event: UIEvent) ``` | iOS 8.3 |

Modified UIResponder.touchesCancelled(Set<NSObject>!, withEvent: UIEvent!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func touchesCancelled(_ touches: NSSet!, withEvent event: UIEvent!) ``` | iOS 8.0 |
| To | ``` func touchesCancelled(_ touches: Set<NSObject>!, withEvent event: UIEvent!) ``` | iOS 8.3 |

Modified UIResponder.touchesEnded(Set<NSObject>, withEvent: UIEvent)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func touchesEnded(_ touches: NSSet, withEvent event: UIEvent) ``` | iOS 8.0 |
| To | ``` func touchesEnded(_ touches: Set<NSObject>, withEvent event: UIEvent) ``` | iOS 8.3 |

Modified UIResponder.touchesMoved(Set<NSObject>, withEvent: UIEvent)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func touchesMoved(_ touches: NSSet, withEvent event: UIEvent) ``` | iOS 8.0 |
| To | ``` func touchesMoved(_ touches: Set<NSObject>, withEvent event: UIEvent) ``` | iOS 8.3 |

Modified UIScrollView.touchesShouldBegin(Set<NSObject>!, withEvent: UIEvent!, inContentView: UIView!) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func touchesShouldBegin(_ touches: NSSet!, withEvent event: UIEvent!, inContentView view: UIView!) -> Bool ``` | iOS 8.0 |
| To | ``` func touchesShouldBegin(_ touches: Set<NSObject>!, withEvent event: UIEvent!, inContentView view: UIView!) -> Bool ``` | iOS 8.3 |

Modified UISegmentedControl.init(items: [AnyObject])

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(items items: [AnyObject]!) ``` | iOS 8.0 |
| To | ``` init(items items: [AnyObject]) ``` | iOS 8.3 |

Modified UIStatusBarStyle.LightContent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIStoryboardSegue.init(identifier: String?, source: UIViewController, destination: UIViewController)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init!(identifier identifier: String!, source source: UIViewController, destination destination: UIViewController) ``` | iOS 8.0 |
| To | ``` init!(identifier identifier: String?, source source: UIViewController, destination destination: UIViewController) ``` | iOS 8.3 |

Modified UIStoryboardSegue.init(identifier: String?, source: UIViewController, destination: UIViewController, performHandler:() -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewCellAccessoryType.DetailButton

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableViewCellSelectionStyle.Default

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIUserNotificationSettings.categories

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var categories: NSSet! { get } ``` |
| To | ``` var categories: Set<NSObject>! { get } ``` |

Modified UIUserNotificationSettings.init(forTypes: UIUserNotificationType, categories: Set<NSObject>?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` convenience init(forTypes types: UIUserNotificationType, categories categories: NSSet?) ``` | iOS 8.0 |
| To | ``` convenience init(forTypes types: UIUserNotificationType, categories categories: Set<NSObject>?) ``` | iOS 8.3 |

Modified UIViewControllerRestoration.viewControllerWithRestorationIdentifierPath([AnyObject], coder: NSCoder) -> UIViewController? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func viewControllerWithRestorationIdentifierPath(_ identifierComponents: [AnyObject], coder coder: NSCoder) -> UIViewController? ``` |
| To | ``` static func viewControllerWithRestorationIdentifierPath(_ identifierComponents: [AnyObject], coder coder: NSCoder) -> UIViewController? ``` |

Modified NSAttachmentAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSAttachmentAttributeName: NSString! ``` |
| To | ``` let NSAttachmentAttributeName: String ``` |

Modified NSBackgroundColorAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSBackgroundColorAttributeName: NSString! ``` |
| To | ``` let NSBackgroundColorAttributeName: String ``` |

Modified NSBackgroundColorDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSBackgroundColorDocumentAttribute: NSString! ``` |
| To | ``` let NSBackgroundColorDocumentAttribute: String ``` |

Modified NSBaselineOffsetAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSBaselineOffsetAttributeName: NSString! ``` |
| To | ``` let NSBaselineOffsetAttributeName: String ``` |

Modified NSCharacterEncodingDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSCharacterEncodingDocumentAttribute: NSString! ``` |
| To | ``` let NSCharacterEncodingDocumentAttribute: String ``` |

Modified NSDefaultAttributesDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSDefaultAttributesDocumentAttribute: NSString! ``` |
| To | ``` let NSDefaultAttributesDocumentAttribute: String ``` |

Modified NSDefaultTabIntervalDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSDefaultTabIntervalDocumentAttribute: NSString! ``` |
| To | ``` let NSDefaultTabIntervalDocumentAttribute: String ``` |

Modified NSDocumentTypeDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSDocumentTypeDocumentAttribute: NSString! ``` |
| To | ``` let NSDocumentTypeDocumentAttribute: String ``` |

Modified NSExpansionAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSExpansionAttributeName: NSString! ``` |
| To | ``` let NSExpansionAttributeName: String ``` |

Modified NSFontAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSFontAttributeName: NSString! ``` |
| To | ``` let NSFontAttributeName: String ``` |

Modified NSForegroundColorAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSForegroundColorAttributeName: NSString! ``` |
| To | ``` let NSForegroundColorAttributeName: String ``` |

Modified NSHTMLTextDocumentType

|  | Declaration |
| --- | --- |
| From | ``` let NSHTMLTextDocumentType: NSString! ``` |
| To | ``` let NSHTMLTextDocumentType: String ``` |

Modified NSHyphenationFactorDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSHyphenationFactorDocumentAttribute: NSString! ``` |
| To | ``` let NSHyphenationFactorDocumentAttribute: String ``` |

Modified NSKernAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSKernAttributeName: NSString! ``` |
| To | ``` let NSKernAttributeName: String ``` |

Modified NSLigatureAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSLigatureAttributeName: NSString! ``` |
| To | ``` let NSLigatureAttributeName: String ``` |

Modified NSLinkAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSLinkAttributeName: NSString! ``` |
| To | ``` let NSLinkAttributeName: String ``` |

Modified NSObliquenessAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSObliquenessAttributeName: NSString! ``` |
| To | ``` let NSObliquenessAttributeName: String ``` |

Modified NSPaperMarginDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSPaperMarginDocumentAttribute: NSString! ``` |
| To | ``` let NSPaperMarginDocumentAttribute: String ``` |

Modified NSPaperSizeDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSPaperSizeDocumentAttribute: NSString! ``` |
| To | ``` let NSPaperSizeDocumentAttribute: String ``` |

Modified NSParagraphStyleAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSParagraphStyleAttributeName: NSString! ``` |
| To | ``` let NSParagraphStyleAttributeName: String ``` |

Modified NSPlainTextDocumentType

|  | Declaration |
| --- | --- |
| From | ``` let NSPlainTextDocumentType: NSString! ``` |
| To | ``` let NSPlainTextDocumentType: String ``` |

Modified NSRTFDTextDocumentType

|  | Declaration |
| --- | --- |
| From | ``` let NSRTFDTextDocumentType: NSString! ``` |
| To | ``` let NSRTFDTextDocumentType: String ``` |

Modified NSRTFTextDocumentType

|  | Declaration |
| --- | --- |
| From | ``` let NSRTFTextDocumentType: NSString! ``` |
| To | ``` let NSRTFTextDocumentType: String ``` |

Modified NSReadOnlyDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSReadOnlyDocumentAttribute: NSString! ``` |
| To | ``` let NSReadOnlyDocumentAttribute: String ``` |

Modified NSShadowAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSShadowAttributeName: NSString! ``` |
| To | ``` let NSShadowAttributeName: String ``` |

Modified NSStrikethroughColorAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSStrikethroughColorAttributeName: NSString! ``` |
| To | ``` let NSStrikethroughColorAttributeName: String ``` |

Modified NSStrikethroughStyleAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSStrikethroughStyleAttributeName: NSString! ``` |
| To | ``` let NSStrikethroughStyleAttributeName: String ``` |

Modified NSStrokeColorAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSStrokeColorAttributeName: NSString! ``` |
| To | ``` let NSStrokeColorAttributeName: String ``` |

Modified NSStrokeWidthAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSStrokeWidthAttributeName: NSString! ``` |
| To | ``` let NSStrokeWidthAttributeName: String ``` |

Modified NSTabColumnTerminatorsAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSTabColumnTerminatorsAttributeName: NSString! ``` |
| To | ``` let NSTabColumnTerminatorsAttributeName: String ``` |

Modified NSTextEffectAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSTextEffectAttributeName: NSString! ``` |
| To | ``` let NSTextEffectAttributeName: String ``` |

Modified NSTextEffectLetterpressStyle

|  | Declaration |
| --- | --- |
| From | ``` let NSTextEffectLetterpressStyle: NSString! ``` |
| To | ``` let NSTextEffectLetterpressStyle: String ``` |

Modified NSTextLayoutSectionOrientation

|  | Declaration |
| --- | --- |
| From | ``` let NSTextLayoutSectionOrientation: NSString! ``` |
| To | ``` let NSTextLayoutSectionOrientation: String ``` |

Modified NSTextLayoutSectionRange

|  | Declaration |
| --- | --- |
| From | ``` let NSTextLayoutSectionRange: NSString! ``` |
| To | ``` let NSTextLayoutSectionRange: String ``` |

Modified NSTextLayoutSectionsAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSTextLayoutSectionsAttribute: NSString! ``` |
| To | ``` let NSTextLayoutSectionsAttribute: String ``` |

Modified NSTextStorageDidProcessEditingNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSTextStorageDidProcessEditingNotification: NSString! ``` |
| To | ``` let NSTextStorageDidProcessEditingNotification: String ``` |

Modified NSTextStorageWillProcessEditingNotification

|  | Declaration |
| --- | --- |
| From | ``` let NSTextStorageWillProcessEditingNotification: NSString! ``` |
| To | ``` let NSTextStorageWillProcessEditingNotification: String ``` |

Modified NSUnderlineColorAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSUnderlineColorAttributeName: NSString! ``` |
| To | ``` let NSUnderlineColorAttributeName: String ``` |

Modified NSUnderlineStyleAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSUnderlineStyleAttributeName: NSString! ``` |
| To | ``` let NSUnderlineStyleAttributeName: String ``` |

Modified NSUserActivityDocumentURLKey

|  | Declaration |
| --- | --- |
| From | ``` let NSUserActivityDocumentURLKey: NSString! ``` |
| To | ``` let NSUserActivityDocumentURLKey: String ``` |

Modified NSVerticalGlyphFormAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSVerticalGlyphFormAttributeName: NSString! ``` |
| To | ``` let NSVerticalGlyphFormAttributeName: String ``` |

Modified NSViewModeDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSViewModeDocumentAttribute: NSString! ``` |
| To | ``` let NSViewModeDocumentAttribute: String ``` |

Modified NSViewSizeDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSViewSizeDocumentAttribute: NSString! ``` |
| To | ``` let NSViewSizeDocumentAttribute: String ``` |

Modified NSViewZoomDocumentAttribute

|  | Declaration |
| --- | --- |
| From | ``` let NSViewZoomDocumentAttribute: NSString! ``` |
| To | ``` let NSViewZoomDocumentAttribute: String ``` |

Modified NSWritingDirectionAttributeName

|  | Declaration |
| --- | --- |
| From | ``` let NSWritingDirectionAttributeName: NSString! ``` |
| To | ``` let NSWritingDirectionAttributeName: String ``` |

Modified UIAccessibilityAnnouncementDidFinishNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityAnnouncementDidFinishNotification: NSString! ``` |
| To | ``` let UIAccessibilityAnnouncementDidFinishNotification: String ``` |

Modified UIAccessibilityAnnouncementKeyStringValue

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityAnnouncementKeyStringValue: NSString! ``` |
| To | ``` let UIAccessibilityAnnouncementKeyStringValue: String ``` |

Modified UIAccessibilityAnnouncementKeyWasSuccessful

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityAnnouncementKeyWasSuccessful: NSString! ``` |
| To | ``` let UIAccessibilityAnnouncementKeyWasSuccessful: String ``` |

Modified UIAccessibilityBoldTextStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityBoldTextStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilityBoldTextStatusDidChangeNotification: String ``` |

Modified UIAccessibilityClosedCaptioningStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityClosedCaptioningStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilityClosedCaptioningStatusDidChangeNotification: String ``` |

Modified UIAccessibilityDarkerSystemColorsStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityDarkerSystemColorsStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilityDarkerSystemColorsStatusDidChangeNotification: String ``` |

Modified UIAccessibilityGrayscaleStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityGrayscaleStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilityGrayscaleStatusDidChangeNotification: String ``` |

Modified UIAccessibilityGuidedAccessStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityGuidedAccessStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilityGuidedAccessStatusDidChangeNotification: String ``` |

Modified UIAccessibilityInvertColorsStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityInvertColorsStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilityInvertColorsStatusDidChangeNotification: String ``` |

Modified UIAccessibilityMonoAudioStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityMonoAudioStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilityMonoAudioStatusDidChangeNotification: String ``` |

Modified UIAccessibilityNotificationSwitchControlIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityNotificationSwitchControlIdentifier: NSString! ``` |
| To | ``` let UIAccessibilityNotificationSwitchControlIdentifier: String ``` |

Modified UIAccessibilityReduceMotionStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityReduceMotionStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilityReduceMotionStatusDidChangeNotification: String ``` |

Modified UIAccessibilityReduceTransparencyStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityReduceTransparencyStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilityReduceTransparencyStatusDidChangeNotification: String ``` |

Modified UIAccessibilitySpeakScreenStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilitySpeakScreenStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilitySpeakScreenStatusDidChangeNotification: String ``` |

Modified UIAccessibilitySpeakSelectionStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilitySpeakSelectionStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilitySpeakSelectionStatusDidChangeNotification: String ``` |

Modified UIAccessibilitySpeechAttributeLanguage

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilitySpeechAttributeLanguage: NSString! ``` |
| To | ``` let UIAccessibilitySpeechAttributeLanguage: String ``` |

Modified UIAccessibilitySpeechAttributePitch

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilitySpeechAttributePitch: NSString! ``` |
| To | ``` let UIAccessibilitySpeechAttributePitch: String ``` |

Modified UIAccessibilitySpeechAttributePunctuation

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilitySpeechAttributePunctuation: NSString! ``` |
| To | ``` let UIAccessibilitySpeechAttributePunctuation: String ``` |

Modified UIAccessibilitySwitchControlStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilitySwitchControlStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIAccessibilitySwitchControlStatusDidChangeNotification: String ``` |

Modified UIAccessibilityVoiceOverStatusChanged

|  | Declaration |
| --- | --- |
| From | ``` let UIAccessibilityVoiceOverStatusChanged: NSString! ``` |
| To | ``` let UIAccessibilityVoiceOverStatusChanged: String ``` |

Modified UIActivityTypeAddToReadingList

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypeAddToReadingList: NSString! ``` |
| To | ``` let UIActivityTypeAddToReadingList: String ``` |

Modified UIActivityTypeAirDrop

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypeAirDrop: NSString! ``` |
| To | ``` let UIActivityTypeAirDrop: String ``` |

Modified UIActivityTypeAssignToContact

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypeAssignToContact: NSString! ``` |
| To | ``` let UIActivityTypeAssignToContact: String ``` |

Modified UIActivityTypeCopyToPasteboard

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypeCopyToPasteboard: NSString! ``` |
| To | ``` let UIActivityTypeCopyToPasteboard: String ``` |

Modified UIActivityTypeMail

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypeMail: NSString! ``` |
| To | ``` let UIActivityTypeMail: String ``` |

Modified UIActivityTypeMessage

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypeMessage: NSString! ``` |
| To | ``` let UIActivityTypeMessage: String ``` |

Modified UIActivityTypePostToFacebook

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypePostToFacebook: NSString! ``` |
| To | ``` let UIActivityTypePostToFacebook: String ``` |

Modified UIActivityTypePostToFlickr

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypePostToFlickr: NSString! ``` |
| To | ``` let UIActivityTypePostToFlickr: String ``` |

Modified UIActivityTypePostToTencentWeibo

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypePostToTencentWeibo: NSString! ``` |
| To | ``` let UIActivityTypePostToTencentWeibo: String ``` |

Modified UIActivityTypePostToTwitter

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypePostToTwitter: NSString! ``` |
| To | ``` let UIActivityTypePostToTwitter: String ``` |

Modified UIActivityTypePostToVimeo

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypePostToVimeo: NSString! ``` |
| To | ``` let UIActivityTypePostToVimeo: String ``` |

Modified UIActivityTypePostToWeibo

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypePostToWeibo: NSString! ``` |
| To | ``` let UIActivityTypePostToWeibo: String ``` |

Modified UIActivityTypePrint

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypePrint: NSString! ``` |
| To | ``` let UIActivityTypePrint: String ``` |

Modified UIActivityTypeSaveToCameraRoll

|  | Declaration |
| --- | --- |
| From | ``` let UIActivityTypeSaveToCameraRoll: NSString! ``` |
| To | ``` let UIActivityTypeSaveToCameraRoll: String ``` |

Modified UIApplicationBackgroundRefreshStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationBackgroundRefreshStatusDidChangeNotification: NSString! ``` |
| To | ``` let UIApplicationBackgroundRefreshStatusDidChangeNotification: String ``` |

Modified UIApplicationDidBecomeActiveNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationDidBecomeActiveNotification: NSString! ``` |
| To | ``` let UIApplicationDidBecomeActiveNotification: String ``` |

Modified UIApplicationDidChangeStatusBarFrameNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationDidChangeStatusBarFrameNotification: NSString! ``` |
| To | ``` let UIApplicationDidChangeStatusBarFrameNotification: String ``` |

Modified UIApplicationDidChangeStatusBarOrientationNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationDidChangeStatusBarOrientationNotification: NSString! ``` |
| To | ``` let UIApplicationDidChangeStatusBarOrientationNotification: String ``` |

Modified UIApplicationDidEnterBackgroundNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationDidEnterBackgroundNotification: NSString! ``` |
| To | ``` let UIApplicationDidEnterBackgroundNotification: String ``` |

Modified UIApplicationDidFinishLaunchingNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationDidFinishLaunchingNotification: NSString! ``` |
| To | ``` let UIApplicationDidFinishLaunchingNotification: String ``` |

Modified UIApplicationDidReceiveMemoryWarningNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationDidReceiveMemoryWarningNotification: NSString! ``` |
| To | ``` let UIApplicationDidReceiveMemoryWarningNotification: String ``` |

Modified UIApplicationInvalidInterfaceOrientationException

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationInvalidInterfaceOrientationException: NSString! ``` |
| To | ``` let UIApplicationInvalidInterfaceOrientationException: String ``` |

Modified UIApplicationKeyboardExtensionPointIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationKeyboardExtensionPointIdentifier: NSString! ``` |
| To | ``` let UIApplicationKeyboardExtensionPointIdentifier: String ``` |

Modified UIApplicationLaunchOptionsAnnotationKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsAnnotationKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsAnnotationKey: String ``` |

Modified UIApplicationLaunchOptionsBluetoothCentralsKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsBluetoothCentralsKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsBluetoothCentralsKey: String ``` |

Modified UIApplicationLaunchOptionsBluetoothPeripheralsKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsBluetoothPeripheralsKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsBluetoothPeripheralsKey: String ``` |

Modified UIApplicationLaunchOptionsLocalNotificationKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsLocalNotificationKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsLocalNotificationKey: String ``` |

Modified UIApplicationLaunchOptionsLocationKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsLocationKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsLocationKey: String ``` |

Modified UIApplicationLaunchOptionsNewsstandDownloadsKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsNewsstandDownloadsKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsNewsstandDownloadsKey: String ``` |

Modified UIApplicationLaunchOptionsRemoteNotificationKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsRemoteNotificationKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsRemoteNotificationKey: String ``` |

Modified UIApplicationLaunchOptionsSourceApplicationKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsSourceApplicationKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsSourceApplicationKey: String ``` |

Modified UIApplicationLaunchOptionsURLKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsURLKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsURLKey: String ``` |

Modified UIApplicationLaunchOptionsUserActivityDictionaryKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsUserActivityDictionaryKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsUserActivityDictionaryKey: String ``` |

Modified UIApplicationLaunchOptionsUserActivityTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationLaunchOptionsUserActivityTypeKey: NSString! ``` |
| To | ``` let UIApplicationLaunchOptionsUserActivityTypeKey: String ``` |

Modified UIApplicationOpenSettingsURLString

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationOpenSettingsURLString: NSString! ``` |
| To | ``` let UIApplicationOpenSettingsURLString: String ``` |

Modified UIApplicationProtectedDataDidBecomeAvailable

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationProtectedDataDidBecomeAvailable: NSString! ``` |
| To | ``` let UIApplicationProtectedDataDidBecomeAvailable: String ``` |

Modified UIApplicationProtectedDataWillBecomeUnavailable

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationProtectedDataWillBecomeUnavailable: NSString! ``` |
| To | ``` let UIApplicationProtectedDataWillBecomeUnavailable: String ``` |

Modified UIApplicationSignificantTimeChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationSignificantTimeChangeNotification: NSString! ``` |
| To | ``` let UIApplicationSignificantTimeChangeNotification: String ``` |

Modified UIApplicationStateRestorationBundleVersionKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationStateRestorationBundleVersionKey: NSString! ``` |
| To | ``` let UIApplicationStateRestorationBundleVersionKey: String ``` |

Modified UIApplicationStateRestorationSystemVersionKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationStateRestorationSystemVersionKey: NSString! ``` |
| To | ``` let UIApplicationStateRestorationSystemVersionKey: String ``` |

Modified UIApplicationStateRestorationTimestampKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationStateRestorationTimestampKey: NSString! ``` |
| To | ``` let UIApplicationStateRestorationTimestampKey: String ``` |

Modified UIApplicationStateRestorationUserInterfaceIdiomKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationStateRestorationUserInterfaceIdiomKey: NSString! ``` |
| To | ``` let UIApplicationStateRestorationUserInterfaceIdiomKey: String ``` |

Modified UIApplicationStatusBarFrameUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationStatusBarFrameUserInfoKey: NSString! ``` |
| To | ``` let UIApplicationStatusBarFrameUserInfoKey: String ``` |

Modified UIApplicationStatusBarOrientationUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationStatusBarOrientationUserInfoKey: NSString! ``` |
| To | ``` let UIApplicationStatusBarOrientationUserInfoKey: String ``` |

Modified UIApplicationUserDidTakeScreenshotNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationUserDidTakeScreenshotNotification: NSString! ``` |
| To | ``` let UIApplicationUserDidTakeScreenshotNotification: String ``` |

Modified UIApplicationWillChangeStatusBarFrameNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationWillChangeStatusBarFrameNotification: NSString! ``` |
| To | ``` let UIApplicationWillChangeStatusBarFrameNotification: String ``` |

Modified UIApplicationWillChangeStatusBarOrientationNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationWillChangeStatusBarOrientationNotification: NSString! ``` |
| To | ``` let UIApplicationWillChangeStatusBarOrientationNotification: String ``` |

Modified UIApplicationWillEnterForegroundNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationWillEnterForegroundNotification: NSString! ``` |
| To | ``` let UIApplicationWillEnterForegroundNotification: String ``` |

Modified UIApplicationWillResignActiveNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationWillResignActiveNotification: NSString! ``` |
| To | ``` let UIApplicationWillResignActiveNotification: String ``` |

Modified UIApplicationWillTerminateNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIApplicationWillTerminateNotification: NSString! ``` |
| To | ``` let UIApplicationWillTerminateNotification: String ``` |

Modified UICollectionElementKindSectionFooter

|  | Declaration |
| --- | --- |
| From | ``` let UICollectionElementKindSectionFooter: NSString! ``` |
| To | ``` let UICollectionElementKindSectionFooter: String ``` |

Modified UICollectionElementKindSectionHeader

|  | Declaration |
| --- | --- |
| From | ``` let UICollectionElementKindSectionHeader: NSString! ``` |
| To | ``` let UICollectionElementKindSectionHeader: String ``` |

Modified UIContentSizeCategoryAccessibilityExtraExtraExtraLarge

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryAccessibilityExtraExtraExtraLarge: NSString! ``` |
| To | ``` let UIContentSizeCategoryAccessibilityExtraExtraExtraLarge: String ``` |

Modified UIContentSizeCategoryAccessibilityExtraExtraLarge

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryAccessibilityExtraExtraLarge: NSString! ``` |
| To | ``` let UIContentSizeCategoryAccessibilityExtraExtraLarge: String ``` |

Modified UIContentSizeCategoryAccessibilityExtraLarge

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryAccessibilityExtraLarge: NSString! ``` |
| To | ``` let UIContentSizeCategoryAccessibilityExtraLarge: String ``` |

Modified UIContentSizeCategoryAccessibilityLarge

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryAccessibilityLarge: NSString! ``` |
| To | ``` let UIContentSizeCategoryAccessibilityLarge: String ``` |

Modified UIContentSizeCategoryAccessibilityMedium

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryAccessibilityMedium: NSString! ``` |
| To | ``` let UIContentSizeCategoryAccessibilityMedium: String ``` |

Modified UIContentSizeCategoryDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryDidChangeNotification: NSString! ``` |
| To | ``` let UIContentSizeCategoryDidChangeNotification: String ``` |

Modified UIContentSizeCategoryExtraExtraExtraLarge

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryExtraExtraExtraLarge: NSString! ``` |
| To | ``` let UIContentSizeCategoryExtraExtraExtraLarge: String ``` |

Modified UIContentSizeCategoryExtraExtraLarge

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryExtraExtraLarge: NSString! ``` |
| To | ``` let UIContentSizeCategoryExtraExtraLarge: String ``` |

Modified UIContentSizeCategoryExtraLarge

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryExtraLarge: NSString! ``` |
| To | ``` let UIContentSizeCategoryExtraLarge: String ``` |

Modified UIContentSizeCategoryExtraSmall

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryExtraSmall: NSString! ``` |
| To | ``` let UIContentSizeCategoryExtraSmall: String ``` |

Modified UIContentSizeCategoryLarge

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryLarge: NSString! ``` |
| To | ``` let UIContentSizeCategoryLarge: String ``` |

Modified UIContentSizeCategoryMedium

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryMedium: NSString! ``` |
| To | ``` let UIContentSizeCategoryMedium: String ``` |

Modified UIContentSizeCategoryNewValueKey

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategoryNewValueKey: NSString! ``` |
| To | ``` let UIContentSizeCategoryNewValueKey: String ``` |

Modified UIContentSizeCategorySmall

|  | Declaration |
| --- | --- |
| From | ``` let UIContentSizeCategorySmall: NSString! ``` |
| To | ``` let UIContentSizeCategorySmall: String ``` |

Modified UIDeviceBatteryLevelDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIDeviceBatteryLevelDidChangeNotification: NSString! ``` |
| To | ``` let UIDeviceBatteryLevelDidChangeNotification: String ``` |

Modified UIDeviceBatteryStateDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIDeviceBatteryStateDidChangeNotification: NSString! ``` |
| To | ``` let UIDeviceBatteryStateDidChangeNotification: String ``` |

Modified UIDeviceOrientationDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIDeviceOrientationDidChangeNotification: NSString! ``` |
| To | ``` let UIDeviceOrientationDidChangeNotification: String ``` |

Modified UIDeviceProximityStateDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIDeviceProximityStateDidChangeNotification: NSString! ``` |
| To | ``` let UIDeviceProximityStateDidChangeNotification: String ``` |

Modified UIDocumentStateChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIDocumentStateChangedNotification: NSString! ``` |
| To | ``` let UIDocumentStateChangedNotification: String ``` |

Modified UIFontDescriptorCascadeListAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorCascadeListAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorCascadeListAttribute: String ``` |

Modified UIFontDescriptorCharacterSetAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorCharacterSetAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorCharacterSetAttribute: String ``` |

Modified UIFontDescriptorFaceAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorFaceAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorFaceAttribute: String ``` |

Modified UIFontDescriptorFamilyAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorFamilyAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorFamilyAttribute: String ``` |

Modified UIFontDescriptorFeatureSettingsAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorFeatureSettingsAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorFeatureSettingsAttribute: String ``` |

Modified UIFontDescriptorFixedAdvanceAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorFixedAdvanceAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorFixedAdvanceAttribute: String ``` |

Modified UIFontDescriptorMatrixAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorMatrixAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorMatrixAttribute: String ``` |

Modified UIFontDescriptorNameAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorNameAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorNameAttribute: String ``` |

Modified UIFontDescriptorSizeAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorSizeAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorSizeAttribute: String ``` |

Modified UIFontDescriptorTextStyleAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorTextStyleAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorTextStyleAttribute: String ``` |

Modified UIFontDescriptorTraitsAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorTraitsAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorTraitsAttribute: String ``` |

Modified UIFontDescriptorVisibleNameAttribute

|  | Declaration |
| --- | --- |
| From | ``` let UIFontDescriptorVisibleNameAttribute: NSString! ``` |
| To | ``` let UIFontDescriptorVisibleNameAttribute: String ``` |

Modified UIFontFeatureSelectorIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let UIFontFeatureSelectorIdentifierKey: NSString! ``` |
| To | ``` let UIFontFeatureSelectorIdentifierKey: String ``` |

Modified UIFontFeatureTypeIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let UIFontFeatureTypeIdentifierKey: NSString! ``` |
| To | ``` let UIFontFeatureTypeIdentifierKey: String ``` |

Modified UIFontSlantTrait

|  | Declaration |
| --- | --- |
| From | ``` let UIFontSlantTrait: NSString! ``` |
| To | ``` let UIFontSlantTrait: String ``` |

Modified UIFontSymbolicTrait

|  | Declaration |
| --- | --- |
| From | ``` let UIFontSymbolicTrait: NSString! ``` |
| To | ``` let UIFontSymbolicTrait: String ``` |

Modified UIFontTextStyleBody

|  | Declaration |
| --- | --- |
| From | ``` let UIFontTextStyleBody: NSString! ``` |
| To | ``` let UIFontTextStyleBody: String ``` |

Modified UIFontTextStyleCaption1

|  | Declaration |
| --- | --- |
| From | ``` let UIFontTextStyleCaption1: NSString! ``` |
| To | ``` let UIFontTextStyleCaption1: String ``` |

Modified UIFontTextStyleCaption2

|  | Declaration |
| --- | --- |
| From | ``` let UIFontTextStyleCaption2: NSString! ``` |
| To | ``` let UIFontTextStyleCaption2: String ``` |

Modified UIFontTextStyleFootnote

|  | Declaration |
| --- | --- |
| From | ``` let UIFontTextStyleFootnote: NSString! ``` |
| To | ``` let UIFontTextStyleFootnote: String ``` |

Modified UIFontTextStyleHeadline

|  | Declaration |
| --- | --- |
| From | ``` let UIFontTextStyleHeadline: NSString! ``` |
| To | ``` let UIFontTextStyleHeadline: String ``` |

Modified UIFontTextStyleSubheadline

|  | Declaration |
| --- | --- |
| From | ``` let UIFontTextStyleSubheadline: NSString! ``` |
| To | ``` let UIFontTextStyleSubheadline: String ``` |

Modified UIFontWeightTrait

|  | Declaration |
| --- | --- |
| From | ``` let UIFontWeightTrait: NSString! ``` |
| To | ``` let UIFontWeightTrait: String ``` |

Modified UIFontWidthTrait

|  | Declaration |
| --- | --- |
| From | ``` let UIFontWidthTrait: NSString! ``` |
| To | ``` let UIFontWidthTrait: String ``` |

Modified UIImagePickerControllerCropRect

|  | Declaration |
| --- | --- |
| From | ``` let UIImagePickerControllerCropRect: NSString! ``` |
| To | ``` let UIImagePickerControllerCropRect: String ``` |

Modified UIImagePickerControllerEditedImage

|  | Declaration |
| --- | --- |
| From | ``` let UIImagePickerControllerEditedImage: NSString! ``` |
| To | ``` let UIImagePickerControllerEditedImage: String ``` |

Modified UIImagePickerControllerMediaMetadata

|  | Declaration |
| --- | --- |
| From | ``` let UIImagePickerControllerMediaMetadata: NSString! ``` |
| To | ``` let UIImagePickerControllerMediaMetadata: String ``` |

Modified UIImagePickerControllerMediaType

|  | Declaration |
| --- | --- |
| From | ``` let UIImagePickerControllerMediaType: NSString! ``` |
| To | ``` let UIImagePickerControllerMediaType: String ``` |

Modified UIImagePickerControllerMediaURL

|  | Declaration |
| --- | --- |
| From | ``` let UIImagePickerControllerMediaURL: NSString! ``` |
| To | ``` let UIImagePickerControllerMediaURL: String ``` |

Modified UIImagePickerControllerOriginalImage

|  | Declaration |
| --- | --- |
| From | ``` let UIImagePickerControllerOriginalImage: NSString! ``` |
| To | ``` let UIImagePickerControllerOriginalImage: String ``` |

Modified UIImagePickerControllerReferenceURL

|  | Declaration |
| --- | --- |
| From | ``` let UIImagePickerControllerReferenceURL: NSString! ``` |
| To | ``` let UIImagePickerControllerReferenceURL: String ``` |

Modified UIKeyInputDownArrow

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyInputDownArrow: NSString! ``` |
| To | ``` let UIKeyInputDownArrow: String ``` |

Modified UIKeyInputEscape

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyInputEscape: NSString! ``` |
| To | ``` let UIKeyInputEscape: String ``` |

Modified UIKeyInputLeftArrow

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyInputLeftArrow: NSString! ``` |
| To | ``` let UIKeyInputLeftArrow: String ``` |

Modified UIKeyInputRightArrow

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyInputRightArrow: NSString! ``` |
| To | ``` let UIKeyInputRightArrow: String ``` |

Modified UIKeyInputUpArrow

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyInputUpArrow: NSString! ``` |
| To | ``` let UIKeyInputUpArrow: String ``` |

Modified UIKeyboardAnimationCurveUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyboardAnimationCurveUserInfoKey: NSString! ``` |
| To | ``` let UIKeyboardAnimationCurveUserInfoKey: String ``` |

Modified UIKeyboardAnimationDurationUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyboardAnimationDurationUserInfoKey: NSString! ``` |
| To | ``` let UIKeyboardAnimationDurationUserInfoKey: String ``` |

Modified UIKeyboardDidChangeFrameNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyboardDidChangeFrameNotification: NSString! ``` |
| To | ``` let UIKeyboardDidChangeFrameNotification: String ``` |

Modified UIKeyboardDidHideNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyboardDidHideNotification: NSString! ``` |
| To | ``` let UIKeyboardDidHideNotification: String ``` |

Modified UIKeyboardDidShowNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyboardDidShowNotification: NSString! ``` |
| To | ``` let UIKeyboardDidShowNotification: String ``` |

Modified UIKeyboardFrameBeginUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyboardFrameBeginUserInfoKey: NSString! ``` |
| To | ``` let UIKeyboardFrameBeginUserInfoKey: String ``` |

Modified UIKeyboardFrameEndUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyboardFrameEndUserInfoKey: NSString! ``` |
| To | ``` let UIKeyboardFrameEndUserInfoKey: String ``` |

Modified UIKeyboardWillChangeFrameNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyboardWillChangeFrameNotification: NSString! ``` |
| To | ``` let UIKeyboardWillChangeFrameNotification: String ``` |

Modified UIKeyboardWillHideNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyboardWillHideNotification: NSString! ``` |
| To | ``` let UIKeyboardWillHideNotification: String ``` |

Modified UIKeyboardWillShowNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIKeyboardWillShowNotification: NSString! ``` |
| To | ``` let UIKeyboardWillShowNotification: String ``` |

Modified UILocalNotificationDefaultSoundName

|  | Declaration |
| --- | --- |
| From | ``` let UILocalNotificationDefaultSoundName: NSString! ``` |
| To | ``` let UILocalNotificationDefaultSoundName: String ``` |

Modified UIMenuControllerDidHideMenuNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIMenuControllerDidHideMenuNotification: NSString! ``` |
| To | ``` let UIMenuControllerDidHideMenuNotification: String ``` |

Modified UIMenuControllerDidShowMenuNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIMenuControllerDidShowMenuNotification: NSString! ``` |
| To | ``` let UIMenuControllerDidShowMenuNotification: String ``` |

Modified UIMenuControllerMenuFrameDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIMenuControllerMenuFrameDidChangeNotification: NSString! ``` |
| To | ``` let UIMenuControllerMenuFrameDidChangeNotification: String ``` |

Modified UIMenuControllerWillHideMenuNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIMenuControllerWillHideMenuNotification: NSString! ``` |
| To | ``` let UIMenuControllerWillHideMenuNotification: String ``` |

Modified UIMenuControllerWillShowMenuNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIMenuControllerWillShowMenuNotification: NSString! ``` |
| To | ``` let UIMenuControllerWillShowMenuNotification: String ``` |

Modified UINibExternalObjects

|  | Declaration |
| --- | --- |
| From | ``` let UINibExternalObjects: NSString! ``` |
| To | ``` let UINibExternalObjects: String ``` |

Modified UIPageViewControllerOptionInterPageSpacingKey

|  | Declaration |
| --- | --- |
| From | ``` let UIPageViewControllerOptionInterPageSpacingKey: NSString! ``` |
| To | ``` let UIPageViewControllerOptionInterPageSpacingKey: String ``` |

Modified UIPageViewControllerOptionSpineLocationKey

|  | Declaration |
| --- | --- |
| From | ``` let UIPageViewControllerOptionSpineLocationKey: NSString! ``` |
| To | ``` let UIPageViewControllerOptionSpineLocationKey: String ``` |

Modified UIPasteboardChangedNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIPasteboardChangedNotification: NSString! ``` |
| To | ``` let UIPasteboardChangedNotification: String ``` |

Modified UIPasteboardChangedTypesAddedKey

|  | Declaration |
| --- | --- |
| From | ``` let UIPasteboardChangedTypesAddedKey: NSString! ``` |
| To | ``` let UIPasteboardChangedTypesAddedKey: String ``` |

Modified UIPasteboardChangedTypesRemovedKey

|  | Declaration |
| --- | --- |
| From | ``` let UIPasteboardChangedTypesRemovedKey: NSString! ``` |
| To | ``` let UIPasteboardChangedTypesRemovedKey: String ``` |

Modified UIPasteboardNameFind

|  | Declaration |
| --- | --- |
| From | ``` let UIPasteboardNameFind: NSString! ``` |
| To | ``` let UIPasteboardNameFind: String ``` |

Modified UIPasteboardNameGeneral

|  | Declaration |
| --- | --- |
| From | ``` let UIPasteboardNameGeneral: NSString! ``` |
| To | ``` let UIPasteboardNameGeneral: String ``` |

Modified UIPasteboardRemovedNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIPasteboardRemovedNotification: NSString! ``` |
| To | ``` let UIPasteboardRemovedNotification: String ``` |

Modified UIPrintErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let UIPrintErrorDomain: NSString! ``` |
| To | ``` let UIPrintErrorDomain: String ``` |

Modified UIScreenBrightnessDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIScreenBrightnessDidChangeNotification: NSString! ``` |
| To | ``` let UIScreenBrightnessDidChangeNotification: String ``` |

Modified UIScreenDidConnectNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIScreenDidConnectNotification: NSString! ``` |
| To | ``` let UIScreenDidConnectNotification: String ``` |

Modified UIScreenDidDisconnectNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIScreenDidDisconnectNotification: NSString! ``` |
| To | ``` let UIScreenDidDisconnectNotification: String ``` |

Modified UIScreenModeDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIScreenModeDidChangeNotification: NSString! ``` |
| To | ``` let UIScreenModeDidChangeNotification: String ``` |

Modified UIStateRestorationViewControllerStoryboardKey

|  | Declaration |
| --- | --- |
| From | ``` let UIStateRestorationViewControllerStoryboardKey: NSString! ``` |
| To | ``` let UIStateRestorationViewControllerStoryboardKey: String ``` |

Modified UITableViewIndexSearch

|  | Declaration |
| --- | --- |
| From | ``` let UITableViewIndexSearch: NSString! ``` |
| To | ``` let UITableViewIndexSearch: String ``` |

Modified UITableViewSelectionDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UITableViewSelectionDidChangeNotification: NSString! ``` |
| To | ``` let UITableViewSelectionDidChangeNotification: String ``` |

Modified UITextFieldTextDidBeginEditingNotification

|  | Declaration |
| --- | --- |
| From | ``` let UITextFieldTextDidBeginEditingNotification: NSString! ``` |
| To | ``` let UITextFieldTextDidBeginEditingNotification: String ``` |

Modified UITextFieldTextDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UITextFieldTextDidChangeNotification: NSString! ``` |
| To | ``` let UITextFieldTextDidChangeNotification: String ``` |

Modified UITextFieldTextDidEndEditingNotification

|  | Declaration |
| --- | --- |
| From | ``` let UITextFieldTextDidEndEditingNotification: NSString! ``` |
| To | ``` let UITextFieldTextDidEndEditingNotification: String ``` |

Modified UITextInputCurrentInputModeDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UITextInputCurrentInputModeDidChangeNotification: NSString! ``` |
| To | ``` let UITextInputCurrentInputModeDidChangeNotification: String ``` |

Modified UITextInputTextBackgroundColorKey

|  | Declaration |
| --- | --- |
| From | ``` let UITextInputTextBackgroundColorKey: NSString! ``` |
| To | ``` let UITextInputTextBackgroundColorKey: String ``` |

Modified UITextInputTextColorKey

|  | Declaration |
| --- | --- |
| From | ``` let UITextInputTextColorKey: NSString! ``` |
| To | ``` let UITextInputTextColorKey: String ``` |

Modified UITextInputTextFontKey

|  | Declaration |
| --- | --- |
| From | ``` let UITextInputTextFontKey: NSString! ``` |
| To | ``` let UITextInputTextFontKey: String ``` |

Modified UITextViewTextDidBeginEditingNotification

|  | Declaration |
| --- | --- |
| From | ``` let UITextViewTextDidBeginEditingNotification: NSString! ``` |
| To | ``` let UITextViewTextDidBeginEditingNotification: String ``` |

Modified UITextViewTextDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UITextViewTextDidChangeNotification: NSString! ``` |
| To | ``` let UITextViewTextDidChangeNotification: String ``` |

Modified UITextViewTextDidEndEditingNotification

|  | Declaration |
| --- | --- |
| From | ``` let UITextViewTextDidEndEditingNotification: NSString! ``` |
| To | ``` let UITextViewTextDidEndEditingNotification: String ``` |

Modified UITrackingRunLoopMode

|  | Declaration |
| --- | --- |
| From | ``` let UITrackingRunLoopMode: NSString! ``` |
| To | ``` let UITrackingRunLoopMode: String ``` |

Modified UITransitionContextFromViewControllerKey

|  | Declaration |
| --- | --- |
| From | ``` let UITransitionContextFromViewControllerKey: NSString! ``` |
| To | ``` let UITransitionContextFromViewControllerKey: String ``` |

Modified UITransitionContextFromViewKey

|  | Declaration |
| --- | --- |
| From | ``` let UITransitionContextFromViewKey: NSString! ``` |
| To | ``` let UITransitionContextFromViewKey: String ``` |

Modified UITransitionContextToViewControllerKey

|  | Declaration |
| --- | --- |
| From | ``` let UITransitionContextToViewControllerKey: NSString! ``` |
| To | ``` let UITransitionContextToViewControllerKey: String ``` |

Modified UITransitionContextToViewKey

|  | Declaration |
| --- | --- |
| From | ``` let UITransitionContextToViewKey: NSString! ``` |
| To | ``` let UITransitionContextToViewKey: String ``` |

Modified UIViewControllerHierarchyInconsistencyException

|  | Declaration |
| --- | --- |
| From | ``` let UIViewControllerHierarchyInconsistencyException: NSString! ``` |
| To | ``` let UIViewControllerHierarchyInconsistencyException: String ``` |

Modified UIViewControllerShowDetailTargetDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIViewControllerShowDetailTargetDidChangeNotification: NSString! ``` |
| To | ``` let UIViewControllerShowDetailTargetDidChangeNotification: String ``` |

Modified UIWindowDidBecomeHiddenNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIWindowDidBecomeHiddenNotification: NSString! ``` |
| To | ``` let UIWindowDidBecomeHiddenNotification: String ``` |

Modified UIWindowDidBecomeKeyNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIWindowDidBecomeKeyNotification: NSString! ``` |
| To | ``` let UIWindowDidBecomeKeyNotification: String ``` |

Modified UIWindowDidBecomeVisibleNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIWindowDidBecomeVisibleNotification: NSString! ``` |
| To | ``` let UIWindowDidBecomeVisibleNotification: String ``` |

Modified UIWindowDidResignKeyNotification

|  | Declaration |
| --- | --- |
| From | ``` let UIWindowDidResignKeyNotification: NSString! ``` |
| To | ``` let UIWindowDidResignKeyNotification: String ``` |

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
