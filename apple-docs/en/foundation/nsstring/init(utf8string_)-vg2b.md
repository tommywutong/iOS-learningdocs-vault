---
title: 'init(utf8String:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/init(utf8string:)-vg2b'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(utf8string:)-vg2b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28utf8string%3A%29-vg2b.json'
content_hash: 'sha256:d8276615aa1ab4b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(utf8String:)

<sub>Initializer</sub>

Returns an @c NSString object initialized by copying the characters from a given C array of UTF8-encoded bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(utf8String nullTerminatedCString: UnsafePointer<CChar>)
```

## Parameters

- `nullTerminatedCString` — A @c NULL-terminated C array of bytes in UTF-8 encoding. This value must not be @c NULL.

## Return Value

An @c NSString object initialized by copying the bytes from @c nullTerminatedCString. The returned object may be different from the original receiver.
