---
title: '在 Mac OS X 上绘制自定义窗口 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/12/drawing-custom-window-on-mac-os-x.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:e4d912c9bc6d61a9'
translated: true
---

> 原文：[Drawing a custom window on Mac OS X | Cocoa with Love](https://www.cocoawithlove.com/2008/12/drawing-custom-window-on-mac-os-x.html)　·　Cocoa with Love (Matt Gallagher)

有些情况下，你可能希望窗口的外观与 Apple 提供的标准窗口样式完全不同。本文将向你展示如何绘制自定义窗口，并实现关闭、调整大小和拖拽功能。

## 引言

在这篇文章中，我将介绍一个自定义窗口和窗框（frame）类，它将绘制如下所示的窗口：

![](https://www.cocoawithlove.com/assets/objc-era/roundwindow.png)

除了用作大小调整控点的灰色方块和以标准方式工作的关闭框外，点击并拖拽此窗口窗框的任何部分都会拖动窗口。

你可以[下载 RoundWindow 的完整 Xcode 3.1 项目](https://www.cocoawithlove.com/assets/objc-era/RoundWindow.zip)（63kB）。

## 构建透明窗口

创建自定义窗口要从一个透明窗口开始。我将使用一个名为 `RoundWindow` 的自定义 `NSWindow` 子类。该子类的构造方法如下：

```objc
- (id)initWithContentRect:(NSRect)contentRect
    styleMask:(NSUInteger)windowStyle
    backing:(NSBackingStoreType)bufferingType
    defer:(BOOL)deferCreation
{
    self = [super
        initWithContentRect:contentRect
        styleMask:NSBorderlessWindowMask
        backing:bufferingType
        defer:deferCreation];
    if (self)
    {
        [self setOpaque:NO];
        [self setBackgroundColor:[NSColor clearColor]];
    }
    return self;
}
```

此构造方法对窗口所做的三项更改相当明显：

- `NSBorderlessWindowMask`（不带标准窗口边框的窗口）
- `setOpaque:NO`（以便窗口的任何部分都可以透明）
- `setBackgroundColor:[NSColor clearColor]`（如果不做其他操作，这将把窗口绘制为透明）

结果是一个透明的矩形窗口。该方法可以直接调用（如果在代码中创建窗口）。当从 NIB 加载窗口时，NIB 加载器也会调用它。

由于此窗口使用了 `NSBorderlessWindowMask` 样式，我们必须重写 `canBecomeKeyWindow` 和 `canBecomeMainWindow` 方法，使其返回 YES。这些重写将允许该窗口分别成为键盘焦点和主应用程序窗口。

## 为窗框预留空间

现在我们有了一个干净的空白画布，需要绘制窗口的窗框。第一个需求是在窗口内容周围预留一些空间来绘制窗框。

为了创建此空间，我们重写内容到窗框的转换方法：

```objc
- (NSRect)contentRectForFrameRect:(NSRect)windowFrame
{
    windowFrame.origin = NSZeroPoint;
    return NSInsetRect(
        windowFrame, WINDOW_FRAME_PADDING, WINDOW_FRAME_PADDING);
}

+ (NSRect)frameRectForContentRect:(NSRect)windowContentRect
    styleMask:(NSUInteger)windowStyle
{
    return NSInsetRect(
        windowContentRect, -WINDOW_FRAME_PADDING, -WINDOW_FRAME_PADDING);
}
```

这将在内容矩形周围添加 `WINDOW_FRAME_PADDING`（75）像素的边框。实际上，由于这是一个无边框窗口，内容视图本身将在每侧扩展 75 像素。下一部分将对此进行补偿，因此内容视图将是预期的、未扩展的大小。

## 创建窗框

Mac OS X 上窗口的常规结构是：

- `NSWindow`

我最初的想法是尝试替换现有的主题窗框视图。然而，这很快被证明过于困难。这个 `NSView` 的私有子类处理了许多与视图层级结构、布局和窗口绘制相关的奇特之处，而这些特性我不想自己实现。

相反，我选择重写窗口上的 `setContentView:` 和 `contentView:` 访问器，这样我的窗框视图总是被插入到主题窗框和 `contentView` 之间：

- `NSWindow`

`RoundWindow` 上的 `setContentView:` 重写如下：

```objc
- (void)setContentView:(NSView *)aView
{
    if ([childContentView isEqualTo:aView])
    {
        return;
    }
    
    NSRect bounds = [self frame];
    bounds.origin = NSZeroPoint;

    RoundWindowFrameView *frameView = [super contentView];
    if (!frameView)
    {
        frameView =
            [[[RoundWindowFrameView alloc]
                initWithFrame:bounds]
            autorelease];
        
        [super setContentView:frameView];
    }
    
    if (childContentView)
    {
        [childContentView removeFromSuperview];
    }
    childContentView = aView;
    [childContentView setFrame:[self contentRectForFrameRect:bounds]];
    [childContentView
        setAutoresizingMask:NSViewWidthSizable | NSViewHeightSizable];
    [frameView addSubview:childContentView];
}
```

因此，此方法将 `RoundWindowFrameView` 插入到内容视图和 `NSNextStepFrame` 之间。`childContentView` 是我们 `RoundWindow` 类上的一个实例变量，用于稍后再次找到此视图（如果需要获取、替换或调整其大小）。

在内部内容视图（我们的 `RoundWindowFrameView`）和外部内容视图（`childContentView`）之间创建这种不一致会引发一些问题。其他 `NSWindow` 方法（如 `setContentSize:`）如果需要按预期运行，也将需要被重写。与用我们的 `RoundWindowFrameView` 替换 `NSNextStepView` 所需的工作相比，这些重写应该相对简单直接。

## 绘制窗框

我们可以随心所欲地绘制窗口窗框：它只是一个自定义的 `NSView`。我们再次使用 `[NSColor clearColor]` 来绘制视图的背景。窗口后面的阴影会根据我们绘制的任何形状自动绘制。窗口任何完全透明的部分都不会接收鼠标点击（它们会穿过窗口）。

对于我的自定义窗口，我添加了一个标准的关闭框。可以使用以下方法创建标准关闭控制：

```objc
closeButton = [NSWindow
    standardWindowButton:NSWindowCloseButton forStyleMask:NSTitledWindowMask];
```

有两个小问题。第一：当窗口成为/放弃 `mainWindow` 状态时，它不会自我更新（因此我们必须检测到这一点并告知它重新显示）。第二：鼠标“悬停”效果似乎不起作用（我无法解决此问题）。

## 处理窗口控制

关闭按钮将直接关闭窗口，无需我们做其他任何事情。拖拽和调整大小的行为则需要我们付出努力。

拖拽和调整窗口大小都涉及更改其窗框。因此，两者都可以通过调用以下方法完成：

```objc
[window setFrame:newFrame display:YES animate:NO];
```

如果我们在一个跟踪 `NSLeftMouseDraggedMask` 操作的焦点锁定事件循环中连续调用此方法，那么随着鼠标的拖拽，更新将平滑地进行。

该事件循环如下所示：

```objc
while (YES)
{
    NSEvent *newEvent = [window
        nextEventMatchingMask:(NSLeftMouseDraggedMask | NSLeftMouseUpMask)];
    
    if ([newEvent type] == NSLeftMouseUp)
    {
        break;
    }
    
    // 确定鼠标操作的窗框更改并应用...

}
```

确定窗框更改的代码虽然直接，但包含在这里会有点长，不过你可以查看 `RoundWindowFrameView` 中的 `mouseDown:` 方法来了解它是如何完成的。

## 结论

你可以[下载 RoundWindow 的完整 Xcode 3.1 项目](https://www.cocoawithlove.com/assets/objc-era/RoundWindow.zip)（63kB）。

绘制一个没有行为的自定义窗口很简单，但与其他类型的自定义控制一样，可能需要添加许多微小的行为改进，才能使其感觉真正精致。

作为一个可调整大小的圆形窗口，`RoundWindow` 受限于其固定的 75 x 75 像素窗框宽度。对于小窗口来说，这个宽度太大了，而对于大窗口来说，又不足以让圆形很好地包围内容视图。为了将一个矩形内容视图正确地包围在圆形窗框中，窗框需要一个可变的宽度（这是我不想为这篇简单的文章设置的内容）。

自定义窗口可能还需要处理标题太长时的截断问题。其他窗口控制，如工具栏按钮、工具栏、最小化和缩放按钮以及关闭按钮上的“未保存更改”状态，都是窗口窗框的责任，但此处尚未探讨。

> [Paramanoir 发布了一篇以不同方式绘制自定义窗口的文章](http://parmanoir.com/Custom_NSThemeFrame)：通过在运行时将一个自定义的 `drawRect:` 方法 swizzle 到默认的 `NSThemeFrame` 类中。这有一些优点（`NSThemeFrame` 继续处理窗口控制），因此你可能需要考虑将该方法作为替代方案。
