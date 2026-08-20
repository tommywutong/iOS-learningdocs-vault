---
title: 使用 AppKit 的高级绘图 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2011/01/advanced-drawing-using-appkit.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:dc6df8aaf4d02139'
translated: true
---

> 原文：[Advanced drawing using AppKit | Cocoa with Love](https://www.cocoawithlove.com/2011/01/advanced-drawing-using-appkit.html)　·　Cocoa with Love (Matt Gallagher)

在这篇文章中，我将探讨如何通过组合多个视觉元素，在代码中绘制一张精细的图片。不同于我之前关于 Cocoa 绘图的文章，这次将重点关注 AppKit 类。代码将使用 `NSGraphicsContext`、`NSBezierPath`、`NSAffineTransform`、`NSGradient`、`NSGlyph`，并演示一些将 `NSView` 内容导出到文件的简单方法。

## 概述

当时我正在阅读一篇关于 Mac App Store 的文章，但我没有专心看文章或工作（那才是我当时该做的事），而是盯着配图发愣（一张 Mac App Store 图标的大图）。作为一个 Cocoa 程序员，我下意识地在脑海里解构这个图标，琢磨着如何在 Cocoa 中绘制类似的东西。

直到我写完了代码并决定就此写一篇文章时，我才注意到我已经写过 [一系列关于创建图标的文章](https://www.cocoawithlove.com/2009/11/creating-iphone-and-mac-icons-using.html)。我并非想重复劳动（这篇文章是关于 Cocoa 绘图技巧的；它*不是*像上一篇文章那样建议你如何创建应用程序图标），但事已至此无法更改，我多希望自己当时能选一个更新颖的视觉主题来写。

> **更新（2011-05-28）**：本文是一个 Mac 应用程序。如果你想看同样的设计用 iOS CoreGraphics 代码绘制的效果，[请查看 Marcus Crafter 的这篇博客文章](http://redartisan.com/2011/05/13/porting-iconapp-core-graphics)。

## 示例 App

![](https://www.cocoawithlove.com/assets/objc-era/iconapp.png)

> 你可以在这里下载本文使用的完整示例项目 [IconApp.zip](https://www.cocoawithlove.com/assets/objc-era/IconApp.zip)（96kB）

该应用程序有一个窗口，并在其中绘制一个图标。你可以调整窗口大小，图标始终会按比例缩放，以适合窗口。你可以将图标导出为 PDF 或 PNG 文件。

显然，虽然灵感来自 Mac App Store 图标，但这个设计并非试图精确复制它。真正的目的是演示如何实现多层渐变、曲线绘制、基于路径的裁剪、阴影和缩放——如果你想在代码中创建一个非平凡的设计，这些技巧你很可能会用到。

## 按比例缩放并居中

即使在开始绘制之前，我们也需要确保图像始终会缩放以适应窗口。第一步是找到一个缩放比例，使得正方形图标无论视图的大小或宽高比如何，都能适配到视图中：

```objc
NSSize nativeSize = [self nativeRect].size;
NSSize boundsSize = self.bounds.size;
CGFloat nativeAspect = nativeSize.width / nativeSize.height;
CGFloat boundsAspect = boundsSize.width / boundsSize.height;
CGFloat scale = nativeAspect > boundsAspect ?
    boundsSize.width / nativeSize.width :
    boundsSize.height / nativeSize.height;
```

在这个例子中，视图的 `nativeRect` 被定义为 `NSMakeRect(0, 0, 512, 512);`

一旦我们有了所需的缩放因子，我们就调整当前绘图上下文的大小并将其居中：

```objc
NSAffineTransform *transform = [[NSAffineTransform alloc] init];
[transform
    translateXBy:0.5 * (boundsSize.width - scale * nativeSize.width)
    yBy:0.5 * (boundsSize.height - scale * nativeSize.height)];
[transform scaleBy:scale];
[transform set];
```

应用这个仿射变换后，我们可以像在 `nativeRect` 大小的画布上一样绘制，但它会针对任何视图大小执行宽高比适配。

这里我没有展示，但如果你更改当前变换（或者像我稍后所做的那样更改当前裁剪路径），你应该记得在修改之前调用 `[[NSGraphicsContext currentContext] saveGraphicsState]`，并在绘制之后调用 `[[NSGraphicsContext currentContext] restoreGraphicsState]` 以将所有状态恢复原状。

## 绘制背景和阴影

![](https://www.cocoawithlove.com/assets/objc-era/iconapp-boundary.png)

我们首先使用纯色绘制背景圆形，并启用 `NSShadow`。

我们在绘制阴影时使用纯色（而不是我们想要在最终输出中使用的渐变），因为我们要使用的渐变绘制方法实际上会裁剪到渐变的边界，这样阴影就不会被绘制出来（因为阴影会在裁剪边界之外）。

此外，渐变的边缘不会抗锯齿。使用大致为渐变平均颜色的纯色来绘制形状，可以为我们提供一个漂亮的、抗锯齿的边缘。

```objc
[NSShadow setShadowWithOffset:NSMakeSize(0, -8 * scale) blurRadius:12 * scale
    color:[NSColor colorWithCalibratedWhite:0 alpha:0.75]];
[[NSColor colorWithCalibratedWhite:0.9 alpha:1.0] set];
[[NSBezierPath bezierPathWithOvalInRect:ellipseRect] fill];
[NSShadow clearShadow];
```

> **编码实践旁白：** 如果你是一个优秀的编码者，你应该避免使用 "[魔数](http://en.wikipedia.org/wiki/Magic_number_(programming)#Unnamed_numerical_constants)"。魔数是在代码中未经解释就使用的未命名数字。它们被认为是不良实践（相反，你应该将这些值赋给一个常量，该常量为值命名并解释任何推导过程，然后才能使用它）。
>
> 不过，我通常对绘图代码破例（就像本例一样）。如果一个数字纯粹是为了美学目的而选择的，并且与其他任何值没有实际关系，我就让它保留魔数的形式，假设其美学目的（以及推导或几何关系）是显而易见的。
>
> 不过，你确实需要严格控制数字的使用。你会注意到在这篇文章的后面（在「光泽渐变」代码中），其中混合了计算值、派生值、关系相关值以及纯粹的美学值，我费心使用了命名常量来阐明哪些是派生值、哪些是比例关系、哪段弧是哪一段。

前面代码块中的阴影方法是一个分类中的便捷方法，实现如下：

```objc
@implementation NSShadow (SingleLineShadows)

+ (void)setShadowWithOffset:(NSSize)offset blurRadius:(CGFloat)radius
    color:(NSColor *)shadowColor
{
    NSShadow *aShadow = [[[self alloc] init] autorelease];
    [aShadow setShadowOffset:offset];
    [aShadow setShadowBlurRadius:radius];
    [aShadow setShadowColor:shadowColor];
    [aShadow set];
}

+ (void)clearShadow
{
    NSShadow *aShadow = [[[self alloc] init] autorelease];
    [aShadow set];
}

@end
```

然后我们在顶部绘制渐变：

```objc
NSBezierPath *ellipse = [NSBezierPath bezierPathWithOvalInRect:ellipseRect];
NSGradient *borderGradient =
    [[[NSGradient alloc]
        initWithStartingColor:[NSColor colorWithCalibratedWhite:1.0 alpha:1.0]
        endingColor:[NSColor colorWithCalibratedWhite:0.82 alpha:1.0]]
    autorelease];
[borderGradient drawInBezierPath:ellipse angle:-90];
```

## 分层渐变以形成背景

单一、简单的渐变往往会显得平淡和人工。我们的眼睛期望比单个渐变通常所能提供的更复杂的光照。

对于这个渐变，我想要一个梨形效果，就好像一个圆形渐变被向上涂抹了一样。`NSGradient` 确实有方法可以让渐变沿着路径以圆形绘制，但它的美学效果比我想要的柔和、模糊的外观要生硬得多。

获得自然的柔和光照风格渐变效果的最简单方法就是简单地将几个渐变叠加在一起。通过正确设置每个渐变的 alpha 透明度，这些渐变看起来都会像是同一效果的一部分。当然，这种方式也很慢，尤其是在高分辨率下，因此这种方法要谨慎使用。

![](https://www.cocoawithlove.com/assets/objc-era/iconapp-gradients.png)

这张图片右下角的最终结果是通过绘制黑色背景，然后在黑色背景之上绘制左上、右上和左下渐变来实现的。

下面是绘制圆形中心为黑色的代码。然后我们设置上下文的裁剪路径，以便所有后续绘制都将裁剪到圆形的边框内部。

```objc
NSRect ellipseCenterRect = NSInsetRect(ellipseRect, 16, 16);
[[NSColor blackColor] set];
NSBezierPath *ellipseCenter = [NSBezierPath bezierPathWithOvalInRect:ellipseCenterRect];
[ellipseCenter fill];

[ellipseCenter setClip];
```

现在代码已经完成，我意识到我其实不需要在这里裁剪。我可以使用 `-[NSBezierPath drawInBezierPath:relativeCenterPosition:] method for the gradients to automatically draw them clipped to the ellipseCenter path and they would have clipped themselves (nothing else would have needed clipping). Performance-wise, it doesn't really matter though (either I apply the clip or the method does).` 方法让渐变自动裁剪到椭圆形中心路径，它们会自行裁剪（不需要裁剪其他任何东西）。但从性能角度来看，这其实无所谓（要么我应用裁剪，要么方法应用裁剪）。

绘制完背景后，我们开始分层叠加渐变。下面是绘制上面所示渐变左上角的代码：

```objc
NSGradient *bottomGlowGradient =
    [[[NSGradient alloc]
        initWithColorsAndLocations:
            [NSColor colorWithCalibratedRed:0 green:0.94 blue:0.82 alpha:1.0], 0.0,
            [NSColor colorWithCalibratedRed:0 green:0.62 blue:0.56 alpha:1.0], 0.35,
            [NSColor colorWithCalibratedRed:0 green:0.05 blue:0.35 alpha:1.0], 0.6,
            [NSColor colorWithCalibratedRed:0 green:0.0 blue:0.0 alpha:1.0], 0.7,
        nil]
    autorelease];
[bottomGlowGradient
    drawInRect:ellipseCenterRect relativeCenterPosition:NSMakePoint(0, -0.2)];
```

## 花心装饰

![](https://www.cocoawithlove.com/assets/objc-era/iconapp-floralheart.png)

花心是 Arial Unicode MS 字体中的一个字符。获取字体字符的贝塞尔路径有点繁琐，因为你需要使用 `NSLayoutManager` 来获取字形，然后才能要求 `NSBezierPath` 从字形创建路径。

```objc
NSString *floralHeart = @"\u2766";
NSRange stringRange = NSMakeRange(0, [floralHeart length]);
NSFont *arialUnicode =
    [[NSFontManager sharedFontManager]
        fontWithFamily:@"Arial Unicode MS"
        traits:0
        weight:5
        size:345];
NSLayoutManager *layoutManager = [[[NSLayoutManager alloc] init] autorelease];
NSTextStorage *textStorage =
    [[[NSTextStorage alloc] initWithString:floralHeart] autorelease];
[textStorage addAttribute:NSFontAttributeName value:arialUnicode range:stringRange];
[textStorage fixAttributesInRange:stringRange];
[textStorage addLayoutManager:layoutManager];
NSInteger numGlyphs = [layoutManager numberOfGlyphs];
NSGlyph *glyphs = (NSGlyph *)malloc(sizeof(NSGlyph) * (numGlyphs + 1)); // includes space for NULL terminator
[layoutManager getGlyphs:glyphs range:NSMakeRange(0, numGlyphs)];
[textStorage removeLayoutManager:layoutManager];

NSBezierPath *floralHeartPath = [[[NSBezierPath alloc] init] autorelease];
[floralHeartPath moveToPoint:NSMakePoint(130, 140)];
[floralHeartPath appendBezierPathWithGlyphs:glyphs count:numGlyphs inFont:arialUnicode];
free(glyphs);
```

如果有更简单的方法，我很想知道。看起来似乎应该可以直接请求一个 Unicode 字符的路径。

然后，花心使用渐变和阴影绘制，方式几乎与边框相同（我们甚至使用了相同的渐变）。

**更新：** 正如 Christopher Lloyd 在评论中指出的，你可以通过 `CTFont` 函数 `CTFontGetGlyphsForCharacters` 更轻松地获取 `NSGlyph`。这节省了 9 行代码，但破坏了我在这篇文章中全部使用 AppKit 而非 Core API 的努力：

```objc
// Replaces lines 1, 2, 9-18 of previous code block
NSInteger numGlyphs = 1; // hard-coded glyph count for floral heart character
NSGlyph *glyphs = (NSGlyph *)malloc(sizeof(NSGlyph) * (numGlyphs + 1)); // includes space for NULL terminator
CTFontGetGlyphsForCharacters(
    (CTFontRef)arialUnicode, (const UniChar *)L"\u2766", (CGGlyph *)glyphs, numGlyphs);
```

## 光泽渐变

![](https://www.cocoawithlove.com/assets/objc-era/iconapp.png)

图标最后用光泽渐变收尾。光泽渐变绘制在两条弧线之间，而这两条弧线正是难点所在。

光泽本身相对于边框内缩，以确保在边框近乎白色的颜色和光泽渐变之间，我们仍然能获得一个深色边缘作为对比。

光泽的左右边缘从圆形的正上方稍下一点开始（我选择了 0.02π 弧度），沿着顶部圆形的弧线，在图像中间向下突出，大约到圆形的中部。

我正确计算了顶部弧线的三角值，但并没有太在意底部突出的弧线（因为它的精确位置并不重要）。由于我为此底部弧线使用的三点弧绘制方法的性质，如果你为三点位置计算了错误的半径，弧线要么在左右端点附近变直，要么弧线超出这些点。我确信本可以做得更好（ bézier 曲线可能是更明智的选择，因为这条曲线并不需要一个完美的圆形）。

```objc
const CGFloat glossInset = 8;
CGFloat glossRadius = (ellipseCenterRect.size.width * 0.5) - glossInset;
NSPoint center = NSMakePoint(NSMidX(ellipseRect), NSMidY(ellipseRect));

double arcFraction = 0.02;
NSPoint arcStartPoint = NSMakePoint(
    center.x - glossRadius * cos(arcFraction * M_PI),
    center.y + glossRadius * sin(arcFraction * M_PI));
NSPoint arcEndPoint = NSMakePoint(
    center.x + glossRadius * cos(arcFraction * M_PI),
    center.y + glossRadius * sin(arcFraction * M_PI));

NSBezierPath *glossPath = [[[NSBezierPath alloc] init] autorelease];
[glossPath moveToPoint:arcStartPoint];
[glossPath
    appendBezierPathWithArcWithCenter:center
    radius:glossRadius
    startAngle:arcFraction * 180
    endAngle:(1.0 - arcFraction) * 180];

const CGFloat bottomArcBulgeDistance = 70;
const CGFloat bottomArcRadius = 2.6;
[glossPath moveToPoint:arcEndPoint];
[glossPath
    appendBezierPathWithArcFromPoint:
        NSMakePoint(center.x, center.y - bottomArcBulgeDistance)
    toPoint:arcStartPoint
    radius:glossRadius * bottomArcRadius];
[glossPath lineToPoint:arcStartPoint];
```

## 导出

在 Cocoa 中将视图导出为 PDF 文件非常简单：

```objc
[[iconView dataWithPDFInsideRect:[iconView nativeRect]]
    writeToURL:[savePanel URL]
    atomically:YES];
```

然而，你会很快发现，在 Mac OS X 中，带有透明度的渐变无法正确输出（其他所有内容，包括阴影，都工作正常）。网上声称这是 PDF 1.4（Mac OS X 中使用的 PDF 标准）的一个限制。

相反，如果我们想保留透明度，我们需要导出为 PNG。有几种不同的方法可以做到这一点，但最快最简单的方法是：

```objc
NSRect iconViewFrame = iconView.frame;
[iconView setFrame:[iconView nativeRect]];

NSBitmapImageRep *bitmapImageRep =
    [iconView bitmapImageRepForCachingDisplayInRect:[iconView frame]];
[iconView
    cacheDisplayInRect:[iconView bounds]
    toBitmapImageRep:bitmapImageRep];
[[bitmapImageRep representationUsingType:NSPNGFileType properties:nil]
    writeToURL:[savePanel URL]
    atomically:YES];

[iconView setFrame:iconViewFrame];
```

这种方法包含一些潜在问题：

- 我们需要调整视图大小，以所需的「原生」分辨率进行渲染
- 它会缓存屏幕渲染，因此可能包含与屏幕相关的异常（例如你的屏幕颜色配置文件）

最终，创建你自己的 `NSBitmapImageRep`，使用 `NSGraphicsContext` 设置 `graphicsContextWithBitmapImageRep:`，自己锁定焦点并直接调用 `drawRect:` 可以避免这些问题，并且更灵活。但这会更多的工作，所以我在这个示例项目中就没有费心（我将这个导出代码添加到 App 中，主要是为了能够创建 App 的图标）。

## 结语

> 你可以在这里下载本文使用的完整示例项目 [IconApp.zip](https://www.cocoawithlove.com/assets/objc-era/IconApp.zip)（96kB）

总的来说，在代码中构造这么多视觉元素并不常见；这些事情在绘图程序中无疑更容易，而预渲染的位图会更快（这在较大尺寸下相当慢）。

然而，在许多情况下，在代码中绘图可以提供优势——特别是如果你的设计需要重塑或适应内容。按钮和其他包含文本的控制就是一个例子，尤其是当你的设计不能简单地拉伸时。

即使你需要做的最复杂的事情是对渐变填充的路径进行抗锯齿处理，本文中也包含了一些技巧，希望对你有所帮助。
