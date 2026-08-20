---
title: CoreGraphics 几何图元
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/cggeometry/'
original_language: en
published: 2019-04-22
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:06591c48187c7dd9'
translated: true
---

> 原文：[CoreGraphics Geometry Primitives](https://nshipster.com/cggeometry/)　·　NSHipster (Mattt)

# [Core​Graphics 几何图元](https://nshipster.com/cggeometry/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2019 年 4 月 22 日（[修订版](https://github.com/nshipster/articles/commits/master/2019-04-22-cggeometry.md)）

除非你曾是数学极客或古希腊人，否则几何多半不是你上学时最喜欢的科目。更可能的是，你是班上那个乖乖把所有必要公式都编进 TI-8X 计算器、免得死记硬背的家伙。

所以，如果你花在学 TI-BASIC 上的时间比学欧几里得还多，这里有一份速查表，告诉你几何在 Apple 平台所用的绘图系统 [Quartz 2D](https://developer.apple.com/library/mac/#documentation/graphicsimaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html) 中是如何运作的：

![](https://nshipster.com/assets/core-graphics-primitives-669295da8c1112f066e80978b96f3f60de8236d450cc3a73e279357195d66bf7703327f02c4affa8775f6233f8f5274abe01d3dd63076fa28dcc6e2b8507fe03.svg)

<sub>CoreGraphics 图元（iOS）</sub>

- `CGFloat` 表示一个标量值。
- `CGPoint` 表示二维坐标系中的一个位置，由 `x` 和 `y` 标量分量定义。
- `CGVector` 表示二维空间中的位置变化，由 `dx` 和 `dy` 标量分量定义。
- `CGSize` 表示二维空间中图形的范围，由 `width` 和 `height` 标量分量定义。
- `CGRect` 表示一个矩形，由一个原点（`CGPoint`）和一个尺寸（`CGSize`）定义。

```
import CoreGraphics

let float: CGFloat = 1.0
let point = CGPoint(x: 1.0, y: 2.0)
let vector = CGVector(dx: 4.0, dy: 3.0)
let size = CGSize(width: 4.0, height: 3.0)
var rectangle = CGRect(origin: point, size: size)
```

![](https://nshipster.com/assets/core-graphics-coordinate-systems-483faf8b5ad2b37db24ac28089115ddc2c71d3a0bbb3b094e1bb9583fe95fbf5073461daed9379c8528d9d11594d990e0091605dc618a6be52fc0de689960f76.svg)

<sub>CoreGraphics 坐标系（iOS）</sub>

在 iOS 上，原点位于窗口的左上角，因此 `x` 和 `y` 值向右下方向递增。macOS 则默认将 `(0, 0)` 设在窗口左下角，因此 `y` 值向上递增。

---

iOS 或 macOS App 中的每个视图（view）都有一个由 `CGRect` 值表示的 `frame`，因此学好这些几何图元的基本功大有裨益。

在本周的文章中，我们将快速浏览每个 App 开发者都该熟悉的 API。

---

## 内省

_“认识你自己。”_ 这句哲学格言在我们开始审视 CoreGraphics API 时，依然是一条实用的指引。

作为结构体（structure），你可以直接通过几何类型的存储属性（stored property）访问其成员值：

```
point.x // 1.0
point.y // 2.0

size.width // 4.0
size.height // 3.0

rectangle.origin // {x 1 y 2}
rectangle.size // {w 4 h 3}
```

你可以通过重新赋值，或使用 `*=` 和 `+=` 这类变异操作符（mutating operator）来更改变量：

```
var mutableRectangle = rectangle // {x 1 y 2 w 4 h 3}
mutableRectangle.origin.x = 7.0
mutableRectangle.size.width *= 2.0
mutableRectangle.size.height += 3.0
mutableRectangle // {x 7 y 2 w 8 h 6}
```

为方便起见，矩形也将 `width` 和 `height` 暴露为顶层的计算属性（computed property）；而 `x` 和 `y` 坐标必须通过中间的 `origin` 属性来访问：

```
rectangle.origin.x
rectangle.origin.y
rectangle.width
rectangle.height
```

### 访问最小值、中值和最大值

虽然矩形可以由位置（`CGPoint`）和范围（`CGSize`）完整描述，但这只是一面之词。

要了解另外三边，可以使用内建的便捷属性来获取 `x` 和 `y` 维度上的最小值（`min`）、中值（`mid`）和最大值（`max`）：

![](https://nshipster.com/assets/core-graphics-cgrect-min-mid-max-b3cb3042dad84d3e0b8881471dfed363933fc5a476453732679885767102db204be1365d3e93ed83677b1d52fb7ab1a48c35399afc076f3da9f1ae187fb3c5e6.svg)

<sub>CoreGraphics CGRect 属性（iOS）</sub>

```
rectangle.minX // 1.0
rectangle.midX // 3.0
rectangle.maxX // 5.0

rectangle.minY // 2.0
rectangle.midY // 3.5
rectangle.maxY // 5.0
```

#### 计算矩形中心点

计算矩形的中心点（center point）往往很实用。虽然这个属性框架 SDK 并未直接提供，但你可以轻松扩展（extend）`CGRect`，利用 `midX` 和 `midY` 属性来实现它：

```
extension CGRect {
    var center: CGPoint {
        return CGPoint(x: midX, y: midY)
    }
}
```

## 标准化

当你在几何计算中使用非整数值或负值时，情况可能会变得有点诡异。幸好，CoreGraphics 正好提供了你需要的 API 来让一切保持规整。

### 标准化矩形

我们期望矩形的原点位于其左上角。但是，如果它的 `width` 或 `height` 为负值，原点就可能变成其他某个角。

例如，来看看下面这个从其原点向左、向上延伸的_怪异_矩形。

```
let ǝןƃuɐʇɔǝɹ = CGRect(origin: point,
                         size: CGSize(width: -4.0, height: -3.0))
ǝןƃuɐʇɔǝɹ // {x 1 y 2 w -4 h -3}
```

我们可以使用 `standardized` 属性来获得 `width` 和 `height` 均非负的等效矩形。在前面的例子中，标准化后的矩形 `width` 为 `4`、`height` 为 `3`，并位于点 `(-3, -1)`：

```
ǝןƃuɐʇɔǝɹ.standardized // {x -3 y -1 w 4 h 3}
```

### 对齐矩形

通常最好让所有 `CGRect` 值都四舍五入到最接近的整数点。小数值会导致 frame 被绘制在**像素边界**上。因为像素是原子单位，小数值意味着绘制结果会在相邻像素间被平均化。结果就是：出现模糊（blur）的线条，观感欠佳。

`integral` 属性会取每个原点值的 `floor`（向下取整）和每个尺寸值的 `ceil`（向上取整）。这能确保你的绘制代码清爽地对齐在像素边界上。

```
let blurry = CGRect(x: 0.1, y: 0.5, width: 3.3, height: 2.7)
blurry // {x 0.1 y 0.5 w 3.3 h 2.7}
blurry.integral // {x 0 y 0 w 4 h 4}
```

## 变换

虽然你可以通过分别修改矩形的 `origin` 和 `size` 来改变它，但 CoreGraphics 框架借助下面讨论的 API，提供了更优的方案。

### 平移矩形

平移（translation）描述的是将形状从一个位置移动到另一个位置的几何操作。

使用 `offsetBy` 方法（或 Objective-C 中的 `CGRectOffset` 函数）即可将矩形的原点平移指定的 `x` 和 `y` 距离。

```
rectangle.offsetBy(dx: 2.0, dy: 2.0) // {x 3 y 4 w 4 h 3}
```

在需要移动矩形位置时，不妨优先考虑这个方法。它不光省一行代码，而且相比逐一修改原点值，在语义上更能表达你实际想做的是什么。

### 收缩与扩展矩形

另一种常见的矩形变换是围绕中心点收缩与扩展。`insetBy(dx:dy:)` 方法能同时实现这两者。

若传入的分量为正值，该方法会返回一个从中心点向内、每侧收缩指定距离的矩形。例如，当水平内缩 `1.0`（即 `dy = 0.0`）时，对于原点在 `(1, 2)`、`width` 为 `4`、`height` 为 `3` 的矩形，会产出一个原点在 `(2, 2)`、`width` 为 `2`、`height` 仍为 `3` 的新矩形。也就是说：**将一个矩形水平内缩 `1` 个点，得到的矩形 `width` 会比原来_小_ `2` 个点。**

```
rectangle // {x 1 y 2 w 4 h 3}
rectangle.insetBy(dx: 1.0, dy: 0.0) // {x 2 y 2 w 2 h 3}
```

若传入的分量为负值，矩形则会从每侧向外扩展该距离。如果传入非整数值，该方法可能产生带小数值分量的矩形。

```
rectangle.insetBy(dx: -1.0, dy: 0.0) // {x 0 y 2 w 6 h 3}
rectangle.insetBy(dx: 0.5, dy: 0.0) // {x 1.5 y 2 w 3 h 3}
```

## 恒等值（Identity）与特殊值

点、尺寸、矩形各自都有一个 `zero` 属性，它定义了对应类型的恒等值：

```
CGPoint.zero // {x 0 y 0}
CGSize.zero // {w 0 h 0}
CGRect.zero // {x 0 y 0 w 0 h 0}
```

Swift 的简写语法允许你直接将 `.zero` 作为参数传给方法和初始化器（initializer），例如 `CGRect.init(origin:size:)`：

```
let square = CGRect(origin: .zero,
                    size: CGSize(width: 4.0, height: 4.0))
```

---

`CGRect` 还有两个额外的特殊值：`infinite` 和 `null`：

```
CGRect.infinite // {x -∞ y -∞ w +∞ h +∞}
CGRect.null // {x +∞ y +∞ w 0 h 0}
```

`CGRect.null` 在概念上类似于 `NSNotFound`，它表示某个预期值的缺失，并通过使用最大可表示的数来排除所有其他值。

`CGRect.infinite` 的性质则更有趣：它与所有点和矩形都相交，包含所有矩形，而且它与任意矩形的并集就是它自身。

```
CGRect.infinite.contains(any point) // true
CGRect.infinite.intersects(any other rectangle) // true
CGRect.infinite.union(any other rectangle) // CGRect.infinite
```

使用 `isInfinite` 可以判断一个矩形是否确实为无穷大。

```
CGRect.infinite.isInfinite // true
```

但要彻底理解这些值为什么存在、怎么用，我们还得聊聊几何关系：

## 关系

截至这里，我们一直在孤立地摆弄几何体。作为收尾，让我们来看看在判定两个或更多矩形之间的关系时，都有哪些可能。

### 交集

若两个矩形有重叠部分，则两者相交。两者的**交集**（intersection）是能包含这两个矩形所共有的全部点的最小矩形。

![](https://nshipster.com/assets/core-graphics-intersection-492033ecd614a0c1583524b7445d4a49f8abee2f9e600d24c0444548f6c070e24979ba092c5998b026906f589329b6e460a2e8261629468f1e5e5324c76d10f3.svg)

<sub>CoreGraphics CGRect 交集（iOS）</sub>

在 Swift 中，你可以用 `intersects(_:)` 和 `intersection(_:)` 方法来高效计算两个 `CGRect` 值的交集：

```
let square = CGRect(origin: .zero,
                    size: CGSize(width: 4.0, height: 4.0))
square // {x 0 y 0 w 4 h 4}

rectangle.intersects(square) // true
rectangle.intersection(square) // {x 1 y 2 w 3 h 2}
```

如果两个矩形_不_相交，`intersection(_:)` 方法会返回 `CGRect.null`：

```
rectangle.intersects(.zero) // false
rectangle.intersection(.zero) // CGRect.null
```

### 并集

两个矩形的**并集**（union）是能够包含两者中任一所拥有的全部点的最小矩形。

![](https://nshipster.com/assets/core-graphics-union-3f0bb9a033a863b9fa22e9a4319a3bbe6db46160562300f29d8f3531cf19cae38481e858c2ef71fa05cf1e3db50fd0c8bd02d0d3e8fdaba14ae2dc52a90e9df4.svg)

<sub>CoreGraphics CGRect 并集（iOS）</sub>

在 Swift 中，名字取得恰到好处的 `union(_:)` 方法就是对两个 `CGRect` 值做这个操作：

```
rectangle.union(square) // {x 0 y 0 w 5 h 5}
```

---

所以，你说你几何课上没听讲——可这才是现实世界。在现实世界里，你有 `CGGeometry.h` 以及它提供的全部类型和函数。

把它吃透，你就能在自己的 App 中发现一番打造出色新界面的天地。要是做得足够好，你说不定还会碰上最美的算术题：把你用超棒的新 App 赚到的钱统统加起来。_妙极了！_
