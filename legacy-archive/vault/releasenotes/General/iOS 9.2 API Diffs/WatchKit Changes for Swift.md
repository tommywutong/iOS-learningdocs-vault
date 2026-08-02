---
title: iOS 9.2 API Diffs
apple_id: TP40016605
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS92APIDiffs/Swift/WatchKit.html
archived_at: '2026-07-18T02:57:13.003850Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.2 API Diffs](iOS%209.1%20to%20iOS%209.2%20API%20Differences.md)


# WatchKit Changes for Swift

### WatchKit

Added [WatchKitErrorCode.RecordingFailedError](https://developer.apple.com/documentation/watchkit/watchkiterror/code/recordingfailed)Modified [WatchKitErrorCode [enum]](https://developer.apple.com/documentation/watchkit/watchkiterror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum WatchKitErrorCode : Int {     case UnknownError     case ApplicationDelegateWatchKitRequestReplyNotCalledError     case InvalidArgumentError     case MediaPlayerError     case DownloadError } extension WatchKitErrorCode : _BridgedNSError { } extension WatchKitErrorCode : _BridgedNSError { } ``` |
| To | ``` enum WatchKitErrorCode : Int {     case UnknownError     case ApplicationDelegateWatchKitRequestReplyNotCalledError     case InvalidArgumentError     case MediaPlayerError     case DownloadError     case RecordingFailedError } extension WatchKitErrorCode : _BridgedNSError { } extension WatchKitErrorCode : _BridgedNSError { } ``` |

Modified [WKInterfaceController](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller)

|  | Declaration |
| --- | --- |
| From | ``` class WKInterfaceController : NSObject {     init()     func awakeWithContext(_ context: AnyObject?)     var contentFrame: CGRect { get }     func willActivate()     func didDeactivate()     func didAppear()     func willDisappear()     func pickerDidFocus(_ picker: WKInterfacePicker)     func pickerDidResignFocus(_ picker: WKInterfacePicker)     func pickerDidSettle(_ picker: WKInterfacePicker)     func table(_ table: WKInterfaceTable, didSelectRowAtIndex rowIndex: Int)     func handleActionWithIdentifier(_ identifier: String?, forRemoteNotification remoteNotification: [NSObject : AnyObject])     func handleActionWithIdentifier(_ identifier: String?, forLocalNotification localNotification: UILocalNotification)     func handleUserActivity(_ userInfo: [NSObject : AnyObject]?)     func setTitle(_ title: String?)     func pushControllerWithName(_ name: String, context context: AnyObject?)     func popController()     func popToRootController()     class func reloadRootControllersWithNames(_ names: [String], contexts contexts: [AnyObject]?)     func becomeCurrentPage()     func presentControllerWithName(_ name: String, context context: AnyObject?)     func presentControllerWithNames(_ names: [String], contexts contexts: [AnyObject]?)     func dismissController()     func presentTextInputControllerWithSuggestions(_ suggestions: [String]?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void)     func presentTextInputControllerWithSuggestionsForLanguage(_ suggestionsHandler: ((String) -> [AnyObject]?)?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void)     func dismissTextInputController()     func presentMediaPlayerControllerWithURL(_ URL: NSURL, options options: [NSObject : AnyObject]?, completion completion: (Bool, NSTimeInterval, NSError?) -> Void)     func dismissMediaPlayerController()     func presentAudioRecordingControllerWithOutputURL(_ URL: NSURL, preset preset: WKAudioRecordingPreset, maximumDuration maximumDuration: NSTimeInterval, actionTitle actionTitle: String?, completion completion: (Bool, NSError?) -> Void)     func dismissAudioRecordingController()     func contextForSegueWithIdentifier(_ segueIdentifier: String) -> AnyObject?     func contextsForSegueWithIdentifier(_ segueIdentifier: String) -> [AnyObject]?     func contextForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> AnyObject?     func contextsForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> [AnyObject]?     func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void)     func presentAlertControllerWithTitle(_ title: String?, message message: String?, preferredStyle preferredStyle: WKAlertControllerStyle, actions actions: [WKAlertAction])     func presentAddPassesControllerWithPasses(_ passes: [PKPass], completion completion: () -> Void)     func dismissAddPassesController()     func addMenuItemWithImage(_ image: UIImage, title title: String, action action: Selector)     func addMenuItemWithImageNamed(_ imageName: String, title title: String, action action: Selector)     func addMenuItemWithItemIcon(_ itemIcon: WKMenuItemIcon, title title: String, action action: Selector)     func clearAllMenuItems()     func updateUserActivity(_ type: String, userInfo userInfo: [NSObject : AnyObject]?, webpageURL webpageURL: NSURL?)     func invalidateUserActivity()     class func openParentApplication(_ userInfo: [NSObject : AnyObject], reply reply: (([NSObject : AnyObject], NSError?) -> Void)?) -> Bool     func beginGlanceUpdates()     func endGlanceUpdates() } extension WKInterfaceController {     class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(_ namesAndContexts: [(name: String, context: AnyObject)]) } extension WKInterfaceController {     class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(_ namesAndContexts: [(name: String, context: AnyObject)]) } ``` |
| To | ``` class WKInterfaceController : NSObject {     init()     func awakeWithContext(_ context: AnyObject?)     var contentFrame: CGRect { get }     func willActivate()     func didDeactivate()     func didAppear()     func willDisappear()     func pickerDidFocus(_ picker: WKInterfacePicker)     func pickerDidResignFocus(_ picker: WKInterfacePicker)     func pickerDidSettle(_ picker: WKInterfacePicker)     func table(_ table: WKInterfaceTable, didSelectRowAtIndex rowIndex: Int)     func handleActionWithIdentifier(_ identifier: String?, forRemoteNotification remoteNotification: [NSObject : AnyObject])     func handleActionWithIdentifier(_ identifier: String?, forLocalNotification localNotification: UILocalNotification)     func handleUserActivity(_ userInfo: [NSObject : AnyObject]?)     func setTitle(_ title: String?)     func pushControllerWithName(_ name: String, context context: AnyObject?)     func popController()     func popToRootController()     class func reloadRootControllersWithNames(_ names: [String], contexts contexts: [AnyObject]?)     func becomeCurrentPage()     func presentControllerWithName(_ name: String, context context: AnyObject?)     func presentControllerWithNames(_ names: [String], contexts contexts: [AnyObject]?)     func dismissController()     func presentTextInputControllerWithSuggestions(_ suggestions: [String]?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void)     func presentTextInputControllerWithSuggestionsForLanguage(_ suggestionsHandler: ((String) -> [AnyObject]?)?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void)     func dismissTextInputController()     func presentMediaPlayerControllerWithURL(_ URL: NSURL, options options: [NSObject : AnyObject]?, completion completion: (Bool, NSTimeInterval, NSError?) -> Void)     func dismissMediaPlayerController()     func presentAudioRecorderControllerWithOutputURL(_ URL: NSURL, preset preset: WKAudioRecorderPreset, options options: [NSObject : AnyObject]?, completion completion: (Bool, NSError?) -> Void)     func dismissAudioRecorderController()     func contextForSegueWithIdentifier(_ segueIdentifier: String) -> AnyObject?     func contextsForSegueWithIdentifier(_ segueIdentifier: String) -> [AnyObject]?     func contextForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> AnyObject?     func contextsForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> [AnyObject]?     func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void)     func presentAlertControllerWithTitle(_ title: String?, message message: String?, preferredStyle preferredStyle: WKAlertControllerStyle, actions actions: [WKAlertAction])     func presentAddPassesControllerWithPasses(_ passes: [PKPass], completion completion: () -> Void)     func dismissAddPassesController()     func addMenuItemWithImage(_ image: UIImage, title title: String, action action: Selector)     func addMenuItemWithImageNamed(_ imageName: String, title title: String, action action: Selector)     func addMenuItemWithItemIcon(_ itemIcon: WKMenuItemIcon, title title: String, action action: Selector)     func clearAllMenuItems()     func updateUserActivity(_ type: String, userInfo userInfo: [NSObject : AnyObject]?, webpageURL webpageURL: NSURL?)     func invalidateUserActivity()     class func openParentApplication(_ userInfo: [NSObject : AnyObject], reply reply: (([NSObject : AnyObject], NSError?) -> Void)?) -> Bool     func beginGlanceUpdates()     func endGlanceUpdates() } extension WKInterfaceController {     class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(_ namesAndContexts: [(name: String, context: AnyObject)]) } extension WKInterfaceController {     class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(_ namesAndContexts: [(name: String, context: AnyObject)]) } ``` |

Modified [WKInterfaceDevice](https://developer.apple.com/documentation/watchkit/wkinterfacedevice)

|  | Declaration |
| --- | --- |
| From | ``` class WKInterfaceDevice : NSObject {     class func currentDevice() -> WKInterfaceDevice     func addCachedImage(_ image: UIImage, name name: String) -> Bool     func addCachedImageWithData(_ imageData: NSData, name name: String) -> Bool     func removeCachedImageWithName(_ name: String)     func removeAllCachedImages()     var screenBounds: CGRect { get }     var screenScale: CGFloat { get }     var preferredContentSizeCategory: String { get }     var cachedImages: [String : NSNumber] { get }     var systemVersion: String { get }     var name: String { get }     var model: String { get }     var localizedModel: String { get }     var systemName: String { get }     func playHaptic(_ type: WKHapticType) } ``` |
| To | ``` class WKInterfaceDevice : NSObject {     class func currentDevice() -> WKInterfaceDevice     func addCachedImage(_ image: UIImage, name name: String) -> Bool     func addCachedImageWithData(_ imageData: NSData, name name: String) -> Bool     func removeCachedImageWithName(_ name: String)     func removeAllCachedImages()     var cachedImages: [String : NSNumber] { get }     var screenBounds: CGRect { get }     var screenScale: CGFloat { get }     var preferredContentSizeCategory: String { get }     var layoutDirection: WKInterfaceLayoutDirection { get }     class func interfaceLayoutDirectionForSemanticContentAttribute(_ semanticContentAttribute: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection     var systemVersion: String { get }     var name: String { get }     var model: String { get }     var localizedModel: String { get }     var systemName: String { get }     func playHaptic(_ type: WKHapticType) } ``` |

Modified [WKInterfaceObject](https://developer.apple.com/documentation/watchkit/wkinterfaceobject)

|  | Declaration |
| --- | --- |
| From | ``` class WKInterfaceObject : NSObject {     init()     func setHidden(_ hidden: Bool)     func setAlpha(_ alpha: CGFloat)     func setHorizontalAlignment(_ horizontalAlignment: WKInterfaceObjectHorizontalAlignment)     func setVerticalAlignment(_ verticalAlignment: WKInterfaceObjectVerticalAlignment)     func setWidth(_ width: CGFloat)     func setHeight(_ height: CGFloat)     func setRelativeWidth(_ width: CGFloat, withAdjustment adjustment: CGFloat)     func setRelativeHeight(_ height: CGFloat, withAdjustment adjustment: CGFloat)     func sizeToFitWidth()     func sizeToFitHeight()     var interfaceProperty: String { get } } extension WKInterfaceObject {     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion]) } ``` |
| To | ``` class WKInterfaceObject : NSObject {     init()     func setHidden(_ hidden: Bool)     func setAlpha(_ alpha: CGFloat)     func setSemanticContentAttribute(_ semanticContentAttribute: WKInterfaceSemanticContentAttribute)     func setHorizontalAlignment(_ horizontalAlignment: WKInterfaceObjectHorizontalAlignment)     func setVerticalAlignment(_ verticalAlignment: WKInterfaceObjectVerticalAlignment)     func setWidth(_ width: CGFloat)     func setHeight(_ height: CGFloat)     func setRelativeWidth(_ width: CGFloat, withAdjustment adjustment: CGFloat)     func setRelativeHeight(_ height: CGFloat, withAdjustment adjustment: CGFloat)     func sizeToFitWidth()     func sizeToFitHeight()     var interfaceProperty: String { get } } extension WKInterfaceObject {     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion]) } ``` |

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
