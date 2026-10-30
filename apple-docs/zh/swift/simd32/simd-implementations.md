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
doc_path: /documentation/swift/simd32/simd-implementations
source_url: 'https://developer.apple.com/documentation/swift/simd32/simd-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd32/simd-implementations.json'
content_hash: 'sha256:d70c41a4a104ecc7'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [SIMD 向量类型](../simd-vector-types.md) · [SIMD32](../simd32.md)

# SIMD 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [&(_:_:)](<&(____)-3y4ee.md>)
- [&(_:_:)](<&(____)-5hn2d.md>)
- [&(_:_:)](<&(____)-6m27n.md>)
- [&*(_:_:)](<&_(____)-18c2j.md>)
- [&*(_:_:)](<&_(____)-39jwx.md>)
- [&*(_:_:)](<&_(____)-7snfm.md>)
- [&*=(_:_:)](<&_=(____)-317ft.md>)
- [&*=(_:_:)](<&_=(____)-4o8xl.md>)
- [&+(_:_:)](<&+(____)-2klka.md>)
- [&+(_:_:)](<&+(____)-5s8y2.md>)
- [&+(_:_:)](<&+(____)-6wi7o.md>)
- [&+=(_:_:)](<&+=(____)-1ho7b.md>)
- [&+=(_:_:)](<&+=(____)-579bp.md>)
- [&-(_:_:)](<&-(____)-1e36y.md>)
- [&-(_:_:)](<&-(____)-4705x.md>)
- [&-(_:_:)](<&-(____)-8s9k4.md>)
- [&-=(_:_:)](<&-=(____)-594jw.md>)
- [&-=(_:_:)](<&-=(____)-5pn4x.md>)
- [&=(_:_:)](<&=(____)-5eswa.md>)
- [&=(_:_:)](<&=(____)-9jgzy.md>)
- [&\<\<(_:_:)](<&__(____)-29eng.md>)
- [&\>\>(_:_:)](<&__(____)-4gsmr.md>)
- [&\>\>(_:_:)](<&__(____)-78ish.md>)
- [&\<\<(_:_:)](<&__(____)-7zqu8.md>)
- [&\>\>(_:_:)](<&__(____)-89xqs.md>)
- [&\<\<(_:_:)](<&__(____)-9hia9.md>)
- [&\>\>=(_:_:)](<&__=(____)-3ali8.md>)
- [&\>\>=(_:_:)](<&__=(____)-762kk.md>)
- [&\<\<=(_:_:)](<&__=(____)-815bv.md>)
- [&\<\<=(_:_:)](<&__=(____)-92dly.md>)
- [*(_:_:)](<_(____)-2s55h.md>)
- [*(_:_:)](<_(____)-418m6.md>) _(已废弃)_
- [*(_:_:)](<_(____)-4x7hq.md>)
- [*(_:_:)](<_(____)-7q0sz.md>) _(已废弃)_
- [*(_:_:)](<_(____)-7shb0.md>) _(已废弃)_
- [*(_:_:)](<_(____)-9qya8.md>)
- [*=(_:_:)](<_=(____)-1i0tm.md>)
- [*=(_:_:)](<_=(____)-36zit.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-46f5z.md>) _(已废弃)_
- [*=(_:_:)](<_=(____)-8kra8.md>)
- [+(_:_:)](<+(____)-2phi3.md>)
- [+(_:_:)](<+(____)-473a4.md>) _(已废弃)_
- [+(_:_:)](<+(____)-4w7pm.md>)
- [+(_:_:)](<+(____)-59ak9.md>) _(已废弃)_
- [+(_:_:)](<+(____)-5rl9l.md>) _(已废弃)_
- [+(_:_:)](<+(____)-tzme.md>)
- [+=(_:_:)](<+=(____)-2gvba.md>)
- [+=(_:_:)](<+=(____)-318n3.md>) _(已废弃)_
- [+=(_:_:)](<+=(____)-6aukb.md>) _(已废弃)_
- [+=(_:_:)](<+=(____)-9yj49.md>)
- [-(_:)](<-(__).md>)
- [-(_:_:)](<-(____)-27153.md>)
- [-(_:_:)](<-(____)-2zgvi.md>)
- [-(_:_:)](<-(____)-4vvz.md>) _(已废弃)_
- [-(_:_:)](<-(____)-7rtph.md>) _(已废弃)_
- [-(_:_:)](<-(____)-8y206.md>)
- [-(_:_:)](<-(____)-ily3.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-1bm21.md>)
- [-=(_:_:)](<-=(____)-2aro2.md>) _(已废弃)_
- [-=(_:_:)](<-=(____)-4c6ab.md>)
- [-=(_:_:)](<-=(____)-6ujbc.md>) _(已废弃)_
- [.!=(_:_:)](<'.!=(____)-2u3yd.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-6dgv1.md>) — 返回一个向量掩码，其中包含逐元素不等比较的结果。
- [.!=(_:_:)](<'.!=(____)-968x6.md>) — 一个向量掩码，其中包含逐元素不等比较的结果。
- [.==(_:_:)](<'.==(____)-5y9oc.md>) — 一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-6oddf.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.==(_:_:)](<'.==(____)-8sr5e.md>) — 返回一个向量掩码，其中包含逐元素相等比较的结果。
- [.\<(_:_:)](<'._(____)-28t6e.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-4ahoi.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>(_:_:)](<'._(____)-6xg1q.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\<(_:_:)](<'._(____)-78u7r.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\<(_:_:)](<'._(____)-7bowa.md>) — 返回一个向量掩码，其中包含逐元素小于比较的结果。
- [.\>(_:_:)](<'._(____)-89ezy.md>) — 返回一个向量掩码，其中包含逐元素大于比较的结果。
- [.\>=(_:_:)](<'._=(____)-2c2t0.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-3t7xa.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-58tjg.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-5htya.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [.\>=(_:_:)](<'._=(____)-64co6.md>) — 返回一个向量掩码，其中包含逐元素大于等于比较的结果。
- [.\<=(_:_:)](<'._=(____)-9lx6q.md>) — 返回一个向量掩码，其中包含逐元素小于等于比较的结果。
- [==(_:_:)](<==(____).md>) — 返回一个布尔值，指示两个向量是否相等。
- [%(_:_:)](<_(____)-34uwb.md>)
- [|(_:_:)](<_(____)-3w1pz.md>)
- [^(_:_:)](<_(____)-414xo.md>)
- [|(_:_:)](<_(____)-44n0x.md>)
- [^(_:_:)](<_(____)-474ry.md>)
- [/(_:_:)](<_(____)-4lwb2.md>)
- [/(_:_:)](<_(____)-4n158.md>)
- [/(_:_:)](<_(____)-4ucgx.md>)
- [|(_:_:)](<_(____)-50id9.md>)
- [/(_:_:)](<_(____)-5j9uq.md>)
- [^(_:_:)](<_(____)-5y65m.md>)
- [%(_:_:)](<_(____)-6zy.md>)
- [%(_:_:)](<_(____)-7fea3.md>)
- [/(_:_:)](<_(____)-8nial.md>)
- [/(_:_:)](<_(____)-pk1j.md>)
- [|=(_:_:)](<_=(____)-11pnj.md>)
- [%=(_:_:)](<_=(____)-1vap7.md>)
- [/=(_:_:)](<_=(____)-20gc6.md>)
- [|=(_:_:)](<_=(____)-26y2h.md>)
- [/=(_:_:)](<_=(____)-2dyv7.md>)
- [/=(_:_:)](<_=(____)-2okko.md>)
- [^=(_:_:)](<_=(____)-49dhy.md>)
- [^=(_:_:)](<_=(____)-4prs.md>)
- [/=(_:_:)](<_=(____)-66xdx.md>)
- [%=(_:_:)](<_=(____)-8y875.md>)
- [~(_:)](<~(__).md>)

### 初始化方法

- [init(_:)](<init(__)-6afuc.md>) — 从给定的序列创建向量。
- [init(arrayLiteral:)](<init(arrayliteral_).md>) — 从指定的元素创建向量。
- [init(from:)](<init(from_).md>) — 通过从给定的解码器解码标量来创建新向量。
- [init(repeating:)](<init(repeating_)-1e473.md>) — 在所有通道中具有指定标量的向量。

### 实例属性

- [description](description.md) — 向量的文字描述。
- [indices](indices.md) — 用于向量下标操作的有效索引。
- [leadingZeroBitCount](leadingzerobitcount.md)
- [nonzeroBitCount](nonzerobitcount.md)
- [trailingZeroBitCount](trailingzerobitcount.md)

### 实例方法

- [addProduct(_:_:)](<addproduct(____)-2e6v4.md>)
- [addProduct(_:_:)](<addproduct(____)-65sbs.md>)
- [addProduct(_:_:)](<addproduct(____)-9epk7.md>)
- [addingProduct(_:_:)](<addingproduct(____)-7uual.md>)
- [addingProduct(_:_:)](<addingproduct(____)-8gka.md>)
- [addingProduct(_:_:)](<addingproduct(____)-8svnk.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-mfa1.md>)
- [clamp(lowerBound:upperBound:)](<clamp(lowerbound_upperbound_)-r8mu.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-3fn6n.md>)
- [clamped(lowerBound:upperBound:)](<clamped(lowerbound_upperbound_)-5edvy.md>)
- [encode(to:)](<encode(to_).md>) — 将此向量的标量编码到给定的编码器中，使用无键容器。
- [formSquareRoot()](<formsquareroot().md>)
- [hash(into:)](<hash(into_).md>) — 使用给定的哈希器对向量的元素进行哈希。
- [max()](<max()-36c8c.md>) — 向量中最大的标量。
- [max()](<max()-9t6zm.md>) — 向量中最大的元素。
- [min()](<min()-5cvw3.md>) — 向量中最小的元素。
- [min()](<min()-9a3ey.md>) — 向量中最小的标量。
- [replace(with:where:)](<replace(with_where_)-7o8hd.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replace(with:where:)](<replace(with_where_)-9jte6.md>) — 在 `mask` 为 `true` 的通道中，将此向量的元素替换为 `other` 中的元素。
- [replacing(with:where:)](<replacing(with_where_)-3v5ph.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素被 `other` 中的元素替换。
- [replacing(with:where:)](<replacing(with_where_)-h40g.md>) — 返回此向量的副本，其中在 `mask` 为 `true` 的通道中，元素为 `other`。
- [round(_:)](<round(__).md>)
- [rounded(_:)](<rounded(__).md>) — 按照指定的舍入 `rule`，将源向量的每个通道舍入为整数值而形成的向量。
- [squareRoot()](<squareroot().md>)
- [sum()](<sum().md>) — 向量中标量的和。
- [wrappedSum()](<wrappedsum().md>) — 返回向量中标量的和，使用回绕加法计算。

### 类型属性

- [one](one-13jdz.md) — 在所有通道中均为 1 的向量。
- [one](one-3mop8.md) — 在所有通道中均为 1 的向量。
- [zero](zero-2wd1r.md) — 在所有通道中均为 0 的向量。
- [zero](zero-3kong.md) — 在所有通道中均为 0 的向量。

### 类型方法

- [random(in:)](<random(in_)-3w4wf.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:)](<random(in_)-82yup.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值。
- [random(in:using:)](<random(in_using_)-7fl57.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
- [random(in:using:)](<random(in_using_)-7xfit.md>) — 返回一个向量，其所有通道中都是指定范围内的随机值，使用给定的生成器作为随机性来源。
