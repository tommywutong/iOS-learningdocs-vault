---
title: 'firstObjectCommon(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/firstobjectcommon(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/firstobjectcommon(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/firstobjectcommon%28with%3A%29.json'
content_hash: 'sha256:aee59e2941978b7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# firstObjectCommon(with:)

<sub>Instance Method</sub>

Returns the first object contained in the receiving array that’s equal to an object in another given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstObjectCommon(with otherArray: [Any]) -> Any?
```

## Parameters

- `otherArray` — An array.

## Return Value

Returns the first object contained in the receiving array that’s equal to an object in `otherArray`. If no such object is found, returns `nil`.

## Discussion

This method uses [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) to check for object equality.

## See Also

### Related Documentation

- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the array.

### Comparing Arrays

- [- isEqualToArray:](<isequal(to_).md>) — Compares the receiving array to another array.
