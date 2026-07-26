---
title: 'init(url:resolvingAgainstBaseURL:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlcomponents/init(url:resolvingagainstbaseurl:)-3bbte'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/init(url:resolvingagainstbaseurl:)-3bbte'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/init%28url%3Aresolvingagainstbaseurl%3A%29-3bbte.json'
content_hash: 'sha256:49f64b004e73b8c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# init(url:resolvingAgainstBaseURL:)

<sub>Initializer</sub>

Creates a URL components object by parsing the URL from an `NSURL` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(url: URL, resolvingAgainstBaseURL resolve: Bool)
```

## Parameters

- `url` — The URL to parse.

- `resolve` — Controls whether the URL should be resolved against its base URL before parsing. If [true](../../swift/true.md), and if the `url` parameter contains a relative URL, the original URL is resolved against its base URL before parsing by calling the [absoluteURL](../nsurl/absoluteurl.md) method. Otherwise, the string portion is used by itself.

## Return Value

Returns the initialized URL components object, or `nil` if the URL could not be parsed.

## See Also

### Creating URL components

- [- init](<init().md>) — Creates a URL components object with all components left undefined.
- [- initWithString:](<init(string_).md>) — Creates a URL components object by parsing a URL in string form.
- [- initWithString:encodingInvalidCharacters:](<init(string_encodinginvalidcharacters_).md>) — Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
