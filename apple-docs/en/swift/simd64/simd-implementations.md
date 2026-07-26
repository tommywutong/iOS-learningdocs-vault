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
doc_path: /documentation/swift/simd64/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd64/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd64/simd-implementations.json'
content_hash: 'sha256:1f6fcfdb2bd09ce1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [SIMD Vector Types](../simd-vector-types.md) · [SIMD64](../simd64.md)

# SIMD Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [&(_:_:)](<&(____)-48kwh.md>)
- [&(_:_:)](<&(____)-5sdoy.md>)
- [&(_:_:)](<&(____)-659cg.md>)
- [&*(_:_:)](<&_(____)-3k94q.md>)
- [&*(_:_:)](<&_(____)-7amwd.md>)
- [&*(_:_:)](<&_(____)-rfmc.md>)
- [&*=(_:_:)](<&_=(____)-2qjaa.md>)
- [&*=(_:_:)](<&_=(____)-551ly.md>)
- [&+(_:_:)](<&+(____)-31fpl.md>)
- [&+(_:_:)](<&+(____)-69btx.md>)
- [&+(_:_:)](<&+(____)-6m447.md>)
- [&+=(_:_:)](<&+=(____)-1s4xc.md>)
- [&+=(_:_:)](<&+=(____)-5gvtu.md>)
- [&-(_:_:)](<&-(____)-1oiep.md>)
- [&-(_:_:)](<&-(____)-4gmrm.md>)
- [&-(_:_:)](<&-(____)-8b6pz.md>)
- [&-=(_:_:)](<&-=(____)-4ygnj.md>)
- [&-=(_:_:)](<&-=(____)-67jym.md>)
- [&=(_:_:)](<&=(____)-5wpkl.md>)
- [&=(_:_:)](<&=(____)-98sr1.md>)
- [&\<\<(_:_:)](<&__(____)-1ri1r.md>)
- [&\>\>(_:_:)](<&__(____)-3zzo0.md>)
- [&\<\<(_:_:)](<&__(____)-7iub3.md>)
- [&\>\>(_:_:)](<&__(____)-7j9fy.md>)
- [&\>\>(_:_:)](<&__(____)-8keg3.md>)
- [&\<\<(_:_:)](<&__(____)-9rxgq.md>)
- [&\>\>=(_:_:)](<&__=(____)-3sibz.md>)
- [&\>\>=(_:_:)](<&__=(____)-6veiv.md>)
- [&\<\<=(_:_:)](<&__=(____)-8i87o.md>)
- [&\<\<=(_:_:)](<&__=(____)-8rzj9.md>)
- [*(_:_:)](<_(____)-38y62.md>)
- [*(_:_:)](<_(____)-3kbvd.md>) _(deprecated)_
- [*(_:_:)](<_(____)-4mjjh.md>)
- [*(_:_:)](<_(____)-7agrf.md>) _(deprecated)_
- [*(_:_:)](<_(____)-80pyw.md>) _(deprecated)_
- [*(_:_:)](<_(____)-99vn7.md>)
- [*=(_:_:)](<_=(____)-1z3id.md>)
- [*=(_:_:)](<_=(____)-3ntoe.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-3vpxk.md>) _(deprecated)_
- [*=(_:_:)](<_=(____)-8vgob.md>)
- [+(_:_:)](<+(____)-27h1w.md>)
- [+(_:_:)](<+(____)-3wpa7.md>) _(deprecated)_
- [+(_:_:)](<+(____)-4ff09.md>)
- [+(_:_:)](<+(____)-5r8e2.md>) _(deprecated)_
- [+(_:_:)](<+(____)-69rpi.md>) _(deprecated)_
- [+(_:_:)](<+(____)-jka1.md>)
- [+=(_:_:)](<+=(____)-26hfp.md>)
- [+=(_:_:)](<+=(____)-2kbw8.md>) _(deprecated)_
- [+=(_:_:)](<+=(____)-5sues.md>) _(deprecated)_
- [+=(_:_:)](<+=(____)-9gmka.md>)
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1q4hs.md>)
- [-(_:_:)](<-(____)-2pwx9.md>)
- [-(_:_:)](<-(____)-7ar0m.md>) _(deprecated)_
- [-(_:_:)](<-(____)-8nctl.md>)
- [-(_:_:)](<-(____)-fbas.md>) _(deprecated)_
- [-(_:_:)](<-(____)-tcjo.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-117zm.md>)
- [-=(_:_:)](<-=(____)-20ca5.md>) _(deprecated)_
- [-=(_:_:)](<-=(____)-4lsxo.md>)
- [-=(_:_:)](<-=(____)-7bdez.md>) _(deprecated)_
- [.!=(_:_:)](<'.!=(____)-2c3lu.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-5wk7u.md>) — Returns a vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<'.!=(____)-8woo1.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.==(_:_:)](<'.==(____)-68z13.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-75g24.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<'.==(____)-99k0t.md>) — Returns a vector mask with the result of a pointwise equality comparison.
- [.\<(_:_:)](<'._(____)-1s0b9.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-3tla5.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\>(_:_:)](<'._(____)-6n0pt.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<'._(____)-6yfx0.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>(_:_:)](<'._(____)-7smbh.md>) — Returns a vector mask with the result of a pointwise greater than comparison.
- [.\<(_:_:)](<'._(____)-7srs5.md>) — Returns a vector mask with the result of a pointwise less than comparison.
- [.\>=(_:_:)](<'._=(____)-1v69f.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-34q4.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-4b5ol.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-4y5lb.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\<=(_:_:)](<'._=(____)-4zn9d.md>) — Returns a vector mask with the result of a pointwise less than or equal comparison.
- [.\>=(_:_:)](<'._=(____)-6dy5p.md>) — Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two vectors are equal.
- [|(_:_:)](<_(____)-3e53o.md>)
- [|(_:_:)](<_(____)-3mmse.md>)
- [%(_:_:)](<_(____)-3mrhw.md>)
- [^(_:_:)](<_(____)-3rknz.md>)
- [/(_:_:)](<_(____)-4b85p.md>)
- [^(_:_:)](<_(____)-4p1dd.md>)
- [/(_:_:)](<_(____)-53v87.md>)
- [|(_:_:)](<_(____)-5axk6.md>)
- [/(_:_:)](<_(____)-5bfge.md>)
- [/(_:_:)](<_(____)-5tz1l.md>)
- [^(_:_:)](<_(____)-6f021.md>)
- [%(_:_:)](<_(____)-7xkx0.md>)
- [/(_:_:)](<_(____)-8y8tm.md>)
- [%(_:_:)](<_(____)-9p4bu.md>)
- [/(_:_:)](<_(____)-f4mg.md>)
- [%=(_:_:)](<_=(____)-1d41k.md>)
- [/=(_:_:)](<_=(____)-2haal.md>)
- [|=(_:_:)](<_=(____)-2nqna.md>)
- [/=(_:_:)](<_=(____)-2opf0.md>)
- [/=(_:_:)](<_=(____)-2z9yb.md>)
- [^=(_:_:)](<_=(____)-3rd8x.md>)
- [/=(_:_:)](<_=(____)-6hdyq.md>)
- [%=(_:_:)](<_=(____)-98nne.md>)
- [^=(_:_:)](<_=(____)-9mati.md>)
- [|=(_:_:)](<_=(____)-r1oc.md>)
- [~(_:)](<~(__).md>)

### Initializers

- [init(_:)](<init(__)-6l6bn.md>) — Creates a vector from the given sequence.
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — Creates a vector from the specified elements.
- [init(from:)](<init(from_).md>) — Creates a new vector by decoding scalars from the given decoder.
- [init(repeating:)](<init(repeating_)-1uy8k.md>) — A vector with the specified scalar in all lanes.

### Instance Properties

- [description](description.md) — A textual description of the vector.
- [indices](indices.md) — The valid indices for subscripting the vector.
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### Instance Methods

- [addProduct(_:_:)](<addproduct(____)-2v9r3.md>)
- [addProduct(_:_:)](<addproduct(____)-6gitz.md>)
- [addProduct(_:_:)](<addproduct(____)-94bac.md>)
- [addingProduct(_:_:)](<addingproduct(____)-8bwvm.md>)
- [addingProduct(_:_:)](<addingproduct(____)-99pn7.md>)
- [addingProduct(_:_:)](<addingproduct(____)-ivsx.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-ac6p.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-wuiq.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-3qdwo.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-5ot5h.md>)
- [encode(to:)](<encode(to_).md>) — Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — Hashes the elements of the vector using the given hasher.
- [max()](<max()-3n69z.md>) — The greatest scalar in the vector.
- [max()](<max()-9irq5.md>) — The greatest element in the vector.
- [min()](<min()-52hug.md>) — The least element in the vector.
- [min()](<min()-9s02d.md>) — The least scalar in the vector.
- [replace(with:where:)](<replace(with_where_)-7685a.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<replace(with_where_)-99fgt.md>) — Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-3ecx2.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<replacing(with_where_)-xwqn.md>) — Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — The sum of the scalars in the vector.
- [wrappedSum()](<wrappedsum().md>) — Returns the sum of the scalars in the vector, computed with wrapping addition.

### Type Properties

- [one](one-1lpug.md) — A vector with one in all lanes.
- [one](one-44mp3.md) — A vector with one in all lanes.
- [zero](zero-2faik.md) — A vector with zero in all lanes.
- [zero](zero-3vf97.md) — A vector with zero in all lanes.

### Type Methods

- [random(in:)](<random(in_)-46u2s.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:)](<random(in_)-8do2i.md>) — Returns a vector with random values from within the specified range in all lanes.
- [random(in:using:)](<random(in_using_)-7qbkk.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-8863m.md>) — Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
