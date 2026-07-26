---
title: 'init(string:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcomponents/init(string:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/init(string:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/init%28string%3A%29.json'
content_hash: 'sha256:b510ec61c2ecc6b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# init(string:)

<sub>Initializer</sub>

Creates a URL components instance from a URL string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(string: String)
```

## Parameters

- `string` — A URL location.

## Discussion

If `string` represents a malformed URL, this initializer returns `nil`.

## See Also

### Creating URL components

- [init()](<init().md>) — Creates a URL components instance without defining any of the components.
- [init(string:encodingInvalidCharacters:)](<init(string_encodinginvalidcharacters_).md>) — Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init(url:resolvingAgainstBaseURL:)](<init(url_resolvingagainstbaseurl_).md>) — Creates a URL components instance from a URL string, optionally resolving against a base URL.
