---
title: 'commonPrefix(with:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/commonprefix(with:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/commonprefix(with:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/commonprefix%28with%3Aoptions%3A%29.json'
content_hash: 'sha256:5701f3c5a8750055'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# commonPrefix(with:options:)

<sub>Instance Method</sub>

Returns a string containing characters the receiver and a given string have in common, starting from the beginning of each up to the first characters that aren’t equivalent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func commonPrefix(with str: String, options mask: NSString.CompareOptions = []) -> String
```

## Parameters

- `str` — The string with which to compare the receiver.

- `mask` — Options for the comparison. The following search options may be specified by combining them with the C bitwise `OR` operator: `NSCaseInsensitiveSearch`, `NSLiteralSearch`. See [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i) for details on these options.

## Return Value

A string containing characters the receiver and `aString` have in common, starting from the beginning of each up to the first characters that aren’t equivalent.

## Discussion

The returned string is based on the characters of the receiver. For example, if the receiver is “Ma¨dchen” and `aString` is “Mädchenschule”, the string returned is “Ma¨dchen”, not “Mädchen”.

## See Also

### Related Documentation

- [- hasPrefix:](<hasprefix(__).md>) — Returns a Boolean value that indicates whether a given string matches the beginning characters of the receiver.
