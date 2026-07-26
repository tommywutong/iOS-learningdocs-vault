---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/isequal%28to%3A%29.json'
content_hash: 'sha256:f89c4ea2d2bc762e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the contents of the receiving dictionary are equal to the contents of another given dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to otherDictionary: [AnyHashable : Any]) -> Bool
```

## Parameters

- `otherDictionary` — The dictionary with which to compare the receiving dictionary.

## Return Value

[true](../../swift/true.md) if the contents of `otherDictionary` are equal to the contents of the receiving dictionary, otherwise [false](../../swift/false.md).

## Discussion

Two dictionaries have equal contents if they each hold the same number of entries and, for a given key, the corresponding value objects in each dictionary satisfy the [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) test.

## See Also

### Related Documentation

- [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) — Returns a Boolean value that indicates whether the receiver and a given object are equal.
