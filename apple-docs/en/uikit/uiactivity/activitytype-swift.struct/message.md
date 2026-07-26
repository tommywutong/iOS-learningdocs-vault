---
title: message
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/activitytype-swift.struct/message
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.struct/message'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activitytype-swift.struct/message.json'
content_hash: 'sha256:7fe87a3fad341008'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIActivity](../../uiactivity.md) · [ActivityType](../activitytype-swift.struct.md)

# message

<sub>Type Property</sub>

A type of activity that posts the provided content to the Messages app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let message: UIActivity.ActivityType
```

## Discussion

When using this service, you can provide [NSString](../../../foundation/nsstring.md) and [NSAttributedString](../../../foundation/nsattributedstring.md) objects as data for the activity items. You may also specify [NSURL](../../../foundation/nsurl.md) objects whose contents use the `sms` scheme.

If the device has MMS or FaceTime enabled, you can provide [UIImage](../../uiimage.md), and [NSURL](../../../foundation/nsurl.md) objects as data for the activity items.

To specify an [NSData](../../../foundation/nsdata.md) object, you must implement the [UIActivityItemSource](../../uiactivityitemsource.md) protocol, return the data object in [- activityViewController:itemForActivityType:](<../../uiactivityitemsource/activityviewcontroller(__itemforactivitytype_).md>), and return the data object’s UTI in [- activityViewController:dataTypeIdentifierForActivityType:](<../../uiactivityitemsource/activityviewcontroller(__datatypeidentifierforactivitytype_).md>).

## See Also

### Constants

- [UIActivityTypeAddToHomeScreen](addtohomescreen.md)
- [UIActivityTypeAddToReadingList](addtoreadinglist.md) — A type of activity that adds the URL to Safari’s reading list.
- [UIActivityTypeAirDrop](airdrop.md) — A type of activity that makes the provided content available through AirDrop.
- [UIActivityTypeAssignToContact](assigntocontact.md) — A type of activity that assigns the image to a contact.
- [UIActivityTypeCollaborationCopyLink](collaborationcopylink.md)
- [UIActivityTypeCollaborationInviteWithLink](collaborationinvitewithlink.md)
- [UIActivityTypeCopyToPasteboard](copytopasteboard.md) — A type of activity that posts the provided content to the pasteboard.
- [UIActivityTypeMail](mail.md) — A type of activity that posts the provided content to a new email message.
- [UIActivityTypeMarkupAsPDF](markupaspdf.md) — A type of activity that marks up the provided content as a PDF file.
- [UIActivityTypeOpenInIBooks](openinibooks.md) — A type of activity that opens the content in iBooks.
- [UIActivityTypePostToFacebook](posttofacebook.md) — A type of activity that posts the provided content to the user’s wall on Facebook.
- [UIActivityTypePostToFlickr](posttoflickr.md) — A type of activity that posts the provided image to the user’s Flickr account.
- [UIActivityTypePostToTencentWeibo](posttotencentweibo.md) — A type of activity that posts the provided content to the user’s Tencent Weibo feed.
- [UIActivityTypePostToTwitter](posttotwitter.md) — A type of activity that posts the provided content to the user’s Twitter feed.
- [UIActivityTypePostToVimeo](posttovimeo.md) — A type of activity that posts the provided video to the user’s Vimeo account.
