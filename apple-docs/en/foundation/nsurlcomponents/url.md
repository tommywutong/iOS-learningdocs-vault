---
title: url
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcomponents/url
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/url.json'
content_hash: 'sha256:e00e6e8b4db62909'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# url

<sub>Instance Property</sub>

A URL object derived from the components object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var url: URL? { get }
```

## Discussion

If the receiver has an authority component (user, password, host, or port) and a path component, then the path must either begin with `"/"` or be an empty string. Otherwise, this property contains `nil`.

If the receiver _does not_ have an authority component (user, password, host, or port) and has a path component, the path component must not start with `"//"`. If it does, this property contains `nil`.

If the receiver has `nil` values for all component properties, such as when initializing with [- init](<init().md>), this property returns an `NSURL` object with an empty string, because a URL always has a path—even if it’s an empty string.

This property can be used only to obtain a URL based on the values of the other properties. To configure a components object based on an existing URL, call either the [componentsWithURL:resolvingAgainstBaseURL:](componentswithurl_resolvingagainstbaseurl_.md) or [- initWithURL:resolvingAgainstBaseURL:](<init(url_resolvingagainstbaseurl_)-3bbte.md>) method.

## See Also

### Getting the URL

- [string](string.md) — A URL derived from the components object, in string form.
- [- URLRelativeToURL:](<url(relativeto_).md>) — Returns a URL object derived from the components object.
