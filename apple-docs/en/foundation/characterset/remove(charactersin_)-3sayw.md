---
title: 'remove(charactersIn:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/characterset/remove(charactersin:)-3sayw'
source_url: 'https://developer.apple.com/documentation/foundation/characterset/remove(charactersin:)-3sayw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/characterset/remove%28charactersin%3A%29-3sayw.json'
content_hash: 'sha256:9816280c137b9caa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CharacterSet](../characterset.md)

# remove(charactersIn:)

<sub>Instance Method</sub>

Remove the values from the specified string from the `CharacterSet`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func remove(charactersIn string: String)
```

## See Also

### Combining Character Sets

- [formIntersection(_:)](<formintersection(__).md>) — Sets the value to an intersection of the `CharacterSet` with another `CharacterSet`.
- [formSymmetricDifference(_:)](<formsymmetricdifference(__).md>) — Sets the value to an exclusive or of the `CharacterSet` with another `CharacterSet`.
- [formUnion(_:)](<formunion(__).md>) — Sets the value to a union of the `CharacterSet` with another `CharacterSet`.
- [hasMember(inPlane:)](<hasmember(inplane_).md>) — Returns true if the `CharacterSet` has a member in the specified plane.
- [insert(charactersIn:)](<insert(charactersin_)-2syuj.md>) — Insert the values from the specified string into the `CharacterSet`.
- [intersection(_:)](<intersection(__).md>) — Returns an intersection of the `CharacterSet` with another `CharacterSet`.
- [invert()](<invert().md>) — Invert the contents of the `CharacterSet`.
- [isSuperset(of:)](<issuperset(of_).md>) — Returns true if `self` is a superset of `other`.
- [subtracting(_:)](<subtracting(__).md>) — Returns a `CharacterSet` created by removing elements in `other` from `self`.
- [symmetricDifference(_:)](<symmetricdifference(__).md>) — Returns an exclusive or of the `CharacterSet` with another `CharacterSet`.
- [union(_:)](<union(__).md>) — Returns a union of the `CharacterSet` with another `CharacterSet`.
