---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/WatchKit.html
archived_at: '2026-07-18T02:57:04.033011Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# WatchKit Changes for Swift

### WatchKit

Removed WKInterfaceGroup.startAnimating()Removed WKInterfaceGroup.startAnimatingWithImagesInRange(_: NSRange, duration: NSTimeInterval, repeatCount: Int)Removed WKInterfaceGroup.stopAnimating()Removed WKInterfaceImage.startAnimating()Removed WKInterfaceImage.startAnimatingWithImagesInRange(_: NSRange, duration: NSTimeInterval, repeatCount: Int)Removed WKInterfaceImage.stopAnimating()Added [WatchKitErrorCode.DownloadError](https://developer.apple.com/documentation/watchkit/watchkiterror/code/downloadfailed)Added [WatchKitErrorCode.InvalidArgumentError](https://developer.apple.com/documentation/watchkit/watchkiterror/code/invalidargument)Added [WatchKitErrorCode.MediaPlayerError](https://developer.apple.com/documentation/watchkit/watchkiterror/code/mediaplayerfailed)Added [WKImageAnimatable](https://developer.apple.com/documentation/watchkit/wkimageanimatable)Added [WKImageAnimatable.startAnimating()](https://developer.apple.com/documentation/watchkit/wkimageanimatable/1615219-startanimating)Added [WKImageAnimatable.startAnimatingWithImagesInRange(_: NSRange, duration: NSTimeInterval, repeatCount: Int)](https://developer.apple.com/documentation/watchkit/wkimageanimatable/1615208-startanimatingwithimagesinrange)Added [WKImageAnimatable.stopAnimating()](https://developer.apple.com/documentation/watchkit/wkimageanimatable/1615225-stopanimating)Added WKInterfaceController.presentController(_: [(name: String, context: AnyObject)])Added [WKInterfaceController.presentTextInputControllerWithSuggestionsForLanguage(_: ((String) -> [AnyObject]?)?, allowedInputMode: WKTextInputMode, completion: ([AnyObject]?) -> Void)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619574-presenttextinputcontrollerwithsu)Added WKInterfaceController.reloadRootControllers(_: [(name: String, context: AnyObject)]) [class]Added [WKInterfaceDevice.localizedModel](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620835-localizedmodel)Added [WKInterfaceDevice.model](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620940-model)Added [WKInterfaceDevice.name](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620883-name)Added [WKInterfaceDevice.systemName](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620857-systemname)Added [WKInterfaceDevice.systemVersion](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620927-systemversion)Added [WKInterfaceObject.setAccessibilityIdentifier(_: String?)](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/1620817-setaccessibilityidentifier)Modified [WatchKitErrorCode [enum]](https://developer.apple.com/documentation/watchkit/watchkiterror/code)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum WatchKitErrorCode : Int {     case UnknownError     case ApplicationDelegateWatchKitRequestReplyNotCalledError } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum WatchKitErrorCode : Int {     case UnknownError     case ApplicationDelegateWatchKitRequestReplyNotCalledError     case InvalidArgumentError     case MediaPlayerError     case DownloadError } extension WatchKitErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension WatchKitErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [WKInterfaceController](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller)

|  | Declaration |
| --- | --- |
| From | ``` class WKInterfaceController : NSObject {     init()     func awakeWithContext(_ context: AnyObject?)     var contentFrame: CGRect { get }     func willActivate()     func didDeactivate()     func table(_ table: WKInterfaceTable, didSelectRowAtIndex rowIndex: Int)     func handleActionWithIdentifier(_ identifier: String?, forRemoteNotification remoteNotification: [NSObject : AnyObject])     func handleActionWithIdentifier(_ identifier: String?, forLocalNotification localNotification: UILocalNotification)     func handleUserActivity(_ userInfo: [NSObject : AnyObject]?)     func setTitle(_ title: String?)     func pushControllerWithName(_ name: String, context context: AnyObject?)     func popController()     func popToRootController()     class func reloadRootControllersWithNames(_ names: [AnyObject], contexts contexts: [AnyObject]?)     func becomeCurrentPage()     func presentControllerWithName(_ name: String, context context: AnyObject?)     func presentControllerWithNames(_ names: [AnyObject], contexts contexts: [AnyObject]?)     func dismissController()     func presentTextInputControllerWithSuggestions(_ suggestions: [AnyObject]?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]!) -> Void)     func dismissTextInputController()     func contextForSegueWithIdentifier(_ segueIdentifier: String) -> AnyObject?     func contextsForSegueWithIdentifier(_ segueIdentifier: String) -> [AnyObject]?     func contextForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> AnyObject?     func contextsForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> [AnyObject]?     func addMenuItemWithImage(_ image: UIImage, title title: String, action action: Selector)     func addMenuItemWithImageNamed(_ imageName: String, title title: String, action action: Selector)     func addMenuItemWithItemIcon(_ itemIcon: WKMenuItemIcon, title title: String, action action: Selector)     func clearAllMenuItems()     func updateUserActivity(_ type: String, userInfo userInfo: [NSObject : AnyObject]?, webpageURL webpageURL: NSURL?)     func invalidateUserActivity()     class func openParentApplication(_ userInfo: [NSObject : AnyObject], reply reply: (([NSObject : AnyObject]!, NSError!) -> Void)?) -> Bool } ``` |
| To | ``` class WKInterfaceController : NSObject {     init()     func awakeWithContext(_ context: AnyObject?)     var contentFrame: CGRect { get }     func willActivate()     func didDeactivate()     func didAppear()     func willDisappear()     func pickerDidFocus(_ picker: WKInterfacePicker)     func pickerDidResignFocus(_ picker: WKInterfacePicker)     func pickerDidSettle(_ picker: WKInterfacePicker)     func table(_ table: WKInterfaceTable, didSelectRowAtIndex rowIndex: Int)     func handleActionWithIdentifier(_ identifier: String?, forRemoteNotification remoteNotification: [NSObject : AnyObject])     func handleActionWithIdentifier(_ identifier: String?, forLocalNotification localNotification: UILocalNotification)     func handleUserActivity(_ userInfo: [NSObject : AnyObject]?)     func setTitle(_ title: String?)     func pushControllerWithName(_ name: String, context context: AnyObject?)     func popController()     func popToRootController()     class func reloadRootControllersWithNames(_ names: [String], contexts contexts: [AnyObject]?)     func becomeCurrentPage()     func presentControllerWithName(_ name: String, context context: AnyObject?)     func presentControllerWithNames(_ names: [String], contexts contexts: [AnyObject]?)     func dismissController()     func presentTextInputControllerWithSuggestions(_ suggestions: [String]?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void)     func presentTextInputControllerWithSuggestionsForLanguage(_ suggestionsHandler: ((String) -> [AnyObject]?)?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void)     func dismissTextInputController()     func presentMediaPlayerControllerWithURL(_ URL: NSURL, options options: [NSObject : AnyObject]?, completion completion: (Bool, NSTimeInterval, NSError?) -> Void)     func dismissMediaPlayerController()     func presentAudioRecordingControllerWithOutputURL(_ URL: NSURL, preset preset: WKAudioRecordingPreset, maximumDuration maximumDuration: NSTimeInterval, actionTitle actionTitle: String?, completion completion: (Bool, NSError?) -> Void)     func dismissAudioRecordingController()     func contextForSegueWithIdentifier(_ segueIdentifier: String) -> AnyObject?     func contextsForSegueWithIdentifier(_ segueIdentifier: String) -> [AnyObject]?     func contextForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> AnyObject?     func contextsForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> [AnyObject]?     func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void)     func presentAlertControllerWithTitle(_ title: String?, message message: String?, preferredStyle preferredStyle: WKAlertControllerStyle, actions actions: [WKAlertAction])     func presentAddPassesControllerWithPasses(_ passes: [PKPass], completion completion: () -> Void)     func dismissAddPassesController()     func addMenuItemWithImage(_ image: UIImage, title title: String, action action: Selector)     func addMenuItemWithImageNamed(_ imageName: String, title title: String, action action: Selector)     func addMenuItemWithItemIcon(_ itemIcon: WKMenuItemIcon, title title: String, action action: Selector)     func clearAllMenuItems()     func updateUserActivity(_ type: String, userInfo userInfo: [NSObject : AnyObject]?, webpageURL webpageURL: NSURL?)     func invalidateUserActivity()     class func openParentApplication(_ userInfo: [NSObject : AnyObject], reply reply: (([NSObject : AnyObject], NSError?) -> Void)?) -> Bool     func beginGlanceUpdates()     func endGlanceUpdates() } extension WKInterfaceController {     class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(_ namesAndContexts: [(name: String, context: AnyObject)]) } extension WKInterfaceController {     class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(_ namesAndContexts: [(name: String, context: AnyObject)]) } ``` |

Modified [WKInterfaceController.openParentApplication(_: [NSObject : AnyObject], reply: (([NSObject : AnyObject], NSError?) -> Void)?) -> Bool [class]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619531-openparentapplication)

|  | Declaration |
| --- | --- |
| From | ``` class func openParentApplication(_ userInfo: [NSObject : AnyObject], reply reply: (([NSObject : AnyObject]!, NSError!) -> Void)?) -> Bool ``` |
| To | ``` class func openParentApplication(_ userInfo: [NSObject : AnyObject], reply reply: (([NSObject : AnyObject], NSError?) -> Void)?) -> Bool ``` |

Modified [WKInterfaceController.presentControllerWithNames(_: [String], contexts: [AnyObject]?)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619561-presentcontrollerwithnames)

|  | Declaration |
| --- | --- |
| From | ``` func presentControllerWithNames(_ names: [AnyObject], contexts contexts: [AnyObject]?) ``` |
| To | ``` func presentControllerWithNames(_ names: [String], contexts contexts: [AnyObject]?) ``` |

Modified [WKInterfaceController.presentTextInputControllerWithSuggestions(_: [String]?, allowedInputMode: WKTextInputMode, completion: ([AnyObject]?) -> Void)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619527-presenttextinputcontrollerwithsu)

|  | Declaration |
| --- | --- |
| From | ``` func presentTextInputControllerWithSuggestions(_ suggestions: [AnyObject]?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]!) -> Void) ``` |
| To | ``` func presentTextInputControllerWithSuggestions(_ suggestions: [String]?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void) ``` |

Modified [WKInterfaceController.reloadRootControllersWithNames(_: [String], contexts: [AnyObject]?) [class]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619563-reloadrootcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` class func reloadRootControllersWithNames(_ names: [AnyObject], contexts contexts: [AnyObject]?) ``` |
| To | ``` class func reloadRootControllersWithNames(_ names: [String], contexts contexts: [AnyObject]?) ``` |

Modified [WKInterfaceDevice](https://developer.apple.com/documentation/watchkit/wkinterfacedevice)

|  | Declaration |
| --- | --- |
| From | ``` class WKInterfaceDevice : NSObject {     class func currentDevice() -> WKInterfaceDevice     func addCachedImage(_ image: UIImage, name name: String) -> Bool     func addCachedImageWithData(_ imageData: NSData, name name: String) -> Bool     func removeCachedImageWithName(_ name: String)     func removeAllCachedImages()     var screenBounds: CGRect { get }     var screenScale: CGFloat { get }     var preferredContentSizeCategory: String { get }     var cachedImages: [NSObject : AnyObject] { get } } ``` |
| To | ``` class WKInterfaceDevice : NSObject {     class func currentDevice() -> WKInterfaceDevice     func addCachedImage(_ image: UIImage, name name: String) -> Bool     func addCachedImageWithData(_ imageData: NSData, name name: String) -> Bool     func removeCachedImageWithName(_ name: String)     func removeAllCachedImages()     var screenBounds: CGRect { get }     var screenScale: CGFloat { get }     var preferredContentSizeCategory: String { get }     var cachedImages: [String : NSNumber] { get }     var systemVersion: String { get }     var name: String { get }     var model: String { get }     var localizedModel: String { get }     var systemName: String { get }     func playHaptic(_ type: WKHapticType) } ``` |

Modified [WKInterfaceDevice.cachedImages](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620887-cachedimages)

|  | Declaration |
| --- | --- |
| From | ``` var cachedImages: [NSObject : AnyObject] { get } ``` |
| To | ``` var cachedImages: [String : NSNumber] { get } ``` |

Modified [WKInterfaceGroup](https://developer.apple.com/documentation/watchkit/wkinterfacegroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceGroup : WKInterfaceObject {     func setCornerRadius(_ cornerRadius: CGFloat)     func setBackgroundColor(_ color: UIColor?)     func setBackgroundImage(_ image: UIImage?)     func setBackgroundImageData(_ imageData: NSData?)     func setBackgroundImageNamed(_ imageName: String?)     func startAnimating()     func startAnimatingWithImagesInRange(_ imageRange: NSRange, duration duration: NSTimeInterval, repeatCount repeatCount: Int)     func stopAnimating() } ``` | AnyObject |
| To | ``` class WKInterfaceGroup : WKInterfaceObject, WKImageAnimatable {     func setCornerRadius(_ cornerRadius: CGFloat)     func setContentInset(_ contentInset: UIEdgeInsets)     func setBackgroundColor(_ color: UIColor?)     func setBackgroundImage(_ image: UIImage?)     func setBackgroundImageData(_ imageData: NSData?)     func setBackgroundImageNamed(_ imageName: String?) } ``` | AnyObject, NSObjectProtocol, WKImageAnimatable |

Modified [WKInterfaceImage](https://developer.apple.com/documentation/watchkit/wkinterfaceimage)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceImage : WKInterfaceObject {     func setImage(_ image: UIImage?)     func setImageData(_ imageData: NSData?)     func setImageNamed(_ imageName: String?)     func setTintColor(_ tintColor: UIColor?)     func startAnimating()     func startAnimatingWithImagesInRange(_ imageRange: NSRange, duration duration: NSTimeInterval, repeatCount repeatCount: Int)     func stopAnimating() } ``` | AnyObject |
| To | ``` class WKInterfaceImage : WKInterfaceObject, WKImageAnimatable {     func setImage(_ image: UIImage?)     func setImageData(_ imageData: NSData?)     func setImageNamed(_ imageName: String?)     func setTintColor(_ tintColor: UIColor?) } ``` | AnyObject, NSObjectProtocol, WKImageAnimatable |

Modified [WKInterfaceMapPinColor [enum]](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [WKInterfaceObject](https://developer.apple.com/documentation/watchkit/wkinterfaceobject)

|  | Declaration |
| --- | --- |
| From | ``` class WKInterfaceObject : NSObject {     init!()     func setHidden(_ hidden: Bool)     func setAlpha(_ alpha: CGFloat)     func setWidth(_ width: CGFloat)     func setHeight(_ height: CGFloat)     var interfaceProperty: String { get } } extension WKInterfaceObject {     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [AnyObject]) } ``` |
| To | ``` class WKInterfaceObject : NSObject {     init()     func setHidden(_ hidden: Bool)     func setAlpha(_ alpha: CGFloat)     func setHorizontalAlignment(_ horizontalAlignment: WKInterfaceObjectHorizontalAlignment)     func setVerticalAlignment(_ verticalAlignment: WKInterfaceObjectVerticalAlignment)     func setWidth(_ width: CGFloat)     func setHeight(_ height: CGFloat)     func setRelativeWidth(_ width: CGFloat, withAdjustment adjustment: CGFloat)     func setRelativeHeight(_ height: CGFloat, withAdjustment adjustment: CGFloat)     func sizeToFitWidth()     func sizeToFitHeight()     var interfaceProperty: String { get } } extension WKInterfaceObject {     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion]) } ``` |

Modified [WKInterfaceObject.setAccessibilityImageRegions(_: [WKAccessibilityImageRegion])](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/1620920-setaccessibilityimageregions)

|  | Declaration |
| --- | --- |
| From | ``` func setAccessibilityImageRegions(_ accessibilityImageRegions: [AnyObject]) ``` |
| To | ``` func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion]) ``` |

Modified [WKInterfaceTable](https://developer.apple.com/documentation/watchkit/wkinterfacetable)

|  | Declaration |
| --- | --- |
| From | ``` class WKInterfaceTable : WKInterfaceObject {     func setRowTypes(_ rowTypes: [AnyObject])     func setNumberOfRows(_ numberOfRows: Int, withRowType rowType: String)     var numberOfRows: Int { get }     func rowControllerAtIndex(_ index: Int) -> AnyObject?     func insertRowsAtIndexes(_ rows: NSIndexSet, withRowType rowType: String)     func removeRowsAtIndexes(_ rows: NSIndexSet)     func scrollToRowAtIndex(_ index: Int) } ``` |
| To | ``` class WKInterfaceTable : WKInterfaceObject {     func setRowTypes(_ rowTypes: [String])     func setNumberOfRows(_ numberOfRows: Int, withRowType rowType: String)     var numberOfRows: Int { get }     func rowControllerAtIndex(_ index: Int) -> AnyObject?     func insertRowsAtIndexes(_ rows: NSIndexSet, withRowType rowType: String)     func removeRowsAtIndexes(_ rows: NSIndexSet)     func scrollToRowAtIndex(_ index: Int) } ``` |

Modified [WKInterfaceTable.setRowTypes(_: [String])](https://developer.apple.com/documentation/watchkit/wkinterfacetable/1615839-setrowtypes)

|  | Declaration |
| --- | --- |
| From | ``` func setRowTypes(_ rowTypes: [AnyObject]) ``` |
| To | ``` func setRowTypes(_ rowTypes: [String]) ``` |

Modified [WKMenuItemIcon [enum]](https://developer.apple.com/documentation/watchkit/wkmenuitemicon)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [WKTextInputMode [enum]](https://developer.apple.com/documentation/watchkit/wktextinputmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [WKUserNotificationInterfaceController](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller)

|  | Declaration |
| --- | --- |
| From | ``` class WKUserNotificationInterfaceController : WKInterfaceController {     init()     func didReceiveRemoteNotification(_ remoteNotification: [NSObject : AnyObject], withCompletion completionHandler: (WKUserNotificationInterfaceType) -> Void)     func didReceiveLocalNotification(_ localNotification: UILocalNotification, withCompletion completionHandler: (WKUserNotificationInterfaceType) -> Void) } ``` |
| To | ``` class WKUserNotificationInterfaceController : WKInterfaceController {     init()     func didReceiveRemoteNotification(_ remoteNotification: [NSObject : AnyObject], withCompletion completionHandler: (WKUserNotificationInterfaceType) -> Void)     func didReceiveLocalNotification(_ localNotification: UILocalNotification, withCompletion completionHandler: (WKUserNotificationInterfaceType) -> Void)     func suggestionsForResponseToActionWithIdentifier(_ identifier: String, forRemoteNotification remoteNotification: [NSObject : AnyObject], inputLanguage inputLanguage: String) -> [String]     func suggestionsForResponseToActionWithIdentifier(_ identifier: String, forLocalNotification localNotification: UILocalNotification, inputLanguage inputLanguage: String) -> [String] } ``` |

Modified [WKUserNotificationInterfaceType [enum]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacetype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

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
