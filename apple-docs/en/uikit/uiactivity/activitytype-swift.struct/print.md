---
title: print
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/activitytype-swift.struct/print
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.struct/print'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activitytype-swift.struct/print.json'
content_hash: 'sha256:9d996f6883d0c8c2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIActivity](../../uiactivity.md) · [ActivityType](../activitytype-swift.struct.md)

# print

<sub>Type Property</sub>

A type of activity that prints the provided content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let print: UIActivity.ActivityType
```

## Discussion

When using this service, you can provide [UIImage](../../uiimage.md) and [NSData](../../../foundation/nsdata.md) objects and [NSURL](../../../foundation/nsurl.md) objects pointing to local files as data for the activity items. You can also provide [UIPrintPageRenderer](../../uiprintpagerenderer.md), [UIPrintFormatter](../../uiprintformatter.md), and [UIPrintInfo](../../uiprintinfo.md) objects.

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
- [UIActivityTypeMessage](message.md) — A type of activity that posts the provided content to the Messages app.
- [UIActivityTypeOpenInIBooks](openinibooks.md) — A type of activity that opens the content in iBooks.
- [UIActivityTypePostToFacebook](posttofacebook.md) — A type of activity that posts the provided content to the user’s wall on Facebook.
- [UIActivityTypePostToFlickr](posttoflickr.md) — A type of activity that posts the provided image to the user’s Flickr account.
- [UIActivityTypePostToTencentWeibo](posttotencentweibo.md) — A type of activity that posts the provided content to the user’s Tencent Weibo feed.
- [UIActivityTypePostToTwitter](posttotwitter.md) — A type of activity that posts the provided content to the user’s Twitter feed.
