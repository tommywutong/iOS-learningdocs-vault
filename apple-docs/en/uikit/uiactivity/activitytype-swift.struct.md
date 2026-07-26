---
title: UIActivity.ActivityType
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/activitytype-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activitytype-swift.struct.json'
content_hash: 'sha256:8ca28701d935b73a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# UIActivity.ActivityType

<sub>Structure</sub>

A structure that describes the types of activities for which the system has built-in support.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct ActivityType
```

## Overview

These constants represent the values that can be stored in the [activityType](activitytype-swift.property.md) property of system-defined activity objects.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIActivityTypeAddToHomeScreen](activitytype-swift.struct/addtohomescreen.md)
- [UIActivityTypeAddToReadingList](activitytype-swift.struct/addtoreadinglist.md) — A type of activity that adds the URL to Safari’s reading list.
- [UIActivityTypeAirDrop](activitytype-swift.struct/airdrop.md) — A type of activity that makes the provided content available through AirDrop.
- [UIActivityTypeAssignToContact](activitytype-swift.struct/assigntocontact.md) — A type of activity that assigns the image to a contact.
- [UIActivityTypeCollaborationCopyLink](activitytype-swift.struct/collaborationcopylink.md)
- [UIActivityTypeCollaborationInviteWithLink](activitytype-swift.struct/collaborationinvitewithlink.md)
- [UIActivityTypeCopyToPasteboard](activitytype-swift.struct/copytopasteboard.md) — A type of activity that posts the provided content to the pasteboard.
- [UIActivityTypeMail](activitytype-swift.struct/mail.md) — A type of activity that posts the provided content to a new email message.
- [UIActivityTypeMarkupAsPDF](activitytype-swift.struct/markupaspdf.md) — A type of activity that marks up the provided content as a PDF file.
- [UIActivityTypeMessage](activitytype-swift.struct/message.md) — A type of activity that posts the provided content to the Messages app.
- [UIActivityTypeOpenInIBooks](activitytype-swift.struct/openinibooks.md) — A type of activity that opens the content in iBooks.
- [UIActivityTypePostToFacebook](activitytype-swift.struct/posttofacebook.md) — A type of activity that posts the provided content to the user’s wall on Facebook.
- [UIActivityTypePostToFlickr](activitytype-swift.struct/posttoflickr.md) — A type of activity that posts the provided image to the user’s Flickr account.
- [UIActivityTypePostToTencentWeibo](activitytype-swift.struct/posttotencentweibo.md) — A type of activity that posts the provided content to the user’s Tencent Weibo feed.
- [UIActivityTypePostToTwitter](activitytype-swift.struct/posttotwitter.md) — A type of activity that posts the provided content to the user’s Twitter feed.
- [UIActivityTypePostToVimeo](activitytype-swift.struct/posttovimeo.md) — A type of activity that posts the provided video to the user’s Vimeo account.
- [UIActivityTypePostToWeibo](activitytype-swift.struct/posttoweibo.md) — A type of activity that posts the provided content to the user’s Weibo feed.
- [UIActivityTypePrint](activitytype-swift.struct/print.md) — A type of activity that prints the provided content.
- [UIActivityTypeSaveToCameraRoll](activitytype-swift.struct/savetocameraroll.md) — A type of activity that assigns the image or video to the user’s camera roll.
- [UIActivityTypeSharePlay](activitytype-swift.struct/shareplay.md) — A type of activity that makes the provided content available through SharePlay.

### Initializers

- [init(_:)](<activitytype-swift.struct/init(__).md>) — Creates an activity type.
- [init(rawValue:)](<activitytype-swift.struct/init(rawvalue_).md>) — Creates a new instance with the specified raw value.

## See Also

### Getting the activity information

- [activityCategory](activitycategory.md) — The category of the activity, which may be used to group activities in the UI.
- [Category](category.md) — An enumeration that defines categories of activities.
- [activityType](activitytype-swift.property.md) — The type of service being provided.
- [activityTitle](activitytitle.md) — A user-readable string that describes the service.
- [activityImage](activityimage.md) — An image that identifies the service to the user.
