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
doc_path: '/documentation/foundation/url/init(string:encodinginvalidcharacters:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(string:encodinginvalidcharacters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28string%3Aencodinginvalidcharacters%3A%29.json'
content_hash: 'sha256:d866d0742338bc42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(string:encodingInvalidCharacters:)

<sub>Initializer</sub>

Creates a URL instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(string: String, encodingInvalidCharacters: Bool)
```

## Parameters

- `string` — A URL location.

- `encodingInvalidCharacters` — A Boolean value that indicates whether the initializer attempts to encode any invalid characters in `string`.

## Discussion

If `encodingInvalidCharacters` is `true`, this initializer tries to encode the string to create a valid URL. If the URL string is still invalid after encoding, the initializer returns `nil`.

## See Also

### Creating a URL from a string

- [init(string:)](<init(string_).md>) — Creates a URL instance from the provided string.
- [init(string:relativeTo:)](<init(string_relativeto_).md>) — Creates a URL instance from the provided string, relative to another URL.
- [init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)](<init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_)-3ic6f.md>) — Creates a URL that refers to a location specified by resolving bookmark data.
- [init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)](<init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_)-97e6x.md>) — Initializes a URL that refers to a location specified by resolving bookmark data.
