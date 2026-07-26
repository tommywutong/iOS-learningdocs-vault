---
title: UNNotificationAttachmentOptionsTypeHintKey
framework: User Notifications
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationattachmentoptionstypehintkey
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionstypehintkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationattachmentoptionstypehintkey.json'
content_hash: 'sha256:92c73cea4a8af19d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationAttachmentOptionsTypeHintKey

<sub>Global Variable</sub>

A hint about an attachment’s file type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let UNNotificationAttachmentOptionsTypeHintKey: String
```

## Discussion

The value of this key is an [NSString](../foundation/nsstring.md) containing a Uniform Type Identifier (UTI) that describes the file’s type. If you don’t include this key, the system uses the attachment’s filename extension to determine its type.

## See Also

### Creating an Attachment

- [+ attachmentWithIdentifier:URL:options:error:](<unnotificationattachment/init(identifier_url_options_)-83grx.md>) — Creates an attachment object from the specified file and options.
- [UNNotificationAttachmentOptionsThumbnailHiddenKey](unnotificationattachmentoptionsthumbnailhiddenkey.md) — A Boolean value indicating whether the system hides the attachment’s thumbnail.
- [UNNotificationAttachmentOptionsThumbnailClippingRectKey](unnotificationattachmentoptionsthumbnailclippingrectkey.md) — The clipping rectangle for a thumbnail image.
- [UNNotificationAttachmentOptionsThumbnailTimeKey](unnotificationattachmentoptionsthumbnailtimekey.md) — The frame number of an animation to use as a thumbnail image.
