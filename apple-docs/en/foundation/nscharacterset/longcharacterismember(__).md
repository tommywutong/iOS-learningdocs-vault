---
title: 'longCharacterIsMember(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscharacterset/longcharacterismember(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/longcharacterismember(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/longcharacterismember%28_%3A%29.json'
content_hash: 'sha256:21d0e4d79b389eb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# longCharacterIsMember(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a given long character is a member of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func longCharacterIsMember(_ theLongChar: UTF32Char) -> Bool
```

## Parameters

- `theLongChar` — A UTF32 character.

## Return Value

[true](../../swift/true.md) if `theLongChar` is in the receiver, otherwise [false](../../swift/false.md).

## Discussion

This method supports the specification of 32-bit characters.

## See Also

### Testing Set Membership

- [- characterIsMember:](<characterismember(__).md>) — Returns a Boolean value that indicates whether a given character is in the receiver.
- [- hasMemberInPlane:](<hasmemberinplane(__).md>) — Returns a Boolean value that indicates whether the receiver has at least one member in a given character plane.
- [- isSupersetOfSet:](<issuperset(of_).md>) — Returns a Boolean value that indicates whether the receiver is a superset of another given character set.
