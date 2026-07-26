---
title: Texture-Layout
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/texture-layout/'
original_language: zh
published: 2019-03-03
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:0222984ffc18d143'
translated: n/a
---

> 原文：[Texture-Layout](https://dirtmelon.github.io/posts/texture-layout/)　·　dirtmelon

原文链接：[Layout](https://texturegroup.org/docs/layout2-quickstart.html)

## 原因和收益

Auto Layout 在处理复杂的 View 时，消耗会指数级上升， Texture 布局在以下几方面比 Auto Layout 好：

- 快，明显比 Auto Layout 快，基本上跟手动布局差不多
- 异步和并发，布局可以在后台线程进行计算，所以不会打断用户交互
- 声明式布局，不可变的数据结构，这使得布局代码易于开发，编写文档，code review ，测试，debug ，描述和维护
- 可缓存，得益于不可变的数据结构，布局可以在后台预先计算和缓存起来
- 可扩展的，代码易于复用

## 受到 CSS Flexbox 的启发

这两个系统有非常多相似的属性。也有不同的地方，[Texture | Web Flexbox Differences](http://texturegroup.org/docs/layout2-web-flexbox-differences.html)

## 基本概念

Texture 的布局以以下两个基本概念为中心：

1. Layout Specs
2. Layout Elements

### Layout Specs

Layout Spec 不包含具体的控价，它相当于一个定义了 Layout Elements 的子 Layout Elements 如何布局的容器。

[Texture

Layout Specs](http://texturegroup.org/docs/layout2-layoutspec-types.html)

### Layout Elements

Layout Spec 包含和排列 Layout Elements 。 `ASDisplayNode` 和 `ASLayoutSpec` 都遵循了  协议，这意味着你可以使用 `ASDisplayNode` 和 `ASLayoutSpec ` 来组成 `ASLayoutSpec ` 。

### 某些 Node 需要设置 size

一些 Node 可以根据它们可直接获取的内容自动设置 intrinsic size ：

- `ASImageNode`
- `ASTextNode`
- `ASbuttonNode`

一些 Node 不具有 intrinsic size ，或者说需要等到外部资源加载完成后才有 intrinsic size ，这些 Node 在初始化时需要设置大小：

- `ASVideoNode`
- `ASVideoPlayerNode`
- `ASNetworkImageNode`
- `ASEditableTextNode`

### Layout Debugging

debug 时调用 `ASDisplayNode` 或者 `ASLayoutSpec` 的 `-asciiArtString` 方法可以打印出 ascii 码形式的布局信息：

```
-----------------------ASStackLayoutSpec----------------------
|  -----ASStackLayoutSpec-----  -----ASStackLayoutSpec-----  |
|  |       ASImageNode       |  |       ASImageNode       |  |
|  |       ASImageNode       |  |       ASImageNode       |  |
|  ---------------------------  ---------------------------  |
--------------------------------------------------------------
```

也可以打印 `ASLayoutElement` 的 style 属性：

```
(lldb) po _photoImageNode.style
Layout Size = min {414pt, 414pt} <= preferred {20%, 50%} <= max {414pt, 414pt}
```

## Layout API 大小调整

### 值(CGFloat, ASDimension)

`ASDimension` 本质上是 CGFloat ，支持表示百分比，字符串，符点值。

```swift
// dimension returned is relative (%)**
ASDimensionMake("50%")
ASDimensionMakeWithFraction(0.5)

// dimension returned in points**
ASDimensionMake("70pt")
ASDimensionMake(70)
ASDimensionMakeWithPoints(70)
```

### Sizes(CGSize, ASLayoutSize)

`ASLayoutSize` 跟 `CGSize` 类似，但是它的宽高可以用浮点值或者百分比来表示，宽高的类型是相互独立的。

```swift
// Dimension type "Auto" indicates that the layout element may 
// be resolved in whatever way makes most sense given the circumstances
let width = ASDimensionMake(.auto, 0)
let height = ASDimensionMake("50%")
        
layoutElement.style.preferredLayoutSize = ASLayoutSizeMake(width, height)

layoutElement.style.preferredSize = CGSize(width: 30, height: 60)
```

### Size Range(ASSizeRange)

`UIKit` 没有提供一种包含最大 `CGSize` 和最小 `CGSize` 的数据结构，为此创建了 `ASSizeRange` 类型。

## Layout Transition API

Layout Transition API 为了 Texture 更易地制造动画效果而设计的。整个过程中，用户只需要定义目标 Layout ，Texture 会自动分辨出它跟当前 Layout 的不同之处。会自动添加新的元素，移除不需要的元素，和更新其它存在的元素的位置。

如果要使用 Layout Transition API ，则必须要用 [Texture

Automatic Subnode Management](http://texturegroup.org/docs/automatic-subnode-mgmt.html)

### Animating between Layouts

我们可以在 `layoutSpecThatFits:` 中通过不同的状态进行不同的布局，然后通过 `transitionLayoutWithAnimation:` 开始转换。调用 `transitionLayoutWithAnimation:` 后，它会调用 `transitionLayoutWithAnimation:` 方法，我们可以在这个方法里面调用动画。

```swift
override func animateLayoutTransition(_ context: ASContextTransitioning) {
  if fieldState == .signupNodeName {
    let initialNameFrame = context.initialFrame(for: ageField)
    
    nameField.frame = initialNameFrame
    nameField.alpha = 0
    
    var finalAgeFrame = context.finalFrame(for: nameField)
    finalAgeFrame.origin.x -= finalAgeFrame.size.width
    
    UIView.animate(withDuration: 0.4, animations: { 
        self.nameField.frame = context.finalFrame(for: self.nameField)
        self.nameField.alpha = 1
        self.ageField.frame = finalAgeFrame
        self.ageField.alpha = 0
    }, completion: { finished in
        context.completeTransition(finished)
    })
  } else {
    var initialAgeFrame = context.initialFrame(for: nameField)
    initialAgeFrame.origin.x += initialAgeFrame.size.width
    
    ageField.frame = initialAgeFrame
    ageField.alpha = 0
    
    var finalNameFrame = context.finalFrame(for: ageField)
    finalNameFrame.origin.x -= finalNameFrame.size.width
    
    UIView.animate(withDuration: 0.4, animations: { 
        self.ageField.frame = context.finalFrame(for: self.ageField)
        self.ageField.alpha = 1
        self.nameField.frame = finalNameFrame
        self.nameField.alpha = 0
    }, completion: { finished in
        context.completeTransition(finished)
    })
  }
}
```

`context` 参数提供了转换前后的信息，包括新旧的 `constrained size` ，插入和移除的 nodes ，新旧的 `ASLayout` 对象。

### Animating constrainedSize Changes

当 node 的 bounds 发生变化时，可以调用 `transitionLayoutWithSizeRange:animated:` 方法。
