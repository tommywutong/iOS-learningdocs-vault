---
title: 'init(url:resolvingAgainstBaseURL:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcomponents/init(url:resolvingagainstbaseurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/init(url:resolvingagainstbaseurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/init%28url%3Aresolvingagainstbaseurl%3A%29.json'
content_hash: 'sha256:96abd47803047960'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# init(url:resolvingAgainstBaseURL:)

<sub>Initializer</sub>

Creates a URL components instance from a URL string, optionally resolving against a base URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(url: URL, resolvingAgainstBaseURL resolve: Bool)
```

## Parameters

- `url` — The URL string to parse.

- `resolve` — Controls whether the initializer resolves the URL against its base URL before parsing. If `url` is a relative URL, setting `resolve` to `true` creates components using the [absoluteURL](../url/absoluteurl.md) property.

## See Also

### Creating URL components

- [init()](<init().md>) — Creates a URL components instance without defining any of the components.
- [init(string:)](<init(string_).md>) — Creates a URL components instance from a URL string.
- [init(string:encodingInvalidCharacters:)](<init(string_encodinginvalidcharacters_).md>) — Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
