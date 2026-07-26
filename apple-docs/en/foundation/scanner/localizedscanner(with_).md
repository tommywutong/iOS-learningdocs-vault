---
title: 'localizedScanner(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/scanner/localizedscanner(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/scanner/localizedscanner(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/localizedscanner%28with%3A%29.json'
content_hash: 'sha256:222215d44fbb78f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# localizedScanner(with:)

<sub>Type Method</sub>

Returns an `NSScanner` object that scans a given string according to the user’s default locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localizedScanner(with string: String) -> Any
```

## Parameters

- `string` — The string to scan.

## Return Value

An `NSScanner` object that scans `aString` according to the user’s default locale.

## Discussion

Sets the string to scan by invoking [- initWithString:](<init(string_).md>) with `aString`. The locale is set with [Scanner](../scanner.md).

## See Also

### Creating a Scanner

- [- initWithString:](<init(string_).md>) — Returns an `NSScanner` object initialized to scan a given string.
