---
title: 'hasMemberInPlane(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscharacterset/hasmemberinplane(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/hasmemberinplane(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/hasmemberinplane%28_%3A%29.json'
content_hash: 'sha256:c13ce2fd9de2091b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# hasMemberInPlane(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver has at least one member in a given character plane.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hasMemberInPlane(_ thePlane: UInt8) -> Bool
```

## Parameters

- `thePlane` — A character plane.

## Return Value

[true](../../swift/true.md) if the receiver has at least one member in `thePlane`, otherwise [false](../../swift/false.md).

## Discussion

This method makes it easier to find the plane containing the members of the current character set. The Basic Multilingual Plane (BMP) is plane `0`.

## See Also

### Testing Set Membership

- [- characterIsMember:](<characterismember(__).md>) — Returns a Boolean value that indicates whether a given character is in the receiver.
- [- isSupersetOfSet:](<issuperset(of_).md>) — Returns a Boolean value that indicates whether the receiver is a superset of another given character set.
- [- longCharacterIsMember:](<longcharacterismember(__).md>) — Returns a Boolean value that indicates whether a given long character is a member of the receiver.
