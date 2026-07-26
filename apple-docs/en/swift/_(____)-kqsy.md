---
title: '>(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/_(_:_:)-kqsy'
source_url: 'https://developer.apple.com/documentation/swift/_(_:_:)-kqsy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/_%28_%3A_%3A%29-kqsy.json'
content_hash: 'sha256:00e7dda31c5489d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# \>(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func > <A, B, C, D, E, F>(lhs: (A, B, C, D, E, F), rhs: (A, B, C, D, E, F)) -> Bool where A : Comparable, B : Comparable, C : Comparable, D : Comparable, E : Comparable, F : Comparable
```

## Parameters

- `lhs` — A tuple of `Comparable` elements.

- `rhs` — Another tuple of elements of the same type as `lhs`.

## Discussion

Given two tuples `(a1, a2, ..., aN)` and `(b1, b2, ..., bN)`, the first tuple is after the second tuple if and only if `a1 > b1` or (`a1 == b1` and `(a2, ..., aN) > (b2, ..., bN)`).

## See Also

### Tuple Comparison

- [\<(_:_:)](<_(____)-1b1cu.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<(_:_:)](<_(____)-4ck5h.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<(_:_:)](<_(____)-23151.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<(_:_:)](<_(____)-6p1tf.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<(_:_:)](<_(____)-3hhjy.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<(_:_:)](<_(____)-8mgtp.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-16p1e.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-3jpod.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-8u5uu.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-6kea2.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-1hzxz.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-7n746.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\>(_:_:)](<_(____)-yktb.md>) — Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [\>(_:_:)](<_(____)-4xg09.md>) — Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [\>(_:_:)](<_(____)-7p512.md>) — Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
