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
doc_path: /documentation/swift/simd8/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd8/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd8/simd-implementations.json'
content_hash: 'sha256:fe6285ede16f4cf6'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [SIMD 向量类型](../simd-vector-types.md) · [SIMD8](../simd8.md)

# SIMD 实现

<sub>API 集合</sub>

## 主题

### 运算符

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
- [*(_:_:)](<_(____)-4lmnj.md>) _(已废弃)_
- [*(_:_:)](<_(____)-50hhc.md>) _(已废弃)_
- [*(_:_:)](<_(____)-6kqtm.md>) _(已废弃)_
- [*(_:_:)](<_(____)-9wsc8.md>)
- [*=(_:_:)](<_=(____)-27m64.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-3zhue.md>)
- [*=(_:_:)](<_=(____)-4j1xn.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-5qsdi.md>)
- [+(_:_:)](<+(____)-1h94n.md>) _(已废弃)_
- [+(_:_:)](<+(____)-1s9hf.md>)
- [+(_:_:)](<+(____)-2bhi5.md>)
- [+(_:_:)](<+(____)-62o3n.md>) _(已废弃)_
- [+(_:_:)](<+(____)-841fq.md>) _(已废弃)_
- [+(_:_:)](<+(____)-9w67l.md>)
- [+=(_:_:)](<+=(____)-13e1e.md>)
- [+=(_:_:)](<+=(____)-33hp7.md>)
- [+=(_:_:)](<+=(____)-3iuqz.md>) _(已废弃)_
- [+=(_:_:)](<+=(____)-4kc6w.md>) _(已废弃)_
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1eoar.md>)
- [-(_:_:)](<-(____)-59qe9.md>) _(已废弃)_
- [-(_:_:)](<-(____)-5hryr.md>)
- [-(_:_:)](<-(____)-5retq.md>) _(已废弃)_
- [-(_:_:)](<-(____)-8p6z1.md>)
- [-(_:_:)](<-(____)-8vqls.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-5efu0.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-6ar35.md>)
- [-=(_:_:)](<-=(____)-8p1mb.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-90g6w.md>)
- [.!=(_:_:)](<'.!=(____)-1o7kh.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-5kl0l.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-70jxh.md>) — 一个向量掩码，其中包含逐元素不等比较的结果。
- [.==(_:_:)](<'.==(____)-1pyi8.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-4dg9j.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-85ylq.md>) — 一个向量掩码，其中包含逐元素相等比较的结果。
- [.\<(_:_:)](<'._(____)-2n112.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-3ikq8.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\<(_:_:)](<'._(____)-49yq2.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\<(_:_:)](<'._(____)-5lgdq.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-5wmbh.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>(_:_:)](<'._(____)-6yrys.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>=(_:_:)](<'._=(____)-132re.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-1ws7k.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-3lyor.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-41o9y.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-5k1es.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-9p7h9.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [==(_:_:)](<==(____).md>) — 返回一个布尔值，指示两个向量是否相等。
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

### 初始化方法

- [init(_:)](<init(__)-3ewxg.md>) — 从给定的序列创建向量。
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — 从指定的元素创建向量。
- [init(from:)](<init(from_).md>) — 通过从给定的解码器解码标量来创建新向量。
- [init(repeating:)](<init(repeating_)-97ws4.md>) — 在所有通道中具有指定标量的向量。

### 实例属性

- [description](description.md) — 向量的文字描述。
- [indices](indices.md) — 用于向量下标操作的有效索引。
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### 实例方法

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
- [encode(to:)](<encode(to_).md>) — 将此向量的标量编码到给定的编码器中，使用无键容器。
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — 使用给定的哈希器对向量的元素进行哈希。
- [max()](<max()-71om5.md>) — 向量中最大的元素。
- [max()](<max()-y0of.md>) — 向量中最大的标量。
- [min()](<min()-7qrdn.md>) — 向量中最小的标量。
- [min()](<min()-8s4qs.md>) — 向量中最小的元素。
- [replace(with:where:)](<replace(with_where_)-7e5tu.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replace(with:where:)](<replace(with_where_)-7ys4t.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replacing(with:where:)](<replacing(with_where_)-32kt0.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素被 `other` 中的元素替换。
- [replacing(with:where:)](<replacing(with_where_)-3o9r2.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素为 `other`。
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — 按照指定的舍入 `rule`，将源向量的每个通道舍入为整数值而形成的向量。
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — 向量中标量的和。
- [wrappedSum()](<wrappedsum().md>) — 返回向量中标量的和，使用回绕加法计算。

### 类型属性

- [one](one-1gl43.md) — 在所有通道中均为 1 的向量。
- [one](one-7efnf.md) — 在所有通道中均为 1 的向量。
- [zero](zero-1xcz3.md) — 在所有通道中均为 0 的向量。
- [zero](zero-6rjkw.md) — 在所有通道中均为 0 的向量。

### 类型方法

- [random(in:)](<random(in_)-3w9ug.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:)](<random(in_)-6jhg8.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:using:)](<random(in_using_)-6d8vw.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
- [random(in:using:)](<random(in_using_)-7x8fn.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
