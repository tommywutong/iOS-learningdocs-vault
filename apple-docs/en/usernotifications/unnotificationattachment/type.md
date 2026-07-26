---
title: type
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationattachment/type
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationattachment/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationattachment/type.json'
content_hash: 'sha256:f3aa7e425b38ca03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationAttachment](../unnotificationattachment.md)

# type

<sub>Instance Property</sub>

The UTI type of the attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var type: String { get }
```

## Discussion

The system derives the value of this property from the attachment data.

## See Also

### Getting the Attachment Contents

- [identifier](identifier.md) — The unique identifier for the attachment.
- [URL](url.md) — The URL of the file for this attachment.
