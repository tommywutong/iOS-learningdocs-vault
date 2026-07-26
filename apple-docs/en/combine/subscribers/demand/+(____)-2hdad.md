---
title: '+(_:_:)'
framework: Combine
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscribers/demand/+(_:_:)-2hdad'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/demand/+(_:_:)-2hdad'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/demand/%2B%28_%3A_%3A%29-2hdad.json'
content_hash: 'sha256:ae8bb11fa1fbc714'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Demand](../demand.md)

# +(_:_:)

<sub>Operator</sub>

Returns the result of adding two demands. When adding any value to `.unlimited`, the result is `.unlimited`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func + (lhs: Subscribers.Demand, rhs: Subscribers.Demand) -> Subscribers.Demand
```

## See Also

### Performing mathematical operations

- [*(_:_:)](<_(____).md>) — Returns the result of multiplying a demand by an integer.
- [*=(_:_:)](<_=(____).md>) — Multiplies a demand by an integer, and assigns the result to the demand.
- [+(_:_:)](<+(____)-902we.md>) — Returns the result of adding an integer to a demand.
- [+=(_:_:)](<+=(____)-20lis.md>) — Adds two demands, and assigns the result to the first demand.
- [+=(_:_:)](<+=(____)-3k1hv.md>) — Adds an integer to a demand, and assigns the result to the demand.
- [-(_:_:)](<-(____)-1r0gm.md>) — Returns the result of subtracting one demand from another.
- [-(_:_:)](<-(____)-6mw4s.md>) — Returns the result of subtracting an integer from a demand.
- [-=(_:_:)](<-=(____)-1d0m9.md>) — Subtracts one demand from another, and assigns the result to the first demand.
- [-=(_:_:)](<-=(____)-9pwnc.md>) — Subtracts an integer from a demand, and assigns the result to the demand.
