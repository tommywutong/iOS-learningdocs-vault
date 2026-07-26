---
title: 'subdivision(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/subdivision-swift.struct/subdivision(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/subdivision-swift.struct/subdivision(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/subdivision-swift.struct/subdivision%28for%3A%29.json'
content_hash: 'sha256:45371fc5b89e69fc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Subdivision](../subdivision-swift.struct.md)

# subdivision(for:)

<sub>Type Method</sub>

Returns the subdivision representing the given region as a whole.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func subdivision(for region: Locale.Region) -> Locale.Subdivision
```

## Parameters

- `region` — A region to represent as a subdivision.

## Return Value

A subdivision that represents the entire region.

## Discussion

For example, this method returns a subdivision with the `uszzzz` identifier for the entire US region.

## See Also

### Creating a subdivision

- [init(_:)](<init(__).md>) — Creates a sudivision from a Unicode identifier.
- [init(stringLiteral:)](<init(stringliteral_).md>) — Creates a sudivision from a Unicode identifier as a string literal.
