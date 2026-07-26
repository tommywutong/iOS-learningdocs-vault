---
title: 'scannerWithString:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscanner/scannerwithstring:'
source_url: 'https://developer.apple.com/documentation/foundation/nsscanner/scannerwithstring:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscanner/scannerwithstring%3A.json'
content_hash: 'sha256:049a46179fbbe9da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# scannerWithString:

<sub>Type Method</sub>

Returns an `NSScanner` object that scans a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) scannerWithString:(NSString *) string;
```

## Parameters

- `string` — The string to scan.

## Return Value

An `NSScanner` object that scans `aString`.

## Discussion

Sets the string to scan by invoking [- initWithString:](<../scanner/init(string_).md>) with `aString`.

## See Also

### Related Documentation

- [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i)

### Creating a Scanner

- [+ localizedScannerWithString:](<../scanner/localizedscanner(with_).md>) — Returns an `NSScanner` object that scans a given string according to the user’s default locale.
- [- initWithString:](<../scanner/init(string_).md>) — Returns an `NSScanner` object initialized to scan a given string.
