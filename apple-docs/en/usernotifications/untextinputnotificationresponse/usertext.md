---
title: userText
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/untextinputnotificationresponse/usertext
source_url: 'https://developer.apple.com/documentation/usernotifications/untextinputnotificationresponse/usertext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/untextinputnotificationresponse/usertext.json'
content_hash: 'sha256:a3cadeac82f08232'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNTextInputNotificationResponse](../untextinputnotificationresponse.md)

# userText

<sub>Instance Property</sub>

The text response provided by the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var userText: String { get }
```

## Discussion

If the user does not specify any text, this property contains an empty string.
