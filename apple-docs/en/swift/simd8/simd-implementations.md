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
doc_path: /documentation/swift/simd8/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd8/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd8/simd-implementations.json'
content_hash: 'sha256:fe6285ede16f4cf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [SIMD Vector Types](../simd-vector-types.md) · [SIMD8](../simd8.md)

# SIMD Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [&(_:_:)](<&(____)-5sp0e.md>)
- [&(_:_:)](<&(____)-6dcjs.md>)
- [&(_:_:)](<&(____)-9csd5.md>)
- [&*(_:_:)](<&_(____)-1tmkr.md>)
- [&*(_:_:)](<&_(____)-2ukc9.md>)
- [&*(_:_:)](<&_(____)-9lpf0.md>)
- [&*=(_:_:)](<&_=(____)-4n56w.md>)
- [&*=(_:_:)](<&_=(____)-4u70c.md>)
- [&+(_:_:)](<&+(____)-5je9i.md>)
- [&+(_:_:)](<&+(____)-6qthu.md>)
- [&+(_:_:)](<&+(____)-s3c0.md>)
- [&+=(_:_:)](<&+=(____)-15jmc.md>)
- [&+=(_:_:)](<&+=(____)-xkmr.md>)
- [&-(_:_:)](<&-(____)-4tkki.md>)
- [&-(_:_:)](<&-(____)-6uw6q.md>)
- [&-(_:_:)](<&-(____)-8tan0.md>)
- [&-=(_:_:)](<&-=(____)-530wa.md>)
- [&-=(_:_:)](<&-=(____)-8d5lv.md>)
- [&=(_:_:)](<&=(____)-586kj.md>)
- [&=(_:_:)](<&=(____)-5a4ls.md>)
- [&\<\<(_:_:)](<&__(____)-1cifw.md>)
- [&\>\>(_:_:)](<&__(____)-8w0hu.md>)
- [&\<\<(_:_:)](<&__(____)-93172.md>)
- [&\<\<(_:_:)](<&__(____)-9j4jc.md>)
- [&\>\>(_:_:)](<&__(____)-iqdy.md>)
- [&\>\>(_:_:)](<&__(____)-op9i.md>)
- [&\>\>=(_:_:)](<&__=(____)-2mxqy.md>)
- [&\>\>=(_:_:)](<&__=(____)-38cyr.md>)
- [&\<\<=(_:_:)](<&__=(____)-7dikc.md>)
- [&\<\<=(_:_:)](<&__=(____)-83he1.md>)
- [*(_:_:)](<_(____)-2huq3.md>)
- [*(_:_:)](<_(____)-4c84m.md>)
- [*(_:_:)](<_(____)-4lmnj.md>) _(deprecated)_
- [*(_:_:)](<_(____)-50hhc.md>) _(deprecated)_
- [*(_:_:)](<_(____)-6kqtm.md>) _(deprecated)_
- [*(_:_:)](<_(____)-9wsc8.md>)
- [*=(_:_:)](<_=(____)-27m64.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-3zhue.md>)
- [*=(_:_:)](<_=(____)-4j1xn.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-5qsdi.md>)
- [+(_:_:)](<+(____)-1h94n.md>) _(deprecated)_
- [+(_:_:)](<+(____)-1s9hf.md>)
- [+(_:_:)](<+(____)-2bhi5.md>)
- [+(_:_:)](<+(____)-62o3n.md>) _(deprecated)_
- [+(_:_:)](<+(____)-841fq.md>) _(deprecated)_
- [+(_:_:)](<+(____)-9w67l.md>)
- [+=(_:_:)](<+=(____)-13e1e.md>)
- [+=(_:_:)](<+=(____)-33hp7.md>)
- [+=(_:_:)](<+=(____)-3iuqz.md>) _(deprecated)_
- [+=(_:_:)](<+=(____)-4kc6w.md>) _(deprecated)_
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1eoar.md>)
- [-(_:_:)](<-(____)-59qe9.md>) _(deprecated)_
- [-(_:_:)](<-(____)-5hryr.md>)
- [-(_:_:)](<-(____)-5retq.md>) _(deprecated)_
- [-(_:_:)](<-(____)-8p6z1.md>)
- [-(_:_:)](<-(____)-8vqls.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-5efu0.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-6ar35.md>)
- [-=(_:_:)](<-=(____)-8p1mb.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-90g6w.md>)
- [.!=(_:_:)](<'.!=(____)-1o7kh.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-5kl0l.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-70jxh.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.==(_:_:)](<'.==(____)-1pyi8.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-4dg9j.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-85ylq.md>) — A vector mask with the result of a pointwise equality comparison.
- [.\<(_:_:)](<'._(____)-2n112.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-3ikq8.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<'._(____)-49yq2.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\<(_:_:)](<'._(____)-5lgdq.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-5wmbh.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>(_:_:)](<'._(____)-6yrys.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>=(_:_:)](<'._=(____)-132re.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-1ws7k.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-3lyor.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-41o9y.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-5k1es.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-9p7h9.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two vectors are equal.
- [|(_:_:)](<_(____)-1t6vi.md>)
- [/(_:_:)](<_(____)-2ntwq.md>)
- [/(_:_:)](<_(____)-2o5d7.md>)
- [%(_:_:)](<_(____)-2sn9f.md>)
- [/(_:_:)](<_(____)-2z76a.md>)
- [|(_:_:)](<_(____)-3pe30.md>)
- [/(_:_:)](<_(____)-3vsab.md>)
- [^(_:_:)](<_(____)-6f442.md>)
- [^(_:_:)](<_(____)-6fwr7.md>)
- [^(_:_:)](<_(____)-7vbmy.md>)
- [|(_:_:)](<_(____)-7yt9.md>)
- [%(_:_:)](<_(____)-903vr.md>)
- [/(_:_:)](<_(____)-932xh.md>)
- [%(_:_:)](<_(____)-9hy8d.md>)
- [/(_:_:)](<_(____)-9ilz9.md>)
- [/=(_:_:)](<_=(____)-18m89.md>)
- [|=(_:_:)](<_=(____)-1tcb0.md>)
- [/=(_:_:)](<_=(____)-5byj9.md>)
- [|=(_:_:)](<_=(____)-6kivi.md>)
- [%=(_:_:)](<_=(____)-721wj.md>)
- [/=(_:_:)](<_=(____)-7u65z.md>)
- [^=(_:_:)](<_=(____)-8jx1x.md>)
- [%=(_:_:)](<_=(____)-9a3t6.md>)
- [/=(_:_:)](<_=(____)-9iue6.md>)
- [^=(_:_:)](<_=(____)-suzf.md>)
- [~(_:)](<~(__).md>)

### Initializers

- [init(_:)](<init(__)-3ewxg.md>) — Creates a vector from the given sequence.
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — Creates a vector from the specified elements.
- [init(from:)](<init(from_).md>) — Creates a new vector by decoding scalars from the given decoder.
- [init(repeating:)](<init(repeating_)-97ws4.md>) — A vector with the specified scalar in all lanes.

### Instance Properties

- [description](description.md) — A textual description of the vector.
- [indices](indices.md) — The valid indices for subscripting the vector.
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### Instance Methods

- [addProduct(_:_:)](<addproduct(____)-24l2l.md>)
- [addProduct(_:_:)](<addproduct(____)-48c01.md>)
- [addProduct(_:_:)](<addproduct(____)-8hsd8.md>)
- [addingProduct(_:_:)](<addingproduct(____)-1n8kp.md>)
- [addingProduct(_:_:)](<addingproduct(____)-76qu8.md>)
- [addingProduct(_:_:)](<addingproduct(____)-94v6i.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-77hrb.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-9he39.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-4qnzr.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-8tmoc.md>)
- [encode(to:)](<encode(to_).md>) — Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — Hashes the elements of the vector using the given hasher.
- [max()](<max()-71om5.md>) — The greatest element in the vector.
- [max()](<max()-y0of.md>) — The greatest scalar in the vector.
- [min()](<min()-7qrdn.md>) — The least scalar in the vector.
- [min()](<min()-8s4qs.md>) — The least element in the vector.
- [replace(with:where:)](<replace(with_where_)-7e5tu.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<replace(with_where_)-7ys4t.md>) — Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-32kt0.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-3o9r2.md>) — Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — The sum of the scalars in the vector.
- [wrappedSum()](<wrappedsum().md>) — Returns the sum of the scalars in the vector, computed with wrapping addition.

### Type Properties

- [one](one-1gl43.md) — A vector with one in all lanes.
- [one](one-7efnf.md) — A vector with one in all lanes.
- [zero](zero-1xcz3.md) — A vector with zero in all lanes.
- [zero](zero-6rjkw.md) — A vector with zero in all lanes.

### Type Methods

- [random(in:)](<random(in_)-3w9ug.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:)](<random(in_)-6jhg8.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:using:)](<random(in_using_)-6d8vw.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-7x8fn.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
