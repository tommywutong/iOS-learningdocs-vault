---
title: UNNotificationAttachmentOptionsThumbnailClippingRectKey
framework: User Notifications
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationattachmentoptionsthumbnailclippingrectkey
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionsthumbnailclippingrectkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationattachmentoptionsthumbnailclippingrectkey.json'
content_hash: 'sha256:b56772d7a0aca6e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationAttachmentOptionsThumbnailClippingRectKey

<sub>Global Variable</sub>

The clipping rectangle for a thumbnail image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let UNNotificationAttachmentOptionsThumbnailClippingRectKey: String
```

## Discussion

The value of this key is a dictionary containing a normalized [CGRect](../corefoundation/cgrect.md) — a unit rectangle whose values are in the range `0.0` to `1.0` and represent the portion of the original image that you want to display. For example, specifying an origin of (`0.25`, `0.25`) and a size of (`0.5`, `0.5`) defines a clipping rectangle that shows only the center portion of the image. Use the [dictionaryRepresentation](../corefoundation/cgrect/dictionaryrepresentation.md) function to create the dictionary for your rectangle.

## See Also

### Creating an Attachment

- [+ attachmentWithIdentifier:URL:options:error:](<unnotificationattachment/init(identifier_url_options_)-83grx.md>) — Creates an attachment object from the specified file and options.
- [UNNotificationAttachmentOptionsTypeHintKey](unnotificationattachmentoptionstypehintkey.md) — A hint about an attachment’s file type.
- [UNNotificationAttachmentOptionsThumbnailHiddenKey](unnotificationattachmentoptionsthumbnailhiddenkey.md) — A Boolean value indicating whether the system hides the attachment’s thumbnail.
- [UNNotificationAttachmentOptionsThumbnailTimeKey](unnotificationattachmentoptionsthumbnailtimekey.md) — The frame number of an animation to use as a thumbnail image.
