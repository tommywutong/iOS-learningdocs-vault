---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/MediaLibrary.html
archived_at: '2026-07-18T02:53:39.062134Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# MediaLibrary Changes for Swift

### MediaLibrary

Removed MLMediaSourceType.init(_: UInt)Added [MLPhotosFrontCameraGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosfrontcameragrouptypeidentifier)Added [MLPhotosScreenshotGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosscreenshotgrouptypeidentifier)Modified [MLMediaGroup](https://developer.apple.com/documentation/medialibrary/mlmediagroup)

|  | Declaration |
| --- | --- |
| From | ``` class MLMediaGroup : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary! { get }     unowned(unsafe) var parent: MLMediaGroup! { get }     var mediaSourceIdentifier: String! { get }     var name: String! { get }     var identifier: String! { get }     var typeIdentifier: String! { get }     var attributes: [NSObject : AnyObject]! { get }     var childGroups: [AnyObject]! { get }     @NSCopying var URL: NSURL! { get }     @NSCopying var modificationDate: NSDate! { get }     @NSCopying var iconImage: NSImage! { get }     var mediaObjects: [AnyObject]! { get } } ``` |
| To | ``` class MLMediaGroup : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get }     unowned(unsafe) var parent: MLMediaGroup? { get }     var mediaSourceIdentifier: String { get }     var name: String? { get }     var identifier: String { get }     var typeIdentifier: String { get }     var attributes: [String : AnyObject] { get }     var childGroups: [MLMediaGroup]? { get }     @NSCopying var URL: NSURL? { get }     @NSCopying var modificationDate: NSDate? { get }     @NSCopying var iconImage: NSImage? { get }     var mediaObjects: [MLMediaObject]? { get } } ``` |

Modified [MLMediaGroup.attributes](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419125-attributes)

|  | Declaration |
| --- | --- |
| From | ``` var attributes: [NSObject : AnyObject]! { get } ``` |
| To | ``` var attributes: [String : AnyObject] { get } ``` |

Modified [MLMediaGroup.childGroups](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1418990-childgroups)

|  | Declaration |
| --- | --- |
| From | ``` var childGroups: [AnyObject]! { get } ``` |
| To | ``` var childGroups: [MLMediaGroup]? { get } ``` |

Modified [MLMediaGroup.iconImage](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419172-iconimage)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var iconImage: NSImage! { get } ``` |
| To | ``` @NSCopying var iconImage: NSImage? { get } ``` |

Modified [MLMediaGroup.identifier](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419339-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String { get } ``` |

Modified [MLMediaGroup.mediaLibrary](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419261-medialibrary)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var mediaLibrary: MLMediaLibrary! { get } ``` |
| To | ``` unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get } ``` |

Modified [MLMediaGroup.mediaObjects](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1418982-mediaobjects)

|  | Declaration |
| --- | --- |
| From | ``` var mediaObjects: [AnyObject]! { get } ``` |
| To | ``` var mediaObjects: [MLMediaObject]? { get } ``` |

Modified [MLMediaGroup.mediaSourceIdentifier](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419322-mediasourceidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var mediaSourceIdentifier: String! { get } ``` |
| To | ``` var mediaSourceIdentifier: String { get } ``` |

Modified [MLMediaGroup.modificationDate](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419335-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var modificationDate: NSDate! { get } ``` |
| To | ``` @NSCopying var modificationDate: NSDate? { get } ``` |

Modified [MLMediaGroup.name](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419121-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified [MLMediaGroup.parent](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419333-parent)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var parent: MLMediaGroup! { get } ``` |
| To | ``` unowned(unsafe) var parent: MLMediaGroup? { get } ``` |

Modified [MLMediaGroup.typeIdentifier](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419155-typeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var typeIdentifier: String! { get } ``` |
| To | ``` var typeIdentifier: String { get } ``` |

Modified [MLMediaGroup.URL](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419079-url)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL? { get } ``` |

Modified [MLMediaLibrary](https://developer.apple.com/documentation/medialibrary/mlmedialibrary)

|  | Declaration |
| --- | --- |
| From | ``` class MLMediaLibrary : NSObject {     init!(options options: [NSObject : AnyObject]!)     var mediaSources: [NSObject : AnyObject]! { get } } ``` |
| To | ``` class MLMediaLibrary : NSObject {     init(options options: [String : AnyObject])     var mediaSources: [String : MLMediaSource]? { get } } ``` |

Modified [MLMediaLibrary.init(options: [String : AnyObject])](https://developer.apple.com/documentation/medialibrary/mlmedialibrary/1418988-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(options options: [NSObject : AnyObject]!) ``` |
| To | ``` init(options options: [String : AnyObject]) ``` |

Modified [MLMediaLibrary.mediaSources](https://developer.apple.com/documentation/medialibrary/mlmedialibrary/1419219-mediasources)

|  | Declaration |
| --- | --- |
| From | ``` var mediaSources: [NSObject : AnyObject]! { get } ``` |
| To | ``` var mediaSources: [String : MLMediaSource]? { get } ``` |

Modified [MLMediaObject](https://developer.apple.com/documentation/medialibrary/mlmediaobject)

|  | Declaration |
| --- | --- |
| From | ``` class MLMediaObject : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary! { get }     var identifier: String! { get }     var mediaSourceIdentifier: String! { get }     var attributes: [NSObject : AnyObject]! { get }     var mediaType: MLMediaType { get }     var contentType: String! { get }     var name: String! { get }     @NSCopying var URL: NSURL! { get }     @NSCopying var originalURL: NSURL! { get }     var fileSize: Int { get }     @NSCopying var modificationDate: NSDate! { get }     @NSCopying var thumbnailURL: NSURL! { get }     @NSCopying var artworkImage: NSImage! { get } } ``` |
| To | ``` class MLMediaObject : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get }     var identifier: String { get }     var mediaSourceIdentifier: String { get }     var attributes: [String : AnyObject] { get }     var mediaType: MLMediaType { get }     var contentType: String? { get }     var name: String? { get }     @NSCopying var URL: NSURL? { get }     @NSCopying var originalURL: NSURL? { get }     var fileSize: Int { get }     @NSCopying var modificationDate: NSDate? { get }     @NSCopying var thumbnailURL: NSURL? { get }     @NSCopying var artworkImage: NSImage? { get } } ``` |

Modified [MLMediaObject.artworkImage](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416701-artworkimage)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var artworkImage: NSImage! { get } ``` |
| To | ``` @NSCopying var artworkImage: NSImage? { get } ``` |

Modified [MLMediaObject.attributes](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416715-attributes)

|  | Declaration |
| --- | --- |
| From | ``` var attributes: [NSObject : AnyObject]! { get } ``` |
| To | ``` var attributes: [String : AnyObject] { get } ``` |

Modified [MLMediaObject.contentType](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416722-contenttype)

|  | Declaration |
| --- | --- |
| From | ``` var contentType: String! { get } ``` |
| To | ``` var contentType: String? { get } ``` |

Modified [MLMediaObject.identifier](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416716-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String { get } ``` |

Modified [MLMediaObject.mediaLibrary](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416699-medialibrary)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var mediaLibrary: MLMediaLibrary! { get } ``` |
| To | ``` unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get } ``` |

Modified [MLMediaObject.mediaSourceIdentifier](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416711-mediasourceidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var mediaSourceIdentifier: String! { get } ``` |
| To | ``` var mediaSourceIdentifier: String { get } ``` |

Modified [MLMediaObject.modificationDate](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416705-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var modificationDate: NSDate! { get } ``` |
| To | ``` @NSCopying var modificationDate: NSDate? { get } ``` |

Modified [MLMediaObject.name](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416720-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified [MLMediaObject.originalURL](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416703-originalurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var originalURL: NSURL! { get } ``` |
| To | ``` @NSCopying var originalURL: NSURL? { get } ``` |

Modified [MLMediaObject.thumbnailURL](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416708-thumbnailurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var thumbnailURL: NSURL! { get } ``` |
| To | ``` @NSCopying var thumbnailURL: NSURL? { get } ``` |

Modified [MLMediaObject.URL](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416718-url)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL? { get } ``` |

Modified [MLMediaSource](https://developer.apple.com/documentation/medialibrary/mlmediasource)

|  | Declaration |
| --- | --- |
| From | ``` class MLMediaSource : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary! { get }     var mediaSourceIdentifier: String! { get }     var attributes: [NSObject : AnyObject]! { get }     var rootMediaGroup: MLMediaGroup! { get }     func mediaGroupForIdentifier(_ mediaGroupIdentifier: String!) -> MLMediaGroup!     func mediaGroupsForIdentifiers(_ mediaGroupIdentifiers: [AnyObject]!) -> [NSObject : AnyObject]!     func mediaObjectForIdentifier(_ mediaObjectIdentifier: String!) -> MLMediaObject!     func mediaObjectsForIdentifiers(_ mediaObjectIdentifiers: [AnyObject]!) -> [NSObject : AnyObject]! } ``` |
| To | ``` class MLMediaSource : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get }     var mediaSourceIdentifier: String { get }     var attributes: [String : AnyObject] { get }     var rootMediaGroup: MLMediaGroup? { get }     func mediaGroupForIdentifier(_ mediaGroupIdentifier: String) -> MLMediaGroup?     func mediaGroupsForIdentifiers(_ mediaGroupIdentifiers: [String]) -> [String : MLMediaGroup]     func mediaObjectForIdentifier(_ mediaObjectIdentifier: String) -> MLMediaObject?     func mediaObjectsForIdentifiers(_ mediaObjectIdentifiers: [String]) -> [String : MLMediaObject] } ``` |

Modified [MLMediaSource.attributes](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419157-attributes)

|  | Declaration |
| --- | --- |
| From | ``` var attributes: [NSObject : AnyObject]! { get } ``` |
| To | ``` var attributes: [String : AnyObject] { get } ``` |

Modified [MLMediaSource.mediaGroupForIdentifier(_: String) -> MLMediaGroup?](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419283-mediagroupforidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func mediaGroupForIdentifier(_ mediaGroupIdentifier: String!) -> MLMediaGroup! ``` |
| To | ``` func mediaGroupForIdentifier(_ mediaGroupIdentifier: String) -> MLMediaGroup? ``` |

Modified [MLMediaSource.mediaGroupsForIdentifiers(_: [String]) -> [String : MLMediaGroup]](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419337-mediagroups)

|  | Declaration |
| --- | --- |
| From | ``` func mediaGroupsForIdentifiers(_ mediaGroupIdentifiers: [AnyObject]!) -> [NSObject : AnyObject]! ``` |
| To | ``` func mediaGroupsForIdentifiers(_ mediaGroupIdentifiers: [String]) -> [String : MLMediaGroup] ``` |

Modified [MLMediaSource.mediaLibrary](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419004-medialibrary)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var mediaLibrary: MLMediaLibrary! { get } ``` |
| To | ``` unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get } ``` |

Modified [MLMediaSource.mediaObjectForIdentifier(_: String) -> MLMediaObject?](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419209-mediaobject)

|  | Declaration |
| --- | --- |
| From | ``` func mediaObjectForIdentifier(_ mediaObjectIdentifier: String!) -> MLMediaObject! ``` |
| To | ``` func mediaObjectForIdentifier(_ mediaObjectIdentifier: String) -> MLMediaObject? ``` |

Modified [MLMediaSource.mediaObjectsForIdentifiers(_: [String]) -> [String : MLMediaObject]](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419123-mediaobjects)

|  | Declaration |
| --- | --- |
| From | ``` func mediaObjectsForIdentifiers(_ mediaObjectIdentifiers: [AnyObject]!) -> [NSObject : AnyObject]! ``` |
| To | ``` func mediaObjectsForIdentifiers(_ mediaObjectIdentifiers: [String]) -> [String : MLMediaObject] ``` |

Modified [MLMediaSource.mediaSourceIdentifier](https://developer.apple.com/documentation/medialibrary/mlmediasource/1418986-mediasourceidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var mediaSourceIdentifier: String! { get } ``` |
| To | ``` var mediaSourceIdentifier: String { get } ``` |

Modified [MLMediaSource.rootMediaGroup](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419255-rootmediagroup)

|  | Declaration |
| --- | --- |
| From | ``` var rootMediaGroup: MLMediaGroup! { get } ``` |
| To | ``` var rootMediaGroup: MLMediaGroup? { get } ``` |

Modified [MLMediaSourceType [struct]](https://developer.apple.com/documentation/medialibrary/mlmediasourcetype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MLMediaSourceType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Audio: MLMediaSourceType { get }     static var Image: MLMediaSourceType { get }     static var Movie: MLMediaSourceType { get } } ``` | RawOptionSetType |
| To | ``` struct MLMediaSourceType : OptionSetType {     init(rawValue rawValue: UInt)     static var Audio: MLMediaSourceType { get }     static var Image: MLMediaSourceType { get }     static var Movie: MLMediaSourceType { get } } ``` | OptionSetType |

Modified [MLMediaType [enum]](https://developer.apple.com/documentation/medialibrary/mlmediatype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

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
