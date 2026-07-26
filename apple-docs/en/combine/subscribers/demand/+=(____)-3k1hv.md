---
title: '+=(_:_:)'
framework: Combine
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscribers/demand/+=(_:_:)-3k1hv'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/demand/+=(_:_:)-3k1hv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/demand/%2B%3D%28_%3A_%3A%29-3k1hv.json'
content_hash: 'sha256:44d82c986ab1b573'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Demand](../demand.md)

# +=(_:_:)

<sub>Operator</sub>

Adds an integer to a demand, and assigns the result to the demand.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func += (lhs: inout Subscribers.Demand, rhs: Int)
```

## Discussion

When adding any value to `.unlimited`, the result is `.unlimited`.

## See Also

### Performing mathematical operations

- [*(_:_:)](<_(____).md>) — Returns the result of multiplying a demand by an integer.
- [*=(_:_:)](<_=(____).md>) — Multiplies a demand by an integer, and assigns the result to the demand.
- [+(_:_:)](<+(____)-2hdad.md>) — Returns the result of adding two demands. When adding any value to `.unlimited`, the result is `.unlimited`.
- [+(_:_:)](<+(____)-902we.md>) — Returns the result of adding an integer to a demand.
- [+=(_:_:)](<+=(____)-20lis.md>) — Adds two demands, and assigns the result to the first demand.
- [-(_:_:)](<-(____)-1r0gm.md>) — Returns the result of subtracting one demand from another.
- [-(_:_:)](<-(____)-6mw4s.md>) — Returns the result of subtracting an integer from a demand.
- [-=(_:_:)](<-=(____)-1d0m9.md>) — Subtracts one demand from another, and assigns the result to the first demand.
- [-=(_:_:)](<-=(____)-9pwnc.md>) — Subtracts an integer from a demand, and assigns the result to the demand.
