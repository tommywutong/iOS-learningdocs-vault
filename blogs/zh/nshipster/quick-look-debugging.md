---
title: 快速查看调试
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/quick-look-debugging/'
original_language: en
published: 2015-03-30
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:4a96b9873850bd58'
translated: true
---

> 原文：[Quick Look Debugging](https://nshipster.com/quick-look-debugging/)　·　NSHipster (Mattt)

# [快速查看调试](https://nshipster.com/quick-look-debugging/)

作者 [Nate Cook](https://nshipster.com/authors/nate-cook/)　2015 年 3 月 30 日

调试有时会沦为一件充满讽刺意味的事。我们编写程序，让口袋里的超级计算机替我们完成千变万化、不可胜数的任务，然而在试图理解这些程序时，我们却又让计算机等待_我们_。

举个例子，假设我想搞清楚为什么我的 App 里的 `UINavigationBar` 没有按预期显示。为了调查，我可能会使用调试器查看在导航栏上设置的 `UIColor` 实例——这个颜色_到底是_什么颜色？

![调试中的 UIColor](https://nshipster.com/assets/quicklook-debug-90b953d443516f9a0c0cbd5d7a0a9afeed8b100b0f3295a88435970897d7dab0e5dad86deb94fe32bfe2bb06d39f894b6113a70e87f10b8dc08c4cf14a9a4b6b.gif)

别急！不用再费力推算那些分量是如何叠加的了。_有一个更好的方法。_

自 Xcode 5 起，调试器中已内置了快速查看（Quick Look）显示功能。就像你在桌面上按一下空格键就能查看文件内容一样，在 Xcode 中你可以用快速查看来直观地显示各种数据类型。在 `color` 变量上按一下空格键，答案立刻呈现——无需进行任何心算 RGB：

![UIColor 快速查看](https://nshipster.com/assets/quicklook-color-d1e9b3a7ef497fb7cc3b2f90a35d5a86df7b9b74ac59cb368cb030d4ff96e052e6eff7594e296a1391bed57eaa1c032da8c1993ae92d0d98e5c472a63ef2ee72.gif)

---

你还可以在调试过程中直接从代码里调用快速查看。来看下面的方法 `buildPathWithRadius(_:steps:loopCount:)`。它创建了一个 `UIBezierPath`，但你已经忘了是何种，而且这段代码真的能工作吗？

```
func buildPathWithRadius(radius: CGFloat, steps: CGFloat, loopCount: CGFloat) -> UIBezierPath {
    let away = radius / steps
    let around = loopCount / steps * 2 * CGFloat(M_PI)
    
    let points = map(stride(from: 1, through: steps, by: 1)) { step -> CGPoint in
        let x = cos(step * around) * step * away
        let y = sin(step * around) * step * away
        
        return CGPoint(x: x, y: y)
    }
    
    let path = UIBezierPath()
    path.moveToPoint(CGPoint.zeroPoint)
    for point in points {
        path.addLineToPoint(point)
    }
    
    return path
}
```

```
- (UIBezierPath *)buildPathWithRadius:(CGFloat)radius steps:(CGFloat)steps loopCount:(CGFloat)loopCount {
    CGFloat x, y;
    CGFloat away = radius / steps;
    CGFloat around = loopCount / steps * 2 * M_PI;
    
    UIBezierPath *path = [UIBezierPath bezierPath];
    [path moveToPoint:CGPointZero];
    
    for (int i = 1; i <= steps; i++) {
        x = cos(i * around) * i * away;
        y = sin(i * around) * i * away;
        
        [path addLineToPoint:CGPointMake(x, y)];
    }
    
    return path;
}
```

要查看结果，你当然可以创建一个自定义视图来渲染这个贝塞尔路径，或者把它绘制到 `UIImage` 里。但更好的办法是，在方法末尾插入一个断点，然后把鼠标悬停在 `path` 上：

![螺旋 UIBezierPath 快速查看](https://nshipster.com/assets/quicklook-spiral-ae59f476054a09af2172bcc5df458cac8bc8b1f94ae9e5fc72a0a9404461d103b19b1c38791e94cfb4557aef426de1d543b5852b4303860831e12a73c0267f30.gif)

螺旋效果太棒了！

---

### 内建类型

快速查看可以直接用于大多数你想直观查看的数据类型。Xcode 已经为以下类型提供了支持：

> - **图像：**`UIImage`、`NSImage`、`UIImageView`、`NSImageView`、`CIImage` 和 `NSBitmapImageRep` 都可以通过快速查看显示。
> - **颜色：**`UIColor` 和 `NSColor`。（`CGColor` 就不行了。）
> - **字符串：**`NSString` 和 `NSAttributedString`。
> - **几何：**`UIBezierPath` 和 `NSBezierPath`，以及 `CGPoint`、`CGRect` 和 `CGSize`。
> - **位置：**`CLLocation` 会提供一个大型、可交互的地图视图，并叠加显示海拔和精度详情。
> - **URL：**`NSURL` 会显示一个展示 URL 所指向的本地或远程内容的视图。
> - **光标：**`NSCursor`，供使用光标的我们使用。
> - **SpriteKit：**`SKSpriteNode`、`SKShapeNode`、`SKTexture` 和 `SKTextureAtlas` 都可显示。
> - **数据：**`NSData` 有一个很棒的视图，可以显示带有偏移量的十六进制和 ASCII 值。
> - **视图：**最后但同样重要的是，任何 `UIView` 的子类都会在快速查看弹窗中显示其内容——非常方便。

此外，这些快速查看弹窗通常还包含一个按钮，可以在相关应用中打开内容。图像数据（以及视图、光标和 SpriteKit 类型）提供了在预览（Preview）中打开的选项。远程 URL 可以在 Safari 中打开；本地 URL 可以在相关应用中打开。最后，纯文本和属性字符串数据也可以同样在文本编辑（TextEdit）中打开。

### 自定义类型

对于超出这些内建类型之外的任何类型，Xcode 6 为自定义对象增加了快速查看功能。实现方式简单得不能再简单——在任何继承自 `NSObject` 的类中添加一个 `debugQuickLookObject()` 方法就可以了。`debugQuickLookObject()` 可以返回上述任何一种内建类型，根据你的自定义类型需求进行配置：

```
func debugQuickLookObject() -> AnyObject {
    let path = buildPathWithRadius(radius, steps: steps, loopCount: loopCount)
    return path
}
```

```
- (id)debugQuickLookObject {
    UIBezierPath *path = [self buildPathWithRadius:self.radius steps:self.steps loopCount:self.loopCount];
    return path;
}
```

---

总之，快速查看使我们能够更直接地与代码中处理的数据建立联系，让我们可以在较小的功能片段上迭代。这种直接查看以往难以理解的数据类型的能力，将 Swift Playground 的一些即时性带入了我们的主要代码库。显示图像？可视化数据？渲染文本？计算机恰恰非常擅长这些！从现在开始，让它们来做吧。
