---
title: 'url(relativeTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlcomponents/url(relativeto:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/url(relativeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/url%28relativeto%3A%29.json'
content_hash: 'sha256:91b1646f27e35953'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# url(relativeTo:)

<sub>Instance Method</sub>

Returns a URL object derived from the components object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func url(relativeTo baseURL: URL?) -> URL?
```

## Parameters

- `baseURL` — If non-`nil`, this URL is used as the base URL portion of the resulting URL object.

## Discussion

If the components object has an authority component (user, password, host, or port) and a path component, then the path must either begin with `"/"` or be an empty string. Otherwise, this property contains `nil`.

If the `NSURLComponents`_does not_ have an authority component (user, password, host, or port) and has a path component, the path component must not start with `"//"`. If it does, this property contains `nil`.

To configure a components object based on an existing URL, call either the [componentsWithURL:resolvingAgainstBaseURL:](componentswithurl_resolvingagainstbaseurl_.md) or [- initWithURL:resolvingAgainstBaseURL:](<init(url_resolvingagainstbaseurl_)-3bbte.md>) method.

## See Also

### Getting the URL

- [string](string.md) — A URL derived from the components object, in string form.
- [URL](url.md) — A URL object derived from the components object.
