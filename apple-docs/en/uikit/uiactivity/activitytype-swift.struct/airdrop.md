---
title: airDrop
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/activitytype-swift.struct/airdrop
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.struct/airdrop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activitytype-swift.struct/airdrop.json'
content_hash: 'sha256:3ba097776a97ba8a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIActivity](../../uiactivity.md) · [ActivityType](../activitytype-swift.struct.md)

# airDrop

<sub>Type Property</sub>

A type of activity that makes the provided content available through AirDrop.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let airDrop: UIActivity.ActivityType
```

## Discussion

When using this service, you can provide [NSString](../../../foundation/nsstring.md), [NSAttributedString](../../../foundation/nsattributedstring.md), [UIImage](../../uiimage.md), and [NSURL](../../../foundation/nsurl.md) objects as data for the activity items. You may also provide [NSArray](../../../foundation/nsarray.md) or [NSDictionary](../../../foundation/nsdictionary.md) objects that contain the listed data types.

## See Also

### Constants

- [UIActivityTypeAddToHomeScreen](addtohomescreen.md)
- [UIActivityTypeAddToReadingList](addtoreadinglist.md) — A type of activity that adds the URL to Safari’s reading list.
- [UIActivityTypeAssignToContact](assigntocontact.md) — A type of activity that assigns the image to a contact.
- [UIActivityTypeCollaborationCopyLink](collaborationcopylink.md)
- [UIActivityTypeCollaborationInviteWithLink](collaborationinvitewithlink.md)
- [UIActivityTypeCopyToPasteboard](copytopasteboard.md) — A type of activity that posts the provided content to the pasteboard.
- [UIActivityTypeMail](mail.md) — A type of activity that posts the provided content to a new email message.
- [UIActivityTypeMarkupAsPDF](markupaspdf.md) — A type of activity that marks up the provided content as a PDF file.
- [UIActivityTypeMessage](message.md) — A type of activity that posts the provided content to the Messages app.
- [UIActivityTypeOpenInIBooks](openinibooks.md) — A type of activity that opens the content in iBooks.
- [UIActivityTypePostToFacebook](posttofacebook.md) — A type of activity that posts the provided content to the user’s wall on Facebook.
- [UIActivityTypePostToFlickr](posttoflickr.md) — A type of activity that posts the provided image to the user’s Flickr account.
- [UIActivityTypePostToTencentWeibo](posttotencentweibo.md) — A type of activity that posts the provided content to the user’s Tencent Weibo feed.
- [UIActivityTypePostToTwitter](posttotwitter.md) — A type of activity that posts the provided content to the user’s Twitter feed.
- [UIActivityTypePostToVimeo](posttovimeo.md) — A type of activity that posts the provided video to the user’s Vimeo account.
