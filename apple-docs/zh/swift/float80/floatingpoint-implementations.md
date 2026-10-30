---
title: FloatingPoint 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/floatingpoint-implementations
source_url: 'https://developer.apple.com/documentation/swift/float80/floatingpoint-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/floatingpoint-implementations.json'
content_hash: 'sha256:219966b55bb95e38'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [Swift 标准库](../swift-standard-library.md) · [数字与基本值](../numbers-and-basic-values.md) · [特殊用途数值类型](../special-use-numeric-types.md) · [Float80](../float80.md)

# FloatingPoint 实现

<sub>API 集合</sub>

## 主题

### 运算符

- [*(_:_:)](<_(____).md>) — 将两个值相乘，得到它们的积，并舍入为可表示的值。
- [*=(_:_:)](<_=(____).md>) — 将两个值相乘，并把结果存储到左侧变量中，同时舍入为可表示的值。
- [+(_:_:)](<+(____).md>) — 将两个值相加，得到它们的和，并舍入为可表示的值。
- [+=(_:_:)](<+=(____).md>) — 将两个值相加，并把结果存储到左侧变量中，同时舍入为可表示的值。
- [-(_:)](<-(__).md>) — 计算一个值的加法逆元。
- [-(_:_:)](<-(____).md>) — 从一个值中减去另一个值，得到它们的差，并舍入为可表示的值。
- [-=(_:_:)](<-=(____).md>) — 用第一个值减去第二个值，并把差存储到左侧变量中，同时舍入为可表示的值。
- [/(_:_:)](<_(____).md>) — 用第一个值除以第二个值，返回商，并舍入为可表示的值。
- [\>(_:_:)](<_(____)-8otyc.md>)
- [/=(_:_:)](<_=(____).md>) — 用第一个值除以第二个值，并把商存储到左侧变量中，同时舍入为可表示的值。
- [\>=(_:_:)](<_=(____)-2myj1.md>)
- [\<=(_:_:)](<_=(____)-502lh.md>)

### 初始化方法

- [init(_:)](<init(__)-33oy4.md>) — 创建一个新值，舍入到最接近的可表示值。
- [init(_:)](<init(__)-42n91.md>) — 创建一个新值，舍入到最接近的可表示值。
- [init(exactly:)](<init(exactly_)-2t92j.md>) — 如果给定的整数可以被精确表示，则创建一个新值。
- [init(sign:exponent:significand:)](<init(sign_exponent_significand_).md>) — 根据给定的符号、指数和尾数创建一个新值。
- [init(signOf:magnitudeOf:)](<init(signof_magnitudeof_).md>) — 使用一个值的符号和另一个值的量级创建一个新的浮点值。
- [init(signOf:magnitudeOf:)](<init(signof_magnitudeof_)-t3cu.md>) — 使用一个值的符号和另一个值的量级创建一个新的浮点值。

### 实例属性

- [exponent](exponent-swift.property.md) — 浮点值的指数。
- [floatingPointClass](floatingpointclass.md) — 此值的分类。
- [isCanonical](iscanonical.md) — 一个布尔值，指示该实例的表示是否处于其规范形式。
- [isFinite](isfinite.md) — 一个布尔值，指示此实例是否为有限值。
- [isInfinite](isinfinite.md) — 一个布尔值，指示该实例是否为无限值。
- [isNaN](isnan.md) — 一个布尔值，指示该实例是否为 NaN（“非数字”）。
- [isNormal](isnormal.md) — 一个布尔值，指示此实例是否为规格化数（normal）。
- [isSignalingNaN](issignalingnan.md) — 一个布尔值，指示该实例是否为 signaling NaN。
- [isSubnormal](issubnormal.md) — 一个布尔值，指示该实例是否为次规格化数。
- [isZero](iszero.md) — 一个布尔值，指示该实例是否等于零。
- [nextDown](nextdown.md) — 按比较结果小于此值的最大可表示值。
- [nextUp](nextup.md) — 按比较结果大于此值的最小可表示值。
- [sign](sign.md) — 浮点值的符号。
- [significand](significand.md) — 浮点值的尾数。
- [ulp](ulp.md) — 此值的最后一位单位。

### 实例方法

- [addProduct(_:_:)](<addproduct(____).md>) — 就地将两个给定值的积加到该值上，计算过程中不进行中间舍入。
- [addingProduct(_:_:)](<addingproduct(____).md>) — 返回将两个给定值的积加到该值上的结果，计算过程中不进行中间舍入。
- [formRemainder(dividingBy:)](<formremainder(dividingby_).md>) — 用自身除以给定值所得的余数替换此值。
- [formSquareRoot()](<formsquareroot().md>) — 用该值的平方根替换该值，并舍入为可表示的值。
- [formTruncatingRemainder(dividingBy:)](<formtruncatingremainder(dividingby_).md>) — 用自身以截断除法除以给定值所得的余数替换此值。
- [isEqual(to:)](<isequal(to_).md>) — 返回一个布尔值，指示此实例是否等于给定值。
- [isLess(than:)](<isless(than_).md>) — 返回一个布尔值，指示此实例是否小于给定值。
- [isLessThanOrEqualTo(_:)](<islessthanorequalto(__).md>) — 返回一个布尔值，指示此实例是否小于或等于给定值。
- [isTotallyOrdered(belowOrEqualTo:)](<istotallyordered(beloworequalto_).md>) — 返回一个布尔值，指示在升序排序中此实例应排在给定值之前还是与其并列。
- [negate()](<negate().md>) — 用该值的加法逆元替换该值本身。
- [remainder(dividingBy:)](<remainder(dividingby_).md>) — 返回此值除以给定值所得的余数。
- [round()](<round().md>)
- [round(_:)](<round(__).md>) — 使用指定的舍入规则将该值舍入为整数值。
- [rounded()](<rounded().md>)
- [rounded(_:)](<rounded(__).md>) — 返回按指定的舍入规则将此值舍入为整数值的结果。
- [squareRoot()](<squareroot().md>) — 返回该值的平方根，并舍入为可表示的值。
- [truncatingRemainder(dividingBy:)](<truncatingremainder(dividingby_).md>) — 返回此值以截断除法除以给定值所得的余数。

### 类型别名

- [Exponent](exponent-swift.typealias.md) — 一种可以表示任何书写形式指数的类型。

### 类型属性

- [greatestFiniteMagnitude](greatestfinitemagnitude.md) — 此类型可表示的最大有限数。
- [infinity](infinity.md) — 正无穷大。
- [leastNonzeroMagnitude](leastnonzeromagnitude.md) — 最小的正数。
- [leastNormalMagnitude](leastnormalmagnitude.md) — 最小的正规格化数。
- [nan](nan.md) — 一个 quiet NaN（“非数字”）。
- [pi](pi.md) — 数学常数 pi（π），约等于 3.14159。
- [radix](radix.md) — 浮点类型的基数，即指数运算的底数。
- [signalingNaN](signalingnan.md) — 一个 signaling NaN（“非数字”）。
- [ulpOfOne](ulpofone.md) — 1.0 的最后一位单位。
- [ulpOfOne](ulpofone-817da.md) — 1.0 的最后一位单位。

### 类型方法

- [maximum(_:_:)](<maximum(____).md>) — 返回两个给定值中较大的一个。
- [maximumMagnitude(_:_:)](<maximummagnitude(____).md>) — 返回量级较大的值。
- [minimum(_:_:)](<minimum(____).md>) — 返回两个给定值中较小的一个。
- [minimumMagnitude(_:_:)](<minimummagnitude(____).md>) — 返回量级较小的值。
