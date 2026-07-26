---
title: 'isSuperset(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscharacterset/issuperset(of:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/issuperset(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/issuperset%28of%3A%29.json'
content_hash: 'sha256:a450e0a89e719489'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# isSuperset(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is a superset of another given character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isSuperset(of theOtherSet: CharacterSet) -> Bool
```

## Parameters

- `theOtherSet` — A character set.

## Return Value

[true](../../swift/true.md) if the receiver is a superset of `theOtherSet`, otherwise [false](../../swift/false.md).

## See Also

### Testing Set Membership

- [- characterIsMember:](<characterismember(__).md>) — Returns a Boolean value that indicates whether a given character is in the receiver.
- [- hasMemberInPlane:](<hasmemberinplane(__).md>) — Returns a Boolean value that indicates whether the receiver has at least one member in a given character plane.
- [- longCharacterIsMember:](<longcharacterismember(__).md>) — Returns a Boolean value that indicates whether a given long character is a member of the receiver.
