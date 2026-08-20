---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/UIKit.html
archived_at: '2026-07-18T02:56:17.049610Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# UIKit Changes

## UIKit

Removed NSLayoutFormatOptions.valueRemoved NSTextStorageEditActions.valueRemoved UICollectionViewScrollPosition.valueRemoved UICollisionBehaviorMode.valueRemoved UIControlEvents.valueRemoved UIControlState.valueRemoved UIDataDetectorTypes.valueRemoved UIDocumentState.valueRemoved UIFontDescriptorSymbolicTraits.valueRemoved UIInterfaceOrientationMask.valueRemoved UIKeyModifierFlags.valueRemoved UIPopoverArrowDirection.valueRemoved UIPrinterJobTypes.valueRemoved UIRectCorner.valueRemoved UIRectEdge.valueRemoved UIRemoteNotificationType.valueRemoved UISwipeGestureRecognizerDirection.valueRemoved UITableViewCellStateMask.valueRemoved UIUserNotificationType.valueRemoved UIViewAnimationOptions.valueRemoved UIViewAutoresizing.valueRemoved UIViewKeyframeAnimationOptions.valueAdded CIColor.init(color: UIColor)Added CIImage.init(image: UIImage!)Added CIImage.init(image: UIImage!, options:[NSObject: AnyObject]!)Added NSAttributedString.init(attachment: NSTextAttachment!)Added NSAttributedString.boundingRectWithSize(CGSize, options: NSStringDrawingOptions, context: NSStringDrawingContext?) -> CGRectAdded NSAttributedString.init(data: NSData, options:[NSObject: AnyObject]?, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error: NSErrorPointer)Added NSAttributedString.dataFromRange(NSRange, documentAttributes:[NSObject: AnyObject]!, error: NSErrorPointer) -> NSData?Added NSAttributedString.drawAtPoint(CGPoint)Added NSAttributedString.drawInRect(CGRect)Added NSAttributedString.drawWithRect(CGRect, options: NSStringDrawingOptions, context: NSStringDrawingContext?)Added NSAttributedString.init(fileURL: NSURL!, options:[NSObject: AnyObject]!, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error: NSErrorPointer)Added NSAttributedString.fileWrapperFromRange(NSRange, documentAttributes:[NSObject: AnyObject]!, error: NSErrorPointer) -> NSFileWrapper?Added NSAttributedString.size() -> CGSizeAdded NSBundle.loadNibNamed(String!, owner: AnyObject!, options:[NSObject: AnyObject]!) -> [AnyObject]!Added NSCoder.decodeCGAffineTransformForKey(String!) -> CGAffineTransformAdded NSCoder.decodeCGPointForKey(String!) -> CGPointAdded NSCoder.decodeCGRectForKey(String!) -> CGRectAdded NSCoder.decodeCGSizeForKey(String!) -> CGSizeAdded NSCoder.decodeCGVectorForKey(String!) -> CGVectorAdded NSCoder.decodeUIEdgeInsetsForKey(String!) -> UIEdgeInsetsAdded NSCoder.decodeUIOffsetForKey(String!) -> UIOffsetAdded NSCoder.encodeCGAffineTransform(CGAffineTransform, forKey: String!)Added NSCoder.encodeCGPoint(CGPoint, forKey: String!)Added NSCoder.encodeCGRect(CGRect, forKey: String!)Added NSCoder.encodeCGSize(CGSize, forKey: String!)Added NSCoder.encodeCGVector(CGVector, forKey: String!)Added NSCoder.encodeUIEdgeInsets(UIEdgeInsets, forKey: String!)Added NSCoder.encodeUIOffset(UIOffset, forKey: String!)Added NSIndexPath.init(forItem: Int, inSection: Int)Added NSIndexPath.init(forRow: Int, inSection: Int)Added NSIndexPath.itemAdded NSIndexPath.rowAdded NSIndexPath.sectionAdded NSLayoutFormatOptions.init(rawValue: UInt)Added NSMutableAttributedString.fixAttributesInRange(NSRange)Added NSMutableAttributedString.readFromData(NSData, options:[NSObject: AnyObject]?, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error: NSErrorPointer) -> BoolAdded NSMutableAttributedString.readFromFileURL(NSURL!, options:[NSObject: AnyObject]!, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error: NSErrorPointer) -> BoolAdded NSObject.accessibilityActivate() -> BoolAdded NSObject.accessibilityActivationPointAdded NSObject.accessibilityCustomActionsAdded NSObject.accessibilityDecrement()Added NSObject.accessibilityElementAtIndex(Int) -> AnyObject!Added NSObject.accessibilityElementCount() -> IntAdded NSObject.accessibilityElementDidBecomeFocused()Added NSObject.accessibilityElementDidLoseFocus()Added NSObject.accessibilityElementIsFocused() -> BoolAdded NSObject.accessibilityElementsAdded NSObject.accessibilityElementsHiddenAdded NSObject.accessibilityFrameAdded NSObject.accessibilityHintAdded NSObject.accessibilityIncrement()Added NSObject.accessibilityLabelAdded NSObject.accessibilityLanguageAdded NSObject.accessibilityNavigationStyleAdded NSObject.accessibilityPathAdded NSObject.accessibilityPerformEscape() -> BoolAdded NSObject.accessibilityPerformMagicTap() -> BoolAdded NSObject.accessibilityScroll(UIAccessibilityScrollDirection) -> BoolAdded NSObject.accessibilityTraitsAdded NSObject.accessibilityValueAdded NSObject.accessibilityViewIsModalAdded NSObject.awakeFromNib()Added NSObject.copy(AnyObject?)Added NSObject.cut(AnyObject?)Added NSObject.decreaseSize(AnyObject?)Added NSObject.delete(AnyObject?)Added NSObject.increaseSize(AnyObject?)Added NSObject.indexOfAccessibilityElement(AnyObject!) -> IntAdded NSObject.isAccessibilityElementAdded NSObject.makeTextWritingDirectionLeftToRight(AnyObject?)Added NSObject.makeTextWritingDirectionRightToLeft(AnyObject?)Added NSObject.paste(AnyObject?)Added NSObject.prepareForInterfaceBuilder()Added NSObject.select(AnyObject?)Added NSObject.selectAll(AnyObject?)Added NSObject.shouldGroupAccessibilityChildrenAdded NSObject.toggleBoldface(AnyObject?)Added NSObject.toggleItalics(AnyObject?)Added NSObject.toggleUnderline(AnyObject?)Added NSString.boundingRectWithSize(CGSize, options: NSStringDrawingOptions, attributes:[NSObject: AnyObject]!, context: NSStringDrawingContext!) -> CGRectAdded NSString.drawAtPoint(CGPoint, withAttributes:[NSObject: AnyObject]?)Added NSString.drawInRect(CGRect, withAttributes:[NSObject: AnyObject]?)Added NSString.drawWithRect(CGRect, options: NSStringDrawingOptions, attributes:[NSObject: AnyObject]!, context: NSStringDrawingContext!)Added NSString.sizeWithAttributes([NSObject: AnyObject]?) -> CGSizeAdded NSTextStorageEditActions.init(rawValue: UInt)Added NSValue.init(CGAffineTransform: CGAffineTransform)Added NSValue.CGAffineTransformValue() -> CGAffineTransformAdded NSValue.init(CGPoint: CGPoint)Added NSValue.CGPointValue() -> CGPointAdded NSValue.init(CGRect: CGRect)Added NSValue.CGRectValue() -> CGRectAdded NSValue.init(CGSize: CGSize)Added NSValue.CGSizeValue() -> CGSizeAdded NSValue.init(CGVector: CGVector)Added NSValue.CGVectorValue() -> CGVectorAdded NSValue.init(UIEdgeInsets: UIEdgeInsets)Added NSValue.UIEdgeInsetsValue() -> UIEdgeInsetsAdded NSValue.init(UIOffset: UIOffset)Added NSValue.UIOffsetValue() -> UIOffsetAdded UICollectionViewScrollPosition.init(rawValue: UInt)Added UICollisionBehaviorMode.init(rawValue: UInt)Added UIControlEvents.init(rawValue: UInt)Added UIControlState.init(rawValue: UInt)Added UIDataDetectorTypes.init(rawValue: UInt)Added UIDocumentState.init(rawValue: UInt)Added UIFontDescriptorSymbolicTraits.init(rawValue: UInt32)Added UIInterfaceOrientationMask.init(rawValue: UInt)Added UIKeyModifierFlags.init(rawValue: Int)Added UILocalNotification.regionAdded UIManagedDocument.managedObjectContextAdded UIManagedDocument.managedObjectModelAdded UIPopoverArrowDirection.init(rawValue: UInt)Added UIPrinterJobTypes.init(rawValue: Int)Added UIRectCorner.init(rawValue: UInt)Added UIRectEdge.init(rawValue: UInt)Added UIRemoteNotificationType.init(rawValue: UInt)Added UISwipeGestureRecognizerDirection.init(rawValue: UInt)Added UITableViewCellStateMask.init(rawValue: UInt)Added UIUserNotificationType.init(rawValue: UInt)Added UIViewAnimationOptions.init(rawValue: UInt)Added UIViewAutoresizing.init(rawValue: UInt)Added UIViewKeyframeAnimationOptions.init(rawValue: UInt)Modified NSControlCharacterAction [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSGlyphProperty [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutConstraint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSLayoutConstraint.identifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutFormatOptions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSLayoutFormatOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var AlignAllLeft: NSLayoutFormatOptions { get }     static var AlignAllRight: NSLayoutFormatOptions { get }     static var AlignAllTop: NSLayoutFormatOptions { get }     static var AlignAllBottom: NSLayoutFormatOptions { get }     static var AlignAllLeading: NSLayoutFormatOptions { get }     static var AlignAllTrailing: NSLayoutFormatOptions { get }     static var AlignAllCenterX: NSLayoutFormatOptions { get }     static var AlignAllCenterY: NSLayoutFormatOptions { get }     static var AlignAllBaseline: NSLayoutFormatOptions { get }     static var AlignAllLastBaseline: NSLayoutFormatOptions { get }     static var AlignAllFirstBaseline: NSLayoutFormatOptions { get }     static var AlignmentMask: NSLayoutFormatOptions { get }     static var DirectionLeadingToTrailing: NSLayoutFormatOptions { get }     static var DirectionLeftToRight: NSLayoutFormatOptions { get }     static var DirectionRightToLeft: NSLayoutFormatOptions { get }     static var DirectionMask: NSLayoutFormatOptions { get } } ``` |
| To | ``` struct NSLayoutFormatOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var AlignAllLeft: NSLayoutFormatOptions { get }     static var AlignAllRight: NSLayoutFormatOptions { get }     static var AlignAllTop: NSLayoutFormatOptions { get }     static var AlignAllBottom: NSLayoutFormatOptions { get }     static var AlignAllLeading: NSLayoutFormatOptions { get }     static var AlignAllTrailing: NSLayoutFormatOptions { get }     static var AlignAllCenterX: NSLayoutFormatOptions { get }     static var AlignAllCenterY: NSLayoutFormatOptions { get }     static var AlignAllBaseline: NSLayoutFormatOptions { get }     static var AlignAllLastBaseline: NSLayoutFormatOptions { get }     static var AlignAllFirstBaseline: NSLayoutFormatOptions { get }     static var AlignmentMask: NSLayoutFormatOptions { get }     static var DirectionLeadingToTrailing: NSLayoutFormatOptions { get }     static var DirectionLeftToRight: NSLayoutFormatOptions { get }     static var DirectionRightToLeft: NSLayoutFormatOptions { get }     static var DirectionMask: NSLayoutFormatOptions { get } } ``` |

Modified NSLayoutFormatOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSLayoutManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManager.setTextContainer(NSTextContainer?, forGlyphRange: NSRange)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setTextContainer(_ container: NSTextContainer, forGlyphRange glyphRange: NSRange) ``` | iOS 8.0 |
| To | ``` func setTextContainer(_ container: NSTextContainer?, forGlyphRange glyphRange: NSRange) ``` | iOS 8.1 |

Modified NSLayoutManagerDelegate.layoutManager(NSLayoutManager, boundingBoxForControlGlyphAtIndex: Int, forTextContainer: NSTextContainer, proposedLineFragment: CGRect, glyphPosition: CGPoint, characterIndex: Int) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManagerDelegate.layoutManager(NSLayoutManager, didCompleteLayoutForTextContainer: NSTextContainer?, atEnd: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManagerDelegate.layoutManager(NSLayoutManager, lineSpacingAfterGlyphAtIndex: Int, withProposedLineFragmentRect: CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManagerDelegate.layoutManager(NSLayoutManager, paragraphSpacingAfterGlyphAtIndex: Int, withProposedLineFragmentRect: CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManagerDelegate.layoutManager(NSLayoutManager, paragraphSpacingBeforeGlyphAtIndex: Int, withProposedLineFragmentRect: CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManagerDelegate.layoutManager(NSLayoutManager, shouldBreakLineByHyphenatingBeforeCharacterAtIndex: Int) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManagerDelegate.layoutManager(NSLayoutManager, shouldBreakLineByWordBeforeCharacterAtIndex: Int) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManagerDelegate.layoutManager(NSLayoutManager, shouldGenerateGlyphs: UnsafePointer<CGGlyph>, properties: UnsafePointer<NSGlyphProperty>, characterIndexes: UnsafePointer<Int>, font: UIFont!, forGlyphRange: NSRange) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManagerDelegate.layoutManager(NSLayoutManager, shouldUseAction: NSControlCharacterAction, forControlCharacterAtIndex: Int) -> NSControlCharacterAction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManagerDelegate.layoutManager(NSLayoutManager, textContainer: NSTextContainer, didChangeGeometryFromSize: CGSize)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLayoutManagerDelegate.layoutManagerDidInvalidateLayout(NSLayoutManager)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSLineBreakMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMutableParagraphStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSMutableParagraphStyle.defaultTabInterval

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSMutableParagraphStyle.tabStops

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSParagraphStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSParagraphStyle.defaultTabInterval

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSParagraphStyle.tabStops

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSShadow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSStringDrawingContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSStringDrawingOptions [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSTextAlignment [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSTextAttachment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextAttachmentContainer.attachmentBoundsForTextContainer(NSTextContainer, proposedLineFragment: CGRect, glyphPosition: CGPoint, characterIndex: Int) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextAttachmentContainer.imageForBounds(CGRect, textContainer: NSTextContainer, characterIndex: Int) -> UIImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextContainer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextLayoutOrientation [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextLayoutOrientationProvider.layoutOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextStorage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextStorageDelegate.textStorage(NSTextStorage, didProcessEditing: NSTextStorageEditActions, range: NSRange, changeInLength: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextStorageDelegate.textStorage(NSTextStorage, willProcessEditing: NSTextStorageEditActions, range: NSRange, changeInLength: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextStorageEditActions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct NSTextStorageEditActions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var EditedAttributes: NSTextStorageEditActions { get }     static var EditedCharacters: NSTextStorageEditActions { get } } ``` | iOS 8.0 |
| To | ``` struct NSTextStorageEditActions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var EditedAttributes: NSTextStorageEditActions { get }     static var EditedCharacters: NSTextStorageEditActions { get } } ``` | iOS 7.0 |

Modified NSTextStorageEditActions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified NSTextTab

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextWritingDirection [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUnderlineStyle [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSWritingDirection [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIAccessibilityElement

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIAccessibilityIdentification.accessibilityIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityReadingContent.accessibilityContentForLineNumber(Int) -> String?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityReadingContent.accessibilityFrameForLineNumber(Int) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityReadingContent.accessibilityLineNumberForPoint(CGPoint) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityReadingContent.accessibilityPageContent() -> String!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityZoomType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIActionSheet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIActionSheet.showFromBarButtonItem(UIBarButtonItem!, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIActionSheet.showFromRect(CGRect, inView: UIView!, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIActivity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivity.activityCategory() -> UIActivityCategory [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIActivityCategory [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIActivityIndicatorView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIActivityIndicatorView.init(activityIndicatorStyle: UIActivityIndicatorViewStyle)

|  | Declaration |
| --- | --- |
| From | ``` init(activityIndicatorStyle style: UIActivityIndicatorViewStyle) ``` |
| To | ``` init!(activityIndicatorStyle style: UIActivityIndicatorViewStyle) ``` |

Modified UIActivityIndicatorView.color

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIActivityItemProvider

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivityViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivityViewController.completionHandler

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified UIAlertView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIAlertView.alertViewStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAlertView.textFieldAtIndex(Int) -> UITextField?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIApplication

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIApplication.applicationState

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.applicationSupportsShakeToEdit

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIApplication.backgroundRefreshStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplication.backgroundTimeRemaining

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.beginBackgroundTaskWithExpirationHandler(() -> Void) -> UIBackgroundTaskIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.beginBackgroundTaskWithName(String?, expirationHandler:(() -> Void)?) -> UIBackgroundTaskIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplication.beginReceivingRemoteControlEvents()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.canOpenURL(NSURL) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIApplication.cancelAllLocalNotifications()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.cancelLocalNotification(UILocalNotification)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.clearKeepAliveTimeout()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.completeStateRestoration()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplication.enabledRemoteNotificationTypes() -> UIRemoteNotificationType

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UIApplication.endBackgroundTask(UIBackgroundTaskIdentifier)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.endReceivingRemoteControlEvents()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.extendStateRestoration()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplication.ignoreSnapshotOnNextApplicationLaunch()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplication.keyWindow

|  | Declaration |
| --- | --- |
| From | ``` var keyWindow: UIWindow { get } ``` |
| To | ``` var keyWindow: UIWindow? { get } ``` |

Modified UIApplication.preferredContentSizeCategory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplication.presentLocalNotificationNow(UILocalNotification)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.protectedDataAvailable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.registerForRemoteNotificationTypes(UIRemoteNotificationType)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UIApplication.registerObjectForStateRestoration(UIStateRestoring, restorationIdentifier: String) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplication.scheduleLocalNotification(UILocalNotification)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.scheduledLocalNotifications

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.setKeepAliveTimeout(NSTimeInterval, handler:(() -> Void)?) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplication.setMinimumBackgroundFetchInterval(NSTimeInterval)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplication.setStatusBarHidden(Bool, withAnimation: UIStatusBarAnimation)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIApplication.supportedInterfaceOrientationsForWindow(UIWindow) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplication.unregisterForRemoteNotifications()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIApplication.userInterfaceLayoutDirection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIApplicationDelegate.application(UIApplication, didDecodeRestorableStateWithCoder: NSCoder)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationDelegate.application(UIApplication, didFailToRegisterForRemoteNotificationsWithError: NSError)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIApplicationDelegate.application(UIApplication, didFinishLaunchingWithOptions:[NSObject: AnyObject]?) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIApplicationDelegate.application(UIApplication, didReceiveLocalNotification: UILocalNotification)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplicationDelegate.application(UIApplication, didReceiveRemoteNotification:[NSObject: AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIApplicationDelegate.application(UIApplication, didReceiveRemoteNotification:[NSObject: AnyObject], fetchCompletionHandler:(UIBackgroundFetchResult) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationDelegate.application(UIApplication, didRegisterForRemoteNotificationsWithDeviceToken: NSData)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIApplicationDelegate.application(UIApplication, handleEventsForBackgroundURLSession: String, completionHandler:() -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationDelegate.application(UIApplication, openURL: NSURL, sourceApplication: String?, annotation: AnyObject?) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func application(_ application: UIApplication, openURL url: NSURL, sourceApplication sourceApplication: String, annotation annotation: AnyObject?) -> Bool ``` | iOS 8.0 |
| To | ``` optional func application(_ application: UIApplication, openURL url: NSURL, sourceApplication sourceApplication: String?, annotation annotation: AnyObject?) -> Bool ``` | iOS 4.2 |

Modified UIApplicationDelegate.application(UIApplication, performFetchWithCompletionHandler:(UIBackgroundFetchResult) -> Void)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationDelegate.application(UIApplication, shouldRestoreApplicationState: NSCoder) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationDelegate.application(UIApplication, shouldSaveApplicationState: NSCoder) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationDelegate.application(UIApplication, supportedInterfaceOrientationsForWindow: UIWindow) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationDelegate.application(UIApplication, viewControllerWithRestorationIdentifierPath:[AnyObject], coder: NSCoder) -> UIViewController?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationDelegate.application(UIApplication, willEncodeRestorableStateWithCoder: NSCoder)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationDelegate.application(UIApplication, willFinishLaunchingWithOptions:[NSObject: AnyObject]?) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationDelegate.applicationDidEnterBackground(UIApplication)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplicationDelegate.applicationProtectedDataDidBecomeAvailable(UIApplication)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplicationDelegate.applicationProtectedDataWillBecomeUnavailable(UIApplication)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplicationDelegate.applicationWillEnterForeground(UIApplication)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplicationDelegate.window

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIApplicationState [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIAttachmentBehavior

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIAttachmentBehavior.init(item: UIDynamicItem, attachedToAnchor: CGPoint)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(item item: UIDynamicItem, attachedToAnchor point: CGPoint) ``` |
| To | ``` convenience init!(item item: UIDynamicItem, attachedToAnchor point: CGPoint) ``` |

Modified UIAttachmentBehavior.init(item: UIDynamicItem, attachedToItem: UIDynamicItem)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(item item1: UIDynamicItem, attachedToItem item2: UIDynamicItem) ``` |
| To | ``` convenience init!(item item1: UIDynamicItem, attachedToItem item2: UIDynamicItem) ``` |

Modified UIAttachmentBehavior.init(item: UIDynamicItem, offsetFromCenter: UIOffset, attachedToAnchor: CGPoint)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(item item: UIDynamicItem, offsetFromCenter offset: UIOffset, attachedToAnchor point: CGPoint) ``` |
| To | ``` convenience init!(item item: UIDynamicItem, offsetFromCenter offset: UIOffset, attachedToAnchor point: CGPoint) ``` |

Modified UIAttachmentBehavior.init(item: UIDynamicItem, offsetFromCenter: UIOffset, attachedToItem: UIDynamicItem, offsetFromCenter: UIOffset)

|  | Declaration |
| --- | --- |
| From | ``` init(item item1: UIDynamicItem, offsetFromCenter offset1: UIOffset, attachedToItem item2: UIDynamicItem, offsetFromCenter offset2: UIOffset) ``` |
| To | ``` init!(item item1: UIDynamicItem, offsetFromCenter offset1: UIOffset, attachedToItem item2: UIDynamicItem, offsetFromCenter offset2: UIOffset) ``` |

Modified UIAttachmentBehaviorType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIBackgroundFetchResult [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIBackgroundRefreshStatus [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIBarButtonItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIBarButtonItem.backButtonBackgroundImageForState(UIControlState, barMetrics: UIBarMetrics) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.backButtonBackgroundVerticalPositionAdjustmentForBarMetrics(UIBarMetrics) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.backButtonTitlePositionAdjustmentForBarMetrics(UIBarMetrics) -> UIOffset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.backgroundImageForState(UIControlState, barMetrics: UIBarMetrics) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.backgroundImageForState(UIControlState, style: UIBarButtonItemStyle, barMetrics: UIBarMetrics) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIBarButtonItem.backgroundVerticalPositionAdjustmentForBarMetrics(UIBarMetrics) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.init(image: UIImage?, landscapeImagePhone: UIImage?, style: UIBarButtonItemStyle, target: AnyObject?, action: Selector)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.setBackButtonBackgroundImage(UIImage?, forState: UIControlState, barMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.setBackButtonBackgroundVerticalPositionAdjustment(CGFloat, forBarMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.setBackButtonTitlePositionAdjustment(UIOffset, forBarMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.setBackgroundImage(UIImage?, forState: UIControlState, barMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.setBackgroundImage(UIImage?, forState: UIControlState, style: UIBarButtonItemStyle, barMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIBarButtonItem.setBackgroundVerticalPositionAdjustment(CGFloat, forBarMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.setTitlePositionAdjustment(UIOffset, forBarMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.tintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarButtonItem.titlePositionAdjustmentForBarMetrics(UIBarMetrics) -> UIOffset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIBarItem.landscapeImagePhone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarItem.landscapeImagePhoneInsets

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarItem.setTitleTextAttributes([NSObject: AnyObject]!, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarItem.titleTextAttributesForState(UIControlState) -> [NSObject: AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIBarPosition [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIBezierPath

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIBezierPath.addArcWithCenter(CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIBezierPath.bezierPathByReversingPath() -> UIBezierPath

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIButton

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIButton.attributedTitleForState(UIControlState) -> NSAttributedString?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIButton.currentAttributedTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIButton.imageView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIButton.setAttributedTitle(NSAttributedString!, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIButton.tintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIButton.titleLabel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UICollectionReusableView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UICollectionView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UICollectionView.cancelInteractiveTransition()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionView.finishInteractiveTransition()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionView.indexPathsForSelectedItems() -> [AnyObject]?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexPathsForSelectedItems() -> [AnyObject] ``` | iOS 8.0 |
| To | ``` func indexPathsForSelectedItems() -> [AnyObject]? ``` | iOS 8.1 |

Modified UICollectionView.performBatchUpdates((() -> Void)?, completion:((Bool) -> Void)?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func performBatchUpdates(_ updates: () -> Void, completion completion: ((Bool) -> Void)!) ``` | iOS 8.0 |
| To | ``` func performBatchUpdates(_ updates: (() -> Void)?, completion completion: ((Bool) -> Void)?) ``` | iOS 8.1 |

Modified UICollectionView.setCollectionViewLayout(UICollectionViewLayout, animated: Bool, completion:((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionView.startInteractiveTransitionToCollectionViewLayout(UICollectionViewLayout, completion: UICollectionViewLayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewCell

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UICollectionViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UICollectionViewController.collectionView

|  | Declaration |
| --- | --- |
| From | ``` var collectionView: UICollectionView? ``` |
| To | ``` var collectionView: UICollectionView ``` |

Modified UICollectionViewController.collectionViewLayout

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewController.useLayoutToLayoutNavigationTransitions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewFlowLayout

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UICollectionViewFlowLayoutInvalidationContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UICollectionViewLayout.finalizeLayoutTransition()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout.indexPathsToDeleteForDecorationViewOfKind(String) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout.indexPathsToDeleteForSupplementaryViewOfKind(String) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout.indexPathsToInsertForDecorationViewOfKind(String) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout.indexPathsToInsertForSupplementaryViewOfKind(String) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout.invalidateLayoutWithContext(UICollectionViewLayoutInvalidationContext)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout.invalidationContextClass() -> AnyClass [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout.invalidationContextForBoundsChange(CGRect) -> UICollectionViewLayoutInvalidationContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout.prepareForTransitionFromLayout(UICollectionViewLayout)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout.prepareForTransitionToLayout(UICollectionViewLayout!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayout.targetContentOffsetForProposedContentOffset(CGPoint) -> CGPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayoutAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UICollectionViewLayoutAttributes.bounds

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayoutAttributes.transform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayoutInvalidationContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewLayoutInvalidationContext.invalidatedItemIndexPaths

|  | Declaration |
| --- | --- |
| From | ``` var invalidatedItemIndexPaths: [AnyObject] { get } ``` |
| To | ``` var invalidatedItemIndexPaths: [AnyObject]? { get } ``` |

Modified UICollectionViewLayoutInvalidationContext.invalidatedSupplementaryIndexPaths

|  | Declaration |
| --- | --- |
| From | ``` var invalidatedSupplementaryIndexPaths: [NSObject : AnyObject]! { get } ``` |
| To | ``` var invalidatedSupplementaryIndexPaths: [NSObject : AnyObject]? { get } ``` |

Modified UICollectionViewScrollPosition [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UICollectionViewScrollPosition : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: UICollectionViewScrollPosition { get }     static var Top: UICollectionViewScrollPosition { get }     static var CenteredVertically: UICollectionViewScrollPosition { get }     static var Bottom: UICollectionViewScrollPosition { get }     static var Left: UICollectionViewScrollPosition { get }     static var CenteredHorizontally: UICollectionViewScrollPosition { get }     static var Right: UICollectionViewScrollPosition { get } } ``` |
| To | ``` struct UICollectionViewScrollPosition : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: UICollectionViewScrollPosition { get }     static var Top: UICollectionViewScrollPosition { get }     static var CenteredVertically: UICollectionViewScrollPosition { get }     static var Bottom: UICollectionViewScrollPosition { get }     static var Left: UICollectionViewScrollPosition { get }     static var CenteredHorizontally: UICollectionViewScrollPosition { get }     static var Right: UICollectionViewScrollPosition { get } } ``` |

Modified UICollectionViewScrollPosition.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UICollectionViewTransitionLayout

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollectionViewUpdateItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UICollisionBehavior

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UICollisionBehavior.init(items: [AnyObject])

|  | Declaration |
| --- | --- |
| From | ``` init(items items: [AnyObject]) ``` |
| To | ``` init!(items items: [AnyObject]) ``` |

Modified UICollisionBehaviorMode [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct UICollisionBehaviorMode : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Items: UICollisionBehaviorMode { get }     static var Boundaries: UICollisionBehaviorMode { get }     static var Everything: UICollisionBehaviorMode { get } } ``` | iOS 8.0 |
| To | ``` struct UICollisionBehaviorMode : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Items: UICollisionBehaviorMode { get }     static var Boundaries: UICollisionBehaviorMode { get }     static var Everything: UICollisionBehaviorMode { get } } ``` | iOS 7.0 |

Modified UICollisionBehaviorMode.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIColor.CIColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIColor.init(CIColor: CIColor)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIColor.getHue(UnsafeMutablePointer<CGFloat>, saturation: UnsafeMutablePointer<CGFloat>, brightness: UnsafeMutablePointer<CGFloat>, alpha: UnsafeMutablePointer<CGFloat>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIColor.getRed(UnsafeMutablePointer<CGFloat>, green: UnsafeMutablePointer<CGFloat>, blue: UnsafeMutablePointer<CGFloat>, alpha: UnsafeMutablePointer<CGFloat>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIColor.getWhite(UnsafeMutablePointer<CGFloat>, alpha: UnsafeMutablePointer<CGFloat>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIControl

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIControlEvents [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIControlEvents : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var TouchDown: UIControlEvents { get }     static var TouchDownRepeat: UIControlEvents { get }     static var TouchDragInside: UIControlEvents { get }     static var TouchDragOutside: UIControlEvents { get }     static var TouchDragEnter: UIControlEvents { get }     static var TouchDragExit: UIControlEvents { get }     static var TouchUpInside: UIControlEvents { get }     static var TouchUpOutside: UIControlEvents { get }     static var TouchCancel: UIControlEvents { get }     static var ValueChanged: UIControlEvents { get }     static var EditingDidBegin: UIControlEvents { get }     static var EditingChanged: UIControlEvents { get }     static var EditingDidEnd: UIControlEvents { get }     static var EditingDidEndOnExit: UIControlEvents { get }     static var AllTouchEvents: UIControlEvents { get }     static var AllEditingEvents: UIControlEvents { get }     static var ApplicationReserved: UIControlEvents { get }     static var SystemReserved: UIControlEvents { get }     static var AllEvents: UIControlEvents { get } } ``` |
| To | ``` struct UIControlEvents : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var TouchDown: UIControlEvents { get }     static var TouchDownRepeat: UIControlEvents { get }     static var TouchDragInside: UIControlEvents { get }     static var TouchDragOutside: UIControlEvents { get }     static var TouchDragEnter: UIControlEvents { get }     static var TouchDragExit: UIControlEvents { get }     static var TouchUpInside: UIControlEvents { get }     static var TouchUpOutside: UIControlEvents { get }     static var TouchCancel: UIControlEvents { get }     static var ValueChanged: UIControlEvents { get }     static var EditingDidBegin: UIControlEvents { get }     static var EditingChanged: UIControlEvents { get }     static var EditingDidEnd: UIControlEvents { get }     static var EditingDidEndOnExit: UIControlEvents { get }     static var AllTouchEvents: UIControlEvents { get }     static var AllEditingEvents: UIControlEvents { get }     static var ApplicationReserved: UIControlEvents { get }     static var SystemReserved: UIControlEvents { get }     static var AllEvents: UIControlEvents { get } } ``` |

Modified UIControlEvents.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIControlState [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIControlState : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Normal: UIControlState { get }     static var Highlighted: UIControlState { get }     static var Disabled: UIControlState { get }     static var Selected: UIControlState { get }     static var Application: UIControlState { get }     static var Reserved: UIControlState { get } } ``` |
| To | ``` struct UIControlState : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Normal: UIControlState { get }     static var Highlighted: UIControlState { get }     static var Disabled: UIControlState { get }     static var Selected: UIControlState { get }     static var Application: UIControlState { get }     static var Reserved: UIControlState { get } } ``` |

Modified UIControlState.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIDataDetectorTypes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIDataDetectorTypes : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var PhoneNumber: UIDataDetectorTypes { get }     static var Link: UIDataDetectorTypes { get }     static var Address: UIDataDetectorTypes { get }     static var CalendarEvent: UIDataDetectorTypes { get }     static var None: UIDataDetectorTypes { get }     static var All: UIDataDetectorTypes { get } } ``` |
| To | ``` struct UIDataDetectorTypes : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PhoneNumber: UIDataDetectorTypes { get }     static var Link: UIDataDetectorTypes { get }     static var Address: UIDataDetectorTypes { get }     static var CalendarEvent: UIDataDetectorTypes { get }     static var None: UIDataDetectorTypes { get }     static var All: UIDataDetectorTypes { get } } ``` |

Modified UIDataDetectorTypes.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIDatePicker

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIDevice

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIDevice.batteryLevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIDevice.batteryMonitoringEnabled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIDevice.batteryState

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIDevice.identifierForVendor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIDevice.multitaskingSupported

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIDevice.playInputClick()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UIDevice.proximityMonitoringEnabled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIDevice.proximityState

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIDevice.userInterfaceIdiom

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIDictationPhrase

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.1 |

Modified UIDocument

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIDocumentInteractionController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIDocumentMenuViewController.init(URL: NSURL, inMode: UIDocumentPickerMode)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL, inMode mode: UIDocumentPickerMode) ``` |
| To | ``` init!(URL url: NSURL, inMode mode: UIDocumentPickerMode) ``` |

Modified UIDocumentMenuViewController.init(documentTypes: [AnyObject], inMode: UIDocumentPickerMode)

|  | Declaration |
| --- | --- |
| From | ``` init(documentTypes allowedUTIs: [AnyObject], inMode mode: UIDocumentPickerMode) ``` |
| To | ``` init!(documentTypes allowedUTIs: [AnyObject], inMode mode: UIDocumentPickerMode) ``` |

Modified UIDocumentState [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIDocumentState : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Normal: UIDocumentState { get }     static var Closed: UIDocumentState { get }     static var InConflict: UIDocumentState { get }     static var SavingError: UIDocumentState { get }     static var EditingDisabled: UIDocumentState { get } } ``` |
| To | ``` struct UIDocumentState : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Normal: UIDocumentState { get }     static var Closed: UIDocumentState { get }     static var InConflict: UIDocumentState { get }     static var SavingError: UIDocumentState { get }     static var EditingDisabled: UIDocumentState { get } } ``` |

Modified UIDocumentState.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIDynamicAnimator

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIDynamicBehavior

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIDynamicItemBehavior

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIEvent.subtype

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIEvent.touchesForGestureRecognizer(UIGestureRecognizer) -> NSSet?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIEvent.type

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIFont

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIFont.fontDescriptor() -> UIFontDescriptor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFont.lineHeight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIFont.init(name: String, size: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` init(name fontName: String, size fontSize: CGFloat) -> UIFont ``` |
| To | ``` init?(name fontName: String, size fontSize: CGFloat) -> UIFont ``` |

Modified UIFont.preferredFontForTextStyle(String) -> UIFont [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptor.init(fontAttributes: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(fontAttributes attributes: [NSObject : AnyObject]!) -> UIFontDescriptor ``` |
| To | ``` init!(fontAttributes attributes: [NSObject : AnyObject]!) -> UIFontDescriptor ``` |

Modified UIFontDescriptor.init(fontAttributes: [NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(fontAttributes attributes: [NSObject : AnyObject]?) ``` |
| To | ``` init!(fontAttributes attributes: [NSObject : AnyObject]?) ``` |

Modified UIFontDescriptorSymbolicTraits [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct UIFontDescriptorSymbolicTraits : RawOptionSetType {     init(_ value: UInt32)     var value: UInt32     static var TraitItalic: UIFontDescriptorSymbolicTraits { get }     static var TraitBold: UIFontDescriptorSymbolicTraits { get }     static var TraitExpanded: UIFontDescriptorSymbolicTraits { get }     static var TraitCondensed: UIFontDescriptorSymbolicTraits { get }     static var TraitMonoSpace: UIFontDescriptorSymbolicTraits { get }     static var TraitVertical: UIFontDescriptorSymbolicTraits { get }     static var TraitUIOptimized: UIFontDescriptorSymbolicTraits { get }     static var TraitTightLeading: UIFontDescriptorSymbolicTraits { get }     static var TraitLooseLeading: UIFontDescriptorSymbolicTraits { get }     static var ClassMask: UIFontDescriptorSymbolicTraits { get }     static var ClassUnknown: UIFontDescriptorSymbolicTraits { get }     static var ClassOldStyleSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassTransitionalSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassModernSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassClarendonSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassSlabSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassFreeformSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassSansSerif: UIFontDescriptorSymbolicTraits { get }     static var ClassOrnamentals: UIFontDescriptorSymbolicTraits { get }     static var ClassScripts: UIFontDescriptorSymbolicTraits { get }     static var ClassSymbolic: UIFontDescriptorSymbolicTraits { get } } ``` | iOS 8.0 |
| To | ``` struct UIFontDescriptorSymbolicTraits : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var TraitItalic: UIFontDescriptorSymbolicTraits { get }     static var TraitBold: UIFontDescriptorSymbolicTraits { get }     static var TraitExpanded: UIFontDescriptorSymbolicTraits { get }     static var TraitCondensed: UIFontDescriptorSymbolicTraits { get }     static var TraitMonoSpace: UIFontDescriptorSymbolicTraits { get }     static var TraitVertical: UIFontDescriptorSymbolicTraits { get }     static var TraitUIOptimized: UIFontDescriptorSymbolicTraits { get }     static var TraitTightLeading: UIFontDescriptorSymbolicTraits { get }     static var TraitLooseLeading: UIFontDescriptorSymbolicTraits { get }     static var ClassMask: UIFontDescriptorSymbolicTraits { get }     static var ClassUnknown: UIFontDescriptorSymbolicTraits { get }     static var ClassOldStyleSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassTransitionalSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassModernSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassClarendonSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassSlabSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassFreeformSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassSansSerif: UIFontDescriptorSymbolicTraits { get }     static var ClassOrnamentals: UIFontDescriptorSymbolicTraits { get }     static var ClassScripts: UIFontDescriptorSymbolicTraits { get }     static var ClassSymbolic: UIFontDescriptorSymbolicTraits { get } } ``` | iOS 7.0 |

Modified UIFontDescriptorSymbolicTraits.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified UIGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIGestureRecognizerDelegate.gestureRecognizer(UIGestureRecognizer, shouldBeRequiredToFailByGestureRecognizer: UIGestureRecognizer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIGestureRecognizerDelegate.gestureRecognizer(UIGestureRecognizer, shouldRequireFailureOfGestureRecognizer: UIGestureRecognizer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIGravityBehavior

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIGuidedAccessRestrictionDelegate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIImage.init(CGImage: CGImage!)

|  | Declaration |
| --- | --- |
| From | ``` init(CGImage cgImage: CGImage!) ``` |
| To | ``` init?(CGImage cgImage: CGImage!) ``` |

Modified UIImage.init(CGImage: CGImage!, scale: CGFloat, orientation: UIImageOrientation)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CGImage cgImage: CGImage!, scale scale: CGFloat, orientation orientation: UIImageOrientation) ``` | iOS 8.0 |
| To | ``` init?(CGImage cgImage: CGImage!, scale scale: CGFloat, orientation orientation: UIImageOrientation) ``` | iOS 4.0 |

Modified UIImage.CIImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIImage.init(CIImage: CIImage)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CIImage ciImage: CIImage) ``` | iOS 8.0 |
| To | ``` init?(CIImage ciImage: CIImage) ``` | iOS 5.0 |

Modified UIImage.init(CIImage: CIImage, scale: CGFloat, orientation: UIImageOrientation)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) ``` | iOS 8.0 |
| To | ``` init?(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) ``` | iOS 6.0 |

Modified UIImage.alignmentRectInsets

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIImage.animatedImageNamed(String, duration: NSTimeInterval) -> UIImage! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIImage.animatedImageWithImages([AnyObject], duration: NSTimeInterval) -> UIImage! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIImage.animatedResizableImageNamed(String, capInsets: UIEdgeInsets, duration: NSTimeInterval) -> UIImage! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIImage.animatedResizableImageNamed(String, capInsets: UIEdgeInsets, resizingMode: UIImageResizingMode, duration: NSTimeInterval) -> UIImage! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIImage.capInsets

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIImage.init(contentsOfFile: String)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfFile path: String) ``` |
| To | ``` init?(contentsOfFile path: String) ``` |

Modified UIImage.init(data: NSData)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData) ``` |
| To | ``` init?(data data: NSData) ``` |

Modified UIImage.init(data: NSData, scale: CGFloat)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(data data: NSData, scale scale: CGFloat) ``` | iOS 8.0 |
| To | ``` init?(data data: NSData, scale scale: CGFloat) ``` | iOS 6.0 |

Modified UIImage.duration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIImage.imageWithAlignmentRectInsets(UIEdgeInsets) -> UIImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIImage.imageWithRenderingMode(UIImageRenderingMode) -> UIImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIImage.images

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIImage.init(named: String)

|  | Declaration |
| --- | --- |
| From | ``` init(named name: String) -> UIImage ``` |
| To | ``` init?(named name: String) -> UIImage ``` |

Modified UIImage.init(named: String, inBundle: NSBundle?, compatibleWithTraitCollection: UITraitCollection?)

|  | Declaration |
| --- | --- |
| From | ``` init(named name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?) -> UIImage ``` |
| To | ``` init?(named name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?) -> UIImage ``` |

Modified UIImage.renderingMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIImage.resizableImageWithCapInsets(UIEdgeInsets) -> UIImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIImage.resizableImageWithCapInsets(UIEdgeInsets, resizingMode: UIImageResizingMode) -> UIImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIImage.resizingMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIImage.scale

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIImagePickerController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIImagePickerController.allowsEditing

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIImagePickerController.availableCaptureModesForCameraDevice(UIImagePickerControllerCameraDevice) -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIImagePickerController.cameraCaptureMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIImagePickerController.cameraDevice

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIImagePickerController.cameraFlashMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIImagePickerController.cameraOverlayView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIImagePickerController.cameraViewTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIImagePickerController.isCameraDeviceAvailable(UIImagePickerControllerCameraDevice) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIImagePickerController.isFlashAvailableForCameraDevice(UIImagePickerControllerCameraDevice) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIImagePickerController.showsCameraControls

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIImagePickerController.startVideoCapture() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIImagePickerController.stopVideoCapture()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIImagePickerController.takePicture()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIImagePickerController.videoMaximumDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIImagePickerController.videoQuality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIImageRenderingMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIImageView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIImageView.highlighted

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIImageView.highlightedAnimationImages

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIImageView.highlightedImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIImageView.init(image: UIImage!, highlightedImage: UIImage?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIImageView.tintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIInputView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIInputViewStyle [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIInterfaceOrientationMask [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIInterfaceOrientationMask : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Portrait: UIInterfaceOrientationMask { get }     static var LandscapeLeft: UIInterfaceOrientationMask { get }     static var LandscapeRight: UIInterfaceOrientationMask { get }     static var PortraitUpsideDown: UIInterfaceOrientationMask { get }     static var Landscape: UIInterfaceOrientationMask { get }     static var All: UIInterfaceOrientationMask { get }     static var AllButUpsideDown: UIInterfaceOrientationMask { get } } ``` |
| To | ``` struct UIInterfaceOrientationMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Portrait: UIInterfaceOrientationMask { get }     static var LandscapeLeft: UIInterfaceOrientationMask { get }     static var LandscapeRight: UIInterfaceOrientationMask { get }     static var PortraitUpsideDown: UIInterfaceOrientationMask { get }     static var Landscape: UIInterfaceOrientationMask { get }     static var All: UIInterfaceOrientationMask { get }     static var AllButUpsideDown: UIInterfaceOrientationMask { get } } ``` |

Modified UIInterfaceOrientationMask.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIInterpolatingMotionEffect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIKeyCommand

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIKeyModifierFlags [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct UIKeyModifierFlags : RawOptionSetType {     init(_ value: Int)     var value: Int     static var AlphaShift: UIKeyModifierFlags { get }     static var Shift: UIKeyModifierFlags { get }     static var Control: UIKeyModifierFlags { get }     static var Alternate: UIKeyModifierFlags { get }     static var Command: UIKeyModifierFlags { get }     static var NumericPad: UIKeyModifierFlags { get } } ``` | iOS 8.0 |
| To | ``` struct UIKeyModifierFlags : RawOptionSetType {     init(_ rawValue: Int)     init(rawValue rawValue: Int)     static var AlphaShift: UIKeyModifierFlags { get }     static var Shift: UIKeyModifierFlags { get }     static var Control: UIKeyModifierFlags { get }     static var Alternate: UIKeyModifierFlags { get }     static var Command: UIKeyModifierFlags { get }     static var NumericPad: UIKeyModifierFlags { get } } ``` | iOS 7.0 |

Modified UIKeyModifierFlags.init(_: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: Int) ``` |
| To | ``` init(_ rawValue: Int) ``` |

Modified UILabel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UILabel.attributedText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UILabel.font

|  | Declaration |
| --- | --- |
| From | ``` var font: UIFont ``` |
| To | ``` var font: UIFont! ``` |

Modified UILabel.minimumScaleFactor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UILabel.preferredMaxLayoutWidth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UILabel.textColor

|  | Declaration |
| --- | --- |
| From | ``` var textColor: UIColor ``` |
| To | ``` var textColor: UIColor! ``` |

Modified UILocalNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UILocalizedIndexedCollation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UILongPressGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIManagedDocument

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIMarkupTextPrintFormatter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UIMarkupTextPrintFormatter.init(markupText: String?)

|  | Declaration |
| --- | --- |
| From | ``` init(markupText markupText: String?) ``` |
| To | ``` init!(markupText markupText: String?) ``` |

Modified UIMenuController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIMenuController.arrowDirection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIMenuController.menuItems

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIMenuItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIMotionEffect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIMotionEffectGroup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationBar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UINavigationBar.backIndicatorImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationBar.backIndicatorTransitionMaskImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationBar.backgroundImageForBarMetrics(UIBarMetrics) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINavigationBar.backgroundImageForBarPosition(UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationBar.barTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationBar.setBackgroundImage(UIImage!, forBarMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINavigationBar.setBackgroundImage(UIImage?, forBarPosition: UIBarPosition, barMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationBar.setTitleVerticalPositionAdjustment(CGFloat, forBarMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINavigationBar.shadowImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UINavigationBar.titleTextAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINavigationBar.titleVerticalPositionAdjustmentForBarMetrics(UIBarMetrics) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINavigationBar.translucent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UINavigationController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UINavigationController.interactivePopGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationController.init(navigationBarClass: AnyClass!, toolbarClass: AnyClass!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINavigationController.setToolbarHidden(Bool, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UINavigationController.setViewControllers([AnyObject]!, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UINavigationController.toolbar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UINavigationController.toolbarHidden

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UINavigationControllerDelegate.navigationController(UINavigationController, animationControllerForOperation: UINavigationControllerOperation, fromViewController: UIViewController, toViewController: UIViewController) -> UIViewControllerAnimatedTransitioning?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationControllerDelegate.navigationController(UINavigationController, interactionControllerForAnimationController: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationControllerDelegate.navigationControllerPreferredInterfaceOrientationForPresentation(UINavigationController) -> UIInterfaceOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationControllerDelegate.navigationControllerSupportedInterfaceOrientations(UINavigationController) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UINavigationItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UINavigationItem.leftBarButtonItems

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINavigationItem.leftItemsSupplementBackButton

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINavigationItem.rightBarButtonItems

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINavigationItem.setLeftBarButtonItems([AnyObject]?, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINavigationItem.setRightBarButtonItems([AnyObject]?, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UINib

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIPageControl

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIPageControl.currentPageIndicatorTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIPageControl.pageIndicatorTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIPageViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIPageViewControllerDataSource.presentationCountForPageViewController(UIPageViewController) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIPageViewControllerDataSource.presentationIndexForPageViewController(UIPageViewController) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIPageViewControllerDelegate.pageViewController(UIPageViewController, willTransitionToViewControllers:[AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIPageViewControllerDelegate.pageViewControllerPreferredInterfaceOrientationForPresentation(UIPageViewController) -> UIInterfaceOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIPageViewControllerDelegate.pageViewControllerSupportedInterfaceOrientations(UIPageViewController) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIPanGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIPasteboard

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIPasteboard.init(name: String!, create: Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(name pasteboardName: String!, create create: Bool) -> UIPasteboard ``` |
| To | ``` init!(name pasteboardName: String!, create create: Bool) -> UIPasteboard ``` |

Modified UIPercentDrivenInteractiveTransition

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIPickerView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIPickerViewDelegate.pickerView(UIPickerView, attributedTitleForRow: Int, forComponent: Int) -> NSAttributedString?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIPinchGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIPopoverArrowDirection [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIPopoverArrowDirection : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Up: UIPopoverArrowDirection { get }     static var Down: UIPopoverArrowDirection { get }     static var Left: UIPopoverArrowDirection { get }     static var Right: UIPopoverArrowDirection { get }     static var Any: UIPopoverArrowDirection { get }     static var Unknown: UIPopoverArrowDirection { get } } ``` |
| To | ``` struct UIPopoverArrowDirection : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Up: UIPopoverArrowDirection { get }     static var Down: UIPopoverArrowDirection { get }     static var Left: UIPopoverArrowDirection { get }     static var Right: UIPopoverArrowDirection { get }     static var Any: UIPopoverArrowDirection { get }     static var Unknown: UIPopoverArrowDirection { get } } ``` |

Modified UIPopoverArrowDirection.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIPopoverBackgroundView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIPopoverBackgroundView.wantsDefaultContentAppearance() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIPopoverController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIPopoverController.backgroundColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIPopoverController.popoverBackgroundViewClass

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIPopoverController.popoverLayoutMargins

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIPopoverControllerDelegate.popoverController(UIPopoverController, willRepositionPopoverToRect: UnsafeMutablePointer<CGRect>, inView: AutoreleasingUnsafeMutablePointer<UIView?>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIPrintFormatter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UIPrintInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UIPrintInfo.init(dictionary: [NSObject: AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` init(dictionary dictionary: [NSObject : AnyObject]?) -> UIPrintInfo ``` |
| To | ``` init!(dictionary dictionary: [NSObject : AnyObject]?) -> UIPrintInfo ``` |

Modified UIPrintInteractionController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UIPrintInteractionController.showsNumberOfCopies

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIPrintInteractionControllerDelegate.printInteractionController(UIPrintInteractionController, cutLengthForPaper: UIPrintPaper) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIPrintPageRenderer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UIPrintPaper

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UIPrinterJobTypes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIPrinterJobTypes : RawOptionSetType {     init(_ value: Int)     var value: Int     static var Unknown: UIPrinterJobTypes { get }     static var Document: UIPrinterJobTypes { get }     static var Envelope: UIPrinterJobTypes { get }     static var Label: UIPrinterJobTypes { get }     static var Photo: UIPrinterJobTypes { get }     static var Receipt: UIPrinterJobTypes { get }     static var Roll: UIPrinterJobTypes { get }     static var LargeFormat: UIPrinterJobTypes { get }     static var Postcard: UIPrinterJobTypes { get } } ``` |
| To | ``` struct UIPrinterJobTypes : RawOptionSetType {     init(_ rawValue: Int)     init(rawValue rawValue: Int)     static var Unknown: UIPrinterJobTypes { get }     static var Document: UIPrinterJobTypes { get }     static var Envelope: UIPrinterJobTypes { get }     static var Label: UIPrinterJobTypes { get }     static var Photo: UIPrinterJobTypes { get }     static var Receipt: UIPrinterJobTypes { get }     static var Roll: UIPrinterJobTypes { get }     static var LargeFormat: UIPrinterJobTypes { get }     static var Postcard: UIPrinterJobTypes { get } } ``` |

Modified UIPrinterJobTypes.init(_: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: Int) ``` |
| To | ``` init(_ rawValue: Int) ``` |

Modified UIPrinterPickerController.init(initiallySelectedPrinter: UIPrinter!)

|  | Declaration |
| --- | --- |
| From | ``` init(initiallySelectedPrinter printer: UIPrinter!) -> UIPrinterPickerController ``` |
| To | ``` init!(initiallySelectedPrinter printer: UIPrinter!) -> UIPrinterPickerController ``` |

Modified UIProgressView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIProgressView.progressImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIProgressView.progressTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIProgressView.setProgress(Float, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIProgressView.trackImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIProgressView.trackTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIPushBehavior

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIPushBehavior.init(items: [AnyObject]!, mode: UIPushBehaviorMode)

|  | Declaration |
| --- | --- |
| From | ``` init(items items: [AnyObject]!, mode mode: UIPushBehaviorMode) ``` |
| To | ``` init!(items items: [AnyObject]!, mode mode: UIPushBehaviorMode) ``` |

Modified UIPushBehaviorMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIRectCorner [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIRectCorner : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var TopLeft: UIRectCorner { get }     static var TopRight: UIRectCorner { get }     static var BottomLeft: UIRectCorner { get }     static var BottomRight: UIRectCorner { get }     static var AllCorners: UIRectCorner { get } } ``` |
| To | ``` struct UIRectCorner : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var TopLeft: UIRectCorner { get }     static var TopRight: UIRectCorner { get }     static var BottomLeft: UIRectCorner { get }     static var BottomRight: UIRectCorner { get }     static var AllCorners: UIRectCorner { get } } ``` |

Modified UIRectCorner.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIRectEdge [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct UIRectEdge : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: UIRectEdge { get }     static var Top: UIRectEdge { get }     static var Left: UIRectEdge { get }     static var Bottom: UIRectEdge { get }     static var Right: UIRectEdge { get }     static var All: UIRectEdge { get } } ``` | iOS 8.0 |
| To | ``` struct UIRectEdge : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: UIRectEdge { get }     static var Top: UIRectEdge { get }     static var Left: UIRectEdge { get }     static var Bottom: UIRectEdge { get }     static var Right: UIRectEdge { get }     static var All: UIRectEdge { get } } ``` | iOS 7.0 |

Modified UIRectEdge.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIReferenceLibraryViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIRefreshControl

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIRefreshControl.beginRefreshing()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIRefreshControl.endRefreshing()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIRemoteNotificationType [struct]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` struct UIRemoteNotificationType : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: UIRemoteNotificationType { get }     static var Badge: UIRemoteNotificationType { get }     static var Sound: UIRemoteNotificationType { get }     static var Alert: UIRemoteNotificationType { get }     static var NewsstandContentAvailability: UIRemoteNotificationType { get } } ``` | iOS 8.0 | -- |
| To | ``` struct UIRemoteNotificationType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: UIRemoteNotificationType { get }     static var Badge: UIRemoteNotificationType { get }     static var Sound: UIRemoteNotificationType { get }     static var Alert: UIRemoteNotificationType { get }     static var NewsstandContentAvailability: UIRemoteNotificationType { get } } ``` | iOS 3.0 | iOS 8.0 |

Modified UIRemoteNotificationType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIResponder

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIResponder.canPerformAction(Selector, withSender: AnyObject?) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIResponder.clearTextInputContextIdentifier(String) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIResponder.inputAccessoryView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIResponder.inputView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIResponder.keyCommands

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIResponder.motionBegan(UIEventSubtype, withEvent: UIEvent)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIResponder.motionCancelled(UIEventSubtype, withEvent: UIEvent)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIResponder.motionEnded(UIEventSubtype, withEvent: UIEvent)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIResponder.reloadInputViews()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIResponder.remoteControlReceivedWithEvent(UIEvent)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIResponder.targetForAction(Selector, withSender: AnyObject?) -> AnyObject?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIResponder.textInputContextIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIResponder.textInputMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIResponder.undoManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIRotationGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIScreen

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIScreen.availableModes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIScreen.brightness

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIScreen.currentMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIScreen.displayLinkWithTarget(AnyObject!, selector: Selector) -> CADisplayLink!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIScreen.mirroredScreen

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified UIScreen.overscanCompensation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIScreen.preferredMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified UIScreen.scale

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIScreen.screens() -> [AnyObject] [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIScreen.snapshotViewAfterScreenUpdates(Bool) -> UIView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIScreen.wantsSoftwareDimming

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIScreenEdgePanGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIScreenMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIScrollView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIScrollView.decelerationRate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIScrollView.keyboardDismissMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIScrollView.panGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIScrollView.pinchGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIScrollView.setZoomScale(CGFloat, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIScrollView.zoomScale

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIScrollView.zoomToRect(CGRect, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIScrollViewDelegate.scrollViewDidZoom(UIScrollView)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIScrollViewDelegate.scrollViewWillBeginZooming(UIScrollView, withView: UIView!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIScrollViewDelegate.scrollViewWillEndDragging(UIScrollView, withVelocity: CGPoint, targetContentOffset: UnsafeMutablePointer<CGPoint>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIScrollViewKeyboardDismissMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISearchBar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UISearchBar.backgroundImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.backgroundImageForBarPosition(UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISearchBar.barTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISearchBar.imageForSearchBarIcon(UISearchBarIcon, state: UIControlState) -> UIImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.positionAdjustmentForSearchBarIcon(UISearchBarIcon) -> UIOffset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.scopeBarBackgroundImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.scopeBarButtonBackgroundImageForState(UIControlState) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.scopeBarButtonDividerImageForLeftSegmentState(UIControlState, rightSegmentState: UIControlState) -> UIImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.scopeBarButtonTitleTextAttributesForState(UIControlState) -> [NSObject: AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.scopeButtonTitles

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UISearchBar.searchBarStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISearchBar.searchFieldBackgroundImageForState(UIControlState) -> UIImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.searchFieldBackgroundPositionAdjustment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.searchResultsButtonSelected

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UISearchBar.searchTextPositionAdjustment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.selectedScopeButtonIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UISearchBar.setBackgroundImage(UIImage?, forBarPosition: UIBarPosition, barMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISearchBar.setImage(UIImage?, forSearchBarIcon: UISearchBarIcon, state: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.setPositionAdjustment(UIOffset, forSearchBarIcon: UISearchBarIcon)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.setScopeBarButtonBackgroundImage(UIImage?, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.setScopeBarButtonDividerImage(UIImage?, forLeftSegmentState: UIControlState, rightSegmentState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.setScopeBarButtonTitleTextAttributes([NSObject: AnyObject]?, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.setSearchFieldBackgroundImage(UIImage?, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchBar.setShowsCancelButton(Bool, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UISearchBar.showsScopeBar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UISearchBar.showsSearchResultsButton

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UISearchBar.translucent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UISearchBarDelegate.searchBar(UISearchBar, selectedScopeButtonIndexDidChange: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UISearchBarDelegate.searchBar(UISearchBar, shouldChangeTextInRange: NSRange, replacementText: String) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UISearchBarDelegate.searchBarResultsListButtonClicked(UISearchBar)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UISearchBarStyle [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISearchDisplayController

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayController.displaysSearchBarInNavigationBar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISearchDisplayController.navigationItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISearchDisplayController.searchResultsTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISearchDisplayDelegate.searchDisplayController(UISearchDisplayController, didHideSearchResultsTableView: UITableView)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayController(UISearchDisplayController, didLoadSearchResultsTableView: UITableView)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayController(UISearchDisplayController, didShowSearchResultsTableView: UITableView)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayController(UISearchDisplayController, shouldReloadTableForSearchScope: Int) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayController(UISearchDisplayController, shouldReloadTableForSearchString: String!) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayController(UISearchDisplayController, willHideSearchResultsTableView: UITableView)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayController(UISearchDisplayController, willShowSearchResultsTableView: UITableView)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayController(UISearchDisplayController, willUnloadSearchResultsTableView: UITableView)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayControllerDidBeginSearch(UISearchDisplayController)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayControllerDidEndSearch(UISearchDisplayController)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayControllerWillBeginSearch(UISearchDisplayController)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISearchDisplayDelegate.searchDisplayControllerWillEndSearch(UISearchDisplayController)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UISegmentedControl

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UISegmentedControl.apportionsSegmentWidthsByContent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISegmentedControl.backgroundImageForState(UIControlState, barMetrics: UIBarMetrics) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISegmentedControl.contentPositionAdjustmentForSegmentType(UISegmentedControlSegment, barMetrics: UIBarMetrics) -> UIOffset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISegmentedControl.dividerImageForLeftSegmentState(UIControlState, rightSegmentState: UIControlState, barMetrics: UIBarMetrics) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISegmentedControl.setBackgroundImage(UIImage?, forState: UIControlState, barMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISegmentedControl.setContentPositionAdjustment(UIOffset, forSegmentType: UISegmentedControlSegment, barMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISegmentedControl.setDividerImage(UIImage?, forLeftSegmentState: UIControlState, rightSegmentState: UIControlState, barMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISegmentedControl.setTitleTextAttributes([NSObject: AnyObject]?, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISegmentedControl.titleTextAttributesForState(UIControlState) -> [NSObject: AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISimpleTextPrintFormatter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UISimpleTextPrintFormatter.attributedText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISimpleTextPrintFormatter.init(attributedText: NSAttributedString?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISlider

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UISlider.maximumTrackTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISlider.minimumTrackTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISlider.thumbTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISnapBehavior

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISnapBehavior.init(item: UIDynamicItem, snapToPoint: CGPoint)

|  | Declaration |
| --- | --- |
| From | ``` init(item item: UIDynamicItem, snapToPoint point: CGPoint) ``` |
| To | ``` init!(item item: UIDynamicItem, snapToPoint point: CGPoint) ``` |

Modified UISplitViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UISplitViewController.presentsWithGesture

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.1 |

Modified UISplitViewControllerDelegate.splitViewController(UISplitViewController, popoverController: UIPopoverController, willPresentViewController: UIViewController)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified UISplitViewControllerDelegate.splitViewController(UISplitViewController, shouldHideViewController: UIViewController, inOrientation: UIInterfaceOrientation) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified UISplitViewControllerDelegate.splitViewController(UISplitViewController, willHideViewController: UIViewController, withBarButtonItem: UIBarButtonItem, forPopoverController: UIPopoverController)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified UISplitViewControllerDelegate.splitViewController(UISplitViewController, willShowViewController: UIViewController, invalidatingBarButtonItem: UIBarButtonItem)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified UISplitViewControllerDelegate.splitViewControllerPreferredInterfaceOrientationForPresentation(UISplitViewController) -> UIInterfaceOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UISplitViewControllerDelegate.splitViewControllerSupportedInterfaceOrientations(UISplitViewController) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIStepper

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIStepper.backgroundImageForState(UIControlState) -> UIImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIStepper.decrementImageForState(UIControlState) -> UIImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIStepper.dividerImageForLeftSegmentState(UIControlState, rightSegmentState: UIControlState) -> UIImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIStepper.incrementImageForState(UIControlState) -> UIImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIStepper.setBackgroundImage(UIImage?, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIStepper.setDecrementImage(UIImage?, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIStepper.setDividerImage(UIImage?, forLeftSegmentState: UIControlState, rightSegmentState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIStepper.setIncrementImage(UIImage?, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIStepper.tintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIStoryboard

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIStoryboardPopoverSegue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIStoryboardSegue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIStoryboardSegue.identifier

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String { get } ``` |
| To | ``` var identifier: String? { get } ``` |

Modified UIStoryboardSegue.init(identifier: String!, source: UIViewController, destination: UIViewController)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier identifier: String!, source source: UIViewController, destination destination: UIViewController) ``` |
| To | ``` init!(identifier identifier: String!, source source: UIViewController, destination destination: UIViewController) ``` |

Modified UISwipeGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UISwipeGestureRecognizerDirection [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UISwipeGestureRecognizerDirection : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Right: UISwipeGestureRecognizerDirection { get }     static var Left: UISwipeGestureRecognizerDirection { get }     static var Up: UISwipeGestureRecognizerDirection { get }     static var Down: UISwipeGestureRecognizerDirection { get } } ``` |
| To | ``` struct UISwipeGestureRecognizerDirection : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Right: UISwipeGestureRecognizerDirection { get }     static var Left: UISwipeGestureRecognizerDirection { get }     static var Up: UISwipeGestureRecognizerDirection { get }     static var Down: UISwipeGestureRecognizerDirection { get } } ``` |

Modified UISwipeGestureRecognizerDirection.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UISwitch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UISwitch.offImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UISwitch.onImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UISwitch.onTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UISwitch.thumbTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UISwitch.tintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UISystemAnimation [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UITabBar.backgroundImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITabBar.barStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBar.barTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBar.itemPositioning

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBar.itemSpacing

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBar.itemWidth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBar.selectedImageTintColor

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified UITabBar.selectionIndicatorImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITabBar.shadowImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITabBar.tintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITabBar.translucent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBarController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UITabBarController.tabBar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITabBarControllerDelegate.tabBarController(UITabBarController, animationControllerForTransitionFromViewController: UIViewController, toViewController: UIViewController) -> UIViewControllerAnimatedTransitioning?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBarControllerDelegate.tabBarController(UITabBarController, interactionControllerForAnimationController: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBarControllerDelegate.tabBarController(UITabBarController, shouldSelectViewController: UIViewController) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITabBarControllerDelegate.tabBarController(UITabBarController, willBeginCustomizingViewControllers:[AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITabBarControllerDelegate.tabBarController(UITabBarController, willEndCustomizingViewControllers:[AnyObject], changed: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITabBarControllerDelegate.tabBarControllerPreferredInterfaceOrientationForPresentation(UITabBarController) -> UIInterfaceOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBarControllerDelegate.tabBarControllerSupportedInterfaceOrientations(UITabBarController) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBarItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UITabBarItem.selectedImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBarItem.setTitlePositionAdjustment(UIOffset)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITabBarItem.init(title: String?, image: UIImage?, selectedImage: UIImage?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITabBarItem.titlePositionAdjustment() -> UIOffset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITabBarItemPositioning [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UITableView.allowsMultipleSelection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableView.allowsMultipleSelectionDuringEditing

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableView.allowsSelection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableView.backgroundView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UITableView.dequeueReusableCellWithIdentifier(String, forIndexPath: NSIndexPath) -> AnyObject

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableView.dequeueReusableHeaderFooterViewWithIdentifier(String) -> AnyObject?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableView.estimatedRowHeight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableView.estimatedSectionFooterHeight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableView.estimatedSectionHeaderHeight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableView.footerViewForSection(Int) -> UITableViewHeaderFooterView?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableView.headerViewForSection(Int) -> UITableViewHeaderFooterView?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableView.indexPathsForSelectedRows() -> [AnyObject]?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableView.moveRowAtIndexPath(NSIndexPath, toIndexPath: NSIndexPath)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableView.moveSection(Int, toSection: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableView.registerClass(AnyClass, forCellReuseIdentifier: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableView.registerClass(AnyClass, forHeaderFooterViewReuseIdentifier: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableView.registerNib(UINib, forCellReuseIdentifier: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableView.registerNib(UINib, forHeaderFooterViewReuseIdentifier: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableView.reloadRowsAtIndexPaths([AnyObject], withRowAnimation: UITableViewRowAnimation)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableView.reloadSectionIndexTitles()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableView.reloadSections(NSIndexSet, withRowAnimation: UITableViewRowAnimation)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableView.sectionIndexBackgroundColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableView.sectionIndexColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableView.sectionIndexTrackingBackgroundColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableView.selectRowAtIndexPath(NSIndexPath?, animated: Bool, scrollPosition: UITableViewScrollPosition)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func selectRowAtIndexPath(_ indexPath: NSIndexPath, animated animated: Bool, scrollPosition scrollPosition: UITableViewScrollPosition) ``` | iOS 8.0 |
| To | ``` func selectRowAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool, scrollPosition scrollPosition: UITableViewScrollPosition) ``` | iOS 8.1 |

Modified UITableView.separatorInset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableViewCell

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UITableViewCell.detailTextLabel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableViewCell.didTransitionToState(UITableViewCellStateMask)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableViewCell.imageView

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var imageView: UIImageView? { get } ``` | iOS 8.0 |
| To | ``` var imageView: UIImageView { get } ``` | iOS 3.0 |

Modified UITableViewCell.multipleSelectionBackgroundView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableViewCell.separatorInset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableViewCell.init(style: UITableViewCellStyle, reuseIdentifier: String?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableViewCell.textLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var textLabel: UILabel? { get } ``` | iOS 8.0 |
| To | ``` var textLabel: UILabel { get } ``` | iOS 3.0 |

Modified UITableViewCell.willTransitionToState(UITableViewCellStateMask)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableViewCellStateMask [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UITableViewCellStateMask : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var DefaultMask: UITableViewCellStateMask { get }     static var ShowingEditControlMask: UITableViewCellStateMask { get }     static var ShowingDeleteConfirmationMask: UITableViewCellStateMask { get } } ``` |
| To | ``` struct UITableViewCellStateMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var DefaultMask: UITableViewCellStateMask { get }     static var ShowingEditControlMask: UITableViewCellStateMask { get }     static var ShowingDeleteConfirmationMask: UITableViewCellStateMask { get } } ``` |

Modified UITableViewCellStateMask.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UITableViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UITableViewController.clearsSelectionOnViewWillAppear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UITableViewController.refreshControl

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewDelegate.tableView(UITableView, canPerformAction: Selector, forRowAtIndexPath: NSIndexPath, withSender: AnyObject) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableViewDelegate.tableView(UITableView, didDeselectRowAtIndexPath: NSIndexPath)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableViewDelegate.tableView(UITableView, didEndDisplayingCell: UITableViewCell, forRowAtIndexPath: NSIndexPath)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewDelegate.tableView(UITableView, didEndDisplayingFooterView: UIView, forSection: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewDelegate.tableView(UITableView, didEndDisplayingHeaderView: UIView, forSection: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewDelegate.tableView(UITableView, didHighlightRowAtIndexPath: NSIndexPath)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewDelegate.tableView(UITableView, didUnhighlightRowAtIndexPath: NSIndexPath)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewDelegate.tableView(UITableView, estimatedHeightForFooterInSection: Int) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableViewDelegate.tableView(UITableView, estimatedHeightForHeaderInSection: Int) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableViewDelegate.tableView(UITableView, estimatedHeightForRowAtIndexPath: NSIndexPath) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITableViewDelegate.tableView(UITableView, performAction: Selector, forRowAtIndexPath: NSIndexPath, withSender: AnyObject!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableViewDelegate.tableView(UITableView, shouldHighlightRowAtIndexPath: NSIndexPath) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewDelegate.tableView(UITableView, shouldShowMenuForRowAtIndexPath: NSIndexPath) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableViewDelegate.tableView(UITableView, titleForDeleteConfirmationButtonForRowAtIndexPath: NSIndexPath) -> String!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableViewDelegate.tableView(UITableView, willDeselectRowAtIndexPath: NSIndexPath) -> NSIndexPath?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITableViewDelegate.tableView(UITableView, willDisplayFooterView: UIView, forSection: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewDelegate.tableView(UITableView, willDisplayHeaderView: UIView, forSection: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewHeaderFooterView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITapGestureRecognizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UITextChecker

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UITextField

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UITextField.allowsEditingTextAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextField.attributedPlaceholder

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextField.attributedText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextField.clearsOnInsertion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextField.defaultTextAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITextField.typingAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextInput.selectionRectsForRange(UITextRange) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextInput.shouldChangeTextInRange(UITextRange, replacementText: String) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextInputMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UITextInputStringTokenizer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UITextInputStringTokenizer.init(textInput: UIResponder)

|  | Declaration |
| --- | --- |
| From | ``` init(textInput textInput: UIResponder) ``` |
| To | ``` init!(textInput textInput: UIResponder) ``` |

Modified UITextInputTraits.spellCheckingType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITextPosition

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UITextRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UITextSelectionRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextSpellCheckingType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITextView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UITextView.allowsEditingTextAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextView.attributedText

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextView.clearsOnInsertion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextView.dataDetectorTypes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITextView.init(frame: CGRect, textContainer: NSTextContainer?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITextView.layoutManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITextView.linkTextAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITextView.selectable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITextView.textContainer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITextView.textContainerInset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITextView.textStorage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITextView.typingAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITextViewDelegate.textView(UITextView, shouldInteractWithTextAttachment: NSTextAttachment, inRange: NSRange) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITextViewDelegate.textView(UITextView, shouldInteractWithURL: NSURL, inRange: NSRange) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIToolbar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIToolbar.backgroundImageForToolbarPosition(UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIToolbar.barTintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIToolbar.delegate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIToolbar.setBackgroundImage(UIImage?, forToolbarPosition: UIBarPosition, barMetrics: UIBarMetrics)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIToolbar.setShadowImage(UIImage?, forToolbarPosition: UIBarPosition)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIToolbar.shadowImageForToolbarPosition(UIBarPosition) -> UIImage?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIToolbar.translucent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITouch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UITouch.gestureRecognizers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UITraitEnvironment.traitCollectionDidChange(UITraitCollection?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection) ``` | iOS 8.0 |
| To | ``` func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) ``` | iOS 8.1 |

Modified UIUserInterfaceLayoutDirection [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIUserNotificationType [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIUserNotificationType : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: UIUserNotificationType { get }     static var Badge: UIUserNotificationType { get }     static var Sound: UIUserNotificationType { get }     static var Alert: UIUserNotificationType { get } } ``` |
| To | ``` struct UIUserNotificationType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: UIUserNotificationType { get }     static var Badge: UIUserNotificationType { get }     static var Sound: UIUserNotificationType { get }     static var Alert: UIUserNotificationType { get } } ``` |

Modified UIUserNotificationType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIVideoEditorController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIVideoEditorController.canEditVideoAtPath(String) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIView.addConstraint(NSLayoutConstraint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.addConstraints([AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.addGestureRecognizer(UIGestureRecognizer)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIView.addKeyframeWithRelativeStartTime(Double, relativeDuration: Double, animations:() -> Void) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.addMotionEffect(UIMotionEffect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.alignmentRectForFrame(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.alignmentRectInsets() -> UIEdgeInsets

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.animateKeyframesWithDuration(NSTimeInterval, delay: NSTimeInterval, options: UIViewKeyframeAnimationOptions, animations:() -> Void, completion:((Bool) -> Void)?) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.animateWithDuration(NSTimeInterval, animations:() -> Void) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIView.animateWithDuration(NSTimeInterval, animations:() -> Void, completion:((Bool) -> Void)?) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIView.animateWithDuration(NSTimeInterval, delay: NSTimeInterval, options: UIViewAnimationOptions, animations:() -> Void, completion:((Bool) -> Void)?) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIView.animateWithDuration(NSTimeInterval, delay: NSTimeInterval, usingSpringWithDamping: CGFloat, initialSpringVelocity: CGFloat, options: UIViewAnimationOptions, animations:() -> Void, completion:((Bool) -> Void)?) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.constraints() -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.constraintsAffectingLayoutForAxis(UILayoutConstraintAxis) -> [AnyObject]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.contentCompressionResistancePriorityForAxis(UILayoutConstraintAxis) -> UILayoutPriority

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.contentHuggingPriorityForAxis(UILayoutConstraintAxis) -> UILayoutPriority

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.contentScaleFactor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIView.decodeRestorableStateWithCoder(NSCoder)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.drawViewHierarchyInRect(CGRect, afterScreenUpdates: Bool) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.encodeRestorableStateWithCoder(NSCoder)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.exerciseAmbiguityInLayout()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.frameForAlignmentRect(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.gestureRecognizers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIView.hasAmbiguousLayout() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.intrinsicContentSize() -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.invalidateIntrinsicContentSize()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.motionEffects

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.needsUpdateConstraints() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.performSystemAnimation(UISystemAnimation, onViews:[AnyObject], options: UIViewAnimationOptions, animations:(() -> Void)?, completion:((Bool) -> Void)?) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.performWithoutAnimation(() -> Void) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.removeConstraint(NSLayoutConstraint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.removeConstraints([AnyObject])

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.removeGestureRecognizer(UIGestureRecognizer)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIView.removeMotionEffect(UIMotionEffect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.requiresConstraintBasedLayout() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.resizableSnapshotViewFromRect(CGRect, afterScreenUpdates: Bool, withCapInsets: UIEdgeInsets) -> UIView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.restorationIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.setContentCompressionResistancePriority(UILayoutPriority, forAxis: UILayoutConstraintAxis)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.setContentHuggingPriority(UILayoutPriority, forAxis: UILayoutConstraintAxis)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.setNeedsUpdateConstraints()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.setTranslatesAutoresizingMaskIntoConstraints(Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.snapshotViewAfterScreenUpdates(Bool) -> UIView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.systemLayoutSizeFittingSize(CGSize) -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.tintAdjustmentMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.tintColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.tintColorDidChange()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIView.transitionFromView(UIView, toView: UIView, duration: NSTimeInterval, options: UIViewAnimationOptions, completion:((Bool) -> Void)?) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIView.transitionWithView(UIView, duration: NSTimeInterval, options: UIViewAnimationOptions, animations:() -> Void, completion:((Bool) -> Void)?) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIView.translatesAutoresizingMaskIntoConstraints() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.updateConstraints()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.updateConstraintsIfNeeded()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIView.viewForBaselineLayout() -> UIView?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewAnimationOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct UIViewAnimationOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var LayoutSubviews: UIViewAnimationOptions { get }     static var AllowUserInteraction: UIViewAnimationOptions { get }     static var BeginFromCurrentState: UIViewAnimationOptions { get }     static var Repeat: UIViewAnimationOptions { get }     static var Autoreverse: UIViewAnimationOptions { get }     static var OverrideInheritedDuration: UIViewAnimationOptions { get }     static var OverrideInheritedCurve: UIViewAnimationOptions { get }     static var AllowAnimatedContent: UIViewAnimationOptions { get }     static var ShowHideTransitionViews: UIViewAnimationOptions { get }     static var OverrideInheritedOptions: UIViewAnimationOptions { get }     static var CurveEaseInOut: UIViewAnimationOptions { get }     static var CurveEaseIn: UIViewAnimationOptions { get }     static var CurveEaseOut: UIViewAnimationOptions { get }     static var CurveLinear: UIViewAnimationOptions { get }     static var TransitionNone: UIViewAnimationOptions { get }     static var TransitionFlipFromLeft: UIViewAnimationOptions { get }     static var TransitionFlipFromRight: UIViewAnimationOptions { get }     static var TransitionCurlUp: UIViewAnimationOptions { get }     static var TransitionCurlDown: UIViewAnimationOptions { get }     static var TransitionCrossDissolve: UIViewAnimationOptions { get }     static var TransitionFlipFromTop: UIViewAnimationOptions { get }     static var TransitionFlipFromBottom: UIViewAnimationOptions { get } } ``` | iOS 8.0 |
| To | ``` struct UIViewAnimationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var LayoutSubviews: UIViewAnimationOptions { get }     static var AllowUserInteraction: UIViewAnimationOptions { get }     static var BeginFromCurrentState: UIViewAnimationOptions { get }     static var Repeat: UIViewAnimationOptions { get }     static var Autoreverse: UIViewAnimationOptions { get }     static var OverrideInheritedDuration: UIViewAnimationOptions { get }     static var OverrideInheritedCurve: UIViewAnimationOptions { get }     static var AllowAnimatedContent: UIViewAnimationOptions { get }     static var ShowHideTransitionViews: UIViewAnimationOptions { get }     static var OverrideInheritedOptions: UIViewAnimationOptions { get }     static var CurveEaseInOut: UIViewAnimationOptions { get }     static var CurveEaseIn: UIViewAnimationOptions { get }     static var CurveEaseOut: UIViewAnimationOptions { get }     static var CurveLinear: UIViewAnimationOptions { get }     static var TransitionNone: UIViewAnimationOptions { get }     static var TransitionFlipFromLeft: UIViewAnimationOptions { get }     static var TransitionFlipFromRight: UIViewAnimationOptions { get }     static var TransitionCurlUp: UIViewAnimationOptions { get }     static var TransitionCurlDown: UIViewAnimationOptions { get }     static var TransitionCrossDissolve: UIViewAnimationOptions { get }     static var TransitionFlipFromTop: UIViewAnimationOptions { get }     static var TransitionFlipFromBottom: UIViewAnimationOptions { get } } ``` | iOS 4.0 |

Modified UIViewAnimationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIViewAutoresizing [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UIViewAutoresizing : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: UIViewAutoresizing { get }     static var FlexibleLeftMargin: UIViewAutoresizing { get }     static var FlexibleWidth: UIViewAutoresizing { get }     static var FlexibleRightMargin: UIViewAutoresizing { get }     static var FlexibleTopMargin: UIViewAutoresizing { get }     static var FlexibleHeight: UIViewAutoresizing { get }     static var FlexibleBottomMargin: UIViewAutoresizing { get } } ``` |
| To | ``` struct UIViewAutoresizing : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: UIViewAutoresizing { get }     static var FlexibleLeftMargin: UIViewAutoresizing { get }     static var FlexibleWidth: UIViewAutoresizing { get }     static var FlexibleRightMargin: UIViewAutoresizing { get }     static var FlexibleTopMargin: UIViewAutoresizing { get }     static var FlexibleHeight: UIViewAutoresizing { get }     static var FlexibleBottomMargin: UIViewAutoresizing { get } } ``` |

Modified UIViewAutoresizing.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIViewController.addChildViewController(UIViewController)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.applicationFinishedRestoringState()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.attemptRotationToDeviceOrientation() [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.automaticallyAdjustsScrollViewInsets

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.beginAppearanceTransition(Bool, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.bottomLayoutGuide

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.canPerformUnwindSegueAction(Selector, fromViewController: UIViewController, withSender: AnyObject) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.childViewControllerForStatusBarHidden() -> UIViewController?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.childViewControllerForStatusBarStyle() -> UIViewController?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.childViewControllers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.decodeRestorableStateWithCoder(NSCoder)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.definesPresentationContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.didMoveToParentViewController(UIViewController?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.didRotateFromInterfaceOrientation(UIInterfaceOrientation)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified UIViewController.disablesAutomaticKeyboardDismissal() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified UIViewController.dismissViewControllerAnimated(Bool, completion:(() -> Void)?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.edgesForExtendedLayout

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.encodeRestorableStateWithCoder(NSCoder)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.endAppearanceTransition()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.extendedLayoutIncludesOpaqueBars

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.interfaceOrientation

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified UIViewController.isBeingDismissed() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.isBeingPresented() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.isMovingFromParentViewController() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.isMovingToParentViewController() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.isViewLoaded() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIViewController.modalInPopover

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIViewController.modalPresentationCapturesStatusBarAppearance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.modalPresentationStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIViewController.modalTransitionStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIViewController.performSegueWithIdentifier(String?, sender: AnyObject?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func performSegueWithIdentifier(_ identifier: String, sender sender: AnyObject?) ``` | iOS 8.0 |
| To | ``` func performSegueWithIdentifier(_ identifier: String?, sender sender: AnyObject?) ``` | iOS 5.0 |

Modified UIViewController.preferredContentSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.preferredInterfaceOrientationForPresentation() -> UIInterfaceOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.preferredStatusBarStyle() -> UIStatusBarStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.preferredStatusBarUpdateAnimation() -> UIStatusBarAnimation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.prefersStatusBarHidden() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.prepareForSegue(UIStoryboardSegue, sender: AnyObject?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.presentViewController(UIViewController, animated: Bool, completion:(() -> Void)?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.presentedViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.presentingViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.providesPresentationContextTransitionStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.removeFromParentViewController()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.restorationClass

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.restorationIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.rotatingFooterView() -> UIView?

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified UIViewController.rotatingHeaderView() -> UIView?

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified UIViewController.searchDisplayController

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UIViewController.segueForUnwindingToViewController(UIViewController, fromViewController: UIViewController, identifier: String?) -> UIStoryboardSegue

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func segueForUnwindingToViewController(_ toViewController: UIViewController, fromViewController fromViewController: UIViewController, identifier identifier: String) -> UIStoryboardSegue ``` | iOS 8.0 |
| To | ``` func segueForUnwindingToViewController(_ toViewController: UIViewController, fromViewController fromViewController: UIViewController, identifier identifier: String?) -> UIStoryboardSegue ``` | iOS 6.0 |

Modified UIViewController.setNeedsStatusBarAppearanceUpdate()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.setToolbarItems([AnyObject]?, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIViewController.shouldAutomaticallyForwardAppearanceMethods() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.shouldAutomaticallyForwardRotationMethods() -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified UIViewController.shouldAutorotate() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.shouldPerformSegueWithIdentifier(String?, sender: AnyObject?) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func shouldPerformSegueWithIdentifier(_ identifier: String, sender sender: AnyObject?) -> Bool ``` | iOS 8.0 |
| To | ``` func shouldPerformSegueWithIdentifier(_ identifier: String?, sender sender: AnyObject?) -> Bool ``` | iOS 6.0 |

Modified UIViewController.storyboard

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.supportedInterfaceOrientations() -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.toolbarItems

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIViewController.topLayoutGuide

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.transitionCoordinator() -> UIViewControllerTransitionCoordinator?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.transitionFromViewController(UIViewController, toViewController: UIViewController, duration: NSTimeInterval, options: UIViewAnimationOptions, animations:(() -> Void)?, completion:((Bool) -> Void)?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func transitionFromViewController(_ fromViewController: UIViewController, toViewController toViewController: UIViewController, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?) ``` | iOS 8.0 |
| To | ``` func transitionFromViewController(_ fromViewController: UIViewController, toViewController toViewController: UIViewController, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: (() -> Void)?, completion completion: ((Bool) -> Void)?) ``` | iOS 5.0 |

Modified UIViewController.transitioningDelegate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIViewController.updateViewConstraints()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.viewControllerForUnwindSegueAction(Selector, fromViewController: UIViewController, withSender: AnyObject?) -> UIViewController?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIViewController.viewDidLayoutSubviews()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.viewWillLayoutSubviews()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.willAnimateRotationToInterfaceOrientation(UIInterfaceOrientation, duration: NSTimeInterval)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified UIViewController.willMoveToParentViewController(UIViewController?)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewController.willRotateToInterfaceOrientation(UIInterfaceOrientation, duration: NSTimeInterval)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified UIViewKeyframeAnimationOptions [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct UIViewKeyframeAnimationOptions : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var LayoutSubviews: UIViewKeyframeAnimationOptions { get }     static var AllowUserInteraction: UIViewKeyframeAnimationOptions { get }     static var BeginFromCurrentState: UIViewKeyframeAnimationOptions { get }     static var Repeat: UIViewKeyframeAnimationOptions { get }     static var Autoreverse: UIViewKeyframeAnimationOptions { get }     static var OverrideInheritedDuration: UIViewKeyframeAnimationOptions { get }     static var OverrideInheritedOptions: UIViewKeyframeAnimationOptions { get }     static var CalculationModeLinear: UIViewKeyframeAnimationOptions { get }     static var CalculationModeDiscrete: UIViewKeyframeAnimationOptions { get }     static var CalculationModePaced: UIViewKeyframeAnimationOptions { get }     static var CalculationModeCubic: UIViewKeyframeAnimationOptions { get }     static var CalculationModeCubicPaced: UIViewKeyframeAnimationOptions { get } } ``` | iOS 8.0 |
| To | ``` struct UIViewKeyframeAnimationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var LayoutSubviews: UIViewKeyframeAnimationOptions { get }     static var AllowUserInteraction: UIViewKeyframeAnimationOptions { get }     static var BeginFromCurrentState: UIViewKeyframeAnimationOptions { get }     static var Repeat: UIViewKeyframeAnimationOptions { get }     static var Autoreverse: UIViewKeyframeAnimationOptions { get }     static var OverrideInheritedDuration: UIViewKeyframeAnimationOptions { get }     static var OverrideInheritedOptions: UIViewKeyframeAnimationOptions { get }     static var CalculationModeLinear: UIViewKeyframeAnimationOptions { get }     static var CalculationModeDiscrete: UIViewKeyframeAnimationOptions { get }     static var CalculationModePaced: UIViewKeyframeAnimationOptions { get }     static var CalculationModeCubic: UIViewKeyframeAnimationOptions { get }     static var CalculationModeCubicPaced: UIViewKeyframeAnimationOptions { get } } ``` | iOS 7.0 |

Modified UIViewKeyframeAnimationOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified UIViewPrintFormatter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UIViewTintAdjustmentMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIWebView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIWebView.allowsInlineMediaPlayback

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIWebView.dataDetectorTypes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIWebView.gapBetweenPages

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIWebView.keyboardDisplayRequiresUserAction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIWebView.mediaPlaybackAllowsAirPlay

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIWebView.mediaPlaybackRequiresUserAction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIWebView.pageCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIWebView.pageLength

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIWebView.paginationBreakingMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIWebView.paginationMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIWebView.scrollView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIWebView.suppressesIncrementalRendering

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIWindow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified UIWindow.rootViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIWindow.screen

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified NSAttachmentAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSAttachmentCharacter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSBackgroundColorAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSBackgroundColorDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSBaselineOffsetAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSCharacterEncodingDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSDefaultAttributesDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSDefaultTabIntervalDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSDocumentTypeDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSExpansionAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSFontAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSForegroundColorAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSHTMLTextDocumentType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSHyphenationFactorDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSKernAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSLigatureAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSLinkAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSObliquenessAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPaperMarginDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSPaperSizeDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSParagraphStyleAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSPlainTextDocumentType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSRTFDTextDocumentType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSRTFTextDocumentType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSReadOnlyDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSShadowAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSStrikethroughColorAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSStrikethroughStyleAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSStrokeColorAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSStrokeWidthAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSTabColumnTerminatorsAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextAlignmentFromCTTextAlignment(CTTextAlignment) -> NSTextAlignment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSTextAlignmentToCTTextAlignment(NSTextAlignment) -> CTTextAlignment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSTextEffectAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextEffectLetterpressStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextLayoutSectionOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextLayoutSectionRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextLayoutSectionsAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextStorageDidProcessEditingNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSTextStorageWillProcessEditingNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUnderlineColorAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSUnderlineStyleAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSVerticalGlyphFormAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified NSViewModeDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSViewSizeDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSViewZoomDocumentAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified NSWritingDirectionAttributeName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIAccessibilityAnnouncementDidFinishNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIAccessibilityAnnouncementKeyStringValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIAccessibilityAnnouncementKeyWasSuccessful

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIAccessibilityAnnouncementNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIAccessibilityClosedCaptioningStatusDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityConvertFrameToScreenCoordinates(CGRect, UIView!) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIAccessibilityConvertPathToScreenCoordinates(UIBezierPath!, UIView!) -> UIBezierPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIAccessibilityGuidedAccessStatusDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIAccessibilityInvertColorsStatusDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIAccessibilityIsClosedCaptioningEnabled() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityIsGuidedAccessEnabled() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIAccessibilityIsInvertColorsEnabled() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIAccessibilityIsMonoAudioEnabled() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityIsVoiceOverRunning() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIAccessibilityMonoAudioStatusDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityPageScrolledNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UIAccessibilityRegisterGestureConflictWithZoom()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityRequestGuidedAccessSession(Bool,((Bool) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIAccessibilitySpeechAttributeLanguage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIAccessibilitySpeechAttributePitch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIAccessibilitySpeechAttributePunctuation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIAccessibilityTraitAdjustable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIAccessibilityTraitAllowsDirectInteraction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityTraitCausesPageTurn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIAccessibilityTraitHeader

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIAccessibilityTraitStartsMediaSession

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIAccessibilityVoiceOverStatusChanged

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIAccessibilityZoomFocusChanged(UIAccessibilityZoomType, CGRect, UIView!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIActivityTypeAddToReadingList

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIActivityTypeAirDrop

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIActivityTypeAssignToContact

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivityTypeCopyToPasteboard

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivityTypeMail

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivityTypeMessage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivityTypePostToFacebook

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivityTypePostToFlickr

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIActivityTypePostToTencentWeibo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIActivityTypePostToTwitter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivityTypePostToVimeo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIActivityTypePostToWeibo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivityTypePrint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIActivityTypeSaveToCameraRoll

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationBackgroundFetchIntervalMinimum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationBackgroundFetchIntervalNever

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationBackgroundRefreshStatusDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationDidEnterBackgroundNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplicationInvalidInterfaceOrientationException

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationLaunchOptionsAnnotationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIApplicationLaunchOptionsBluetoothCentralsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationLaunchOptionsBluetoothPeripheralsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationLaunchOptionsLocalNotificationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplicationLaunchOptionsLocationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplicationLaunchOptionsNewsstandDownloadsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIApplicationLaunchOptionsRemoteNotificationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIApplicationLaunchOptionsSourceApplicationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIApplicationLaunchOptionsURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIApplicationProtectedDataDidBecomeAvailable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplicationProtectedDataWillBecomeUnavailable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIApplicationStateRestorationBundleVersionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationStateRestorationSystemVersionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationStateRestorationTimestampKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationStateRestorationUserInterfaceIdiomKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIApplicationUserDidTakeScreenshotNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIApplicationWillEnterForegroundNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIBackgroundTaskInvalid

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UICollectionElementKindSectionFooter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UICollectionElementKindSectionHeader

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UIContentSizeCategoryAccessibilityExtraExtraExtraLarge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryAccessibilityExtraExtraLarge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryAccessibilityExtraLarge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryAccessibilityLarge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryAccessibilityMedium

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryExtraExtraExtraLarge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryExtraExtraLarge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryExtraLarge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryExtraSmall

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryLarge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryMedium

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategoryNewValueKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIContentSizeCategorySmall

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIDeviceBatteryLevelDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIDeviceBatteryStateDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIDeviceProximityStateDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIDocumentStateChangedNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIFontDescriptorCascadeListAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorCharacterSetAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorFaceAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorFamilyAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorFeatureSettingsAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorFixedAdvanceAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorMatrixAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorNameAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorSizeAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorTextStyleAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorTraitsAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontDescriptorVisibleNameAttribute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontFeatureSelectorIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontFeatureTypeIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontSlantTrait

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontSymbolicTrait

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontTextStyleBody

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontTextStyleCaption1

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontTextStyleCaption2

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontTextStyleFootnote

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontTextStyleHeadline

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontTextStyleSubheadline

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontWeightTrait

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIFontWidthTrait

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIGraphicsAddPDFContextDestinationAtPoint(String!, CGPoint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIGraphicsBeginImageContextWithOptions(CGSize, Bool, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIGraphicsBeginPDFContextToData(NSMutableData!, CGRect,[NSObject: AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIGraphicsBeginPDFContextToFile(String!, CGRect,[NSObject: AnyObject]!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIGraphicsBeginPDFPage()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIGraphicsBeginPDFPageWithInfo(CGRect,[NSObject: AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIGraphicsEndPDFContext()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIGraphicsGetPDFContextBounds() -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIGraphicsSetPDFContextDestinationForRect(String!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIGraphicsSetPDFContextURLForRect(NSURL!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIGuidedAccessRestrictionStateForIdentifier(String!) -> UIGuidedAccessRestrictionState

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIImagePickerControllerMediaMetadata

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified UIImagePickerControllerReferenceURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified UIKeyInputDownArrow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIKeyInputEscape

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIKeyInputLeftArrow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIKeyInputRightArrow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIKeyInputUpArrow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIKeyboardAnimationCurveUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIKeyboardAnimationDurationUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIKeyboardDidChangeFrameNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIKeyboardFrameBeginUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIKeyboardFrameEndUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIKeyboardWillChangeFrameNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UILayoutFittingCompressedSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UILayoutFittingExpandedSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UILayoutPriorityDefaultHigh

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UILayoutPriorityDefaultLow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UILayoutPriorityFittingSizeLevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UILayoutPriorityRequired

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UILocalNotificationDefaultSoundName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UIMinimumKeepAliveTimeout

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified UINibExternalObjects

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIPageViewControllerOptionInterPageSpacingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UISaveVideoAtPathToSavedPhotosAlbum(String!, AnyObject!, Selector, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIScreenBrightnessDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIScreenDidConnectNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIScreenDidDisconnectNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIScreenModeDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified UIScrollViewDecelerationRateFast

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIScrollViewDecelerationRateNormal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UIStateRestorationViewControllerStoryboardKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified UITableViewAutomaticDimension

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UITableViewIndexSearch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified UITextInputCurrentInputModeDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified UITextInputTextBackgroundColorKey

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.2 | iOS 8.0 |

Modified UITextInputTextColorKey

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.2 | iOS 8.0 |

Modified UITextInputTextFontKey

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.2 | iOS 8.0 |

Modified UITransitionContextFromViewControllerKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UITransitionContextToViewControllerKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(String!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified UIViewControllerHierarchyInconsistencyException

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified UIViewNoIntrinsicMetric

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

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
