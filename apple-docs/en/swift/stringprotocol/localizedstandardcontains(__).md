---
title: 'localizedStandardContains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/localizedstandardcontains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/localizedstandardcontains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/localizedstandardcontains%28_%3A%29.json'
content_hash: 'sha256:f81f72de87dbd388'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# localizedStandardContains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the string contains the given string, taking the current locale into account.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedStandardContains<T>(_ string: T) -> Bool where T : StringProtocol
```

## Discussion

This is the most appropriate method for doing user-level string searches, similar to how searches are done generally in the system.  The search is locale-aware, case and diacritic insensitive.  The exact list of search options applied may change over time.
