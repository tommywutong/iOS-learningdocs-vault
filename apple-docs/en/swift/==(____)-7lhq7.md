---
title: '==(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/==(_:_:)-7lhq7'
source_url: 'https://developer.apple.com/documentation/swift/==(_:_:)-7lhq7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/%3D%3D%28_%3A_%3A%29-7lhq7.json'
content_hash: 'sha256:be43715e573368e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ==(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the corresponding components of two tuples are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func == <A, B, C, D>(lhs: (A, B, C, D), rhs: (A, B, C, D)) -> Bool where A : Equatable, B : Equatable, C : Equatable, D : Equatable
```

## Parameters

- `lhs` — A tuple of `Equatable` elements.

- `rhs` — Another tuple of elements of the same type as `lhs`.

## Discussion

For two tuples to compare as equal, each corresponding pair of components must be equal. The following example compares tuples made up of 4 components:

```swift
let a = ("a", 1, 2, 3)
let b = ("a", 1, 2, 3)
print(a == b)
// Prints "true"

let c = ("a", 1, 2, 4)
print(a == c)
// Prints "false"
```

## See Also

### Tuple Comparison

- [==(_:_:)](<==(____)-958in.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-2htbb.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-h88g.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-1hbor.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-1ud2a.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-9kf9y.md>) — Returns a Boolean value indicating whether two types are identical.
- [!=(_:_:)](<!=(____)-18co7.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-7er1l.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-754t2.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-7ao4l.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-4fzl6.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-3nrcc.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-1mxms.md>) — Returns a Boolean value indicating whether two types are not identical.
