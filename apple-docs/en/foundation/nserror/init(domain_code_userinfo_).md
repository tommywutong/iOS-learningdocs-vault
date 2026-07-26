---
title: 'init(domain:code:userInfo:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nserror/init(domain:code:userinfo:)'
source_url: 'https://developer.apple.com/documentation/foundation/nserror/init(domain:code:userinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/init%28domain%3Acode%3Auserinfo%3A%29.json'
content_hash: 'sha256:77ae432e3682ba27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# init(domain:code:userInfo:)

<sub>Initializer</sub>

Returns an `NSError` object initialized for a given domain and code with a given `userInfo` dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(domain: String, code: Int, userInfo dict: [String : Any]? = nil)
```

## Parameters

- `domain` — The error domain—this can be one of the predefined `NSError` domains, or an arbitrary string describing a custom domain. `domain` must not be `nil`. See `Error Domains` for a list of predefined domains.

- `code` — The error code for the error.

- `dict` — The `userInfo` dictionary for the error. `userInfo` may be `nil`.

## Return Value

An `NSError` object initialized for `domain` with the specified error `code` and the dictionary of arbitrary data `userInfo`.

## Discussion

This is the designated initializer for `NSError`.
