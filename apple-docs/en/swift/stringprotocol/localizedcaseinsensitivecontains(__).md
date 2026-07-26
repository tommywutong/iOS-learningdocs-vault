---
title: 'localizedCaseInsensitiveContains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/localizedcaseinsensitivecontains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/localizedcaseinsensitivecontains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/localizedcaseinsensitivecontains%28_%3A%29.json'
content_hash: 'sha256:58e99ec2535b2821'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# localizedCaseInsensitiveContains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the given string is non-empty and contained within this string by case-insensitive, non-literal search, taking into account the current locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedCaseInsensitiveContains<T>(_ other: T) -> Bool where T : StringProtocol
```

## Discussion

Locale-independent case-insensitive operation, and other needs, can be achieved by calling `range(of:options:range:locale:)`.

Equivalent to:

```swift
range(of: other, options: .caseInsensitiveSearch,
      locale: Locale.current) != nil
```
