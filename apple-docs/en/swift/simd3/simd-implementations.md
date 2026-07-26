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
doc_path: /documentation/swift/simd3/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd3/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd3/simd-implementations.json'
content_hash: 'sha256:88d19e1961986ea3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [SIMD Vector Types](../simd-vector-types.md) · [SIMD3](../simd3.md)

# SIMD Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [&(_:_:)](<&(____)-5sle8.md>)
- [&(_:_:)](<&(____)-6dadi.md>)
- [&(_:_:)](<&(____)-9cv5x.md>)
- [&*(_:_:)](<&_(____)-1tpdr.md>)
- [&*(_:_:)](<&_(____)-2ui6l.md>)
- [&*(_:_:)](<&_(____)-9lqx2.md>)
- [&*=(_:_:)](<&_=(____)-4n2gi.md>)
- [&*=(_:_:)](<&_=(____)-4uaeq.md>)
- [&+(_:_:)](<&+(____)-5jgfk.md>)
- [&+(_:_:)](<&+(____)-6qry0.md>)
- [&+(_:_:)](<&+(____)-s6mm.md>)
- [&+=(_:_:)](<&+=(____)-15hgq.md>)
- [&+=(_:_:)](<&+=(____)-xndr.md>)
- [&-(_:_:)](<&-(____)-4tne0.md>)
- [&-(_:_:)](<&-(____)-6usqk.md>)
- [&-(_:_:)](<&-(____)-8tcdi.md>)
- [&-=(_:_:)](<&-=(____)-534bk.md>)
- [&-=(_:_:)](<&-=(____)-8d2rr.md>)
- [&=(_:_:)](<&=(____)-583on.md>)
- [&=(_:_:)](<&=(____)-5a80m.md>)
- [&\<\<(_:_:)](<&__(____)-1cf4m.md>)
- [&\>\>(_:_:)](<&__(____)-8w3ew.md>)
- [&\<\<(_:_:)](<&__(____)-92xk8.md>)
- [&\<\<(_:_:)](<&__(____)-9j2cu.md>)
- [&\>\>(_:_:)](<&__(____)-in54.md>)
- [&\>\>(_:_:)](<&__(____)-on38.md>)
- [&\>\>=(_:_:)](<&__=(____)-2n11s.md>)
- [&\>\>=(_:_:)](<&__=(____)-38a87.md>)
- [&\<\<=(_:_:)](<&__=(____)-7dkpa.md>)
- [&\<\<=(_:_:)](<&__=(____)-83fu5.md>)
- [*(_:_:)](<_(____)-2hvzj.md>)
- [*(_:_:)](<_(____)-4cbmk.md>)
- [*(_:_:)](<_(____)-4lo7f.md>) _(deprecated)_
- [*(_:_:)](<_(____)-50fba.md>) _(deprecated)_
- [*(_:_:)](<_(____)-6ktkg.md>) _(deprecated)_
- [*(_:_:)](<_(____)-9wplu.md>)
- [*=(_:_:)](<_=(____)-27oce.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-3zjhs.md>)
- [*=(_:_:)](<_=(____)-4j0iv.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-5qujk.md>)
- [+(_:_:)](<+(____)-1h7rv.md>) _(deprecated)_
- [+(_:_:)](<+(____)-1s6av.md>)
- [+(_:_:)](<+(____)-2bek1.md>)
- [+(_:_:)](<+(____)-62q9z.md>) _(deprecated)_
- [+(_:_:)](<+(____)-844rw.md>) _(deprecated)_
- [+(_:_:)](<+(____)-9w8yd.md>)
- [+=(_:_:)](<+=(____)-13ac4.md>)
- [+=(_:_:)](<+=(____)-33ge7.md>)
- [+=(_:_:)](<+=(____)-3islb.md>) _(deprecated)_
- [+=(_:_:)](<+=(____)-4kezy.md>) _(deprecated)_
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1eqhb.md>)
- [-(_:_:)](<-(____)-59t4d.md>) _(deprecated)_
- [-(_:_:)](<-(____)-5hurb.md>)
- [-(_:_:)](<-(____)-5rbfs.md>) _(deprecated)_
- [-(_:_:)](<-(____)-8pag1.md>)
- [-(_:_:)](<-(____)-8vs62.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-5ej92.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-6att9.md>)
- [-=(_:_:)](<-=(____)-8oysv.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-90eji.md>)
- [.!=(_:_:)](<'.!=(____)-1o5ed.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-5knpd.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-70ndl.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.==(_:_:)](<'.==(____)-1q0oq.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-4ddir.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-8605k.md>) — A vector mask with the result of a pointwise equality comparison.
- [.\<(_:_:)](<'._(____)-2n374.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-3inh2.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<'._(____)-49xao.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\<(_:_:)](<'._(____)-5ld34.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-5wj69.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>(_:_:)](<'._(____)-6yoj2.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>=(_:_:)](<'._=(____)-134b8.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-1wtru.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-3m1wf.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-41rws.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-5jyme.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-9paeh.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two vectors are equal.
- [|(_:_:)](<_(____)-1t3fs.md>)
- [/(_:_:)](<_(____)-2nvgk.md>)
- [/(_:_:)](<_(____)-2o86v.md>)
- [%(_:_:)](<_(____)-2skh3.md>)
- [/(_:_:)](<_(____)-2zako.md>)
- [|(_:_:)](<_(____)-3pbx6.md>)
- [/(_:_:)](<_(____)-3vpcf.md>)
- [^(_:_:)](<_(____)-6f2o8.md>)
- [^(_:_:)](<_(____)-6fu2f.md>)
- [|(_:_:)](<_(____)-7v8x.md>)
- [^(_:_:)](<_(____)-7vf28.md>)
- [%(_:_:)](<_(____)-9061v.md>)
- [/(_:_:)](<_(____)-936c1.md>)
- [%(_:_:)](<_(____)-9i1nl.md>)
- [/(_:_:)](<_(____)-9io5d.md>)
- [/=(_:_:)](<_=(____)-18ko5.md>)
- [|=(_:_:)](<_=(____)-1tfky.md>)
- [/=(_:_:)](<_=(____)-5c1dl.md>)
- [|=(_:_:)](<_=(____)-6kg54.md>)
- [%=(_:_:)](<_=(____)-723if.md>)
- [/=(_:_:)](<_=(____)-7u3yj.md>)
- [^=(_:_:)](<_=(____)-8juvl.md>)
- [%=(_:_:)](<_=(____)-9a0es.md>)
- [/=(_:_:)](<_=(____)-9ivy0.md>)
- [^=(_:_:)](<_=(____)-sxrj.md>)
- [~(_:)](<~(__).md>)

### Initializers

- [init(_:)](<init(__)-3f00q.md>) — Creates a vector from the given sequence.
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — Creates a vector from the specified elements.
- [init(from:)](<init(from_).md>) — Creates a new vector by decoding scalars from the given decoder.
- [init(repeating:)](<init(repeating_)-97v6a.md>) — A vector with the specified scalar in all lanes.

### Instance Properties

- [description](description.md) — A textual description of the vector.
- [indices](indices.md) — The valid indices for subscripting the vector.
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### Instance Methods

- [addProduct(_:_:)](<addproduct(____)-24nyp.md>)
- [addProduct(_:_:)](<addproduct(____)-48e6d.md>)
- [addProduct(_:_:)](<addproduct(____)-8hqma.md>)
- [addingProduct(_:_:)](<addingproduct(____)-1naql.md>)
- [addingProduct(_:_:)](<addingproduct(____)-76u4u.md>)
- [addingProduct(_:_:)](<addingproduct(____)-94rr8.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-77fkz.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-9has1.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-4qqqj.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-8tjee.md>)
- [encode(to:)](<encode(to_).md>) — Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — Hashes the elements of the vector using the given hasher.
- [max()](<max()-71ltd.md>) — The greatest element in the vector.
- [max()](<max()-xz2j.md>) — The greatest scalar in the vector.
- [min()](<min()-7qoof.md>) — The least scalar in the vector.
- [min()](<min()-8s36y.md>) — The least element in the vector.
- [replace(with:where:)](<replace(with_where_)-7e3ns.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<replace(with_where_)-7yqk1.md>) — Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-32h3i.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-3o6zs.md>) — Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — The sum of the scalars in the vector.
- [wrappedSum()](<wrappedsum().md>) — Returns the sum of the scalars in the vector, computed with wrapping addition.

### Type Properties

- [one](one-1gjj3.md) — A vector with one in all lanes.
- [one](one-7ehtb.md) — A vector with one in all lanes.
- [zero](zero-1xegj.md) — A vector with zero in all lanes.
- [zero](zero-6rmb2.md) — A vector with zero in all lanes.

### Type Methods

- [random(in:)](<random(in_)-3wbg2.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:)](<random(in_)-6jj3m.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:using:)](<random(in_using_)-6dbs2.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-7xbdr.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
