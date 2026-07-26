---
title: Subscribers.Demand
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscribers/demand
source_url: 'https://developer.apple.com/documentation/combine/subscribers/demand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/demand.json'
content_hash: 'sha256:bca516ba6971e02b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscribers](../subscribers.md)

# Subscribers.Demand

<sub>Structure</sub>

A requested number of items, sent to a publisher from a subscriber through the subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Demand
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Comparable](../../swift/comparable.md), [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a demand instance

- [max(_:)](<demand/max(__).md>) — Creates a demand for the given maximum number of elements.

### Using special demands

- [unlimited](demand/unlimited.md) — A request for as many values as the publisher can produce.
- [none](demand/none.md) — A request for no elements from the publisher.

### Inspecing demand properties

- [max](demand/max.md) — The number of requested values.

### Encoding and decoding

- [encode(to:)](<demand/encode(to_).md>) — Encodes the demand to the provide encoder.
- [init(from:)](<demand/init(from_).md>) — Creates a demand instance from a decoder.

### Performing mathematical operations

- [*(_:_:)](<demand/_(____).md>) — Returns the result of multiplying a demand by an integer.
- [*=(_:_:)](<demand/_=(____).md>) — Multiplies a demand by an integer, and assigns the result to the demand.
- [+(_:_:)](<demand/+(____)-2hdad.md>) — Returns the result of adding two demands. When adding any value to `.unlimited`, the result is `.unlimited`.
- [+(_:_:)](<demand/+(____)-902we.md>) — Returns the result of adding an integer to a demand.
- [+=(_:_:)](<demand/+=(____)-20lis.md>) — Adds two demands, and assigns the result to the first demand.
- [+=(_:_:)](<demand/+=(____)-3k1hv.md>) — Adds an integer to a demand, and assigns the result to the demand.
- [-(_:_:)](<demand/-(____)-1r0gm.md>) — Returns the result of subtracting one demand from another.
- [-(_:_:)](<demand/-(____)-6mw4s.md>) — Returns the result of subtracting an integer from a demand.
- [-=(_:_:)](<demand/-=(____)-1d0m9.md>) — Subtracts one demand from another, and assigns the result to the first demand.
- [-=(_:_:)](<demand/-=(____)-9pwnc.md>) — Subtracts an integer from a demand, and assigns the result to the demand.

### Comparing demands

- [==(_:_:)](<demand/==(____)-4oy8i.md>) — Returns a Boolean value that indicates whether a given number of elements matches the request of a given demand.
- [==(_:_:)](<demand/==(____)-7246z.md>) — Returns a Boolean value that indicates whether a demand requests the given number of elements.
- [!=(_:_:)](<demand/!=(____)-3j2h8.md>) — Returns a Boolean value that indicates whether an integer is unequal to a demand.
- [!=(_:_:)](<demand/!=(____)-2dj1p.md>) — Returns a Boolean value that indicates whether a demand isn’t equal to an integer.
- [\<(_:_:)](<demand/_(____)-1wuod.md>) — Returns a Boolean that indicates a given number of elements is less than the maximum specified by the demand.
- [\<(_:_:)](<demand/_(____)-ciby.md>) — Returns a Boolean that indicates whether the demand requests fewer than the given number of elements.
- [\<(_:_:)](<demand/_(____)-8nf1g.md>) — Returns a Boolean that indicates whether the first demand requests fewer elements than the second.
- [\<=(_:_:)](<demand/_=(____)-5f62z.md>) — Returns a Boolean value that indicates a given number of elements is less than or equal the maximum specified by the demand.
- [\<=(_:_:)](<demand/_=(____)-2otvi.md>) — Returns a Boolean that indicates whether the demand requests fewer or the same number of elements as the given integer.
- [\<=(_:_:)](<demand/_=(____)-9cywv.md>) — Returns a Boolean value that indicates whether the first demand requests fewer or the same number of elements as the second.
- [\>(_:_:)](<demand/_(____)-35p6f.md>) — Returns a Boolean that indicates a given number of elements is greater than the maximum specified by the demand.
- [\>(_:_:)](<demand/_(____)-4k1xp.md>) — Returns a Boolean that indicates whether the demand requests more than the given number of elements.
- [\>(_:_:)](<demand/_(____)-74yle.md>) — Returns a Boolean that indicates whether the first demand requests more elements than the second.
- [\>=(_:_:)](<demand/_=(____)-6lv9s.md>) — Returns a Boolean that indicates a given number of elements is greater than or equal to the maximum specified by the demand.
- [\>=(_:_:)](<demand/_=(____)-28c1e.md>) — Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.
- [\>=(_:_:)](<demand/_=(____)-5xnt.md>) — Returns a Boolean that indicates whether the first demand requests more or the same number of elements as the second.
