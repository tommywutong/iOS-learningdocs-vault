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
doc_path: /documentation/swift/simd64/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd64/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd64/simd-implementations.json'
content_hash: 'sha256:1f6fcfdb2bd09ce1'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [SIMD 向量类型](../simd-vector-types.md) · [SIMD64](../simd64.md)

# SIMD 实现

<sub>API 集合</sub>

## 主题

### 运算符

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
- [*(_:_:)](<_(____)-3kbvd.md>) _(已废弃)_
- [*(_:_:)](<_(____)-4mjjh.md>)
- [*(_:_:)](<_(____)-7agrf.md>) _(已废弃)_
- [*(_:_:)](<_(____)-80pyw.md>) _(已废弃)_
- [*(_:_:)](<_(____)-99vn7.md>)
- [*=(_:_:)](<_=(____)-1z3id.md>)
- [*=(_:_:)](<_=(____)-3ntoe.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-3vpxk.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-8vgob.md>)
- [+(_:_:)](<+(____)-27h1w.md>)
- [+(_:_:)](<+(____)-3wpa7.md>) _(已废弃)_
- [+(_:_:)](<+(____)-4ff09.md>)
- [+(_:_:)](<+(____)-5r8e2.md>) _(已废弃)_
- [+(_:_:)](<+(____)-69rpi.md>) _(已废弃)_
- [+(_:_:)](<+(____)-jka1.md>)
- [+=(_:_:)](<+=(____)-26hfp.md>)
- [+=(_:_:)](<+=(____)-2kbw8.md>) _(已废弃)_
- [+=(_:_:)](<+=(____)-5sues.md>) _(已废弃)_
- [+=(_:_:)](<+=(____)-9gmka.md>)
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-1q4hs.md>)
- [-(_:_:)](<-(____)-2pwx9.md>)
- [-(_:_:)](<-(____)-7ar0m.md>) _(已废弃)_
- [-(_:_:)](<-(____)-8nctl.md>)
- [-(_:_:)](<-(____)-fbas.md>) _(已废弃)_
- [-(_:_:)](<-(____)-tcjo.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-117zm.md>)
- [-=(_:_:)](<-=(____)-20ca5.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-4lsxo.md>)
- [-=(_:_:)](<-=(____)-7bdez.md>) _(已废弃)_
- [.!=(_:_:)](<'.!=(____)-2c3lu.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-5wk7u.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-8woo1.md>) — 一个向量掩码，其中包含逐元素不等比较的结果。
- [.==(_:_:)](<'.==(____)-68z13.md>) — 一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-75g24.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-99k0t.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.\<(_:_:)](<'._(____)-1s0b9.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-3tla5.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>(_:_:)](<'._(____)-6n0pt.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\<(_:_:)](<'._(____)-6yfx0.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-7smbh.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\<(_:_:)](<'._(____)-7srs5.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>=(_:_:)](<'._=(____)-1v69f.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-34q4.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-4b5ol.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-4y5lb.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-4zn9d.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-6dy5p.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [==(_:_:)](<==(____).md>) — 返回一个布尔值，指示两个向量是否相等。
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

### 初始化方法

- [init(_:)](<init(__)-6l6bn.md>) — 从给定的序列创建向量。
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — 从指定的元素创建向量。
- [init(from:)](<init(from_).md>) — 通过从给定的解码器解码标量来创建新向量。
- [init(repeating:)](<init(repeating_)-1uy8k.md>) — 在所有通道中具有指定标量的向量。

### 实例属性

- [description](description.md) — 向量的文字描述。
- [indices](indices.md) — 用于向量下标操作的有效索引。
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### 实例方法

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
- [encode(to:)](<encode(to_).md>) — 将此向量的标量编码到给定的编码器中，使用无键容器。
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — 使用给定的哈希器对向量的元素进行哈希。
- [max()](<max()-3n69z.md>) — 向量中最大的标量。
- [max()](<max()-9irq5.md>) — 向量中最大的元素。
- [min()](<min()-52hug.md>) — 向量中最小的元素。
- [min()](<min()-9s02d.md>) — 向量中最小的标量。
- [replace(with:where:)](<replace(with_where_)-7685a.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replace(with:where:)](<replace(with_where_)-99fgt.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replacing(with:where:)](<replacing(with_where_)-3ecx2.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素被 `other` 中的元素替换。
- [replacing(with:where:)](<replacing(with_where_)-xwqn.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素为 `other`。
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — 按照指定的舍入 `rule`，将源向量的每个通道舍入为整数值而形成的向量。
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — 向量中标量的和。
- [wrappedSum()](<wrappedsum().md>) — 返回向量中标量的和，使用回绕加法计算。

### 类型属性

- [one](one-1lpug.md) — 在所有通道中均为 1 的向量。
- [one](one-44mp3.md) — 在所有通道中均为 1 的向量。
- [zero](zero-2faik.md) — 在所有通道中均为 0 的向量。
- [zero](zero-3vf97.md) — 在所有通道中均为 0 的向量。

### 类型方法

- [random(in:)](<random(in_)-46u2s.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:)](<random(in_)-8do2i.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:using:)](<random(in_using_)-7qbkk.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
- [random(in:using:)](<random(in_using_)-8863m.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
