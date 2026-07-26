---
title: 'init(identifier:url:options:)'
framework: User Notifications
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unnotificationattachment/init(identifier:url:options:)-83grx'
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationattachment/init(identifier:url:options:)-83grx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationattachment/init%28identifier%3Aurl%3Aoptions%3A%29-83grx.json'
content_hash: 'sha256:329b95852ef6f124'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationAttachment](../unnotificationattachment.md)

# init(identifier:url:options:)

<sub>Initializer</sub>

Creates an attachment object from the specified file and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
convenience init(identifier: String, url URL: URL, options: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `identifier` — The unique identifier of the attachment. Use this string to identify the attachment later. If you specify an empty string, this method creates a unique identifier string for you.

- `URL` — The URL of the file you want to attach to the notification. The URL must be a file URL and the file must be readable by the current process. This parameter must not be `nil`. For a list of supported file types, see [Supported File Types](../unnotificationattachment.md#Supported-File-Types).

- `options` — A dictionary of options related to the attached file. Use the options to specify meta information about the attachment, such as the clipping rectangle to use for the resulting thumbnail.

## Return Value

An attachment object containing information about the specified file or `nil` if the attachment could not be created.

## Discussion

This method verifies that the specified file is readable and that the file format is one of the supported types. When errors occur, the method provides an appropriate `error` object.

When you schedule a notification request containing the attachment, the system moves the attachment’s file to a new location to facilitate access by the appropriate processes. After the move, the only way to access the file is using the methods of the [UNUserNotificationCenter](../unusernotificationcenter.md) object.

## See Also

### Creating an Attachment

- [UNNotificationAttachmentOptionsTypeHintKey](../unnotificationattachmentoptionstypehintkey.md) — A hint about an attachment’s file type.
- [UNNotificationAttachmentOptionsThumbnailHiddenKey](../unnotificationattachmentoptionsthumbnailhiddenkey.md) — A Boolean value indicating whether the system hides the attachment’s thumbnail.
- [UNNotificationAttachmentOptionsThumbnailClippingRectKey](../unnotificationattachmentoptionsthumbnailclippingrectkey.md) — The clipping rectangle for a thumbnail image.
- [UNNotificationAttachmentOptionsThumbnailTimeKey](../unnotificationattachmentoptionsthumbnailtimekey.md) — The frame number of an animation to use as a thumbnail image.
