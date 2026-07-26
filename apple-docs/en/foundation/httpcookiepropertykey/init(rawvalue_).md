---
title: 'init(rawValue:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiepropertykey/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiepropertykey/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiepropertykey/init%28rawvalue%3A%29.json'
content_hash: 'sha256:3efaba208d9bf6be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookiePropertyKey](../httpcookiepropertykey.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates an HTTP cookie property key using the given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(rawValue: String)
```

## Parameters

- `rawValue` — The string to use as a key.

## Discussion

You can use this initializer to create HTTP cookie property keys that aren’t already represented by the predefined constants.

## See Also

### Creating custom cookie property keys

- [init(_:)](<init(__).md>) — Creates an HTTP cookie property key using the given string.
