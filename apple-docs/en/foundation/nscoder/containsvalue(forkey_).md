---
title: 'containsValue(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/containsvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/containsvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/containsvalue%28forkey%3A%29.json'
content_hash: 'sha256:4efbd694120ca209'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# containsValue(forKey:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether an encoded value is available for a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func containsValue(forKey key: String) -> Bool
```

## Discussion

Subclasses must override this method if they perform keyed coding.

The string is passed as `key`.

## See Also

### Inspecting a Coder

- [allowsKeyedCoding](allowskeyedcoding.md) — A Boolean value that indicates whether the receiver supports keyed coding of objects.
- [decodingFailurePolicy](decodingfailurepolicy-swift.property.md) — The action the coder should take when decoding fails.
- [DecodingFailurePolicy](decodingfailurepolicy-swift.enum.md) — Policies describing the action the coder should take when encountering decode failures.
