---
title: UNNotificationAttachmentOptionsThumbnailHiddenKey
framework: User Notifications
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationattachmentoptionsthumbnailhiddenkey
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionsthumbnailhiddenkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationattachmentoptionsthumbnailhiddenkey.json'
content_hash: 'sha256:0a56abb5d20caf08'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationAttachmentOptionsThumbnailHiddenKey

<sub>Global Variable</sub>

A Boolean value indicating whether the system hides the attachment’s thumbnail.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let UNNotificationAttachmentOptionsThumbnailHiddenKey: String
```

## Discussion

The value of this key is an [NSNumber](../foundation/nsnumber.md) containing a Boolean value. When set to [true](../swift/true.md), the attachment’s thumbnail isn’t displayed. If you don’t include this key, the system shows the thumbnail.

## See Also

### Creating an Attachment

- [+ attachmentWithIdentifier:URL:options:error:](<unnotificationattachment/init(identifier_url_options_)-83grx.md>) — Creates an attachment object from the specified file and options.
- [UNNotificationAttachmentOptionsTypeHintKey](unnotificationattachmentoptionstypehintkey.md) — A hint about an attachment’s file type.
- [UNNotificationAttachmentOptionsThumbnailClippingRectKey](unnotificationattachmentoptionsthumbnailclippingrectkey.md) — The clipping rectangle for a thumbnail image.
- [UNNotificationAttachmentOptionsThumbnailTimeKey](unnotificationattachmentoptionsthumbnailtimekey.md) — The frame number of an animation to use as a thumbnail image.
