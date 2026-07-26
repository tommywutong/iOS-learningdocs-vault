---
title: 'init(string:encodingInvalidCharacters:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlcomponents/init(string:encodinginvalidcharacters:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/init(string:encodinginvalidcharacters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/init%28string%3Aencodinginvalidcharacters%3A%29.json'
content_hash: 'sha256:5fb2ebf937da7b71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# init(string:encodingInvalidCharacters:)

<sub>Initializer</sub>

Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(string URLString: String, encodingInvalidCharacters: Bool)
```

## Parameters

- `URLString` — The URL string to parse.

- `encodingInvalidCharacters` — A Boolean value that indicates whether the initializer attempts to encode any invalid characters in `URLString`.

## Discussion

If `encodingInvalidCharacters` is `true`, this initializer tries to encode the string to create a valid URL. If the URL string is still invalid after encoding, the initializer returns `nil`.

## See Also

### Creating URL components

- [- init](<init().md>) — Creates a URL components object with all components left undefined.
- [- initWithString:](<init(string_).md>) — Creates a URL components object by parsing a URL in string form.
- [- initWithURL:resolvingAgainstBaseURL:](<init(url_resolvingagainstbaseurl_)-3bbte.md>) — Creates a URL components object by parsing the URL from an `NSURL` object.
