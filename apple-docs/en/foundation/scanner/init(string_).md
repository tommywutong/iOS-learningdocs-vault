---
title: 'init(string:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/scanner/init(string:)'
source_url: 'https://developer.apple.com/documentation/foundation/scanner/init(string:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/init%28string%3A%29.json'
content_hash: 'sha256:065a0eeccd94da6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# init(string:)

<sub>Initializer</sub>

Returns an `NSScanner` object initialized to scan a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(string: String)
```

## Parameters

- `string` — The string to scan.

## Return Value

An `NSScanner` object initialized to scan `aString` from the beginning. The returned object might be different than the original receiver.

## See Also

### Creating a Scanner

- [+ localizedScannerWithString:](<localizedscanner(with_).md>) — Returns an `NSScanner` object that scans a given string according to the user’s default locale.
