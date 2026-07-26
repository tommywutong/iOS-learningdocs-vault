---
title: 'removeObject(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/removeobject(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/removeobject(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/removeobject%28forkey%3A%29.json'
content_hash: 'sha256:1223525b20f1b0fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# removeObject(forKey:)

<sub>Instance Method</sub>

Removes the value for the specified key from the defaults database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObject(forKey defaultName: String)
```

## Parameters

- `defaultName` — The key with the value you want to remove.

## Discussion

This method removes the specified key and value from the app-specific settings. If your `UserDefaults` object writes to settings for an app group or other shared settings file, the method removes the key from that file instead. This method removes the key and value only from the target domain, and doesn’t impact values for the same key in other domains. For example, it doesn’t remove keys and values from the global domain.

After you remove the key, the system generates a [NSUserDefaultsDidChangeNotification](didchangenotification.md) for registered observers.
