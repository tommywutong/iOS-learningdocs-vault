---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Objective-C/UIKit.html
archived_at: '2026-07-18T02:57:05.188468Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# UIKit Changes for Objective-C

### UIKit

#### UIApplicationShortcutItem.h

Added [UIApplicationShortcutIconTypeAlarm](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypealarm)Added [UIApplicationShortcutIconTypeAudio](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypeaudio)Added [UIApplicationShortcutIconTypeBookmark](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypebookmark)Added [UIApplicationShortcutIconTypeCapturePhoto](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypecapturephoto)Added [UIApplicationShortcutIconTypeCaptureVideo](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypecapturevideo)Added [UIApplicationShortcutIconTypeCloud](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/cloud)Added [UIApplicationShortcutIconTypeConfirmation](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypeconfirmation)Added [UIApplicationShortcutIconTypeContact](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypecontact)Added [UIApplicationShortcutIconTypeDate](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/date)Added [UIApplicationShortcutIconTypeFavorite](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/favorite)Added [UIApplicationShortcutIconTypeHome](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/home)Added [UIApplicationShortcutIconTypeInvitation](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/invitation)Added [UIApplicationShortcutIconTypeLove](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/love)Added [UIApplicationShortcutIconTypeMail](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypemail)Added [UIApplicationShortcutIconTypeMarkLocation](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypemarklocation)Added [UIApplicationShortcutIconTypeMessage](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypemessage)Added [UIApplicationShortcutIconTypeProhibit](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/prohibit)Added [UIApplicationShortcutIconTypeShuffle](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/shuffle)Added [UIApplicationShortcutIconTypeTask](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypetask)Added [UIApplicationShortcutIconTypeTaskCompleted](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/taskcompleted)Added [UIApplicationShortcutIconTypeTime](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticontype/uiapplicationshortcuticontypetime)Added [UIApplicationShortcutIconTypeUpdate](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/icontype/update)

#### UICollectionView.h

Added [UICollectionView.remembersLastFocusedIndexPath](https://developer.apple.com/documentation/uikit/uicollectionview/1618022-rememberslastfocusedindexpath)Added [-[UICollectionViewDelegate collectionView:canFocusItemAtIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618013-collectionview)Added [-[UICollectionViewDelegate collectionView:didUpdateFocusInContext:withAnimationCoordinator:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618081-collectionview)Added [-[UICollectionViewDelegate collectionView:shouldUpdateFocusInContext:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618072-collectionview)Added [-[UICollectionViewDelegate indexPathForPreferredFocusedViewInCollectionView:]](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/1618066-indexpathforpreferredfocusedview)Added [UICollectionViewFocusUpdateContext](https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext)Added [UICollectionViewFocusUpdateContext.nextFocusedIndexPath](https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext/1618011-nextfocusedindexpath)Added [UICollectionViewFocusUpdateContext.previouslyFocusedIndexPath](https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext/1618077-previouslyfocusedindexpath)

#### UIControl.h

Added [UIControlStateFocused](https://developer.apple.com/documentation/uikit/uicontrolstate/uicontrolstatefocused)

#### UIDevice.h

Added [UIUserInterfaceIdiomTV](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom/tv)

#### UIEvent.h

Added [UIEventTypePresses](https://developer.apple.com/documentation/uikit/uieventtype/uieventtypepresses)

#### UIFocus.h (Added)

Added [UIFocusEnvironment](https://developer.apple.com/documentation/uikit/uifocusenvironment)Added [-[UIFocusEnvironment didUpdateFocusInContext:withAnimationCoordinator:]](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616841-didupdatefocusincontext)Added [UIFocusEnvironment.preferredFocusedView](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616830-preferredfocusedview)Added [-[UIFocusEnvironment setNeedsFocusUpdate]](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616837-setneedsfocusupdate)Added [-[UIFocusEnvironment shouldUpdateFocusInContext:]](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616831-shouldupdatefocusincontext)Added [-[UIFocusEnvironment updateFocusIfNeeded]](https://developer.apple.com/documentation/uikit/uifocusenvironment/1616833-updatefocusifneeded)Added [UIFocusGuide](https://developer.apple.com/documentation/uikit/uifocusguide)Added [UIFocusGuide.enabled](https://developer.apple.com/documentation/uikit/uifocusguide/1616838-isenabled)Added [UIFocusGuide.preferredFocusedView](https://developer.apple.com/documentation/uikit/uifocusguide/1616848-preferredfocusedview)Added [UIFocusUpdateContext](https://developer.apple.com/documentation/uikit/uifocusupdatecontext)Added [UIFocusUpdateContext.focusHeading](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/1616834-focusheading)Added [UIFocusUpdateContext.nextFocusedView](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/1616843-nextfocusedview)Added [UIFocusUpdateContext.previouslyFocusedView](https://developer.apple.com/documentation/uikit/uifocusupdatecontext/1616839-previouslyfocusedview)Added [UIFocusHeading](https://developer.apple.com/documentation/uikit/uifocusheading)Added [UIFocusHeadingDown](https://developer.apple.com/documentation/uikit/uifocusheading/uifocusheadingdown)Added [UIFocusHeadingLeft](https://developer.apple.com/documentation/uikit/uifocusheading/1616844-left)Added [UIFocusHeadingNext](https://developer.apple.com/documentation/uikit/uifocusheading/uifocusheadingnext)Added [UIFocusHeadingPrevious](https://developer.apple.com/documentation/uikit/uifocusheading/1616842-previous)Added [UIFocusHeadingRight](https://developer.apple.com/documentation/uikit/uifocusheading/uifocusheadingright)Added [UIFocusHeadingUp](https://developer.apple.com/documentation/uikit/uifocusheading/uifocusheadingup)

#### UIFocusAnimationCoordinator.h (Added)

Added [UIFocusAnimationCoordinator](https://developer.apple.com/documentation/uikit/uifocusanimationcoordinator)Added [-[UIFocusAnimationCoordinator addCoordinatedAnimations:completion:]](https://developer.apple.com/documentation/uikit/uifocusanimationcoordinator/1619045-addcoordinatedanimations)

#### UIGestureRecognizer.h

Added [UIGestureRecognizer.allowedPressTypes](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624231-allowedpresstypes)Added [UIGestureRecognizer.allowedTouchTypes](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624223-allowedtouchtypes)Added [-[UIGestureRecognizerDelegate gestureRecognizer:shouldReceivePress:]](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/1624216-gesturerecognizer)

#### UIGestureRecognizerSubclass.h

Added [-[UIGestureRecognizer ignorePress:forEvent:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1620007-ignorepress)Added [-[UIGestureRecognizer pressesBegan:withEvent:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1619995-pressesbegan)Added [-[UIGestureRecognizer pressesCancelled:withEvent:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1619999-pressescancelled)Added [-[UIGestureRecognizer pressesChanged:withEvent:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1620001-presseschanged)Added [-[UIGestureRecognizer pressesEnded:withEvent:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1620000-pressesended)Added [-[UIGestureRecognizer touchesEstimatedPropertiesUpdated:]](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1619997-touchesestimatedpropertiesupdate)

#### UIImagePickerController.h

Added [UIImagePickerControllerLivePhoto](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerlivephoto)

#### UIKitDefines.h

Added #def UIKIT_AVAILABLE_IOS_TVOSAdded #def UIKIT_AVAILABLE_IOS_WATCHOS_TVOSAdded #def UIKIT_AVAILABLE_TVOS_ONLY

#### UIPresentationController.h

Modified [UIPresentationController](https://developer.apple.com/documentation/uikit/uipresentationcontroller)

|  | Protocols |
| --- | --- |
| From | UIAppearanceContainer, UIContentContainer, UITraitEnvironment |
| To | UIAppearanceContainer, UIContentContainer, UIFocusEnvironment, UITraitEnvironment |

#### UIPress.h (Added)

Added [UIPress](https://developer.apple.com/documentation/uikit/uipress)Added [UIPress.force](https://developer.apple.com/documentation/uikit/uipress/1620364-force)Added [UIPress.gestureRecognizers](https://developer.apple.com/documentation/uikit/uipress/1620376-gesturerecognizers)Added [UIPress.phase](https://developer.apple.com/documentation/uikit/uipress/1620367-phase)Added [UIPress.responder](https://developer.apple.com/documentation/uikit/uipress/1620374-responder)Added [UIPress.timestamp](https://developer.apple.com/documentation/uikit/uipress/1620360-timestamp)Added [UIPress.type](https://developer.apple.com/documentation/uikit/uipress/1620370-type)Added [UIPress.window](https://developer.apple.com/documentation/uikit/uipress/1620366-window)Added [UIPressPhase](https://developer.apple.com/documentation/uikit/uipressphase)Added [UIPressPhaseBegan](https://developer.apple.com/documentation/uikit/uipressphase/uipressphasebegan)Added [UIPressPhaseCancelled](https://developer.apple.com/documentation/uikit/uipress/phase/cancelled)Added [UIPressPhaseChanged](https://developer.apple.com/documentation/uikit/uipressphase/uipressphasechanged)Added [UIPressPhaseEnded](https://developer.apple.com/documentation/uikit/uipress/phase/ended)Added [UIPressPhaseStationary](https://developer.apple.com/documentation/uikit/uipress/phase/stationary)Added [UIPressType](https://developer.apple.com/documentation/uikit/uipress/presstype)Added [UIPressTypeDownArrow](https://developer.apple.com/documentation/uikit/uipress/presstype/downarrow)Added [UIPressTypeLeftArrow](https://developer.apple.com/documentation/uikit/uipresstype/uipresstypeleftarrow)Added [UIPressTypeMenu](https://developer.apple.com/documentation/uikit/uipresstype/uipresstypemenu)Added [UIPressTypePlayPause](https://developer.apple.com/documentation/uikit/uipresstype/uipresstypeplaypause)Added [UIPressTypeRightArrow](https://developer.apple.com/documentation/uikit/uipresstype/uipresstyperightarrow)Added [UIPressTypeSelect](https://developer.apple.com/documentation/uikit/uipresstype/uipresstypeselect)Added [UIPressTypeUpArrow](https://developer.apple.com/documentation/uikit/uipresstype/uipresstypeuparrow)

#### UIPressesEvent.h (Added)

Added [UIPressesEvent](https://developer.apple.com/documentation/uikit/uipressesevent)Added [-[UIPressesEvent allPresses]](https://developer.apple.com/documentation/uikit/uipressesevent/1623575-allpresses)Added [-[UIPressesEvent pressesForGestureRecognizer:]](https://developer.apple.com/documentation/uikit/uipressesevent/1623574-presses)

#### UIResponder.h

Added [-[UIResponder pressesBegan:withEvent:]](https://developer.apple.com/documentation/uikit/uiresponder/1621134-pressesbegan)Added [-[UIResponder pressesCancelled:withEvent:]](https://developer.apple.com/documentation/uikit/uiresponder/1621148-pressescancelled)Added [-[UIResponder pressesChanged:withEvent:]](https://developer.apple.com/documentation/uikit/uiresponder/1621150-presseschanged)Added [-[UIResponder pressesEnded:withEvent:]](https://developer.apple.com/documentation/uikit/uiresponder/1621128-pressesended)Added [-[UIResponder touchesEstimatedPropertiesUpdated:]](https://developer.apple.com/documentation/uikit/uiresponder/1621147-touchesestimatedpropertiesupdate)

#### UIScreen.h

Added [UIScreen.focusedView](https://developer.apple.com/documentation/uikit/uiscreen/1617831-focusedview)Added [UIScreen.supportsFocus](https://developer.apple.com/documentation/uikit/uiscreen/1617816-supportsfocus)

#### UISearchContainerViewController.h (Added)

Added [UISearchContainerViewController](https://developer.apple.com/documentation/uikit/uisearchcontainerviewcontroller)Added [-[UISearchContainerViewController initWithSearchController:]](https://developer.apple.com/documentation/uikit/uisearchcontainerviewcontroller/1615746-initwithsearchcontroller)Added [UISearchContainerViewController.searchController](https://developer.apple.com/documentation/uikit/uisearchcontainerviewcontroller/1615748-searchcontroller)

#### UISearchController.h

Added [UISearchController.obscuresBackgroundDuringPresentation](https://developer.apple.com/documentation/uikit/uisearchcontroller/1618656-obscuresbackgroundduringpresenta)

#### UITableView.h

Added [UITableView.remembersLastFocusedIndexPath](https://developer.apple.com/documentation/uikit/uitableview/1614858-rememberslastfocusedindexpath)Added [-[UITableViewDelegate indexPathForPreferredFocusedViewInTableView:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614929-indexpathforpreferredfocusedview)Added [-[UITableViewDelegate tableView:canFocusRowAtIndexPath:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614973-tableview)Added [-[UITableViewDelegate tableView:didUpdateFocusInContext:withAnimationCoordinator:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614945-tableview)Added [-[UITableViewDelegate tableView:shouldUpdateFocusInContext:]](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614949-tableview)Added [UITableViewFocusUpdateContext](https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext)Added [UITableViewFocusUpdateContext.nextFocusedIndexPath](https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext/1614919-nextfocusedindexpath)Added [UITableViewFocusUpdateContext.previouslyFocusedIndexPath](https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext/1614930-previouslyfocusedindexpath)

#### UITableViewCell.h

Added [UITableViewCell.focusStyle](https://developer.apple.com/documentation/uikit/uitableviewcell/1623248-focusstyle)Added [UITableViewCellFocusStyle](https://developer.apple.com/documentation/uikit/uitableviewcellfocusstyle)Added [UITableViewCellFocusStyleCustom](https://developer.apple.com/documentation/uikit/uitableviewcellfocusstyle/uitableviewcellfocusstylecustom)Added [UITableViewCellFocusStyleDefault](https://developer.apple.com/documentation/uikit/uitableviewcellfocusstyle/uitableviewcellfocusstyledefault)

#### UITouch.h

Added [UITouch.altitudeAngle](https://developer.apple.com/documentation/uikit/uitouch/1618118-altitudeangle)Added [-[UITouch azimuthAngleInView:]](https://developer.apple.com/documentation/uikit/uitouch/1618131-azimuthangleinview)Added [-[UITouch azimuthUnitVectorInView:]](https://developer.apple.com/documentation/uikit/uitouch/1618133-azimuthunitvector)Added [UITouch.estimatedProperties](https://developer.apple.com/documentation/uikit/uitouch/1618130-estimatedproperties)Added [UITouch.estimatedPropertiesExpectingUpdates](https://developer.apple.com/documentation/uikit/uitouch/1618119-estimatedpropertiesexpectingupda)Added [UITouch.estimationUpdateIndex](https://developer.apple.com/documentation/uikit/uitouch/1618137-estimationupdateindex)Added [-[UITouch preciseLocationInView:]](https://developer.apple.com/documentation/uikit/uitouch/1618134-preciselocationinview)Added [-[UITouch precisePreviousLocationInView:]](https://developer.apple.com/documentation/uikit/uitouch/1618129-precisepreviouslocationinview)Added [UITouch.type](https://developer.apple.com/documentation/uikit/uitouch/1618143-type)Added [UITouchProperties](https://developer.apple.com/documentation/uikit/uitouch/properties)Added [UITouchPropertyAltitude](https://developer.apple.com/documentation/uikit/uitouch/properties/1618141-altitude)Added [UITouchPropertyAzimuth](https://developer.apple.com/documentation/uikit/uitouch/properties/1618104-azimuth)Added [UITouchPropertyForce](https://developer.apple.com/documentation/uikit/uitouchproperties/uitouchpropertyforce)Added [UITouchPropertyLocation](https://developer.apple.com/documentation/uikit/uitouchproperties/uitouchpropertylocation)Added [UITouchType](https://developer.apple.com/documentation/uikit/uitouchtype)Added [UITouchTypeDirect](https://developer.apple.com/documentation/uikit/uitouchtype/uitouchtypedirect)Added [UITouchTypeIndirect](https://developer.apple.com/documentation/uikit/uitouch/touchtype/indirect)Added [UITouchTypeStylus](https://developer.apple.com/documentation/uikit/uitouch/touchtype/1618124-stylus)

#### UIView.h

Added [-[UIView canBecomeFocused]](https://developer.apple.com/documentation/uikit/uiview/1622584-canbecomefocused)Added [UIView.focused](https://developer.apple.com/documentation/uikit/uiview/1622565-isfocused)Modified [UIView](https://developer.apple.com/documentation/uikit/uiview)

|  | Protocols |
| --- | --- |
| From | NSCoding, UIAppearance, UIAppearanceContainer, UICoordinateSpace, UIDynamicItem, UITraitEnvironment |
| To | NSCoding, UIAppearance, UIAppearanceContainer, UICoordinateSpace, UIDynamicItem, UIFocusEnvironment, UITraitEnvironment |

Modified [-[UIView viewWithTag:]](https://developer.apple.com/documentation/uikit/uiview/1622429-viewwithtag)

|  | Declaration |
| --- | --- |
| From | ``` - (UIView * _Nullable)viewWithTag:(NSInteger)tag ``` |
| To | ``` - (__kindof UIView *)viewWithTag:(NSInteger)tag ``` |

#### UIViewController.h

Modified [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller)

|  | Protocols |
| --- | --- |
| From | NSCoding, UIAppearanceContainer, UIContentContainer, UITraitEnvironment |
| To | NSCoding, UIAppearanceContainer, UIContentContainer, UIFocusEnvironment, UITraitEnvironment |

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
