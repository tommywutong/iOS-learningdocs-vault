---
title: UNNotificationAttachmentOptionsThumbnailTimeKey
framework: User Notifications
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationattachmentoptionsthumbnailtimekey
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionsthumbnailtimekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationattachmentoptionsthumbnailtimekey.json'
content_hash: 'sha256:5897a901f1aaf882'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationAttachmentOptionsThumbnailTimeKey

<sub>Global Variable</sub>

The frame number of an animation to use as a thumbnail image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let UNNotificationAttachmentOptionsThumbnailTimeKey: String
```

## Discussion

For animated images, the value of this key is an [NSNumber](../foundation/nsnumber.md) containing the frame number to use as the thumbnail. For movies, the value of this key is the time (in seconds) into the movie from which to grab the thumbnail image; you may also specify the value as a [CMTime](../coremedia/cmtime.md) structure encoded using the [CMTimeCopyAsDictionary(_:allocator:)](<../coremedia/cmtimecopyasdictionary(__allocator_).md>) function.

## See Also

### Creating an Attachment

- [+ attachmentWithIdentifier:URL:options:error:](<unnotificationattachment/init(identifier_url_options_)-83grx.md>) — Creates an attachment object from the specified file and options.
- [UNNotificationAttachmentOptionsTypeHintKey](unnotificationattachmentoptionstypehintkey.md) — A hint about an attachment’s file type.
- [UNNotificationAttachmentOptionsThumbnailHiddenKey](unnotificationattachmentoptionsthumbnailhiddenkey.md) — A Boolean value indicating whether the system hides the attachment’s thumbnail.
- [UNNotificationAttachmentOptionsThumbnailClippingRectKey](unnotificationattachmentoptionsthumbnailclippingrectkey.md) — The clipping rectangle for a thumbnail image.
