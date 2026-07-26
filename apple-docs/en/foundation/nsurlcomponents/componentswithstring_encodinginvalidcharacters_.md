---
title: 'componentsWithString:encodingInvalidCharacters:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlcomponents/componentswithstring:encodinginvalidcharacters:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/componentswithstring:encodinginvalidcharacters:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/componentswithstring%3Aencodinginvalidcharacters%3A.json'
content_hash: 'sha256:38403dfa0e18a62d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# componentsWithString:encodingInvalidCharacters:

<sub>Type Method</sub>

Returns a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) componentsWithString:(NSString *) URLString encodingInvalidCharacters:(BOOL) encodingInvalidCharacters;
```

## Parameters

- `URLString` — The URL string to parse.

- `encodingInvalidCharacters` — A Boolean value that indicates whether the initializer attempts to encode any invalid characters in `URLString`.

## Return Value

A URL components instance from the provided string, optionally with invalid characters percent-encoded.

## Discussion

If `encodingInvalidCharacters` is `true`, this initializer tries to encode the string to create a valid URL. If the URL string is still invalid after encoding, the method returns `nil`.

## See Also

### Creating URL components

- [componentsWithString:](componentswithstring_.md) — Returns a URL components object by parsing a URL in string form.
- [componentsWithURL:resolvingAgainstBaseURL:](componentswithurl_resolvingagainstbaseurl_.md) — Returns a URL components object by parsing the URL from an `NSURL` object.
- [- init](<init().md>) — Creates a URL components object with all components left undefined.
- [- initWithString:](<init(string_).md>) — Creates a URL components object by parsing a URL in string form.
- [- initWithString:encodingInvalidCharacters:](<init(string_encodinginvalidcharacters_).md>) — Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [- initWithURL:resolvingAgainstBaseURL:](<init(url_resolvingagainstbaseurl_)-3bbte.md>) — Creates a URL components object by parsing the URL from an `NSURL` object.
