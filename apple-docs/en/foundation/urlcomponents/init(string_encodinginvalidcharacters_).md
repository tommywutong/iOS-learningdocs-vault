---
title: 'init(string:encodingInvalidCharacters:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcomponents/init(string:encodinginvalidcharacters:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/init(string:encodinginvalidcharacters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/init%28string%3Aencodinginvalidcharacters%3A%29.json'
content_hash: 'sha256:1e51b2b6272bd777'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# init(string:encodingInvalidCharacters:)

<sub>Initializer</sub>

Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(string: String, encodingInvalidCharacters: Bool)
```

## Parameters

- `string` — The URL string to parse.

- `encodingInvalidCharacters` — A Boolean value that indicates whether the initializer attempts to encode any invalid characters in `string`.

## Discussion

If `encodingInvalidCharacters` is `true`, this initializer tries to encode the string to create a valid URL. If the URL string is still invalid after encoding, the initializer returns `nil`.

## See Also

### Creating URL components

- [init()](<init().md>) — Creates a URL components instance without defining any of the components.
- [init(string:)](<init(string_).md>) — Creates a URL components instance from a URL string.
- [init(url:resolvingAgainstBaseURL:)](<init(url_resolvingagainstbaseurl_).md>) — Creates a URL components instance from a URL string, optionally resolving against a base URL.
