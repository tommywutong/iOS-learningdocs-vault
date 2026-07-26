---
title: Double 的浮点运算符
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floating-point-operators-for-double
source_url: 'https://developer.apple.com/documentation/swift/floating-point-operators-for-double'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floating-point-operators-for-double.json'
content_hash: 'sha256:a0abc42b274ab140'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md) · [Double](double.md)

# Double 的浮点运算符

<sub>API 集合</sub>

执行算术和位运算操作，或比较值。

## 主题

### 算术运算

- [+(_:_:)](<double/+(____).md>) — 将两个值相加，得到它们的和，并舍入为可表示的值。
- [-(_:_:)](<double/-(____).md>) — 从一个值中减去另一个值，得到它们的差，并舍入为可表示的值。
- [*(_:_:)](<double/_(____).md>) — 将两个值相乘，得到它们的积，并舍入为可表示的值。
- [/(_:_:)](<double/_(____).md>) — 用第一个值除以第二个值，返回商，并舍入为可表示的值。

### 带赋值的算术运算

- [+=(_:_:)](<double/+=(____).md>) — 将两个值相加，并把结果存储到左侧变量中，同时舍入为可表示的值。
- [-=(_:_:)](<double/-=(____).md>) — 用第一个值减去第二个值，并把差存储到左侧变量中，同时舍入为可表示的值。
- [*=(_:_:)](<double/_=(____).md>) — 将两个值相乘，并把结果存储到左侧变量中，同时舍入为可表示的值。
- [/=(_:_:)](<double/_=(____).md>) — 用第一个值除以第二个值，并把商存储到左侧变量中，同时舍入为可表示的值。

### 比较运算

- [==(_:_:)](<double/==(____)-12hdv.md>) — 返回一个布尔值，表示两个值是否相等。
- [!=(_:_:)](<double/!=(____).md>) — 返回一个布尔值，表示两个值是否不相等。

### 取负

- [-(_:)](<double/-(__).md>) — 计算一个值的加法逆元。
- [+(_:)](<double/+(__).md>) — 原样返回给定的数值。

### 区间表达式

- [...(_:)](<double/'...(__)-4mm67.md>) — 返回一个到（且包含）上界的部分区间。
- [...(_:)](<double/'...(__)-6ct5v.md>) — 返回一个从下界向上延伸的部分区间。

## 另请参阅

### 执行计算

- [addingProduct(_:_:)](<double/addingproduct(____).md>) — 返回将两个给定值的积加到该值上的结果，计算过程中不进行中间舍入。
- [addProduct(_:_:)](<double/addproduct(____).md>) — 就地将两个给定值的积加到该值上，计算过程中不进行中间舍入。
- [squareRoot()](<double/squareroot().md>) — 返回该值的平方根，并舍入为可表示的值。
- [formSquareRoot()](<double/formsquareroot().md>) — 用该值的平方根替换该值，并舍入为可表示的值。
- [remainder(dividingBy:)](<double/remainder(dividingby_).md>) — 返回该值除以给定值所得的余数。
- [formRemainder(dividingBy:)](<double/formremainder(dividingby_).md>) — 用该值除以给定值所得的余数替换该值本身。
- [truncatingRemainder(dividingBy:)](<double/truncatingremainder(dividingby_).md>) — 使用截断除法，返回该值除以给定值所得的余数。
- [formTruncatingRemainder(dividingBy:)](<double/formtruncatingremainder(dividingby_).md>) — 使用截断除法，用该值除以给定值所得的余数替换该值本身。
- [negate()](<double/negate().md>) — 用该值的加法逆元替换该值本身。
