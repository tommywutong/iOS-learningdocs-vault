---
title: sizeLimitExceededNotification
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/sizelimitexceedednotification
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/sizelimitexceedednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/sizelimitexceedednotification.json'
content_hash: 'sha256:872d9cbd8dc12af7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# sizeLimitExceededNotification

<sub>Type Property</sub>

Posted when the amount of data in the defaults database exceeds the allowed maximum.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class let sizeLimitExceededNotification: NSNotification.Name
```

## Discussion

In tvOS, the system posts this notification as a warning when the size of your app’s defaults database reaches 512 kilobytes. If your app continues to write to the defaults database, the system terminates your app when the database reaches or exceeds 1 megabyte in size. The system doesn’t post size exceeded notifications for other platforms.

The system posts this notification on your app’s main thread.

## See Also

### Monitoring settings changes and issues

- [DidChangeMessage](didchangemessage.md) — A message the system sends when a user-defaults setting changes.
- [NSUserDefaultsDidChangeNotification](didchangenotification.md) — Posted when the current process changes the value of a setting.
- [SizeLimitExceededMessage](sizelimitexceededmessage.md) — A message the system sends when the size of the data in the defaults database exceeds the maximum.
