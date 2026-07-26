---
title: '==(_:_:)'
framework: Combine
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscribers/demand/==(_:_:)-4oy8i'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/demand/==(_:_:)-4oy8i'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/demand/%3D%3D%28_%3A_%3A%29-4oy8i.json'
content_hash: 'sha256:83d25bb271a9f39f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Demand](../demand.md)

# ==(_:_:)

<sub>Operator</sub>

Returns a Boolean value that indicates whether a given number of elements matches the request of a given demand.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func == (lhs: Int, rhs: Subscribers.Demand) -> Bool
```

## Discussion

An `.unlimited` demand doesn’t match any integer.

## See Also

### Comparing demands

- [==(_:_:)](<==(____)-7246z.md>) — Returns a Boolean value that indicates whether a demand requests the given number of elements.
- [!=(_:_:)](<!=(____)-3j2h8.md>) — Returns a Boolean value that indicates whether an integer is unequal to a demand.
- [!=(_:_:)](<!=(____)-2dj1p.md>) — Returns a Boolean value that indicates whether a demand isn’t equal to an integer.
- [\<(_:_:)](<_(____)-1wuod.md>) — Returns a Boolean that indicates a given number of elements is less than the maximum specified by the demand.
- [\<(_:_:)](<_(____)-ciby.md>) — Returns a Boolean that indicates whether the demand requests fewer than the given number of elements.
- [\<(_:_:)](<_(____)-8nf1g.md>) — Returns a Boolean that indicates whether the first demand requests fewer elements than the second.
- [\<=(_:_:)](<_=(____)-5f62z.md>) — Returns a Boolean value that indicates a given number of elements is less than or equal the maximum specified by the demand.
- [\<=(_:_:)](<_=(____)-2otvi.md>) — Returns a Boolean that indicates whether the demand requests fewer or the same number of elements as the given integer.
- [\<=(_:_:)](<_=(____)-9cywv.md>) — Returns a Boolean value that indicates whether the first demand requests fewer or the same number of elements as the second.
- [\>(_:_:)](<_(____)-35p6f.md>) — Returns a Boolean that indicates a given number of elements is greater than the maximum specified by the demand.
- [\>(_:_:)](<_(____)-4k1xp.md>) — Returns a Boolean that indicates whether the demand requests more than the given number of elements.
- [\>(_:_:)](<_(____)-74yle.md>) — Returns a Boolean that indicates whether the first demand requests more elements than the second.
- [\>=(_:_:)](<_=(____)-6lv9s.md>) — Returns a Boolean that indicates a given number of elements is greater than or equal to the maximum specified by the demand.
- [\>=(_:_:)](<_=(____)-28c1e.md>) — Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.
- [\>=(_:_:)](<_=(____)-5xnt.md>) — Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.
