---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcomponents/init()
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/init%28%29.json'
content_hash: 'sha256:99a050e48202f099'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# init()

<sub>Initializer</sub>

Creates a URL components object with all components left undefined.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Return Value

Returns the initialized URL components object, or `nil` if an error occurs.

## See Also

### Creating URL components

- [- initWithString:](<init(string_).md>) — Creates a URL components object by parsing a URL in string form.
- [- initWithString:encodingInvalidCharacters:](<init(string_encodinginvalidcharacters_).md>) — Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [- initWithURL:resolvingAgainstBaseURL:](<init(url_resolvingagainstbaseurl_)-3bbte.md>) — Creates a URL components object by parsing the URL from an `NSURL` object.
