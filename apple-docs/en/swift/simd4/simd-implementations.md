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
doc_path: /documentation/swift/simd4/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd4/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd4/simd-implementations.json'
content_hash: 'sha256:adb88c73d252bbf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [SIMD Vector Types](../simd-vector-types.md) · [SIMD4](../simd4.md)

# SIMD Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [&(_:_:)](<&(____)-5slae.md>)
- [&(_:_:)](<&(____)-6d8rc.md>)
- [&(_:_:)](<&(____)-9ctm1.md>)
- [&*(_:_:)](<&_(____)-1tqez.md>)
- [&*(_:_:)](<&_(____)-2uiyx.md>)
- [&*(_:_:)](<&_(____)-9lt38.md>)
- [&*=(_:_:)](<&_=(____)-4n42g.md>)
- [&*=(_:_:)](<&_=(____)-4uao4.md>)
- [&+(_:_:)](<&+(____)-5jhzi.md>)
- [&+(_:_:)](<&+(____)-6qs5e.md>)
- [&+(_:_:)](<&+(____)-s4hc.md>)
- [&+=(_:_:)](<&+=(____)-15ft8.md>)
- [&+=(_:_:)](<&+=(____)-xlyb.md>)
- [&-(_:_:)](<&-(____)-4tm0i.md>)
- [&-(_:_:)](<&-(____)-6uuv6.md>)
- [&-(_:_:)](<&-(____)-8tbv8.md>)
- [&-=(_:_:)](<&-=(____)-534my.md>)
- [&-=(_:_:)](<&-=(____)-8d4df.md>)
- [&=(_:_:)](<&=(____)-5858j.md>)
- [&=(_:_:)](<&=(____)-5a8dc.md>)
- [&\<\<(_:_:)](<&__(____)-1cep0.md>)
- [&\>\>(_:_:)](<&__(____)-8w1v6.md>)
- [&\<\<(_:_:)](<&__(____)-92zqu.md>)
- [&\<\<(_:_:)](<&__(____)-9j33c.md>)
- [&\>\>(_:_:)](<&__(____)-imny.md>)
- [&\>\>(_:_:)](<&__(____)-olfi.md>)
- [&\>\>=(_:_:)](<&__=(____)-2n1ii.md>)
- [&\>\>=(_:_:)](<&__=(____)-38btv.md>)
- [&\<\<=(_:_:)](<&__=(____)-7dmas.md>)
- [&\<\<=(_:_:)](<&__=(____)-83fy1.md>)
- [*(_:_:)](<_(____)-2hvvf.md>)
- [*(_:_:)](<_(____)-4cbwu.md>)
- [*(_:_:)](<_(____)-4lqdj.md>) _(deprecated)_
- [*(_:_:)](<_(____)-50g1c.md>) _(deprecated)_
- [*(_:_:)](<_(____)-6kum2.md>) _(deprecated)_
- [*(_:_:)](<_(____)-9wqx4.md>)
- [*=(_:_:)](<_=(____)-27n78.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-3zlny.md>)
- [*=(_:_:)](<_=(____)-4iyd7.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-5qw5a.md>)
- [+(_:_:)](<+(____)-1h7vz.md>) _(deprecated)_
- [+(_:_:)](<+(____)-1s5sj.md>)
- [+(_:_:)](<+(____)-2bds5.md>)
- [+(_:_:)](<+(____)-62rmr.md>) _(deprecated)_
- [+(_:_:)](<+(____)-842lq.md>) _(deprecated)_
- [+(_:_:)](<+(____)-9w9vl.md>)
- [+=(_:_:)](<+=(____)-13aaq.md>)
- [+=(_:_:)](<+=(____)-33gh7.md>)
- [+=(_:_:)](<+=(____)-3itnf.md>) _(deprecated)_
- [+=(_:_:)](<+=(____)-4kfxk.md>) _(deprecated)_
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1epj7.md>)
- [-(_:_:)](<-(____)-59rjl.md>) _(deprecated)_
- [-(_:_:)](<-(____)-5hvnn.md>)
- [-(_:_:)](<-(____)-5rdme.md>) _(deprecated)_
- [-(_:_:)](<-(____)-8par9.md>)
- [-(_:_:)](<-(____)-8vs0w.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-5eh2w.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-6asc1.md>)
- [-=(_:_:)](<-=(____)-8oxw3.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-90eug.md>)
- [.!=(_:_:)](<'.!=(____)-1o6bl.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-5kor1.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-70nnx.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.==(_:_:)](<'.==(____)-1q28g.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-4deu7.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-862bq.md>) — A vector mask with the result of a pointwise equality comparison.
- [.\<(_:_:)](<'._(____)-2n4ry.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-3iokg.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<'._(____)-49xlm.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\<(_:_:)](<'._(____)-5lcly.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-5wiit.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>(_:_:)](<'._(____)-6yo8s.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>=(_:_:)](<'._=(____)-136h6.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-1wt9c.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-3m2gb.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-41pqm.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-5k06k.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-9pb8l.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two vectors are equal.
- [|(_:_:)](<_(____)-1t5na.md>)
- [/(_:_:)](<_(____)-2nxne.md>)
- [/(_:_:)](<_(____)-2o6l7.md>)
- [%(_:_:)](<_(____)-2sm0z.md>)
- [/(_:_:)](<_(____)-2zaxu.md>)
- [|(_:_:)](<_(____)-3pcys.md>)
- [/(_:_:)](<_(____)-3voib.md>)
- [^(_:_:)](<_(____)-6f0hu.md>)
- [^(_:_:)](<_(____)-6fvmb.md>)
- [|(_:_:)](<_(____)-7uxx.md>)
- [^(_:_:)](<_(____)-7vfdm.md>)
- [%(_:_:)](<_(____)-907nj.md>)
- [/(_:_:)](<_(____)-93465.md>)
- [%(_:_:)](<_(____)-9i1yt.md>)
- [/(_:_:)](<_(____)-9ipq5.md>)
- [/=(_:_:)](<_=(____)-18ijd.md>)
- [|=(_:_:)](<_=(____)-1tg44.md>)
- [/=(_:_:)](<_=(____)-5bzrx.md>)
- [|=(_:_:)](<_=(____)-6khqe.md>)
- [%=(_:_:)](<_=(____)-72383.md>)
- [/=(_:_:)](<_=(____)-7u2en.md>)
- [^=(_:_:)](<_=(____)-8jvxp.md>)
- [%=(_:_:)](<_=(____)-9a2l6.md>)
- [/=(_:_:)](<_=(____)-9iy46.md>)
- [^=(_:_:)](<_=(____)-syej.md>)
- [~(_:)](<~(__).md>)

### Initializers

- [init(_:)](<init(__)-3eyf0.md>) — Creates a vector from the given sequence.
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — Creates a vector from the specified elements.
- [init(from:)](<init(from_).md>) — Creates a new vector by decoding scalars from the given decoder.
- [init(repeating:)](<init(repeating_)-97szw.md>) — A vector with the specified scalar in all lanes.

### Instance Properties

- [description](description.md) — A textual description of the vector.
- [indices](indices.md) — The valid indices for subscripting the vector.
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### Instance Methods

- [addProduct(_:_:)](<addproduct(____)-24met.md>)
- [addProduct(_:_:)](<addproduct(____)-48fq9.md>)
- [addProduct(_:_:)](<addproduct(____)-8hr4k.md>)
- [addingProduct(_:_:)](<addingproduct(____)-1ncc9.md>)
- [addingProduct(_:_:)](<addingproduct(____)-76ryo.md>)
- [addingProduct(_:_:)](<addingproduct(____)-94txm.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-77gjj.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-9hcyl.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-4qp6n.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-8tlkk.md>)
- [encode(to:)](<encode(to_).md>) — Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — Hashes the elements of the vector using the given hasher.
- [max()](<max()-71kv9.md>) — The greatest element in the vector.
- [max()](<max()-xww7.md>) — The greatest scalar in the vector.
- [min()](<min()-7qq8b.md>) — The least scalar in the vector.
- [min()](<min()-8s3i4.md>) — The least element in the vector.
- [replace(with:where:)](<replace(with_where_)-7e4sy.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<replace(with_where_)-7yqkl.md>) — Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-32h18.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-3o8ie.md>) — Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — The sum of the scalars in the vector.
- [wrappedSum()](<wrappedsum().md>) — Returns the sum of the scalars in the vector, computed with wrapping addition.

### Type Properties

- [one](one-1ghcj.md) — A vector with one in all lanes.
- [one](one-7ejbf.md) — A vector with one in all lanes.
- [zero](zero-1xe4n.md) — A vector with zero in all lanes.
- [zero](zero-6rkq8.md) — A vector with zero in all lanes.

### Type Methods

- [random(in:)](<random(in_)-3wdfs.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:)](<random(in_)-6jl8o.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:using:)](<random(in_using_)-6da4k.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-7x9mr.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
