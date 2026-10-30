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
doc_path: /documentation/swift/simd2/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd2/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd2/simd-implementations.json'
content_hash: 'sha256:1a21f738067fcf2d'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [SIMD 向量类型](../simd-vector-types.md) · [SIMD2](../simd2.md)

# SIMD 实现

<sub>API 集合</sub>

## 主题

### 运算符

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
- [*(_:_:)](<_(____)-4lojf.md>) _(已废弃)_
- [*(_:_:)](<_(____)-50ffc.md>) _(已废弃)_
- [*(_:_:)](<_(____)-6ktum.md>) _(已废弃)_
- [*(_:_:)](<_(____)-9wp8w.md>)
- [*=(_:_:)](<_=(____)-27nt8.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-3zjz6.md>)
- [*=(_:_:)](<_=(____)-4j02f.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-5qufm.md>)
- [+(_:_:)](<+(____)-1h79f.md>) _(已废弃)_
- [+(_:_:)](<+(____)-1s6ev.md>)
- [+(_:_:)](<+(____)-2begd.md>)
- [+(_:_:)](<+(____)-62pyv.md>) _(已废弃)_
- [+(_:_:)](<+(____)-844oq.md>) _(已废弃)_
- [+(_:_:)](<+(____)-9w9bt.md>)
- [+=(_:_:)](<+=(____)-13ati.md>)
- [+=(_:_:)](<+=(____)-33g1r.md>)
- [+=(_:_:)](<+=(____)-3it33.md>) _(已废弃)_
- [+=(_:_:)](<+=(____)-4kf28.md>) _(已废弃)_
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1eq67.md>)
- [-(_:_:)](<-(____)-59t7d.md>) _(已废弃)_
- [-(_:_:)](<-(____)-5hv3b.md>)
- [-(_:_:)](<-(____)-5rbq2.md>) _(已废弃)_
- [-(_:_:)](<-(____)-8pa31.md>)
- [-(_:_:)](<-(____)-8vsnc.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-5eiqo.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-6au1l.md>)
- [-=(_:_:)](<-=(____)-8oyin.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-90e80.md>)
- [.!=(_:_:)](<'.!=(____)-1o5rd.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-5ko8d.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-70n1x.md>) — 一个向量掩码，其中包含逐元素不等比较的结果。
- [.==(_:_:)](<'.==(____)-1q06g.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-4dd4z.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-860hm.md>) — 一个向量掩码，其中包含逐元素相等比较的结果。
- [.\<(_:_:)](<'._(____)-2n2w2.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-3inug.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\<(_:_:)](<'._(____)-49wsu.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\<(_:_:)](<'._(____)-5ldki.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-5wj3h.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>(_:_:)](<'._(____)-6yov0.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>=(_:_:)](<'._=(____)-134li.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-1wtvs.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-3m1tr.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-41ri2.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-5jyc4.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-9pao5.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [==(_:_:)](<==(____).md>) — 返回一个布尔值，指示两个向量是否相等。
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

### 初始化方法

- [init(_:)](<init(__)-3f03w.md>) — 从给定的序列创建向量。
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — 从指定的元素创建向量。
- [init(from:)](<init(from_).md>) — 通过从给定的解码器解码标量来创建新向量。
- [init(repeating:)](<init(repeating_)-97uo4.md>) — 在所有通道中具有指定标量的向量。

### 实例属性

- [description](description.md) — 向量的文字描述。
- [indices](indices.md) — 用于向量下标操作的有效索引。
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### 实例方法

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
- [encode(to:)](<encode(to_).md>) — 将此向量的标量编码到给定的编码器中，使用无键容器。
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — 使用给定的哈希器对向量的元素进行哈希。
- [max()](<max()-71lal.md>) — 向量中最大的元素。
- [max()](<max()-xykz.md>) — 向量中最大的标量。
- [min()](<min()-7qoe7.md>) — 向量中最小的标量。
- [min()](<min()-8s2vo.md>) — 向量中最小的元素。
- [replace(with:where:)](<replace(with_where_)-7e48m.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replace(with:where:)](<replace(with_where_)-7yq25.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replacing(with:where:)](<replacing(with_where_)-32hlo.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素被 `other` 中的元素替换。
- [replacing(with:where:)](<replacing(with_where_)-3o6pm.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素为 `other`。
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — 按照指定的舍入 `rule`，将源向量的每个通道舍入为整数值而形成的向量。
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — 向量中标量的和。
- [wrappedSum()](<wrappedsum().md>) — 返回向量中标量的和，使用回绕加法计算。

### 类型属性

- [one](one-1gj1r.md) — 在所有通道中均为 1 的向量。
- [one](one-7ehgf.md) — 在所有通道中均为 1 的向量。
- [zero](zero-1xeqr.md) — 在所有通道中均为 0 的向量。
- [zero](zero-6rme0.md) — 在所有通道中均为 0 的向量。

### 类型方法

- [random(in:)](<random(in_)-3wbi8.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:)](<random(in_)-6jji8.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:using:)](<random(in_using_)-6dc38.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
- [random(in:using:)](<random(in_using_)-7xbgv.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
