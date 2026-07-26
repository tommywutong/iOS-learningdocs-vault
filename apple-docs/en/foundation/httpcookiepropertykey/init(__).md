---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiepropertykey/init(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiepropertykey/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiepropertykey/init%28_%3A%29.json'
content_hash: 'sha256:2664fa2f3347a43f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookiePropertyKey](../httpcookiepropertykey.md)

# init(_:)

<sub>Initializer</sub>

Creates an HTTP cookie property key using the given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ rawValue: String)
```

## Parameters

- `rawValue` — The string to use as a key.

## Discussion

You can use this initializer to create HTTP cookie property keys that aren’t already represented by the predefined constants.

This convenience initializer is identical to [init(rawValue:)](<init(rawvalue_).md>).

## See Also

### Creating custom cookie property keys

- [init(rawValue:)](<init(rawvalue_).md>) — Creates an HTTP cookie property key using the given string.
