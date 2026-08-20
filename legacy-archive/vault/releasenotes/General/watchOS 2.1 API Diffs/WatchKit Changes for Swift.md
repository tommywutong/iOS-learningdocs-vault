---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/WatchKit.html
archived_at: '2026-07-18T02:58:09.465707Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# WatchKit Changes for Swift

### WatchKit

Added [WKInterfaceDevice.interfaceLayoutDirectionForSemanticContentAttribute(_: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection [class]](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1628117-interfacelayoutdirection)Added [WKInterfaceDevice.layoutDirection](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1628161-layoutdirection)Added [WKInterfaceLayoutDirection [enum]](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection)Added [WKInterfaceLayoutDirection.LeftToRight](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection/lefttoright)Added [WKInterfaceLayoutDirection.RightToLeft](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection/righttoleft)Added [WKInterfaceObject.setSemanticContentAttribute(_: WKInterfaceSemanticContentAttribute)](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/1628136-setsemanticcontentattribute)Added [WKInterfaceSemanticContentAttribute [enum]](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute)Added [WKInterfaceSemanticContentAttribute.ForceLeftToRight](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/wkinterfacesemanticcontentattributeforcelefttoright)Added [WKInterfaceSemanticContentAttribute.ForceRightToLeft](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/wkinterfacesemanticcontentattributeforcerighttoleft)Added [WKInterfaceSemanticContentAttribute.Playback](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/playback)Added [WKInterfaceSemanticContentAttribute.Spatial](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/wkinterfacesemanticcontentattributespatial)Added [WKInterfaceSemanticContentAttribute.Unspecified](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/wkinterfacesemanticcontentattributeunspecified)Modified [WatchKitErrorCode [enum]](https://developer.apple.com/documentation/watchkit/watchkiterror/code)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum WatchKitErrorCode : Int {     case UnknownError     case ApplicationDelegateWatchKitRequestReplyNotCalledError     case InvalidArgumentError     case MediaPlayerError     case DownloadError     case RecordingFailedError } extension WatchKitErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension WatchKitErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum WatchKitErrorCode : Int {     case UnknownError     case ApplicationDelegateWatchKitRequestReplyNotCalledError     case InvalidArgumentError     case MediaPlayerError     case DownloadError     case RecordingFailedError } extension WatchKitErrorCode : _BridgedNSError { } extension WatchKitErrorCode : _BridgedNSError { } ``` | -- |

Modified [WKAccessibilityImageRegion](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKAlertAction](https://developer.apple.com/documentation/watchkit/wkalertaction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKAlertActionStyle [enum]](https://developer.apple.com/documentation/watchkit/wkalertactionstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKAlertControllerStyle [enum]](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKAudioFileAsset](https://developer.apple.com/documentation/watchkit/wkaudiofileasset)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKAudioFilePlayer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKAudioFilePlayerItem](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKAudioFilePlayerItemStatus [enum]](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKAudioFilePlayerStatus [enum]](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKAudioFileQueuePlayer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKAudioRecorderPreset [enum]](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKExtension](https://developer.apple.com/documentation/watchkit/wkextension)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKHapticType [enum]](https://developer.apple.com/documentation/watchkit/wkhaptictype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKImage](https://developer.apple.com/documentation/watchkit/wkimage)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKImage : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(image image: UIImage)     class func imageWithImage(_ image: UIImage) -> Self     convenience init(imageData imageData: NSData)     class func imageWithImageData(_ imageData: NSData) -> Self     convenience init(imageName imageName: String)     class func imageWithImageName(_ imageName: String) -> Self     init()     var image: UIImage? { get }     var imageData: NSData? { get }     var imageName: String? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class WKImage : NSObject, NSCopying, NSSecureCoding {     convenience init(image image: UIImage)     class func imageWithImage(_ image: UIImage) -> Self     convenience init(imageData imageData: NSData)     class func imageWithImageData(_ imageData: NSData) -> Self     convenience init(imageName imageName: String)     class func imageWithImageName(_ imageName: String) -> Self     init()     var image: UIImage? { get }     var imageData: NSData? { get }     var imageName: String? { get } } ``` | NSCopying, NSSecureCoding |

Modified [WKInterfaceButton](https://developer.apple.com/documentation/watchkit/wkinterfacebutton)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceController](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceDate](https://developer.apple.com/documentation/watchkit/wkinterfacedate)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceDevice](https://developer.apple.com/documentation/watchkit/wkinterfacedevice)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceDevice : NSObject {     class func currentDevice() -> WKInterfaceDevice     func addCachedImage(_ image: UIImage, name name: String) -> Bool     func addCachedImageWithData(_ imageData: NSData, name name: String) -> Bool     func removeCachedImageWithName(_ name: String)     func removeAllCachedImages()     var cachedImages: [String : NSNumber] { get }     var screenBounds: CGRect { get }     var screenScale: CGFloat { get }     var preferredContentSizeCategory: String { get }     var systemVersion: String { get }     var name: String { get }     var model: String { get }     var localizedModel: String { get }     var systemName: String { get }     func playHaptic(_ type: WKHapticType) } ``` | AnyObject |
| To | ``` class WKInterfaceDevice : NSObject {     class func currentDevice() -> WKInterfaceDevice     func addCachedImage(_ image: UIImage, name name: String) -> Bool     func addCachedImageWithData(_ imageData: NSData, name name: String) -> Bool     func removeCachedImageWithName(_ name: String)     func removeAllCachedImages()     var cachedImages: [String : NSNumber] { get }     var screenBounds: CGRect { get }     var screenScale: CGFloat { get }     var preferredContentSizeCategory: String { get }     var layoutDirection: WKInterfaceLayoutDirection { get }     class func interfaceLayoutDirectionForSemanticContentAttribute(_ semanticContentAttribute: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection     var systemVersion: String { get }     var name: String { get }     var model: String { get }     var localizedModel: String { get }     var systemName: String { get }     func playHaptic(_ type: WKHapticType) } ``` | -- |

Modified [WKInterfaceGroup](https://developer.apple.com/documentation/watchkit/wkinterfacegroup)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, WKImageAnimatable |
| To | WKImageAnimatable |

Modified [WKInterfaceImage](https://developer.apple.com/documentation/watchkit/wkinterfaceimage)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSObjectProtocol, WKImageAnimatable |
| To | WKImageAnimatable |

Modified [WKInterfaceLabel](https://developer.apple.com/documentation/watchkit/wkinterfacelabel)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceMap](https://developer.apple.com/documentation/watchkit/wkinterfacemap)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceMapPinColor [enum]](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKInterfaceMovie](https://developer.apple.com/documentation/watchkit/wkinterfacemovie)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceObject](https://developer.apple.com/documentation/watchkit/wkinterfaceobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceObject : NSObject {     init()     func setHidden(_ hidden: Bool)     func setAlpha(_ alpha: CGFloat)     func setHorizontalAlignment(_ horizontalAlignment: WKInterfaceObjectHorizontalAlignment)     func setVerticalAlignment(_ verticalAlignment: WKInterfaceObjectVerticalAlignment)     func setWidth(_ width: CGFloat)     func setHeight(_ height: CGFloat)     func setRelativeWidth(_ width: CGFloat, withAdjustment adjustment: CGFloat)     func setRelativeHeight(_ height: CGFloat, withAdjustment adjustment: CGFloat)     func sizeToFitWidth()     func sizeToFitHeight()     var interfaceProperty: String { get } } extension WKInterfaceObject {     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion]) } ``` | AnyObject |
| To | ``` class WKInterfaceObject : NSObject {     init()     func setHidden(_ hidden: Bool)     func setAlpha(_ alpha: CGFloat)     func setSemanticContentAttribute(_ semanticContentAttribute: WKInterfaceSemanticContentAttribute)     func setHorizontalAlignment(_ horizontalAlignment: WKInterfaceObjectHorizontalAlignment)     func setVerticalAlignment(_ verticalAlignment: WKInterfaceObjectVerticalAlignment)     func setWidth(_ width: CGFloat)     func setHeight(_ height: CGFloat)     func setRelativeWidth(_ width: CGFloat, withAdjustment adjustment: CGFloat)     func setRelativeHeight(_ height: CGFloat, withAdjustment adjustment: CGFloat)     func sizeToFitWidth()     func sizeToFitHeight()     var interfaceProperty: String { get } } extension WKInterfaceObject {     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion]) } ``` | -- |

Modified [WKInterfaceObjectHorizontalAlignment [enum]](https://developer.apple.com/documentation/watchkit/wkinterfaceobjecthorizontalalignment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKInterfaceObjectVerticalAlignment [enum]](https://developer.apple.com/documentation/watchkit/wkinterfaceobjectverticalalignment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKInterfacePicker](https://developer.apple.com/documentation/watchkit/wkinterfacepicker)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceSeparator](https://developer.apple.com/documentation/watchkit/wkinterfaceseparator)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceSlider](https://developer.apple.com/documentation/watchkit/wkinterfaceslider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceSwitch](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceTable](https://developer.apple.com/documentation/watchkit/wkinterfacetable)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKInterfaceTimer](https://developer.apple.com/documentation/watchkit/wkinterfacetimer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKMenuItemIcon [enum]](https://developer.apple.com/documentation/watchkit/wkmenuitemicon)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKPickerItem](https://developer.apple.com/documentation/watchkit/wkpickeritem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKPickerItem : NSObject, NSSecureCoding, NSCoding {     var title: String?     var caption: String?     @NSCopying var accessoryImage: WKImage?     @NSCopying var contentImage: WKImage? } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class WKPickerItem : NSObject, NSSecureCoding {     var title: String?     var caption: String?     @NSCopying var accessoryImage: WKImage?     @NSCopying var contentImage: WKImage? } ``` | NSSecureCoding |

Modified [WKTextInputMode [enum]](https://developer.apple.com/documentation/watchkit/wktextinputmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKUserNotificationInterfaceController](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [WKUserNotificationInterfaceType [enum]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [WKVideoGravity [enum]](https://developer.apple.com/documentation/watchkit/wkvideogravity)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
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
