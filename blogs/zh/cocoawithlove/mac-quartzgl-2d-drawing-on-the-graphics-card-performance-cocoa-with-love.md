---
title: Mac QuartzGL（显卡上的 2D 绘图）性能 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2011/03/mac-quartzgl-2d-drawing-on-graphics.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:dedd5e1d8be41d1f'
translated: true
---

> 原文：[Mac QuartzGL (2D drawing on the graphics card) performance | Cocoa with Love](https://www.cocoawithlove.com/2011/03/mac-quartzgl-2d-drawing-on-graphics.html)　·　Cocoa with Love (Matt Gallagher)

QuartzGL 在 Mac OS X 10.5 Leopard 中被作为一项官方特性引入（尽管它在 Mac OS X 10.4 中作为 Quartz 2D Extreme 只是一个面向开发者的特性）。然而，它默认处于关闭状态，并且被大多数开发者基本忽视。在这篇文章中，我会研究如何启用 QuartzGL、它对不同绘图类型的性能影响，以及你是否应该在 Mac 程序中使用它。

## 介绍

显卡渲染 3D 图形的速度可以比 CPU 快数百倍，并且显卡被用来加速桌面上窗口的合成（compositing），以获得数倍的性能提升。

尽管显卡在这些领域具有优势，Mac 上的 2D 几何图形通常还是由 CPU 在主内存中生成。你可以选择让程序在显卡上绘图，但这个选项默认是关闭的。这种在显卡上进行的 2D 绘图被称为 QuartzGL。

QuartzGL 的工作原理是生成一个 OpenGL ARB_fragment_program（像素缓冲绘图命令），并在显卡上执行通常由 CPU 完成的操作。

你不需要花很长时间就能猜到它默认被禁用的原因：QuartzGL 并不能提升所有类型的绘图。ARB_fragment_program 不使用 3D 图形所依赖的几何处理，因此它不太可能是 GPU 中最高效的部分。对于某些类型的绘图，它的性能甚至可能显著低于基于 CPU 的常规绘图。我希望回答的问题是：哪些类型的操作会更快，哪些不受影响，哪些可能会更慢？

## 如何启用 QuartzGL

你可以通过编辑程序的 Info.plist 文件来启用 QuartzGL。只需插入一个布尔值 `QuartzGLEnable` 并将其设为 true。

```objc
&lt;key&gt;QuartzGLEnable&lt;/key&gt;
&lt;true/&gt;
```

当然，如果你愿意，也可以对_任何_程序这样做。编辑 Info.plist，然后看看下次运行时会发生什么。

## 测试代码

我会运行三个测试：

1. 绘制半透明矩形
2. 绘制文本
3. 绘制随机放置的线条

如果你好奇我为什么测试这些：我实验了许多不同的绘图图元（drawing primitives），并认定这些是最常见的绘图图元，且它们产生了差异最大的结果。

这是绘图代码：

```objc
#if TEST == 1

    [[[NSColor redColor] colorWithAlphaComponent:0.01] set];
    for (NSInteger k = 0; k < 1000; k++)
    {
        [[NSBezierPath bezierPathWithRect:rect] fill];
    }

#elif TEST == 2

    for (NSInteger j = 0; j < 2000; j++)
    {
        NSString *displayString =
            @"A string to excercise basic Cocoa text drawing.";
        [displayString
            drawAtPoint:NSMakePoint(0, 0.5 * self.bounds.size.height)
            withAttributes:nil];
    }

#elif TEST == 3

    [[NSColor grayColor] set];
    for (NSInteger l = 0; l < 2000; l++)
    {
        CGFloat xCoord1 = self.bounds.size.width * random() / (CGFloat)INT_MAX;
        CGFloat xCoord2 = self.bounds.size.width * random() / (CGFloat)INT_MAX;
        CGFloat yCoord1 = self.bounds.size.height * random() / (CGFloat)INT_MAX;
        CGFloat yCoord2 = self.bounds.size.height * random() / (CGFloat)INT_MAX;
        
        NSBezierPath *line = [NSBezierPath bezierPath];
        [line moveToPoint:NSMakePoint(xCoord1, yCoord1)];
        [line lineToPoint:NSMakePoint(xCoord2, yCoord2)];
        [line stroke];
    }

#endif
```

## 测试结果

你可以[下载 QuartzGLTest 的完整项目](https://www.cocoawithlove.com/assets/objc-era/QuartzGLTest.zip)（32kb）。

我在一台配备 ATI Radeon HD 4870 显卡的 2.66Ghz 四核 Mac Pro 上运行了测试。我使用 Quartz Debug 程序在测试期间禁用了“Beam Sync”。测试应用中的窗口是可调整大小的，但我以默认的 480 x 400 像素内容尺寸运行。

![](https://www.cocoawithlove.com/assets/objc-era/quartzglperformance.png)

这里的原始 FPS 数据并不重要（我相当随意地选择了迭代次数）。重要的是 QuartzGL 测试与 CPU 测试之间的相对差异。

如你所见，QuartzGL 的影响范围从最佳情况下近 10 倍的性能提升，到降低 83% 的速度不等。

## 结论

半透明矩形的性能提升相当可观，但很难普遍推荐使用 QuartzGL。耗时的绘图操作很可能同时包含线条和纯色区域，最终使得两者差异微乎其微。

我曾花时间与一位参与过当时称为 Quartz 2D Extreme 开发的工程师交流。他给人的印象是，Apple 最初对其潜力寄予厚望——就像包括我在内的许多旁观者一样。在显卡上绘图似乎应该能让一切快上 10 倍。但正如这位工程师所述，他们就是可以绕过那些使整个系统速度令人失望的瓶颈。

最终，你更有可能通过减少重绘而非提高绘图速度来改善绘图性能。例如，你可以将绘图的某些区域缓存到 CoreAnimation 图层中，从而避免重绘，并依赖显卡擅长的操作：合成。顺便提一下，CoreAnimation 似乎会禁用 QuartzGL，因此你无法同时使用两者。

目前还不清楚未来显卡绘图是否会有所改善。我怀疑当前的 ARB_fragment_program 实现能否取得显著改进，但考虑到 OpenCL 和其他形式的 GPU 编程，使用更新技术的重新实现_感觉上_确实能带来更好的结果。当然，这种“感觉”并没有帮助最初的 ARB_fragment_program 实现取得成功。此外，OpenCL 仍然受到只能在特定显卡上工作的功能（如图像缓冲区）的限制。并且 OpenCL 并没有改变在 CPU 和显卡之间来回传输数据的瓶颈（即使 CPU 和 GPU 本身速度提升，这个瓶颈也不一定能改善）。

最后，不应将这些视为 CPU 上的 Quartz 绘图特别慢的迹象；它并不慢。但如果你想知道是否可以通过切换到 QuartzGL 来从程序中榨取一点额外的性能——可能不行，除非你程序中的关键限制是纯粹的像素填充率，并且你的线条相对较少。
