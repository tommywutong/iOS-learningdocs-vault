---
title: SIMD Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/simd16/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd16/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd16/simd-implementations.json'
content_hash: 'sha256:dd79856b9bf00603'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [SIMD Vector Types](../simd-vector-types.md) · [SIMD16](../simd16.md)

# SIMD Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [&(_:_:)](<&(____)-3qlss.md>)
- [&(_:_:)](<&(____)-5aelr.md>)
- [&(_:_:)](<&(____)-6tkkh.md>)
- [&*(_:_:)](<&_(____)-110zd.md>)
- [&*(_:_:)](<&_(____)-3h4zn.md>)
- [&*(_:_:)](<&_(____)-7l2c0.md>)
- [&*=(_:_:)](<&_=(____)-2tosr.md>)
- [&*=(_:_:)](<&_=(____)-4ul6j.md>)
- [&+(_:_:)](<&+(____)-2d5m0.md>)
- [&+(_:_:)](<&+(____)-5yle0.md>)
- [&+(_:_:)](<&+(____)-6p9ta.md>)
- [&+=(_:_:)](<&+=(____)-1a5tp.md>)
- [&+=(_:_:)](<&+=(____)-500n3.md>)
- [&-(_:_:)](<&-(____)-1kaco.md>)
- [&-(_:_:)](<&-(____)-3zrkv.md>)
- [&-(_:_:)](<&-(____)-8zi32.md>)
- [&-=(_:_:)](<&-=(____)-51lye.md>)
- [&-=(_:_:)](<&-=(____)-5x3ab.md>)
- [&=(_:_:)](<&=(____)-5m8ug.md>)
- [&=(_:_:)](<&=(____)-9d1yc.md>)
- [&\<\<(_:_:)](<&__(____)-2ftme.md>)
- [&\>\>(_:_:)](<&__(____)-4oaw1.md>)
- [&\>\>(_:_:)](<&__(____)-71acz.md>)
- [&\<\<(_:_:)](<&__(____)-7t9iq.md>)
- [&\>\>(_:_:)](<&__(____)-82fce.md>)
- [&\<\<(_:_:)](<&__(____)-9nper.md>)
- [&\>\>=(_:_:)](<&__=(____)-3i1nm.md>)
- [&\>\>=(_:_:)](<&__=(____)-6znxq.md>)
- [&\<\<=(_:_:)](<&__=(____)-88lh5.md>)
- [&\<\<=(_:_:)](<&__=(____)-8v518.md>)
- [*(_:_:)](<_(____)-2yhe7.md>)
- [*(_:_:)](<_(____)-3ur7o.md>) _(deprecated)_
- [*(_:_:)](<_(____)-4pozo.md>)
- [*(_:_:)](<_(____)-7l65y.md>) _(deprecated)_
- [*(_:_:)](<_(____)-7whvl.md>) _(deprecated)_
- [*(_:_:)](<_(____)-9y6zm.md>)
- [*=(_:_:)](<_=(____)-1od2g.md>)
- [*=(_:_:)](<_=(____)-2zjkv.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-4dnsd.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-8scfm.md>)
- [+(_:_:)](<+(____)-10ebw.md>)
- [+(_:_:)](<+(____)-2i69l.md>)
- [+(_:_:)](<+(____)-40yo6.md>) _(deprecated)_
- [+(_:_:)](<+(____)-52yaj.md>) _(deprecated)_
- [+(_:_:)](<+(____)-53q5k.md>)
- [+(_:_:)](<+(____)-5z1ez.md>) _(deprecated)_
- [+=(_:_:)](<+=(____)-29mqk.md>)
- [+=(_:_:)](<+=(____)-2urad.md>) _(deprecated)_
- [+=(_:_:)](<+=(____)-5ciy.md>)
- [+=(_:_:)](<+=(____)-63jfd.md>) _(deprecated)_
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1zpzh.md>)
- [-(_:_:)](<-(____)-2t24k.md>)
- [-(_:_:)](<-(____)-7z2dr.md>) _(deprecated)_
- [-(_:_:)](<-(____)-946vg.md>)
- [-(_:_:)](<-(____)-bdg9.md>) _(deprecated)_
- [-(_:_:)](<-(____)-c6qt.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-15h6z.md>)
- [-=(_:_:)](<-=(____)-2iaa8.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-44xi9.md>)
- [-=(_:_:)](<-=(____)-6n3d6.md>) _(deprecated)_
- [.!=(_:_:)](<'.!=(____)-2mivz.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-679dj.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-8zu6g.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.==(_:_:)](<'.==(____)-64qzq.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-6vtbl.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-8z3e8.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.\<(_:_:)](<'._(____)-2gbn0.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-436q8.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<'._(____)-71lm5.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-73ut0.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<'._(____)-7j4ug.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-8gxec.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>=(_:_:)](<'._=(____)-25vha.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-3mvms.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-52esm.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-5nyi8.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-6au0s.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-9s9fk.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two vectors are equal.
- [%(_:_:)](<_(____)-3cb1l.md>)
- [^(_:_:)](<_(____)-3uq7q.md>)
- [|(_:_:)](<_(____)-3x1xf.md>)
- [|(_:_:)](<_(____)-42gh9.md>)
- [^(_:_:)](<_(____)-4ekpw.md>)
- [/(_:_:)](<_(____)-4fhk4.md>)
- [/(_:_:)](<_(____)-4fl12.md>)
- [/(_:_:)](<_(____)-50opv.md>)
- [|(_:_:)](<_(____)-57tav.md>)
- [/(_:_:)](<_(____)-5pqvk.md>)
- [^(_:_:)](<_(____)-5qq08.md>)
- [%(_:_:)](<_(____)-7mufd.md>)
- [/(_:_:)](<_(____)-8g9p3.md>)
- [%(_:_:)](<_(____)-9s9s3.md>)
- [/(_:_:)](<_(____)-vyq5.md>)
- [/=(_:_:)](<_=(____)-1t070.md>)
- [%=(_:_:)](<_=(____)-21f7t.md>)
- [/=(_:_:)](<_=(____)-26qa9.md>)
- [|=(_:_:)](<_=(____)-2da4b.md>)
- [/=(_:_:)](<_=(____)-2w5pm.md>)
- [^=(_:_:)](<_=(____)-422nw.md>)
- [/=(_:_:)](<_=(____)-60irj.md>)
- [%=(_:_:)](<_=(____)-95j6b.md>)
- [^=(_:_:)](<_=(____)-9wq7v.md>)
- [|=(_:_:)](<_=(____)-vb11.md>)
- [~(_:)](<~(__).md>)

### Initializers

- [init(_:)](<init(__)-64awu.md>) — Creates a vector from the given sequence.
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — Creates a vector from the specified elements.
- [init(from:)](<init(from_).md>) — Creates a new vector by decoding scalars from the given decoder.
- [init(repeating:)](<init(repeating_)-16o1h.md>) — A vector with the specified scalar in all lanes.

### Instance Properties

- [description](description.md) — A textual description of the vector.
- [indices](indices.md) — The valid indices for subscripting the vector.
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### Instance Methods

- [addProduct(_:_:)](<addproduct(____)-2kjb6.md>)
- [addProduct(_:_:)](<addproduct(____)-5yjpm.md>)
- [addProduct(_:_:)](<addproduct(____)-97gsd.md>)
- [addingProduct(_:_:)](<addingproduct(____)-816br.md>)
- [addingProduct(_:_:)](<addingproduct(____)-8lfqq.md>)
- [addingProduct(_:_:)](<addingproduct(____)-freg.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-krkc.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-tq4b.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-38es5.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-5lop0.md>)
- [encode(to:)](<encode(to_).md>) — Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — Hashes the elements of the vector using the given hasher.
- [max()](<max()-2yw9y.md>) — The greatest scalar in the vector.
- [max()](<max()-ap.md>) — The greatest element in the vector.
- [min()](<min()-55nb5.md>) — The least element in the vector.
- [min()](<min()-9hjd4.md>) — The least scalar in the vector.
- [replace(with:where:)](<replace(with_where_)-7gncz.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<replace(with_where_)-9cks4.md>) — Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-42oan.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-ng2a.md>) — Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — The sum of the scalars in the vector.
- [wrappedSum()](<wrappedsum().md>) — Returns the sum of the scalars in the vector, computed with wrapping addition.

### Type Properties

- [one](one-1azcd.md) — A vector with one in all lanes.
- [one](one-3gc92.md) — A vector with one in all lanes.
- [zero](zero-33lnp.md) — A vector with zero in all lanes.
- [zero](zero-3dg4m.md) — A vector with zero in all lanes.

### Type Methods

- [random(in:)](<random(in_)-42m5x.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:)](<random(in_)-8ajs3.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:using:)](<random(in_using_)-78ch5.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-7rau7.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
