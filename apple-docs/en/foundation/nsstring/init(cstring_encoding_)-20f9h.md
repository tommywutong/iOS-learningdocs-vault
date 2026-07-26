---
title: 'init(cString:encoding:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/init(cstring:encoding:)-20f9h'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(cstring:encoding:)-20f9h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28cstring%3Aencoding%3A%29-20f9h.json'
content_hash: 'sha256:9f3bb095e7093b7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(cString:encoding:)

<sub>Initializer</sub>

Returns an @c NSString object initialized using the characters in a given C array, interpreted according to a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(cString nullTerminatedCString: UnsafePointer<CChar>, encoding: UInt)
```

## Parameters

- `nullTerminatedCString` — A C array of characters. The array must end with a @c NULL character; intermediate @c NULL characters are not allowed.

- `encoding` — The encoding of @c nullTerminatedCString.

## Return Value

An @c NSString object initialized using the characters from @c nullTerminatedCString. The returned object may be different from the original receiver.
