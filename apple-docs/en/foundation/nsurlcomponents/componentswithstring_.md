---
title: 'componentsWithString:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlcomponents/componentswithstring:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/componentswithstring:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/componentswithstring%3A.json'
content_hash: 'sha256:45596000e7dab733'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# componentsWithString:

<sub>Type Method</sub>

Returns a URL components object by parsing a URL in string form.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) componentsWithString:(NSString *) URLString;
```

## Parameters

- `URLString` — The URL string to parse.

## Return Value

Returns the new URL components object, or `nil` if the URL string could not be parsed.

## See Also

### Creating URL components

- [componentsWithString:encodingInvalidCharacters:](componentswithstring_encodinginvalidcharacters_.md) — Returns a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [componentsWithURL:resolvingAgainstBaseURL:](componentswithurl_resolvingagainstbaseurl_.md) — Returns a URL components object by parsing the URL from an `NSURL` object.
- [- init](<init().md>) — Creates a URL components object with all components left undefined.
- [- initWithString:](<init(string_).md>) — Creates a URL components object by parsing a URL in string form.
- [- initWithString:encodingInvalidCharacters:](<init(string_encodinginvalidcharacters_).md>) — Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [- initWithURL:resolvingAgainstBaseURL:](<init(url_resolvingagainstbaseurl_)-3bbte.md>) — Creates a URL components object by parsing the URL from an `NSURL` object.
