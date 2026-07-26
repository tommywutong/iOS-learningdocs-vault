---
title: standard
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/standard
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/standard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/standard.json'
content_hash: 'sha256:92b7e2641f5e3377'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# standard

<sub>Type Property</sub>

The shared defaults object for the current app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var standard: UserDefaults { get }
```

## Return Value

The shared defaults object for the app.

## Discussion

Each app maintains a single, shared defaults object for you to use in your code. The first time your app retrieves the value of this property, it creates the shared object and caches the result. Subsequent retrieval attempts return the cached object.

The shared object retrieves settings from all of the standard domains. If you add a domain using the [- addSuiteNamed:](<addsuite(named_).md>) method, the object retrieves values from that domain in addition to the standard ones. Custom domains remain in the search list until you remove them or the app exits. When you write settings using the shared object, it writes them to the current app’s settings.

## See Also

### Creating a user defaults object

- [- init](<init().md>) — Creates a new defaults object and initializes it with the app’s current settings.
- [- initWithSuiteName:](<init(suitename_).md>) — Creates a new defaults object and initializes it with the settings from the specified database.
