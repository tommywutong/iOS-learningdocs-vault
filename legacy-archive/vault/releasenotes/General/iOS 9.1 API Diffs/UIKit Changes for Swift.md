---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/UIKit.html
archived_at: '2026-07-18T02:57:11.345304Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# UIKit Changes for Swift

### UIKit

Added [UIApplicationShortcutIconType.Alarm](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypealarm)Added [UIApplicationShortcutIconType.Audio](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypeaudio)Added [UIApplicationShortcutIconType.Bookmark](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypebookmark)Added [UIApplicationShortcutIconType.CapturePhoto](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypecapturephoto)Added [UIApplicationShortcutIconType.CaptureVideo](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypecapturevideo)Added [UIApplicationShortcutIconType.Cloud](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/cloud)Added [UIApplicationShortcutIconType.Confirmation](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/confirmation)Added [UIApplicationShortcutIconType.Contact](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/contact)Added [UIApplicationShortcutIconType.Date](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypedate)Added [UIApplicationShortcutIconType.Favorite](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/favorite)Added [UIApplicationShortcutIconType.Home](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/home)Added [UIApplicationShortcutIconType.Invitation](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/invitation)Added [UIApplicationShortcutIconType.Love](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/love)Added [UIApplicationShortcutIconType.Mail](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypemail)Added [UIApplicationShortcutIconType.MarkLocation](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypemarklocation)Added [UIApplicationShortcutIconType.Message](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypemessage)Added [UIApplicationShortcutIconType.Prohibit](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/prohibit)Added [UIApplicationShortcutIconType.Shuffle](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/shuffle)Added [UIApplicationShortcutIconType.Task](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/task)Added [UIApplicationShortcutIconType.TaskCompleted](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypetaskcompleted)Added [UIApplicationShortcutIconType.Time](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/time)Added [UIApplicationShortcutIconType.Update](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/update)Added [UICollectionView.remembersLastFocusedIndexPath](https://developer.apple.com/documentation/uikit/uicollectionview/1618022-rememberslastfocusedindexpath)Added [UICollectionViewDelegate.collectionView(_: UICollectionView, canFocusItemAtIndexPath: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618013-collectionview)Added [UICollectionViewDelegate.collectionView(_: UICollectionView, didUpdateFocusInContext: UICollectionViewFocusUpdateContext, withAnimationCoordinator: UIFocusAnimationCoordinator)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618081-collectionview)Added [UICollectionViewDelegate.collectionView(_: UICollectionView, shouldUpdateFocusInContext: UICollectionViewFocusUpdateContext) -> Bool](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618072-collectionview)Added [UICollectionViewDelegate.indexPathForPreferredFocusedViewInCollectionView(_: UICollectionView) -> NSIndexPath?](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618066-indexpathforpreferredfocusedview)Added [UICollectionViewFocusUpdateContext](https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext)Added [UICollectionViewFocusUpdateContext.nextFocusedIndexPath](https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext/1618011-nextfocusedindexpath)Added [UICollectionViewFocusUpdateContext.previouslyFocusedIndexPath](https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext/1618077-previouslyfocusedindexpath)Added UIColor.init(colorLiteralRed: Float, green: Float, blue: Float, alpha: Float)Added [UIControlState.Focused](https://developer.apple.com/documentation/uikit/uicontrolstate/uicontrolstatefocused)Added [UIEventType.Presses](https://developer.apple.com/documentation/uikit/uieventtype/uieventtypepresses)Added [UIFocusAnimationCoordinator](https://developer.apple.com/documentation/uikit/uifocusanimationcoordinator)Added [UIFocusAnimationCoordinator.addCoordinatedAnimations(_: (() -> Void)?, completion: (() -> Void)?)](https://developer.apple.com/documentation/uikit/uifocusanimationcoordinator/1619045-addcoordinatedanimations)Added [UIFocusEnvironment](https://developer.apple.com/documentation/uikit/uifocusenvironment)Added [UIFocusEnvironment.didUpdateFocusInContext(_: UIFocusUpdateContext, withAnimationCoordinator: UIFocusAnimationCoordinator)](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616841-didupdatefocusincontext)Added [UIFocusEnvironment.preferredFocusedView](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616830-preferredfocusedview)Added [UIFocusEnvironment.setNeedsFocusUpdate()](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616837-setneedsfocusupdate)Added [UIFocusEnvironment.shouldUpdateFocusInContext(_: UIFocusUpdateContext) -> Bool](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616831-shouldupdatefocusincontext)Added [UIFocusEnvironment.updateFocusIfNeeded()](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616833-updatefocusifneeded)Added [UIFocusGuide](https://developer.apple.com/documentation/uikit/uifocusguide)Added [UIFocusGuide.enabled](https://developer.apple.com/documentation/uikit/uifocusguide/1616838-isenabled)Added [UIFocusGuide.preferredFocusedView](https://developer.apple.com/documentation/uikit/uifocusguide/1616848-preferredfocusedview)Added [UIFocusHeading [struct]](https://developer.apple.com/documentation/uikit/uifocusheading)Added [UIFocusHeading.Down](https://developer.apple.com/documentation/uikit/uifocusheading/uifocusheadingdown)Added UIFocusHeading.init(rawValue: UInt)Added [UIFocusHeading.Left](https://developer.apple.com/documentation/uikit/uifocusheading/uifocusheadingleft)Added [UIFocusHeading.Next](https://developer.apple.com/documentation/uikit/uifocusheading/uifocusheadingnext)Added [UIFocusHeading.Previous](https://developer.apple.com/documentation/uikit/uifocusheading/uifocusheadingprevious)Added [UIFocusHeading.Right](https://developer.apple.com/documentation/uikit/uifocusheading/1616836-right)Added [UIFocusHeading.Up](https://developer.apple.com/documentation/uikit/uifocusheading/uifocusheadingup)Added [UIFocusUpdateContext](https://developer.apple.com/documentation/uikit/uifocusupdatecontext)Added [UIFocusUpdateContext.focusHeading](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/1616834-focusheading)Added [UIFocusUpdateContext.nextFocusedView](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/1616843-nextfocusedview)Added [UIFocusUpdateContext.previouslyFocusedView](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/1616839-previouslyfocusedview)Added [UIGestureRecognizer.allowedPressTypes](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624231-allowedpresstypes)Added [UIGestureRecognizer.allowedTouchTypes](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624223-allowedtouchtypes)Added [UIGestureRecognizerDelegate.gestureRecognizer(_: UIGestureRecognizer, shouldReceivePress: UIPress) -> Bool](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624216-gesturerecognizer)Added UIImage.init(imageLiteral: String)Added [UIPress](https://developer.apple.com/documentation/uikit/uipress)Added [UIPress.force](https://developer.apple.com/documentation/uikit/uipress/1620364-force)Added [UIPress.gestureRecognizers](https://developer.apple.com/documentation/uikit/uipress/1620376-gesturerecognizers)Added [UIPress.phase](https://developer.apple.com/documentation/uikit/uipress/1620367-phase)Added [UIPress.responder](https://developer.apple.com/documentation/uikit/uipress/1620374-responder)Added [UIPress.timestamp](https://developer.apple.com/documentation/uikit/uipress/1620360-timestamp)Added [UIPress.type](https://developer.apple.com/documentation/uikit/uipress/1620370-type)Added [UIPress.window](https://developer.apple.com/documentation/uikit/uipress/1620366-window)Added [UIPressesEvent](https://developer.apple.com/documentation/uikit/uipressesevent)Added [UIPressesEvent.allPresses() -> Set<UIPress>](https://developer.apple.com/documentation/uikit/uipressesevent/1623575-allpresses)Added [UIPressesEvent.pressesForGestureRecognizer(_: UIGestureRecognizer) -> Set<UIPress>](https://developer.apple.com/documentation/uikit/uipressesevent/1623574-pressesforgesturerecognizer)Added [UIPressPhase [enum]](https://developer.apple.com/documentation/uikit/uipressphase)Added [UIPressPhase.Began](https://developer.apple.com/documentation/uikit/uipressphase/uipressphasebegan)Added [UIPressPhase.Cancelled](https://developer.apple.com/documentation/uikit/uipress/phase/cancelled)Added [UIPressPhase.Changed](https://developer.apple.com/documentation/uikit/uipressphase/uipressphasechanged)Added [UIPressPhase.Ended](https://developer.apple.com/documentation/uikit/uipressphase/uipressphaseended)Added [UIPressPhase.Stationary](https://developer.apple.com/documentation/uikit/uipressphase/uipressphasestationary)Added [UIPressType [enum]](https://developer.apple.com/documentation/uikit/uipresstype)Added [UIPressType.DownArrow](https://developer.apple.com/documentation/uikit/uipresstype/uipresstypedownarrow)Added [UIPressType.LeftArrow](https://developer.apple.com/documentation/uikit/uipress/presstype/leftarrow)Added [UIPressType.Menu](https://developer.apple.com/documentation/uikit/uipress/presstype/menu)Added [UIPressType.PlayPause](https://developer.apple.com/documentation/uikit/uipress/presstype/playpause)Added [UIPressType.RightArrow](https://developer.apple.com/documentation/uikit/uipresstype/uipresstyperightarrow)Added [UIPressType.Select](https://developer.apple.com/documentation/uikit/uipress/presstype/select)Added [UIPressType.UpArrow](https://developer.apple.com/documentation/uikit/uipress/presstype/uparrow)Added [UIResponder.pressesBegan(_: Set<UIPress>, withEvent: UIPressesEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621134-pressesbegan)Added [UIResponder.pressesCancelled(_: Set<UIPress>, withEvent: UIPressesEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621148-pressescancelled)Added [UIResponder.pressesChanged(_: Set<UIPress>, withEvent: UIPressesEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621150-presseschanged)Added [UIResponder.pressesEnded(_: Set<UIPress>, withEvent: UIPressesEvent?)](https://developer.apple.com/documentation/uikit/uiresponder/1621128-pressesended)Added [UIResponder.touchesEstimatedPropertiesUpdated(_: Set<NSObject>)](https://developer.apple.com/documentation/uikit/uiresponder/1621147-touchesestimatedpropertiesupdate)Added [UIScreen.focusedView](https://developer.apple.com/documentation/uikit/uiscreen/1617831-focusedview)Added [UIScreen.supportsFocus](https://developer.apple.com/documentation/uikit/uiscreen/1617816-supportsfocus)Added [UISearchContainerViewController](https://developer.apple.com/documentation/uikit/uisearchcontainerviewcontroller)Added [UISearchContainerViewController.init(searchController: UISearchController)](https://developer.apple.com/documentation/uikit/uisearchcontainerviewcontroller/1615746-init)Added [UISearchContainerViewController.searchController](https://developer.apple.com/documentation/uikit/uisearchcontainerviewcontroller/1615748-searchcontroller)Added [UISearchController.obscuresBackgroundDuringPresentation](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618656-obscuresbackgroundduringpresenta)Added [UITableView.remembersLastFocusedIndexPath](https://developer.apple.com/documentation/uikit/uitableview/1614858-rememberslastfocusedindexpath)Added [UITableViewCell.focusStyle](https://developer.apple.com/documentation/uikit/uitableviewcell/1623248-focusstyle)Added [UITableViewCellFocusStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewcell/focusstyle)Added [UITableViewCellFocusStyle.Custom](https://developer.apple.com/documentation/uikit/uitableviewcell/focusstyle/custom)Added [UITableViewCellFocusStyle.Default](https://developer.apple.com/documentation/uikit/uitableviewcellfocusstyle/uitableviewcellfocusstyledefault)Added [UITableViewDelegate.indexPathForPreferredFocusedViewInTableView(_: UITableView) -> NSIndexPath?](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614929-indexpathforpreferredfocusedview)Added [UITableViewDelegate.tableView(_: UITableView, canFocusRowAtIndexPath: NSIndexPath) -> Bool](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614973-tableview)Added [UITableViewDelegate.tableView(_: UITableView, didUpdateFocusInContext: UITableViewFocusUpdateContext, withAnimationCoordinator: UIFocusAnimationCoordinator)](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614945-tableview)Added [UITableViewDelegate.tableView(_: UITableView, shouldUpdateFocusInContext: UITableViewFocusUpdateContext) -> Bool](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614949-tableview)Added [UITableViewFocusUpdateContext](https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext)Added [UITableViewFocusUpdateContext.nextFocusedIndexPath](https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext/1614919-nextfocusedindexpath)Added [UITableViewFocusUpdateContext.previouslyFocusedIndexPath](https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext/1614930-previouslyfocusedindexpath)Added [UITouch.altitudeAngle](https://developer.apple.com/documentation/uikit/uitouch/1618118-altitudeangle)Added [UITouch.azimuthAngleInView(_: UIView?) -> CGFloat](https://developer.apple.com/documentation/uikit/uitouch/1618131-azimuthangle)Added [UITouch.azimuthUnitVectorInView(_: UIView?) -> CGVector](https://developer.apple.com/documentation/uikit/uitouch/1618133-azimuthunitvector)Added [UITouch.estimatedProperties](https://developer.apple.com/documentation/uikit/uitouch/1618130-estimatedproperties)Added [UITouch.estimatedPropertiesExpectingUpdates](https://developer.apple.com/documentation/uikit/uitouch/1618119-estimatedpropertiesexpectingupda)Added [UITouch.estimationUpdateIndex](https://developer.apple.com/documentation/uikit/uitouch/1618137-estimationupdateindex)Added [UITouch.preciseLocationInView(_: UIView?) -> CGPoint](https://developer.apple.com/documentation/uikit/uitouch/1618134-preciselocation)Added [UITouch.precisePreviousLocationInView(_: UIView?) -> CGPoint](https://developer.apple.com/documentation/uikit/uitouch/1618129-precisepreviouslocationinview)Added [UITouch.type](https://developer.apple.com/documentation/uikit/uitouch/1618143-type)Added [UITouchProperties [struct]](https://developer.apple.com/documentation/uikit/uitouchproperties)Added [UITouchProperties.Altitude](https://developer.apple.com/documentation/uikit/uitouchproperties/uitouchpropertyaltitude)Added [UITouchProperties.Azimuth](https://developer.apple.com/documentation/uikit/uitouchproperties/uitouchpropertyazimuth)Added [UITouchProperties.Force](https://developer.apple.com/documentation/uikit/uitouchproperties/uitouchpropertyforce)Added UITouchProperties.init(rawValue: Int)Added [UITouchProperties.Location](https://developer.apple.com/documentation/uikit/uitouchproperties/uitouchpropertylocation)Added [UITouchType [enum]](https://developer.apple.com/documentation/uikit/uitouch/touchtype)Added [UITouchType.Direct](https://developer.apple.com/documentation/uikit/uitouch/touchtype/direct)Added [UITouchType.Indirect](https://developer.apple.com/documentation/uikit/uitouchtype/uitouchtypeindirect)Added [UITouchType.Stylus](https://developer.apple.com/documentation/uikit/uitouch/touchtype/1618124-stylus)Added [UIUserInterfaceIdiom.TV](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom/tv)Added [UIView.canBecomeFocused() -> Bool](https://developer.apple.com/documentation/uikit/uiview/1622584-canbecomefocused)Added [UIView.focused](https://developer.apple.com/documentation/uikit/uiview/1622565-isfocused)Added [UIImagePickerControllerLivePhoto](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerlivephoto)Modified [NSControlCharacterAction [enum]](https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSDataAsset](https://developer.apple.com/documentation/uikit/nsdataasset)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [NSFileProviderExtension](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSGlyphProperty [enum]](https://developer.apple.com/documentation/uikit/nsglyphproperty)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSLayoutAnchor](https://developer.apple.com/documentation/uikit/nslayoutanchor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSLayoutAttribute [enum]](https://developer.apple.com/documentation/appkit/nslayoutattribute)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSLayoutConstraint](https://developer.apple.com/documentation/uikit/nslayoutconstraint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSLayoutDimension](https://developer.apple.com/documentation/uikit/nslayoutdimension)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [NSLayoutRelation [enum]](https://developer.apple.com/documentation/uikit/nslayoutconstraint/relation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSLayoutXAxisAnchor](https://developer.apple.com/documentation/uikit/nslayoutxaxisanchor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSLayoutYAxisAnchor](https://developer.apple.com/documentation/uikit/nslayoutyaxisanchor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSLineBreakMode [enum]](https://developer.apple.com/documentation/uikit/nslinebreakmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSMutableParagraphStyle](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSParagraphStyle](https://developer.apple.com/documentation/uikit/nsparagraphstyle)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSParagraphStyle : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     class func defaultParagraphStyle() -> NSParagraphStyle     class func defaultWritingDirectionForLanguage(_ languageName: String?) -> NSWritingDirection     var lineSpacing: CGFloat { get }     var paragraphSpacing: CGFloat { get }     var alignment: NSTextAlignment { get }     var headIndent: CGFloat { get }     var tailIndent: CGFloat { get }     var firstLineHeadIndent: CGFloat { get }     var minimumLineHeight: CGFloat { get }     var maximumLineHeight: CGFloat { get }     var lineBreakMode: NSLineBreakMode { get }     var baseWritingDirection: NSWritingDirection { get }     var lineHeightMultiple: CGFloat { get }     var paragraphSpacingBefore: CGFloat { get }     var hyphenationFactor: Float { get }     var tabStops: [NSTextTab] { get }     var defaultTabInterval: CGFloat { get }     var allowsDefaultTighteningForTruncation: Bool { get } } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class NSParagraphStyle : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     class func defaultParagraphStyle() -> NSParagraphStyle     class func defaultWritingDirectionForLanguage(_ languageName: String?) -> NSWritingDirection     var lineSpacing: CGFloat { get }     var paragraphSpacing: CGFloat { get }     var alignment: NSTextAlignment { get }     var headIndent: CGFloat { get }     var tailIndent: CGFloat { get }     var firstLineHeadIndent: CGFloat { get }     var minimumLineHeight: CGFloat { get }     var maximumLineHeight: CGFloat { get }     var lineBreakMode: NSLineBreakMode { get }     var baseWritingDirection: NSWritingDirection { get }     var lineHeightMultiple: CGFloat { get }     var paragraphSpacingBefore: CGFloat { get }     var hyphenationFactor: Float { get }     var tabStops: [NSTextTab] { get }     var defaultTabInterval: CGFloat { get }     var allowsDefaultTighteningForTruncation: Bool { get } } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [NSShadow](https://developer.apple.com/documentation/uikit/nsshadow)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSStringDrawingContext](https://developer.apple.com/documentation/appkit/nsstringdrawingcontext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSTextAlignment [enum]](https://developer.apple.com/documentation/uikit/nstextalignment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSTextAttachment](https://developer.apple.com/documentation/uikit/nstextattachment)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSObjectProtocol, NSTextAttachmentContainer |
| To | NSCoding, NSTextAttachmentContainer |

Modified [NSTextContainer](https://developer.apple.com/documentation/uikit/nstextcontainer)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSTextLayoutOrientationProvider |
| To | NSCoding, NSTextLayoutOrientationProvider |

Modified [NSTextLayoutOrientation [enum]](https://developer.apple.com/documentation/appkit/nstextlayoutorientation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSTextStorage](https://developer.apple.com/documentation/appkit/nstextstorage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSTextTab](https://developer.apple.com/documentation/uikit/nstexttab)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSTextWritingDirection [enum]](https://developer.apple.com/documentation/uikit/nstextwritingdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSUnderlineStyle [enum]](https://developer.apple.com/documentation/uikit/nsunderlinestyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSWritingDirection [enum]](https://developer.apple.com/documentation/appkit/nswritingdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSWritingDirectionFormatType [enum]](https://developer.apple.com/documentation/uikit/nswritingdirectionformattype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIAccessibilityCustomAction](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIAccessibilityElement](https://developer.apple.com/documentation/uikit/uiaccessibilityelement)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, UIAccessibilityIdentification |
| To | UIAccessibilityIdentification |

Modified [UIAccessibilityNavigationStyle [enum]](https://developer.apple.com/documentation/uikit/uiaccessibilitynavigationstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIAccessibilityScrollDirection [enum]](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilityscrolldirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIAccessibilityZoomType [enum]](https://developer.apple.com/documentation/uikit/uiaccessibilityzoomtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIActionSheet](https://developer.apple.com/documentation/uikit/uiactionsheet)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIActionSheetStyle [enum]](https://developer.apple.com/documentation/uikit/uiactionsheetstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIActivity](https://developer.apple.com/documentation/uikit/uiactivity)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIActivityCategory [enum]](https://developer.apple.com/documentation/uikit/uiactivity/category)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIActivityIndicatorView : UIView {     init(activityIndicatorStyle style: UIActivityIndicatorViewStyle)     init(frame frame: CGRect)     init(coder coder: NSCoder)     var activityIndicatorViewStyle: UIActivityIndicatorViewStyle     var hidesWhenStopped: Bool     var color: UIColor?     func startAnimating()     func stopAnimating()     func isAnimating() -> Bool } ``` | AnyObject, NSCoding |
| To | ``` class UIActivityIndicatorView : UIView, NSCoding {     init(activityIndicatorStyle style: UIActivityIndicatorViewStyle)     init(frame frame: CGRect)     init(coder coder: NSCoder)     var activityIndicatorViewStyle: UIActivityIndicatorViewStyle     var hidesWhenStopped: Bool     var color: UIColor?     func startAnimating()     func stopAnimating()     func isAnimating() -> Bool } ``` | NSCoding |

Modified [UIActivityIndicatorViewStyle [enum]](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/style)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIActivityItemProvider](https://developer.apple.com/documentation/uikit/uiactivityitemprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, UIActivityItemSource |
| To | UIActivityItemSource |

Modified [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIAlertAction](https://developer.apple.com/documentation/uikit/uialertaction)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [UIAlertActionStyle [enum]](https://developer.apple.com/documentation/uikit/uialertactionstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIAlertControllerStyle [enum]](https://developer.apple.com/documentation/uikit/uialertcontrollerstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIAlertView](https://developer.apple.com/documentation/uikit/uialertview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIAlertViewStyle [enum]](https://developer.apple.com/documentation/uikit/uialertviewstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIApplication](https://developer.apple.com/documentation/uikit/uiapplication)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIApplicationShortcutIcon](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [UIApplicationShortcutIconType [enum]](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum UIApplicationShortcutIconType : Int {     case Compose     case Play     case Pause     case Add     case Location     case Search     case Share } ``` | Equatable, Hashable, RawRepresentable |
| To | ``` enum UIApplicationShortcutIconType : Int {     case Compose     case Play     case Pause     case Add     case Location     case Search     case Share     case Prohibit     case Contact     case Home     case MarkLocation     case Favorite     case Love     case Cloud     case Invitation     case Confirmation     case Mail     case Message     case Date     case Time     case CapturePhoto     case CaptureVideo     case Task     case TaskCompleted     case Alarm     case Bookmark     case Shuffle     case Audio     case Update } ``` | -- |

Modified [UIApplicationShortcutItem](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying |

Modified [UIApplicationState [enum]](https://developer.apple.com/documentation/uikit/uiapplicationstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIAttachmentBehavior](https://developer.apple.com/documentation/uikit/uiattachmentbehavior)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIAttachmentBehaviorType [enum]](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/attachmenttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIBackgroundFetchResult [enum]](https://developer.apple.com/documentation/uikit/uibackgroundfetchresult)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIBackgroundRefreshStatus [enum]](https://developer.apple.com/documentation/uikit/uibackgroundrefreshstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIBarButtonItem : UIBarItem {     init()     init?(coder aDecoder: NSCoder)     convenience init(image image: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     convenience init(image image: UIImage?, landscapeImagePhone landscapeImagePhone: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     convenience init(title title: String?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     convenience init(barButtonSystemItem systemItem: UIBarButtonSystemItem, target target: AnyObject?, action action: Selector)     convenience init(customView customView: UIView)     var style: UIBarButtonItemStyle     var width: CGFloat     var possibleTitles: Set<String>?     var customView: UIView?     var action: Selector     weak var target: AnyObject?     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, style style: UIBarButtonItemStyle, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, style style: UIBarButtonItemStyle, barMetrics barMetrics: UIBarMetrics) -> UIImage?     var tintColor: UIColor?     func setBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func backgroundVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat     func setTitlePositionAdjustment(_ adjustment: UIOffset, forBarMetrics barMetrics: UIBarMetrics)     func titlePositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> UIOffset     func setBackButtonBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backButtonBackgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackButtonTitlePositionAdjustment(_ adjustment: UIOffset, forBarMetrics barMetrics: UIBarMetrics)     func backButtonTitlePositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> UIOffset     func setBackButtonBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func backButtonBackgroundVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat } extension UIBarButtonItem {     weak var buttonGroup: UIBarButtonItemGroup? { get } } ``` | AnyObject, NSCoding |
| To | ``` class UIBarButtonItem : UIBarItem, NSCoding {     init()     init?(coder aDecoder: NSCoder)     convenience init(image image: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     convenience init(image image: UIImage?, landscapeImagePhone landscapeImagePhone: UIImage?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     convenience init(title title: String?, style style: UIBarButtonItemStyle, target target: AnyObject?, action action: Selector)     convenience init(barButtonSystemItem systemItem: UIBarButtonSystemItem, target target: AnyObject?, action action: Selector)     convenience init(customView customView: UIView)     var style: UIBarButtonItemStyle     var width: CGFloat     var possibleTitles: Set<String>?     var customView: UIView?     var action: Selector     weak var target: AnyObject?     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, style style: UIBarButtonItemStyle, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, style style: UIBarButtonItemStyle, barMetrics barMetrics: UIBarMetrics) -> UIImage?     var tintColor: UIColor?     func setBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func backgroundVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat     func setTitlePositionAdjustment(_ adjustment: UIOffset, forBarMetrics barMetrics: UIBarMetrics)     func titlePositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> UIOffset     func setBackButtonBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backButtonBackgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackButtonTitlePositionAdjustment(_ adjustment: UIOffset, forBarMetrics barMetrics: UIBarMetrics)     func backButtonTitlePositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> UIOffset     func setBackButtonBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func backButtonBackgroundVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat } extension UIBarButtonItem {     weak var buttonGroup: UIBarButtonItemGroup? { get } } ``` | NSCoding |

Modified [UIBarButtonItemGroup](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [UIBarButtonItemStyle [enum]](https://developer.apple.com/documentation/uikit/uibarbuttonitemstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIBarButtonSystemItem [enum]](https://developer.apple.com/documentation/uikit/uibarbuttonitem/systemitem)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIBarItem](https://developer.apple.com/documentation/uikit/uibaritem)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSObjectProtocol, UIAccessibilityIdentification, UIAppearance |
| To | NSCoding, UIAccessibilityIdentification, UIAppearance |

Modified [UIBarMetrics [enum]](https://developer.apple.com/documentation/uikit/uibarmetrics)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIBarPosition [enum]](https://developer.apple.com/documentation/uikit/uibarposition)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIBarStyle [enum]](https://developer.apple.com/documentation/uikit/uibarstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIBaselineAdjustment [enum]](https://developer.apple.com/documentation/uikit/uibaselineadjustment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIBezierPath](https://developer.apple.com/documentation/uikit/uibezierpath)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [UIBlurEffect](https://developer.apple.com/documentation/uikit/uiblureffect)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIBlurEffectStyle [enum]](https://developer.apple.com/documentation/uikit/uiblureffect/style)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIButton](https://developer.apple.com/documentation/uikit/uibutton)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIButton : UIControl {     convenience init(type buttonType: UIButtonType)     class func buttonWithType(_ buttonType: UIButtonType) -> Self     var contentEdgeInsets: UIEdgeInsets     var titleEdgeInsets: UIEdgeInsets     var reversesTitleShadowWhenHighlighted: Bool     var imageEdgeInsets: UIEdgeInsets     var adjustsImageWhenHighlighted: Bool     var adjustsImageWhenDisabled: Bool     var showsTouchWhenHighlighted: Bool     var tintColor: UIColor!     var buttonType: UIButtonType { get }     func setTitle(_ title: String?, forState state: UIControlState)     func setTitleColor(_ color: UIColor?, forState state: UIControlState)     func setTitleShadowColor(_ color: UIColor?, forState state: UIControlState)     func setImage(_ image: UIImage?, forState state: UIControlState)     func setBackgroundImage(_ image: UIImage?, forState state: UIControlState)     func setAttributedTitle(_ title: NSAttributedString?, forState state: UIControlState)     func titleForState(_ state: UIControlState) -> String?     func titleColorForState(_ state: UIControlState) -> UIColor?     func titleShadowColorForState(_ state: UIControlState) -> UIColor?     func imageForState(_ state: UIControlState) -> UIImage?     func backgroundImageForState(_ state: UIControlState) -> UIImage?     func attributedTitleForState(_ state: UIControlState) -> NSAttributedString?     var currentTitle: String? { get }     var currentTitleColor: UIColor { get }     var currentTitleShadowColor: UIColor? { get }     var currentImage: UIImage? { get }     var currentBackgroundImage: UIImage? { get }     var currentAttributedTitle: NSAttributedString? { get }     var titleLabel: UILabel? { get }     var imageView: UIImageView? { get }     func backgroundRectForBounds(_ bounds: CGRect) -> CGRect     func contentRectForBounds(_ bounds: CGRect) -> CGRect     func titleRectForContentRect(_ contentRect: CGRect) -> CGRect     func imageRectForContentRect(_ contentRect: CGRect) -> CGRect } extension UIButton {     var font: UIFont     var lineBreakMode: NSLineBreakMode     var titleShadowOffset: CGSize } ``` | AnyObject, NSCoding |
| To | ``` class UIButton : UIControl, NSCoding {     convenience init(type buttonType: UIButtonType)     class func buttonWithType(_ buttonType: UIButtonType) -> Self     var contentEdgeInsets: UIEdgeInsets     var titleEdgeInsets: UIEdgeInsets     var reversesTitleShadowWhenHighlighted: Bool     var imageEdgeInsets: UIEdgeInsets     var adjustsImageWhenHighlighted: Bool     var adjustsImageWhenDisabled: Bool     var showsTouchWhenHighlighted: Bool     var tintColor: UIColor!     var buttonType: UIButtonType { get }     func setTitle(_ title: String?, forState state: UIControlState)     func setTitleColor(_ color: UIColor?, forState state: UIControlState)     func setTitleShadowColor(_ color: UIColor?, forState state: UIControlState)     func setImage(_ image: UIImage?, forState state: UIControlState)     func setBackgroundImage(_ image: UIImage?, forState state: UIControlState)     func setAttributedTitle(_ title: NSAttributedString?, forState state: UIControlState)     func titleForState(_ state: UIControlState) -> String?     func titleColorForState(_ state: UIControlState) -> UIColor?     func titleShadowColorForState(_ state: UIControlState) -> UIColor?     func imageForState(_ state: UIControlState) -> UIImage?     func backgroundImageForState(_ state: UIControlState) -> UIImage?     func attributedTitleForState(_ state: UIControlState) -> NSAttributedString?     var currentTitle: String? { get }     var currentTitleColor: UIColor { get }     var currentTitleShadowColor: UIColor? { get }     var currentImage: UIImage? { get }     var currentBackgroundImage: UIImage? { get }     var currentAttributedTitle: NSAttributedString? { get }     var titleLabel: UILabel? { get }     var imageView: UIImageView? { get }     func backgroundRectForBounds(_ bounds: CGRect) -> CGRect     func contentRectForBounds(_ bounds: CGRect) -> CGRect     func titleRectForContentRect(_ contentRect: CGRect) -> CGRect     func imageRectForContentRect(_ contentRect: CGRect) -> CGRect } extension UIButton {     var font: UIFont     var lineBreakMode: NSLineBreakMode     var titleShadowOffset: CGSize } ``` | NSCoding |

Modified [UIButtonType [enum]](https://developer.apple.com/documentation/uikit/uibutton/buttontype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UICollectionElementCategory [enum]](https://developer.apple.com/documentation/uikit/uicollectionview/elementcategory)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UICollectionReusableView](https://developer.apple.com/documentation/uikit/uicollectionreusableview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UICollectionUpdateAction [enum]](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/action)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UICollectionView : UIScrollView {     init(frame frame: CGRect, collectionViewLayout layout: UICollectionViewLayout)     init?(coder aDecoder: NSCoder)     var collectionViewLayout: UICollectionViewLayout     weak var delegate: UICollectionViewDelegate?     weak var dataSource: UICollectionViewDataSource?     var backgroundView: UIView?     func registerClass(_ cellClass: AnyClass?, forCellWithReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forCellWithReuseIdentifier identifier: String)     func registerClass(_ viewClass: AnyClass?, forSupplementaryViewOfKind elementKind: String, withReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forSupplementaryViewOfKind kind: String, withReuseIdentifier identifier: String)     func dequeueReusableCellWithReuseIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath) -> UICollectionViewCell     func dequeueReusableSupplementaryViewOfKind(_ elementKind: String, withReuseIdentifier identifier: String, forIndexPath indexPath: NSIndexPath) -> UICollectionReusableView     var allowsSelection: Bool     var allowsMultipleSelection: Bool     func indexPathsForSelectedItems() -> [NSIndexPath]?     func selectItemAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool, scrollPosition scrollPosition: UICollectionViewScrollPosition)     func deselectItemAtIndexPath(_ indexPath: NSIndexPath, animated animated: Bool)     func reloadData()     func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated animated: Bool)     func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated animated: Bool, completion completion: ((Bool) -> Void)?)     func startInteractiveTransitionToCollectionViewLayout(_ layout: UICollectionViewLayout, completion completion: UICollectionViewLayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout     func finishInteractiveTransition()     func cancelInteractiveTransition()     func numberOfSections() -> Int     func numberOfItemsInSection(_ section: Int) -> Int     func layoutAttributesForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func layoutAttributesForSupplementaryElementOfKind(_ kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func indexPathForItemAtPoint(_ point: CGPoint) -> NSIndexPath?     func indexPathForCell(_ cell: UICollectionViewCell) -> NSIndexPath?     func cellForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewCell?     func visibleCells() -> [UICollectionViewCell]     func indexPathsForVisibleItems() -> [NSIndexPath]     func supplementaryViewForElementKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionReusableView     func visibleSupplementaryViewsOfKind(_ elementKind: String) -> [UICollectionReusableView]     func indexPathsForVisibleSupplementaryElementsOfKind(_ elementKind: String) -> [NSIndexPath]     func scrollToItemAtIndexPath(_ indexPath: NSIndexPath, atScrollPosition scrollPosition: UICollectionViewScrollPosition, animated animated: Bool)     func insertSections(_ sections: NSIndexSet)     func deleteSections(_ sections: NSIndexSet)     func reloadSections(_ sections: NSIndexSet)     func moveSection(_ section: Int, toSection newSection: Int)     func insertItemsAtIndexPaths(_ indexPaths: [NSIndexPath])     func deleteItemsAtIndexPaths(_ indexPaths: [NSIndexPath])     func reloadItemsAtIndexPaths(_ indexPaths: [NSIndexPath])     func moveItemAtIndexPath(_ indexPath: NSIndexPath, toIndexPath newIndexPath: NSIndexPath)     func performBatchUpdates(_ updates: (() -> Void)?, completion completion: ((Bool) -> Void)?)     func beginInteractiveMovementForItemAtIndexPath(_ indexPath: NSIndexPath) -> Bool     func updateInteractiveMovementTargetPosition(_ targetPosition: CGPoint)     func endInteractiveMovement()     func cancelInteractiveMovement() } ``` | AnyObject |
| To | ``` class UICollectionView : UIScrollView {     init(frame frame: CGRect, collectionViewLayout layout: UICollectionViewLayout)     init?(coder aDecoder: NSCoder)     var collectionViewLayout: UICollectionViewLayout     weak var delegate: UICollectionViewDelegate?     weak var dataSource: UICollectionViewDataSource?     var backgroundView: UIView?     func registerClass(_ cellClass: AnyClass?, forCellWithReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forCellWithReuseIdentifier identifier: String)     func registerClass(_ viewClass: AnyClass?, forSupplementaryViewOfKind elementKind: String, withReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forSupplementaryViewOfKind kind: String, withReuseIdentifier identifier: String)     func dequeueReusableCellWithReuseIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath) -> UICollectionViewCell     func dequeueReusableSupplementaryViewOfKind(_ elementKind: String, withReuseIdentifier identifier: String, forIndexPath indexPath: NSIndexPath) -> UICollectionReusableView     var allowsSelection: Bool     var allowsMultipleSelection: Bool     func indexPathsForSelectedItems() -> [NSIndexPath]?     func selectItemAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool, scrollPosition scrollPosition: UICollectionViewScrollPosition)     func deselectItemAtIndexPath(_ indexPath: NSIndexPath, animated animated: Bool)     func reloadData()     func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated animated: Bool)     func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated animated: Bool, completion completion: ((Bool) -> Void)?)     func startInteractiveTransitionToCollectionViewLayout(_ layout: UICollectionViewLayout, completion completion: UICollectionViewLayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout     func finishInteractiveTransition()     func cancelInteractiveTransition()     func numberOfSections() -> Int     func numberOfItemsInSection(_ section: Int) -> Int     func layoutAttributesForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func layoutAttributesForSupplementaryElementOfKind(_ kind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionViewLayoutAttributes?     func indexPathForItemAtPoint(_ point: CGPoint) -> NSIndexPath?     func indexPathForCell(_ cell: UICollectionViewCell) -> NSIndexPath?     func cellForItemAtIndexPath(_ indexPath: NSIndexPath) -> UICollectionViewCell?     func visibleCells() -> [UICollectionViewCell]     func indexPathsForVisibleItems() -> [NSIndexPath]     func supplementaryViewForElementKind(_ elementKind: String, atIndexPath indexPath: NSIndexPath) -> UICollectionReusableView     func visibleSupplementaryViewsOfKind(_ elementKind: String) -> [UICollectionReusableView]     func indexPathsForVisibleSupplementaryElementsOfKind(_ elementKind: String) -> [NSIndexPath]     func scrollToItemAtIndexPath(_ indexPath: NSIndexPath, atScrollPosition scrollPosition: UICollectionViewScrollPosition, animated animated: Bool)     func insertSections(_ sections: NSIndexSet)     func deleteSections(_ sections: NSIndexSet)     func reloadSections(_ sections: NSIndexSet)     func moveSection(_ section: Int, toSection newSection: Int)     func insertItemsAtIndexPaths(_ indexPaths: [NSIndexPath])     func deleteItemsAtIndexPaths(_ indexPaths: [NSIndexPath])     func reloadItemsAtIndexPaths(_ indexPaths: [NSIndexPath])     func moveItemAtIndexPath(_ indexPath: NSIndexPath, toIndexPath newIndexPath: NSIndexPath)     func performBatchUpdates(_ updates: (() -> Void)?, completion completion: ((Bool) -> Void)?)     func beginInteractiveMovementForItemAtIndexPath(_ indexPath: NSIndexPath) -> Bool     func updateInteractiveMovementTargetPosition(_ targetPosition: CGPoint)     func endInteractiveMovement()     func cancelInteractiveMovement()     var remembersLastFocusedIndexPath: Bool } ``` | -- |

Modified [UICollectionViewCell](https://developer.apple.com/documentation/uikit/uicollectionviewcell)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UICollectionViewController](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UICollectionViewController : UIViewController, UICollectionViewDelegate, UIScrollViewDelegate, UICollectionViewDataSource {     init(collectionViewLayout layout: UICollectionViewLayout)     init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     init?(coder aDecoder: NSCoder)     var collectionView: UICollectionView?     var clearsSelectionOnViewWillAppear: Bool     var useLayoutToLayoutNavigationTransitions: Bool     var collectionViewLayout: UICollectionViewLayout { get }     var installsStandardGestureForInteractiveMovement: Bool } ``` | AnyObject, NSObjectProtocol, UICollectionViewDataSource, UICollectionViewDelegate, UIScrollViewDelegate |
| To | ``` class UICollectionViewController : UIViewController, UICollectionViewDelegate, UICollectionViewDataSource {     init(collectionViewLayout layout: UICollectionViewLayout)     init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     init?(coder aDecoder: NSCoder)     var collectionView: UICollectionView?     var clearsSelectionOnViewWillAppear: Bool     var useLayoutToLayoutNavigationTransitions: Bool     var collectionViewLayout: UICollectionViewLayout { get }     var installsStandardGestureForInteractiveMovement: Bool } ``` | UICollectionViewDataSource, UICollectionViewDelegate |

Modified [UICollectionViewDelegate](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UICollectionViewDelegate : UIScrollViewDelegate, NSObjectProtocol {     optional func collectionView(_ collectionView: UICollectionView, shouldHighlightItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, didHighlightItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didUnhighlightItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, shouldSelectItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, shouldDeselectItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, didSelectItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didDeselectItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, willDisplayCell cell: UICollectionViewCell, forItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, willDisplaySupplementaryView view: UICollectionReusableView, forElementKind elementKind: String, atIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didEndDisplayingCell cell: UICollectionViewCell, forItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didEndDisplayingSupplementaryView view: UICollectionReusableView, forElementOfKind elementKind: String, atIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, shouldShowMenuForItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, canPerformAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) -> Bool     optional func collectionView(_ collectionView: UICollectionView, performAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?)     optional func collectionView(_ collectionView: UICollectionView, transitionLayoutForOldLayout fromLayout: UICollectionViewLayout, newLayout toLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout     optional func collectionView(_ collectionView: UICollectionView, targetIndexPathForMoveFromItemAtIndexPath originalIndexPath: NSIndexPath, toProposedIndexPath proposedIndexPath: NSIndexPath) -> NSIndexPath     optional func collectionView(_ collectionView: UICollectionView, targetContentOffsetForProposedContentOffset proposedContentOffset: CGPoint) -> CGPoint } ``` | NSObjectProtocol, UIScrollViewDelegate |
| To | ``` protocol UICollectionViewDelegate : UIScrollViewDelegate {     optional func collectionView(_ collectionView: UICollectionView, shouldHighlightItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, didHighlightItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didUnhighlightItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, shouldSelectItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, shouldDeselectItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, didSelectItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didDeselectItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, willDisplayCell cell: UICollectionViewCell, forItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, willDisplaySupplementaryView view: UICollectionReusableView, forElementKind elementKind: String, atIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didEndDisplayingCell cell: UICollectionViewCell, forItemAtIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, didEndDisplayingSupplementaryView view: UICollectionReusableView, forElementOfKind elementKind: String, atIndexPath indexPath: NSIndexPath)     optional func collectionView(_ collectionView: UICollectionView, shouldShowMenuForItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, canPerformAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) -> Bool     optional func collectionView(_ collectionView: UICollectionView, performAction action: Selector, forItemAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?)     optional func collectionView(_ collectionView: UICollectionView, transitionLayoutForOldLayout fromLayout: UICollectionViewLayout, newLayout toLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout     optional func collectionView(_ collectionView: UICollectionView, canFocusItemAtIndexPath indexPath: NSIndexPath) -> Bool     optional func collectionView(_ collectionView: UICollectionView, shouldUpdateFocusInContext context: UICollectionViewFocusUpdateContext) -> Bool     optional func collectionView(_ collectionView: UICollectionView, didUpdateFocusInContext context: UICollectionViewFocusUpdateContext, withAnimationCoordinator coordinator: UIFocusAnimationCoordinator)     optional func indexPathForPreferredFocusedViewInCollectionView(_ collectionView: UICollectionView) -> NSIndexPath?     optional func collectionView(_ collectionView: UICollectionView, targetIndexPathForMoveFromItemAtIndexPath originalIndexPath: NSIndexPath, toProposedIndexPath proposedIndexPath: NSIndexPath) -> NSIndexPath     optional func collectionView(_ collectionView: UICollectionView, targetContentOffsetForProposedContentOffset proposedContentOffset: CGPoint) -> CGPoint } ``` | UIScrollViewDelegate |

Modified [UICollectionViewDelegateFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UICollectionViewDelegateFlowLayout : UICollectionViewDelegate, UIScrollViewDelegate, NSObjectProtocol {     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAtIndexPath indexPath: NSIndexPath) -> CGSize     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, insetForSectionAtIndex section: Int) -> UIEdgeInsets     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAtIndex section: Int) -> CGFloat     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumInteritemSpacingForSectionAtIndex section: Int) -> CGFloat     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, referenceSizeForHeaderInSection section: Int) -> CGSize     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, referenceSizeForFooterInSection section: Int) -> CGSize } ``` | NSObjectProtocol, UICollectionViewDelegate, UIScrollViewDelegate |
| To | ``` protocol UICollectionViewDelegateFlowLayout : UICollectionViewDelegate {     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAtIndexPath indexPath: NSIndexPath) -> CGSize     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, insetForSectionAtIndex section: Int) -> UIEdgeInsets     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAtIndex section: Int) -> CGFloat     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumInteritemSpacingForSectionAtIndex section: Int) -> CGFloat     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, referenceSizeForHeaderInSection section: Int) -> CGSize     optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, referenceSizeForFooterInSection section: Int) -> CGSize } ``` | UICollectionViewDelegate |

Modified [UICollectionViewFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UICollectionViewFlowLayoutInvalidationContext](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UICollectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionviewlayout)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [UICollectionViewLayoutAttributes](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSObjectProtocol, UIDynamicItem |
| To | NSCopying, UIDynamicItem |

Modified [UICollectionViewLayoutInvalidationContext](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UICollectionViewScrollDirection [enum]](https://developer.apple.com/documentation/uikit/uicollectionviewscrolldirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UICollectionViewTransitionLayout](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UICollectionViewUpdateItem](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UICollisionBehavior](https://developer.apple.com/documentation/uikit/uicollisionbehavior)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIColor](https://developer.apple.com/documentation/uikit/uicolor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIColor : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(white white: CGFloat, alpha alpha: CGFloat)     class func colorWithWhite(_ white: CGFloat, alpha alpha: CGFloat) -> UIColor      init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     class func colorWithHue(_ hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     class func colorWithRed(_ red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor      init(CGColor cgColor: CGColor)     class func colorWithCGColor(_ cgColor: CGColor) -> UIColor      init(patternImage image: UIImage)     class func colorWithPatternImage(_ image: UIImage) -> UIColor      init(CIColor ciColor: CIColor)     class func colorWithCIColor(_ ciColor: CIColor) -> UIColor     init(white white: CGFloat, alpha alpha: CGFloat)     init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(CGColor cgColor: CGColor)     init(patternImage image: UIImage)     init(CIColor ciColor: CIColor)     class func blackColor() -> UIColor     class func darkGrayColor() -> UIColor     class func lightGrayColor() -> UIColor     class func whiteColor() -> UIColor     class func grayColor() -> UIColor     class func redColor() -> UIColor     class func greenColor() -> UIColor     class func blueColor() -> UIColor     class func cyanColor() -> UIColor     class func yellowColor() -> UIColor     class func magentaColor() -> UIColor     class func orangeColor() -> UIColor     class func purpleColor() -> UIColor     class func brownColor() -> UIColor     class func clearColor() -> UIColor     func set()     func setFill()     func setStroke()     func getWhite(_ white: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getHue(_ hue: UnsafeMutablePointer<CGFloat>, saturation saturation: UnsafeMutablePointer<CGFloat>, brightness brightness: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getRed(_ red: UnsafeMutablePointer<CGFloat>, green green: UnsafeMutablePointer<CGFloat>, blue blue: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func colorWithAlphaComponent(_ alpha: CGFloat) -> UIColor     var CGColor: CGColor { get }     var CIColor: CIColor { get } } extension UIColor {     class func lightTextColor() -> UIColor     class func darkTextColor() -> UIColor     class func groupTableViewBackgroundColor() -> UIColor     class func viewFlipsideBackgroundColor() -> UIColor     class func scrollViewTexturedBackgroundColor() -> UIColor     class func underPageBackgroundColor() -> UIColor } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class UIColor : NSObject, NSSecureCoding, NSCopying {      init(white white: CGFloat, alpha alpha: CGFloat)     class func colorWithWhite(_ white: CGFloat, alpha alpha: CGFloat) -> UIColor      init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     class func colorWithHue(_ hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat) -> UIColor      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     class func colorWithRed(_ red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) -> UIColor      init(CGColor cgColor: CGColor)     class func colorWithCGColor(_ cgColor: CGColor) -> UIColor      init(patternImage image: UIImage)     class func colorWithPatternImage(_ image: UIImage) -> UIColor      init(CIColor ciColor: CIColor)     class func colorWithCIColor(_ ciColor: CIColor) -> UIColor     init(white white: CGFloat, alpha alpha: CGFloat)     init(hue hue: CGFloat, saturation saturation: CGFloat, brightness brightness: CGFloat, alpha alpha: CGFloat)     init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(CGColor cgColor: CGColor)     init(patternImage image: UIImage)     init(CIColor ciColor: CIColor)     class func blackColor() -> UIColor     class func darkGrayColor() -> UIColor     class func lightGrayColor() -> UIColor     class func whiteColor() -> UIColor     class func grayColor() -> UIColor     class func redColor() -> UIColor     class func greenColor() -> UIColor     class func blueColor() -> UIColor     class func cyanColor() -> UIColor     class func yellowColor() -> UIColor     class func magentaColor() -> UIColor     class func orangeColor() -> UIColor     class func purpleColor() -> UIColor     class func brownColor() -> UIColor     class func clearColor() -> UIColor     func set()     func setFill()     func setStroke()     func getWhite(_ white: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getHue(_ hue: UnsafeMutablePointer<CGFloat>, saturation saturation: UnsafeMutablePointer<CGFloat>, brightness brightness: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func getRed(_ red: UnsafeMutablePointer<CGFloat>, green green: UnsafeMutablePointer<CGFloat>, blue blue: UnsafeMutablePointer<CGFloat>, alpha alpha: UnsafeMutablePointer<CGFloat>) -> Bool     func colorWithAlphaComponent(_ alpha: CGFloat) -> UIColor     var CGColor: CGColor { get }     var CIColor: CIColor { get } } extension UIColor : _ColorLiteralConvertible {     required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } extension UIColor {     class func lightTextColor() -> UIColor     class func darkTextColor() -> UIColor     class func groupTableViewBackgroundColor() -> UIColor     class func viewFlipsideBackgroundColor() -> UIColor     class func scrollViewTexturedBackgroundColor() -> UIColor     class func underPageBackgroundColor() -> UIColor } extension UIColor : _ColorLiteralConvertible {     required convenience init(colorLiteralRed red: Float, green green: Float, blue blue: Float, alpha alpha: Float) } ``` | NSCopying, NSSecureCoding |

Modified [UIControl](https://developer.apple.com/documentation/uikit/uicontrol)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIControlContentHorizontalAlignment [enum]](https://developer.apple.com/documentation/uikit/uicontrol/contenthorizontalalignment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIControlContentVerticalAlignment [enum]](https://developer.apple.com/documentation/uikit/uicontrol/contentverticalalignment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIControlState [struct]](https://developer.apple.com/documentation/uikit/uicontrolstate)

|  | Declaration |
| --- | --- |
| From | ``` struct UIControlState : OptionSetType {     init(rawValue rawValue: UInt)     static var Normal: UIControlState { get }     static var Highlighted: UIControlState { get }     static var Disabled: UIControlState { get }     static var Selected: UIControlState { get }     static var Application: UIControlState { get }     static var Reserved: UIControlState { get } } ``` |
| To | ``` struct UIControlState : OptionSetType {     init(rawValue rawValue: UInt)     static var Normal: UIControlState { get }     static var Highlighted: UIControlState { get }     static var Disabled: UIControlState { get }     static var Selected: UIControlState { get }     static var Focused: UIControlState { get }     static var Application: UIControlState { get }     static var Reserved: UIControlState { get } } ``` |

Modified [UIDatePicker](https://developer.apple.com/documentation/uikit/uidatepicker)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIDatePicker : UIControl {     var datePickerMode: UIDatePickerMode     var locale: NSLocale?     @NSCopying var calendar: NSCalendar!     var timeZone: NSTimeZone?     var date: NSDate     var minimumDate: NSDate?     var maximumDate: NSDate?     var countDownDuration: NSTimeInterval     var minuteInterval: Int     func setDate(_ date: NSDate, animated animated: Bool) } ``` | AnyObject, NSCoding |
| To | ``` class UIDatePicker : UIControl, NSCoding {     var datePickerMode: UIDatePickerMode     var locale: NSLocale?     @NSCopying var calendar: NSCalendar!     var timeZone: NSTimeZone?     var date: NSDate     var minimumDate: NSDate?     var maximumDate: NSDate?     var countDownDuration: NSTimeInterval     var minuteInterval: Int     func setDate(_ date: NSDate, animated animated: Bool) } ``` | NSCoding |

Modified [UIDatePickerMode [enum]](https://developer.apple.com/documentation/uikit/uidatepicker/mode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIDevice](https://developer.apple.com/documentation/uikit/uidevice)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIDeviceBatteryState [enum]](https://developer.apple.com/documentation/uikit/uidevice/batterystate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIDeviceOrientation [enum]](https://developer.apple.com/documentation/uikit/uideviceorientation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIDictationPhrase](https://developer.apple.com/documentation/uikit/uidictationphrase)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIDocument](https://developer.apple.com/documentation/uikit/uidocument)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSFilePresenter, NSObjectProtocol, NSProgressReporting |
| To | NSFilePresenter, NSProgressReporting |

Modified [UIDocumentChangeKind [enum]](https://developer.apple.com/documentation/uikit/uidocument/changekind)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIDocumentInteractionController](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, UIActionSheetDelegate |
| To | UIActionSheetDelegate |

Modified [UIDocumentMenuOrder [enum]](https://developer.apple.com/documentation/uikit/uidocumentmenuorder)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIDocumentMenuViewController](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIDocumentPickerExtensionViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIDocumentPickerMode [enum]](https://developer.apple.com/documentation/uikit/uidocumentpickermode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIDocumentPickerViewController](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIDocumentSaveOperation [enum]](https://developer.apple.com/documentation/uikit/uidocument/saveoperation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIDynamicAnimator](https://developer.apple.com/documentation/uikit/uidynamicanimator)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIDynamicBehavior](https://developer.apple.com/documentation/uikit/uidynamicbehavior)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIDynamicItemBehavior](https://developer.apple.com/documentation/uikit/uidynamicitembehavior)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIDynamicItemCollisionBoundsType [enum]](https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIDynamicItemGroup](https://developer.apple.com/documentation/uikit/uidynamicitemgroup)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, UIDynamicItem |
| To | UIDynamicItem |

Modified [UIEvent](https://developer.apple.com/documentation/uikit/uievent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIEventSubtype [enum]](https://developer.apple.com/documentation/uikit/uievent/eventsubtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIEventType [enum]](https://developer.apple.com/documentation/uikit/uieventtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum UIEventType : Int {     case Touches     case Motion     case RemoteControl } ``` | Equatable, Hashable, RawRepresentable |
| To | ``` enum UIEventType : Int {     case Touches     case Motion     case RemoteControl     case Presses } ``` | -- |

Modified [UIFieldBehavior](https://developer.apple.com/documentation/uikit/uifieldbehavior)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIFont](https://developer.apple.com/documentation/uikit/uifont)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [UIFontDescriptor](https://developer.apple.com/documentation/uikit/uifontdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIFontDescriptor : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init()     init?(coder aDecoder: NSCoder)     var postscriptName: String { get }     var pointSize: CGFloat { get }     var matrix: CGAffineTransform { get }     var symbolicTraits: UIFontDescriptorSymbolicTraits { get }     func objectForKey(_ anAttribute: String) -> AnyObject?     func fontAttributes() -> [String : AnyObject]     func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<String>?) -> [UIFontDescriptor]      init(fontAttributes attributes: [String : AnyObject])     class func fontDescriptorWithFontAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor      init(name fontName: String, size size: CGFloat)     class func fontDescriptorWithName(_ fontName: String, size size: CGFloat) -> UIFontDescriptor      init(name fontName: String, matrix matrix: CGAffineTransform)     class func fontDescriptorWithName(_ fontName: String, matrix matrix: CGAffineTransform) -> UIFontDescriptor     class func preferredFontDescriptorWithTextStyle(_ style: String) -> UIFontDescriptor     init(fontAttributes attributes: [String : AnyObject])     func fontDescriptorByAddingAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor     func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor     func fontDescriptorWithSize(_ newPointSize: CGFloat) -> UIFontDescriptor     func fontDescriptorWithMatrix(_ matrix: CGAffineTransform) -> UIFontDescriptor     func fontDescriptorWithFace(_ newFace: String) -> UIFontDescriptor     func fontDescriptorWithFamily(_ newFamily: String) -> UIFontDescriptor } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class UIFontDescriptor : NSObject, NSCopying, NSSecureCoding {     convenience init()     init?(coder aDecoder: NSCoder)     var postscriptName: String { get }     var pointSize: CGFloat { get }     var matrix: CGAffineTransform { get }     var symbolicTraits: UIFontDescriptorSymbolicTraits { get }     func objectForKey(_ anAttribute: String) -> AnyObject?     func fontAttributes() -> [String : AnyObject]     func matchingFontDescriptorsWithMandatoryKeys(_ mandatoryKeys: Set<String>?) -> [UIFontDescriptor]      init(fontAttributes attributes: [String : AnyObject])     class func fontDescriptorWithFontAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor      init(name fontName: String, size size: CGFloat)     class func fontDescriptorWithName(_ fontName: String, size size: CGFloat) -> UIFontDescriptor      init(name fontName: String, matrix matrix: CGAffineTransform)     class func fontDescriptorWithName(_ fontName: String, matrix matrix: CGAffineTransform) -> UIFontDescriptor     class func preferredFontDescriptorWithTextStyle(_ style: String) -> UIFontDescriptor     init(fontAttributes attributes: [String : AnyObject])     func fontDescriptorByAddingAttributes(_ attributes: [String : AnyObject]) -> UIFontDescriptor     func fontDescriptorWithSymbolicTraits(_ symbolicTraits: UIFontDescriptorSymbolicTraits) -> UIFontDescriptor     func fontDescriptorWithSize(_ newPointSize: CGFloat) -> UIFontDescriptor     func fontDescriptorWithMatrix(_ matrix: CGAffineTransform) -> UIFontDescriptor     func fontDescriptorWithFace(_ newFace: String) -> UIFontDescriptor     func fontDescriptorWithFamily(_ newFamily: String) -> UIFontDescriptor } ``` | NSCopying, NSSecureCoding |

Modified [UIForceTouchCapability [enum]](https://developer.apple.com/documentation/uikit/uiforcetouchcapability)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIGestureRecognizer](https://developer.apple.com/documentation/uikit/uigesturerecognizer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIGestureRecognizer : NSObject {     init(target target: AnyObject?, action action: Selector)     func addTarget(_ target: AnyObject, action action: Selector)     func removeTarget(_ target: AnyObject?, action action: Selector)     var state: UIGestureRecognizerState { get }     weak var delegate: UIGestureRecognizerDelegate?     var enabled: Bool     var view: UIView? { get }     var cancelsTouchesInView: Bool     var delaysTouchesBegan: Bool     var delaysTouchesEnded: Bool     func requireGestureRecognizerToFail(_ otherGestureRecognizer: UIGestureRecognizer)     func locationInView(_ view: UIView?) -> CGPoint     func numberOfTouches() -> Int     func locationOfTouch(_ touchIndex: Int, inView view: UIView?) -> CGPoint } ``` | AnyObject |
| To | ``` class UIGestureRecognizer : NSObject {     init(target target: AnyObject?, action action: Selector)     func addTarget(_ target: AnyObject, action action: Selector)     func removeTarget(_ target: AnyObject?, action action: Selector)     var state: UIGestureRecognizerState { get }     weak var delegate: UIGestureRecognizerDelegate?     var enabled: Bool     var view: UIView? { get }     var cancelsTouchesInView: Bool     var delaysTouchesBegan: Bool     var delaysTouchesEnded: Bool     var allowedTouchTypes: [NSNumber]     var allowedPressTypes: [NSNumber]     func requireGestureRecognizerToFail(_ otherGestureRecognizer: UIGestureRecognizer)     func locationInView(_ view: UIView?) -> CGPoint     func numberOfTouches() -> Int     func locationOfTouch(_ touchIndex: Int, inView view: UIView?) -> CGPoint } ``` | -- |

Modified [UIGestureRecognizerDelegate](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UIGestureRecognizerDelegate : NSObjectProtocol {     optional func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool     optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWithGestureRecognizer otherGestureRecognizer: UIGestureRecognizer) -> Bool     optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRequireFailureOfGestureRecognizer otherGestureRecognizer: UIGestureRecognizer) -> Bool     optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldBeRequiredToFailByGestureRecognizer otherGestureRecognizer: UIGestureRecognizer) -> Bool     optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceiveTouch touch: UITouch) -> Bool } ``` |
| To | ``` protocol UIGestureRecognizerDelegate : NSObjectProtocol {     optional func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool     optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWithGestureRecognizer otherGestureRecognizer: UIGestureRecognizer) -> Bool     optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRequireFailureOfGestureRecognizer otherGestureRecognizer: UIGestureRecognizer) -> Bool     optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldBeRequiredToFailByGestureRecognizer otherGestureRecognizer: UIGestureRecognizer) -> Bool     optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceiveTouch touch: UITouch) -> Bool     optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldReceivePress press: UIPress) -> Bool } ``` |

Modified [UIGestureRecognizerState [enum]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/state)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIGravityBehavior](https://developer.apple.com/documentation/uikit/uigravitybehavior)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIGuidedAccessRestrictionState [enum]](https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImage](https://developer.apple.com/documentation/uikit/uiimage)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIImage : NSObject, NSSecureCoding, NSCoding {      init?(named name: String)     class func imageNamed(_ name: String) -> UIImage?      init?(named name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?)     class func imageNamed(_ name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?) -> UIImage?      init?(contentsOfFile path: String)     class func imageWithContentsOfFile(_ path: String) -> UIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> UIImage?      init?(data data: NSData, scale scale: CGFloat)     class func imageWithData(_ data: NSData, scale scale: CGFloat) -> UIImage?      init(CGImage cgImage: CGImage)     class func imageWithCGImage(_ cgImage: CGImage) -> UIImage      init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCGImage(_ cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage      init(CIImage ciImage: CIImage)     class func imageWithCIImage(_ ciImage: CIImage) -> UIImage      init(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCIImage(_ ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     init?(contentsOfFile path: String)     init?(data data: NSData)     init?(data data: NSData, scale scale: CGFloat)     init(CGImage cgImage: CGImage)     init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     init(CIImage ciImage: CIImage)     init(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     var size: CGSize { get }     var CGImage: CGImage? { get }     var CIImage: CIImage? { get }     var imageOrientation: UIImageOrientation { get }     var scale: CGFloat { get }     class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage?     class func animatedImageWithImages(_ images: [UIImage], duration duration: NSTimeInterval) -> UIImage?     var images: [UIImage]? { get }     var duration: NSTimeInterval { get }     func drawAtPoint(_ point: CGPoint)     func drawAtPoint(_ point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawInRect(_ rect: CGRect)     func drawInRect(_ rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawAsPatternInRect(_ rect: CGRect)     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets) -> UIImage     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage     var capInsets: UIEdgeInsets { get }     var resizingMode: UIImageResizingMode { get }     func imageWithAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage     var alignmentRectInsets: UIEdgeInsets { get }     func imageWithRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage     var renderingMode: UIImageRenderingMode { get }     @NSCopying var traitCollection: UITraitCollection { get }     var imageAsset: UIImageAsset? { get }     func imageFlippedForRightToLeftLayoutDirection() -> UIImage     var flipsForRightToLeftLayoutDirection: Bool { get } } extension UIImage : UIAccessibilityIdentification { } extension UIImage {     func stretchableImageWithLeftCapWidth(_ leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get } } ``` | AnyObject, NSCoding, NSObjectProtocol, NSSecureCoding, UIAccessibilityIdentification |
| To | ``` class UIImage : NSObject, NSSecureCoding {      init?(named name: String)     class func imageNamed(_ name: String) -> UIImage?      init?(named name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?)     class func imageNamed(_ name: String, inBundle bundle: NSBundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?) -> UIImage?      init?(contentsOfFile path: String)     class func imageWithContentsOfFile(_ path: String) -> UIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> UIImage?      init?(data data: NSData, scale scale: CGFloat)     class func imageWithData(_ data: NSData, scale scale: CGFloat) -> UIImage?      init(CGImage cgImage: CGImage)     class func imageWithCGImage(_ cgImage: CGImage) -> UIImage      init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCGImage(_ cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage      init(CIImage ciImage: CIImage)     class func imageWithCIImage(_ ciImage: CIImage) -> UIImage      init(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     class func imageWithCIImage(_ ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation) -> UIImage     init?(contentsOfFile path: String)     init?(data data: NSData)     init?(data data: NSData, scale scale: CGFloat)     init(CGImage cgImage: CGImage)     init(CGImage cgImage: CGImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     init(CIImage ciImage: CIImage)     init(CIImage ciImage: CIImage, scale scale: CGFloat, orientation orientation: UIImageOrientation)     var size: CGSize { get }     var CGImage: CGImage? { get }     var CIImage: CIImage? { get }     var imageOrientation: UIImageOrientation { get }     var scale: CGFloat { get }     class func animatedImageNamed(_ name: String, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, duration duration: NSTimeInterval) -> UIImage?     class func animatedResizableImageNamed(_ name: String, capInsets capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode, duration duration: NSTimeInterval) -> UIImage?     class func animatedImageWithImages(_ images: [UIImage], duration duration: NSTimeInterval) -> UIImage?     var images: [UIImage]? { get }     var duration: NSTimeInterval { get }     func drawAtPoint(_ point: CGPoint)     func drawAtPoint(_ point: CGPoint, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawInRect(_ rect: CGRect)     func drawInRect(_ rect: CGRect, blendMode blendMode: CGBlendMode, alpha alpha: CGFloat)     func drawAsPatternInRect(_ rect: CGRect)     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets) -> UIImage     func resizableImageWithCapInsets(_ capInsets: UIEdgeInsets, resizingMode resizingMode: UIImageResizingMode) -> UIImage     var capInsets: UIEdgeInsets { get }     var resizingMode: UIImageResizingMode { get }     func imageWithAlignmentRectInsets(_ alignmentInsets: UIEdgeInsets) -> UIImage     var alignmentRectInsets: UIEdgeInsets { get }     func imageWithRenderingMode(_ renderingMode: UIImageRenderingMode) -> UIImage     var renderingMode: UIImageRenderingMode { get }     @NSCopying var traitCollection: UITraitCollection { get }     var imageAsset: UIImageAsset? { get }     func imageFlippedForRightToLeftLayoutDirection() -> UIImage     var flipsForRightToLeftLayoutDirection: Bool { get } } extension UIImage : UIAccessibilityIdentification { } extension UIImage : _ImageLiteralConvertible {     required convenience init(imageLiteral name: String) } extension UIImage {     func stretchableImageWithLeftCapWidth(_ leftCapWidth: Int, topCapHeight topCapHeight: Int) -> UIImage     var leftCapWidth: Int { get }     var topCapHeight: Int { get } } extension UIImage : _ImageLiteralConvertible {     required convenience init(imageLiteral name: String) } ``` | NSSecureCoding, UIAccessibilityIdentification |

Modified [UIImageAsset](https://developer.apple.com/documentation/uikit/uiimageasset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIImageAsset : NSObject, NSSecureCoding, NSCoding {     init()     init?(coder aDecoder: NSCoder)     func imageWithTraitCollection(_ traitCollection: UITraitCollection) -> UIImage     func registerImage(_ image: UIImage, withTraitCollection traitCollection: UITraitCollection)     func unregisterImageWithTraitCollection(_ traitCollection: UITraitCollection) } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class UIImageAsset : NSObject, NSSecureCoding {     init()     init?(coder aDecoder: NSCoder)     func imageWithTraitCollection(_ traitCollection: UITraitCollection) -> UIImage     func registerImage(_ image: UIImage, withTraitCollection traitCollection: UITraitCollection)     func unregisterImageWithTraitCollection(_ traitCollection: UITraitCollection) } ``` | NSSecureCoding |

Modified [UIImageOrientation [enum]](https://developer.apple.com/documentation/uikit/uiimageorientation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIImagePickerController : UINavigationController {     class func isSourceTypeAvailable(_ sourceType: UIImagePickerControllerSourceType) -> Bool     class func availableMediaTypesForSourceType(_ sourceType: UIImagePickerControllerSourceType) -> [String]?     class func isCameraDeviceAvailable(_ cameraDevice: UIImagePickerControllerCameraDevice) -> Bool     class func isFlashAvailableForCameraDevice(_ cameraDevice: UIImagePickerControllerCameraDevice) -> Bool     class func availableCaptureModesForCameraDevice(_ cameraDevice: UIImagePickerControllerCameraDevice) -> [NSNumber]?     weak var delegate: protocol<UIImagePickerControllerDelegate, UINavigationControllerDelegate>?     var sourceType: UIImagePickerControllerSourceType     var mediaTypes: [String]     var allowsEditing: Bool     var allowsImageEditing: Bool     var videoMaximumDuration: NSTimeInterval     var videoQuality: UIImagePickerControllerQualityType     var showsCameraControls: Bool     var cameraOverlayView: UIView?     var cameraViewTransform: CGAffineTransform     func takePicture()     func startVideoCapture() -> Bool     func stopVideoCapture()     var cameraCaptureMode: UIImagePickerControllerCameraCaptureMode     var cameraDevice: UIImagePickerControllerCameraDevice     var cameraFlashMode: UIImagePickerControllerCameraFlashMode } ``` | AnyObject, NSCoding |
| To | ``` class UIImagePickerController : UINavigationController, NSCoding {     class func isSourceTypeAvailable(_ sourceType: UIImagePickerControllerSourceType) -> Bool     class func availableMediaTypesForSourceType(_ sourceType: UIImagePickerControllerSourceType) -> [String]?     class func isCameraDeviceAvailable(_ cameraDevice: UIImagePickerControllerCameraDevice) -> Bool     class func isFlashAvailableForCameraDevice(_ cameraDevice: UIImagePickerControllerCameraDevice) -> Bool     class func availableCaptureModesForCameraDevice(_ cameraDevice: UIImagePickerControllerCameraDevice) -> [NSNumber]?     weak var delegate: protocol<UIImagePickerControllerDelegate, UINavigationControllerDelegate>?     var sourceType: UIImagePickerControllerSourceType     var mediaTypes: [String]     var allowsEditing: Bool     var allowsImageEditing: Bool     var videoMaximumDuration: NSTimeInterval     var videoQuality: UIImagePickerControllerQualityType     var showsCameraControls: Bool     var cameraOverlayView: UIView?     var cameraViewTransform: CGAffineTransform     func takePicture()     func startVideoCapture() -> Bool     func stopVideoCapture()     var cameraCaptureMode: UIImagePickerControllerCameraCaptureMode     var cameraDevice: UIImagePickerControllerCameraDevice     var cameraFlashMode: UIImagePickerControllerCameraFlashMode } ``` | NSCoding |

Modified [UIImagePickerControllerCameraCaptureMode [enum]](https://developer.apple.com/documentation/uikit/uiimagepickercontrollercameracapturemode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImagePickerControllerCameraDevice [enum]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameradevice)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImagePickerControllerCameraFlashMode [enum]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameraflashmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImagePickerControllerQualityType [enum]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/qualitytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImagePickerControllerSourceType [enum]](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImageRenderingMode [enum]](https://developer.apple.com/documentation/uikit/uiimage/renderingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImageResizingMode [enum]](https://developer.apple.com/documentation/uikit/uiimageresizingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIImageView : UIView {     init(image image: UIImage?)     init(image image: UIImage?, highlightedImage highlightedImage: UIImage?)     var image: UIImage?     var highlightedImage: UIImage?     var userInteractionEnabled: Bool     var highlighted: Bool     var animationImages: [UIImage]?     var highlightedAnimationImages: [UIImage]?     var animationDuration: NSTimeInterval     var animationRepeatCount: Int     var tintColor: UIColor!     func startAnimating()     func stopAnimating()     func isAnimating() -> Bool } ``` | AnyObject |
| To | ``` class UIImageView : UIView {     init(image image: UIImage?)     init(image image: UIImage?, highlightedImage highlightedImage: UIImage?)     var image: UIImage?     var highlightedImage: UIImage?     var userInteractionEnabled: Bool     var highlighted: Bool     var animationImages: [UIImage]?     var highlightedAnimationImages: [UIImage]?     var animationDuration: NSTimeInterval     var animationRepeatCount: Int     var tintColor: UIColor!     func startAnimating()     func stopAnimating()     func isAnimating() -> Bool     var adjustsImageWhenAncestorFocused: Bool     var focusedFrameGuide: UILayoutGuide { get } } ``` | -- |

Modified [UIInputView](https://developer.apple.com/documentation/uikit/uiinputview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIInputViewController](https://developer.apple.com/documentation/uikit/uiinputviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, UITextInputDelegate |
| To | UITextInputDelegate |

Modified [UIInputViewStyle [enum]](https://developer.apple.com/documentation/uikit/uiinputview/style)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIInterfaceOrientation [enum]](https://developer.apple.com/documentation/uikit/uiinterfaceorientation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIInterpolatingMotionEffect](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIInterpolatingMotionEffectType [enum]](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffecttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIKeyboardAppearance [enum]](https://developer.apple.com/documentation/uikit/uikeyboardappearance)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIKeyboardType [enum]](https://developer.apple.com/documentation/uikit/uikeyboardtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIKeyCommand](https://developer.apple.com/documentation/uikit/uikeycommand)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIKeyCommand : NSObject, NSCopying, NSSecureCoding, NSCoding {     init()     init?(coder aDecoder: NSCoder)     var input: String { get }     var modifierFlags: UIKeyModifierFlags { get }     var discoverabilityTitle: String?      init(input input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector)     class func keyCommandWithInput(_ input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector) -> UIKeyCommand      init(input input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector, discoverabilityTitle discoverabilityTitle: String)     class func keyCommandWithInput(_ input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector, discoverabilityTitle discoverabilityTitle: String) -> UIKeyCommand } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class UIKeyCommand : NSObject, NSCopying, NSSecureCoding {     init()     init?(coder aDecoder: NSCoder)     var input: String { get }     var modifierFlags: UIKeyModifierFlags { get }     var discoverabilityTitle: String?      init(input input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector)     class func keyCommandWithInput(_ input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector) -> UIKeyCommand      init(input input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector, discoverabilityTitle discoverabilityTitle: String)     class func keyCommandWithInput(_ input: String, modifierFlags modifierFlags: UIKeyModifierFlags, action action: Selector, discoverabilityTitle discoverabilityTitle: String) -> UIKeyCommand } ``` | NSCopying, NSSecureCoding |

Modified [UIKeyInput](https://developer.apple.com/documentation/uikit/uikeyinput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UIKeyInput : UITextInputTraits, NSObjectProtocol {     func hasText() -> Bool     func insertText(_ text: String)     func deleteBackward() } ``` | NSObjectProtocol, UITextInputTraits |
| To | ``` protocol UIKeyInput : UITextInputTraits {     func hasText() -> Bool     func insertText(_ text: String)     func deleteBackward() } ``` | UITextInputTraits |

Modified [UILabel](https://developer.apple.com/documentation/uikit/uilabel)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UILabel : UIView {     var text: String?     var font: UIFont!     var textColor: UIColor!     var shadowColor: UIColor?     var shadowOffset: CGSize     var textAlignment: NSTextAlignment     var lineBreakMode: NSLineBreakMode     @NSCopying var attributedText: NSAttributedString?     var highlightedTextColor: UIColor?     var highlighted: Bool     var userInteractionEnabled: Bool     var enabled: Bool     var numberOfLines: Int     var adjustsFontSizeToFitWidth: Bool     var baselineAdjustment: UIBaselineAdjustment     var minimumScaleFactor: CGFloat     var allowsDefaultTighteningForTruncation: Bool     func textRectForBounds(_ bounds: CGRect, limitedToNumberOfLines numberOfLines: Int) -> CGRect     func drawTextInRect(_ rect: CGRect)     var preferredMaxLayoutWidth: CGFloat     var minimumFontSize: CGFloat     var adjustsLetterSpacingToFitWidth: Bool } ``` | AnyObject, NSCoding |
| To | ``` class UILabel : UIView, NSCoding {     var text: String?     var font: UIFont!     var textColor: UIColor!     var shadowColor: UIColor?     var shadowOffset: CGSize     var textAlignment: NSTextAlignment     var lineBreakMode: NSLineBreakMode     @NSCopying var attributedText: NSAttributedString?     var highlightedTextColor: UIColor?     var highlighted: Bool     var userInteractionEnabled: Bool     var enabled: Bool     var numberOfLines: Int     var adjustsFontSizeToFitWidth: Bool     var baselineAdjustment: UIBaselineAdjustment     var minimumScaleFactor: CGFloat     var allowsDefaultTighteningForTruncation: Bool     func textRectForBounds(_ bounds: CGRect, limitedToNumberOfLines numberOfLines: Int) -> CGRect     func drawTextInRect(_ rect: CGRect)     var preferredMaxLayoutWidth: CGFloat     var minimumFontSize: CGFloat     var adjustsLetterSpacingToFitWidth: Bool } ``` | NSCoding |

Modified [UILayoutConstraintAxis [enum]](https://developer.apple.com/documentation/uikit/uilayoutconstraintaxis)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UILayoutGuide](https://developer.apple.com/documentation/uikit/uilayoutguide)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [UILexicon](https://developer.apple.com/documentation/uikit/uilexicon)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [UILexiconEntry](https://developer.apple.com/documentation/uikit/uilexiconentry)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [UILocalizedIndexedCollation](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UILocalNotification](https://developer.apple.com/documentation/uikit/uilocalnotification)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [UILongPressGestureRecognizer](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIManagedDocument](https://developer.apple.com/documentation/uikit/uimanageddocument)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIMarkupTextPrintFormatter](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIMenuController](https://developer.apple.com/documentation/uikit/uimenucontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIMenuControllerArrowDirection [enum]](https://developer.apple.com/documentation/uikit/uimenucontroller/arrowdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIMenuItem](https://developer.apple.com/documentation/uikit/uimenuitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIModalPresentationStyle [enum]](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIModalTransitionStyle [enum]](https://developer.apple.com/documentation/uikit/uimodaltransitionstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIMotionEffect](https://developer.apple.com/documentation/uikit/uimotioneffect)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [UIMotionEffectGroup](https://developer.apple.com/documentation/uikit/uimotioneffectgroup)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIMutableApplicationShortcutItem](https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIMutableUserNotificationAction](https://developer.apple.com/documentation/uikit/uimutableusernotificationaction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIMutableUserNotificationCategory](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UINavigationBar : UIView, UIBarPositioning {     var barStyle: UIBarStyle     weak var delegate: UINavigationBarDelegate?     var translucent: Bool     func pushNavigationItem(_ item: UINavigationItem, animated animated: Bool)     func popNavigationItemAnimated(_ animated: Bool) -> UINavigationItem?     var topItem: UINavigationItem? { get }     var backItem: UINavigationItem? { get }     var items: [UINavigationItem]?     func setItems(_ items: [UINavigationItem]?, animated animated: Bool)     var tintColor: UIColor!     var barTintColor: UIColor?     func setBackgroundImage(_ backgroundImage: UIImage?, forBarPosition barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForBarPosition(_ barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackgroundImage(_ backgroundImage: UIImage?, forBarMetrics barMetrics: UIBarMetrics)     func backgroundImageForBarMetrics(_ barMetrics: UIBarMetrics) -> UIImage?     var shadowImage: UIImage?     var titleTextAttributes: [String : AnyObject]?     func setTitleVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func titleVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat     var backIndicatorImage: UIImage?     var backIndicatorTransitionMaskImage: UIImage? } ``` | AnyObject, NSCoding, NSObjectProtocol, UIBarPositioning |
| To | ``` class UINavigationBar : UIView, NSCoding, UIBarPositioning {     var barStyle: UIBarStyle     weak var delegate: UINavigationBarDelegate?     var translucent: Bool     func pushNavigationItem(_ item: UINavigationItem, animated animated: Bool)     func popNavigationItemAnimated(_ animated: Bool) -> UINavigationItem?     var topItem: UINavigationItem? { get }     var backItem: UINavigationItem? { get }     var items: [UINavigationItem]?     func setItems(_ items: [UINavigationItem]?, animated animated: Bool)     var tintColor: UIColor!     var barTintColor: UIColor?     func setBackgroundImage(_ backgroundImage: UIImage?, forBarPosition barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForBarPosition(_ barPosition: UIBarPosition, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setBackgroundImage(_ backgroundImage: UIImage?, forBarMetrics barMetrics: UIBarMetrics)     func backgroundImageForBarMetrics(_ barMetrics: UIBarMetrics) -> UIImage?     var shadowImage: UIImage?     var titleTextAttributes: [String : AnyObject]?     func setTitleVerticalPositionAdjustment(_ adjustment: CGFloat, forBarMetrics barMetrics: UIBarMetrics)     func titleVerticalPositionAdjustmentForBarMetrics(_ barMetrics: UIBarMetrics) -> CGFloat     var backIndicatorImage: UIImage?     var backIndicatorTransitionMaskImage: UIImage? } ``` | NSCoding, UIBarPositioning |

Modified [UINavigationBarDelegate](https://developer.apple.com/documentation/uikit/uinavigationbardelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UINavigationBarDelegate : UIBarPositioningDelegate, NSObjectProtocol {     optional func navigationBar(_ navigationBar: UINavigationBar, shouldPushItem item: UINavigationItem) -> Bool     optional func navigationBar(_ navigationBar: UINavigationBar, didPushItem item: UINavigationItem)     optional func navigationBar(_ navigationBar: UINavigationBar, shouldPopItem item: UINavigationItem) -> Bool     optional func navigationBar(_ navigationBar: UINavigationBar, didPopItem item: UINavigationItem) } ``` | NSObjectProtocol, UIBarPositioningDelegate |
| To | ``` protocol UINavigationBarDelegate : UIBarPositioningDelegate {     optional func navigationBar(_ navigationBar: UINavigationBar, shouldPushItem item: UINavigationItem) -> Bool     optional func navigationBar(_ navigationBar: UINavigationBar, didPushItem item: UINavigationItem)     optional func navigationBar(_ navigationBar: UINavigationBar, shouldPopItem item: UINavigationItem) -> Bool     optional func navigationBar(_ navigationBar: UINavigationBar, didPopItem item: UINavigationItem) } ``` | UIBarPositioningDelegate |

Modified [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UINavigationControllerOperation [enum]](https://developer.apple.com/documentation/uikit/uinavigationcontrolleroperation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UINavigationItem](https://developer.apple.com/documentation/uikit/uinavigationitem)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [UINib](https://developer.apple.com/documentation/uikit/uinib)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPageControl](https://developer.apple.com/documentation/uikit/uipagecontrol)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPageViewController](https://developer.apple.com/documentation/uikit/uipageviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPageViewControllerNavigationDirection [enum]](https://developer.apple.com/documentation/uikit/uipageviewcontrollernavigationdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIPageViewControllerNavigationOrientation [enum]](https://developer.apple.com/documentation/uikit/uipageviewcontroller/navigationorientation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIPageViewControllerSpineLocation [enum]](https://developer.apple.com/documentation/uikit/uipageviewcontrollerspinelocation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIPageViewControllerTransitionStyle [enum]](https://developer.apple.com/documentation/uikit/uipageviewcontroller/transitionstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIPanGestureRecognizer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPasteboard](https://developer.apple.com/documentation/uikit/uipasteboard)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPercentDrivenInteractiveTransition](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, UIViewControllerInteractiveTransitioning |
| To | UIViewControllerInteractiveTransitioning |

Modified [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIPickerView : UIView, UITableViewDataSource {     weak var dataSource: UIPickerViewDataSource?     weak var delegate: UIPickerViewDelegate?     var showsSelectionIndicator: Bool     var numberOfComponents: Int { get }     func numberOfRowsInComponent(_ component: Int) -> Int     func rowSizeForComponent(_ component: Int) -> CGSize     func viewForRow(_ row: Int, forComponent component: Int) -> UIView?     func reloadAllComponents()     func reloadComponent(_ component: Int)     func selectRow(_ row: Int, inComponent component: Int, animated animated: Bool)     func selectedRowInComponent(_ component: Int) -> Int } ``` | AnyObject, NSCoding, NSObjectProtocol, UITableViewDataSource |
| To | ``` class UIPickerView : UIView, NSCoding, UITableViewDataSource {     weak var dataSource: UIPickerViewDataSource?     weak var delegate: UIPickerViewDelegate?     var showsSelectionIndicator: Bool     var numberOfComponents: Int { get }     func numberOfRowsInComponent(_ component: Int) -> Int     func rowSizeForComponent(_ component: Int) -> CGSize     func viewForRow(_ row: Int, forComponent component: Int) -> UIView?     func reloadAllComponents()     func reloadComponent(_ component: Int)     func selectRow(_ row: Int, inComponent component: Int, animated animated: Bool)     func selectedRowInComponent(_ component: Int) -> Int } ``` | NSCoding, UITableViewDataSource |

Modified [UIPickerViewAccessibilityDelegate](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UIPickerViewAccessibilityDelegate : UIPickerViewDelegate, NSObjectProtocol {     optional func pickerView(_ pickerView: UIPickerView, accessibilityLabelForComponent component: Int) -> String?     optional func pickerView(_ pickerView: UIPickerView, accessibilityHintForComponent component: Int) -> String? } ``` | NSObjectProtocol, UIPickerViewDelegate |
| To | ``` protocol UIPickerViewAccessibilityDelegate : UIPickerViewDelegate {     optional func pickerView(_ pickerView: UIPickerView, accessibilityLabelForComponent component: Int) -> String?     optional func pickerView(_ pickerView: UIPickerView, accessibilityHintForComponent component: Int) -> String? } ``` | UIPickerViewDelegate |

Modified [UIPinchGestureRecognizer](https://developer.apple.com/documentation/uikit/uipinchgesturerecognizer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPopoverBackgroundView](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview)

|  | Protocols |
| --- | --- |
| From | AnyObject, UIPopoverBackgroundViewMethods |
| To | UIPopoverBackgroundViewMethods |

Modified [UIPopoverController](https://developer.apple.com/documentation/uikit/uipopovercontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, UIAppearanceContainer |
| To | UIAppearanceContainer |

Modified [UIPopoverPresentationController](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPopoverPresentationControllerDelegate](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UIPopoverPresentationControllerDelegate : UIAdaptivePresentationControllerDelegate, NSObjectProtocol {     optional func prepareForPopoverPresentation(_ popoverPresentationController: UIPopoverPresentationController)     optional func popoverPresentationControllerShouldDismissPopover(_ popoverPresentationController: UIPopoverPresentationController) -> Bool     optional func popoverPresentationControllerDidDismissPopover(_ popoverPresentationController: UIPopoverPresentationController)     optional func popoverPresentationController(_ popoverPresentationController: UIPopoverPresentationController, willRepositionPopoverToRect rect: UnsafeMutablePointer<CGRect>, inView view: AutoreleasingUnsafeMutablePointer<UIView?>) } ``` | NSObjectProtocol, UIAdaptivePresentationControllerDelegate |
| To | ``` protocol UIPopoverPresentationControllerDelegate : UIAdaptivePresentationControllerDelegate {     optional func prepareForPopoverPresentation(_ popoverPresentationController: UIPopoverPresentationController)     optional func popoverPresentationControllerShouldDismissPopover(_ popoverPresentationController: UIPopoverPresentationController) -> Bool     optional func popoverPresentationControllerDidDismissPopover(_ popoverPresentationController: UIPopoverPresentationController)     optional func popoverPresentationController(_ popoverPresentationController: UIPopoverPresentationController, willRepositionPopoverToRect rect: UnsafeMutablePointer<CGRect>, inView view: AutoreleasingUnsafeMutablePointer<UIView?>) } ``` | UIAdaptivePresentationControllerDelegate |

Modified [UIPresentationController](https://developer.apple.com/documentation/uikit/uipresentationcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIPresentationController : NSObject, UIAppearanceContainer, UITraitEnvironment, UIContentContainer {     var presentingViewController: UIViewController { get }     var presentedViewController: UIViewController { get }     var presentationStyle: UIModalPresentationStyle { get }     var containerView: UIView? { get }     weak var delegate: UIAdaptivePresentationControllerDelegate?     init(presentedViewController presentedViewController: UIViewController, presentingViewController presentingViewController: UIViewController)     func adaptivePresentationStyle() -> UIModalPresentationStyle     func adaptivePresentationStyleForTraitCollection(_ traitCollection: UITraitCollection) -> UIModalPresentationStyle     func containerViewWillLayoutSubviews()     func containerViewDidLayoutSubviews()     func presentedView() -> UIView?     func frameOfPresentedViewInContainerView() -> CGRect     func shouldPresentInFullscreen() -> Bool     func shouldRemovePresentersView() -> Bool     func presentationTransitionWillBegin()     func presentationTransitionDidEnd(_ completed: Bool)     func dismissalTransitionWillBegin()     func dismissalTransitionDidEnd(_ completed: Bool)     @NSCopying var overrideTraitCollection: UITraitCollection? } ``` | AnyObject, NSObjectProtocol, UIAppearanceContainer, UIContentContainer, UITraitEnvironment |
| To | ``` class UIPresentationController : NSObject, UIAppearanceContainer, UITraitEnvironment, UIContentContainer, UIFocusEnvironment {     var presentingViewController: UIViewController { get }     var presentedViewController: UIViewController { get }     var presentationStyle: UIModalPresentationStyle { get }     var containerView: UIView? { get }     weak var delegate: UIAdaptivePresentationControllerDelegate?     init(presentedViewController presentedViewController: UIViewController, presentingViewController presentingViewController: UIViewController)     func adaptivePresentationStyle() -> UIModalPresentationStyle     func adaptivePresentationStyleForTraitCollection(_ traitCollection: UITraitCollection) -> UIModalPresentationStyle     func containerViewWillLayoutSubviews()     func containerViewDidLayoutSubviews()     func presentedView() -> UIView?     func frameOfPresentedViewInContainerView() -> CGRect     func shouldPresentInFullscreen() -> Bool     func shouldRemovePresentersView() -> Bool     func presentationTransitionWillBegin()     func presentationTransitionDidEnd(_ completed: Bool)     func dismissalTransitionWillBegin()     func dismissalTransitionDidEnd(_ completed: Bool)     @NSCopying var overrideTraitCollection: UITraitCollection? } ``` | UIAppearanceContainer, UIContentContainer, UIFocusEnvironment, UITraitEnvironment |

Modified [UIPreviewAction](https://developer.apple.com/documentation/uikit/uipreviewaction)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSObjectProtocol, UIPreviewActionItem |
| To | NSCopying, UIPreviewActionItem |

Modified [UIPreviewActionGroup](https://developer.apple.com/documentation/uikit/uipreviewactiongroup)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSObjectProtocol, UIPreviewActionItem |
| To | NSCopying, UIPreviewActionItem |

Modified [UIPreviewActionStyle [enum]](https://developer.apple.com/documentation/uikit/uipreviewactionstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIPrinter](https://developer.apple.com/documentation/uikit/uiprinter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPrinterCutterBehavior [enum]](https://developer.apple.com/documentation/uikit/uiprinter/cutterbehavior)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIPrinterPickerController](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPrintFormatter](https://developer.apple.com/documentation/uikit/uiprintformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [UIPrintInfo](https://developer.apple.com/documentation/uikit/uiprintinfo)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [UIPrintInfoDuplex [enum]](https://developer.apple.com/documentation/uikit/uiprintinfo/duplex)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIPrintInfoOrientation [enum]](https://developer.apple.com/documentation/uikit/uiprintinfoorientation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIPrintInfoOutputType [enum]](https://developer.apple.com/documentation/uikit/uiprintinfooutputtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIPrintInteractionController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPrintPageRenderer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPrintPaper](https://developer.apple.com/documentation/uikit/uiprintpaper)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIProgressView](https://developer.apple.com/documentation/uikit/uiprogressview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIProgressView : UIView {     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     convenience init(progressViewStyle style: UIProgressViewStyle)     var progressViewStyle: UIProgressViewStyle     var progress: Float     var progressTintColor: UIColor?     var trackTintColor: UIColor?     var progressImage: UIImage?     var trackImage: UIImage?     func setProgress(_ progress: Float, animated animated: Bool)     var observedProgress: NSProgress? } ``` | AnyObject, NSCoding |
| To | ``` class UIProgressView : UIView, NSCoding {     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     convenience init(progressViewStyle style: UIProgressViewStyle)     var progressViewStyle: UIProgressViewStyle     var progress: Float     var progressTintColor: UIColor?     var trackTintColor: UIColor?     var progressImage: UIImage?     var trackImage: UIImage?     func setProgress(_ progress: Float, animated animated: Bool)     var observedProgress: NSProgress? } ``` | NSCoding |

Modified [UIProgressViewStyle [enum]](https://developer.apple.com/documentation/uikit/uiprogressviewstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIPushBehavior](https://developer.apple.com/documentation/uikit/uipushbehavior)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIPushBehaviorMode [enum]](https://developer.apple.com/documentation/uikit/uipushbehavior/mode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIReferenceLibraryViewController](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIRegion](https://developer.apple.com/documentation/uikit/uiregion)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIResponder : NSObject {     func nextResponder() -> UIResponder?     func canBecomeFirstResponder() -> Bool     func becomeFirstResponder() -> Bool     func canResignFirstResponder() -> Bool     func resignFirstResponder() -> Bool     func isFirstResponder() -> Bool     func touchesBegan(_ touches: Set<UITouch>, withEvent event: UIEvent?)     func touchesMoved(_ touches: Set<UITouch>, withEvent event: UIEvent?)     func touchesEnded(_ touches: Set<UITouch>, withEvent event: UIEvent?)     func touchesCancelled(_ touches: Set<UITouch>?, withEvent event: UIEvent?)     func motionBegan(_ motion: UIEventSubtype, withEvent event: UIEvent?)     func motionEnded(_ motion: UIEventSubtype, withEvent event: UIEvent?)     func motionCancelled(_ motion: UIEventSubtype, withEvent event: UIEvent?)     func remoteControlReceivedWithEvent(_ event: UIEvent?)     func canPerformAction(_ action: Selector, withSender sender: AnyObject?) -> Bool     func targetForAction(_ action: Selector, withSender sender: AnyObject?) -> AnyObject?     var undoManager: NSUndoManager? { get } } extension UIResponder {     var keyCommands: [UIKeyCommand]? { get } } extension UIResponder {     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews() } extension UIResponder {     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity) } ``` | AnyObject |
| To | ``` class UIResponder : NSObject {     func nextResponder() -> UIResponder?     func canBecomeFirstResponder() -> Bool     func becomeFirstResponder() -> Bool     func canResignFirstResponder() -> Bool     func resignFirstResponder() -> Bool     func isFirstResponder() -> Bool     func touchesBegan(_ touches: Set<UITouch>, withEvent event: UIEvent?)     func touchesMoved(_ touches: Set<UITouch>, withEvent event: UIEvent?)     func touchesEnded(_ touches: Set<UITouch>, withEvent event: UIEvent?)     func touchesCancelled(_ touches: Set<UITouch>?, withEvent event: UIEvent?)     func touchesEstimatedPropertiesUpdated(_ touches: Set<NSObject>)     func pressesBegan(_ presses: Set<UIPress>, withEvent event: UIPressesEvent?)     func pressesChanged(_ presses: Set<UIPress>, withEvent event: UIPressesEvent?)     func pressesEnded(_ presses: Set<UIPress>, withEvent event: UIPressesEvent?)     func pressesCancelled(_ presses: Set<UIPress>, withEvent event: UIPressesEvent?)     func motionBegan(_ motion: UIEventSubtype, withEvent event: UIEvent?)     func motionEnded(_ motion: UIEventSubtype, withEvent event: UIEvent?)     func motionCancelled(_ motion: UIEventSubtype, withEvent event: UIEvent?)     func remoteControlReceivedWithEvent(_ event: UIEvent?)     func canPerformAction(_ action: Selector, withSender sender: AnyObject?) -> Bool     func targetForAction(_ action: Selector, withSender sender: AnyObject?) -> AnyObject?     var undoManager: NSUndoManager? { get } } extension UIResponder {     var keyCommands: [UIKeyCommand]? { get } } extension UIResponder {     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews() } extension UIResponder {     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity) } ``` | -- |

Modified [UIReturnKeyType [enum]](https://developer.apple.com/documentation/uikit/uireturnkeytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIRotationGestureRecognizer](https://developer.apple.com/documentation/uikit/uirotationgesturerecognizer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIScreen](https://developer.apple.com/documentation/uikit/uiscreen)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIScreen : NSObject, UITraitEnvironment {     class func screens() -> [UIScreen]     class func mainScreen() -> UIScreen     var bounds: CGRect { get }     var scale: CGFloat { get }     var availableModes: [UIScreenMode] { get }     var preferredMode: UIScreenMode? { get }     var currentMode: UIScreenMode?     var overscanCompensation: UIScreenOverscanCompensation     var overscanCompensationInsets: UIEdgeInsets { get }     var mirroredScreen: UIScreen? { get }     var brightness: CGFloat     var wantsSoftwareDimming: Bool     var coordinateSpace: UICoordinateSpace { get }     var fixedCoordinateSpace: UICoordinateSpace { get }     var nativeBounds: CGRect { get }     var nativeScale: CGFloat { get }     func displayLinkWithTarget(_ target: AnyObject, selector sel: Selector) -> CADisplayLink?     var applicationFrame: CGRect { get } } extension UIScreen {     func snapshotViewAfterScreenUpdates(_ afterUpdates: Bool) -> UIView } ``` | AnyObject, NSObjectProtocol, UITraitEnvironment |
| To | ``` class UIScreen : NSObject, UITraitEnvironment {     class func screens() -> [UIScreen]     class func mainScreen() -> UIScreen     var bounds: CGRect { get }     var scale: CGFloat { get }     var availableModes: [UIScreenMode] { get }     var preferredMode: UIScreenMode? { get }     var currentMode: UIScreenMode?     var overscanCompensation: UIScreenOverscanCompensation     var overscanCompensationInsets: UIEdgeInsets { get }     var mirroredScreen: UIScreen? { get }     var brightness: CGFloat     var wantsSoftwareDimming: Bool     var coordinateSpace: UICoordinateSpace { get }     var fixedCoordinateSpace: UICoordinateSpace { get }     var nativeBounds: CGRect { get }     var nativeScale: CGFloat { get }     func displayLinkWithTarget(_ target: AnyObject, selector sel: Selector) -> CADisplayLink?     weak var focusedView: UIView? { get }     var supportsFocus: Bool { get }     var applicationFrame: CGRect { get } } extension UIScreen {     func snapshotViewAfterScreenUpdates(_ afterUpdates: Bool) -> UIView } ``` | UITraitEnvironment |

Modified [UIScreenEdgePanGestureRecognizer](https://developer.apple.com/documentation/uikit/uiscreenedgepangesturerecognizer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIScreenMode](https://developer.apple.com/documentation/uikit/uiscreenmode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIScreenOverscanCompensation [enum]](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIScrollView : UIView {     var contentOffset: CGPoint     var contentSize: CGSize     var contentInset: UIEdgeInsets     weak var delegate: UIScrollViewDelegate?     var directionalLockEnabled: Bool     var bounces: Bool     var alwaysBounceVertical: Bool     var alwaysBounceHorizontal: Bool     var pagingEnabled: Bool     var scrollEnabled: Bool     var showsHorizontalScrollIndicator: Bool     var showsVerticalScrollIndicator: Bool     var scrollIndicatorInsets: UIEdgeInsets     var indicatorStyle: UIScrollViewIndicatorStyle     var decelerationRate: CGFloat     func setContentOffset(_ contentOffset: CGPoint, animated animated: Bool)     func scrollRectToVisible(_ rect: CGRect, animated animated: Bool)     func flashScrollIndicators()     var tracking: Bool { get }     var dragging: Bool { get }     var decelerating: Bool { get }     var delaysContentTouches: Bool     var canCancelContentTouches: Bool     func touchesShouldBegin(_ touches: Set<UITouch>, withEvent event: UIEvent?, inContentView view: UIView) -> Bool     func touchesShouldCancelInContentView(_ view: UIView) -> Bool     var minimumZoomScale: CGFloat     var maximumZoomScale: CGFloat     var zoomScale: CGFloat     func setZoomScale(_ scale: CGFloat, animated animated: Bool)     func zoomToRect(_ rect: CGRect, animated animated: Bool)     var bouncesZoom: Bool     var zooming: Bool { get }     var zoomBouncing: Bool { get }     var scrollsToTop: Bool     var panGestureRecognizer: UIPanGestureRecognizer { get }     var pinchGestureRecognizer: UIPinchGestureRecognizer? { get }     var keyboardDismissMode: UIScrollViewKeyboardDismissMode } ``` | AnyObject, NSCoding |
| To | ``` class UIScrollView : UIView, NSCoding {     var contentOffset: CGPoint     var contentSize: CGSize     var contentInset: UIEdgeInsets     weak var delegate: UIScrollViewDelegate?     var directionalLockEnabled: Bool     var bounces: Bool     var alwaysBounceVertical: Bool     var alwaysBounceHorizontal: Bool     var pagingEnabled: Bool     var scrollEnabled: Bool     var showsHorizontalScrollIndicator: Bool     var showsVerticalScrollIndicator: Bool     var scrollIndicatorInsets: UIEdgeInsets     var indicatorStyle: UIScrollViewIndicatorStyle     var decelerationRate: CGFloat     func setContentOffset(_ contentOffset: CGPoint, animated animated: Bool)     func scrollRectToVisible(_ rect: CGRect, animated animated: Bool)     func flashScrollIndicators()     var tracking: Bool { get }     var dragging: Bool { get }     var decelerating: Bool { get }     var delaysContentTouches: Bool     var canCancelContentTouches: Bool     func touchesShouldBegin(_ touches: Set<UITouch>, withEvent event: UIEvent?, inContentView view: UIView) -> Bool     func touchesShouldCancelInContentView(_ view: UIView) -> Bool     var minimumZoomScale: CGFloat     var maximumZoomScale: CGFloat     var zoomScale: CGFloat     func setZoomScale(_ scale: CGFloat, animated animated: Bool)     func zoomToRect(_ rect: CGRect, animated animated: Bool)     var bouncesZoom: Bool     var zooming: Bool { get }     var zoomBouncing: Bool { get }     var scrollsToTop: Bool     var panGestureRecognizer: UIPanGestureRecognizer { get }     var pinchGestureRecognizer: UIPinchGestureRecognizer? { get }     var directionalPressGestureRecognizer: UIGestureRecognizer { get }     var keyboardDismissMode: UIScrollViewKeyboardDismissMode } ``` | NSCoding |

Modified [UIScrollViewAccessibilityDelegate](https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UIScrollViewAccessibilityDelegate : UIScrollViewDelegate, NSObjectProtocol {     optional func accessibilityScrollStatusForScrollView(_ scrollView: UIScrollView) -> String? } ``` | NSObjectProtocol, UIScrollViewDelegate |
| To | ``` protocol UIScrollViewAccessibilityDelegate : UIScrollViewDelegate {     optional func accessibilityScrollStatusForScrollView(_ scrollView: UIScrollView) -> String? } ``` | UIScrollViewDelegate |

Modified [UIScrollViewIndicatorStyle [enum]](https://developer.apple.com/documentation/uikit/uiscrollview/indicatorstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIScrollViewKeyboardDismissMode [enum]](https://developer.apple.com/documentation/uikit/uiscrollviewkeyboarddismissmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, UIBarPositioning, UITextInputTraits |
| To | UIBarPositioning, UITextInputTraits |

Modified [UISearchBarDelegate](https://developer.apple.com/documentation/uikit/uisearchbardelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UISearchBarDelegate : UIBarPositioningDelegate, NSObjectProtocol {     optional func searchBarShouldBeginEditing(_ searchBar: UISearchBar) -> Bool     optional func searchBarTextDidBeginEditing(_ searchBar: UISearchBar)     optional func searchBarShouldEndEditing(_ searchBar: UISearchBar) -> Bool     optional func searchBarTextDidEndEditing(_ searchBar: UISearchBar)     optional func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String)     optional func searchBar(_ searchBar: UISearchBar, shouldChangeTextInRange range: NSRange, replacementText text: String) -> Bool     optional func searchBarSearchButtonClicked(_ searchBar: UISearchBar)     optional func searchBarBookmarkButtonClicked(_ searchBar: UISearchBar)     optional func searchBarCancelButtonClicked(_ searchBar: UISearchBar)     optional func searchBarResultsListButtonClicked(_ searchBar: UISearchBar)     optional func searchBar(_ searchBar: UISearchBar, selectedScopeButtonIndexDidChange selectedScope: Int) } ``` | NSObjectProtocol, UIBarPositioningDelegate |
| To | ``` protocol UISearchBarDelegate : UIBarPositioningDelegate {     optional func searchBarShouldBeginEditing(_ searchBar: UISearchBar) -> Bool     optional func searchBarTextDidBeginEditing(_ searchBar: UISearchBar)     optional func searchBarShouldEndEditing(_ searchBar: UISearchBar) -> Bool     optional func searchBarTextDidEndEditing(_ searchBar: UISearchBar)     optional func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String)     optional func searchBar(_ searchBar: UISearchBar, shouldChangeTextInRange range: NSRange, replacementText text: String) -> Bool     optional func searchBarSearchButtonClicked(_ searchBar: UISearchBar)     optional func searchBarBookmarkButtonClicked(_ searchBar: UISearchBar)     optional func searchBarCancelButtonClicked(_ searchBar: UISearchBar)     optional func searchBarResultsListButtonClicked(_ searchBar: UISearchBar)     optional func searchBar(_ searchBar: UISearchBar, selectedScopeButtonIndexDidChange selectedScope: Int) } ``` | UIBarPositioningDelegate |

Modified [UISearchBarIcon [enum]](https://developer.apple.com/documentation/uikit/uisearchbar/icon)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UISearchBarStyle [enum]](https://developer.apple.com/documentation/uikit/uisearchbarstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UISearchController : UIViewController, UIViewControllerTransitioningDelegate, UIViewControllerAnimatedTransitioning {     init(searchResultsController searchResultsController: UIViewController?)     weak var searchResultsUpdater: UISearchResultsUpdating?     var active: Bool     weak var delegate: UISearchControllerDelegate?     var dimsBackgroundDuringPresentation: Bool     var hidesNavigationBarDuringPresentation: Bool     var searchResultsController: UIViewController? { get }     var searchBar: UISearchBar { get } } ``` | AnyObject, NSObjectProtocol, UIViewControllerAnimatedTransitioning, UIViewControllerTransitioningDelegate |
| To | ``` class UISearchController : UIViewController, UIViewControllerTransitioningDelegate, UIViewControllerAnimatedTransitioning {     init(searchResultsController searchResultsController: UIViewController?)     weak var searchResultsUpdater: UISearchResultsUpdating?     var active: Bool     weak var delegate: UISearchControllerDelegate?     var dimsBackgroundDuringPresentation: Bool     var obscuresBackgroundDuringPresentation: Bool     var hidesNavigationBarDuringPresentation: Bool     var searchResultsController: UIViewController? { get }     var searchBar: UISearchBar { get } } ``` | UIViewControllerAnimatedTransitioning, UIViewControllerTransitioningDelegate |

Modified [UISearchDisplayController](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UISegmentedControl](https://developer.apple.com/documentation/uikit/uisegmentedcontrol)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UISegmentedControl : UIControl {     init(items items: [AnyObject]?)     var segmentedControlStyle: UISegmentedControlStyle     var momentary: Bool     var numberOfSegments: Int { get }     var apportionsSegmentWidthsByContent: Bool     func insertSegmentWithTitle(_ title: String?, atIndex segment: Int, animated animated: Bool)     func insertSegmentWithImage(_ image: UIImage?, atIndex segment: Int, animated animated: Bool)     func removeSegmentAtIndex(_ segment: Int, animated animated: Bool)     func removeAllSegments()     func setTitle(_ title: String?, forSegmentAtIndex segment: Int)     func titleForSegmentAtIndex(_ segment: Int) -> String?     func setImage(_ image: UIImage?, forSegmentAtIndex segment: Int)     func imageForSegmentAtIndex(_ segment: Int) -> UIImage?     func setWidth(_ width: CGFloat, forSegmentAtIndex segment: Int)     func widthForSegmentAtIndex(_ segment: Int) -> CGFloat     func setContentOffset(_ offset: CGSize, forSegmentAtIndex segment: Int)     func contentOffsetForSegmentAtIndex(_ segment: Int) -> CGSize     func setEnabled(_ enabled: Bool, forSegmentAtIndex segment: Int)     func isEnabledForSegmentAtIndex(_ segment: Int) -> Bool     var selectedSegmentIndex: Int     var tintColor: UIColor!     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setDividerImage(_ dividerImage: UIImage?, forLeftSegmentState leftState: UIControlState, rightSegmentState rightState: UIControlState, barMetrics barMetrics: UIBarMetrics)     func dividerImageForLeftSegmentState(_ leftState: UIControlState, rightSegmentState rightState: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setTitleTextAttributes(_ attributes: [NSObject : AnyObject]?, forState state: UIControlState)     func titleTextAttributesForState(_ state: UIControlState) -> [NSObject : AnyObject]?     func setContentPositionAdjustment(_ adjustment: UIOffset, forSegmentType leftCenterRightOrAlone: UISegmentedControlSegment, barMetrics barMetrics: UIBarMetrics)     func contentPositionAdjustmentForSegmentType(_ leftCenterRightOrAlone: UISegmentedControlSegment, barMetrics barMetrics: UIBarMetrics) -> UIOffset } ``` | AnyObject, NSCoding |
| To | ``` class UISegmentedControl : UIControl, NSCoding {     init(items items: [AnyObject]?)     var segmentedControlStyle: UISegmentedControlStyle     var momentary: Bool     var numberOfSegments: Int { get }     var apportionsSegmentWidthsByContent: Bool     func insertSegmentWithTitle(_ title: String?, atIndex segment: Int, animated animated: Bool)     func insertSegmentWithImage(_ image: UIImage?, atIndex segment: Int, animated animated: Bool)     func removeSegmentAtIndex(_ segment: Int, animated animated: Bool)     func removeAllSegments()     func setTitle(_ title: String?, forSegmentAtIndex segment: Int)     func titleForSegmentAtIndex(_ segment: Int) -> String?     func setImage(_ image: UIImage?, forSegmentAtIndex segment: Int)     func imageForSegmentAtIndex(_ segment: Int) -> UIImage?     func setWidth(_ width: CGFloat, forSegmentAtIndex segment: Int)     func widthForSegmentAtIndex(_ segment: Int) -> CGFloat     func setContentOffset(_ offset: CGSize, forSegmentAtIndex segment: Int)     func contentOffsetForSegmentAtIndex(_ segment: Int) -> CGSize     func setEnabled(_ enabled: Bool, forSegmentAtIndex segment: Int)     func isEnabledForSegmentAtIndex(_ segment: Int) -> Bool     var selectedSegmentIndex: Int     var tintColor: UIColor!     func setBackgroundImage(_ backgroundImage: UIImage?, forState state: UIControlState, barMetrics barMetrics: UIBarMetrics)     func backgroundImageForState(_ state: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setDividerImage(_ dividerImage: UIImage?, forLeftSegmentState leftState: UIControlState, rightSegmentState rightState: UIControlState, barMetrics barMetrics: UIBarMetrics)     func dividerImageForLeftSegmentState(_ leftState: UIControlState, rightSegmentState rightState: UIControlState, barMetrics barMetrics: UIBarMetrics) -> UIImage?     func setTitleTextAttributes(_ attributes: [NSObject : AnyObject]?, forState state: UIControlState)     func titleTextAttributesForState(_ state: UIControlState) -> [NSObject : AnyObject]?     func setContentPositionAdjustment(_ adjustment: UIOffset, forSegmentType leftCenterRightOrAlone: UISegmentedControlSegment, barMetrics barMetrics: UIBarMetrics)     func contentPositionAdjustmentForSegmentType(_ leftCenterRightOrAlone: UISegmentedControlSegment, barMetrics barMetrics: UIBarMetrics) -> UIOffset } ``` | NSCoding |

Modified [UISegmentedControlSegment [enum]](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UISemanticContentAttribute [enum]](https://developer.apple.com/documentation/uikit/uisemanticcontentattribute)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UISimpleTextPrintFormatter](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UISlider](https://developer.apple.com/documentation/uikit/uislider)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UISlider : UIControl {     var value: Float     var minimumValue: Float     var maximumValue: Float     var minimumValueImage: UIImage?     var maximumValueImage: UIImage?     var continuous: Bool     var minimumTrackTintColor: UIColor?     var maximumTrackTintColor: UIColor?     var thumbTintColor: UIColor?     func setValue(_ value: Float, animated animated: Bool)     func setThumbImage(_ image: UIImage?, forState state: UIControlState)     func setMinimumTrackImage(_ image: UIImage?, forState state: UIControlState)     func setMaximumTrackImage(_ image: UIImage?, forState state: UIControlState)     func thumbImageForState(_ state: UIControlState) -> UIImage?     func minimumTrackImageForState(_ state: UIControlState) -> UIImage?     func maximumTrackImageForState(_ state: UIControlState) -> UIImage?     var currentThumbImage: UIImage? { get }     var currentMinimumTrackImage: UIImage? { get }     var currentMaximumTrackImage: UIImage? { get }     func minimumValueImageRectForBounds(_ bounds: CGRect) -> CGRect     func maximumValueImageRectForBounds(_ bounds: CGRect) -> CGRect     func trackRectForBounds(_ bounds: CGRect) -> CGRect     func thumbRectForBounds(_ bounds: CGRect, trackRect rect: CGRect, value value: Float) -> CGRect } ``` | AnyObject, NSCoding |
| To | ``` class UISlider : UIControl, NSCoding {     var value: Float     var minimumValue: Float     var maximumValue: Float     var minimumValueImage: UIImage?     var maximumValueImage: UIImage?     var continuous: Bool     var minimumTrackTintColor: UIColor?     var maximumTrackTintColor: UIColor?     var thumbTintColor: UIColor?     func setValue(_ value: Float, animated animated: Bool)     func setThumbImage(_ image: UIImage?, forState state: UIControlState)     func setMinimumTrackImage(_ image: UIImage?, forState state: UIControlState)     func setMaximumTrackImage(_ image: UIImage?, forState state: UIControlState)     func thumbImageForState(_ state: UIControlState) -> UIImage?     func minimumTrackImageForState(_ state: UIControlState) -> UIImage?     func maximumTrackImageForState(_ state: UIControlState) -> UIImage?     var currentThumbImage: UIImage? { get }     var currentMinimumTrackImage: UIImage? { get }     var currentMaximumTrackImage: UIImage? { get }     func minimumValueImageRectForBounds(_ bounds: CGRect) -> CGRect     func maximumValueImageRectForBounds(_ bounds: CGRect) -> CGRect     func trackRectForBounds(_ bounds: CGRect) -> CGRect     func thumbRectForBounds(_ bounds: CGRect, trackRect rect: CGRect, value value: Float) -> CGRect } ``` | NSCoding |

Modified [UISnapBehavior](https://developer.apple.com/documentation/uikit/uisnapbehavior)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UISplitViewControllerDisplayMode [enum]](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIStackView](https://developer.apple.com/documentation/uikit/uistackview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIStackViewAlignment [enum]](https://developer.apple.com/documentation/uikit/uistackview/alignment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIStackViewDistribution [enum]](https://developer.apple.com/documentation/uikit/uistackview/distribution)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIStatusBarAnimation [enum]](https://developer.apple.com/documentation/uikit/uistatusbaranimation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIStatusBarStyle [enum]](https://developer.apple.com/documentation/uikit/uistatusbarstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIStepper](https://developer.apple.com/documentation/uikit/uistepper)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIStoryboard](https://developer.apple.com/documentation/uikit/uistoryboard)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIStoryboardPopoverSegue](https://developer.apple.com/documentation/uikit/uistoryboardpopoversegue)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIStoryboardSegue](https://developer.apple.com/documentation/uikit/uistoryboardsegue)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIStoryboardUnwindSegueSource](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UISwipeGestureRecognizer](https://developer.apple.com/documentation/uikit/uiswipegesturerecognizer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UISwitch](https://developer.apple.com/documentation/uikit/uiswitch)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UISwitch : UIControl {     var onTintColor: UIColor?     var tintColor: UIColor!     var thumbTintColor: UIColor?     var onImage: UIImage?     var offImage: UIImage?     var on: Bool     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     func setOn(_ on: Bool, animated animated: Bool) } ``` | AnyObject, NSCoding |
| To | ``` class UISwitch : UIControl, NSCoding {     var onTintColor: UIColor?     var tintColor: UIColor!     var thumbTintColor: UIColor?     var onImage: UIImage?     var offImage: UIImage?     var on: Bool     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     func setOn(_ on: Bool, animated animated: Bool) } ``` | NSCoding |

Modified [UISystemAnimation [enum]](https://developer.apple.com/documentation/uikit/uisystemanimation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UITabBarController](https://developer.apple.com/documentation/uikit/uitabbarcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UITabBarController : UIViewController, UITabBarDelegate {     var viewControllers: [UIViewController]?     func setViewControllers(_ viewControllers: [UIViewController]?, animated animated: Bool)     unowned(unsafe) var selectedViewController: UIViewController?     var selectedIndex: Int     var moreNavigationController: UINavigationController { get }     var customizableViewControllers: [UIViewController]?     var tabBar: UITabBar { get }     weak var delegate: UITabBarControllerDelegate? } ``` | AnyObject, NSCoding, NSObjectProtocol, UITabBarDelegate |
| To | ``` class UITabBarController : UIViewController, UITabBarDelegate, NSCoding {     var viewControllers: [UIViewController]?     func setViewControllers(_ viewControllers: [UIViewController]?, animated animated: Bool)     unowned(unsafe) var selectedViewController: UIViewController?     var selectedIndex: Int     var moreNavigationController: UINavigationController { get }     var customizableViewControllers: [UIViewController]?     var tabBar: UITabBar { get }     weak var delegate: UITabBarControllerDelegate? } ``` | NSCoding, UITabBarDelegate |

Modified [UITabBarItem](https://developer.apple.com/documentation/uikit/uitabbaritem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UITabBarItemPositioning [enum]](https://developer.apple.com/documentation/uikit/uitabbaritempositioning)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITabBarSystemItem [enum]](https://developer.apple.com/documentation/uikit/uitabbaritem/systemitem)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITableView](https://developer.apple.com/documentation/uikit/uitableview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UITableView : UIScrollView {     init(frame frame: CGRect, style style: UITableViewStyle)     init?(coder aDecoder: NSCoder)     var style: UITableViewStyle { get }     weak var dataSource: UITableViewDataSource?     weak var delegate: UITableViewDelegate?     var rowHeight: CGFloat     var sectionHeaderHeight: CGFloat     var sectionFooterHeight: CGFloat     var estimatedRowHeight: CGFloat     var estimatedSectionHeaderHeight: CGFloat     var estimatedSectionFooterHeight: CGFloat     var separatorInset: UIEdgeInsets     var backgroundView: UIView?     func reloadData()     func reloadSectionIndexTitles()     var numberOfSections: Int { get }     func numberOfRowsInSection(_ section: Int) -> Int     func rectForSection(_ section: Int) -> CGRect     func rectForHeaderInSection(_ section: Int) -> CGRect     func rectForFooterInSection(_ section: Int) -> CGRect     func rectForRowAtIndexPath(_ indexPath: NSIndexPath) -> CGRect     func indexPathForRowAtPoint(_ point: CGPoint) -> NSIndexPath?     func indexPathForCell(_ cell: UITableViewCell) -> NSIndexPath?     func indexPathsForRowsInRect(_ rect: CGRect) -> [NSIndexPath]?     func cellForRowAtIndexPath(_ indexPath: NSIndexPath) -> UITableViewCell?     var visibleCells: [UITableViewCell] { get }     var indexPathsForVisibleRows: [NSIndexPath]? { get }     func headerViewForSection(_ section: Int) -> UITableViewHeaderFooterView?     func footerViewForSection(_ section: Int) -> UITableViewHeaderFooterView?     func scrollToRowAtIndexPath(_ indexPath: NSIndexPath, atScrollPosition scrollPosition: UITableViewScrollPosition, animated animated: Bool)     func scrollToNearestSelectedRowAtScrollPosition(_ scrollPosition: UITableViewScrollPosition, animated animated: Bool)     func beginUpdates()     func endUpdates()     func insertSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func deleteSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func reloadSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func moveSection(_ section: Int, toSection newSection: Int)     func insertRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation)     func deleteRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation)     func reloadRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation)     func moveRowAtIndexPath(_ indexPath: NSIndexPath, toIndexPath newIndexPath: NSIndexPath)     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var allowsSelection: Bool     var allowsSelectionDuringEditing: Bool     var allowsMultipleSelection: Bool     var allowsMultipleSelectionDuringEditing: Bool     var indexPathForSelectedRow: NSIndexPath? { get }     var indexPathsForSelectedRows: [NSIndexPath]? { get }     func selectRowAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool, scrollPosition scrollPosition: UITableViewScrollPosition)     func deselectRowAtIndexPath(_ indexPath: NSIndexPath, animated animated: Bool)     var sectionIndexMinimumDisplayRowCount: Int     var sectionIndexColor: UIColor?     var sectionIndexBackgroundColor: UIColor?     var sectionIndexTrackingBackgroundColor: UIColor?     var separatorStyle: UITableViewCellSeparatorStyle     var separatorColor: UIColor?     @NSCopying var separatorEffect: UIVisualEffect?     var cellLayoutMarginsFollowReadableWidth: Bool     var tableHeaderView: UIView?     var tableFooterView: UIView?     func dequeueReusableCellWithIdentifier(_ identifier: String) -> UITableViewCell?     func dequeueReusableCellWithIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath) -> UITableViewCell     func dequeueReusableHeaderFooterViewWithIdentifier(_ identifier: String) -> UITableViewHeaderFooterView?     func registerNib(_ nib: UINib?, forCellReuseIdentifier identifier: String)     func registerClass(_ cellClass: AnyClass?, forCellReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forHeaderFooterViewReuseIdentifier identifier: String)     func registerClass(_ aClass: AnyClass?, forHeaderFooterViewReuseIdentifier identifier: String) } ``` | AnyObject, NSCoding |
| To | ``` class UITableView : UIScrollView, NSCoding {     init(frame frame: CGRect, style style: UITableViewStyle)     init?(coder aDecoder: NSCoder)     var style: UITableViewStyle { get }     weak var dataSource: UITableViewDataSource?     weak var delegate: UITableViewDelegate?     var rowHeight: CGFloat     var sectionHeaderHeight: CGFloat     var sectionFooterHeight: CGFloat     var estimatedRowHeight: CGFloat     var estimatedSectionHeaderHeight: CGFloat     var estimatedSectionFooterHeight: CGFloat     var separatorInset: UIEdgeInsets     var backgroundView: UIView?     func reloadData()     func reloadSectionIndexTitles()     var numberOfSections: Int { get }     func numberOfRowsInSection(_ section: Int) -> Int     func rectForSection(_ section: Int) -> CGRect     func rectForHeaderInSection(_ section: Int) -> CGRect     func rectForFooterInSection(_ section: Int) -> CGRect     func rectForRowAtIndexPath(_ indexPath: NSIndexPath) -> CGRect     func indexPathForRowAtPoint(_ point: CGPoint) -> NSIndexPath?     func indexPathForCell(_ cell: UITableViewCell) -> NSIndexPath?     func indexPathsForRowsInRect(_ rect: CGRect) -> [NSIndexPath]?     func cellForRowAtIndexPath(_ indexPath: NSIndexPath) -> UITableViewCell?     var visibleCells: [UITableViewCell] { get }     var indexPathsForVisibleRows: [NSIndexPath]? { get }     func headerViewForSection(_ section: Int) -> UITableViewHeaderFooterView?     func footerViewForSection(_ section: Int) -> UITableViewHeaderFooterView?     func scrollToRowAtIndexPath(_ indexPath: NSIndexPath, atScrollPosition scrollPosition: UITableViewScrollPosition, animated animated: Bool)     func scrollToNearestSelectedRowAtScrollPosition(_ scrollPosition: UITableViewScrollPosition, animated animated: Bool)     func beginUpdates()     func endUpdates()     func insertSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func deleteSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func reloadSections(_ sections: NSIndexSet, withRowAnimation animation: UITableViewRowAnimation)     func moveSection(_ section: Int, toSection newSection: Int)     func insertRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation)     func deleteRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation)     func reloadRowsAtIndexPaths(_ indexPaths: [NSIndexPath], withRowAnimation animation: UITableViewRowAnimation)     func moveRowAtIndexPath(_ indexPath: NSIndexPath, toIndexPath newIndexPath: NSIndexPath)     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var allowsSelection: Bool     var allowsSelectionDuringEditing: Bool     var allowsMultipleSelection: Bool     var allowsMultipleSelectionDuringEditing: Bool     var indexPathForSelectedRow: NSIndexPath? { get }     var indexPathsForSelectedRows: [NSIndexPath]? { get }     func selectRowAtIndexPath(_ indexPath: NSIndexPath?, animated animated: Bool, scrollPosition scrollPosition: UITableViewScrollPosition)     func deselectRowAtIndexPath(_ indexPath: NSIndexPath, animated animated: Bool)     var sectionIndexMinimumDisplayRowCount: Int     var sectionIndexColor: UIColor?     var sectionIndexBackgroundColor: UIColor?     var sectionIndexTrackingBackgroundColor: UIColor?     var separatorStyle: UITableViewCellSeparatorStyle     var separatorColor: UIColor?     @NSCopying var separatorEffect: UIVisualEffect?     var cellLayoutMarginsFollowReadableWidth: Bool     var tableHeaderView: UIView?     var tableFooterView: UIView?     func dequeueReusableCellWithIdentifier(_ identifier: String) -> UITableViewCell?     func dequeueReusableCellWithIdentifier(_ identifier: String, forIndexPath indexPath: NSIndexPath) -> UITableViewCell     func dequeueReusableHeaderFooterViewWithIdentifier(_ identifier: String) -> UITableViewHeaderFooterView?     func registerNib(_ nib: UINib?, forCellReuseIdentifier identifier: String)     func registerClass(_ cellClass: AnyClass?, forCellReuseIdentifier identifier: String)     func registerNib(_ nib: UINib?, forHeaderFooterViewReuseIdentifier identifier: String)     func registerClass(_ aClass: AnyClass?, forHeaderFooterViewReuseIdentifier identifier: String)     var remembersLastFocusedIndexPath: Bool } ``` | NSCoding |

Modified [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UITableViewCell : UIView, UIGestureRecognizerDelegate {     init(style style: UITableViewCellStyle, reuseIdentifier reuseIdentifier: String?)     init?(coder aDecoder: NSCoder)     var imageView: UIImageView? { get }     var textLabel: UILabel? { get }     var detailTextLabel: UILabel? { get }     var contentView: UIView { get }     var backgroundView: UIView?     var selectedBackgroundView: UIView?     var multipleSelectionBackgroundView: UIView?     var reuseIdentifier: String? { get }     func prepareForReuse()     var selectionStyle: UITableViewCellSelectionStyle     var selected: Bool     var highlighted: Bool     func setSelected(_ selected: Bool, animated animated: Bool)     func setHighlighted(_ highlighted: Bool, animated animated: Bool)     var editingStyle: UITableViewCellEditingStyle { get }     var showsReorderControl: Bool     var shouldIndentWhileEditing: Bool     var accessoryType: UITableViewCellAccessoryType     var accessoryView: UIView?     var editingAccessoryType: UITableViewCellAccessoryType     var editingAccessoryView: UIView?     var indentationLevel: Int     var indentationWidth: CGFloat     var separatorInset: UIEdgeInsets     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var showingDeleteConfirmation: Bool { get }     func willTransitionToState(_ state: UITableViewCellStateMask)     func didTransitionToState(_ state: UITableViewCellStateMask) } extension UITableViewCell {     convenience init(frame frame: CGRect, reuseIdentifier reuseIdentifier: String?)     var text: String?     var font: UIFont?     var textAlignment: NSTextAlignment     var lineBreakMode: NSLineBreakMode     var textColor: UIColor?     var selectedTextColor: UIColor?     var image: UIImage?     var selectedImage: UIImage?     var hidesAccessoryWhenEditing: Bool     unowned(unsafe) var target: AnyObject?     var editAction: Selector     var accessoryAction: Selector } ``` | AnyObject, NSCoding, NSObjectProtocol, UIGestureRecognizerDelegate |
| To | ``` class UITableViewCell : UIView, NSCoding, UIGestureRecognizerDelegate {     init(style style: UITableViewCellStyle, reuseIdentifier reuseIdentifier: String?)     init?(coder aDecoder: NSCoder)     var imageView: UIImageView? { get }     var textLabel: UILabel? { get }     var detailTextLabel: UILabel? { get }     var contentView: UIView { get }     var backgroundView: UIView?     var selectedBackgroundView: UIView?     var multipleSelectionBackgroundView: UIView?     var reuseIdentifier: String? { get }     func prepareForReuse()     var selectionStyle: UITableViewCellSelectionStyle     var selected: Bool     var highlighted: Bool     func setSelected(_ selected: Bool, animated animated: Bool)     func setHighlighted(_ highlighted: Bool, animated animated: Bool)     var editingStyle: UITableViewCellEditingStyle { get }     var showsReorderControl: Bool     var shouldIndentWhileEditing: Bool     var accessoryType: UITableViewCellAccessoryType     var accessoryView: UIView?     var editingAccessoryType: UITableViewCellAccessoryType     var editingAccessoryView: UIView?     var indentationLevel: Int     var indentationWidth: CGFloat     var separatorInset: UIEdgeInsets     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var showingDeleteConfirmation: Bool { get }     var focusStyle: UITableViewCellFocusStyle     func willTransitionToState(_ state: UITableViewCellStateMask)     func didTransitionToState(_ state: UITableViewCellStateMask) } extension UITableViewCell {     convenience init(frame frame: CGRect, reuseIdentifier reuseIdentifier: String?)     var text: String?     var font: UIFont?     var textAlignment: NSTextAlignment     var lineBreakMode: NSLineBreakMode     var textColor: UIColor?     var selectedTextColor: UIColor?     var image: UIImage?     var selectedImage: UIImage?     var hidesAccessoryWhenEditing: Bool     unowned(unsafe) var target: AnyObject?     var editAction: Selector     var accessoryAction: Selector } ``` | NSCoding, UIGestureRecognizerDelegate |

Modified [UITableViewCellAccessoryType [enum]](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITableViewCellEditingStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewcelleditingstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITableViewCellSelectionStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewcellselectionstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITableViewCellSeparatorStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewcellseparatorstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITableViewCellStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewcellstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITableViewController](https://developer.apple.com/documentation/uikit/uitableviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UITableViewController : UIViewController, UITableViewDelegate, UIScrollViewDelegate, UITableViewDataSource {     init(style style: UITableViewStyle)     init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     init?(coder aDecoder: NSCoder)     var tableView: UITableView!     var clearsSelectionOnViewWillAppear: Bool     var refreshControl: UIRefreshControl? } ``` | AnyObject, NSObjectProtocol, UIScrollViewDelegate, UITableViewDataSource, UITableViewDelegate |
| To | ``` class UITableViewController : UIViewController, UITableViewDelegate, UITableViewDataSource {     init(style style: UITableViewStyle)     init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     init?(coder aDecoder: NSCoder)     var tableView: UITableView!     var clearsSelectionOnViewWillAppear: Bool     var refreshControl: UIRefreshControl? } ``` | UITableViewDataSource, UITableViewDelegate |

Modified [UITableViewDelegate](https://developer.apple.com/documentation/uikit/uitableviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol UITableViewDelegate : NSObjectProtocol, UIScrollViewDelegate {     optional func tableView(_ tableView: UITableView, willDisplayCell cell: UITableViewCell, forRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, willDisplayHeaderView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, willDisplayFooterView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, didEndDisplayingCell cell: UITableViewCell, forRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didEndDisplayingHeaderView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, didEndDisplayingFooterView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat     optional func tableView(_ tableView: UITableView, heightForHeaderInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, heightForFooterInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForHeaderInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForFooterInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, viewForHeaderInSection section: Int) -> UIView?     optional func tableView(_ tableView: UITableView, viewForFooterInSection section: Int) -> UIView?     optional func tableView(_ tableView: UITableView, accessoryTypeForRowWithIndexPath indexPath: NSIndexPath) -> UITableViewCellAccessoryType     optional func tableView(_ tableView: UITableView, accessoryButtonTappedForRowWithIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, shouldHighlightRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, didHighlightRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didUnhighlightRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, willSelectRowAtIndexPath indexPath: NSIndexPath) -> NSIndexPath?     optional func tableView(_ tableView: UITableView, willDeselectRowAtIndexPath indexPath: NSIndexPath) -> NSIndexPath?     optional func tableView(_ tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didDeselectRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, editingStyleForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCellEditingStyle     optional func tableView(_ tableView: UITableView, titleForDeleteConfirmationButtonForRowAtIndexPath indexPath: NSIndexPath) -> String?     optional func tableView(_ tableView: UITableView, editActionsForRowAtIndexPath indexPath: NSIndexPath) -> [UITableViewRowAction]?     optional func tableView(_ tableView: UITableView, shouldIndentWhileEditingRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, willBeginEditingRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didEndEditingRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, targetIndexPathForMoveFromRowAtIndexPath sourceIndexPath: NSIndexPath, toProposedIndexPath proposedDestinationIndexPath: NSIndexPath) -> NSIndexPath     optional func tableView(_ tableView: UITableView, indentationLevelForRowAtIndexPath indexPath: NSIndexPath) -> Int     optional func tableView(_ tableView: UITableView, shouldShowMenuForRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, canPerformAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) -> Bool     optional func tableView(_ tableView: UITableView, performAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) } ``` |
| To | ``` protocol UITableViewDelegate : NSObjectProtocol, UIScrollViewDelegate {     optional func tableView(_ tableView: UITableView, willDisplayCell cell: UITableViewCell, forRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, willDisplayHeaderView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, willDisplayFooterView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, didEndDisplayingCell cell: UITableViewCell, forRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didEndDisplayingHeaderView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, didEndDisplayingFooterView view: UIView, forSection section: Int)     optional func tableView(_ tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat     optional func tableView(_ tableView: UITableView, heightForHeaderInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, heightForFooterInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForHeaderInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, estimatedHeightForFooterInSection section: Int) -> CGFloat     optional func tableView(_ tableView: UITableView, viewForHeaderInSection section: Int) -> UIView?     optional func tableView(_ tableView: UITableView, viewForFooterInSection section: Int) -> UIView?     optional func tableView(_ tableView: UITableView, accessoryTypeForRowWithIndexPath indexPath: NSIndexPath) -> UITableViewCellAccessoryType     optional func tableView(_ tableView: UITableView, accessoryButtonTappedForRowWithIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, shouldHighlightRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, didHighlightRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didUnhighlightRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, willSelectRowAtIndexPath indexPath: NSIndexPath) -> NSIndexPath?     optional func tableView(_ tableView: UITableView, willDeselectRowAtIndexPath indexPath: NSIndexPath) -> NSIndexPath?     optional func tableView(_ tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didDeselectRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, editingStyleForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCellEditingStyle     optional func tableView(_ tableView: UITableView, titleForDeleteConfirmationButtonForRowAtIndexPath indexPath: NSIndexPath) -> String?     optional func tableView(_ tableView: UITableView, editActionsForRowAtIndexPath indexPath: NSIndexPath) -> [UITableViewRowAction]?     optional func tableView(_ tableView: UITableView, shouldIndentWhileEditingRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, willBeginEditingRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, didEndEditingRowAtIndexPath indexPath: NSIndexPath)     optional func tableView(_ tableView: UITableView, targetIndexPathForMoveFromRowAtIndexPath sourceIndexPath: NSIndexPath, toProposedIndexPath proposedDestinationIndexPath: NSIndexPath) -> NSIndexPath     optional func tableView(_ tableView: UITableView, indentationLevelForRowAtIndexPath indexPath: NSIndexPath) -> Int     optional func tableView(_ tableView: UITableView, shouldShowMenuForRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, canPerformAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?) -> Bool     optional func tableView(_ tableView: UITableView, performAction action: Selector, forRowAtIndexPath indexPath: NSIndexPath, withSender sender: AnyObject?)     optional func tableView(_ tableView: UITableView, canFocusRowAtIndexPath indexPath: NSIndexPath) -> Bool     optional func tableView(_ tableView: UITableView, shouldUpdateFocusInContext context: UITableViewFocusUpdateContext) -> Bool     optional func tableView(_ tableView: UITableView, didUpdateFocusInContext context: UITableViewFocusUpdateContext, withAnimationCoordinator coordinator: UIFocusAnimationCoordinator)     optional func indexPathForPreferredFocusedViewInTableView(_ tableView: UITableView) -> NSIndexPath? } ``` |

Modified [UITableViewHeaderFooterView](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UITableViewRowAction](https://developer.apple.com/documentation/uikit/uitableviewrowaction)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [UITableViewRowActionStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewrowaction/style)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITableViewRowAnimation [enum]](https://developer.apple.com/documentation/uikit/uitableviewrowanimation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITableViewScrollPosition [enum]](https://developer.apple.com/documentation/uikit/uitableview/scrollposition)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITableViewStyle [enum]](https://developer.apple.com/documentation/uikit/uitableviewstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITapGestureRecognizer](https://developer.apple.com/documentation/uikit/uitapgesturerecognizer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UITextAutocapitalizationType [enum]](https://developer.apple.com/documentation/uikit/uitextautocapitalizationtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITextAutocorrectionType [enum]](https://developer.apple.com/documentation/uikit/uitextautocorrectiontype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITextBorderStyle [enum]](https://developer.apple.com/documentation/uikit/uitextfield/borderstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITextChecker](https://developer.apple.com/documentation/uikit/uitextchecker)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UITextDocumentProxy](https://developer.apple.com/documentation/uikit/uitextdocumentproxy)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UITextDocumentProxy : UIKeyInput, UITextInputTraits, NSObjectProtocol {     var documentContextBeforeInput: String? { get }     var documentContextAfterInput: String? { get }     func adjustTextPositionByCharacterOffset(_ offset: Int) } ``` | NSObjectProtocol, UIKeyInput, UITextInputTraits |
| To | ``` protocol UITextDocumentProxy : UIKeyInput {     var documentContextBeforeInput: String? { get }     var documentContextAfterInput: String? { get }     func adjustTextPositionByCharacterOffset(_ offset: Int) } ``` | UIKeyInput |

Modified [UITextField](https://developer.apple.com/documentation/uikit/uitextfield)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UITextField : UIControl, UITextInput, UIKeyInput, UITextInputTraits {     var text: String?     @NSCopying var attributedText: NSAttributedString?     var textColor: UIColor?     var font: UIFont?     var textAlignment: NSTextAlignment     var borderStyle: UITextBorderStyle     var defaultTextAttributes: [String : AnyObject]     var placeholder: String?     @NSCopying var attributedPlaceholder: NSAttributedString?     var clearsOnBeginEditing: Bool     var adjustsFontSizeToFitWidth: Bool     var minimumFontSize: CGFloat     weak var delegate: UITextFieldDelegate?     var background: UIImage?     var disabledBackground: UIImage?     var editing: Bool { get }     var allowsEditingTextAttributes: Bool     var typingAttributes: [String : AnyObject]?     var clearButtonMode: UITextFieldViewMode     var leftView: UIView?     var leftViewMode: UITextFieldViewMode     var rightView: UIView?     var rightViewMode: UITextFieldViewMode     func borderRectForBounds(_ bounds: CGRect) -> CGRect     func textRectForBounds(_ bounds: CGRect) -> CGRect     func placeholderRectForBounds(_ bounds: CGRect) -> CGRect     func editingRectForBounds(_ bounds: CGRect) -> CGRect     func clearButtonRectForBounds(_ bounds: CGRect) -> CGRect     func leftViewRectForBounds(_ bounds: CGRect) -> CGRect     func rightViewRectForBounds(_ bounds: CGRect) -> CGRect     func drawTextInRect(_ rect: CGRect)     func drawPlaceholderInRect(_ rect: CGRect)     var inputView: UIView?     var inputAccessoryView: UIView?     var clearsOnInsertion: Bool } ``` | AnyObject, NSCoding, NSObjectProtocol, UIKeyInput, UITextInput, UITextInputTraits |
| To | ``` class UITextField : UIControl, UITextInput, NSCoding {     var text: String?     @NSCopying var attributedText: NSAttributedString?     var textColor: UIColor?     var font: UIFont?     var textAlignment: NSTextAlignment     var borderStyle: UITextBorderStyle     var defaultTextAttributes: [String : AnyObject]     var placeholder: String?     @NSCopying var attributedPlaceholder: NSAttributedString?     var clearsOnBeginEditing: Bool     var adjustsFontSizeToFitWidth: Bool     var minimumFontSize: CGFloat     weak var delegate: UITextFieldDelegate?     var background: UIImage?     var disabledBackground: UIImage?     var editing: Bool { get }     var allowsEditingTextAttributes: Bool     var typingAttributes: [String : AnyObject]?     var clearButtonMode: UITextFieldViewMode     var leftView: UIView?     var leftViewMode: UITextFieldViewMode     var rightView: UIView?     var rightViewMode: UITextFieldViewMode     func borderRectForBounds(_ bounds: CGRect) -> CGRect     func textRectForBounds(_ bounds: CGRect) -> CGRect     func placeholderRectForBounds(_ bounds: CGRect) -> CGRect     func editingRectForBounds(_ bounds: CGRect) -> CGRect     func clearButtonRectForBounds(_ bounds: CGRect) -> CGRect     func leftViewRectForBounds(_ bounds: CGRect) -> CGRect     func rightViewRectForBounds(_ bounds: CGRect) -> CGRect     func drawTextInRect(_ rect: CGRect)     func drawPlaceholderInRect(_ rect: CGRect)     var inputView: UIView?     var inputAccessoryView: UIView?     var clearsOnInsertion: Bool } ``` | NSCoding, UITextInput |

Modified [UITextFieldViewMode [enum]](https://developer.apple.com/documentation/uikit/uitextfield/viewmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITextGranularity [enum]](https://developer.apple.com/documentation/uikit/uitextgranularity)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UITextInput : UIKeyInput, UITextInputTraits, NSObjectProtocol {     func textInRange(_ range: UITextRange) -> String?     func replaceRange(_ range: UITextRange, withText text: String)     @NSCopying var selectedTextRange: UITextRange? { get set }     var markedTextRange: UITextRange? { get }     var markedTextStyle: [NSObject : AnyObject]? { get set }     func setMarkedText(_ markedText: String?, selectedRange selectedRange: NSRange)     func unmarkText()     var beginningOfDocument: UITextPosition { get }     var endOfDocument: UITextPosition { get }     func textRangeFromPosition(_ fromPosition: UITextPosition, toPosition toPosition: UITextPosition) -> UITextRange?     func positionFromPosition(_ position: UITextPosition, offset offset: Int) -> UITextPosition?     func positionFromPosition(_ position: UITextPosition, inDirection direction: UITextLayoutDirection, offset offset: Int) -> UITextPosition?     func comparePosition(_ position: UITextPosition, toPosition other: UITextPosition) -> NSComparisonResult     func offsetFromPosition(_ from: UITextPosition, toPosition toPosition: UITextPosition) -> Int     weak var inputDelegate: UITextInputDelegate? { get set }     var tokenizer: UITextInputTokenizer { get }     func positionWithinRange(_ range: UITextRange, farthestInDirection direction: UITextLayoutDirection) -> UITextPosition?     func characterRangeByExtendingPosition(_ position: UITextPosition, inDirection direction: UITextLayoutDirection) -> UITextRange?     func baseWritingDirectionForPosition(_ position: UITextPosition, inDirection direction: UITextStorageDirection) -> UITextWritingDirection     func setBaseWritingDirection(_ writingDirection: UITextWritingDirection, forRange range: UITextRange)     func firstRectForRange(_ range: UITextRange) -> CGRect     func caretRectForPosition(_ position: UITextPosition) -> CGRect     func selectionRectsForRange(_ range: UITextRange) -> [AnyObject]     func closestPositionToPoint(_ point: CGPoint) -> UITextPosition?     func closestPositionToPoint(_ point: CGPoint, withinRange range: UITextRange) -> UITextPosition?     func characterRangeAtPoint(_ point: CGPoint) -> UITextRange?     optional func shouldChangeTextInRange(_ range: UITextRange, replacementText text: String) -> Bool     optional func textStylingAtPosition(_ position: UITextPosition, inDirection direction: UITextStorageDirection) -> [String : AnyObject]?     optional func positionWithinRange(_ range: UITextRange, atCharacterOffset offset: Int) -> UITextPosition?     optional func characterOffsetOfPosition(_ position: UITextPosition, withinRange range: UITextRange) -> Int     optional var textInputView: UIView { get }     optional var selectionAffinity: UITextStorageDirection { get set }     optional func insertDictationResult(_ dictationResult: [UIDictationPhrase])     optional func dictationRecordingDidEnd()     optional func dictationRecognitionFailed()     optional func insertDictationResultPlaceholder() -> AnyObject     optional func frameForDictationResultPlaceholder(_ placeholder: AnyObject) -> CGRect     optional func removeDictationResultPlaceholder(_ placeholder: AnyObject, willInsertResult willInsertResult: Bool)     optional func beginFloatingCursorAtPoint(_ point: CGPoint)     optional func updateFloatingCursorAtPoint(_ point: CGPoint)     optional func endFloatingCursor() } ``` | NSObjectProtocol, UIKeyInput, UITextInputTraits |
| To | ``` protocol UITextInput : UIKeyInput {     func textInRange(_ range: UITextRange) -> String?     func replaceRange(_ range: UITextRange, withText text: String)     @NSCopying var selectedTextRange: UITextRange? { get set }     var markedTextRange: UITextRange? { get }     var markedTextStyle: [NSObject : AnyObject]? { get set }     func setMarkedText(_ markedText: String?, selectedRange selectedRange: NSRange)     func unmarkText()     var beginningOfDocument: UITextPosition { get }     var endOfDocument: UITextPosition { get }     func textRangeFromPosition(_ fromPosition: UITextPosition, toPosition toPosition: UITextPosition) -> UITextRange?     func positionFromPosition(_ position: UITextPosition, offset offset: Int) -> UITextPosition?     func positionFromPosition(_ position: UITextPosition, inDirection direction: UITextLayoutDirection, offset offset: Int) -> UITextPosition?     func comparePosition(_ position: UITextPosition, toPosition other: UITextPosition) -> NSComparisonResult     func offsetFromPosition(_ from: UITextPosition, toPosition toPosition: UITextPosition) -> Int     weak var inputDelegate: UITextInputDelegate? { get set }     var tokenizer: UITextInputTokenizer { get }     func positionWithinRange(_ range: UITextRange, farthestInDirection direction: UITextLayoutDirection) -> UITextPosition?     func characterRangeByExtendingPosition(_ position: UITextPosition, inDirection direction: UITextLayoutDirection) -> UITextRange?     func baseWritingDirectionForPosition(_ position: UITextPosition, inDirection direction: UITextStorageDirection) -> UITextWritingDirection     func setBaseWritingDirection(_ writingDirection: UITextWritingDirection, forRange range: UITextRange)     func firstRectForRange(_ range: UITextRange) -> CGRect     func caretRectForPosition(_ position: UITextPosition) -> CGRect     func selectionRectsForRange(_ range: UITextRange) -> [AnyObject]     func closestPositionToPoint(_ point: CGPoint) -> UITextPosition?     func closestPositionToPoint(_ point: CGPoint, withinRange range: UITextRange) -> UITextPosition?     func characterRangeAtPoint(_ point: CGPoint) -> UITextRange?     optional func shouldChangeTextInRange(_ range: UITextRange, replacementText text: String) -> Bool     optional func textStylingAtPosition(_ position: UITextPosition, inDirection direction: UITextStorageDirection) -> [String : AnyObject]?     optional func positionWithinRange(_ range: UITextRange, atCharacterOffset offset: Int) -> UITextPosition?     optional func characterOffsetOfPosition(_ position: UITextPosition, withinRange range: UITextRange) -> Int     optional var textInputView: UIView { get }     optional var selectionAffinity: UITextStorageDirection { get set }     optional func insertDictationResult(_ dictationResult: [UIDictationPhrase])     optional func dictationRecordingDidEnd()     optional func dictationRecognitionFailed()     optional func insertDictationResultPlaceholder() -> AnyObject     optional func frameForDictationResultPlaceholder(_ placeholder: AnyObject) -> CGRect     optional func removeDictationResultPlaceholder(_ placeholder: AnyObject, willInsertResult willInsertResult: Bool)     optional func beginFloatingCursorAtPoint(_ point: CGPoint)     optional func updateFloatingCursorAtPoint(_ point: CGPoint)     optional func endFloatingCursor() } ``` | UIKeyInput |

Modified [UITextInputAssistantItem](https://developer.apple.com/documentation/uikit/uitextinputassistantitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UITextInputMode](https://developer.apple.com/documentation/uikit/uitextinputmode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UITextInputMode : NSObject, NSSecureCoding, NSCoding {     var primaryLanguage: String? { get }     class func currentInputMode() -> UITextInputMode?     class func activeInputModes() -> [String] } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class UITextInputMode : NSObject, NSSecureCoding {     var primaryLanguage: String? { get }     class func currentInputMode() -> UITextInputMode?     class func activeInputModes() -> [String] } ``` | NSSecureCoding |

Modified [UITextInputStringTokenizer](https://developer.apple.com/documentation/uikit/uitextinputstringtokenizer)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, UITextInputTokenizer |
| To | UITextInputTokenizer |

Modified [UITextLayoutDirection [enum]](https://developer.apple.com/documentation/uikit/uitextlayoutdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITextPosition](https://developer.apple.com/documentation/uikit/uitextposition)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UITextRange](https://developer.apple.com/documentation/uikit/uitextrange)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UITextSelectionRect](https://developer.apple.com/documentation/uikit/uitextselectionrect)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UITextSpellCheckingType [enum]](https://developer.apple.com/documentation/uikit/uitextspellcheckingtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITextStorageDirection [enum]](https://developer.apple.com/documentation/uikit/uitextstoragedirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITextView](https://developer.apple.com/documentation/uikit/uitextview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UITextView : UIScrollView, UITextInput, UIKeyInput, UITextInputTraits {     weak var delegate: UITextViewDelegate?     var text: String!     var font: UIFont?     var textColor: UIColor?     var textAlignment: NSTextAlignment     var selectedRange: NSRange     var editable: Bool     var selectable: Bool     var dataDetectorTypes: UIDataDetectorTypes     var allowsEditingTextAttributes: Bool     @NSCopying var attributedText: NSAttributedString!     var typingAttributes: [String : AnyObject]     func scrollRangeToVisible(_ range: NSRange)     var inputView: UIView?     var inputAccessoryView: UIView?     var clearsOnInsertion: Bool     init(frame frame: CGRect, textContainer textContainer: NSTextContainer?)     init?(coder aDecoder: NSCoder)     var textContainer: NSTextContainer { get }     var textContainerInset: UIEdgeInsets     var layoutManager: NSLayoutManager { get }     var textStorage: NSTextStorage { get }     var linkTextAttributes: [String : AnyObject]! } ``` | AnyObject, NSObjectProtocol, UIKeyInput, UITextInput, UITextInputTraits |
| To | ``` class UITextView : UIScrollView, UITextInput {     weak var delegate: UITextViewDelegate?     var text: String!     var font: UIFont?     var textColor: UIColor?     var textAlignment: NSTextAlignment     var selectedRange: NSRange     var editable: Bool     var selectable: Bool     var dataDetectorTypes: UIDataDetectorTypes     var allowsEditingTextAttributes: Bool     @NSCopying var attributedText: NSAttributedString!     var typingAttributes: [String : AnyObject]     func scrollRangeToVisible(_ range: NSRange)     var inputView: UIView?     var inputAccessoryView: UIView?     var clearsOnInsertion: Bool     init(frame frame: CGRect, textContainer textContainer: NSTextContainer?)     init?(coder aDecoder: NSCoder)     var textContainer: NSTextContainer { get }     var textContainerInset: UIEdgeInsets     var layoutManager: NSLayoutManager { get }     var textStorage: NSTextStorage { get }     var linkTextAttributes: [String : AnyObject]! } ``` | UITextInput |

Modified [UITextWritingDirection [enum]](https://developer.apple.com/documentation/uikit/uitextwritingdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIToolbar](https://developer.apple.com/documentation/uikit/uitoolbar)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, UIBarPositioning |
| To | UIBarPositioning |

Modified [UIToolbarDelegate](https://developer.apple.com/documentation/uikit/uitoolbardelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UIToolbarDelegate : UIBarPositioningDelegate, NSObjectProtocol { } ``` | NSObjectProtocol, UIBarPositioningDelegate |
| To | ``` protocol UIToolbarDelegate : UIBarPositioningDelegate { } ``` | UIBarPositioningDelegate |

Modified [UITouch](https://developer.apple.com/documentation/uikit/uitouch)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UITouch : NSObject {     var timestamp: NSTimeInterval { get }     var phase: UITouchPhase { get }     var tapCount: Int { get }     var majorRadius: CGFloat { get }     var majorRadiusTolerance: CGFloat { get }     var window: UIWindow? { get }     var view: UIView? { get }     var gestureRecognizers: [UIGestureRecognizer]? { get }     func locationInView(_ view: UIView?) -> CGPoint     func previousLocationInView(_ view: UIView?) -> CGPoint     var force: CGFloat { get }     var maximumPossibleForce: CGFloat { get } } extension UITouch {     func locationInNode(_ node: SKNode) -> CGPoint     func previousLocationInNode(_ node: SKNode) -> CGPoint } ``` | AnyObject |
| To | ``` class UITouch : NSObject {     var timestamp: NSTimeInterval { get }     var phase: UITouchPhase { get }     var tapCount: Int { get }     var type: UITouchType { get }     var majorRadius: CGFloat { get }     var majorRadiusTolerance: CGFloat { get }     var window: UIWindow? { get }     var view: UIView? { get }     var gestureRecognizers: [UIGestureRecognizer]? { get }     func locationInView(_ view: UIView?) -> CGPoint     func previousLocationInView(_ view: UIView?) -> CGPoint     func preciseLocationInView(_ view: UIView?) -> CGPoint     func precisePreviousLocationInView(_ view: UIView?) -> CGPoint     var force: CGFloat { get }     var maximumPossibleForce: CGFloat { get }     func azimuthAngleInView(_ view: UIView?) -> CGFloat     func azimuthUnitVectorInView(_ view: UIView?) -> CGVector     var altitudeAngle: CGFloat { get }     var estimationUpdateIndex: NSNumber? { get }     var estimatedProperties: UITouchProperties { get }     var estimatedPropertiesExpectingUpdates: UITouchProperties { get } } extension UITouch {     func locationInNode(_ node: SKNode) -> CGPoint     func previousLocationInNode(_ node: SKNode) -> CGPoint } ``` | -- |

Modified [UITouchPhase [enum]](https://developer.apple.com/documentation/uikit/uitouch/phase)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UITraitCollection](https://developer.apple.com/documentation/uikit/uitraitcollection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UITraitCollection : NSObject, NSCopying, NSSecureCoding, NSCoding {     init()     init?(coder aDecoder: NSCoder)     func containsTraitsInCollection(_ trait: UITraitCollection?) -> Bool      init(traitsFromCollections traitCollections: [UITraitCollection])     class func traitCollectionWithTraitsFromCollections(_ traitCollections: [UITraitCollection]) -> UITraitCollection      init(userInterfaceIdiom idiom: UIUserInterfaceIdiom)     class func traitCollectionWithUserInterfaceIdiom(_ idiom: UIUserInterfaceIdiom) -> UITraitCollection     var userInterfaceIdiom: UIUserInterfaceIdiom { get }      init(displayScale scale: CGFloat)     class func traitCollectionWithDisplayScale(_ scale: CGFloat) -> UITraitCollection     var displayScale: CGFloat { get }      init(horizontalSizeClass horizontalSizeClass: UIUserInterfaceSizeClass)     class func traitCollectionWithHorizontalSizeClass(_ horizontalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection     var horizontalSizeClass: UIUserInterfaceSizeClass { get }      init(verticalSizeClass verticalSizeClass: UIUserInterfaceSizeClass)     class func traitCollectionWithVerticalSizeClass(_ verticalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection     var verticalSizeClass: UIUserInterfaceSizeClass { get }      init(forceTouchCapability capability: UIForceTouchCapability)     class func traitCollectionWithForceTouchCapability(_ capability: UIForceTouchCapability) -> UITraitCollection     var forceTouchCapability: UIForceTouchCapability { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class UITraitCollection : NSObject, NSCopying, NSSecureCoding {     init()     init?(coder aDecoder: NSCoder)     func containsTraitsInCollection(_ trait: UITraitCollection?) -> Bool      init(traitsFromCollections traitCollections: [UITraitCollection])     class func traitCollectionWithTraitsFromCollections(_ traitCollections: [UITraitCollection]) -> UITraitCollection      init(userInterfaceIdiom idiom: UIUserInterfaceIdiom)     class func traitCollectionWithUserInterfaceIdiom(_ idiom: UIUserInterfaceIdiom) -> UITraitCollection     var userInterfaceIdiom: UIUserInterfaceIdiom { get }      init(displayScale scale: CGFloat)     class func traitCollectionWithDisplayScale(_ scale: CGFloat) -> UITraitCollection     var displayScale: CGFloat { get }      init(horizontalSizeClass horizontalSizeClass: UIUserInterfaceSizeClass)     class func traitCollectionWithHorizontalSizeClass(_ horizontalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection     var horizontalSizeClass: UIUserInterfaceSizeClass { get }      init(verticalSizeClass verticalSizeClass: UIUserInterfaceSizeClass)     class func traitCollectionWithVerticalSizeClass(_ verticalSizeClass: UIUserInterfaceSizeClass) -> UITraitCollection     var verticalSizeClass: UIUserInterfaceSizeClass { get }      init(forceTouchCapability capability: UIForceTouchCapability)     class func traitCollectionWithForceTouchCapability(_ capability: UIForceTouchCapability) -> UITraitCollection     var forceTouchCapability: UIForceTouchCapability { get } } ``` | NSCopying, NSSecureCoding |

Modified [UIUserInterfaceIdiom [enum]](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum UIUserInterfaceIdiom : Int {     case Unspecified     case Phone     case Pad } ``` | Equatable, Hashable, RawRepresentable |
| To | ``` enum UIUserInterfaceIdiom : Int {     case Unspecified     case Phone     case Pad     case TV } ``` | -- |

Modified [UIUserInterfaceLayoutDirection [enum]](https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIUserInterfaceSizeClass [enum]](https://developer.apple.com/documentation/uikit/uiuserinterfacesizeclass)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIUserNotificationAction](https://developer.apple.com/documentation/uikit/uiusernotificationaction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIUserNotificationAction : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     init()     init?(coder aDecoder: NSCoder)     var identifier: String? { get }     var title: String? { get }     var behavior: UIUserNotificationActionBehavior { get }     var parameters: [NSObject : AnyObject] { get }     var activationMode: UIUserNotificationActivationMode { get }     var authenticationRequired: Bool { get }     var destructive: Bool { get } } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class UIUserNotificationAction : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     init()     init?(coder aDecoder: NSCoder)     var identifier: String? { get }     var title: String? { get }     var behavior: UIUserNotificationActionBehavior { get }     var parameters: [NSObject : AnyObject] { get }     var activationMode: UIUserNotificationActivationMode { get }     var authenticationRequired: Bool { get }     var destructive: Bool { get } } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [UIUserNotificationActionBehavior [enum]](https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIUserNotificationActionContext [enum]](https://developer.apple.com/documentation/uikit/uiusernotificationactioncontext)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIUserNotificationActivationMode [enum]](https://developer.apple.com/documentation/uikit/uiusernotificationactivationmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIUserNotificationCategory](https://developer.apple.com/documentation/uikit/uiusernotificationcategory)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIUserNotificationCategory : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     init()     init?(coder aDecoder: NSCoder)     var identifier: String? { get }     func actionsForContext(_ context: UIUserNotificationActionContext) -> [UIUserNotificationAction]? } ``` | AnyObject, NSCoding, NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class UIUserNotificationCategory : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     init()     init?(coder aDecoder: NSCoder)     var identifier: String? { get }     func actionsForContext(_ context: UIUserNotificationActionContext) -> [UIUserNotificationAction]? } ``` | NSCopying, NSMutableCopying, NSSecureCoding |

Modified [UIUserNotificationSettings](https://developer.apple.com/documentation/uikit/uiusernotificationsettings)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIVibrancyEffect](https://developer.apple.com/documentation/uikit/uivibrancyeffect)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIVideoEditorController](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIView](https://developer.apple.com/documentation/uikit/uiview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIView : UIResponder, NSCoding, UIAppearance, UIAppearanceContainer, UIDynamicItem, UITraitEnvironment, UICoordinateSpace {     class func layerClass() -> AnyClass     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     var userInteractionEnabled: Bool     var tag: Int     var layer: CALayer { get }     class func userInterfaceLayoutDirectionForSemanticContentAttribute(_ attribute: UISemanticContentAttribute) -> UIUserInterfaceLayoutDirection     var semanticContentAttribute: UISemanticContentAttribute } extension UIView : UIAccessibilityIdentification { } extension UIView {     func viewPrintFormatter() -> UIViewPrintFormatter     func drawRect(_ rect: CGRect, forViewPrintFormatter formatter: UIViewPrintFormatter) } extension UIView {     func endEditing(_ force: Bool) -> Bool } extension UIView : _Reflectable { } extension UIView {     var frame: CGRect     var bounds: CGRect     var center: CGPoint     var transform: CGAffineTransform     var contentScaleFactor: CGFloat     var multipleTouchEnabled: Bool     var exclusiveTouch: Bool     func hitTest(_ point: CGPoint, withEvent event: UIEvent?) -> UIView?     func pointInside(_ point: CGPoint, withEvent event: UIEvent?) -> Bool     func convertPoint(_ point: CGPoint, toView view: UIView?) -> CGPoint     func convertPoint(_ point: CGPoint, fromView view: UIView?) -> CGPoint     func convertRect(_ rect: CGRect, toView view: UIView?) -> CGRect     func convertRect(_ rect: CGRect, fromView view: UIView?) -> CGRect     var autoresizesSubviews: Bool     var autoresizingMask: UIViewAutoresizing     func sizeThatFits(_ size: CGSize) -> CGSize     func sizeToFit() } extension UIView {     var superview: UIView? { get }     var subviews: [UIView] { get }     var window: UIWindow? { get }     func removeFromSuperview()     func insertSubview(_ view: UIView, atIndex index: Int)     func exchangeSubviewAtIndex(_ index1: Int, withSubviewAtIndex index2: Int)     func addSubview(_ view: UIView)     func insertSubview(_ view: UIView, belowSubview siblingSubview: UIView)     func insertSubview(_ view: UIView, aboveSubview siblingSubview: UIView)     func bringSubviewToFront(_ view: UIView)     func sendSubviewToBack(_ view: UIView)     func didAddSubview(_ subview: UIView)     func willRemoveSubview(_ subview: UIView)     func willMoveToSuperview(_ newSuperview: UIView?)     func didMoveToSuperview()     func willMoveToWindow(_ newWindow: UIWindow?)     func didMoveToWindow()     func isDescendantOfView(_ view: UIView) -> Bool     func viewWithTag(_ tag: Int) -> UIView?     func setNeedsLayout()     func layoutIfNeeded()     func layoutSubviews()     var layoutMargins: UIEdgeInsets     var preservesSuperviewLayoutMargins: Bool     func layoutMarginsDidChange()     var layoutMarginsGuide: UILayoutGuide { get }     var readableContentGuide: UILayoutGuide { get } } extension UIView {     func drawRect(_ rect: CGRect)     func setNeedsDisplay()     func setNeedsDisplayInRect(_ rect: CGRect)     var clipsToBounds: Bool     @NSCopying var backgroundColor: UIColor?     var alpha: CGFloat     var opaque: Bool     var clearsContextBeforeDrawing: Bool     var hidden: Bool     var contentMode: UIViewContentMode     var contentStretch: CGRect     var maskView: UIView?     var tintColor: UIColor!     var tintAdjustmentMode: UIViewTintAdjustmentMode     func tintColorDidChange() } extension UIView {     class func beginAnimations(_ animationID: String?, context context: UnsafeMutablePointer<Void>)     class func commitAnimations()     class func setAnimationDelegate(_ delegate: AnyObject?)     class func setAnimationWillStartSelector(_ selector: Selector)     class func setAnimationDidStopSelector(_ selector: Selector)     class func setAnimationDuration(_ duration: NSTimeInterval)     class func setAnimationDelay(_ delay: NSTimeInterval)     class func setAnimationStartDate(_ startDate: NSDate)     class func setAnimationCurve(_ curve: UIViewAnimationCurve)     class func setAnimationRepeatCount(_ repeatCount: Float)     class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)     class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)     class func setAnimationTransition(_ transition: UIViewAnimationTransition, forView view: UIView, cache cache: Bool)     class func setAnimationsEnabled(_ enabled: Bool)     class func areAnimationsEnabled() -> Bool     class func performWithoutAnimation(_ actionsWithoutAnimation: () -> Void)     class func inheritedAnimationDuration() -> NSTimeInterval } extension UIView {     class func animateWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void)     class func animateWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func transitionWithView(_ view: UIView, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: (() -> Void)?, completion completion: ((Bool) -> Void)?)     class func transitionFromView(_ fromView: UIView, toView toView: UIView, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, completion completion: ((Bool) -> Void)?)     class func performSystemAnimation(_ animation: UISystemAnimation, onViews views: [UIView], options options: UIViewAnimationOptions, animations parallelAnimations: (() -> Void)?, completion completion: ((Bool) -> Void)?) } extension UIView {     class func animateKeyframesWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, options options: UIViewKeyframeAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func addKeyframeWithRelativeStartTime(_ frameStartTime: Double, relativeDuration frameDuration: Double, animations animations: () -> Void) } extension UIView {     var gestureRecognizers: [UIGestureRecognizer]?     func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool } extension UIView {     func addMotionEffect(_ effect: UIMotionEffect)     func removeMotionEffect(_ effect: UIMotionEffect)     var motionEffects: [UIMotionEffect] } extension UIView {     var constraints: [NSLayoutConstraint] { get }     func addConstraint(_ constraint: NSLayoutConstraint)     func addConstraints(_ constraints: [NSLayoutConstraint])     func removeConstraint(_ constraint: NSLayoutConstraint)     func removeConstraints(_ constraints: [NSLayoutConstraint]) } extension UIView {     func updateConstraintsIfNeeded()     func updateConstraints()     func needsUpdateConstraints() -> Bool     func setNeedsUpdateConstraints() } extension UIView {     var translatesAutoresizingMaskIntoConstraints: Bool     class func requiresConstraintBasedLayout() -> Bool } extension UIView {     func alignmentRectForFrame(_ frame: CGRect) -> CGRect     func frameForAlignmentRect(_ alignmentRect: CGRect) -> CGRect     func alignmentRectInsets() -> UIEdgeInsets     func viewForBaselineLayout() -> UIView     var viewForFirstBaselineLayout: UIView { get }     var viewForLastBaselineLayout: UIView { get }     func intrinsicContentSize() -> CGSize     func invalidateIntrinsicContentSize()     func contentHuggingPriorityForAxis(_ axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentHuggingPriority(_ priority: UILayoutPriority, forAxis axis: UILayoutConstraintAxis)     func contentCompressionResistancePriorityForAxis(_ axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentCompressionResistancePriority(_ priority: UILayoutPriority, forAxis axis: UILayoutConstraintAxis) } extension UIView {     func systemLayoutSizeFittingSize(_ targetSize: CGSize) -> CGSize     func systemLayoutSizeFittingSize(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority verticalFittingPriority: UILayoutPriority) -> CGSize } extension UIView {     var layoutGuides: [UILayoutGuide] { get }     func addLayoutGuide(_ layoutGuide: UILayoutGuide)     func removeLayoutGuide(_ layoutGuide: UILayoutGuide) } extension UIView {     var leadingAnchor: NSLayoutXAxisAnchor { get }     var trailingAnchor: NSLayoutXAxisAnchor { get }     var leftAnchor: NSLayoutXAxisAnchor { get }     var rightAnchor: NSLayoutXAxisAnchor { get }     var topAnchor: NSLayoutYAxisAnchor { get }     var bottomAnchor: NSLayoutYAxisAnchor { get }     var widthAnchor: NSLayoutDimension { get }     var heightAnchor: NSLayoutDimension { get }     var centerXAnchor: NSLayoutXAxisAnchor { get }     var centerYAnchor: NSLayoutYAxisAnchor { get }     var firstBaselineAnchor: NSLayoutYAxisAnchor { get }     var lastBaselineAnchor: NSLayoutYAxisAnchor { get } } extension UIView {     func constraintsAffectingLayoutForAxis(_ axis: UILayoutConstraintAxis) -> [NSLayoutConstraint]     func hasAmbiguousLayout() -> Bool     func exerciseAmbiguityInLayout() } extension UIView {     var restorationIdentifier: String?     func encodeRestorableStateWithCoder(_ coder: NSCoder)     func decodeRestorableStateWithCoder(_ coder: NSCoder) } extension UIView {     func snapshotViewAfterScreenUpdates(_ afterUpdates: Bool) -> UIView     func resizableSnapshotViewFromRect(_ rect: CGRect, afterScreenUpdates afterUpdates: Bool, withCapInsets capInsets: UIEdgeInsets) -> UIView     func drawViewHierarchyInRect(_ rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool } extension UIView : _Reflectable { } ``` | AnyObject, NSCoding, NSObjectProtocol, UIAccessibilityIdentification, UIAppearance, UIAppearanceContainer, UICoordinateSpace, UIDynamicItem, UITraitEnvironment |
| To | ``` class UIView : UIResponder, NSCoding, UIAppearance, UIAppearanceContainer, UIDynamicItem, UITraitEnvironment, UICoordinateSpace, UIFocusEnvironment {     class func layerClass() -> AnyClass     init(frame frame: CGRect)     init?(coder aDecoder: NSCoder)     var userInteractionEnabled: Bool     var tag: Int     var layer: CALayer { get }     func canBecomeFocused() -> Bool     var focused: Bool { get }     class func userInterfaceLayoutDirectionForSemanticContentAttribute(_ attribute: UISemanticContentAttribute) -> UIUserInterfaceLayoutDirection     var semanticContentAttribute: UISemanticContentAttribute } extension UIView : UIAccessibilityIdentification { } extension UIView {     func viewPrintFormatter() -> UIViewPrintFormatter     func drawRect(_ rect: CGRect, forViewPrintFormatter formatter: UIViewPrintFormatter) } extension UIView {     func endEditing(_ force: Bool) -> Bool } extension UIView : _Reflectable { } extension UIView {     var frame: CGRect     var bounds: CGRect     var center: CGPoint     var transform: CGAffineTransform     var contentScaleFactor: CGFloat     var multipleTouchEnabled: Bool     var exclusiveTouch: Bool     func hitTest(_ point: CGPoint, withEvent event: UIEvent?) -> UIView?     func pointInside(_ point: CGPoint, withEvent event: UIEvent?) -> Bool     func convertPoint(_ point: CGPoint, toView view: UIView?) -> CGPoint     func convertPoint(_ point: CGPoint, fromView view: UIView?) -> CGPoint     func convertRect(_ rect: CGRect, toView view: UIView?) -> CGRect     func convertRect(_ rect: CGRect, fromView view: UIView?) -> CGRect     var autoresizesSubviews: Bool     var autoresizingMask: UIViewAutoresizing     func sizeThatFits(_ size: CGSize) -> CGSize     func sizeToFit() } extension UIView {     var superview: UIView? { get }     var subviews: [UIView] { get }     var window: UIWindow? { get }     func removeFromSuperview()     func insertSubview(_ view: UIView, atIndex index: Int)     func exchangeSubviewAtIndex(_ index1: Int, withSubviewAtIndex index2: Int)     func addSubview(_ view: UIView)     func insertSubview(_ view: UIView, belowSubview siblingSubview: UIView)     func insertSubview(_ view: UIView, aboveSubview siblingSubview: UIView)     func bringSubviewToFront(_ view: UIView)     func sendSubviewToBack(_ view: UIView)     func didAddSubview(_ subview: UIView)     func willRemoveSubview(_ subview: UIView)     func willMoveToSuperview(_ newSuperview: UIView?)     func didMoveToSuperview()     func willMoveToWindow(_ newWindow: UIWindow?)     func didMoveToWindow()     func isDescendantOfView(_ view: UIView) -> Bool     func viewWithTag(_ tag: Int) -> UIView?     func setNeedsLayout()     func layoutIfNeeded()     func layoutSubviews()     var layoutMargins: UIEdgeInsets     var preservesSuperviewLayoutMargins: Bool     func layoutMarginsDidChange()     var layoutMarginsGuide: UILayoutGuide { get }     var readableContentGuide: UILayoutGuide { get } } extension UIView {     func drawRect(_ rect: CGRect)     func setNeedsDisplay()     func setNeedsDisplayInRect(_ rect: CGRect)     var clipsToBounds: Bool     @NSCopying var backgroundColor: UIColor?     var alpha: CGFloat     var opaque: Bool     var clearsContextBeforeDrawing: Bool     var hidden: Bool     var contentMode: UIViewContentMode     var contentStretch: CGRect     var maskView: UIView?     var tintColor: UIColor!     var tintAdjustmentMode: UIViewTintAdjustmentMode     func tintColorDidChange() } extension UIView {     class func beginAnimations(_ animationID: String?, context context: UnsafeMutablePointer<Void>)     class func commitAnimations()     class func setAnimationDelegate(_ delegate: AnyObject?)     class func setAnimationWillStartSelector(_ selector: Selector)     class func setAnimationDidStopSelector(_ selector: Selector)     class func setAnimationDuration(_ duration: NSTimeInterval)     class func setAnimationDelay(_ delay: NSTimeInterval)     class func setAnimationStartDate(_ startDate: NSDate)     class func setAnimationCurve(_ curve: UIViewAnimationCurve)     class func setAnimationRepeatCount(_ repeatCount: Float)     class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)     class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)     class func setAnimationTransition(_ transition: UIViewAnimationTransition, forView view: UIView, cache cache: Bool)     class func setAnimationsEnabled(_ enabled: Bool)     class func areAnimationsEnabled() -> Bool     class func performWithoutAnimation(_ actionsWithoutAnimation: () -> Void)     class func inheritedAnimationDuration() -> NSTimeInterval } extension UIView {     class func animateWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void)     class func animateWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options options: UIViewAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func transitionWithView(_ view: UIView, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: (() -> Void)?, completion completion: ((Bool) -> Void)?)     class func transitionFromView(_ fromView: UIView, toView toView: UIView, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, completion completion: ((Bool) -> Void)?)     class func performSystemAnimation(_ animation: UISystemAnimation, onViews views: [UIView], options options: UIViewAnimationOptions, animations parallelAnimations: (() -> Void)?, completion completion: ((Bool) -> Void)?) } extension UIView {     class func animateKeyframesWithDuration(_ duration: NSTimeInterval, delay delay: NSTimeInterval, options options: UIViewKeyframeAnimationOptions, animations animations: () -> Void, completion completion: ((Bool) -> Void)?)     class func addKeyframeWithRelativeStartTime(_ frameStartTime: Double, relativeDuration frameDuration: Double, animations animations: () -> Void) } extension UIView {     var gestureRecognizers: [UIGestureRecognizer]?     func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool } extension UIView {     func addMotionEffect(_ effect: UIMotionEffect)     func removeMotionEffect(_ effect: UIMotionEffect)     var motionEffects: [UIMotionEffect] } extension UIView {     var constraints: [NSLayoutConstraint] { get }     func addConstraint(_ constraint: NSLayoutConstraint)     func addConstraints(_ constraints: [NSLayoutConstraint])     func removeConstraint(_ constraint: NSLayoutConstraint)     func removeConstraints(_ constraints: [NSLayoutConstraint]) } extension UIView {     func updateConstraintsIfNeeded()     func updateConstraints()     func needsUpdateConstraints() -> Bool     func setNeedsUpdateConstraints() } extension UIView {     var translatesAutoresizingMaskIntoConstraints: Bool     class func requiresConstraintBasedLayout() -> Bool } extension UIView {     func alignmentRectForFrame(_ frame: CGRect) -> CGRect     func frameForAlignmentRect(_ alignmentRect: CGRect) -> CGRect     func alignmentRectInsets() -> UIEdgeInsets     func viewForBaselineLayout() -> UIView     var viewForFirstBaselineLayout: UIView { get }     var viewForLastBaselineLayout: UIView { get }     func intrinsicContentSize() -> CGSize     func invalidateIntrinsicContentSize()     func contentHuggingPriorityForAxis(_ axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentHuggingPriority(_ priority: UILayoutPriority, forAxis axis: UILayoutConstraintAxis)     func contentCompressionResistancePriorityForAxis(_ axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentCompressionResistancePriority(_ priority: UILayoutPriority, forAxis axis: UILayoutConstraintAxis) } extension UIView {     func systemLayoutSizeFittingSize(_ targetSize: CGSize) -> CGSize     func systemLayoutSizeFittingSize(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority verticalFittingPriority: UILayoutPriority) -> CGSize } extension UIView {     var layoutGuides: [UILayoutGuide] { get }     func addLayoutGuide(_ layoutGuide: UILayoutGuide)     func removeLayoutGuide(_ layoutGuide: UILayoutGuide) } extension UIView {     var leadingAnchor: NSLayoutXAxisAnchor { get }     var trailingAnchor: NSLayoutXAxisAnchor { get }     var leftAnchor: NSLayoutXAxisAnchor { get }     var rightAnchor: NSLayoutXAxisAnchor { get }     var topAnchor: NSLayoutYAxisAnchor { get }     var bottomAnchor: NSLayoutYAxisAnchor { get }     var widthAnchor: NSLayoutDimension { get }     var heightAnchor: NSLayoutDimension { get }     var centerXAnchor: NSLayoutXAxisAnchor { get }     var centerYAnchor: NSLayoutYAxisAnchor { get }     var firstBaselineAnchor: NSLayoutYAxisAnchor { get }     var lastBaselineAnchor: NSLayoutYAxisAnchor { get } } extension UIView {     func constraintsAffectingLayoutForAxis(_ axis: UILayoutConstraintAxis) -> [NSLayoutConstraint]     func hasAmbiguousLayout() -> Bool     func exerciseAmbiguityInLayout() } extension UIView {     var restorationIdentifier: String?     func encodeRestorableStateWithCoder(_ coder: NSCoder)     func decodeRestorableStateWithCoder(_ coder: NSCoder) } extension UIView {     func snapshotViewAfterScreenUpdates(_ afterUpdates: Bool) -> UIView     func resizableSnapshotViewFromRect(_ rect: CGRect, afterScreenUpdates afterUpdates: Bool, withCapInsets capInsets: UIEdgeInsets) -> UIView     func drawViewHierarchyInRect(_ rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool } extension UIView : _Reflectable { } ``` | NSCoding, UIAccessibilityIdentification, UIAppearance, UIAppearanceContainer, UICoordinateSpace, UIDynamicItem, UIFocusEnvironment, UITraitEnvironment |

Modified [UIViewAnimationCurve [enum]](https://developer.apple.com/documentation/uikit/uiview/animationcurve)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIViewAnimationTransition [enum]](https://developer.apple.com/documentation/uikit/uiviewanimationtransition)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIViewContentMode [enum]](https://developer.apple.com/documentation/uikit/uiview/contentmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIViewController : UIResponder, NSCoding, UIAppearanceContainer, UITraitEnvironment, UIContentContainer {     init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     init?(coder aDecoder: NSCoder)     var view: UIView!     func loadView()     func loadViewIfNeeded()     var viewIfLoaded: UIView? { get }     func viewWillUnload()     func viewDidUnload()     func viewDidLoad()     func isViewLoaded() -> Bool     var nibName: String? { get }     var nibBundle: NSBundle? { get }     var storyboard: UIStoryboard? { get }     func performSegueWithIdentifier(_ identifier: String, sender sender: AnyObject?)     func shouldPerformSegueWithIdentifier(_ identifier: String, sender sender: AnyObject?) -> Bool     func prepareForSegue(_ segue: UIStoryboardSegue, sender sender: AnyObject?)     func canPerformUnwindSegueAction(_ action: Selector, fromViewController fromViewController: UIViewController, withSender sender: AnyObject) -> Bool     func allowedChildViewControllersForUnwindingFromSource(_ source: UIStoryboardUnwindSegueSource) -> [UIViewController]     func childViewControllerContainingSegueSource(_ source: UIStoryboardUnwindSegueSource) -> UIViewController?     func viewControllerForUnwindSegueAction(_ action: Selector, fromViewController fromViewController: UIViewController, withSender sender: AnyObject?) -> UIViewController?     func unwindForSegue(_ unwindSegue: UIStoryboardSegue, towardsViewController subsequentVC: UIViewController)     func segueForUnwindingToViewController(_ toViewController: UIViewController, fromViewController fromViewController: UIViewController, identifier identifier: String?) -> UIStoryboardSegue?     func viewWillAppear(_ animated: Bool)     func viewDidAppear(_ animated: Bool)     func viewWillDisappear(_ animated: Bool)     func viewDidDisappear(_ animated: Bool)     func viewWillLayoutSubviews()     func viewDidLayoutSubviews()     var title: String?     func didReceiveMemoryWarning()     weak var parentViewController: UIViewController? { get }     var modalViewController: UIViewController? { get }     var presentedViewController: UIViewController? { get }     var presentingViewController: UIViewController? { get }     var definesPresentationContext: Bool     var providesPresentationContextTransitionStyle: Bool     func isBeingPresented() -> Bool     func isBeingDismissed() -> Bool     func isMovingToParentViewController() -> Bool     func isMovingFromParentViewController() -> Bool     func presentViewController(_ viewControllerToPresent: UIViewController, animated flag: Bool, completion completion: (() -> Void)?)     func dismissViewControllerAnimated(_ flag: Bool, completion completion: (() -> Void)?)     func presentModalViewController(_ modalViewController: UIViewController, animated animated: Bool)     func dismissModalViewControllerAnimated(_ animated: Bool)     var modalTransitionStyle: UIModalTransitionStyle     var modalPresentationStyle: UIModalPresentationStyle     var modalPresentationCapturesStatusBarAppearance: Bool     func disablesAutomaticKeyboardDismissal() -> Bool     var wantsFullScreenLayout: Bool     var edgesForExtendedLayout: UIRectEdge     var extendedLayoutIncludesOpaqueBars: Bool     var automaticallyAdjustsScrollViewInsets: Bool     var preferredContentSize: CGSize     func preferredStatusBarStyle() -> UIStatusBarStyle     func prefersStatusBarHidden() -> Bool     func preferredStatusBarUpdateAnimation() -> UIStatusBarAnimation     func setNeedsStatusBarAppearanceUpdate()     func targetViewControllerForAction(_ action: Selector, sender sender: AnyObject?) -> UIViewController?     func showViewController(_ vc: UIViewController, sender sender: AnyObject?)     func showDetailViewController(_ vc: UIViewController, sender sender: AnyObject?) } extension UIViewController {     func presentMoviePlayerViewControllerAnimated(_ moviePlayerViewController: MPMoviePlayerViewController!)     func dismissMoviePlayerViewControllerAnimated() } extension UIViewController {     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get } } extension UIViewController {     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool) } extension UIViewController {     var modalInPopover: Bool     var contentSizeForViewInPopover: CGSize } extension UIViewController {     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, forSplitViewController splitViewController: UISplitViewController)     func separateSecondaryViewControllerForSplitViewController(_ splitViewController: UISplitViewController) -> UIViewController? } extension UIViewController {     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get } } extension UIViewController {     class func attemptRotationToDeviceOrientation()     func shouldAutorotateToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation) -> Bool     func shouldAutorotate() -> Bool     func supportedInterfaceOrientations() -> UIInterfaceOrientationMask     func preferredInterfaceOrientationForPresentation() -> UIInterfaceOrientation     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotateToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func didRotateFromInterfaceOrientation(_ fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func willAnimateFirstHalfOfRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func didAnimateFirstHalfOfRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotationFromInterfaceOrientation(_ fromInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval) } extension UIViewController {     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     func editButtonItem() -> UIBarButtonItem } extension UIViewController {     var searchDisplayController: UISearchDisplayController? { get } } extension UIViewController {     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transitionFromViewController(_ fromViewController: UIViewController, toViewController toViewController: UIViewController, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: (() -> Void)?, completion completion: ((Bool) -> Void)?)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     func childViewControllerForStatusBarStyle() -> UIViewController?     func childViewControllerForStatusBarHidden() -> UIViewController?     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollectionForChildViewController(_ childViewController: UIViewController) -> UITraitCollection? } extension UIViewController {     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     func shouldAutomaticallyForwardAppearanceMethods() -> Bool     func willMoveToParentViewController(_ parent: UIViewController?)     func didMoveToParentViewController(_ parent: UIViewController?) } extension UIViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: AnyObject.Type?     func encodeRestorableStateWithCoder(_ coder: NSCoder)     func decodeRestorableStateWithCoder(_ coder: NSCoder)     func applicationFinishedRestoringState() } extension UIViewController {     func updateViewConstraints() } extension UIViewController {     weak var transitioningDelegate: UIViewControllerTransitioningDelegate? } extension UIViewController {     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get } } extension UIViewController {     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand) } extension UIViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension UIViewController {     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get } } extension UIViewController {     func registerForPreviewingWithDelegate(_ delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewingWithContext(_ previewing: UIViewControllerPreviewing) } extension UIViewController {     func previewActionItems() -> [UIPreviewActionItem] } extension UIViewController {     func transitionCoordinator() -> UIViewControllerTransitionCoordinator? } extension UIViewController {     class func prepareInterstitialAds()     var interstitialPresentationPolicy: ADInterstitialPresentationPolicy     var canDisplayBannerAds: Bool     var originalContentView: UIView! { get }     var presentingFullScreenAd: Bool { get }     var displayingBannerAd: Bool { get }     func requestInterstitialAdPresentation() -> Bool     var shouldPresentInterstitialAd: Bool { get } } ``` | AnyObject, NSCoding, NSExtensionRequestHandling, NSObjectProtocol, UIAppearanceContainer, UIContentContainer, UIStateRestoring, UITraitEnvironment |
| To | ``` class UIViewController : UIResponder, NSCoding, UIAppearanceContainer, UITraitEnvironment, UIContentContainer, UIFocusEnvironment {     init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: NSBundle?)     init?(coder aDecoder: NSCoder)     var view: UIView!     func loadView()     func loadViewIfNeeded()     var viewIfLoaded: UIView? { get }     func viewWillUnload()     func viewDidUnload()     func viewDidLoad()     func isViewLoaded() -> Bool     var nibName: String? { get }     var nibBundle: NSBundle? { get }     var storyboard: UIStoryboard? { get }     func performSegueWithIdentifier(_ identifier: String, sender sender: AnyObject?)     func shouldPerformSegueWithIdentifier(_ identifier: String, sender sender: AnyObject?) -> Bool     func prepareForSegue(_ segue: UIStoryboardSegue, sender sender: AnyObject?)     func canPerformUnwindSegueAction(_ action: Selector, fromViewController fromViewController: UIViewController, withSender sender: AnyObject) -> Bool     func allowedChildViewControllersForUnwindingFromSource(_ source: UIStoryboardUnwindSegueSource) -> [UIViewController]     func childViewControllerContainingSegueSource(_ source: UIStoryboardUnwindSegueSource) -> UIViewController?     func viewControllerForUnwindSegueAction(_ action: Selector, fromViewController fromViewController: UIViewController, withSender sender: AnyObject?) -> UIViewController?     func unwindForSegue(_ unwindSegue: UIStoryboardSegue, towardsViewController subsequentVC: UIViewController)     func segueForUnwindingToViewController(_ toViewController: UIViewController, fromViewController fromViewController: UIViewController, identifier identifier: String?) -> UIStoryboardSegue?     func viewWillAppear(_ animated: Bool)     func viewDidAppear(_ animated: Bool)     func viewWillDisappear(_ animated: Bool)     func viewDidDisappear(_ animated: Bool)     func viewWillLayoutSubviews()     func viewDidLayoutSubviews()     var title: String?     func didReceiveMemoryWarning()     weak var parentViewController: UIViewController? { get }     var modalViewController: UIViewController? { get }     var presentedViewController: UIViewController? { get }     var presentingViewController: UIViewController? { get }     var definesPresentationContext: Bool     var providesPresentationContextTransitionStyle: Bool     func isBeingPresented() -> Bool     func isBeingDismissed() -> Bool     func isMovingToParentViewController() -> Bool     func isMovingFromParentViewController() -> Bool     func presentViewController(_ viewControllerToPresent: UIViewController, animated flag: Bool, completion completion: (() -> Void)?)     func dismissViewControllerAnimated(_ flag: Bool, completion completion: (() -> Void)?)     func presentModalViewController(_ modalViewController: UIViewController, animated animated: Bool)     func dismissModalViewControllerAnimated(_ animated: Bool)     var modalTransitionStyle: UIModalTransitionStyle     var modalPresentationStyle: UIModalPresentationStyle     var modalPresentationCapturesStatusBarAppearance: Bool     func disablesAutomaticKeyboardDismissal() -> Bool     var wantsFullScreenLayout: Bool     var edgesForExtendedLayout: UIRectEdge     var extendedLayoutIncludesOpaqueBars: Bool     var automaticallyAdjustsScrollViewInsets: Bool     var preferredContentSize: CGSize     func preferredStatusBarStyle() -> UIStatusBarStyle     func prefersStatusBarHidden() -> Bool     func preferredStatusBarUpdateAnimation() -> UIStatusBarAnimation     func setNeedsStatusBarAppearanceUpdate()     func targetViewControllerForAction(_ action: Selector, sender sender: AnyObject?) -> UIViewController?     func showViewController(_ vc: UIViewController, sender sender: AnyObject?)     func showDetailViewController(_ vc: UIViewController, sender sender: AnyObject?) } extension UIViewController {     func presentMoviePlayerViewControllerAnimated(_ moviePlayerViewController: MPMoviePlayerViewController!)     func dismissMoviePlayerViewControllerAnimated() } extension UIViewController {     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get } } extension UIViewController {     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool) } extension UIViewController {     var modalInPopover: Bool     var contentSizeForViewInPopover: CGSize } extension UIViewController {     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, forSplitViewController splitViewController: UISplitViewController)     func separateSecondaryViewControllerForSplitViewController(_ splitViewController: UISplitViewController) -> UIViewController? } extension UIViewController {     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get } } extension UIViewController {     class func attemptRotationToDeviceOrientation()     func shouldAutorotateToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation) -> Bool     func shouldAutorotate() -> Bool     func supportedInterfaceOrientations() -> UIInterfaceOrientationMask     func preferredInterfaceOrientationForPresentation() -> UIInterfaceOrientation     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotateToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func didRotateFromInterfaceOrientation(_ fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func willAnimateFirstHalfOfRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval)     func didAnimateFirstHalfOfRotationToInterfaceOrientation(_ toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotationFromInterfaceOrientation(_ fromInterfaceOrientation: UIInterfaceOrientation, duration duration: NSTimeInterval) } extension UIViewController {     var editing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     func editButtonItem() -> UIBarButtonItem } extension UIViewController {     var searchDisplayController: UISearchDisplayController? { get } } extension UIViewController {     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transitionFromViewController(_ fromViewController: UIViewController, toViewController toViewController: UIViewController, duration duration: NSTimeInterval, options options: UIViewAnimationOptions, animations animations: (() -> Void)?, completion completion: ((Bool) -> Void)?)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     func childViewControllerForStatusBarStyle() -> UIViewController?     func childViewControllerForStatusBarHidden() -> UIViewController?     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollectionForChildViewController(_ childViewController: UIViewController) -> UITraitCollection? } extension UIViewController {     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     func shouldAutomaticallyForwardAppearanceMethods() -> Bool     func willMoveToParentViewController(_ parent: UIViewController?)     func didMoveToParentViewController(_ parent: UIViewController?) } extension UIViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: AnyObject.Type?     func encodeRestorableStateWithCoder(_ coder: NSCoder)     func decodeRestorableStateWithCoder(_ coder: NSCoder)     func applicationFinishedRestoringState() } extension UIViewController {     func updateViewConstraints() } extension UIViewController {     weak var transitioningDelegate: UIViewControllerTransitioningDelegate? } extension UIViewController {     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get } } extension UIViewController {     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand) } extension UIViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension UIViewController {     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get } } extension UIViewController {     func registerForPreviewingWithDelegate(_ delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewingWithContext(_ previewing: UIViewControllerPreviewing) } extension UIViewController {     func previewActionItems() -> [UIPreviewActionItem] } extension UIViewController {     func transitionCoordinator() -> UIViewControllerTransitionCoordinator? } extension UIViewController {     class func prepareInterstitialAds()     var interstitialPresentationPolicy: ADInterstitialPresentationPolicy     var canDisplayBannerAds: Bool     var originalContentView: UIView! { get }     var presentingFullScreenAd: Bool { get }     var displayingBannerAd: Bool { get }     func requestInterstitialAdPresentation() -> Bool     var shouldPresentInterstitialAd: Bool { get } } ``` | NSCoding, NSExtensionRequestHandling, UIAppearanceContainer, UIContentContainer, UIFocusEnvironment, UIStateRestoring, UITraitEnvironment |

Modified [UIViewControllerTransitionCoordinator](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol UIViewControllerTransitionCoordinator : UIViewControllerTransitionCoordinatorContext, NSObjectProtocol {     func animateAlongsideTransition(_ animation: ((UIViewControllerTransitionCoordinatorContext) -> Void)?, completion completion: ((UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool     func animateAlongsideTransitionInView(_ view: UIView?, animation animation: ((UIViewControllerTransitionCoordinatorContext) -> Void)?, completion completion: ((UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool     func notifyWhenInteractionEndsUsingBlock(_ handler: (UIViewControllerTransitionCoordinatorContext) -> Void) } ``` | NSObjectProtocol, UIViewControllerTransitionCoordinatorContext |
| To | ``` protocol UIViewControllerTransitionCoordinator : UIViewControllerTransitionCoordinatorContext {     func animateAlongsideTransition(_ animation: ((UIViewControllerTransitionCoordinatorContext) -> Void)?, completion completion: ((UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool     func animateAlongsideTransitionInView(_ view: UIView?, animation animation: ((UIViewControllerTransitionCoordinatorContext) -> Void)?, completion completion: ((UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool     func notifyWhenInteractionEndsUsingBlock(_ handler: (UIViewControllerTransitionCoordinatorContext) -> Void) } ``` | UIViewControllerTransitionCoordinatorContext |

Modified [UIViewPrintFormatter](https://developer.apple.com/documentation/uikit/uiviewprintformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [UIViewTintAdjustmentMode [enum]](https://developer.apple.com/documentation/uikit/uiviewtintadjustmentmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIVisualEffect](https://developer.apple.com/documentation/uikit/uivisualeffect)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIVisualEffect : NSObject, NSCopying, NSSecureCoding, NSCoding { } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class UIVisualEffect : NSObject, NSCopying, NSSecureCoding { } ``` | NSCopying, NSSecureCoding |

Modified [UIVisualEffectView](https://developer.apple.com/documentation/uikit/uivisualeffectview)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSSecureCoding |
| To | NSSecureCoding |

Modified [UIWebPaginationBreakingMode [enum]](https://developer.apple.com/documentation/uikit/uiwebview/paginationbreakingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIWebPaginationMode [enum]](https://developer.apple.com/documentation/uikit/uiwebpaginationmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class UIWebView : UIView, UIScrollViewDelegate {     unowned(unsafe) var delegate: UIWebViewDelegate?     var scrollView: UIScrollView { get }     func loadRequest(_ request: NSURLRequest)     func loadHTMLString(_ string: String, baseURL baseURL: NSURL?)     func loadData(_ data: NSData, MIMEType MIMEType: String, textEncodingName textEncodingName: String, baseURL baseURL: NSURL)     var request: NSURLRequest? { get }     func reload()     func stopLoading()     func goBack()     func goForward()     var canGoBack: Bool { get }     var canGoForward: Bool { get }     var loading: Bool { get }     func stringByEvaluatingJavaScriptFromString(_ script: String) -> String?     var scalesPageToFit: Bool     var detectsPhoneNumbers: Bool     var dataDetectorTypes: UIDataDetectorTypes     var allowsInlineMediaPlayback: Bool     var mediaPlaybackRequiresUserAction: Bool     var mediaPlaybackAllowsAirPlay: Bool     var suppressesIncrementalRendering: Bool     var keyboardDisplayRequiresUserAction: Bool     var paginationMode: UIWebPaginationMode     var paginationBreakingMode: UIWebPaginationBreakingMode     var pageLength: CGFloat     var gapBetweenPages: CGFloat     var pageCount: Int { get }     var allowsPictureInPictureMediaPlayback: Bool     var allowsLinkPreview: Bool } ``` | AnyObject, NSCoding, NSObjectProtocol, UIScrollViewDelegate |
| To | ``` class UIWebView : UIView, NSCoding, UIScrollViewDelegate {     unowned(unsafe) var delegate: UIWebViewDelegate?     var scrollView: UIScrollView { get }     func loadRequest(_ request: NSURLRequest)     func loadHTMLString(_ string: String, baseURL baseURL: NSURL?)     func loadData(_ data: NSData, MIMEType MIMEType: String, textEncodingName textEncodingName: String, baseURL baseURL: NSURL)     var request: NSURLRequest? { get }     func reload()     func stopLoading()     func goBack()     func goForward()     var canGoBack: Bool { get }     var canGoForward: Bool { get }     var loading: Bool { get }     func stringByEvaluatingJavaScriptFromString(_ script: String) -> String?     var scalesPageToFit: Bool     var detectsPhoneNumbers: Bool     var dataDetectorTypes: UIDataDetectorTypes     var allowsInlineMediaPlayback: Bool     var mediaPlaybackRequiresUserAction: Bool     var mediaPlaybackAllowsAirPlay: Bool     var suppressesIncrementalRendering: Bool     var keyboardDisplayRequiresUserAction: Bool     var paginationMode: UIWebPaginationMode     var paginationBreakingMode: UIWebPaginationBreakingMode     var pageLength: CGFloat     var gapBetweenPages: CGFloat     var pageCount: Int { get }     var allowsPictureInPictureMediaPlayback: Bool     var allowsLinkPreview: Bool } ``` | NSCoding, UIScrollViewDelegate |

Modified [UIWebViewNavigationType [enum]](https://developer.apple.com/documentation/uikit/uiwebviewnavigationtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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
