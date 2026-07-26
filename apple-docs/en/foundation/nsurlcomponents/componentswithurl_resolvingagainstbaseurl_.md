---
title: 'componentsWithURL:resolvingAgainstBaseURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlcomponents/componentswithurl:resolvingagainstbaseurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/componentswithurl:resolvingagainstbaseurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/componentswithurl%3Aresolvingagainstbaseurl%3A.json'
content_hash: 'sha256:ec54ac19102df946'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# componentsWithURL:resolvingAgainstBaseURL:

<sub>Type Method</sub>

Returns a URL components object by parsing the URL from an `NSURL` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) componentsWithURL:(NSURL *) url resolvingAgainstBaseURL:(BOOL) resolve;
```

## Parameters

- `url` — The URL to parse.

- `resolve` — Controls whether the URL should be resolved against its base URL before parsing. If [true](../../swift/true.md), and if the `url` parameter contains a relative URL, the original URL is resolved against its base URL before parsing by calling the [absoluteURL](../nsurl/absoluteurl.md) method. Otherwise, the string portion is used by itself.

## Return Value

Returns the new URL components object, or `nil` if the URL could not be parsed.

## See Also

### Creating URL components

- [componentsWithString:](componentswithstring_.md) — Returns a URL components object by parsing a URL in string form.
- [componentsWithString:encodingInvalidCharacters:](componentswithstring_encodinginvalidcharacters_.md) — Returns a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [- init](<init().md>) — Creates a URL components object with all components left undefined.
- [- initWithString:](<init(string_).md>) — Creates a URL components object by parsing a URL in string form.
- [- initWithString:encodingInvalidCharacters:](<init(string_encodinginvalidcharacters_).md>) — Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [- initWithURL:resolvingAgainstBaseURL:](<init(url_resolvingagainstbaseurl_)-3bbte.md>) — Creates a URL components object by parsing the URL from an `NSURL` object.
