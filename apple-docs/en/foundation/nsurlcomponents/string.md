---
title: string
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcomponents/string
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/string'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/string.json'
content_hash: 'sha256:030b8a2659aef099'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# string

<sub>Instance Property</sub>

A URL derived from the components object, in string form.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var string: String? { get }
```

## Discussion

If the receiver has an authority component (user, password, host, or port) and a path component, then the path must either begin with `"/"` or be an empty string. Otherwise, this property contains `nil`.

If the receiver  _does not_ have an authority component (user, password, host, or port) and has a path component, the path component must not start with `"//"`. If it does, this property contains `nil`.

This property can be used only to obtain a URL string based on the values of the other properties. To configure a components object based on an existing URL string, call either the [componentsWithString:](componentswithstring_.md) or [- initWithString:](<init(string_).md>) method.

## See Also

### Getting the URL

- [URL](url.md) — A URL object derived from the components object.
- [- URLRelativeToURL:](<url(relativeto_).md>) — Returns a URL object derived from the components object.
