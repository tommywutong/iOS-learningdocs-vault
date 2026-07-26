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
doc_path: /documentation/swift/simd32/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd32/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd32/simd-implementations.json'
content_hash: 'sha256:d70c41a4a104ecc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [SIMD Vector Types](../simd-vector-types.md) · [SIMD32](../simd32.md)

# SIMD Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [&(_:_:)](<&(____)-3y4ee.md>)
- [&(_:_:)](<&(____)-5hn2d.md>)
- [&(_:_:)](<&(____)-6m27n.md>)
- [&*(_:_:)](<&_(____)-18c2j.md>)
- [&*(_:_:)](<&_(____)-39jwx.md>)
- [&*(_:_:)](<&_(____)-7snfm.md>)
- [&*=(_:_:)](<&_=(____)-317ft.md>)
- [&*=(_:_:)](<&_=(____)-4o8xl.md>)
- [&+(_:_:)](<&+(____)-2klka.md>)
- [&+(_:_:)](<&+(____)-5s8y2.md>)
- [&+(_:_:)](<&+(____)-6wi7o.md>)
- [&+=(_:_:)](<&+=(____)-1ho7b.md>)
- [&+=(_:_:)](<&+=(____)-579bp.md>)
- [&-(_:_:)](<&-(____)-1e36y.md>)
- [&-(_:_:)](<&-(____)-4705x.md>)
- [&-(_:_:)](<&-(____)-8s9k4.md>)
- [&-=(_:_:)](<&-=(____)-594jw.md>)
- [&-=(_:_:)](<&-=(____)-5pn4x.md>)
- [&=(_:_:)](<&=(____)-5eswa.md>)
- [&=(_:_:)](<&=(____)-9jgzy.md>)
- [&\<\<(_:_:)](<&__(____)-29eng.md>)
- [&\>\>(_:_:)](<&__(____)-4gsmr.md>)
- [&\>\>(_:_:)](<&__(____)-78ish.md>)
- [&\<\<(_:_:)](<&__(____)-7zqu8.md>)
- [&\>\>(_:_:)](<&__(____)-89xqs.md>)
- [&\<\<(_:_:)](<&__(____)-9hia9.md>)
- [&\>\>=(_:_:)](<&__=(____)-3ali8.md>)
- [&\>\>=(_:_:)](<&__=(____)-762kk.md>)
- [&\<\<=(_:_:)](<&__=(____)-815bv.md>)
- [&\<\<=(_:_:)](<&__=(____)-92dly.md>)
- [*(_:_:)](<_(____)-2s55h.md>)
- [*(_:_:)](<_(____)-418m6.md>) _(deprecated)_
- [*(_:_:)](<_(____)-4x7hq.md>)
- [*(_:_:)](<_(____)-7q0sz.md>) _(deprecated)_
- [*(_:_:)](<_(____)-7shb0.md>) _(deprecated)_
- [*(_:_:)](<_(____)-9qya8.md>)
- [*=(_:_:)](<_=(____)-1i0tm.md>)
- [*=(_:_:)](<_=(____)-36zit.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-46f5z.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-8kra8.md>)
- [+(_:_:)](<+(____)-2phi3.md>)
- [+(_:_:)](<+(____)-473a4.md>) _(deprecated)_
- [+(_:_:)](<+(____)-4w7pm.md>)
- [+(_:_:)](<+(____)-59ak9.md>) _(deprecated)_
- [+(_:_:)](<+(____)-5rl9l.md>) _(deprecated)_
- [+(_:_:)](<+(____)-tzme.md>)
- [+=(_:_:)](<+=(____)-2gvba.md>)
- [+=(_:_:)](<+=(____)-318n3.md>) _(deprecated)_
- [+=(_:_:)](<+=(____)-6aukb.md>) _(deprecated)_
- [+=(_:_:)](<+=(____)-9yj49.md>)
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-27153.md>)
- [-(_:_:)](<-(____)-2zgvi.md>)
- [-(_:_:)](<-(____)-4vvz.md>) _(deprecated)_
- [-(_:_:)](<-(____)-7rtph.md>) _(deprecated)_
- [-(_:_:)](<-(____)-8y206.md>)
- [-(_:_:)](<-(____)-ily3.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-1bm21.md>)
- [-=(_:_:)](<-=(____)-2aro2.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-4c6ab.md>)
- [-=(_:_:)](<-=(____)-6ujbc.md>) _(deprecated)_
- [.!=(_:_:)](<'.!=(____)-2u3yd.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-6dgv1.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-968x6.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.==(_:_:)](<'.==(____)-5y9oc.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-6oddf.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-8sr5e.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.\<(_:_:)](<'._(____)-28t6e.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-4ahoi.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>(_:_:)](<'._(____)-6xg1q.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<'._(____)-78u7r.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\<(_:_:)](<'._(____)-7bowa.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-89ezy.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>=(_:_:)](<'._=(____)-2c2t0.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-3t7xa.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-58tjg.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-5htya.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-64co6.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-9lx6q.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two vectors are equal.
- [%(_:_:)](<_(____)-34uwb.md>)
- [|(_:_:)](<_(____)-3w1pz.md>)
- [^(_:_:)](<_(____)-414xo.md>)
- [|(_:_:)](<_(____)-44n0x.md>)
- [^(_:_:)](<_(____)-474ry.md>)
- [/(_:_:)](<_(____)-4lwb2.md>)
- [/(_:_:)](<_(____)-4n158.md>)
- [/(_:_:)](<_(____)-4ucgx.md>)
- [|(_:_:)](<_(____)-50id9.md>)
- [/(_:_:)](<_(____)-5j9uq.md>)
- [^(_:_:)](<_(____)-5y65m.md>)
- [%(_:_:)](<_(____)-6zy.md>)
- [%(_:_:)](<_(____)-7fea3.md>)
- [/(_:_:)](<_(____)-8nial.md>)
- [/(_:_:)](<_(____)-pk1j.md>)
- [|=(_:_:)](<_=(____)-11pnj.md>)
- [%=(_:_:)](<_=(____)-1vap7.md>)
- [/=(_:_:)](<_=(____)-20gc6.md>)
- [|=(_:_:)](<_=(____)-26y2h.md>)
- [/=(_:_:)](<_=(____)-2dyv7.md>)
- [/=(_:_:)](<_=(____)-2okko.md>)
- [^=(_:_:)](<_=(____)-49dhy.md>)
- [^=(_:_:)](<_=(____)-4prs.md>)
- [/=(_:_:)](<_=(____)-66xdx.md>)
- [%=(_:_:)](<_=(____)-8y875.md>)
- [~(_:)](<~(__).md>)

### Initializers

- [init(_:)](<init(__)-6afuc.md>) — Creates a vector from the given sequence.
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — Creates a vector from the specified elements.
- [init(from:)](<init(from_).md>) — Creates a new vector by decoding scalars from the given decoder.
- [init(repeating:)](<init(repeating_)-1e473.md>) — A vector with the specified scalar in all lanes.

### Instance Properties

- [description](description.md) — A textual description of the vector.
- [indices](indices.md) — The valid indices for subscripting the vector.
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### Instance Methods

- [addProduct(_:_:)](<addproduct(____)-2e6v4.md>)
- [addProduct(_:_:)](<addproduct(____)-65sbs.md>)
- [addProduct(_:_:)](<addproduct(____)-9epk7.md>)
- [addingProduct(_:_:)](<addingproduct(____)-7uual.md>)
- [addingProduct(_:_:)](<addingproduct(____)-8gka.md>)
- [addingProduct(_:_:)](<addingproduct(____)-8svnk.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-mfa1.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-r8mu.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-3fn6n.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-5edvy.md>)
- [encode(to:)](<encode(to_).md>) — Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — Hashes the elements of the vector using the given hasher.
- [max()](<max()-36c8c.md>) — The greatest scalar in the vector.
- [max()](<max()-9t6zm.md>) — The greatest element in the vector.
- [min()](<min()-5cvw3.md>) — The least element in the vector.
- [min()](<min()-9a3ey.md>) — The least scalar in the vector.
- [replace(with:where:)](<replace(with_where_)-7o8hd.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<replace(with_where_)-9jte6.md>) — Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-3v5ph.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-h40g.md>) — Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — The sum of the scalars in the vector.
- [wrappedSum()](<wrappedsum().md>) — Returns the sum of the scalars in the vector, computed with wrapping addition.

### Type Properties

- [one](one-13jdz.md) — A vector with one in all lanes.
- [one](one-3mop8.md) — A vector with one in all lanes.
- [zero](zero-2wd1r.md) — A vector with zero in all lanes.
- [zero](zero-3kong.md) — A vector with zero in all lanes.

### Type Methods

- [random(in:)](<random(in_)-3w4wf.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:)](<random(in_)-82yup.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:using:)](<random(in_using_)-7fl57.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-7xfit.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
