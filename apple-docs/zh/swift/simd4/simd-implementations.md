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
doc_path: /documentation/swift/simd4/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd4/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd4/simd-implementations.json'
content_hash: 'sha256:adb88c73d252bbf9'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [SIMD 向量类型](../simd-vector-types.md) · [SIMD4](../simd4.md)

# SIMD 实现

<sub>API 集合</sub>

## 主题

### 运算符

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
- [*(_:_:)](<_(____)-4lqdj.md>) _(已废弃)_
- [*(_:_:)](<_(____)-50g1c.md>) _(已废弃)_
- [*(_:_:)](<_(____)-6kum2.md>) _(已废弃)_
- [*(_:_:)](<_(____)-9wqx4.md>)
- [*=(_:_:)](<_=(____)-27n78.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-3zlny.md>)
- [*=(_:_:)](<_=(____)-4iyd7.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-5qw5a.md>)
- [+(_:_:)](<+(____)-1h7vz.md>) _(已废弃)_
- [+(_:_:)](<+(____)-1s5sj.md>)
- [+(_:_:)](<+(____)-2bds5.md>)
- [+(_:_:)](<+(____)-62rmr.md>) _(已废弃)_
- [+(_:_:)](<+(____)-842lq.md>) _(已废弃)_
- [+(_:_:)](<+(____)-9w9vl.md>)
- [+=(_:_:)](<+=(____)-13aaq.md>)
- [+=(_:_:)](<+=(____)-33gh7.md>)
- [+=(_:_:)](<+=(____)-3itnf.md>) _(已废弃)_
- [+=(_:_:)](<+=(____)-4kfxk.md>) _(已废弃)_
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1epj7.md>)
- [-(_:_:)](<-(____)-59rjl.md>) _(已废弃)_
- [-(_:_:)](<-(____)-5hvnn.md>)
- [-(_:_:)](<-(____)-5rdme.md>) _(已废弃)_
- [-(_:_:)](<-(____)-8par9.md>)
- [-(_:_:)](<-(____)-8vs0w.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-5eh2w.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-6asc1.md>)
- [-=(_:_:)](<-=(____)-8oxw3.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-90eug.md>)
- [.!=(_:_:)](<'.!=(____)-1o6bl.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-5kor1.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-70nnx.md>) — 一个向量掩码，其中包含逐元素不等比较的结果。
- [.==(_:_:)](<'.==(____)-1q28g.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-4deu7.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-862bq.md>) — 一个向量掩码，其中包含逐元素相等比较的结果。
- [.\<(_:_:)](<'._(____)-2n4ry.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-3iokg.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\<(_:_:)](<'._(____)-49xlm.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\<(_:_:)](<'._(____)-5lcly.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-5wiit.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>(_:_:)](<'._(____)-6yo8s.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>=(_:_:)](<'._=(____)-136h6.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-1wt9c.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-3m2gb.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-41pqm.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-5k06k.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-9pb8l.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [==(_:_:)](<==(____).md>) — 返回一个布尔值，指示两个向量是否相等。
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

### 初始化方法

- [init(_:)](<init(__)-3eyf0.md>) — 从给定的序列创建向量。
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — 从指定的元素创建向量。
- [init(from:)](<init(from_).md>) — 通过从给定的解码器解码标量来创建新向量。
- [init(repeating:)](<init(repeating_)-97szw.md>) — 在所有通道中具有指定标量的向量。

### 实例属性

- [description](description.md) — 向量的文字描述。
- [indices](indices.md) — 用于向量下标操作的有效索引。
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### 实例方法

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
- [encode(to:)](<encode(to_).md>) — 将此向量的标量编码到给定的编码器中，使用无键容器。
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — 使用给定的哈希器对向量的元素进行哈希。
- [max()](<max()-71kv9.md>) — 向量中最大的元素。
- [max()](<max()-xww7.md>) — 向量中最大的标量。
- [min()](<min()-7qq8b.md>) — 向量中最小的标量。
- [min()](<min()-8s3i4.md>) — 向量中最小的元素。
- [replace(with:where:)](<replace(with_where_)-7e4sy.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replace(with:where:)](<replace(with_where_)-7yqkl.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replacing(with:where:)](<replacing(with_where_)-32h18.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素被 `other` 中的元素替换。
- [replacing(with:where:)](<replacing(with_where_)-3o8ie.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素为 `other`。
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — 按照指定的舍入 `rule`，将源向量的每个通道舍入为整数值而形成的向量。
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — 向量中标量的和。
- [wrappedSum()](<wrappedsum().md>) — 返回向量中标量的和，使用回绕加法计算。

### 类型属性

- [one](one-1ghcj.md) — 在所有通道中均为 1 的向量。
- [one](one-7ejbf.md) — 在所有通道中均为 1 的向量。
- [zero](zero-1xe4n.md) — 在所有通道中均为 0 的向量。
- [zero](zero-6rkq8.md) — 在所有通道中均为 0 的向量。

### 类型方法

- [random(in:)](<random(in_)-3wdfs.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:)](<random(in_)-6jl8o.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:using:)](<random(in_using_)-6da4k.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
- [random(in:using:)](<random(in_using_)-7x9mr.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
