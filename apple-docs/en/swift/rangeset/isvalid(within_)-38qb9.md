---
title: 'isValid(within:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/isvalid(within:)-38qb9'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/isvalid(within:)-38qb9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/isvalid%28within%3A%29-38qb9.json'
content_hash: 'sha256:6cb68321aa3fa6b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# isValid(within:)

<sub>Instance Method</sub>

Indicates whether the range set is valid for use with the provided discontiguous attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isValid(within text: DiscontiguousAttributedSubstring) -> Bool
```

## Parameters

- `text` — A discontiguous attributed string used to validate the range set.

## Return Value

`true` when the range set is valid for use with the provided discontiguous attributed string; otherwise, false. A range set is valid if each of its ranges are valid in the discontiguous attributed string.
