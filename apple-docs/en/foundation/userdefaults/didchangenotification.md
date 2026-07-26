---
title: didChangeNotification
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/didchangenotification
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/didchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/didchangenotification.json'
content_hash: 'sha256:b3c7da8108ac3ac7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# didChangeNotification

<sub>Type Property</sub>

Posted when the current process changes the value of a setting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let didChangeNotification: NSNotification.Name
```

## Discussion

When you write a new value to a setting, or remove an existing value, the system generates this notification to alert you that your app’s settings changed. Use this notification in other parts of your app to incorporate updated settings. The system posts this notification on the same thread you used to make the change.

If a different process changes your app’s settings, the system doesn’t generate this notification. To detect changes made by another process, register a key-value observer on the [UserDefaults](../userdefaults.md) object. Key-value observing reports all updates to setting values, regardless of which process made the change.

## See Also

### Monitoring settings changes and issues

- [DidChangeMessage](didchangemessage.md) — A message the system sends when a user-defaults setting changes.
- [SizeLimitExceededMessage](sizelimitexceededmessage.md) — A message the system sends when the size of the data in the defaults database exceeds the maximum.
- [NSUserDefaultsSizeLimitExceededNotification](sizelimitexceedednotification.md) — Posted when the amount of data in the defaults database exceeds the allowed maximum.
