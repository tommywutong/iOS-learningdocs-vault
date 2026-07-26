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
doc_path: /documentation/swift/simd2/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd2/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd2/simd-implementations.json'
content_hash: 'sha256:1a21f738067fcf2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [SIMD Vector Types](../simd-vector-types.md) · [SIMD2](../simd2.md)

# SIMD Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [&(_:_:)](<&(____)-5sluq.md>)
- [&(_:_:)](<&(____)-6dank.md>)
- [&(_:_:)](<&(____)-9cv9t.md>)
- [&*(_:_:)](<&_(____)-1tpsv.md>)
- [&*(_:_:)](<&_(____)-2uia9.md>)
- [&*(_:_:)](<&_(____)-9lr3o.md>)
- [&*=(_:_:)](<&_=(____)-4n268.md>)
- [&*=(_:_:)](<&_=(____)-4ua1o.md>)
- [&+(_:_:)](<&+(____)-5jg3m.md>)
- [&+(_:_:)](<&+(____)-6qrmu.md>)
- [&+(_:_:)](<&+(____)-s654.md>)
- [&+=(_:_:)](<&+=(____)-15hks.md>)
- [&+=(_:_:)](<&+=(____)-xnu7.md>)
- [&-(_:_:)](<&-(____)-4tntq.md>)
- [&-(_:_:)](<&-(____)-6usy6.md>)
- [&-(_:_:)](<&-(____)-8tchg.md>)
- [&-=(_:_:)](<&-=(____)-5340e.md>)
- [&-=(_:_:)](<&-=(____)-8d2hj.md>)
- [&=(_:_:)](<&=(____)-583dj.md>)
- [&=(_:_:)](<&=(____)-5a7qw.md>)
- [&\<\<(_:_:)](<&__(____)-1cf7o.md>)
- [&\>\>(_:_:)](<&__(____)-8w3q6.md>)
- [&\<\<(_:_:)](<&__(____)-92xzu.md>)
- [&\<\<(_:_:)](<&__(____)-9j2fk.md>)
- [&\>\>(_:_:)](<&__(____)-inkq.md>)
- [&\>\>(_:_:)](<&__(____)-onf6.md>)
- [&\>\>=(_:_:)](<&__=(____)-2n0zi.md>)
- [&\>\>=(_:_:)](<&__=(____)-389yv.md>)
- [&\<\<=(_:_:)](<&__=(____)-7dkm4.md>)
- [&\<\<=(_:_:)](<&__=(____)-83fbl.md>)
- [*(_:_:)](<_(____)-2hwhr.md>)
- [*(_:_:)](<_(____)-4cbci.md>)
- [*(_:_:)](<_(____)-4lojf.md>) _(deprecated)_
- [*(_:_:)](<_(____)-50ffc.md>) _(deprecated)_
- [*(_:_:)](<_(____)-6ktum.md>) _(deprecated)_
- [*(_:_:)](<_(____)-9wp8w.md>)
- [*=(_:_:)](<_=(____)-27nt8.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-3zjz6.md>)
- [*=(_:_:)](<_=(____)-4j02f.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-5qufm.md>)
- [+(_:_:)](<+(____)-1h79f.md>) _(deprecated)_
- [+(_:_:)](<+(____)-1s6ev.md>)
- [+(_:_:)](<+(____)-2begd.md>)
- [+(_:_:)](<+(____)-62pyv.md>) _(deprecated)_
- [+(_:_:)](<+(____)-844oq.md>) _(deprecated)_
- [+(_:_:)](<+(____)-9w9bt.md>)
- [+=(_:_:)](<+=(____)-13ati.md>)
- [+=(_:_:)](<+=(____)-33g1r.md>)
- [+=(_:_:)](<+=(____)-3it33.md>) _(deprecated)_
- [+=(_:_:)](<+=(____)-4kf28.md>) _(deprecated)_
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1eq67.md>)
- [-(_:_:)](<-(____)-59t7d.md>) _(deprecated)_
- [-(_:_:)](<-(____)-5hv3b.md>)
- [-(_:_:)](<-(____)-5rbq2.md>) _(deprecated)_
- [-(_:_:)](<-(____)-8pa31.md>)
- [-(_:_:)](<-(____)-8vsnc.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-5eiqo.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-6au1l.md>)
- [-=(_:_:)](<-=(____)-8oyin.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-90e80.md>)
- [.!=(_:_:)](<'.!=(____)-1o5rd.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-5ko8d.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-70n1x.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.==(_:_:)](<'.==(____)-1q06g.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-4dd4z.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-860hm.md>) — A vector mask with the result of a pointwise equality comparison.
- [.\<(_:_:)](<'._(____)-2n2w2.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-3inug.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<'._(____)-49wsu.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\<(_:_:)](<'._(____)-5ldki.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-5wj3h.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>(_:_:)](<'._(____)-6yov0.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>=(_:_:)](<'._=(____)-134li.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-1wtvs.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-3m1tr.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-41ri2.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-5jyc4.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-9pao5.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two vectors are equal.
- [|(_:_:)](<_(____)-1t3qy.md>)
- [/(_:_:)](<_(____)-2nvzq.md>)
- [/(_:_:)](<_(____)-2o8h3.md>)
- [%(_:_:)](<_(____)-2sk6v.md>)
- [/(_:_:)](<_(____)-2zahy.md>)
- [|(_:_:)](<_(____)-3pc04.md>)
- [/(_:_:)](<_(____)-3vp33.md>)
- [^(_:_:)](<_(____)-6f29q.md>)
- [^(_:_:)](<_(____)-6ftk7.md>)
- [^(_:_:)](<_(____)-7veum.md>)
- [|(_:_:)](<_(____)-7vid.md>)
- [%(_:_:)](<_(____)-905lf.md>)
- [/(_:_:)](<_(____)-935ut.md>)
- [%(_:_:)](<_(____)-9i1cd.md>)
- [/(_:_:)](<_(____)-9ino5.md>)
- [/=(_:_:)](<_=(____)-18kdt.md>)
- [|=(_:_:)](<_=(____)-1tfgs.md>)
- [/=(_:_:)](<_=(____)-5c1gt.md>)
- [|=(_:_:)](<_=(____)-6kfnu.md>)
- [%=(_:_:)](<_=(____)-723sn.md>)
- [/=(_:_:)](<_=(____)-7u42r.md>)
- [^=(_:_:)](<_=(____)-8jvd9.md>)
- [%=(_:_:)](<_=(____)-9a0hy.md>)
- [/=(_:_:)](<_=(____)-9iwfe.md>)
- [^=(_:_:)](<_=(____)-sxsf.md>)
- [~(_:)](<~(__).md>)

### Initializers

- [init(_:)](<init(__)-3f03w.md>) — Creates a vector from the given sequence.
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — Creates a vector from the specified elements.
- [init(from:)](<init(from_).md>) — Creates a new vector by decoding scalars from the given decoder.
- [init(repeating:)](<init(repeating_)-97uo4.md>) — A vector with the specified scalar in all lanes.

### Instance Properties

- [description](description.md) — A textual description of the vector.
- [indices](indices.md) — The valid indices for subscripting the vector.
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### Instance Methods

- [addProduct(_:_:)](<addproduct(____)-24o9x.md>)
- [addProduct(_:_:)](<addproduct(____)-48dp5.md>)
- [addProduct(_:_:)](<addproduct(____)-8hqkc.md>)
- [addingProduct(_:_:)](<addingproduct(____)-1nafl.md>)
- [addingProduct(_:_:)](<addingproduct(____)-76tvc.md>)
- [addingProduct(_:_:)](<addingproduct(____)-94rva.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-77fvf.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-9havh.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-4qr0j.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-8tjus.md>)
- [encode(to:)](<encode(to_).md>) — Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — Hashes the elements of the vector using the given hasher.
- [max()](<max()-71lal.md>) — The greatest element in the vector.
- [max()](<max()-xykz.md>) — The greatest scalar in the vector.
- [min()](<min()-7qoe7.md>) — The least scalar in the vector.
- [min()](<min()-8s2vo.md>) — The least element in the vector.
- [replace(with:where:)](<replace(with_where_)-7e48m.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<replace(with_where_)-7yq25.md>) — Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-32hlo.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-3o6pm.md>) — Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — The sum of the scalars in the vector.
- [wrappedSum()](<wrappedsum().md>) — Returns the sum of the scalars in the vector, computed with wrapping addition.

### Type Properties

- [one](one-1gj1r.md) — A vector with one in all lanes.
- [one](one-7ehgf.md) — A vector with one in all lanes.
- [zero](zero-1xeqr.md) — A vector with zero in all lanes.
- [zero](zero-6rme0.md) — A vector with zero in all lanes.

### Type Methods

- [random(in:)](<random(in_)-3wbi8.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:)](<random(in_)-6jji8.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:using:)](<random(in_using_)-6dc38.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-7xbgv.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
