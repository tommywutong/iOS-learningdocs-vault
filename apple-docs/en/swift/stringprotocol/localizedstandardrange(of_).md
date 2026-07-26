---
title: 'localizedStandardRange(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/localizedstandardrange(of:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/localizedstandardrange(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/localizedstandardrange%28of%3A%29.json'
content_hash: 'sha256:a0d74e92b9261d49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# localizedStandardRange(of:)

<sub>Instance Method</sub>

Finds and returns the range of the first occurrence of a given string, taking the current locale into account.  Returns `nil` if the string was not found.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedStandardRange<T>(of string: T) -> Range<Self.Index>? where T : StringProtocol
```

## Discussion

This is the most appropriate method for doing user-level string searches, similar to how searches are done generally in the system.  The search is locale-aware, case and diacritic insensitive.  The exact list of search options applied may change over time.
