---
title: 'init(string:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/init(string:)-7xgq7'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/init(string:)-7xgq7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/init%28string%3A%29-7xgq7.json'
content_hash: 'sha256:74b10361ac69160d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# init(string:)

<sub>Initializer</sub>

Returns an `NSString` object initialized by copying the characters from another given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc convenience init(string aString: NSString)
```

## Return Value

An `NSString` object initialized by copying the characters from `aString`. The returned object may be different from the original receiver.
