---
title: 在 macOS 中为 Metal 管理你的游戏窗口
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/managing-your-game-window-for-metal-in-macos
source_url: 'https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/managing-your-game-window-for-metal-in-macos.json'
content_hash: 'sha256:853a3e476d3bdef1'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md)

# 在 macOS 中为 Metal 管理你的游戏窗口

<sub>文章</sub>

设置一个窗口和视图，以最佳方式显示你的 Metal 内容。

## 概述

借助 Metal，App 可以利用 GPU 快速渲染复杂场景，并并行运行计算任务。你的渲染结果会累积到一个 [CAMetalLayer](../quartzcore/cametallayer.md) 中，你可以用窗口将其显示在屏幕上。通过正确配置窗口，你的 App 就能让其 Metal drawable 启用直连显示（direct-to-display），从而获得最佳效果。而且，在非全屏模式下，你游戏的内容会显示在一个以 macOS 用户熟悉的方式运作的窗口中，符合预期。

当某个 Metal drawable 处于直连显示状态时，硬件会以极低的性能开销、通过高质量的放大或缩小算法，将其直接合成到显示器上。这意味着你的 App 可以高速地将 drawable 呈现到显示器上，所有细节都已被处理妥当。

要启用直连显示，你的 App 需要在全屏模式下运行，显示一个不透明的 [CAMetalLayer](../quartzcore/cametallayer.md) 图层和 RGB 内容，并且运行在搭载 Apple 芯片的 Mac 上。根据硬件和系统软件的不同，可能还存在其他边缘情况，但如果你按照这种方式设置窗口，在大多数情况下 drawable 都会是直连显示的。Metal 图层支持的所有 RGB 格式都能够绘制直连显示内容。你可以启用 Metal HUD，或者使用 Instruments 来验证你的 drawable 是否走的是直连显示。

### 为显示你的窗口选择屏幕

要在 macOS 中设置一个用于显示你游戏的窗口，首先要选择一个你想用来显示游戏的屏幕。运行你游戏的电脑可能配备了不止一台显示器。你可以使用 [NSScreen](../appkit/nsscreen.md) 类来发现运行 macOS 的电脑上连接了哪些[屏幕](../appkit/nsscreen/screens.md)，以及用户指定的主屏幕是哪一个。[main](../appkit/nsscreen/main.md) 是显示游戏的最佳选择。你可以像这样获取主屏幕的引用：

```objective-c
NSScreen *screen = [NSScreen mainScreen];
```

[NSScreen](../appkit/nsscreen.md) 对象包含详细信息，例如屏幕的分辨率、位深度、尺寸和位置、其色彩空间以及其他细节。如果你需要关于某个屏幕的更多信息，或者想要进行超出 [NSScreen](../appkit/nsscreen.md) AppKit API 所提供功能之外的交互，请参阅 [Quartz Display Services](../coregraphics/quartz-display-services.md) API。[Quartz Display Services](../coregraphics/quartz-display-services.md) 是一个更底层的 API，可直接访问 macOS 窗口服务器中用于配置和控制显示硬件的功能。

### 为你的窗口选择样式

macOS 中的 AppKit 有一个叫做 _窗口样式（window style）_ 的概念，你将其存储为一组标志位，用以描述窗口边框的布局以及装饰在窗口外沿的控制。对于显示 Metal 游戏内容的窗口，请使用以下值：

```objective-c
NSWindowStyleMask style= NSWindowStyleMaskClosable
                       | NSWindowStyleMaskTitled
                       | NSWindowStyleMaskMiniaturizable
                       | NSWindowStyleMaskResizable;
```

以下是上述样式的各个组成部分，以及各自为你的窗口添加的功能：

- **[closable](../appkit/nswindow/stylemask-swift.struct/closable.md)** — 用户可以关闭窗口。
- **[titled](../appkit/nswindow/stylemask-swift.struct/titled.md)** — 窗口会显示一个标题栏。
- **[miniaturizable](../appkit/nswindow/stylemask-swift.struct/miniaturizable.md)** — 窗口包含一个最小化（黄色圆点）控制，用户可以用它把窗口收进程序坞（Dock）。
- **[resizable](../appkit/nswindow/stylemask-swift.struct/resizable.md)** — 用户可以调整窗口大小。请注意，允许调整大小并不意味着你需要动态调整所有渲染目标的大小。本文后面的章节会讨论，当有人调整你的窗口大小时，如何调整你的 [CAMetalLayer](../quartzcore/cametallayer.md) 的 [drawableSize](../quartzcore/cametallayer/drawablesize.md) 以匹配屏幕上的像素。

### 为你的窗口和 Metal 视图选择内容尺寸

创建新窗口时，你需要以相对于某个屏幕坐标的点（point）来指定其坐标。_点_ 是一种抽象的度量单位，并不对应任何实际的像素尺寸。大约每英寸有 72 个点。有关点的更多信息，请参阅 [OS X 高分辨率指南](https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/Explained/Explained.html#//apple_ref/doc/uid/TP40012302-CH4-SW1)。

系统会替你处理与像素尺寸和显示分辨率相关的大多数问题，并根据用户使用的设备硬件优化其体验。你的 App 只需关心按照此处所述来设置其窗口。

对于你的初始窗口大小，你可以使用任何你认为在预期用户会使用你 App 的显示器上看起来合适的点尺寸：

```objective-c
NSRect contentRect = NSMakeRect(0, 0, 1280, 720);
```

创建窗口时选择的尺寸并不重要，但要让你的窗口在屏幕上居中：

```objective-c
contentRect.origin.x = (screen.frame.size.width - contentRect.size.width) / 2;
contentRect.origin.y = (screen.frame.size.height - contentRect.size.height) / 2;
```

创建窗口后，你可以使用 [convertPointToBacking(_:)](<../appkit/nswindow/convertpointtobacking(__).md>) 方法，获取有关 AppKit 用于渲染你视图的实际分辨率的更多信息。例如，如果你用窗口的尺寸调用 [convertPointToBacking(_:)](<../appkit/nswindow/convertpointtobacking(__).md>)，它会返回该窗口内容在屏幕上的实际像素尺寸。在将窗口中的位置转换为实际屏幕像素位置时，了解这一点会很有用，但在创建窗口时你不需要关心这些细节。

将用于管理窗口及其所依赖的 [CALayer](../quartzcore/calayer.md) 实例的所有 AppKit 设置保持默认值，这样你的 App 才能在系统的其余部分中保持外观一致。

### 创建窗口

在 macOS 中，AppKit 框架使用 [NSWindow](../appkit/nswindow.md) 类来表示窗口，因此你可以轻松地为你的 [NSWindow](../appkit/nswindow.md) 添加额外功能。像这样对 [NSWindow](../appkit/nswindow.md) 进行子类化：

```objective-c
@interface GameWindow: NSWindow
@end

@implementation GameWindow
@end
```

然后你可以按如下方式分配并初始化你的窗口：

```objective-c
GameWindow *window = [[GameWindow alloc] initWithContentRect:contentRect
                                                   styleMask:style
                                                     backing:NSBackingStoreBuffered
                                                       defer:NO
                                                      screen:screen];
```

你已经在前面的小节中设置好了 [contentRect](../appkit/nstabview/contentrect.md)、mask 和 screen 这几个参数。[NSWindow.BackingStoreType.buffered](../appkit/nswindow/backingstoretype/buffered.md) 参数会告诉 AppKit，你想要一个具有 [CALayer](../quartzcore/calayer.md) 后备存储（backing store）的窗口。之后，你会把这个 [CALayer](../quartzcore/calayer.md) 替换为 [CAMetalLayer](../quartzcore/cametallayer.md)，从而让窗口显示你的内容。

### 添加窗口

为了提供更好的用户体验，在创建新窗口之后，请在你的窗口上设置以下属性：

- 设置 [minSize](../appkit/nswindow/minsize.md)，以防止用户不小心把窗口调整得过小：

  ```objective-c
  window.minSize = NSMakeSize(640, 360);
  ```
- 如果你的游戏保留了对某个窗口的引用，请将 [isReleasedWhenClosed](../appkit/nswindow/isreleasedwhenclosed.md) 属性设置为 `NO`。这可以防止系统在有人关闭窗口时释放你的 [NSWindow](../appkit/nswindow.md) 对象：`window.releasedWhenClosed = NO;`。

> [!note] 注意
> 如果你的窗口已关闭且未显示，你可以通过调用窗口的 [setIsVisible(_:)](<../appkit/nswindow/setisvisible(__).md>) 和 [makeKeyAndOrderFront(_:)](<../appkit/nswindow/makekeyandorderfront(__).md>) 方法再次显示它。相关示例请参阅下面的“使窗口可见并呈现到最前”一节。

### 在你的新视图中显示 Metal 内容

当你希望 Metal 渲染某个图层的内容时，请使用 [CAMetalLayer](../quartzcore/cametallayer.md)。你要设置一个 [CAMetalLayer](../quartzcore/cametallayer.md)，并用它替换你之前设置的视图中的 [CALayer](../quartzcore/calayer.md)。首先创建一个新的 [CAMetalLayer](../quartzcore/cametallayer.md)：

```objective-c
CAMetalLayer *metalLayer = [[CAMetalLayer alloc] init]
```

然后，配置以下设置：

1. 使用默认值 `metalLayer.device = MTLCreateSystemDefaultDevice();` 将你的 [CAMetalLayer](../quartzcore/cametallayer.md) 与某个 Metal 设备关联起来。
2. 使该图层不透明。在合适的条件下，不透明图层可以提供直连显示内容：

  ```objective-c
  metalLayer.opaque = YES;
  ```
3. 为你的 [CAMetalLayer](../quartzcore/cametallayer.md) 图层选择一个分辨率。[CAMetalLayer](../quartzcore/cametallayer.md) 的像素分辨率决定了为填满该图层而生成的 drawable 的大小。

请尽可能支持动态调整大小，并在为你的 [CAMetalLayer](../quartzcore/cametallayer.md) 决定像素分辨率时，留意以下几点考虑：

- [CAMetalLayer](../quartzcore/cametallayer.md) 的像素分辨率不必与视图的后备尺寸（屏幕的分辨率）相匹配。
- 渲染与视图后备尺寸相匹配的 2D UI，并在另一个尺寸适合该设备的渲染目标中渲染 3D 内容。然后使用自定义渲染流程或 MetalFX 将其放大到最终的 drawable：`metalLayer.drawableSize = [view convertSizeToBacking:view.frame.size];`。
- 不过，对某些游戏来说，以任意尺寸渲染 drawable 可能更方便：`metalLayer.drawableSize = NSMakeSize(3840, 2160);`。
- 根据你的具体情况，drawable 的宽高比可能并不总是与视图的宽高比相匹配。在这种情况下，你可以使用 `metalLayer.contentsGravity = kCAGravityResizeAspect` 和 `metalLayer.backgroundColor = CGColorGetConstantColor(kCGColorBlack);`，让 Core Animation 替你保持宽高比。
- 不管怎样，即使 drawable 的尺寸与显示器尺寸不匹配，macOS 合成器也会高效地将该 drawable 直接发送到显示器。

设置好 [CAMetalLayer](../quartzcore/cametallayer.md) 之后，你可以用新的 [CAMetalLayer](../quartzcore/cametallayer.md) 替换该图层的 [CALayer](../quartzcore/calayer.md) 来激活它：

```objective-c
view.layer = metalLayer;
```

至此，你的窗口已经准备好开始渲染 Metal 内容了。

### 使窗口可见并呈现到最前

到目前为止，你所做的一切都还在屏幕之外。要将你的新窗口和 Metal 视图呈现到屏幕上，请调用以下 API：

```objective-c
[window setIsVisible:true];
[window makeKeyAndOrderFront:nil];
```

如果有人恰好关闭了你的窗口，而你在创建窗口时之前已经设置了 `window.releasedWhenClosed = NO;`，你可以使用这些 API 再次将窗口呈现到屏幕上。

### 使用整个窗口

最后，通过调用 [toggleFullScreen(_:)](<../appkit/nswindow/togglefullscreen(__).md>) 方法，将你的窗口设置为全屏模式：

```objective-c
[window toggleFullScreen:nil];
```

你可以再次调用同一个方法来退出全屏模式。有关 AppKit 与全屏模式的更多信息，请参阅 [Mac App 编程指南：实现全屏体验](https://developer.apple.com/library/archive/documentation/General/Conceptual/MOSXAppProgrammingGuide/FullScreenApp/FullScreenApp.html)。

请注意，在使用 [toggleFullScreen(_:)](<../appkit/nswindow/togglefullscreen(__).md>) 方法时，你并不指定“全屏”具体意味着什么，而是让系统以对用户来说最熟悉的方式来决定其含义。当你调用 [toggleFullScreen(_:)](<../appkit/nswindow/togglefullscreen(__).md>) 时，系统会将你窗口的尺寸调整为它认为的全屏尺寸。

> [!important] 重要
> 使用 [toggleFullScreen(_:)](<../appkit/nswindow/togglefullscreen(__).md>) 来切换到全屏，这样你 App 的全屏模式才能与其他使用全屏模式的 App 保持一致的行为方式。这能让窗口的控制权始终掌握在用户手中，而由 AppKit 负责在你选定的屏幕上为你的窗口找到最佳的位置和尺寸。请避免对 [toggleFullScreen(_:)](<../appkit/nswindow/togglefullscreen(__).md>) 所做的任何事情进行自定义。

### 添加代码使你的窗口能够处理尺寸调整

为了让 `CAMetalLayer` 实例的 [drawableSize](../quartzcore/cametallayer/drawablesize.md) 与窗口正在绘制的那部分屏幕保持同步，请按下文所述，在窗口的委托上设置一个 [windowDidResize(_:)](<../appkit/nswindowdelegate/windowdidresize(__).md>) 方法。每当你的窗口调整尺寸时都要调用这个方法，包括你的 App 调用 [toggleFullScreen(_:)](<../appkit/nswindow/togglefullscreen(__).md>) 的那些时刻。

通过为你的 [NSWindow](../appkit/nswindow.md) 子类（`GameWindow`）添加一个 [NSWindowDelegate](../appkit/nswindowdelegate.md)，你可以响应该窗口的尺寸调整事件。这些事件可能发生在用户操作、显示器属性发生变化，或者你的应用调整窗口尺寸时。使用 [NSWindowDelegate](../appkit/nswindowdelegate.md) 协议来定义你自己的委托类，使其能够按如下方式响应 [windowDidResize(_:)](<../appkit/nswindowdelegate/windowdidresize(__).md>) 事件：

```objective-c
@interface GameWindowDelegate: NSObject<NSWindowDelegate>
@end

@implementation GameWindowDelegate {
}

-(void)windowDidResize:(NSNotification *)notification {
// 自动调整视图的尺寸。
// 在这里使用视图的尺寸
// 调整 Metal 图层的尺寸。如有需要，你可以使用任何其他尺寸。
    NSWindow window = notification.object; // 1
    NSView *view = window.contentView; // 2
    CAMetalLayer *metalLayer = (CAMetalLayer *)view.layer; // 3
    metalLayer.drawableSize = [view convertSizeToBacking:view.frame.size]; // 4
}

@end
```

以下是上述语句所做的事情：

- 将 [NSWindow](../appkit/nswindow.md) 对象作为 [NSNotification](../foundation/nsnotification.md) 对象的 object 属性接收。
- 获取你在“创建窗口”一节中创建的视图的引用。
- 获取你在“在你的新视图中显示 Metal 内容”一节中创建的 [CAMetalLayer](../quartzcore/cametallayer.md) 的引用。
- 通过调用你 [NSView](../appkit/nsview.md) 实例的 [convertToBacking(_:)](<../appkit/nsview/converttobacking(__)-4ra9y.md>) 方法（“为你的窗口和 Metal 视图选择内容尺寸”一节有所介绍），将 [CAMetalLayer](../quartzcore/cametallayer.md) 实例的 [drawableSize](../quartzcore/cametallayer/drawablesize.md) 属性重置为你打算绘制的屏幕的实际像素尺寸。请注意，这些做法是让 drawable 匹配显示器的尺寸和分辨率，但这并非必需。如果 drawable 不匹配显示器的尺寸和分辨率，它在显示器上呈现时会自动缩放。

最终的结果是，每当你调整窗口尺寸时，系统都会将 `CAMetalLayer` 实例的 [drawableSize](../metalkit/mtkview/drawablesize.md) 属性重置为你窗口所绘制显示器的实际像素分辨率。

通过将符合 [NSWindowDelegate](../appkit/nswindowdelegate.md) 协议的类的实例赋值给窗口的 [delegate](../appkit/nswindow/delegate.md) 属性，将该实例设为你 `GameWindow` 的委托。

```objective-c
GameWindowDelegate *windowDelegate = [[GameWindowDelegate alloc] init];
if (windowDelegate != NULL) {
    window.delegate = windowDelegate;
}
```

设置好窗口委托之后，每当你窗口的尺寸发生变化时，它就会开始收到对你 [windowDidResize(_:)](<../appkit/nswindowdelegate/windowdidresize(__).md>) 方法的调用。当你的 App 调用 [toggleFullScreen(_:)](<../appkit/nswindow/togglefullscreen(__).md>) 时，AppKit 会重新计算你窗口的尺寸，并调用你委托的 [windowDidResize(_:)](<../appkit/nswindowdelegate/windowdidresize(__).md>) 方法。

### 添加代码，防止你的窗口类无意中消费按键事件

在某些情况下，AppKit 框架与 Game Controller 框架之间的交互，可能会让 [NSWindow](../appkit/nswindow.md) 的 API 无意中消费了本应发送给 [GCController](../gamecontroller/gccontroller.md) 的按键事件。为避免这种可能性，请在你的 `GameWindow` 类上添加一个什么都不做的按键按下处理程序：

```objective-c
@interface GameWindow : NSWindow
@end

@implementation GameWindow

- (void)keyDown:(NSEvent *)event
{
}

@end
```

## 另请参阅

### 呈现

- [Managing your Metal app window in iPadOS](managing-your-metal-app-window-in-ipados.md) — 设置一个能够动态调整你 Metal 内容尺寸的窗口。
- [Adapting your game interface for smaller screens](adapting-your-game-interface-for-smaller-screens.md) — 让玩家选择运行你游戏的所有设备上的文本都清晰可读。
- [Onscreen presentation](onscreen-presentation.md) — 在你的 App 中向用户展示 GPU 渲染流程的输出。
- [HDR content](hdr-content.md) — 利用高动态范围，在你的 App 和游戏中呈现更鲜艳的色彩。
