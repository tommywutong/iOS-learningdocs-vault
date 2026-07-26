---
title: url
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationattachment/url
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationattachment/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationattachment/url.json'
content_hash: 'sha256:7380206263e89cec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationAttachment](../unnotificationattachment.md)

# url

<sub>Instance Property</sub>

The URL of the file for this attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var url: URL { get }
```

## Discussion

The file at the specified URL is security scoped to your app. Before you access it, call the [startAccessingSecurityScopedResource()](<../../foundation/url/startaccessingsecurityscopedresource().md>) method of [NSURL](../../foundation/nsurl.md).

## See Also

### Getting the Attachment Contents

- [identifier](identifier.md) — The unique identifier for the attachment.
- [type](type.md) — The UTI type of the attachment.
