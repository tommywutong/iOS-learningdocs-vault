---
title: SIMD 实现
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
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [SIMD 向量类型](../simd-vector-types.md) · [SIMD16](../simd16.md)

# SIMD 实现

<sub>API 集合</sub>

## 主题

### 运算符

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
- [*(_:_:)](<_(____)-3ur7o.md>) _(已废弃)_
- [*(_:_:)](<_(____)-4pozo.md>)
- [*(_:_:)](<_(____)-7l65y.md>) _(已废弃)_
- [*(_:_:)](<_(____)-7whvl.md>) _(已废弃)_
- [*(_:_:)](<_(____)-9y6zm.md>)
- [*=(_:_:)](<_=(____)-1od2g.md>)
- [*=(_:_:)](<_=(____)-2zjkv.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-4dnsd.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-8scfm.md>)
- [+(_:_:)](<+(____)-10ebw.md>)
- [+(_:_:)](<+(____)-2i69l.md>)
- [+(_:_:)](<+(____)-40yo6.md>) _(已废弃)_
- [+(_:_:)](<+(____)-52yaj.md>) _(已废弃)_
- [+(_:_:)](<+(____)-53q5k.md>)
- [+(_:_:)](<+(____)-5z1ez.md>) _(已废弃)_
- [+=(_:_:)](<+=(____)-29mqk.md>)
- [+=(_:_:)](<+=(____)-2urad.md>) _(已废弃)_
- [+=(_:_:)](<+=(____)-5ciy.md>)
- [+=(_:_:)](<+=(____)-63jfd.md>) _(已废弃)_
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1zpzh.md>)
- [-(_:_:)](<-(____)-2t24k.md>)
- [-(_:_:)](<-(____)-7z2dr.md>) _(已废弃)_
- [-(_:_:)](<-(____)-946vg.md>)
- [-(_:_:)](<-(____)-bdg9.md>) _(已废弃)_
- [-(_:_:)](<-(____)-c6qt.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-15h6z.md>)
- [-=(_:_:)](<-=(____)-2iaa8.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-44xi9.md>)
- [-=(_:_:)](<-=(____)-6n3d6.md>) _(已废弃)_
- [.!=(_:_:)](<'.!=(____)-2mivz.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-679dj.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-8zu6g.md>) — 一个向量掩码，其中包含逐元素不等比较的结果。
- [.==(_:_:)](<'.==(____)-64qzq.md>) — 一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-6vtbl.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-8z3e8.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.\<(_:_:)](<'._(____)-2gbn0.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-436q8.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\<(_:_:)](<'._(____)-71lm5.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-73ut0.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\<(_:_:)](<'._(____)-7j4ug.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-8gxec.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>=(_:_:)](<'._=(____)-25vha.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-3mvms.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-52esm.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-5nyi8.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-6au0s.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-9s9fk.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [==(_:_:)](<==(____).md>) — 返回一个布尔值，指示两个向量是否相等。
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

### 初始化方法

- [init(_:)](<init(__)-64awu.md>) — 从给定的序列创建向量。
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — 从指定的元素创建向量。
- [init(from:)](<init(from_).md>) — 通过从给定的解码器解码标量来创建新向量。
- [init(repeating:)](<init(repeating_)-16o1h.md>) — 在所有通道中具有指定标量的向量。

### 实例属性

- [description](description.md) — 向量的文字描述。
- [indices](indices.md) — 用于向量下标操作的有效索引。
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### 实例方法

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
- [encode(to:)](<encode(to_).md>) — 将此向量的标量编码到给定的编码器中，使用无键容器。
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — 使用给定的哈希器对向量的元素进行哈希。
- [max()](<max()-2yw9y.md>) — 向量中最大的标量。
- [max()](<max()-ap.md>) — 向量中最大的元素。
- [min()](<min()-55nb5.md>) — 向量中最小的元素。
- [min()](<min()-9hjd4.md>) — 向量中最小的标量。
- [replace(with:where:)](<replace(with_where_)-7gncz.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replace(with:where:)](<replace(with_where_)-9cks4.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replacing(with:where:)](<replacing(with_where_)-42oan.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素被 `other` 中的元素替换。
- [replacing(with:where:)](<replacing(with_where_)-ng2a.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素为 `other`。
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — 按照指定的舍入 `rule`，将源向量的每个通道舍入为整数值而形成的向量。
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — 向量中标量的和。
- [wrappedSum()](<wrappedsum().md>) — 返回向量中标量的和，使用回绕加法计算。

### 类型属性

- [one](one-1azcd.md) — 在所有通道中均为 1 的向量。
- [one](one-3gc92.md) — 在所有通道中均为 1 的向量。
- [zero](zero-33lnp.md) — 在所有通道中均为 0 的向量。
- [zero](zero-3dg4m.md) — 在所有通道中均为 0 的向量。

### 类型方法

- [random(in:)](<random(in_)-42m5x.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:)](<random(in_)-8ajs3.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:using:)](<random(in_using_)-78ch5.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
- [random(in:using:)](<random(in_using_)-7rau7.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
