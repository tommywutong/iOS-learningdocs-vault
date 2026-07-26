---
title: addToReadingList
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/activitytype-swift.struct/addtoreadinglist
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.struct/addtoreadinglist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activitytype-swift.struct/addtoreadinglist.json'
content_hash: 'sha256:feadc8c44f570a22'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIActivity](../../uiactivity.md) · [ActivityType](../activitytype-swift.struct.md)

# addToReadingList

<sub>Type Property</sub>

A type of activity that adds the URL to Safari’s reading list.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let addToReadingList: UIActivity.ActivityType
```

## Discussion

When using this service, you can provide an [NSURL](../../../foundation/nsurl.md) object whose contents uses the `http` or `https` scheme that points to the page to add.

## See Also

### Constants

- [UIActivityTypeAddToHomeScreen](addtohomescreen.md)
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
- [UIActivityTypePostToVimeo](posttovimeo.md) — A type of activity that posts the provided video to the user’s Vimeo account.
