---
title: iOS 8.2 API Diffs
apple_id: TP40015021
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS82APIDiffs/modules/WatchKit.html
archived_at: '2026-07-18T02:56:19.549380Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.2 API Diffs](iOS%208.1%20to%20iOS%208.2%20API%20Differences.md)


# WatchKit Changes

## WatchKit (Added)

Added WKAccessibilityImageRegionAdded WKAccessibilityImageRegion.frameAdded WKAccessibilityImageRegion.labelAdded WKInterfaceButtonAdded WKInterfaceButton.setAttributedTitle(NSAttributedString?)Added WKInterfaceButton.setBackgroundColor(UIColor!)Added WKInterfaceButton.setBackgroundImage(UIImage?)Added WKInterfaceButton.setBackgroundImageData(NSData?)Added WKInterfaceButton.setBackgroundImageNamed(String?)Added WKInterfaceButton.setEnabled(Bool)Added WKInterfaceButton.setTitle(String?)Added WKInterfaceControllerAdded WKInterfaceController.init()Added WKInterfaceController.addMenuItemWithImage(UIImage, title: String, action: Selector)Added WKInterfaceController.addMenuItemWithImageNamed(String, title: String, action: Selector)Added WKInterfaceController.addMenuItemWithItemIcon(WKMenuItemIcon, title: String, action: Selector)Added WKInterfaceController.awakeWithContext(AnyObject?)Added WKInterfaceController.becomeCurrentPage()Added WKInterfaceController.clearAllMenuItems()Added WKInterfaceController.contentFrameAdded WKInterfaceController.contextForSegueWithIdentifier(String) -> AnyObject?Added WKInterfaceController.contextForSegueWithIdentifier(String, inTable: WKInterfaceTable, rowIndex: Int) -> AnyObject?Added WKInterfaceController.contextsForSegueWithIdentifier(String) -> [AnyObject]?Added WKInterfaceController.contextsForSegueWithIdentifier(String, inTable: WKInterfaceTable, rowIndex: Int) -> [AnyObject]?Added WKInterfaceController.didDeactivate()Added WKInterfaceController.dismissController()Added WKInterfaceController.dismissTextInputController()Added WKInterfaceController.handleActionWithIdentifier(String?, forLocalNotification: UILocalNotification)Added WKInterfaceController.handleActionWithIdentifier(String?, forRemoteNotification:[NSObject: AnyObject])Added WKInterfaceController.handleUserActivity([NSObject: AnyObject]!)Added WKInterfaceController.invalidateUserActivity()Added WKInterfaceController.openParentApplication([NSObject: AnyObject]!, reply:(([NSObject: AnyObject]!, NSError!) -> Void)!) -> Bool [class]Added WKInterfaceController.popController()Added WKInterfaceController.popToRootController()Added WKInterfaceController.presentControllerWithName(String, context: AnyObject?)Added WKInterfaceController.presentControllerWithNames([AnyObject], contexts:[AnyObject]?)Added WKInterfaceController.presentTextInputControllerWithSuggestions([AnyObject]!, allowedInputMode: WKTextInputMode, completion:(([AnyObject]!) -> Void)!)Added WKInterfaceController.pushControllerWithName(String, context: AnyObject?)Added WKInterfaceController.reloadRootControllersWithNames([AnyObject]!, contexts:[AnyObject]!) [class]Added WKInterfaceController.setTitle(String?)Added WKInterfaceController.table(WKInterfaceTable, didSelectRowAtIndex: Int)Added WKInterfaceController.updateUserActivity(String!, userInfo:[NSObject: AnyObject]!, webpageURL: NSURL!)Added WKInterfaceController.willActivate()Added WKInterfaceDateAdded WKInterfaceDate.setCalendar(NSCalendar?)Added WKInterfaceDate.setTextColor(UIColor?)Added WKInterfaceDate.setTimeZone(NSTimeZone?)Added WKInterfaceDeviceAdded WKInterfaceDevice.addCachedImage(UIImage, name: String) -> BoolAdded WKInterfaceDevice.addCachedImageWithData(NSData, name: String) -> BoolAdded WKInterfaceDevice.cachedImagesAdded WKInterfaceDevice.currentDevice() -> WKInterfaceDevice [class]Added WKInterfaceDevice.preferredContentSizeCategoryAdded WKInterfaceDevice.removeAllCachedImages()Added WKInterfaceDevice.removeCachedImageWithName(String)Added WKInterfaceDevice.screenBoundsAdded WKInterfaceDevice.screenScaleAdded WKInterfaceGroupAdded WKInterfaceGroup.setBackgroundColor(UIColor?)Added WKInterfaceGroup.setBackgroundImage(UIImage?)Added WKInterfaceGroup.setBackgroundImageData(NSData?)Added WKInterfaceGroup.setBackgroundImageNamed(String?)Added WKInterfaceGroup.setCornerRadius(CGFloat)Added WKInterfaceGroup.startAnimating()Added WKInterfaceGroup.startAnimatingWithImagesInRange(NSRange, duration: NSTimeInterval, repeatCount: Int)Added WKInterfaceGroup.stopAnimating()Added WKInterfaceImageAdded WKInterfaceImage.setImage(UIImage?)Added WKInterfaceImage.setImageData(NSData?)Added WKInterfaceImage.setImageNamed(String?)Added WKInterfaceImage.setTintColor(UIColor!)Added WKInterfaceImage.startAnimating()Added WKInterfaceImage.startAnimatingWithImagesInRange(NSRange, duration: NSTimeInterval, repeatCount: Int)Added WKInterfaceImage.stopAnimating()Added WKInterfaceLabelAdded WKInterfaceLabel.setAttributedText(NSAttributedString?)Added WKInterfaceLabel.setText(String?)Added WKInterfaceLabel.setTextColor(UIColor?)Added WKInterfaceMapAdded WKInterfaceMap.addAnnotation(CLLocationCoordinate2D, withImage: UIImage!, centerOffset: CGPoint)Added WKInterfaceMap.addAnnotation(CLLocationCoordinate2D, withImageNamed: String!, centerOffset: CGPoint)Added WKInterfaceMap.addAnnotation(CLLocationCoordinate2D, withPinColor: WKInterfaceMapPinColor)Added WKInterfaceMap.removeAllAnnotations()Added WKInterfaceMap.setRegion(MKCoordinateRegion)Added WKInterfaceMap.setVisibleMapRect(MKMapRect)Added WKInterfaceMapPinColor [enum]Added WKInterfaceMapPinColor.GreenAdded WKInterfaceMapPinColor.PurpleAdded WKInterfaceMapPinColor.RedAdded WKInterfaceObjectAdded WKInterfaceObject.interfacePropertyAdded WKInterfaceObject.setAccessibilityHint(String?)Added WKInterfaceObject.setAccessibilityImageRegions([AnyObject]!)Added WKInterfaceObject.setAccessibilityLabel(String?)Added WKInterfaceObject.setAccessibilityTraits(UIAccessibilityTraits)Added WKInterfaceObject.setAccessibilityValue(String?)Added WKInterfaceObject.setAlpha(CGFloat)Added WKInterfaceObject.setHeight(CGFloat)Added WKInterfaceObject.setHidden(Bool)Added WKInterfaceObject.setIsAccessibilityElement(Bool)Added WKInterfaceObject.setWidth(CGFloat)Added WKInterfaceSeparatorAdded WKInterfaceSeparator.setColor(UIColor?)Added WKInterfaceSliderAdded WKInterfaceSlider.setColor(UIColor?)Added WKInterfaceSlider.setEnabled(Bool)Added WKInterfaceSlider.setNumberOfSteps(Int)Added WKInterfaceSlider.setValue(Float)Added WKInterfaceSwitchAdded WKInterfaceSwitch.setAttributedTitle(NSAttributedString!)Added WKInterfaceSwitch.setColor(UIColor!)Added WKInterfaceSwitch.setEnabled(Bool)Added WKInterfaceSwitch.setOn(Bool)Added WKInterfaceSwitch.setTitle(String!)Added WKInterfaceTableAdded WKInterfaceTable.insertRowsAtIndexes(NSIndexSet, withRowType: String)Added WKInterfaceTable.numberOfRowsAdded WKInterfaceTable.removeRowsAtIndexes(NSIndexSet)Added WKInterfaceTable.rowControllerAtIndex(Int) -> AnyObject?Added WKInterfaceTable.scrollToRowAtIndex(Int)Added WKInterfaceTable.setNumberOfRows(Int, withRowType: String)Added WKInterfaceTable.setRowTypes([AnyObject])Added WKInterfaceTimerAdded WKInterfaceTimer.setDate(NSDate)Added WKInterfaceTimer.setTextColor(UIColor?)Added WKInterfaceTimer.start()Added WKInterfaceTimer.stop()Added WKMenuItemIcon [enum]Added WKMenuItemIcon.AcceptAdded WKMenuItemIcon.AddAdded WKMenuItemIcon.BlockAdded WKMenuItemIcon.DeclineAdded WKMenuItemIcon.InfoAdded WKMenuItemIcon.MaybeAdded WKMenuItemIcon.MoreAdded WKMenuItemIcon.MuteAdded WKMenuItemIcon.PauseAdded WKMenuItemIcon.PlayAdded WKMenuItemIcon.RepeatAdded WKMenuItemIcon.ResumeAdded WKMenuItemIcon.ShareAdded WKMenuItemIcon.ShuffleAdded WKMenuItemIcon.SpeakerAdded WKMenuItemIcon.TrashAdded WKTextInputMode [enum]Added WKTextInputMode.AllowAnimatedEmojiAdded WKTextInputMode.AllowEmojiAdded WKTextInputMode.PlainAdded WKUserNotificationInterfaceControllerAdded WKUserNotificationInterfaceController.init()Added WKUserNotificationInterfaceController.didReceiveLocalNotification(UILocalNotification, withCompletion:(WKUserNotificationInterfaceType) -> Void)Added WKUserNotificationInterfaceController.didReceiveRemoteNotification([NSObject: AnyObject], withCompletion:(WKUserNotificationInterfaceType) -> Void)Added WKUserNotificationInterfaceType [enum]Added WKUserNotificationInterfaceType.CustomAdded WKUserNotificationInterfaceType.DefaultAdded WatchKitErrorCode [enum]Added WatchKitErrorCode.ApplicationDelegateWatchKitRequestReplyNotCalledErrorAdded WatchKitErrorCode.UnknownErrorAdded WatchKitErrorDomain

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
