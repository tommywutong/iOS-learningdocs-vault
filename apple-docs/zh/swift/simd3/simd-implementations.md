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
doc_path: /documentation/swift/simd3/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd3/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd3/simd-implementations.json'
content_hash: 'sha256:88d19e1961986ea3'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [SIMD 向量类型](../simd-vector-types.md) · [SIMD3](../simd3.md)

# SIMD 实现

<sub>API 集合</sub>

## 主题

### 运算符

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
- [*(_:_:)](<_(____)-4lo7f.md>) _(已废弃)_
- [*(_:_:)](<_(____)-50fba.md>) _(已废弃)_
- [*(_:_:)](<_(____)-6ktkg.md>) _(已废弃)_
- [*(_:_:)](<_(____)-9wplu.md>)
- [*=(_:_:)](<_=(____)-27oce.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-3zjhs.md>)
- [*=(_:_:)](<_=(____)-4j0iv.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-5qujk.md>)
- [+(_:_:)](<+(____)-1h7rv.md>) _(已废弃)_
- [+(_:_:)](<+(____)-1s6av.md>)
- [+(_:_:)](<+(____)-2bek1.md>)
- [+(_:_:)](<+(____)-62q9z.md>) _(已废弃)_
- [+(_:_:)](<+(____)-844rw.md>) _(已废弃)_
- [+(_:_:)](<+(____)-9w8yd.md>)
- [+=(_:_:)](<+=(____)-13ac4.md>)
- [+=(_:_:)](<+=(____)-33ge7.md>)
- [+=(_:_:)](<+=(____)-3islb.md>) _(已废弃)_
- [+=(_:_:)](<+=(____)-4kezy.md>) _(已废弃)_
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1eqhb.md>)
- [-(_:_:)](<-(____)-59t4d.md>) _(已废弃)_
- [-(_:_:)](<-(____)-5hurb.md>)
- [-(_:_:)](<-(____)-5rbfs.md>) _(已废弃)_
- [-(_:_:)](<-(____)-8pag1.md>)
- [-(_:_:)](<-(____)-8vs62.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-5ej92.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-6att9.md>)
- [-=(_:_:)](<-=(____)-8oysv.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-90eji.md>)
- [.!=(_:_:)](<'.!=(____)-1o5ed.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-5knpd.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-70ndl.md>) — 一个向量掩码，其中包含逐元素不等比较的结果。
- [.==(_:_:)](<'.==(____)-1q0oq.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-4ddir.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-8605k.md>) — 一个向量掩码，其中包含逐元素相等比较的结果。
- [.\<(_:_:)](<'._(____)-2n374.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-3inh2.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\<(_:_:)](<'._(____)-49xao.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\<(_:_:)](<'._(____)-5ld34.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-5wj69.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>(_:_:)](<'._(____)-6yoj2.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>=(_:_:)](<'._=(____)-134b8.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-1wtru.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-3m1wf.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-41rws.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-5jyme.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-9paeh.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [==(_:_:)](<==(____).md>) — 返回一个布尔值，指示两个向量是否相等。
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

### 初始化方法

- [init(_:)](<init(__)-3f00q.md>) — 从给定的序列创建向量。
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — 从指定的元素创建向量。
- [init(from:)](<init(from_).md>) — 通过从给定的解码器解码标量来创建新向量。
- [init(repeating:)](<init(repeating_)-97v6a.md>) — 在所有通道中具有指定标量的向量。

### 实例属性

- [description](description.md) — 向量的文字描述。
- [indices](indices.md) — 用于向量下标操作的有效索引。
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### 实例方法

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
- [encode(to:)](<encode(to_).md>) — 将此向量的标量编码到给定的编码器中，使用无键容器。
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — 使用给定的哈希器对向量的元素进行哈希。
- [max()](<max()-71ltd.md>) — 向量中最大的元素。
- [max()](<max()-xz2j.md>) — 向量中最大的标量。
- [min()](<min()-7qoof.md>) — 向量中最小的标量。
- [min()](<min()-8s36y.md>) — 向量中最小的元素。
- [replace(with:where:)](<replace(with_where_)-7e3ns.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replace(with:where:)](<replace(with_where_)-7yqk1.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replacing(with:where:)](<replacing(with_where_)-32h3i.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素被 `other` 中的元素替换。
- [replacing(with:where:)](<replacing(with_where_)-3o6zs.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素为 `other`。
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — 按照指定的舍入 `rule`，将源向量的每个通道舍入为整数值而形成的向量。
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — 向量中标量的和。
- [wrappedSum()](<wrappedsum().md>) — 返回向量中标量的和，使用回绕加法计算。

### 类型属性

- [one](one-1gjj3.md) — 在所有通道中均为 1 的向量。
- [one](one-7ehtb.md) — 在所有通道中均为 1 的向量。
- [zero](zero-1xegj.md) — 在所有通道中均为 0 的向量。
- [zero](zero-6rmb2.md) — 在所有通道中均为 0 的向量。

### 类型方法

- [random(in:)](<random(in_)-3wbg2.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:)](<random(in_)-6jj3m.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:using:)](<random(in_using_)-6dbs2.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
- [random(in:using:)](<random(in_using_)-7xbdr.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
