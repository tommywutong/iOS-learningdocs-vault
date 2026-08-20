---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/UIKit.html
archived_at: '2026-07-18T02:57:01.104081Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# UIKit Changes for Swift

### UIKit

Removed NSControlCharacterAction.ContainerBreakActionRemoved NSControlCharacterAction.HorizontalTabActionRemoved NSControlCharacterAction.LineBreakActionRemoved NSControlCharacterAction.ParagraphBreakActionRemoved NSControlCharacterAction.WhitespaceActionRemoved NSControlCharacterAction.ZeroAdvancementActionRemoved NSLayoutFormatOptions.init(_: UInt)Removed NSStringDrawingOptions.init(_: Int)Removed NSTextStorageEditActions.init(_: UInt)Removed UICollectionViewScrollPosition.init(_: UInt)Removed UICollisionBehaviorMode.init(_: UInt)Removed UIColor.init(CGColor: CGColor!) -> UIColorRemoved UIControlEvents.init(_: UInt)Removed UIControlState.init(_: UInt)Removed UIDataDetectorTypes.init(_: UInt)Removed UIDocumentState.init(_: UInt)Removed UIFontDescriptor.init(fontAttributes: [NSObject : AnyObject]!) -> UIFontDescriptorRemoved UIFontDescriptorSymbolicTraits.init(_: UInt32)Removed UIInterfaceOrientationMask.init(_: UInt)Removed UIKeyModifierFlags.init(_: Int)Removed UIPopoverArrowDirection.init(_: UInt)Removed UIPrinterJobTypes.init(_: Int)Removed UIRectCorner.init(_: UInt)Removed UIRectEdge.init(_: UInt)Removed UIRemoteNotificationType.init(_: UInt)Removed UISwipeGestureRecognizerDirection.init(_: UInt)Removed UITabBarItem.setTitlePositionAdjustment(_: UIOffset)Removed UITabBarItem.titlePositionAdjustment() -> UIOffsetRemoved UITableView.indexPathForSelectedRow() -> NSIndexPath?Removed UITableView.indexPathsForSelectedRows() -> [AnyObject]?Removed UITableView.indexPathsForVisibleRows() -> [AnyObject]?Removed UITableView.numberOfSections() -> IntRemoved UITableView.visibleCells() -> [AnyObject]Removed UITableViewCellStateMask.init(_: UInt)Removed UIUserNotificationType.init(_: UInt)Removed UIView.constraints() -> [AnyObject]Removed UIView.getMirror() -> MirrorTypeRemoved UIView.setTranslatesAutoresizingMaskIntoConstraints(_: Bool)Removed UIView.translatesAutoresizingMaskIntoConstraints() -> BoolRemoved UIViewAnimationOptions.init(_: UInt)Removed UIViewAutoresizing.init(_: UInt)Removed UIViewKeyframeAnimationOptions.init(_: UInt)Added [NSAttributedString.containsAttachmentsInRange(_: NSRange) -> Bool](https://developer.apple.com/documentation/foundation/nsattributedstring/1525086-containsattachments)Added [NSAttributedString.init(URL: NSURL, options: [String : AnyObject], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws](https://developer.apple.com/documentation/foundation/nsattributedstring/1530490-init)Added [NSControlCharacterAction.ContainerBreak](https://developer.apple.com/documentation/uikit/nscontrolcharacteraction/nscontrolcharacteractioncontainerbreak)Added [NSControlCharacterAction.HorizontalTab](https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction/1403233-horizontaltab)Added [NSControlCharacterAction.LineBreak](https://developer.apple.com/documentation/uikit/nscontrolcharacteraction/nscontrolcharacteractionlinebreak)Added [NSControlCharacterAction.ParagraphBreak](https://developer.apple.com/documentation/appkit/nscontrolcharacteraction/nscontrolcharacteractionparagraphbreak)Added [NSControlCharacterAction.Whitespace](https://developer.apple.com/documentation/appkit/nscontrolcharacteraction/nscontrolcharacteractionwhitespace)Added [NSControlCharacterAction.ZeroAdvancement](https://developer.apple.com/documentation/appkit/nscontrolcharacteraction/nscontrolcharacteractionzeroadvancement)Added [NSDataAsset](https://developer.apple.com/documentation/uikit/nsdataasset)Added [NSDataAsset.data](https://developer.apple.com/documentation/appkit/nsdataasset/1403437-data)Added [NSDataAsset.init(name: String)](https://developer.apple.com/documentation/uikit/nsdataasset/1403439-initwithname)Added [NSDataAsset.init(name: String, bundle: NSBundle)](https://developer.apple.com/documentation/appkit/nsdataasset/1403436-initwithname)Added [NSDataAsset.name](https://developer.apple.com/documentation/uikit/nsdataasset/1403435-name)Added [NSDataAsset.typeIdentifier](https://developer.apple.com/documentation/appkit/nsdataasset/1403434-typeidentifier)Added [NSLayoutAnchor](https://developer.apple.com/documentation/uikit/nslayoutanchor)Added [NSLayoutAnchor.constraintEqualToAnchor(_: NSLayoutAnchor!) -> NSLayoutConstraint!](https://developer.apple.com/documentation/uikit/nslayoutanchor/1500946-constraint)Added [NSLayoutAnchor.constraintEqualToAnchor(_: NSLayoutAnchor!, constant: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/uikit/nslayoutanchor/1500937-constraint)Added [NSLayoutAnchor.constraintGreaterThanOrEqualToAnchor(_: NSLayoutAnchor!) -> NSLayoutConstraint!](https://developer.apple.com/documentation/appkit/nslayoutanchor/1500936-constraint)Added [NSLayoutAnchor.constraintGreaterThanOrEqualToAnchor(_: NSLayoutAnchor!, constant: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/uikit/nslayoutanchor/1500948-constraintgreaterthanorequaltoan)Added [NSLayoutAnchor.constraintLessThanOrEqualToAnchor(_: NSLayoutAnchor!) -> NSLayoutConstraint!](https://developer.apple.com/documentation/appkit/nslayoutanchor/1500953-constraint)Added [NSLayoutAnchor.constraintLessThanOrEqualToAnchor(_: NSLayoutAnchor!, constant: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/appkit/nslayoutanchor/1500959-constraint)Added [NSLayoutAttribute.LastBaseline](https://developer.apple.com/documentation/appkit/nslayoutattribute/nslayoutattributelastbaseline)Added [NSLayoutDimension](https://developer.apple.com/documentation/uikit/nslayoutdimension)Added [NSLayoutDimension.constraintEqualToAnchor(_: NSLayoutDimension!, multiplier: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500951-constraintequaltoanchor)Added [NSLayoutDimension.constraintEqualToAnchor(_: NSLayoutDimension!, multiplier: CGFloat, constant: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500934-constraintequaltoanchor)Added [NSLayoutDimension.constraintEqualToConstant(_: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500941-constraint)Added [NSLayoutDimension.constraintGreaterThanOrEqualToAnchor(_: NSLayoutDimension!, multiplier: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500961-constraint)Added [NSLayoutDimension.constraintGreaterThanOrEqualToAnchor(_: NSLayoutDimension!, multiplier: CGFloat, constant: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500965-constraint)Added [NSLayoutDimension.constraintGreaterThanOrEqualToConstant(_: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500939-constraint)Added [NSLayoutDimension.constraintLessThanOrEqualToAnchor(_: NSLayoutDimension!, multiplier: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/uikit/nslayoutdimension/1500943-constraintlessthanorequaltoancho)Added [NSLayoutDimension.constraintLessThanOrEqualToAnchor(_: NSLayoutDimension!, multiplier: CGFloat, constant: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/appkit/nslayoutdimension/1500957-constraintlessthanorequaltoancho)Added [NSLayoutDimension.constraintLessThanOrEqualToConstant(_: CGFloat) -> NSLayoutConstraint!](https://developer.apple.com/documentation/uikit/nslayoutdimension/1500963-constraint)Added [NSLayoutManager.CGGlyphAtIndex(_: Int) -> CGGlyph](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403039-cgglyph)Added [NSLayoutManager.CGGlyphAtIndex(_: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>) -> CGGlyph](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403132-cgglyphatindex)Added [NSLayoutManager.init()](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402975-init)Added [NSLayoutManager.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403043-initwithcoder)Added [NSLayoutManager.lineFragmentRectForGlyphAtIndex(_: Int, effectiveRange: NSRangePointer, withoutAdditionalLayout: Bool) -> CGRect](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403116-linefragmentrect)Added [NSLayoutManager.lineFragmentUsedRectForGlyphAtIndex(_: Int, effectiveRange: NSRangePointer, withoutAdditionalLayout: Bool) -> CGRect](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403035-linefragmentusedrect)Added [NSLayoutManager.textContainerForGlyphAtIndex(_: Int, effectiveRange: NSRangePointer, withoutAdditionalLayout: Bool) -> NSTextContainer?](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403055-textcontainerforglyphatindex)Added [NSLayoutManagerDelegate.layoutManager(_: NSLayoutManager, shouldSetLineFragmentRect: UnsafeMutablePointer<CGRect>, lineFragmentUsedRect: UnsafeMutablePointer<CGRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, inTextContainer: NSTextContainer, forGlyphRange: NSRange) -> Bool](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403122-layoutmanager)Added [NSLayoutXAxisAnchor](https://developer.apple.com/documentation/uikit/nslayoutxaxisanchor)Added [NSLayoutYAxisAnchor](https://developer.apple.com/documentation/uikit/nslayoutyaxisanchor)Added [NSMutableAttributedString.readFromURL(_: NSURL, options: [String : AnyObject], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1524892-readfromurl)Added [NSMutableParagraphStyle.addTabStop(_: NSTextTab)](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1525051-addtabstop)Added [NSMutableParagraphStyle.allowsDefaultTighteningForTruncation](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1534136-allowsdefaulttighteningfortrunca)Added [NSMutableParagraphStyle.removeTabStop(_: NSTextTab)](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1535084-removetabstop)Added [NSMutableParagraphStyle.setParagraphStyle(_: NSParagraphStyle)](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1533980-setparagraphstyle)Added [NSObject.accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?](https://developer.apple.com/documentation/objectivec/nsobject/1615206-accessibilityassistivetechnology)Added [NSParagraphStyle.allowsDefaultTighteningForTruncation](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1528994-allowsdefaulttighteningfortrunca)Added [NSShadow.init()](https://developer.apple.com/documentation/appkit/nsshadow/1429853-init)Added [NSShadow.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/nsshadow/1623903-init)Added [NSTextContainer.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/nstextcontainer/1444573-init)Added [NSTextContainer.replaceLayoutManager(_: NSLayoutManager)](https://developer.apple.com/documentation/appkit/nstextcontainer/1444545-replacelayoutmanager)Added [NSTextContainer.simpleRectangularTextContainer](https://developer.apple.com/documentation/appkit/nstextcontainer/1444525-issimplerectangulartextcontainer)Added [NSUnderlineStyle.PatternSolid](https://developer.apple.com/documentation/uikit/nsunderlinestyle/nsunderlinestylepatternsolid)Added [NSWritingDirectionFormatType [enum]](https://developer.apple.com/documentation/uikit/nswritingdirectionformattype)Added [NSWritingDirectionFormatType.Embedding](https://developer.apple.com/documentation/appkit/nswritingdirectionformattype/nswritingdirectionembedding)Added [NSWritingDirectionFormatType.Override](https://developer.apple.com/documentation/appkit/nswritingdirectionformattype/nswritingdirectionoverride)Added [UIActivityIndicatorView.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622844-initwithcoder)Added [UIActivityIndicatorView.init(frame: CGRect)](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622841-init)Added [UIAlertController.preferredAction](https://developer.apple.com/documentation/uikit/uialertcontroller/1620102-preferredaction)Added [UIAlertView.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uialertview/1620779-initwithcoder)Added [UIAlertView.init(frame: CGRect)](https://developer.apple.com/documentation/uikit/uialertview/1620759-initwithframe)Added [UIAppearance.appearanceForTraitCollection(_: UITraitCollection, whenContainedInInstancesOfClasses: [AnyObject.Type]) -> Self [class]](https://developer.apple.com/documentation/uikit/uiappearance/1615008-appearancefortraitcollection)Added [UIAppearance.appearanceWhenContainedInInstancesOfClasses(_: [AnyObject.Type]) -> Self [class]](https://developer.apple.com/documentation/uikit/uiappearance/1615013-appearancewhencontainedininstanc)Added [UIApplication.shortcutItems](https://developer.apple.com/documentation/uikit/uiapplication/1623033-shortcutitems)Added [UIApplicationDelegate.application(_: UIApplication, handleActionWithIdentifier: String?, forLocalNotification: UILocalNotification, withResponseInfo: [NSObject : AnyObject], completionHandler: () -> Void)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623105-application)Added [UIApplicationDelegate.application(_: UIApplication, handleActionWithIdentifier: String?, forRemoteNotification: [NSObject : AnyObject], withResponseInfo: [NSObject : AnyObject], completionHandler: () -> Void)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623021-application)Added [UIApplicationDelegate.application(_: UIApplication, openURL: NSURL, options: [String : AnyObject]) -> Bool](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623112-application)Added [UIApplicationDelegate.application(_: UIApplication, performActionForShortcutItem: UIApplicationShortcutItem, completionHandler: (Bool) -> Void)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622935-application)Added [UIApplicationDelegate.applicationShouldRequestHealthAuthorization(_: UIApplication)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622998-applicationshouldrequesthealthau)Added [UIApplicationShortcutIcon](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon)Added [UIApplicationShortcutIcon.init(templateImageName: String)](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/1623367-iconwithtemplateimagename)Added [UIApplicationShortcutIcon.init(type: UIApplicationShortcutIconType)](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/1623389-iconwithtype)Added [UIApplicationShortcutIconType [enum]](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype)Added [UIApplicationShortcutIconType.Add](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypeadd)Added [UIApplicationShortcutIconType.Compose](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypecompose)Added [UIApplicationShortcutIconType.Location](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypelocation)Added [UIApplicationShortcutIconType.Pause](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/pause)Added [UIApplicationShortcutIconType.Play](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/play)Added [UIApplicationShortcutIconType.Search](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypesearch)Added [UIApplicationShortcutIconType.Share](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/share)Added [UIApplicationShortcutItem](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem)Added [UIApplicationShortcutItem.icon](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623352-icon)Added [UIApplicationShortcutItem.init(type: String, localizedTitle: String)](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623355-init)Added [UIApplicationShortcutItem.init(type: String, localizedTitle: String, localizedSubtitle: String?, icon: UIApplicationShortcutIcon?, userInfo: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623372-init)Added [UIApplicationShortcutItem.localizedSubtitle](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623376-localizedsubtitle)Added [UIApplicationShortcutItem.localizedTitle](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623354-localizedtitle)Added [UIApplicationShortcutItem.type](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623382-type)Added [UIApplicationShortcutItem.userInfo](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/1623370-userinfo)Added [UIAttachmentBehavior.attachmentRange](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621294-attachmentrange)Added [UIAttachmentBehavior.fixedAttachmentWithItem(_: UIDynamicItem, attachedToItem: UIDynamicItem, attachmentAnchor: CGPoint) -> Self [class]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621308-fixedattachment)Added [UIAttachmentBehavior.frictionTorque](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621307-frictiontorque)Added [UIAttachmentBehavior.limitAttachmentWithItem(_: UIDynamicItem, offsetFromCenter: UIOffset, attachedToItem: UIDynamicItem, offsetFromCenter: UIOffset) -> Self [class]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621320-limitattachmentwithitem)Added [UIAttachmentBehavior.pinAttachmentWithItem(_: UIDynamicItem, attachedToItem: UIDynamicItem, attachmentAnchor: CGPoint) -> Self [class]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621322-pinattachment)Added [UIAttachmentBehavior.slidingAttachmentWithItem(_: UIDynamicItem, attachedToItem: UIDynamicItem, attachmentAnchor: CGPoint, axisOfTranslation: CGVector) -> Self [class]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621318-slidingattachment)Added [UIAttachmentBehavior.slidingAttachmentWithItem(_: UIDynamicItem, attachmentAnchor: CGPoint, axisOfTranslation: CGVector) -> Self [class]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621314-slidingattachment)Added [UIBarButtonItem.buttonGroup](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1623564-buttongroup)Added [UIBarButtonItem.init()](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617166-init)Added [UIBarButtonItem.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617111-init)Added [UIBarButtonItemGroup](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup)Added [UIBarButtonItemGroup.barButtonItems](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/1623565-barbuttonitems)Added [UIBarButtonItemGroup.displayingRepresentativeItem](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/1623560-displayingrepresentativeitem)Added [UIBarButtonItemGroup.init(barButtonItems: [UIBarButtonItem], representativeItem: UIBarButtonItem?)](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/1623559-init)Added [UIBarButtonItemGroup.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/1623562-init)Added [UIBarButtonItemGroup.representativeItem](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/1623563-representativeitem)Added [UIBarItem.init()](https://developer.apple.com/documentation/uikit/uibaritem/1616411-init)Added [UIBarItem.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uibaritem/1616416-initwithcoder)Added [UIBarMetrics.LandscapePhone](https://developer.apple.com/documentation/uikit/uibarmetrics/uibarmetricslandscapephone)Added [UIBarMetrics.LandscapePhonePrompt](https://developer.apple.com/documentation/uikit/uibarmetrics/1624862-landscapephoneprompt)Added [UIBarStyle.BlackOpaque](https://developer.apple.com/documentation/uikit/uibarstyle/uibarstyleblackopaque)Added [UIBezierPath.init()](https://developer.apple.com/documentation/uikit/uibezierpath/1624381-init)Added [UIBezierPath.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uibezierpath/1624346-init)Added [UIButtonType.RoundedRect](https://developer.apple.com/documentation/uikit/uibuttontype/uibuttontyperoundedrect)Added [UICollectionView.beginInteractiveMovementForItemAtIndexPath(_: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uicollectionview/1618019-begininteractivemovementforitema)Added [UICollectionView.cancelInteractiveMovement()](https://developer.apple.com/documentation/uikit/uicollectionview/1618076-cancelinteractivemovement)Added [UICollectionView.endInteractiveMovement()](https://developer.apple.com/documentation/uikit/uicollectionview/1618082-endinteractivemovement)Added [UICollectionView.indexPathsForVisibleSupplementaryElementsOfKind(_: String) -> [NSIndexPath]](https://developer.apple.com/documentation/uikit/uicollectionview/1618034-indexpathsforvisiblesupplementar)Added [UICollectionView.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uicollectionview/1618065-init)Added [UICollectionView.supplementaryViewForElementKind(_: String, atIndexPath: NSIndexPath) -> UICollectionReusableView](https://developer.apple.com/documentation/uikit/uicollectionview/1618041-supplementaryview)Added [UICollectionView.updateInteractiveMovementTargetPosition(_: CGPoint)](https://developer.apple.com/documentation/uikit/uicollectionview/1618079-updateinteractivemovementtargetp)Added [UICollectionView.visibleSupplementaryViewsOfKind(_: String) -> [UICollectionReusableView]](https://developer.apple.com/documentation/uikit/uicollectionview/1618026-visiblesupplementaryviewsofkind)Added [UICollectionViewController.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623981-initwithcoder)Added [UICollectionViewController.init(nibName: String?, bundle: NSBundle?)](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623975-initwithnibname)Added [UICollectionViewController.installsStandardGestureForInteractiveMovement](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623979-installsstandardgestureforintera)Added [UICollectionViewDataSource.collectionView(_: UICollectionView, canMoveItemAtIndexPath: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618015-collectionview)Added [UICollectionViewDataSource.collectionView(_: UICollectionView, moveItemAtIndexPath: NSIndexPath, toIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618064-collectionview)Added [UICollectionViewDelegate.collectionView(_: UICollectionView, targetContentOffsetForProposedContentOffset: CGPoint) -> CGPoint](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618007-collectionview)Added [UICollectionViewDelegate.collectionView(_: UICollectionView, targetIndexPathForMoveFromItemAtIndexPath: NSIndexPath, toProposedIndexPath: NSIndexPath) -> NSIndexPath](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618052-collectionview)Added [UICollectionViewFlowLayout.sectionFootersPinToVisibleBounds](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617701-sectionfooterspintovisiblebounds)Added [UICollectionViewFlowLayout.sectionHeadersPinToVisibleBounds](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617699-sectionheaderspintovisiblebounds)Added [UICollectionViewLayout.init()](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617734-init)Added [UICollectionViewLayout.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617766-init)Added [UICollectionViewLayout.invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths(_: [NSIndexPath], previousIndexPaths: [NSIndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617755-invalidationcontextforendinginte)Added [UICollectionViewLayout.invalidationContextForInteractivelyMovingItems(_: [NSIndexPath], withTargetPosition: CGPoint, previousIndexPaths: [NSIndexPath], previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617757-invalidationcontext)Added [UICollectionViewLayout.layoutAttributesForInteractivelyMovingItemAtIndexPath(_: NSIndexPath, withTargetPosition: CGPoint) -> UICollectionViewLayoutAttributes](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617788-layoutattributesforinteractively)Added [UICollectionViewLayout.targetIndexPathForInteractivelyMovingItem(_: NSIndexPath, withPosition: CGPoint) -> NSIndexPath](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617778-targetindexpath)Added [UICollectionViewLayoutInvalidationContext.interactiveMovementTarget](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617808-interactivemovementtarget)Added [UICollectionViewLayoutInvalidationContext.previousIndexPathsForInteractivelyMovingItems](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617800-previousindexpathsforinteractive)Added [UICollectionViewLayoutInvalidationContext.targetIndexPathsForInteractivelyMovingItems](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617780-targetindexpathsforinteractively)Added [UICollectionViewTransitionLayout.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622192-initwithcoder)Added [UIControlEvents.PrimaryActionTriggered](https://developer.apple.com/documentation/uikit/uicontrolevents/uicontroleventprimaryactiontriggered)Added [UIDocumentMenuViewController.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614182-init)Added [UIDocumentPickerViewController.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618686-init)Added [UIDocumentState.ProgressAvailable](https://developer.apple.com/documentation/uikit/uidocumentstate/uidocumentstateprogressavailable)Added [UIDynamicItem.collisionBoundingPath](https://developer.apple.com/documentation/uikit/uidynamicitem/1618494-collisionboundingpath)Added [UIDynamicItem.collisionBoundsType](https://developer.apple.com/documentation/uikit/uidynamicitem/1618493-collisionboundstype)Added [UIDynamicItemBehavior.anchored](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624394-isanchored)Added [UIDynamicItemBehavior.charge](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624390-charge)Added [UIDynamicItemCollisionBoundsType [enum]](https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype)Added [UIDynamicItemCollisionBoundsType.Ellipse](https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype/uidynamicitemcollisionboundstypeellipse)Added [UIDynamicItemCollisionBoundsType.Path](https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype/uidynamicitemcollisionboundstypepath)Added [UIDynamicItemCollisionBoundsType.Rectangle](https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype/uidynamicitemcollisionboundstyperectangle)Added [UIDynamicItemGroup](https://developer.apple.com/documentation/uikit/uidynamicitemgroup)Added [UIDynamicItemGroup.init(items: [UIDynamicItem])](https://developer.apple.com/documentation/uikit/uidynamicitemgroup/1618485-init)Added [UIDynamicItemGroup.items](https://developer.apple.com/documentation/uikit/uidynamicitemgroup/1618489-items)Added [UIEvent.coalescedTouchesForTouch(_: UITouch) -> [UITouch]?](https://developer.apple.com/documentation/uikit/uievent/1613808-coalescedtouchesfortouch)Added [UIEvent.predictedTouchesForTouch(_: UITouch) -> [UITouch]?](https://developer.apple.com/documentation/uikit/uievent/1613814-predictedtouches)Added [UIFieldBehavior](https://developer.apple.com/documentation/uikit/uifieldbehavior)Added [UIFieldBehavior.addItem(_: UIDynamicItem)](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624996-additem)Added [UIFieldBehavior.animationSpeed](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624986-animationspeed)Added [UIFieldBehavior.direction](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624987-direction)Added [UIFieldBehavior.dragField() -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624990-dragfield)Added [UIFieldBehavior.electricField() -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625004-electricfield)Added [UIFieldBehavior.falloff](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624988-falloff)Added [UIFieldBehavior.fieldWithEvaluationBlock(_: (UIFieldBehavior, CGPoint, CGVector, CGFloat, CGFloat, NSTimeInterval) -> CGVector) -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625001-field)Added [UIFieldBehavior.items](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625002-items)Added [UIFieldBehavior.linearGravityFieldWithVector(_: CGVector) -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624991-lineargravityfield)Added [UIFieldBehavior.magneticField() -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625007-magneticfield)Added [UIFieldBehavior.minimumRadius](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624994-minimumradius)Added [UIFieldBehavior.noiseFieldWithSmoothness(_: CGFloat, animationSpeed: CGFloat) -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625006-noisefieldwithsmoothness)Added [UIFieldBehavior.position](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625003-position)Added [UIFieldBehavior.radialGravityFieldWithPosition(_: CGPoint) -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624985-radialgravityfield)Added [UIFieldBehavior.region](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625005-region)Added [UIFieldBehavior.removeItem(_: UIDynamicItem)](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624993-removeitem)Added [UIFieldBehavior.smoothness](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624998-smoothness)Added [UIFieldBehavior.springField() -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624995-springfield)Added [UIFieldBehavior.strength](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624997-strength)Added [UIFieldBehavior.turbulenceFieldWithSmoothness(_: CGFloat, animationSpeed: CGFloat) -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624992-turbulencefieldwithsmoothness)Added [UIFieldBehavior.velocityFieldWithVector(_: CGVector) -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1624989-velocityfield)Added [UIFieldBehavior.vortexField() -> Self [class]](https://developer.apple.com/documentation/uikit/uifieldbehavior/1625000-vortexfield)Added [UIFloatRange [struct]](https://developer.apple.com/documentation/uikit/uifloatrange)Added UIFloatRange.init()Added UIFloatRange.init(minimum: CGFloat, maximum: CGFloat)Added [UIFloatRange.maximum](https://developer.apple.com/documentation/uikit/uifloatrange/1621305-maximum)Added [UIFloatRange.minimum](https://developer.apple.com/documentation/uikit/uifloatrange/1621300-minimum)Added [UIFont.monospacedDigitSystemFontOfSize(_: CGFloat, weight: CGFloat) -> UIFont [class]](https://developer.apple.com/documentation/uikit/uifont/1619022-monospaceddigitsystemfontofsize)Added [UIFontDescriptor.init()](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616667-init)Added [UIFontDescriptor.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616662-init)Added [UIForceTouchCapability [enum]](https://developer.apple.com/documentation/uikit/uiforcetouchcapability)Added [UIForceTouchCapability.Available](https://developer.apple.com/documentation/uikit/uiforcetouchcapability/uiforcetouchcapabilityavailable)Added [UIForceTouchCapability.Unavailable](https://developer.apple.com/documentation/uikit/uiforcetouchcapability/unavailable)Added [UIForceTouchCapability.Unknown](https://developer.apple.com/documentation/uikit/uiforcetouchcapability/unknown)Added [UIGestureRecognizerState.Recognized](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state/1624228-recognized)Added [UIImage.flipsForRightToLeftLayoutDirection](https://developer.apple.com/documentation/uikit/uiimage/1624128-flipsforrighttoleftlayoutdirecti)Added [UIImage.imageFlippedForRightToLeftLayoutDirection() -> UIImage](https://developer.apple.com/documentation/uikit/uiimage/1624140-imageflippedforrighttoleftlayout)Added [UIImageAsset.init()](https://developer.apple.com/documentation/uikit/uiimageasset/1624977-init)Added [UIImageAsset.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiimageasset/1624978-initwithcoder)Added [UIInputView.allowsSelfSizing](https://developer.apple.com/documentation/uikit/uiinputview/1619473-allowsselfsizing)Added [UIInputView.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiinputview/1619475-initwithcoder)Added [UIInterpolatingMotionEffect.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622368-init)Added [UIKeyboardAppearance.Alert](https://developer.apple.com/documentation/uikit/uikeyboardappearance/uikeyboardappearancealert)Added [UIKeyboardType.Alphabet](https://developer.apple.com/documentation/uikit/uikeyboardtype/uikeyboardtypealphabet)Added [UIKeyCommand.discoverabilityTitle](https://developer.apple.com/documentation/uikit/uikeycommand/1621094-discoverabilitytitle)Added [UIKeyCommand.init()](https://developer.apple.com/documentation/uikit/uikeycommand/1621100-init)Added [UIKeyCommand.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uikeycommand/1621115-initwithcoder)Added [UIKeyCommand.init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector, discoverabilityTitle: String)](https://developer.apple.com/documentation/uikit/uikeycommand/1621139-keycommandwithinput)Added [UILabel.allowsDefaultTighteningForTruncation](https://developer.apple.com/documentation/uikit/uilabel/1620533-allowsdefaulttighteningfortrunca)Added [UILayoutGuide](https://developer.apple.com/documentation/uikit/uilayoutguide)Added [UILayoutGuide.bottomAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619661-bottomanchor)Added [UILayoutGuide.centerXAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619654-centerxanchor)Added [UILayoutGuide.centerYAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619659-centeryanchor)Added [UILayoutGuide.heightAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619652-heightanchor)Added [UILayoutGuide.identifier](https://developer.apple.com/documentation/uikit/uilayoutguide/1619655-identifier)Added [UILayoutGuide.layoutFrame](https://developer.apple.com/documentation/uikit/uilayoutguide/1619657-layoutframe)Added [UILayoutGuide.leadingAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619658-leadinganchor)Added [UILayoutGuide.leftAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619656-leftanchor)Added [UILayoutGuide.owningView](https://developer.apple.com/documentation/uikit/uilayoutguide/1619648-owningview)Added [UILayoutGuide.rightAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619649-rightanchor)Added [UILayoutGuide.topAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619650-topanchor)Added [UILayoutGuide.trailingAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619660-trailinganchor)Added [UILayoutGuide.widthAnchor](https://developer.apple.com/documentation/uikit/uilayoutguide/1619653-widthanchor)Added [UILayoutSupport.bottomAnchor](https://developer.apple.com/documentation/uikit/uilayoutsupport/1622239-bottomanchor)Added [UILayoutSupport.heightAnchor](https://developer.apple.com/documentation/uikit/uilayoutsupport/1622236-heightanchor)Added [UILayoutSupport.topAnchor](https://developer.apple.com/documentation/uikit/uilayoutsupport/1622255-topanchor)Added [UILocalNotification.init()](https://developer.apple.com/documentation/uikit/uilocalnotification/1616645-init)Added [UILocalNotification.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uilocalnotification/1616653-initwithcoder)Added [UIMotionEffect.init()](https://developer.apple.com/documentation/uikit/uimotioneffect/1622375-init)Added [UIMotionEffect.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uimotioneffect/1622371-initwithcoder)Added [UIMutableApplicationShortcutItem](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem)Added [UIMutableApplicationShortcutItem.icon](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/1623351-icon)Added [UIMutableApplicationShortcutItem.localizedSubtitle](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/1623384-localizedsubtitle)Added [UIMutableApplicationShortcutItem.localizedTitle](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/1623371-localizedtitle)Added [UIMutableApplicationShortcutItem.type](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/1623362-type)Added [UIMutableApplicationShortcutItem.userInfo](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/1623375-userinfo)Added [UIMutableUserNotificationAction.behavior](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615395-behavior)Added [UIMutableUserNotificationAction.parameters](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615354-parameters)Added [UINavigationItem.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uinavigationitem/1624950-init)Added [UIPageViewController.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614108-init)Added [UIPopoverPresentationController.canOverlapSourceViewRect](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622325-canoverlapsourceviewrect)Added [UIPreviewAction](https://developer.apple.com/documentation/uikit/uipreviewaction)Added [UIPreviewAction.handler](https://developer.apple.com/documentation/uikit/uipreviewaction/1621447-handler)Added [UIPreviewAction.init(title: String, style: UIPreviewActionStyle, handler: (UIPreviewAction, UIViewController) -> Void)](https://developer.apple.com/documentation/uikit/uipreviewaction/1621445-init)Added [UIPreviewActionGroup](https://developer.apple.com/documentation/uikit/uipreviewactiongroup)Added [UIPreviewActionGroup.init(title: String, style: UIPreviewActionStyle, actions: [UIPreviewAction])](https://developer.apple.com/documentation/uikit/uipreviewactiongroup/1621514-actiongroupwithtitle)Added [UIPreviewActionItem](https://developer.apple.com/documentation/uikit/uipreviewactionitem)Added [UIPreviewActionItem.title](https://developer.apple.com/documentation/uikit/uipreviewactionitem/1621352-title)Added [UIPreviewActionStyle [enum]](https://developer.apple.com/documentation/uikit/uipreviewactionstyle)Added [UIPreviewActionStyle.Default](https://developer.apple.com/documentation/uikit/uipreviewactionstyle/uipreviewactionstyledefault)Added [UIPreviewActionStyle.Destructive](https://developer.apple.com/documentation/uikit/uipreviewactionstyle/uipreviewactionstyledestructive)Added [UIPreviewActionStyle.Selected](https://developer.apple.com/documentation/uikit/uipreviewaction/style/selected)Added [UIPrinterCutterBehavior [enum]](https://developer.apple.com/documentation/uikit/uiprinter/cutterbehavior)Added [UIPrinterCutterBehavior.CutAfterEachCopy](https://developer.apple.com/documentation/uikit/uiprintercutterbehavior/uiprintercutterbehaviorcutaftereachcopy)Added [UIPrinterCutterBehavior.CutAfterEachJob](https://developer.apple.com/documentation/uikit/uiprintercutterbehavior/uiprintercutterbehaviorcutaftereachjob)Added [UIPrinterCutterBehavior.CutAfterEachPage](https://developer.apple.com/documentation/uikit/uiprintercutterbehavior/uiprintercutterbehaviorcutaftereachpage)Added [UIPrinterCutterBehavior.NoCut](https://developer.apple.com/documentation/uikit/uiprinter/cutterbehavior/nocut)Added [UIPrinterCutterBehavior.PrinterDefault](https://developer.apple.com/documentation/uikit/uiprintercutterbehavior/uiprintercutterbehaviorprinterdefault)Added [UIPrintInfo.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiprintinfo/1623546-init)Added [UIPrintInteractionControllerDelegate.printInteractionController(_: UIPrintInteractionController, chooseCutterBehavior: [AnyObject]) -> UIPrinterCutterBehavior](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618178-printinteractioncontroller)Added [UIProgressView.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiprogressview/1619839-init)Added [UIProgressView.init(frame: CGRect)](https://developer.apple.com/documentation/uikit/uiprogressview/1619842-init)Added [UIProgressView.observedProgress](https://developer.apple.com/documentation/uikit/uiprogressview/1619840-observedprogress)Added [UIReferenceLibraryViewController.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/1624809-initwithcoder)Added [UIRegion](https://developer.apple.com/documentation/uikit/uiregion)Added [UIRegion.containsPoint(_: CGPoint) -> Bool](https://developer.apple.com/documentation/uikit/uiregion/1621893-contains)Added [UIRegion.infiniteRegion() -> Self [class]](https://developer.apple.com/documentation/uikit/uiregion/1621896-infinite)Added [UIRegion.init(radius: CGFloat)](https://developer.apple.com/documentation/uikit/uiregion/1621889-initwithradius)Added [UIRegion.init(size: CGSize)](https://developer.apple.com/documentation/uikit/uiregion/1621891-init)Added [UIRegion.inverseRegion() -> Self](https://developer.apple.com/documentation/uikit/uiregion/1621894-inverseregion)Added [UIRegion.regionByDifferenceFromRegion(_: UIRegion) -> Self](https://developer.apple.com/documentation/uikit/uiregion/1621892-bydifference)Added [UIRegion.regionByIntersectionWithRegion(_: UIRegion) -> Self](https://developer.apple.com/documentation/uikit/uiregion/1621895-regionbyintersectionwithregion)Added [UIRegion.regionByUnionWithRegion(_: UIRegion) -> Self](https://developer.apple.com/documentation/uikit/uiregion/1621890-byunion)Added [UIResponder.inputAssistantItem](https://developer.apple.com/documentation/uikit/uiresponder/1621135-inputassistantitem)Added [UIReturnKeyType.Continue](https://developer.apple.com/documentation/uikit/uireturnkeytype/uireturnkeycontinue)Added [UIScreen.overscanCompensationInsets](https://developer.apple.com/documentation/uikit/uiscreen/1617824-overscancompensationinsets)Added [UIScreenOverscanCompensation.None](https://developer.apple.com/documentation/uikit/uiscreenoverscancompensation/uiscreenoverscancompensationnone)Added [UISearchBar.init()](https://developer.apple.com/documentation/uikit/uisearchbar/1624304-init)Added [UISearchBar.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uisearchbar/1624324-initwithcoder)Added [UISearchBar.init(frame: CGRect)](https://developer.apple.com/documentation/uikit/uisearchbar/1624269-initwithframe)Added [UISearchBar.inputAssistantItem](https://developer.apple.com/documentation/uikit/uisearchbar/1624275-inputassistantitem)Added [UISemanticContentAttribute [enum]](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute)Added [UISemanticContentAttribute.ForceLeftToRight](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute/uisemanticcontentattributeforcelefttoright)Added [UISemanticContentAttribute.ForceRightToLeft](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute/forcerighttoleft)Added [UISemanticContentAttribute.Playback](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute/uisemanticcontentattributeplayback)Added [UISemanticContentAttribute.Spatial](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute/uisemanticcontentattributespatial)Added [UISemanticContentAttribute.Unspecified](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute/unspecified)Added [UISnapBehavior.snapPoint](https://developer.apple.com/documentation/uikit/uisnapbehavior/1621013-snappoint)Added [UIStackView](https://developer.apple.com/documentation/uikit/uistackview)Added [UIStackView.addArrangedSubview(_: UIView)](https://developer.apple.com/documentation/uikit/uistackview/1616227-addarrangedsubview)Added [UIStackView.alignment](https://developer.apple.com/documentation/uikit/uistackview/1616243-alignment)Added [UIStackView.arrangedSubviews](https://developer.apple.com/documentation/uikit/uistackview/1616232-arrangedsubviews)Added [UIStackView.axis](https://developer.apple.com/documentation/uikit/uistackview/1616223-axis)Added [UIStackView.baselineRelativeArrangement](https://developer.apple.com/documentation/uikit/uistackview/1616224-isbaselinerelativearrangement)Added [UIStackView.distribution](https://developer.apple.com/documentation/uikit/uistackview/1616233-distribution)Added [UIStackView.init(arrangedSubviews: [UIView])](https://developer.apple.com/documentation/uikit/uistackview/1616240-initwitharrangedsubviews)Added [UIStackView.insertArrangedSubview(_: UIView, atIndex: Int)](https://developer.apple.com/documentation/uikit/uistackview/1616237-insertarrangedsubview)Added [UIStackView.layoutMarginsRelativeArrangement](https://developer.apple.com/documentation/uikit/uistackview/1616220-islayoutmarginsrelativearrangeme)Added [UIStackView.removeArrangedSubview(_: UIView)](https://developer.apple.com/documentation/uikit/uistackview/1616235-removearrangedsubview)Added [UIStackView.spacing](https://developer.apple.com/documentation/uikit/uistackview/1616225-spacing)Added [UIStackViewAlignment [enum]](https://developer.apple.com/documentation/uikit/uistackview/alignment)Added [UIStackViewAlignment.Bottom](https://developer.apple.com/documentation/uikit/uistackview/alignment/1616234-bottom)Added [UIStackViewAlignment.Center](https://developer.apple.com/documentation/uikit/uistackviewalignment/uistackviewalignmentcenter)Added [UIStackViewAlignment.Fill](https://developer.apple.com/documentation/uikit/uistackview/alignment/fill)Added [UIStackViewAlignment.FirstBaseline](https://developer.apple.com/documentation/uikit/uistackviewalignment/uistackviewalignmentfirstbaseline)Added [UIStackViewAlignment.LastBaseline](https://developer.apple.com/documentation/uikit/uistackview/alignment/lastbaseline)Added [UIStackViewAlignment.Leading](https://developer.apple.com/documentation/uikit/uistackview/alignment/leading)Added [UIStackViewAlignment.Top](https://developer.apple.com/documentation/uikit/uistackview/alignment/1616238-top)Added [UIStackViewAlignment.Trailing](https://developer.apple.com/documentation/uikit/uistackview/alignment/trailing)Added [UIStackViewDistribution [enum]](https://developer.apple.com/documentation/uikit/uistackview/distribution)Added [UIStackViewDistribution.EqualCentering](https://developer.apple.com/documentation/uikit/uistackview/distribution/equalcentering)Added [UIStackViewDistribution.EqualSpacing](https://developer.apple.com/documentation/uikit/uistackview/distribution/equalspacing)Added [UIStackViewDistribution.Fill](https://developer.apple.com/documentation/uikit/uistackviewdistribution/uistackviewdistributionfill)Added [UIStackViewDistribution.FillEqually](https://developer.apple.com/documentation/uikit/uistackview/distribution/fillequally)Added [UIStackViewDistribution.FillProportionally](https://developer.apple.com/documentation/uikit/uistackview/distribution/fillproportionally)Added [UIStoryboardUnwindSegueSource](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource)Added [UIStoryboardUnwindSegueSource.sender](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/1621914-sender)Added [UIStoryboardUnwindSegueSource.sourceViewController](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/1621917-sourceviewcontroller)Added [UIStoryboardUnwindSegueSource.unwindAction](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/1621915-unwindaction)Added [UISwitch.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiswitch/1623685-init)Added [UITabBarItem.init()](https://developer.apple.com/documentation/uikit/uitabbaritem/1617055-init)Added [UITabBarItem.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uitabbaritem/1617071-initwithcoder)Added [UITabBarItem.titlePositionAdjustment](https://developer.apple.com/documentation/uikit/uitabbaritem/1617070-titlepositionadjustment)Added [UITableView.cellLayoutMarginsFollowReadableWidth](https://developer.apple.com/documentation/uikit/uitableview/1614849-celllayoutmarginsfollowreadablew)Added [UITableView.indexPathForSelectedRow](https://developer.apple.com/documentation/uikit/uitableview/1615000-indexpathforselectedrow)Added [UITableView.indexPathsForSelectedRows](https://developer.apple.com/documentation/uikit/uitableview/1614864-indexpathsforselectedrows)Added [UITableView.indexPathsForVisibleRows](https://developer.apple.com/documentation/uikit/uitableview/1614885-indexpathsforvisiblerows)Added [UITableView.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uitableview/1614859-init)Added [UITableView.numberOfSections](https://developer.apple.com/documentation/uikit/uitableview/1614924-numberofsections)Added [UITableView.visibleCells](https://developer.apple.com/documentation/uikit/uitableview/1614896-visiblecells)Added [UITableViewCell.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uitableviewcell/1623220-initwithcoder)Added [UITableViewHeaderFooterView.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624917-init)Added [UITableViewRowActionStyle.Destructive](https://developer.apple.com/documentation/uikit/uitableviewrowaction/style/1614917-destructive)Added [UITextInput.beginFloatingCursorAtPoint(_: CGPoint)](https://developer.apple.com/documentation/uikit/uitextinput/1614557-beginfloatingcursoratpoint)Added [UITextInput.endFloatingCursor()](https://developer.apple.com/documentation/uikit/uitextinput/1614497-endfloatingcursor)Added [UITextInput.updateFloatingCursorAtPoint(_: CGPoint)](https://developer.apple.com/documentation/uikit/uitextinput/1614550-updatefloatingcursoratpoint)Added [UITextInputAssistantItem](https://developer.apple.com/documentation/uikit/uitextinputassistantitem)Added [UITextInputAssistantItem.allowsHidingShortcuts](https://developer.apple.com/documentation/uikit/uitextinputassistantitem/1614529-allowshidingshortcuts)Added [UITextInputAssistantItem.leadingBarButtonGroups](https://developer.apple.com/documentation/uikit/uitextinputassistantitem/1614575-leadingbarbuttongroups)Added [UITextInputAssistantItem.trailingBarButtonGroups](https://developer.apple.com/documentation/uikit/uitextinputassistantitem/1614532-trailingbarbuttongroups)Added [UITextView.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uitextview/1618617-initwithcoder)Added [UITouch.force](https://developer.apple.com/documentation/uikit/uitouch/1618110-force)Added [UITouch.maximumPossibleForce](https://developer.apple.com/documentation/uikit/uitouch/1618121-maximumpossibleforce)Added [UITraitCollection.forceTouchCapability](https://developer.apple.com/documentation/uikit/uitraitcollection/1623515-forcetouchcapability)Added [UITraitCollection.init()](https://developer.apple.com/documentation/uikit/uitraitcollection/1623517-init)Added [UITraitCollection.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uitraitcollection/1623504-initwithcoder)Added [UITraitCollection.init(forceTouchCapability: UIForceTouchCapability)](https://developer.apple.com/documentation/uikit/uitraitcollection/1623511-traitcollectionwithforcetouchcap)Added [UIUserNotificationAction.behavior](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615399-behavior)Added [UIUserNotificationAction.init()](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615368-init)Added [UIUserNotificationAction.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615366-initwithcoder)Added [UIUserNotificationAction.parameters](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615337-parameters)Added [UIUserNotificationActionBehavior [enum]](https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior)Added [UIUserNotificationActionBehavior.Default](https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior/uiusernotificationactionbehaviordefault)Added [UIUserNotificationActionBehavior.TextInput](https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior/uiusernotificationactionbehaviortextinput)Added [UIUserNotificationCategory.init()](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/1615327-init)Added [UIUserNotificationCategory.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/1615391-initwithcoder)Added [UIView.addLayoutGuide(_: UILayoutGuide)](https://developer.apple.com/documentation/uikit/uiview/1622414-addlayoutguide)Added [UIView.bottomAnchor](https://developer.apple.com/documentation/uikit/uiview/1622483-bottomanchor)Added [UIView.centerXAnchor](https://developer.apple.com/documentation/uikit/uiview/1622596-centerxanchor)Added [UIView.centerYAnchor](https://developer.apple.com/documentation/uikit/uiview/1622447-centeryanchor)Added [UIView.constraints](https://developer.apple.com/documentation/uikit/uiview/1622464-constraints)Added [UIView.firstBaselineAnchor](https://developer.apple.com/documentation/uikit/uiview/1622508-firstbaselineanchor)Added [UIView.heightAnchor](https://developer.apple.com/documentation/uikit/uiview/1622590-heightanchor)Added [UIView.inheritedAnimationDuration() -> NSTimeInterval [class]](https://developer.apple.com/documentation/uikit/uiview/1622479-inheritedanimationduration)Added [UIView.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiview/1622477-init)Added [UIView.lastBaselineAnchor](https://developer.apple.com/documentation/uikit/uiview/1622471-lastbaselineanchor)Added [UIView.layoutGuides](https://developer.apple.com/documentation/uikit/uiview/1622536-layoutguides)Added [UIView.layoutMarginsGuide](https://developer.apple.com/documentation/uikit/uiview/1622651-layoutmarginsguide)Added [UIView.leadingAnchor](https://developer.apple.com/documentation/uikit/uiview/1622520-leadinganchor)Added [UIView.leftAnchor](https://developer.apple.com/documentation/uikit/uiview/1622435-leftanchor)Added [UIView.readableContentGuide](https://developer.apple.com/documentation/uikit/uiview/1622644-readablecontentguide)Added [UIView.removeLayoutGuide(_: UILayoutGuide)](https://developer.apple.com/documentation/uikit/uiview/1622506-removelayoutguide)Added [UIView.rightAnchor](https://developer.apple.com/documentation/uikit/uiview/1622579-rightanchor)Added [UIView.semanticContentAttribute](https://developer.apple.com/documentation/uikit/uiview/1622461-semanticcontentattribute)Added [UIView.topAnchor](https://developer.apple.com/documentation/uikit/uiview/1622613-topanchor)Added [UIView.trailingAnchor](https://developer.apple.com/documentation/uikit/uiview/1622522-trailinganchor)Added [UIView.translatesAutoresizingMaskIntoConstraints](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco)Added [UIView.userInterfaceLayoutDirectionForSemanticContentAttribute(_: UISemanticContentAttribute) -> UIUserInterfaceLayoutDirection [class]](https://developer.apple.com/documentation/uikit/uiview/1622480-userinterfacelayoutdirectionfors)Added [UIView.viewForFirstBaselineLayout](https://developer.apple.com/documentation/uikit/uiview/1622452-forfirstbaselinelayout)Added [UIView.viewForLastBaselineLayout](https://developer.apple.com/documentation/uikit/uiview/1622633-viewforlastbaselinelayout)Added [UIView.widthAnchor](https://developer.apple.com/documentation/uikit/uiview/1622605-widthanchor)Added [UIViewController.addKeyCommand(_: UIKeyCommand)](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621439-addkeycommand)Added [UIViewController.allowedChildViewControllersForUnwindingFromSource(_: UIStoryboardUnwindSegueSource) -> [UIViewController]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621371-allowedchildviewcontrollersforun)Added [UIViewController.childViewControllerContainingSegueSource(_: UIStoryboardUnwindSegueSource) -> UIViewController?](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621384-childcontaining)Added [UIViewController.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621403-initwithcoder)Added [UIViewController.loadViewIfNeeded()](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621446-loadviewifneeded)Added [UIViewController.previewActionItems() -> [UIPreviewActionItem]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621408-previewactionitems)Added [UIViewController.registerForPreviewingWithDelegate(_: UIViewControllerPreviewingDelegate, sourceView: UIView) -> UIViewControllerPreviewing](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621463-registerforpreviewing)Added [UIViewController.removeKeyCommand(_: UIKeyCommand)](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621410-removekeycommand)Added [UIViewController.unregisterForPreviewingWithContext(_: UIViewControllerPreviewing)](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621395-unregisterforpreviewing)Added [UIViewController.unwindForSegue(_: UIStoryboardSegue, towardsViewController: UIViewController)](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621473-unwindforsegue)Added [UIViewController.viewIfLoaded](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621360-viewifloaded)Added [UIViewControllerPreviewing](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing)Added [UIViewControllerPreviewing.delegate](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/1621422-delegate)Added [UIViewControllerPreviewing.previewingGestureRecognizerForFailureRelationship](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/1621467-previewinggesturerecognizerforfa)Added [UIViewControllerPreviewing.sourceRect](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/1621431-sourcerect)Added [UIViewControllerPreviewing.sourceView](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/1621436-sourceview)Added [UIViewControllerPreviewingDelegate](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate)Added [UIViewControllerPreviewingDelegate.previewingContext(_: UIViewControllerPreviewing, commitViewController: UIViewController)](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate/1621366-previewingcontext)Added [UIViewControllerPreviewingDelegate.previewingContext(_: UIViewControllerPreviewing, viewControllerForLocation: CGPoint) -> UIViewController?](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate/1621464-previewingcontext)Added [UIVisualEffectView.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uivisualeffectview/1615054-init)Added [UIWebView.allowsLinkPreview](https://developer.apple.com/documentation/uikit/uiwebview/1617976-allowslinkpreview)Added [UIWebView.allowsPictureInPictureMediaPlayback](https://developer.apple.com/documentation/uikit/uiwebview/1617944-allowspictureinpicturemediaplayb)Added ==(_: UIEdgeInsets, _: UIEdgeInsets) -> BoolAdded ==(_: UIOffset, _: UIOffset) -> BoolAdded [NSControlCharacterContainerBreakAction](https://developer.apple.com/documentation/uikit/1619233-anonymous/nscontrolcharactercontainerbreakaction)Added [NSControlCharacterHorizontalTabAction](https://developer.apple.com/documentation/uikit/nscontrolcharacterhorizontaltabaction)Added [NSControlCharacterLineBreakAction](https://developer.apple.com/documentation/uikit/nscontrolcharacterlinebreakaction)Added [NSControlCharacterParagraphBreakAction](https://developer.apple.com/documentation/uikit/1619233-anonymous/nscontrolcharacterparagraphbreakaction)Added [NSControlCharacterWhitespaceAction](https://developer.apple.com/documentation/uikit/1619233-anonymous/nscontrolcharacterwhitespaceaction)Added [NSControlCharacterZeroAdvancementAction](https://developer.apple.com/documentation/uikit/nscontrolcharacterzeroadvancementaction)Added [UIAccessibilityAssistiveTechnologyKey](https://developer.apple.com/documentation/uikit/uiaccessibilityassistivetechnologykey)Added [UIAccessibilityElementFocusedNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1620210-elementfocusednotification)Added [UIAccessibilityFocusedElement(_: String?) -> AnyObject?](https://developer.apple.com/documentation/uikit/1615119-uiaccessibilityfocusedelement)Added [UIAccessibilityFocusedElementKey](https://developer.apple.com/documentation/uikit/uiaccessibility/1620180-focusedelementuserinfokey)Added [UIAccessibilityIsShakeToUndoEnabled() -> Bool](https://developer.apple.com/documentation/uikit/1615103-uiaccessibilityisshaketoundoenab)Added [UIAccessibilityNotificationVoiceOverIdentifier](https://developer.apple.com/documentation/uikit/uiaccessibility/assistivetechnologyidentifier/1620184-notificationvoiceover)Added [UIAccessibilityShakeToUndoDidChangeNotification](https://developer.apple.com/documentation/uikit/uiaccessibilityshaketoundodidchangenotification)Added [UIAccessibilityUnfocusedElementKey](https://developer.apple.com/documentation/uikit/uiaccessibility/1620196-unfocusedelementuserinfokey)Added [UIActivityTypeOpenInIBooks](https://developer.apple.com/documentation/uikit/uiactivitytypeopeninibooks)Added [UIApplicationLaunchOptionsShortcutItemKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1622972-shortcutitem)Added [UIApplicationOpenURLOptionsAnnotationKey](https://developer.apple.com/documentation/uikit/uiapplicationopenurloptionsannotationkey)Added [UIApplicationOpenURLOptionsOpenInPlaceKey](https://developer.apple.com/documentation/uikit/uiapplicationopenurloptionsopeninplacekey)Added [UIApplicationOpenURLOptionsSourceApplicationKey](https://developer.apple.com/documentation/uikit/uiapplicationopenurloptionssourceapplicationkey)Added [UIFloatRangeInfinite](https://developer.apple.com/documentation/uikit/uifloatrange/1621319-infinite)Added [UIFloatRangeIsEqualToRange(_: UIFloatRange, _: UIFloatRange) -> Bool](https://developer.apple.com/documentation/uikit/1621316-uifloatrangeisequaltorange)Added [UIFloatRangeIsInfinite(_: UIFloatRange) -> Bool](https://developer.apple.com/documentation/uikit/1621299-uifloatrangeisinfinite)Added [UIFloatRangeMake(_: CGFloat, _: CGFloat) -> UIFloatRange](https://developer.apple.com/documentation/uikit/1621310-uifloatrangemake)Added [UIFloatRangeZero](https://developer.apple.com/documentation/uikit/uifloatrangezero)Added [UIFontTextStyleCallout](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616710-callout)Added [UIFontTextStyleTitle1](https://developer.apple.com/documentation/uikit/uifonttextstyletitle1)Added [UIFontTextStyleTitle2](https://developer.apple.com/documentation/uikit/uifonttextstyletitle2)Added [UIFontTextStyleTitle3](https://developer.apple.com/documentation/uikit/uifont/textstyle/1616673-title3)Added [UIKeyboardIsLocalUserInfoKey](https://developer.apple.com/documentation/uikit/uiresponder/1621603-keyboardislocaluserinfokey)Added [UIUserNotificationActionResponseTypedTextKey](https://developer.apple.com/documentation/watchkit/uiusernotificationactionresponsetypedtextkey)Added [UIUserNotificationTextInputActionButtonTitleKey](https://developer.apple.com/documentation/uikit/uiusernotificationtextinputactionbuttontitlekey)Modified [CIColor.init(color: UIColor)](https://developer.apple.com/documentation/coreimage/cicolor/1528762-initwithcolor)

|  | Declaration |
| --- | --- |
| From | ``` init?(color color: UIColor) ``` |
| To | ``` convenience init(color color: UIColor) ``` |

Modified [CIImage.init(image: UIImage)](https://developer.apple.com/documentation/coreimage/ciimage/1624119-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(image image: UIImage!) ``` |
| To | ``` init?(image image: UIImage) ``` |

Modified [CIImage.init(image: UIImage, options: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1624098-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(image image: UIImage!, options options: [NSObject : AnyObject]!) ``` |
| To | ``` init?(image image: UIImage, options options: [NSObject : AnyObject]?) ``` |

Modified [NSAttributedString.dataFromRange(_: NSRange, documentAttributes: [String : AnyObject]) throws -> NSData](https://developer.apple.com/documentation/foundation/nsattributedstring/1534090-data)

|  | Declaration |
| --- | --- |
| From | ``` func dataFromRange(_ range: NSRange, documentAttributes dict: [NSObject : AnyObject], error error: NSErrorPointer) -> NSData? ``` |
| To | ``` func dataFromRange(_ range: NSRange, documentAttributes dict: [String : AnyObject]) throws -> NSData ``` |

Modified [NSAttributedString.fileWrapperFromRange(_: NSRange, documentAttributes: [String : AnyObject]) throws -> NSFileWrapper](https://developer.apple.com/documentation/foundation/nsattributedstring/1530461-filewrapperfromrange)

|  | Declaration |
| --- | --- |
| From | ``` func fileWrapperFromRange(_ range: NSRange, documentAttributes dict: [NSObject : AnyObject], error error: NSErrorPointer) -> NSFileWrapper? ``` |
| To | ``` func fileWrapperFromRange(_ range: NSRange, documentAttributes dict: [String : AnyObject]) throws -> NSFileWrapper ``` |

Modified [NSAttributedString.init(attachment: NSTextAttachment)](https://developer.apple.com/documentation/foundation/nsattributedstring/1508376-attributedstringwithattachment)

|  | Declaration |
| --- | --- |
| From | ``` init(attachment attachment: NSTextAttachment) -> NSAttributedString ``` |
| To | ``` init(attachment attachment: NSTextAttachment) ``` |

Modified [NSAttributedString.init(data: NSData, options: [String : AnyObject], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws](https://developer.apple.com/documentation/foundation/nsattributedstring/1524613-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(data data: NSData, options options: [NSObject : AnyObject]?, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error error: NSErrorPointer) ``` |
| To | ``` init(data data: NSData, options options: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws ``` |

Modified [NSAttributedString.init(fileURL: NSURL, options: [NSObject : AnyObject], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws](https://developer.apple.com/documentation/foundation/nsattributedstring/1620492-init)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` init?(fileURL url: NSURL!, options options: [NSObject : AnyObject]!, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error error: NSErrorPointer) ``` | -- |
| To | ``` init(fileURL url: NSURL, options options: [NSObject : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws ``` | iOS 9.0 |

Modified [NSCoder.decodeCGAffineTransformForKey(_: String) -> CGAffineTransform](https://developer.apple.com/documentation/foundation/nscoder/1624478-decodecgaffinetransformforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCGAffineTransformForKey(_ key: String!) -> CGAffineTransform ``` |
| To | ``` func decodeCGAffineTransformForKey(_ key: String) -> CGAffineTransform ``` |

Modified [NSCoder.decodeCGPointForKey(_: String) -> CGPoint](https://developer.apple.com/documentation/foundation/nscoder/1624523-decodecgpointforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCGPointForKey(_ key: String!) -> CGPoint ``` |
| To | ``` func decodeCGPointForKey(_ key: String) -> CGPoint ``` |

Modified [NSCoder.decodeCGRectForKey(_: String) -> CGRect](https://developer.apple.com/documentation/foundation/nscoder/1624522-decodecgrect)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCGRectForKey(_ key: String!) -> CGRect ``` |
| To | ``` func decodeCGRectForKey(_ key: String) -> CGRect ``` |

Modified [NSCoder.decodeCGSizeForKey(_: String) -> CGSize](https://developer.apple.com/documentation/foundation/nscoder/1624519-decodecgsizeforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCGSizeForKey(_ key: String!) -> CGSize ``` |
| To | ``` func decodeCGSizeForKey(_ key: String) -> CGSize ``` |

Modified [NSCoder.decodeCGVectorForKey(_: String) -> CGVector](https://developer.apple.com/documentation/foundation/nscoder/1624488-decodecgvectorforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeCGVectorForKey(_ key: String!) -> CGVector ``` |
| To | ``` func decodeCGVectorForKey(_ key: String) -> CGVector ``` |

Modified [NSCoder.decodeUIEdgeInsetsForKey(_: String) -> UIEdgeInsets](https://developer.apple.com/documentation/foundation/nscoder/1624492-decodeuiedgeinsetsforkey)

|  | Declaration |
| --- | --- |
| From | ``` func decodeUIEdgeInsetsForKey(_ key: String!) -> UIEdgeInsets ``` |
| To | ``` func decodeUIEdgeInsetsForKey(_ key: String) -> UIEdgeInsets ``` |

Modified [NSCoder.decodeUIOffsetForKey(_: String) -> UIOffset](https://developer.apple.com/documentation/foundation/nscoder/1624507-decodeuioffset)

|  | Declaration |
| --- | --- |
| From | ``` func decodeUIOffsetForKey(_ key: String!) -> UIOffset ``` |
| To | ``` func decodeUIOffsetForKey(_ key: String) -> UIOffset ``` |

Modified [NSCoder.encodeCGAffineTransform(_: CGAffineTransform, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624502-encodecgaffinetransform)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCGAffineTransform(_ transform: CGAffineTransform, forKey key: String!) ``` |
| To | ``` func encodeCGAffineTransform(_ transform: CGAffineTransform, forKey key: String) ``` |

Modified [NSCoder.encodeCGPoint(_: CGPoint, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624520-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCGPoint(_ point: CGPoint, forKey key: String!) ``` |
| To | ``` func encodeCGPoint(_ point: CGPoint, forKey key: String) ``` |

Modified [NSCoder.encodeCGRect(_: CGRect, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624472-encodecgrect)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCGRect(_ rect: CGRect, forKey key: String!) ``` |
| To | ``` func encodeCGRect(_ rect: CGRect, forKey key: String) ``` |

Modified [NSCoder.encodeCGSize(_: CGSize, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624482-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCGSize(_ size: CGSize, forKey key: String!) ``` |
| To | ``` func encodeCGSize(_ size: CGSize, forKey key: String) ``` |

Modified [NSCoder.encodeCGVector(_: CGVector, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624532-encodecgvector)

|  | Declaration |
| --- | --- |
| From | ``` func encodeCGVector(_ vector: CGVector, forKey key: String!) ``` |
| To | ``` func encodeCGVector(_ vector: CGVector, forKey key: String) ``` |

Modified [NSCoder.encodeUIEdgeInsets(_: UIEdgeInsets, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624481-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeUIEdgeInsets(_ insets: UIEdgeInsets, forKey key: String!) ``` |
| To | ``` func encodeUIEdgeInsets(_ insets: UIEdgeInsets, forKey key: String) ``` |

Modified [NSCoder.encodeUIOffset(_: UIOffset, forKey: String)](https://developer.apple.com/documentation/foundation/nscoder/1624494-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeUIOffset(_ offset: UIOffset, forKey key: String!) ``` |
| To | ``` func encodeUIOffset(_ offset: UIOffset, forKey key: String) ``` |

Modified [NSControlCharacterAction [enum]](https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NSControlCharacterAction : Int {     case ZeroAdvancementAction     case WhitespaceAction     case HorizontalTabAction     case LineBreakAction     case ParagraphBreakAction     case ContainerBreakAction } ``` | -- |
| To | ``` enum NSControlCharacterAction : Int {     case ZeroAdvancement     case Whitespace     case HorizontalTab     case LineBreak     case ParagraphBreak     case ContainerBreak } ``` | Int |

Modified [NSFileProviderExtension](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension)

|  | Declaration |
| --- | --- |
| From | ``` class NSFileProviderExtension : NSObject {     class func writePlaceholderAtURL(_ placeholderURL: NSURL, withMetadata metadata: [NSObject : AnyObject], error error: NSErrorPointer) -> Bool     class func placeholderURLForURL(_ url: NSURL) -> NSURL     func providerIdentifier() -> String     func documentStorageURL() -> NSURL     func URLForItemWithPersistentIdentifier(_ identifier: String) -> NSURL!     func persistentIdentifierForItemAtURL(_ url: NSURL) -> String     func providePlaceholderAtURL(_ url: NSURL, completionHandler completionHandler: ((NSError!) -> Void)?)     func startProvidingItemAtURL(_ url: NSURL, completionHandler completionHandler: ((NSError!) -> Void)!)     func itemChangedAtURL(_ url: NSURL)     func stopProvidingItemAtURL(_ url: NSURL) } ``` |
| To | ``` class NSFileProviderExtension : NSObject {     class func writePlaceholderAtURL(_ placeholderURL: NSURL, withMetadata metadata: [NSObject : AnyObject]) throws     class func placeholderURLForURL(_ url: NSURL) -> NSURL     func providerIdentifier() -> String     func documentStorageURL() -> NSURL     func URLForItemWithPersistentIdentifier(_ identifier: String) -> NSURL?     func persistentIdentifierForItemAtURL(_ url: NSURL) -> String?     func providePlaceholderAtURL(_ url: NSURL, completionHandler completionHandler: (NSError?) -> Void)     func startProvidingItemAtURL(_ url: NSURL, completionHandler completionHandler: (NSError?) -> Void)     func itemChangedAtURL(_ url: NSURL)     func stopProvidingItemAtURL(_ url: NSURL) } ``` |

Modified [NSFileProviderExtension.persistentIdentifierForItemAtURL(_: NSURL) -> String?](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623479-persistentidentifierforitematurl)

|  | Declaration |
| --- | --- |
| From | ``` func persistentIdentifierForItemAtURL(_ url: NSURL) -> String ``` |
| To | ``` func persistentIdentifierForItemAtURL(_ url: NSURL) -> String? ``` |

Modified [NSFileProviderExtension.providePlaceholderAtURL(_: NSURL, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623483-provideplaceholderaturl)

|  | Declaration |
| --- | --- |
| From | ``` func providePlaceholderAtURL(_ url: NSURL, completionHandler completionHandler: ((NSError!) -> Void)?) ``` |
| To | ``` func providePlaceholderAtURL(_ url: NSURL, completionHandler completionHandler: (NSError?) -> Void) ``` |

Modified [NSFileProviderExtension.startProvidingItemAtURL(_: NSURL, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623482-startprovidingitem)

|  | Declaration |
| --- | --- |
| From | ``` func startProvidingItemAtURL(_ url: NSURL, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func startProvidingItemAtURL(_ url: NSURL, completionHandler completionHandler: (NSError?) -> Void) ``` |

Modified [NSFileProviderExtension.URLForItemWithPersistentIdentifier(_: String) -> NSURL?](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623481-urlforitemwithpersistentidentifi)

|  | Declaration |
| --- | --- |
| From | ``` func URLForItemWithPersistentIdentifier(_ identifier: String) -> NSURL! ``` |
| To | ``` func URLForItemWithPersistentIdentifier(_ identifier: String) -> NSURL? ``` |

Modified [NSFileProviderExtension.writePlaceholderAtURL(_: NSURL, withMetadata: [NSObject : AnyObject]) throws [class]](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/1623475-writeplaceholderaturl)

|  | Declaration |
| --- | --- |
| From | ``` class func writePlaceholderAtURL(_ placeholderURL: NSURL, withMetadata metadata: [NSObject : AnyObject], error error: NSErrorPointer) -> Bool ``` |
| To | ``` class func writePlaceholderAtURL(_ placeholderURL: NSURL, withMetadata metadata: [NSObject : AnyObject]) throws ``` |

Modified [NSGlyphProperty [enum]](https://developer.apple.com/documentation/uikit/nsglyphproperty)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSIndexPath.init(forItem: Int, inSection: Int)](https://developer.apple.com/documentation/foundation/nsindexpath/1526053-indexpathforitem)

|  | Declaration |
| --- | --- |
| From | ``` init!(forItem item: Int, inSection section: Int) -> NSIndexPath ``` |
| To | ``` convenience init(forItem item: Int, inSection section: Int) ``` |

Modified [NSIndexPath.init(forRow: Int, inSection: Int)](https://developer.apple.com/documentation/foundation/nsindexpath/1614934-indexpathforrow)

|  | Declaration |
| --- | --- |
| From | ``` init!(forRow row: Int, inSection section: Int) -> NSIndexPath ``` |
| To | ``` convenience init(forRow row: Int, inSection section: Int) ``` |

Modified [NSLayoutAttribute [enum]](https://developer.apple.com/documentation/appkit/nslayoutattribute)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NSLayoutAttribute : Int {     case Left     case Right     case Top     case Bottom     case Leading     case Trailing     case Width     case Height     case CenterX     case CenterY     case Baseline     case FirstBaseline     case LeftMargin     case RightMargin     case TopMargin     case BottomMargin     case LeadingMargin     case TrailingMargin     case CenterXWithinMargins     case CenterYWithinMargins     case NotAnAttribute } ``` | -- |
| To | ``` enum NSLayoutAttribute : Int {     case Left     case Right     case Top     case Bottom     case Leading     case Trailing     case Width     case Height     case CenterX     case CenterY     case Baseline     static var LastBaseline: NSLayoutAttribute { get }     case FirstBaseline     case LeftMargin     case RightMargin     case TopMargin     case BottomMargin     case LeadingMargin     case TrailingMargin     case CenterXWithinMargins     case CenterYWithinMargins     case NotAnAttribute } ``` | Int |

Modified [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint)

|  | Declaration |
| --- | --- |
| From | ``` class NSLayoutConstraint : NSObject {     class func constraintsWithVisualFormat(_ format: String, options opts: NSLayoutFormatOptions, metrics metrics: [NSObject : AnyObject]?, views views: [NSObject : AnyObject]) -> [AnyObject]     convenience init(item view1: AnyObject, attribute attr1: NSLayoutAttribute, relatedBy relation: NSLayoutRelation, toItem view2: AnyObject?, attribute attr2: NSLayoutAttribute, multiplier multiplier: CGFloat, constant c: CGFloat)     class func constraintWithItem(_ view1: AnyObject, attribute attr1: NSLayoutAttribute, relatedBy relation: NSLayoutRelation, toItem view2: AnyObject?, attribute attr2: NSLayoutAttribute, multiplier multiplier: CGFloat, constant c: CGFloat) -> Self     var priority: UILayoutPriority     var shouldBeArchived: Bool     unowned(unsafe) var firstItem: AnyObject { get }     var firstAttribute: NSLayoutAttribute { get }     var relation: NSLayoutRelation { get }     unowned(unsafe) var secondItem: AnyObject? { get }     var secondAttribute: NSLayoutAttribute { get }     var multiplier: CGFloat { get }     var constant: CGFloat     var active: Bool     class func activateConstraints(_ constraints: [AnyObject])     class func deactivateConstraints(_ constraints: [AnyObject]) } extension NSLayoutConstraint {     var identifier: String? } ``` |
| To | ``` class NSLayoutConstraint : NSObject {     class func constraintsWithVisualFormat(_ format: String, options opts: NSLayoutFormatOptions, metrics metrics: [String : AnyObject]?, views views: [String : AnyObject]) -> [NSLayoutConstraint]     convenience init(item view1: AnyObject, attribute attr1: NSLayoutAttribute, relatedBy relation: NSLayoutRelation, toItem view2: AnyObject?, attribute attr2: NSLayoutAttribute, multiplier multiplier: CGFloat, constant c: CGFloat)     class func constraintWithItem(_ view1: AnyObject, attribute attr1: NSLayoutAttribute, relatedBy relation: NSLayoutRelation, toItem view2: AnyObject?, attribute attr2: NSLayoutAttribute, multiplier multiplier: CGFloat, constant c: CGFloat) -> Self     var priority: UILayoutPriority     var shouldBeArchived: Bool     unowned(unsafe) var firstItem: AnyObject { get }     var firstAttribute: NSLayoutAttribute { get }     var relation: NSLayoutRelation { get }     unowned(unsafe) var secondItem: AnyObject? { get }     var secondAttribute: NSLayoutAttribute { get }     var multiplier: CGFloat { get }     var constant: CGFloat     var active: Bool     class func activateConstraints(_ constraints: [NSLayoutConstraint])     class func deactivateConstraints(_ constraints: [NSLayoutConstraint]) } extension NSLayoutConstraint {     var identifier: String? } ``` |

Modified [NSLayoutConstraint.activateConstraints(_: [NSLayoutConstraint]) [class]](https://developer.apple.com/documentation/uikit/nslayoutconstraint/1526955-activateconstraints)

|  | Declaration |
| --- | --- |
| From | ``` class func activateConstraints(_ constraints: [AnyObject]) ``` |
| To | ``` class func activateConstraints(_ constraints: [NSLayoutConstraint]) ``` |

Modified [NSLayoutConstraint.constraintsWithVisualFormat(_: String, options: NSLayoutFormatOptions, metrics: [String : AnyObject]?, views: [String : AnyObject]) -> [NSLayoutConstraint] [class]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526944-constraints)

|  | Declaration |
| --- | --- |
| From | ``` class func constraintsWithVisualFormat(_ format: String, options opts: NSLayoutFormatOptions, metrics metrics: [NSObject : AnyObject]?, views views: [NSObject : AnyObject]) -> [AnyObject] ``` |
| To | ``` class func constraintsWithVisualFormat(_ format: String, options opts: NSLayoutFormatOptions, metrics metrics: [String : AnyObject]?, views views: [String : AnyObject]) -> [NSLayoutConstraint] ``` |

Modified [NSLayoutConstraint.deactivateConstraints(_: [NSLayoutConstraint]) [class]](https://developer.apple.com/documentation/appkit/nslayoutconstraint/1526066-deactivate)

|  | Declaration |
| --- | --- |
| From | ``` class func deactivateConstraints(_ constraints: [AnyObject]) ``` |
| To | ``` class func deactivateConstraints(_ constraints: [NSLayoutConstraint]) ``` |

Modified [NSLayoutFormatOptions [struct]](https://developer.apple.com/documentation/uikit/nslayoutconstraint/formatoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSLayoutFormatOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var AlignAllLeft: NSLayoutFormatOptions { get }     static var AlignAllRight: NSLayoutFormatOptions { get }     static var AlignAllTop: NSLayoutFormatOptions { get }     static var AlignAllBottom: NSLayoutFormatOptions { get }     static var AlignAllLeading: NSLayoutFormatOptions { get }     static var AlignAllTrailing: NSLayoutFormatOptions { get }     static var AlignAllCenterX: NSLayoutFormatOptions { get }     static var AlignAllCenterY: NSLayoutFormatOptions { get }     static var AlignAllBaseline: NSLayoutFormatOptions { get }     static var AlignAllLastBaseline: NSLayoutFormatOptions { get }     static var AlignAllFirstBaseline: NSLayoutFormatOptions { get }     static var AlignmentMask: NSLayoutFormatOptions { get }     static var DirectionLeadingToTrailing: NSLayoutFormatOptions { get }     static var DirectionLeftToRight: NSLayoutFormatOptions { get }     static var DirectionRightToLeft: NSLayoutFormatOptions { get }     static var DirectionMask: NSLayoutFormatOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSLayoutFormatOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var AlignAllLeft: NSLayoutFormatOptions { get }     static var AlignAllRight: NSLayoutFormatOptions { get }     static var AlignAllTop: NSLayoutFormatOptions { get }     static var AlignAllBottom: NSLayoutFormatOptions { get }     static var AlignAllLeading: NSLayoutFormatOptions { get }     static var AlignAllTrailing: NSLayoutFormatOptions { get }     static var AlignAllCenterX: NSLayoutFormatOptions { get }     static var AlignAllCenterY: NSLayoutFormatOptions { get }     static var AlignAllBaseline: NSLayoutFormatOptions { get }     static var AlignAllLastBaseline: NSLayoutFormatOptions { get }     static var AlignAllFirstBaseline: NSLayoutFormatOptions { get }     static var AlignmentMask: NSLayoutFormatOptions { get }     static var DirectionLeadingToTrailing: NSLayoutFormatOptions { get }     static var DirectionLeftToRight: NSLayoutFormatOptions { get }     static var DirectionRightToLeft: NSLayoutFormatOptions { get }     static var DirectionMask: NSLayoutFormatOptions { get } } ``` | OptionSetType |

Modified [NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager)

|  | Declaration |
| --- | --- |
| From | ``` class NSLayoutManager : NSObject, NSCoding {     unowned(unsafe) var textStorage: NSTextStorage?     var textContainers: [AnyObject] { get }     func addTextContainer(_ container: NSTextContainer)     func insertTextContainer(_ container: NSTextContainer, atIndex index: Int)     func removeTextContainerAtIndex(_ index: Int)     func textContainerChangedGeometry(_ container: NSTextContainer)     unowned(unsafe) var delegate: NSLayoutManagerDelegate?     var showsInvisibleCharacters: Bool     var showsControlCharacters: Bool     var hyphenationFactor: CGFloat     var usesFontLeading: Bool     var allowsNonContiguousLayout: Bool     var hasNonContiguousLayout: Bool { get }     func invalidateGlyphsForCharacterRange(_ charRange: NSRange, changeInLength delta: Int, actualCharacterRange actualCharRange: NSRangePointer)     func invalidateLayoutForCharacterRange(_ charRange: NSRange, actualCharacterRange actualCharRange: NSRangePointer)     func invalidateDisplayForCharacterRange(_ charRange: NSRange)     func invalidateDisplayForGlyphRange(_ glyphRange: NSRange)     func processEditingForTextStorage(_ textStorage: NSTextStorage, edited editMask: NSTextStorageEditActions, range newCharRange: NSRange, changeInLength delta: Int, invalidatedRange invalidatedCharRange: NSRange)     func ensureGlyphsForCharacterRange(_ charRange: NSRange)     func ensureGlyphsForGlyphRange(_ glyphRange: NSRange)     func ensureLayoutForCharacterRange(_ charRange: NSRange)     func ensureLayoutForGlyphRange(_ glyphRange: NSRange)     func ensureLayoutForTextContainer(_ container: NSTextContainer)     func ensureLayoutForBoundingRect(_ bounds: CGRect, inTextContainer container: NSTextContainer)     func setGlyphs(_ glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSGlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont?, forGlyphRange glyphRange: NSRange)     var numberOfGlyphs: Int { get }     func glyphAtIndex(_ glyphIndex: Int, isValidIndex isValidIndex: UnsafeMutablePointer<ObjCBool>) -> CGGlyph     func glyphAtIndex(_ glyphIndex: Int) -> CGGlyph     func isValidGlyphIndex(_ glyphIndex: Int) -> Bool     func propertyForGlyphAtIndex(_ glyphIndex: Int) -> NSGlyphProperty     func characterIndexForGlyphAtIndex(_ glyphIndex: Int) -> Int     func glyphIndexForCharacterAtIndex(_ charIndex: Int) -> Int     func getGlyphsInRange(_ glyphRange: NSRange, glyphs glyphBuffer: UnsafeMutablePointer<CGGlyph>, properties props: UnsafeMutablePointer<NSGlyphProperty>, characterIndexes charIndexBuffer: UnsafeMutablePointer<Int>, bidiLevels bidiLevelBuffer: UnsafeMutablePointer<UInt8>) -> Int     func setTextContainer(_ container: NSTextContainer?, forGlyphRange glyphRange: NSRange)     func setLineFragmentRect(_ fragmentRect: CGRect, forGlyphRange glyphRange: NSRange, usedRect usedRect: CGRect)     func setExtraLineFragmentRect(_ fragmentRect: CGRect, usedRect usedRect: CGRect, textContainer container: NSTextContainer?)     func setLocation(_ location: CGPoint, forStartOfGlyphRange glyphRange: NSRange)     func setNotShownAttribute(_ flag: Bool, forGlyphAtIndex glyphIndex: Int)     func setDrawsOutsideLineFragment(_ flag: Bool, forGlyphAtIndex glyphIndex: Int)     func setAttachmentSize(_ attachmentSize: CGSize, forGlyphRange glyphRange: NSRange)     func getFirstUnlaidCharacterIndex(_ charIndex: UnsafeMutablePointer<Int>, glyphIndex glyphIndex: UnsafeMutablePointer<Int>)     func firstUnlaidCharacterIndex() -> Int     func firstUnlaidGlyphIndex() -> Int     func textContainerForGlyphAtIndex(_ glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer) -> NSTextContainer?     func usedRectForTextContainer(_ container: NSTextContainer) -> CGRect     func lineFragmentRectForGlyphAtIndex(_ glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer) -> CGRect     func lineFragmentUsedRectForGlyphAtIndex(_ glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer) -> CGRect     var extraLineFragmentRect: CGRect { get }     var extraLineFragmentUsedRect: CGRect { get }     var extraLineFragmentTextContainer: NSTextContainer? { get }     func locationForGlyphAtIndex(_ glyphIndex: Int) -> CGPoint     func notShownAttributeForGlyphAtIndex(_ glyphIndex: Int) -> Bool     func drawsOutsideLineFragmentForGlyphAtIndex(_ glyphIndex: Int) -> Bool     func attachmentSizeForGlyphAtIndex(_ glyphIndex: Int) -> CGSize     func truncatedGlyphRangeInLineFragmentForGlyphAtIndex(_ glyphIndex: Int) -> NSRange     func glyphRangeForCharacterRange(_ charRange: NSRange, actualCharacterRange actualCharRange: NSRangePointer) -> NSRange     func characterRangeForGlyphRange(_ glyphRange: NSRange, actualGlyphRange actualGlyphRange: NSRangePointer) -> NSRange     func glyphRangeForTextContainer(_ container: NSTextContainer) -> NSRange     func rangeOfNominallySpacedGlyphsContainingIndex(_ glyphIndex: Int) -> NSRange     func boundingRectForGlyphRange(_ glyphRange: NSRange, inTextContainer container: NSTextContainer) -> CGRect     func glyphRangeForBoundingRect(_ bounds: CGRect, inTextContainer container: NSTextContainer) -> NSRange     func glyphRangeForBoundingRectWithoutAdditionalLayout(_ bounds: CGRect, inTextContainer container: NSTextContainer) -> NSRange     func glyphIndexForPoint(_ point: CGPoint, inTextContainer container: NSTextContainer, fractionOfDistanceThroughGlyph partialFraction: UnsafeMutablePointer<CGFloat>) -> Int     func glyphIndexForPoint(_ point: CGPoint, inTextContainer container: NSTextContainer) -> Int     func fractionOfDistanceThroughGlyphForPoint(_ point: CGPoint, inTextContainer container: NSTextContainer) -> CGFloat     func characterIndexForPoint(_ point: CGPoint, inTextContainer container: NSTextContainer, fractionOfDistanceBetweenInsertionPoints partialFraction: UnsafeMutablePointer<CGFloat>) -> Int     func getLineFragmentInsertionPointsForCharacterAtIndex(_ charIndex: Int, alternatePositions aFlag: Bool, inDisplayOrder dFlag: Bool, positions positions: UnsafeMutablePointer<CGFloat>, characterIndexes charIndexes: UnsafeMutablePointer<Int>) -> Int     func enumerateLineFragmentsForGlyphRange(_ glyphRange: NSRange, usingBlock block: (CGRect, CGRect, NSTextContainer!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateEnclosingRectsForGlyphRange(_ glyphRange: NSRange, withinSelectedGlyphRange selectedRange: NSRange, inTextContainer textContainer: NSTextContainer, usingBlock block: (CGRect, UnsafeMutablePointer<ObjCBool>) -> Void)     func drawBackgroundForGlyphRange(_ glyphsToShow: NSRange, atPoint origin: CGPoint)     func drawGlyphsForGlyphRange(_ glyphsToShow: NSRange, atPoint origin: CGPoint)     func showCGGlyphs(_ glyphs: UnsafePointer<CGGlyph>, positions positions: UnsafePointer<CGPoint>, count glyphCount: Int, font font: UIFont, matrix textMatrix: CGAffineTransform, attributes attributes: [NSObject : AnyObject]?, inContext graphicsContext: CGContext?)     func fillBackgroundRectArray(_ rectArray: UnsafePointer<CGRect>, count rectCount: Int, forCharacterRange charRange: NSRange, color color: UIColor)     func drawUnderlineForGlyphRange(_ glyphRange: NSRange, underlineType underlineVal: NSUnderlineStyle, baselineOffset baselineOffset: CGFloat, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin containerOrigin: CGPoint)     func underlineGlyphRange(_ glyphRange: NSRange, underlineType underlineVal: NSUnderlineStyle, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin containerOrigin: CGPoint)     func drawStrikethroughForGlyphRange(_ glyphRange: NSRange, strikethroughType strikethroughVal: NSUnderlineStyle, baselineOffset baselineOffset: CGFloat, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin containerOrigin: CGPoint)     func strikethroughGlyphRange(_ glyphRange: NSRange, strikethroughType strikethroughVal: NSUnderlineStyle, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin containerOrigin: CGPoint) } ``` |
| To | ``` class NSLayoutManager : NSObject, NSCoding {     init()     init?(coder coder: NSCoder)     unowned(unsafe) var textStorage: NSTextStorage?     var textContainers: [NSTextContainer] { get }     func addTextContainer(_ container: NSTextContainer)     func insertTextContainer(_ container: NSTextContainer, atIndex index: Int)     func removeTextContainerAtIndex(_ index: Int)     func textContainerChangedGeometry(_ container: NSTextContainer)     unowned(unsafe) var delegate: NSLayoutManagerDelegate?     var showsInvisibleCharacters: Bool     var showsControlCharacters: Bool     var hyphenationFactor: CGFloat     var usesFontLeading: Bool     var allowsNonContiguousLayout: Bool     var hasNonContiguousLayout: Bool { get }     func invalidateGlyphsForCharacterRange(_ charRange: NSRange, changeInLength delta: Int, actualCharacterRange actualCharRange: NSRangePointer)     func invalidateLayoutForCharacterRange(_ charRange: NSRange, actualCharacterRange actualCharRange: NSRangePointer)     func invalidateDisplayForCharacterRange(_ charRange: NSRange)     func invalidateDisplayForGlyphRange(_ glyphRange: NSRange)     func processEditingForTextStorage(_ textStorage: NSTextStorage, edited editMask: NSTextStorageEditActions, range newCharRange: NSRange, changeInLength delta: Int, invalidatedRange invalidatedCharRange: NSRange)     func ensureGlyphsForCharacterRange(_ charRange: NSRange)     func ensureGlyphsForGlyphRange(_ glyphRange: NSRange)     func ensureLayoutForCharacterRange(_ charRange: NSRange)     func ensureLayoutForGlyphRange(_ glyphRange: NSRange)     func ensureLayoutForTextContainer(_ container: NSTextContainer)     func ensureLayoutForBoundingRect(_ bounds: CGRect, inTextContainer container: NSTextContainer)     func setGlyphs(_ glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSGlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont, forGlyphRange glyphRange: NSRange)     var numberOfGlyphs: Int { get }     func CGGlyphAtIndex(_ glyphIndex: Int, isValidIndex isValidIndex: UnsafeMutablePointer<ObjCBool>) -> CGGlyph     func CGGlyphAtIndex(_ glyphIndex: Int) -> CGGlyph     func isValidGlyphIndex(_ glyphIndex: Int) -> Bool     func propertyForGlyphAtIndex(_ glyphIndex: Int) -> NSGlyphProperty     func characterIndexForGlyphAtIndex(_ glyphIndex: Int) -> Int     func glyphIndexForCharacterAtIndex(_ charIndex: Int) -> Int     func getGlyphsInRange(_ glyphRange: NSRange, glyphs glyphBuffer: UnsafeMutablePointer<CGGlyph>, properties props: UnsafeMutablePointer<NSGlyphProperty>, characterIndexes charIndexBuffer: UnsafeMutablePointer<Int>, bidiLevels bidiLevelBuffer: UnsafeMutablePointer<UInt8>) -> Int     func setTextContainer(_ container: NSTextContainer, forGlyphRange glyphRange: NSRange)     func setLineFragmentRect(_ fragmentRect: CGRect, forGlyphRange glyphRange: NSRange, usedRect usedRect: CGRect)     func setExtraLineFragmentRect(_ fragmentRect: CGRect, usedRect usedRect: CGRect, textContainer container: NSTextContainer)     func setLocation(_ location: CGPoint, forStartOfGlyphRange glyphRange: NSRange)     func setNotShownAttribute(_ flag: Bool, forGlyphAtIndex glyphIndex: Int)     func setDrawsOutsideLineFragment(_ flag: Bool, forGlyphAtIndex glyphIndex: Int)     func setAttachmentSize(_ attachmentSize: CGSize, forGlyphRange glyphRange: NSRange)     func getFirstUnlaidCharacterIndex(_ charIndex: UnsafeMutablePointer<Int>, glyphIndex glyphIndex: UnsafeMutablePointer<Int>)     func firstUnlaidCharacterIndex() -> Int     func firstUnlaidGlyphIndex() -> Int     func textContainerForGlyphAtIndex(_ glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer) -> NSTextContainer?     func textContainerForGlyphAtIndex(_ glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer, withoutAdditionalLayout flag: Bool) -> NSTextContainer?     func usedRectForTextContainer(_ container: NSTextContainer) -> CGRect     func lineFragmentRectForGlyphAtIndex(_ glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer) -> CGRect     func lineFragmentRectForGlyphAtIndex(_ glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer, withoutAdditionalLayout flag: Bool) -> CGRect     func lineFragmentUsedRectForGlyphAtIndex(_ glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer) -> CGRect     func lineFragmentUsedRectForGlyphAtIndex(_ glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer, withoutAdditionalLayout flag: Bool) -> CGRect     var extraLineFragmentRect: CGRect { get }     var extraLineFragmentUsedRect: CGRect { get }     var extraLineFragmentTextContainer: NSTextContainer? { get }     func locationForGlyphAtIndex(_ glyphIndex: Int) -> CGPoint     func notShownAttributeForGlyphAtIndex(_ glyphIndex: Int) -> Bool     func drawsOutsideLineFragmentForGlyphAtIndex(_ glyphIndex: Int) -> Bool     func attachmentSizeForGlyphAtIndex(_ glyphIndex: Int) -> CGSize     func truncatedGlyphRangeInLineFragmentForGlyphAtIndex(_ glyphIndex: Int) -> NSRange     func glyphRangeForCharacterRange(_ charRange: NSRange, actualCharacterRange actualCharRange: NSRangePointer) -> NSRange     func characterRangeForGlyphRange(_ glyphRange: NSRange, actualGlyphRange actualGlyphRange: NSRangePointer) -> NSRange     func glyphRangeForTextContainer(_ container: NSTextContainer) -> NSRange     func rangeOfNominallySpacedGlyphsContainingIndex(_ glyphIndex: Int) -> NSRange     func boundingRectForGlyphRange(_ glyphRange: NSRange, inTextContainer container: NSTextContainer) -> CGRect     func glyphRangeForBoundingRect(_ bounds: CGRect, inTextContainer container: NSTextContainer) -> NSRange     func glyphRangeForBoundingRectWithoutAdditionalLayout(_ bounds: CGRect, inTextContainer container: NSTextContainer) -> NSRange     func glyphIndexForPoint(_ point: CGPoint, inTextContainer container: NSTextContainer, fractionOfDistanceThroughGlyph partialFraction: UnsafeMutablePointer<CGFloat>) -> Int     func glyphIndexForPoint(_ point: CGPoint, inTextContainer container: NSTextContainer) -> Int     func fractionOfDistanceThroughGlyphForPoint(_ point: CGPoint, inTextContainer container: NSTextContainer) -> CGFloat     func characterIndexForPoint(_ point: CGPoint, inTextContainer container: NSTextContainer, fractionOfDistanceBetweenInsertionPoints partialFraction: UnsafeMutablePointer<CGFloat>) -> Int     func getLineFragmentInsertionPointsForCharacterAtIndex(_ charIndex: Int, alternatePositions aFlag: Bool, inDisplayOrder dFlag: Bool, positions positions: UnsafeMutablePointer<CGFloat>, characterIndexes charIndexes: UnsafeMutablePointer<Int>) -> Int     func enumerateLineFragmentsForGlyphRange(_ glyphRange: NSRange, usingBlock block: (CGRect, CGRect, NSTextContainer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateEnclosingRectsForGlyphRange(_ glyphRange: NSRange, withinSelectedGlyphRange selectedRange: NSRange, inTextContainer textContainer: NSTextContainer, usingBlock block: (CGRect, UnsafeMutablePointer<ObjCBool>) -> Void)     func drawBackgroundForGlyphRange(_ glyphsToShow: NSRange, atPoint origin: CGPoint)     func drawGlyphsForGlyphRange(_ glyphsToShow: NSRange, atPoint origin: CGPoint)     func showCGGlyphs(_ glyphs: UnsafePointer<CGGlyph>, positions positions: UnsafePointer<CGPoint>, count glyphCount: Int, font font: UIFont, matrix textMatrix: CGAffineTransform, attributes attributes: [String : AnyObject], inContext graphicsContext: CGContext)     func fillBackgroundRectArray(_ rectArray: UnsafePointer<CGRect>, count rectCount: Int, forCharacterRange charRange: NSRange, color color: UIColor)     func drawUnderlineForGlyphRange(_ glyphRange: NSRange, underlineType underlineVal: NSUnderlineStyle, baselineOffset baselineOffset: CGFloat, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin containerOrigin: CGPoint)     func underlineGlyphRange(_ glyphRange: NSRange, underlineType underlineVal: NSUnderlineStyle, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin containerOrigin: CGPoint)     func drawStrikethroughForGlyphRange(_ glyphRange: NSRange, strikethroughType strikethroughVal: NSUnderlineStyle, baselineOffset baselineOffset: CGFloat, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin containerOrigin: CGPoint)     func strikethroughGlyphRange(_ glyphRange: NSRange, strikethroughType strikethroughVal: NSUnderlineStyle, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin containerOrigin: CGPoint) } extension NSLayoutManager {     func glyphAtIndex(_ glyphIndex: Int, isValidIndex isValidIndex: UnsafeMutablePointer<ObjCBool>) -> CGGlyph     func glyphAtIndex(_ glyphIndex: Int) -> CGGlyph } ``` |

Modified [NSLayoutManager.allowsNonContiguousLayout](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403197-allowsnoncontiguouslayout)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSLayoutManager.enumerateEnclosingRectsForGlyphRange(_: NSRange, withinSelectedGlyphRange: NSRange, inTextContainer: NSTextContainer, usingBlock: (CGRect, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403021-enumerateenclosingrectsforglyphr)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSLayoutManager.enumerateLineFragmentsForGlyphRange(_: NSRange, usingBlock: (CGRect, CGRect, NSTextContainer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403160-enumeratelinefragments)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateLineFragmentsForGlyphRange(_ glyphRange: NSRange, usingBlock block: (CGRect, CGRect, NSTextContainer!, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | iOS 8.0 |
| To | ``` func enumerateLineFragmentsForGlyphRange(_ glyphRange: NSRange, usingBlock block: (CGRect, CGRect, NSTextContainer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void) ``` | iOS 7.0 |

Modified [NSLayoutManager.fillBackgroundRectArray(_: UnsafePointer<CGRect>, count: Int, forCharacterRange: NSRange, color: UIColor)](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403161-fillbackgroundrectarray)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSLayoutManager.getGlyphsInRange(_: NSRange, glyphs: UnsafeMutablePointer<CGGlyph>, properties: UnsafeMutablePointer<NSGlyphProperty>, characterIndexes: UnsafeMutablePointer<Int>, bidiLevels: UnsafeMutablePointer<UInt8>) -> Int](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403104-getglyphs)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSLayoutManager.hasNonContiguousLayout](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403207-hasnoncontiguouslayout)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSLayoutManager.invalidateLayoutForCharacterRange(_: NSRange, actualCharacterRange: NSRangePointer)](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403248-invalidatelayout)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSLayoutManager.processEditingForTextStorage(_: NSTextStorage, edited: NSTextStorageEditActions, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403065-processeditingfortextstorage)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSLayoutManager.propertyForGlyphAtIndex(_: Int) -> NSGlyphProperty](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403014-propertyforglyphatindex)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSLayoutManager.setExtraLineFragmentRect(_: CGRect, usedRect: CGRect, textContainer: NSTextContainer)](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403071-setextralinefragmentrect)

|  | Declaration |
| --- | --- |
| From | ``` func setExtraLineFragmentRect(_ fragmentRect: CGRect, usedRect usedRect: CGRect, textContainer container: NSTextContainer?) ``` |
| To | ``` func setExtraLineFragmentRect(_ fragmentRect: CGRect, usedRect usedRect: CGRect, textContainer container: NSTextContainer) ``` |

Modified [NSLayoutManager.setGlyphs(_: UnsafePointer<CGGlyph>, properties: UnsafePointer<NSGlyphProperty>, characterIndexes: UnsafePointer<Int>, font: UIFont, forGlyphRange: NSRange)](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403030-setglyphs)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setGlyphs(_ glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSGlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont?, forGlyphRange glyphRange: NSRange) ``` | iOS 8.0 |
| To | ``` func setGlyphs(_ glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSGlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont, forGlyphRange glyphRange: NSRange) ``` | iOS 7.0 |

Modified [NSLayoutManager.setTextContainer(_: NSTextContainer, forGlyphRange: NSRange)](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403241-settextcontainer)

|  | Declaration |
| --- | --- |
| From | ``` func setTextContainer(_ container: NSTextContainer?, forGlyphRange glyphRange: NSRange) ``` |
| To | ``` func setTextContainer(_ container: NSTextContainer, forGlyphRange glyphRange: NSRange) ``` |

Modified [NSLayoutManager.showCGGlyphs(_: UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: UIFont, matrix: CGAffineTransform, attributes: [String : AnyObject], inContext: CGContext)](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403247-showcgglyphs)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func showCGGlyphs(_ glyphs: UnsafePointer<CGGlyph>, positions positions: UnsafePointer<CGPoint>, count glyphCount: Int, font font: UIFont, matrix textMatrix: CGAffineTransform, attributes attributes: [NSObject : AnyObject]?, inContext graphicsContext: CGContext?) ``` | iOS 8.0 |
| To | ``` func showCGGlyphs(_ glyphs: UnsafePointer<CGGlyph>, positions positions: UnsafePointer<CGPoint>, count glyphCount: Int, font font: UIFont, matrix textMatrix: CGAffineTransform, attributes attributes: [String : AnyObject], inContext graphicsContext: CGContext) ``` | iOS 7.0 |

Modified [NSLayoutManager.textContainers](https://developer.apple.com/documentation/uikit/nslayoutmanager/1403144-textcontainers)

|  | Declaration |
| --- | --- |
| From | ``` var textContainers: [AnyObject] { get } ``` |
| To | ``` var textContainers: [NSTextContainer] { get } ``` |

Modified [NSLayoutManager.truncatedGlyphRangeInLineFragmentForGlyphAtIndex(_: Int) -> NSRange](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403203-truncatedglyphrangeinlinefragmen)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSLayoutManagerDelegate](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSLayoutManagerDelegate : NSObjectProtocol {     optional func layoutManager(_ layoutManager: NSLayoutManager, shouldGenerateGlyphs glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSGlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont!, forGlyphRange glyphRange: NSRange) -> Int     optional func layoutManager(_ layoutManager: NSLayoutManager, lineSpacingAfterGlyphAtIndex glyphIndex: Int, withProposedLineFragmentRect rect: CGRect) -> CGFloat     optional func layoutManager(_ layoutManager: NSLayoutManager, paragraphSpacingBeforeGlyphAtIndex glyphIndex: Int, withProposedLineFragmentRect rect: CGRect) -> CGFloat     optional func layoutManager(_ layoutManager: NSLayoutManager, paragraphSpacingAfterGlyphAtIndex glyphIndex: Int, withProposedLineFragmentRect rect: CGRect) -> CGFloat     optional func layoutManager(_ layoutManager: NSLayoutManager, shouldUseAction action: NSControlCharacterAction, forControlCharacterAtIndex charIndex: Int) -> NSControlCharacterAction     optional func layoutManager(_ layoutManager: NSLayoutManager, shouldBreakLineByWordBeforeCharacterAtIndex charIndex: Int) -> Bool     optional func layoutManager(_ layoutManager: NSLayoutManager, shouldBreakLineByHyphenatingBeforeCharacterAtIndex charIndex: Int) -> Bool     optional func layoutManager(_ layoutManager: NSLayoutManager, boundingBoxForControlGlyphAtIndex glyphIndex: Int, forTextContainer textContainer: NSTextContainer, proposedLineFragment proposedRect: CGRect, glyphPosition glyphPosition: CGPoint, characterIndex charIndex: Int) -> CGRect     optional func layoutManagerDidInvalidateLayout(_ sender: NSLayoutManager)     optional func layoutManager(_ layoutManager: NSLayoutManager, didCompleteLayoutForTextContainer textContainer: NSTextContainer?, atEnd layoutFinishedFlag: Bool)     optional func layoutManager(_ layoutManager: NSLayoutManager, textContainer textContainer: NSTextContainer, didChangeGeometryFromSize oldSize: CGSize) } ``` |
| To | ``` protocol NSLayoutManagerDelegate : NSObjectProtocol {     optional func layoutManager(_ layoutManager: NSLayoutManager, shouldGenerateGlyphs glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSGlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont, forGlyphRange glyphRange: NSRange) -> Int     optional func layoutManager(_ layoutManager: NSLayoutManager, lineSpacingAfterGlyphAtIndex glyphIndex: Int, withProposedLineFragmentRect rect: CGRect) -> CGFloat     optional func layoutManager(_ layoutManager: NSLayoutManager, paragraphSpacingBeforeGlyphAtIndex glyphIndex: Int, withProposedLineFragmentRect rect: CGRect) -> CGFloat     optional func layoutManager(_ layoutManager: NSLayoutManager, paragraphSpacingAfterGlyphAtIndex glyphIndex: Int, withProposedLineFragmentRect rect: CGRect) -> CGFloat     optional func layoutManager(_ layoutManager: NSLayoutManager, shouldUseAction action: NSControlCharacterAction, forControlCharacterAtIndex charIndex: Int) -> NSControlCharacterAction     optional func layoutManager(_ layoutManager: NSLayoutManager, shouldBreakLineByWordBeforeCharacterAtIndex charIndex: Int) -> Bool     optional func layoutManager(_ layoutManager: NSLayoutManager, shouldBreakLineByHyphenatingBeforeCharacterAtIndex charIndex: Int) -> Bool     optional func layoutManager(_ layoutManager: NSLayoutManager, boundingBoxForControlGlyphAtIndex glyphIndex: Int, forTextContainer textContainer: NSTextContainer, proposedLineFragment proposedRect: CGRect, glyphPosition glyphPosition: CGPoint, characterIndex charIndex: Int) -> CGRect     optional func layoutManager(_ layoutManager: NSLayoutManager, shouldSetLineFragmentRect lineFragmentRect: UnsafeMutablePointer<CGRect>, lineFragmentUsedRect lineFragmentUsedRect: UnsafeMutablePointer<CGRect>, baselineOffset baselineOffset: UnsafeMutablePointer<CGFloat>, inTextContainer textContainer: NSTextContainer, forGlyphRange glyphRange: NSRange) -> Bool     optional func layoutManagerDidInvalidateLayout(_ sender: NSLayoutManager)     optional func layoutManager(_ layoutManager: NSLayoutManager, didCompleteLayoutForTextContainer textContainer: NSTextContainer?, atEnd layoutFinishedFlag: Bool)     optional func layoutManager(_ layoutManager: NSLayoutManager, textContainer textContainer: NSTextContainer, didChangeGeometryFromSize oldSize: CGSize) } ``` |

Modified [NSLayoutManagerDelegate.layoutManager(_: NSLayoutManager, shouldGenerateGlyphs: UnsafePointer<CGGlyph>, properties: UnsafePointer<NSGlyphProperty>, characterIndexes: UnsafePointer<Int>, font: UIFont, forGlyphRange: NSRange) -> Int](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/1403073-layoutmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func layoutManager(_ layoutManager: NSLayoutManager, shouldGenerateGlyphs glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSGlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont!, forGlyphRange glyphRange: NSRange) -> Int ``` |
| To | ``` optional func layoutManager(_ layoutManager: NSLayoutManager, shouldGenerateGlyphs glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSGlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont, forGlyphRange glyphRange: NSRange) -> Int ``` |

Modified [NSLayoutRelation [enum]](https://developer.apple.com/documentation/uikit/nslayoutconstraint/relation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSLineBreakMode [enum]](https://developer.apple.com/documentation/uikit/nslinebreakmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSMutableAttributedString.readFromData(_: NSData, options: [String : AnyObject], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1535465-read)

|  | Declaration |
| --- | --- |
| From | ``` func readFromData(_ data: NSData, options opts: [NSObject : AnyObject]?, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func readFromData(_ data: NSData, options opts: [String : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws ``` |

Modified [NSMutableAttributedString.readFromFileURL(_: NSURL, options: [NSObject : AnyObject], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1620496-readfromfileurl)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func readFromFileURL(_ url: NSURL!, options opts: [NSObject : AnyObject]!, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>, error error: NSErrorPointer) -> Bool ``` | -- |
| To | ``` func readFromFileURL(_ url: NSURL, options opts: [NSObject : AnyObject], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>) throws ``` | iOS 9.0 |

Modified [NSMutableParagraphStyle](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle)

|  | Declaration |
| --- | --- |
| From | ``` class NSMutableParagraphStyle : NSParagraphStyle {     var lineSpacing: CGFloat     var paragraphSpacing: CGFloat     var alignment: NSTextAlignment     var firstLineHeadIndent: CGFloat     var headIndent: CGFloat     var tailIndent: CGFloat     var lineBreakMode: NSLineBreakMode     var minimumLineHeight: CGFloat     var maximumLineHeight: CGFloat     var baseWritingDirection: NSWritingDirection     var lineHeightMultiple: CGFloat     var paragraphSpacingBefore: CGFloat     var hyphenationFactor: Float     var tabStops: [AnyObject]?     var defaultTabInterval: CGFloat } ``` |
| To | ``` class NSMutableParagraphStyle : NSParagraphStyle {     var lineSpacing: CGFloat     var paragraphSpacing: CGFloat     var alignment: NSTextAlignment     var firstLineHeadIndent: CGFloat     var headIndent: CGFloat     var tailIndent: CGFloat     var lineBreakMode: NSLineBreakMode     var minimumLineHeight: CGFloat     var maximumLineHeight: CGFloat     var baseWritingDirection: NSWritingDirection     var lineHeightMultiple: CGFloat     var paragraphSpacingBefore: CGFloat     var hyphenationFactor: Float     var tabStops: [NSTextTab]!     var defaultTabInterval: CGFloat     var allowsDefaultTighteningForTruncation: Bool     func addTabStop(_ anObject: NSTextTab)     func removeTabStop(_ anObject: NSTextTab)     func setParagraphStyle(_ obj: NSParagraphStyle) } ``` |

Modified [NSMutableParagraphStyle.tabStops](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/1531988-tabstops)

|  | Declaration |
| --- | --- |
| From | ``` var tabStops: [AnyObject]? ``` |
| To | ``` var tabStops: [NSTextTab]! ``` |

Modified [NSObject.accessibilityCustomActions](https://developer.apple.com/documentation/objectivec/nsobject/1615150-accessibilitycustomactions)

|  | Declaration |
| --- | --- |
| From | ``` var accessibilityCustomActions: [AnyObject]! ``` |
| To | ``` var accessibilityCustomActions: [UIAccessibilityCustomAction]? ``` |

Modified [NSObject.accessibilityElementAtIndex(_: Int) -> AnyObject?](https://developer.apple.com/documentation/objectivec/nsobject/1615084-accessibilityelementatindex)

|  | Declaration |
| --- | --- |
| From | ``` func accessibilityElementAtIndex(_ index: Int) -> AnyObject! ``` |
| To | ``` func accessibilityElementAtIndex(_ index: Int) -> AnyObject? ``` |

Modified [NSObject.accessibilityElements](https://developer.apple.com/documentation/objectivec/nsobject/1615147-accessibilityelements)

|  | Declaration |
| --- | --- |
| From | ``` var accessibilityElements: [AnyObject]! ``` |
| To | ``` var accessibilityElements: [AnyObject]? ``` |

Modified [NSObject.accessibilityHint](https://developer.apple.com/documentation/objectivec/nsobject/1615093-accessibilityhint)

|  | Declaration |
| --- | --- |
| From | ``` var accessibilityHint: String! ``` |
| To | ``` var accessibilityHint: String? ``` |

Modified [NSObject.accessibilityLabel](https://developer.apple.com/documentation/objectivec/nsobject/1615181-accessibilitylabel)

|  | Declaration |
| --- | --- |
| From | ``` var accessibilityLabel: String! ``` |
| To | ``` var accessibilityLabel: String? ``` |

Modified [NSObject.accessibilityLanguage](https://developer.apple.com/documentation/objectivec/nsobject/1615192-accessibilitylanguage)

|  | Declaration |
| --- | --- |
| From | ``` var accessibilityLanguage: String! ``` |
| To | ``` var accessibilityLanguage: String? ``` |

Modified [NSObject.accessibilityPath](https://developer.apple.com/documentation/objectivec/nsobject/1615159-accessibilitypath)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var accessibilityPath: UIBezierPath! ``` |
| To | ``` @NSCopying var accessibilityPath: UIBezierPath? ``` |

Modified [NSObject.accessibilityValue](https://developer.apple.com/documentation/objectivec/nsobject/1615117-accessibilityvalue)

|  | Declaration |
| --- | --- |
| From | ``` var accessibilityValue: String! ``` |
| To | ``` var accessibilityValue: String? ``` |

Modified [NSObject.indexOfAccessibilityElement(_: AnyObject) -> Int](https://developer.apple.com/documentation/objectivec/nsobject/1615078-index)

|  | Declaration |
| --- | --- |
| From | ``` func indexOfAccessibilityElement(_ element: AnyObject!) -> Int ``` |
| To | ``` func indexOfAccessibilityElement(_ element: AnyObject) -> Int ``` |

Modified [NSParagraphStyle](https://developer.apple.com/documentation/uikit/nsparagraphstyle)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSParagraphStyle : NSObject, NSCopying, NSMutableCopying, NSCoding {     class func defaultParagraphStyle() -> NSParagraphStyle     class func defaultWritingDirectionForLanguage(_ languageName: String?) -> NSWritingDirection     var lineSpacing: CGFloat { get }     var paragraphSpacing: CGFloat { get }     var alignment: NSTextAlignment { get }     var headIndent: CGFloat { get }     var tailIndent: CGFloat { get }     var firstLineHeadIndent: CGFloat { get }     var minimumLineHeight: CGFloat { get }     var maximumLineHeight: CGFloat { get }     var lineBreakMode: NSLineBreakMode { get }     var baseWritingDirection: NSWritingDirection { get }     var lineHeightMultiple: CGFloat { get }     var paragraphSpacingBefore: CGFloat { get }     var hyphenationFactor: Float { get }     var tabStops: [AnyObject]? { get }     var defaultTabInterval: CGFloat { get } } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying |
| To | ``` class NSParagraphStyle : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     class func defaultParagraphStyle() -> NSParagraphStyle     class func defaultWritingDirectionForLanguage(_ languageName: String?) -> NSWritingDirection     var lineSpacing: CGFloat { get }     var paragraphSpacing: CGFloat { get }     var alignment: NSTextAlignment { get }     var headIndent: CGFloat { get }     var tailIndent: CGFloat { get }     var firstLineHeadIndent: CGFloat { get }     var minimumLineHeight: CGFloat { get }     var maximumLineHeight: CGFloat { get }     var lineBreakMode: NSLineBreakMode { get }     var baseWritingDirection: NSWritingDirection { get }     var lineHeightMultiple: CGFloat { get }     var paragraphSpacingBefore: CGFloat { get }     var hyphenationFactor: Float { get }     var tabStops: [NSTextTab] { get }     var defaultTabInterval: CGFloat { get }     var allowsDefaultTighteningForTruncation: Bool { get } } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |

Modified [NSParagraphStyle.tabStops](https://developer.apple.com/documentation/uikit/nsparagraphstyle/1532841-tabstops)

|  | Declaration |
| --- | --- |
| From | ``` var tabStops: [AnyObject]? { get } ``` |
| To | ``` var tabStops: [NSTextTab] { get } ``` |

Modified [NSShadow](https://developer.apple.com/documentation/uikit/nsshadow)

|  | Declaration |
| --- | --- |
| From | ``` class NSShadow : NSObject, NSCopying, NSCoding {     var shadowOffset: CGSize     var shadowBlurRadius: CGFloat     var shadowColor: AnyObject? } ``` |
| To | ``` class NSShadow : NSObject, NSCopying, NSCoding {     init()     init?(coder aDecoder: NSCoder)     var shadowOffset: CGSize     var shadowBlurRadius: CGFloat     var shadowColor: AnyObject? } ``` |

Modified [NSString.boundingRectWithSize(_: CGSize, options: NSStringDrawingOptions, attributes: [String : AnyObject]?, context: NSStringDrawingContext?) -> CGRect](https://developer.apple.com/documentation/foundation/nsstring/1524729-boundingrect)

|  | Declaration |
| --- | --- |
| From | ``` func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, attributes attributes: [NSObject : AnyObject]!, context context: NSStringDrawingContext!) -> CGRect ``` |
| To | ``` func boundingRectWithSize(_ size: CGSize, options options: NSStringDrawingOptions, attributes attributes: [String : AnyObject]?, context context: NSStringDrawingContext?) -> CGRect ``` |

Modified [NSString.drawAtPoint(_: CGPoint, withAttributes: [String : AnyObject]?)](https://developer.apple.com/documentation/foundation/nsstring/1533109-draw)

|  | Declaration |
| --- | --- |
| From | ``` func drawAtPoint(_ point: CGPoint, withAttributes attrs: [NSObject : AnyObject]?) ``` |
| To | ``` func drawAtPoint(_ point: CGPoint, withAttributes attrs: [String : AnyObject]?) ``` |

Modified [NSString.drawInRect(_: CGRect, withAttributes: [String : AnyObject]?)](https://developer.apple.com/documentation/foundation/nsstring/1529855-drawinrect)

|  | Declaration |
| --- | --- |
| From | ``` func drawInRect(_ rect: CGRect, withAttributes attrs: [NSObject : AnyObject]?) ``` |
| To | ``` func drawInRect(_ rect: CGRect, withAttributes attrs: [String : AnyObject]?) ``` |

Modified [NSString.drawWithRect(_: CGRect, options: NSStringDrawingOptions, attributes: [String : AnyObject]?, context: NSStringDrawingContext?)](https://developer.apple.com/documentation/foundation/nsstring/1530195-drawwithrect)

|  | Declaration |
| --- | --- |
| From | ``` func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, attributes attributes: [NSObject : AnyObject]!, context context: NSStringDrawingContext!) ``` |
| To | ``` func drawWithRect(_ rect: CGRect, options options: NSStringDrawingOptions, attributes attributes: [String : AnyObject]?, context context: NSStringDrawingContext?) ``` |

Modified [NSString.sizeWithAttributes(_: [String : AnyObject]?) -> CGSize](https://developer.apple.com/documentation/foundation/nsstring/1531844-sizewithattributes)

|  | Declaration |
| --- | --- |
| From | ``` func sizeWithAttributes(_ attrs: [NSObject : AnyObject]?) -> CGSize ``` |
| To | ``` func sizeWithAttributes(_ attrs: [String : AnyObject]?) -> CGSize ``` |

Modified [NSStringDrawingContext](https://developer.apple.com/documentation/appkit/nsstringdrawingcontext)

|  | Declaration |
| --- | --- |
| From | ``` class NSStringDrawingContext : NSObject {     var minimumScaleFactor: CGFloat     var minimumTrackingAdjustment: CGFloat     var actualScaleFactor: CGFloat { get }     var actualTrackingAdjustment: CGFloat { get }     var totalBounds: CGRect { get } } ``` |
| To | ``` class NSStringDrawingContext : NSObject {     var minimumScaleFactor: CGFloat     var actualScaleFactor: CGFloat { get }     var totalBounds: CGRect { get } } extension NSStringDrawingContext {     var minimumTrackingAdjustment: CGFloat     var actualTrackingAdjustment: CGFloat { get } } ``` |

Modified [NSStringDrawingOptions [struct]](https://developer.apple.com/documentation/uikit/nsstringdrawingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSStringDrawingOptions : RawOptionSetType {     init(_ rawValue: Int)     init(rawValue rawValue: Int)     static var TruncatesLastVisibleLine: NSStringDrawingOptions { get }     static var UsesLineFragmentOrigin: NSStringDrawingOptions { get }     static var UsesFontLeading: NSStringDrawingOptions { get }     static var UsesDeviceMetrics: NSStringDrawingOptions { get } } ``` | RawOptionSetType |
| To | ``` struct NSStringDrawingOptions : OptionSetType {     init(rawValue rawValue: Int)     static var UsesLineFragmentOrigin: NSStringDrawingOptions { get }     static var UsesFontLeading: NSStringDrawingOptions { get }     static var UsesDeviceMetrics: NSStringDrawingOptions { get }     static var TruncatesLastVisibleLine: NSStringDrawingOptions { get } } ``` | OptionSetType |

Modified [NSStringDrawingOptions.TruncatesLastVisibleLine](https://developer.apple.com/documentation/foundation/nsstring/nsstringdrawingoptions/1527952-truncateslastvisibleline)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 6.0 |

Modified [NSTextAlignment [enum]](https://developer.apple.com/documentation/uikit/nstextalignment)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSTextAttachment](https://developer.apple.com/documentation/uikit/nstextattachment)

|  | Declaration |
| --- | --- |
| From | ``` class NSTextAttachment : NSObject, NSTextAttachmentContainer, NSObjectProtocol, NSCoding {     init(data contentData: NSData?, ofType uti: String?)     var contents: NSData?     var fileType: String?     var fileWrapper: NSFileWrapper?     var image: UIImage?     var bounds: CGRect } ``` |
| To | ``` class NSTextAttachment : NSObject, NSTextAttachmentContainer, NSCoding {     init(data contentData: NSData?, ofType uti: String?)     @NSCopying var contents: NSData?     var fileType: String?     var image: UIImage?     var bounds: CGRect     var fileWrapper: NSFileWrapper? } ``` |

Modified [NSTextAttachment.bounds](https://developer.apple.com/documentation/appkit/nstextattachment/1508394-bounds)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSTextAttachment.contents](https://developer.apple.com/documentation/appkit/nstextattachment/1508401-contents)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var contents: NSData? ``` | iOS 8.0 |
| To | ``` @NSCopying var contents: NSData? ``` | iOS 7.0 |

Modified [NSTextAttachment.fileType](https://developer.apple.com/documentation/uikit/nstextattachment/1508416-filetype)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSTextAttachment.image](https://developer.apple.com/documentation/appkit/nstextattachment/1508378-image)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSTextAttachment.init(data: NSData?, ofType: String?)](https://developer.apple.com/documentation/uikit/nstextattachment/1508374-init)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSTextAttachmentContainer](https://developer.apple.com/documentation/appkit/nstextattachmentcontainer)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSTextAttachmentContainer : NSObjectProtocol {     func imageForBounds(_ imageBounds: CGRect, textContainer textContainer: NSTextContainer, characterIndex charIndex: Int) -> UIImage!     func attachmentBoundsForTextContainer(_ textContainer: NSTextContainer, proposedLineFragment lineFrag: CGRect, glyphPosition position: CGPoint, characterIndex charIndex: Int) -> CGRect } ``` |
| To | ``` protocol NSTextAttachmentContainer : NSObjectProtocol {     func imageForBounds(_ imageBounds: CGRect, textContainer textContainer: NSTextContainer?, characterIndex charIndex: Int) -> UIImage?     func attachmentBoundsForTextContainer(_ textContainer: NSTextContainer?, proposedLineFragment lineFrag: CGRect, glyphPosition position: CGPoint, characterIndex charIndex: Int) -> CGRect } ``` |

Modified [NSTextAttachmentContainer.attachmentBoundsForTextContainer(_: NSTextContainer?, proposedLineFragment: CGRect, glyphPosition: CGPoint, characterIndex: Int) -> CGRect](https://developer.apple.com/documentation/uikit/nstextattachmentcontainer/1508382-attachmentboundsfortextcontainer)

|  | Declaration |
| --- | --- |
| From | ``` func attachmentBoundsForTextContainer(_ textContainer: NSTextContainer, proposedLineFragment lineFrag: CGRect, glyphPosition position: CGPoint, characterIndex charIndex: Int) -> CGRect ``` |
| To | ``` func attachmentBoundsForTextContainer(_ textContainer: NSTextContainer?, proposedLineFragment lineFrag: CGRect, glyphPosition position: CGPoint, characterIndex charIndex: Int) -> CGRect ``` |

Modified [NSTextAttachmentContainer.imageForBounds(_: CGRect, textContainer: NSTextContainer?, characterIndex: Int) -> UIImage?](https://developer.apple.com/documentation/appkit/nstextattachmentcontainer/1508386-imageforbounds)

|  | Declaration |
| --- | --- |
| From | ``` func imageForBounds(_ imageBounds: CGRect, textContainer textContainer: NSTextContainer, characterIndex charIndex: Int) -> UIImage! ``` |
| To | ``` func imageForBounds(_ imageBounds: CGRect, textContainer textContainer: NSTextContainer?, characterIndex charIndex: Int) -> UIImage? ``` |

Modified [NSTextContainer](https://developer.apple.com/documentation/uikit/nstextcontainer)

|  | Declaration |
| --- | --- |
| From | ``` class NSTextContainer : NSObject, NSCoding, NSTextLayoutOrientationProvider {     init(size size: CGSize)     unowned(unsafe) var layoutManager: NSLayoutManager?     var size: CGSize     var exclusionPaths: [AnyObject]?     var lineBreakMode: NSLineBreakMode     var lineFragmentPadding: CGFloat     var maximumNumberOfLines: Int     func lineFragmentRectForProposedRect(_ proposedRect: CGRect, atIndex characterIndex: Int, writingDirection baseWritingDirection: NSWritingDirection, remainingRect remainingRect: UnsafeMutablePointer<CGRect>) -> CGRect     var widthTracksTextView: Bool     var heightTracksTextView: Bool } ``` |
| To | ``` class NSTextContainer : NSObject, NSCoding, NSTextLayoutOrientationProvider {     init(size size: CGSize)     init?(coder coder: NSCoder)     unowned(unsafe) var layoutManager: NSLayoutManager?     func replaceLayoutManager(_ newLayoutManager: NSLayoutManager)     var size: CGSize     var exclusionPaths: [UIBezierPath]     var lineBreakMode: NSLineBreakMode     var lineFragmentPadding: CGFloat     var maximumNumberOfLines: Int     func lineFragmentRectForProposedRect(_ proposedRect: CGRect, atIndex characterIndex: Int, writingDirection baseWritingDirection: NSWritingDirection, remainingRect remainingRect: UnsafeMutablePointer<CGRect>) -> CGRect     var simpleRectangularTextContainer: Bool { get }     var widthTracksTextView: Bool     var heightTracksTextView: Bool } ``` |

Modified [NSTextContainer.exclusionPaths](https://developer.apple.com/documentation/appkit/nstextcontainer/1444569-exclusionpaths)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var exclusionPaths: [AnyObject]? ``` | iOS 8.0 |
| To | ``` var exclusionPaths: [UIBezierPath] ``` | iOS 7.0 |

Modified [NSTextContainer.init(size: CGSize)](https://developer.apple.com/documentation/uikit/nstextcontainer/1444529-initwithsize)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSTextContainer.lineBreakMode](https://developer.apple.com/documentation/uikit/nstextcontainer/1444519-linebreakmode)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSTextContainer.lineFragmentRectForProposedRect(_: CGRect, atIndex: Int, writingDirection: NSWritingDirection, remainingRect: UnsafeMutablePointer<CGRect>) -> CGRect](https://developer.apple.com/documentation/appkit/nstextcontainer/1444555-linefragmentrectforproposedrect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSTextContainer.maximumNumberOfLines](https://developer.apple.com/documentation/uikit/nstextcontainer/1444531-maximumnumberoflines)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSTextContainer.size](https://developer.apple.com/documentation/uikit/nstextcontainer/1444553-size)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSTextLayoutOrientation [enum]](https://developer.apple.com/documentation/appkit/nstextlayoutorientation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NSTextLayoutOrientationProvider](https://developer.apple.com/documentation/appkit/nstextlayoutorientationprovider)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSTextLayoutOrientationProvider {     var layoutOrientation: NSTextLayoutOrientation { get set } } ``` |
| To | ``` protocol NSTextLayoutOrientationProvider {     var layoutOrientation: NSTextLayoutOrientation { get } } ``` |

Modified [NSTextLayoutOrientationProvider.layoutOrientation](https://developer.apple.com/documentation/uikit/nstextlayoutorientationprovider/1402990-layoutorientation)

|  | Declaration |
| --- | --- |
| From | ``` var layoutOrientation: NSTextLayoutOrientation { get set } ``` |
| To | ``` var layoutOrientation: NSTextLayoutOrientation { get } ``` |

Modified [NSTextStorage](https://developer.apple.com/documentation/appkit/nstextstorage)

|  | Declaration |
| --- | --- |
| From | ``` class NSTextStorage : NSMutableAttributedString {     var layoutManagers: [AnyObject] { get }     func addLayoutManager(_ aLayoutManager: NSLayoutManager)     func removeLayoutManager(_ aLayoutManager: NSLayoutManager)     var editedMask: NSTextStorageEditActions     var editedRange: NSRange     var changeInLength: Int     unowned(unsafe) var delegate: NSTextStorageDelegate?     func edited(_ editedMask: NSTextStorageEditActions, range editedRange: NSRange, changeInLength delta: Int)     func processEditing()     var fixesAttributesLazily: Bool { get }     func invalidateAttributesInRange(_ range: NSRange)     func ensureAttributesAreFixedInRange(_ range: NSRange) } ``` |
| To | ``` class NSTextStorage : NSMutableAttributedString {     var layoutManagers: [NSLayoutManager] { get }     func addLayoutManager(_ aLayoutManager: NSLayoutManager)     func removeLayoutManager(_ aLayoutManager: NSLayoutManager)     var editedMask: NSTextStorageEditActions { get }     var editedRange: NSRange { get }     var changeInLength: Int { get }     unowned(unsafe) var delegate: NSTextStorageDelegate?     func edited(_ editedMask: NSTextStorageEditActions, range editedRange: NSRange, changeInLength delta: Int)     func processEditing()     var fixesAttributesLazily: Bool { get }     func invalidateAttributesInRange(_ range: NSRange)     func ensureAttributesAreFixedInRange(_ range: NSRange) } ``` |

Modified [NSTextStorage.changeInLength](https://developer.apple.com/documentation/appkit/nstextstorage/1528400-changeinlength)

|  | Declaration |
| --- | --- |
| From | ``` var changeInLength: Int ``` |
| To | ``` var changeInLength: Int { get } ``` |

Modified [NSTextStorage.editedMask](https://developer.apple.com/documentation/appkit/nstextstorage/1525323-editedmask)

|  | Declaration |
| --- | --- |
| From | ``` var editedMask: NSTextStorageEditActions ``` |
| To | ``` var editedMask: NSTextStorageEditActions { get } ``` |

Modified [NSTextStorage.editedRange](https://developer.apple.com/documentation/appkit/nstextstorage/1524379-editedrange)

|  | Declaration |
| --- | --- |
| From | ``` var editedRange: NSRange ``` |
| To | ``` var editedRange: NSRange { get } ``` |

Modified [NSTextStorage.layoutManagers](https://developer.apple.com/documentation/uikit/nstextstorage/1527938-layoutmanagers)

|  | Declaration |
| --- | --- |
| From | ``` var layoutManagers: [AnyObject] { get } ``` |
| To | ``` var layoutManagers: [NSLayoutManager] { get } ``` |

Modified [NSTextStorageEditActions [struct]](https://developer.apple.com/documentation/appkit/nstextstorageeditactions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSTextStorageEditActions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var EditedAttributes: NSTextStorageEditActions { get }     static var EditedCharacters: NSTextStorageEditActions { get } } ``` | RawOptionSetType |
| To | ``` struct NSTextStorageEditActions : OptionSetType {     init(rawValue rawValue: UInt)     static var EditedAttributes: NSTextStorageEditActions { get }     static var EditedCharacters: NSTextStorageEditActions { get } } ``` | OptionSetType |

Modified [NSTextTab](https://developer.apple.com/documentation/uikit/nstexttab)

|  | Declaration |
| --- | --- |
| From | ``` class NSTextTab : NSObject, NSCopying, NSCoding {     init(textAlignment alignment: NSTextAlignment, location loc: CGFloat, options options: [NSObject : AnyObject]?)     class func columnTerminatorsForLocale(_ aLocale: NSLocale?) -> NSCharacterSet     var alignment: NSTextAlignment { get }     var location: CGFloat { get }     var options: [NSObject : AnyObject]? { get } } ``` |
| To | ``` class NSTextTab : NSObject, NSCopying, NSCoding {     class func columnTerminatorsForLocale(_ aLocale: NSLocale?) -> NSCharacterSet     init(textAlignment alignment: NSTextAlignment, location loc: CGFloat, options options: [String : AnyObject])     var alignment: NSTextAlignment { get }     var location: CGFloat { get }     var options: [String : AnyObject] { get } } ``` |

Modified [NSTextTab.columnTerminatorsForLocale(_: NSLocale?) -> NSCharacterSet [class]](https://developer.apple.com/documentation/uikit/nstexttab/1535107-columnterminatorsforlocale)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [NSTextTab.init(textAlignment: NSTextAlignment, location: CGFloat, options: [String : AnyObject])](https://developer.apple.com/documentation/appkit/nstexttab/1526080-init)

|  | Declaration |
| --- | --- |
| From | ``` init(textAlignment alignment: NSTextAlignment, location loc: CGFloat, options options: [NSObject : AnyObject]?) ``` |
| To | ``` init(textAlignment alignment: NSTextAlignment, location loc: CGFloat, options options: [String : AnyObject]) ``` |

Modified [NSTextTab.options](https://developer.apple.com/documentation/appkit/nstexttab/1534965-options)

|  | Declaration |
| --- | --- |
| From | ``` var options: [NSObject : AnyObject]? { get } ``` |
| To | ``` var options: [String : AnyObject] { get } ``` |

Modified [NSTextWritingDirection [enum]](https://developer.apple.com/documentation/uikit/nstextwritingdirection)

|  | Deprecation | Raw Value Type |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 9.0 | Int |

Modified [NSUnderlineStyle [enum]](https://developer.apple.com/documentation/uikit/nsunderlinestyle)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NSUnderlineStyle : Int {     case StyleNone     case StyleSingle     case StyleThick     case StyleDouble     case PatternDot     case PatternDash     case PatternDashDot     case PatternDashDotDot     case ByWord } ``` | -- |
| To | ``` enum NSUnderlineStyle : Int {     case StyleNone     case StyleSingle     case StyleThick     case StyleDouble     static var PatternSolid: NSUnderlineStyle { get }     case PatternDot     case PatternDash     case PatternDashDot     case PatternDashDotDot     case ByWord } ``` | Int |

Modified [NSValue.init(CGAffineTransform: CGAffineTransform)](https://developer.apple.com/documentation/foundation/nsvalue/1624503-valuewithcgaffinetransform)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGAffineTransform transform: CGAffineTransform) -> NSValue ``` |
| To | ``` init(CGAffineTransform transform: CGAffineTransform) ``` |

Modified [NSValue.init(CGPoint: CGPoint)](https://developer.apple.com/documentation/foundation/nsvalue/1624531-valuewithcgpoint)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGPoint point: CGPoint) -> NSValue ``` |
| To | ``` init(CGPoint point: CGPoint) ``` |

Modified [NSValue.init(CGRect: CGRect)](https://developer.apple.com/documentation/foundation/nsvalue/1624529-valuewithcgrect)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGRect rect: CGRect) -> NSValue ``` |
| To | ``` init(CGRect rect: CGRect) ``` |

Modified [NSValue.init(CGSize: CGSize)](https://developer.apple.com/documentation/foundation/nsvalue/1624511-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGSize size: CGSize) -> NSValue ``` |
| To | ``` init(CGSize size: CGSize) ``` |

Modified [NSValue.init(CGVector: CGVector)](https://developer.apple.com/documentation/foundation/nsvalue/1624493-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGVector vector: CGVector) -> NSValue ``` |
| To | ``` init(CGVector vector: CGVector) ``` |

Modified [NSValue.init(UIEdgeInsets: UIEdgeInsets)](https://developer.apple.com/documentation/foundation/nsvalue/1624485-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(UIEdgeInsets insets: UIEdgeInsets) -> NSValue ``` |
| To | ``` init(UIEdgeInsets insets: UIEdgeInsets) ``` |

Modified [NSValue.init(UIOffset: UIOffset)](https://developer.apple.com/documentation/foundation/nsvalue/1624530-valuewithuioffset)

|  | Declaration |
| --- | --- |
| From | ``` init!(UIOffset insets: UIOffset) -> NSValue ``` |
| To | ``` init(UIOffset insets: UIOffset) ``` |

Modified [NSWritingDirection [enum]](https://developer.apple.com/documentation/appkit/nswritingdirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIAccelerometerDelegate](https://developer.apple.com/documentation/uikit/uiaccelerometerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIAccelerometerDelegate : NSObjectProtocol {     optional func accelerometer(_ accelerometer: UIAccelerometer, didAccelerate acceleration: UIAcceleration!) } ``` |
| To | ``` protocol UIAccelerometerDelegate : NSObjectProtocol {     optional func accelerometer(_ accelerometer: UIAccelerometer, didAccelerate acceleration: UIAcceleration) } ``` |

Modified [UIAccessibilityCustomAction](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction)

|  | Declaration |
| --- | --- |
| From | ``` class UIAccessibilityCustomAction : NSObject {     init(name name: String!, target target: AnyObject!, selector selector: Selector)     var name: String!     weak var target: AnyObject?     var selector: Selector } ``` |
| To | ``` class UIAccessibilityCustomAction : NSObject {     init(name name: String, target target: AnyObject?, selector selector: Selector)     var name: String     weak var target: AnyObject?     var selector: Selector } ``` |

Modified [UIAccessibilityCustomAction.init(name: String, target: AnyObject?, selector: Selector)](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/1620499-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, target target: AnyObject!, selector selector: Selector) ``` |
| To | ``` init(name name: String, target target: AnyObject?, selector selector: Selector) ``` |

Modified [UIAccessibilityCustomAction.name](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/1620502-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String ``` |

Modified [UIAccessibilityElement](https://developer.apple.com/documentation/uikit/uiaccessibilityelement)

|  | Declaration |
| --- | --- |
| From | ``` class UIAccessibilityElement : NSObject, UIAccessibilityIdentification, NSObjectProtocol {     init(accessibilityContainer container: AnyObject)     unowned(unsafe) var accessibilityContainer: AnyObject     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityFrame: CGRect     var accessibilityTraits: UIAccessibilityTraits } ``` |
| To | ``` class UIAccessibilityElement : NSObject, UIAccessibilityIdentification {     init(accessibilityContainer container: AnyObject)     unowned(unsafe) var accessibilityContainer: AnyObject?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityFrame: CGRect     var accessibilityTraits: UIAccessibilityTraits } ``` |

Modified [UIAccessibilityElement.accessibilityContainer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619581-accessibilitycontainer)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var accessibilityContainer: AnyObject ``` |
| To | ``` unowned(unsafe) var accessibilityContainer: AnyObject? ``` |

Modified [UIAccessibilityIdentification](https://developer.apple.com/documentation/uikit/uiaccessibilityidentification)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIAccessibilityIdentification : NSObjectProtocol {     var accessibilityIdentifier: String! { get set } } ``` |
| To | ``` protocol UIAccessibilityIdentification : NSObjectProtocol {     var accessibilityIdentifier: String? { get set } } ``` |

Modified [UIAccessibilityIdentification.accessibilityIdentifier](https://developer.apple.com/documentation/uikit/uiaccessibilityidentification/1623132-accessibilityidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var accessibilityIdentifier: String! { get set } ``` |
| To | ``` var accessibilityIdentifier: String? { get set } ``` |

Modified [UIAccessibilityNavigationStyle [enum]](https://developer.apple.com/documentation/uikit/uiaccessibilitynavigationstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIAccessibilityReadingContent](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIAccessibilityReadingContent {     func accessibilityLineNumberForPoint(_ point: CGPoint) -> Int     func accessibilityContentForLineNumber(_ lineNumber: Int) -> String?     func accessibilityFrameForLineNumber(_ lineNumber: Int) -> CGRect     func accessibilityPageContent() -> String! } ``` |
| To | ``` protocol UIAccessibilityReadingContent {     func accessibilityLineNumberForPoint(_ point: CGPoint) -> Int     func accessibilityContentForLineNumber(_ lineNumber: Int) -> String?     func accessibilityFrameForLineNumber(_ lineNumber: Int) -> CGRect     func accessibilityPageContent() -> String? } ``` |

Modified [UIAccessibilityReadingContent.accessibilityPageContent() -> String?](https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/1615157-accessibilitypagecontent)

|  | Declaration |
| --- | --- |
| From | ``` func accessibilityPageContent() -> String! ``` |
| To | ``` func accessibilityPageContent() -> String? ``` |

Modified [UIAccessibilityScrollDirection [enum]](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilityscrolldirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIAccessibilityScrollDirection.Next](https://developer.apple.com/documentation/uikit/uiaccessibilityscrolldirection/uiaccessibilityscrolldirectionnext)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [UIAccessibilityScrollDirection.Previous](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilityscrolldirection/previous)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [UIAccessibilityZoomType [enum]](https://developer.apple.com/documentation/uikit/uiaccessibilityzoomtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIActionSheet](https://developer.apple.com/documentation/uikit/uiactionsheet)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class UIActionSheet : UIView {     init(title title: String?, delegate delegate: UIActionSheetDelegate?, cancelButtonTitle cancelButtonTitle: String?, destructiveButtonTitle destructiveButtonTitle: String?)     unowned(unsafe) var delegate: UIActionSheetDelegate?     var title: String     var actionSheetStyle: UIActionSheetStyle     func addButtonWithTitle(_ title: String) -> Int     func buttonTitleAtIndex(_ buttonIndex: Int) -> String     var numberOfButtons: Int { get }     var cancelButtonIndex: Int     var destructiveButtonIndex: Int     var firstOtherButtonIndex: Int { get }     var visible: Bool { get }     func showFromToolbar(_ view: UIToolbar!)     func showFromTabBar(_ view: UITabBar!)     func showFromBarButtonItem(_ item: UIBarButtonItem!, animated animated: Bool)     func showFromRect(_ rect: CGRect, inView view: UIView!, animated animated: Bool)     func showInView(_ view: UIView!)     func dismissWithClickedButtonIndex(_ buttonIndex: Int, animated animated: Bool) } extension UIActionSheet {     convenience init(title title: String?, delegate delegate: UIActionSheetDelegate?, cancelButtonTitle cancelButtonTitle: String?, destructiveButtonTitle destructiveButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...) } extension UIActionSheet {     convenience init(title title: String?, delegate delegate: UIActionSheetDelegate?, cancelButtonTitle cancelButtonTitle: String?, destructiveButtonTitle destructiveButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...) } ``` | -- |
| To | ``` class UIActionSheet : UIView {     init(title title: String?, delegate delegate: UIActionSheetDelegate?, cancelButtonTitle cancelButtonTitle: String?, destructiveButtonTitle destructiveButtonTitle: String?)     weak var delegate: UIActionSheetDelegate?     var title: String     var actionSheetStyle: UIActionSheetStyle     func addButtonWithTitle(_ title: String?) -> Int     func buttonTitleAtIndex(_ buttonIndex: Int) -> String?     var numberOfButtons: Int { get }     var cancelButtonIndex: Int     var destructiveButtonIndex: Int     var firstOtherButtonIndex: Int { get }     var visible: Bool { get }     func showFromToolbar(_ view: UIToolbar)     func showFromTabBar(_ view: UITabBar)     func showFromBarButtonItem(_ item: UIBarButtonItem, animated animated: Bool)     func showFromRect(_ rect: CGRect, inView view: UIView, animated animated: Bool)     func showInView(_ view: UIView)     func dismissWithClickedButtonIndex(_ buttonIndex: Int, animated animated: Bool) } extension UIActionSheet {     convenience init(title title: String?, delegate delegate: UIActionSheetDelegate?, cancelButtonTitle cancelButtonTitle: String?, destructiveButtonTitle destructiveButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...) } extension UIActionSheet {     convenience init(title title: String?, delegate delegate: UIActionSheetDelegate?, cancelButtonTitle cancelButtonTitle: String?, destructiveButtonTitle destructiveButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...) } ``` | iOS 8.3 |

Modified [UIActionSheet.actionSheetStyle](https://developer.apple.com/documentation/uikit/uiactionsheet/1622881-actionsheetstyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.addButtonWithTitle(_: String?) -> Int](https://developer.apple.com/documentation/uikit/uiactionsheet/1622864-addbuttonwithtitle)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func addButtonWithTitle(_ title: String) -> Int ``` | -- |
| To | ``` func addButtonWithTitle(_ title: String?) -> Int ``` | iOS 8.3 |

Modified [UIActionSheet.buttonTitleAtIndex(_: Int) -> String?](https://developer.apple.com/documentation/uikit/uiactionsheet/1622871-buttontitle)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func buttonTitleAtIndex(_ buttonIndex: Int) -> String ``` | -- |
| To | ``` func buttonTitleAtIndex(_ buttonIndex: Int) -> String? ``` | iOS 8.3 |

Modified [UIActionSheet.cancelButtonIndex](https://developer.apple.com/documentation/uikit/uiactionsheet/1622866-cancelbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.delegate](https://developer.apple.com/documentation/uikit/uiactionsheet/1622878-delegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` unowned(unsafe) var delegate: UIActionSheetDelegate? ``` | -- |
| To | ``` weak var delegate: UIActionSheetDelegate? ``` | iOS 8.3 |

Modified [UIActionSheet.destructiveButtonIndex](https://developer.apple.com/documentation/uikit/uiactionsheet/1622863-destructivebuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.dismissWithClickedButtonIndex(_: Int, animated: Bool)](https://developer.apple.com/documentation/uikit/uiactionsheet/1622888-dismisswithclickedbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.firstOtherButtonIndex](https://developer.apple.com/documentation/uikit/uiactionsheet/1622870-firstotherbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.init(title: String?, delegate: UIActionSheetDelegate?, cancelButtonTitle: String?, destructiveButtonTitle: String?)](https://developer.apple.com/documentation/uikit/uiactionsheet/1622875-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.numberOfButtons](https://developer.apple.com/documentation/uikit/uiactionsheet/1622891-numberofbuttons)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.showFromBarButtonItem(_: UIBarButtonItem, animated: Bool)](https://developer.apple.com/documentation/uikit/uiactionsheet/1622869-showfrombarbuttonitem)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func showFromBarButtonItem(_ item: UIBarButtonItem!, animated animated: Bool) ``` | -- |
| To | ``` func showFromBarButtonItem(_ item: UIBarButtonItem, animated animated: Bool) ``` | iOS 8.3 |

Modified [UIActionSheet.showFromRect(_: CGRect, inView: UIView, animated: Bool)](https://developer.apple.com/documentation/uikit/uiactionsheet/1622892-show)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func showFromRect(_ rect: CGRect, inView view: UIView!, animated animated: Bool) ``` | -- |
| To | ``` func showFromRect(_ rect: CGRect, inView view: UIView, animated animated: Bool) ``` | iOS 8.3 |

Modified [UIActionSheet.showFromTabBar(_: UITabBar)](https://developer.apple.com/documentation/uikit/uiactionsheet/1622872-show)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func showFromTabBar(_ view: UITabBar!) ``` | -- |
| To | ``` func showFromTabBar(_ view: UITabBar) ``` | iOS 8.3 |

Modified [UIActionSheet.showFromToolbar(_: UIToolbar)](https://developer.apple.com/documentation/uikit/uiactionsheet/1622874-showfromtoolbar)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func showFromToolbar(_ view: UIToolbar!) ``` | -- |
| To | ``` func showFromToolbar(_ view: UIToolbar) ``` | iOS 8.3 |

Modified [UIActionSheet.showInView(_: UIView)](https://developer.apple.com/documentation/uikit/uiactionsheet/1622886-show)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func showInView(_ view: UIView!) ``` | -- |
| To | ``` func showInView(_ view: UIView) ``` | iOS 8.3 |

Modified [UIActionSheet.title](https://developer.apple.com/documentation/uikit/uiactionsheet/1622882-title)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheet.visible](https://developer.apple.com/documentation/uikit/uiactionsheet/1622885-isvisible)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.3 |

Modified [UIActionSheetDelegate.actionSheet(_: UIActionSheet, clickedButtonAtIndex: Int)](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622876-actionsheet)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.3 |

Modified [UIActionSheetDelegate.actionSheet(_: UIActionSheet, didDismissWithButtonIndex: Int)](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622879-actionsheet)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.3 |

Modified [UIActionSheetDelegate.actionSheet(_: UIActionSheet, willDismissWithButtonIndex: Int)](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622884-actionsheet)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.3 |

Modified [UIActionSheetDelegate.actionSheetCancel(_: UIActionSheet)](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622867-actionsheetcancel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.3 |

Modified [UIActionSheetDelegate.didPresentActionSheet(_: UIActionSheet)](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622877-didpresentactionsheet)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.3 |

Modified [UIActionSheetDelegate.willPresentActionSheet(_: UIActionSheet)](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/1622865-willpresent)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.3 |

Modified [UIActionSheetStyle [enum]](https://developer.apple.com/documentation/uikit/uiactionsheetstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIActivityCategory [enum]](https://developer.apple.com/documentation/uikit/uiactivity/category)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview)

|  | Declaration |
| --- | --- |
| From | ``` class UIActivityIndicatorView : UIView, NSCoding {     init!(activityIndicatorStyle style: UIActivityIndicatorViewStyle)     var activityIndicatorViewStyle: UIActivityIndicatorViewStyle     var hidesWhenStopped: Bool     var color: UIColor!     func startAnimating()     func stopAnimating()     func isAnimating() -> Bool } ``` |
| To | ``` class UIActivityIndicatorView : UIView {     init(activityIndicatorStyle style: UIActivityIndicatorViewStyle)     init(frame frame: CGRect)     init(coder coder: NSCoder)     var activityIndicatorViewStyle: UIActivityIndicatorViewStyle     var hidesWhenStopped: Bool     var color: UIColor?     func startAnimating()     func stopAnimating()     func isAnimating() -> Bool } ``` |

Modified [UIActivityIndicatorView.color](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622836-color)

|  | Declaration |
| --- | --- |
| From | ``` var color: UIColor! ``` |
| To | ``` var color: UIColor? ``` |

Modified [UIActivityIndicatorView.init(activityIndicatorStyle: UIActivityIndicatorViewStyle)](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/1622840-initwithactivityindicatorstyle)

|  | Declaration |
| --- | --- |
| From | ``` init!(activityIndicatorStyle style: UIActivityIndicatorViewStyle) ``` |
| To | ``` init(activityIndicatorStyle style: UIActivityIndicatorViewStyle) ``` |

Modified [UIActivityIndicatorViewStyle [enum]](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/style)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIActivityItemProvider](https://developer.apple.com/documentation/uikit/uiactivityitemprovider)

|  | Declaration |
| --- | --- |
| From | ``` class UIActivityItemProvider : NSOperation, UIActivityItemSource, NSObjectProtocol {     init(placeholderItem placeholderItem: AnyObject)     var placeholderItem: AnyObject! { get }     var activityType: String? { get }     func item() -> AnyObject! } ``` |
| To | ``` class UIActivityItemProvider : NSOperation, UIActivityItemSource {     convenience init()     init(placeholderItem placeholderItem: AnyObject)     var placeholderItem: AnyObject? { get }     var activityType: String? { get }     func item() -> AnyObject } ``` |

Modified [UIActivityItemProvider.item() -> AnyObject](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/1620457-item)

|  | Declaration |
| --- | --- |
| From | ``` func item() -> AnyObject! ``` |
| To | ``` func item() -> AnyObject ``` |

Modified [UIActivityItemProvider.placeholderItem](https://developer.apple.com/documentation/uikit/uiactivityitemprovider/1620454-placeholderitem)

|  | Declaration |
| --- | --- |
| From | ``` var placeholderItem: AnyObject! { get } ``` |
| To | ``` var placeholderItem: AnyObject? { get } ``` |

Modified [UIActivityItemSource](https://developer.apple.com/documentation/uikit/uiactivityitemsource)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIActivityItemSource : NSObjectProtocol {     func activityViewControllerPlaceholderItem(_ activityViewController: UIActivityViewController) -> AnyObject     func activityViewController(_ activityViewController: UIActivityViewController, itemForActivityType activityType: String) -> AnyObject?     optional func activityViewController(_ activityViewController: UIActivityViewController, subjectForActivityType activityType: String?) -> String     optional func activityViewController(_ activityViewController: UIActivityViewController, dataTypeIdentifierForActivityType activityType: String?) -> String     optional func activityViewController(_ activityViewController: UIActivityViewController, thumbnailImageForActivityType activityType: String!, suggestedSize size: CGSize) -> UIImage! } ``` |
| To | ``` protocol UIActivityItemSource : NSObjectProtocol {     func activityViewControllerPlaceholderItem(_ activityViewController: UIActivityViewController) -> AnyObject     func activityViewController(_ activityViewController: UIActivityViewController, itemForActivityType activityType: String) -> AnyObject?     optional func activityViewController(_ activityViewController: UIActivityViewController, subjectForActivityType activityType: String?) -> String     optional func activityViewController(_ activityViewController: UIActivityViewController, dataTypeIdentifierForActivityType activityType: String?) -> String     optional func activityViewController(_ activityViewController: UIActivityViewController, thumbnailImageForActivityType activityType: String?, suggestedSize size: CGSize) -> UIImage? } ``` |

Modified [UIActivityItemSource.activityViewController(_: UIActivityViewController, dataTypeIdentifierForActivityType: String?) -> String](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620456-activityviewcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UIActivityItemSource.activityViewController(_: UIActivityViewController, itemForActivityType: String) -> AnyObject?](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620453-activityviewcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UIActivityItemSource.activityViewController(_: UIActivityViewController, subjectForActivityType: String?) -> String](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620455-activityviewcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UIActivityItemSource.activityViewController(_: UIActivityViewController, thumbnailImageForActivityType: String?, suggestedSize: CGSize) -> UIImage?](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620462-activityviewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func activityViewController(_ activityViewController: UIActivityViewController, thumbnailImageForActivityType activityType: String!, suggestedSize size: CGSize) -> UIImage! ``` | iOS 8.0 |
| To | ``` optional func activityViewController(_ activityViewController: UIActivityViewController, thumbnailImageForActivityType activityType: String?, suggestedSize size: CGSize) -> UIImage? ``` | iOS 6.0 |

Modified [UIActivityItemSource.activityViewControllerPlaceholderItem(_: UIActivityViewController) -> AnyObject](https://developer.apple.com/documentation/uikit/uiactivityitemsource/1620458-activityviewcontrollerplaceholde)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIActivityViewController : UIViewController {     init(activityItems activityItems: [AnyObject], applicationActivities applicationActivities: [AnyObject]?)     var completionHandler: UIActivityViewControllerCompletionHandler?     var completionWithItemsHandler: UIActivityViewControllerCompletionWithItemsHandler?     var excludedActivityTypes: [AnyObject]? } ``` |
| To | ``` class UIActivityViewController : UIViewController {     convenience init()     convenience init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     convenience init?(coder aDecoder: NSCoder)     init(activityItems activityItems: [AnyObject], applicationActivities applicationActivities: [UIActivity]?)     var completionHandler: UIActivityViewControllerCompletionHandler?     var completionWithItemsHandler: UIActivityViewControllerCompletionWithItemsHandler?     var excludedActivityTypes: [String]? } ``` |

Modified [UIActivityViewController.excludedActivityTypes](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622009-excludedactivitytypes)

|  | Declaration |
| --- | --- |
| From | ``` var excludedActivityTypes: [AnyObject]? ``` |
| To | ``` var excludedActivityTypes: [String]? ``` |

Modified [UIActivityViewController.init(activityItems: [AnyObject], applicationActivities: [UIActivity]?)](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622019-initwithactivityitems)

|  | Declaration |
| --- | --- |
| From | ``` init(activityItems activityItems: [AnyObject], applicationActivities applicationActivities: [AnyObject]?) ``` |
| To | ``` init(activityItems activityItems: [AnyObject], applicationActivities applicationActivities: [UIActivity]?) ``` |

Modified [UIAdaptivePresentationControllerDelegate](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIAdaptivePresentationControllerDelegate : NSObjectProtocol {     optional func adaptivePresentationStyleForPresentationController(_ controller: UIPresentationController) -> UIModalPresentationStyle     optional func adaptivePresentationStyleForPresentationController(_ controller: UIPresentationController!, traitCollection traitCollection: UITraitCollection!) -> UIModalPresentationStyle     optional func presentationController(_ controller: UIPresentationController, viewControllerForAdaptivePresentationStyle style: UIModalPresentationStyle) -> UIViewController?     optional func presentationController(_ presentationController: UIPresentationController!, willPresentWithAdaptiveStyle style: UIModalPresentationStyle, transitionCoordinator transitionCoordinator: UIViewControllerTransitionCoordinator!) } ``` |
| To | ``` protocol UIAdaptivePresentationControllerDelegate : NSObjectProtocol {     optional func adaptivePresentationStyleForPresentationController(_ controller: UIPresentationController) -> UIModalPresentationStyle     optional func adaptivePresentationStyleForPresentationController(_ controller: UIPresentationController, traitCollection traitCollection: UITraitCollection) -> UIModalPresentationStyle     optional func presentationController(_ controller: UIPresentationController, viewControllerForAdaptivePresentationStyle style: UIModalPresentationStyle) -> UIViewController?     optional func presentationController(_ presentationController: UIPresentationController, willPresentWithAdaptiveStyle style: UIModalPresentationStyle, transitionCoordinator transitionCoordinator: UIViewControllerTransitionCoordinator?) } ``` |

Modified [UIAdaptivePresentationControllerDelegate.adaptivePresentationStyleForPresentationController(_: UIPresentationController, traitCollection: UITraitCollection) -> UIModalPresentationStyle](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/1618334-adaptivepresentationstyleforpres)

|  | Declaration |
| --- | --- |
| From | ``` optional func adaptivePresentationStyleForPresentationController(_ controller: UIPresentationController!, traitCollection traitCollection: UITraitCollection!) -> UIModalPresentationStyle ``` |
| To | ``` optional func adaptivePresentationStyleForPresentationController(_ controller: UIPresentationController, traitCollection traitCollection: UITraitCollection) -> UIModalPresentationStyle ``` |

Modified [UIAdaptivePresentationControllerDelegate.presentationController(_: UIPresentationController, willPresentWithAdaptiveStyle: UIModalPresentationStyle, transitionCoordinator: UIViewControllerTransitionCoordinator?)](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/1618324-presentationcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func presentationController(_ presentationController: UIPresentationController!, willPresentWithAdaptiveStyle style: UIModalPresentationStyle, transitionCoordinator transitionCoordinator: UIViewControllerTransitionCoordinator!) ``` |
| To | ``` optional func presentationController(_ presentationController: UIPresentationController, willPresentWithAdaptiveStyle style: UIModalPresentationStyle, transitionCoordinator transitionCoordinator: UIViewControllerTransitionCoordinator?) ``` |

Modified [UIAlertAction](https://developer.apple.com/documentation/uikit/uialertaction)

|  | Declaration |
| --- | --- |
| From | ``` class UIAlertAction : NSObject, NSCopying {     convenience init(title title: String, style style: UIAlertActionStyle, handler handler: ((UIAlertAction!) -> Void)!)     class func actionWithTitle(_ title: String, style style: UIAlertActionStyle, handler handler: ((UIAlertAction!) -> Void)!) -> Self     var title: String { get }     var style: UIAlertActionStyle { get }     var enabled: Bool } ``` |
| To | ``` class UIAlertAction : NSObject, NSCopying {     convenience init(title title: String?, style style: UIAlertActionStyle, handler handler: ((UIAlertAction) -> Void)?)     class func actionWithTitle(_ title: String?, style style: UIAlertActionStyle, handler handler: ((UIAlertAction) -> Void)?) -> Self     var title: String? { get }     var style: UIAlertActionStyle { get }     var enabled: Bool } ``` |

Modified [UIAlertAction.init(title: String?, style: UIAlertActionStyle, handler: ((UIAlertAction) -> Void)?)](https://developer.apple.com/documentation/uikit/uialertaction/1620097-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(title title: String, style style: UIAlertActionStyle, handler handler: ((UIAlertAction!) -> Void)!) ``` |
| To | ``` convenience init(title title: String?, style style: UIAlertActionStyle, handler handler: ((UIAlertAction) -> Void)?) ``` |

Modified [UIAlertAction.title](https://developer.apple.com/documentation/uikit/uialertaction/1620098-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String { get } ``` |
| To | ``` var title: String? { get } ``` |

Modified [UIAlertActionStyle [enum]](https://developer.apple.com/documentation/uikit/uialertactionstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIAlertController : UIViewController {     convenience init(title title: String?, message message: String?, preferredStyle preferredStyle: UIAlertControllerStyle)     class func alertControllerWithTitle(_ title: String?, message message: String?, preferredStyle preferredStyle: UIAlertControllerStyle) -> Self     func addAction(_ action: UIAlertAction)     var actions: [AnyObject] { get }     func addTextFieldWithConfigurationHandler(_ configurationHandler: ((UITextField!) -> Void)!)     var textFields: [AnyObject]? { get }     var title: String?     var message: String?     var preferredStyle: UIAlertControllerStyle { get } } ``` |
| To | ``` class UIAlertController : UIViewController {     convenience init(title title: String?, message message: String?, preferredStyle preferredStyle: UIAlertControllerStyle)     class func alertControllerWithTitle(_ title: String?, message message: String?, preferredStyle preferredStyle: UIAlertControllerStyle) -> Self     func addAction(_ action: UIAlertAction)     var actions: [UIAlertAction] { get }     var preferredAction: UIAlertAction?     func addTextFieldWithConfigurationHandler(_ configurationHandler: ((UITextField) -> Void)?)     var textFields: [UITextField]? { get }     var title: String?     var message: String?     var preferredStyle: UIAlertControllerStyle { get } } ``` |

Modified [UIAlertController.actions](https://developer.apple.com/documentation/uikit/uialertcontroller/1620099-actions)

|  | Declaration |
| --- | --- |
| From | ``` var actions: [AnyObject] { get } ``` |
| To | ``` var actions: [UIAlertAction] { get } ``` |

Modified [UIAlertController.addTextFieldWithConfigurationHandler(_: ((UITextField) -> Void)?)](https://developer.apple.com/documentation/uikit/uialertcontroller/1620093-addtextfieldwithconfigurationhan)

|  | Declaration |
| --- | --- |
| From | ``` func addTextFieldWithConfigurationHandler(_ configurationHandler: ((UITextField!) -> Void)!) ``` |
| To | ``` func addTextFieldWithConfigurationHandler(_ configurationHandler: ((UITextField) -> Void)?) ``` |

Modified [UIAlertController.textFields](https://developer.apple.com/documentation/uikit/uialertcontroller/1620104-textfields)

|  | Declaration |
| --- | --- |
| From | ``` var textFields: [AnyObject]? { get } ``` |
| To | ``` var textFields: [UITextField]? { get } ``` |

Modified [UIAlertControllerStyle [enum]](https://developer.apple.com/documentation/uikit/uialertcontrollerstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIAlertView](https://developer.apple.com/documentation/uikit/uialertview)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class UIAlertView : UIView {     init(title title: String?, message message: String?, delegate delegate: AnyObject?, cancelButtonTitle cancelButtonTitle: String?)     unowned(unsafe) var delegate: AnyObject?     var title: String     var message: String?     func addButtonWithTitle(_ title: String) -> Int     func buttonTitleAtIndex(_ buttonIndex: Int) -> String!     var numberOfButtons: Int { get }     var cancelButtonIndex: Int     var firstOtherButtonIndex: Int { get }     var visible: Bool { get }     func show()     func dismissWithClickedButtonIndex(_ buttonIndex: Int, animated animated: Bool)     var alertViewStyle: UIAlertViewStyle     func textFieldAtIndex(_ textFieldIndex: Int) -> UITextField? } extension UIAlertView {     convenience init(title title: String, message message: String, delegate delegate: UIAlertViewDelegate?, cancelButtonTitle cancelButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...) } extension UIAlertView {     convenience init(title title: String, message message: String, delegate delegate: UIAlertViewDelegate?, cancelButtonTitle cancelButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...) } ``` | -- |
| To | ``` class UIAlertView : UIView {     convenience init(title title: String?, message message: String?, delegate delegate: AnyObject?, cancelButtonTitle cancelButtonTitle: String?)     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     weak var delegate: AnyObject?     var title: String     var message: String?     func addButtonWithTitle(_ title: String?) -> Int     func buttonTitleAtIndex(_ buttonIndex: Int) -> String?     var numberOfButtons: Int { get }     var cancelButtonIndex: Int     var firstOtherButtonIndex: Int { get }     var visible: Bool { get }     func show()     func dismissWithClickedButtonIndex(_ buttonIndex: Int, animated animated: Bool)     var alertViewStyle: UIAlertViewStyle     func textFieldAtIndex(_ textFieldIndex: Int) -> UITextField? } extension UIAlertView {     convenience init(title title: String, message message: String, delegate delegate: UIAlertViewDelegate?, cancelButtonTitle cancelButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...) } extension UIAlertView {     convenience init(title title: String, message message: String, delegate delegate: UIAlertViewDelegate?, cancelButtonTitle cancelButtonTitle: String?, otherButtonTitles firstButtonTitle: String, _ moreButtonTitles: String...) } ``` | iOS 9.0 |

Modified [UIAlertView.addButtonWithTitle(_: String?) -> Int](https://developer.apple.com/documentation/uikit/uialertview/1620761-addbutton)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func addButtonWithTitle(_ title: String) -> Int ``` | -- |
| To | ``` func addButtonWithTitle(_ title: String?) -> Int ``` | iOS 9.0 |

Modified [UIAlertView.alertViewStyle](https://developer.apple.com/documentation/uikit/uialertview/1620780-alertviewstyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.buttonTitleAtIndex(_: Int) -> String?](https://developer.apple.com/documentation/uikit/uialertview/1620756-buttontitleatindex)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func buttonTitleAtIndex(_ buttonIndex: Int) -> String! ``` | -- |
| To | ``` func buttonTitleAtIndex(_ buttonIndex: Int) -> String? ``` | iOS 9.0 |

Modified [UIAlertView.cancelButtonIndex](https://developer.apple.com/documentation/uikit/uialertview/1620766-cancelbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.delegate](https://developer.apple.com/documentation/uikit/uialertview/1620769-delegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` unowned(unsafe) var delegate: AnyObject? ``` | -- |
| To | ``` weak var delegate: AnyObject? ``` | iOS 9.0 |

Modified [UIAlertView.dismissWithClickedButtonIndex(_: Int, animated: Bool)](https://developer.apple.com/documentation/uikit/uialertview/1620754-dismiss)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.firstOtherButtonIndex](https://developer.apple.com/documentation/uikit/uialertview/1620771-firstotherbuttonindex)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.init(title: String?, message: String?, delegate: AnyObject?, cancelButtonTitle: String?)](https://developer.apple.com/documentation/uikit/uialertview/1620765-initwithtitle)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` init(title title: String?, message message: String?, delegate delegate: AnyObject?, cancelButtonTitle cancelButtonTitle: String?) ``` | -- |
| To | ``` convenience init(title title: String?, message message: String?, delegate delegate: AnyObject?, cancelButtonTitle cancelButtonTitle: String?) ``` | iOS 9.0 |

Modified [UIAlertView.message](https://developer.apple.com/documentation/uikit/uialertview/1620758-message)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.numberOfButtons](https://developer.apple.com/documentation/uikit/uialertview/1620753-numberofbuttons)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.show()](https://developer.apple.com/documentation/uikit/uialertview/1620751-show)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.textFieldAtIndex(_: Int) -> UITextField?](https://developer.apple.com/documentation/uikit/uialertview/1620757-textfield)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.title](https://developer.apple.com/documentation/uikit/uialertview/1620768-title)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertView.visible](https://developer.apple.com/documentation/uikit/uialertview/1620764-visible)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIAlertViewDelegate.alertView(_: UIAlertView, clickedButtonAtIndex: Int)](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620752-alertview)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIAlertViewDelegate.alertView(_: UIAlertView, didDismissWithButtonIndex: Int)](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620772-alertview)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIAlertViewDelegate.alertView(_: UIAlertView, willDismissWithButtonIndex: Int)](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620763-alertview)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIAlertViewDelegate.alertViewCancel(_: UIAlertView)](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620778-alertviewcancel)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIAlertViewDelegate.alertViewShouldEnableFirstOtherButton(_: UIAlertView) -> Bool](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620774-alertviewshouldenablefirstotherb)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIAlertViewDelegate.didPresentAlertView(_: UIAlertView)](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620750-didpresent)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIAlertViewDelegate.willPresentAlertView(_: UIAlertView)](https://developer.apple.com/documentation/uikit/uialertviewdelegate/1620767-willpresent)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIAlertViewStyle [enum]](https://developer.apple.com/documentation/uikit/uialertviewstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIAppearance](https://developer.apple.com/documentation/uikit/uiappearance)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIAppearance : NSObjectProtocol {     static func appearance() -> Self     static func appearanceForTraitCollection(_ trait: UITraitCollection) -> Self } ``` |
| To | ``` protocol UIAppearance : NSObjectProtocol {     static func appearance() -> Self     static func appearanceWhenContainedInInstancesOfClasses(_ containerTypes: [AnyObject.Type]) -> Self     static func appearanceForTraitCollection(_ trait: UITraitCollection) -> Self     static func appearanceForTraitCollection(_ trait: UITraitCollection, whenContainedInInstancesOfClasses containerTypes: [AnyObject.Type]) -> Self } ``` |

Modified [UIApplication](https://developer.apple.com/documentation/uikit/uiapplication)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIApplication : UIResponder, UIActionSheetDelegate, NSObjectProtocol {     class func sharedApplication() -> UIApplication     unowned(unsafe) var delegate: UIApplicationDelegate?     func beginIgnoringInteractionEvents()     func endIgnoringInteractionEvents()     func isIgnoringInteractionEvents() -> Bool     var idleTimerDisabled: Bool     func openURL(_ url: NSURL) -> Bool     func canOpenURL(_ url: NSURL) -> Bool     func sendEvent(_ event: UIEvent)     var keyWindow: UIWindow? { get }     var windows: [AnyObject] { get }     func sendAction(_ action: Selector, to target: AnyObject?, from sender: AnyObject?, forEvent event: UIEvent?) -> Bool     var networkActivityIndicatorVisible: Bool     var statusBarStyle: UIStatusBarStyle     func setStatusBarStyle(_ statusBarStyle: UIStatusBarStyle, animated animated: Bool)     var statusBarHidden: Bool     func setStatusBarHidden(_ hidden: Bool, withAnimation animation: UIStatusBarAnimation)     var statusBarOrientation: UIInterfaceOrientation     func setStatusBarOrientation(_ interfaceOrientation: UIInterfaceOrientation, animated animated: Bool)     func supportedInterfaceOrientationsForWindow(_ window: UIWindow) -> Int     var statusBarOrientationAnimationDuration: NSTimeInterval { get }     var statusBarFrame: CGRect { get }     var applicationIconBadgeNumber: Int     var applicationSupportsShakeToEdit: Bool     var applicationState: UIApplicationState { get }     var backgroundTimeRemaining: NSTimeInterval { get }     func beginBackgroundTaskWithExpirationHandler(_ handler: () -> Void) -> UIBackgroundTaskIdentifier     func beginBackgroundTaskWithName(_ taskName: String?, expirationHandler handler: (() -> Void)?) -> UIBackgroundTaskIdentifier     func endBackgroundTask(_ identifier: UIBackgroundTaskIdentifier)     func setMinimumBackgroundFetchInterval(_ minimumBackgroundFetchInterval: NSTimeInterval)     var backgroundRefreshStatus: UIBackgroundRefreshStatus { get }     func setKeepAliveTimeout(_ timeout: NSTimeInterval, handler keepAliveHandler: (() -> Void)?) -> Bool     func clearKeepAliveTimeout()     var protectedDataAvailable: Bool { get }     var userInterfaceLayoutDirection: UIUserInterfaceLayoutDirection { get }     var preferredContentSizeCategory: String { get } } extension UIApplication {     func registerForRemoteNotifications()     func unregisterForRemoteNotifications()     func isRegisteredForRemoteNotifications() -> Bool     func registerForRemoteNotificationTypes(_ types: UIRemoteNotificationType)     func enabledRemoteNotificationTypes() -> UIRemoteNotificationType } extension UIApplication {     func presentLocalNotificationNow(_ notification: UILocalNotification)     func scheduleLocalNotification(_ notification: UILocalNotification)     func cancelLocalNotification(_ notification: UILocalNotification)     func cancelAllLocalNotifications()     var scheduledLocalNotifications: [AnyObject]! } extension UIApplication {     func registerUserNotificationSettings(_ notificationSettings: UIUserNotificationSettings)     func currentUserNotificationSettings() -> UIUserNotificationSettings! } extension UIApplication {     func beginReceivingRemoteControlEvents()     func endReceivingRemoteControlEvents() } extension UIApplication {     func setNewsstandIconImage(_ image: UIImage?) } extension UIApplication {     func extendStateRestoration()     func completeStateRestoration()     func ignoreSnapshotOnNextApplicationLaunch()     class func registerObjectForStateRestoration(_ object: UIStateRestoring, restorationIdentifier restorationIdentifier: String) } extension UIApplication {     var proximitySensingEnabled: Bool     func setStatusBarHidden(_ hidden: Bool, animated animated: Bool) } ``` | AnyObject, NSObjectProtocol, UIActionSheetDelegate |
| To | ``` class UIApplication : UIResponder {     class func sharedApplication() -> UIApplication     unowned(unsafe) var delegate: UIApplicationDelegate?     func beginIgnoringInteractionEvents()     func endIgnoringInteractionEvents()     func isIgnoringInteractionEvents() -> Bool     var idleTimerDisabled: Bool     func openURL(_ url: NSURL) -> Bool     func canOpenURL(_ url: NSURL) -> Bool     func sendEvent(_ event: UIEvent)     var keyWindow: UIWindow? { get }     var windows: [UIWindow] { get }     func sendAction(_ action: Selector, to target: AnyObject?, from sender: AnyObject?, forEvent event: UIEvent?) -> Bool     var networkActivityIndicatorVisible: Bool     func supportedInterfaceOrientationsForWindow(_ window: UIWindow?) -> UIInterfaceOrientationMask     var statusBarOrientationAnimationDuration: NSTimeInterval { get }     var statusBarFrame: CGRect { get }     var applicationIconBadgeNumber: Int     var applicationSupportsShakeToEdit: Bool     var applicationState: UIApplicationState { get }     var backgroundTimeRemaining: NSTimeInterval { get }     func beginBackgroundTaskWithExpirationHandler(_ handler: (() -> Void)?) -> UIBackgroundTaskIdentifier     func beginBackgroundTaskWithName(_ taskName: String?, expirationHandler handler: (() -> Void)?) -> UIBackgroundTaskIdentifier     func endBackgroundTask(_ identifier: UIBackgroundTaskIdentifier)     func setMinimumBackgroundFetchInterval(_ minimumBackgroundFetchInterval: NSTimeInterval)     var backgroundRefreshStatus: UIBackgroundRefreshStatus { get }     var protectedDataAvailable: Bool { get }     var userInterfaceLayoutDirection: UIUserInterfaceLayoutDirection { get }     var preferredContentSizeCategory: String { get } } extension UIApplication {     func registerForRemoteNotifications()     func unregisterForRemoteNotifications()     func isRegisteredForRemoteNotifications() -> Bool     func registerForRemoteNotificationTypes(_ types: UIRemoteNotificationType)     func enabledRemoteNotificationTypes() -> UIRemoteNotificationType } extension UIApplication {     func presentLocalNotificationNow(_ notification: UILocalNotification)     func scheduleLocalNotification(_ notification: UILocalNotification)     func cancelLocalNotification(_ notification: UILocalNotification)     func cancelAllLocalNotifications()     var scheduledLocalNotifications: [UILocalNotification]? } extension UIApplication {     func registerUserNotificationSettings(_ notificationSettings: UIUserNotificationSettings)     func currentUserNotificationSettings() -> UIUserNotificationSettings? } extension UIApplication {     func beginReceivingRemoteControlEvents()     func endReceivingRemoteControlEvents() } extension UIApplication {     func setNewsstandIconImage(_ image: UIImage?) } extension UIApplication {     var shortcutItems: [UIApplicationShortcutItem]? } extension UIApplication {     func extendStateRestoration()     func completeStateRestoration()     func ignoreSnapshotOnNextApplicationLaunch()     class func registerObjectForStateRestoration(_ object: UIStateRestoring, restorationIdentifier restorationIdentifier: String) } extension UIApplication {     var proximitySensingEnabled: Bool     func setStatusBarHidden(_ hidden: Bool, animated animated: Bool)     var statusBarOrientation: UIInterfaceOrientation     func setStatusBarOrientation(_ interfaceOrientation: UIInterfaceOrientation, animated animated: Bool)     var statusBarStyle: UIStatusBarStyle     func setStatusBarStyle(_ statusBarStyle: UIStatusBarStyle, animated animated: Bool)     var statusBarHidden: Bool     func setStatusBarHidden(_ hidden: Bool, withAnimation animation: UIStatusBarAnimation)     func setKeepAliveTimeout(_ timeout: NSTimeInterval, handler keepAliveHandler: (() -> Void)?) -> Bool     func clearKeepAliveTimeout() } ``` | AnyObject |

Modified [UIApplication.beginBackgroundTaskWithExpirationHandler(_: (() -> Void)?) -> UIBackgroundTaskIdentifier](https://developer.apple.com/documentation/uikit/uiapplication/1623031-beginbackgroundtaskwithexpiratio)

|  | Declaration |
| --- | --- |
| From | ``` func beginBackgroundTaskWithExpirationHandler(_ handler: () -> Void) -> UIBackgroundTaskIdentifier ``` |
| To | ``` func beginBackgroundTaskWithExpirationHandler(_ handler: (() -> Void)?) -> UIBackgroundTaskIdentifier ``` |

Modified [UIApplication.clearKeepAliveTimeout()](https://developer.apple.com/documentation/uikit/uiapplication/1622986-clearkeepalivetimeout)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIApplication.currentUserNotificationSettings() -> UIUserNotificationSettings?](https://developer.apple.com/documentation/uikit/uiapplication/1623092-currentusernotificationsettings)

|  | Declaration |
| --- | --- |
| From | ``` func currentUserNotificationSettings() -> UIUserNotificationSettings! ``` |
| To | ``` func currentUserNotificationSettings() -> UIUserNotificationSettings? ``` |

Modified [UIApplication.scheduledLocalNotifications](https://developer.apple.com/documentation/uikit/uiapplication/1622993-scheduledlocalnotifications)

|  | Declaration |
| --- | --- |
| From | ``` var scheduledLocalNotifications: [AnyObject]! ``` |
| To | ``` var scheduledLocalNotifications: [UILocalNotification]? ``` |

Modified [UIApplication.setKeepAliveTimeout(_: NSTimeInterval, handler: (() -> Void)?) -> Bool](https://developer.apple.com/documentation/uikit/uiapplication/1622989-setkeepalivetimeout)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIApplication.setNewsstandIconImage(_: UIImage?)](https://developer.apple.com/documentation/uikit/uiapplication/1623016-setnewsstandiconimage)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 9.0 | iOS 9.0 |

Modified [UIApplication.setStatusBarHidden(_: Bool, withAnimation: UIStatusBarAnimation)](https://developer.apple.com/documentation/uikit/uiapplication/1622949-setstatusbarhidden)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIApplication.setStatusBarOrientation(_: UIInterfaceOrientation, animated: Bool)](https://developer.apple.com/documentation/uikit/uiapplication/1622939-setstatusbarorientation)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIApplication.setStatusBarStyle(_: UIStatusBarStyle, animated: Bool)](https://developer.apple.com/documentation/uikit/uiapplication/1622923-setstatusbarstyle)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIApplication.statusBarHidden](https://developer.apple.com/documentation/uikit/uiapplication/1622982-isstatusbarhidden)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIApplication.statusBarOrientation](https://developer.apple.com/documentation/uikit/uiapplication/1623026-statusbarorientation)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIApplication.statusBarStyle](https://developer.apple.com/documentation/uikit/uiapplication/1622988-statusbarstyle)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIApplication.supportedInterfaceOrientationsForWindow(_: UIWindow?) -> UIInterfaceOrientationMask](https://developer.apple.com/documentation/uikit/uiapplication/1623091-supportedinterfaceorientations)

|  | Declaration |
| --- | --- |
| From | ``` func supportedInterfaceOrientationsForWindow(_ window: UIWindow) -> Int ``` |
| To | ``` func supportedInterfaceOrientationsForWindow(_ window: UIWindow?) -> UIInterfaceOrientationMask ``` |

Modified [UIApplication.windows](https://developer.apple.com/documentation/uikit/uiapplication/1623104-windows)

|  | Declaration |
| --- | --- |
| From | ``` var windows: [AnyObject] { get } ``` |
| To | ``` var windows: [UIWindow] { get } ``` |

Modified [UIApplicationDelegate](https://developer.apple.com/documentation/uikit/uiapplicationdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIApplicationDelegate : NSObjectProtocol {     optional func applicationDidFinishLaunching(_ application: UIApplication)     optional func application(_ application: UIApplication, willFinishLaunchingWithOptions launchOptions: [NSObject : AnyObject]?) -> Bool     optional func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject : AnyObject]?) -> Bool     optional func applicationDidBecomeActive(_ application: UIApplication)     optional func applicationWillResignActive(_ application: UIApplication)     optional func application(_ application: UIApplication, handleOpenURL url: NSURL) -> Bool     optional func application(_ application: UIApplication, openURL url: NSURL, sourceApplication sourceApplication: String?, annotation annotation: AnyObject?) -> Bool     optional func applicationDidReceiveMemoryWarning(_ application: UIApplication)     optional func applicationWillTerminate(_ application: UIApplication)     optional func applicationSignificantTimeChange(_ application: UIApplication)     optional func application(_ application: UIApplication, willChangeStatusBarOrientation newStatusBarOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     optional func application(_ application: UIApplication, didChangeStatusBarOrientation oldStatusBarOrientation: UIInterfaceOrientation)     optional func application(_ application: UIApplication, willChangeStatusBarFrame newStatusBarFrame: CGRect)     optional func application(_ application: UIApplication, didChangeStatusBarFrame oldStatusBarFrame: CGRect)     optional func application(_ application: UIApplication, didRegisterUserNotificationSettings notificationSettings: UIUserNotificationSettings)     optional func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: NSData)     optional func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: NSError)     optional func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [NSObject : AnyObject])     optional func application(_ application: UIApplication, didReceiveLocalNotification notification: UILocalNotification)     optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, forLocalNotification notification: UILocalNotification, completionHandler completionHandler: () -> Void)     optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, forRemoteNotification userInfo: [NSObject : AnyObject], completionHandler completionHandler: () -> Void)     optional func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [NSObject : AnyObject], fetchCompletionHandler completionHandler: (UIBackgroundFetchResult) -> Void)     optional func application(_ application: UIApplication, performFetchWithCompletionHandler completionHandler: (UIBackgroundFetchResult) -> Void)     optional func application(_ application: UIApplication, handleEventsForBackgroundURLSession identifier: String, completionHandler completionHandler: () -> Void)     optional func application(_ application: UIApplication, handleWatchKitExtensionRequest userInfo: [NSObject : AnyObject]?, reply reply: (([NSObject : AnyObject]!) -> Void)!)     optional func applicationDidEnterBackground(_ application: UIApplication)     optional func applicationWillEnterForeground(_ application: UIApplication)     optional func applicationProtectedDataWillBecomeUnavailable(_ application: UIApplication)     optional func applicationProtectedDataDidBecomeAvailable(_ application: UIApplication)     optional var window: UIWindow? { get set }     optional func application(_ application: UIApplication, supportedInterfaceOrientationsForWindow window: UIWindow?) -> Int     optional func application(_ application: UIApplication, shouldAllowExtensionPointIdentifier extensionPointIdentifier: String) -> Bool     optional func application(_ application: UIApplication, viewControllerWithRestorationIdentifierPath identifierComponents: [AnyObject], coder coder: NSCoder) -> UIViewController?     optional func application(_ application: UIApplication, shouldSaveApplicationState coder: NSCoder) -> Bool     optional func application(_ application: UIApplication, shouldRestoreApplicationState coder: NSCoder) -> Bool     optional func application(_ application: UIApplication, willEncodeRestorableStateWithCoder coder: NSCoder)     optional func application(_ application: UIApplication, didDecodeRestorableStateWithCoder coder: NSCoder)     optional func application(_ application: UIApplication, willContinueUserActivityWithType userActivityType: String) -> Bool     optional func application(_ application: UIApplication, continueUserActivity userActivity: NSUserActivity, restorationHandler restorationHandler: ([AnyObject]!) -> Void) -> Bool     optional func application(_ application: UIApplication, didFailToContinueUserActivityWithType userActivityType: String, error error: NSError)     optional func application(_ application: UIApplication, didUpdateUserActivity userActivity: NSUserActivity) } ``` |
| To | ``` protocol UIApplicationDelegate : NSObjectProtocol {     optional func applicationDidFinishLaunching(_ application: UIApplication)     optional func application(_ application: UIApplication, willFinishLaunchingWithOptions launchOptions: [NSObject : AnyObject]?) -> Bool     optional func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject : AnyObject]?) -> Bool     optional func applicationDidBecomeActive(_ application: UIApplication)     optional func applicationWillResignActive(_ application: UIApplication)     optional func application(_ application: UIApplication, handleOpenURL url: NSURL) -> Bool     optional func application(_ application: UIApplication, openURL url: NSURL, sourceApplication sourceApplication: String?, annotation annotation: AnyObject) -> Bool     optional func application(_ app: UIApplication, openURL url: NSURL, options options: [String : AnyObject]) -> Bool     optional func applicationDidReceiveMemoryWarning(_ application: UIApplication)     optional func applicationWillTerminate(_ application: UIApplication)     optional func applicationSignificantTimeChange(_ application: UIApplication)     optional func application(_ application: UIApplication, willChangeStatusBarOrientation newStatusBarOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     optional func application(_ application: UIApplication, didChangeStatusBarOrientation oldStatusBarOrientation: UIInterfaceOrientation)     optional func application(_ application: UIApplication, willChangeStatusBarFrame newStatusBarFrame: CGRect)     optional func application(_ application: UIApplication, didChangeStatusBarFrame oldStatusBarFrame: CGRect)     optional func application(_ application: UIApplication, didRegisterUserNotificationSettings notificationSettings: UIUserNotificationSettings)     optional func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: NSData)     optional func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: NSError)     optional func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [NSObject : AnyObject])     optional func application(_ application: UIApplication, didReceiveLocalNotification notification: UILocalNotification)     optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, forLocalNotification notification: UILocalNotification, completionHandler completionHandler: () -> Void)     optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, forRemoteNotification userInfo: [NSObject : AnyObject], withResponseInfo responseInfo: [NSObject : AnyObject], completionHandler completionHandler: () -> Void)     optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, forRemoteNotification userInfo: [NSObject : AnyObject], completionHandler completionHandler: () -> Void)     optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, forLocalNotification notification: UILocalNotification, withResponseInfo responseInfo: [NSObject : AnyObject], completionHandler completionHandler: () -> Void)     optional func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [NSObject : AnyObject], fetchCompletionHandler completionHandler: (UIBackgroundFetchResult) -> Void)     optional func application(_ application: UIApplication, performFetchWithCompletionHandler completionHandler: (UIBackgroundFetchResult) -> Void)     optional func application(_ application: UIApplication, performActionForShortcutItem shortcutItem: UIApplicationShortcutItem, completionHandler completionHandler: (Bool) -> Void)     optional func application(_ application: UIApplication, handleEventsForBackgroundURLSession identifier: String, completionHandler completionHandler: () -> Void)     optional func application(_ application: UIApplication, handleWatchKitExtensionRequest userInfo: [NSObject : AnyObject]?, reply reply: ([NSObject : AnyObject]?) -> Void)     optional func applicationShouldRequestHealthAuthorization(_ application: UIApplication)     optional func applicationDidEnterBackground(_ application: UIApplication)     optional func applicationWillEnterForeground(_ application: UIApplication)     optional func applicationProtectedDataWillBecomeUnavailable(_ application: UIApplication)     optional func applicationProtectedDataDidBecomeAvailable(_ application: UIApplication)     optional var window: UIWindow? { get set }     optional func application(_ application: UIApplication, supportedInterfaceOrientationsForWindow window: UIWindow?) -> UIInterfaceOrientationMask     optional func application(_ application: UIApplication, shouldAllowExtensionPointIdentifier extensionPointIdentifier: String) -> Bool     optional func application(_ application: UIApplication, viewControllerWithRestorationIdentifierPath identifierComponents: [AnyObject], coder coder: NSCoder) -> UIViewController?     optional func application(_ application: UIApplication, shouldSaveApplicationState coder: NSCoder) -> Bool     optional func application(_ application: UIApplication, shouldRestoreApplicationState coder: NSCoder) -> Bool     optional func application(_ application: UIApplication, willEncodeRestorableStateWithCoder coder: NSCoder)     optional func application(_ application: UIApplication, didDecodeRestorableStateWithCoder coder: NSCoder)     optional func application(_ application: UIApplication, willContinueUserActivityWithType userActivityType: String) -> Bool     optional func application(_ application: UIApplication, continueUserActivity userActivity: NSUserActivity, restorationHandler restorationHandler: ([AnyObject]?) -> Void) -> Bool     optional func application(_ application: UIApplication, didFailToContinueUserActivityWithType userActivityType: String, error error: NSError)     optional func application(_ application: UIApplication, didUpdateUserActivity userActivity: NSUserActivity) } ``` |

Modified [UIApplicationDelegate.application(_: UIApplication, continueUserActivity: NSUserActivity, restorationHandler: ([AnyObject]?) -> Void) -> Bool](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application)

|  | Declaration |
| --- | --- |
| From | ``` optional func application(_ application: UIApplication, continueUserActivity userActivity: NSUserActivity, restorationHandler restorationHandler: ([AnyObject]!) -> Void) -> Bool ``` |
| To | ``` optional func application(_ application: UIApplication, continueUserActivity userActivity: NSUserActivity, restorationHandler restorationHandler: ([AnyObject]?) -> Void) -> Bool ``` |

Modified [UIApplicationDelegate.application(_: UIApplication, didChangeStatusBarFrame: CGRect)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622947-application)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIApplicationDelegate.application(_: UIApplication, didChangeStatusBarOrientation: UIInterfaceOrientation)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622943-application)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIApplicationDelegate.application(_: UIApplication, handleOpenURL: NSURL) -> Bool](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622964-application)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIApplicationDelegate.application(_: UIApplication, handleWatchKitExtensionRequest: [NSObject : AnyObject]?, reply: ([NSObject : AnyObject]?) -> Void)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623041-application)

|  | Declaration |
| --- | --- |
| From | ``` optional func application(_ application: UIApplication, handleWatchKitExtensionRequest userInfo: [NSObject : AnyObject]?, reply reply: (([NSObject : AnyObject]!) -> Void)!) ``` |
| To | ``` optional func application(_ application: UIApplication, handleWatchKitExtensionRequest userInfo: [NSObject : AnyObject]?, reply reply: ([NSObject : AnyObject]?) -> Void) ``` |

Modified [UIApplicationDelegate.application(_: UIApplication, openURL: NSURL, sourceApplication: String?, annotation: AnyObject) -> Bool](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623073-application)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` optional func application(_ application: UIApplication, openURL url: NSURL, sourceApplication sourceApplication: String?, annotation annotation: AnyObject?) -> Bool ``` | -- |
| To | ``` optional func application(_ application: UIApplication, openURL url: NSURL, sourceApplication sourceApplication: String?, annotation annotation: AnyObject) -> Bool ``` | iOS 9.0 |

Modified [UIApplicationDelegate.application(_: UIApplication, supportedInterfaceOrientationsForWindow: UIWindow?) -> UIInterfaceOrientationMask](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623107-application)

|  | Declaration |
| --- | --- |
| From | ``` optional func application(_ application: UIApplication, supportedInterfaceOrientationsForWindow window: UIWindow?) -> Int ``` |
| To | ``` optional func application(_ application: UIApplication, supportedInterfaceOrientationsForWindow window: UIWindow?) -> UIInterfaceOrientationMask ``` |

Modified [UIApplicationDelegate.application(_: UIApplication, willChangeStatusBarFrame: CGRect)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623020-application)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIApplicationDelegate.application(_: UIApplication, willChangeStatusBarOrientation: UIInterfaceOrientation, duration: NSTimeInterval)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623054-application)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIApplicationDelegate.applicationDidBecomeActive(_: UIApplication)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622956-applicationdidbecomeactive)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIApplicationDelegate.applicationDidFinishLaunching(_: UIApplication)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIApplicationDelegate.applicationDidReceiveMemoryWarning(_: UIApplication)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623063-applicationdidreceivememorywarni)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIApplicationDelegate.applicationSignificantTimeChange(_: UIApplication)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622992-applicationsignificanttimechange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIApplicationDelegate.applicationWillResignActive(_: UIApplication)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622950-applicationwillresignactive)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIApplicationDelegate.applicationWillTerminate(_: UIApplication)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623111-applicationwillterminate)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIApplicationState [enum]](https://developer.apple.com/documentation/uikit/uiapplicationstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIAttachmentBehavior](https://developer.apple.com/documentation/uikit/uiattachmentbehavior)

|  | Declaration |
| --- | --- |
| From | ``` class UIAttachmentBehavior : UIDynamicBehavior {     convenience init!(item item: UIDynamicItem, attachedToAnchor point: CGPoint)     convenience init!(item item: UIDynamicItem, offsetFromCenter offset: UIOffset, attachedToAnchor point: CGPoint)     convenience init!(item item1: UIDynamicItem, attachedToItem item2: UIDynamicItem)     init!(item item1: UIDynamicItem, offsetFromCenter offset1: UIOffset, attachedToItem item2: UIDynamicItem, offsetFromCenter offset2: UIOffset)     var items: [AnyObject] { get }     var attachedBehaviorType: UIAttachmentBehaviorType { get }     var anchorPoint: CGPoint     var length: CGFloat     var damping: CGFloat     var frequency: CGFloat } ``` |
| To | ``` class UIAttachmentBehavior : UIDynamicBehavior {     convenience init(item item: UIDynamicItem, attachedToAnchor point: CGPoint)     init(item item: UIDynamicItem, offsetFromCenter offset: UIOffset, attachedToAnchor point: CGPoint)     convenience init(item item1: UIDynamicItem, attachedToItem item2: UIDynamicItem)     init(item item1: UIDynamicItem, offsetFromCenter offset1: UIOffset, attachedToItem item2: UIDynamicItem, offsetFromCenter offset2: UIOffset)     class func slidingAttachmentWithItem(_ item1: UIDynamicItem, attachedToItem item2: UIDynamicItem, attachmentAnchor point: CGPoint, axisOfTranslation axis: CGVector) -> Self     class func slidingAttachmentWithItem(_ item: UIDynamicItem, attachmentAnchor point: CGPoint, axisOfTranslation axis: CGVector) -> Self     class func limitAttachmentWithItem(_ item1: UIDynamicItem, offsetFromCenter offset1: UIOffset, attachedToItem item2: UIDynamicItem, offsetFromCenter offset2: UIOffset) -> Self     class func fixedAttachmentWithItem(_ item1: UIDynamicItem, attachedToItem item2: UIDynamicItem, attachmentAnchor point: CGPoint) -> Self     class func pinAttachmentWithItem(_ item1: UIDynamicItem, attachedToItem item2: UIDynamicItem, attachmentAnchor point: CGPoint) -> Self     var items: [UIDynamicItem] { get }     var attachedBehaviorType: UIAttachmentBehaviorType { get }     var anchorPoint: CGPoint     var length: CGFloat     var damping: CGFloat     var frequency: CGFloat     var frictionTorque: CGFloat     var attachmentRange: UIFloatRange } ``` |

Modified [UIAttachmentBehavior.init(item: UIDynamicItem, attachedToAnchor: CGPoint)](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621297-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(item item: UIDynamicItem, attachedToAnchor point: CGPoint) ``` |
| To | ``` convenience init(item item: UIDynamicItem, attachedToAnchor point: CGPoint) ``` |

Modified [UIAttachmentBehavior.init(item: UIDynamicItem, attachedToItem: UIDynamicItem)](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621309-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(item item1: UIDynamicItem, attachedToItem item2: UIDynamicItem) ``` |
| To | ``` convenience init(item item1: UIDynamicItem, attachedToItem item2: UIDynamicItem) ``` |

Modified [UIAttachmentBehavior.init(item: UIDynamicItem, offsetFromCenter: UIOffset, attachedToAnchor: CGPoint)](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621301-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(item item: UIDynamicItem, offsetFromCenter offset: UIOffset, attachedToAnchor point: CGPoint) ``` |
| To | ``` init(item item: UIDynamicItem, offsetFromCenter offset: UIOffset, attachedToAnchor point: CGPoint) ``` |

Modified [UIAttachmentBehavior.init(item: UIDynamicItem, offsetFromCenter: UIOffset, attachedToItem: UIDynamicItem, offsetFromCenter: UIOffset)](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621298-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(item item1: UIDynamicItem, offsetFromCenter offset1: UIOffset, attachedToItem item2: UIDynamicItem, offsetFromCenter offset2: UIOffset) ``` |
| To | ``` init(item item1: UIDynamicItem, offsetFromCenter offset1: UIOffset, attachedToItem item2: UIDynamicItem, offsetFromCenter offset2: UIOffset) ``` |

Modified [UIAttachmentBehavior.items](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/1621311-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject] { get } ``` |
| To | ``` var items: [UIDynamicItem] { get } ``` |

Modified [UIAttachmentBehaviorType [enum]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/attachmenttype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIBackgroundFetchResult [enum]](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [UIBackgroundRefreshStatus [enum]](https://developer.apple.com/documentation/uikit/uibackgroundrefreshstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem)

|  | Declaration |
| --- | --- |
| From | ``` class UIBarButtonItem : UIBarItem, NSCoding {     init(image image: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     init(image image: UIImage?, landscapeImagePhone landscapeImagePhone: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     init(title title: String?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     init(barButtonSystemItem systemItem: UIBarButtonSystemItem, target target: AnyObject?, action action: Selector)     init(customView customView: UIView)     var style: UIBarButtonItemStyle     var width: CGFloat     var possibleTitles: Set<NSObject>?     var customView: UIView?     var action: Selector     unowned(unsafe) var target: AnyObject?     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, style style: UIBarButtonItemStyle, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, style style: UIBarButtonItemStyle, barMetrics barMetrics: UIBarMetrics) -> UIImage?     var tintColor: UIColor!     func setBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func backgroundVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat     func setTitlePositionAdjustment(_ adjustment: UIOffset, forBarMetrics barMetrics: UIBarMetrics)     func titlePositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> UIOffset     func setBackButtonBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backButtonBackgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackButtonTitlePositionAdjustment(_ adjustment: UIOffset, forBarMetrics barMetrics: UIBarMetrics)     func backButtonTitlePositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> UIOffset     func setBackButtonBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func backButtonBackgroundVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat } ``` |
| To | ``` class UIBarButtonItem : UIBarItem {     init()     init?(coder aDecoder: NSCoder)     convenience init(image image: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     convenience init(image image: UIImage?, landscapeImagePhone landscapeImagePhone: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     convenience init(title title: String?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     convenience init(barButtonSystemItem systemItem: UIBarButtonSystemItem, target target: AnyObject?, action action: Selector)     convenience init(customView customView: UIView)     var style: UIBarButtonItemStyle     var width: CGFloat     var possibleTitles: Set<String>?     var customView: UIView?     var action: Selector     weak var target: AnyObject?     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, style style: UIBarButtonItemStyle, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, style style: UIBarButtonItemStyle, barMetrics barMetrics: UIBarMetrics) -> UIImage?     var tintColor: UIColor?     func setBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func backgroundVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat     func setTitlePositionAdjustment(_ adjustment: UIOffset, forBarMetrics barMetrics: UIBarMetrics)     func titlePositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> UIOffset     func setBackButtonBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backButtonBackgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackButtonTitlePositionAdjustment(_ adjustment: UIOffset, forBarMetrics barMetrics: UIBarMetrics)     func backButtonTitlePositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> UIOffset     func setBackButtonBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func backButtonBackgroundVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat } extension UIBarButtonItem {     weak var buttonGroup: UIBarButtonItemGroup? { get } } ``` |

Modified [UIBarButtonItem.init(barButtonSystemItem: UIBarButtonSystemItem, target: AnyObject?, action: Selector)](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617153-init)

|  | Declaration |
| --- | --- |
| From | ``` init(barButtonSystemItem systemItem: UIBarButtonSystemItem, target target: AnyObject?, action action: Selector) ``` |
| To | ``` convenience init(barButtonSystemItem systemItem: UIBarButtonSystemItem, target target: AnyObject?, action action: Selector) ``` |

Modified [UIBarButtonItem.init(customView: UIView)](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617151-initwithcustomview)

|  | Declaration |
| --- | --- |
| From | ``` init(customView customView: UIView) ``` |
| To | ``` convenience init(customView customView: UIView) ``` |

Modified [UIBarButtonItem.init(image: UIImage?, landscapeImagePhone: UIImage?, style: UIBarButtonItemStyle, target: AnyObject?, action: Selector)](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617118-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` init(image image: UIImage?, landscapeImagePhone landscapeImagePhone: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector) ``` |
| To | ``` convenience init(image image: UIImage?, landscapeImagePhone landscapeImagePhone: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector) ``` |

Modified [UIBarButtonItem.init(image: UIImage?, style: UIBarButtonItemStyle, target: AnyObject?, action: Selector)](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617163-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` init(image image: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector) ``` |
| To | ``` convenience init(image image: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector) ``` |

Modified [UIBarButtonItem.init(title: String?, style: UIBarButtonItemStyle, target: AnyObject?, action: Selector)](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617148-initwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` init(title title: String?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector) ``` |
| To | ``` convenience init(title title: String?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector) ``` |

Modified [UIBarButtonItem.possibleTitles](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617132-possibletitles)

|  | Declaration |
| --- | --- |
| From | ``` var possibleTitles: Set<NSObject>? ``` |
| To | ``` var possibleTitles: Set<String>? ``` |

Modified [UIBarButtonItem.target](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617154-target)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var target: AnyObject? ``` |
| To | ``` weak var target: AnyObject? ``` |

Modified [UIBarButtonItem.tintColor](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617135-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` var tintColor: UIColor! ``` |
| To | ``` var tintColor: UIColor? ``` |

Modified [UIBarButtonItemStyle [enum]](https://developer.apple.com/documentation/uikit/uibarbuttonitemstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIBarButtonSystemItem [enum]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/systemitem)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIBarButtonSystemItem.PageCurl](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitempagecurl)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [UIBarButtonSystemItem.Redo](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemredo)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified [UIBarButtonSystemItem.Undo](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemundo)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified [UIBarItem](https://developer.apple.com/documentation/uikit/uibaritem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIBarItem : NSObject, UIAppearance, NSObjectProtocol {     var enabled: Bool     var title: String?     var image: UIImage?     var landscapeImagePhone: UIImage?     var imageInsets: UIEdgeInsets     var landscapeImagePhoneInsets: UIEdgeInsets     var tag: Int     func setTitleTextAttributes(_ attributes: [NSObject : AnyObject]!, forState state: UIControlState)     func titleTextAttributesForState(_ state: UIControlState) -> [NSObject : AnyObject]! } extension UIBarItem : UIAccessibilityIdentification, NSObjectProtocol { } ``` | AnyObject, NSObjectProtocol, UIAccessibilityIdentification, UIAppearance |
| To | ``` class UIBarItem : NSObject, NSCoding, UIAppearance {     init()     init?(coder aDecoder: NSCoder)     var enabled: Bool     var title: String?     var image: UIImage?     var landscapeImagePhone: UIImage?     var imageInsets: UIEdgeInsets     var landscapeImagePhoneInsets: UIEdgeInsets     var tag: Int     func setTitleTextAttributes(_ attributes: [String : AnyObject]?, forState state: UIControlState)     func titleTextAttributesForState(_ state: UIControlState) -> [String : AnyObject]? } extension UIBarItem : UIAccessibilityIdentification { } ``` | AnyObject, NSCoding, NSObjectProtocol, UIAccessibilityIdentification, UIAppearance |

Modified [UIBarItem.setTitleTextAttributes(_: [String : AnyObject]?, forState: UIControlState)](https://developer.apple.com/documentation/uikit/uibaritem/1616414-settitletextattributes)

|  | Declaration |
| --- | --- |
| From | ``` func setTitleTextAttributes(_ attributes: [NSObject : AnyObject]!, forState state: UIControlState) ``` |
| To | ``` func setTitleTextAttributes(_ attributes: [String : AnyObject]?, forState state: UIControlState) ``` |

Modified [UIBarItem.titleTextAttributesForState(_: UIControlState) -> [String : AnyObject]?](https://developer.apple.com/documentation/uikit/uibaritem/1616422-titletextattributes)

|  | Declaration |
| --- | --- |
| From | ``` func titleTextAttributesForState(_ state: UIControlState) -> [NSObject : AnyObject]! ``` |
| To | ``` func titleTextAttributesForState(_ state: UIControlState) -> [String : AnyObject]? ``` |

Modified [UIBarMetrics [enum]](https://developer.apple.com/documentation/uikit/uibarmetrics)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum UIBarMetrics : Int {     case Default     case Compact     case DefaultPrompt     case CompactPrompt } ``` | -- |
| To | ``` enum UIBarMetrics : Int {     case Default     case Compact     case DefaultPrompt     case CompactPrompt     static var LandscapePhone: UIBarMetrics { get }     static var LandscapePhonePrompt: UIBarMetrics { get } } ``` | Int |

Modified [UIBarPosition [enum]](https://developer.apple.com/documentation/uikit/uibarposition)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIBarPositioning.barPosition](https://developer.apple.com/documentation/uikit/uibarpositioning/1624857-barposition)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [UIBarPositioningDelegate.positionForBar(_: UIBarPositioning) -> UIBarPosition](https://developer.apple.com/documentation/uikit/uibarpositioningdelegate/1624872-positionforbar)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [UIBarStyle [enum]](https://developer.apple.com/documentation/uikit/uibarstyle)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum UIBarStyle : Int {     case Default     case Black     case BlackTranslucent } ``` | -- |
| To | ``` enum UIBarStyle : Int {     case Default     case Black     static var BlackOpaque: UIBarStyle { get }     case BlackTranslucent } ``` | Int |

Modified [UIBaselineAdjustment [enum]](https://developer.apple.com/documentation/uikit/uibaselineadjustment)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIBezierPath](https://developer.apple.com/documentation/uikit/uibezierpath)

|  | Declaration |
| --- | --- |
| From | ``` class UIBezierPath : NSObject, NSCopying, NSCoding {     init!() -> UIBezierPath     class func bezierPath() -> UIBezierPath!     init(rect rect: CGRect) -> UIBezierPath     class func bezierPathWithRect(_ rect: CGRect) -> UIBezierPath     init(ovalInRect rect: CGRect) -> UIBezierPath     class func bezierPathWithOvalInRect(_ rect: CGRect) -> UIBezierPath     init(roundedRect rect: CGRect, cornerRadius cornerRadius: CGFloat) -> UIBezierPath     class func bezierPathWithRoundedRect(_ rect: CGRect, cornerRadius cornerRadius: CGFloat) -> UIBezierPath     init(roundedRect rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii cornerRadii: CGSize) -> UIBezierPath     class func bezierPathWithRoundedRect(_ rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii cornerRadii: CGSize) -> UIBezierPath     init(arcCenter center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool) -> UIBezierPath     class func bezierPathWithArcCenter(_ center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool) -> UIBezierPath     init(CGPath CGPath: CGPath!) -> UIBezierPath     class func bezierPathWithCGPath(_ CGPath: CGPath!) -> UIBezierPath     var CGPath: CGPath     func moveToPoint(_ point: CGPoint)     func addLineToPoint(_ point: CGPoint)     func addCurveToPoint(_ endPoint: CGPoint, controlPoint1 controlPoint1: CGPoint, controlPoint2 controlPoint2: CGPoint)     func addQuadCurveToPoint(_ endPoint: CGPoint, controlPoint controlPoint: CGPoint)     func addArcWithCenter(_ center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     func closePath()     func removeAllPoints()     func appendPath(_ bezierPath: UIBezierPath)     func bezierPathByReversingPath() -> UIBezierPath     func applyTransform(_ transform: CGAffineTransform)     var empty: Bool { get }     var bounds: CGRect { get }     var currentPoint: CGPoint { get }     func containsPoint(_ point: CGPoint) -> Bool     var lineWidth: CGFloat     var lineCapStyle: CGLineCap     var lineJoinStyle: CGLineJoin     var miterLimit: CGFloat     var flatness: CGFloat     var usesEvenOddFillRule: Bool     func setLineDash(_ pattern: UnsafePointer<CGFloat>, count count: Int, phase phase: CGFloat)     func getLineDash(_ pattern: UnsafeMutablePointer<CGFloat>, count count: UnsafeMutablePointer<Int>, phase phase: UnsafeMutablePointer<CGFloat>)     func fill()     func stroke()     func fillWithBlendMode(_ blendMode: CGBlendMode, alpha alpha: CGFloat)     func strokeWithBlendMode(_ blendMode: CGBlendMode, alpha alpha: CGFloat)     func addClip() } ``` |
| To | ``` class UIBezierPath : NSObject, NSCopying, NSCoding {     convenience init()     class func bezierPath() -> Self     convenience init(rect rect: CGRect)     class func bezierPathWithRect(_ rect: CGRect) -> Self     convenience init(ovalInRect rect: CGRect)     class func bezierPathWithOvalInRect(_ rect: CGRect) -> Self     convenience init(roundedRect rect: CGRect, cornerRadius cornerRadius: CGFloat)     class func bezierPathWithRoundedRect(_ rect: CGRect, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(roundedRect rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii cornerRadii: CGSize)     class func bezierPathWithRoundedRect(_ rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii cornerRadii: CGSize) -> Self     convenience init(arcCenter center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     class func bezierPathWithArcCenter(_ center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool) -> Self     convenience init(CGPath CGPath: CGPath)     class func bezierPathWithCGPath(_ CGPath: CGPath) -> Self     init()     init?(coder aDecoder: NSCoder)     var CGPath: CGPath     func moveToPoint(_ point: CGPoint)     func addLineToPoint(_ point: CGPoint)     func addCurveToPoint(_ endPoint: CGPoint, controlPoint1 controlPoint1: CGPoint, controlPoint2 controlPoint2: CGPoint)     func addQuadCurveToPoint(_ endPoint: CGPoint, controlPoint controlPoint: CGPoint)     func addArcWithCenter(_ center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     func closePath()     func removeAllPoints()     func appendPath(_ bezierPath: UIBezierPath)     func bezierPathByReversingPath() -> UIBezierPath     func applyTransform(_ transform: CGAffineTransform)     var empty: Bool { get }     var bounds: CGRect { get }     var currentPoint: CGPoint { get }     func containsPoint(_ point: CGPoint) -> Bool     var lineWidth: CGFloat     var lineCapStyle: CGLineCap     var lineJoinStyle: CGLineJoin     var miterLimit: CGFloat     var flatness: CGFloat     var usesEvenOddFillRule: Bool     func setLineDash(_ pattern: UnsafePointer<CGFloat>, count count: Int, phase phase: CGFloat)     func getLineDash(_ pattern: UnsafeMutablePointer<CGFloat>, count count: UnsafeMutablePointer<Int>, phase phase: UnsafeMutablePointer<CGFloat>)     func fill()     func stroke()     func fillWithBlendMode(_ blendMode: CGBlendMode, alpha alpha: CGFloat)     func strokeWithBlendMode(_ blendMode: CGBlendMode, alpha alpha: CGFloat)     func addClip() } ``` |

Modified [UIBezierPath.init(arcCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](https://developer.apple.com/documentation/uikit/uibezierpath/1624358-init)

|  | Declaration |
| --- | --- |
| From | ``` init(arcCenter center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool) -> UIBezierPath ``` |
| To | ``` convenience init(arcCenter center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool) ``` |

Modified [UIBezierPath.init(CGPath: CGPath)](https://developer.apple.com/documentation/uikit/uibezierpath/1624362-bezierpathwithcgpath)

|  | Declaration |
| --- | --- |
| From | ``` init(CGPath CGPath: CGPath!) -> UIBezierPath ``` |
| To | ``` convenience init(CGPath CGPath: CGPath) ``` |

Modified [UIBezierPath.init(ovalInRect: CGRect)](https://developer.apple.com/documentation/uikit/uibezierpath/1624379-bezierpathwithovalinrect)

|  | Declaration |
| --- | --- |
| From | ``` init(ovalInRect rect: CGRect) -> UIBezierPath ``` |
| To | ``` convenience init(ovalInRect rect: CGRect) ``` |

Modified [UIBezierPath.init(rect: CGRect)](https://developer.apple.com/documentation/uikit/uibezierpath/1624359-bezierpathwithrect)

|  | Declaration |
| --- | --- |
| From | ``` init(rect rect: CGRect) -> UIBezierPath ``` |
| To | ``` convenience init(rect rect: CGRect) ``` |

Modified [UIBezierPath.init(roundedRect: CGRect, byRoundingCorners: UIRectCorner, cornerRadii: CGSize)](https://developer.apple.com/documentation/uikit/uibezierpath/1624368-init)

|  | Declaration |
| --- | --- |
| From | ``` init(roundedRect rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii cornerRadii: CGSize) -> UIBezierPath ``` |
| To | ``` convenience init(roundedRect rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii cornerRadii: CGSize) ``` |

Modified [UIBezierPath.init(roundedRect: CGRect, cornerRadius: CGFloat)](https://developer.apple.com/documentation/uikit/uibezierpath/1624356-bezierpathwithroundedrect)

|  | Declaration |
| --- | --- |
| From | ``` init(roundedRect rect: CGRect, cornerRadius cornerRadius: CGFloat) -> UIBezierPath ``` |
| To | ``` convenience init(roundedRect rect: CGRect, cornerRadius cornerRadius: CGFloat) ``` |

Modified [UIBlurEffect](https://developer.apple.com/documentation/uikit/uiblureffect)

|  | Declaration |
| --- | --- |
| From | ``` class UIBlurEffect : UIVisualEffect {     init(style style: UIBlurEffectStyle) -> UIBlurEffect     class func effectWithStyle(_ style: UIBlurEffectStyle) -> UIBlurEffect } ``` |
| To | ``` class UIBlurEffect : UIVisualEffect {      init(style style: UIBlurEffectStyle)     class func effectWithStyle(_ style: UIBlurEffectStyle) -> UIBlurEffect } ``` |

Modified [UIBlurEffect.init(style: UIBlurEffectStyle)](https://developer.apple.com/documentation/uikit/uiblureffect/1615060-effectwithstyle)

|  | Declaration |
| --- | --- |
| From | ``` init(style style: UIBlurEffectStyle) -> UIBlurEffect ``` |
| To | ``` init(style style: UIBlurEffectStyle) ``` |

Modified [UIBlurEffectStyle [enum]](https://developer.apple.com/documentation/uikit/uiblureffect/style)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIButton](https://developer.apple.com/documentation/uikit/uibutton)

|  | Declaration |
| --- | --- |
| From | ``` class UIButton : UIControl, NSCoding {     class func buttonWithType(_ buttonType: UIButtonType) -> AnyObject     var contentEdgeInsets: UIEdgeInsets     var titleEdgeInsets: UIEdgeInsets     var reversesTitleShadowWhenHighlighted: Bool     var imageEdgeInsets: UIEdgeInsets     var adjustsImageWhenHighlighted: Bool     var adjustsImageWhenDisabled: Bool     var showsTouchWhenHighlighted: Bool     var tintColor: UIColor?     var buttonType: UIButtonType { get }     func setTitle(_ title: String?, forState state: UIControlState)     func setTitleColor(_ color: UIColor?, forState state: UIControlState)     func setTitleShadowColor(_ color: UIColor?, forState state: UIControlState)     func setImage(_ image: UIImage?, forState state: UIControlState)     func setBackgroundImage(_ image: UIImage?, forState state: UIControlState)     func setAttributedTitle(_ title: NSAttributedString!, forState state: UIControlState)     func titleForState(_ state: UIControlState) -> String?     func titleColorForState(_ state: UIControlState) -> UIColor?     func titleShadowColorForState(_ state: UIControlState) -> UIColor?     func imageForState(_ state: UIControlState) -> UIImage?     func backgroundImageForState(_ state: UIControlState) -> UIImage?     func attributedTitleForState(_ state: UIControlState) -> NSAttributedString?     var currentTitle: String? { get }     var currentTitleColor: UIColor! { get }     var currentTitleShadowColor: UIColor? { get }     var currentImage: UIImage? { get }     var currentBackgroundImage: UIImage? { get }     var currentAttributedTitle: NSAttributedString? { get }     var titleLabel: UILabel? { get }     var imageView: UIImageView? { get }     func backgroundRectForBounds(_ bounds: CGRect) -> CGRect     func contentRectForBounds(_ bounds: CGRect) -> CGRect     func titleRectForContentRect(_ contentRect: CGRect) -> CGRect     func imageRectForContentRect(_ contentRect: CGRect) -> CGRect } extension UIButton {     var font: UIFont!     var lineBreakMode: NSLineBreakMode     var titleShadowOffset: CGSize } ``` |
| To | ``` class UIButton : UIControl {     convenience init(type buttonType: UIButtonType)     class func buttonWithType(_ buttonType: UIButtonType) -> Self     var contentEdgeInsets: UIEdgeInsets     var titleEdgeInsets: UIEdgeInsets     var reversesTitleShadowWhenHighlighted: Bool     var imageEdgeInsets: UIEdgeInsets     var adjustsImageWhenHighlighted: Bool     var adjustsImageWhenDisabled: Bool     var showsTouchWhenHighlighted: Bool     var tintColor: UIColor!     var buttonType: UIButtonType { get }     func setTitle(_ title: String?, forState state: UIControlState)     func setTitleColor(_ color: UIColor?, forState state: UIControlState)     func setTitleShadowColor(_ color: UIColor?, forState state: UIControlState)     func setImage(_ image: UIImage?, forState state: UIControlState)     func setBackgroundImage(_ image: UIImage?, forState state: UIControlState)     func setAttributedTitle(_ title: NSAttributedString?, forState state: UIControlState)     func titleForState(_ state: UIControlState) -> String?     func titleColorForState(_ state: UIControlState) -> UIColor?     func titleShadowColorForState(_ state: UIControlState) -> UIColor?     func imageForState(_ state: UIControlState) -> UIImage?     func backgroundImageForState(_ state: UIControlState) -> UIImage?     func attributedTitleForState(_ state: UIControlState) -> NSAttributedString?     var currentTitle: String? { get }     var currentTitleColor: UIColor { get }     var currentTitleShadowColor: UIColor? { get }     var currentImage: UIImage? { get }     var currentBackgroundImage: UIImage? { get }     var currentAttributedTitle: NSAttributedString? { get }     var titleLabel: UILabel? { get }     var imageView: UIImageView? { get }     func backgroundRectForBounds(_ bounds: CGRect) -> CGRect     func contentRectForBounds(_ bounds: CGRect) -> CGRect     func titleRectForContentRect(_ contentRect: CGRect) -> CGRect     func imageRectForContentRect(_ contentRect: CGRect) -> CGRect } extension UIButton {     var font: UIFont     var lineBreakMode: NSLineBreakMode     var titleShadowOffset: CGSize } ``` |

Modified [UIButton.currentTitleColor](https://developer.apple.com/documentation/uikit/uibutton/1624006-currenttitlecolor)

|  | Declaration |
| --- | --- |
| From | ``` var currentTitleColor: UIColor! { get } ``` |
| To | ``` var currentTitleColor: UIColor { get } ``` |

Modified [UIButton.init(type: UIButtonType)](https://developer.apple.com/documentation/uikit/uibutton/1624028-init)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | buttonWithType(_:) | ``` class func buttonWithType(_ buttonType: UIButtonType) -> AnyObject ``` | iOS 8.0 |
| To | init(type:) | ``` convenience init(type buttonType: UIButtonType) ``` | iOS 9.0 |

Modified [UIButton.setAttributedTitle(_: NSAttributedString?, forState: UIControlState)](https://developer.apple.com/documentation/uikit/uibutton/1624012-setattributedtitle)

|  | Declaration |
| --- | --- |
| From | ``` func setAttributedTitle(_ title: NSAttributedString!, forState state: UIControlState) ``` |
| To | ``` func setAttributedTitle(_ title: NSAttributedString?, forState state: UIControlState) ``` |

Modified [UIButton.tintColor](https://developer.apple.com/documentation/uikit/uibutton/1624025-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` var tintColor: UIColor? ``` |
| To | ``` var tintColor: UIColor! ``` |

Modified [UIButtonType [enum]](https://developer.apple.com/documentation/uikit/uibutton/buttontype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum UIButtonType : Int {     case Custom     case System     case DetailDisclosure     case InfoLight     case InfoDark     case ContactAdd } ``` | -- |
| To | ``` enum UIButtonType : Int {     case Custom     case System     case DetailDisclosure     case InfoLight     case InfoDark     case ContactAdd     static var RoundedRect: UIButtonType { get } } ``` | Int |

Modified [UICollectionElementCategory [enum]](https://developer.apple.com/documentation/uikit/uicollectionview/elementcategory)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [UICollectionReusableView](https://developer.apple.com/documentation/uikit/uicollectionreusableview)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionReusableView : UIView {     var reuseIdentifier: String { get }     func prepareForReuse()     func applyLayoutAttributes(_ layoutAttributes: UICollectionViewLayoutAttributes!)     func willTransitionFromLayout(_ oldLayout: UICollectionViewLayout, toLayout newLayout: UICollectionViewLayout)     func didTransitionFromLayout(_ oldLayout: UICollectionViewLayout, toLayout newLayout: UICollectionViewLayout)     func preferredLayoutAttributesFittingAttributes(_ layoutAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes! } ``` |
| To | ``` class UICollectionReusableView : UIView {     var reuseIdentifier: String? { get }     func prepareForReuse()     func applyLayoutAttributes(_ layoutAttributes: UICollectionViewLayoutAttributes)     func willTransitionFromLayout(_ oldLayout: UICollectionViewLayout, toLayout newLayout: UICollectionViewLayout)     func didTransitionFromLayout(_ oldLayout: UICollectionViewLayout, toLayout newLayout: UICollectionViewLayout)     func preferredLayoutAttributesFittingAttributes(_ layoutAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes } ``` |

Modified [UICollectionReusableView.applyLayoutAttributes(_: UICollectionViewLayoutAttributes)](https://developer.apple.com/documentation/uikit/uicollectionreusableview/1620139-apply)

|  | Declaration |
| --- | --- |
| From | ``` func applyLayoutAttributes(_ layoutAttributes: UICollectionViewLayoutAttributes!) ``` |
| To | ``` func applyLayoutAttributes(_ layoutAttributes: UICollectionViewLayoutAttributes) ``` |

Modified [UICollectionReusableView.preferredLayoutAttributesFittingAttributes(_: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes](https://developer.apple.com/documentation/uikit/uicollectionreusableview/1620132-preferredlayoutattributesfitting)

|  | Declaration |
| --- | --- |
| From | ``` func preferredLayoutAttributesFittingAttributes(_ layoutAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes! ``` |
| To | ``` func preferredLayoutAttributesFittingAttributes(_ layoutAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes ``` |

Modified [UICollectionReusableView.reuseIdentifier](https://developer.apple.com/documentation/uikit/uicollectionreusableview/1620136-reuseidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var reuseIdentifier: String { get } ``` |
| To | ``` var reuseIdentifier: String? { get } ``` |

Modified [UICollectionUpdateAction [enum]](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/action)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionView : UIScrollView {     init(frame frame: CGRect, collectionViewLayout layout: UICollectionViewLayout)     var collectionViewLayout: UICollectionViewLayout     unowned(unsafe) var delegate: UICollectionViewDelegate?     unowned(unsafe) var dataSource: UICollectionViewDataSource?     var backgroundView: UIView?     func registerClass(_ cellClass: AnyClass?, forCellWithReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forCellWithReuseIdentifier identifier: String)     func registerClass(_ viewClass: AnyClass?, forSupplementaryViewOfKind elementKind: String, withReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forSupplementaryViewOfKind kind: String, withReuseIdentifier identifier: String)     func dequeueReusableCellWithReuseIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath!) -> AnyObject     func dequeueReusableSupplementaryViewOfKind(_ elementKind: String, withReuseIdentifier identifier: String, forIndexPath indexPath: NSIndexPath!) -> AnyObject     var allowsSelection: Bool     var allowsMultipleSelection: Bool     func indexPathsForSelectedItems() -> [AnyObject]     func selectItemAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool, scrollPosition scrollPosition: UICollectionViewScrollPosition)     func deselectItemAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool)     func reloadData()     func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated animated: Bool)     func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated animated: Bool, completion completion: ((Bool) -> Void)!)     func startInteractiveTransitionToCollectionViewLayout(_ layout: UICollectionViewLayout, completion completion: UICollectionViewLayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout     func finishInteractiveTransition()     func cancelInteractiveTransition()     func numberOfSections() -> Int     func numberOfItemsInSection(_ section: Int) -> Int     func layoutAttributesForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func layoutAttributesForSupplementaryElementOfKind(_ kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func indexPathForItemAtPoint(_ point: CGPoint) -> NSIndexPath?     func indexPathForCell(_ cell: UICollectionViewCell) -> NSIndexPath?     func cellForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewCell?     func visibleCells() -> [AnyObject]     func indexPathsForVisibleItems() -> [AnyObject]     func scrollToItemAtIndexPath(_ indexPath: NSIndexPath, atScrollPosition scrollPosition: UICollectionViewScrollPosition, animated animated: Bool)     func insertSections(_ sections: NSIndexSet)     func deleteSections(_ sections: NSIndexSet)     func reloadSections(_ sections: NSIndexSet)     func moveSection(_ section: Int, toSection newSection: Int)     func insertItemsAtIndexPaths(_ indexPaths: [AnyObject])     func deleteItemsAtIndexPaths(_ indexPaths: [AnyObject])     func reloadItemsAtIndexPaths(_ indexPaths: [AnyObject])     func moveItemAtIndexPath(_ indexPath: NSIndexPath, toIndexPath newIndexPath: NSIndexPath)     func performBatchUpdates(_ updates: (() -> Void)?, completion completion: ((Bool) -> Void)?) } ``` |
| To | ``` class UICollectionView : UIScrollView {     init(frame frame: CGRect, collectionViewLayout layout: UICollectionViewLayout)     init?(coder aDecoder: NSCoder)     var collectionViewLayout: UICollectionViewLayout     weak var delegate: UICollectionViewDelegate?     weak var dataSource: UICollectionViewDataSource?     var backgroundView: UIView?     func registerClass(_ cellClass: AnyClass?, forCellWithReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forCellWithReuseIdentifier identifier: String)     func registerClass(_ viewClass: AnyClass?, forSupplementaryViewOfKind elementKind: String, withReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forSupplementaryViewOfKind kind: String, withReuseIdentifier identifier: String)     func dequeueReusableCellWithReuseIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath) -> UICollectionViewCell     func dequeueReusableSupplementaryViewOfKind(_ elementKind: String, withReuseIdentifier identifier: String, forIndexPath indexPath: NSIndexPath) -> UICollectionReusableView     var allowsSelection: Bool     var allowsMultipleSelection: Bool     func indexPathsForSelectedItems() -> [NSIndexPath]?     func selectItemAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool, scrollPosition scrollPosition: UICollectionViewScrollPosition)     func deselectItemAtIndexPath(_ indexPath: NSIndexPath, animated animated: Bool)     func reloadData()     func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated animated: Bool)     func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated animated: Bool, completion completion: ((Bool) -> Void)?)     func startInteractiveTransitionToCollectionViewLayout(_ layout: UICollectionViewLayout, completion completion: UICollectionViewLayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout     func finishInteractiveTransition()     func cancelInteractiveTransition()     func numberOfSections() -> Int     func numberOfItemsInSection(_ section: Int) -> Int     func layoutAttributesForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func layoutAttributesForSupplementaryElementOfKind(_ kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func indexPathForItemAtPoint(_ point: CGPoint) -> NSIndexPath?     func indexPathForCell(_ cell: UICollectionViewCell) -> NSIndexPath?     func cellForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewCell?     func visibleCells() -> [UICollectionViewCell]     func indexPathsForVisibleItems() -> [NSIndexPath]     func supplementaryViewForElementKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionReusableView     func visibleSupplementaryViewsOfKind(_ elementKind: String) -> [UICollectionReusableView]     func indexPathsForVisibleSupplementaryElementsOfKind(_ elementKind: String) -> [NSIndexPath]     func scrollToItemAtIndexPath(_ indexPath: NSIndexPath, atScrollPosition scrollPosition: UICollectionViewScrollPosition, animated animated: Bool)     func insertSections(_ sections: NSIndexSet)     func deleteSections(_ sections: NSIndexSet)     func reloadSections(_ sections: NSIndexSet)     func moveSection(_ section: Int, toSection newSection: Int)     func insertItemsAtIndexPaths(_ indexPaths: [NSIndexPath])     func deleteItemsAtIndexPaths(_ indexPaths: [NSIndexPath])     func reloadItemsAtIndexPaths(_ indexPaths: [NSIndexPath])     func moveItemAtIndexPath(_ indexPath: NSIndexPath, toIndexPath newIndexPath: NSIndexPath)     func performBatchUpdates(_ updates: (() -> Void)?, completion completion: ((Bool) -> Void)?)     func beginInteractiveMovementForItemAtIndexPath(_ indexPath: NSIndexPath) -> Bool     func updateInteractiveMovementTargetPosition(_ targetPosition: CGPoint)     func endInteractiveMovement()     func cancelInteractiveMovement() } ``` |

Modified [UICollectionView.dataSource](https://developer.apple.com/documentation/uikit/uicollectionview/1618091-datasource)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var dataSource: UICollectionViewDataSource? ``` |
| To | ``` weak var dataSource: UICollectionViewDataSource? ``` |

Modified [UICollectionView.delegate](https://developer.apple.com/documentation/uikit/uicollectionview/1618033-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UICollectionViewDelegate? ``` |
| To | ``` weak var delegate: UICollectionViewDelegate? ``` |

Modified [UICollectionView.deleteItemsAtIndexPaths(_: [NSIndexPath])](https://developer.apple.com/documentation/uikit/uicollectionview/1618060-deleteitems)

|  | Declaration |
| --- | --- |
| From | ``` func deleteItemsAtIndexPaths(_ indexPaths: [AnyObject]) ``` |
| To | ``` func deleteItemsAtIndexPaths(_ indexPaths: [NSIndexPath]) ``` |

Modified [UICollectionView.dequeueReusableCellWithReuseIdentifier(_: String, forIndexPath: NSIndexPath) -> UICollectionViewCell](https://developer.apple.com/documentation/uikit/uicollectionview/1618063-dequeuereusablecell)

|  | Declaration |
| --- | --- |
| From | ``` func dequeueReusableCellWithReuseIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath!) -> AnyObject ``` |
| To | ``` func dequeueReusableCellWithReuseIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath) -> UICollectionViewCell ``` |

Modified [UICollectionView.dequeueReusableSupplementaryViewOfKind(_: String, withReuseIdentifier: String, forIndexPath: NSIndexPath) -> UICollectionReusableView](https://developer.apple.com/documentation/uikit/uicollectionview/1618068-dequeuereusablesupplementaryview)

|  | Declaration |
| --- | --- |
| From | ``` func dequeueReusableSupplementaryViewOfKind(_ elementKind: String, withReuseIdentifier identifier: String, forIndexPath indexPath: NSIndexPath!) -> AnyObject ``` |
| To | ``` func dequeueReusableSupplementaryViewOfKind(_ elementKind: String, withReuseIdentifier identifier: String, forIndexPath indexPath: NSIndexPath) -> UICollectionReusableView ``` |

Modified [UICollectionView.deselectItemAtIndexPath(_: NSIndexPath, animated: Bool)](https://developer.apple.com/documentation/uikit/uicollectionview/1618040-deselectitem)

|  | Declaration |
| --- | --- |
| From | ``` func deselectItemAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool) ``` |
| To | ``` func deselectItemAtIndexPath(_ indexPath: NSIndexPath, animated animated: Bool) ``` |

Modified [UICollectionView.indexPathsForSelectedItems() -> [NSIndexPath]?](https://developer.apple.com/documentation/uikit/uicollectionview/1618099-indexpathsforselecteditems)

|  | Declaration |
| --- | --- |
| From | ``` func indexPathsForSelectedItems() -> [AnyObject] ``` |
| To | ``` func indexPathsForSelectedItems() -> [NSIndexPath]? ``` |

Modified [UICollectionView.indexPathsForVisibleItems() -> [NSIndexPath]](https://developer.apple.com/documentation/uikit/uicollectionview/1618020-indexpathsforvisibleitems)

|  | Declaration |
| --- | --- |
| From | ``` func indexPathsForVisibleItems() -> [AnyObject] ``` |
| To | ``` func indexPathsForVisibleItems() -> [NSIndexPath] ``` |

Modified [UICollectionView.insertItemsAtIndexPaths(_: [NSIndexPath])](https://developer.apple.com/documentation/uikit/uicollectionview/1618097-insertitemsatindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` func insertItemsAtIndexPaths(_ indexPaths: [AnyObject]) ``` |
| To | ``` func insertItemsAtIndexPaths(_ indexPaths: [NSIndexPath]) ``` |

Modified [UICollectionView.reloadItemsAtIndexPaths(_: [NSIndexPath])](https://developer.apple.com/documentation/uikit/uicollectionview/1618055-reloaditems)

|  | Declaration |
| --- | --- |
| From | ``` func reloadItemsAtIndexPaths(_ indexPaths: [AnyObject]) ``` |
| To | ``` func reloadItemsAtIndexPaths(_ indexPaths: [NSIndexPath]) ``` |

Modified [UICollectionView.setCollectionViewLayout(_: UICollectionViewLayout, animated: Bool, completion: ((Bool) -> Void)?)](https://developer.apple.com/documentation/uikit/uicollectionview/1618017-setcollectionviewlayout)

|  | Declaration |
| --- | --- |
| From | ``` func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated animated: Bool, completion completion: ((Bool) -> Void)!) ``` |
| To | ``` func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated animated: Bool, completion completion: ((Bool) -> Void)?) ``` |

Modified [UICollectionView.visibleCells() -> [UICollectionViewCell]](https://developer.apple.com/documentation/uikit/uicollectionview/1618056-visiblecells)

|  | Declaration |
| --- | --- |
| From | ``` func visibleCells() -> [AnyObject] ``` |
| To | ``` func visibleCells() -> [UICollectionViewCell] ``` |

Modified [UICollectionViewCell](https://developer.apple.com/documentation/uikit/uicollectionviewcell)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionViewCell : UICollectionReusableView {     var contentView: UIView { get }     var selected: Bool     var highlighted: Bool     var backgroundView: UIView?     var selectedBackgroundView: UIView! } ``` |
| To | ``` class UICollectionViewCell : UICollectionReusableView {     var contentView: UIView { get }     var selected: Bool     var highlighted: Bool     var backgroundView: UIView?     var selectedBackgroundView: UIView? } ``` |

Modified [UICollectionViewCell.selectedBackgroundView](https://developer.apple.com/documentation/uikit/uicollectionviewcell/1620138-selectedbackgroundview)

|  | Declaration |
| --- | --- |
| From | ``` var selectedBackgroundView: UIView! ``` |
| To | ``` var selectedBackgroundView: UIView? ``` |

Modified [UICollectionViewController](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionViewController : UIViewController, UICollectionViewDelegate, UIScrollViewDelegate, NSObjectProtocol, UICollectionViewDataSource {     init(collectionViewLayout layout: UICollectionViewLayout)     var collectionView: UICollectionView?     var clearsSelectionOnViewWillAppear: Bool     var useLayoutToLayoutNavigationTransitions: Bool     var collectionViewLayout: UICollectionViewLayout! { get } } ``` |
| To | ``` class UICollectionViewController : UIViewController, UICollectionViewDelegate, UIScrollViewDelegate, UICollectionViewDataSource {     init(collectionViewLayout layout: UICollectionViewLayout)     init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     init?(coder aDecoder: NSCoder)     var collectionView: UICollectionView?     var clearsSelectionOnViewWillAppear: Bool     var useLayoutToLayoutNavigationTransitions: Bool     var collectionViewLayout: UICollectionViewLayout { get }     var installsStandardGestureForInteractiveMovement: Bool } ``` |

Modified [UICollectionViewController.collectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/1623980-collectionviewlayout)

|  | Declaration |
| --- | --- |
| From | ``` var collectionViewLayout: UICollectionViewLayout! { get } ``` |
| To | ``` var collectionViewLayout: UICollectionViewLayout { get } ``` |

Modified [UICollectionViewDataSource](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource)

|  | Declaration |
| --- | --- |
| From | ``` protocol UICollectionViewDataSource : NSObjectProtocol {     func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int     func collectionView(_ collectionView: UICollectionView, cellForItemAtIndexPath indexPath: NSIndexPath) -> UICollectionViewCell     optional func numberOfSectionsInCollectionView(_ collectionView: UICollectionView) -> Int     optional func collectionView(_ collectionView: UICollectionView, viewForSupplementaryElementOfKind kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionReusableView } ``` |
| To | ``` protocol UICollectionViewDataSource : NSObjectProtocol {     func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int     func collectionView(_ collectionView: UICollectionView, cellForItemAtIndexPath indexPath: NSIndexPath) -> UICollectionViewCell     optional func numberOfSectionsInCollectionView(_ collectionView: UICollectionView) -> Int     optional func collectionView(_ collectionView: UICollectionView, viewForSupplementaryElementOfKind kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionReusableView     optional func collectionView(_ collectionView: UICollectionView, canMoveItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, moveItemAtIndexPath sourceIndexPath: NSIndexPath, toIndexPath destinationIndexPath: NSIndexPath) } ``` |

Modified [UICollectionViewDataSource.collectionView(_: UICollectionView, cellForItemAtIndexPath: NSIndexPath) -> UICollectionViewCell](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618029-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDataSource.collectionView(_: UICollectionView, numberOfItemsInSection: Int) -> Int](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618058-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDataSource.collectionView(_: UICollectionView, viewForSupplementaryElementOfKind: String, atIndexPath: NSIndexPath) -> UICollectionReusableView](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618037-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDataSource.numberOfSectionsInCollectionView(_: UICollectionView) -> Int](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618023-numberofsections)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UICollectionViewDelegate : UIScrollViewDelegate, NSObjectProtocol {     optional func collectionView(_ collectionView: UICollectionView, shouldHighlightItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, didHighlightItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didUnhighlightItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, shouldSelectItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, shouldDeselectItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, didSelectItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didDeselectItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, willDisplayCell cell: UICollectionViewCell, forItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, willDisplaySupplementaryView view: UICollectionReusableView, forElementKind elementKind: String, atIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didEndDisplayingCell cell: UICollectionViewCell, forItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didEndDisplayingSupplementaryView view: UICollectionReusableView, forElementOfKind elementKind: String, atIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, shouldShowMenuForItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, canPerformAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject!) -> Bool     optional func collectionView(_ collectionView: UICollectionView, performAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject!)     optional func collectionView(_ collectionView: UICollectionView, transitionLayoutForOldLayout fromLayout: UICollectionViewLayout, newLayout toLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout! } ``` |
| To | ``` protocol UICollectionViewDelegate : UIScrollViewDelegate, NSObjectProtocol {     optional func collectionView(_ collectionView: UICollectionView, shouldHighlightItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, didHighlightItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didUnhighlightItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, shouldSelectItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, shouldDeselectItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, didSelectItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didDeselectItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, willDisplayCell cell: UICollectionViewCell, forItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, willDisplaySupplementaryView view: UICollectionReusableView, forElementKind elementKind: String, atIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didEndDisplayingCell cell: UICollectionViewCell, forItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didEndDisplayingSupplementaryView view: UICollectionReusableView, forElementOfKind elementKind: String, atIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, shouldShowMenuForItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, canPerformAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) -> Bool     optional func collectionView(_ collectionView: UICollectionView, performAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?)     optional func collectionView(_ collectionView: UICollectionView, transitionLayoutForOldLayout fromLayout: UICollectionViewLayout, newLayout toLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout     optional func collectionView(_ collectionView: UICollectionView, targetIndexPathForMoveFromItemAtIndexPath originalIndexPath: NSIndexPath, toProposedIndexPath proposedIndexPath: NSIndexPath) -> NSIndexPath     optional func collectionView(_ collectionView: UICollectionView, targetContentOffsetForProposedContentOffset proposedContentOffset: CGPoint) -> CGPoint } ``` |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, canPerformAction: Selector, forItemAtIndexPath: NSIndexPath, withSender: AnyObject?) -> Bool](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618051-collectionview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func collectionView(_ collectionView: UICollectionView, canPerformAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject!) -> Bool ``` | iOS 8.0 |
| To | ``` optional func collectionView(_ collectionView: UICollectionView, canPerformAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) -> Bool ``` | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, didDeselectItemAtIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618035-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, didEndDisplayingCell: UICollectionViewCell, forItemAtIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618006-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, didEndDisplayingSupplementaryView: UICollectionReusableView, forElementOfKind: String, atIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618036-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, didHighlightItemAtIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618049-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, didSelectItemAtIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618032-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, didUnhighlightItemAtIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618027-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, performAction: Selector, forItemAtIndexPath: NSIndexPath, withSender: AnyObject?)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618073-collectionview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func collectionView(_ collectionView: UICollectionView, performAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject!) ``` | iOS 8.0 |
| To | ``` optional func collectionView(_ collectionView: UICollectionView, performAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) ``` | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, shouldDeselectItemAtIndexPath: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618067-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, shouldHighlightItemAtIndexPath: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618070-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, shouldSelectItemAtIndexPath: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618095-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, shouldShowMenuForItemAtIndexPath: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618010-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegate.collectionView(_: UICollectionView, transitionLayoutForOldLayout: UICollectionViewLayout, newLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618100-collectionview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func collectionView(_ collectionView: UICollectionView, transitionLayoutForOldLayout fromLayout: UICollectionViewLayout, newLayout toLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout! ``` | iOS 8.0 |
| To | ``` optional func collectionView(_ collectionView: UICollectionView, transitionLayoutForOldLayout fromLayout: UICollectionViewLayout, newLayout toLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout ``` | iOS 7.0 |

Modified [UICollectionViewDelegateFlowLayout.collectionView(_: UICollectionView, layout: UICollectionViewLayout, insetForSectionAtIndex: Int) -> UIEdgeInsets](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617718-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegateFlowLayout.collectionView(_: UICollectionView, layout: UICollectionViewLayout, minimumInteritemSpacingForSectionAtIndex: Int) -> CGFloat](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617696-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegateFlowLayout.collectionView(_: UICollectionView, layout: UICollectionViewLayout, minimumLineSpacingForSectionAtIndex: Int) -> CGFloat](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617705-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegateFlowLayout.collectionView(_: UICollectionView, layout: UICollectionViewLayout, referenceSizeForFooterInSection: Int) -> CGSize](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617713-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegateFlowLayout.collectionView(_: UICollectionView, layout: UICollectionViewLayout, referenceSizeForHeaderInSection: Int) -> CGSize](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617702-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewDelegateFlowLayout.collectionView(_: UICollectionView, layout: UICollectionViewLayout, sizeForItemAtIndexPath: NSIndexPath) -> CGSize](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617708-collectionview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified [UICollectionViewFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionViewFlowLayout : UICollectionViewLayout {     var minimumLineSpacing: CGFloat     var minimumInteritemSpacing: CGFloat     var itemSize: CGSize     var estimatedItemSize: CGSize     var scrollDirection: UICollectionViewScrollDirection     var headerReferenceSize: CGSize     var footerReferenceSize: CGSize     var sectionInset: UIEdgeInsets } ``` |
| To | ``` class UICollectionViewFlowLayout : UICollectionViewLayout {     var minimumLineSpacing: CGFloat     var minimumInteritemSpacing: CGFloat     var itemSize: CGSize     var estimatedItemSize: CGSize     var scrollDirection: UICollectionViewScrollDirection     var headerReferenceSize: CGSize     var footerReferenceSize: CGSize     var sectionInset: UIEdgeInsets     var sectionHeadersPinToVisibleBounds: Bool     var sectionFootersPinToVisibleBounds: Bool } ``` |

Modified [UICollectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionviewlayout)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionViewLayout : NSObject, NSCoding {     var collectionView: UICollectionView? { get }     func invalidateLayout()     func invalidateLayoutWithContext(_ context: UICollectionViewLayoutInvalidationContext)     func registerClass(_ viewClass: AnyClass?, forDecorationViewOfKind elementKind: String)     func registerNib(_ nib: UINib?, forDecorationViewOfKind elementKind: String) } extension UICollectionViewLayout {     class func layoutAttributesClass() -> AnyClass     class func invalidationContextClass() -> AnyClass     func prepareLayout()     func layoutAttributesForElementsInRect(_ rect: CGRect) -> [AnyObject]?     func layoutAttributesForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes!     func layoutAttributesForSupplementaryViewOfKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes!     func layoutAttributesForDecorationViewOfKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes!     func shouldInvalidateLayoutForBoundsChange(_ newBounds: CGRect) -> Bool     func invalidationContextForBoundsChange(_ newBounds: CGRect) -> UICollectionViewLayoutInvalidationContext     func shouldInvalidateLayoutForPreferredLayoutAttributes(_ preferredAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: UICollectionViewLayoutAttributes) -> Bool     func invalidationContextForPreferredLayoutAttributes(_ preferredAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext     func targetContentOffsetForProposedContentOffset(_ proposedContentOffset: CGPoint, withScrollingVelocity velocity: CGPoint) -> CGPoint     func targetContentOffsetForProposedContentOffset(_ proposedContentOffset: CGPoint) -> CGPoint     func collectionViewContentSize() -> CGSize } extension UICollectionViewLayout {     func prepareForCollectionViewUpdates(_ updateItems: [AnyObject]!)     func finalizeCollectionViewUpdates()     func prepareForAnimatedBoundsChange(_ oldBounds: CGRect)     func finalizeAnimatedBoundsChange()     func prepareForTransitionToLayout(_ newLayout: UICollectionViewLayout!)     func prepareForTransitionFromLayout(_ oldLayout: UICollectionViewLayout)     func finalizeLayoutTransition()     func initialLayoutAttributesForAppearingItemAtIndexPath(_ itemIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func finalLayoutAttributesForDisappearingItemAtIndexPath(_ itemIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func initialLayoutAttributesForAppearingSupplementaryElementOfKind(_ elementKind: String, atIndexPath elementIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func finalLayoutAttributesForDisappearingSupplementaryElementOfKind(_ elementKind: String, atIndexPath elementIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func initialLayoutAttributesForAppearingDecorationElementOfKind(_ elementKind: String, atIndexPath decorationIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func finalLayoutAttributesForDisappearingDecorationElementOfKind(_ elementKind: String, atIndexPath decorationIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func indexPathsToDeleteForSupplementaryViewOfKind(_ elementKind: String) -> [AnyObject]     func indexPathsToDeleteForDecorationViewOfKind(_ elementKind: String) -> [AnyObject]     func indexPathsToInsertForSupplementaryViewOfKind(_ elementKind: String) -> [AnyObject]     func indexPathsToInsertForDecorationViewOfKind(_ elementKind: String) -> [AnyObject] } ``` |
| To | ``` class UICollectionViewLayout : NSObject, NSCoding {     init()     init?(coder aDecoder: NSCoder)     var collectionView: UICollectionView? { get }     func invalidateLayout()     func invalidateLayoutWithContext(_ context: UICollectionViewLayoutInvalidationContext)     func registerClass(_ viewClass: AnyClass?, forDecorationViewOfKind elementKind: String)     func registerNib(_ nib: UINib?, forDecorationViewOfKind elementKind: String) } extension UICollectionViewLayout {     class func layoutAttributesClass() -> AnyClass     class func invalidationContextClass() -> AnyClass     func prepareLayout()     func layoutAttributesForElementsInRect(_ rect: CGRect) -> [UICollectionViewLayoutAttributes]?     func layoutAttributesForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func layoutAttributesForSupplementaryViewOfKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func layoutAttributesForDecorationViewOfKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func shouldInvalidateLayoutForBoundsChange(_ newBounds: CGRect) -> Bool     func invalidationContextForBoundsChange(_ newBounds: CGRect) -> UICollectionViewLayoutInvalidationContext     func shouldInvalidateLayoutForPreferredLayoutAttributes(_ preferredAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: UICollectionViewLayoutAttributes) -> Bool     func invalidationContextForPreferredLayoutAttributes(_ preferredAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext     func targetContentOffsetForProposedContentOffset(_ proposedContentOffset: CGPoint, withScrollingVelocity velocity: CGPoint) -> CGPoint     func targetContentOffsetForProposedContentOffset(_ proposedContentOffset: CGPoint) -> CGPoint     func collectionViewContentSize() -> CGSize } extension UICollectionViewLayout {     func prepareForCollectionViewUpdates(_ updateItems: [UICollectionViewUpdateItem])     func finalizeCollectionViewUpdates()     func prepareForAnimatedBoundsChange(_ oldBounds: CGRect)     func finalizeAnimatedBoundsChange()     func prepareForTransitionToLayout(_ newLayout: UICollectionViewLayout)     func prepareForTransitionFromLayout(_ oldLayout: UICollectionViewLayout)     func finalizeLayoutTransition()     func initialLayoutAttributesForAppearingItemAtIndexPath(_ itemIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func finalLayoutAttributesForDisappearingItemAtIndexPath(_ itemIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func initialLayoutAttributesForAppearingSupplementaryElementOfKind(_ elementKind: String, atIndexPath elementIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func finalLayoutAttributesForDisappearingSupplementaryElementOfKind(_ elementKind: String, atIndexPath elementIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func initialLayoutAttributesForAppearingDecorationElementOfKind(_ elementKind: String, atIndexPath decorationIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func finalLayoutAttributesForDisappearingDecorationElementOfKind(_ elementKind: String, atIndexPath decorationIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func indexPathsToDeleteForSupplementaryViewOfKind(_ elementKind: String) -> [NSIndexPath]     func indexPathsToDeleteForDecorationViewOfKind(_ elementKind: String) -> [NSIndexPath]     func indexPathsToInsertForSupplementaryViewOfKind(_ elementKind: String) -> [NSIndexPath]     func indexPathsToInsertForDecorationViewOfKind(_ elementKind: String) -> [NSIndexPath] } extension UICollectionViewLayout {     func targetIndexPathForInteractivelyMovingItem(_ previousIndexPath: NSIndexPath, withPosition position: CGPoint) -> NSIndexPath     func layoutAttributesForInteractivelyMovingItemAtIndexPath(_ indexPath: NSIndexPath, withTargetPosition position: CGPoint) -> UICollectionViewLayoutAttributes     func invalidationContextForInteractivelyMovingItems(_ targetIndexPaths: [NSIndexPath], withTargetPosition targetPosition: CGPoint, previousIndexPaths previousIndexPaths: [NSIndexPath], previousPosition previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext     func invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths(_ indexPaths: [NSIndexPath], previousIndexPaths previousIndexPaths: [NSIndexPath], movementCancelled movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext } ``` |

Modified [UICollectionViewLayout.indexPathsToDeleteForDecorationViewOfKind(_: String) -> [NSIndexPath]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617730-indexpathstodeletefordecorationv)

|  | Declaration |
| --- | --- |
| From | ``` func indexPathsToDeleteForDecorationViewOfKind(_ elementKind: String) -> [AnyObject] ``` |
| To | ``` func indexPathsToDeleteForDecorationViewOfKind(_ elementKind: String) -> [NSIndexPath] ``` |

Modified [UICollectionViewLayout.indexPathsToDeleteForSupplementaryViewOfKind(_: String) -> [NSIndexPath]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617807-indexpathstodeleteforsupplementa)

|  | Declaration |
| --- | --- |
| From | ``` func indexPathsToDeleteForSupplementaryViewOfKind(_ elementKind: String) -> [AnyObject] ``` |
| To | ``` func indexPathsToDeleteForSupplementaryViewOfKind(_ elementKind: String) -> [NSIndexPath] ``` |

Modified [UICollectionViewLayout.indexPathsToInsertForDecorationViewOfKind(_: String) -> [NSIndexPath]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617750-indexpathstoinsertfordecorationv)

|  | Declaration |
| --- | --- |
| From | ``` func indexPathsToInsertForDecorationViewOfKind(_ elementKind: String) -> [AnyObject] ``` |
| To | ``` func indexPathsToInsertForDecorationViewOfKind(_ elementKind: String) -> [NSIndexPath] ``` |

Modified [UICollectionViewLayout.indexPathsToInsertForSupplementaryViewOfKind(_: String) -> [NSIndexPath]](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617770-indexpathstoinsertforsupplementa)

|  | Declaration |
| --- | --- |
| From | ``` func indexPathsToInsertForSupplementaryViewOfKind(_ elementKind: String) -> [AnyObject] ``` |
| To | ``` func indexPathsToInsertForSupplementaryViewOfKind(_ elementKind: String) -> [NSIndexPath] ``` |

Modified [UICollectionViewLayout.layoutAttributesForDecorationViewOfKind(_: String, atIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617809-layoutattributesfordecorationvie)

|  | Declaration |
| --- | --- |
| From | ``` func layoutAttributesForDecorationViewOfKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes! ``` |
| To | ``` func layoutAttributesForDecorationViewOfKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes? ``` |

Modified [UICollectionViewLayout.layoutAttributesForElementsInRect(_: CGRect) -> [UICollectionViewLayoutAttributes]?](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617769-layoutattributesforelementsinrec)

|  | Declaration |
| --- | --- |
| From | ``` func layoutAttributesForElementsInRect(_ rect: CGRect) -> [AnyObject]? ``` |
| To | ``` func layoutAttributesForElementsInRect(_ rect: CGRect) -> [UICollectionViewLayoutAttributes]? ``` |

Modified [UICollectionViewLayout.layoutAttributesForItemAtIndexPath(_: NSIndexPath) -> UICollectionViewLayoutAttributes?](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617797-layoutattributesforitematindexpa)

|  | Declaration |
| --- | --- |
| From | ``` func layoutAttributesForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes! ``` |
| To | ``` func layoutAttributesForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes? ``` |

Modified [UICollectionViewLayout.layoutAttributesForSupplementaryViewOfKind(_: String, atIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617792-layoutattributesforsupplementary)

|  | Declaration |
| --- | --- |
| From | ``` func layoutAttributesForSupplementaryViewOfKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes! ``` |
| To | ``` func layoutAttributesForSupplementaryViewOfKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes? ``` |

Modified [UICollectionViewLayout.prepareForCollectionViewUpdates(_: [UICollectionViewUpdateItem])](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617784-prepareforcollectionviewupdates)

|  | Declaration |
| --- | --- |
| From | ``` func prepareForCollectionViewUpdates(_ updateItems: [AnyObject]!) ``` |
| To | ``` func prepareForCollectionViewUpdates(_ updateItems: [UICollectionViewUpdateItem]) ``` |

Modified [UICollectionViewLayout.prepareForTransitionToLayout(_: UICollectionViewLayout)](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617791-preparefortransitiontolayout)

|  | Declaration |
| --- | --- |
| From | ``` func prepareForTransitionToLayout(_ newLayout: UICollectionViewLayout!) ``` |
| To | ``` func prepareForTransitionToLayout(_ newLayout: UICollectionViewLayout) ``` |

Modified [UICollectionViewLayoutAttributes](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionViewLayoutAttributes : NSObject, NSCopying, UIDynamicItem, NSObjectProtocol {     var frame: CGRect     var center: CGPoint     var size: CGSize     var transform3D: CATransform3D     var bounds: CGRect     var transform: CGAffineTransform     var alpha: CGFloat     var zIndex: Int     var hidden: Bool     var indexPath: NSIndexPath!     var representedElementCategory: UICollectionElementCategory { get }     var representedElementKind: String! { get }     convenience init(forCellWithIndexPath indexPath: NSIndexPath)     class func layoutAttributesForCellWithIndexPath(_ indexPath: NSIndexPath) -> Self     convenience init(forSupplementaryViewOfKind elementKind: String, withIndexPath indexPath: NSIndexPath)     class func layoutAttributesForSupplementaryViewOfKind(_ elementKind: String, withIndexPath indexPath: NSIndexPath) -> Self     convenience init(forDecorationViewOfKind decorationViewKind: String, withIndexPath indexPath: NSIndexPath)     class func layoutAttributesForDecorationViewOfKind(_ decorationViewKind: String, withIndexPath indexPath: NSIndexPath) -> Self } ``` |
| To | ``` class UICollectionViewLayoutAttributes : NSObject, NSCopying, UIDynamicItem {     var frame: CGRect     var center: CGPoint     var size: CGSize     var transform3D: CATransform3D     var bounds: CGRect     var transform: CGAffineTransform     var alpha: CGFloat     var zIndex: Int     var hidden: Bool     var indexPath: NSIndexPath     var representedElementCategory: UICollectionElementCategory { get }     var representedElementKind: String? { get }     convenience init(forCellWithIndexPath indexPath: NSIndexPath)     class func layoutAttributesForCellWithIndexPath(_ indexPath: NSIndexPath) -> Self     convenience init(forSupplementaryViewOfKind elementKind: String, withIndexPath indexPath: NSIndexPath)     class func layoutAttributesForSupplementaryViewOfKind(_ elementKind: String, withIndexPath indexPath: NSIndexPath) -> Self     convenience init(forDecorationViewOfKind decorationViewKind: String, withIndexPath indexPath: NSIndexPath)     class func layoutAttributesForDecorationViewOfKind(_ decorationViewKind: String, withIndexPath indexPath: NSIndexPath) -> Self } ``` |

Modified [UICollectionViewLayoutAttributes.indexPath](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617776-indexpath)

|  | Declaration |
| --- | --- |
| From | ``` var indexPath: NSIndexPath! ``` |
| To | ``` var indexPath: NSIndexPath ``` |

Modified [UICollectionViewLayoutAttributes.representedElementKind](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617806-representedelementkind)

|  | Declaration |
| --- | --- |
| From | ``` var representedElementKind: String! { get } ``` |
| To | ``` var representedElementKind: String? { get } ``` |

Modified [UICollectionViewLayoutInvalidationContext](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionViewLayoutInvalidationContext : NSObject {     var invalidateEverything: Bool { get }     var invalidateDataSourceCounts: Bool { get }     func invalidateItemsAtIndexPaths(_ indexPaths: [AnyObject])     func invalidateSupplementaryElementsOfKind(_ elementKind: String, atIndexPaths indexPaths: [AnyObject])     func invalidateDecorationElementsOfKind(_ elementKind: String, atIndexPaths indexPaths: [AnyObject])     var invalidatedItemIndexPaths: [AnyObject]? { get }     var invalidatedSupplementaryIndexPaths: [NSObject : AnyObject]? { get }     var invalidatedDecorationIndexPaths: [NSObject : AnyObject]! { get }     var contentOffsetAdjustment: CGPoint     var contentSizeAdjustment: CGSize } ``` |
| To | ``` class UICollectionViewLayoutInvalidationContext : NSObject {     var invalidateEverything: Bool { get }     var invalidateDataSourceCounts: Bool { get }     func invalidateItemsAtIndexPaths(_ indexPaths: [NSIndexPath])     func invalidateSupplementaryElementsOfKind(_ elementKind: String, atIndexPaths indexPaths: [NSIndexPath])     func invalidateDecorationElementsOfKind(_ elementKind: String, atIndexPaths indexPaths: [NSIndexPath])     var invalidatedItemIndexPaths: [NSIndexPath]? { get }     var invalidatedSupplementaryIndexPaths: [String : [NSIndexPath]]? { get }     var invalidatedDecorationIndexPaths: [String : [NSIndexPath]]? { get }     var contentOffsetAdjustment: CGPoint     var contentSizeAdjustment: CGSize     var previousIndexPathsForInteractivelyMovingItems: [NSIndexPath]? { get }     var targetIndexPathsForInteractivelyMovingItems: [NSIndexPath]? { get }     var interactiveMovementTarget: CGPoint { get } } ``` |

Modified [UICollectionViewLayoutInvalidationContext.invalidatedDecorationIndexPaths](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617805-invalidateddecorationindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` var invalidatedDecorationIndexPaths: [NSObject : AnyObject]! { get } ``` |
| To | ``` var invalidatedDecorationIndexPaths: [String : [NSIndexPath]]? { get } ``` |

Modified [UICollectionViewLayoutInvalidationContext.invalidateDecorationElementsOfKind(_: String, atIndexPaths: [NSIndexPath])](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617736-invalidatedecorationelements)

|  | Declaration |
| --- | --- |
| From | ``` func invalidateDecorationElementsOfKind(_ elementKind: String, atIndexPaths indexPaths: [AnyObject]) ``` |
| To | ``` func invalidateDecorationElementsOfKind(_ elementKind: String, atIndexPaths indexPaths: [NSIndexPath]) ``` |

Modified [UICollectionViewLayoutInvalidationContext.invalidatedItemIndexPaths](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617723-invalidateditemindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` var invalidatedItemIndexPaths: [AnyObject]? { get } ``` |
| To | ``` var invalidatedItemIndexPaths: [NSIndexPath]? { get } ``` |

Modified [UICollectionViewLayoutInvalidationContext.invalidatedSupplementaryIndexPaths](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617777-invalidatedsupplementaryindexpat)

|  | Declaration |
| --- | --- |
| From | ``` var invalidatedSupplementaryIndexPaths: [NSObject : AnyObject]? { get } ``` |
| To | ``` var invalidatedSupplementaryIndexPaths: [String : [NSIndexPath]]? { get } ``` |

Modified [UICollectionViewLayoutInvalidationContext.invalidateItemsAtIndexPaths(_: [NSIndexPath])](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617795-invalidateitems)

|  | Declaration |
| --- | --- |
| From | ``` func invalidateItemsAtIndexPaths(_ indexPaths: [AnyObject]) ``` |
| To | ``` func invalidateItemsAtIndexPaths(_ indexPaths: [NSIndexPath]) ``` |

Modified [UICollectionViewLayoutInvalidationContext.invalidateSupplementaryElementsOfKind(_: String, atIndexPaths: [NSIndexPath])](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/1617747-invalidatesupplementaryelements)

|  | Declaration |
| --- | --- |
| From | ``` func invalidateSupplementaryElementsOfKind(_ elementKind: String, atIndexPaths indexPaths: [AnyObject]) ``` |
| To | ``` func invalidateSupplementaryElementsOfKind(_ elementKind: String, atIndexPaths indexPaths: [NSIndexPath]) ``` |

Modified [UICollectionViewScrollDirection [enum]](https://developer.apple.com/documentation/uikit/uicollectionviewscrolldirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UICollectionViewScrollPosition [struct]](https://developer.apple.com/documentation/uikit/uicollectionview/scrollposition)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UICollectionViewScrollPosition : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: UICollectionViewScrollPosition { get }     static var Top: UICollectionViewScrollPosition { get }     static var CenteredVertically: UICollectionViewScrollPosition { get }     static var Bottom: UICollectionViewScrollPosition { get }     static var Left: UICollectionViewScrollPosition { get }     static var CenteredHorizontally: UICollectionViewScrollPosition { get }     static var Right: UICollectionViewScrollPosition { get } } ``` | RawOptionSetType |
| To | ``` struct UICollectionViewScrollPosition : OptionSetType {     init(rawValue rawValue: UInt)     static var None: UICollectionViewScrollPosition { get }     static var Top: UICollectionViewScrollPosition { get }     static var CenteredVertically: UICollectionViewScrollPosition { get }     static var Bottom: UICollectionViewScrollPosition { get }     static var Left: UICollectionViewScrollPosition { get }     static var CenteredHorizontally: UICollectionViewScrollPosition { get }     static var Right: UICollectionViewScrollPosition { get } } ``` | OptionSetType |

Modified [UICollectionViewTransitionLayout](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionViewTransitionLayout : UICollectionViewLayout {     var transitionProgress: CGFloat     var currentLayout: UICollectionViewLayout! { get }     var nextLayout: UICollectionViewLayout! { get }     init(currentLayout currentLayout: UICollectionViewLayout, nextLayout newLayout: UICollectionViewLayout)     func updateValue(_ value: CGFloat, forAnimatedKey key: String)     func valueForAnimatedKey(_ key: String) -> CGFloat } ``` |
| To | ``` class UICollectionViewTransitionLayout : UICollectionViewLayout {     var transitionProgress: CGFloat     var currentLayout: UICollectionViewLayout { get }     var nextLayout: UICollectionViewLayout { get }     init(currentLayout currentLayout: UICollectionViewLayout, nextLayout newLayout: UICollectionViewLayout)     init?(coder aDecoder: NSCoder)     convenience init()     func updateValue(_ value: CGFloat, forAnimatedKey key: String)     func valueForAnimatedKey(_ key: String) -> CGFloat } ``` |

Modified [UICollectionViewTransitionLayout.currentLayout](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622190-currentlayout)

|  | Declaration |
| --- | --- |
| From | ``` var currentLayout: UICollectionViewLayout! { get } ``` |
| To | ``` var currentLayout: UICollectionViewLayout { get } ``` |

Modified [UICollectionViewTransitionLayout.nextLayout](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/1622188-nextlayout)

|  | Declaration |
| --- | --- |
| From | ``` var nextLayout: UICollectionViewLayout! { get } ``` |
| To | ``` var nextLayout: UICollectionViewLayout { get } ``` |

Modified [UICollectionViewUpdateItem](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem)

|  | Declaration |
| --- | --- |
| From | ``` class UICollectionViewUpdateItem : NSObject {     var indexPathBeforeUpdate: NSIndexPath? { get }     var indexPathAfterUpdate: NSIndexPath? { get }     var updateAction: UICollectionUpdateAction { get } } ``` |
| To | ``` class UICollectionViewUpdateItem : NSObject {     var indexPathBeforeUpdate: NSIndexPath { get }     var indexPathAfterUpdate: NSIndexPath { get }     var updateAction: UICollectionUpdateAction { get } } ``` |

Modified [UICollectionViewUpdateItem.indexPathAfterUpdate](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/1617765-indexpathafterupdate)

|  | Declaration |
| --- | --- |
| From | ``` var indexPathAfterUpdate: NSIndexPath? { get } ``` |
| To | ``` var indexPathAfterUpdate: NSIndexPath { get } ``` |

Modified [UICollectionViewUpdateItem.indexPathBeforeUpdate](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/1617772-indexpathbeforeupdate)

|  | Declaration |
| --- | --- |
| From | ``` var indexPathBeforeUpdate: NSIndexPath? { get } ``` |
| To | ``` var indexPathBeforeUpdate: NSIndexPath { get } ``` |

Modified [UICollisionBehavior](https://developer.apple.com/documentation/uikit/uicollisionbehavior)

|  | Declaration |
| --- | --- |
| From | ``` class UICollisionBehavior : UIDynamicBehavior {     init!(items items: [AnyObject])     func addItem(_ item: UIDynamicItem)     func removeItem(_ item: UIDynamicItem)     var items: [AnyObject] { get }     var collisionMode: UICollisionBehaviorMode     var translatesReferenceBoundsIntoBoundary: Bool     func setTranslatesReferenceBoundsIntoBoundaryWithInsets(_ insets: UIEdgeInsets)     func addBoundaryWithIdentifier(_ identifier: NSCopying, forPath bezierPath: UIBezierPath)     func addBoundaryWithIdentifier(_ identifier: NSCopying, fromPoint p1: CGPoint, toPoint p2: CGPoint)     func boundaryWithIdentifier(_ identifier: NSCopying) -> UIBezierPath?     func removeBoundaryWithIdentifier(_ identifier: NSCopying)     var boundaryIdentifiers: [AnyObject]? { get }     func removeAllBoundaries()     unowned(unsafe) var collisionDelegate: UICollisionBehaviorDelegate? } ``` |
| To | ``` class UICollisionBehavior : UIDynamicBehavior {     init(items items: [UIDynamicItem])     func addItem(_ item: UIDynamicItem)     func removeItem(_ item: UIDynamicItem)     var items: [UIDynamicItem] { get }     var collisionMode: UICollisionBehaviorMode     var translatesReferenceBoundsIntoBoundary: Bool     func setTranslatesReferenceBoundsIntoBoundaryWithInsets(_ insets: UIEdgeInsets)     func addBoundaryWithIdentifier(_ identifier: NSCopying, forPath bezierPath: UIBezierPath)     func addBoundaryWithIdentifier(_ identifier: NSCopying, fromPoint p1: CGPoint, toPoint p2: CGPoint)     func boundaryWithIdentifier(_ identifier: NSCopying) -> UIBezierPath?     func removeBoundaryWithIdentifier(_ identifier: NSCopying)     var boundaryIdentifiers: [NSCopying]? { get }     func removeAllBoundaries()     weak var collisionDelegate: UICollisionBehaviorDelegate? } ``` |

Modified [UICollisionBehavior.boundaryIdentifiers](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624812-boundaryidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` var boundaryIdentifiers: [AnyObject]? { get } ``` |
| To | ``` var boundaryIdentifiers: [NSCopying]? { get } ``` |

Modified [UICollisionBehavior.collisionDelegate](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624828-collisiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var collisionDelegate: UICollisionBehaviorDelegate? ``` |
| To | ``` weak var collisionDelegate: UICollisionBehaviorDelegate? ``` |

Modified [UICollisionBehavior.init(items: [UIDynamicItem])](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624820-initwithitems)

|  | Declaration |
| --- | --- |
| From | ``` init!(items items: [AnyObject]) ``` |
| To | ``` init(items items: [UIDynamicItem]) ``` |

Modified [UICollisionBehavior.items](https://developer.apple.com/documentation/uikit/uicollisionbehavior/1624819-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject] { get } ``` |
| To | ``` var items: [UIDynamicItem] { get } ``` |

Modified [UICollisionBehaviorDelegate](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UICollisionBehaviorDelegate : NSObjectProtocol {     optional func collisionBehavior(_ behavior: UICollisionBehavior, beganContactForItem item1: UIDynamicItem, withItem item2: UIDynamicItem, atPoint p: CGPoint)     optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactForItem item1: UIDynamicItem, withItem item2: UIDynamicItem)     optional func collisionBehavior(_ behavior: UICollisionBehavior, beganContactForItem item: UIDynamicItem, withBoundaryIdentifier identifier: NSCopying, atPoint p: CGPoint)     optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactForItem item: UIDynamicItem, withBoundaryIdentifier identifier: NSCopying) } ``` |
| To | ``` protocol UICollisionBehaviorDelegate : NSObjectProtocol {     optional func collisionBehavior(_ behavior: UICollisionBehavior, beganContactForItem item1: UIDynamicItem, withItem item2: UIDynamicItem, atPoint p: CGPoint)     optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactForItem item1: UIDynamicItem, withItem item2: UIDynamicItem)     optional func collisionBehavior(_ behavior: UICollisionBehavior, beganContactForItem item: UIDynamicItem, withBoundaryIdentifier identifier: NSCopying?, atPoint p: CGPoint)     optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactForItem item: UIDynamicItem, withBoundaryIdentifier identifier: NSCopying?) } ``` |

Modified [UICollisionBehaviorDelegate.collisionBehavior(_: UICollisionBehavior, beganContactForItem: UIDynamicItem, withBoundaryIdentifier: NSCopying?, atPoint: CGPoint)](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624816-collisionbehavior)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func collisionBehavior(_ behavior: UICollisionBehavior, beganContactForItem item: UIDynamicItem, withBoundaryIdentifier identifier: NSCopying, atPoint p: CGPoint) ``` | iOS 8.0 |
| To | ``` optional func collisionBehavior(_ behavior: UICollisionBehavior, beganContactForItem item: UIDynamicItem, withBoundaryIdentifier identifier: NSCopying?, atPoint p: CGPoint) ``` | iOS 7.0 |

Modified [UICollisionBehaviorDelegate.collisionBehavior(_: UICollisionBehavior, beganContactForItem: UIDynamicItem, withItem: UIDynamicItem, atPoint: CGPoint)](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624835-collisionbehavior)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [UICollisionBehaviorDelegate.collisionBehavior(_: UICollisionBehavior, endedContactForItem: UIDynamicItem, withBoundaryIdentifier: NSCopying?)](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624834-collisionbehavior)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactForItem item: UIDynamicItem, withBoundaryIdentifier identifier: NSCopying) ``` | iOS 8.0 |
| To | ``` optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactForItem item: UIDynamicItem, withBoundaryIdentifier identifier: NSCopying?) ``` | iOS 7.0 |

Modified [UICollisionBehaviorDelegate.collisionBehavior(_: UICollisionBehavior, endedContactForItem: UIDynamicItem, withItem: UIDynamicItem)](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/1624833-collisionbehavior)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [UICollisionBehaviorMode [struct]](https://developer.apple.com/documentation/uikit/uicollisionbehavior/mode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UICollisionBehaviorMode : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Items: UICollisionBehaviorMode { get }     static var Boundaries: UICollisionBehaviorMode { get }     static var Everything: UICollisionBehaviorMode { get } } ``` | RawOptionSetType |
| To | ``` struct UICollisionBehaviorMode : OptionSetType {     init(rawValue rawValue: UInt)     static var Items: UICollisionBehaviorMode { get }     static var Boundaries: UICollisionBehaviorMode { get }     static var Everything: UICollisionBehaviorMode { get } } ``` | OptionSetType |

Modified [UIColor](https://developer.apple.com/documentation/uikit/uicolor)

|  | Declaration |
| --- | --- |
| From | ``` class UIColor : NSObject, NSSecureCoding, NSCoding, NSCopying {     init!(white white: CGFloat, alpha alpha: CGFloat) -> UIColor     class func colorWithWhite(_ white: CGFloat, alpha alpha: CGFloat) -> UIColor!     init!(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor     class func colorWithHue(_ hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor!     init!(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor     class func colorWithRed(_ red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor!     init!(CGColor cgColor: CGColor!) -> UIColor     class func colorWithCGColor(_ cgColor: CGColor!) -> UIColor!     init(patternImage image: UIImage) -> UIColor     class func colorWithPatternImage(_ image: UIImage) -> UIColor     init(CIColor ciColor: CIColor) -> UIColor     class func colorWithCIColor(_ ciColor: CIColor) -> UIColor     init(white white: CGFloat, alpha alpha: CGFloat)     init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init?(CGColor cgColor: CGColor)     init(patternImage image: UIImage)     init(CIColor ciColor: CIColor)     class func blackColor() -> UIColor     class func darkGrayColor() -> UIColor     class func lightGrayColor() -> UIColor     class func whiteColor() -> UIColor     class func grayColor() -> UIColor     class func redColor() -> UIColor     class func greenColor() -> UIColor     class func blueColor() -> UIColor     class func cyanColor() -> UIColor     class func yellowColor() -> UIColor     class func magentaColor() -> UIColor     class func orangeColor() -> UIColor     class func purpleColor() -> UIColor     class func brownColor() -> UIColor     class func clearColor() -> UIColor     func set()     func setFill()     func setStroke()     func getWhite(_ white: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getHue(_ hue: UnsafeMutablePointer<CGFloat>, saturation saturation: UnsafeMutablePointer<CGFloat>, brightness brightness: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getRed(_ red: UnsafeMutablePointer<CGFloat>, green green: UnsafeMutablePointer<CGFloat>, blue blue: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func colorWithAlphaComponent(_ alpha: CGFloat) -> UIColor     var CGColor: CGColor! { get }     var CIColor: CIColor { get } } extension UIColor {     class func lightTextColor() -> UIColor     class func darkTextColor() -> UIColor     class func groupTableViewBackgroundColor() -> UIColor     class func viewFlipsideBackgroundColor() -> UIColor!     class func scrollViewTexturedBackgroundColor() -> UIColor!     class func underPageBackgroundColor() -> UIColor! } ``` |
| To | ``` class UIColor : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(white white: CGFloat, alpha alpha: CGFloat)     class func colorWithWhite(_ white: CGFloat, alpha alpha: CGFloat) -> UIColor      init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     class func colorWithHue(_ hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     class func colorWithRed(_ red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor      init(CGColor cgColor: CGColor)     class func colorWithCGColor(_ cgColor: CGColor) -> UIColor      init(patternImage image: UIImage)     class func colorWithPatternImage(_ image: UIImage) -> UIColor      init(CIColor ciColor: CIColor)     class func colorWithCIColor(_ ciColor: CIColor) -> UIColor     init(white white: CGFloat, alpha alpha: CGFloat)     init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(CGColor cgColor: CGColor)     init(patternImage image: UIImage)     init(CIColor ciColor: CIColor)     class func blackColor() -> UIColor     class func darkGrayColor() -> UIColor     class func lightGrayColor() -> UIColor     class func whiteColor() -> UIColor     class func grayColor() -> UIColor     class func redColor() -> UIColor     class func greenColor() -> UIColor     class func blueColor() -> UIColor     class func cyanColor() -> UIColor     class func yellowColor() -> UIColor     class func magentaColor() -> UIColor     class func orangeColor() -> UIColor     class func purpleColor() -> UIColor     class func brownColor() -> UIColor     class func clearColor() -> UIColor     func set()     func setFill()     func setStroke()     func getWhite(_ white: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getHue(_ hue: UnsafeMutablePointer<CGFloat>, saturation saturation: UnsafeMutablePointer<CGFloat>, brightness brightness: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getRed(_ red: UnsafeMutablePointer<CGFloat>, green green: UnsafeMutablePointer<CGFloat>, blue blue: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func colorWithAlphaComponent(_ alpha: CGFloat) -> UIColor     var CGColor: CGColor { get }     var CIColor: CIColor { get } } extension UIColor {     class func lightTextColor() -> UIColor     class func darkTextColor() -> UIColor     class func groupTableViewBackgroundColor() -> UIColor     class func viewFlipsideBackgroundColor() -> UIColor     class func scrollViewTexturedBackgroundColor() -> UIColor     class func underPageBackgroundColor() -> UIColor } ``` |

Modified [UIColor.CGColor](https://developer.apple.com/documentation/uikit/uicolor/1621954-cgcolor)

|  | Declaration |
| --- | --- |
| From | ``` var CGColor: CGColor! { get } ``` |
| To | ``` var CGColor: CGColor { get } ``` |

Modified [UIColor.init(CGColor: CGColor)](https://developer.apple.com/documentation/uikit/uicolor/1621921-initwithcgcolor)

|  | Declaration |
| --- | --- |
| From | ``` init?(CGColor cgColor: CGColor) ``` |
| To | ``` init(CGColor cgColor: CGColor) ``` |

Modified [UIControl](https://developer.apple.com/documentation/uikit/uicontrol)

|  | Declaration |
| --- | --- |
| From | ``` class UIControl : UIView {     var enabled: Bool     var selected: Bool     var highlighted: Bool     var contentVerticalAlignment: UIControlContentVerticalAlignment     var contentHorizontalAlignment: UIControlContentHorizontalAlignment     var state: UIControlState { get }     var tracking: Bool { get }     var touchInside: Bool { get }     func beginTrackingWithTouch(_ touch: UITouch, withEvent event: UIEvent) -> Bool     func continueTrackingWithTouch(_ touch: UITouch, withEvent event: UIEvent) -> Bool     func endTrackingWithTouch(_ touch: UITouch, withEvent event: UIEvent)     func cancelTrackingWithEvent(_ event: UIEvent?)     func addTarget(_ target: AnyObject?, action action: Selector, forControlEvents controlEvents: UIControlEvents)     func removeTarget(_ target: AnyObject?, action action: Selector, forControlEvents controlEvents: UIControlEvents)     func allTargets() -> Set<NSObject>     func allControlEvents() -> UIControlEvents     func actionsForTarget(_ target: AnyObject, forControlEvent controlEvent: UIControlEvents) -> [AnyObject]?     func sendAction(_ action: Selector, to target: AnyObject?, forEvent event: UIEvent?)     func sendActionsForControlEvents(_ controlEvents: UIControlEvents) } ``` |
| To | ``` class UIControl : UIView {     var enabled: Bool     var selected: Bool     var highlighted: Bool     var contentVerticalAlignment: UIControlContentVerticalAlignment     var contentHorizontalAlignment: UIControlContentHorizontalAlignment     var state: UIControlState { get }     var tracking: Bool { get }     var touchInside: Bool { get }     func beginTrackingWithTouch(_ touch: UITouch, withEvent event: UIEvent?) -> Bool     func continueTrackingWithTouch(_ touch: UITouch, withEvent event: UIEvent?) -> Bool     func endTrackingWithTouch(_ touch: UITouch?, withEvent event: UIEvent?)     func cancelTrackingWithEvent(_ event: UIEvent?)     func addTarget(_ target: AnyObject?, action action: Selector, forControlEvents controlEvents: UIControlEvents)     func removeTarget(_ target: AnyObject?, action action: Selector, forControlEvents controlEvents: UIControlEvents)     func allTargets() -> Set<NSObject>     func allControlEvents() -> UIControlEvents     func actionsForTarget(_ target: AnyObject?, forControlEvent controlEvent: UIControlEvents) -> [String]?     func sendAction(_ action: Selector, to target: AnyObject?, forEvent event: UIEvent?)     func sendActionsForControlEvents(_ controlEvents: UIControlEvents) } ``` |

Modified [UIControl.actionsForTarget(_: AnyObject?, forControlEvent: UIControlEvents) -> [String]?](https://developer.apple.com/documentation/uikit/uicontrol/1618251-actionsfortarget)

|  | Declaration |
| --- | --- |
| From | ``` func actionsForTarget(_ target: AnyObject, forControlEvent controlEvent: UIControlEvents) -> [AnyObject]? ``` |
| To | ``` func actionsForTarget(_ target: AnyObject?, forControlEvent controlEvent: UIControlEvents) -> [String]? ``` |

Modified [UIControl.beginTrackingWithTouch(_: UITouch, withEvent: UIEvent?) -> Bool](https://developer.apple.com/documentation/uikit/uicontrol/1618227-begintracking)

|  | Declaration |
| --- | --- |
| From | ``` func beginTrackingWithTouch(_ touch: UITouch, withEvent event: UIEvent) -> Bool ``` |
| To | ``` func beginTrackingWithTouch(_ touch: UITouch, withEvent event: UIEvent?) -> Bool ``` |

Modified [UIControl.continueTrackingWithTouch(_: UITouch, withEvent: UIEvent?) -> Bool](https://developer.apple.com/documentation/uikit/uicontrol/1618216-continuetracking)

|  | Declaration |
| --- | --- |
| From | ``` func continueTrackingWithTouch(_ touch: UITouch, withEvent event: UIEvent) -> Bool ``` |
| To | ``` func continueTrackingWithTouch(_ touch: UITouch, withEvent event: UIEvent?) -> Bool ``` |

Modified [UIControl.endTrackingWithTouch(_: UITouch?, withEvent: UIEvent?)](https://developer.apple.com/documentation/uikit/uicontrol/1618234-endtrackingwithtouch)

|  | Declaration |
| --- | --- |
| From | ``` func endTrackingWithTouch(_ touch: UITouch, withEvent event: UIEvent) ``` |
| To | ``` func endTrackingWithTouch(_ touch: UITouch?, withEvent event: UIEvent?) ``` |

Modified [UIControlContentHorizontalAlignment [enum]](https://developer.apple.com/documentation/uikit/uicontrol/contenthorizontalalignment)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIControlContentVerticalAlignment [enum]](https://developer.apple.com/documentation/uikit/uicontrol/contentverticalalignment)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIControlEvents [struct]](https://developer.apple.com/documentation/uikit/uicontrol/event)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIControlEvents : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var TouchDown: UIControlEvents { get }     static var TouchDownRepeat: UIControlEvents { get }     static var TouchDragInside: UIControlEvents { get }     static var TouchDragOutside: UIControlEvents { get }     static var TouchDragEnter: UIControlEvents { get }     static var TouchDragExit: UIControlEvents { get }     static var TouchUpInside: UIControlEvents { get }     static var TouchUpOutside: UIControlEvents { get }     static var TouchCancel: UIControlEvents { get }     static var ValueChanged: UIControlEvents { get }     static var EditingDidBegin: UIControlEvents { get }     static var EditingChanged: UIControlEvents { get }     static var EditingDidEnd: UIControlEvents { get }     static var EditingDidEndOnExit: UIControlEvents { get }     static var AllTouchEvents: UIControlEvents { get }     static var AllEditingEvents: UIControlEvents { get }     static var ApplicationReserved: UIControlEvents { get }     static var SystemReserved: UIControlEvents { get }     static var AllEvents: UIControlEvents { get } } ``` | RawOptionSetType |
| To | ``` struct UIControlEvents : OptionSetType {     init(rawValue rawValue: UInt)     static var TouchDown: UIControlEvents { get }     static var TouchDownRepeat: UIControlEvents { get }     static var TouchDragInside: UIControlEvents { get }     static var TouchDragOutside: UIControlEvents { get }     static var TouchDragEnter: UIControlEvents { get }     static var TouchDragExit: UIControlEvents { get }     static var TouchUpInside: UIControlEvents { get }     static var TouchUpOutside: UIControlEvents { get }     static var TouchCancel: UIControlEvents { get }     static var ValueChanged: UIControlEvents { get }     static var PrimaryActionTriggered: UIControlEvents { get }     static var EditingDidBegin: UIControlEvents { get }     static var EditingChanged: UIControlEvents { get }     static var EditingDidEnd: UIControlEvents { get }     static var EditingDidEndOnExit: UIControlEvents { get }     static var AllTouchEvents: UIControlEvents { get }     static var AllEditingEvents: UIControlEvents { get }     static var ApplicationReserved: UIControlEvents { get }     static var SystemReserved: UIControlEvents { get }     static var AllEvents: UIControlEvents { get } } ``` | OptionSetType |

Modified [UIControlState [struct]](https://developer.apple.com/documentation/uikit/uicontrolstate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIControlState : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Normal: UIControlState { get }     static var Highlighted: UIControlState { get }     static var Disabled: UIControlState { get }     static var Selected: UIControlState { get }     static var Application: UIControlState { get }     static var Reserved: UIControlState { get } } ``` | RawOptionSetType |
| To | ``` struct UIControlState : OptionSetType {     init(rawValue rawValue: UInt)     static var Normal: UIControlState { get }     static var Highlighted: UIControlState { get }     static var Disabled: UIControlState { get }     static var Selected: UIControlState { get }     static var Application: UIControlState { get }     static var Reserved: UIControlState { get } } ``` | OptionSetType |

Modified [UIDataDetectorTypes [struct]](https://developer.apple.com/documentation/uikit/uidatadetectortypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIDataDetectorTypes : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PhoneNumber: UIDataDetectorTypes { get }     static var Link: UIDataDetectorTypes { get }     static var Address: UIDataDetectorTypes { get }     static var CalendarEvent: UIDataDetectorTypes { get }     static var None: UIDataDetectorTypes { get }     static var All: UIDataDetectorTypes { get } } ``` | RawOptionSetType |
| To | ``` struct UIDataDetectorTypes : OptionSetType {     init(rawValue rawValue: UInt)     static var PhoneNumber: UIDataDetectorTypes { get }     static var Link: UIDataDetectorTypes { get }     static var Address: UIDataDetectorTypes { get }     static var CalendarEvent: UIDataDetectorTypes { get }     static var None: UIDataDetectorTypes { get }     static var All: UIDataDetectorTypes { get } } ``` | OptionSetType |

Modified [UIDataDetectorTypes.Address](https://developer.apple.com/documentation/uikit/uidatadetectortypes/uidatadetectortypeaddress)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [UIDataDetectorTypes.CalendarEvent](https://developer.apple.com/documentation/uikit/uidatadetectortypes/uidatadetectortypecalendarevent)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [UIDataSourceModelAssociation](https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIDataSourceModelAssociation {     func modelIdentifierForElementAtIndexPath(_ idx: NSIndexPath, inView view: UIView) -> String     func indexPathForElementWithModelIdentifier(_ identifier: String, inView view: UIView) -> NSIndexPath? } ``` |
| To | ``` protocol UIDataSourceModelAssociation {     func modelIdentifierForElementAtIndexPath(_ idx: NSIndexPath, inView view: UIView) -> String?     func indexPathForElementWithModelIdentifier(_ identifier: String, inView view: UIView) -> NSIndexPath? } ``` |

Modified [UIDataSourceModelAssociation.indexPathForElementWithModelIdentifier(_: String, inView: UIView) -> NSIndexPath?](https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation/1616850-indexpathforelement)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIDataSourceModelAssociation.modelIdentifierForElementAtIndexPath(_: NSIndexPath, inView: UIView) -> String?](https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation/1616862-modelidentifierforelement)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func modelIdentifierForElementAtIndexPath(_ idx: NSIndexPath, inView view: UIView) -> String ``` | iOS 8.0 |
| To | ``` func modelIdentifierForElementAtIndexPath(_ idx: NSIndexPath, inView view: UIView) -> String? ``` | iOS 2.0 |

Modified [UIDatePicker](https://developer.apple.com/documentation/uikit/uidatepicker)

|  | Declaration |
| --- | --- |
| From | ``` class UIDatePicker : UIControl, NSCoding {     var datePickerMode: UIDatePickerMode     var locale: NSLocale?     @NSCopying var calendar: NSCalendar!     var timeZone: NSTimeZone?     var date: NSDate     var minimumDate: NSDate?     var maximumDate: NSDate?     var countDownDuration: NSTimeInterval     var minuteInterval: Int     func setDate(_ date: NSDate, animated animated: Bool) } ``` |
| To | ``` class UIDatePicker : UIControl {     var datePickerMode: UIDatePickerMode     var locale: NSLocale?     @NSCopying var calendar: NSCalendar!     var timeZone: NSTimeZone?     var date: NSDate     var minimumDate: NSDate?     var maximumDate: NSDate?     var countDownDuration: NSTimeInterval     var minuteInterval: Int     func setDate(_ date: NSDate, animated animated: Bool) } ``` |

Modified [UIDatePickerMode [enum]](https://developer.apple.com/documentation/uikit/uidatepicker/mode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIDevice](https://developer.apple.com/documentation/uikit/uidevice)

|  | Declaration |
| --- | --- |
| From | ``` class UIDevice : NSObject {     class func currentDevice() -> UIDevice     var name: String { get }     var model: String { get }     var localizedModel: String { get }     var systemName: String { get }     var systemVersion: String { get }     var orientation: UIDeviceOrientation { get }     var identifierForVendor: NSUUID! { get }     var generatesDeviceOrientationNotifications: Bool { get }     func beginGeneratingDeviceOrientationNotifications()     func endGeneratingDeviceOrientationNotifications()     var batteryMonitoringEnabled: Bool     var batteryState: UIDeviceBatteryState { get }     var batteryLevel: Float { get }     var proximityMonitoringEnabled: Bool     var proximityState: Bool { get }     var multitaskingSupported: Bool { get }     var userInterfaceIdiom: UIUserInterfaceIdiom { get }     func playInputClick() } ``` |
| To | ``` class UIDevice : NSObject {     class func currentDevice() -> UIDevice     var name: String { get }     var model: String { get }     var localizedModel: String { get }     var systemName: String { get }     var systemVersion: String { get }     var orientation: UIDeviceOrientation { get }     var identifierForVendor: NSUUID? { get }     var generatesDeviceOrientationNotifications: Bool { get }     func beginGeneratingDeviceOrientationNotifications()     func endGeneratingDeviceOrientationNotifications()     var batteryMonitoringEnabled: Bool     var batteryState: UIDeviceBatteryState { get }     var batteryLevel: Float { get }     var proximityMonitoringEnabled: Bool     var proximityState: Bool { get }     var multitaskingSupported: Bool { get }     var userInterfaceIdiom: UIUserInterfaceIdiom { get }     func playInputClick() } ``` |

Modified [UIDevice.identifierForVendor](https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor)

|  | Declaration |
| --- | --- |
| From | ``` var identifierForVendor: NSUUID! { get } ``` |
| To | ``` var identifierForVendor: NSUUID? { get } ``` |

Modified [UIDeviceBatteryState [enum]](https://developer.apple.com/documentation/uikit/uidevice/batterystate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIDeviceOrientation [enum]](https://developer.apple.com/documentation/uikit/uideviceorientation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIDictationPhrase](https://developer.apple.com/documentation/uikit/uidictationphrase)

|  | Declaration |
| --- | --- |
| From | ``` class UIDictationPhrase : NSObject {     var text: String! { get }     var alternativeInterpretations: [AnyObject]? { get } } ``` |
| To | ``` class UIDictationPhrase : NSObject {     var text: String { get }     var alternativeInterpretations: [String]? { get } } ``` |

Modified [UIDictationPhrase.alternativeInterpretations](https://developer.apple.com/documentation/uikit/uidictationphrase/1614510-alternativeinterpretations)

|  | Declaration |
| --- | --- |
| From | ``` var alternativeInterpretations: [AnyObject]? { get } ``` |
| To | ``` var alternativeInterpretations: [String]? { get } ``` |

Modified [UIDictationPhrase.text](https://developer.apple.com/documentation/uikit/uidictationphrase/1614456-text)

|  | Declaration |
| --- | --- |
| From | ``` var text: String! { get } ``` |
| To | ``` var text: String { get } ``` |

Modified [UIDocument](https://developer.apple.com/documentation/uikit/uidocument)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIDocument : NSObject, NSFilePresenter, NSObjectProtocol {     init(fileURL url: NSURL)     var fileURL: NSURL { get }     var localizedName: String { get }     var fileType: String { get }     @NSCopying var fileModificationDate: NSDate?     var documentState: UIDocumentState { get }     func openWithCompletionHandler(_ completionHandler: ((Bool) -> Void)?)     func closeWithCompletionHandler(_ completionHandler: ((Bool) -> Void)?)     func loadFromContents(_ contents: AnyObject, ofType typeName: String, error outError: NSErrorPointer) -> Bool     func contentsForType(_ typeName: String, error outError: NSErrorPointer) -> AnyObject?     func disableEditing()     func enableEditing()     var undoManager: NSUndoManager     func hasUnsavedChanges() -> Bool     func updateChangeCount(_ change: UIDocumentChangeKind)     func changeCountTokenForSaveOperation(_ saveOperation: UIDocumentSaveOperation) -> AnyObject     func updateChangeCountWithToken(_ changeCountToken: AnyObject, forSaveOperation saveOperation: UIDocumentSaveOperation)     func saveToURL(_ url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation, completionHandler completionHandler: ((Bool) -> Void)?)     func autosaveWithCompletionHandler(_ completionHandler: ((Bool) -> Void)?)     func savingFileType() -> String!     func fileNameExtensionForType(_ typeName: String, saveOperation saveOperation: UIDocumentSaveOperation) -> String     func writeContents(_ contents: AnyObject, andAttributes additionalFileAttributes: [NSObject : AnyObject]?, safelyToURL url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation, error outError: NSErrorPointer) -> Bool     func writeContents(_ contents: AnyObject, toURL url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation, originalContentsURL originalContentsURL: NSURL?, error outError: NSErrorPointer) -> Bool     func fileAttributesToWriteToURL(_ url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation, error outError: NSErrorPointer) -> [NSObject : AnyObject]?     func readFromURL(_ url: NSURL, error outError: NSErrorPointer) -> Bool     func performAsynchronousFileAccessUsingBlock(_ block: (() -> Void)!)     func handleError(_ error: NSError, userInteractionPermitted userInteractionPermitted: Bool)     func finishedHandlingError(_ error: NSError, recovered recovered: Bool)     func userInteractionNoLongerPermittedForError(_ error: NSError)     func revertToContentsOfURL(_ url: NSURL, completionHandler completionHandler: ((Bool) -> Void)?) } extension UIDocument {     var userActivity: NSUserActivity?     func updateUserActivityState(_ userActivity: NSUserActivity)     func restoreUserActivityState(_ userActivity: NSUserActivity) } ``` | AnyObject, NSFilePresenter, NSObjectProtocol |
| To | ``` class UIDocument : NSObject, NSFilePresenter, NSProgressReporting {     init(fileURL url: NSURL)     var fileURL: NSURL { get }     var localizedName: String { get }     var fileType: String? { get }     @NSCopying var fileModificationDate: NSDate?     var documentState: UIDocumentState { get }     func openWithCompletionHandler(_ completionHandler: ((Bool) -> Void)?)     func closeWithCompletionHandler(_ completionHandler: ((Bool) -> Void)?)     func loadFromContents(_ contents: AnyObject, ofType typeName: String?) throws     func contentsForType(_ typeName: String) throws -> AnyObject     func disableEditing()     func enableEditing()     var undoManager: NSUndoManager!     func hasUnsavedChanges() -> Bool     func updateChangeCount(_ change: UIDocumentChangeKind)     func changeCountTokenForSaveOperation(_ saveOperation: UIDocumentSaveOperation) -> AnyObject     func updateChangeCountWithToken(_ changeCountToken: AnyObject, forSaveOperation saveOperation: UIDocumentSaveOperation)     func saveToURL(_ url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation, completionHandler completionHandler: ((Bool) -> Void)?)     func autosaveWithCompletionHandler(_ completionHandler: ((Bool) -> Void)?)     func savingFileType() -> String?     func fileNameExtensionForType(_ typeName: String?, saveOperation saveOperation: UIDocumentSaveOperation) -> String     func writeContents(_ contents: AnyObject, andAttributes additionalFileAttributes: [NSObject : AnyObject]?, safelyToURL url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation) throws     func writeContents(_ contents: AnyObject, toURL url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation, originalContentsURL originalContentsURL: NSURL?) throws     func fileAttributesToWriteToURL(_ url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation) throws -> [NSObject : AnyObject]     func readFromURL(_ url: NSURL) throws     func performAsynchronousFileAccessUsingBlock(_ block: () -> Void)     func handleError(_ error: NSError, userInteractionPermitted userInteractionPermitted: Bool)     func finishedHandlingError(_ error: NSError, recovered recovered: Bool)     func userInteractionNoLongerPermittedForError(_ error: NSError)     func revertToContentsOfURL(_ url: NSURL, completionHandler completionHandler: ((Bool) -> Void)?) } extension UIDocument {     var userActivity: NSUserActivity?     func updateUserActivityState(_ userActivity: NSUserActivity)     func restoreUserActivityState(_ userActivity: NSUserActivity) } ``` | AnyObject, NSFilePresenter, NSObjectProtocol, NSProgressReporting |

Modified [UIDocument.contentsForType(_: String) throws -> AnyObject](https://developer.apple.com/documentation/uikit/uidocument/1619978-contents)

|  | Declaration |
| --- | --- |
| From | ``` func contentsForType(_ typeName: String, error outError: NSErrorPointer) -> AnyObject? ``` |
| To | ``` func contentsForType(_ typeName: String) throws -> AnyObject ``` |

Modified [UIDocument.fileAttributesToWriteToURL(_: NSURL, forSaveOperation: UIDocumentSaveOperation) throws -> [NSObject : AnyObject]](https://developer.apple.com/documentation/uikit/uidocument/1619947-fileattributestowritetourl)

|  | Declaration |
| --- | --- |
| From | ``` func fileAttributesToWriteToURL(_ url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation, error outError: NSErrorPointer) -> [NSObject : AnyObject]? ``` |
| To | ``` func fileAttributesToWriteToURL(_ url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation) throws -> [NSObject : AnyObject] ``` |

Modified [UIDocument.fileNameExtensionForType(_: String?, saveOperation: UIDocumentSaveOperation) -> String](https://developer.apple.com/documentation/uikit/uidocument/1619969-filenameextension)

|  | Declaration |
| --- | --- |
| From | ``` func fileNameExtensionForType(_ typeName: String, saveOperation saveOperation: UIDocumentSaveOperation) -> String ``` |
| To | ``` func fileNameExtensionForType(_ typeName: String?, saveOperation saveOperation: UIDocumentSaveOperation) -> String ``` |

Modified [UIDocument.fileType](https://developer.apple.com/documentation/uikit/uidocument/1619992-filetype)

|  | Declaration |
| --- | --- |
| From | ``` var fileType: String { get } ``` |
| To | ``` var fileType: String? { get } ``` |

Modified [UIDocument.loadFromContents(_: AnyObject, ofType: String?) throws](https://developer.apple.com/documentation/uikit/uidocument/1619971-loadfromcontents)

|  | Declaration |
| --- | --- |
| From | ``` func loadFromContents(_ contents: AnyObject, ofType typeName: String, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func loadFromContents(_ contents: AnyObject, ofType typeName: String?) throws ``` |

Modified [UIDocument.performAsynchronousFileAccessUsingBlock(_: () -> Void)](https://developer.apple.com/documentation/uikit/uidocument/1619980-performasynchronousfileaccessusi)

|  | Declaration |
| --- | --- |
| From | ``` func performAsynchronousFileAccessUsingBlock(_ block: (() -> Void)!) ``` |
| To | ``` func performAsynchronousFileAccessUsingBlock(_ block: () -> Void) ``` |

Modified [UIDocument.readFromURL(_: NSURL) throws](https://developer.apple.com/documentation/uikit/uidocument/1619967-readfromurl)

|  | Declaration |
| --- | --- |
| From | ``` func readFromURL(_ url: NSURL, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func readFromURL(_ url: NSURL) throws ``` |

Modified [UIDocument.savingFileType() -> String?](https://developer.apple.com/documentation/uikit/uidocument/1619991-savingfiletype)

|  | Declaration |
| --- | --- |
| From | ``` func savingFileType() -> String! ``` |
| To | ``` func savingFileType() -> String? ``` |

Modified [UIDocument.undoManager](https://developer.apple.com/documentation/uikit/uidocument/1619953-undomanager)

|  | Declaration |
| --- | --- |
| From | ``` var undoManager: NSUndoManager ``` |
| To | ``` var undoManager: NSUndoManager! ``` |

Modified [UIDocument.writeContents(_: AnyObject, andAttributes: [NSObject : AnyObject]?, safelyToURL: NSURL, forSaveOperation: UIDocumentSaveOperation) throws](https://developer.apple.com/documentation/uikit/uidocument/1619951-writecontents)

|  | Declaration |
| --- | --- |
| From | ``` func writeContents(_ contents: AnyObject, andAttributes additionalFileAttributes: [NSObject : AnyObject]?, safelyToURL url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func writeContents(_ contents: AnyObject, andAttributes additionalFileAttributes: [NSObject : AnyObject]?, safelyToURL url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation) throws ``` |

Modified [UIDocument.writeContents(_: AnyObject, toURL: NSURL, forSaveOperation: UIDocumentSaveOperation, originalContentsURL: NSURL?) throws](https://developer.apple.com/documentation/uikit/uidocument/1619989-writecontents)

|  | Declaration |
| --- | --- |
| From | ``` func writeContents(_ contents: AnyObject, toURL url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation, originalContentsURL originalContentsURL: NSURL?, error outError: NSErrorPointer) -> Bool ``` |
| To | ``` func writeContents(_ contents: AnyObject, toURL url: NSURL, forSaveOperation saveOperation: UIDocumentSaveOperation, originalContentsURL originalContentsURL: NSURL?) throws ``` |

Modified [UIDocumentChangeKind [enum]](https://developer.apple.com/documentation/uikit/uidocument/changekind)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIDocumentInteractionController](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIDocumentInteractionController : NSObject, UIActionSheetDelegate, NSObjectProtocol {     init(URL url: NSURL) -> UIDocumentInteractionController     class func interactionControllerWithURL(_ url: NSURL) -> UIDocumentInteractionController     unowned(unsafe) var delegate: UIDocumentInteractionControllerDelegate?     var URL: NSURL     var UTI: String?     var name: String!     var icons: [AnyObject] { get }     var annotation: AnyObject?     func presentOptionsMenuFromRect(_ rect: CGRect, inView view: UIView, animated animated: Bool) -> Bool     func presentOptionsMenuFromBarButtonItem(_ item: UIBarButtonItem, animated animated: Bool) -> Bool     func presentPreviewAnimated(_ animated: Bool) -> Bool     func presentOpenInMenuFromRect(_ rect: CGRect, inView view: UIView, animated animated: Bool) -> Bool     func presentOpenInMenuFromBarButtonItem(_ item: UIBarButtonItem, animated animated: Bool) -> Bool     func dismissPreviewAnimated(_ animated: Bool)     func dismissMenuAnimated(_ animated: Bool)     var gestureRecognizers: [AnyObject] { get } } ``` |
| To | ``` class UIDocumentInteractionController : NSObject, UIActionSheetDelegate {      init(URL url: NSURL)     class func interactionControllerWithURL(_ url: NSURL) -> UIDocumentInteractionController     weak var delegate: UIDocumentInteractionControllerDelegate?     var URL: NSURL?     var UTI: String?     var name: String?     var icons: [UIImage] { get }     var annotation: AnyObject?     func presentOptionsMenuFromRect(_ rect: CGRect, inView view: UIView, animated animated: Bool) -> Bool     func presentOptionsMenuFromBarButtonItem(_ item: UIBarButtonItem, animated animated: Bool) -> Bool     func presentPreviewAnimated(_ animated: Bool) -> Bool     func presentOpenInMenuFromRect(_ rect: CGRect, inView view: UIView, animated animated: Bool) -> Bool     func presentOpenInMenuFromBarButtonItem(_ item: UIBarButtonItem, animated animated: Bool) -> Bool     func dismissPreviewAnimated(_ animated: Bool)     func dismissMenuAnimated(_ animated: Bool)     var gestureRecognizers: [UIGestureRecognizer] { get } } ``` |

Modified [UIDocumentInteractionController.delegate](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616812-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UIDocumentInteractionControllerDelegate? ``` |
| To | ``` weak var delegate: UIDocumentInteractionControllerDelegate? ``` |

Modified [UIDocumentInteractionController.gestureRecognizers](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616817-gesturerecognizers)

|  | Declaration |
| --- | --- |
| From | ``` var gestureRecognizers: [AnyObject] { get } ``` |
| To | ``` var gestureRecognizers: [UIGestureRecognizer] { get } ``` |

Modified [UIDocumentInteractionController.icons](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616801-icons)

|  | Declaration |
| --- | --- |
| From | ``` var icons: [AnyObject] { get } ``` |
| To | ``` var icons: [UIImage] { get } ``` |

Modified [UIDocumentInteractionController.init(URL: NSURL)](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616821-interactioncontrollerwithurl)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL) -> UIDocumentInteractionController ``` |
| To | ``` init(URL url: NSURL) ``` |

Modified [UIDocumentInteractionController.name](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616810-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified [UIDocumentInteractionController.URL](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616804-url)

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL ``` |
| To | ``` var URL: NSURL? ``` |

Modified [UIDocumentInteractionControllerDelegate](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIDocumentInteractionControllerDelegate : NSObjectProtocol {     optional func documentInteractionControllerViewControllerForPreview(_ controller: UIDocumentInteractionController) -> UIViewController     optional func documentInteractionControllerRectForPreview(_ controller: UIDocumentInteractionController) -> CGRect     optional func documentInteractionControllerViewForPreview(_ controller: UIDocumentInteractionController) -> UIView?     optional func documentInteractionControllerWillBeginPreview(_ controller: UIDocumentInteractionController)     optional func documentInteractionControllerDidEndPreview(_ controller: UIDocumentInteractionController)     optional func documentInteractionControllerWillPresentOptionsMenu(_ controller: UIDocumentInteractionController)     optional func documentInteractionControllerDidDismissOptionsMenu(_ controller: UIDocumentInteractionController)     optional func documentInteractionControllerWillPresentOpenInMenu(_ controller: UIDocumentInteractionController)     optional func documentInteractionControllerDidDismissOpenInMenu(_ controller: UIDocumentInteractionController)     optional func documentInteractionController(_ controller: UIDocumentInteractionController, willBeginSendingToApplication application: String)     optional func documentInteractionController(_ controller: UIDocumentInteractionController, didEndSendingToApplication application: String)     optional func documentInteractionController(_ controller: UIDocumentInteractionController, canPerformAction action: Selector) -> Bool     optional func documentInteractionController(_ controller: UIDocumentInteractionController, performAction action: Selector) -> Bool } ``` |
| To | ``` protocol UIDocumentInteractionControllerDelegate : NSObjectProtocol {     optional func documentInteractionControllerViewControllerForPreview(_ controller: UIDocumentInteractionController) -> UIViewController     optional func documentInteractionControllerRectForPreview(_ controller: UIDocumentInteractionController) -> CGRect     optional func documentInteractionControllerViewForPreview(_ controller: UIDocumentInteractionController) -> UIView?     optional func documentInteractionControllerWillBeginPreview(_ controller: UIDocumentInteractionController)     optional func documentInteractionControllerDidEndPreview(_ controller: UIDocumentInteractionController)     optional func documentInteractionControllerWillPresentOptionsMenu(_ controller: UIDocumentInteractionController)     optional func documentInteractionControllerDidDismissOptionsMenu(_ controller: UIDocumentInteractionController)     optional func documentInteractionControllerWillPresentOpenInMenu(_ controller: UIDocumentInteractionController)     optional func documentInteractionControllerDidDismissOpenInMenu(_ controller: UIDocumentInteractionController)     optional func documentInteractionController(_ controller: UIDocumentInteractionController, willBeginSendingToApplication application: String?)     optional func documentInteractionController(_ controller: UIDocumentInteractionController, didEndSendingToApplication application: String?)     optional func documentInteractionController(_ controller: UIDocumentInteractionController, canPerformAction action: Selector) -> Bool     optional func documentInteractionController(_ controller: UIDocumentInteractionController, performAction action: Selector) -> Bool } ``` |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionController(_: UIDocumentInteractionController, didEndSendingToApplication: String?)](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616824-documentinteractioncontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func documentInteractionController(_ controller: UIDocumentInteractionController, didEndSendingToApplication application: String) ``` | iOS 8.0 |
| To | ``` optional func documentInteractionController(_ controller: UIDocumentInteractionController, didEndSendingToApplication application: String?) ``` | iOS 3.2 |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionController(_: UIDocumentInteractionController, willBeginSendingToApplication: String?)](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616825-documentinteractioncontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func documentInteractionController(_ controller: UIDocumentInteractionController, willBeginSendingToApplication application: String) ``` | iOS 8.0 |
| To | ``` optional func documentInteractionController(_ controller: UIDocumentInteractionController, willBeginSendingToApplication application: String?) ``` | iOS 3.2 |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionControllerDidDismissOpenInMenu(_: UIDocumentInteractionController)](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616826-documentinteractioncontrollerdid)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionControllerDidDismissOptionsMenu(_: UIDocumentInteractionController)](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616803-documentinteractioncontrollerdid)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionControllerDidEndPreview(_: UIDocumentInteractionController)](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616809-documentinteractioncontrollerdid)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionControllerRectForPreview(_: UIDocumentInteractionController) -> CGRect](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616805-documentinteractioncontrollerrec)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionControllerViewControllerForPreview(_: UIDocumentInteractionController) -> UIViewController](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616799-documentinteractioncontrollervie)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionControllerViewForPreview(_: UIDocumentInteractionController) -> UIView?](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616819-documentinteractioncontrollervie)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionControllerWillBeginPreview(_: UIDocumentInteractionController)](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616806-documentinteractioncontrollerwil)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionControllerWillPresentOpenInMenu(_: UIDocumentInteractionController)](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616818-documentinteractioncontrollerwil)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIDocumentInteractionControllerDelegate.documentInteractionControllerWillPresentOptionsMenu(_: UIDocumentInteractionController)](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616822-documentinteractioncontrollerwil)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIDocumentMenuOrder [enum]](https://developer.apple.com/documentation/uikit/uidocumentmenuorder)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [UIDocumentMenuViewController](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIDocumentMenuViewController : UIViewController {     init!(documentTypes allowedUTIs: [AnyObject], inMode mode: UIDocumentPickerMode)     init!(URL url: NSURL, inMode mode: UIDocumentPickerMode)     func addOptionWithTitle(_ title: String?, image image: UIImage?, order order: UIDocumentMenuOrder, handler handler: (() -> Void)!)     weak var delegate: UIDocumentMenuDelegate? } ``` |
| To | ``` class UIDocumentMenuViewController : UIViewController {     init(documentTypes allowedUTIs: [String], inMode mode: UIDocumentPickerMode)     init(URL url: NSURL, inMode mode: UIDocumentPickerMode)     init?(coder aDecoder: NSCoder)     func addOptionWithTitle(_ title: String, image image: UIImage?, order order: UIDocumentMenuOrder, handler handler: () -> Void)     weak var delegate: UIDocumentMenuDelegate? } ``` |

Modified [UIDocumentMenuViewController.addOptionWithTitle(_: String, image: UIImage?, order: UIDocumentMenuOrder, handler: () -> Void)](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614193-addoptionwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` func addOptionWithTitle(_ title: String?, image image: UIImage?, order order: UIDocumentMenuOrder, handler handler: (() -> Void)!) ``` |
| To | ``` func addOptionWithTitle(_ title: String, image image: UIImage?, order order: UIDocumentMenuOrder, handler handler: () -> Void) ``` |

Modified [UIDocumentMenuViewController.init(documentTypes: [String], inMode: UIDocumentPickerMode)](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614187-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(documentTypes allowedUTIs: [AnyObject], inMode mode: UIDocumentPickerMode) ``` |
| To | ``` init(documentTypes allowedUTIs: [String], inMode mode: UIDocumentPickerMode) ``` |

Modified [UIDocumentMenuViewController.init(URL: NSURL, inMode: UIDocumentPickerMode)](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/1614191-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(URL url: NSURL, inMode mode: UIDocumentPickerMode) ``` |
| To | ``` init(URL url: NSURL, inMode mode: UIDocumentPickerMode) ``` |

Modified [UIDocumentPickerExtensionViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIDocumentPickerExtensionViewController : UIViewController {     func dismissGrantingAccessToURL(_ url: NSURL!)     func prepareForPresentationInMode(_ mode: UIDocumentPickerMode)     var documentPickerMode: UIDocumentPickerMode { get }     @NSCopying var originalURL: NSURL? { get }     var validTypes: [AnyObject]? { get }     var providerIdentifier: String { get }     @NSCopying var documentStorageURL: NSURL! { get } } ``` |
| To | ``` class UIDocumentPickerExtensionViewController : UIViewController {     func dismissGrantingAccessToURL(_ url: NSURL?)     func prepareForPresentationInMode(_ mode: UIDocumentPickerMode)     var documentPickerMode: UIDocumentPickerMode { get }     @NSCopying var originalURL: NSURL? { get }     var validTypes: [String]? { get }     var providerIdentifier: String { get }     @NSCopying var documentStorageURL: NSURL? { get } } ``` |

Modified [UIDocumentPickerExtensionViewController.dismissGrantingAccessToURL(_: NSURL?)](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614391-dismissgrantingaccess)

|  | Declaration |
| --- | --- |
| From | ``` func dismissGrantingAccessToURL(_ url: NSURL!) ``` |
| To | ``` func dismissGrantingAccessToURL(_ url: NSURL?) ``` |

Modified [UIDocumentPickerExtensionViewController.documentStorageURL](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614390-documentstorageurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var documentStorageURL: NSURL! { get } ``` |
| To | ``` @NSCopying var documentStorageURL: NSURL? { get } ``` |

Modified [UIDocumentPickerExtensionViewController.validTypes](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/1614394-validtypes)

|  | Declaration |
| --- | --- |
| From | ``` var validTypes: [AnyObject]? { get } ``` |
| To | ``` var validTypes: [String]? { get } ``` |

Modified [UIDocumentPickerMode [enum]](https://developer.apple.com/documentation/uikit/uidocumentpickermode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [UIDocumentPickerViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIDocumentPickerViewController : UIViewController {     init(documentTypes allowedUTIs: [AnyObject], inMode mode: UIDocumentPickerMode)     init(URL url: NSURL, inMode mode: UIDocumentPickerMode)     weak var delegate: UIDocumentPickerDelegate?     var documentPickerMode: UIDocumentPickerMode { get } } ``` |
| To | ``` class UIDocumentPickerViewController : UIViewController {     init(documentTypes allowedUTIs: [String], inMode mode: UIDocumentPickerMode)     init?(coder aDecoder: NSCoder)     init(URL url: NSURL, inMode mode: UIDocumentPickerMode)     weak var delegate: UIDocumentPickerDelegate?     var documentPickerMode: UIDocumentPickerMode { get } } ``` |

Modified [UIDocumentPickerViewController.init(documentTypes: [String], inMode: UIDocumentPickerMode)](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/1618678-init)

|  | Declaration |
| --- | --- |
| From | ``` init(documentTypes allowedUTIs: [AnyObject], inMode mode: UIDocumentPickerMode) ``` |
| To | ``` init(documentTypes allowedUTIs: [String], inMode mode: UIDocumentPickerMode) ``` |

Modified [UIDocumentSaveOperation [enum]](https://developer.apple.com/documentation/uikit/uidocument/saveoperation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIDocumentState [struct]](https://developer.apple.com/documentation/uikit/uidocumentstate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIDocumentState : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Normal: UIDocumentState { get }     static var Closed: UIDocumentState { get }     static var InConflict: UIDocumentState { get }     static var SavingError: UIDocumentState { get }     static var EditingDisabled: UIDocumentState { get } } ``` | RawOptionSetType |
| To | ``` struct UIDocumentState : OptionSetType {     init(rawValue rawValue: UInt)     static var Normal: UIDocumentState { get }     static var Closed: UIDocumentState { get }     static var InConflict: UIDocumentState { get }     static var SavingError: UIDocumentState { get }     static var EditingDisabled: UIDocumentState { get }     static var ProgressAvailable: UIDocumentState { get } } ``` | OptionSetType |

Modified [UIDynamicAnimator](https://developer.apple.com/documentation/uikit/uidynamicanimator)

|  | Declaration |
| --- | --- |
| From | ``` class UIDynamicAnimator : NSObject {     init(referenceView view: UIView)     func addBehavior(_ behavior: UIDynamicBehavior!)     func removeBehavior(_ behavior: UIDynamicBehavior!)     func removeAllBehaviors()     var referenceView: UIView? { get }     var behaviors: [AnyObject] { get }     func itemsInRect(_ rect: CGRect) -> [AnyObject]     func updateItemUsingCurrentState(_ item: UIDynamicItem)     var running: Bool { get }     func elapsedTime() -> NSTimeInterval     unowned(unsafe) var delegate: UIDynamicAnimatorDelegate? } extension UIDynamicAnimator {     init(collectionViewLayout layout: UICollectionViewLayout)     func layoutAttributesForCellAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes!     func layoutAttributesForSupplementaryViewOfKind(_ kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes!     func layoutAttributesForDecorationViewOfKind(_ decorationViewKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes! } ``` |
| To | ``` class UIDynamicAnimator : NSObject {     init(referenceView view: UIView)     func addBehavior(_ behavior: UIDynamicBehavior)     func removeBehavior(_ behavior: UIDynamicBehavior)     func removeAllBehaviors()     var referenceView: UIView? { get }     var behaviors: [UIDynamicBehavior] { get }     func itemsInRect(_ rect: CGRect) -> [UIDynamicItem]     func updateItemUsingCurrentState(_ item: UIDynamicItem)     var running: Bool { get }     func elapsedTime() -> NSTimeInterval     weak var delegate: UIDynamicAnimatorDelegate? } extension UIDynamicAnimator {     convenience init(collectionViewLayout layout: UICollectionViewLayout)     func layoutAttributesForCellAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func layoutAttributesForSupplementaryViewOfKind(_ kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func layoutAttributesForDecorationViewOfKind(_ decorationViewKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes? } ``` |

Modified [UIDynamicAnimator.addBehavior(_: UIDynamicBehavior)](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621189-addbehavior)

|  | Declaration |
| --- | --- |
| From | ``` func addBehavior(_ behavior: UIDynamicBehavior!) ``` |
| To | ``` func addBehavior(_ behavior: UIDynamicBehavior) ``` |

Modified [UIDynamicAnimator.behaviors](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621198-behaviors)

|  | Declaration |
| --- | --- |
| From | ``` var behaviors: [AnyObject] { get } ``` |
| To | ``` var behaviors: [UIDynamicBehavior] { get } ``` |

Modified [UIDynamicAnimator.delegate](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621199-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UIDynamicAnimatorDelegate? ``` |
| To | ``` weak var delegate: UIDynamicAnimatorDelegate? ``` |

Modified [UIDynamicAnimator.init(collectionViewLayout: UICollectionViewLayout)](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621196-initwithcollectionviewlayout)

|  | Declaration |
| --- | --- |
| From | ``` init(collectionViewLayout layout: UICollectionViewLayout) ``` |
| To | ``` convenience init(collectionViewLayout layout: UICollectionViewLayout) ``` |

Modified [UIDynamicAnimator.itemsInRect(_: CGRect) -> [UIDynamicItem]](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621191-items)

|  | Declaration |
| --- | --- |
| From | ``` func itemsInRect(_ rect: CGRect) -> [AnyObject] ``` |
| To | ``` func itemsInRect(_ rect: CGRect) -> [UIDynamicItem] ``` |

Modified [UIDynamicAnimator.layoutAttributesForCellAtIndexPath(_: NSIndexPath) -> UICollectionViewLayoutAttributes?](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621204-layoutattributesforcell)

|  | Declaration |
| --- | --- |
| From | ``` func layoutAttributesForCellAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes! ``` |
| To | ``` func layoutAttributesForCellAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes? ``` |

Modified [UIDynamicAnimator.layoutAttributesForDecorationViewOfKind(_: String, atIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621195-layoutattributesfordecorationvie)

|  | Declaration |
| --- | --- |
| From | ``` func layoutAttributesForDecorationViewOfKind(_ decorationViewKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes! ``` |
| To | ``` func layoutAttributesForDecorationViewOfKind(_ decorationViewKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes? ``` |

Modified [UIDynamicAnimator.layoutAttributesForSupplementaryViewOfKind(_: String, atIndexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621186-layoutattributesforsupplementary)

|  | Declaration |
| --- | --- |
| From | ``` func layoutAttributesForSupplementaryViewOfKind(_ kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes! ``` |
| To | ``` func layoutAttributesForSupplementaryViewOfKind(_ kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes? ``` |

Modified [UIDynamicAnimator.removeBehavior(_: UIDynamicBehavior)](https://developer.apple.com/documentation/uikit/uidynamicanimator/1621201-removebehavior)

|  | Declaration |
| --- | --- |
| From | ``` func removeBehavior(_ behavior: UIDynamicBehavior!) ``` |
| To | ``` func removeBehavior(_ behavior: UIDynamicBehavior) ``` |

Modified [UIDynamicAnimatorDelegate.dynamicAnimatorDidPause(_: UIDynamicAnimator)](https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate/1621193-dynamicanimatordidpause)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [UIDynamicAnimatorDelegate.dynamicAnimatorWillResume(_: UIDynamicAnimator)](https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate/1621188-dynamicanimatorwillresume)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [UIDynamicBehavior](https://developer.apple.com/documentation/uikit/uidynamicbehavior)

|  | Declaration |
| --- | --- |
| From | ``` class UIDynamicBehavior : NSObject {     func addChildBehavior(_ behavior: UIDynamicBehavior!)     func removeChildBehavior(_ behavior: UIDynamicBehavior)     var childBehaviors: [AnyObject] { get }     var action: (() -> Void)!     func willMoveToAnimator(_ dynamicAnimator: UIDynamicAnimator?)     var dynamicAnimator: UIDynamicAnimator? { get } } ``` |
| To | ``` class UIDynamicBehavior : NSObject {     func addChildBehavior(_ behavior: UIDynamicBehavior)     func removeChildBehavior(_ behavior: UIDynamicBehavior)     var childBehaviors: [UIDynamicBehavior] { get }     var action: (() -> Void)?     func willMoveToAnimator(_ dynamicAnimator: UIDynamicAnimator?)     var dynamicAnimator: UIDynamicAnimator? { get } } ``` |

Modified [UIDynamicBehavior.action](https://developer.apple.com/documentation/uikit/uidynamicbehavior/1618499-action)

|  | Declaration |
| --- | --- |
| From | ``` var action: (() -> Void)! ``` |
| To | ``` var action: (() -> Void)? ``` |

Modified [UIDynamicBehavior.addChildBehavior(_: UIDynamicBehavior)](https://developer.apple.com/documentation/uikit/uidynamicbehavior/1618496-addchildbehavior)

|  | Declaration |
| --- | --- |
| From | ``` func addChildBehavior(_ behavior: UIDynamicBehavior!) ``` |
| To | ``` func addChildBehavior(_ behavior: UIDynamicBehavior) ``` |

Modified [UIDynamicBehavior.childBehaviors](https://developer.apple.com/documentation/uikit/uidynamicbehavior/1618482-childbehaviors)

|  | Declaration |
| --- | --- |
| From | ``` var childBehaviors: [AnyObject] { get } ``` |
| To | ``` var childBehaviors: [UIDynamicBehavior] { get } ``` |

Modified [UIDynamicItem](https://developer.apple.com/documentation/uikit/uidynamicitem)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIDynamicItem : NSObjectProtocol {     var center: CGPoint { get set }     var bounds: CGRect { get }     var transform: CGAffineTransform { get set } } ``` |
| To | ``` protocol UIDynamicItem : NSObjectProtocol {     var center: CGPoint { get set }     var bounds: CGRect { get }     var transform: CGAffineTransform { get set }     optional var collisionBoundsType: UIDynamicItemCollisionBoundsType { get }     optional var collisionBoundingPath: UIBezierPath { get } } ``` |

Modified [UIDynamicItemBehavior](https://developer.apple.com/documentation/uikit/uidynamicitembehavior)

|  | Declaration |
| --- | --- |
| From | ``` class UIDynamicItemBehavior : UIDynamicBehavior {     init(items items: [AnyObject])     func addItem(_ item: UIDynamicItem)     func removeItem(_ item: UIDynamicItem)     var items: [AnyObject] { get }     var elasticity: CGFloat     var friction: CGFloat     var density: CGFloat     var resistance: CGFloat     var angularResistance: CGFloat     var allowsRotation: Bool     func addLinearVelocity(_ velocity: CGPoint, forItem item: UIDynamicItem)     func linearVelocityForItem(_ item: UIDynamicItem) -> CGPoint     func addAngularVelocity(_ velocity: CGFloat, forItem item: UIDynamicItem)     func angularVelocityForItem(_ item: UIDynamicItem) -> CGFloat } ``` |
| To | ``` class UIDynamicItemBehavior : UIDynamicBehavior {     init(items items: [UIDynamicItem])     func addItem(_ item: UIDynamicItem)     func removeItem(_ item: UIDynamicItem)     var items: [UIDynamicItem] { get }     var elasticity: CGFloat     var friction: CGFloat     var density: CGFloat     var resistance: CGFloat     var angularResistance: CGFloat     var charge: CGFloat     var anchored: Bool     var allowsRotation: Bool     func addLinearVelocity(_ velocity: CGPoint, forItem item: UIDynamicItem)     func linearVelocityForItem(_ item: UIDynamicItem) -> CGPoint     func addAngularVelocity(_ velocity: CGFloat, forItem item: UIDynamicItem)     func angularVelocityForItem(_ item: UIDynamicItem) -> CGFloat } ``` |

Modified [UIDynamicItemBehavior.init(items: [UIDynamicItem])](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624397-initwithitems)

|  | Declaration |
| --- | --- |
| From | ``` init(items items: [AnyObject]) ``` |
| To | ``` init(items items: [UIDynamicItem]) ``` |

Modified [UIDynamicItemBehavior.items](https://developer.apple.com/documentation/uikit/uidynamicitembehavior/1624400-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject] { get } ``` |
| To | ``` var items: [UIDynamicItem] { get } ``` |

Modified [UIEdgeInsets [struct]](https://developer.apple.com/documentation/uikit/uiedgeinsets)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIEdgeInsets {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat     init()     init(top top: CGFloat, left left: CGFloat, bottom bottom: CGFloat, right right: CGFloat) } ``` | -- |
| To | ``` struct UIEdgeInsets {     var top: CGFloat     var left: CGFloat     var bottom: CGFloat     var right: CGFloat     init()     init(top top: CGFloat, left left: CGFloat, bottom bottom: CGFloat, right right: CGFloat) } extension UIEdgeInsets : Equatable { } extension UIEdgeInsets : Equatable { } ``` | Equatable |

Modified [UIEvent](https://developer.apple.com/documentation/uikit/uievent)

|  | Declaration |
| --- | --- |
| From | ``` class UIEvent : NSObject {     var type: UIEventType { get }     var subtype: UIEventSubtype { get }     var timestamp: NSTimeInterval { get }     func allTouches() -> Set<NSObject>?     func touchesForWindow(_ window: UIWindow) -> Set<NSObject>?     func touchesForView(_ view: UIView) -> Set<NSObject>?     func touchesForGestureRecognizer(_ gesture: UIGestureRecognizer) -> Set<NSObject>? } ``` |
| To | ``` class UIEvent : NSObject {     var type: UIEventType { get }     var subtype: UIEventSubtype { get }     var timestamp: NSTimeInterval { get }     func allTouches() -> Set<UITouch>?     func touchesForWindow(_ window: UIWindow) -> Set<UITouch>?     func touchesForView(_ view: UIView) -> Set<UITouch>?     func touchesForGestureRecognizer(_ gesture: UIGestureRecognizer) -> Set<UITouch>?     func coalescedTouchesForTouch(_ touch: UITouch) -> [UITouch]?     func predictedTouchesForTouch(_ touch: UITouch) -> [UITouch]? } ``` |

Modified [UIEvent.allTouches() -> Set<UITouch>?](https://developer.apple.com/documentation/uikit/uievent/1613836-alltouches)

|  | Declaration |
| --- | --- |
| From | ``` func allTouches() -> Set<NSObject>? ``` |
| To | ``` func allTouches() -> Set<UITouch>? ``` |

Modified [UIEvent.touchesForGestureRecognizer(_: UIGestureRecognizer) -> Set<UITouch>?](https://developer.apple.com/documentation/uikit/uievent/1613832-touches)

|  | Declaration |
| --- | --- |
| From | ``` func touchesForGestureRecognizer(_ gesture: UIGestureRecognizer) -> Set<NSObject>? ``` |
| To | ``` func touchesForGestureRecognizer(_ gesture: UIGestureRecognizer) -> Set<UITouch>? ``` |

Modified [UIEvent.touchesForView(_: UIView) -> Set<UITouch>?](https://developer.apple.com/documentation/uikit/uievent/1613812-touches)

|  | Declaration |
| --- | --- |
| From | ``` func touchesForView(_ view: UIView) -> Set<NSObject>? ``` |
| To | ``` func touchesForView(_ view: UIView) -> Set<UITouch>? ``` |

Modified [UIEvent.touchesForWindow(_: UIWindow) -> Set<UITouch>?](https://developer.apple.com/documentation/uikit/uievent/1613794-touchesforwindow)

|  | Declaration |
| --- | --- |
| From | ``` func touchesForWindow(_ window: UIWindow) -> Set<NSObject>? ``` |
| To | ``` func touchesForWindow(_ window: UIWindow) -> Set<UITouch>? ``` |

Modified [UIEventSubtype [enum]](https://developer.apple.com/documentation/uikit/uievent/eventsubtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIEventType [enum]](https://developer.apple.com/documentation/uikit/uieventtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIFont](https://developer.apple.com/documentation/uikit/uifont)

|  | Declaration |
| --- | --- |
| From | ``` class UIFont : NSObject, NSCopying {     class func preferredFontForTextStyle(_ style: String) -> UIFont     init?(name fontName: String, size fontSize: CGFloat) -> UIFont     class func fontWithName(_ fontName: String, size fontSize: CGFloat) -> UIFont?     class func familyNames() -> [AnyObject]     class func fontNamesForFamilyName(_ familyName: String) -> [AnyObject]     class func systemFontOfSize(_ fontSize: CGFloat) -> UIFont     class func boldSystemFontOfSize(_ fontSize: CGFloat) -> UIFont     class func italicSystemFontOfSize(_ fontSize: CGFloat) -> UIFont     class func systemFontOfSize(_ fontSize: CGFloat, weight weight: CGFloat) -> UIFont!     var familyName: String { get }     var fontName: String { get }     var pointSize: CGFloat { get }     var ascender: CGFloat { get }     var descender: CGFloat { get }     var capHeight: CGFloat { get }     var xHeight: CGFloat { get }     var lineHeight: CGFloat { get }     var leading: CGFloat { get }     func fontWithSize(_ fontSize: CGFloat) -> UIFont     init(descriptor descriptor: UIFontDescriptor, size pointSize: CGFloat) -> UIFont     class func fontWithDescriptor(_ descriptor: UIFontDescriptor, size pointSize: CGFloat) -> UIFont     func fontDescriptor() -> UIFontDescriptor } extension UIFont {     class func labelFontSize() -> CGFloat     class func buttonFontSize() -> CGFloat     class func smallSystemFontSize() -> CGFloat     class func systemFontSize() -> CGFloat } ``` |
| To | ``` class UIFont : NSObject, NSCopying {     class func preferredFontForTextStyle(_ style: String) -> UIFont      init?(name fontName: String, size fontSize: CGFloat)     class func fontWithName(_ fontName: String, size fontSize: CGFloat) -> UIFont?     class func familyNames() -> [String]     class func fontNamesForFamilyName(_ familyName: String) -> [String]     class func systemFontOfSize(_ fontSize: CGFloat) -> UIFont     class func boldSystemFontOfSize(_ fontSize: CGFloat) -> UIFont     class func italicSystemFontOfSize(_ fontSize: CGFloat) -> UIFont     class func systemFontOfSize(_ fontSize: CGFloat, weight weight: CGFloat) -> UIFont     class func monospacedDigitSystemFontOfSize(_ fontSize: CGFloat, weight weight: CGFloat) -> UIFont     var familyName: String { get }     var fontName: String { get }     var pointSize: CGFloat { get }     var ascender: CGFloat { get }     var descender: CGFloat { get }     var capHeight: CGFloat { get }     var xHeight: CGFloat { get }     var lineHeight: CGFloat { get }     var leading: CGFloat { get }     func fontWithSize(_ fontSize: CGFloat) -> UIFont      init(descriptor descriptor: UIFontDescriptor, size pointSize: CGFloat)     class func fontWithDescriptor(_ descriptor: UIFontDescriptor, size pointSize: CGFloat) -> UIFont     func fontDescriptor() -> UIFontDescriptor } extension UIFont {     class func labelFontSize() -> CGFloat     class func buttonFontSize() -> CGFloat     class func smallSystemFontSize() -> CGFloat     class func systemFontSize() -> CGFloat } ``` |

Modified [UIFont.familyNames() -> [String] [class]](https://developer.apple.com/documentation/uikit/uifont/1619040-familynames)

|  | Declaration |
| --- | --- |
| From | ``` class func familyNames() -> [AnyObject] ``` |
| To | ``` class func familyNames() -> [String] ``` |

Modified [UIFont.fontNamesForFamilyName(_: String) -> [String] [class]](https://developer.apple.com/documentation/uikit/uifont/1619023-fontnamesforfamilyname)

|  | Declaration |
| --- | --- |
| From | ``` class func fontNamesForFamilyName(_ familyName: String) -> [AnyObject] ``` |
| To | ``` class func fontNamesForFamilyName(_ familyName: String) -> [String] ``` |

Modified [UIFont.init(descriptor: UIFontDescriptor, size: CGFloat)](https://developer.apple.com/documentation/uikit/uifont/1619025-init)

|  | Declaration |
| --- | --- |
| From | ``` init(descriptor descriptor: UIFontDescriptor, size pointSize: CGFloat) -> UIFont ``` |
| To | ``` init(descriptor descriptor: UIFontDescriptor, size pointSize: CGFloat) ``` |

Modified [UIFont.init(name: String, size: CGFloat)](https://developer.apple.com/documentation/uikit/uifont/1619041-fontwithname)

|  | Declaration |
| --- | --- |
| From | ``` init?(name fontName: String, size fontSize: CGFloat) -> UIFont ``` |
| To | ``` init?(name fontName: String, size fontSize: CGFloat) ``` |

Modified [UIFont.systemFontOfSize(_: CGFloat, weight: CGFloat) -> UIFont [class]](https://developer.apple.com/documentation/uikit/uifont/1619027-systemfontofsize)

|  | Declaration |
| --- | --- |
| From | ``` class func systemFontOfSize(_ fontSize: CGFloat, weight weight: CGFloat) -> UIFont! ``` |
| To | ``` class func systemFontOfSize(_ fontSize: CGFloat, weight weight: CGFloat) -> UIFont ``` |

Modified [UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIFontDescriptor : NSObject, NSCopying, NSCoding {     var postscriptName: String { get }     var pointSize: CGFloat { get }     var matrix: CGAffineTransform { get }     var symbolicTraits: UIFontDescriptorSymbolicTraits { get }     func objectForKey(_ anAttribute: String) -> AnyObject!     func fontAttributes() -> [NSObject : AnyObject]     func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<NSObject>?) -> [AnyObject]     init!(fontAttributes attributes: [NSObject : AnyObject]!) -> UIFontDescriptor     class func fontDescriptorWithFontAttributes(_ attributes: [NSObject : AnyObject]!) -> UIFontDescriptor!     init(name fontName: String, size size: CGFloat) -> UIFontDescriptor     class func fontDescriptorWithName(_ fontName: String, size size: CGFloat) -> UIFontDescriptor     init(name fontName: String, matrix matrix: CGAffineTransform) -> UIFontDescriptor     class func fontDescriptorWithName(_ fontName: String, matrix matrix: CGAffineTransform) -> UIFontDescriptor     class func preferredFontDescriptorWithTextStyle(_ style: String) -> UIFontDescriptor     init!(fontAttributes attributes: [NSObject : AnyObject]?)     func fontDescriptorByAddingAttributes(_ attributes: [NSObject : AnyObject]) -> UIFontDescriptor     func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor?     func fontDescriptorWithSize(_ newPointSize: CGFloat) -> UIFontDescriptor     func fontDescriptorWithMatrix(_ matrix: CGAffineTransform) -> UIFontDescriptor     func fontDescriptorWithFace(_ newFace: String) -> UIFontDescriptor     func fontDescriptorWithFamily(_ newFamily: String) -> UIFontDescriptor } ``` | AnyObject, NSCoding, NSCopying |
| To | ``` class UIFontDescriptor : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init()     init?(coder aDecoder: NSCoder)     var postscriptName: String { get }     var pointSize: CGFloat { get }     var matrix: CGAffineTransform { get }     var symbolicTraits: UIFontDescriptorSymbolicTraits { get }     func objectForKey(_ anAttribute: String) -> AnyObject?     func fontAttributes() -> [String : AnyObject]     func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<String>?) -> [UIFontDescriptor]      init(fontAttributes attributes: [String : AnyObject])     class func fontDescriptorWithFontAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor      init(name fontName: String, size size: CGFloat)     class func fontDescriptorWithName(_ fontName: String, size size: CGFloat) -> UIFontDescriptor      init(name fontName: String, matrix matrix: CGAffineTransform)     class func fontDescriptorWithName(_ fontName: String, matrix matrix: CGAffineTransform) -> UIFontDescriptor     class func preferredFontDescriptorWithTextStyle(_ style: String) -> UIFontDescriptor     init(fontAttributes attributes: [String : AnyObject])     func fontDescriptorByAddingAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor     func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor     func fontDescriptorWithSize(_ newPointSize: CGFloat) -> UIFontDescriptor     func fontDescriptorWithMatrix(_ matrix: CGAffineTransform) -> UIFontDescriptor     func fontDescriptorWithFace(_ newFace: String) -> UIFontDescriptor     func fontDescriptorWithFamily(_ newFamily: String) -> UIFontDescriptor } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |

Modified [UIFontDescriptor.fontAttributes() -> [String : AnyObject]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616698-fontattributes)

|  | Declaration |
| --- | --- |
| From | ``` func fontAttributes() -> [NSObject : AnyObject] ``` |
| To | ``` func fontAttributes() -> [String : AnyObject] ``` |

Modified [UIFontDescriptor.fontDescriptorByAddingAttributes(_: [String : AnyObject]) -> UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616666-fontdescriptorbyaddingattributes)

|  | Declaration |
| --- | --- |
| From | ``` func fontDescriptorByAddingAttributes(_ attributes: [NSObject : AnyObject]) -> UIFontDescriptor ``` |
| To | ``` func fontDescriptorByAddingAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor ``` |

Modified [UIFontDescriptor.fontDescriptorWithSymbolicTraits(_: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616665-fontdescriptorwithsymbolictraits)

|  | Declaration |
| --- | --- |
| From | ``` func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor? ``` |
| To | ``` func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor ``` |

Modified [UIFontDescriptor.init(fontAttributes: [String : AnyObject])](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616679-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(fontAttributes attributes: [NSObject : AnyObject]?) ``` |
| To | ``` init(fontAttributes attributes: [String : AnyObject]) ``` |

Modified [UIFontDescriptor.init(name: String, matrix: CGAffineTransform)](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616670-fontdescriptorwithname)

|  | Declaration |
| --- | --- |
| From | ``` init(name fontName: String, matrix matrix: CGAffineTransform) -> UIFontDescriptor ``` |
| To | ``` init(name fontName: String, matrix matrix: CGAffineTransform) ``` |

Modified [UIFontDescriptor.init(name: String, size: CGFloat)](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616674-init)

|  | Declaration |
| --- | --- |
| From | ``` init(name fontName: String, size size: CGFloat) -> UIFontDescriptor ``` |
| To | ``` init(name fontName: String, size size: CGFloat) ``` |

Modified [UIFontDescriptor.matchingFontDescriptorsWithMandatoryKeys(_: Set<String>?) -> [UIFontDescriptor]](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616699-matchingfontdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<NSObject>?) -> [AnyObject] ``` |
| To | ``` func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<String>?) -> [UIFontDescriptor] ``` |

Modified [UIFontDescriptor.objectForKey(_: String) -> AnyObject?](https://developer.apple.com/documentation/uikit/uifontdescriptor/1616733-object)

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ anAttribute: String) -> AnyObject! ``` |
| To | ``` func objectForKey(_ anAttribute: String) -> AnyObject? ``` |

Modified [UIFontDescriptorSymbolicTraits [struct]](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIFontDescriptorSymbolicTraits : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var TraitItalic: UIFontDescriptorSymbolicTraits { get }     static var TraitBold: UIFontDescriptorSymbolicTraits { get }     static var TraitExpanded: UIFontDescriptorSymbolicTraits { get }     static var TraitCondensed: UIFontDescriptorSymbolicTraits { get }     static var TraitMonoSpace: UIFontDescriptorSymbolicTraits { get }     static var TraitVertical: UIFontDescriptorSymbolicTraits { get }     static var TraitUIOptimized: UIFontDescriptorSymbolicTraits { get }     static var TraitTightLeading: UIFontDescriptorSymbolicTraits { get }     static var TraitLooseLeading: UIFontDescriptorSymbolicTraits { get }     static var ClassMask: UIFontDescriptorSymbolicTraits { get }     static var ClassUnknown: UIFontDescriptorSymbolicTraits { get }     static var ClassOldStyleSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassTransitionalSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassModernSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassClarendonSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassSlabSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassFreeformSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassSansSerif: UIFontDescriptorSymbolicTraits { get }     static var ClassOrnamentals: UIFontDescriptorSymbolicTraits { get }     static var ClassScripts: UIFontDescriptorSymbolicTraits { get }     static var ClassSymbolic: UIFontDescriptorSymbolicTraits { get } } ``` | RawOptionSetType |
| To | ``` struct UIFontDescriptorSymbolicTraits : OptionSetType {     init(rawValue rawValue: UInt32)     static var TraitItalic: UIFontDescriptorSymbolicTraits { get }     static var TraitBold: UIFontDescriptorSymbolicTraits { get }     static var TraitExpanded: UIFontDescriptorSymbolicTraits { get }     static var TraitCondensed: UIFontDescriptorSymbolicTraits { get }     static var TraitMonoSpace: UIFontDescriptorSymbolicTraits { get }     static var TraitVertical: UIFontDescriptorSymbolicTraits { get }     static var TraitUIOptimized: UIFontDescriptorSymbolicTraits { get }     static var TraitTightLeading: UIFontDescriptorSymbolicTraits { get }     static var TraitLooseLeading: UIFontDescriptorSymbolicTraits { get }     static var ClassMask: UIFontDescriptorSymbolicTraits { get }     static var ClassUnknown: UIFontDescriptorSymbolicTraits { get }     static var ClassOldStyleSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassTransitionalSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassModernSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassClarendonSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassSlabSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassFreeformSerifs: UIFontDescriptorSymbolicTraits { get }     static var ClassSansSerif: UIFontDescriptorSymbolicTraits { get }     static var ClassOrnamentals: UIFontDescriptorSymbolicTraits { get }     static var ClassScripts: UIFontDescriptorSymbolicTraits { get }     static var ClassSymbolic: UIFontDescriptorSymbolicTraits { get } } ``` | OptionSetType |

Modified [UIGestureRecognizer](https://developer.apple.com/documentation/uikit/uigesturerecognizer)

|  | Declaration |
| --- | --- |
| From | ``` class UIGestureRecognizer : NSObject {     init(target target: AnyObject, action action: Selector)     func addTarget(_ target: AnyObject, action action: Selector)     func removeTarget(_ target: AnyObject?, action action: Selector)     var state: UIGestureRecognizerState { get }     unowned(unsafe) var delegate: UIGestureRecognizerDelegate?     var enabled: Bool     var view: UIView? { get }     var cancelsTouchesInView: Bool     var delaysTouchesBegan: Bool     var delaysTouchesEnded: Bool     func requireGestureRecognizerToFail(_ otherGestureRecognizer: UIGestureRecognizer)     func locationInView(_ view: UIView?) -> CGPoint     func numberOfTouches() -> Int     func locationOfTouch(_ touchIndex: Int, inView view: UIView?) -> CGPoint } ``` |
| To | ``` class UIGestureRecognizer : NSObject {     init(target target: AnyObject?, action action: Selector)     func addTarget(_ target: AnyObject, action action: Selector)     func removeTarget(_ target: AnyObject?, action action: Selector)     var state: UIGestureRecognizerState { get }     weak var delegate: UIGestureRecognizerDelegate?     var enabled: Bool     var view: UIView? { get }     var cancelsTouchesInView: Bool     var delaysTouchesBegan: Bool     var delaysTouchesEnded: Bool     func requireGestureRecognizerToFail(_ otherGestureRecognizer: UIGestureRecognizer)     func locationInView(_ view: UIView?) -> CGPoint     func numberOfTouches() -> Int     func locationOfTouch(_ touchIndex: Int, inView view: UIView?) -> CGPoint } ``` |

Modified [UIGestureRecognizer.delegate](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624207-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UIGestureRecognizerDelegate? ``` |
| To | ``` weak var delegate: UIGestureRecognizerDelegate? ``` |

Modified [UIGestureRecognizer.init(target: AnyObject?, action: Selector)](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624211-initwithtarget)

|  | Declaration |
| --- | --- |
| From | ``` init(target target: AnyObject, action action: Selector) ``` |
| To | ``` init(target target: AnyObject?, action action: Selector) ``` |

Modified [UIGestureRecognizerDelegate.gestureRecognizer(_: UIGestureRecognizer, shouldReceiveTouch: UITouch) -> Bool](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624214-gesturerecognizer)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIGestureRecognizerDelegate.gestureRecognizer(_: UIGestureRecognizer, shouldRecognizeSimultaneouslyWithGestureRecognizer: UIGestureRecognizer) -> Bool](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624208-gesturerecognizer)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIGestureRecognizerDelegate.gestureRecognizerShouldBegin(_: UIGestureRecognizer) -> Bool](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624213-gesturerecognizershouldbegin)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIGestureRecognizerState [enum]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum UIGestureRecognizerState : Int {     case Possible     case Began     case Changed     case Ended     case Cancelled     case Failed } ``` | -- |
| To | ``` enum UIGestureRecognizerState : Int {     case Possible     case Began     case Changed     case Ended     case Cancelled     case Failed     static var Recognized: UIGestureRecognizerState { get } } ``` | Int |

Modified [UIGravityBehavior](https://developer.apple.com/documentation/uikit/uigravitybehavior)

|  | Declaration |
| --- | --- |
| From | ``` class UIGravityBehavior : UIDynamicBehavior {     init(items items: [AnyObject])     func addItem(_ item: UIDynamicItem)     func removeItem(_ item: UIDynamicItem)     var items: [AnyObject] { get }     var gravityDirection: CGVector     var angle: CGFloat     var magnitude: CGFloat     func setAngle(_ angle: CGFloat, magnitude magnitude: CGFloat) } ``` |
| To | ``` class UIGravityBehavior : UIDynamicBehavior {     init(items items: [UIDynamicItem])     func addItem(_ item: UIDynamicItem)     func removeItem(_ item: UIDynamicItem)     var items: [UIDynamicItem] { get }     var gravityDirection: CGVector     var angle: CGFloat     var magnitude: CGFloat     func setAngle(_ angle: CGFloat, magnitude magnitude: CGFloat) } ``` |

Modified [UIGravityBehavior.init(items: [UIDynamicItem])](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620416-init)

|  | Declaration |
| --- | --- |
| From | ``` init(items items: [AnyObject]) ``` |
| To | ``` init(items items: [UIDynamicItem]) ``` |

Modified [UIGravityBehavior.items](https://developer.apple.com/documentation/uikit/uigravitybehavior/1620420-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject] { get } ``` |
| To | ``` var items: [UIDynamicItem] { get } ``` |

Modified [UIGuidedAccessRestrictionDelegate](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIGuidedAccessRestrictionDelegate : NSObjectProtocol {     func guidedAccessRestrictionIdentifiers() -> [AnyObject]     func guidedAccessRestrictionWithIdentifier(_ restrictionIdentifier: String, didChangeState newRestrictionState: UIGuidedAccessRestrictionState)     func textForGuidedAccessRestrictionWithIdentifier(_ restrictionIdentifier: String) -> String!     optional func detailTextForGuidedAccessRestrictionWithIdentifier(_ restrictionIdentifier: String) -> String! } ``` |
| To | ``` protocol UIGuidedAccessRestrictionDelegate : NSObjectProtocol {     func guidedAccessRestrictionIdentifiers() -> [String]?     func guidedAccessRestrictionWithIdentifier(_ restrictionIdentifier: String, didChangeState newRestrictionState: UIGuidedAccessRestrictionState)     func textForGuidedAccessRestrictionWithIdentifier(_ restrictionIdentifier: String) -> String?     optional func detailTextForGuidedAccessRestrictionWithIdentifier(_ restrictionIdentifier: String) -> String? } ``` |

Modified [UIGuidedAccessRestrictionDelegate.detailTextForGuidedAccessRestrictionWithIdentifier(_: String) -> String?](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/1621158-detailtextforguidedaccessrestric)

|  | Declaration |
| --- | --- |
| From | ``` optional func detailTextForGuidedAccessRestrictionWithIdentifier(_ restrictionIdentifier: String) -> String! ``` |
| To | ``` optional func detailTextForGuidedAccessRestrictionWithIdentifier(_ restrictionIdentifier: String) -> String? ``` |

Modified [UIGuidedAccessRestrictionDelegate.guidedAccessRestrictionIdentifiers() -> [String]?](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/1621160-guidedaccessrestrictionidentifie)

|  | Declaration |
| --- | --- |
| From | ``` func guidedAccessRestrictionIdentifiers() -> [AnyObject] ``` |
| To | ``` func guidedAccessRestrictionIdentifiers() -> [String]? ``` |

Modified [UIGuidedAccessRestrictionDelegate.textForGuidedAccessRestrictionWithIdentifier(_: String) -> String?](https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/1621161-textforguidedaccessrestrictionwi)

|  | Declaration |
| --- | --- |
| From | ``` func textForGuidedAccessRestrictionWithIdentifier(_ restrictionIdentifier: String) -> String! ``` |
| To | ``` func textForGuidedAccessRestrictionWithIdentifier(_ restrictionIdentifier: String) -> String? ``` |

Modified [UIGuidedAccessRestrictionState [enum]](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIImage](https://developer.apple.com/documentation/uikit/uiimage)

|  | Declaration |
| --- | --- |
| From | ``` class UIImage : NSObject, NSSecureCoding, NSCoding {     init?(named name: String) -> UIImage     class func imageNamed(_ name: String) -> UIImage?     init?(named name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?) -> UIImage     class func imageNamed(_ name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?) -> UIImage?     init?(contentsOfFile path: String) -> UIImage     class func imageWithContentsOfFile(_ path: String) -> UIImage?     init?(data data: NSData) -> UIImage     class func imageWithData(_ data: NSData) -> UIImage?     init?(data data: NSData, scale scale: CGFloat) -> UIImage     class func imageWithData(_ data: NSData, scale scale: CGFloat) -> UIImage?     init!(CGImage cgImage: CGImage!) -> UIImage     class func imageWithCGImage(_ cgImage: CGImage!) -> UIImage!     init!(CGImage cgImage: CGImage!, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     class func imageWithCGImage(_ cgImage: CGImage!, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage!     init?(CIImage ciImage: CIImage) -> UIImage     class func imageWithCIImage(_ ciImage: CIImage) -> UIImage?     init?(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     class func imageWithCIImage(_ ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage?     init?(contentsOfFile path: String)     init?(data data: NSData)     init?(data data: NSData, scale scale: CGFloat)     init?(CGImage cgImage: CGImage!)     init?(CGImage cgImage: CGImage!, scale scale: CGFloat, orientation orientation: UIImageOrientation)     init?(CIImage ciImage: CIImage)     init?(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     var size: CGSize { get }     var CGImage: CGImage! { get }     var CIImage: CIImage? { get }     var imageOrientation: UIImageOrientation { get }     var scale: CGFloat { get }     class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage!     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage!     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage!     class func animatedImageWithImages(_ images: [AnyObject], duration duration: NSTimeInterval) -> UIImage!     var images: [AnyObject]? { get }     var duration: NSTimeInterval { get }     func drawAtPoint(_ point: CGPoint)     func drawAtPoint(_ point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawInRect(_ rect: CGRect)     func drawInRect(_ rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawAsPatternInRect(_ rect: CGRect)     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets) -> UIImage     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage     var capInsets: UIEdgeInsets { get }     var resizingMode: UIImageResizingMode { get }     func imageWithAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage     var alignmentRectInsets: UIEdgeInsets { get }     func imageWithRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage     var renderingMode: UIImageRenderingMode { get }     var traitCollection: UITraitCollection { get }     var imageAsset: UIImageAsset! { get } } extension UIImage : UIAccessibilityIdentification, NSObjectProtocol { } extension UIImage {     func stretchableImageWithLeftCapWidth(_ leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get } } ``` |
| To | ``` class UIImage : NSObject, NSSecureCoding, NSCoding {      init?(named name: String)     class func imageNamed(_ name: String) -> UIImage?      init?(named name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?)     class func imageNamed(_ name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?) -> UIImage?      init?(contentsOfFile path: String)     class func imageWithContentsOfFile(_ path: String) -> UIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> UIImage?      init?(data data: NSData, scale scale: CGFloat)     class func imageWithData(_ data: NSData, scale scale: CGFloat) -> UIImage?      init(CGImage cgImage: CGImage)     class func imageWithCGImage(_ cgImage: CGImage) -> UIImage      init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCGImage(_ cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage      init(CIImage ciImage: CIImage)     class func imageWithCIImage(_ ciImage: CIImage) -> UIImage      init(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCIImage(_ ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     init?(contentsOfFile path: String)     init?(data data: NSData)     init?(data data: NSData, scale scale: CGFloat)     init(CGImage cgImage: CGImage)     init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     init(CIImage ciImage: CIImage)     init(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     var size: CGSize { get }     var CGImage: CGImage? { get }     var CIImage: CIImage? { get }     var imageOrientation: UIImageOrientation { get }     var scale: CGFloat { get }     class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage?     class func animatedImageWithImages(_ images: [UIImage], duration duration: NSTimeInterval) -> UIImage?     var images: [UIImage]? { get }     var duration: NSTimeInterval { get }     func drawAtPoint(_ point: CGPoint)     func drawAtPoint(_ point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawInRect(_ rect: CGRect)     func drawInRect(_ rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawAsPatternInRect(_ rect: CGRect)     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets) -> UIImage     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage     var capInsets: UIEdgeInsets { get }     var resizingMode: UIImageResizingMode { get }     func imageWithAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage     var alignmentRectInsets: UIEdgeInsets { get }     func imageWithRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage     var renderingMode: UIImageRenderingMode { get }     @NSCopying var traitCollection: UITraitCollection { get }     var imageAsset: UIImageAsset? { get }     func imageFlippedForRightToLeftLayoutDirection() -> UIImage     var flipsForRightToLeftLayoutDirection: Bool { get } } extension UIImage : UIAccessibilityIdentification { } extension UIImage {     func stretchableImageWithLeftCapWidth(_ leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get } } ``` |

Modified [UIImage.animatedImageNamed(_: String, duration: NSTimeInterval) -> UIImage? [class]](https://developer.apple.com/documentation/uikit/uiimage/1624094-animatedimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage! ``` |
| To | ``` class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage? ``` |

Modified [UIImage.animatedImageWithImages(_: [UIImage], duration: NSTimeInterval) -> UIImage? [class]](https://developer.apple.com/documentation/uikit/uiimage/1624149-animatedimage)

|  | Declaration |
| --- | --- |
| From | ``` class func animatedImageWithImages(_ images: [AnyObject], duration duration: NSTimeInterval) -> UIImage! ``` |
| To | ``` class func animatedImageWithImages(_ images: [UIImage], duration duration: NSTimeInterval) -> UIImage? ``` |

Modified [UIImage.animatedResizableImageNamed(_: String, capInsets: UIEdgeInsets, duration: NSTimeInterval) -> UIImage? [class]](https://developer.apple.com/documentation/uikit/uiimage/1624143-animatedresizableimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage! ``` |
| To | ``` class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage? ``` |

Modified [UIImage.animatedResizableImageNamed(_: String, capInsets: UIEdgeInsets, resizingMode: UIImageResizingMode, duration: NSTimeInterval) -> UIImage? [class]](https://developer.apple.com/documentation/uikit/uiimage/1624103-animatedresizableimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage! ``` |
| To | ``` class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage? ``` |

Modified [UIImage.CGImage](https://developer.apple.com/documentation/uikit/uiimage/1624147-cgimage)

|  | Declaration |
| --- | --- |
| From | ``` var CGImage: CGImage! { get } ``` |
| To | ``` var CGImage: CGImage? { get } ``` |

Modified [UIImage.imageAsset](https://developer.apple.com/documentation/uikit/uiimage/1624151-imageasset)

|  | Declaration |
| --- | --- |
| From | ``` var imageAsset: UIImageAsset! { get } ``` |
| To | ``` var imageAsset: UIImageAsset? { get } ``` |

Modified [UIImage.images](https://developer.apple.com/documentation/uikit/uiimage/1624117-images)

|  | Declaration |
| --- | --- |
| From | ``` var images: [AnyObject]? { get } ``` |
| To | ``` var images: [UIImage]? { get } ``` |

Modified [UIImage.init(CGImage: CGImage)](https://developer.apple.com/documentation/uikit/uiimage/1624090-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` init?(CGImage cgImage: CGImage!) ``` |
| To | ``` init(CGImage cgImage: CGImage) ``` |

Modified [UIImage.init(CGImage: CGImage, scale: CGFloat, orientation: UIImageOrientation)](https://developer.apple.com/documentation/uikit/uiimage/1624091-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` init?(CGImage cgImage: CGImage!, scale scale: CGFloat, orientation orientation: UIImageOrientation) ``` |
| To | ``` init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) ``` |

Modified [UIImage.init(CIImage: CIImage)](https://developer.apple.com/documentation/uikit/uiimage/1624114-initwithciimage)

|  | Declaration |
| --- | --- |
| From | ``` init?(CIImage ciImage: CIImage) ``` |
| To | ``` init(CIImage ciImage: CIImage) ``` |

Modified [UIImage.init(CIImage: CIImage, scale: CGFloat, orientation: UIImageOrientation)](https://developer.apple.com/documentation/uikit/uiimage/1624150-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) ``` |
| To | ``` init(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) ``` |

Modified [UIImage.init(named: String)](https://developer.apple.com/documentation/uikit/uiimage/1624146-imagenamed)

|  | Declaration |
| --- | --- |
| From | ``` init?(named name: String) -> UIImage ``` |
| To | ``` init?(named name: String) ``` |

Modified [UIImage.init(named: String, inBundle: NSBundle?, compatibleWithTraitCollection: UITraitCollection?)](https://developer.apple.com/documentation/uikit/uiimage/1624154-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(named name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?) -> UIImage ``` |
| To | ``` init?(named name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?) ``` |

Modified [UIImage.traitCollection](https://developer.apple.com/documentation/uikit/uiimage/1624158-traitcollection)

|  | Declaration |
| --- | --- |
| From | ``` var traitCollection: UITraitCollection { get } ``` |
| To | ``` @NSCopying var traitCollection: UITraitCollection { get } ``` |

Modified [UIImageAsset](https://developer.apple.com/documentation/uikit/uiimageasset)

|  | Declaration |
| --- | --- |
| From | ``` class UIImageAsset : NSObject, NSSecureCoding, NSCoding {     func imageWithTraitCollection(_ traitCollection: UITraitCollection) -> UIImage     func registerImage(_ image: UIImage, withTraitCollection traitCollection: UITraitCollection)     func unregisterImageWithTraitCollection(_ traitCollection: UITraitCollection) } ``` |
| To | ``` class UIImageAsset : NSObject, NSSecureCoding, NSCoding {     init()     init?(coder aDecoder: NSCoder)     func imageWithTraitCollection(_ traitCollection: UITraitCollection) -> UIImage     func registerImage(_ image: UIImage, withTraitCollection traitCollection: UITraitCollection)     func unregisterImageWithTraitCollection(_ traitCollection: UITraitCollection) } ``` |

Modified [UIImageOrientation [enum]](https://developer.apple.com/documentation/uikit/uiimageorientation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIImagePickerController : UINavigationController, NSCoding {     class func isSourceTypeAvailable(_ sourceType: UIImagePickerControllerSourceType) -> Bool     class func availableMediaTypesForSourceType(_ sourceType: UIImagePickerControllerSourceType) -> [AnyObject]?     class func isCameraDeviceAvailable(_ cameraDevice: UIImagePickerControllerCameraDevice) -> Bool     class func isFlashAvailableForCameraDevice(_ cameraDevice: UIImagePickerControllerCameraDevice) -> Bool     class func availableCaptureModesForCameraDevice(_ cameraDevice: UIImagePickerControllerCameraDevice) -> [AnyObject]!     unowned(unsafe) var delegate: protocol<UIImagePickerControllerDelegate, UINavigationControllerDelegate>?     var sourceType: UIImagePickerControllerSourceType     var mediaTypes: [AnyObject]     var allowsEditing: Bool     var allowsImageEditing: Bool     var videoMaximumDuration: NSTimeInterval     var videoQuality: UIImagePickerControllerQualityType     var showsCameraControls: Bool     var cameraOverlayView: UIView?     var cameraViewTransform: CGAffineTransform     func takePicture()     func startVideoCapture() -> Bool     func stopVideoCapture()     var cameraCaptureMode: UIImagePickerControllerCameraCaptureMode     var cameraDevice: UIImagePickerControllerCameraDevice     var cameraFlashMode: UIImagePickerControllerCameraFlashMode } ``` |
| To | ``` class UIImagePickerController : UINavigationController {     class func isSourceTypeAvailable(_ sourceType: UIImagePickerControllerSourceType) -> Bool     class func availableMediaTypesForSourceType(_ sourceType: UIImagePickerControllerSourceType) -> [String]?     class func isCameraDeviceAvailable(_ cameraDevice: UIImagePickerControllerCameraDevice) -> Bool     class func isFlashAvailableForCameraDevice(_ cameraDevice: UIImagePickerControllerCameraDevice) -> Bool     class func availableCaptureModesForCameraDevice(_ cameraDevice: UIImagePickerControllerCameraDevice) -> [NSNumber]?     weak var delegate: protocol<UIImagePickerControllerDelegate, UINavigationControllerDelegate>?     var sourceType: UIImagePickerControllerSourceType     var mediaTypes: [String]     var allowsEditing: Bool     var allowsImageEditing: Bool     var videoMaximumDuration: NSTimeInterval     var videoQuality: UIImagePickerControllerQualityType     var showsCameraControls: Bool     var cameraOverlayView: UIView?     var cameraViewTransform: CGAffineTransform     func takePicture()     func startVideoCapture() -> Bool     func stopVideoCapture()     var cameraCaptureMode: UIImagePickerControllerCameraCaptureMode     var cameraDevice: UIImagePickerControllerCameraDevice     var cameraFlashMode: UIImagePickerControllerCameraFlashMode } ``` |

Modified [UIImagePickerController.availableCaptureModesForCameraDevice(_: UIImagePickerControllerCameraDevice) -> [NSNumber]? [class]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619127-availablecapturemodesforcamerade)

|  | Declaration |
| --- | --- |
| From | ``` class func availableCaptureModesForCameraDevice(_ cameraDevice: UIImagePickerControllerCameraDevice) -> [AnyObject]! ``` |
| To | ``` class func availableCaptureModesForCameraDevice(_ cameraDevice: UIImagePickerControllerCameraDevice) -> [NSNumber]? ``` |

Modified [UIImagePickerController.availableMediaTypesForSourceType(_: UIImagePickerControllerSourceType) -> [String]? [class]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619169-availablemediatypesforsourcetype)

|  | Declaration |
| --- | --- |
| From | ``` class func availableMediaTypesForSourceType(_ sourceType: UIImagePickerControllerSourceType) -> [AnyObject]? ``` |
| To | ``` class func availableMediaTypesForSourceType(_ sourceType: UIImagePickerControllerSourceType) -> [String]? ``` |

Modified [UIImagePickerController.delegate](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619145-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: protocol<UIImagePickerControllerDelegate, UINavigationControllerDelegate>? ``` |
| To | ``` weak var delegate: protocol<UIImagePickerControllerDelegate, UINavigationControllerDelegate>? ``` |

Modified [UIImagePickerController.mediaTypes](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/1619173-mediatypes)

|  | Declaration |
| --- | --- |
| From | ``` var mediaTypes: [AnyObject] ``` |
| To | ``` var mediaTypes: [String] ``` |

Modified [UIImagePickerControllerCameraCaptureMode [enum]](https://developer.apple.com/documentation/uikit/uiimagepickercontrollercameracapturemode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIImagePickerControllerCameraDevice [enum]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameradevice)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIImagePickerControllerCameraFlashMode [enum]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameraflashmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIImagePickerControllerDelegate](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIImagePickerControllerDelegate : NSObjectProtocol {     optional func imagePickerController(_ picker: UIImagePickerController, didFinishPickingImage image: UIImage!, editingInfo editingInfo: [NSObject : AnyObject]!)     optional func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [NSObject : AnyObject])     optional func imagePickerControllerDidCancel(_ picker: UIImagePickerController) } ``` |
| To | ``` protocol UIImagePickerControllerDelegate : NSObjectProtocol {     optional func imagePickerController(_ picker: UIImagePickerController, didFinishPickingImage image: UIImage, editingInfo editingInfo: [String : AnyObject]?)     optional func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : AnyObject])     optional func imagePickerControllerDidCancel(_ picker: UIImagePickerController) } ``` |

Modified [UIImagePickerControllerDelegate.imagePickerController(_: UIImagePickerController, didFinishPickingMediaWithInfo: [String : AnyObject])](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619126-imagepickercontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [NSObject : AnyObject]) ``` | iOS 8.0 |
| To | ``` optional func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : AnyObject]) ``` | iOS 2.0 |

Modified [UIImagePickerControllerDelegate.imagePickerControllerDidCancel(_: UIImagePickerController)](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619133-imagepickercontrollerdidcancel)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIImagePickerControllerQualityType [enum]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/qualitytype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIImagePickerControllerQualityType.Type640x480](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/qualitytype/type640x480)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified [UIImagePickerControllerQualityType.TypeIFrame1280x720](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/qualitytype/typeiframe1280x720)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [UIImagePickerControllerQualityType.TypeIFrame960x540](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/qualitytype/typeiframe960x540)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [UIImagePickerControllerSourceType [enum]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIImageRenderingMode [enum]](https://developer.apple.com/documentation/uikit/uiimage/renderingmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIImageResizingMode [enum]](https://developer.apple.com/documentation/uikit/uiimageresizingmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview)

|  | Declaration |
| --- | --- |
| From | ``` class UIImageView : UIView {     init(image image: UIImage!)     init(image image: UIImage!, highlightedImage highlightedImage: UIImage?)     var image: UIImage?     var highlightedImage: UIImage?     var userInteractionEnabled: Bool     var highlighted: Bool     var animationImages: [AnyObject]?     var highlightedAnimationImages: [AnyObject]?     var animationDuration: NSTimeInterval     var animationRepeatCount: Int     var tintColor: UIColor!     func startAnimating()     func stopAnimating()     func isAnimating() -> Bool } ``` |
| To | ``` class UIImageView : UIView {     init(image image: UIImage?)     init(image image: UIImage?, highlightedImage highlightedImage: UIImage?)     var image: UIImage?     var highlightedImage: UIImage?     var userInteractionEnabled: Bool     var highlighted: Bool     var animationImages: [UIImage]?     var highlightedAnimationImages: [UIImage]?     var animationDuration: NSTimeInterval     var animationRepeatCount: Int     var tintColor: UIColor!     func startAnimating()     func stopAnimating()     func isAnimating() -> Bool } ``` |

Modified [UIImageView.animationImages](https://developer.apple.com/documentation/uikit/uiimageview/1621068-animationimages)

|  | Declaration |
| --- | --- |
| From | ``` var animationImages: [AnyObject]? ``` |
| To | ``` var animationImages: [UIImage]? ``` |

Modified [UIImageView.highlightedAnimationImages](https://developer.apple.com/documentation/uikit/uiimageview/1621065-highlightedanimationimages)

|  | Declaration |
| --- | --- |
| From | ``` var highlightedAnimationImages: [AnyObject]? ``` |
| To | ``` var highlightedAnimationImages: [UIImage]? ``` |

Modified [UIImageView.init(image: UIImage?)](https://developer.apple.com/documentation/uikit/uiimageview/1621062-init)

|  | Declaration |
| --- | --- |
| From | ``` init(image image: UIImage!) ``` |
| To | ``` init(image image: UIImage?) ``` |

Modified [UIImageView.init(image: UIImage?, highlightedImage: UIImage?)](https://developer.apple.com/documentation/uikit/uiimageview/1621064-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` init(image image: UIImage!, highlightedImage highlightedImage: UIImage?) ``` |
| To | ``` init(image image: UIImage?, highlightedImage highlightedImage: UIImage?) ``` |

Modified [UIInputView](https://developer.apple.com/documentation/uikit/uiinputview)

|  | Declaration |
| --- | --- |
| From | ``` class UIInputView : UIView {     var inputViewStyle: UIInputViewStyle { get }     init(frame frame: CGRect, inputViewStyle inputViewStyle: UIInputViewStyle) } ``` |
| To | ``` class UIInputView : UIView {     var inputViewStyle: UIInputViewStyle { get }     var allowsSelfSizing: Bool     init(frame frame: CGRect, inputViewStyle inputViewStyle: UIInputViewStyle)     init?(coder aDecoder: NSCoder) } ``` |

Modified [UIInputViewController](https://developer.apple.com/documentation/uikit/uiinputviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIInputViewController : UIViewController, UITextInputDelegate, NSObjectProtocol {     var inputView: UIInputView!     var textDocumentProxy: NSObject { get }     var primaryLanguage: String?     func dismissKeyboard()     func advanceToNextInputMode()     func requestSupplementaryLexiconWithCompletion(_ completionHandler: (UILexicon!) -> Void) } ``` |
| To | ``` class UIInputViewController : UIViewController, UITextInputDelegate {     var inputView: UIInputView?     var textDocumentProxy: UITextDocumentProxy { get }     var primaryLanguage: String?     func dismissKeyboard()     func advanceToNextInputMode()     func requestSupplementaryLexiconWithCompletion(_ completionHandler: (UILexicon) -> Void) } ``` |

Modified [UIInputViewController.inputView](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618192-inputview)

|  | Declaration |
| --- | --- |
| From | ``` var inputView: UIInputView! ``` |
| To | ``` var inputView: UIInputView? ``` |

Modified [UIInputViewController.requestSupplementaryLexiconWithCompletion(_: (UILexicon) -> Void)](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618195-requestsupplementarylexicon)

|  | Declaration |
| --- | --- |
| From | ``` func requestSupplementaryLexiconWithCompletion(_ completionHandler: (UILexicon!) -> Void) ``` |
| To | ``` func requestSupplementaryLexiconWithCompletion(_ completionHandler: (UILexicon) -> Void) ``` |

Modified [UIInputViewController.textDocumentProxy](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/1618193-textdocumentproxy)

|  | Declaration |
| --- | --- |
| From | ``` var textDocumentProxy: NSObject { get } ``` |
| To | ``` var textDocumentProxy: UITextDocumentProxy { get } ``` |

Modified [UIInputViewStyle [enum]](https://developer.apple.com/documentation/uikit/uiinputview/style)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIInterfaceOrientation [enum]](https://developer.apple.com/documentation/uikit/uiinterfaceorientation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIInterfaceOrientationMask [struct]](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIInterfaceOrientationMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Portrait: UIInterfaceOrientationMask { get }     static var LandscapeLeft: UIInterfaceOrientationMask { get }     static var LandscapeRight: UIInterfaceOrientationMask { get }     static var PortraitUpsideDown: UIInterfaceOrientationMask { get }     static var Landscape: UIInterfaceOrientationMask { get }     static var All: UIInterfaceOrientationMask { get }     static var AllButUpsideDown: UIInterfaceOrientationMask { get } } ``` | RawOptionSetType |
| To | ``` struct UIInterfaceOrientationMask : OptionSetType {     init(rawValue rawValue: UInt)     static var Portrait: UIInterfaceOrientationMask { get }     static var LandscapeLeft: UIInterfaceOrientationMask { get }     static var LandscapeRight: UIInterfaceOrientationMask { get }     static var PortraitUpsideDown: UIInterfaceOrientationMask { get }     static var Landscape: UIInterfaceOrientationMask { get }     static var All: UIInterfaceOrientationMask { get }     static var AllButUpsideDown: UIInterfaceOrientationMask { get } } ``` | OptionSetType |

Modified [UIInterpolatingMotionEffect](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect)

|  | Declaration |
| --- | --- |
| From | ``` class UIInterpolatingMotionEffect : UIMotionEffect {     init(keyPath keyPath: String, type type: UIInterpolatingMotionEffectType)     var keyPath: String { get }     var type: UIInterpolatingMotionEffectType { get }     var minimumRelativeValue: AnyObject!     var maximumRelativeValue: AnyObject! } ``` |
| To | ``` class UIInterpolatingMotionEffect : UIMotionEffect {     init(keyPath keyPath: String, type type: UIInterpolatingMotionEffectType)     init?(coder aDecoder: NSCoder)     var keyPath: String { get }     var type: UIInterpolatingMotionEffectType { get }     var minimumRelativeValue: AnyObject?     var maximumRelativeValue: AnyObject? } ``` |

Modified [UIInterpolatingMotionEffect.maximumRelativeValue](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622376-maximumrelativevalue)

|  | Declaration |
| --- | --- |
| From | ``` var maximumRelativeValue: AnyObject! ``` |
| To | ``` var maximumRelativeValue: AnyObject? ``` |

Modified [UIInterpolatingMotionEffect.minimumRelativeValue](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/1622365-minimumrelativevalue)

|  | Declaration |
| --- | --- |
| From | ``` var minimumRelativeValue: AnyObject! ``` |
| To | ``` var minimumRelativeValue: AnyObject? ``` |

Modified [UIInterpolatingMotionEffectType [enum]](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffecttype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIKeyboardAppearance [enum]](https://developer.apple.com/documentation/uikit/uikeyboardappearance)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum UIKeyboardAppearance : Int {     case Default     case Dark     case Light } ``` | -- |
| To | ``` enum UIKeyboardAppearance : Int {     case Default     case Dark     case Light     static var Alert: UIKeyboardAppearance { get } } ``` | Int |

Modified [UIKeyboardType [enum]](https://developer.apple.com/documentation/uikit/uikeyboardtype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum UIKeyboardType : Int {     case Default     case ASCIICapable     case NumbersAndPunctuation     case URL     case NumberPad     case PhonePad     case NamePhonePad     case EmailAddress     case DecimalPad     case Twitter     case WebSearch } ``` | -- |
| To | ``` enum UIKeyboardType : Int {     case Default     case ASCIICapable     case NumbersAndPunctuation     case URL     case NumberPad     case PhonePad     case NamePhonePad     case EmailAddress     case DecimalPad     case Twitter     case WebSearch     static var Alphabet: UIKeyboardType { get } } ``` | Int |

Modified [UIKeyCommand](https://developer.apple.com/documentation/uikit/uikeycommand)

|  | Declaration |
| --- | --- |
| From | ``` class UIKeyCommand : NSObject, NSCopying, NSSecureCoding, NSCoding {     var input: String { get }     var modifierFlags: UIKeyModifierFlags { get }     init(input input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector) -> UIKeyCommand     class func keyCommandWithInput(_ input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector) -> UIKeyCommand } ``` |
| To | ``` class UIKeyCommand : NSObject, NSCopying, NSSecureCoding, NSCoding {     init()     init?(coder aDecoder: NSCoder)     var input: String { get }     var modifierFlags: UIKeyModifierFlags { get }     var discoverabilityTitle: String?      init(input input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector)     class func keyCommandWithInput(_ input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector) -> UIKeyCommand      init(input input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector, discoverabilityTitle discoverabilityTitle: String)     class func keyCommandWithInput(_ input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector, discoverabilityTitle discoverabilityTitle: String) -> UIKeyCommand } ``` |

Modified [UIKeyCommand.init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector)](https://developer.apple.com/documentation/uikit/uikeycommand/1621131-keycommandwithinput)

|  | Declaration |
| --- | --- |
| From | ``` init(input input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector) -> UIKeyCommand ``` |
| To | ``` init(input input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector) ``` |

Modified [UIKeyModifierFlags [struct]](https://developer.apple.com/documentation/uikit/uikeymodifierflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIKeyModifierFlags : RawOptionSetType {     init(_ rawValue: Int)     init(rawValue rawValue: Int)     static var AlphaShift: UIKeyModifierFlags { get }     static var Shift: UIKeyModifierFlags { get }     static var Control: UIKeyModifierFlags { get }     static var Alternate: UIKeyModifierFlags { get }     static var Command: UIKeyModifierFlags { get }     static var NumericPad: UIKeyModifierFlags { get } } ``` | RawOptionSetType |
| To | ``` struct UIKeyModifierFlags : OptionSetType {     init(rawValue rawValue: Int)     static var AlphaShift: UIKeyModifierFlags { get }     static var Shift: UIKeyModifierFlags { get }     static var Control: UIKeyModifierFlags { get }     static var Alternate: UIKeyModifierFlags { get }     static var Command: UIKeyModifierFlags { get }     static var NumericPad: UIKeyModifierFlags { get } } ``` | OptionSetType |

Modified [UILabel](https://developer.apple.com/documentation/uikit/uilabel)

|  | Declaration |
| --- | --- |
| From | ``` class UILabel : UIView, NSCoding {     var text: String?     var font: UIFont!     var textColor: UIColor!     var shadowColor: UIColor?     var shadowOffset: CGSize     var textAlignment: NSTextAlignment     var lineBreakMode: NSLineBreakMode     @NSCopying var attributedText: NSAttributedString!     var highlightedTextColor: UIColor?     var highlighted: Bool     var userInteractionEnabled: Bool     var enabled: Bool     var numberOfLines: Int     var adjustsFontSizeToFitWidth: Bool     var adjustsLetterSpacingToFitWidth: Bool     var minimumFontSize: CGFloat     var baselineAdjustment: UIBaselineAdjustment     var minimumScaleFactor: CGFloat     func textRectForBounds(_ bounds: CGRect, limitedToNumberOfLines numberOfLines: Int) -> CGRect     func drawTextInRect(_ rect: CGRect)     var preferredMaxLayoutWidth: CGFloat } ``` |
| To | ``` class UILabel : UIView {     var text: String?     var font: UIFont!     var textColor: UIColor!     var shadowColor: UIColor?     var shadowOffset: CGSize     var textAlignment: NSTextAlignment     var lineBreakMode: NSLineBreakMode     @NSCopying var attributedText: NSAttributedString?     var highlightedTextColor: UIColor?     var highlighted: Bool     var userInteractionEnabled: Bool     var enabled: Bool     var numberOfLines: Int     var adjustsFontSizeToFitWidth: Bool     var baselineAdjustment: UIBaselineAdjustment     var minimumScaleFactor: CGFloat     var allowsDefaultTighteningForTruncation: Bool     func textRectForBounds(_ bounds: CGRect, limitedToNumberOfLines numberOfLines: Int) -> CGRect     func drawTextInRect(_ rect: CGRect)     var preferredMaxLayoutWidth: CGFloat     var minimumFontSize: CGFloat     var adjustsLetterSpacingToFitWidth: Bool } ``` |

Modified [UILabel.attributedText](https://developer.apple.com/documentation/uikit/uilabel/1620542-attributedtext)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var attributedText: NSAttributedString! ``` |
| To | ``` @NSCopying var attributedText: NSAttributedString? ``` |

Modified [UILayoutConstraintAxis [enum]](https://developer.apple.com/documentation/uikit/uilayoutconstraintaxis)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UILayoutSupport](https://developer.apple.com/documentation/uikit/uilayoutsupport)

|  | Declaration |
| --- | --- |
| From | ``` protocol UILayoutSupport : NSObjectProtocol {     var length: CGFloat { get } } ``` |
| To | ``` protocol UILayoutSupport : NSObjectProtocol {     var length: CGFloat { get }     var topAnchor: NSLayoutYAxisAnchor { get }     var bottomAnchor: NSLayoutYAxisAnchor { get }     var heightAnchor: NSLayoutDimension { get } } ``` |

Modified [UILexicon](https://developer.apple.com/documentation/uikit/uilexicon)

|  | Declaration |
| --- | --- |
| From | ``` class UILexicon : NSObject, NSCopying {     var entries: [AnyObject] { get } } ``` |
| To | ``` class UILexicon : NSObject, NSCopying {     var entries: [UILexiconEntry] { get } } ``` |

Modified [UILexicon.entries](https://developer.apple.com/documentation/uikit/uilexicon/1614133-entries)

|  | Declaration |
| --- | --- |
| From | ``` var entries: [AnyObject] { get } ``` |
| To | ``` var entries: [UILexiconEntry] { get } ``` |

Modified [UILexiconEntry](https://developer.apple.com/documentation/uikit/uilexiconentry)

|  | Declaration |
| --- | --- |
| From | ``` class UILexiconEntry : NSObject, NSCopying {     var documentText: String! { get }     var userInput: String! { get } } ``` |
| To | ``` class UILexiconEntry : NSObject, NSCopying {     var documentText: String { get }     var userInput: String { get } } ``` |

Modified [UILexiconEntry.documentText](https://developer.apple.com/documentation/uikit/uilexiconentry/1614130-documenttext)

|  | Declaration |
| --- | --- |
| From | ``` var documentText: String! { get } ``` |
| To | ``` var documentText: String { get } ``` |

Modified [UILexiconEntry.userInput](https://developer.apple.com/documentation/uikit/uilexiconentry/1614132-userinput)

|  | Declaration |
| --- | --- |
| From | ``` var userInput: String! { get } ``` |
| To | ``` var userInput: String { get } ``` |

Modified [UILocalizedIndexedCollation](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation)

|  | Declaration |
| --- | --- |
| From | ``` class UILocalizedIndexedCollation : NSObject {     class func currentCollation() -> AnyObject!     var sectionTitles: [AnyObject] { get }     var sectionIndexTitles: [AnyObject] { get }     func sectionForSectionIndexTitleAtIndex(_ indexTitleIndex: Int) -> Int     func sectionForObject(_ object: AnyObject, collationStringSelector selector: Selector) -> Int     func sortedArrayFromArray(_ array: [AnyObject], collationStringSelector selector: Selector) -> [AnyObject] } ``` |
| To | ``` class UILocalizedIndexedCollation : NSObject {     class func currentCollation() -> Self     var sectionTitles: [String] { get }     var sectionIndexTitles: [String] { get }     func sectionForSectionIndexTitleAtIndex(_ indexTitleIndex: Int) -> Int     func sectionForObject(_ object: AnyObject, collationStringSelector selector: Selector) -> Int     func sortedArrayFromArray(_ array: [AnyObject], collationStringSelector selector: Selector) -> [AnyObject] } ``` |

Modified [UILocalizedIndexedCollation.currentCollation() -> Self [class]](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/1620384-current)

|  | Declaration |
| --- | --- |
| From | ``` class func currentCollation() -> AnyObject! ``` |
| To | ``` class func currentCollation() -> Self ``` |

Modified [UILocalizedIndexedCollation.sectionIndexTitles](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/1620383-sectionindextitles)

|  | Declaration |
| --- | --- |
| From | ``` var sectionIndexTitles: [AnyObject] { get } ``` |
| To | ``` var sectionIndexTitles: [String] { get } ``` |

Modified [UILocalizedIndexedCollation.sectionTitles](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/1620379-sectiontitles)

|  | Declaration |
| --- | --- |
| From | ``` var sectionTitles: [AnyObject] { get } ``` |
| To | ``` var sectionTitles: [String] { get } ``` |

Modified [UILocalNotification](https://developer.apple.com/documentation/uikit/uilocalnotification)

|  | Declaration |
| --- | --- |
| From | ``` class UILocalNotification : NSObject, NSCopying, NSCoding {     @NSCopying var fireDate: NSDate?     @NSCopying var timeZone: NSTimeZone?     var repeatInterval: NSCalendarUnit     @NSCopying var repeatCalendar: NSCalendar?     @NSCopying var region: CLRegion!     var regionTriggersOnce: Bool     var alertBody: String?     var hasAction: Bool     var alertAction: String?     var alertLaunchImage: String?     var alertTitle: String!     var soundName: String?     var applicationIconBadgeNumber: Int     var userInfo: [NSObject : AnyObject]?     var category: String? } ``` |
| To | ``` class UILocalNotification : NSObject, NSCopying, NSCoding {     init()     init?(coder aDecoder: NSCoder)     @NSCopying var fireDate: NSDate?     @NSCopying var timeZone: NSTimeZone?     var repeatInterval: NSCalendarUnit     @NSCopying var repeatCalendar: NSCalendar?     @NSCopying var region: CLRegion?     var regionTriggersOnce: Bool     var alertBody: String?     var hasAction: Bool     var alertAction: String?     var alertLaunchImage: String?     var alertTitle: String?     var soundName: String?     var applicationIconBadgeNumber: Int     var userInfo: [NSObject : AnyObject]?     var category: String? } ``` |

Modified [UILocalNotification.alertTitle](https://developer.apple.com/documentation/uikit/uilocalnotification/1616647-alerttitle)

|  | Declaration |
| --- | --- |
| From | ``` var alertTitle: String! ``` |
| To | ``` var alertTitle: String? ``` |

Modified [UILocalNotification.region](https://developer.apple.com/documentation/uikit/uilocalnotification/1616644-region)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var region: CLRegion! ``` |
| To | ``` @NSCopying var region: CLRegion? ``` |

Modified [UIManagedDocument](https://developer.apple.com/documentation/uikit/uimanageddocument)

|  | Declaration |
| --- | --- |
| From | ``` class UIManagedDocument : UIDocument {     class func persistentStoreName() -> String     var managedObjectContext: NSManagedObjectContext! { get }     var managedObjectModel: NSManagedObjectModel! { get }     var persistentStoreOptions: [NSObject : AnyObject]?     var modelConfiguration: String?     func configurePersistentStoreCoordinatorForURL(_ storeURL: NSURL!, ofType fileType: String!, modelConfiguration configuration: String?, storeOptions storeOptions: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool     func persistentStoreTypeForFileType(_ fileType: String!) -> String!     func readAdditionalContentFromURL(_ absoluteURL: NSURL, error error: NSErrorPointer) -> Bool     func additionalContentForURL(_ absoluteURL: NSURL, error error: NSErrorPointer) -> AnyObject?     func writeAdditionalContent(_ content: AnyObject!, toURL absoluteURL: NSURL!, originalContentsURL absoluteOriginalContentsURL: NSURL!, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class UIManagedDocument : UIDocument {     class func persistentStoreName() -> String     var managedObjectContext: NSManagedObjectContext { get }     var managedObjectModel: NSManagedObjectModel { get }     var persistentStoreOptions: [NSObject : AnyObject]?     var modelConfiguration: String?     func configurePersistentStoreCoordinatorForURL(_ storeURL: NSURL, ofType fileType: String, modelConfiguration configuration: String?, storeOptions storeOptions: [NSObject : AnyObject]?) throws     func persistentStoreTypeForFileType(_ fileType: String) -> String     func readAdditionalContentFromURL(_ absoluteURL: NSURL) throws     func additionalContentForURL(_ absoluteURL: NSURL) throws -> AnyObject     func writeAdditionalContent(_ content: AnyObject, toURL absoluteURL: NSURL, originalContentsURL absoluteOriginalContentsURL: NSURL?) throws } ``` |

Modified [UIManagedDocument.additionalContentForURL(_: NSURL) throws -> AnyObject](https://developer.apple.com/documentation/uikit/uimanageddocument/1622665-additionalcontentforurl)

|  | Declaration |
| --- | --- |
| From | ``` func additionalContentForURL(_ absoluteURL: NSURL, error error: NSErrorPointer) -> AnyObject? ``` |
| To | ``` func additionalContentForURL(_ absoluteURL: NSURL) throws -> AnyObject ``` |

Modified [UIManagedDocument.configurePersistentStoreCoordinatorForURL(_: NSURL, ofType: String, modelConfiguration: String?, storeOptions: [NSObject : AnyObject]?) throws](https://developer.apple.com/documentation/uikit/uimanageddocument/1622674-configurepersistentstorecoordina)

|  | Declaration |
| --- | --- |
| From | ``` func configurePersistentStoreCoordinatorForURL(_ storeURL: NSURL!, ofType fileType: String!, modelConfiguration configuration: String?, storeOptions storeOptions: [NSObject : AnyObject]?, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func configurePersistentStoreCoordinatorForURL(_ storeURL: NSURL, ofType fileType: String, modelConfiguration configuration: String?, storeOptions storeOptions: [NSObject : AnyObject]?) throws ``` |

Modified [UIManagedDocument.managedObjectContext](https://developer.apple.com/documentation/uikit/uimanageddocument/1622667-managedobjectcontext)

|  | Declaration |
| --- | --- |
| From | ``` var managedObjectContext: NSManagedObjectContext! { get } ``` |
| To | ``` var managedObjectContext: NSManagedObjectContext { get } ``` |

Modified [UIManagedDocument.managedObjectModel](https://developer.apple.com/documentation/uikit/uimanageddocument/1622669-managedobjectmodel)

|  | Declaration |
| --- | --- |
| From | ``` var managedObjectModel: NSManagedObjectModel! { get } ``` |
| To | ``` var managedObjectModel: NSManagedObjectModel { get } ``` |

Modified [UIManagedDocument.persistentStoreTypeForFileType(_: String) -> String](https://developer.apple.com/documentation/uikit/uimanageddocument/1622673-persistentstoretype)

|  | Declaration |
| --- | --- |
| From | ``` func persistentStoreTypeForFileType(_ fileType: String!) -> String! ``` |
| To | ``` func persistentStoreTypeForFileType(_ fileType: String) -> String ``` |

Modified [UIManagedDocument.readAdditionalContentFromURL(_: NSURL) throws](https://developer.apple.com/documentation/uikit/uimanageddocument/1622670-readadditionalcontent)

|  | Declaration |
| --- | --- |
| From | ``` func readAdditionalContentFromURL(_ absoluteURL: NSURL, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func readAdditionalContentFromURL(_ absoluteURL: NSURL) throws ``` |

Modified [UIManagedDocument.writeAdditionalContent(_: AnyObject, toURL: NSURL, originalContentsURL: NSURL?) throws](https://developer.apple.com/documentation/uikit/uimanageddocument/1622668-writeadditionalcontent)

|  | Declaration |
| --- | --- |
| From | ``` func writeAdditionalContent(_ content: AnyObject!, toURL absoluteURL: NSURL!, originalContentsURL absoluteOriginalContentsURL: NSURL!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func writeAdditionalContent(_ content: AnyObject, toURL absoluteURL: NSURL, originalContentsURL absoluteOriginalContentsURL: NSURL?) throws ``` |

Modified [UIMarkupTextPrintFormatter](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter)

|  | Declaration |
| --- | --- |
| From | ``` class UIMarkupTextPrintFormatter : UIPrintFormatter {     init!(markupText markupText: String?)     var markupText: String? } ``` |
| To | ``` class UIMarkupTextPrintFormatter : UIPrintFormatter {     init(markupText markupText: String)     var markupText: String? } ``` |

Modified [UIMarkupTextPrintFormatter.init(markupText: String)](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter/1621845-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(markupText markupText: String?) ``` |
| To | ``` init(markupText markupText: String) ``` |

Modified [UIMenuController](https://developer.apple.com/documentation/uikit/uimenucontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIMenuController : NSObject {     class func sharedMenuController() -> UIMenuController     var menuVisible: Bool     func setMenuVisible(_ menuVisible: Bool, animated animated: Bool)     func setTargetRect(_ targetRect: CGRect, inView targetView: UIView)     var arrowDirection: UIMenuControllerArrowDirection     var menuItems: [AnyObject]?     func update()     var menuFrame: CGRect { get } } ``` |
| To | ``` class UIMenuController : NSObject {     class func sharedMenuController() -> UIMenuController     var menuVisible: Bool     func setMenuVisible(_ menuVisible: Bool, animated animated: Bool)     func setTargetRect(_ targetRect: CGRect, inView targetView: UIView)     var arrowDirection: UIMenuControllerArrowDirection     var menuItems: [UIMenuItem]?     func update()     var menuFrame: CGRect { get } } ``` |

Modified [UIMenuController.menuItems](https://developer.apple.com/documentation/uikit/uimenucontroller/1622811-menuitems)

|  | Declaration |
| --- | --- |
| From | ``` var menuItems: [AnyObject]? ``` |
| To | ``` var menuItems: [UIMenuItem]? ``` |

Modified [UIMenuControllerArrowDirection [enum]](https://developer.apple.com/documentation/uikit/uimenucontroller/arrowdirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIMenuControllerArrowDirection.Down](https://developer.apple.com/documentation/uikit/uimenucontroller/arrowdirection/down)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIMenuControllerArrowDirection.Left](https://developer.apple.com/documentation/uikit/uimenucontroller/arrowdirection/left)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIMenuControllerArrowDirection.Right](https://developer.apple.com/documentation/uikit/uimenucontrollerarrowdirection/uimenucontrollerarrowright)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIMenuControllerArrowDirection.Up](https://developer.apple.com/documentation/uikit/uimenucontroller/arrowdirection/up)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIMenuItem](https://developer.apple.com/documentation/uikit/uimenuitem)

|  | Declaration |
| --- | --- |
| From | ``` class UIMenuItem : NSObject {     init(title title: String, action action: Selector)     var title: String!     var action: Selector } ``` |
| To | ``` class UIMenuItem : NSObject {     init(title title: String, action action: Selector)     var title: String     var action: Selector } ``` |

Modified [UIMenuItem.title](https://developer.apple.com/documentation/uikit/uimenuitem/1622827-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String ``` |

Modified [UIModalPresentationStyle [enum]](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIModalTransitionStyle [enum]](https://developer.apple.com/documentation/uikit/uimodaltransitionstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIMotionEffect](https://developer.apple.com/documentation/uikit/uimotioneffect)

|  | Declaration |
| --- | --- |
| From | ``` class UIMotionEffect : NSObject, NSCopying, NSCoding {     func keyPathsAndRelativeValuesForViewerOffset(_ viewerOffset: UIOffset) -> [NSObject : AnyObject]! } ``` |
| To | ``` class UIMotionEffect : NSObject, NSCopying, NSCoding {     init()     init?(coder aDecoder: NSCoder)     func keyPathsAndRelativeValuesForViewerOffset(_ viewerOffset: UIOffset) -> [String : AnyObject]? } ``` |

Modified [UIMotionEffect.keyPathsAndRelativeValuesForViewerOffset(_: UIOffset) -> [String : AnyObject]?](https://developer.apple.com/documentation/uikit/uimotioneffect/1622380-keypathsandrelativevalues)

|  | Declaration |
| --- | --- |
| From | ``` func keyPathsAndRelativeValuesForViewerOffset(_ viewerOffset: UIOffset) -> [NSObject : AnyObject]! ``` |
| To | ``` func keyPathsAndRelativeValuesForViewerOffset(_ viewerOffset: UIOffset) -> [String : AnyObject]? ``` |

Modified [UIMotionEffectGroup](https://developer.apple.com/documentation/uikit/uimotioneffectgroup)

|  | Declaration |
| --- | --- |
| From | ``` class UIMotionEffectGroup : UIMotionEffect {     var motionEffects: [AnyObject]! } ``` |
| To | ``` class UIMotionEffectGroup : UIMotionEffect {     var motionEffects: [UIMotionEffect]? } ``` |

Modified [UIMotionEffectGroup.motionEffects](https://developer.apple.com/documentation/uikit/uimotioneffectgroup/1622374-motioneffects)

|  | Declaration |
| --- | --- |
| From | ``` var motionEffects: [AnyObject]! ``` |
| To | ``` var motionEffects: [UIMotionEffect]? ``` |

Modified [UIMutableUserNotificationAction](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction)

|  | Declaration |
| --- | --- |
| From | ``` class UIMutableUserNotificationAction : UIUserNotificationAction {     var identifier: String!     var title: String!     var activationMode: UIUserNotificationActivationMode     var authenticationRequired: Bool     var destructive: Bool } ``` |
| To | ``` class UIMutableUserNotificationAction : UIUserNotificationAction {     var identifier: String?     var title: String?     var behavior: UIUserNotificationActionBehavior     var parameters: [NSObject : AnyObject]     var activationMode: UIUserNotificationActivationMode     var authenticationRequired: Bool     var destructive: Bool } ``` |

Modified [UIMutableUserNotificationAction.identifier](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615379-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! ``` |
| To | ``` var identifier: String? ``` |

Modified [UIMutableUserNotificationAction.title](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/1615370-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String? ``` |

Modified [UIMutableUserNotificationCategory](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory)

|  | Declaration |
| --- | --- |
| From | ``` class UIMutableUserNotificationCategory : UIUserNotificationCategory {     var identifier: String!     func setActions(_ actions: [AnyObject]!, forContext context: UIUserNotificationActionContext) } ``` |
| To | ``` class UIMutableUserNotificationCategory : UIUserNotificationCategory {     var identifier: String?     func setActions(_ actions: [UIUserNotificationAction]?, forContext context: UIUserNotificationActionContext) } ``` |

Modified [UIMutableUserNotificationCategory.identifier](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory/1615376-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! ``` |
| To | ``` var identifier: String? ``` |

Modified [UIMutableUserNotificationCategory.setActions(_: [UIUserNotificationAction]?, forContext: UIUserNotificationActionContext)](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory/1615397-setactions)

|  | Declaration |
| --- | --- |
| From | ``` func setActions(_ actions: [AnyObject]!, forContext context: UIUserNotificationActionContext) ``` |
| To | ``` func setActions(_ actions: [UIUserNotificationAction]?, forContext context: UIUserNotificationActionContext) ``` |

Modified [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar)

|  | Declaration |
| --- | --- |
| From | ``` class UINavigationBar : UIView, NSCoding, UIBarPositioning, NSObjectProtocol {     var barStyle: UIBarStyle     unowned(unsafe) var delegate: UINavigationBarDelegate?     var translucent: Bool     func pushNavigationItem(_ item: UINavigationItem, animated animated: Bool)     func popNavigationItemAnimated(_ animated: Bool) -> UINavigationItem?     var topItem: UINavigationItem? { get }     var backItem: UINavigationItem? { get }     var items: [AnyObject]!     func setItems(_ items: [AnyObject]!, animated animated: Bool)     var tintColor: UIColor!     var barTintColor: UIColor?     func setBackgroundImage(_ backgroundImage: UIImage?, forBarPosition barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForBarPosition(_ barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackgroundImage(_ backgroundImage: UIImage!, forBarMetrics barMetrics: UIBarMetrics)     func backgroundImageForBarMetrics(_ barMetrics: UIBarMetrics) -> UIImage?     var shadowImage: UIImage?     var titleTextAttributes: [NSObject : AnyObject]?     func setTitleVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func titleVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat     var backIndicatorImage: UIImage?     var backIndicatorTransitionMaskImage: UIImage? } ``` |
| To | ``` class UINavigationBar : UIView, UIBarPositioning {     var barStyle: UIBarStyle     weak var delegate: UINavigationBarDelegate?     var translucent: Bool     func pushNavigationItem(_ item: UINavigationItem, animated animated: Bool)     func popNavigationItemAnimated(_ animated: Bool) -> UINavigationItem?     var topItem: UINavigationItem? { get }     var backItem: UINavigationItem? { get }     var items: [UINavigationItem]?     func setItems(_ items: [UINavigationItem]?, animated animated: Bool)     var tintColor: UIColor!     var barTintColor: UIColor?     func setBackgroundImage(_ backgroundImage: UIImage?, forBarPosition barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForBarPosition(_ barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackgroundImage(_ backgroundImage: UIImage?, forBarMetrics barMetrics: UIBarMetrics)     func backgroundImageForBarMetrics(_ barMetrics: UIBarMetrics) -> UIImage?     var shadowImage: UIImage?     var titleTextAttributes: [String : AnyObject]?     func setTitleVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func titleVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat     var backIndicatorImage: UIImage?     var backIndicatorTransitionMaskImage: UIImage? } ``` |

Modified [UINavigationBar.delegate](https://developer.apple.com/documentation/uikit/uinavigationbar/1624951-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UINavigationBarDelegate? ``` |
| To | ``` weak var delegate: UINavigationBarDelegate? ``` |

Modified [UINavigationBar.items](https://developer.apple.com/documentation/uikit/uinavigationbar/1624961-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject]! ``` |
| To | ``` var items: [UINavigationItem]? ``` |

Modified [UINavigationBar.setBackgroundImage(_: UIImage?, forBarMetrics: UIBarMetrics)](https://developer.apple.com/documentation/uikit/uinavigationbar/1624926-setbackgroundimage)

|  | Declaration |
| --- | --- |
| From | ``` func setBackgroundImage(_ backgroundImage: UIImage!, forBarMetrics barMetrics: UIBarMetrics) ``` |
| To | ``` func setBackgroundImage(_ backgroundImage: UIImage?, forBarMetrics barMetrics: UIBarMetrics) ``` |

Modified [UINavigationBar.setItems(_: [UINavigationItem]?, animated: Bool)](https://developer.apple.com/documentation/uikit/uinavigationbar/1624945-setitems)

|  | Declaration |
| --- | --- |
| From | ``` func setItems(_ items: [AnyObject]!, animated animated: Bool) ``` |
| To | ``` func setItems(_ items: [UINavigationItem]?, animated animated: Bool) ``` |

Modified [UINavigationBar.titleTextAttributes](https://developer.apple.com/documentation/uikit/uinavigationbar/1624953-titletextattributes)

|  | Declaration |
| --- | --- |
| From | ``` var titleTextAttributes: [NSObject : AnyObject]? ``` |
| To | ``` var titleTextAttributes: [String : AnyObject]? ``` |

Modified [UINavigationBarDelegate.navigationBar(_: UINavigationBar, didPopItem: UINavigationItem)](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/1624948-navigationbar)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UINavigationBarDelegate.navigationBar(_: UINavigationBar, didPushItem: UINavigationItem)](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/1624964-navigationbar)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UINavigationBarDelegate.navigationBar(_: UINavigationBar, shouldPopItem: UINavigationItem) -> Bool](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/1624944-navigationbar)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UINavigationBarDelegate.navigationBar(_: UINavigationBar, shouldPushItem: UINavigationItem) -> Bool](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/1624941-navigationbar)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UINavigationController : UIViewController {     init(navigationBarClass navigationBarClass: AnyClass?, toolbarClass toolbarClass: AnyClass?)     init(rootViewController rootViewController: UIViewController)     func pushViewController(_ viewController: UIViewController, animated animated: Bool)     func popViewControllerAnimated(_ animated: Bool) -> UIViewController?     func popToViewController(_ viewController: UIViewController, animated animated: Bool) -> [AnyObject]?     func popToRootViewControllerAnimated(_ animated: Bool) -> [AnyObject]?     var topViewController: UIViewController! { get }     var visibleViewController: UIViewController! { get }     var viewControllers: [AnyObject]!     func setViewControllers(_ viewControllers: [AnyObject]!, animated animated: Bool)     var navigationBarHidden: Bool     func setNavigationBarHidden(_ hidden: Bool, animated animated: Bool)     var navigationBar: UINavigationBar { get }     var toolbarHidden: Bool     func setToolbarHidden(_ hidden: Bool, animated animated: Bool)     var toolbar: UIToolbar! { get }     unowned(unsafe) var delegate: UINavigationControllerDelegate?     var interactivePopGestureRecognizer: UIGestureRecognizer! { get }     func showViewController(_ vc: UIViewController, sender sender: AnyObject!)     var hidesBarsWhenKeyboardAppears: Bool     var hidesBarsOnSwipe: Bool     var barHideOnSwipeGestureRecognizer: UIPanGestureRecognizer { get }     var hidesBarsWhenVerticallyCompact: Bool     var hidesBarsOnTap: Bool     unowned(unsafe) var barHideOnTapGestureRecognizer: UITapGestureRecognizer { get } } ``` |
| To | ``` class UINavigationController : UIViewController {     init(navigationBarClass navigationBarClass: AnyClass?, toolbarClass toolbarClass: AnyClass?)     init(rootViewController rootViewController: UIViewController)     func pushViewController(_ viewController: UIViewController, animated animated: Bool)     func popViewControllerAnimated(_ animated: Bool) -> UIViewController?     func popToViewController(_ viewController: UIViewController, animated animated: Bool) -> [UIViewController]?     func popToRootViewControllerAnimated(_ animated: Bool) -> [UIViewController]?     var topViewController: UIViewController? { get }     var visibleViewController: UIViewController? { get }     var viewControllers: [UIViewController]     func setViewControllers(_ viewControllers: [UIViewController], animated animated: Bool)     var navigationBarHidden: Bool     func setNavigationBarHidden(_ hidden: Bool, animated animated: Bool)     var navigationBar: UINavigationBar { get }     var toolbarHidden: Bool     func setToolbarHidden(_ hidden: Bool, animated animated: Bool)     var toolbar: UIToolbar! { get }     weak var delegate: UINavigationControllerDelegate?     var interactivePopGestureRecognizer: UIGestureRecognizer? { get }     func showViewController(_ vc: UIViewController, sender sender: AnyObject?)     var hidesBarsWhenKeyboardAppears: Bool     var hidesBarsOnSwipe: Bool     var barHideOnSwipeGestureRecognizer: UIPanGestureRecognizer { get }     var hidesBarsWhenVerticallyCompact: Bool     var hidesBarsOnTap: Bool     unowned(unsafe) var barHideOnTapGestureRecognizer: UITapGestureRecognizer { get } } ``` |

Modified [UINavigationController.delegate](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621876-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UINavigationControllerDelegate? ``` |
| To | ``` weak var delegate: UINavigationControllerDelegate? ``` |

Modified [UINavigationController.interactivePopGestureRecognizer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621847-interactivepopgesturerecognizer)

|  | Declaration |
| --- | --- |
| From | ``` var interactivePopGestureRecognizer: UIGestureRecognizer! { get } ``` |
| To | ``` var interactivePopGestureRecognizer: UIGestureRecognizer? { get } ``` |

Modified [UINavigationController.popToRootViewControllerAnimated(_: Bool) -> [UIViewController]?](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621855-poptorootviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func popToRootViewControllerAnimated(_ animated: Bool) -> [AnyObject]? ``` |
| To | ``` func popToRootViewControllerAnimated(_ animated: Bool) -> [UIViewController]? ``` |

Modified [UINavigationController.popToViewController(_: UIViewController, animated: Bool) -> [UIViewController]?](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621871-poptoviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func popToViewController(_ viewController: UIViewController, animated animated: Bool) -> [AnyObject]? ``` |
| To | ``` func popToViewController(_ viewController: UIViewController, animated animated: Bool) -> [UIViewController]? ``` |

Modified [UINavigationController.setViewControllers(_: [UIViewController], animated: Bool)](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621861-setviewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` func setViewControllers(_ viewControllers: [AnyObject]!, animated animated: Bool) ``` |
| To | ``` func setViewControllers(_ viewControllers: [UIViewController], animated animated: Bool) ``` |

Modified [UINavigationController.showViewController(_: UIViewController, sender: AnyObject?)](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621872-show)

|  | Declaration |
| --- | --- |
| From | ``` func showViewController(_ vc: UIViewController, sender sender: AnyObject!) ``` |
| To | ``` func showViewController(_ vc: UIViewController, sender sender: AnyObject?) ``` |

Modified [UINavigationController.topViewController](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621849-topviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` var topViewController: UIViewController! { get } ``` |
| To | ``` var topViewController: UIViewController? { get } ``` |

Modified [UINavigationController.viewControllers](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621873-viewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` var viewControllers: [AnyObject]! ``` |
| To | ``` var viewControllers: [UIViewController] ``` |

Modified [UINavigationController.visibleViewController](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621862-visibleviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` var visibleViewController: UIViewController! { get } ``` |
| To | ``` var visibleViewController: UIViewController? { get } ``` |

Modified [UINavigationControllerDelegate](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UINavigationControllerDelegate : NSObjectProtocol {     optional func navigationController(_ navigationController: UINavigationController, willShowViewController viewController: UIViewController, animated animated: Bool)     optional func navigationController(_ navigationController: UINavigationController, didShowViewController viewController: UIViewController, animated animated: Bool)     optional func navigationControllerSupportedInterfaceOrientations(_ navigationController: UINavigationController) -> Int     optional func navigationControllerPreferredInterfaceOrientationForPresentation(_ navigationController: UINavigationController) -> UIInterfaceOrientation     optional func navigationController(_ navigationController: UINavigationController, interactionControllerForAnimationController animationController: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning?     optional func navigationController(_ navigationController: UINavigationController, animationControllerForOperation operation: UINavigationControllerOperation, fromViewController fromVC: UIViewController, toViewController toVC: UIViewController) -> UIViewControllerAnimatedTransitioning? } ``` |
| To | ``` protocol UINavigationControllerDelegate : NSObjectProtocol {     optional func navigationController(_ navigationController: UINavigationController, willShowViewController viewController: UIViewController, animated animated: Bool)     optional func navigationController(_ navigationController: UINavigationController, didShowViewController viewController: UIViewController, animated animated: Bool)     optional func navigationControllerSupportedInterfaceOrientations(_ navigationController: UINavigationController) -> UIInterfaceOrientationMask     optional func navigationControllerPreferredInterfaceOrientationForPresentation(_ navigationController: UINavigationController) -> UIInterfaceOrientation     optional func navigationController(_ navigationController: UINavigationController, interactionControllerForAnimationController animationController: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning?     optional func navigationController(_ navigationController: UINavigationController, animationControllerForOperation operation: UINavigationControllerOperation, fromViewController fromVC: UIViewController, toViewController toVC: UIViewController) -> UIViewControllerAnimatedTransitioning? } ``` |

Modified [UINavigationControllerDelegate.navigationController(_: UINavigationController, didShowViewController: UIViewController, animated: Bool)](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621848-navigationcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UINavigationControllerDelegate.navigationController(_: UINavigationController, willShowViewController: UIViewController, animated: Bool)](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621878-navigationcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UINavigationControllerDelegate.navigationControllerSupportedInterfaceOrientations(_: UINavigationController) -> UIInterfaceOrientationMask](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/1621884-navigationcontrollersupportedint)

|  | Declaration |
| --- | --- |
| From | ``` optional func navigationControllerSupportedInterfaceOrientations(_ navigationController: UINavigationController) -> Int ``` |
| To | ``` optional func navigationControllerSupportedInterfaceOrientations(_ navigationController: UINavigationController) -> UIInterfaceOrientationMask ``` |

Modified [UINavigationControllerOperation [enum]](https://developer.apple.com/documentation/uikit/uinavigationcontrolleroperation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UINavigationItem](https://developer.apple.com/documentation/uikit/uinavigationitem)

|  | Declaration |
| --- | --- |
| From | ``` class UINavigationItem : NSObject, NSCoding {     init(title title: String?)     var title: String?     var backBarButtonItem: UIBarButtonItem?     var titleView: UIView?     var prompt: String?     var hidesBackButton: Bool     func setHidesBackButton(_ hidesBackButton: Bool, animated animated: Bool)     var leftBarButtonItems: [AnyObject]?     var rightBarButtonItems: [AnyObject]?     func setLeftBarButtonItems(_ items: [AnyObject]?, animated animated: Bool)     func setRightBarButtonItems(_ items: [AnyObject]?, animated animated: Bool)     var leftItemsSupplementBackButton: Bool     var leftBarButtonItem: UIBarButtonItem?     var rightBarButtonItem: UIBarButtonItem?     func setLeftBarButtonItem(_ item: UIBarButtonItem?, animated animated: Bool)     func setRightBarButtonItem(_ item: UIBarButtonItem?, animated animated: Bool) } ``` |
| To | ``` class UINavigationItem : NSObject, NSCoding {     init(title title: String)     init?(coder coder: NSCoder)     var title: String?     var titleView: UIView?     var prompt: String?     var backBarButtonItem: UIBarButtonItem?     var hidesBackButton: Bool     func setHidesBackButton(_ hidesBackButton: Bool, animated animated: Bool)     var leftBarButtonItems: [UIBarButtonItem]?     var rightBarButtonItems: [UIBarButtonItem]?     func setLeftBarButtonItems(_ items: [UIBarButtonItem]?, animated animated: Bool)     func setRightBarButtonItems(_ items: [UIBarButtonItem]?, animated animated: Bool)     var leftItemsSupplementBackButton: Bool     var leftBarButtonItem: UIBarButtonItem?     var rightBarButtonItem: UIBarButtonItem?     func setLeftBarButtonItem(_ item: UIBarButtonItem?, animated animated: Bool)     func setRightBarButtonItem(_ item: UIBarButtonItem?, animated animated: Bool) } ``` |

Modified [UINavigationItem.init(title: String)](https://developer.apple.com/documentation/uikit/uinavigationitem/1624943-init)

|  | Declaration |
| --- | --- |
| From | ``` init(title title: String?) ``` |
| To | ``` init(title title: String) ``` |

Modified [UINavigationItem.leftBarButtonItems](https://developer.apple.com/documentation/uikit/uinavigationitem/1624946-leftbarbuttonitems)

|  | Declaration |
| --- | --- |
| From | ``` var leftBarButtonItems: [AnyObject]? ``` |
| To | ``` var leftBarButtonItems: [UIBarButtonItem]? ``` |

Modified [UINavigationItem.rightBarButtonItems](https://developer.apple.com/documentation/uikit/uinavigationitem/1624956-rightbarbuttonitems)

|  | Declaration |
| --- | --- |
| From | ``` var rightBarButtonItems: [AnyObject]? ``` |
| To | ``` var rightBarButtonItems: [UIBarButtonItem]? ``` |

Modified [UINavigationItem.setLeftBarButtonItems(_: [UIBarButtonItem]?, animated: Bool)](https://developer.apple.com/documentation/uikit/uinavigationitem/1624949-setleftbarbuttonitems)

|  | Declaration |
| --- | --- |
| From | ``` func setLeftBarButtonItems(_ items: [AnyObject]?, animated animated: Bool) ``` |
| To | ``` func setLeftBarButtonItems(_ items: [UIBarButtonItem]?, animated animated: Bool) ``` |

Modified [UINavigationItem.setRightBarButtonItems(_: [UIBarButtonItem]?, animated: Bool)](https://developer.apple.com/documentation/uikit/uinavigationitem/1624939-setrightbarbuttonitems)

|  | Declaration |
| --- | --- |
| From | ``` func setRightBarButtonItems(_ items: [AnyObject]?, animated animated: Bool) ``` |
| To | ``` func setRightBarButtonItems(_ items: [UIBarButtonItem]?, animated animated: Bool) ``` |

Modified [UINib](https://developer.apple.com/documentation/uikit/uinib)

|  | Declaration |
| --- | --- |
| From | ``` class UINib : NSObject {     init(nibName name: String, bundle bundleOrNil: NSBundle?) -> UINib     class func nibWithNibName(_ name: String, bundle bundleOrNil: NSBundle?) -> UINib     init(data data: NSData, bundle bundleOrNil: NSBundle?) -> UINib     class func nibWithData(_ data: NSData, bundle bundleOrNil: NSBundle?) -> UINib     func instantiateWithOwner(_ ownerOrNil: AnyObject?, options optionsOrNil: [NSObject : AnyObject]?) -> [AnyObject] } ``` |
| To | ``` class UINib : NSObject {      init(nibName name: String, bundle bundleOrNil: NSBundle?)     class func nibWithNibName(_ name: String, bundle bundleOrNil: NSBundle?) -> UINib      init(data data: NSData, bundle bundleOrNil: NSBundle?)     class func nibWithData(_ data: NSData, bundle bundleOrNil: NSBundle?) -> UINib     func instantiateWithOwner(_ ownerOrNil: AnyObject?, options optionsOrNil: [NSObject : AnyObject]?) -> [AnyObject] } ``` |

Modified [UINib.init(data: NSData, bundle: NSBundle?)](https://developer.apple.com/documentation/uikit/uinib/1614135-init)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData, bundle bundleOrNil: NSBundle?) -> UINib ``` |
| To | ``` init(data data: NSData, bundle bundleOrNil: NSBundle?) ``` |

Modified [UINib.init(nibName: String, bundle: NSBundle?)](https://developer.apple.com/documentation/uikit/uinib/1614138-init)

|  | Declaration |
| --- | --- |
| From | ``` init(nibName name: String, bundle bundleOrNil: NSBundle?) -> UINib ``` |
| To | ``` init(nibName name: String, bundle bundleOrNil: NSBundle?) ``` |

Modified [UIObjectRestoration](https://developer.apple.com/documentation/uikit/uiobjectrestoration)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIObjectRestoration {     static func objectWithRestorationIdentifierPath(_ identifierComponents: [AnyObject], coder coder: NSCoder) -> UIStateRestoring? } ``` |
| To | ``` protocol UIObjectRestoration {     static func objectWithRestorationIdentifierPath(_ identifierComponents: [String], coder coder: NSCoder) -> UIStateRestoring? } ``` |

Modified [UIObjectRestoration.objectWithRestorationIdentifierPath(_: [String], coder: NSCoder) -> UIStateRestoring? [class]](https://developer.apple.com/documentation/uikit/uiobjectrestoration/1616855-objectwithrestorationidentifierp)

|  | Declaration |
| --- | --- |
| From | ``` static func objectWithRestorationIdentifierPath(_ identifierComponents: [AnyObject], coder coder: NSCoder) -> UIStateRestoring? ``` |
| To | ``` static func objectWithRestorationIdentifierPath(_ identifierComponents: [String], coder coder: NSCoder) -> UIStateRestoring? ``` |

Modified [UIOffset [struct]](https://developer.apple.com/documentation/uikit/uioffset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIOffset {     var horizontal: CGFloat     var vertical: CGFloat     init()     init(horizontal horizontal: CGFloat, vertical vertical: CGFloat) } ``` | -- |
| To | ``` struct UIOffset {     var horizontal: CGFloat     var vertical: CGFloat     init()     init(horizontal horizontal: CGFloat, vertical vertical: CGFloat) } extension UIOffset : Equatable { } extension UIOffset : Equatable { } ``` | Equatable |

Modified [UIPageViewController](https://developer.apple.com/documentation/uikit/uipageviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIPageViewController : UIViewController {     init(transitionStyle style: UIPageViewControllerTransitionStyle, navigationOrientation navigationOrientation: UIPageViewControllerNavigationOrientation, options options: [NSObject : AnyObject]?)     unowned(unsafe) var delegate: UIPageViewControllerDelegate?     unowned(unsafe) var dataSource: UIPageViewControllerDataSource?     var transitionStyle: UIPageViewControllerTransitionStyle { get }     var navigationOrientation: UIPageViewControllerNavigationOrientation { get }     var spineLocation: UIPageViewControllerSpineLocation { get }     var doubleSided: Bool     var gestureRecognizers: [AnyObject] { get }     var viewControllers: [AnyObject]! { get }     func setViewControllers(_ viewControllers: [AnyObject]!, direction direction: UIPageViewControllerNavigationDirection, animated animated: Bool, completion completion: ((Bool) -> Void)!) } ``` |
| To | ``` class UIPageViewController : UIViewController {     init(transitionStyle style: UIPageViewControllerTransitionStyle, navigationOrientation navigationOrientation: UIPageViewControllerNavigationOrientation, options options: [String : AnyObject]?)     init?(coder coder: NSCoder)     weak var delegate: UIPageViewControllerDelegate?     weak var dataSource: UIPageViewControllerDataSource?     var transitionStyle: UIPageViewControllerTransitionStyle { get }     var navigationOrientation: UIPageViewControllerNavigationOrientation { get }     var spineLocation: UIPageViewControllerSpineLocation { get }     var doubleSided: Bool     var gestureRecognizers: [UIGestureRecognizer] { get }     var viewControllers: [UIViewController]? { get }     func setViewControllers(_ viewControllers: [UIViewController]?, direction direction: UIPageViewControllerNavigationDirection, animated animated: Bool, completion completion: ((Bool) -> Void)?) } ``` |

Modified [UIPageViewController.dataSource](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614117-datasource)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var dataSource: UIPageViewControllerDataSource? ``` |
| To | ``` weak var dataSource: UIPageViewControllerDataSource? ``` |

Modified [UIPageViewController.delegate](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614089-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UIPageViewControllerDelegate? ``` |
| To | ``` weak var delegate: UIPageViewControllerDelegate? ``` |

Modified [UIPageViewController.gestureRecognizers](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614107-gesturerecognizers)

|  | Declaration |
| --- | --- |
| From | ``` var gestureRecognizers: [AnyObject] { get } ``` |
| To | ``` var gestureRecognizers: [UIGestureRecognizer] { get } ``` |

Modified [UIPageViewController.init(transitionStyle: UIPageViewControllerTransitionStyle, navigationOrientation: UIPageViewControllerNavigationOrientation, options: [String : AnyObject]?)](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614105-init)

|  | Declaration |
| --- | --- |
| From | ``` init(transitionStyle style: UIPageViewControllerTransitionStyle, navigationOrientation navigationOrientation: UIPageViewControllerNavigationOrientation, options options: [NSObject : AnyObject]?) ``` |
| To | ``` init(transitionStyle style: UIPageViewControllerTransitionStyle, navigationOrientation navigationOrientation: UIPageViewControllerNavigationOrientation, options options: [String : AnyObject]?) ``` |

Modified [UIPageViewController.setViewControllers(_: [UIViewController]?, direction: UIPageViewControllerNavigationDirection, animated: Bool, completion: ((Bool) -> Void)?)](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614087-setviewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` func setViewControllers(_ viewControllers: [AnyObject]!, direction direction: UIPageViewControllerNavigationDirection, animated animated: Bool, completion completion: ((Bool) -> Void)!) ``` |
| To | ``` func setViewControllers(_ viewControllers: [UIViewController]?, direction direction: UIPageViewControllerNavigationDirection, animated animated: Bool, completion completion: ((Bool) -> Void)?) ``` |

Modified [UIPageViewController.viewControllers](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614106-viewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` var viewControllers: [AnyObject]! { get } ``` |
| To | ``` var viewControllers: [UIViewController]? { get } ``` |

Modified [UIPageViewControllerDataSource.pageViewController(_: UIPageViewController, viewControllerAfterViewController: UIViewController) -> UIViewController?](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/1614118-pageviewcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [UIPageViewControllerDataSource.pageViewController(_: UIPageViewController, viewControllerBeforeViewController: UIViewController) -> UIViewController?](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/1614086-pageviewcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [UIPageViewControllerDelegate](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIPageViewControllerDelegate : NSObjectProtocol {     optional func pageViewController(_ pageViewController: UIPageViewController, willTransitionToViewControllers pendingViewControllers: [AnyObject])     optional func pageViewController(_ pageViewController: UIPageViewController, didFinishAnimating finished: Bool, previousViewControllers previousViewControllers: [AnyObject], transitionCompleted completed: Bool)     optional func pageViewController(_ pageViewController: UIPageViewController, spineLocationForInterfaceOrientation orientation: UIInterfaceOrientation) -> UIPageViewControllerSpineLocation     optional func pageViewControllerSupportedInterfaceOrientations(_ pageViewController: UIPageViewController) -> Int     optional func pageViewControllerPreferredInterfaceOrientationForPresentation(_ pageViewController: UIPageViewController) -> UIInterfaceOrientation } ``` |
| To | ``` protocol UIPageViewControllerDelegate : NSObjectProtocol {     optional func pageViewController(_ pageViewController: UIPageViewController, willTransitionToViewControllers pendingViewControllers: [UIViewController])     optional func pageViewController(_ pageViewController: UIPageViewController, didFinishAnimating finished: Bool, previousViewControllers previousViewControllers: [UIViewController], transitionCompleted completed: Bool)     optional func pageViewController(_ pageViewController: UIPageViewController, spineLocationForInterfaceOrientation orientation: UIInterfaceOrientation) -> UIPageViewControllerSpineLocation     optional func pageViewControllerSupportedInterfaceOrientations(_ pageViewController: UIPageViewController) -> UIInterfaceOrientationMask     optional func pageViewControllerPreferredInterfaceOrientationForPresentation(_ pageViewController: UIPageViewController) -> UIInterfaceOrientation } ``` |

Modified [UIPageViewControllerDelegate.pageViewController(_: UIPageViewController, didFinishAnimating: Bool, previousViewControllers: [UIViewController], transitionCompleted: Bool)](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614090-pageviewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func pageViewController(_ pageViewController: UIPageViewController, didFinishAnimating finished: Bool, previousViewControllers previousViewControllers: [AnyObject], transitionCompleted completed: Bool) ``` | iOS 8.0 |
| To | ``` optional func pageViewController(_ pageViewController: UIPageViewController, didFinishAnimating finished: Bool, previousViewControllers previousViewControllers: [UIViewController], transitionCompleted completed: Bool) ``` | iOS 5.0 |

Modified [UIPageViewControllerDelegate.pageViewController(_: UIPageViewController, spineLocationForInterfaceOrientation: UIInterfaceOrientation) -> UIPageViewControllerSpineLocation](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614083-pageviewcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [UIPageViewControllerDelegate.pageViewController(_: UIPageViewController, willTransitionToViewControllers: [UIViewController])](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614091-pageviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func pageViewController(_ pageViewController: UIPageViewController, willTransitionToViewControllers pendingViewControllers: [AnyObject]) ``` |
| To | ``` optional func pageViewController(_ pageViewController: UIPageViewController, willTransitionToViewControllers pendingViewControllers: [UIViewController]) ``` |

Modified [UIPageViewControllerDelegate.pageViewControllerSupportedInterfaceOrientations(_: UIPageViewController) -> UIInterfaceOrientationMask](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/1614100-pageviewcontrollersupportedinter)

|  | Declaration |
| --- | --- |
| From | ``` optional func pageViewControllerSupportedInterfaceOrientations(_ pageViewController: UIPageViewController) -> Int ``` |
| To | ``` optional func pageViewControllerSupportedInterfaceOrientations(_ pageViewController: UIPageViewController) -> UIInterfaceOrientationMask ``` |

Modified [UIPageViewControllerNavigationDirection [enum]](https://developer.apple.com/documentation/uikit/uipageviewcontrollernavigationdirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIPageViewControllerNavigationOrientation [enum]](https://developer.apple.com/documentation/uikit/uipageviewcontroller/navigationorientation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIPageViewControllerSpineLocation [enum]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerspinelocation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIPageViewControllerTransitionStyle [enum]](https://developer.apple.com/documentation/uikit/uipageviewcontroller/transitionstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIPanGestureRecognizer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer)

|  | Declaration |
| --- | --- |
| From | ``` class UIPanGestureRecognizer : UIGestureRecognizer {     var minimumNumberOfTouches: Int     var maximumNumberOfTouches: Int     func translationInView(_ view: UIView) -> CGPoint     func setTranslation(_ translation: CGPoint, inView view: UIView!)     func velocityInView(_ view: UIView!) -> CGPoint } ``` |
| To | ``` class UIPanGestureRecognizer : UIGestureRecognizer {     var minimumNumberOfTouches: Int     var maximumNumberOfTouches: Int     func translationInView(_ view: UIView?) -> CGPoint     func setTranslation(_ translation: CGPoint, inView view: UIView?)     func velocityInView(_ view: UIView?) -> CGPoint } ``` |

Modified [UIPanGestureRecognizer.setTranslation(_: CGPoint, inView: UIView?)](https://developer.apple.com/documentation/uikit/uipangesturerecognizer/1621206-settranslation)

|  | Declaration |
| --- | --- |
| From | ``` func setTranslation(_ translation: CGPoint, inView view: UIView!) ``` |
| To | ``` func setTranslation(_ translation: CGPoint, inView view: UIView?) ``` |

Modified [UIPanGestureRecognizer.translationInView(_: UIView?) -> CGPoint](https://developer.apple.com/documentation/uikit/uipangesturerecognizer/1621207-translation)

|  | Declaration |
| --- | --- |
| From | ``` func translationInView(_ view: UIView) -> CGPoint ``` |
| To | ``` func translationInView(_ view: UIView?) -> CGPoint ``` |

Modified [UIPanGestureRecognizer.velocityInView(_: UIView?) -> CGPoint](https://developer.apple.com/documentation/uikit/uipangesturerecognizer/1621209-velocity)

|  | Declaration |
| --- | --- |
| From | ``` func velocityInView(_ view: UIView!) -> CGPoint ``` |
| To | ``` func velocityInView(_ view: UIView?) -> CGPoint ``` |

Modified [UIPasteboard](https://developer.apple.com/documentation/uikit/uipasteboard)

|  | Declaration |
| --- | --- |
| From | ``` class UIPasteboard : NSObject {     class func generalPasteboard() -> UIPasteboard     init!(name pasteboardName: String!, create create: Bool) -> UIPasteboard     class func pasteboardWithName(_ pasteboardName: String!, create create: Bool) -> UIPasteboard!     class func pasteboardWithUniqueName() -> UIPasteboard     var name: String { get }     class func removePasteboardWithName(_ pasteboardName: String)     var persistent: Bool     var changeCount: Int { get }     func pasteboardTypes() -> [AnyObject]!     func containsPasteboardTypes(_ pasteboardTypes: [AnyObject]) -> Bool     func dataForPasteboardType(_ pasteboardType: String) -> NSData?     func valueForPasteboardType(_ pasteboardType: String) -> AnyObject?     func setValue(_ value: AnyObject, forPasteboardType pasteboardType: String)     func setData(_ data: NSData, forPasteboardType pasteboardType: String)     var numberOfItems: Int { get }     func pasteboardTypesForItemSet(_ itemSet: NSIndexSet?) -> [AnyObject]?     func containsPasteboardTypes(_ pasteboardTypes: [AnyObject], inItemSet itemSet: NSIndexSet?) -> Bool     func itemSetWithPasteboardTypes(_ pasteboardTypes: [AnyObject]) -> NSIndexSet?     func valuesForPasteboardType(_ pasteboardType: String, inItemSet itemSet: NSIndexSet?) -> [AnyObject]!     func dataForPasteboardType(_ pasteboardType: String, inItemSet itemSet: NSIndexSet?) -> [AnyObject]     var items: [AnyObject]!     func addItems(_ items: [AnyObject]) } extension UIPasteboard {     var string: String?     var strings: [AnyObject]?     @NSCopying var URL: NSURL?     var URLs: [AnyObject]!     @NSCopying var image: UIImage?     var images: [AnyObject]!     @NSCopying var color: UIColor?     var colors: [AnyObject]! } ``` |
| To | ``` class UIPasteboard : NSObject {     class func generalPasteboard() -> UIPasteboard      init?(name pasteboardName: String, create create: Bool)     class func pasteboardWithName(_ pasteboardName: String, create create: Bool) -> UIPasteboard?     class func pasteboardWithUniqueName() -> UIPasteboard     var name: String { get }     class func removePasteboardWithName(_ pasteboardName: String)     var persistent: Bool     var changeCount: Int { get }     func pasteboardTypes() -> [String]     func containsPasteboardTypes(_ pasteboardTypes: [String]) -> Bool     func dataForPasteboardType(_ pasteboardType: String) -> NSData?     func valueForPasteboardType(_ pasteboardType: String) -> AnyObject?     func setValue(_ value: AnyObject, forPasteboardType pasteboardType: String)     func setData(_ data: NSData, forPasteboardType pasteboardType: String)     var numberOfItems: Int { get }     func pasteboardTypesForItemSet(_ itemSet: NSIndexSet?) -> [AnyObject]?     func containsPasteboardTypes(_ pasteboardTypes: [String], inItemSet itemSet: NSIndexSet?) -> Bool     func itemSetWithPasteboardTypes(_ pasteboardTypes: [AnyObject]) -> NSIndexSet?     func valuesForPasteboardType(_ pasteboardType: String, inItemSet itemSet: NSIndexSet?) -> [AnyObject]?     func dataForPasteboardType(_ pasteboardType: String, inItemSet itemSet: NSIndexSet?) -> [AnyObject]?     var items: [AnyObject]     func addItems(_ items: [[String : AnyObject]]) } extension UIPasteboard {     var string: String?     var strings: [String]?     @NSCopying var URL: NSURL?     var URLs: [NSURL]?     @NSCopying var image: UIImage?     var images: [UIImage]?     @NSCopying var color: UIColor?     var colors: [UIColor]? } ``` |

Modified [UIPasteboard.addItems(_: [[String : AnyObject]])](https://developer.apple.com/documentation/uikit/uipasteboard/1622101-additems)

|  | Declaration |
| --- | --- |
| From | ``` func addItems(_ items: [AnyObject]) ``` |
| To | ``` func addItems(_ items: [[String : AnyObject]]) ``` |

Modified [UIPasteboard.colors](https://developer.apple.com/documentation/uikit/uipasteboard/1622078-colors)

|  | Declaration |
| --- | --- |
| From | ``` var colors: [AnyObject]! ``` |
| To | ``` var colors: [UIColor]? ``` |

Modified [UIPasteboard.containsPasteboardTypes(_: [String]) -> Bool](https://developer.apple.com/documentation/uikit/uipasteboard/1622070-contains)

|  | Declaration |
| --- | --- |
| From | ``` func containsPasteboardTypes(_ pasteboardTypes: [AnyObject]) -> Bool ``` |
| To | ``` func containsPasteboardTypes(_ pasteboardTypes: [String]) -> Bool ``` |

Modified [UIPasteboard.containsPasteboardTypes(_: [String], inItemSet: NSIndexSet?) -> Bool](https://developer.apple.com/documentation/uikit/uipasteboard/1622100-containspasteboardtypes)

|  | Declaration |
| --- | --- |
| From | ``` func containsPasteboardTypes(_ pasteboardTypes: [AnyObject], inItemSet itemSet: NSIndexSet?) -> Bool ``` |
| To | ``` func containsPasteboardTypes(_ pasteboardTypes: [String], inItemSet itemSet: NSIndexSet?) -> Bool ``` |

Modified [UIPasteboard.dataForPasteboardType(_: String, inItemSet: NSIndexSet?) -> [AnyObject]?](https://developer.apple.com/documentation/uikit/uipasteboard/1622068-dataforpasteboardtype)

|  | Declaration |
| --- | --- |
| From | ``` func dataForPasteboardType(_ pasteboardType: String, inItemSet itemSet: NSIndexSet?) -> [AnyObject] ``` |
| To | ``` func dataForPasteboardType(_ pasteboardType: String, inItemSet itemSet: NSIndexSet?) -> [AnyObject]? ``` |

Modified [UIPasteboard.images](https://developer.apple.com/documentation/uikit/uipasteboard/1622086-images)

|  | Declaration |
| --- | --- |
| From | ``` var images: [AnyObject]! ``` |
| To | ``` var images: [UIImage]? ``` |

Modified [UIPasteboard.init(name: String, create: Bool)](https://developer.apple.com/documentation/uikit/uipasteboard/1622074-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(name pasteboardName: String!, create create: Bool) -> UIPasteboard ``` |
| To | ``` init?(name pasteboardName: String, create create: Bool) ``` |

Modified [UIPasteboard.items](https://developer.apple.com/documentation/uikit/uipasteboard/1622067-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject]! ``` |
| To | ``` var items: [AnyObject] ``` |

Modified [UIPasteboard.pasteboardTypes() -> [String]](https://developer.apple.com/documentation/uikit/uipasteboard/1622077-types)

|  | Declaration |
| --- | --- |
| From | ``` func pasteboardTypes() -> [AnyObject]! ``` |
| To | ``` func pasteboardTypes() -> [String] ``` |

Modified [UIPasteboard.strings](https://developer.apple.com/documentation/uikit/uipasteboard/1622091-strings)

|  | Declaration |
| --- | --- |
| From | ``` var strings: [AnyObject]? ``` |
| To | ``` var strings: [String]? ``` |

Modified [UIPasteboard.URLs](https://developer.apple.com/documentation/uikit/uipasteboard/1622097-urls)

|  | Declaration |
| --- | --- |
| From | ``` var URLs: [AnyObject]! ``` |
| To | ``` var URLs: [NSURL]? ``` |

Modified [UIPasteboard.valuesForPasteboardType(_: String, inItemSet: NSIndexSet?) -> [AnyObject]?](https://developer.apple.com/documentation/uikit/uipasteboard/1622094-values)

|  | Declaration |
| --- | --- |
| From | ``` func valuesForPasteboardType(_ pasteboardType: String, inItemSet itemSet: NSIndexSet?) -> [AnyObject]! ``` |
| To | ``` func valuesForPasteboardType(_ pasteboardType: String, inItemSet itemSet: NSIndexSet?) -> [AnyObject]? ``` |

Modified [UIPercentDrivenInteractiveTransition](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition)

|  | Declaration |
| --- | --- |
| From | ``` class UIPercentDrivenInteractiveTransition : NSObject, UIViewControllerInteractiveTransitioning, NSObjectProtocol {     var duration: CGFloat { get }     var percentComplete: CGFloat { get }     var completionSpeed: CGFloat     var completionCurve: UIViewAnimationCurve     func updateInteractiveTransition(_ percentComplete: CGFloat)     func cancelInteractiveTransition()     func finishInteractiveTransition() } ``` |
| To | ``` class UIPercentDrivenInteractiveTransition : NSObject, UIViewControllerInteractiveTransitioning {     var duration: CGFloat { get }     var percentComplete: CGFloat { get }     var completionSpeed: CGFloat     var completionCurve: UIViewAnimationCurve     func updateInteractiveTransition(_ percentComplete: CGFloat)     func cancelInteractiveTransition()     func finishInteractiveTransition() } ``` |

Modified [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview)

|  | Declaration |
| --- | --- |
| From | ``` class UIPickerView : UIView, NSCoding, UITableViewDataSource, NSObjectProtocol {     unowned(unsafe) var dataSource: UIPickerViewDataSource?     unowned(unsafe) var delegate: UIPickerViewDelegate?     var showsSelectionIndicator: Bool     var numberOfComponents: Int { get }     func numberOfRowsInComponent(_ component: Int) -> Int     func rowSizeForComponent(_ component: Int) -> CGSize     func viewForRow(_ row: Int, forComponent component: Int) -> UIView?     func reloadAllComponents()     func reloadComponent(_ component: Int)     func selectRow(_ row: Int, inComponent component: Int, animated animated: Bool)     func selectedRowInComponent(_ component: Int) -> Int } ``` |
| To | ``` class UIPickerView : UIView, UITableViewDataSource {     weak var dataSource: UIPickerViewDataSource?     weak var delegate: UIPickerViewDelegate?     var showsSelectionIndicator: Bool     var numberOfComponents: Int { get }     func numberOfRowsInComponent(_ component: Int) -> Int     func rowSizeForComponent(_ component: Int) -> CGSize     func viewForRow(_ row: Int, forComponent component: Int) -> UIView?     func reloadAllComponents()     func reloadComponent(_ component: Int)     func selectRow(_ row: Int, inComponent component: Int, animated animated: Bool)     func selectedRowInComponent(_ component: Int) -> Int } ``` |

Modified [UIPickerView.dataSource](https://developer.apple.com/documentation/uikit/uipickerview/1614370-datasource)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var dataSource: UIPickerViewDataSource? ``` |
| To | ``` weak var dataSource: UIPickerViewDataSource? ``` |

Modified [UIPickerView.delegate](https://developer.apple.com/documentation/uikit/uipickerview/1614379-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UIPickerViewDelegate? ``` |
| To | ``` weak var delegate: UIPickerViewDelegate? ``` |

Modified [UIPickerViewAccessibilityDelegate](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIPickerViewAccessibilityDelegate : UIPickerViewDelegate, NSObjectProtocol {     optional func pickerView(_ pickerView: UIPickerView, accessibilityLabelForComponent component: Int) -> String     optional func pickerView(_ pickerView: UIPickerView, accessibilityHintForComponent component: Int) -> String } ``` |
| To | ``` protocol UIPickerViewAccessibilityDelegate : UIPickerViewDelegate, NSObjectProtocol {     optional func pickerView(_ pickerView: UIPickerView, accessibilityLabelForComponent component: Int) -> String?     optional func pickerView(_ pickerView: UIPickerView, accessibilityHintForComponent component: Int) -> String? } ``` |

Modified [UIPickerViewAccessibilityDelegate.pickerView(_: UIPickerView, accessibilityHintForComponent: Int) -> String?](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/1621056-pickerview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func pickerView(_ pickerView: UIPickerView, accessibilityHintForComponent component: Int) -> String ``` | iOS 8.0 |
| To | ``` optional func pickerView(_ pickerView: UIPickerView, accessibilityHintForComponent component: Int) -> String? ``` | iOS 2.0 |

Modified [UIPickerViewAccessibilityDelegate.pickerView(_: UIPickerView, accessibilityLabelForComponent: Int) -> String?](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/1621052-pickerview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func pickerView(_ pickerView: UIPickerView, accessibilityLabelForComponent component: Int) -> String ``` | iOS 8.0 |
| To | ``` optional func pickerView(_ pickerView: UIPickerView, accessibilityLabelForComponent component: Int) -> String? ``` | iOS 2.0 |

Modified [UIPickerViewDataSource.numberOfComponentsInPickerView(_: UIPickerView) -> Int](https://developer.apple.com/documentation/uikit/uipickerviewdatasource/1614377-numberofcomponents)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIPickerViewDataSource.pickerView(_: UIPickerView, numberOfRowsInComponent: Int) -> Int](https://developer.apple.com/documentation/uikit/uipickerviewdatasource/1614388-pickerview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIPickerViewDelegate](https://developer.apple.com/documentation/uikit/uipickerviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIPickerViewDelegate : NSObjectProtocol {     optional func pickerView(_ pickerView: UIPickerView, widthForComponent component: Int) -> CGFloat     optional func pickerView(_ pickerView: UIPickerView, rowHeightForComponent component: Int) -> CGFloat     optional func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String!     optional func pickerView(_ pickerView: UIPickerView, attributedTitleForRow row: Int, forComponent component: Int) -> NSAttributedString?     optional func pickerView(_ pickerView: UIPickerView, viewForRow row: Int, forComponent component: Int, reusingView view: UIView!) -> UIView     optional func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) } ``` |
| To | ``` protocol UIPickerViewDelegate : NSObjectProtocol {     optional func pickerView(_ pickerView: UIPickerView, widthForComponent component: Int) -> CGFloat     optional func pickerView(_ pickerView: UIPickerView, rowHeightForComponent component: Int) -> CGFloat     optional func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String?     optional func pickerView(_ pickerView: UIPickerView, attributedTitleForRow row: Int, forComponent component: Int) -> NSAttributedString?     optional func pickerView(_ pickerView: UIPickerView, viewForRow row: Int, forComponent component: Int, reusingView view: UIView?) -> UIView     optional func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) } ``` |

Modified [UIPickerViewDelegate.pickerView(_: UIPickerView, didSelectRow: Int, inComponent: Int)](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614371-pickerview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIPickerViewDelegate.pickerView(_: UIPickerView, rowHeightForComponent: Int) -> CGFloat](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614386-pickerview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIPickerViewDelegate.pickerView(_: UIPickerView, titleForRow: Int, forComponent: Int) -> String?](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614384-pickerview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String! ``` | iOS 8.0 |
| To | ``` optional func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? ``` | iOS 2.0 |

Modified [UIPickerViewDelegate.pickerView(_: UIPickerView, viewForRow: Int, forComponent: Int, reusingView: UIView?) -> UIView](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614389-pickerview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func pickerView(_ pickerView: UIPickerView, viewForRow row: Int, forComponent component: Int, reusingView view: UIView!) -> UIView ``` | iOS 8.0 |
| To | ``` optional func pickerView(_ pickerView: UIPickerView, viewForRow row: Int, forComponent component: Int, reusingView view: UIView?) -> UIView ``` | iOS 2.0 |

Modified [UIPickerViewDelegate.pickerView(_: UIPickerView, widthForComponent: Int) -> CGFloat](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614378-pickerview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIPopoverArrowDirection [struct]](https://developer.apple.com/documentation/uikit/uipopoverarrowdirection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIPopoverArrowDirection : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Up: UIPopoverArrowDirection { get }     static var Down: UIPopoverArrowDirection { get }     static var Left: UIPopoverArrowDirection { get }     static var Right: UIPopoverArrowDirection { get }     static var Any: UIPopoverArrowDirection { get }     static var Unknown: UIPopoverArrowDirection { get } } ``` | RawOptionSetType |
| To | ``` struct UIPopoverArrowDirection : OptionSetType {     init(rawValue rawValue: UInt)     static var Up: UIPopoverArrowDirection { get }     static var Down: UIPopoverArrowDirection { get }     static var Left: UIPopoverArrowDirection { get }     static var Right: UIPopoverArrowDirection { get }     static var Any: UIPopoverArrowDirection { get }     static var Unknown: UIPopoverArrowDirection { get } } ``` | OptionSetType |

Modified [UIPopoverController](https://developer.apple.com/documentation/uikit/uipopovercontroller)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class UIPopoverController : NSObject, UIAppearanceContainer, NSObjectProtocol {     init(contentViewController viewController: UIViewController)     unowned(unsafe) var delegate: UIPopoverControllerDelegate?     var contentViewController: UIViewController     func setContentViewController(_ viewController: UIViewController, animated animated: Bool)     var popoverContentSize: CGSize     func setPopoverContentSize(_ size: CGSize, animated animated: Bool)     var popoverVisible: Bool { get }     var popoverArrowDirection: UIPopoverArrowDirection { get }     var passthroughViews: [AnyObject]?     func presentPopoverFromRect(_ rect: CGRect, inView view: UIView, permittedArrowDirections arrowDirections: UIPopoverArrowDirection, animated animated: Bool)     func presentPopoverFromBarButtonItem(_ item: UIBarButtonItem, permittedArrowDirections arrowDirections: UIPopoverArrowDirection, animated animated: Bool)     func dismissPopoverAnimated(_ animated: Bool)     @NSCopying var backgroundColor: UIColor?     var popoverLayoutMargins: UIEdgeInsets     var popoverBackgroundViewClass: AnyClass? } ``` | -- |
| To | ``` class UIPopoverController : NSObject, UIAppearanceContainer {     init(contentViewController viewController: UIViewController)     weak var delegate: UIPopoverControllerDelegate?     var contentViewController: UIViewController     func setContentViewController(_ viewController: UIViewController, animated animated: Bool)     var popoverContentSize: CGSize     func setPopoverContentSize(_ size: CGSize, animated animated: Bool)     var popoverVisible: Bool { get }     var popoverArrowDirection: UIPopoverArrowDirection { get }     var passthroughViews: [UIView]?     func presentPopoverFromRect(_ rect: CGRect, inView view: UIView, permittedArrowDirections arrowDirections: UIPopoverArrowDirection, animated animated: Bool)     func presentPopoverFromBarButtonItem(_ item: UIBarButtonItem, permittedArrowDirections arrowDirections: UIPopoverArrowDirection, animated animated: Bool)     func dismissPopoverAnimated(_ animated: Bool)     @NSCopying var backgroundColor: UIColor?     var popoverLayoutMargins: UIEdgeInsets     var popoverBackgroundViewClass: AnyClass? } ``` | iOS 9.0 |

Modified [UIPopoverController.backgroundColor](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624673-backgroundcolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.contentViewController](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624672-contentviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.delegate](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624666-delegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` unowned(unsafe) var delegate: UIPopoverControllerDelegate? ``` | -- |
| To | ``` weak var delegate: UIPopoverControllerDelegate? ``` | iOS 9.0 |

Modified [UIPopoverController.dismissPopoverAnimated(_: Bool)](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624662-dismisspopoveranimated)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.init(contentViewController: UIViewController)](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624669-initwithcontentviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.passthroughViews](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624654-passthroughviews)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var passthroughViews: [AnyObject]? ``` | -- |
| To | ``` var passthroughViews: [UIView]? ``` | iOS 9.0 |

Modified [UIPopoverController.popoverArrowDirection](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624665-popoverarrowdirection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.popoverBackgroundViewClass](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624659-popoverbackgroundviewclass)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.popoverContentSize](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624667-popovercontentsize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.popoverLayoutMargins](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624657-popoverlayoutmargins)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.popoverVisible](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624656-popovervisible)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.presentPopoverFromBarButtonItem(_: UIBarButtonItem, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624668-present)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.presentPopoverFromRect(_: CGRect, inView: UIView, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624660-present)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.setContentViewController(_: UIViewController, animated: Bool)](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624655-setcontentviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverController.setPopoverContentSize(_: CGSize, animated: Bool)](https://developer.apple.com/documentation/uikit/uipopovercontroller/1624670-setpopovercontentsize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverControllerDelegate.popoverController(_: UIPopoverController, willRepositionPopoverToRect: UnsafeMutablePointer<CGRect>, inView: AutoreleasingUnsafeMutablePointer<UIView?>)](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624664-popovercontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIPopoverControllerDelegate.popoverControllerDidDismissPopover(_: UIPopoverController)](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624671-popovercontrollerdiddismisspopov)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.2 | iOS 9.0 |

Modified [UIPopoverControllerDelegate.popoverControllerShouldDismissPopover(_: UIPopoverController) -> Bool](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/1624661-popovercontrollershoulddismisspo)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.2 | iOS 9.0 |

Modified [UIPopoverPresentationController](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIPopoverPresentationController : UIPresentationController {     unowned(unsafe) var delegate: UIPopoverPresentationControllerDelegate?     var permittedArrowDirections: UIPopoverArrowDirection     var sourceView: UIView!     var sourceRect: CGRect     var barButtonItem: UIBarButtonItem!     var arrowDirection: UIPopoverArrowDirection { get }     var passthroughViews: [AnyObject]!     @NSCopying var backgroundColor: UIColor!     var popoverLayoutMargins: UIEdgeInsets     var popoverBackgroundViewClass: AnyObject.Type? } ``` |
| To | ``` class UIPopoverPresentationController : UIPresentationController {     weak var delegate: UIPopoverPresentationControllerDelegate?     var permittedArrowDirections: UIPopoverArrowDirection     var sourceView: UIView?     var sourceRect: CGRect     var canOverlapSourceViewRect: Bool     var barButtonItem: UIBarButtonItem?     var arrowDirection: UIPopoverArrowDirection { get }     var passthroughViews: [UIView]?     @NSCopying var backgroundColor: UIColor?     var popoverLayoutMargins: UIEdgeInsets     var popoverBackgroundViewClass: AnyObject.Type? } ``` |

Modified [UIPopoverPresentationController.backgroundColor](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622316-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var backgroundColor: UIColor! ``` |
| To | ``` @NSCopying var backgroundColor: UIColor? ``` |

Modified [UIPopoverPresentationController.barButtonItem](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622314-barbuttonitem)

|  | Declaration |
| --- | --- |
| From | ``` var barButtonItem: UIBarButtonItem! ``` |
| To | ``` var barButtonItem: UIBarButtonItem? ``` |

Modified [UIPopoverPresentationController.delegate](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622320-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UIPopoverPresentationControllerDelegate? ``` |
| To | ``` weak var delegate: UIPopoverPresentationControllerDelegate? ``` |

Modified [UIPopoverPresentationController.passthroughViews](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622312-passthroughviews)

|  | Declaration |
| --- | --- |
| From | ``` var passthroughViews: [AnyObject]! ``` |
| To | ``` var passthroughViews: [UIView]? ``` |

Modified [UIPopoverPresentationController.sourceView](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/1622313-sourceview)

|  | Declaration |
| --- | --- |
| From | ``` var sourceView: UIView! ``` |
| To | ``` var sourceView: UIView? ``` |

Modified [UIPresentationController](https://developer.apple.com/documentation/uikit/uipresentationcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIPresentationController : NSObject, UIAppearanceContainer, NSObjectProtocol, UITraitEnvironment, UIContentContainer {     var presentingViewController: UIViewController { get }     var presentedViewController: UIViewController { get }     var presentationStyle: UIModalPresentationStyle { get }     var containerView: UIView! { get }     unowned(unsafe) var delegate: UIAdaptivePresentationControllerDelegate?     init(presentedViewController presentedViewController: UIViewController!, presentingViewController presentingViewController: UIViewController!)     func adaptivePresentationStyle() -> UIModalPresentationStyle     func adaptivePresentationStyleForTraitCollection(_ traitCollection: UITraitCollection!) -> UIModalPresentationStyle     func containerViewWillLayoutSubviews()     func containerViewDidLayoutSubviews()     func presentedView() -> UIView!     func frameOfPresentedViewInContainerView() -> CGRect     func shouldPresentInFullscreen() -> Bool     func shouldRemovePresentersView() -> Bool     func presentationTransitionWillBegin()     func presentationTransitionDidEnd(_ completed: Bool)     func dismissalTransitionWillBegin()     func dismissalTransitionDidEnd(_ completed: Bool)     @NSCopying var overrideTraitCollection: UITraitCollection? } ``` |
| To | ``` class UIPresentationController : NSObject, UIAppearanceContainer, UITraitEnvironment, UIContentContainer {     var presentingViewController: UIViewController { get }     var presentedViewController: UIViewController { get }     var presentationStyle: UIModalPresentationStyle { get }     var containerView: UIView? { get }     weak var delegate: UIAdaptivePresentationControllerDelegate?     init(presentedViewController presentedViewController: UIViewController, presentingViewController presentingViewController: UIViewController)     func adaptivePresentationStyle() -> UIModalPresentationStyle     func adaptivePresentationStyleForTraitCollection(_ traitCollection: UITraitCollection) -> UIModalPresentationStyle     func containerViewWillLayoutSubviews()     func containerViewDidLayoutSubviews()     func presentedView() -> UIView?     func frameOfPresentedViewInContainerView() -> CGRect     func shouldPresentInFullscreen() -> Bool     func shouldRemovePresentersView() -> Bool     func presentationTransitionWillBegin()     func presentationTransitionDidEnd(_ completed: Bool)     func dismissalTransitionWillBegin()     func dismissalTransitionDidEnd(_ completed: Bool)     @NSCopying var overrideTraitCollection: UITraitCollection? } ``` |

Modified [UIPresentationController.adaptivePresentationStyleForTraitCollection(_: UITraitCollection) -> UIModalPresentationStyle](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618325-adaptivepresentationstyle)

|  | Declaration |
| --- | --- |
| From | ``` func adaptivePresentationStyleForTraitCollection(_ traitCollection: UITraitCollection!) -> UIModalPresentationStyle ``` |
| To | ``` func adaptivePresentationStyleForTraitCollection(_ traitCollection: UITraitCollection) -> UIModalPresentationStyle ``` |

Modified [UIPresentationController.containerView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618332-containerview)

|  | Declaration |
| --- | --- |
| From | ``` var containerView: UIView! { get } ``` |
| To | ``` var containerView: UIView? { get } ``` |

Modified [UIPresentationController.delegate](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618329-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UIAdaptivePresentationControllerDelegate? ``` |
| To | ``` weak var delegate: UIAdaptivePresentationControllerDelegate? ``` |

Modified [UIPresentationController.init(presentedViewController: UIViewController, presentingViewController: UIViewController)](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618328-initwithpresentedviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` init(presentedViewController presentedViewController: UIViewController!, presentingViewController presentingViewController: UIViewController!) ``` |
| To | ``` init(presentedViewController presentedViewController: UIViewController, presentingViewController presentingViewController: UIViewController) ``` |

Modified [UIPresentationController.presentedView() -> UIView?](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618321-presentedview)

|  | Declaration |
| --- | --- |
| From | ``` func presentedView() -> UIView! ``` |
| To | ``` func presentedView() -> UIView? ``` |

Modified [UIPrinter](https://developer.apple.com/documentation/uikit/uiprinter)

|  | Declaration |
| --- | --- |
| From | ``` class UIPrinter : NSObject {     init(URL url: NSURL) -> UIPrinter     class func printerWithURL(_ url: NSURL) -> UIPrinter     @NSCopying var URL: NSURL! { get }     var displayName: String? { get }     var displayLocation: String? { get }     var supportedJobTypes: UIPrinterJobTypes { get }     var makeAndModel: String? { get }     var supportsColor: Bool { get }     var supportsDuplex: Bool { get }     func contactPrinter(_ completionHandler: ((Bool) -> Void)!) } ``` |
| To | ``` class UIPrinter : NSObject {      init(URL url: NSURL)     class func printerWithURL(_ url: NSURL) -> UIPrinter     @NSCopying var URL: NSURL { get }     var displayName: String { get }     var displayLocation: String? { get }     var supportedJobTypes: UIPrinterJobTypes { get }     var makeAndModel: String? { get }     var supportsColor: Bool { get }     var supportsDuplex: Bool { get }     func contactPrinter(_ completionHandler: ((Bool) -> Void)?) } ``` |

Modified [UIPrinter.contactPrinter(_: ((Bool) -> Void)?)](https://developer.apple.com/documentation/uikit/uiprinter/1620431-contactprinter)

|  | Declaration |
| --- | --- |
| From | ``` func contactPrinter(_ completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func contactPrinter(_ completionHandler: ((Bool) -> Void)?) ``` |

Modified [UIPrinter.displayName](https://developer.apple.com/documentation/uikit/uiprinter/1620427-displayname)

|  | Declaration |
| --- | --- |
| From | ``` var displayName: String? { get } ``` |
| To | ``` var displayName: String { get } ``` |

Modified [UIPrinter.init(URL: NSURL)](https://developer.apple.com/documentation/uikit/uiprinter/1620442-init)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL) -> UIPrinter ``` |
| To | ``` init(URL url: NSURL) ``` |

Modified [UIPrinter.URL](https://developer.apple.com/documentation/uikit/uiprinter/1620440-url)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL { get } ``` |

Modified [UIPrinterJobTypes [struct]](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIPrinterJobTypes : RawOptionSetType {     init(_ rawValue: Int)     init(rawValue rawValue: Int)     static var Unknown: UIPrinterJobTypes { get }     static var Document: UIPrinterJobTypes { get }     static var Envelope: UIPrinterJobTypes { get }     static var Label: UIPrinterJobTypes { get }     static var Photo: UIPrinterJobTypes { get }     static var Receipt: UIPrinterJobTypes { get }     static var Roll: UIPrinterJobTypes { get }     static var LargeFormat: UIPrinterJobTypes { get }     static var Postcard: UIPrinterJobTypes { get } } ``` | RawOptionSetType |
| To | ``` struct UIPrinterJobTypes : OptionSetType {     init(rawValue rawValue: Int)     static var Unknown: UIPrinterJobTypes { get }     static var Document: UIPrinterJobTypes { get }     static var Envelope: UIPrinterJobTypes { get }     static var Label: UIPrinterJobTypes { get }     static var Photo: UIPrinterJobTypes { get }     static var Receipt: UIPrinterJobTypes { get }     static var Roll: UIPrinterJobTypes { get }     static var LargeFormat: UIPrinterJobTypes { get }     static var Postcard: UIPrinterJobTypes { get } } ``` | OptionSetType |

Modified [UIPrinterPickerController](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIPrinterPickerController : NSObject {     init!(initiallySelectedPrinter printer: UIPrinter!) -> UIPrinterPickerController     class func printerPickerControllerWithInitiallySelectedPrinter(_ printer: UIPrinter!) -> UIPrinterPickerController!     var selectedPrinter: UIPrinter? { get }     unowned(unsafe) var delegate: UIPrinterPickerControllerDelegate?     func presentAnimated(_ animated: Bool, completionHandler completion: UIPrinterPickerCompletionHandler?) -> Bool     func presentFromRect(_ rect: CGRect, inView view: UIView!, animated animated: Bool, completionHandler completion: UIPrinterPickerCompletionHandler!) -> Bool     func presentFromBarButtonItem(_ item: UIBarButtonItem!, animated animated: Bool, completionHandler completion: UIPrinterPickerCompletionHandler?) -> Bool     func dismissAnimated(_ animated: Bool) } ``` |
| To | ``` class UIPrinterPickerController : NSObject {      init(initiallySelectedPrinter printer: UIPrinter?)     class func printerPickerControllerWithInitiallySelectedPrinter(_ printer: UIPrinter?) -> UIPrinterPickerController     var selectedPrinter: UIPrinter? { get }     weak var delegate: UIPrinterPickerControllerDelegate?     func presentAnimated(_ animated: Bool, completionHandler completion: UIPrinterPickerCompletionHandler?) -> Bool     func presentFromRect(_ rect: CGRect, inView view: UIView, animated animated: Bool, completionHandler completion: UIPrinterPickerCompletionHandler?) -> Bool     func presentFromBarButtonItem(_ item: UIBarButtonItem, animated animated: Bool, completionHandler completion: UIPrinterPickerCompletionHandler?) -> Bool     func dismissAnimated(_ animated: Bool) } ``` |

Modified [UIPrinterPickerController.delegate](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620511-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UIPrinterPickerControllerDelegate? ``` |
| To | ``` weak var delegate: UIPrinterPickerControllerDelegate? ``` |

Modified [UIPrinterPickerController.init(initiallySelectedPrinter: UIPrinter?)](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620517-printerpickercontrollerwithiniti)

|  | Declaration |
| --- | --- |
| From | ``` init!(initiallySelectedPrinter printer: UIPrinter!) -> UIPrinterPickerController ``` |
| To | ``` init(initiallySelectedPrinter printer: UIPrinter?) ``` |

Modified [UIPrinterPickerController.presentFromBarButtonItem(_: UIBarButtonItem, animated: Bool, completionHandler: UIPrinterPickerCompletionHandler?) -> Bool](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620507-presentfrombarbuttonitem)

|  | Declaration |
| --- | --- |
| From | ``` func presentFromBarButtonItem(_ item: UIBarButtonItem!, animated animated: Bool, completionHandler completion: UIPrinterPickerCompletionHandler?) -> Bool ``` |
| To | ``` func presentFromBarButtonItem(_ item: UIBarButtonItem, animated animated: Bool, completionHandler completion: UIPrinterPickerCompletionHandler?) -> Bool ``` |

Modified [UIPrinterPickerController.presentFromRect(_: CGRect, inView: UIView, animated: Bool, completionHandler: UIPrinterPickerCompletionHandler?) -> Bool](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/1620515-presentfromrect)

|  | Declaration |
| --- | --- |
| From | ``` func presentFromRect(_ rect: CGRect, inView view: UIView!, animated animated: Bool, completionHandler completion: UIPrinterPickerCompletionHandler!) -> Bool ``` |
| To | ``` func presentFromRect(_ rect: CGRect, inView view: UIView, animated animated: Bool, completionHandler completion: UIPrinterPickerCompletionHandler?) -> Bool ``` |

Modified [UIPrinterPickerControllerDelegate](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIPrinterPickerControllerDelegate : NSObjectProtocol {     optional func printerPickerControllerParentViewController(_ printerPickerController: UIPrinterPickerController) -> UIViewController!     optional func printerPickerController(_ printerPickerController: UIPrinterPickerController, shouldShowPrinter printer: UIPrinter) -> Bool     optional func printerPickerControllerWillPresent(_ printerPickerController: UIPrinterPickerController)     optional func printerPickerControllerDidPresent(_ printerPickerController: UIPrinterPickerController)     optional func printerPickerControllerWillDismiss(_ printerPickerController: UIPrinterPickerController)     optional func printerPickerControllerDidDismiss(_ printerPickerController: UIPrinterPickerController)     optional func printerPickerControllerDidSelectPrinter(_ printerPickerController: UIPrinterPickerController) } ``` |
| To | ``` protocol UIPrinterPickerControllerDelegate : NSObjectProtocol {     optional func printerPickerControllerParentViewController(_ printerPickerController: UIPrinterPickerController) -> UIViewController?     optional func printerPickerController(_ printerPickerController: UIPrinterPickerController, shouldShowPrinter printer: UIPrinter) -> Bool     optional func printerPickerControllerWillPresent(_ printerPickerController: UIPrinterPickerController)     optional func printerPickerControllerDidPresent(_ printerPickerController: UIPrinterPickerController)     optional func printerPickerControllerWillDismiss(_ printerPickerController: UIPrinterPickerController)     optional func printerPickerControllerDidDismiss(_ printerPickerController: UIPrinterPickerController)     optional func printerPickerControllerDidSelectPrinter(_ printerPickerController: UIPrinterPickerController) } ``` |

Modified [UIPrinterPickerControllerDelegate.printerPickerControllerParentViewController(_: UIPrinterPickerController) -> UIViewController?](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/1620518-printerpickercontrollerparentvie)

|  | Declaration |
| --- | --- |
| From | ``` optional func printerPickerControllerParentViewController(_ printerPickerController: UIPrinterPickerController) -> UIViewController! ``` |
| To | ``` optional func printerPickerControllerParentViewController(_ printerPickerController: UIPrinterPickerController) -> UIViewController? ``` |

Modified [UIPrintFormatter](https://developer.apple.com/documentation/uikit/uiprintformatter)

|  | Declaration |
| --- | --- |
| From | ``` class UIPrintFormatter : NSObject, NSCopying {     unowned(unsafe) var printPageRenderer: UIPrintPageRenderer! { get }     func removeFromPrintPageRenderer()     var maximumContentHeight: CGFloat     var maximumContentWidth: CGFloat     var contentInsets: UIEdgeInsets     var perPageContentInsets: UIEdgeInsets     var startPage: Int     var pageCount: Int { get }     func rectForPageAtIndex(_ pageIndex: Int) -> CGRect     func drawInRect(_ rect: CGRect, forPageAtIndex pageIndex: Int) } ``` |
| To | ``` class UIPrintFormatter : NSObject, NSCopying {     weak var printPageRenderer: UIPrintPageRenderer? { get }     func removeFromPrintPageRenderer()     var maximumContentHeight: CGFloat     var maximumContentWidth: CGFloat     var contentInsets: UIEdgeInsets     var perPageContentInsets: UIEdgeInsets     var startPage: Int     var pageCount: Int { get }     func rectForPageAtIndex(_ pageIndex: Int) -> CGRect     func drawInRect(_ rect: CGRect, forPageAtIndex pageIndex: Int) } ``` |

Modified [UIPrintFormatter.printPageRenderer](https://developer.apple.com/documentation/uikit/uiprintformatter/1621821-printpagerenderer)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var printPageRenderer: UIPrintPageRenderer! { get } ``` |
| To | ``` weak var printPageRenderer: UIPrintPageRenderer? { get } ``` |

Modified [UIPrintInfo](https://developer.apple.com/documentation/uikit/uiprintinfo)

|  | Declaration |
| --- | --- |
| From | ``` class UIPrintInfo : NSObject, NSCopying, NSCoding {     class func printInfo() -> UIPrintInfo!     init!(dictionary dictionary: [NSObject : AnyObject]?) -> UIPrintInfo     class func printInfoWithDictionary(_ dictionary: [NSObject : AnyObject]?) -> UIPrintInfo!     func dictionaryRepresentation() -> [NSObject : AnyObject]?     var printerID: String?     var jobName: String!     var outputType: UIPrintInfoOutputType     var orientation: UIPrintInfoOrientation     var duplex: UIPrintInfoDuplex } ``` |
| To | ``` class UIPrintInfo : NSObject, NSCopying, NSCoding {     init?(coder aDecoder: NSCoder)     class func printInfo() -> UIPrintInfo      init(dictionary dictionary: [NSObject : AnyObject]?)     class func printInfoWithDictionary(_ dictionary: [NSObject : AnyObject]?) -> UIPrintInfo     func dictionaryRepresentation() -> [NSObject : AnyObject]     var printerID: String?     var jobName: String     var outputType: UIPrintInfoOutputType     var orientation: UIPrintInfoOrientation     var duplex: UIPrintInfoDuplex } ``` |

Modified [UIPrintInfo.dictionaryRepresentation() -> [NSObject : AnyObject]](https://developer.apple.com/documentation/uikit/uiprintinfo/1623539-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` func dictionaryRepresentation() -> [NSObject : AnyObject]? ``` |
| To | ``` func dictionaryRepresentation() -> [NSObject : AnyObject] ``` |

Modified [UIPrintInfo.init(dictionary: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/uikit/uiprintinfo/1623553-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(dictionary dictionary: [NSObject : AnyObject]?) -> UIPrintInfo ``` |
| To | ``` init(dictionary dictionary: [NSObject : AnyObject]?) ``` |

Modified [UIPrintInfo.jobName](https://developer.apple.com/documentation/uikit/uiprintinfo/1623543-jobname)

|  | Declaration |
| --- | --- |
| From | ``` var jobName: String! ``` |
| To | ``` var jobName: String ``` |

Modified [UIPrintInfo.printInfo() -> UIPrintInfo [class]](https://developer.apple.com/documentation/uikit/uiprintinfo/1623545-printinfo)

|  | Declaration |
| --- | --- |
| From | ``` class func printInfo() -> UIPrintInfo! ``` |
| To | ``` class func printInfo() -> UIPrintInfo ``` |

Modified [UIPrintInfoDuplex [enum]](https://developer.apple.com/documentation/uikit/uiprintinfo/duplex)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIPrintInfoOrientation [enum]](https://developer.apple.com/documentation/uikit/uiprintinfoorientation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIPrintInfoOutputType [enum]](https://developer.apple.com/documentation/uikit/uiprintinfooutputtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIPrintInfoOutputType.PhotoGrayscale](https://developer.apple.com/documentation/uikit/uiprintinfo/outputtype/photograyscale)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified [UIPrintInteractionController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIPrintInteractionController : NSObject {     class func isPrintingAvailable() -> Bool     class func printableUTIs() -> Set<NSObject>     class func canPrintURL(_ url: NSURL) -> Bool     class func canPrintData(_ data: NSData) -> Bool     class func sharedPrintController() -> UIPrintInteractionController?     var printInfo: UIPrintInfo!     unowned(unsafe) var delegate: UIPrintInteractionControllerDelegate?     var showsPageRange: Bool     var showsNumberOfCopies: Bool     var showsPaperSelectionForLoadedPapers: Bool     var printPaper: UIPrintPaper! { get }     var printPageRenderer: UIPrintPageRenderer!     var printFormatter: UIPrintFormatter!     @NSCopying var printingItem: AnyObject!     var printingItems: [AnyObject]!     func presentAnimated(_ animated: Bool, completionHandler completion: UIPrintInteractionCompletionHandler?) -> Bool     func presentFromRect(_ rect: CGRect, inView view: UIView, animated animated: Bool, completionHandler completion: UIPrintInteractionCompletionHandler?) -> Bool     func presentFromBarButtonItem(_ item: UIBarButtonItem, animated animated: Bool, completionHandler completion: UIPrintInteractionCompletionHandler?) -> Bool     func printToPrinter(_ printer: UIPrinter, completionHandler completion: UIPrintInteractionCompletionHandler?) -> Bool     func dismissAnimated(_ animated: Bool) } ``` |
| To | ``` class UIPrintInteractionController : NSObject {     class func isPrintingAvailable() -> Bool     class func printableUTIs() -> Set<String>     class func canPrintURL(_ url: NSURL) -> Bool     class func canPrintData(_ data: NSData) -> Bool     class func sharedPrintController() -> UIPrintInteractionController     var printInfo: UIPrintInfo?     weak var delegate: UIPrintInteractionControllerDelegate?     var showsPageRange: Bool     var showsNumberOfCopies: Bool     var showsPaperSelectionForLoadedPapers: Bool     var printPaper: UIPrintPaper? { get }     var printPageRenderer: UIPrintPageRenderer?     var printFormatter: UIPrintFormatter?     @NSCopying var printingItem: AnyObject?     var printingItems: [AnyObject]?     func presentAnimated(_ animated: Bool, completionHandler completion: UIPrintInteractionCompletionHandler?) -> Bool     func presentFromRect(_ rect: CGRect, inView view: UIView, animated animated: Bool, completionHandler completion: UIPrintInteractionCompletionHandler?) -> Bool     func presentFromBarButtonItem(_ item: UIBarButtonItem, animated animated: Bool, completionHandler completion: UIPrintInteractionCompletionHandler?) -> Bool     func printToPrinter(_ printer: UIPrinter, completionHandler completion: UIPrintInteractionCompletionHandler?) -> Bool     func dismissAnimated(_ animated: Bool) } ``` |

Modified [UIPrintInteractionController.delegate](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618153-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UIPrintInteractionControllerDelegate? ``` |
| To | ``` weak var delegate: UIPrintInteractionControllerDelegate? ``` |

Modified [UIPrintInteractionController.printableUTIs() -> Set<String> [class]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618150-printableutis)

|  | Declaration |
| --- | --- |
| From | ``` class func printableUTIs() -> Set<NSObject> ``` |
| To | ``` class func printableUTIs() -> Set<String> ``` |

Modified [UIPrintInteractionController.printFormatter](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618152-printformatter)

|  | Declaration |
| --- | --- |
| From | ``` var printFormatter: UIPrintFormatter! ``` |
| To | ``` var printFormatter: UIPrintFormatter? ``` |

Modified [UIPrintInteractionController.printInfo](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618171-printinfo)

|  | Declaration |
| --- | --- |
| From | ``` var printInfo: UIPrintInfo! ``` |
| To | ``` var printInfo: UIPrintInfo? ``` |

Modified [UIPrintInteractionController.printingItem](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618157-printingitem)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var printingItem: AnyObject! ``` |
| To | ``` @NSCopying var printingItem: AnyObject? ``` |

Modified [UIPrintInteractionController.printingItems](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618156-printingitems)

|  | Declaration |
| --- | --- |
| From | ``` var printingItems: [AnyObject]! ``` |
| To | ``` var printingItems: [AnyObject]? ``` |

Modified [UIPrintInteractionController.printPageRenderer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618148-printpagerenderer)

|  | Declaration |
| --- | --- |
| From | ``` var printPageRenderer: UIPrintPageRenderer! ``` |
| To | ``` var printPageRenderer: UIPrintPageRenderer? ``` |

Modified [UIPrintInteractionController.printPaper](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618165-printpaper)

|  | Declaration |
| --- | --- |
| From | ``` var printPaper: UIPrintPaper! { get } ``` |
| To | ``` var printPaper: UIPrintPaper? { get } ``` |

Modified [UIPrintInteractionController.sharedPrintController() -> UIPrintInteractionController [class]](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/1618159-sharedprintcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedPrintController() -> UIPrintInteractionController? ``` |
| To | ``` class func sharedPrintController() -> UIPrintInteractionController ``` |

Modified [UIPrintInteractionControllerDelegate](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIPrintInteractionControllerDelegate : NSObjectProtocol {     optional func printInteractionControllerParentViewController(_ printInteractionController: UIPrintInteractionController) -> UIViewController?     optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, choosePaper paperList: [AnyObject]) -> UIPrintPaper?     optional func printInteractionControllerWillPresentPrinterOptions(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionControllerDidPresentPrinterOptions(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionControllerWillDismissPrinterOptions(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionControllerDidDismissPrinterOptions(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionControllerWillStartJob(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionControllerDidFinishJob(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, cutLengthForPaper paper: UIPrintPaper) -> CGFloat } ``` |
| To | ``` protocol UIPrintInteractionControllerDelegate : NSObjectProtocol {     optional func printInteractionControllerParentViewController(_ printInteractionController: UIPrintInteractionController) -> UIViewController     optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, choosePaper paperList: [UIPrintPaper]) -> UIPrintPaper     optional func printInteractionControllerWillPresentPrinterOptions(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionControllerDidPresentPrinterOptions(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionControllerWillDismissPrinterOptions(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionControllerDidDismissPrinterOptions(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionControllerWillStartJob(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionControllerDidFinishJob(_ printInteractionController: UIPrintInteractionController)     optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, cutLengthForPaper paper: UIPrintPaper) -> CGFloat     optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, chooseCutterBehavior availableBehaviors: [AnyObject]) -> UIPrinterCutterBehavior } ``` |

Modified [UIPrintInteractionControllerDelegate.printInteractionController(_: UIPrintInteractionController, choosePaper: [UIPrintPaper]) -> UIPrintPaper](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618160-printinteractioncontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, choosePaper paperList: [AnyObject]) -> UIPrintPaper? ``` | iOS 8.0 |
| To | ``` optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, choosePaper paperList: [UIPrintPaper]) -> UIPrintPaper ``` | iOS 4.2 |

Modified [UIPrintInteractionControllerDelegate.printInteractionControllerDidDismissPrinterOptions(_: UIPrintInteractionController)](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618175-printinteractioncontrollerdiddis)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified [UIPrintInteractionControllerDelegate.printInteractionControllerDidFinishJob(_: UIPrintInteractionController)](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618154-printinteractioncontrollerdidfin)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified [UIPrintInteractionControllerDelegate.printInteractionControllerDidPresentPrinterOptions(_: UIPrintInteractionController)](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618158-printinteractioncontrollerdidpre)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified [UIPrintInteractionControllerDelegate.printInteractionControllerParentViewController(_: UIPrintInteractionController) -> UIViewController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618162-printinteractioncontrollerparent)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func printInteractionControllerParentViewController(_ printInteractionController: UIPrintInteractionController) -> UIViewController? ``` | iOS 8.0 |
| To | ``` optional func printInteractionControllerParentViewController(_ printInteractionController: UIPrintInteractionController) -> UIViewController ``` | iOS 4.2 |

Modified [UIPrintInteractionControllerDelegate.printInteractionControllerWillDismissPrinterOptions(_: UIPrintInteractionController)](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618151-printinteractioncontrollerwilldi)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified [UIPrintInteractionControllerDelegate.printInteractionControllerWillPresentPrinterOptions(_: UIPrintInteractionController)](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618168-printinteractioncontrollerwillpr)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified [UIPrintInteractionControllerDelegate.printInteractionControllerWillStartJob(_: UIPrintInteractionController)](https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/1618185-printinteractioncontrollerwillst)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified [UIPrintPageRenderer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer)

|  | Declaration |
| --- | --- |
| From | ``` class UIPrintPageRenderer : NSObject {     var headerHeight: CGFloat     var footerHeight: CGFloat     var paperRect: CGRect { get }     var printableRect: CGRect { get }     var printFormatters: [AnyObject]!     func printFormattersForPageAtIndex(_ pageIndex: Int) -> [AnyObject]!     func addPrintFormatter(_ formatter: UIPrintFormatter!, startingAtPageAtIndex pageIndex: Int)     func numberOfPages() -> Int     func prepareForDrawingPages(_ range: NSRange)     func drawPageAtIndex(_ pageIndex: Int, inRect printableRect: CGRect)     func drawPrintFormatter(_ printFormatter: UIPrintFormatter!, forPageAtIndex pageIndex: Int)     func drawHeaderForPageAtIndex(_ pageIndex: Int, inRect headerRect: CGRect)     func drawContentForPageAtIndex(_ pageIndex: Int, inRect contentRect: CGRect)     func drawFooterForPageAtIndex(_ pageIndex: Int, inRect footerRect: CGRect) } ``` |
| To | ``` class UIPrintPageRenderer : NSObject {     var headerHeight: CGFloat     var footerHeight: CGFloat     var paperRect: CGRect { get }     var printableRect: CGRect { get }     var printFormatters: [UIPrintFormatter]?     func printFormattersForPageAtIndex(_ pageIndex: Int) -> [UIPrintFormatter]?     func addPrintFormatter(_ formatter: UIPrintFormatter, startingAtPageAtIndex pageIndex: Int)     func numberOfPages() -> Int     func prepareForDrawingPages(_ range: NSRange)     func drawPageAtIndex(_ pageIndex: Int, inRect printableRect: CGRect)     func drawPrintFormatter(_ printFormatter: UIPrintFormatter, forPageAtIndex pageIndex: Int)     func drawHeaderForPageAtIndex(_ pageIndex: Int, inRect headerRect: CGRect)     func drawContentForPageAtIndex(_ pageIndex: Int, inRect contentRect: CGRect)     func drawFooterForPageAtIndex(_ pageIndex: Int, inRect footerRect: CGRect) } ``` |

Modified [UIPrintPageRenderer.addPrintFormatter(_: UIPrintFormatter, startingAtPageAtIndex: Int)](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621632-addprintformatter)

|  | Declaration |
| --- | --- |
| From | ``` func addPrintFormatter(_ formatter: UIPrintFormatter!, startingAtPageAtIndex pageIndex: Int) ``` |
| To | ``` func addPrintFormatter(_ formatter: UIPrintFormatter, startingAtPageAtIndex pageIndex: Int) ``` |

Modified [UIPrintPageRenderer.drawPrintFormatter(_: UIPrintFormatter, forPageAtIndex: Int)](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621644-drawprintformatter)

|  | Declaration |
| --- | --- |
| From | ``` func drawPrintFormatter(_ printFormatter: UIPrintFormatter!, forPageAtIndex pageIndex: Int) ``` |
| To | ``` func drawPrintFormatter(_ printFormatter: UIPrintFormatter, forPageAtIndex pageIndex: Int) ``` |

Modified [UIPrintPageRenderer.printFormatters](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621640-printformatters)

|  | Declaration |
| --- | --- |
| From | ``` var printFormatters: [AnyObject]! ``` |
| To | ``` var printFormatters: [UIPrintFormatter]? ``` |

Modified [UIPrintPageRenderer.printFormattersForPageAtIndex(_: Int) -> [UIPrintFormatter]?](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/1621635-printformattersforpage)

|  | Declaration |
| --- | --- |
| From | ``` func printFormattersForPageAtIndex(_ pageIndex: Int) -> [AnyObject]! ``` |
| To | ``` func printFormattersForPageAtIndex(_ pageIndex: Int) -> [UIPrintFormatter]? ``` |

Modified [UIPrintPaper](https://developer.apple.com/documentation/uikit/uiprintpaper)

|  | Declaration |
| --- | --- |
| From | ``` class UIPrintPaper : NSObject {     class func bestPaperForPageSize(_ contentSize: CGSize, withPapersFromArray paperList: [AnyObject]!) -> UIPrintPaper?     var paperSize: CGSize { get }     var printableRect: CGRect { get } } extension UIPrintPaper {     func printRect() -> CGRect } ``` |
| To | ``` class UIPrintPaper : NSObject {     class func bestPaperForPageSize(_ contentSize: CGSize, withPapersFromArray paperList: [UIPrintPaper]) -> UIPrintPaper     var paperSize: CGSize { get }     var printableRect: CGRect { get } } extension UIPrintPaper {     func printRect() -> CGRect } ``` |

Modified [UIPrintPaper.bestPaperForPageSize(_: CGSize, withPapersFromArray: [UIPrintPaper]) -> UIPrintPaper [class]](https://developer.apple.com/documentation/uikit/uiprintpaper/1623527-bestpaperforpagesize)

|  | Declaration |
| --- | --- |
| From | ``` class func bestPaperForPageSize(_ contentSize: CGSize, withPapersFromArray paperList: [AnyObject]!) -> UIPrintPaper? ``` |
| To | ``` class func bestPaperForPageSize(_ contentSize: CGSize, withPapersFromArray paperList: [UIPrintPaper]) -> UIPrintPaper ``` |

Modified [UIProgressView](https://developer.apple.com/documentation/uikit/uiprogressview)

|  | Declaration |
| --- | --- |
| From | ``` class UIProgressView : UIView, NSCoding {     init(progressViewStyle style: UIProgressViewStyle)     var progressViewStyle: UIProgressViewStyle     var progress: Float     var progressTintColor: UIColor?     var trackTintColor: UIColor?     var progressImage: UIImage?     var trackImage: UIImage?     func setProgress(_ progress: Float, animated animated: Bool) } ``` |
| To | ``` class UIProgressView : UIView {     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     convenience init(progressViewStyle style: UIProgressViewStyle)     var progressViewStyle: UIProgressViewStyle     var progress: Float     var progressTintColor: UIColor?     var trackTintColor: UIColor?     var progressImage: UIImage?     var trackImage: UIImage?     func setProgress(_ progress: Float, animated animated: Bool)     var observedProgress: NSProgress? } ``` |

Modified [UIProgressView.init(progressViewStyle: UIProgressViewStyle)](https://developer.apple.com/documentation/uikit/uiprogressview/1619833-initwithprogressviewstyle)

|  | Declaration |
| --- | --- |
| From | ``` init(progressViewStyle style: UIProgressViewStyle) ``` |
| To | ``` convenience init(progressViewStyle style: UIProgressViewStyle) ``` |

Modified [UIProgressViewStyle [enum]](https://developer.apple.com/documentation/uikit/uiprogressviewstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIPushBehavior](https://developer.apple.com/documentation/uikit/uipushbehavior)

|  | Declaration |
| --- | --- |
| From | ``` class UIPushBehavior : UIDynamicBehavior {     init!(items items: [AnyObject]!, mode mode: UIPushBehaviorMode)     func addItem(_ item: UIDynamicItem)     func removeItem(_ item: UIDynamicItem)     var items: [AnyObject] { get }     func targetOffsetFromCenterForItem(_ item: UIDynamicItem) -> UIOffset     func setTargetOffsetFromCenter(_ o: UIOffset, forItem item: UIDynamicItem)     var mode: UIPushBehaviorMode { get }     var active: Bool     var angle: CGFloat     var magnitude: CGFloat     var pushDirection: CGVector     func setAngle(_ angle: CGFloat, magnitude magnitude: CGFloat) } ``` |
| To | ``` class UIPushBehavior : UIDynamicBehavior {     init(items items: [UIDynamicItem], mode mode: UIPushBehaviorMode)     func addItem(_ item: UIDynamicItem)     func removeItem(_ item: UIDynamicItem)     var items: [UIDynamicItem] { get }     func targetOffsetFromCenterForItem(_ item: UIDynamicItem) -> UIOffset     func setTargetOffsetFromCenter(_ o: UIOffset, forItem item: UIDynamicItem)     var mode: UIPushBehaviorMode { get }     var active: Bool     var angle: CGFloat     var magnitude: CGFloat     var pushDirection: CGVector     func setAngle(_ angle: CGFloat, magnitude magnitude: CGFloat) } ``` |

Modified [UIPushBehavior.init(items: [UIDynamicItem], mode: UIPushBehaviorMode)](https://developer.apple.com/documentation/uikit/uipushbehavior/1623329-initwithitems)

|  | Declaration |
| --- | --- |
| From | ``` init!(items items: [AnyObject]!, mode mode: UIPushBehaviorMode) ``` |
| To | ``` init(items items: [UIDynamicItem], mode mode: UIPushBehaviorMode) ``` |

Modified [UIPushBehavior.items](https://developer.apple.com/documentation/uikit/uipushbehavior/1623339-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject] { get } ``` |
| To | ``` var items: [UIDynamicItem] { get } ``` |

Modified [UIPushBehaviorMode [enum]](https://developer.apple.com/documentation/uikit/uipushbehavior/mode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIRectCorner [struct]](https://developer.apple.com/documentation/uikit/uirectcorner)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIRectCorner : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var TopLeft: UIRectCorner { get }     static var TopRight: UIRectCorner { get }     static var BottomLeft: UIRectCorner { get }     static var BottomRight: UIRectCorner { get }     static var AllCorners: UIRectCorner { get } } ``` | RawOptionSetType |
| To | ``` struct UIRectCorner : OptionSetType {     init(rawValue rawValue: UInt)     static var TopLeft: UIRectCorner { get }     static var TopRight: UIRectCorner { get }     static var BottomLeft: UIRectCorner { get }     static var BottomRight: UIRectCorner { get }     static var AllCorners: UIRectCorner { get } } ``` | OptionSetType |

Modified [UIRectEdge [struct]](https://developer.apple.com/documentation/uikit/uirectedge)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIRectEdge : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: UIRectEdge { get }     static var Top: UIRectEdge { get }     static var Left: UIRectEdge { get }     static var Bottom: UIRectEdge { get }     static var Right: UIRectEdge { get }     static var All: UIRectEdge { get } } ``` | RawOptionSetType |
| To | ``` struct UIRectEdge : OptionSetType {     init(rawValue rawValue: UInt)     static var None: UIRectEdge { get }     static var Top: UIRectEdge { get }     static var Left: UIRectEdge { get }     static var Bottom: UIRectEdge { get }     static var Right: UIRectEdge { get }     static var All: UIRectEdge { get } } ``` | OptionSetType |

Modified [UIReferenceLibraryViewController](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIReferenceLibraryViewController : UIViewController {     class func dictionaryHasDefinitionForTerm(_ term: String) -> Bool     init(term term: String) } ``` |
| To | ``` class UIReferenceLibraryViewController : UIViewController {     class func dictionaryHasDefinitionForTerm(_ term: String) -> Bool     init(term term: String)     init(coder aDecoder: NSCoder)     convenience init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     convenience init() } ``` |

Modified [UIRemoteNotificationType [struct]](https://developer.apple.com/documentation/uikit/uiremotenotificationtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIRemoteNotificationType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: UIRemoteNotificationType { get }     static var Badge: UIRemoteNotificationType { get }     static var Sound: UIRemoteNotificationType { get }     static var Alert: UIRemoteNotificationType { get }     static var NewsstandContentAvailability: UIRemoteNotificationType { get } } ``` | RawOptionSetType |
| To | ``` struct UIRemoteNotificationType : OptionSetType {     init(rawValue rawValue: UInt)     static var None: UIRemoteNotificationType { get }     static var Badge: UIRemoteNotificationType { get }     static var Sound: UIRemoteNotificationType { get }     static var Alert: UIRemoteNotificationType { get }     static var NewsstandContentAvailability: UIRemoteNotificationType { get } } ``` | OptionSetType |

Modified [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder)

|  | Declaration |
| --- | --- |
| From | ``` class UIResponder : NSObject {     func nextResponder() -> UIResponder?     func canBecomeFirstResponder() -> Bool     func becomeFirstResponder() -> Bool     func canResignFirstResponder() -> Bool     func resignFirstResponder() -> Bool     func isFirstResponder() -> Bool     func touchesBegan(_ touches: Set<NSObject>, withEvent event: UIEvent)     func touchesMoved(_ touches: Set<NSObject>, withEvent event: UIEvent)     func touchesEnded(_ touches: Set<NSObject>, withEvent event: UIEvent)     func touchesCancelled(_ touches: Set<NSObject>!, withEvent event: UIEvent!)     func motionBegan(_ motion: UIEventSubtype, withEvent event: UIEvent)     func motionEnded(_ motion: UIEventSubtype, withEvent event: UIEvent)     func motionCancelled(_ motion: UIEventSubtype, withEvent event: UIEvent)     func remoteControlReceivedWithEvent(_ event: UIEvent)     func canPerformAction(_ action: Selector, withSender sender: AnyObject?) -> Bool     func targetForAction(_ action: Selector, withSender sender: AnyObject?) -> AnyObject?     var undoManager: NSUndoManager? { get } } extension UIResponder {     var keyCommands: [AnyObject]? { get } } extension UIResponder {     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews() } extension UIResponder {     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity) } ``` |
| To | ``` class UIResponder : NSObject {     func nextResponder() -> UIResponder?     func canBecomeFirstResponder() -> Bool     func becomeFirstResponder() -> Bool     func canResignFirstResponder() -> Bool     func resignFirstResponder() -> Bool     func isFirstResponder() -> Bool     func touchesBegan(_ touches: Set<UITouch>, withEvent event: UIEvent?)     func touchesMoved(_ touches: Set<UITouch>, withEvent event: UIEvent?)     func touchesEnded(_ touches: Set<UITouch>, withEvent event: UIEvent?)     func touchesCancelled(_ touches: Set<UITouch>?, withEvent event: UIEvent?)     func motionBegan(_ motion: UIEventSubtype, withEvent event: UIEvent?)     func motionEnded(_ motion: UIEventSubtype, withEvent event: UIEvent?)     func motionCancelled(_ motion: UIEventSubtype, withEvent event: UIEvent?)     func remoteControlReceivedWithEvent(_ event: UIEvent?)     func canPerformAction(_ action: Selector, withSender sender: AnyObject?) -> Bool     func targetForAction(_ action: Selector, withSender sender: AnyObject?) -> AnyObject?     var undoManager: NSUndoManager? { get } } extension UIResponder {     var keyCommands: [UIKeyCommand]? { get } } extension UIResponder {     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews() } extension UIResponder {     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity) } ``` |

Modified [UIResponder.keyCommands](https://developer.apple.com/documentation/uikit/uiresponder/1621141-keycommands)

|  | Declaration |
| --- | --- |
| From | ``` var keyCommands: [AnyObject]? { get } ``` |
| To | ``` var keyCommands: [UIKeyCommand]? { get } ``` |

Modified [UIResponder.motionBegan(_: UIEventSubtype, withEvent: UIEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621120-motionbegan)

|  | Declaration |
| --- | --- |
| From | ``` func motionBegan(_ motion: UIEventSubtype, withEvent event: UIEvent) ``` |
| To | ``` func motionBegan(_ motion: UIEventSubtype, withEvent event: UIEvent?) ``` |

Modified [UIResponder.motionCancelled(_: UIEventSubtype, withEvent: UIEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621087-motioncancelled)

|  | Declaration |
| --- | --- |
| From | ``` func motionCancelled(_ motion: UIEventSubtype, withEvent event: UIEvent) ``` |
| To | ``` func motionCancelled(_ motion: UIEventSubtype, withEvent event: UIEvent?) ``` |

Modified [UIResponder.motionEnded(_: UIEventSubtype, withEvent: UIEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621090-motionended)

|  | Declaration |
| --- | --- |
| From | ``` func motionEnded(_ motion: UIEventSubtype, withEvent event: UIEvent) ``` |
| To | ``` func motionEnded(_ motion: UIEventSubtype, withEvent event: UIEvent?) ``` |

Modified [UIResponder.remoteControlReceivedWithEvent(_: UIEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621118-remotecontrolreceivedwithevent)

|  | Declaration |
| --- | --- |
| From | ``` func remoteControlReceivedWithEvent(_ event: UIEvent) ``` |
| To | ``` func remoteControlReceivedWithEvent(_ event: UIEvent?) ``` |

Modified [UIResponder.touchesBegan(_: Set<UITouch>, withEvent: UIEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621142-touchesbegan)

|  | Declaration |
| --- | --- |
| From | ``` func touchesBegan(_ touches: Set<NSObject>, withEvent event: UIEvent) ``` |
| To | ``` func touchesBegan(_ touches: Set<UITouch>, withEvent event: UIEvent?) ``` |

Modified [UIResponder.touchesCancelled(_: Set<UITouch>?, withEvent: UIEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621116-touchescancelled)

|  | Declaration |
| --- | --- |
| From | ``` func touchesCancelled(_ touches: Set<NSObject>!, withEvent event: UIEvent!) ``` |
| To | ``` func touchesCancelled(_ touches: Set<UITouch>?, withEvent event: UIEvent?) ``` |

Modified [UIResponder.touchesEnded(_: Set<UITouch>, withEvent: UIEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621084-touchesended)

|  | Declaration |
| --- | --- |
| From | ``` func touchesEnded(_ touches: Set<NSObject>, withEvent event: UIEvent) ``` |
| To | ``` func touchesEnded(_ touches: Set<UITouch>, withEvent event: UIEvent?) ``` |

Modified [UIResponder.touchesMoved(_: Set<UITouch>, withEvent: UIEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621107-touchesmoved)

|  | Declaration |
| --- | --- |
| From | ``` func touchesMoved(_ touches: Set<NSObject>, withEvent event: UIEvent) ``` |
| To | ``` func touchesMoved(_ touches: Set<UITouch>, withEvent event: UIEvent?) ``` |

Modified [UIReturnKeyType [enum]](https://developer.apple.com/documentation/uikit/uireturnkeytype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum UIReturnKeyType : Int {     case Default     case Go     case Google     case Join     case Next     case Route     case Search     case Send     case Yahoo     case Done     case EmergencyCall } ``` | -- |
| To | ``` enum UIReturnKeyType : Int {     case Default     case Go     case Google     case Join     case Next     case Route     case Search     case Send     case Yahoo     case Done     case EmergencyCall     case Continue } ``` | Int |

Modified [UIScreen](https://developer.apple.com/documentation/uikit/uiscreen)

|  | Declaration |
| --- | --- |
| From | ``` class UIScreen : NSObject, UITraitEnvironment, NSObjectProtocol {     class func screens() -> [AnyObject]     class func mainScreen() -> UIScreen     var bounds: CGRect { get }     var applicationFrame: CGRect { get }     var scale: CGFloat { get }     var availableModes: [AnyObject] { get }     var preferredMode: UIScreenMode! { get }     var currentMode: UIScreenMode?     var overscanCompensation: UIScreenOverscanCompensation     var mirroredScreen: UIScreen? { get }     var brightness: CGFloat     var wantsSoftwareDimming: Bool     var coordinateSpace: UICoordinateSpace { get }     var fixedCoordinateSpace: UICoordinateSpace { get }     var nativeBounds: CGRect { get }     var nativeScale: CGFloat { get }     func displayLinkWithTarget(_ target: AnyObject!, selector sel: Selector) -> CADisplayLink! } extension UIScreen {     func snapshotViewAfterScreenUpdates(_ afterUpdates: Bool) -> UIView } ``` |
| To | ``` class UIScreen : NSObject, UITraitEnvironment {     class func screens() -> [UIScreen]     class func mainScreen() -> UIScreen     var bounds: CGRect { get }     var scale: CGFloat { get }     var availableModes: [UIScreenMode] { get }     var preferredMode: UIScreenMode? { get }     var currentMode: UIScreenMode?     var overscanCompensation: UIScreenOverscanCompensation     var overscanCompensationInsets: UIEdgeInsets { get }     var mirroredScreen: UIScreen? { get }     var brightness: CGFloat     var wantsSoftwareDimming: Bool     var coordinateSpace: UICoordinateSpace { get }     var fixedCoordinateSpace: UICoordinateSpace { get }     var nativeBounds: CGRect { get }     var nativeScale: CGFloat { get }     func displayLinkWithTarget(_ target: AnyObject, selector sel: Selector) -> CADisplayLink?     var applicationFrame: CGRect { get } } extension UIScreen {     func snapshotViewAfterScreenUpdates(_ afterUpdates: Bool) -> UIView } ``` |

Modified [UIScreen.applicationFrame](https://developer.apple.com/documentation/uikit/uiscreen/1617835-applicationframe)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [UIScreen.availableModes](https://developer.apple.com/documentation/uikit/uiscreen/1617839-availablemodes)

|  | Declaration |
| --- | --- |
| From | ``` var availableModes: [AnyObject] { get } ``` |
| To | ``` var availableModes: [UIScreenMode] { get } ``` |

Modified [UIScreen.displayLinkWithTarget(_: AnyObject, selector: Selector) -> CADisplayLink?](https://developer.apple.com/documentation/uikit/uiscreen/1617820-displaylinkwithtarget)

|  | Declaration |
| --- | --- |
| From | ``` func displayLinkWithTarget(_ target: AnyObject!, selector sel: Selector) -> CADisplayLink! ``` |
| To | ``` func displayLinkWithTarget(_ target: AnyObject, selector sel: Selector) -> CADisplayLink? ``` |

Modified [UIScreen.preferredMode](https://developer.apple.com/documentation/uikit/uiscreen/1617823-preferredmode)

|  | Declaration |
| --- | --- |
| From | ``` var preferredMode: UIScreenMode! { get } ``` |
| To | ``` var preferredMode: UIScreenMode? { get } ``` |

Modified [UIScreen.screens() -> [UIScreen] [class]](https://developer.apple.com/documentation/uikit/uiscreen/1617812-screens)

|  | Declaration |
| --- | --- |
| From | ``` class func screens() -> [AnyObject] ``` |
| To | ``` class func screens() -> [UIScreen] ``` |

Modified [UIScreenOverscanCompensation [enum]](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum UIScreenOverscanCompensation : Int {     case Scale     case InsetBounds     case InsetApplicationFrame } ``` | -- |
| To | ``` enum UIScreenOverscanCompensation : Int {     case Scale     case InsetBounds     case None     static var InsetApplicationFrame: UIScreenOverscanCompensation { get } } ``` | Int |

Modified [UIScreenOverscanCompensation.InsetApplicationFrame](https://developer.apple.com/documentation/uikit/uiscreenoverscancompensation/uiscreenoverscancompensationinsetapplicationframe)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` case InsetApplicationFrame ``` | iOS 8.0 | -- |
| To | ``` static var InsetApplicationFrame: UIScreenOverscanCompensation { get } ``` | iOS 5.0 | iOS 9.0 |

Modified [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview)

|  | Declaration |
| --- | --- |
| From | ``` class UIScrollView : UIView, NSCoding {     var contentOffset: CGPoint     var contentSize: CGSize     var contentInset: UIEdgeInsets     unowned(unsafe) var delegate: UIScrollViewDelegate?     var directionalLockEnabled: Bool     var bounces: Bool     var alwaysBounceVertical: Bool     var alwaysBounceHorizontal: Bool     var pagingEnabled: Bool     var scrollEnabled: Bool     var showsHorizontalScrollIndicator: Bool     var showsVerticalScrollIndicator: Bool     var scrollIndicatorInsets: UIEdgeInsets     var indicatorStyle: UIScrollViewIndicatorStyle     var decelerationRate: CGFloat     func setContentOffset(_ contentOffset: CGPoint, animated animated: Bool)     func scrollRectToVisible(_ rect: CGRect, animated animated: Bool)     func flashScrollIndicators()     var tracking: Bool { get }     var dragging: Bool { get }     var decelerating: Bool { get }     var delaysContentTouches: Bool     var canCancelContentTouches: Bool     func touchesShouldBegin(_ touches: Set<NSObject>!, withEvent event: UIEvent!, inContentView view: UIView!) -> Bool     func touchesShouldCancelInContentView(_ view: UIView!) -> Bool     var minimumZoomScale: CGFloat     var maximumZoomScale: CGFloat     var zoomScale: CGFloat     func setZoomScale(_ scale: CGFloat, animated animated: Bool)     func zoomToRect(_ rect: CGRect, animated animated: Bool)     var bouncesZoom: Bool     var zooming: Bool { get }     var zoomBouncing: Bool { get }     var scrollsToTop: Bool     var panGestureRecognizer: UIPanGestureRecognizer { get }     var pinchGestureRecognizer: UIPinchGestureRecognizer! { get }     var keyboardDismissMode: UIScrollViewKeyboardDismissMode } ``` |
| To | ``` class UIScrollView : UIView {     var contentOffset: CGPoint     var contentSize: CGSize     var contentInset: UIEdgeInsets     weak var delegate: UIScrollViewDelegate?     var directionalLockEnabled: Bool     var bounces: Bool     var alwaysBounceVertical: Bool     var alwaysBounceHorizontal: Bool     var pagingEnabled: Bool     var scrollEnabled: Bool     var showsHorizontalScrollIndicator: Bool     var showsVerticalScrollIndicator: Bool     var scrollIndicatorInsets: UIEdgeInsets     var indicatorStyle: UIScrollViewIndicatorStyle     var decelerationRate: CGFloat     func setContentOffset(_ contentOffset: CGPoint, animated animated: Bool)     func scrollRectToVisible(_ rect: CGRect, animated animated: Bool)     func flashScrollIndicators()     var tracking: Bool { get }     var dragging: Bool { get }     var decelerating: Bool { get }     var delaysContentTouches: Bool     var canCancelContentTouches: Bool     func touchesShouldBegin(_ touches: Set<UITouch>, withEvent event: UIEvent?, inContentView view: UIView) -> Bool     func touchesShouldCancelInContentView(_ view: UIView) -> Bool     var minimumZoomScale: CGFloat     var maximumZoomScale: CGFloat     var zoomScale: CGFloat     func setZoomScale(_ scale: CGFloat, animated animated: Bool)     func zoomToRect(_ rect: CGRect, animated animated: Bool)     var bouncesZoom: Bool     var zooming: Bool { get }     var zoomBouncing: Bool { get }     var scrollsToTop: Bool     var panGestureRecognizer: UIPanGestureRecognizer { get }     var pinchGestureRecognizer: UIPinchGestureRecognizer? { get }     var keyboardDismissMode: UIScrollViewKeyboardDismissMode } ``` |

Modified [UIScrollView.delegate](https://developer.apple.com/documentation/uikit/uiscrollview/1619430-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UIScrollViewDelegate? ``` |
| To | ``` weak var delegate: UIScrollViewDelegate? ``` |

Modified [UIScrollView.pinchGestureRecognizer](https://developer.apple.com/documentation/uikit/uiscrollview/1619381-pinchgesturerecognizer)

|  | Declaration |
| --- | --- |
| From | ``` var pinchGestureRecognizer: UIPinchGestureRecognizer! { get } ``` |
| To | ``` var pinchGestureRecognizer: UIPinchGestureRecognizer? { get } ``` |

Modified [UIScrollView.touchesShouldBegin(_: Set<UITouch>, withEvent: UIEvent?, inContentView: UIView) -> Bool](https://developer.apple.com/documentation/uikit/uiscrollview/1619418-touchesshouldbegin)

|  | Declaration |
| --- | --- |
| From | ``` func touchesShouldBegin(_ touches: Set<NSObject>!, withEvent event: UIEvent!, inContentView view: UIView!) -> Bool ``` |
| To | ``` func touchesShouldBegin(_ touches: Set<UITouch>, withEvent event: UIEvent?, inContentView view: UIView) -> Bool ``` |

Modified [UIScrollView.touchesShouldCancelInContentView(_: UIView) -> Bool](https://developer.apple.com/documentation/uikit/uiscrollview/1619387-touchesshouldcancelincontentview)

|  | Declaration |
| --- | --- |
| From | ``` func touchesShouldCancelInContentView(_ view: UIView!) -> Bool ``` |
| To | ``` func touchesShouldCancelInContentView(_ view: UIView) -> Bool ``` |

Modified [UIScrollViewAccessibilityDelegate](https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIScrollViewAccessibilityDelegate : UIScrollViewDelegate, NSObjectProtocol {     optional func accessibilityScrollStatusForScrollView(_ scrollView: UIScrollView!) -> String! } ``` |
| To | ``` protocol UIScrollViewAccessibilityDelegate : UIScrollViewDelegate, NSObjectProtocol {     optional func accessibilityScrollStatusForScrollView(_ scrollView: UIScrollView) -> String? } ``` |

Modified [UIScrollViewAccessibilityDelegate.accessibilityScrollStatusForScrollView(_: UIScrollView) -> String?](https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate/1621055-accessibilityscrollstatus)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func accessibilityScrollStatusForScrollView(_ scrollView: UIScrollView!) -> String! ``` | iOS 8.0 |
| To | ``` optional func accessibilityScrollStatusForScrollView(_ scrollView: UIScrollView) -> String? ``` | iOS 2.0 |

Modified [UIScrollViewDelegate](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIScrollViewDelegate : NSObjectProtocol {     optional func scrollViewDidScroll(_ scrollView: UIScrollView)     optional func scrollViewDidZoom(_ scrollView: UIScrollView)     optional func scrollViewWillBeginDragging(_ scrollView: UIScrollView)     optional func scrollViewWillEndDragging(_ scrollView: UIScrollView, withVelocity velocity: CGPoint, targetContentOffset targetContentOffset: UnsafeMutablePointer<CGPoint>)     optional func scrollViewDidEndDragging(_ scrollView: UIScrollView, willDecelerate decelerate: Bool)     optional func scrollViewWillBeginDecelerating(_ scrollView: UIScrollView)     optional func scrollViewDidEndDecelerating(_ scrollView: UIScrollView)     optional func scrollViewDidEndScrollingAnimation(_ scrollView: UIScrollView)     optional func viewForZoomingInScrollView(_ scrollView: UIScrollView) -> UIView?     optional func scrollViewWillBeginZooming(_ scrollView: UIScrollView, withView view: UIView!)     optional func scrollViewDidEndZooming(_ scrollView: UIScrollView, withView view: UIView!, atScale scale: CGFloat)     optional func scrollViewShouldScrollToTop(_ scrollView: UIScrollView) -> Bool     optional func scrollViewDidScrollToTop(_ scrollView: UIScrollView) } ``` |
| To | ``` protocol UIScrollViewDelegate : NSObjectProtocol {     optional func scrollViewDidScroll(_ scrollView: UIScrollView)     optional func scrollViewDidZoom(_ scrollView: UIScrollView)     optional func scrollViewWillBeginDragging(_ scrollView: UIScrollView)     optional func scrollViewWillEndDragging(_ scrollView: UIScrollView, withVelocity velocity: CGPoint, targetContentOffset targetContentOffset: UnsafeMutablePointer<CGPoint>)     optional func scrollViewDidEndDragging(_ scrollView: UIScrollView, willDecelerate decelerate: Bool)     optional func scrollViewWillBeginDecelerating(_ scrollView: UIScrollView)     optional func scrollViewDidEndDecelerating(_ scrollView: UIScrollView)     optional func scrollViewDidEndScrollingAnimation(_ scrollView: UIScrollView)     optional func viewForZoomingInScrollView(_ scrollView: UIScrollView) -> UIView?     optional func scrollViewWillBeginZooming(_ scrollView: UIScrollView, withView view: UIView?)     optional func scrollViewDidEndZooming(_ scrollView: UIScrollView, withView view: UIView?, atScale scale: CGFloat)     optional func scrollViewShouldScrollToTop(_ scrollView: UIScrollView) -> Bool     optional func scrollViewDidScrollToTop(_ scrollView: UIScrollView) } ``` |

Modified [UIScrollViewDelegate.scrollViewDidEndDecelerating(_: UIScrollView)](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619417-scrollviewdidenddecelerating)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIScrollViewDelegate.scrollViewDidEndDragging(_: UIScrollView, willDecelerate: Bool)](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619436-scrollviewdidenddragging)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIScrollViewDelegate.scrollViewDidEndScrollingAnimation(_: UIScrollView)](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619379-scrollviewdidendscrollinganimati)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIScrollViewDelegate.scrollViewDidEndZooming(_: UIScrollView, withView: UIView?, atScale: CGFloat)](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619407-scrollviewdidendzooming)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func scrollViewDidEndZooming(_ scrollView: UIScrollView, withView view: UIView!, atScale scale: CGFloat) ``` | iOS 8.0 |
| To | ``` optional func scrollViewDidEndZooming(_ scrollView: UIScrollView, withView view: UIView?, atScale scale: CGFloat) ``` | iOS 2.0 |

Modified [UIScrollViewDelegate.scrollViewDidScroll(_: UIScrollView)](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619392-scrollviewdidscroll)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIScrollViewDelegate.scrollViewDidScrollToTop(_: UIScrollView)](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619382-scrollviewdidscrolltotop)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIScrollViewDelegate.scrollViewShouldScrollToTop(_: UIScrollView) -> Bool](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619378-scrollviewshouldscrolltotop)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIScrollViewDelegate.scrollViewWillBeginDecelerating(_: UIScrollView)](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619386-scrollviewwillbegindecelerating)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIScrollViewDelegate.scrollViewWillBeginDragging(_: UIScrollView)](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619394-scrollviewwillbegindragging)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIScrollViewDelegate.scrollViewWillBeginZooming(_: UIScrollView, withView: UIView?)](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619396-scrollviewwillbeginzooming)

|  | Declaration |
| --- | --- |
| From | ``` optional func scrollViewWillBeginZooming(_ scrollView: UIScrollView, withView view: UIView!) ``` |
| To | ``` optional func scrollViewWillBeginZooming(_ scrollView: UIScrollView, withView view: UIView?) ``` |

Modified [UIScrollViewDelegate.viewForZoomingInScrollView(_: UIScrollView) -> UIView?](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/1619426-viewforzoominginscrollview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIScrollViewIndicatorStyle [enum]](https://developer.apple.com/documentation/uikit/uiscrollview/indicatorstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIScrollViewKeyboardDismissMode [enum]](https://developer.apple.com/documentation/uikit/uiscrollviewkeyboarddismissmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar)

|  | Declaration |
| --- | --- |
| From | ``` class UISearchBar : UIView, UIBarPositioning, NSObjectProtocol, UITextInputTraits {     var barStyle: UIBarStyle     unowned(unsafe) var delegate: UISearchBarDelegate?     var text: String!     var prompt: String?     var placeholder: String?     var showsBookmarkButton: Bool     var showsCancelButton: Bool     var showsSearchResultsButton: Bool     var searchResultsButtonSelected: Bool     func setShowsCancelButton(_ showsCancelButton: Bool, animated animated: Bool)     var tintColor: UIColor?     var barTintColor: UIColor?     var searchBarStyle: UISearchBarStyle     var translucent: Bool     var scopeButtonTitles: [AnyObject]?     var selectedScopeButtonIndex: Int     var showsScopeBar: Bool     var inputAccessoryView: UIView?     var backgroundImage: UIImage?     var scopeBarBackgroundImage: UIImage?     func setBackgroundImage(_ backgroundImage: UIImage?, forBarPosition barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForBarPosition(_ barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setSearchFieldBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState)     func searchFieldBackgroundImageForState(_ state: UIControlState) -> UIImage!     func setImage(_ iconImage: UIImage?, forSearchBarIcon icon: UISearchBarIcon, state state: UIControlState)     func imageForSearchBarIcon(_ icon: UISearchBarIcon, state state: UIControlState) -> UIImage!     func setScopeBarButtonBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState)     func scopeBarButtonBackgroundImageForState(_ state: UIControlState) -> UIImage?     func setScopeBarButtonDividerImage(_ dividerImage: UIImage?, forLeftSegmentState leftState: UIControlState, rightSegmentState rightState: UIControlState)     func scopeBarButtonDividerImageForLeftSegmentState(_ leftState: UIControlState, rightSegmentState rightState: UIControlState) -> UIImage!     func setScopeBarButtonTitleTextAttributes(_ attributes: [NSObject : AnyObject]?, forState state: UIControlState)     func scopeBarButtonTitleTextAttributesForState(_ state: UIControlState) -> [NSObject : AnyObject]?     var searchFieldBackgroundPositionAdjustment: UIOffset     var searchTextPositionAdjustment: UIOffset     func setPositionAdjustment(_ adjustment: UIOffset, forSearchBarIcon icon: UISearchBarIcon)     func positionAdjustmentForSearchBarIcon(_ icon: UISearchBarIcon) -> UIOffset } ``` |
| To | ``` class UISearchBar : UIView, UIBarPositioning, UITextInputTraits {     convenience init()     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     var barStyle: UIBarStyle     weak var delegate: UISearchBarDelegate?     var text: String?     var prompt: String?     var placeholder: String?     var showsBookmarkButton: Bool     var showsCancelButton: Bool     var showsSearchResultsButton: Bool     var searchResultsButtonSelected: Bool     func setShowsCancelButton(_ showsCancelButton: Bool, animated animated: Bool)     var inputAssistantItem: UITextInputAssistantItem { get }     var tintColor: UIColor!     var barTintColor: UIColor?     var searchBarStyle: UISearchBarStyle     var translucent: Bool     var scopeButtonTitles: [String]?     var selectedScopeButtonIndex: Int     var showsScopeBar: Bool     var inputAccessoryView: UIView?     var backgroundImage: UIImage?     var scopeBarBackgroundImage: UIImage?     func setBackgroundImage(_ backgroundImage: UIImage?, forBarPosition barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForBarPosition(_ barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setSearchFieldBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState)     func searchFieldBackgroundImageForState(_ state: UIControlState) -> UIImage?     func setImage(_ iconImage: UIImage?, forSearchBarIcon icon: UISearchBarIcon, state state: UIControlState)     func imageForSearchBarIcon(_ icon: UISearchBarIcon, state state: UIControlState) -> UIImage?     func setScopeBarButtonBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState)     func scopeBarButtonBackgroundImageForState(_ state: UIControlState) -> UIImage?     func setScopeBarButtonDividerImage(_ dividerImage: UIImage?, forLeftSegmentState leftState: UIControlState, rightSegmentState rightState: UIControlState)     func scopeBarButtonDividerImageForLeftSegmentState(_ leftState: UIControlState, rightSegmentState rightState: UIControlState) -> UIImage?     func setScopeBarButtonTitleTextAttributes(_ attributes: [String : AnyObject]?, forState state: UIControlState)     func scopeBarButtonTitleTextAttributesForState(_ state: UIControlState) -> [String : AnyObject]?     var searchFieldBackgroundPositionAdjustment: UIOffset     var searchTextPositionAdjustment: UIOffset     func setPositionAdjustment(_ adjustment: UIOffset, forSearchBarIcon icon: UISearchBarIcon)     func positionAdjustmentForSearchBarIcon(_ icon: UISearchBarIcon) -> UIOffset } ``` |

Modified [UISearchBar.delegate](https://developer.apple.com/documentation/uikit/uisearchbar/1624291-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UISearchBarDelegate? ``` |
| To | ``` weak var delegate: UISearchBarDelegate? ``` |

Modified [UISearchBar.imageForSearchBarIcon(_: UISearchBarIcon, state: UIControlState) -> UIImage?](https://developer.apple.com/documentation/uikit/uisearchbar/1624296-imageforsearchbaricon)

|  | Declaration |
| --- | --- |
| From | ``` func imageForSearchBarIcon(_ icon: UISearchBarIcon, state state: UIControlState) -> UIImage! ``` |
| To | ``` func imageForSearchBarIcon(_ icon: UISearchBarIcon, state state: UIControlState) -> UIImage? ``` |

Modified [UISearchBar.scopeBarButtonDividerImageForLeftSegmentState(_: UIControlState, rightSegmentState: UIControlState) -> UIImage?](https://developer.apple.com/documentation/uikit/uisearchbar/1624313-scopebarbuttondividerimageforlef)

|  | Declaration |
| --- | --- |
| From | ``` func scopeBarButtonDividerImageForLeftSegmentState(_ leftState: UIControlState, rightSegmentState rightState: UIControlState) -> UIImage! ``` |
| To | ``` func scopeBarButtonDividerImageForLeftSegmentState(_ leftState: UIControlState, rightSegmentState rightState: UIControlState) -> UIImage? ``` |

Modified [UISearchBar.scopeBarButtonTitleTextAttributesForState(_: UIControlState) -> [String : AnyObject]?](https://developer.apple.com/documentation/uikit/uisearchbar/1624309-scopebarbuttontitletextattribute)

|  | Declaration |
| --- | --- |
| From | ``` func scopeBarButtonTitleTextAttributesForState(_ state: UIControlState) -> [NSObject : AnyObject]? ``` |
| To | ``` func scopeBarButtonTitleTextAttributesForState(_ state: UIControlState) -> [String : AnyObject]? ``` |

Modified [UISearchBar.scopeButtonTitles](https://developer.apple.com/documentation/uikit/uisearchbar/1624292-scopebuttontitles)

|  | Declaration |
| --- | --- |
| From | ``` var scopeButtonTitles: [AnyObject]? ``` |
| To | ``` var scopeButtonTitles: [String]? ``` |

Modified [UISearchBar.searchFieldBackgroundImageForState(_: UIControlState) -> UIImage?](https://developer.apple.com/documentation/uikit/uisearchbar/1624288-searchfieldbackgroundimageforsta)

|  | Declaration |
| --- | --- |
| From | ``` func searchFieldBackgroundImageForState(_ state: UIControlState) -> UIImage! ``` |
| To | ``` func searchFieldBackgroundImageForState(_ state: UIControlState) -> UIImage? ``` |

Modified [UISearchBar.setScopeBarButtonTitleTextAttributes(_: [String : AnyObject]?, forState: UIControlState)](https://developer.apple.com/documentation/uikit/uisearchbar/1624277-setscopebarbuttontitletextattrib)

|  | Declaration |
| --- | --- |
| From | ``` func setScopeBarButtonTitleTextAttributes(_ attributes: [NSObject : AnyObject]?, forState state: UIControlState) ``` |
| To | ``` func setScopeBarButtonTitleTextAttributes(_ attributes: [String : AnyObject]?, forState state: UIControlState) ``` |

Modified [UISearchBar.text](https://developer.apple.com/documentation/uikit/uisearchbar/1624282-text)

|  | Declaration |
| --- | --- |
| From | ``` var text: String! ``` |
| To | ``` var text: String? ``` |

Modified [UISearchBar.tintColor](https://developer.apple.com/documentation/uikit/uisearchbar/1624286-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` var tintColor: UIColor? ``` |
| To | ``` var tintColor: UIColor! ``` |

Modified [UISearchBarDelegate.searchBar(_: UISearchBar, textDidChange: String)](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624299-searchbar)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UISearchBarDelegate.searchBarBookmarkButtonClicked(_: UISearchBar)](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624312-searchbarbookmarkbuttonclicked)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UISearchBarDelegate.searchBarCancelButtonClicked(_: UISearchBar)](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624314-searchbarcancelbuttonclicked)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UISearchBarDelegate.searchBarSearchButtonClicked(_: UISearchBar)](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624294-searchbarsearchbuttonclicked)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UISearchBarDelegate.searchBarShouldBeginEditing(_: UISearchBar) -> Bool](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624306-searchbarshouldbeginediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UISearchBarDelegate.searchBarShouldEndEditing(_: UISearchBar) -> Bool](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624329-searchbarshouldendediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UISearchBarDelegate.searchBarTextDidBeginEditing(_: UISearchBar)](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624303-searchbartextdidbeginediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UISearchBarDelegate.searchBarTextDidEndEditing(_: UISearchBar)](https://developer.apple.com/documentation/uikit/uisearchbardelegate/1624301-searchbartextdidendediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UISearchBarIcon [enum]](https://developer.apple.com/documentation/uikit/uisearchbar/icon)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UISearchBarStyle [enum]](https://developer.apple.com/documentation/uikit/uisearchbarstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UISearchController : UIViewController, UIViewControllerTransitioningDelegate, NSObjectProtocol, UIViewControllerAnimatedTransitioning {     init(searchResultsController searchResultsController: UIViewController!)     unowned(unsafe) var searchResultsUpdater: UISearchResultsUpdating?     var active: Bool     unowned(unsafe) var delegate: UISearchControllerDelegate?     var dimsBackgroundDuringPresentation: Bool     var hidesNavigationBarDuringPresentation: Bool     var searchResultsController: UIViewController! { get }     var searchBar: UISearchBar { get } } ``` |
| To | ``` class UISearchController : UIViewController, UIViewControllerTransitioningDelegate, UIViewControllerAnimatedTransitioning {     init(searchResultsController searchResultsController: UIViewController?)     weak var searchResultsUpdater: UISearchResultsUpdating?     var active: Bool     weak var delegate: UISearchControllerDelegate?     var dimsBackgroundDuringPresentation: Bool     var hidesNavigationBarDuringPresentation: Bool     var searchResultsController: UIViewController? { get }     var searchBar: UISearchBar { get } } ``` |

Modified [UISearchController.delegate](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618654-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UISearchControllerDelegate? ``` |
| To | ``` weak var delegate: UISearchControllerDelegate? ``` |

Modified [UISearchController.init(searchResultsController: UIViewController?)](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618647-init)

|  | Declaration |
| --- | --- |
| From | ``` init(searchResultsController searchResultsController: UIViewController!) ``` |
| To | ``` init(searchResultsController searchResultsController: UIViewController?) ``` |

Modified [UISearchController.searchResultsController](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618649-searchresultscontroller)

|  | Declaration |
| --- | --- |
| From | ``` var searchResultsController: UIViewController! { get } ``` |
| To | ``` var searchResultsController: UIViewController? { get } ``` |

Modified [UISearchController.searchResultsUpdater](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618661-searchresultsupdater)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var searchResultsUpdater: UISearchResultsUpdating? ``` |
| To | ``` weak var searchResultsUpdater: UISearchResultsUpdating? ``` |

Modified [UISearchDisplayController](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UISearchDisplayController : NSObject {     init(searchBar searchBar: UISearchBar!, contentsController viewController: UIViewController!)     unowned(unsafe) var delegate: UISearchDisplayDelegate?     var active: Bool     func setActive(_ visible: Bool, animated animated: Bool)     var searchBar: UISearchBar! { get }     var searchContentsController: UIViewController! { get }     var searchResultsTableView: UITableView! { get }     unowned(unsafe) var searchResultsDataSource: UITableViewDataSource?     unowned(unsafe) var searchResultsDelegate: UITableViewDelegate?     var searchResultsTitle: String?     var displaysSearchBarInNavigationBar: Bool     var navigationItem: UINavigationItem! { get } } ``` |
| To | ``` class UISearchDisplayController : NSObject {     init(searchBar searchBar: UISearchBar, contentsController viewController: UIViewController)     unowned(unsafe) var delegate: UISearchDisplayDelegate?     var active: Bool     func setActive(_ visible: Bool, animated animated: Bool)     var searchBar: UISearchBar { get }     var searchContentsController: UIViewController { get }     var searchResultsTableView: UITableView { get }     weak var searchResultsDataSource: UITableViewDataSource?     weak var searchResultsDelegate: UITableViewDelegate?     var searchResultsTitle: String?     var displaysSearchBarInNavigationBar: Bool     var navigationItem: UINavigationItem? { get } } ``` |

Modified [UISearchDisplayController.init(searchBar: UISearchBar, contentsController: UIViewController)](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620411-initwithsearchbar)

|  | Declaration |
| --- | --- |
| From | ``` init(searchBar searchBar: UISearchBar!, contentsController viewController: UIViewController!) ``` |
| To | ``` init(searchBar searchBar: UISearchBar, contentsController viewController: UIViewController) ``` |

Modified [UISearchDisplayController.navigationItem](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620408-navigationitem)

|  | Declaration |
| --- | --- |
| From | ``` var navigationItem: UINavigationItem! { get } ``` |
| To | ``` var navigationItem: UINavigationItem? { get } ``` |

Modified [UISearchDisplayController.searchBar](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620387-searchbar)

|  | Declaration |
| --- | --- |
| From | ``` var searchBar: UISearchBar! { get } ``` |
| To | ``` var searchBar: UISearchBar { get } ``` |

Modified [UISearchDisplayController.searchContentsController](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620393-searchcontentscontroller)

|  | Declaration |
| --- | --- |
| From | ``` var searchContentsController: UIViewController! { get } ``` |
| To | ``` var searchContentsController: UIViewController { get } ``` |

Modified [UISearchDisplayController.searchResultsDataSource](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620390-searchresultsdatasource)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var searchResultsDataSource: UITableViewDataSource? ``` |
| To | ``` weak var searchResultsDataSource: UITableViewDataSource? ``` |

Modified [UISearchDisplayController.searchResultsDelegate](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620404-searchresultsdelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var searchResultsDelegate: UITableViewDelegate? ``` |
| To | ``` weak var searchResultsDelegate: UITableViewDelegate? ``` |

Modified [UISearchDisplayController.searchResultsTableView](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/1620400-searchresultstableview)

|  | Declaration |
| --- | --- |
| From | ``` var searchResultsTableView: UITableView! { get } ``` |
| To | ``` var searchResultsTableView: UITableView { get } ``` |

Modified [UISearchDisplayDelegate](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UISearchDisplayDelegate : NSObjectProtocol {     optional func searchDisplayControllerWillBeginSearch(_ controller: UISearchDisplayController)     optional func searchDisplayControllerDidBeginSearch(_ controller: UISearchDisplayController)     optional func searchDisplayControllerWillEndSearch(_ controller: UISearchDisplayController)     optional func searchDisplayControllerDidEndSearch(_ controller: UISearchDisplayController)     optional func searchDisplayController(_ controller: UISearchDisplayController, didLoadSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, willUnloadSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, willShowSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, didShowSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, willHideSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, didHideSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearchString searchString: String!) -> Bool     optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearchScope searchOption: Int) -> Bool } ``` |
| To | ``` protocol UISearchDisplayDelegate : NSObjectProtocol {     optional func searchDisplayControllerWillBeginSearch(_ controller: UISearchDisplayController)     optional func searchDisplayControllerDidBeginSearch(_ controller: UISearchDisplayController)     optional func searchDisplayControllerWillEndSearch(_ controller: UISearchDisplayController)     optional func searchDisplayControllerDidEndSearch(_ controller: UISearchDisplayController)     optional func searchDisplayController(_ controller: UISearchDisplayController, didLoadSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, willUnloadSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, willShowSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, didShowSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, willHideSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, didHideSearchResultsTableView tableView: UITableView)     optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearchString searchString: String?) -> Bool     optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearchScope searchOption: Int) -> Bool } ``` |

Modified [UISearchDisplayDelegate.searchDisplayController(_: UISearchDisplayController, shouldReloadTableForSearchString: String?) -> Bool](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/1620403-searchdisplaycontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearchString searchString: String!) -> Bool ``` |
| To | ``` optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearchString searchString: String?) -> Bool ``` |

Modified [UISegmentedControl](https://developer.apple.com/documentation/uikit/uisegmentedcontrol)

|  | Declaration |
| --- | --- |
| From | ``` class UISegmentedControl : UIControl, NSCoding {     init(items items: [AnyObject])     var segmentedControlStyle: UISegmentedControlStyle     var momentary: Bool     var numberOfSegments: Int { get }     var apportionsSegmentWidthsByContent: Bool     func insertSegmentWithTitle(_ title: String!, atIndex segment: Int, animated animated: Bool)     func insertSegmentWithImage(_ image: UIImage, atIndex segment: Int, animated animated: Bool)     func removeSegmentAtIndex(_ segment: Int, animated animated: Bool)     func removeAllSegments()     func setTitle(_ title: String?, forSegmentAtIndex segment: Int)     func titleForSegmentAtIndex(_ segment: Int) -> String?     func setImage(_ image: UIImage?, forSegmentAtIndex segment: Int)     func imageForSegmentAtIndex(_ segment: Int) -> UIImage?     func setWidth(_ width: CGFloat, forSegmentAtIndex segment: Int)     func widthForSegmentAtIndex(_ segment: Int) -> CGFloat     func setContentOffset(_ offset: CGSize, forSegmentAtIndex segment: Int)     func contentOffsetForSegmentAtIndex(_ segment: Int) -> CGSize     func setEnabled(_ enabled: Bool, forSegmentAtIndex segment: Int)     func isEnabledForSegmentAtIndex(_ segment: Int) -> Bool     var selectedSegmentIndex: Int     var tintColor: UIColor!     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setDividerImage(_ dividerImage: UIImage?, forLeftSegmentState leftState: UIControlState, rightSegmentState rightState: UIControlState, barMetrics barMetrics: UIBarMetrics)     func dividerImageForLeftSegmentState(_ leftState: UIControlState, rightSegmentState rightState: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setTitleTextAttributes(_ attributes: [NSObject : AnyObject]?, forState state: UIControlState)     func titleTextAttributesForState(_ state: UIControlState) -> [NSObject : AnyObject]!     func setContentPositionAdjustment(_ adjustment: UIOffset, forSegmentType leftCenterRightOrAlone: UISegmentedControlSegment, barMetrics barMetrics: UIBarMetrics)     func contentPositionAdjustmentForSegmentType(_ leftCenterRightOrAlone: UISegmentedControlSegment, barMetrics barMetrics: UIBarMetrics) -> UIOffset } ``` |
| To | ``` class UISegmentedControl : UIControl {     init(items items: [AnyObject]?)     var segmentedControlStyle: UISegmentedControlStyle     var momentary: Bool     var numberOfSegments: Int { get }     var apportionsSegmentWidthsByContent: Bool     func insertSegmentWithTitle(_ title: String?, atIndex segment: Int, animated animated: Bool)     func insertSegmentWithImage(_ image: UIImage?, atIndex segment: Int, animated animated: Bool)     func removeSegmentAtIndex(_ segment: Int, animated animated: Bool)     func removeAllSegments()     func setTitle(_ title: String?, forSegmentAtIndex segment: Int)     func titleForSegmentAtIndex(_ segment: Int) -> String?     func setImage(_ image: UIImage?, forSegmentAtIndex segment: Int)     func imageForSegmentAtIndex(_ segment: Int) -> UIImage?     func setWidth(_ width: CGFloat, forSegmentAtIndex segment: Int)     func widthForSegmentAtIndex(_ segment: Int) -> CGFloat     func setContentOffset(_ offset: CGSize, forSegmentAtIndex segment: Int)     func contentOffsetForSegmentAtIndex(_ segment: Int) -> CGSize     func setEnabled(_ enabled: Bool, forSegmentAtIndex segment: Int)     func isEnabledForSegmentAtIndex(_ segment: Int) -> Bool     var selectedSegmentIndex: Int     var tintColor: UIColor!     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setDividerImage(_ dividerImage: UIImage?, forLeftSegmentState leftState: UIControlState, rightSegmentState rightState: UIControlState, barMetrics barMetrics: UIBarMetrics)     func dividerImageForLeftSegmentState(_ leftState: UIControlState, rightSegmentState rightState: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setTitleTextAttributes(_ attributes: [NSObject : AnyObject]?, forState state: UIControlState)     func titleTextAttributesForState(_ state: UIControlState) -> [NSObject : AnyObject]?     func setContentPositionAdjustment(_ adjustment: UIOffset, forSegmentType leftCenterRightOrAlone: UISegmentedControlSegment, barMetrics barMetrics: UIBarMetrics)     func contentPositionAdjustmentForSegmentType(_ leftCenterRightOrAlone: UISegmentedControlSegment, barMetrics barMetrics: UIBarMetrics) -> UIOffset } ``` |

Modified [UISegmentedControl.init(items: [AnyObject]?)](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618569-init)

|  | Declaration |
| --- | --- |
| From | ``` init(items items: [AnyObject]) ``` |
| To | ``` init(items items: [AnyObject]?) ``` |

Modified [UISegmentedControl.insertSegmentWithImage(_: UIImage?, atIndex: Int, animated: Bool)](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618572-insertsegment)

|  | Declaration |
| --- | --- |
| From | ``` func insertSegmentWithImage(_ image: UIImage, atIndex segment: Int, animated animated: Bool) ``` |
| To | ``` func insertSegmentWithImage(_ image: UIImage?, atIndex segment: Int, animated animated: Bool) ``` |

Modified [UISegmentedControl.insertSegmentWithTitle(_: String?, atIndex: Int, animated: Bool)](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618588-insertsegmentwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` func insertSegmentWithTitle(_ title: String!, atIndex segment: Int, animated animated: Bool) ``` |
| To | ``` func insertSegmentWithTitle(_ title: String?, atIndex segment: Int, animated animated: Bool) ``` |

Modified [UISegmentedControl.titleTextAttributesForState(_: UIControlState) -> [NSObject : AnyObject]?](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/1618566-titletextattributesforstate)

|  | Declaration |
| --- | --- |
| From | ``` func titleTextAttributesForState(_ state: UIControlState) -> [NSObject : AnyObject]! ``` |
| To | ``` func titleTextAttributesForState(_ state: UIControlState) -> [NSObject : AnyObject]? ``` |

Modified [UISegmentedControlSegment [enum]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segment)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UISimpleTextPrintFormatter](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter)

|  | Declaration |
| --- | --- |
| From | ``` class UISimpleTextPrintFormatter : UIPrintFormatter {     init(text text: String?)     init(attributedText attributedText: NSAttributedString?)     var text: String!     @NSCopying var attributedText: NSAttributedString!     var font: UIFont!     var color: UIColor?     var textAlignment: NSTextAlignment } ``` |
| To | ``` class UISimpleTextPrintFormatter : UIPrintFormatter {     init(text text: String)     init(attributedText attributedText: NSAttributedString)     var text: String?     @NSCopying var attributedText: NSAttributedString?     var font: UIFont?     var color: UIColor?     var textAlignment: NSTextAlignment } ``` |

Modified [UISimpleTextPrintFormatter.attributedText](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621820-attributedtext)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var attributedText: NSAttributedString! ``` |
| To | ``` @NSCopying var attributedText: NSAttributedString? ``` |

Modified [UISimpleTextPrintFormatter.font](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621837-font)

|  | Declaration |
| --- | --- |
| From | ``` var font: UIFont! ``` |
| To | ``` var font: UIFont? ``` |

Modified [UISimpleTextPrintFormatter.init(attributedText: NSAttributedString)](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621838-initwithattributedtext)

|  | Declaration |
| --- | --- |
| From | ``` init(attributedText attributedText: NSAttributedString?) ``` |
| To | ``` init(attributedText attributedText: NSAttributedString) ``` |

Modified [UISimpleTextPrintFormatter.init(text: String)](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621822-initwithtext)

|  | Declaration |
| --- | --- |
| From | ``` init(text text: String?) ``` |
| To | ``` init(text text: String) ``` |

Modified [UISimpleTextPrintFormatter.text](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/1621833-text)

|  | Declaration |
| --- | --- |
| From | ``` var text: String! ``` |
| To | ``` var text: String? ``` |

Modified [UISlider](https://developer.apple.com/documentation/uikit/uislider)

|  | Declaration |
| --- | --- |
| From | ``` class UISlider : UIControl, NSCoding {     var value: Float     var minimumValue: Float     var maximumValue: Float     var minimumValueImage: UIImage?     var maximumValueImage: UIImage?     var continuous: Bool     var minimumTrackTintColor: UIColor?     var maximumTrackTintColor: UIColor?     var thumbTintColor: UIColor?     func setValue(_ value: Float, animated animated: Bool)     func setThumbImage(_ image: UIImage?, forState state: UIControlState)     func setMinimumTrackImage(_ image: UIImage?, forState state: UIControlState)     func setMaximumTrackImage(_ image: UIImage?, forState state: UIControlState)     func thumbImageForState(_ state: UIControlState) -> UIImage?     func minimumTrackImageForState(_ state: UIControlState) -> UIImage?     func maximumTrackImageForState(_ state: UIControlState) -> UIImage?     var currentThumbImage: UIImage? { get }     var currentMinimumTrackImage: UIImage! { get }     var currentMaximumTrackImage: UIImage! { get }     func minimumValueImageRectForBounds(_ bounds: CGRect) -> CGRect     func maximumValueImageRectForBounds(_ bounds: CGRect) -> CGRect     func trackRectForBounds(_ bounds: CGRect) -> CGRect     func thumbRectForBounds(_ bounds: CGRect, trackRect rect: CGRect, value value: Float) -> CGRect } ``` |
| To | ``` class UISlider : UIControl {     var value: Float     var minimumValue: Float     var maximumValue: Float     var minimumValueImage: UIImage?     var maximumValueImage: UIImage?     var continuous: Bool     var minimumTrackTintColor: UIColor?     var maximumTrackTintColor: UIColor?     var thumbTintColor: UIColor?     func setValue(_ value: Float, animated animated: Bool)     func setThumbImage(_ image: UIImage?, forState state: UIControlState)     func setMinimumTrackImage(_ image: UIImage?, forState state: UIControlState)     func setMaximumTrackImage(_ image: UIImage?, forState state: UIControlState)     func thumbImageForState(_ state: UIControlState) -> UIImage?     func minimumTrackImageForState(_ state: UIControlState) -> UIImage?     func maximumTrackImageForState(_ state: UIControlState) -> UIImage?     var currentThumbImage: UIImage? { get }     var currentMinimumTrackImage: UIImage? { get }     var currentMaximumTrackImage: UIImage? { get }     func minimumValueImageRectForBounds(_ bounds: CGRect) -> CGRect     func maximumValueImageRectForBounds(_ bounds: CGRect) -> CGRect     func trackRectForBounds(_ bounds: CGRect) -> CGRect     func thumbRectForBounds(_ bounds: CGRect, trackRect rect: CGRect, value value: Float) -> CGRect } ``` |

Modified [UISlider.currentMaximumTrackImage](https://developer.apple.com/documentation/uikit/uislider/1621343-currentmaximumtrackimage)

|  | Declaration |
| --- | --- |
| From | ``` var currentMaximumTrackImage: UIImage! { get } ``` |
| To | ``` var currentMaximumTrackImage: UIImage? { get } ``` |

Modified [UISlider.currentMinimumTrackImage](https://developer.apple.com/documentation/uikit/uislider/1621339-currentminimumtrackimage)

|  | Declaration |
| --- | --- |
| From | ``` var currentMinimumTrackImage: UIImage! { get } ``` |
| To | ``` var currentMinimumTrackImage: UIImage? { get } ``` |

Modified [UISnapBehavior](https://developer.apple.com/documentation/uikit/uisnapbehavior)

|  | Declaration |
| --- | --- |
| From | ``` class UISnapBehavior : UIDynamicBehavior {     init!(item item: UIDynamicItem, snapToPoint point: CGPoint)     var damping: CGFloat } ``` |
| To | ``` class UISnapBehavior : UIDynamicBehavior {     init(item item: UIDynamicItem, snapToPoint point: CGPoint)     var snapPoint: CGPoint     var damping: CGFloat } ``` |

Modified [UISnapBehavior.init(item: UIDynamicItem, snapToPoint: CGPoint)](https://developer.apple.com/documentation/uikit/uisnapbehavior/1621011-initwithitem)

|  | Declaration |
| --- | --- |
| From | ``` init!(item item: UIDynamicItem, snapToPoint point: CGPoint) ``` |
| To | ``` init(item item: UIDynamicItem, snapToPoint point: CGPoint) ``` |

Modified [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UISplitViewController : UIViewController {     var viewControllers: [AnyObject]     unowned(unsafe) var delegate: UISplitViewControllerDelegate?     var presentsWithGesture: Bool     var collapsed: Bool { get }     var preferredDisplayMode: UISplitViewControllerDisplayMode     var displayMode: UISplitViewControllerDisplayMode { get }     func displayModeButtonItem() -> UIBarButtonItem     var preferredPrimaryColumnWidthFraction: CGFloat     var minimumPrimaryColumnWidth: CGFloat     var maximumPrimaryColumnWidth: CGFloat     var primaryColumnWidth: CGFloat { get }     func showViewController(_ vc: UIViewController, sender sender: AnyObject!)     func showDetailViewController(_ vc: UIViewController!, sender sender: AnyObject!) } ``` |
| To | ``` class UISplitViewController : UIViewController {     var viewControllers: [UIViewController]     weak var delegate: UISplitViewControllerDelegate?     var presentsWithGesture: Bool     var collapsed: Bool { get }     var preferredDisplayMode: UISplitViewControllerDisplayMode     var displayMode: UISplitViewControllerDisplayMode { get }     func displayModeButtonItem() -> UIBarButtonItem     var preferredPrimaryColumnWidthFraction: CGFloat     var minimumPrimaryColumnWidth: CGFloat     var maximumPrimaryColumnWidth: CGFloat     var primaryColumnWidth: CGFloat { get }     func showViewController(_ vc: UIViewController, sender sender: AnyObject?)     func showDetailViewController(_ vc: UIViewController, sender sender: AnyObject?) } ``` |

Modified [UISplitViewController.delegate](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623167-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UISplitViewControllerDelegate? ``` |
| To | ``` weak var delegate: UISplitViewControllerDelegate? ``` |

Modified [UISplitViewController.showDetailViewController(_: UIViewController, sender: AnyObject?)](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623182-showdetailviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func showDetailViewController(_ vc: UIViewController!, sender sender: AnyObject!) ``` |
| To | ``` func showDetailViewController(_ vc: UIViewController, sender sender: AnyObject?) ``` |

Modified [UISplitViewController.showViewController(_: UIViewController, sender: AnyObject?)](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623199-show)

|  | Declaration |
| --- | --- |
| From | ``` func showViewController(_ vc: UIViewController, sender sender: AnyObject!) ``` |
| To | ``` func showViewController(_ vc: UIViewController, sender sender: AnyObject?) ``` |

Modified [UISplitViewController.viewControllers](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623181-viewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` var viewControllers: [AnyObject] ``` |
| To | ``` var viewControllers: [UIViewController] ``` |

Modified [UISplitViewControllerDelegate](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UISplitViewControllerDelegate {     optional func splitViewController(_ svc: UISplitViewController, willChangeToDisplayMode displayMode: UISplitViewControllerDisplayMode)     optional func targetDisplayModeForActionInSplitViewController(_ svc: UISplitViewController) -> UISplitViewControllerDisplayMode     optional func splitViewController(_ splitViewController: UISplitViewController, showViewController vc: UIViewController, sender sender: AnyObject?) -> Bool     optional func splitViewController(_ splitViewController: UISplitViewController, showDetailViewController vc: UIViewController, sender sender: AnyObject?) -> Bool     optional func primaryViewControllerForCollapsingSplitViewController(_ splitViewController: UISplitViewController) -> UIViewController?     optional func primaryViewControllerForExpandingSplitViewController(_ splitViewController: UISplitViewController) -> UIViewController?     optional func splitViewController(_ splitViewController: UISplitViewController, collapseSecondaryViewController secondaryViewController: UIViewController!, ontoPrimaryViewController primaryViewController: UIViewController!) -> Bool     optional func splitViewController(_ splitViewController: UISplitViewController, separateSecondaryViewControllerFromPrimaryViewController primaryViewController: UIViewController!) -> UIViewController?     optional func splitViewControllerSupportedInterfaceOrientations(_ splitViewController: UISplitViewController) -> Int     optional func splitViewControllerPreferredInterfaceOrientationForPresentation(_ splitViewController: UISplitViewController) -> UIInterfaceOrientation     optional func splitViewController(_ svc: UISplitViewController, willHideViewController aViewController: UIViewController, withBarButtonItem barButtonItem: UIBarButtonItem, forPopoverController pc: UIPopoverController)     optional func splitViewController(_ svc: UISplitViewController, willShowViewController aViewController: UIViewController, invalidatingBarButtonItem barButtonItem: UIBarButtonItem)     optional func splitViewController(_ svc: UISplitViewController, popoverController pc: UIPopoverController, willPresentViewController aViewController: UIViewController)     optional func splitViewController(_ svc: UISplitViewController, shouldHideViewController vc: UIViewController, inOrientation orientation: UIInterfaceOrientation) -> Bool } ``` |
| To | ``` protocol UISplitViewControllerDelegate {     optional func splitViewController(_ svc: UISplitViewController, willChangeToDisplayMode displayMode: UISplitViewControllerDisplayMode)     optional func targetDisplayModeForActionInSplitViewController(_ svc: UISplitViewController) -> UISplitViewControllerDisplayMode     optional func splitViewController(_ splitViewController: UISplitViewController, showViewController vc: UIViewController, sender sender: AnyObject?) -> Bool     optional func splitViewController(_ splitViewController: UISplitViewController, showDetailViewController vc: UIViewController, sender sender: AnyObject?) -> Bool     optional func primaryViewControllerForCollapsingSplitViewController(_ splitViewController: UISplitViewController) -> UIViewController?     optional func primaryViewControllerForExpandingSplitViewController(_ splitViewController: UISplitViewController) -> UIViewController?     optional func splitViewController(_ splitViewController: UISplitViewController, collapseSecondaryViewController secondaryViewController: UIViewController, ontoPrimaryViewController primaryViewController: UIViewController) -> Bool     optional func splitViewController(_ splitViewController: UISplitViewController, separateSecondaryViewControllerFromPrimaryViewController primaryViewController: UIViewController) -> UIViewController?     optional func splitViewControllerSupportedInterfaceOrientations(_ splitViewController: UISplitViewController) -> UIInterfaceOrientationMask     optional func splitViewControllerPreferredInterfaceOrientationForPresentation(_ splitViewController: UISplitViewController) -> UIInterfaceOrientation     optional func splitViewController(_ svc: UISplitViewController, willHideViewController aViewController: UIViewController, withBarButtonItem barButtonItem: UIBarButtonItem, forPopoverController pc: UIPopoverController)     optional func splitViewController(_ svc: UISplitViewController, willShowViewController aViewController: UIViewController, invalidatingBarButtonItem barButtonItem: UIBarButtonItem)     optional func splitViewController(_ svc: UISplitViewController, popoverController pc: UIPopoverController, willPresentViewController aViewController: UIViewController)     optional func splitViewController(_ svc: UISplitViewController, shouldHideViewController vc: UIViewController, inOrientation orientation: UIInterfaceOrientation) -> Bool } ``` |

Modified [UISplitViewControllerDelegate.splitViewController(_: UISplitViewController, collapseSecondaryViewController: UIViewController, ontoPrimaryViewController: UIViewController) -> Bool](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623184-splitviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func splitViewController(_ splitViewController: UISplitViewController, collapseSecondaryViewController secondaryViewController: UIViewController!, ontoPrimaryViewController primaryViewController: UIViewController!) -> Bool ``` |
| To | ``` optional func splitViewController(_ splitViewController: UISplitViewController, collapseSecondaryViewController secondaryViewController: UIViewController, ontoPrimaryViewController primaryViewController: UIViewController) -> Bool ``` |

Modified [UISplitViewControllerDelegate.splitViewController(_: UISplitViewController, separateSecondaryViewControllerFromPrimaryViewController: UIViewController) -> UIViewController?](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623189-splitviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func splitViewController(_ splitViewController: UISplitViewController, separateSecondaryViewControllerFromPrimaryViewController primaryViewController: UIViewController!) -> UIViewController? ``` |
| To | ``` optional func splitViewController(_ splitViewController: UISplitViewController, separateSecondaryViewControllerFromPrimaryViewController primaryViewController: UIViewController) -> UIViewController? ``` |

Modified [UISplitViewControllerDelegate.splitViewControllerSupportedInterfaceOrientations(_: UISplitViewController) -> UIInterfaceOrientationMask](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/1623178-splitviewcontrollersupportedinte)

|  | Declaration |
| --- | --- |
| From | ``` optional func splitViewControllerSupportedInterfaceOrientations(_ splitViewController: UISplitViewController) -> Int ``` |
| To | ``` optional func splitViewControllerSupportedInterfaceOrientations(_ splitViewController: UISplitViewController) -> UIInterfaceOrientationMask ``` |

Modified [UISplitViewControllerDisplayMode [enum]](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIStateRestoring](https://developer.apple.com/documentation/uikit/uistaterestoring)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIStateRestoring : NSObjectProtocol {     optional var restorationParent: UIStateRestoring! { get }     optional var objectRestorationClass: AnyObject.Type! { get }     optional func encodeRestorableStateWithCoder(_ coder: NSCoder)     optional func decodeRestorableStateWithCoder(_ coder: NSCoder!)     optional func applicationFinishedRestoringState() } ``` |
| To | ``` protocol UIStateRestoring : NSObjectProtocol {     optional var restorationParent: UIStateRestoring? { get }     optional var objectRestorationClass: AnyObject.Type? { get }     optional func encodeRestorableStateWithCoder(_ coder: NSCoder)     optional func decodeRestorableStateWithCoder(_ coder: NSCoder)     optional func applicationFinishedRestoringState() } ``` |

Modified [UIStateRestoring.decodeRestorableStateWithCoder(_: NSCoder)](https://developer.apple.com/documentation/uikit/uistaterestoring/1616854-decoderestorablestate)

|  | Declaration |
| --- | --- |
| From | ``` optional func decodeRestorableStateWithCoder(_ coder: NSCoder!) ``` |
| To | ``` optional func decodeRestorableStateWithCoder(_ coder: NSCoder) ``` |

Modified [UIStateRestoring.objectRestorationClass](https://developer.apple.com/documentation/uikit/uistaterestoring/1616851-objectrestorationclass)

|  | Declaration |
| --- | --- |
| From | ``` optional var objectRestorationClass: AnyObject.Type! { get } ``` |
| To | ``` optional var objectRestorationClass: AnyObject.Type? { get } ``` |

Modified [UIStateRestoring.restorationParent](https://developer.apple.com/documentation/uikit/uistaterestoring/1616867-restorationparent)

|  | Declaration |
| --- | --- |
| From | ``` optional var restorationParent: UIStateRestoring! { get } ``` |
| To | ``` optional var restorationParent: UIStateRestoring? { get } ``` |

Modified [UIStatusBarAnimation [enum]](https://developer.apple.com/documentation/uikit/uistatusbaranimation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIStatusBarAnimation.Fade](https://developer.apple.com/documentation/uikit/uistatusbaranimation/fade)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIStatusBarAnimation.Slide](https://developer.apple.com/documentation/uikit/uistatusbaranimation/uistatusbaranimationslide)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIStatusBarStyle [enum]](https://developer.apple.com/documentation/uikit/uistatusbarstyle)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum UIStatusBarStyle : Int {     case Default     case LightContent     case BlackOpaque } ``` | -- |
| To | ``` enum UIStatusBarStyle : Int {     case Default     case LightContent     static var BlackTranslucent: UIStatusBarStyle { get }     case BlackOpaque } ``` | Int |

Modified [UIStepper](https://developer.apple.com/documentation/uikit/uistepper)

|  | Declaration |
| --- | --- |
| From | ``` class UIStepper : UIControl {     var continuous: Bool     var autorepeat: Bool     var wraps: Bool     var value: Double     var minimumValue: Double     var maximumValue: Double     var stepValue: Double     var tintColor: UIColor!     func setBackgroundImage(_ image: UIImage?, forState state: UIControlState)     func backgroundImageForState(_ state: UIControlState) -> UIImage     func setDividerImage(_ image: UIImage?, forLeftSegmentState leftState: UIControlState, rightSegmentState rightState: UIControlState)     func dividerImageForLeftSegmentState(_ state: UIControlState, rightSegmentState state: UIControlState) -> UIImage!     func setIncrementImage(_ image: UIImage?, forState state: UIControlState)     func incrementImageForState(_ state: UIControlState) -> UIImage     func setDecrementImage(_ image: UIImage?, forState state: UIControlState)     func decrementImageForState(_ state: UIControlState) -> UIImage } ``` |
| To | ``` class UIStepper : UIControl {     var continuous: Bool     var autorepeat: Bool     var wraps: Bool     var value: Double     var minimumValue: Double     var maximumValue: Double     var stepValue: Double     var tintColor: UIColor!     func setBackgroundImage(_ image: UIImage?, forState state: UIControlState)     func backgroundImageForState(_ state: UIControlState) -> UIImage?     func setDividerImage(_ image: UIImage?, forLeftSegmentState leftState: UIControlState, rightSegmentState rightState: UIControlState)     func dividerImageForLeftSegmentState(_ state: UIControlState, rightSegmentState state: UIControlState) -> UIImage?     func setIncrementImage(_ image: UIImage?, forState state: UIControlState)     func incrementImageForState(_ state: UIControlState) -> UIImage?     func setDecrementImage(_ image: UIImage?, forState state: UIControlState)     func decrementImageForState(_ state: UIControlState) -> UIImage? } ``` |

Modified [UIStepper.backgroundImageForState(_: UIControlState) -> UIImage?](https://developer.apple.com/documentation/uikit/uistepper/1624069-backgroundimageforstate)

|  | Declaration |
| --- | --- |
| From | ``` func backgroundImageForState(_ state: UIControlState) -> UIImage ``` |
| To | ``` func backgroundImageForState(_ state: UIControlState) -> UIImage? ``` |

Modified [UIStepper.decrementImageForState(_: UIControlState) -> UIImage?](https://developer.apple.com/documentation/uikit/uistepper/1624077-decrementimageforstate)

|  | Declaration |
| --- | --- |
| From | ``` func decrementImageForState(_ state: UIControlState) -> UIImage ``` |
| To | ``` func decrementImageForState(_ state: UIControlState) -> UIImage? ``` |

Modified [UIStepper.dividerImageForLeftSegmentState(_: UIControlState, rightSegmentState: UIControlState) -> UIImage?](https://developer.apple.com/documentation/uikit/uistepper/1624072-dividerimage)

|  | Declaration |
| --- | --- |
| From | ``` func dividerImageForLeftSegmentState(_ state: UIControlState, rightSegmentState state: UIControlState) -> UIImage! ``` |
| To | ``` func dividerImageForLeftSegmentState(_ state: UIControlState, rightSegmentState state: UIControlState) -> UIImage? ``` |

Modified [UIStepper.incrementImageForState(_: UIControlState) -> UIImage?](https://developer.apple.com/documentation/uikit/uistepper/1624080-incrementimageforstate)

|  | Declaration |
| --- | --- |
| From | ``` func incrementImageForState(_ state: UIControlState) -> UIImage ``` |
| To | ``` func incrementImageForState(_ state: UIControlState) -> UIImage? ``` |

Modified [UIStoryboard](https://developer.apple.com/documentation/uikit/uistoryboard)

|  | Declaration |
| --- | --- |
| From | ``` class UIStoryboard : NSObject {     init(name name: String, bundle storyboardBundleOrNil: NSBundle?) -> UIStoryboard     class func storyboardWithName(_ name: String, bundle storyboardBundleOrNil: NSBundle?) -> UIStoryboard     func instantiateInitialViewController() -> AnyObject     func instantiateViewControllerWithIdentifier(_ identifier: String) -> AnyObject! } ``` |
| To | ``` class UIStoryboard : NSObject {      init(name name: String, bundle storyboardBundleOrNil: NSBundle?)     class func storyboardWithName(_ name: String, bundle storyboardBundleOrNil: NSBundle?) -> UIStoryboard     func instantiateInitialViewController() -> UIViewController?     func instantiateViewControllerWithIdentifier(_ identifier: String) -> UIViewController } ``` |

Modified [UIStoryboard.init(name: String, bundle: NSBundle?)](https://developer.apple.com/documentation/uikit/uistoryboard/1616216-storyboardwithname)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String, bundle storyboardBundleOrNil: NSBundle?) -> UIStoryboard ``` |
| To | ``` init(name name: String, bundle storyboardBundleOrNil: NSBundle?) ``` |

Modified [UIStoryboard.instantiateInitialViewController() -> UIViewController?](https://developer.apple.com/documentation/uikit/uistoryboard/1616213-instantiateinitialviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func instantiateInitialViewController() -> AnyObject ``` |
| To | ``` func instantiateInitialViewController() -> UIViewController? ``` |

Modified [UIStoryboard.instantiateViewControllerWithIdentifier(_: String) -> UIViewController](https://developer.apple.com/documentation/uikit/uistoryboard/1616214-instantiateviewcontrollerwithide)

|  | Declaration |
| --- | --- |
| From | ``` func instantiateViewControllerWithIdentifier(_ identifier: String) -> AnyObject! ``` |
| To | ``` func instantiateViewControllerWithIdentifier(_ identifier: String) -> UIViewController ``` |

Modified [UIStoryboardPopoverSegue](https://developer.apple.com/documentation/uikit/uistoryboardpopoversegue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIStoryboardPopoverSegue.popoverController](https://developer.apple.com/documentation/uikit/uistoryboardpopoversegue/1624759-popovercontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIStoryboardSegue](https://developer.apple.com/documentation/uikit/uistoryboardsegue)

|  | Declaration |
| --- | --- |
| From | ``` class UIStoryboardSegue : NSObject {     convenience init(identifier identifier: String?, source source: UIViewController, destination destination: UIViewController, performHandler performHandler: () -> Void)     class func segueWithIdentifier(_ identifier: String?, source source: UIViewController, destination destination: UIViewController, performHandler performHandler: () -> Void) -> Self     init!(identifier identifier: String?, source source: UIViewController, destination destination: UIViewController)     var identifier: String? { get }     var sourceViewController: AnyObject { get }     var destinationViewController: AnyObject { get }     func perform() } ``` |
| To | ``` class UIStoryboardSegue : NSObject {     convenience init(identifier identifier: String?, source source: UIViewController, destination destination: UIViewController, performHandler performHandler: () -> Void)     class func segueWithIdentifier(_ identifier: String?, source source: UIViewController, destination destination: UIViewController, performHandler performHandler: () -> Void) -> Self     init(identifier identifier: String?, source source: UIViewController, destination destination: UIViewController)     convenience init()     var identifier: String? { get }     var sourceViewController: UIViewController { get }     var destinationViewController: UIViewController { get }     func perform() } ``` |

Modified [UIStoryboardSegue.destinationViewController](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621916-destinationviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` var destinationViewController: AnyObject { get } ``` |
| To | ``` var destinationViewController: UIViewController { get } ``` |

Modified [UIStoryboardSegue.init(identifier: String?, source: UIViewController, destination: UIViewController)](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621908-initwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(identifier identifier: String?, source source: UIViewController, destination destination: UIViewController) ``` |
| To | ``` init(identifier identifier: String?, source source: UIViewController, destination destination: UIViewController) ``` |

Modified [UIStoryboardSegue.sourceViewController](https://developer.apple.com/documentation/uikit/uistoryboardsegue/1621918-sourceviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` var sourceViewController: AnyObject { get } ``` |
| To | ``` var sourceViewController: UIViewController { get } ``` |

Modified [UISwipeGestureRecognizerDirection [struct]](https://developer.apple.com/documentation/uikit/uiswipegesturerecognizerdirection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UISwipeGestureRecognizerDirection : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Right: UISwipeGestureRecognizerDirection { get }     static var Left: UISwipeGestureRecognizerDirection { get }     static var Up: UISwipeGestureRecognizerDirection { get }     static var Down: UISwipeGestureRecognizerDirection { get } } ``` | RawOptionSetType |
| To | ``` struct UISwipeGestureRecognizerDirection : OptionSetType {     init(rawValue rawValue: UInt)     static var Right: UISwipeGestureRecognizerDirection { get }     static var Left: UISwipeGestureRecognizerDirection { get }     static var Up: UISwipeGestureRecognizerDirection { get }     static var Down: UISwipeGestureRecognizerDirection { get } } ``` | OptionSetType |

Modified [UISwitch](https://developer.apple.com/documentation/uikit/uiswitch)

|  | Declaration |
| --- | --- |
| From | ``` class UISwitch : UIControl, NSCoding {     var onTintColor: UIColor!     var tintColor: UIColor?     var thumbTintColor: UIColor?     var onImage: UIImage?     var offImage: UIImage?     var on: Bool     init(frame frame: CGRect)     func setOn(_ on: Bool, animated animated: Bool) } ``` |
| To | ``` class UISwitch : UIControl {     var onTintColor: UIColor?     var tintColor: UIColor!     var thumbTintColor: UIColor?     var onImage: UIImage?     var offImage: UIImage?     var on: Bool     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     func setOn(_ on: Bool, animated animated: Bool) } ``` |

Modified [UISwitch.onTintColor](https://developer.apple.com/documentation/uikit/uiswitch/1623687-ontintcolor)

|  | Declaration |
| --- | --- |
| From | ``` var onTintColor: UIColor! ``` |
| To | ``` var onTintColor: UIColor? ``` |

Modified [UISwitch.tintColor](https://developer.apple.com/documentation/uikit/uiswitch/1623688-tintcolor)

|  | Declaration |
| --- | --- |
| From | ``` var tintColor: UIColor? ``` |
| To | ``` var tintColor: UIColor! ``` |

Modified [UISystemAnimation [enum]](https://developer.apple.com/documentation/uikit/uisystemanimation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar)

|  | Declaration |
| --- | --- |
| From | ``` class UITabBar : UIView {     unowned(unsafe) var delegate: UITabBarDelegate?     var items: [AnyObject]?     unowned(unsafe) var selectedItem: UITabBarItem?     func setItems(_ items: [AnyObject]?, animated animated: Bool)     func beginCustomizingItems(_ items: [AnyObject])     func endCustomizingAnimated(_ animated: Bool) -> Bool     func isCustomizing() -> Bool     var tintColor: UIColor!     var barTintColor: UIColor?     var selectedImageTintColor: UIColor?     var backgroundImage: UIImage?     var selectionIndicatorImage: UIImage?     var shadowImage: UIImage?     var itemPositioning: UITabBarItemPositioning     var itemWidth: CGFloat     var itemSpacing: CGFloat     var barStyle: UIBarStyle     var translucent: Bool } ``` |
| To | ``` class UITabBar : UIView {     unowned(unsafe) var delegate: UITabBarDelegate?     var items: [UITabBarItem]?     unowned(unsafe) var selectedItem: UITabBarItem?     func setItems(_ items: [UITabBarItem]?, animated animated: Bool)     func beginCustomizingItems(_ items: [UITabBarItem])     func endCustomizingAnimated(_ animated: Bool) -> Bool     func isCustomizing() -> Bool     var tintColor: UIColor!     var barTintColor: UIColor?     var selectedImageTintColor: UIColor?     var backgroundImage: UIImage?     var selectionIndicatorImage: UIImage?     var shadowImage: UIImage?     var itemPositioning: UITabBarItemPositioning     var itemWidth: CGFloat     var itemSpacing: CGFloat     var barStyle: UIBarStyle     var translucent: Bool } ``` |

Modified [UITabBar.beginCustomizingItems(_: [UITabBarItem])](https://developer.apple.com/documentation/uikit/uitabbar/1623462-begincustomizingitems)

|  | Declaration |
| --- | --- |
| From | ``` func beginCustomizingItems(_ items: [AnyObject]) ``` |
| To | ``` func beginCustomizingItems(_ items: [UITabBarItem]) ``` |

Modified [UITabBar.items](https://developer.apple.com/documentation/uikit/uitabbar/1623466-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject]? ``` |
| To | ``` var items: [UITabBarItem]? ``` |

Modified [UITabBar.setItems(_: [UITabBarItem]?, animated: Bool)](https://developer.apple.com/documentation/uikit/uitabbar/1623455-setitems)

|  | Declaration |
| --- | --- |
| From | ``` func setItems(_ items: [AnyObject]?, animated animated: Bool) ``` |
| To | ``` func setItems(_ items: [UITabBarItem]?, animated animated: Bool) ``` |

Modified [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UITabBarController : UIViewController, UITabBarDelegate, NSObjectProtocol, NSCoding {     var viewControllers: [AnyObject]?     func setViewControllers(_ viewControllers: [AnyObject], animated animated: Bool)     unowned(unsafe) var selectedViewController: UIViewController?     var selectedIndex: Int     var moreNavigationController: UINavigationController { get }     var customizableViewControllers: [AnyObject]?     var tabBar: UITabBar { get }     unowned(unsafe) var delegate: UITabBarControllerDelegate? } ``` |
| To | ``` class UITabBarController : UIViewController, UITabBarDelegate {     var viewControllers: [UIViewController]?     func setViewControllers(_ viewControllers: [UIViewController]?, animated animated: Bool)     unowned(unsafe) var selectedViewController: UIViewController?     var selectedIndex: Int     var moreNavigationController: UINavigationController { get }     var customizableViewControllers: [UIViewController]?     var tabBar: UITabBar { get }     weak var delegate: UITabBarControllerDelegate? } ``` |

Modified [UITabBarController.customizableViewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621184-customizableviewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` var customizableViewControllers: [AnyObject]? ``` |
| To | ``` var customizableViewControllers: [UIViewController]? ``` |

Modified [UITabBarController.delegate](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621164-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UITabBarControllerDelegate? ``` |
| To | ``` weak var delegate: UITabBarControllerDelegate? ``` |

Modified [UITabBarController.setViewControllers(_: [UIViewController]?, animated: Bool)](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621177-setviewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` func setViewControllers(_ viewControllers: [AnyObject], animated animated: Bool) ``` |
| To | ``` func setViewControllers(_ viewControllers: [UIViewController]?, animated animated: Bool) ``` |

Modified [UITabBarController.viewControllers](https://developer.apple.com/documentation/uikit/uitabbarcontroller/1621185-viewcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` var viewControllers: [AnyObject]? ``` |
| To | ``` var viewControllers: [UIViewController]? ``` |

Modified [UITabBarControllerDelegate](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UITabBarControllerDelegate : NSObjectProtocol {     optional func tabBarController(_ tabBarController: UITabBarController, shouldSelectViewController viewController: UIViewController) -> Bool     optional func tabBarController(_ tabBarController: UITabBarController, didSelectViewController viewController: UIViewController)     optional func tabBarController(_ tabBarController: UITabBarController, willBeginCustomizingViewControllers viewControllers: [AnyObject])     optional func tabBarController(_ tabBarController: UITabBarController, willEndCustomizingViewControllers viewControllers: [AnyObject], changed changed: Bool)     optional func tabBarController(_ tabBarController: UITabBarController, didEndCustomizingViewControllers viewControllers: [AnyObject], changed changed: Bool)     optional func tabBarControllerSupportedInterfaceOrientations(_ tabBarController: UITabBarController) -> Int     optional func tabBarControllerPreferredInterfaceOrientationForPresentation(_ tabBarController: UITabBarController) -> UIInterfaceOrientation     optional func tabBarController(_ tabBarController: UITabBarController, interactionControllerForAnimationController animationController: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning?     optional func tabBarController(_ tabBarController: UITabBarController, animationControllerForTransitionFromViewController fromVC: UIViewController, toViewController toVC: UIViewController) -> UIViewControllerAnimatedTransitioning? } ``` |
| To | ``` protocol UITabBarControllerDelegate : NSObjectProtocol {     optional func tabBarController(_ tabBarController: UITabBarController, shouldSelectViewController viewController: UIViewController) -> Bool     optional func tabBarController(_ tabBarController: UITabBarController, didSelectViewController viewController: UIViewController)     optional func tabBarController(_ tabBarController: UITabBarController, willBeginCustomizingViewControllers viewControllers: [UIViewController])     optional func tabBarController(_ tabBarController: UITabBarController, willEndCustomizingViewControllers viewControllers: [UIViewController], changed changed: Bool)     optional func tabBarController(_ tabBarController: UITabBarController, didEndCustomizingViewControllers viewControllers: [UIViewController], changed changed: Bool)     optional func tabBarControllerSupportedInterfaceOrientations(_ tabBarController: UITabBarController) -> UIInterfaceOrientationMask     optional func tabBarControllerPreferredInterfaceOrientationForPresentation(_ tabBarController: UITabBarController) -> UIInterfaceOrientation     optional func tabBarController(_ tabBarController: UITabBarController, interactionControllerForAnimationController animationController: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning?     optional func tabBarController(_ tabBarController: UITabBarController, animationControllerForTransitionFromViewController fromVC: UIViewController, toViewController toVC: UIViewController) -> UIViewControllerAnimatedTransitioning? } ``` |

Modified [UITabBarControllerDelegate.tabBarController(_: UITabBarController, didEndCustomizingViewControllers: [UIViewController], changed: Bool)](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621168-tabbarcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func tabBarController(_ tabBarController: UITabBarController, didEndCustomizingViewControllers viewControllers: [AnyObject], changed changed: Bool) ``` | iOS 8.0 |
| To | ``` optional func tabBarController(_ tabBarController: UITabBarController, didEndCustomizingViewControllers viewControllers: [UIViewController], changed changed: Bool) ``` | iOS 2.0 |

Modified [UITabBarControllerDelegate.tabBarController(_: UITabBarController, didSelectViewController: UIViewController)](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621173-tabbarcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITabBarControllerDelegate.tabBarController(_: UITabBarController, willBeginCustomizingViewControllers: [UIViewController])](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621179-tabbarcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func tabBarController(_ tabBarController: UITabBarController, willBeginCustomizingViewControllers viewControllers: [AnyObject]) ``` |
| To | ``` optional func tabBarController(_ tabBarController: UITabBarController, willBeginCustomizingViewControllers viewControllers: [UIViewController]) ``` |

Modified [UITabBarControllerDelegate.tabBarController(_: UITabBarController, willEndCustomizingViewControllers: [UIViewController], changed: Bool)](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621178-tabbarcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func tabBarController(_ tabBarController: UITabBarController, willEndCustomizingViewControllers viewControllers: [AnyObject], changed changed: Bool) ``` |
| To | ``` optional func tabBarController(_ tabBarController: UITabBarController, willEndCustomizingViewControllers viewControllers: [UIViewController], changed changed: Bool) ``` |

Modified [UITabBarControllerDelegate.tabBarControllerSupportedInterfaceOrientations(_: UITabBarController) -> UIInterfaceOrientationMask](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/1621180-tabbarcontrollersupportedinterfa)

|  | Declaration |
| --- | --- |
| From | ``` optional func tabBarControllerSupportedInterfaceOrientations(_ tabBarController: UITabBarController) -> Int ``` |
| To | ``` optional func tabBarControllerSupportedInterfaceOrientations(_ tabBarController: UITabBarController) -> UIInterfaceOrientationMask ``` |

Modified [UITabBarDelegate](https://developer.apple.com/documentation/uikit/uitabbardelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UITabBarDelegate : NSObjectProtocol {     optional func tabBar(_ tabBar: UITabBar, didSelectItem item: UITabBarItem!)     optional func tabBar(_ tabBar: UITabBar, willBeginCustomizingItems items: [AnyObject])     optional func tabBar(_ tabBar: UITabBar, didBeginCustomizingItems items: [AnyObject])     optional func tabBar(_ tabBar: UITabBar, willEndCustomizingItems items: [AnyObject], changed changed: Bool)     optional func tabBar(_ tabBar: UITabBar, didEndCustomizingItems items: [AnyObject], changed changed: Bool) } ``` |
| To | ``` protocol UITabBarDelegate : NSObjectProtocol {     optional func tabBar(_ tabBar: UITabBar, didSelectItem item: UITabBarItem)     optional func tabBar(_ tabBar: UITabBar, willBeginCustomizingItems items: [UITabBarItem])     optional func tabBar(_ tabBar: UITabBar, didBeginCustomizingItems items: [UITabBarItem])     optional func tabBar(_ tabBar: UITabBar, willEndCustomizingItems items: [UITabBarItem], changed changed: Bool)     optional func tabBar(_ tabBar: UITabBar, didEndCustomizingItems items: [UITabBarItem], changed changed: Bool) } ``` |

Modified [UITabBarDelegate.tabBar(_: UITabBar, didBeginCustomizingItems: [UITabBarItem])](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623471-tabbar)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func tabBar(_ tabBar: UITabBar, didBeginCustomizingItems items: [AnyObject]) ``` | iOS 8.0 |
| To | ``` optional func tabBar(_ tabBar: UITabBar, didBeginCustomizingItems items: [UITabBarItem]) ``` | iOS 2.0 |

Modified [UITabBarDelegate.tabBar(_: UITabBar, didEndCustomizingItems: [UITabBarItem], changed: Bool)](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623447-tabbar)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func tabBar(_ tabBar: UITabBar, didEndCustomizingItems items: [AnyObject], changed changed: Bool) ``` | iOS 8.0 |
| To | ``` optional func tabBar(_ tabBar: UITabBar, didEndCustomizingItems items: [UITabBarItem], changed changed: Bool) ``` | iOS 2.0 |

Modified [UITabBarDelegate.tabBar(_: UITabBar, didSelectItem: UITabBarItem)](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623463-tabbar)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func tabBar(_ tabBar: UITabBar, didSelectItem item: UITabBarItem!) ``` | iOS 8.0 |
| To | ``` optional func tabBar(_ tabBar: UITabBar, didSelectItem item: UITabBarItem) ``` | iOS 2.0 |

Modified [UITabBarDelegate.tabBar(_: UITabBar, willBeginCustomizingItems: [UITabBarItem])](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623451-tabbar)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func tabBar(_ tabBar: UITabBar, willBeginCustomizingItems items: [AnyObject]) ``` | iOS 8.0 |
| To | ``` optional func tabBar(_ tabBar: UITabBar, willBeginCustomizingItems items: [UITabBarItem]) ``` | iOS 2.0 |

Modified [UITabBarDelegate.tabBar(_: UITabBar, willEndCustomizingItems: [UITabBarItem], changed: Bool)](https://developer.apple.com/documentation/uikit/uitabbardelegate/1623464-tabbar)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func tabBar(_ tabBar: UITabBar, willEndCustomizingItems items: [AnyObject], changed changed: Bool) ``` | iOS 8.0 |
| To | ``` optional func tabBar(_ tabBar: UITabBar, willEndCustomizingItems items: [UITabBarItem], changed changed: Bool) ``` | iOS 2.0 |

Modified [UITabBarItem](https://developer.apple.com/documentation/uikit/uitabbaritem)

|  | Declaration |
| --- | --- |
| From | ``` class UITabBarItem : UIBarItem {     init(title title: String?, image image: UIImage?, tag tag: Int)     init(title title: String?, image image: UIImage?, selectedImage selectedImage: UIImage?)     init(tabBarSystemItem systemItem: UITabBarSystemItem, tag tag: Int)     var selectedImage: UIImage!     var badgeValue: String?     func setFinishedSelectedImage(_ selectedImage: UIImage!, withFinishedUnselectedImage unselectedImage: UIImage!)     func finishedSelectedImage() -> UIImage!     func finishedUnselectedImage() -> UIImage!     func setTitlePositionAdjustment(_ adjustment: UIOffset)     func titlePositionAdjustment() -> UIOffset } ``` |
| To | ``` class UITabBarItem : UIBarItem {     init()     init?(coder aDecoder: NSCoder)     convenience init(title title: String?, image image: UIImage?, tag tag: Int)     convenience init(title title: String?, image image: UIImage?, selectedImage selectedImage: UIImage?)     convenience init(tabBarSystemItem systemItem: UITabBarSystemItem, tag tag: Int)     var selectedImage: UIImage?     var badgeValue: String?     func setFinishedSelectedImage(_ selectedImage: UIImage?, withFinishedUnselectedImage unselectedImage: UIImage?)     func finishedSelectedImage() -> UIImage?     func finishedUnselectedImage() -> UIImage?     var titlePositionAdjustment: UIOffset } ``` |

Modified [UITabBarItem.init(tabBarSystemItem: UITabBarSystemItem, tag: Int)](https://developer.apple.com/documentation/uikit/uitabbaritem/1617067-init)

|  | Declaration |
| --- | --- |
| From | ``` init(tabBarSystemItem systemItem: UITabBarSystemItem, tag tag: Int) ``` |
| To | ``` convenience init(tabBarSystemItem systemItem: UITabBarSystemItem, tag tag: Int) ``` |

Modified [UITabBarItem.init(title: String?, image: UIImage?, selectedImage: UIImage?)](https://developer.apple.com/documentation/uikit/uitabbaritem/1617066-init)

|  | Declaration |
| --- | --- |
| From | ``` init(title title: String?, image image: UIImage?, selectedImage selectedImage: UIImage?) ``` |
| To | ``` convenience init(title title: String?, image image: UIImage?, selectedImage selectedImage: UIImage?) ``` |

Modified [UITabBarItem.init(title: String?, image: UIImage?, tag: Int)](https://developer.apple.com/documentation/uikit/uitabbaritem/1617056-init)

|  | Declaration |
| --- | --- |
| From | ``` init(title title: String?, image image: UIImage?, tag tag: Int) ``` |
| To | ``` convenience init(title title: String?, image image: UIImage?, tag tag: Int) ``` |

Modified [UITabBarItem.selectedImage](https://developer.apple.com/documentation/uikit/uitabbaritem/1617072-selectedimage)

|  | Declaration |
| --- | --- |
| From | ``` var selectedImage: UIImage! ``` |
| To | ``` var selectedImage: UIImage? ``` |

Modified [UITabBarItemPositioning [enum]](https://developer.apple.com/documentation/uikit/uitabbaritempositioning)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITabBarSystemItem [enum]](https://developer.apple.com/documentation/uikit/uitabbaritem/systemitem)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITableView](https://developer.apple.com/documentation/uikit/uitableview)

|  | Declaration |
| --- | --- |
| From | ``` class UITableView : UIScrollView, NSCoding {     init(frame frame: CGRect, style style: UITableViewStyle)     var style: UITableViewStyle { get }     unowned(unsafe) var dataSource: UITableViewDataSource?     unowned(unsafe) var delegate: UITableViewDelegate?     var rowHeight: CGFloat     var sectionHeaderHeight: CGFloat     var sectionFooterHeight: CGFloat     var estimatedRowHeight: CGFloat     var estimatedSectionHeaderHeight: CGFloat     var estimatedSectionFooterHeight: CGFloat     var separatorInset: UIEdgeInsets     var backgroundView: UIView?     func reloadData()     func reloadSectionIndexTitles()     func numberOfSections() -> Int     func numberOfRowsInSection(_ section: Int) -> Int     func rectForSection(_ section: Int) -> CGRect     func rectForHeaderInSection(_ section: Int) -> CGRect     func rectForFooterInSection(_ section: Int) -> CGRect     func rectForRowAtIndexPath(_ indexPath: NSIndexPath) -> CGRect     func indexPathForRowAtPoint(_ point: CGPoint) -> NSIndexPath?     func indexPathForCell(_ cell: UITableViewCell) -> NSIndexPath?     func indexPathsForRowsInRect(_ rect: CGRect) -> [AnyObject]     func cellForRowAtIndexPath(_ indexPath: NSIndexPath) -> UITableViewCell?     func visibleCells() -> [AnyObject]     func indexPathsForVisibleRows() -> [AnyObject]?     func headerViewForSection(_ section: Int) -> UITableViewHeaderFooterView?     func footerViewForSection(_ section: Int) -> UITableViewHeaderFooterView?     func scrollToRowAtIndexPath(_ indexPath: NSIndexPath, atScrollPosition scrollPosition: UITableViewScrollPosition, animated animated: Bool)     func scrollToNearestSelectedRowAtScrollPosition(_ scrollPosition: UITableViewScrollPosition, animated animated: Bool)     func beginUpdates()     func endUpdates()     func insertSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func deleteSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func reloadSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func moveSection(_ section: Int, toSection newSection: Int)     func insertRowsAtIndexPaths(_ indexPaths: [AnyObject], withRowAnimation animation: UITableViewRowAnimation)     func deleteRowsAtIndexPaths(_ indexPaths: [AnyObject], withRowAnimation animation: UITableViewRowAnimation)     func reloadRowsAtIndexPaths(_ indexPaths: [AnyObject], withRowAnimation animation: UITableViewRowAnimation)     func moveRowAtIndexPath(_ indexPath: NSIndexPath, toIndexPath newIndexPath: NSIndexPath)     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var allowsSelection: Bool     var allowsSelectionDuringEditing: Bool     var allowsMultipleSelection: Bool     var allowsMultipleSelectionDuringEditing: Bool     func indexPathForSelectedRow() -> NSIndexPath?     func indexPathsForSelectedRows() -> [AnyObject]?     func selectRowAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool, scrollPosition scrollPosition: UITableViewScrollPosition)     func deselectRowAtIndexPath(_ indexPath: NSIndexPath, animated animated: Bool)     var sectionIndexMinimumDisplayRowCount: Int     var sectionIndexColor: UIColor?     var sectionIndexBackgroundColor: UIColor?     var sectionIndexTrackingBackgroundColor: UIColor?     var separatorStyle: UITableViewCellSeparatorStyle     var separatorColor: UIColor!     @NSCopying var separatorEffect: UIVisualEffect?     var tableHeaderView: UIView?     var tableFooterView: UIView?     func dequeueReusableCellWithIdentifier(_ identifier: String) -> AnyObject?     func dequeueReusableCellWithIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath) -> AnyObject     func dequeueReusableHeaderFooterViewWithIdentifier(_ identifier: String) -> AnyObject?     func registerNib(_ nib: UINib, forCellReuseIdentifier identifier: String)     func registerClass(_ cellClass: AnyClass, forCellReuseIdentifier identifier: String)     func registerNib(_ nib: UINib, forHeaderFooterViewReuseIdentifier identifier: String)     func registerClass(_ aClass: AnyClass, forHeaderFooterViewReuseIdentifier identifier: String) } ``` |
| To | ``` class UITableView : UIScrollView {     init(frame frame: CGRect, style style: UITableViewStyle)     init?(coder aDecoder: NSCoder)     var style: UITableViewStyle { get }     weak var dataSource: UITableViewDataSource?     weak var delegate: UITableViewDelegate?     var rowHeight: CGFloat     var sectionHeaderHeight: CGFloat     var sectionFooterHeight: CGFloat     var estimatedRowHeight: CGFloat     var estimatedSectionHeaderHeight: CGFloat     var estimatedSectionFooterHeight: CGFloat     var separatorInset: UIEdgeInsets     var backgroundView: UIView?     func reloadData()     func reloadSectionIndexTitles()     var numberOfSections: Int { get }     func numberOfRowsInSection(_ section: Int) -> Int     func rectForSection(_ section: Int) -> CGRect     func rectForHeaderInSection(_ section: Int) -> CGRect     func rectForFooterInSection(_ section: Int) -> CGRect     func rectForRowAtIndexPath(_ indexPath: NSIndexPath) -> CGRect     func indexPathForRowAtPoint(_ point: CGPoint) -> NSIndexPath?     func indexPathForCell(_ cell: UITableViewCell) -> NSIndexPath?     func indexPathsForRowsInRect(_ rect: CGRect) -> [NSIndexPath]?     func cellForRowAtIndexPath(_ indexPath: NSIndexPath) -> UITableViewCell?     var visibleCells: [UITableViewCell] { get }     var indexPathsForVisibleRows: [NSIndexPath]? { get }     func headerViewForSection(_ section: Int) -> UITableViewHeaderFooterView?     func footerViewForSection(_ section: Int) -> UITableViewHeaderFooterView?     func scrollToRowAtIndexPath(_ indexPath: NSIndexPath, atScrollPosition scrollPosition: UITableViewScrollPosition, animated animated: Bool)     func scrollToNearestSelectedRowAtScrollPosition(_ scrollPosition: UITableViewScrollPosition, animated animated: Bool)     func beginUpdates()     func endUpdates()     func insertSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func deleteSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func reloadSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func moveSection(_ section: Int, toSection newSection: Int)     func insertRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation)     func deleteRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation)     func reloadRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation)     func moveRowAtIndexPath(_ indexPath: NSIndexPath, toIndexPath newIndexPath: NSIndexPath)     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var allowsSelection: Bool     var allowsSelectionDuringEditing: Bool     var allowsMultipleSelection: Bool     var allowsMultipleSelectionDuringEditing: Bool     var indexPathForSelectedRow: NSIndexPath? { get }     var indexPathsForSelectedRows: [NSIndexPath]? { get }     func selectRowAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool, scrollPosition scrollPosition: UITableViewScrollPosition)     func deselectRowAtIndexPath(_ indexPath: NSIndexPath, animated animated: Bool)     var sectionIndexMinimumDisplayRowCount: Int     var sectionIndexColor: UIColor?     var sectionIndexBackgroundColor: UIColor?     var sectionIndexTrackingBackgroundColor: UIColor?     var separatorStyle: UITableViewCellSeparatorStyle     var separatorColor: UIColor?     @NSCopying var separatorEffect: UIVisualEffect?     var cellLayoutMarginsFollowReadableWidth: Bool     var tableHeaderView: UIView?     var tableFooterView: UIView?     func dequeueReusableCellWithIdentifier(_ identifier: String) -> UITableViewCell?     func dequeueReusableCellWithIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath) -> UITableViewCell     func dequeueReusableHeaderFooterViewWithIdentifier(_ identifier: String) -> UITableViewHeaderFooterView?     func registerNib(_ nib: UINib?, forCellReuseIdentifier identifier: String)     func registerClass(_ cellClass: AnyClass?, forCellReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forHeaderFooterViewReuseIdentifier identifier: String)     func registerClass(_ aClass: AnyClass?, forHeaderFooterViewReuseIdentifier identifier: String) } ``` |

Modified [UITableView.dataSource](https://developer.apple.com/documentation/uikit/uitableview/1614955-datasource)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var dataSource: UITableViewDataSource? ``` |
| To | ``` weak var dataSource: UITableViewDataSource? ``` |

Modified [UITableView.delegate](https://developer.apple.com/documentation/uikit/uitableview/1614894-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UITableViewDelegate? ``` |
| To | ``` weak var delegate: UITableViewDelegate? ``` |

Modified [UITableView.deleteRowsAtIndexPaths(_: [NSIndexPath], withRowAnimation: UITableViewRowAnimation)](https://developer.apple.com/documentation/uikit/uitableview/1614960-deleterows)

|  | Declaration |
| --- | --- |
| From | ``` func deleteRowsAtIndexPaths(_ indexPaths: [AnyObject], withRowAnimation animation: UITableViewRowAnimation) ``` |
| To | ``` func deleteRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation) ``` |

Modified [UITableView.dequeueReusableCellWithIdentifier(_: String) -> UITableViewCell?](https://developer.apple.com/documentation/uikit/uitableview/1614891-dequeuereusablecell)

|  | Declaration |
| --- | --- |
| From | ``` func dequeueReusableCellWithIdentifier(_ identifier: String) -> AnyObject? ``` |
| To | ``` func dequeueReusableCellWithIdentifier(_ identifier: String) -> UITableViewCell? ``` |

Modified [UITableView.dequeueReusableCellWithIdentifier(_: String, forIndexPath: NSIndexPath) -> UITableViewCell](https://developer.apple.com/documentation/uikit/uitableview/1614878-dequeuereusablecellwithidentifie)

|  | Declaration |
| --- | --- |
| From | ``` func dequeueReusableCellWithIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath) -> AnyObject ``` |
| To | ``` func dequeueReusableCellWithIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath) -> UITableViewCell ``` |

Modified [UITableView.dequeueReusableHeaderFooterViewWithIdentifier(_: String) -> UITableViewHeaderFooterView?](https://developer.apple.com/documentation/uikit/uitableview/1614975-dequeuereusableheaderfooterview)

|  | Declaration |
| --- | --- |
| From | ``` func dequeueReusableHeaderFooterViewWithIdentifier(_ identifier: String) -> AnyObject? ``` |
| To | ``` func dequeueReusableHeaderFooterViewWithIdentifier(_ identifier: String) -> UITableViewHeaderFooterView? ``` |

Modified [UITableView.indexPathsForRowsInRect(_: CGRect) -> [NSIndexPath]?](https://developer.apple.com/documentation/uikit/uitableview/1614991-indexpathsforrowsinrect)

|  | Declaration |
| --- | --- |
| From | ``` func indexPathsForRowsInRect(_ rect: CGRect) -> [AnyObject] ``` |
| To | ``` func indexPathsForRowsInRect(_ rect: CGRect) -> [NSIndexPath]? ``` |

Modified [UITableView.insertRowsAtIndexPaths(_: [NSIndexPath], withRowAnimation: UITableViewRowAnimation)](https://developer.apple.com/documentation/uikit/uitableview/1614879-insertrows)

|  | Declaration |
| --- | --- |
| From | ``` func insertRowsAtIndexPaths(_ indexPaths: [AnyObject], withRowAnimation animation: UITableViewRowAnimation) ``` |
| To | ``` func insertRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation) ``` |

Modified [UITableView.registerClass(_: AnyClass?, forCellReuseIdentifier: String)](https://developer.apple.com/documentation/uikit/uitableview/1614888-register)

|  | Declaration |
| --- | --- |
| From | ``` func registerClass(_ cellClass: AnyClass, forCellReuseIdentifier identifier: String) ``` |
| To | ``` func registerClass(_ cellClass: AnyClass?, forCellReuseIdentifier identifier: String) ``` |

Modified [UITableView.registerClass(_: AnyClass?, forHeaderFooterViewReuseIdentifier: String)](https://developer.apple.com/documentation/uikit/uitableview/1614964-register)

|  | Declaration |
| --- | --- |
| From | ``` func registerClass(_ aClass: AnyClass, forHeaderFooterViewReuseIdentifier identifier: String) ``` |
| To | ``` func registerClass(_ aClass: AnyClass?, forHeaderFooterViewReuseIdentifier identifier: String) ``` |

Modified [UITableView.registerNib(_: UINib?, forCellReuseIdentifier: String)](https://developer.apple.com/documentation/uikit/uitableview/1614937-registernib)

|  | Declaration |
| --- | --- |
| From | ``` func registerNib(_ nib: UINib, forCellReuseIdentifier identifier: String) ``` |
| To | ``` func registerNib(_ nib: UINib?, forCellReuseIdentifier identifier: String) ``` |

Modified [UITableView.registerNib(_: UINib?, forHeaderFooterViewReuseIdentifier: String)](https://developer.apple.com/documentation/uikit/uitableview/1614921-register)

|  | Declaration |
| --- | --- |
| From | ``` func registerNib(_ nib: UINib, forHeaderFooterViewReuseIdentifier identifier: String) ``` |
| To | ``` func registerNib(_ nib: UINib?, forHeaderFooterViewReuseIdentifier identifier: String) ``` |

Modified [UITableView.reloadRowsAtIndexPaths(_: [NSIndexPath], withRowAnimation: UITableViewRowAnimation)](https://developer.apple.com/documentation/uikit/uitableview/1614935-reloadrowsatindexpaths)

|  | Declaration |
| --- | --- |
| From | ``` func reloadRowsAtIndexPaths(_ indexPaths: [AnyObject], withRowAnimation animation: UITableViewRowAnimation) ``` |
| To | ``` func reloadRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation) ``` |

Modified [UITableView.separatorColor](https://developer.apple.com/documentation/uikit/uitableview/1614984-separatorcolor)

|  | Declaration |
| --- | --- |
| From | ``` var separatorColor: UIColor! ``` |
| To | ``` var separatorColor: UIColor? ``` |

Modified [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell)

|  | Declaration |
| --- | --- |
| From | ``` class UITableViewCell : UIView, NSCoding, UIGestureRecognizerDelegate, NSObjectProtocol {     init(style style: UITableViewCellStyle, reuseIdentifier reuseIdentifier: String?)     var imageView: UIImageView? { get }     var textLabel: UILabel? { get }     var detailTextLabel: UILabel? { get }     var contentView: UIView { get }     var backgroundView: UIView?     var selectedBackgroundView: UIView!     var multipleSelectionBackgroundView: UIView?     var reuseIdentifier: String? { get }     func prepareForReuse()     var selectionStyle: UITableViewCellSelectionStyle     var selected: Bool     var highlighted: Bool     func setSelected(_ selected: Bool, animated animated: Bool)     func setHighlighted(_ highlighted: Bool, animated animated: Bool)     var editingStyle: UITableViewCellEditingStyle { get }     var showsReorderControl: Bool     var shouldIndentWhileEditing: Bool     var accessoryType: UITableViewCellAccessoryType     var accessoryView: UIView?     var editingAccessoryType: UITableViewCellAccessoryType     var editingAccessoryView: UIView?     var indentationLevel: Int     var indentationWidth: CGFloat     var separatorInset: UIEdgeInsets     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var showingDeleteConfirmation: Bool { get }     func willTransitionToState(_ state: UITableViewCellStateMask)     func didTransitionToState(_ state: UITableViewCellStateMask) } extension UITableViewCell {     convenience init!(frame frame: CGRect, reuseIdentifier reuseIdentifier: String!)     var text: String!     var font: UIFont!     var textAlignment: NSTextAlignment     var lineBreakMode: NSLineBreakMode     var textColor: UIColor!     var selectedTextColor: UIColor!     var image: UIImage!     var selectedImage: UIImage!     var hidesAccessoryWhenEditing: Bool     unowned(unsafe) var target: AnyObject!     var editAction: Selector     var accessoryAction: Selector } ``` |
| To | ``` class UITableViewCell : UIView, UIGestureRecognizerDelegate {     init(style style: UITableViewCellStyle, reuseIdentifier reuseIdentifier: String?)     init?(coder aDecoder: NSCoder)     var imageView: UIImageView? { get }     var textLabel: UILabel? { get }     var detailTextLabel: UILabel? { get }     var contentView: UIView { get }     var backgroundView: UIView?     var selectedBackgroundView: UIView?     var multipleSelectionBackgroundView: UIView?     var reuseIdentifier: String? { get }     func prepareForReuse()     var selectionStyle: UITableViewCellSelectionStyle     var selected: Bool     var highlighted: Bool     func setSelected(_ selected: Bool, animated animated: Bool)     func setHighlighted(_ highlighted: Bool, animated animated: Bool)     var editingStyle: UITableViewCellEditingStyle { get }     var showsReorderControl: Bool     var shouldIndentWhileEditing: Bool     var accessoryType: UITableViewCellAccessoryType     var accessoryView: UIView?     var editingAccessoryType: UITableViewCellAccessoryType     var editingAccessoryView: UIView?     var indentationLevel: Int     var indentationWidth: CGFloat     var separatorInset: UIEdgeInsets     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var showingDeleteConfirmation: Bool { get }     func willTransitionToState(_ state: UITableViewCellStateMask)     func didTransitionToState(_ state: UITableViewCellStateMask) } extension UITableViewCell {     convenience init(frame frame: CGRect, reuseIdentifier reuseIdentifier: String?)     var text: String?     var font: UIFont?     var textAlignment: NSTextAlignment     var lineBreakMode: NSLineBreakMode     var textColor: UIColor?     var selectedTextColor: UIColor?     var image: UIImage?     var selectedImage: UIImage?     var hidesAccessoryWhenEditing: Bool     unowned(unsafe) var target: AnyObject?     var editAction: Selector     var accessoryAction: Selector } ``` |

Modified [UITableViewCell.selectedBackgroundView](https://developer.apple.com/documentation/uikit/uitableviewcell/1623226-selectedbackgroundview)

|  | Declaration |
| --- | --- |
| From | ``` var selectedBackgroundView: UIView! ``` |
| To | ``` var selectedBackgroundView: UIView? ``` |

Modified [UITableViewCellAccessoryType [enum]](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITableViewCellEditingStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewcelleditingstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITableViewCellSelectionStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewcellselectionstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITableViewCellSeparatorStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewcellseparatorstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITableViewCellStateMask [struct]](https://developer.apple.com/documentation/uikit/uitableviewcellstatemask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UITableViewCellStateMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var DefaultMask: UITableViewCellStateMask { get }     static var ShowingEditControlMask: UITableViewCellStateMask { get }     static var ShowingDeleteConfirmationMask: UITableViewCellStateMask { get } } ``` | RawOptionSetType |
| To | ``` struct UITableViewCellStateMask : OptionSetType {     init(rawValue rawValue: UInt)     static var DefaultMask: UITableViewCellStateMask { get }     static var ShowingEditControlMask: UITableViewCellStateMask { get }     static var ShowingDeleteConfirmationMask: UITableViewCellStateMask { get } } ``` | OptionSetType |

Modified [UITableViewCellStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewcellstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITableViewController](https://developer.apple.com/documentation/uikit/uitableviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UITableViewController : UIViewController, UITableViewDelegate, NSObjectProtocol, UIScrollViewDelegate, UITableViewDataSource {     init(style style: UITableViewStyle)     init!(nibName nibNameOrNil: String!, bundle nibBundleOrNil: NSBundle!)     init!(coder aDecoder: NSCoder!)     var tableView: UITableView!     var clearsSelectionOnViewWillAppear: Bool     var refreshControl: UIRefreshControl? } ``` |
| To | ``` class UITableViewController : UIViewController, UITableViewDelegate, UIScrollViewDelegate, UITableViewDataSource {     init(style style: UITableViewStyle)     init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     init?(coder aDecoder: NSCoder)     var tableView: UITableView!     var clearsSelectionOnViewWillAppear: Bool     var refreshControl: UIRefreshControl? } ``` |

Modified [UITableViewController.init(coder: NSCoder)](https://developer.apple.com/documentation/uikit/uitableviewcontroller/1614760-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` init!(coder aDecoder: NSCoder!) ``` |
| To | ``` init?(coder aDecoder: NSCoder) ``` |

Modified [UITableViewController.init(nibName: String?, bundle: NSBundle?)](https://developer.apple.com/documentation/uikit/uitableviewcontroller/1614757-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(nibName nibNameOrNil: String!, bundle nibBundleOrNil: NSBundle!) ``` |
| To | ``` init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?) ``` |

Modified [UITableViewDataSource](https://developer.apple.com/documentation/uikit/uitableviewdatasource)

|  | Declaration |
| --- | --- |
| From | ``` protocol UITableViewDataSource : NSObjectProtocol {     func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int     func tableView(_ tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell     optional func numberOfSectionsInTableView(_ tableView: UITableView) -> Int     optional func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String?     optional func tableView(_ tableView: UITableView, titleForFooterInSection section: Int) -> String?     optional func tableView(_ tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func sectionIndexTitlesForTableView(_ tableView: UITableView) -> [AnyObject]!     optional func tableView(_ tableView: UITableView, sectionForSectionIndexTitle title: String, atIndex index: Int) -> Int     optional func tableView(_ tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, moveRowAtIndexPath sourceIndexPath: NSIndexPath, toIndexPath destinationIndexPath: NSIndexPath) } ``` |
| To | ``` protocol UITableViewDataSource : NSObjectProtocol {     func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int     func tableView(_ tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell     optional func numberOfSectionsInTableView(_ tableView: UITableView) -> Int     optional func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String?     optional func tableView(_ tableView: UITableView, titleForFooterInSection section: Int) -> String?     optional func tableView(_ tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func sectionIndexTitlesForTableView(_ tableView: UITableView) -> [String]?     optional func tableView(_ tableView: UITableView, sectionForSectionIndexTitle title: String, atIndex index: Int) -> Int     optional func tableView(_ tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, moveRowAtIndexPath sourceIndexPath: NSIndexPath, toIndexPath destinationIndexPath: NSIndexPath) } ``` |

Modified [UITableViewDataSource.numberOfSectionsInTableView(_: UITableView) -> Int](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614860-numberofsectionsintableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDataSource.sectionIndexTitlesForTableView(_: UITableView) -> [String]?](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614857-sectionindextitlesfortableview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func sectionIndexTitlesForTableView(_ tableView: UITableView) -> [AnyObject]! ``` | iOS 8.0 |
| To | ``` optional func sectionIndexTitlesForTableView(_ tableView: UITableView) -> [String]? ``` | iOS 2.0 |

Modified [UITableViewDataSource.tableView(_: UITableView, canEditRowAtIndexPath: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614900-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDataSource.tableView(_: UITableView, canMoveRowAtIndexPath: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614927-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDataSource.tableView(_: UITableView, cellForRowAtIndexPath: NSIndexPath) -> UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614861-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDataSource.tableView(_: UITableView, commitEditingStyle: UITableViewCellEditingStyle, forRowAtIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614871-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDataSource.tableView(_: UITableView, moveRowAtIndexPath: NSIndexPath, toIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614867-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDataSource.tableView(_: UITableView, numberOfRowsInSection: Int) -> Int](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614931-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDataSource.tableView(_: UITableView, sectionForSectionIndexTitle: String, atIndex: Int) -> Int](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614933-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDataSource.tableView(_: UITableView, titleForFooterInSection: Int) -> String?](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614994-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDataSource.tableView(_: UITableView, titleForHeaderInSection: Int) -> String?](https://developer.apple.com/documentation/uikit/uitableviewdatasource/1614850-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate](https://developer.apple.com/documentation/uikit/uitableviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UITableViewDelegate : NSObjectProtocol, UIScrollViewDelegate {     optional func tableView(_ tableView: UITableView, willDisplayCell cell: UITableViewCell, forRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, willDisplayHeaderView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, willDisplayFooterView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, didEndDisplayingCell cell: UITableViewCell, forRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didEndDisplayingHeaderView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, didEndDisplayingFooterView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat     optional func tableView(_ tableView: UITableView, heightForHeaderInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, heightForFooterInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForHeaderInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForFooterInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, viewForHeaderInSection section: Int) -> UIView?     optional func tableView(_ tableView: UITableView, viewForFooterInSection section: Int) -> UIView?     optional func tableView(_ tableView: UITableView, accessoryTypeForRowWithIndexPath indexPath: NSIndexPath!) -> UITableViewCellAccessoryType     optional func tableView(_ tableView: UITableView, accessoryButtonTappedForRowWithIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, shouldHighlightRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, didHighlightRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didUnhighlightRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, willSelectRowAtIndexPath indexPath: NSIndexPath) -> NSIndexPath?     optional func tableView(_ tableView: UITableView, willDeselectRowAtIndexPath indexPath: NSIndexPath) -> NSIndexPath?     optional func tableView(_ tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didDeselectRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, editingStyleForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCellEditingStyle     optional func tableView(_ tableView: UITableView, titleForDeleteConfirmationButtonForRowAtIndexPath indexPath: NSIndexPath) -> String!     optional func tableView(_ tableView: UITableView, editActionsForRowAtIndexPath indexPath: NSIndexPath) -> [AnyObject]?     optional func tableView(_ tableView: UITableView, shouldIndentWhileEditingRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, willBeginEditingRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didEndEditingRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, targetIndexPathForMoveFromRowAtIndexPath sourceIndexPath: NSIndexPath, toProposedIndexPath proposedDestinationIndexPath: NSIndexPath) -> NSIndexPath     optional func tableView(_ tableView: UITableView, indentationLevelForRowAtIndexPath indexPath: NSIndexPath) -> Int     optional func tableView(_ tableView: UITableView, shouldShowMenuForRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, canPerformAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject) -> Bool     optional func tableView(_ tableView: UITableView, performAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject!) } ``` |
| To | ``` protocol UITableViewDelegate : NSObjectProtocol, UIScrollViewDelegate {     optional func tableView(_ tableView: UITableView, willDisplayCell cell: UITableViewCell, forRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, willDisplayHeaderView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, willDisplayFooterView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, didEndDisplayingCell cell: UITableViewCell, forRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didEndDisplayingHeaderView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, didEndDisplayingFooterView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat     optional func tableView(_ tableView: UITableView, heightForHeaderInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, heightForFooterInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForHeaderInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForFooterInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, viewForHeaderInSection section: Int) -> UIView?     optional func tableView(_ tableView: UITableView, viewForFooterInSection section: Int) -> UIView?     optional func tableView(_ tableView: UITableView, accessoryTypeForRowWithIndexPath indexPath: NSIndexPath) -> UITableViewCellAccessoryType     optional func tableView(_ tableView: UITableView, accessoryButtonTappedForRowWithIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, shouldHighlightRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, didHighlightRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didUnhighlightRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, willSelectRowAtIndexPath indexPath: NSIndexPath) -> NSIndexPath?     optional func tableView(_ tableView: UITableView, willDeselectRowAtIndexPath indexPath: NSIndexPath) -> NSIndexPath?     optional func tableView(_ tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didDeselectRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, editingStyleForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCellEditingStyle     optional func tableView(_ tableView: UITableView, titleForDeleteConfirmationButtonForRowAtIndexPath indexPath: NSIndexPath) -> String?     optional func tableView(_ tableView: UITableView, editActionsForRowAtIndexPath indexPath: NSIndexPath) -> [UITableViewRowAction]?     optional func tableView(_ tableView: UITableView, shouldIndentWhileEditingRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, willBeginEditingRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didEndEditingRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, targetIndexPathForMoveFromRowAtIndexPath sourceIndexPath: NSIndexPath, toProposedIndexPath proposedDestinationIndexPath: NSIndexPath) -> NSIndexPath     optional func tableView(_ tableView: UITableView, indentationLevelForRowAtIndexPath indexPath: NSIndexPath) -> Int     optional func tableView(_ tableView: UITableView, shouldShowMenuForRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, canPerformAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) -> Bool     optional func tableView(_ tableView: UITableView, performAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) } ``` |

Modified [UITableViewDelegate.tableView(_: UITableView, accessoryButtonTappedForRowWithIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614996-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, canPerformAction: Selector, forRowAtIndexPath: NSIndexPath, withSender: AnyObject?) -> Bool](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614898-tableview)

|  | Declaration |
| --- | --- |
| From | ``` optional func tableView(_ tableView: UITableView, canPerformAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject) -> Bool ``` |
| To | ``` optional func tableView(_ tableView: UITableView, canPerformAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) -> Bool ``` |

Modified [UITableViewDelegate.tableView(_: UITableView, didEndEditingRowAtIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614963-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, didSelectRowAtIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614877-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, editActionsForRowAtIndexPath: NSIndexPath) -> [UITableViewRowAction]?](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614956-tableview)

|  | Declaration |
| --- | --- |
| From | ``` optional func tableView(_ tableView: UITableView, editActionsForRowAtIndexPath indexPath: NSIndexPath) -> [AnyObject]? ``` |
| To | ``` optional func tableView(_ tableView: UITableView, editActionsForRowAtIndexPath indexPath: NSIndexPath) -> [UITableViewRowAction]? ``` |

Modified [UITableViewDelegate.tableView(_: UITableView, editingStyleForRowAtIndexPath: NSIndexPath) -> UITableViewCellEditingStyle](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614869-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, heightForFooterInSection: Int) -> CGFloat](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614967-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, heightForHeaderInSection: Int) -> CGFloat](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614855-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, heightForRowAtIndexPath: NSIndexPath) -> CGFloat](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614998-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, indentationLevelForRowAtIndexPath: NSIndexPath) -> Int](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614966-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, performAction: Selector, forRowAtIndexPath: NSIndexPath, withSender: AnyObject?)](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614980-tableview)

|  | Declaration |
| --- | --- |
| From | ``` optional func tableView(_ tableView: UITableView, performAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject!) ``` |
| To | ``` optional func tableView(_ tableView: UITableView, performAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) ``` |

Modified [UITableViewDelegate.tableView(_: UITableView, shouldIndentWhileEditingRowAtIndexPath: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614873-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, targetIndexPathForMoveFromRowAtIndexPath: NSIndexPath, toProposedIndexPath: NSIndexPath) -> NSIndexPath](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614953-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, titleForDeleteConfirmationButtonForRowAtIndexPath: NSIndexPath) -> String?](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614970-tableview)

|  | Declaration |
| --- | --- |
| From | ``` optional func tableView(_ tableView: UITableView, titleForDeleteConfirmationButtonForRowAtIndexPath indexPath: NSIndexPath) -> String! ``` |
| To | ``` optional func tableView(_ tableView: UITableView, titleForDeleteConfirmationButtonForRowAtIndexPath indexPath: NSIndexPath) -> String? ``` |

Modified [UITableViewDelegate.tableView(_: UITableView, viewForFooterInSection: Int) -> UIView?](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614946-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, viewForHeaderInSection: Int) -> UIView?](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614901-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, willBeginEditingRowAtIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614907-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, willDisplayCell: UITableViewCell, forRowAtIndexPath: NSIndexPath)](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614883-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewDelegate.tableView(_: UITableView, willSelectRowAtIndexPath: NSIndexPath) -> NSIndexPath?](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614943-tableview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITableViewHeaderFooterView](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview)

|  | Declaration |
| --- | --- |
| From | ``` class UITableViewHeaderFooterView : UIView {     var tintColor: UIColor?     var textLabel: UILabel { get }     var detailTextLabel: UILabel! { get }     var contentView: UIView { get }     var backgroundView: UIView?     var reuseIdentifier: String? { get }     init(reuseIdentifier reuseIdentifier: String?)     func prepareForReuse() } ``` |
| To | ``` class UITableViewHeaderFooterView : UIView {     init(reuseIdentifier reuseIdentifier: String?)     init?(coder aDecoder: NSCoder)     var tintColor: UIColor!     var textLabel: UILabel? { get }     var detailTextLabel: UILabel? { get }     var contentView: UIView { get }     var backgroundView: UIView?     var reuseIdentifier: String? { get }     func prepareForReuse() } ``` |

Modified [UITableViewHeaderFooterView.detailTextLabel](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624910-detailtextlabel)

|  | Declaration |
| --- | --- |
| From | ``` var detailTextLabel: UILabel! { get } ``` |
| To | ``` var detailTextLabel: UILabel? { get } ``` |

Modified [UITableViewHeaderFooterView.textLabel](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/1624912-textlabel)

|  | Declaration |
| --- | --- |
| From | ``` var textLabel: UILabel { get } ``` |
| To | ``` var textLabel: UILabel? { get } ``` |

Modified UITableViewHeaderFooterView.tintColor

|  | Declaration |
| --- | --- |
| From | ``` var tintColor: UIColor? ``` |
| To | ``` var tintColor: UIColor! ``` |

Modified [UITableViewRowAction](https://developer.apple.com/documentation/uikit/uitableviewrowaction)

|  | Declaration |
| --- | --- |
| From | ``` class UITableViewRowAction : NSObject, NSCopying {     convenience init(style style: UITableViewRowActionStyle, title title: String!, handler handler: (UITableViewRowAction!, NSIndexPath!) -> Void)     class func rowActionWithStyle(_ style: UITableViewRowActionStyle, title title: String!, handler handler: (UITableViewRowAction!, NSIndexPath!) -> Void) -> Self     var style: UITableViewRowActionStyle { get }     var title: String!     @NSCopying var backgroundColor: UIColor!     @NSCopying var backgroundEffect: UIVisualEffect? } ``` |
| To | ``` class UITableViewRowAction : NSObject, NSCopying {     convenience init(style style: UITableViewRowActionStyle, title title: String?, handler handler: (UITableViewRowAction, NSIndexPath) -> Void)     class func rowActionWithStyle(_ style: UITableViewRowActionStyle, title title: String?, handler handler: (UITableViewRowAction, NSIndexPath) -> Void) -> Self     var style: UITableViewRowActionStyle { get }     var title: String?     @NSCopying var backgroundColor: UIColor?     @NSCopying var backgroundEffect: UIVisualEffect? } ``` |

Modified [UITableViewRowAction.backgroundColor](https://developer.apple.com/documentation/uikit/uitableviewrowaction/1614995-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var backgroundColor: UIColor! ``` |
| To | ``` @NSCopying var backgroundColor: UIColor? ``` |

Modified [UITableViewRowAction.init(style: UITableViewRowActionStyle, title: String?, handler: (UITableViewRowAction, NSIndexPath) -> Void)](https://developer.apple.com/documentation/uikit/uitableviewrowaction/1614893-rowactionwithstyle)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(style style: UITableViewRowActionStyle, title title: String!, handler handler: (UITableViewRowAction!, NSIndexPath!) -> Void) ``` |
| To | ``` convenience init(style style: UITableViewRowActionStyle, title title: String?, handler handler: (UITableViewRowAction, NSIndexPath) -> Void) ``` |

Modified [UITableViewRowAction.title](https://developer.apple.com/documentation/uikit/uitableviewrowaction/1614993-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String? ``` |

Modified [UITableViewRowActionStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewrowaction/style)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum UITableViewRowActionStyle : Int {     case Default     case Normal } ``` | -- |
| To | ``` enum UITableViewRowActionStyle : Int {     case Default     static var Destructive: UITableViewRowActionStyle { get }     case Normal } ``` | Int |

Modified [UITableViewRowAnimation [enum]](https://developer.apple.com/documentation/uikit/uitableviewrowanimation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITableViewScrollPosition [enum]](https://developer.apple.com/documentation/uikit/uitableview/scrollposition)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITableViewStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITextAutocapitalizationType [enum]](https://developer.apple.com/documentation/uikit/uitextautocapitalizationtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITextAutocorrectionType [enum]](https://developer.apple.com/documentation/uikit/uitextautocorrectiontype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITextBorderStyle [enum]](https://developer.apple.com/documentation/uikit/uitextfield/borderstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITextChecker](https://developer.apple.com/documentation/uikit/uitextchecker)

|  | Declaration |
| --- | --- |
| From | ``` class UITextChecker : NSObject {     func rangeOfMisspelledWordInString(_ stringToCheck: String!, range range: NSRange, startingAt startingOffset: Int, wrap wrapFlag: Bool, language language: String) -> NSRange     func guessesForWordRange(_ range: NSRange, inString string: String, language language: String) -> [AnyObject]?     func completionsForPartialWordRange(_ range: NSRange, inString string: String?, language language: String) -> [AnyObject]?     func ignoreWord(_ wordToIgnore: String)     func ignoredWords() -> [AnyObject]!     func setIgnoredWords(_ words: [AnyObject]!)     class func learnWord(_ word: String!)     class func hasLearnedWord(_ word: String) -> Bool     class func unlearnWord(_ word: String)     class func availableLanguages() -> [AnyObject] } ``` |
| To | ``` class UITextChecker : NSObject {     func rangeOfMisspelledWordInString(_ stringToCheck: String, range range: NSRange, startingAt startingOffset: Int, wrap wrapFlag: Bool, language language: String) -> NSRange     func guessesForWordRange(_ range: NSRange, inString string: String, language language: String) -> [AnyObject]?     func completionsForPartialWordRange(_ range: NSRange, inString string: String?, language language: String) -> [AnyObject]?     func ignoreWord(_ wordToIgnore: String)     func ignoredWords() -> [AnyObject]?     func setIgnoredWords(_ words: [AnyObject]?)     class func learnWord(_ word: String)     class func hasLearnedWord(_ word: String) -> Bool     class func unlearnWord(_ word: String)     class func availableLanguages() -> [AnyObject] } ``` |

Modified [UITextChecker.ignoredWords() -> [AnyObject]?](https://developer.apple.com/documentation/uikit/uitextchecker/1621032-ignoredwords)

|  | Declaration |
| --- | --- |
| From | ``` func ignoredWords() -> [AnyObject]! ``` |
| To | ``` func ignoredWords() -> [AnyObject]? ``` |

Modified [UITextChecker.learnWord(_: String) [class]](https://developer.apple.com/documentation/uikit/uitextchecker/1621028-learnword)

|  | Declaration |
| --- | --- |
| From | ``` class func learnWord(_ word: String!) ``` |
| To | ``` class func learnWord(_ word: String) ``` |

Modified [UITextChecker.rangeOfMisspelledWordInString(_: String, range: NSRange, startingAt: Int, wrap: Bool, language: String) -> NSRange](https://developer.apple.com/documentation/uikit/uitextchecker/1621029-rangeofmisspelledword)

|  | Declaration |
| --- | --- |
| From | ``` func rangeOfMisspelledWordInString(_ stringToCheck: String!, range range: NSRange, startingAt startingOffset: Int, wrap wrapFlag: Bool, language language: String) -> NSRange ``` |
| To | ``` func rangeOfMisspelledWordInString(_ stringToCheck: String, range range: NSRange, startingAt startingOffset: Int, wrap wrapFlag: Bool, language language: String) -> NSRange ``` |

Modified UITextChecker.setIgnoredWords(_: [AnyObject]?)

|  | Declaration |
| --- | --- |
| From | ``` func setIgnoredWords(_ words: [AnyObject]!) ``` |
| To | ``` func setIgnoredWords(_ words: [AnyObject]?) ``` |

Modified [UITextDocumentProxy](https://developer.apple.com/documentation/uikit/uitextdocumentproxy)

|  | Declaration |
| --- | --- |
| From | ``` protocol UITextDocumentProxy : UIKeyInput, UITextInputTraits, NSObjectProtocol {     var documentContextBeforeInput: String! { get }     var documentContextAfterInput: String! { get }     func adjustTextPositionByCharacterOffset(_ offset: Int) } ``` |
| To | ``` protocol UITextDocumentProxy : UIKeyInput, UITextInputTraits, NSObjectProtocol {     var documentContextBeforeInput: String? { get }     var documentContextAfterInput: String? { get }     func adjustTextPositionByCharacterOffset(_ offset: Int) } ``` |

Modified [UITextDocumentProxy.documentContextAfterInput](https://developer.apple.com/documentation/uikit/uitextdocumentproxy/1618199-documentcontextafterinput)

|  | Declaration |
| --- | --- |
| From | ``` var documentContextAfterInput: String! { get } ``` |
| To | ``` var documentContextAfterInput: String? { get } ``` |

Modified [UITextDocumentProxy.documentContextBeforeInput](https://developer.apple.com/documentation/uikit/uitextdocumentproxy/1618190-documentcontextbeforeinput)

|  | Declaration |
| --- | --- |
| From | ``` var documentContextBeforeInput: String! { get } ``` |
| To | ``` var documentContextBeforeInput: String? { get } ``` |

Modified [UITextField](https://developer.apple.com/documentation/uikit/uitextfield)

|  | Declaration |
| --- | --- |
| From | ``` class UITextField : UIControl, UITextInput, UIKeyInput, UITextInputTraits, NSObjectProtocol, NSCoding {     var text: String!     @NSCopying var attributedText: NSAttributedString?     var textColor: UIColor!     var font: UIFont!     var textAlignment: NSTextAlignment     var borderStyle: UITextBorderStyle     var defaultTextAttributes: [NSObject : AnyObject]!     var placeholder: String?     @NSCopying var attributedPlaceholder: NSAttributedString?     var clearsOnBeginEditing: Bool     var adjustsFontSizeToFitWidth: Bool     var minimumFontSize: CGFloat     unowned(unsafe) var delegate: UITextFieldDelegate?     var background: UIImage?     var disabledBackground: UIImage?     var editing: Bool { get }     var allowsEditingTextAttributes: Bool     var typingAttributes: [NSObject : AnyObject]?     var clearButtonMode: UITextFieldViewMode     var leftView: UIView?     var leftViewMode: UITextFieldViewMode     var rightView: UIView?     var rightViewMode: UITextFieldViewMode     func borderRectForBounds(_ bounds: CGRect) -> CGRect     func textRectForBounds(_ bounds: CGRect) -> CGRect     func placeholderRectForBounds(_ bounds: CGRect) -> CGRect     func editingRectForBounds(_ bounds: CGRect) -> CGRect     func clearButtonRectForBounds(_ bounds: CGRect) -> CGRect     func leftViewRectForBounds(_ bounds: CGRect) -> CGRect     func rightViewRectForBounds(_ bounds: CGRect) -> CGRect     func drawTextInRect(_ rect: CGRect)     func drawPlaceholderInRect(_ rect: CGRect)     var inputView: UIView?     var inputAccessoryView: UIView?     var clearsOnInsertion: Bool } ``` |
| To | ``` class UITextField : UIControl, UITextInput, UIKeyInput, UITextInputTraits {     var text: String?     @NSCopying var attributedText: NSAttributedString?     var textColor: UIColor?     var font: UIFont?     var textAlignment: NSTextAlignment     var borderStyle: UITextBorderStyle     var defaultTextAttributes: [String : AnyObject]     var placeholder: String?     @NSCopying var attributedPlaceholder: NSAttributedString?     var clearsOnBeginEditing: Bool     var adjustsFontSizeToFitWidth: Bool     var minimumFontSize: CGFloat     weak var delegate: UITextFieldDelegate?     var background: UIImage?     var disabledBackground: UIImage?     var editing: Bool { get }     var allowsEditingTextAttributes: Bool     var typingAttributes: [String : AnyObject]?     var clearButtonMode: UITextFieldViewMode     var leftView: UIView?     var leftViewMode: UITextFieldViewMode     var rightView: UIView?     var rightViewMode: UITextFieldViewMode     func borderRectForBounds(_ bounds: CGRect) -> CGRect     func textRectForBounds(_ bounds: CGRect) -> CGRect     func placeholderRectForBounds(_ bounds: CGRect) -> CGRect     func editingRectForBounds(_ bounds: CGRect) -> CGRect     func clearButtonRectForBounds(_ bounds: CGRect) -> CGRect     func leftViewRectForBounds(_ bounds: CGRect) -> CGRect     func rightViewRectForBounds(_ bounds: CGRect) -> CGRect     func drawTextInRect(_ rect: CGRect)     func drawPlaceholderInRect(_ rect: CGRect)     var inputView: UIView?     var inputAccessoryView: UIView?     var clearsOnInsertion: Bool } ``` |

Modified [UITextField.defaultTextAttributes](https://developer.apple.com/documentation/uikit/uitextfield/1619618-defaulttextattributes)

|  | Declaration |
| --- | --- |
| From | ``` var defaultTextAttributes: [NSObject : AnyObject]! ``` |
| To | ``` var defaultTextAttributes: [String : AnyObject] ``` |

Modified [UITextField.delegate](https://developer.apple.com/documentation/uikit/uitextfield/1619595-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UITextFieldDelegate? ``` |
| To | ``` weak var delegate: UITextFieldDelegate? ``` |

Modified [UITextField.font](https://developer.apple.com/documentation/uikit/uitextfield/1619604-font)

|  | Declaration |
| --- | --- |
| From | ``` var font: UIFont! ``` |
| To | ``` var font: UIFont? ``` |

Modified [UITextField.text](https://developer.apple.com/documentation/uikit/uitextfield/1619635-text)

|  | Declaration |
| --- | --- |
| From | ``` var text: String! ``` |
| To | ``` var text: String? ``` |

Modified [UITextField.textColor](https://developer.apple.com/documentation/uikit/uitextfield/1619617-textcolor)

|  | Declaration |
| --- | --- |
| From | ``` var textColor: UIColor! ``` |
| To | ``` var textColor: UIColor? ``` |

Modified [UITextField.typingAttributes](https://developer.apple.com/documentation/uikit/uitextfield/1619632-typingattributes)

|  | Declaration |
| --- | --- |
| From | ``` var typingAttributes: [NSObject : AnyObject]? ``` |
| To | ``` var typingAttributes: [String : AnyObject]? ``` |

Modified [UITextFieldDelegate.textField(_: UITextField, shouldChangeCharactersInRange: NSRange, replacementString: String) -> Bool](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619599-textfield)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextFieldDelegate.textFieldDidBeginEditing(_: UITextField)](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619590-textfielddidbeginediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextFieldDelegate.textFieldDidEndEditing(_: UITextField)](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619591-textfielddidendediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextFieldDelegate.textFieldShouldBeginEditing(_: UITextField) -> Bool](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619601-textfieldshouldbeginediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextFieldDelegate.textFieldShouldClear(_: UITextField) -> Bool](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619594-textfieldshouldclear)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextFieldDelegate.textFieldShouldEndEditing(_: UITextField) -> Bool](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619592-textfieldshouldendediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextFieldDelegate.textFieldShouldReturn(_: UITextField) -> Bool](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619603-textfieldshouldreturn)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextFieldViewMode [enum]](https://developer.apple.com/documentation/uikit/uitextfield/viewmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITextGranularity [enum]](https://developer.apple.com/documentation/uikit/uitextgranularity)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput)

|  | Declaration |
| --- | --- |
| From | ``` protocol UITextInput : UIKeyInput, UITextInputTraits, NSObjectProtocol {     func textInRange(_ range: UITextRange) -> String     func replaceRange(_ range: UITextRange, withText text: String)     @NSCopying var selectedTextRange: UITextRange? { get set }     var markedTextRange: UITextRange? { get }     var markedTextStyle: [NSObject : AnyObject]! { get set }     func setMarkedText(_ markedText: String!, selectedRange selectedRange: NSRange)     func unmarkText()     var beginningOfDocument: UITextPosition! { get }     var endOfDocument: UITextPosition { get }     func textRangeFromPosition(_ fromPosition: UITextPosition!, toPosition toPosition: UITextPosition!) -> UITextRange!     func positionFromPosition(_ position: UITextPosition, offset offset: Int) -> UITextPosition?     func positionFromPosition(_ position: UITextPosition, inDirection direction: UITextLayoutDirection, offset offset: Int) -> UITextPosition?     func comparePosition(_ position: UITextPosition, toPosition other: UITextPosition) -> NSComparisonResult     func offsetFromPosition(_ from: UITextPosition, toPosition toPosition: UITextPosition) -> Int     unowned(unsafe) var inputDelegate: UITextInputDelegate! { get set }     var tokenizer: UITextInputTokenizer { get }     func positionWithinRange(_ range: UITextRange!, farthestInDirection direction: UITextLayoutDirection) -> UITextPosition!     func characterRangeByExtendingPosition(_ position: UITextPosition, inDirection direction: UITextLayoutDirection) -> UITextRange!     func baseWritingDirectionForPosition(_ position: UITextPosition, inDirection direction: UITextStorageDirection) -> UITextWritingDirection     func setBaseWritingDirection(_ writingDirection: UITextWritingDirection, forRange range: UITextRange!)     func firstRectForRange(_ range: UITextRange) -> CGRect     func caretRectForPosition(_ position: UITextPosition!) -> CGRect     func selectionRectsForRange(_ range: UITextRange) -> [AnyObject]     func closestPositionToPoint(_ point: CGPoint) -> UITextPosition!     func closestPositionToPoint(_ point: CGPoint, withinRange range: UITextRange!) -> UITextPosition!     func characterRangeAtPoint(_ point: CGPoint) -> UITextRange?     optional func shouldChangeTextInRange(_ range: UITextRange, replacementText text: String) -> Bool     optional func textStylingAtPosition(_ position: UITextPosition, inDirection direction: UITextStorageDirection) -> [NSObject : AnyObject]!     optional func positionWithinRange(_ range: UITextRange!, atCharacterOffset offset: Int) -> UITextPosition!     optional func characterOffsetOfPosition(_ position: UITextPosition, withinRange range: UITextRange) -> Int     optional var textInputView: UIView { get }     optional var selectionAffinity: UITextStorageDirection { get set }     optional func insertDictationResult(_ dictationResult: [AnyObject])     optional func dictationRecordingDidEnd()     optional func dictationRecognitionFailed()     optional func insertDictationResultPlaceholder() -> AnyObject     optional func frameForDictationResultPlaceholder(_ placeholder: AnyObject!) -> CGRect     optional func removeDictationResultPlaceholder(_ placeholder: AnyObject, willInsertResult willInsertResult: Bool) } ``` |
| To | ``` protocol UITextInput : UIKeyInput, UITextInputTraits, NSObjectProtocol {     func textInRange(_ range: UITextRange) -> String?     func replaceRange(_ range: UITextRange, withText text: String)     @NSCopying var selectedTextRange: UITextRange? { get set }     var markedTextRange: UITextRange? { get }     var markedTextStyle: [NSObject : AnyObject]? { get set }     func setMarkedText(_ markedText: String?, selectedRange selectedRange: NSRange)     func unmarkText()     var beginningOfDocument: UITextPosition { get }     var endOfDocument: UITextPosition { get }     func textRangeFromPosition(_ fromPosition: UITextPosition, toPosition toPosition: UITextPosition) -> UITextRange?     func positionFromPosition(_ position: UITextPosition, offset offset: Int) -> UITextPosition?     func positionFromPosition(_ position: UITextPosition, inDirection direction: UITextLayoutDirection, offset offset: Int) -> UITextPosition?     func comparePosition(_ position: UITextPosition, toPosition other: UITextPosition) -> NSComparisonResult     func offsetFromPosition(_ from: UITextPosition, toPosition toPosition: UITextPosition) -> Int     weak var inputDelegate: UITextInputDelegate? { get set }     var tokenizer: UITextInputTokenizer { get }     func positionWithinRange(_ range: UITextRange, farthestInDirection direction: UITextLayoutDirection) -> UITextPosition?     func characterRangeByExtendingPosition(_ position: UITextPosition, inDirection direction: UITextLayoutDirection) -> UITextRange?     func baseWritingDirectionForPosition(_ position: UITextPosition, inDirection direction: UITextStorageDirection) -> UITextWritingDirection     func setBaseWritingDirection(_ writingDirection: UITextWritingDirection, forRange range: UITextRange)     func firstRectForRange(_ range: UITextRange) -> CGRect     func caretRectForPosition(_ position: UITextPosition) -> CGRect     func selectionRectsForRange(_ range: UITextRange) -> [AnyObject]     func closestPositionToPoint(_ point: CGPoint) -> UITextPosition?     func closestPositionToPoint(_ point: CGPoint, withinRange range: UITextRange) -> UITextPosition?     func characterRangeAtPoint(_ point: CGPoint) -> UITextRange?     optional func shouldChangeTextInRange(_ range: UITextRange, replacementText text: String) -> Bool     optional func textStylingAtPosition(_ position: UITextPosition, inDirection direction: UITextStorageDirection) -> [String : AnyObject]?     optional func positionWithinRange(_ range: UITextRange, atCharacterOffset offset: Int) -> UITextPosition?     optional func characterOffsetOfPosition(_ position: UITextPosition, withinRange range: UITextRange) -> Int     optional var textInputView: UIView { get }     optional var selectionAffinity: UITextStorageDirection { get set }     optional func insertDictationResult(_ dictationResult: [UIDictationPhrase])     optional func dictationRecordingDidEnd()     optional func dictationRecognitionFailed()     optional func insertDictationResultPlaceholder() -> AnyObject     optional func frameForDictationResultPlaceholder(_ placeholder: AnyObject) -> CGRect     optional func removeDictationResultPlaceholder(_ placeholder: AnyObject, willInsertResult willInsertResult: Bool)     optional func beginFloatingCursorAtPoint(_ point: CGPoint)     optional func updateFloatingCursorAtPoint(_ point: CGPoint)     optional func endFloatingCursor() } ``` |

Modified [UITextInput.baseWritingDirectionForPosition(_: UITextPosition, inDirection: UITextStorageDirection) -> UITextWritingDirection](https://developer.apple.com/documentation/uikit/uitextinput/1614502-basewritingdirectionforposition)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.beginningOfDocument](https://developer.apple.com/documentation/uikit/uitextinput/1614528-beginningofdocument)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var beginningOfDocument: UITextPosition! { get } ``` | iOS 8.0 |
| To | ``` var beginningOfDocument: UITextPosition { get } ``` | iOS 3.2 |

Modified [UITextInput.caretRectForPosition(_: UITextPosition) -> CGRect](https://developer.apple.com/documentation/uikit/uitextinput/1614518-caretrectforposition)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func caretRectForPosition(_ position: UITextPosition!) -> CGRect ``` | iOS 8.0 |
| To | ``` func caretRectForPosition(_ position: UITextPosition) -> CGRect ``` | iOS 3.2 |

Modified [UITextInput.characterOffsetOfPosition(_: UITextPosition, withinRange: UITextRange) -> Int](https://developer.apple.com/documentation/uikit/uitextinput/1614545-characteroffset)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.characterRangeAtPoint(_: CGPoint) -> UITextRange?](https://developer.apple.com/documentation/uikit/uitextinput/1614574-characterrange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.characterRangeByExtendingPosition(_: UITextPosition, inDirection: UITextLayoutDirection) -> UITextRange?](https://developer.apple.com/documentation/uikit/uitextinput/1614462-characterrangebyextendingpositio)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func characterRangeByExtendingPosition(_ position: UITextPosition, inDirection direction: UITextLayoutDirection) -> UITextRange! ``` | iOS 8.0 |
| To | ``` func characterRangeByExtendingPosition(_ position: UITextPosition, inDirection direction: UITextLayoutDirection) -> UITextRange? ``` | iOS 3.2 |

Modified [UITextInput.closestPositionToPoint(_: CGPoint) -> UITextPosition?](https://developer.apple.com/documentation/uikit/uitextinput/1614523-closestpositiontopoint)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func closestPositionToPoint(_ point: CGPoint) -> UITextPosition! ``` | iOS 8.0 |
| To | ``` func closestPositionToPoint(_ point: CGPoint) -> UITextPosition? ``` | iOS 3.2 |

Modified [UITextInput.closestPositionToPoint(_: CGPoint, withinRange: UITextRange) -> UITextPosition?](https://developer.apple.com/documentation/uikit/uitextinput/1614533-closestposition)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func closestPositionToPoint(_ point: CGPoint, withinRange range: UITextRange!) -> UITextPosition! ``` | iOS 8.0 |
| To | ``` func closestPositionToPoint(_ point: CGPoint, withinRange range: UITextRange) -> UITextPosition? ``` | iOS 3.2 |

Modified [UITextInput.comparePosition(_: UITextPosition, toPosition: UITextPosition) -> NSComparisonResult](https://developer.apple.com/documentation/uikit/uitextinput/1614526-compareposition)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.endOfDocument](https://developer.apple.com/documentation/uikit/uitextinput/1614555-endofdocument)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.firstRectForRange(_: UITextRange) -> CGRect](https://developer.apple.com/documentation/uikit/uitextinput/1614570-firstrectforrange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.frameForDictationResultPlaceholder(_: AnyObject) -> CGRect](https://developer.apple.com/documentation/uikit/uitextinput/1614493-framefordictationresultplacehold)

|  | Declaration |
| --- | --- |
| From | ``` optional func frameForDictationResultPlaceholder(_ placeholder: AnyObject!) -> CGRect ``` |
| To | ``` optional func frameForDictationResultPlaceholder(_ placeholder: AnyObject) -> CGRect ``` |

Modified [UITextInput.inputDelegate](https://developer.apple.com/documentation/uikit/uitextinput/1614508-inputdelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var inputDelegate: UITextInputDelegate! { get set } ``` |
| To | ``` weak var inputDelegate: UITextInputDelegate? { get set } ``` |

Modified [UITextInput.insertDictationResult(_: [UIDictationPhrase])](https://developer.apple.com/documentation/uikit/uitextinput/1614568-insertdictationresult)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func insertDictationResult(_ dictationResult: [AnyObject]) ``` | iOS 8.0 |
| To | ``` optional func insertDictationResult(_ dictationResult: [UIDictationPhrase]) ``` | iOS 5.1 |

Modified [UITextInput.markedTextRange](https://developer.apple.com/documentation/uikit/uitextinput/1614489-markedtextrange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.markedTextStyle](https://developer.apple.com/documentation/uikit/uitextinput/1614500-markedtextstyle)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var markedTextStyle: [NSObject : AnyObject]! { get set } ``` | iOS 8.0 |
| To | ``` var markedTextStyle: [NSObject : AnyObject]? { get set } ``` | iOS 2.0 |

Modified [UITextInput.offsetFromPosition(_: UITextPosition, toPosition: UITextPosition) -> Int](https://developer.apple.com/documentation/uikit/uitextinput/1614473-offsetfromposition)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.positionFromPosition(_: UITextPosition, inDirection: UITextLayoutDirection, offset: Int) -> UITextPosition?](https://developer.apple.com/documentation/uikit/uitextinput/1614515-position)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.positionFromPosition(_: UITextPosition, offset: Int) -> UITextPosition?](https://developer.apple.com/documentation/uikit/uitextinput/1614511-position)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.positionWithinRange(_: UITextRange, atCharacterOffset: Int) -> UITextPosition?](https://developer.apple.com/documentation/uikit/uitextinput/1614542-positionwithinrange)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func positionWithinRange(_ range: UITextRange!, atCharacterOffset offset: Int) -> UITextPosition! ``` | iOS 8.0 |
| To | ``` optional func positionWithinRange(_ range: UITextRange, atCharacterOffset offset: Int) -> UITextPosition? ``` | iOS 3.2 |

Modified [UITextInput.positionWithinRange(_: UITextRange, farthestInDirection: UITextLayoutDirection) -> UITextPosition?](https://developer.apple.com/documentation/uikit/uitextinput/1614547-positionwithinrange)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func positionWithinRange(_ range: UITextRange!, farthestInDirection direction: UITextLayoutDirection) -> UITextPosition! ``` | iOS 8.0 |
| To | ``` func positionWithinRange(_ range: UITextRange, farthestInDirection direction: UITextLayoutDirection) -> UITextPosition? ``` | iOS 3.2 |

Modified [UITextInput.replaceRange(_: UITextRange, withText: String)](https://developer.apple.com/documentation/uikit/uitextinput/1614558-replace)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.selectedTextRange](https://developer.apple.com/documentation/uikit/uitextinput/1614541-selectedtextrange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInput.setBaseWritingDirection(_: UITextWritingDirection, forRange: UITextRange)](https://developer.apple.com/documentation/uikit/uitextinput/1614563-setbasewritingdirection)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setBaseWritingDirection(_ writingDirection: UITextWritingDirection, forRange range: UITextRange!) ``` | iOS 8.0 |
| To | ``` func setBaseWritingDirection(_ writingDirection: UITextWritingDirection, forRange range: UITextRange) ``` | iOS 3.2 |

Modified [UITextInput.setMarkedText(_: String?, selectedRange: NSRange)](https://developer.apple.com/documentation/uikit/uitextinput/1614465-setmarkedtext)

|  | Declaration |
| --- | --- |
| From | ``` func setMarkedText(_ markedText: String!, selectedRange selectedRange: NSRange) ``` |
| To | ``` func setMarkedText(_ markedText: String?, selectedRange selectedRange: NSRange) ``` |

Modified [UITextInput.textInputView](https://developer.apple.com/documentation/uikit/uitextinput/1614564-textinputview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextInput.textInRange(_: UITextRange) -> String?](https://developer.apple.com/documentation/uikit/uitextinput/1614527-textinrange)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func textInRange(_ range: UITextRange) -> String ``` | iOS 8.0 |
| To | ``` func textInRange(_ range: UITextRange) -> String? ``` | iOS 3.2 |

Modified [UITextInput.textRangeFromPosition(_: UITextPosition, toPosition: UITextPosition) -> UITextRange?](https://developer.apple.com/documentation/uikit/uitextinput/1614573-textrangefromposition)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func textRangeFromPosition(_ fromPosition: UITextPosition!, toPosition toPosition: UITextPosition!) -> UITextRange! ``` | iOS 8.0 |
| To | ``` func textRangeFromPosition(_ fromPosition: UITextPosition, toPosition toPosition: UITextPosition) -> UITextRange? ``` | iOS 3.2 |

Modified [UITextInput.textStylingAtPosition(_: UITextPosition, inDirection: UITextStorageDirection) -> [String : AnyObject]?](https://developer.apple.com/documentation/uikit/uitextinput/1614566-textstylingatposition)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func textStylingAtPosition(_ position: UITextPosition, inDirection direction: UITextStorageDirection) -> [NSObject : AnyObject]! ``` | iOS 8.0 |
| To | ``` optional func textStylingAtPosition(_ position: UITextPosition, inDirection direction: UITextStorageDirection) -> [String : AnyObject]? ``` | iOS 3.2 |

Modified [UITextInputDelegate](https://developer.apple.com/documentation/uikit/uitextinputdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UITextInputDelegate : NSObjectProtocol {     func selectionWillChange(_ textInput: UITextInput)     func selectionDidChange(_ textInput: UITextInput)     func textWillChange(_ textInput: UITextInput)     func textDidChange(_ textInput: UITextInput) } ``` |
| To | ``` protocol UITextInputDelegate : NSObjectProtocol {     func selectionWillChange(_ textInput: UITextInput?)     func selectionDidChange(_ textInput: UITextInput?)     func textWillChange(_ textInput: UITextInput?)     func textDidChange(_ textInput: UITextInput?) } ``` |

Modified [UITextInputDelegate.selectionDidChange(_: UITextInput?)](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614551-selectiondidchange)

|  | Declaration |
| --- | --- |
| From | ``` func selectionDidChange(_ textInput: UITextInput) ``` |
| To | ``` func selectionDidChange(_ textInput: UITextInput?) ``` |

Modified [UITextInputDelegate.selectionWillChange(_: UITextInput?)](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614540-selectionwillchange)

|  | Declaration |
| --- | --- |
| From | ``` func selectionWillChange(_ textInput: UITextInput) ``` |
| To | ``` func selectionWillChange(_ textInput: UITextInput?) ``` |

Modified [UITextInputDelegate.textDidChange(_: UITextInput?)](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614499-textdidchange)

|  | Declaration |
| --- | --- |
| From | ``` func textDidChange(_ textInput: UITextInput) ``` |
| To | ``` func textDidChange(_ textInput: UITextInput?) ``` |

Modified [UITextInputDelegate.textWillChange(_: UITextInput?)](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614520-textwillchange)

|  | Declaration |
| --- | --- |
| From | ``` func textWillChange(_ textInput: UITextInput) ``` |
| To | ``` func textWillChange(_ textInput: UITextInput?) ``` |

Modified [UITextInputMode](https://developer.apple.com/documentation/uikit/uitextinputmode)

|  | Declaration |
| --- | --- |
| From | ``` class UITextInputMode : NSObject, NSSecureCoding, NSCoding {     var primaryLanguage: String? { get }     class func currentInputMode() -> UITextInputMode!     class func activeInputModes() -> [AnyObject] } ``` |
| To | ``` class UITextInputMode : NSObject, NSSecureCoding, NSCoding {     var primaryLanguage: String? { get }     class func currentInputMode() -> UITextInputMode?     class func activeInputModes() -> [String] } ``` |

Modified [UITextInputMode.activeInputModes() -> [String] [class]](https://developer.apple.com/documentation/uikit/uitextinputmode/1614522-activeinputmodes)

|  | Declaration |
| --- | --- |
| From | ``` class func activeInputModes() -> [AnyObject] ``` |
| To | ``` class func activeInputModes() -> [String] ``` |

Modified [UITextInputStringTokenizer](https://developer.apple.com/documentation/uikit/uitextinputstringtokenizer)

|  | Declaration |
| --- | --- |
| From | ``` class UITextInputStringTokenizer : NSObject, UITextInputTokenizer, NSObjectProtocol {     init!(textInput textInput: UIResponder) } ``` |
| To | ``` class UITextInputStringTokenizer : NSObject, UITextInputTokenizer {     init(textInput textInput: UIResponder) } ``` |

Modified [UITextInputStringTokenizer.init(textInput: UIResponder)](https://developer.apple.com/documentation/uikit/uitextinputstringtokenizer/1614469-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(textInput textInput: UIResponder) ``` |
| To | ``` init(textInput textInput: UIResponder) ``` |

Modified [UITextInputTokenizer.isPosition(_: UITextPosition, atBoundary: UITextGranularity, inDirection: UITextDirection) -> Bool](https://developer.apple.com/documentation/uikit/uitextinputtokenizer/1614553-isposition)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInputTokenizer.isPosition(_: UITextPosition, withinTextUnit: UITextGranularity, inDirection: UITextDirection) -> Bool](https://developer.apple.com/documentation/uikit/uitextinputtokenizer/1614491-isposition)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInputTokenizer.positionFromPosition(_: UITextPosition, toBoundary: UITextGranularity, inDirection: UITextDirection) -> UITextPosition?](https://developer.apple.com/documentation/uikit/uitextinputtokenizer/1614513-positionfromposition)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextInputTokenizer.rangeEnclosingPosition(_: UITextPosition, withGranularity: UITextGranularity, inDirection: UITextDirection) -> UITextRange?](https://developer.apple.com/documentation/uikit/uitextinputtokenizer/1614464-rangeenclosingposition)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UITextLayoutDirection [enum]](https://developer.apple.com/documentation/uikit/uitextlayoutdirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITextSpellCheckingType [enum]](https://developer.apple.com/documentation/uikit/uitextspellcheckingtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITextStorageDirection [enum]](https://developer.apple.com/documentation/uikit/uitextstoragedirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITextView](https://developer.apple.com/documentation/uikit/uitextview)

|  | Declaration |
| --- | --- |
| From | ``` class UITextView : UIScrollView, UITextInput, UIKeyInput, UITextInputTraits, NSObjectProtocol {     unowned(unsafe) var delegate: UITextViewDelegate?     var text: String!     var font: UIFont!     var textColor: UIColor!     var textAlignment: NSTextAlignment     var selectedRange: NSRange     var editable: Bool     var selectable: Bool     var dataDetectorTypes: UIDataDetectorTypes     var allowsEditingTextAttributes: Bool     @NSCopying var attributedText: NSAttributedString!     var typingAttributes: [NSObject : AnyObject]!     func scrollRangeToVisible(_ range: NSRange)     var inputView: UIView?     var inputAccessoryView: UIView?     var clearsOnInsertion: Bool     init(frame frame: CGRect, textContainer textContainer: NSTextContainer?)     var textContainer: NSTextContainer { get }     var textContainerInset: UIEdgeInsets     var layoutManager: NSLayoutManager { get }     var textStorage: NSTextStorage { get }     var linkTextAttributes: [NSObject : AnyObject]! } ``` |
| To | ``` class UITextView : UIScrollView, UITextInput, UIKeyInput, UITextInputTraits {     weak var delegate: UITextViewDelegate?     var text: String!     var font: UIFont?     var textColor: UIColor?     var textAlignment: NSTextAlignment     var selectedRange: NSRange     var editable: Bool     var selectable: Bool     var dataDetectorTypes: UIDataDetectorTypes     var allowsEditingTextAttributes: Bool     @NSCopying var attributedText: NSAttributedString!     var typingAttributes: [String : AnyObject]     func scrollRangeToVisible(_ range: NSRange)     var inputView: UIView?     var inputAccessoryView: UIView?     var clearsOnInsertion: Bool     init(frame frame: CGRect, textContainer textContainer: NSTextContainer?)     init?(coder aDecoder: NSCoder)     var textContainer: NSTextContainer { get }     var textContainerInset: UIEdgeInsets     var layoutManager: NSLayoutManager { get }     var textStorage: NSTextStorage { get }     var linkTextAttributes: [String : AnyObject]! } ``` |

Modified [UITextView.delegate](https://developer.apple.com/documentation/uikit/uitextview/1618631-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: UITextViewDelegate? ``` |
| To | ``` weak var delegate: UITextViewDelegate? ``` |

Modified [UITextView.font](https://developer.apple.com/documentation/uikit/uitextview/1618600-font)

|  | Declaration |
| --- | --- |
| From | ``` var font: UIFont! ``` |
| To | ``` var font: UIFont? ``` |

Modified [UITextView.linkTextAttributes](https://developer.apple.com/documentation/uikit/uitextview/1618632-linktextattributes)

|  | Declaration |
| --- | --- |
| From | ``` var linkTextAttributes: [NSObject : AnyObject]! ``` |
| To | ``` var linkTextAttributes: [String : AnyObject]! ``` |

Modified [UITextView.textColor](https://developer.apple.com/documentation/uikit/uitextview/1618601-textcolor)

|  | Declaration |
| --- | --- |
| From | ``` var textColor: UIColor! ``` |
| To | ``` var textColor: UIColor? ``` |

Modified [UITextView.typingAttributes](https://developer.apple.com/documentation/uikit/uitextview/1618629-typingattributes)

|  | Declaration |
| --- | --- |
| From | ``` var typingAttributes: [NSObject : AnyObject]! ``` |
| To | ``` var typingAttributes: [String : AnyObject] ``` |

Modified [UITextViewDelegate.textView(_: UITextView, shouldChangeTextInRange: NSRange, replacementText: String) -> Bool](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618630-textview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextViewDelegate.textViewDidBeginEditing(_: UITextView)](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618610-textviewdidbeginediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextViewDelegate.textViewDidChange(_: UITextView)](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618599-textviewdidchange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextViewDelegate.textViewDidChangeSelection(_: UITextView)](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618620-textviewdidchangeselection)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextViewDelegate.textViewDidEndEditing(_: UITextView)](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618628-textviewdidendediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextViewDelegate.textViewShouldBeginEditing(_: UITextView) -> Bool](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618608-textviewshouldbeginediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextViewDelegate.textViewShouldEndEditing(_: UITextView) -> Bool](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618603-textviewshouldendediting)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UITextWritingDirection [enum]](https://developer.apple.com/documentation/uikit/uitextwritingdirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIToolbar](https://developer.apple.com/documentation/uikit/uitoolbar)

|  | Declaration |
| --- | --- |
| From | ``` class UIToolbar : UIView, UIBarPositioning, NSObjectProtocol {     var barStyle: UIBarStyle     var items: [AnyObject]?     var translucent: Bool     func setItems(_ items: [AnyObject]?, animated animated: Bool)     var tintColor: UIColor!     var barTintColor: UIColor?     func setBackgroundImage(_ backgroundImage: UIImage?, forToolbarPosition topOrBottom: UIBarPosition, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForToolbarPosition(_ topOrBottom: UIBarPosition, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setShadowImage(_ shadowImage: UIImage?, forToolbarPosition topOrBottom: UIBarPosition)     func shadowImageForToolbarPosition(_ topOrBottom: UIBarPosition) -> UIImage?     unowned(unsafe) var delegate: UIToolbarDelegate? } ``` |
| To | ``` class UIToolbar : UIView, UIBarPositioning {     var barStyle: UIBarStyle     var items: [UIBarButtonItem]?     var translucent: Bool     func setItems(_ items: [UIBarButtonItem]?, animated animated: Bool)     var tintColor: UIColor!     var barTintColor: UIColor?     func setBackgroundImage(_ backgroundImage: UIImage?, forToolbarPosition topOrBottom: UIBarPosition, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForToolbarPosition(_ topOrBottom: UIBarPosition, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setShadowImage(_ shadowImage: UIImage?, forToolbarPosition topOrBottom: UIBarPosition)     func shadowImageForToolbarPosition(_ topOrBottom: UIBarPosition) -> UIImage?     unowned(unsafe) var delegate: UIToolbarDelegate? } ``` |

Modified [UIToolbar.items](https://developer.apple.com/documentation/uikit/uitoolbar/1617997-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject]? ``` |
| To | ``` var items: [UIBarButtonItem]? ``` |

Modified [UIToolbar.setItems(_: [UIBarButtonItem]?, animated: Bool)](https://developer.apple.com/documentation/uikit/uitoolbar/1617999-setitems)

|  | Declaration |
| --- | --- |
| From | ``` func setItems(_ items: [AnyObject]?, animated animated: Bool) ``` |
| To | ``` func setItems(_ items: [UIBarButtonItem]?, animated animated: Bool) ``` |

Modified [UITouch](https://developer.apple.com/documentation/uikit/uitouch)

|  | Declaration |
| --- | --- |
| From | ``` class UITouch : NSObject {     var timestamp: NSTimeInterval { get }     var phase: UITouchPhase { get }     var tapCount: Int { get }     var majorRadius: CGFloat { get }     var majorRadiusTolerance: CGFloat { get }     var window: UIWindow { get }     var view: UIView { get }     var gestureRecognizers: [AnyObject] { get }     func locationInView(_ view: UIView?) -> CGPoint     func previousLocationInView(_ view: UIView?) -> CGPoint } extension UITouch {     func locationInNode(_ node: SKNode!) -> CGPoint     func previousLocationInNode(_ node: SKNode!) -> CGPoint } ``` |
| To | ``` class UITouch : NSObject {     var timestamp: NSTimeInterval { get }     var phase: UITouchPhase { get }     var tapCount: Int { get }     var majorRadius: CGFloat { get }     var majorRadiusTolerance: CGFloat { get }     var window: UIWindow? { get }     var view: UIView? { get }     var gestureRecognizers: [UIGestureRecognizer]? { get }     func locationInView(_ view: UIView?) -> CGPoint     func previousLocationInView(_ view: UIView?) -> CGPoint     var force: CGFloat { get }     var maximumPossibleForce: CGFloat { get } } extension UITouch {     func locationInNode(_ node: SKNode) -> CGPoint     func previousLocationInNode(_ node: SKNode) -> CGPoint } ``` |

Modified [UITouch.gestureRecognizers](https://developer.apple.com/documentation/uikit/uitouch/1618114-gesturerecognizers)

|  | Declaration |
| --- | --- |
| From | ``` var gestureRecognizers: [AnyObject] { get } ``` |
| To | ``` var gestureRecognizers: [UIGestureRecognizer]? { get } ``` |

Modified [UITouch.view](https://developer.apple.com/documentation/uikit/uitouch/1618109-view)

|  | Declaration |
| --- | --- |
| From | ``` var view: UIView { get } ``` |
| To | ``` var view: UIView? { get } ``` |

Modified [UITouch.window](https://developer.apple.com/documentation/uikit/uitouch/1618126-window)

|  | Declaration |
| --- | --- |
| From | ``` var window: UIWindow { get } ``` |
| To | ``` var window: UIWindow? { get } ``` |

Modified [UITouchPhase [enum]](https://developer.apple.com/documentation/uikit/uitouch/phase)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UITraitCollection](https://developer.apple.com/documentation/uikit/uitraitcollection)

|  | Declaration |
| --- | --- |
| From | ``` class UITraitCollection : NSObject, NSCopying, NSSecureCoding, NSCoding {     func containsTraitsInCollection(_ trait: UITraitCollection!) -> Bool     init(traitsFromCollections traitCollections: [AnyObject]) -> UITraitCollection     class func traitCollectionWithTraitsFromCollections(_ traitCollections: [AnyObject]) -> UITraitCollection     init(userInterfaceIdiom idiom: UIUserInterfaceIdiom) -> UITraitCollection     class func traitCollectionWithUserInterfaceIdiom(_ idiom: UIUserInterfaceIdiom) -> UITraitCollection     var userInterfaceIdiom: UIUserInterfaceIdiom { get }     init(displayScale scale: CGFloat) -> UITraitCollection     class func traitCollectionWithDisplayScale(_ scale: CGFloat) -> UITraitCollection     var displayScale: CGFloat { get }     init(horizontalSizeClass horizontalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection     class func traitCollectionWithHorizontalSizeClass(_ horizontalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection     var horizontalSizeClass: UIUserInterfaceSizeClass { get }     init(verticalSizeClass verticalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection     class func traitCollectionWithVerticalSizeClass(_ verticalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection     var verticalSizeClass: UIUserInterfaceSizeClass { get } } ``` |
| To | ``` class UITraitCollection : NSObject, NSCopying, NSSecureCoding, NSCoding {     init()     init?(coder aDecoder: NSCoder)     func containsTraitsInCollection(_ trait: UITraitCollection?) -> Bool      init(traitsFromCollections traitCollections: [UITraitCollection])     class func traitCollectionWithTraitsFromCollections(_ traitCollections: [UITraitCollection]) -> UITraitCollection      init(userInterfaceIdiom idiom: UIUserInterfaceIdiom)     class func traitCollectionWithUserInterfaceIdiom(_ idiom: UIUserInterfaceIdiom) -> UITraitCollection     var userInterfaceIdiom: UIUserInterfaceIdiom { get }      init(displayScale scale: CGFloat)     class func traitCollectionWithDisplayScale(_ scale: CGFloat) -> UITraitCollection     var displayScale: CGFloat { get }      init(horizontalSizeClass horizontalSizeClass: UIUserInterfaceSizeClass)     class func traitCollectionWithHorizontalSizeClass(_ horizontalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection     var horizontalSizeClass: UIUserInterfaceSizeClass { get }      init(verticalSizeClass verticalSizeClass: UIUserInterfaceSizeClass)     class func traitCollectionWithVerticalSizeClass(_ verticalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection     var verticalSizeClass: UIUserInterfaceSizeClass { get }      init(forceTouchCapability capability: UIForceTouchCapability)     class func traitCollectionWithForceTouchCapability(_ capability: UIForceTouchCapability) -> UITraitCollection     var forceTouchCapability: UIForceTouchCapability { get } } ``` |

Modified [UITraitCollection.containsTraitsInCollection(_: UITraitCollection?) -> Bool](https://developer.apple.com/documentation/uikit/uitraitcollection/1623506-containstraitsincollection)

|  | Declaration |
| --- | --- |
| From | ``` func containsTraitsInCollection(_ trait: UITraitCollection!) -> Bool ``` |
| To | ``` func containsTraitsInCollection(_ trait: UITraitCollection?) -> Bool ``` |

Modified [UITraitCollection.init(displayScale: CGFloat)](https://developer.apple.com/documentation/uikit/uitraitcollection/1623518-traitcollectionwithdisplayscale)

|  | Declaration |
| --- | --- |
| From | ``` init(displayScale scale: CGFloat) -> UITraitCollection ``` |
| To | ``` init(displayScale scale: CGFloat) ``` |

Modified [UITraitCollection.init(horizontalSizeClass: UIUserInterfaceSizeClass)](https://developer.apple.com/documentation/uikit/uitraitcollection/1623520-init)

|  | Declaration |
| --- | --- |
| From | ``` init(horizontalSizeClass horizontalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection ``` |
| To | ``` init(horizontalSizeClass horizontalSizeClass: UIUserInterfaceSizeClass) ``` |

Modified [UITraitCollection.init(traitsFromCollections: [UITraitCollection])](https://developer.apple.com/documentation/uikit/uitraitcollection/1623512-init)

|  | Declaration |
| --- | --- |
| From | ``` init(traitsFromCollections traitCollections: [AnyObject]) -> UITraitCollection ``` |
| To | ``` init(traitsFromCollections traitCollections: [UITraitCollection]) ``` |

Modified [UITraitCollection.init(userInterfaceIdiom: UIUserInterfaceIdiom)](https://developer.apple.com/documentation/uikit/uitraitcollection/1623507-traitcollectionwithuserinterface)

|  | Declaration |
| --- | --- |
| From | ``` init(userInterfaceIdiom idiom: UIUserInterfaceIdiom) -> UITraitCollection ``` |
| To | ``` init(userInterfaceIdiom idiom: UIUserInterfaceIdiom) ``` |

Modified [UITraitCollection.init(verticalSizeClass: UIUserInterfaceSizeClass)](https://developer.apple.com/documentation/uikit/uitraitcollection/1623505-init)

|  | Declaration |
| --- | --- |
| From | ``` init(verticalSizeClass verticalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection ``` |
| To | ``` init(verticalSizeClass verticalSizeClass: UIUserInterfaceSizeClass) ``` |

Modified [UIUserInterfaceIdiom [enum]](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIUserInterfaceIdiom.Pad](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom/uiuserinterfaceidiompad)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIUserInterfaceIdiom.Phone](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom/phone)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified [UIUserInterfaceLayoutDirection [enum]](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIUserInterfaceSizeClass [enum]](https://developer.apple.com/documentation/uikit/uiuserinterfacesizeclass)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIUserNotificationAction](https://developer.apple.com/documentation/uikit/uiusernotificationaction)

|  | Declaration |
| --- | --- |
| From | ``` class UIUserNotificationAction : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var identifier: String! { get }     var title: String! { get }     var activationMode: UIUserNotificationActivationMode { get }     var authenticationRequired: Bool { get }     var destructive: Bool { get } } ``` |
| To | ``` class UIUserNotificationAction : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     init()     init?(coder aDecoder: NSCoder)     var identifier: String? { get }     var title: String? { get }     var behavior: UIUserNotificationActionBehavior { get }     var parameters: [NSObject : AnyObject] { get }     var activationMode: UIUserNotificationActivationMode { get }     var authenticationRequired: Bool { get }     var destructive: Bool { get } } ``` |

Modified [UIUserNotificationAction.identifier](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615361-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String? { get } ``` |

Modified [UIUserNotificationAction.title](https://developer.apple.com/documentation/uikit/uiusernotificationaction/1615358-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String? { get } ``` |

Modified [UIUserNotificationActionContext [enum]](https://developer.apple.com/documentation/uikit/uiusernotificationactioncontext)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [UIUserNotificationActivationMode [enum]](https://developer.apple.com/documentation/uikit/uiusernotificationactivationmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [UIUserNotificationCategory](https://developer.apple.com/documentation/uikit/uiusernotificationcategory)

|  | Declaration |
| --- | --- |
| From | ``` class UIUserNotificationCategory : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var identifier: String! { get }     func actionsForContext(_ context: UIUserNotificationActionContext) -> [AnyObject]! } ``` |
| To | ``` class UIUserNotificationCategory : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     init()     init?(coder aDecoder: NSCoder)     var identifier: String? { get }     func actionsForContext(_ context: UIUserNotificationActionContext) -> [UIUserNotificationAction]? } ``` |

Modified [UIUserNotificationCategory.actionsForContext(_: UIUserNotificationActionContext) -> [UIUserNotificationAction]?](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/1615374-actions)

|  | Declaration |
| --- | --- |
| From | ``` func actionsForContext(_ context: UIUserNotificationActionContext) -> [AnyObject]! ``` |
| To | ``` func actionsForContext(_ context: UIUserNotificationActionContext) -> [UIUserNotificationAction]? ``` |

Modified [UIUserNotificationCategory.identifier](https://developer.apple.com/documentation/uikit/uiusernotificationcategory/1615383-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String? { get } ``` |

Modified [UIUserNotificationSettings](https://developer.apple.com/documentation/uikit/uiusernotificationsettings)

|  | Declaration |
| --- | --- |
| From | ``` class UIUserNotificationSettings : NSObject {     convenience init(forTypes types: UIUserNotificationType, categories categories: Set<NSObject>?)     class func settingsForTypes(_ types: UIUserNotificationType, categories categories: Set<NSObject>?) -> Self     var types: UIUserNotificationType { get }     var categories: Set<NSObject>! { get } } ``` |
| To | ``` class UIUserNotificationSettings : NSObject {     convenience init(forTypes types: UIUserNotificationType, categories categories: Set<UIUserNotificationCategory>?)     class func settingsForTypes(_ types: UIUserNotificationType, categories categories: Set<UIUserNotificationCategory>?) -> Self     var types: UIUserNotificationType { get }     var categories: Set<UIUserNotificationCategory>? { get } } ``` |

Modified [UIUserNotificationSettings.categories](https://developer.apple.com/documentation/uikit/uiusernotificationsettings/1615365-categories)

|  | Declaration |
| --- | --- |
| From | ``` var categories: Set<NSObject>! { get } ``` |
| To | ``` var categories: Set<UIUserNotificationCategory>? { get } ``` |

Modified [UIUserNotificationSettings.init(forTypes: UIUserNotificationType, categories: Set<UIUserNotificationCategory>?)](https://developer.apple.com/documentation/uikit/uiusernotificationsettings/1615401-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(forTypes types: UIUserNotificationType, categories categories: Set<NSObject>?) ``` |
| To | ``` convenience init(forTypes types: UIUserNotificationType, categories categories: Set<UIUserNotificationCategory>?) ``` |

Modified [UIUserNotificationType [struct]](https://developer.apple.com/documentation/uikit/uiusernotificationtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIUserNotificationType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: UIUserNotificationType { get }     static var Badge: UIUserNotificationType { get }     static var Sound: UIUserNotificationType { get }     static var Alert: UIUserNotificationType { get } } ``` | RawOptionSetType |
| To | ``` struct UIUserNotificationType : OptionSetType {     init(rawValue rawValue: UInt)     static var None: UIUserNotificationType { get }     static var Badge: UIUserNotificationType { get }     static var Sound: UIUserNotificationType { get }     static var Alert: UIUserNotificationType { get } } ``` | OptionSetType |

Modified [UIVibrancyEffect](https://developer.apple.com/documentation/uikit/uivibrancyeffect)

|  | Declaration |
| --- | --- |
| From | ``` class UIVibrancyEffect : UIVisualEffect {     init(forBlurEffect blurEffect: UIBlurEffect) -> UIVibrancyEffect     class func effectForBlurEffect(_ blurEffect: UIBlurEffect) -> UIVibrancyEffect } extension UIVibrancyEffect {     class func notificationCenterVibrancyEffect() -> UIVibrancyEffect! } ``` |
| To | ``` class UIVibrancyEffect : UIVisualEffect {      init(forBlurEffect blurEffect: UIBlurEffect)     class func effectForBlurEffect(_ blurEffect: UIBlurEffect) -> UIVibrancyEffect } extension UIVibrancyEffect {     class func notificationCenterVibrancyEffect() -> UIVibrancyEffect } ``` |

Modified [UIVibrancyEffect.init(forBlurEffect: UIBlurEffect)](https://developer.apple.com/documentation/uikit/uivibrancyeffect/1615064-init)

|  | Declaration |
| --- | --- |
| From | ``` init(forBlurEffect blurEffect: UIBlurEffect) -> UIVibrancyEffect ``` |
| To | ``` init(forBlurEffect blurEffect: UIBlurEffect) ``` |

Modified [UIVideoEditorControllerDelegate.videoEditorController(_: UIVideoEditorController, didFailWithError: NSError)](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622342-videoeditorcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified [UIVideoEditorControllerDelegate.videoEditorController(_: UIVideoEditorController, didSaveEditedVideoToPath: String)](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622336-videoeditorcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified [UIVideoEditorControllerDelegate.videoEditorControllerDidCancel(_: UIVideoEditorController)](https://developer.apple.com/documentation/uikit/uivideoeditorcontrollerdelegate/1622335-videoeditorcontrollerdidcancel)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.1 |

Modified [UIView](https://developer.apple.com/documentation/uikit/uiview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIView : UIResponder, NSCoding, UIAppearance, NSObjectProtocol, UIAppearanceContainer, UIDynamicItem, UITraitEnvironment, UICoordinateSpace {     class func layerClass() -> AnyClass     init(frame frame: CGRect)     var userInteractionEnabled: Bool     var tag: Int     var layer: CALayer { get } } extension UIView : UIAccessibilityIdentification, NSObjectProtocol { } extension UIView {     func viewPrintFormatter() -> UIViewPrintFormatter     func drawRect(_ rect: CGRect, forViewPrintFormatter formatter: UIViewPrintFormatter) } extension UIView {     func endEditing(_ force: Bool) -> Bool } extension UIView : Reflectable {     func getMirror() -> MirrorType } extension UIView {     var frame: CGRect     var bounds: CGRect     var center: CGPoint     var transform: CGAffineTransform     var contentScaleFactor: CGFloat     var multipleTouchEnabled: Bool     var exclusiveTouch: Bool     func hitTest(_ point: CGPoint, withEvent event: UIEvent?) -> UIView?     func pointInside(_ point: CGPoint, withEvent event: UIEvent?) -> Bool     func convertPoint(_ point: CGPoint, toView view: UIView?) -> CGPoint     func convertPoint(_ point: CGPoint, fromView view: UIView?) -> CGPoint     func convertRect(_ rect: CGRect, toView view: UIView?) -> CGRect     func convertRect(_ rect: CGRect, fromView view: UIView?) -> CGRect     var autoresizesSubviews: Bool     var autoresizingMask: UIViewAutoresizing     func sizeThatFits(_ size: CGSize) -> CGSize     func sizeToFit() } extension UIView {     var superview: UIView? { get }     var subviews: [AnyObject] { get }     var window: UIWindow? { get }     func removeFromSuperview()     func insertSubview(_ view: UIView, atIndex index: Int)     func exchangeSubviewAtIndex(_ index1: Int, withSubviewAtIndex index2: Int)     func addSubview(_ view: UIView)     func insertSubview(_ view: UIView, belowSubview siblingSubview: UIView)     func insertSubview(_ view: UIView, aboveSubview siblingSubview: UIView)     func bringSubviewToFront(_ view: UIView)     func sendSubviewToBack(_ view: UIView)     func didAddSubview(_ subview: UIView)     func willRemoveSubview(_ subview: UIView)     func willMoveToSuperview(_ newSuperview: UIView?)     func didMoveToSuperview()     func willMoveToWindow(_ newWindow: UIWindow?)     func didMoveToWindow()     func isDescendantOfView(_ view: UIView) -> Bool     func viewWithTag(_ tag: Int) -> UIView?     func setNeedsLayout()     func layoutIfNeeded()     func layoutSubviews()     var layoutMargins: UIEdgeInsets     var preservesSuperviewLayoutMargins: Bool     func layoutMarginsDidChange() } extension UIView {     func drawRect(_ rect: CGRect)     func setNeedsDisplay()     func setNeedsDisplayInRect(_ rect: CGRect)     var clipsToBounds: Bool     @NSCopying var backgroundColor: UIColor?     var alpha: CGFloat     var opaque: Bool     var clearsContextBeforeDrawing: Bool     var hidden: Bool     var contentMode: UIViewContentMode     var contentStretch: CGRect     var maskView: UIView?     var tintColor: UIColor!     var tintAdjustmentMode: UIViewTintAdjustmentMode     func tintColorDidChange() } extension UIView {     class func beginAnimations(_ animationID: String?, context context: UnsafeMutablePointer<Void>)     class func commitAnimations()     class func setAnimationDelegate(_ delegate: AnyObject?)     class func setAnimationWillStartSelector(_ selector: Selector)     class func setAnimationDidStopSelector(_ selector: Selector)     class func setAnimationDuration(_ duration: NSTimeInterval)     class func setAnimationDelay(_ delay: NSTimeInterval)     class func setAnimationStartDate(_ startDate: NSDate)     class func setAnimationCurve(_ curve: UIViewAnimationCurve)     class func setAnimationRepeatCount(_ repeatCount: Float)     class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)     class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)     class func setAnimationTransition(_ transition: UIViewAnimationTransition, forView view: UIView, cache cache: Bool)     class func setAnimationsEnabled(_ enabled: Bool)     class func areAnimationsEnabled() -> Bool     class func performWithoutAnimation(_ actionsWithoutAnimation: () -> Void) } extension UIView {     class func animateWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void)     class func animateWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func transitionWithView(_ view: UIView, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func transitionFromView(_ fromView: UIView, toView toView: UIView, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, completion completion: ((Bool) -> Void)?)     class func performSystemAnimation(_ animation: UISystemAnimation, onViews views: [AnyObject], options options: UIViewAnimationOptions, animations parallelAnimations: (() -> Void)?, completion completion: ((Bool) -> Void)?) } extension UIView {     class func animateKeyframesWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, options options: UIViewKeyframeAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func addKeyframeWithRelativeStartTime(_ frameStartTime: Double, relativeDuration frameDuration: Double, animations animations: () -> Void) } extension UIView {     var gestureRecognizers: [AnyObject]?     func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool } extension UIView {     func addMotionEffect(_ effect: UIMotionEffect)     func removeMotionEffect(_ effect: UIMotionEffect)     var motionEffects: [AnyObject]? } extension UIView {     func constraints() -> [AnyObject]     func addConstraint(_ constraint: NSLayoutConstraint)     func addConstraints(_ constraints: [AnyObject])     func removeConstraint(_ constraint: NSLayoutConstraint)     func removeConstraints(_ constraints: [AnyObject]) } extension UIView {     func updateConstraintsIfNeeded()     func updateConstraints()     func needsUpdateConstraints() -> Bool     func setNeedsUpdateConstraints() } extension UIView {     func translatesAutoresizingMaskIntoConstraints() -> Bool     func setTranslatesAutoresizingMaskIntoConstraints(_ flag: Bool)     class func requiresConstraintBasedLayout() -> Bool } extension UIView {     func alignmentRectForFrame(_ frame: CGRect) -> CGRect     func frameForAlignmentRect(_ alignmentRect: CGRect) -> CGRect     func alignmentRectInsets() -> UIEdgeInsets     func viewForBaselineLayout() -> UIView?     func intrinsicContentSize() -> CGSize     func invalidateIntrinsicContentSize()     func contentHuggingPriorityForAxis(_ axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentHuggingPriority(_ priority: UILayoutPriority, forAxis axis: UILayoutConstraintAxis)     func contentCompressionResistancePriorityForAxis(_ axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentCompressionResistancePriority(_ priority: UILayoutPriority, forAxis axis: UILayoutConstraintAxis) } extension UIView {     func systemLayoutSizeFittingSize(_ targetSize: CGSize) -> CGSize     func systemLayoutSizeFittingSize(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority verticalFittingPriority: UILayoutPriority) -> CGSize } extension UIView {     func constraintsAffectingLayoutForAxis(_ axis: UILayoutConstraintAxis) -> [AnyObject]     func hasAmbiguousLayout() -> Bool     func exerciseAmbiguityInLayout() } extension UIView {     var restorationIdentifier: String?     func encodeRestorableStateWithCoder(_ coder: NSCoder)     func decodeRestorableStateWithCoder(_ coder: NSCoder) } extension UIView {     func snapshotViewAfterScreenUpdates(_ afterUpdates: Bool) -> UIView     func resizableSnapshotViewFromRect(_ rect: CGRect, afterScreenUpdates afterUpdates: Bool, withCapInsets capInsets: UIEdgeInsets) -> UIView     func drawViewHierarchyInRect(_ rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool } extension UIView : Reflectable {     func getMirror() -> MirrorType } ``` | AnyObject, NSCoding, NSObjectProtocol, Reflectable, UIAccessibilityIdentification, UIAppearance, UIAppearanceContainer, UICoordinateSpace, UIDynamicItem, UITraitEnvironment |
| To | ``` class UIView : UIResponder, NSCoding, UIAppearance, UIAppearanceContainer, UIDynamicItem, UITraitEnvironment, UICoordinateSpace {     class func layerClass() -> AnyClass     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     var userInteractionEnabled: Bool     var tag: Int     var layer: CALayer { get }     class func userInterfaceLayoutDirectionForSemanticContentAttribute(_ attribute: UISemanticContentAttribute) -> UIUserInterfaceLayoutDirection     var semanticContentAttribute: UISemanticContentAttribute } extension UIView : UIAccessibilityIdentification { } extension UIView {     func viewPrintFormatter() -> UIViewPrintFormatter     func drawRect(_ rect: CGRect, forViewPrintFormatter formatter: UIViewPrintFormatter) } extension UIView {     func endEditing(_ force: Bool) -> Bool } extension UIView : _Reflectable { } extension UIView {     var frame: CGRect     var bounds: CGRect     var center: CGPoint     var transform: CGAffineTransform     var contentScaleFactor: CGFloat     var multipleTouchEnabled: Bool     var exclusiveTouch: Bool     func hitTest(_ point: CGPoint, withEvent event: UIEvent?) -> UIView?     func pointInside(_ point: CGPoint, withEvent event: UIEvent?) -> Bool     func convertPoint(_ point: CGPoint, toView view: UIView?) -> CGPoint     func convertPoint(_ point: CGPoint, fromView view: UIView?) -> CGPoint     func convertRect(_ rect: CGRect, toView view: UIView?) -> CGRect     func convertRect(_ rect: CGRect, fromView view: UIView?) -> CGRect     var autoresizesSubviews: Bool     var autoresizingMask: UIViewAutoresizing     func sizeThatFits(_ size: CGSize) -> CGSize     func sizeToFit() } extension UIView {     var superview: UIView? { get }     var subviews: [UIView] { get }     var window: UIWindow? { get }     func removeFromSuperview()     func insertSubview(_ view: UIView, atIndex index: Int)     func exchangeSubviewAtIndex(_ index1: Int, withSubviewAtIndex index2: Int)     func addSubview(_ view: UIView)     func insertSubview(_ view: UIView, belowSubview siblingSubview: UIView)     func insertSubview(_ view: UIView, aboveSubview siblingSubview: UIView)     func bringSubviewToFront(_ view: UIView)     func sendSubviewToBack(_ view: UIView)     func didAddSubview(_ subview: UIView)     func willRemoveSubview(_ subview: UIView)     func willMoveToSuperview(_ newSuperview: UIView?)     func didMoveToSuperview()     func willMoveToWindow(_ newWindow: UIWindow?)     func didMoveToWindow()     func isDescendantOfView(_ view: UIView) -> Bool     func viewWithTag(_ tag: Int) -> UIView?     func setNeedsLayout()     func layoutIfNeeded()     func layoutSubviews()     var layoutMargins: UIEdgeInsets     var preservesSuperviewLayoutMargins: Bool     func layoutMarginsDidChange()     var layoutMarginsGuide: UILayoutGuide { get }     var readableContentGuide: UILayoutGuide { get } } extension UIView {     func drawRect(_ rect: CGRect)     func setNeedsDisplay()     func setNeedsDisplayInRect(_ rect: CGRect)     var clipsToBounds: Bool     @NSCopying var backgroundColor: UIColor?     var alpha: CGFloat     var opaque: Bool     var clearsContextBeforeDrawing: Bool     var hidden: Bool     var contentMode: UIViewContentMode     var contentStretch: CGRect     var maskView: UIView?     var tintColor: UIColor!     var tintAdjustmentMode: UIViewTintAdjustmentMode     func tintColorDidChange() } extension UIView {     class func beginAnimations(_ animationID: String?, context context: UnsafeMutablePointer<Void>)     class func commitAnimations()     class func setAnimationDelegate(_ delegate: AnyObject?)     class func setAnimationWillStartSelector(_ selector: Selector)     class func setAnimationDidStopSelector(_ selector: Selector)     class func setAnimationDuration(_ duration: NSTimeInterval)     class func setAnimationDelay(_ delay: NSTimeInterval)     class func setAnimationStartDate(_ startDate: NSDate)     class func setAnimationCurve(_ curve: UIViewAnimationCurve)     class func setAnimationRepeatCount(_ repeatCount: Float)     class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)     class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)     class func setAnimationTransition(_ transition: UIViewAnimationTransition, forView view: UIView, cache cache: Bool)     class func setAnimationsEnabled(_ enabled: Bool)     class func areAnimationsEnabled() -> Bool     class func performWithoutAnimation(_ actionsWithoutAnimation: () -> Void)     class func inheritedAnimationDuration() -> NSTimeInterval } extension UIView {     class func animateWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void)     class func animateWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func transitionWithView(_ view: UIView, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: (() -> Void)?, completion completion: ((Bool) -> Void)?)     class func transitionFromView(_ fromView: UIView, toView toView: UIView, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, completion completion: ((Bool) -> Void)?)     class func performSystemAnimation(_ animation: UISystemAnimation, onViews views: [UIView], options options: UIViewAnimationOptions, animations parallelAnimations: (() -> Void)?, completion completion: ((Bool) -> Void)?) } extension UIView {     class func animateKeyframesWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, options options: UIViewKeyframeAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func addKeyframeWithRelativeStartTime(_ frameStartTime: Double, relativeDuration frameDuration: Double, animations animations: () -> Void) } extension UIView {     var gestureRecognizers: [UIGestureRecognizer]?     func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool } extension UIView {     func addMotionEffect(_ effect: UIMotionEffect)     func removeMotionEffect(_ effect: UIMotionEffect)     var motionEffects: [UIMotionEffect] } extension UIView {     var constraints: [NSLayoutConstraint] { get }     func addConstraint(_ constraint: NSLayoutConstraint)     func addConstraints(_ constraints: [NSLayoutConstraint])     func removeConstraint(_ constraint: NSLayoutConstraint)     func removeConstraints(_ constraints: [NSLayoutConstraint]) } extension UIView {     func updateConstraintsIfNeeded()     func updateConstraints()     func needsUpdateConstraints() -> Bool     func setNeedsUpdateConstraints() } extension UIView {     var translatesAutoresizingMaskIntoConstraints: Bool     class func requiresConstraintBasedLayout() -> Bool } extension UIView {     func alignmentRectForFrame(_ frame: CGRect) -> CGRect     func frameForAlignmentRect(_ alignmentRect: CGRect) -> CGRect     func alignmentRectInsets() -> UIEdgeInsets     func viewForBaselineLayout() -> UIView     var viewForFirstBaselineLayout: UIView { get }     var viewForLastBaselineLayout: UIView { get }     func intrinsicContentSize() -> CGSize     func invalidateIntrinsicContentSize()     func contentHuggingPriorityForAxis(_ axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentHuggingPriority(_ priority: UILayoutPriority, forAxis axis: UILayoutConstraintAxis)     func contentCompressionResistancePriorityForAxis(_ axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentCompressionResistancePriority(_ priority: UILayoutPriority, forAxis axis: UILayoutConstraintAxis) } extension UIView {     func systemLayoutSizeFittingSize(_ targetSize: CGSize) -> CGSize     func systemLayoutSizeFittingSize(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority verticalFittingPriority: UILayoutPriority) -> CGSize } extension UIView {     var layoutGuides: [UILayoutGuide] { get }     func addLayoutGuide(_ layoutGuide: UILayoutGuide)     func removeLayoutGuide(_ layoutGuide: UILayoutGuide) } extension UIView {     var leadingAnchor: NSLayoutXAxisAnchor { get }     var trailingAnchor: NSLayoutXAxisAnchor { get }     var leftAnchor: NSLayoutXAxisAnchor { get }     var rightAnchor: NSLayoutXAxisAnchor { get }     var topAnchor: NSLayoutYAxisAnchor { get }     var bottomAnchor: NSLayoutYAxisAnchor { get }     var widthAnchor: NSLayoutDimension { get }     var heightAnchor: NSLayoutDimension { get }     var centerXAnchor: NSLayoutXAxisAnchor { get }     var centerYAnchor: NSLayoutYAxisAnchor { get }     var firstBaselineAnchor: NSLayoutYAxisAnchor { get }     var lastBaselineAnchor: NSLayoutYAxisAnchor { get } } extension UIView {     func constraintsAffectingLayoutForAxis(_ axis: UILayoutConstraintAxis) -> [NSLayoutConstraint]     func hasAmbiguousLayout() -> Bool     func exerciseAmbiguityInLayout() } extension UIView {     var restorationIdentifier: String?     func encodeRestorableStateWithCoder(_ coder: NSCoder)     func decodeRestorableStateWithCoder(_ coder: NSCoder) } extension UIView {     func snapshotViewAfterScreenUpdates(_ afterUpdates: Bool) -> UIView     func resizableSnapshotViewFromRect(_ rect: CGRect, afterScreenUpdates afterUpdates: Bool, withCapInsets capInsets: UIEdgeInsets) -> UIView     func drawViewHierarchyInRect(_ rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool } extension UIView : _Reflectable { } ``` | AnyObject, NSCoding, NSObjectProtocol, UIAccessibilityIdentification, UIAppearance, UIAppearanceContainer, UICoordinateSpace, UIDynamicItem, UITraitEnvironment |

Modified [UIView.addConstraints(_: [NSLayoutConstraint])](https://developer.apple.com/documentation/uikit/uiview/1622513-addconstraints)

|  | Declaration |
| --- | --- |
| From | ``` func addConstraints(_ constraints: [AnyObject]) ``` |
| To | ``` func addConstraints(_ constraints: [NSLayoutConstraint]) ``` |

Modified [UIView.constraintsAffectingLayoutForAxis(_: UILayoutConstraintAxis) -> [NSLayoutConstraint]](https://developer.apple.com/documentation/uikit/uiview/1622432-constraintsaffectinglayoutforaxi)

|  | Declaration |
| --- | --- |
| From | ``` func constraintsAffectingLayoutForAxis(_ axis: UILayoutConstraintAxis) -> [AnyObject] ``` |
| To | ``` func constraintsAffectingLayoutForAxis(_ axis: UILayoutConstraintAxis) -> [NSLayoutConstraint] ``` |

Modified [UIView.gestureRecognizers](https://developer.apple.com/documentation/uikit/uiview/1622542-gesturerecognizers)

|  | Declaration |
| --- | --- |
| From | ``` var gestureRecognizers: [AnyObject]? ``` |
| To | ``` var gestureRecognizers: [UIGestureRecognizer]? ``` |

Modified [UIView.motionEffects](https://developer.apple.com/documentation/uikit/uiview/1622428-motioneffects)

|  | Declaration |
| --- | --- |
| From | ``` var motionEffects: [AnyObject]? ``` |
| To | ``` var motionEffects: [UIMotionEffect] ``` |

Modified [UIView.performSystemAnimation(_: UISystemAnimation, onViews: [UIView], options: UIViewAnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?) [class]](https://developer.apple.com/documentation/uikit/uiview/1622635-performsystemanimation)

|  | Declaration |
| --- | --- |
| From | ``` class func performSystemAnimation(_ animation: UISystemAnimation, onViews views: [AnyObject], options options: UIViewAnimationOptions, animations parallelAnimations: (() -> Void)?, completion completion: ((Bool) -> Void)?) ``` |
| To | ``` class func performSystemAnimation(_ animation: UISystemAnimation, onViews views: [UIView], options options: UIViewAnimationOptions, animations parallelAnimations: (() -> Void)?, completion completion: ((Bool) -> Void)?) ``` |

Modified [UIView.removeConstraints(_: [NSLayoutConstraint])](https://developer.apple.com/documentation/uikit/uiview/1622593-removeconstraints)

|  | Declaration |
| --- | --- |
| From | ``` func removeConstraints(_ constraints: [AnyObject]) ``` |
| To | ``` func removeConstraints(_ constraints: [NSLayoutConstraint]) ``` |

Modified [UIView.subviews](https://developer.apple.com/documentation/uikit/uiview/1622614-subviews)

|  | Declaration |
| --- | --- |
| From | ``` var subviews: [AnyObject] { get } ``` |
| To | ``` var subviews: [UIView] { get } ``` |

Modified [UIView.transitionWithView(_: UIView, duration: NSTimeInterval, options: UIViewAnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?) [class]](https://developer.apple.com/documentation/uikit/uiview/1622574-transitionwithview)

|  | Declaration |
| --- | --- |
| From | ``` class func transitionWithView(_ view: UIView, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?) ``` |
| To | ``` class func transitionWithView(_ view: UIView, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: (() -> Void)?, completion completion: ((Bool) -> Void)?) ``` |

Modified [UIView.viewForBaselineLayout() -> UIView](https://developer.apple.com/documentation/uikit/uiview/1622439-viewforbaselinelayout)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func viewForBaselineLayout() -> UIView? ``` | -- |
| To | ``` func viewForBaselineLayout() -> UIView ``` | iOS 9.0 |

Modified [UIViewAnimationCurve [enum]](https://developer.apple.com/documentation/uikit/uiview/animationcurve)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIViewAnimationOptions [struct]](https://developer.apple.com/documentation/uikit/uiviewanimationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIViewAnimationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var LayoutSubviews: UIViewAnimationOptions { get }     static var AllowUserInteraction: UIViewAnimationOptions { get }     static var BeginFromCurrentState: UIViewAnimationOptions { get }     static var Repeat: UIViewAnimationOptions { get }     static var Autoreverse: UIViewAnimationOptions { get }     static var OverrideInheritedDuration: UIViewAnimationOptions { get }     static var OverrideInheritedCurve: UIViewAnimationOptions { get }     static var AllowAnimatedContent: UIViewAnimationOptions { get }     static var ShowHideTransitionViews: UIViewAnimationOptions { get }     static var OverrideInheritedOptions: UIViewAnimationOptions { get }     static var CurveEaseInOut: UIViewAnimationOptions { get }     static var CurveEaseIn: UIViewAnimationOptions { get }     static var CurveEaseOut: UIViewAnimationOptions { get }     static var CurveLinear: UIViewAnimationOptions { get }     static var TransitionNone: UIViewAnimationOptions { get }     static var TransitionFlipFromLeft: UIViewAnimationOptions { get }     static var TransitionFlipFromRight: UIViewAnimationOptions { get }     static var TransitionCurlUp: UIViewAnimationOptions { get }     static var TransitionCurlDown: UIViewAnimationOptions { get }     static var TransitionCrossDissolve: UIViewAnimationOptions { get }     static var TransitionFlipFromTop: UIViewAnimationOptions { get }     static var TransitionFlipFromBottom: UIViewAnimationOptions { get } } ``` | RawOptionSetType |
| To | ``` struct UIViewAnimationOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var LayoutSubviews: UIViewAnimationOptions { get }     static var AllowUserInteraction: UIViewAnimationOptions { get }     static var BeginFromCurrentState: UIViewAnimationOptions { get }     static var Repeat: UIViewAnimationOptions { get }     static var Autoreverse: UIViewAnimationOptions { get }     static var OverrideInheritedDuration: UIViewAnimationOptions { get }     static var OverrideInheritedCurve: UIViewAnimationOptions { get }     static var AllowAnimatedContent: UIViewAnimationOptions { get }     static var ShowHideTransitionViews: UIViewAnimationOptions { get }     static var OverrideInheritedOptions: UIViewAnimationOptions { get }     static var CurveEaseInOut: UIViewAnimationOptions { get }     static var CurveEaseIn: UIViewAnimationOptions { get }     static var CurveEaseOut: UIViewAnimationOptions { get }     static var CurveLinear: UIViewAnimationOptions { get }     static var TransitionNone: UIViewAnimationOptions { get }     static var TransitionFlipFromLeft: UIViewAnimationOptions { get }     static var TransitionFlipFromRight: UIViewAnimationOptions { get }     static var TransitionCurlUp: UIViewAnimationOptions { get }     static var TransitionCurlDown: UIViewAnimationOptions { get }     static var TransitionCrossDissolve: UIViewAnimationOptions { get }     static var TransitionFlipFromTop: UIViewAnimationOptions { get }     static var TransitionFlipFromBottom: UIViewAnimationOptions { get } } ``` | OptionSetType |

Modified [UIViewAnimationTransition [enum]](https://developer.apple.com/documentation/uikit/uiviewanimationtransition)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIViewAutoresizing [struct]](https://developer.apple.com/documentation/uikit/uiviewautoresizing)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIViewAutoresizing : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: UIViewAutoresizing { get }     static var FlexibleLeftMargin: UIViewAutoresizing { get }     static var FlexibleWidth: UIViewAutoresizing { get }     static var FlexibleRightMargin: UIViewAutoresizing { get }     static var FlexibleTopMargin: UIViewAutoresizing { get }     static var FlexibleHeight: UIViewAutoresizing { get }     static var FlexibleBottomMargin: UIViewAutoresizing { get } } ``` | RawOptionSetType |
| To | ``` struct UIViewAutoresizing : OptionSetType {     init(rawValue rawValue: UInt)     static var None: UIViewAutoresizing { get }     static var FlexibleLeftMargin: UIViewAutoresizing { get }     static var FlexibleWidth: UIViewAutoresizing { get }     static var FlexibleRightMargin: UIViewAutoresizing { get }     static var FlexibleTopMargin: UIViewAutoresizing { get }     static var FlexibleHeight: UIViewAutoresizing { get }     static var FlexibleBottomMargin: UIViewAutoresizing { get } } ``` | OptionSetType |

Modified [UIViewContentMode [enum]](https://developer.apple.com/documentation/uikit/uiview/contentmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class UIViewController : UIResponder, NSCoding, UIAppearanceContainer, NSObjectProtocol, UITraitEnvironment, UIContentContainer {     init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     var view: UIView!     func loadView()     func viewWillUnload()     func viewDidUnload()     func viewDidLoad()     func isViewLoaded() -> Bool     var nibName: String? { get }     var nibBundle: NSBundle? { get }     var storyboard: UIStoryboard? { get }     func performSegueWithIdentifier(_ identifier: String?, sender sender: AnyObject?)     func shouldPerformSegueWithIdentifier(_ identifier: String?, sender sender: AnyObject?) -> Bool     func prepareForSegue(_ segue: UIStoryboardSegue, sender sender: AnyObject?)     func canPerformUnwindSegueAction(_ action: Selector, fromViewController fromViewController: UIViewController, withSender sender: AnyObject) -> Bool     func viewControllerForUnwindSegueAction(_ action: Selector, fromViewController fromViewController: UIViewController, withSender sender: AnyObject?) -> UIViewController?     func segueForUnwindingToViewController(_ toViewController: UIViewController, fromViewController fromViewController: UIViewController, identifier identifier: String?) -> UIStoryboardSegue     func viewWillAppear(_ animated: Bool)     func viewDidAppear(_ animated: Bool)     func viewWillDisappear(_ animated: Bool)     func viewDidDisappear(_ animated: Bool)     func viewWillLayoutSubviews()     func viewDidLayoutSubviews()     var title: String?     func didReceiveMemoryWarning()     var parentViewController: UIViewController? { get }     var modalViewController: UIViewController! { get }     var presentedViewController: UIViewController? { get }     var presentingViewController: UIViewController? { get }     var definesPresentationContext: Bool     var providesPresentationContextTransitionStyle: Bool     func isBeingPresented() -> Bool     func isBeingDismissed() -> Bool     func isMovingToParentViewController() -> Bool     func isMovingFromParentViewController() -> Bool     func presentViewController(_ viewControllerToPresent: UIViewController, animated flag: Bool, completion completion: (() -> Void)?)     func dismissViewControllerAnimated(_ flag: Bool, completion completion: (() -> Void)?)     func presentModalViewController(_ modalViewController: UIViewController!, animated animated: Bool)     func dismissModalViewControllerAnimated(_ animated: Bool)     var modalTransitionStyle: UIModalTransitionStyle     var modalPresentationStyle: UIModalPresentationStyle     var modalPresentationCapturesStatusBarAppearance: Bool     func disablesAutomaticKeyboardDismissal() -> Bool     var wantsFullScreenLayout: Bool     var edgesForExtendedLayout: UIRectEdge     var extendedLayoutIncludesOpaqueBars: Bool     var automaticallyAdjustsScrollViewInsets: Bool     var preferredContentSize: CGSize     func preferredStatusBarStyle() -> UIStatusBarStyle     func prefersStatusBarHidden() -> Bool     func preferredStatusBarUpdateAnimation() -> UIStatusBarAnimation     func setNeedsStatusBarAppearanceUpdate()     func targetViewControllerForAction(_ action: Selector, sender sender: AnyObject?) -> UIViewController?     func showViewController(_ vc: UIViewController, sender sender: AnyObject?)     func showDetailViewController(_ vc: UIViewController, sender sender: AnyObject?) } extension UIViewController {     func presentMoviePlayerViewControllerAnimated(_ moviePlayerViewController: MPMoviePlayerViewController!)     func dismissMoviePlayerViewControllerAnimated() } extension UIViewController {     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get } } extension UIViewController {     var toolbarItems: [AnyObject]?     func setToolbarItems(_ toolbarItems: [AnyObject]?, animated animated: Bool) } extension UIViewController {     var modalInPopover: Bool     var contentSizeForViewInPopover: CGSize } extension UIViewController {     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, forSplitViewController splitViewController: UISplitViewController)     func separateSecondaryViewControllerForSplitViewController(_ splitViewController: UISplitViewController) -> UIViewController } extension UIViewController {     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get } } extension UIViewController {     class func attemptRotationToDeviceOrientation()     func shouldAutorotateToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation) -> Bool     func shouldAutorotate() -> Bool     func supportedInterfaceOrientations() -> Int     func preferredInterfaceOrientationForPresentation() -> UIInterfaceOrientation     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotateToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func didRotateFromInterfaceOrientation(_ fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func willAnimateFirstHalfOfRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func didAnimateFirstHalfOfRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotationFromInterfaceOrientation(_ fromInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval) } extension UIViewController {     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     func editButtonItem() -> UIBarButtonItem } extension UIViewController {     var searchDisplayController: UISearchDisplayController? { get } } extension UIViewController {     var childViewControllers: [AnyObject] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transitionFromViewController(_ fromViewController: UIViewController, toViewController toViewController: UIViewController, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: (() -> Void)?, completion completion: ((Bool) -> Void)?)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     func childViewControllerForStatusBarStyle() -> UIViewController?     func childViewControllerForStatusBarHidden() -> UIViewController?     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollectionForChildViewController(_ childViewController: UIViewController) -> UITraitCollection! } extension UIViewController {     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     func shouldAutomaticallyForwardAppearanceMethods() -> Bool     func willMoveToParentViewController(_ parent: UIViewController?)     func didMoveToParentViewController(_ parent: UIViewController?) } extension UIViewController : UIStateRestoring, NSObjectProtocol {     var restorationIdentifier: String?     var restorationClass: AnyObject.Type?     func encodeRestorableStateWithCoder(_ coder: NSCoder)     func decodeRestorableStateWithCoder(_ coder: NSCoder)     func applicationFinishedRestoringState() } extension UIViewController {     func updateViewConstraints() } extension UIViewController {     unowned(unsafe) var transitioningDelegate: UIViewControllerTransitioningDelegate? } extension UIViewController {     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get } } extension UIViewController : NSExtensionRequestHandling, NSObjectProtocol {     var extensionContext: NSExtensionContext? { get } } extension UIViewController {     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get } } extension UIViewController {     func transitionCoordinator() -> UIViewControllerTransitionCoordinator? } extension UIViewController {     class func prepareInterstitialAds()     var interstitialPresentationPolicy: ADInterstitialPresentationPolicy     var canDisplayBannerAds: Bool     var originalContentView: UIView! { get }     var presentingFullScreenAd: Bool { get }     var displayingBannerAd: Bool { get }     func requestInterstitialAdPresentation() -> Bool     var shouldPresentInterstitialAd: Bool { get } } ``` |
| To | ``` class UIViewController : UIResponder, NSCoding, UIAppearanceContainer, UITraitEnvironment, UIContentContainer {     init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     init?(coder aDecoder: NSCoder)     var view: UIView!     func loadView()     func loadViewIfNeeded()     var viewIfLoaded: UIView? { get }     func viewWillUnload()     func viewDidUnload()     func viewDidLoad()     func isViewLoaded() -> Bool     var nibName: String? { get }     var nibBundle: NSBundle? { get }     var storyboard: UIStoryboard? { get }     func performSegueWithIdentifier(_ identifier: String, sender sender: AnyObject?)     func shouldPerformSegueWithIdentifier(_ identifier: String, sender sender: AnyObject?) -> Bool     func prepareForSegue(_ segue: UIStoryboardSegue, sender sender: AnyObject?)     func canPerformUnwindSegueAction(_ action: Selector, fromViewController fromViewController: UIViewController, withSender sender: AnyObject) -> Bool     func allowedChildViewControllersForUnwindingFromSource(_ source: UIStoryboardUnwindSegueSource) -> [UIViewController]     func childViewControllerContainingSegueSource(_ source: UIStoryboardUnwindSegueSource) -> UIViewController?     func viewControllerForUnwindSegueAction(_ action: Selector, fromViewController fromViewController: UIViewController, withSender sender: AnyObject?) -> UIViewController?     func unwindForSegue(_ unwindSegue: UIStoryboardSegue, towardsViewController subsequentVC: UIViewController)     func segueForUnwindingToViewController(_ toViewController: UIViewController, fromViewController fromViewController: UIViewController, identifier identifier: String?) -> UIStoryboardSegue?     func viewWillAppear(_ animated: Bool)     func viewDidAppear(_ animated: Bool)     func viewWillDisappear(_ animated: Bool)     func viewDidDisappear(_ animated: Bool)     func viewWillLayoutSubviews()     func viewDidLayoutSubviews()     var title: String?     func didReceiveMemoryWarning()     weak var parentViewController: UIViewController? { get }     var modalViewController: UIViewController? { get }     var presentedViewController: UIViewController? { get }     var presentingViewController: UIViewController? { get }     var definesPresentationContext: Bool     var providesPresentationContextTransitionStyle: Bool     func isBeingPresented() -> Bool     func isBeingDismissed() -> Bool     func isMovingToParentViewController() -> Bool     func isMovingFromParentViewController() -> Bool     func presentViewController(_ viewControllerToPresent: UIViewController, animated flag: Bool, completion completion: (() -> Void)?)     func dismissViewControllerAnimated(_ flag: Bool, completion completion: (() -> Void)?)     func presentModalViewController(_ modalViewController: UIViewController, animated animated: Bool)     func dismissModalViewControllerAnimated(_ animated: Bool)     var modalTransitionStyle: UIModalTransitionStyle     var modalPresentationStyle: UIModalPresentationStyle     var modalPresentationCapturesStatusBarAppearance: Bool     func disablesAutomaticKeyboardDismissal() -> Bool     var wantsFullScreenLayout: Bool     var edgesForExtendedLayout: UIRectEdge     var extendedLayoutIncludesOpaqueBars: Bool     var automaticallyAdjustsScrollViewInsets: Bool     var preferredContentSize: CGSize     func preferredStatusBarStyle() -> UIStatusBarStyle     func prefersStatusBarHidden() -> Bool     func preferredStatusBarUpdateAnimation() -> UIStatusBarAnimation     func setNeedsStatusBarAppearanceUpdate()     func targetViewControllerForAction(_ action: Selector, sender sender: AnyObject?) -> UIViewController?     func showViewController(_ vc: UIViewController, sender sender: AnyObject?)     func showDetailViewController(_ vc: UIViewController, sender sender: AnyObject?) } extension UIViewController {     func presentMoviePlayerViewControllerAnimated(_ moviePlayerViewController: MPMoviePlayerViewController!)     func dismissMoviePlayerViewControllerAnimated() } extension UIViewController {     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get } } extension UIViewController {     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool) } extension UIViewController {     var modalInPopover: Bool     var contentSizeForViewInPopover: CGSize } extension UIViewController {     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, forSplitViewController splitViewController: UISplitViewController)     func separateSecondaryViewControllerForSplitViewController(_ splitViewController: UISplitViewController) -> UIViewController? } extension UIViewController {     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get } } extension UIViewController {     class func attemptRotationToDeviceOrientation()     func shouldAutorotateToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation) -> Bool     func shouldAutorotate() -> Bool     func supportedInterfaceOrientations() -> UIInterfaceOrientationMask     func preferredInterfaceOrientationForPresentation() -> UIInterfaceOrientation     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotateToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func didRotateFromInterfaceOrientation(_ fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func willAnimateFirstHalfOfRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func didAnimateFirstHalfOfRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotationFromInterfaceOrientation(_ fromInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval) } extension UIViewController {     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     func editButtonItem() -> UIBarButtonItem } extension UIViewController {     var searchDisplayController: UISearchDisplayController? { get } } extension UIViewController {     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transitionFromViewController(_ fromViewController: UIViewController, toViewController toViewController: UIViewController, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: (() -> Void)?, completion completion: ((Bool) -> Void)?)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     func childViewControllerForStatusBarStyle() -> UIViewController?     func childViewControllerForStatusBarHidden() -> UIViewController?     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollectionForChildViewController(_ childViewController: UIViewController) -> UITraitCollection? } extension UIViewController {     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     func shouldAutomaticallyForwardAppearanceMethods() -> Bool     func willMoveToParentViewController(_ parent: UIViewController?)     func didMoveToParentViewController(_ parent: UIViewController?) } extension UIViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: AnyObject.Type?     func encodeRestorableStateWithCoder(_ coder: NSCoder)     func decodeRestorableStateWithCoder(_ coder: NSCoder)     func applicationFinishedRestoringState() } extension UIViewController {     func updateViewConstraints() } extension UIViewController {     weak var transitioningDelegate: UIViewControllerTransitioningDelegate? } extension UIViewController {     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get } } extension UIViewController {     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand) } extension UIViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension UIViewController {     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get } } extension UIViewController {     func registerForPreviewingWithDelegate(_ delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewingWithContext(_ previewing: UIViewControllerPreviewing) } extension UIViewController {     func previewActionItems() -> [UIPreviewActionItem] } extension UIViewController {     func transitionCoordinator() -> UIViewControllerTransitionCoordinator? } extension UIViewController {     class func prepareInterstitialAds()     var interstitialPresentationPolicy: ADInterstitialPresentationPolicy     var canDisplayBannerAds: Bool     var originalContentView: UIView! { get }     var presentingFullScreenAd: Bool { get }     var displayingBannerAd: Bool { get }     func requestInterstitialAdPresentation() -> Bool     var shouldPresentInterstitialAd: Bool { get } } ``` |

Modified [UIViewController.childViewControllers](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621452-children)

|  | Declaration |
| --- | --- |
| From | ``` var childViewControllers: [AnyObject] { get } ``` |
| To | ``` var childViewControllers: [UIViewController] { get } ``` |

Modified [UIViewController.overrideTraitCollectionForChildViewController(_: UIViewController) -> UITraitCollection?](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621486-overridetraitcollection)

|  | Declaration |
| --- | --- |
| From | ``` func overrideTraitCollectionForChildViewController(_ childViewController: UIViewController) -> UITraitCollection! ``` |
| To | ``` func overrideTraitCollectionForChildViewController(_ childViewController: UIViewController) -> UITraitCollection? ``` |

Modified [UIViewController.parentViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621362-parentviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` var parentViewController: UIViewController? { get } ``` |
| To | ``` weak var parentViewController: UIViewController? { get } ``` |

Modified [UIViewController.performSegueWithIdentifier(_: String, sender: AnyObject?)](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621413-performseguewithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func performSegueWithIdentifier(_ identifier: String?, sender sender: AnyObject?) ``` |
| To | ``` func performSegueWithIdentifier(_ identifier: String, sender sender: AnyObject?) ``` |

Modified [UIViewController.segueForUnwindingToViewController(_: UIViewController, fromViewController: UIViewController, identifier: String?) -> UIStoryboardSegue?](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621500-segueforunwinding)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func segueForUnwindingToViewController(_ toViewController: UIViewController, fromViewController fromViewController: UIViewController, identifier identifier: String?) -> UIStoryboardSegue ``` | -- |
| To | ``` func segueForUnwindingToViewController(_ toViewController: UIViewController, fromViewController fromViewController: UIViewController, identifier identifier: String?) -> UIStoryboardSegue? ``` | iOS 9.0 |

Modified [UIViewController.separateSecondaryViewControllerForSplitViewController(_: UISplitViewController) -> UIViewController?](https://developer.apple.com/documentation/uikit/uiviewcontroller/1623191-separatesecondaryviewcontrollerf)

|  | Declaration |
| --- | --- |
| From | ``` func separateSecondaryViewControllerForSplitViewController(_ splitViewController: UISplitViewController) -> UIViewController ``` |
| To | ``` func separateSecondaryViewControllerForSplitViewController(_ splitViewController: UISplitViewController) -> UIViewController? ``` |

Modified [UIViewController.setToolbarItems(_: [UIBarButtonItem]?, animated: Bool)](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621874-settoolbaritems)

|  | Declaration |
| --- | --- |
| From | ``` func setToolbarItems(_ toolbarItems: [AnyObject]?, animated animated: Bool) ``` |
| To | ``` func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool) ``` |

Modified [UIViewController.shouldPerformSegueWithIdentifier(_: String, sender: AnyObject?) -> Bool](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621502-shouldperformsegue)

|  | Declaration |
| --- | --- |
| From | ``` func shouldPerformSegueWithIdentifier(_ identifier: String?, sender sender: AnyObject?) -> Bool ``` |
| To | ``` func shouldPerformSegueWithIdentifier(_ identifier: String, sender sender: AnyObject?) -> Bool ``` |

Modified [UIViewController.supportedInterfaceOrientations() -> UIInterfaceOrientationMask](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621435-supportedinterfaceorientations)

|  | Declaration |
| --- | --- |
| From | ``` func supportedInterfaceOrientations() -> Int ``` |
| To | ``` func supportedInterfaceOrientations() -> UIInterfaceOrientationMask ``` |

Modified [UIViewController.toolbarItems](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621867-toolbaritems)

|  | Declaration |
| --- | --- |
| From | ``` var toolbarItems: [AnyObject]? ``` |
| To | ``` var toolbarItems: [UIBarButtonItem]? ``` |

Modified [UIViewController.transitioningDelegate](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621421-transitioningdelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var transitioningDelegate: UIViewControllerTransitioningDelegate? ``` |
| To | ``` weak var transitioningDelegate: UIViewControllerTransitioningDelegate? ``` |

Modified [UIViewController.viewControllerForUnwindSegueAction(_: Selector, fromViewController: UIViewController, withSender: AnyObject?) -> UIViewController?](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621448-viewcontrollerforunwindsegueacti)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [UIViewControllerAnimatedTransitioning](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIViewControllerAnimatedTransitioning : NSObjectProtocol {     func transitionDuration(_ transitionContext: UIViewControllerContextTransitioning) -> NSTimeInterval     func animateTransition(_ transitionContext: UIViewControllerContextTransitioning)     optional func animationEnded(_ transitionCompleted: Bool) } ``` |
| To | ``` protocol UIViewControllerAnimatedTransitioning : NSObjectProtocol {     func transitionDuration(_ transitionContext: UIViewControllerContextTransitioning?) -> NSTimeInterval     func animateTransition(_ transitionContext: UIViewControllerContextTransitioning)     optional func animationEnded(_ transitionCompleted: Bool) } ``` |

Modified [UIViewControllerAnimatedTransitioning.transitionDuration(_: UIViewControllerContextTransitioning?) -> NSTimeInterval](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/1622032-transitionduration)

|  | Declaration |
| --- | --- |
| From | ``` func transitionDuration(_ transitionContext: UIViewControllerContextTransitioning) -> NSTimeInterval ``` |
| To | ``` func transitionDuration(_ transitionContext: UIViewControllerContextTransitioning?) -> NSTimeInterval ``` |

Modified [UIViewControllerContextTransitioning](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIViewControllerContextTransitioning : NSObjectProtocol {     func containerView() -> UIView     func isAnimated() -> Bool     func isInteractive() -> Bool     func transitionWasCancelled() -> Bool     func presentationStyle() -> UIModalPresentationStyle     func updateInteractiveTransition(_ percentComplete: CGFloat)     func finishInteractiveTransition()     func cancelInteractiveTransition()     func completeTransition(_ didComplete: Bool)     func viewControllerForKey(_ key: String) -> UIViewController?     func viewForKey(_ key: String) -> UIView?     func targetTransform() -> CGAffineTransform     func initialFrameForViewController(_ vc: UIViewController) -> CGRect     func finalFrameForViewController(_ vc: UIViewController) -> CGRect } ``` |
| To | ``` protocol UIViewControllerContextTransitioning : NSObjectProtocol {     func containerView() -> UIView?     func isAnimated() -> Bool     func isInteractive() -> Bool     func transitionWasCancelled() -> Bool     func presentationStyle() -> UIModalPresentationStyle     func updateInteractiveTransition(_ percentComplete: CGFloat)     func finishInteractiveTransition()     func cancelInteractiveTransition()     func completeTransition(_ didComplete: Bool)     func viewControllerForKey(_ key: String) -> UIViewController?     func viewForKey(_ key: String) -> UIView?     func targetTransform() -> CGAffineTransform     func initialFrameForViewController(_ vc: UIViewController) -> CGRect     func finalFrameForViewController(_ vc: UIViewController) -> CGRect } ``` |

Modified [UIViewControllerContextTransitioning.containerView() -> UIView?](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622045-containerview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func containerView() -> UIView ``` | iOS 8.0 |
| To | ``` func containerView() -> UIView? ``` | iOS 2.0 |

Modified [UIViewControllerContextTransitioning.finalFrameForViewController(_: UIViewController) -> CGRect](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622024-finalframeforviewcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIViewControllerContextTransitioning.initialFrameForViewController(_: UIViewController) -> CGRect](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622033-initialframeforviewcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIViewControllerContextTransitioning.viewControllerForKey(_: String) -> UIViewController?](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/1622043-viewcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIViewControllerRestoration.viewControllerWithRestorationIdentifierPath(_: [AnyObject], coder: NSCoder) -> UIViewController? [class]](https://developer.apple.com/documentation/uikit/uiviewcontrollerrestoration/1616859-viewcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIViewControllerTransitionCoordinator](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIViewControllerTransitionCoordinator : UIViewControllerTransitionCoordinatorContext, NSObjectProtocol {     func animateAlongsideTransition(_ animation: ((UIViewControllerTransitionCoordinatorContext!) -> Void)!, completion completion: ((UIViewControllerTransitionCoordinatorContext!) -> Void)!) -> Bool     func animateAlongsideTransitionInView(_ view: UIView!, animation animation: ((UIViewControllerTransitionCoordinatorContext!) -> Void)!, completion completion: ((UIViewControllerTransitionCoordinatorContext!) -> Void)!) -> Bool     func notifyWhenInteractionEndsUsingBlock(_ handler: (UIViewControllerTransitionCoordinatorContext!) -> Void) } ``` |
| To | ``` protocol UIViewControllerTransitionCoordinator : UIViewControllerTransitionCoordinatorContext, NSObjectProtocol {     func animateAlongsideTransition(_ animation: ((UIViewControllerTransitionCoordinatorContext) -> Void)?, completion completion: ((UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool     func animateAlongsideTransitionInView(_ view: UIView?, animation animation: ((UIViewControllerTransitionCoordinatorContext) -> Void)?, completion completion: ((UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool     func notifyWhenInteractionEndsUsingBlock(_ handler: (UIViewControllerTransitionCoordinatorContext) -> Void) } ``` |

Modified [UIViewControllerTransitionCoordinator.animateAlongsideTransition(_: ((UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/1619300-animate)

|  | Declaration |
| --- | --- |
| From | ``` func animateAlongsideTransition(_ animation: ((UIViewControllerTransitionCoordinatorContext!) -> Void)!, completion completion: ((UIViewControllerTransitionCoordinatorContext!) -> Void)!) -> Bool ``` |
| To | ``` func animateAlongsideTransition(_ animation: ((UIViewControllerTransitionCoordinatorContext) -> Void)?, completion completion: ((UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool ``` |

Modified [UIViewControllerTransitionCoordinator.animateAlongsideTransitionInView(_: UIView?, animation: ((UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/1619295-animatealongsidetransitioninview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func animateAlongsideTransitionInView(_ view: UIView!, animation animation: ((UIViewControllerTransitionCoordinatorContext!) -> Void)!, completion completion: ((UIViewControllerTransitionCoordinatorContext!) -> Void)!) -> Bool ``` | iOS 8.0 |
| To | ``` func animateAlongsideTransitionInView(_ view: UIView?, animation animation: ((UIViewControllerTransitionCoordinatorContext) -> Void)?, completion completion: ((UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool ``` | iOS 2.0 |

Modified [UIViewControllerTransitionCoordinator.notifyWhenInteractionEndsUsingBlock(_: (UIViewControllerTransitionCoordinatorContext) -> Void)](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/1619292-notifywheninteractionends)

|  | Declaration |
| --- | --- |
| From | ``` func notifyWhenInteractionEndsUsingBlock(_ handler: (UIViewControllerTransitionCoordinatorContext!) -> Void) ``` |
| To | ``` func notifyWhenInteractionEndsUsingBlock(_ handler: (UIViewControllerTransitionCoordinatorContext) -> Void) ``` |

Modified [UIViewControllerTransitionCoordinatorContext](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIViewControllerTransitionCoordinatorContext : NSObjectProtocol {     func isAnimated() -> Bool     func presentationStyle() -> UIModalPresentationStyle     func initiallyInteractive() -> Bool     func isInteractive() -> Bool     func isCancelled() -> Bool     func transitionDuration() -> NSTimeInterval     func percentComplete() -> CGFloat     func completionVelocity() -> CGFloat     func completionCurve() -> UIViewAnimationCurve     func viewControllerForKey(_ key: String) -> UIViewController!     func viewForKey(_ key: String) -> UIView?     func containerView() -> UIView     func targetTransform() -> CGAffineTransform } ``` |
| To | ``` protocol UIViewControllerTransitionCoordinatorContext : NSObjectProtocol {     func isAnimated() -> Bool     func presentationStyle() -> UIModalPresentationStyle     func initiallyInteractive() -> Bool     func isInteractive() -> Bool     func isCancelled() -> Bool     func transitionDuration() -> NSTimeInterval     func percentComplete() -> CGFloat     func completionVelocity() -> CGFloat     func completionCurve() -> UIViewAnimationCurve     func viewControllerForKey(_ key: String) -> UIViewController?     func viewForKey(_ key: String) -> UIView?     func containerView() -> UIView     func targetTransform() -> CGAffineTransform } ``` |

Modified [UIViewControllerTransitionCoordinatorContext.containerView() -> UIView](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619280-containerview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIViewControllerTransitionCoordinatorContext.viewControllerForKey(_: String) -> UIViewController?](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/1619293-viewcontrollerforkey)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func viewControllerForKey(_ key: String) -> UIViewController! ``` | iOS 8.0 |
| To | ``` func viewControllerForKey(_ key: String) -> UIViewController? ``` | iOS 2.0 |

Modified [UIViewControllerTransitioningDelegate](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIViewControllerTransitioningDelegate : NSObjectProtocol {     optional func animationControllerForPresentedController(_ presented: UIViewController, presentingController presenting: UIViewController, sourceController source: UIViewController) -> UIViewControllerAnimatedTransitioning?     optional func animationControllerForDismissedController(_ dismissed: UIViewController) -> UIViewControllerAnimatedTransitioning?     optional func interactionControllerForPresentation(_ animator: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning?     optional func interactionControllerForDismissal(_ animator: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning?     optional func presentationControllerForPresentedViewController(_ presented: UIViewController, presentingViewController presenting: UIViewController!, sourceViewController source: UIViewController) -> UIPresentationController? } ``` |
| To | ``` protocol UIViewControllerTransitioningDelegate : NSObjectProtocol {     optional func animationControllerForPresentedController(_ presented: UIViewController, presentingController presenting: UIViewController, sourceController source: UIViewController) -> UIViewControllerAnimatedTransitioning?     optional func animationControllerForDismissedController(_ dismissed: UIViewController) -> UIViewControllerAnimatedTransitioning?     optional func interactionControllerForPresentation(_ animator: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning?     optional func interactionControllerForDismissal(_ animator: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning?     optional func presentationControllerForPresentedViewController(_ presented: UIViewController, presentingViewController presenting: UIViewController, sourceViewController source: UIViewController) -> UIPresentationController? } ``` |

Modified [UIViewControllerTransitioningDelegate.animationControllerForDismissedController(_: UIViewController) -> UIViewControllerAnimatedTransitioning?](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622047-animationcontroller)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIViewControllerTransitioningDelegate.animationControllerForPresentedController(_: UIViewController, presentingController: UIViewController, sourceController: UIViewController) -> UIViewControllerAnimatedTransitioning?](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622037-animationcontrollerforpresentedc)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIViewControllerTransitioningDelegate.presentationControllerForPresentedViewController(_: UIViewController, presentingViewController: UIViewController, sourceViewController: UIViewController) -> UIPresentationController?](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622057-presentationcontrollerforpresent)

|  | Declaration |
| --- | --- |
| From | ``` optional func presentationControllerForPresentedViewController(_ presented: UIViewController, presentingViewController presenting: UIViewController!, sourceViewController source: UIViewController) -> UIPresentationController? ``` |
| To | ``` optional func presentationControllerForPresentedViewController(_ presented: UIViewController, presentingViewController presenting: UIViewController, sourceViewController source: UIViewController) -> UIPresentationController? ``` |

Modified [UIViewKeyframeAnimationOptions [struct]](https://developer.apple.com/documentation/uikit/uiviewkeyframeanimationoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UIViewKeyframeAnimationOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var LayoutSubviews: UIViewKeyframeAnimationOptions { get }     static var AllowUserInteraction: UIViewKeyframeAnimationOptions { get }     static var BeginFromCurrentState: UIViewKeyframeAnimationOptions { get }     static var Repeat: UIViewKeyframeAnimationOptions { get }     static var Autoreverse: UIViewKeyframeAnimationOptions { get }     static var OverrideInheritedDuration: UIViewKeyframeAnimationOptions { get }     static var OverrideInheritedOptions: UIViewKeyframeAnimationOptions { get }     static var CalculationModeLinear: UIViewKeyframeAnimationOptions { get }     static var CalculationModeDiscrete: UIViewKeyframeAnimationOptions { get }     static var CalculationModePaced: UIViewKeyframeAnimationOptions { get }     static var CalculationModeCubic: UIViewKeyframeAnimationOptions { get }     static var CalculationModeCubicPaced: UIViewKeyframeAnimationOptions { get } } ``` | RawOptionSetType |
| To | ``` struct UIViewKeyframeAnimationOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var LayoutSubviews: UIViewKeyframeAnimationOptions { get }     static var AllowUserInteraction: UIViewKeyframeAnimationOptions { get }     static var BeginFromCurrentState: UIViewKeyframeAnimationOptions { get }     static var Repeat: UIViewKeyframeAnimationOptions { get }     static var Autoreverse: UIViewKeyframeAnimationOptions { get }     static var OverrideInheritedDuration: UIViewKeyframeAnimationOptions { get }     static var OverrideInheritedOptions: UIViewKeyframeAnimationOptions { get }     static var CalculationModeLinear: UIViewKeyframeAnimationOptions { get }     static var CalculationModeDiscrete: UIViewKeyframeAnimationOptions { get }     static var CalculationModePaced: UIViewKeyframeAnimationOptions { get }     static var CalculationModeCubic: UIViewKeyframeAnimationOptions { get }     static var CalculationModeCubicPaced: UIViewKeyframeAnimationOptions { get } } ``` | OptionSetType |

Modified [UIViewTintAdjustmentMode [enum]](https://developer.apple.com/documentation/uikit/uiviewtintadjustmentmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIVisualEffectView](https://developer.apple.com/documentation/uikit/uivisualeffectview)

|  | Declaration |
| --- | --- |
| From | ``` class UIVisualEffectView : UIView, NSSecureCoding, NSCoding {     var contentView: UIView { get }     @NSCopying var effect: UIVisualEffect { get }     init(effect effect: UIVisualEffect) } ``` |
| To | ``` class UIVisualEffectView : UIView, NSSecureCoding {     var contentView: UIView { get }     @NSCopying var effect: UIVisualEffect?     init(effect effect: UIVisualEffect?)     init?(coder aDecoder: NSCoder) } ``` |

Modified [UIVisualEffectView.effect](https://developer.apple.com/documentation/uikit/uivisualeffectview/1615072-effect)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var effect: UIVisualEffect { get } ``` |
| To | ``` @NSCopying var effect: UIVisualEffect? ``` |

Modified [UIVisualEffectView.init(effect: UIVisualEffect?)](https://developer.apple.com/documentation/uikit/uivisualeffectview/1615051-initwitheffect)

|  | Declaration |
| --- | --- |
| From | ``` init(effect effect: UIVisualEffect) ``` |
| To | ``` init(effect effect: UIVisualEffect?) ``` |

Modified [UIWebPaginationBreakingMode [enum]](https://developer.apple.com/documentation/uikit/uiwebview/paginationbreakingmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIWebPaginationMode [enum]](https://developer.apple.com/documentation/uikit/uiwebpaginationmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview)

|  | Declaration |
| --- | --- |
| From | ``` class UIWebView : UIView, NSCoding, UIScrollViewDelegate, NSObjectProtocol {     unowned(unsafe) var delegate: UIWebViewDelegate?     var scrollView: UIScrollView { get }     func loadRequest(_ request: NSURLRequest)     func loadHTMLString(_ string: String!, baseURL baseURL: NSURL!)     func loadData(_ data: NSData!, MIMEType MIMEType: String!, textEncodingName textEncodingName: String!, baseURL baseURL: NSURL!)     var request: NSURLRequest? { get }     func reload()     func stopLoading()     func goBack()     func goForward()     var canGoBack: Bool { get }     var canGoForward: Bool { get }     var loading: Bool { get }     func stringByEvaluatingJavaScriptFromString(_ script: String) -> String?     var scalesPageToFit: Bool     var detectsPhoneNumbers: Bool     var dataDetectorTypes: UIDataDetectorTypes     var allowsInlineMediaPlayback: Bool     var mediaPlaybackRequiresUserAction: Bool     var mediaPlaybackAllowsAirPlay: Bool     var suppressesIncrementalRendering: Bool     var keyboardDisplayRequiresUserAction: Bool     var paginationMode: UIWebPaginationMode     var paginationBreakingMode: UIWebPaginationBreakingMode     var pageLength: CGFloat     var gapBetweenPages: CGFloat     var pageCount: Int { get } } ``` |
| To | ``` class UIWebView : UIView, UIScrollViewDelegate {     unowned(unsafe) var delegate: UIWebViewDelegate?     var scrollView: UIScrollView { get }     func loadRequest(_ request: NSURLRequest)     func loadHTMLString(_ string: String, baseURL baseURL: NSURL?)     func loadData(_ data: NSData, MIMEType MIMEType: String, textEncodingName textEncodingName: String, baseURL baseURL: NSURL)     var request: NSURLRequest? { get }     func reload()     func stopLoading()     func goBack()     func goForward()     var canGoBack: Bool { get }     var canGoForward: Bool { get }     var loading: Bool { get }     func stringByEvaluatingJavaScriptFromString(_ script: String) -> String?     var scalesPageToFit: Bool     var detectsPhoneNumbers: Bool     var dataDetectorTypes: UIDataDetectorTypes     var allowsInlineMediaPlayback: Bool     var mediaPlaybackRequiresUserAction: Bool     var mediaPlaybackAllowsAirPlay: Bool     var suppressesIncrementalRendering: Bool     var keyboardDisplayRequiresUserAction: Bool     var paginationMode: UIWebPaginationMode     var paginationBreakingMode: UIWebPaginationBreakingMode     var pageLength: CGFloat     var gapBetweenPages: CGFloat     var pageCount: Int { get }     var allowsPictureInPictureMediaPlayback: Bool     var allowsLinkPreview: Bool } ``` |

Modified [UIWebView.loadData(_: NSData, MIMEType: String, textEncodingName: String, baseURL: NSURL)](https://developer.apple.com/documentation/uikit/uiwebview/1617941-loaddata)

|  | Declaration |
| --- | --- |
| From | ``` func loadData(_ data: NSData!, MIMEType MIMEType: String!, textEncodingName textEncodingName: String!, baseURL baseURL: NSURL!) ``` |
| To | ``` func loadData(_ data: NSData, MIMEType MIMEType: String, textEncodingName textEncodingName: String, baseURL baseURL: NSURL) ``` |

Modified [UIWebView.loadHTMLString(_: String, baseURL: NSURL?)](https://developer.apple.com/documentation/uikit/uiwebview/1617979-loadhtmlstring)

|  | Declaration |
| --- | --- |
| From | ``` func loadHTMLString(_ string: String!, baseURL baseURL: NSURL!) ``` |
| To | ``` func loadHTMLString(_ string: String, baseURL baseURL: NSURL?) ``` |

Modified [UIWebViewDelegate](https://developer.apple.com/documentation/uikit/uiwebviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIWebViewDelegate : NSObjectProtocol {     optional func webView(_ webView: UIWebView, shouldStartLoadWithRequest request: NSURLRequest, navigationType navigationType: UIWebViewNavigationType) -> Bool     optional func webViewDidStartLoad(_ webView: UIWebView)     optional func webViewDidFinishLoad(_ webView: UIWebView)     optional func webView(_ webView: UIWebView, didFailLoadWithError error: NSError) } ``` |
| To | ``` protocol UIWebViewDelegate : NSObjectProtocol {     optional func webView(_ webView: UIWebView, shouldStartLoadWithRequest request: NSURLRequest, navigationType navigationType: UIWebViewNavigationType) -> Bool     optional func webViewDidStartLoad(_ webView: UIWebView)     optional func webViewDidFinishLoad(_ webView: UIWebView)     optional func webView(_ webView: UIWebView, didFailLoadWithError error: NSError?) } ``` |

Modified [UIWebViewDelegate.webView(_: UIWebView, didFailLoadWithError: NSError?)](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617970-webview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func webView(_ webView: UIWebView, didFailLoadWithError error: NSError) ``` | iOS 8.0 |
| To | ``` optional func webView(_ webView: UIWebView, didFailLoadWithError error: NSError?) ``` | iOS 2.0 |

Modified [UIWebViewDelegate.webView(_: UIWebView, shouldStartLoadWithRequest: NSURLRequest, navigationType: UIWebViewNavigationType) -> Bool](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617945-webview)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIWebViewDelegate.webViewDidFinishLoad(_: UIWebView)](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617969-webviewdidfinishload)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIWebViewDelegate.webViewDidStartLoad(_: UIWebView)](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617947-webviewdidstartload)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [UIWebViewNavigationType [enum]](https://developer.apple.com/documentation/uikit/uiwebviewnavigationtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CGAffineTransformFromString(_: String) -> CGAffineTransform](https://developer.apple.com/documentation/uikit/1624505-cgaffinetransformfromstring)

|  | Declaration |
| --- | --- |
| From | ``` func CGAffineTransformFromString(_ string: String!) -> CGAffineTransform ``` |
| To | ``` func CGAffineTransformFromString(_ string: String) -> CGAffineTransform ``` |

Modified [CGPointFromString(_: String) -> CGPoint](https://developer.apple.com/documentation/foundation/nscoder/1624477-cgpoint)

|  | Declaration |
| --- | --- |
| From | ``` func CGPointFromString(_ string: String!) -> CGPoint ``` |
| To | ``` func CGPointFromString(_ string: String) -> CGPoint ``` |

Modified [CGRectFromString(_: String) -> CGRect](https://developer.apple.com/documentation/uikit/1624508-cgrectfromstring)

|  | Declaration |
| --- | --- |
| From | ``` func CGRectFromString(_ string: String!) -> CGRect ``` |
| To | ``` func CGRectFromString(_ string: String) -> CGRect ``` |

Modified [CGSizeFromString(_: String) -> CGSize](https://developer.apple.com/documentation/foundation/nscoder/1624484-cgsize)

|  | Declaration |
| --- | --- |
| From | ``` func CGSizeFromString(_ string: String!) -> CGSize ``` |
| To | ``` func CGSizeFromString(_ string: String) -> CGSize ``` |

Modified [CGVectorFromString(_: String) -> CGVector](https://developer.apple.com/documentation/uikit/1624513-cgvectorfromstring)

|  | Declaration |
| --- | --- |
| From | ``` func CGVectorFromString(_ string: String!) -> CGVector ``` |
| To | ``` func CGVectorFromString(_ string: String) -> CGVector ``` |

Modified [NSStringFromCGAffineTransform(_: CGAffineTransform) -> String](https://developer.apple.com/documentation/foundation/nscoder/1624497-string)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromCGAffineTransform(_ transform: CGAffineTransform) -> String! ``` |
| To | ``` func NSStringFromCGAffineTransform(_ transform: CGAffineTransform) -> String ``` |

Modified [NSStringFromCGPoint(_: CGPoint) -> String](https://developer.apple.com/documentation/foundation/nscoder/1624504-string)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromCGPoint(_ point: CGPoint) -> String! ``` |
| To | ``` func NSStringFromCGPoint(_ point: CGPoint) -> String ``` |

Modified [NSStringFromCGRect(_: CGRect) -> String](https://developer.apple.com/documentation/foundation/nscoder/1624474-string)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromCGRect(_ rect: CGRect) -> String! ``` |
| To | ``` func NSStringFromCGRect(_ rect: CGRect) -> String ``` |

Modified [NSStringFromCGSize(_: CGSize) -> String](https://developer.apple.com/documentation/uikit/1624514-nsstringfromcgsize)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromCGSize(_ size: CGSize) -> String! ``` |
| To | ``` func NSStringFromCGSize(_ size: CGSize) -> String ``` |

Modified [NSStringFromCGVector(_: CGVector) -> String](https://developer.apple.com/documentation/foundation/nscoder/1624476-string)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromCGVector(_ vector: CGVector) -> String! ``` |
| To | ``` func NSStringFromCGVector(_ vector: CGVector) -> String ``` |

Modified [NSStringFromUIEdgeInsets(_: UIEdgeInsets) -> String](https://developer.apple.com/documentation/uikit/1624527-nsstringfromuiedgeinsets)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromUIEdgeInsets(_ insets: UIEdgeInsets) -> String! ``` |
| To | ``` func NSStringFromUIEdgeInsets(_ insets: UIEdgeInsets) -> String ``` |

Modified [NSStringFromUIOffset(_: UIOffset) -> String](https://developer.apple.com/documentation/uikit/1624491-nsstringfromuioffset)

|  | Declaration |
| --- | --- |
| From | ``` func NSStringFromUIOffset(_ offset: UIOffset) -> String! ``` |
| To | ``` func NSStringFromUIOffset(_ offset: UIOffset) -> String ``` |

Modified [UIAccessibilityConvertFrameToScreenCoordinates(_: CGRect, _: UIView) -> CGRect](https://developer.apple.com/documentation/uikit/1615145-uiaccessibilityconvertframetoscr)

|  | Declaration |
| --- | --- |
| From | ``` func UIAccessibilityConvertFrameToScreenCoordinates(_ rect: CGRect, _ view: UIView!) -> CGRect ``` |
| To | ``` func UIAccessibilityConvertFrameToScreenCoordinates(_ rect: CGRect, _ view: UIView) -> CGRect ``` |

Modified [UIAccessibilityConvertPathToScreenCoordinates(_: UIBezierPath, _: UIView) -> UIBezierPath](https://developer.apple.com/documentation/uikit/1615139-uiaccessibilityconvertpathtoscre)

|  | Declaration |
| --- | --- |
| From | ``` func UIAccessibilityConvertPathToScreenCoordinates(_ path: UIBezierPath!, _ view: UIView!) -> UIBezierPath! ``` |
| To | ``` func UIAccessibilityConvertPathToScreenCoordinates(_ path: UIBezierPath, _ view: UIView) -> UIBezierPath ``` |

Modified [UIAccessibilityPostNotification(_: UIAccessibilityNotifications, _: AnyObject?)](https://developer.apple.com/documentation/uikit/1615194-uiaccessibilitypostnotification)

|  | Declaration |
| --- | --- |
| From | ``` func UIAccessibilityPostNotification(_ notification: UIAccessibilityNotifications, _ argument: AnyObject!) ``` |
| To | ``` func UIAccessibilityPostNotification(_ notification: UIAccessibilityNotifications, _ argument: AnyObject?) ``` |

Modified [UIAccessibilityRequestGuidedAccessSession(_: Bool, _: (Bool) -> Void)](https://developer.apple.com/documentation/uikit/1615186-uiaccessibilityrequestguidedacce)

|  | Declaration |
| --- | --- |
| From | ``` func UIAccessibilityRequestGuidedAccessSession(_ enable: Bool, _ completionHandler: ((Bool) -> Void)!) ``` |
| To | ``` func UIAccessibilityRequestGuidedAccessSession(_ enable: Bool, _ completionHandler: (Bool) -> Void) ``` |

Modified [UIAccessibilityZoomFocusChanged(_: UIAccessibilityZoomType, _: CGRect, _: UIView)](https://developer.apple.com/documentation/uikit/uiaccessibility/1624921-zoomfocuschanged)

|  | Declaration |
| --- | --- |
| From | ``` func UIAccessibilityZoomFocusChanged(_ type: UIAccessibilityZoomType, _ frame: CGRect, _ view: UIView!) ``` |
| To | ``` func UIAccessibilityZoomFocusChanged(_ type: UIAccessibilityZoomType, _ frame: CGRect, _ view: UIView) ``` |

Modified [UIActivityViewControllerCompletionHandler](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias UIActivityViewControllerCompletionHandler = (String!, Bool) -> Void ``` |
| To | ``` typealias UIActivityViewControllerCompletionHandler = (String?, Bool) -> Void ``` |

Modified [UIActivityViewControllerCompletionWithItemsHandler](https://developer.apple.com/documentation/uikit/uiactivityviewcontrollercompletionwithitemshandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias UIActivityViewControllerCompletionWithItemsHandler = (String!, Bool, [AnyObject]!, NSError!) -> Void ``` |
| To | ``` typealias UIActivityViewControllerCompletionWithItemsHandler = (String?, Bool, [AnyObject]?, NSError?) -> Void ``` |

Modified [UIApplicationMain(_: Int32, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _: String?, _: String?) -> Int32](https://developer.apple.com/documentation/uikit/1622933-uiapplicationmain)

|  | Declaration |
| --- | --- |
| From | ``` func UIApplicationMain(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ principalClassName: String!, _ delegateClassName: String!) -> Int32 ``` |
| To | ``` func UIApplicationMain(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ principalClassName: String?, _ delegateClassName: String?) -> Int32 ``` |

Modified UIDeviceOrientationIsLandscape(_: UIDeviceOrientation) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func UIDeviceOrientationIsLandscape(_ orientation: UIDeviceOrientation) -> Bool ``` |
| To | ``` @warn_unused_result func UIDeviceOrientationIsLandscape(_ orientation: UIDeviceOrientation) -> Bool ``` |

Modified UIDeviceOrientationIsPortrait(_: UIDeviceOrientation) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func UIDeviceOrientationIsPortrait(_ orientation: UIDeviceOrientation) -> Bool ``` |
| To | ``` @warn_unused_result func UIDeviceOrientationIsPortrait(_ orientation: UIDeviceOrientation) -> Bool ``` |

Modified UIDeviceOrientationIsValidInterfaceOrientation(_: UIDeviceOrientation) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func UIDeviceOrientationIsValidInterfaceOrientation(_ orientation: UIDeviceOrientation) -> Bool ``` |
| To | ``` @warn_unused_result func UIDeviceOrientationIsValidInterfaceOrientation(_ orientation: UIDeviceOrientation) -> Bool ``` |

Modified [UIEdgeInsetsFromString(_: String) -> UIEdgeInsets](https://developer.apple.com/documentation/foundation/nscoder/1624525-uiedgeinsets)

|  | Declaration |
| --- | --- |
| From | ``` func UIEdgeInsetsFromString(_ string: String!) -> UIEdgeInsets ``` |
| To | ``` func UIEdgeInsetsFromString(_ string: String) -> UIEdgeInsets ``` |

Modified [UIGraphicsAddPDFContextDestinationAtPoint(_: String, _: CGPoint)](https://developer.apple.com/documentation/uikit/1623911-uigraphicsaddpdfcontextdestinati)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsAddPDFContextDestinationAtPoint(_ name: String!, _ point: CGPoint) ``` |
| To | ``` func UIGraphicsAddPDFContextDestinationAtPoint(_ name: String, _ point: CGPoint) ``` |

Modified [UIGraphicsBeginPDFContextToData(_: NSMutableData, _: CGRect, _: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/uikit/1623931-uigraphicsbeginpdfcontexttodata)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsBeginPDFContextToData(_ data: NSMutableData!, _ bounds: CGRect, _ documentInfo: [NSObject : AnyObject]!) ``` |
| To | ``` func UIGraphicsBeginPDFContextToData(_ data: NSMutableData, _ bounds: CGRect, _ documentInfo: [NSObject : AnyObject]?) ``` |

Modified [UIGraphicsBeginPDFContextToFile(_: String, _: CGRect, _: [NSObject : AnyObject]?) -> Bool](https://developer.apple.com/documentation/uikit/1623927-uigraphicsbeginpdfcontexttofile)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsBeginPDFContextToFile(_ path: String!, _ bounds: CGRect, _ documentInfo: [NSObject : AnyObject]!) -> Bool ``` |
| To | ``` func UIGraphicsBeginPDFContextToFile(_ path: String, _ bounds: CGRect, _ documentInfo: [NSObject : AnyObject]?) -> Bool ``` |

Modified [UIGraphicsBeginPDFPageWithInfo(_: CGRect, _: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/uikit/1623915-uigraphicsbeginpdfpagewithinfo)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsBeginPDFPageWithInfo(_ bounds: CGRect, _ pageInfo: [NSObject : AnyObject]!) ``` |
| To | ``` func UIGraphicsBeginPDFPageWithInfo(_ bounds: CGRect, _ pageInfo: [NSObject : AnyObject]?) ``` |

Modified [UIGraphicsGetCurrentContext() -> CGContext?](https://developer.apple.com/documentation/uikit/1623918-uigraphicsgetcurrentcontext)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsGetCurrentContext() -> CGContext! ``` |
| To | ``` func UIGraphicsGetCurrentContext() -> CGContext? ``` |

Modified [UIGraphicsPushContext(_: CGContext)](https://developer.apple.com/documentation/uikit/1623921-uigraphicspushcontext)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsPushContext(_ context: CGContext!) ``` |
| To | ``` func UIGraphicsPushContext(_ context: CGContext) ``` |

Modified [UIGraphicsSetPDFContextDestinationForRect(_: String, _: CGRect)](https://developer.apple.com/documentation/uikit/1623925-uigraphicssetpdfcontextdestinati)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsSetPDFContextDestinationForRect(_ name: String!, _ rect: CGRect) ``` |
| To | ``` func UIGraphicsSetPDFContextDestinationForRect(_ name: String, _ rect: CGRect) ``` |

Modified [UIGraphicsSetPDFContextURLForRect(_: NSURL, _: CGRect)](https://developer.apple.com/documentation/uikit/1623916-uigraphicssetpdfcontexturlforrec)

|  | Declaration |
| --- | --- |
| From | ``` func UIGraphicsSetPDFContextURLForRect(_ url: NSURL!, _ rect: CGRect) ``` |
| To | ``` func UIGraphicsSetPDFContextURLForRect(_ url: NSURL, _ rect: CGRect) ``` |

Modified [UIGuidedAccessRestrictionStateForIdentifier(_: String) -> UIGuidedAccessRestrictionState](https://developer.apple.com/documentation/uikit/1621153-uiguidedaccessrestrictionstatefo)

|  | Declaration |
| --- | --- |
| From | ``` func UIGuidedAccessRestrictionStateForIdentifier(_ restrictionIdentifier: String!) -> UIGuidedAccessRestrictionState ``` |
| To | ``` func UIGuidedAccessRestrictionStateForIdentifier(_ restrictionIdentifier: String) -> UIGuidedAccessRestrictionState ``` |

Modified [UIImageJPEGRepresentation(_: UIImage, _: CGFloat) -> NSData?](https://developer.apple.com/documentation/uikit/uiimage/1624115-jpegdata)

|  | Declaration |
| --- | --- |
| From | ``` func UIImageJPEGRepresentation(_ image: UIImage!, _ compressionQuality: CGFloat) -> NSData! ``` |
| To | ``` func UIImageJPEGRepresentation(_ image: UIImage, _ compressionQuality: CGFloat) -> NSData? ``` |

Modified [UIImagePNGRepresentation(_: UIImage) -> NSData?](https://developer.apple.com/documentation/uikit/uiimage/1624096-pngdata)

|  | Declaration |
| --- | --- |
| From | ``` func UIImagePNGRepresentation(_ image: UIImage!) -> NSData! ``` |
| To | ``` func UIImagePNGRepresentation(_ image: UIImage) -> NSData? ``` |

Modified [UIImageWriteToSavedPhotosAlbum(_: UIImage, _: AnyObject?, _: Selector, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/uikit/1619125-uiimagewritetosavedphotosalbum)

|  | Declaration |
| --- | --- |
| From | ``` func UIImageWriteToSavedPhotosAlbum(_ image: UIImage!, _ completionTarget: AnyObject!, _ completionSelector: Selector, _ contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func UIImageWriteToSavedPhotosAlbum(_ image: UIImage, _ completionTarget: AnyObject?, _ completionSelector: Selector, _ contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified UIInterfaceOrientationIsLandscape(_: UIInterfaceOrientation) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func UIInterfaceOrientationIsLandscape(_ orientation: UIInterfaceOrientation) -> Bool ``` |
| To | ``` @warn_unused_result func UIInterfaceOrientationIsLandscape(_ orientation: UIInterfaceOrientation) -> Bool ``` |

Modified UIInterfaceOrientationIsPortrait(_: UIInterfaceOrientation) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func UIInterfaceOrientationIsPortrait(_ orientation: UIInterfaceOrientation) -> Bool ``` |
| To | ``` @warn_unused_result func UIInterfaceOrientationIsPortrait(_ orientation: UIInterfaceOrientation) -> Bool ``` |

Modified [UIOffsetFromString(_: String) -> UIOffset](https://developer.apple.com/documentation/foundation/nscoder/1624509-uioffset)

|  | Declaration |
| --- | --- |
| From | ``` func UIOffsetFromString(_ string: String!) -> UIOffset ``` |
| To | ``` func UIOffsetFromString(_ string: String) -> UIOffset ``` |

Modified [UIPasteboardTypeListColor](https://developer.apple.com/documentation/uikit/uipasteboard/1622102-typelistcolor)

|  | Declaration |
| --- | --- |
| From | ``` var UIPasteboardTypeListColor: NSArray! ``` |
| To | ``` var UIPasteboardTypeListColor: NSArray ``` |

Modified [UIPasteboardTypeListImage](https://developer.apple.com/documentation/uikit/uipasteboardtypelistimage)

|  | Declaration |
| --- | --- |
| From | ``` var UIPasteboardTypeListImage: NSArray! ``` |
| To | ``` var UIPasteboardTypeListImage: NSArray ``` |

Modified [UIPasteboardTypeListString](https://developer.apple.com/documentation/uikit/uipasteboardtypeliststring)

|  | Declaration |
| --- | --- |
| From | ``` var UIPasteboardTypeListString: NSArray! ``` |
| To | ``` var UIPasteboardTypeListString: NSArray ``` |

Modified [UIPasteboardTypeListURL](https://developer.apple.com/documentation/uikit/uipasteboard/1622073-typelisturl)

|  | Declaration |
| --- | --- |
| From | ``` var UIPasteboardTypeListURL: NSArray! ``` |
| To | ``` var UIPasteboardTypeListURL: NSArray ``` |

Modified [UIPrinterPickerCompletionHandler](https://developer.apple.com/documentation/uikit/uiprinterpickercompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias UIPrinterPickerCompletionHandler = (UIPrinterPickerController!, Bool, NSError!) -> Void ``` |
| To | ``` typealias UIPrinterPickerCompletionHandler = (UIPrinterPickerController, Bool, NSError?) -> Void ``` |

Modified [UIPrintInteractionCompletionHandler](https://developer.apple.com/documentation/uikit/uiprintinteractioncompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias UIPrintInteractionCompletionHandler = (UIPrintInteractionController!, Bool, NSError!) -> Void ``` |
| To | ``` typealias UIPrintInteractionCompletionHandler = (UIPrintInteractionController, Bool, NSError?) -> Void ``` |

Modified [UISaveVideoAtPathToSavedPhotosAlbum(_: String, _: AnyObject?, _: Selector, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/uikit/1619162-uisavevideoatpathtosavedphotosal)

|  | Declaration |
| --- | --- |
| From | ``` func UISaveVideoAtPathToSavedPhotosAlbum(_ videoPath: String!, _ completionTarget: AnyObject!, _ completionSelector: Selector, _ contextInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func UISaveVideoAtPathToSavedPhotosAlbum(_ videoPath: String, _ completionTarget: AnyObject?, _ completionSelector: Selector, _ contextInfo: UnsafeMutablePointer<Void>) ``` |

Modified [UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(_: String) -> Bool](https://developer.apple.com/documentation/uikit/1619158-uivideoatpathiscompatiblewithsav)

|  | Declaration |
| --- | --- |
| From | ``` func UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(_ videoPath: String!) -> Bool ``` |
| To | ``` func UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(_ videoPath: String) -> Bool ``` |

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
