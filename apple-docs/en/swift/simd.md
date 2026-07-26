---
title: SIMD
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/simd
source_url: 'https://developer.apple.com/documentation/swift/simd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd.json'
content_hash: 'sha256:d967a85fa2925932'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# SIMD

<sub>Protocol</sub>

A SIMD vector of a fixed number of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SIMD<Scalar> : CustomStringConvertible, Decodable, Encodable, ExpressibleByArrayLiteral, Hashable, SIMDStorage
```

## Relationships

- **Inherits From**: [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md), [Hashable](hashable.md), [SIMDStorage](simdstorage.md)

- **Conforming Types**: [SIMD16](simd16.md), [SIMD2](simd2.md), [SIMD3](simd3.md), [SIMD32](simd32.md), [SIMD4](simd4.md), [SIMD64](simd64.md), [SIMD8](simd8.md), [SIMDMask](simdmask.md)

## Topics

### Operators

- [&(_:_:)](<simd/&(____)-7euv2.md>)
- [&(_:_:)](<simd/&(____)-9iwe1.md>)
- [&(_:_:)](<simd/&(____)-hube.md>)
- [&*(_:_:)](<simd/&_(____)-6dnx3.md>)
- [&*(_:_:)](<simd/&_(____)-6q9r4.md>)
- [&*(_:_:)](<simd/&_(____)-96x3e.md>)
- [&*=(_:_:)](<simd/&_=(____)-2nncu.md>)
- [&*=(_:_:)](<simd/&_=(____)-7upvw.md>)
- [&+(_:_:)](<simd/&+(____)-11ezq.md>)
- [&+(_:_:)](<simd/&+(____)-2dwe6.md>)
- [&+(_:_:)](<simd/&+(____)-7atvo.md>)
- [&+=(_:_:)](<simd/&+=(____)-4nb37.md>)
- [&+=(_:_:)](<simd/&+=(____)-6bl8h.md>)
- [&-(_:_:)](<simd/&-(____)-18r5t.md>)
- [&-(_:_:)](<simd/&-(____)-3k78n.md>)
- [&-(_:_:)](<simd/&-(____)-8sti5.md>)
- [&-=(_:_:)](<simd/&-=(____)-8wqjs.md>)
- [&-=(_:_:)](<simd/&-=(____)-9uxv2.md>)
- [&=(_:_:)](<simd/&=(____)-8ruc4.md>)
- [&=(_:_:)](<simd/&=(____)-9p2uz.md>)
- [&\>\>(_:_:)](<simd/&__(____)-4zcvd.md>)
- [&\>\>(_:_:)](<simd/&__(____)-5ccr.md>)
- [&\<\<(_:_:)](<simd/&__(____)-5zfif.md>)
- [&\<\<(_:_:)](<simd/&__(____)-6vdh9.md>)
- [&\>\>(_:_:)](<simd/&__(____)-8f94f.md>)
- [&\<\<(_:_:)](<simd/&__(____)-9p0g4.md>)
- [&\<\<=(_:_:)](<simd/&__=(____)-2r7mx.md>)
- [&\>\>=(_:_:)](<simd/&__=(____)-66i5n.md>)
- [&\>\>=(_:_:)](<simd/&__=(____)-8yrf.md>)
- [&\<\<=(_:_:)](<simd/&__=(____)-94hft.md>)
- [*(_:_:)](<simd/_(____)-33k6i.md>)
- [*(_:_:)](<simd/_(____)-4fl9b.md>)
- [*(_:_:)](<simd/_(____)-4wltm.md>)
- [*=(_:_:)](<simd/_=(____)-33czt.md>)
- [*=(_:_:)](<simd/_=(____)-jal7.md>)
- [+(_:_:)](<simd/+(____)-48zcp.md>)
- [+(_:_:)](<simd/+(____)-64jan.md>)
- [+(_:_:)](<simd/+(____)-68uuk.md>)
- [+=(_:_:)](<simd/+=(____)-14pp9.md>)
- [+=(_:_:)](<simd/+=(____)-3jf1j.md>)
- [+=(_:_:)](<simd/+=(____)-9f7e0.md>)
- [-(_:)](<simd/-(__)-7asi6.md>)
- [-(_:)](<simd/-(__)-9ukvl.md>)
- [-(_:_:)](<simd/-(____)-2ad59.md>)
- [-(_:_:)](<simd/-(____)-3lx2i.md>)
- [-(_:_:)](<simd/-(____)-oego.md>)
- [-=(_:_:)](<simd/-=(____)-4uwnp.md>)
- [-=(_:_:)](<simd/-=(____)-6dwmc.md>)
- [-=(_:_:)](<simd/-=(____)-6ejxe.md>)
- [.!=(_:_:)](<simd/'.!=(____)-3m98p.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simd/'.!=(____)-402ba.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simd/'.!=(____)-8undu.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.==(_:_:)](<simd/'.==(____)-1nb4h.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simd/'.==(____)-5akc8.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simd/'.==(____)-8utr5.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.\>(_:_:)](<simd/'._(____)-2bb66.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<simd/'._(____)-2g6i2.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<simd/'._(____)-6kr63.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>(_:_:)](<simd/'._(____)-7ad36.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<simd/'._(____)-8bwmo.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\<(_:_:)](<simd/'._(____)-935pf.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>=(_:_:)](<simd/'._=(____)-1grcf.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\>=(_:_:)](<simd/'._=(____)-4poyx.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<simd/'._=(____)-7ulie.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\<=(_:_:)](<simd/'._=(____)-8vgvo.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<simd/'._=(____)-d7g2.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<simd/'._=(____)-iulp.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [%(_:_:)](<simd/_(____)-1qdv9.md>)
- [/(_:_:)](<simd/_(____)-1rb4.md>)
- [|(_:_:)](<simd/_(____)-225ln.md>)
- [/(_:_:)](<simd/_(____)-2hi2t.md>)
- [/(_:_:)](<simd/_(____)-2om3p.md>)
- [|(_:_:)](<simd/_(____)-3ge91.md>)
- [%(_:_:)](<simd/_(____)-3scvv.md>)
- [%(_:_:)](<simd/_(____)-4djx9.md>)
- [|(_:_:)](<simd/_(____)-5f3rz.md>)
- [^(_:_:)](<simd/_(____)-620ag.md>)
- [^(_:_:)](<simd/_(____)-6ryjr.md>)
- [/(_:_:)](<simd/_(____)-6tba5.md>)
- [^(_:_:)](<simd/_(____)-73syd.md>)
- [/(_:_:)](<simd/_(____)-80bu5.md>)
- [/(_:_:)](<simd/_(____)-8gl48.md>)
- [%=(_:_:)](<simd/_=(____)-17fvb.md>)
- [|=(_:_:)](<simd/_=(____)-1olgw.md>)
- [/=(_:_:)](<simd/_=(____)-1xum3.md>)
- [/=(_:_:)](<simd/_=(____)-2i5w5.md>)
- [^=(_:_:)](<simd/_=(____)-5qmfn.md>)
- [|=(_:_:)](<simd/_=(____)-7q26h.md>)
- [/=(_:_:)](<simd/_=(____)-9rh2.md>)
- [^=(_:_:)](<simd/_=(____)-9yqbl.md>)
- [/=(_:_:)](<simd/_=(____)-dtaz.md>)
- [%=(_:_:)](<simd/_=(____)-eq5q.md>)
- [~(_:)](<simd/~(__).md>)

### Associated Types

- [MaskStorage](simd/maskstorage.md) — The mask type resulting from pointwise comparisons of this vector type.

### Initializers

- [init(_:)](<simd/init(__)-18uy8.md>) — Creates a vector from the given sequence.
- [init(_:)](<simd/init(__)-4h623.md>)
- [init(repeating:)](<simd/init(repeating_).md>) — A vector with the specified scalar in all lanes.

### Instance Properties

- [indices](simd/indices.md) — The valid indices for subscripting the vector.
- [leadingZeroBitCount](simd/leadingzerobitcount.md)
- [nonzeroBitCount](simd/nonzerobitcount.md)
- [trailingZeroBitCount](simd/trailingzerobitcount.md)

### Instance Methods

- [addProduct(_:_:)](<simd/addproduct(____)-256j6.md>)
- [addProduct(_:_:)](<simd/addproduct(____)-3mvjt.md>)
- [addProduct(_:_:)](<simd/addproduct(____)-i1fp.md>)
- [addingProduct(_:_:)](<simd/addingproduct(____)-4h4k3.md>)
- [addingProduct(_:_:)](<simd/addingproduct(____)-59qn8.md>)
- [addingProduct(_:_:)](<simd/addingproduct(____)-kk15.md>)
- [clamp(lowerBound:upperBound:)](<simd/clamp(lowerbound_upperbound_)-3tdwm.md>)
- [clamp(lowerBound:upperBound:)](<simd/clamp(lowerbound_upperbound_)-yh51.md>)
- [clamped(lowerBound:upperBound:)](<simd/clamped(lowerbound_upperbound_)-4k4gy.md>)
- [clamped(lowerBound:upperBound:)](<simd/clamped(lowerbound_upperbound_)-9hl58.md>)
- [formSquareRoot()](<simd/formsquareroot().md>)
- [max()](<simd/max()-7j0po.md>) — The greatest scalar in the vector.
- [max()](<simd/max()-l6ds.md>) — The greatest element in the vector.
- [min()](<simd/min()-7pa71.md>) — The least scalar in the vector.
- [min()](<simd/min()-9z12h.md>) — The least element in the vector.
- [replace(with:where:)](<simd/replace(with_where_)-6if0p.md>) — Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simd/replace(with_where_)-91tn3.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simd/replacing(with_where_)-1nga6.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simd/replacing(with_where_)-8vzk.md>) — Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [round(_:)](<simd/round(__).md>)
- [rounded(_:)](<simd/rounded(__).md>) — A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [squareRoot()](<simd/squareroot().md>)
- [sum()](<simd/sum().md>) — The sum of the scalars in the vector.
- [wrappedSum()](<simd/wrappedsum().md>) — Returns the sum of the scalars in the vector, computed with wrapping addition.

### Type Properties

- [one](simd/one-428b1.md) — A vector with one in all lanes.
- [one](simd/one-6bgr9.md) — A vector with one in all lanes.
- [zero](simd/zero-6gnz.md) — A vector with zero in all lanes.
- [zero](simd/zero-8n566.md) — A vector with zero in all lanes.

### Type Methods

- [random(in:)](<simd/random(in_)-13ruo.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:)](<simd/random(in_)-3meec.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:)](<simd/random(in_)-4rat4.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:)](<simd/random(in_)-5ur5a.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:using:)](<simd/random(in_using_)-5uz8w.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [random(in:using:)](<simd/random(in_using_)-86tab.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [random(in:using:)](<simd/random(in_using_)-8bcnv.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [random(in:using:)](<simd/random(in_using_)-8yt59.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.

## See Also

### Supporting Types

- [SIMDScalar](simdscalar.md) — A type that can be used as an element in a SIMD vector.
- [SIMDStorage](simdstorage.md) — A type that can function as storage for a SIMD vector type.
- [SIMDMask](simdmask.md)
