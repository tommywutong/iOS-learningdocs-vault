---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/init()
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/init%28%29.json'
content_hash: 'sha256:40030742d0b2e1ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# init()

<sub>Initializer</sub>

Creates a new defaults object and initializes it with the app’s current settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init()
```

## Discussion

Use this method to create a new defaults object to manage the app’s settings. If you add a domain using the [- addSuiteNamed:](<addsuite(named_).md>) method, the returned object retrieves values in that domain in addition to the standard ones. Custom domains remain in the search list until you remove them or release the object. When you write setting values using this object, it writes them to the current app’s settings.

## See Also

### Creating a user defaults object

- [standardUserDefaults](standard.md) — The shared defaults object for the current app.
- [- initWithSuiteName:](<init(suitename_).md>) — Creates a new defaults object and initializes it with the settings from the specified database.
