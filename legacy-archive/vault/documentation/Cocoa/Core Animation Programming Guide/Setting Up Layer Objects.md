---
title: Core Animation 编程指南
apple_id: TP40004514
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/SettingUpLayerObjects/SettingUpLayerObjects.html
archived_at: '2026-07-15T07:14:07.989305Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Core Animation 编程指南](About%20Core%20Animation.md)


[下一页](Animating%20Layer%20Content.md)[上一页](Core%20Animation%20Basics.md)

# 设置图层对象

图层对象是你用 Core Animation 所做一切事情的核心。图层管理着你的应用的视觉内容，并提供了修改该内容样式和外观的选项。虽然 iOS 应用会自动启用图层支持，但 OS X 应用的开发者必须先显式启用它，才能利用图层带来的性能优势。启用之后，你还需要了解如何配置和操作应用中的图层，才能获得你想要的效果。

在 iOS 应用中，Core Animation 始终处于启用状态，每个视图都由一个图层提供支撑。在 OS X 中，应用必须通过以下方式显式启用 Core Animation 支持：

- 链接 QuartzCore 框架。（iOS 应用只有在显式使用 Core Animation 接口时才需要链接此框架。）
- 通过以下方式之一为一个或多个 [NSView](https://developer.apple.com/documentation/appkit/nsview) 对象启用图层支持：

  - 在 nib 文件中，使用 View Effects 检查器为视图启用图层支持。该检查器会为所选视图及其子视图显示复选框。建议尽可能在窗口的内容视图中启用图层支持。
  - 对于以编程方式创建的视图，调用该视图的 [setWantsLayer:](https://developer.apple.com/documentation/appkit/nsview/1483695-wantslayer) 方法并传入 `YES`，表明该视图应当使用图层。

通过上述任一方式启用图层支持后，就会创建出一个图层支撑视图（layer-backed view）。对于图层支撑视图，系统负责创建底层的图层对象并保持该图层的更新。在 OS X 中，你还可以创建图层承载视图（layer-hosting view），由你的应用自行创建和管理底层的图层对象。（在 iOS 中无法创建图层承载视图。）关于如何创建图层承载视图的更多信息，请参阅 [Layer Hosting Lets You Change the Layer Object in OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjtfvjvomq)。

图层支撑视图默认会创建一个 [CALayer](https://developer.apple.com/documentation/quartzcore/calayer) 类的实例，多数情况下你可能不需要其他类型的图层对象。不过，Core Animation 还提供了多种不同的图层类，每一种都提供了你可能会用到的专门能力。选用不同的图层类，可以让你以简单的方式提升性能或支持某种特定类型的内容。例如，[CATiledLayer](https://developer.apple.com/documentation/quartzcore/catiledlayer) 类就针对高效显示大图像做了优化。

你可以通过重写视图的 [layerClass](https://developer.apple.com/documentation/uikit/uiview/1622626-layerclass) 方法并返回一个不同的类对象，来更改 iOS 视图所使用的图层类型。多数 iOS 视图会创建一个 [CALayer](https://developer.apple.com/documentation/quartzcore/calayer) 对象，并将该图层用作其内容的后备存储。对于你自己的大多数视图来说，这个默认选择就是不错的选择，通常不需要更改。但在某些情况下，你可能会发现使用不同的图层类更为合适。例如，在以下情况下你可能想要更改图层类：

- 你的视图使用 Metal 或 OpenGL ES 绘制内容，此时你会用到 [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer) 或 [CAEAGLLayer](https://developer.apple.com/documentation/quartzcore/caeagllayer) 对象。
- 存在某个能带来更好性能的专门图层类。
- 你想利用某些专门的 Core Animation 图层类，例如粒子发射器或复制器。

更改视图的图层类非常简单；清单 2-1 展示了一个示例。你只需重写 `layerClass` 方法并返回你想改用的类对象即可。在显示之前，视图会调用 `layerClass` 方法，并使用返回的类为自身创建一个新的图层对象。图层对象一旦创建，就无法再更改。

__清单 2-1__  指定 iOS 视图的图层类

```objc
+ (Class) layerClass {
   return [CAMetalLayer class];
}
```

关于图层类列表及其使用方法，请参阅 [Different Layer Classes Provide Specialized Behaviors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjtfvjvomrv)。

你可以通过重写 [makeBackingLayer](https://developer.apple.com/documentation/appkit/nsview/1483687-makebackinglayer) 方法来更改 `NSView` 对象所使用的默认图层类。在该方法的实现中，创建并返回你希望 AppKit 用来支撑自定义视图的图层对象。当你想使用滚动图层或分块图层等自定义图层时，可以重写这个方法。

关于图层类列表及其使用方法，请参阅 [Different Layer Classes Provide Specialized Behaviors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjtfvjvomrv)。

图层承载视图是一个 [NSView](https://developer.apple.com/documentation/appkit/nsview) 对象，其底层的图层对象由你自己创建和管理。当你想控制与视图关联的图层对象类型时，可以使用图层承载。例如，你可能会创建一个图层承载视图，以便指定默认 `CALayer` 类之外的图层类。你也可能在想用单个视图来管理一组独立图层层级结构时使用它。

当你调用视图的 [setLayer:](https://developer.apple.com/documentation/appkit/nsview/1483298-layer) 方法并提供一个图层对象时，AppKit 会对该图层采取放手不管的态度。通常情况下，AppKit 会更新视图的图层对象，但在图层承载的情形下，它对大多数属性都不会这样做。

要创建图层承载视图，需要在把视图显示到屏幕上之前创建图层对象并将其与视图关联，如清单 2-2 所示。除了设置图层对象之外，你仍必须调用 [setWantsLayer:](https://developer.apple.com/documentation/appkit/nsview/1483695-wantslayer) 方法，以便让视图知道它应当使用图层。

__清单 2-2__  创建图层承载视图

```objc
// 创建 myView...

[myView setWantsLayer:YES];
CATiledLayer* hostedLayer = [CATiledLayer layer];
[myView setLayer:hostedLayer];

// 将 myView 添加到视图层级结构中。
```

如果你选择自己承载图层，就必须自行设置 [contentsScale](https://developer.apple.com/documentation/quartzcore/calayer/1410746-contentsscale) 属性，并在适当的时机提供高分辨率内容。关于高分辨率内容和缩放因子的更多信息，请参阅 [Working with High-Resolution Images](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjtfvjvonq)。

Core Animation 定义了许多标准图层类，每一种都是为特定用例设计的。[CALayer](https://developer.apple.com/documentation/quartzcore/calayer) 类是所有图层对象的根类。它定义了所有图层对象都必须支持的行为，也是图层支撑视图使用的默认类型。不过，你也可以指定表 2-1 中的某个图层类。

__表 2-1__  `CALayer` 的子类及其用途

| 类 | 用途 |
| --- | --- |
| [CAEmitterLayer](https://developer.apple.com/documentation/quartzcore/caemitterlayer) | 用于实现基于 Core Animation 的粒子发射系统。发射器图层对象控制粒子的生成及其来源。 |
| [CAGradientLayer](https://developer.apple.com/documentation/quartzcore/cagradientlayer) | 用于绘制填充图层形状的颜色渐变（在圆角范围之内）。 |
| [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer) | 用于设置并提供可绘制纹理，以便使用 Metal 渲染图层内容。 |
| [CAEAGLLayer](https://developer.apple.com/documentation/quartzcore/caeagllayer)/[CAOpenGLLayer](https://developer.apple.com/documentation/quartzcore/caopengllayer) | 用于设置后备存储和上下文，以便使用 OpenGL ES（iOS）或 OpenGL（OS X）渲染图层内容。 |
| [CAReplicatorLayer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer) | 用于自动生成一个或多个子图层的副本。复制器会替你生成这些副本，并使用你指定的属性来更改副本的外观或特性。 |
| [CAScrollLayer](https://developer.apple.com/documentation/quartzcore/cascrolllayer) | 用于管理由多个子图层组成的大型可滚动区域。 |
| [CAShapeLayer](https://developer.apple.com/documentation/quartzcore/cashapelayer) | 用于绘制三次贝塞尔样条曲线。形状图层在绘制基于路径的形状时很有优势，因为它们总能得到清晰锐利的路径，而在图层的后备存储中绘制的路径在缩放时观感就没那么好。不过，要得到清晰的结果，就需要在主线程上渲染形状并缓存结果。 |
| [CATextLayer](https://developer.apple.com/documentation/quartzcore/catextlayer) | 用于渲染纯文本字符串或属性字符串。 |
| [CATiledLayer](https://developer.apple.com/documentation/quartzcore/catiledlayer) | 用于管理可分割为若干小块并单独渲染的大图像，并支持内容的放大和缩小。 |
| [CATransformLayer](https://developer.apple.com/documentation/quartzcore/catransformlayer) | 用于渲染真正的 3D 图层层级结构，而不是其他图层类所实现的扁平化图层层级结构。 |
| [QCCompositionLayer](https://developer.apple.com/documentation/quartz/qccompositionlayer) | 用于渲染 Quartz Composer 合成作品。（仅限 OS X） |

图层是管理你的应用所提供内容的数据对象。图层的内容由一个包含你想要显示的视觉数据的位图组成。你可以通过以下三种方式之一来提供该位图的内容：

- 直接将一个图像对象赋值给图层对象的 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性。（这种方式最适合几乎从不改变的图层内容。）
- 为图层指定一个委托对象，让委托来绘制图层的内容。（这种方式最适合可能会周期性变化、并且可以由外部对象（例如视图）提供的图层内容。）
- 定义一个图层子类，并重写其中一个绘制方法，自行提供图层内容。（如果你无论如何都需要创建一个自定义图层子类，或者想要改变图层的基本绘制行为，这种方式就很合适。）

只有在你自己创建图层对象时，才需要考虑为图层提供内容的问题。如果你的应用中只有图层支撑视图，就不必操心使用上述任何一种技巧来提供图层内容。图层支撑视图会以尽可能高效的方式，自动为其关联的图层提供内容。

由于图层只是管理位图图像的容器，你可以把一个图像直接赋值给图层的 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性。给图层赋值图像很简单，它能让你精确指定想要在屏幕上显示的图像。图层会直接使用你提供的图像对象，而不会尝试创建该图像的自有副本。当你的应用在多处使用同一图像时，这种行为可以节省内存。

赋值给图层的图像必须是 [CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref) 类型。（在 OS X v10.6 及更高版本中，你也可以赋值一个 [NSImage](https://developer.apple.com/documentation/appkit/nsimage) 对象。）在赋值图像时，请记得提供一个分辨率与原生设备分辨率相匹配的图像。对于配备 Retina 显示屏的设备，这可能还需要你调整该图像的 [contentsScale](https://developer.apple.com/documentation/quartzcore/calayer/1410746-contentsscale) 属性。关于如何为图层使用高分辨率内容的更多信息，请参阅 [Working with High-Resolution Images](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjtfvjvonq)。

如果图层的内容会动态变化，你可以使用一个委托对象，在需要时提供并更新该内容。在显示时，图层会调用你的委托的方法来提供所需的内容：

- 如果你的委托实现了 [displayLayer:](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097261-displaylayer) 方法，该实现就负责创建一个位图并将其赋值给图层的 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性。
- 如果你的委托实现了 [drawLayer:inContext:](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097262-drawlayer) 方法，Core Animation 会创建一个位图，再创建一个用于绘制到该位图的图形上下文，然后调用你的委托方法来填充该位图。你的委托方法要做的，只是绘制到所提供的图形上下文中。

委托对象必须实现 `displayLayer:` 或 `drawLayer:inContext:` 方法中的一个。如果委托同时实现了 `displayLayer:` 和 `drawLayer:inContext:` 方法，图层只会调用 `displayLayer:` 方法。

重写 `displayLayer:` 方法最适合你的应用倾向于加载或创建想要显示的位图的情形。清单 2-3 展示了 `displayLayer:` 委托方法的一个示例实现。在这个示例中，委托使用一个辅助对象来加载并显示所需的图像。该委托方法根据自身的内部状态来选择要显示哪张图像，在示例中这个状态是一个名为 `displayYesImage` 的自定义属性。

__清单 2-3__  直接设置图层内容

```objc
- (void)displayLayer:(CALayer *)theLayer {
    // 检查某个状态属性的值
    if (self.displayYesImage) {
        // 显示 Yes 图像
        theLayer.contents = [someHelperObject loadStateYesImage];
    }
    else {
        // 显示 No 图像
        theLayer.contents = [someHelperObject loadStateNoImage];
    }
}
```

如果你没有预先渲染好的图像，也没有可以帮你创建位图的辅助对象，你的委托可以使用 `drawLayer:inContext:` 方法动态绘制内容。清单 2-4 展示了 `drawLayer:inContext:` 方法的一个示例实现。在这个示例中，委托使用固定的线宽和当前的渲染颜色绘制了一条简单的曲线路径。

__清单 2-4__  绘制图层的内容

```objc
- (void)drawLayer:(CALayer *)theLayer inContext:(CGContextRef)theContext {
    CGMutablePathRef thePath = CGPathCreateMutable();

    CGPathMoveToPoint(thePath,NULL,15.0f,15.f);
    CGPathAddCurveToPoint(thePath,
                          NULL,
                          15.f,250.0f,
                          295.0f,250.0f,
                          295.0f,15.0f);

    CGContextBeginPath(theContext);
    CGContextAddPath(theContext, thePath);

    CGContextSetLineWidth(theContext, 5);
    CGContextStrokePath(theContext);

    // 释放该路径
    CFRelease(thePath);
}
```

对于带有自定义内容的图层支撑视图，你应当继续重写视图的方法来完成绘制。图层支撑视图会自动将自身设为其图层的委托，并实现所需的委托方法，你不应更改这种配置。你应当做的是实现视图的 `drawRect:` 方法来绘制你的内容。

在 OS X v10.8 及更高版本中，绘制之外的另一种做法是通过重写视图的 [wantsUpdateLayer](https://developer.apple.com/documentation/appkit/nsview/1483461-wantsupdatelayer) 和 [updateLayer](https://developer.apple.com/documentation/appkit/nsview/1483580-updatelayer) 方法来提供位图。重写 `wantsUpdateLayer` 并返回 `YES`，会使 `NSView` 类走一条不同的渲染路径。此时视图不会调用 `drawRect:`，而是调用你的 `updateLayer` 方法，该方法的实现必须直接将一个位图赋值给图层的 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性。这是唯一一种 AppKit 期望你直接设置视图图层对象内容的场景。

如果你无论如何都要实现一个自定义图层类，就可以重写该图层类的绘制方法来完成任何绘制工作。图层对象自行生成自定义内容的情况并不常见，但图层当然可以管理内容的显示。例如，[CATiledLayer](https://developer.apple.com/documentation/quartzcore/catiledlayer) 类通过将一张大图像拆分成可以单独管理和渲染的小块来管理它。由于只有图层才掌握在任意给定时刻哪些块需要渲染的信息，因此它直接管理绘制行为。

在派生子类时，你可以使用以下两种技巧之一来绘制图层的内容：

- 重写图层的 [display](https://developer.apple.com/documentation/quartzcore/calayer/1410926-display) 方法，并用它直接设置图层的 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性。
- 重写图层的 [drawInContext:](https://developer.apple.com/documentation/quartzcore/calayer/1410757-draw) 方法，并用它绘制到所提供的图形上下文中。

该重写哪个方法，取决于你需要在多大程度上掌控绘制过程。`display` 方法是更新图层内容的主要入口点，因此重写该方法能让你完全掌控整个过程。重写 `display` 方法同时也意味着你要负责创建将要赋值给 `contents` 属性的 [CGImageRef](https://developer.apple.com/documentation/coregraphics/cgimageref)。如果你只是想绘制内容（或者让图层来管理绘制操作），可以改为重写 `drawInContext:` 方法，让图层替你创建后备存储。

当你把一个图像赋值给图层的 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性时，图层的 [contentsGravity](https://developer.apple.com/documentation/quartzcore/calayer/1410872-contentsgravity) 属性决定了该图像会如何被处理以适配当前的 bounds。默认情况下，如果图像比当前 bounds 大或小，图层对象会缩放图像以适配可用空间。如果图层 bounds 的宽高比与图像的宽高比不同，这可能会导致图像发生形变。你可以使用 `contentsGravity` 属性，确保内容以最佳方式呈现。

可以赋值给 `contentsGravity` 属性的值分为两大类：

- 基于位置的重力常量让你可以把图像固定在图层 bounds 矩形的某个边或角上，而不对图像进行缩放。
- 基于缩放的重力常量让你可以使用多种选项之一来拉伸图像，其中一些会保持宽高比，另一些则不会。

图 2-1 展示了基于位置的重力设置会如何影响你的图像。除了 [kCAGravityCenter](https://developer.apple.com/documentation/quartzcore/kcagravitycenter) 常量之外，其余每个常量都会把图像固定在图层 bounds 矩形的某个边或角上。`kCAGravityCenter` 常量会把图像居中放置在图层中。这些常量都不会以任何方式缩放图像，因此图像始终会以其原始尺寸渲染。如果图像比图层的 bounds 大，可能会导致图像的部分内容被裁切；如果图像比较小，图层中未被图像覆盖的部分则会显露出图层的背景色（如果设置了背景色的话）。

__图 2-1__  图层的基于位置的重力常量

!

图 2-2 展示了基于缩放的重力常量会如何影响你的图像。如果图像不能完全贴合图层的 bounds 矩形，这些常量都会对图像进行缩放。各种模式之间的区别在于它们如何处理图像的原始宽高比：有些模式会保持宽高比，有些则不会。默认情况下，图层的 `contentsGravity` 属性被设为 [kCAGravityResize](https://developer.apple.com/documentation/quartzcore/kcagravityresize) 常量，这是唯一不保持图像宽高比的模式。

__图 2-2__  图层的基于缩放的重力常量

!

图层本身并不了解底层设备屏幕的分辨率。图层只是存储了指向你的位图的一个指针，并根据可用的像素以最佳方式显示它。如果你把一个图像赋值给图层的 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性，就必须通过将图层的 [contentsScale](https://developer.apple.com/documentation/quartzcore/calayer/1410746-contentsscale) 属性设为适当的值，来告诉 Core Animation 该图像的分辨率。该属性的默认值是 `1.0`，适用于打算在标准分辨率屏幕上显示的图像。如果你的图像是为 Retina 显示屏准备的，请将该属性的值设为 `2.0`。

只有在你直接为图层赋值位图时，才需要更改 `contentsScale` 属性的值。UIKit 和 AppKit 中的图层支撑视图会根据屏幕分辨率以及该视图所管理的内容，自动将其图层的缩放因子设为适当的值。例如，如果你在 OS X 中把一个 [NSImage](https://developer.apple.com/documentation/appkit/nsimage) 对象赋值给图层的 `contents` 属性，AppKit 会查看该图像是否同时存在标准分辨率和高分辨率两种版本。如果存在，AppKit 会为当前分辨率选用正确的版本，并相应地设置 `contentsScale` 属性的值。

在 OS X 中，基于位置的重力常量会影响从赋值给图层的 `NSImage` 对象中选择图像表现形式的方式。由于这些常量不会导致图像被缩放，Core Animation 需要依靠 `contentsScale` 属性来挑选像素密度最合适的图像表现形式。

在 OS X 中，图层的委托可以实现 `layer:shouldInheritContentsScale:fromWindow:` 方法，并用它来响应缩放因子的变化。每当某个窗口的分辨率发生变化时（比如窗口在标准分辨率屏幕和高分辨率屏幕之间移动），AppKit 都会自动调用该方法。如果委托支持更改图层图像的分辨率，你对该方法的实现就应当返回 `YES`。然后该方法应当按需更新图层的内容，以反映新的分辨率。

图层对象内置了边框和背景色等视觉装饰，你可以用它们来补充图层的主要内容。由于这些视觉装饰不需要你来做任何渲染工作，它们使得在某些情况下把图层当作独立实体使用成为可能。你只需在图层上设置一个属性，图层就会处理必要的绘制工作，包括任何动画。关于这些视觉装饰如何影响图层外观的更多说明，请参阅 [Layer Style Property Animations](Layer%20Style%20Property%20Animations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjqfvjvomi)。

除了基于图像的内容之外，图层还可以显示一个填充背景和一条描边边框。背景色会渲染在图层内容图像的下方，而边框会渲染在该图像的上方，如图 2-3 所示。如果图层包含子图层，它们也会出现在边框下方。由于背景色位于图像的下方，因此图像中任何透明的部分都会透出该颜色。

__图 2-3__  为图层添加边框和背景

!

清单 2-5 展示了为图层设置背景色和边框所需的代码。所有这些属性都是可动画的。

__清单 2-5__  设置图层的背景色和边框

```objc
myLayer.backgroundColor = [NSColor greenColor].CGColor;
myLayer.borderColor = [NSColor blackColor].CGColor;
myLayer.borderWidth = 3.0;
```

如果你把图层的背景色设为一种不透明的颜色，可以考虑把图层的 opaque 属性设为 `YES`。这样做可以提升在屏幕上合成该图层时的性能，并且不再需要图层的后备存储管理 alpha 通道。不过，如果图层的圆角半径不为零，就不能将其标记为不透明。

你可以通过为图层添加圆角半径，来营造出圆角矩形的效果。圆角半径是一种视觉装饰，它会遮罩图层 bounds 矩形各角的部分区域，让底层内容得以透出，如图 2-4 所示。由于圆角半径涉及应用一个透明度遮罩，除非 [masksToBounds](https://developer.apple.com/documentation/quartzcore/calayer/1410896-maskstobounds) 属性被设为 `YES`，否则圆角半径不会影响图层 `contents` 属性中的图像。不过，圆角半径始终会影响图层背景色和边框的绘制方式。

__图 2-4__  图层上的圆角半径

!

要为图层应用圆角半径，请为图层的 [cornerRadius](https://developer.apple.com/documentation/quartzcore/calayer/1410818-cornerradius) 属性指定一个值。你指定的半径值以点为单位，会在显示之前应用到图层的全部四个角上。

[CALayer](https://developer.apple.com/documentation/quartzcore/calayer) 类包含若干用于配置阴影效果的属性。阴影通过让图层看起来仿佛悬浮在其底层内容之上，为图层增添了深度感。这是另一种视觉装饰，你可能会在应用的特定情形下发现它很有用。借助图层，你可以控制阴影的颜色、相对于图层内容的位置、不透明度以及形状。

图层阴影的不透明度值默认设为 `0`，这实际上隐藏了阴影。将不透明度改为一个非零值，会使 Core Animation 绘制该阴影。由于阴影默认直接位于图层正下方，你可能还需要更改阴影的偏移量才能看到它。不过要记住一点很重要：你为阴影指定的偏移量，是按照图层的原生坐标系应用的，而这套坐标系在 iOS 和 OS X 上是不同的。图 2-5 展示了一个阴影向图层的右下方延伸的图层。在 iOS 中，这需要为 y 轴指定一个正值，但在 OS X 中该值则需要是负数。

__图 2-5__  为图层应用阴影

!

在为图层添加阴影时，阴影是图层内容的一部分，但实际上会延伸到图层 bounds 矩形之外。因此，如果你为该图层启用了 [masksToBounds](https://developer.apple.com/documentation/quartzcore/calayer/1410896-maskstobounds) 属性，阴影效果就会在边缘处被裁切。如果你的图层包含任何透明内容，这可能会造成一种奇怪的效果：阴影中正好位于图层正下方的部分仍然可见，而延伸到图层之外的部分则不可见。如果你既想要阴影又想使用 bounds 遮罩，可以使用两个图层而不是一个：把遮罩应用到包含内容的那个图层上，然后把该图层嵌入到另一个尺寸完全相同、启用了阴影效果的图层中。

关于阴影如何应用到图层的示例，请参阅 [Shadow Properties](Layer%20Style%20Property%20Animations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjqfvjvomjy)。

在 OS X 应用中，你可以将 Core Image 滤镜直接应用到图层的内容上。你可以借此模糊或锐化图层的内容、改变颜色、扭曲内容，或者执行许多其他类型的操作。例如，图像处理程序可能会用这些滤镜来对图像进行非破坏性的修改，而视频编辑程序则可能用它们来实现不同类型的视频转场效果。而且由于这些滤镜是在硬件中应用到图层内容上的，渲染既快速又流畅。

对于给定的一个图层，你既可以为它的前景内容应用滤镜，也可以为它的背景内容应用滤镜。前景内容由图层自身包含的一切构成，包括其 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性中的图像、背景色、边框，以及其子图层的内容。背景内容则是位于图层正下方、但实际上并不属于图层本身的内容。多数图层的背景内容就是其直接父图层的内容，该内容可能会被该图层完全或部分遮挡。举例来说，当你希望用户把注意力集中在图层的前景内容上时，可以为背景内容应用模糊滤镜。

你可以通过将 [CIFilter](https://developer.apple.com/documentation/coreimage/cifilter) 对象添加到图层的以下属性中来指定滤镜：

- [filters](https://developer.apple.com/documentation/quartzcore/calayer/1410901-filters) 属性包含一个滤镜数组，仅影响图层的前景内容。
- [backgroundFilters](https://developer.apple.com/documentation/quartzcore/calayer/1410827-backgroundfilters) 属性包含一个滤镜数组，仅影响图层的背景内容。
- [compositingFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410748-compositingfilter) 属性定义了图层的前景内容和背景内容要如何合成在一起。

要为图层添加滤镜，你必须先定位并创建 `CIFilter` 对象，然后在把它添加到图层之前对其进行配置。`CIFilter` 类包含若干用于定位可用 Core Image 滤镜的类方法，例如 [filterWithName:](https://developer.apple.com/documentation/coreimage/cifilter/1438255-filterwithname) 方法。不过，创建滤镜只是第一步。许多滤镜都有一些参数用来定义该滤镜如何修改图像。例如，方框模糊滤镜有一个输入半径参数，用于影响所应用的模糊程度。在配置滤镜的过程中，你应当始终为这些参数提供值。不过，有一个常见的参数你不需要指定，那就是输入图像，它由图层自身提供。

在为图层添加滤镜时，最好在把滤镜添加到图层之前就配置好滤镜参数。这样做的主要原因是：一旦添加到图层上，你就无法再修改 `CIFilter` 对象本身了。不过，你可以使用图层的 [setValue:forKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1418139-setvalue) 方法在事后更改滤镜的值。

清单 2-6 展示了如何创建一个挤压变形滤镜并将其应用到图层对象上。该滤镜会将图层的源像素向内挤压，离指定中心点最近的像素变形程度最大。请注意，在这个示例中你不需要为滤镜指定输入图像，因为图层的图像会被自动使用。

__清单 2-6__  为图层应用滤镜

```objc
CIFilter* aFilter = [CIFilter filterWithName:@"CIPinchDistortion"];
[aFilter setValue:[NSNumber numberWithFloat:500.0] forKey:@"inputRadius"];
[aFilter setValue:[NSNumber numberWithFloat:1.25] forKey:@"inputScale"];
[aFilter setValue:[CIVector vectorWithX:250.0 Y:150.0] forKey:@"inputCenter"];

myLayer.filters = [NSArray arrayWithObject:aFilter];
```

关于可用 Core Image 滤镜的信息，请参阅 _[Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346)_。

在 OS X 中，图层支撑视图支持几种不同的策略，用来决定何时更新底层图层的内容。由于原生的 AppKit 绘制模型与 Core Animation 引入的绘制模型之间存在差异，这些策略让你更容易把旧代码迁移到 Core Animation 上。你可以逐个视图配置这些策略，以确保每个视图都能获得最佳性能。

每个视图都定义了一个 [layerContentsRedrawPolicy](https://developer.apple.com/documentation/appkit/nsview/1483514-layercontentsredrawpolicy) 方法，用来返回该视图图层的重绘策略。你可以使用 [setLayerContentsRedrawPolicy:](https://developer.apple.com/documentation/appkit/nsview/1483514-layercontentsredrawpolicy) 方法来设置该策略。为了保持与其传统绘制模型的兼容性，AppKit 默认会把重绘策略设为 [NSViewLayerContentsRedrawDuringViewResize](https://developer.apple.com/documentation/appkit/nsview/layercontentsredrawpolicy/duringviewresize)。不过，你可以把该策略更改为表 2-2 中的任意一个值。请注意，推荐使用的重绘策略并不是默认策略。

__表 2-2__  OS X 视图的图层重绘策略

| 策略 | 用途 |
| --- | --- |
| [NSViewLayerContentsRedrawOnSetNeedsDisplay](https://developer.apple.com/documentation/appkit/nsviewlayercontentsredrawpolicy/nsviewlayercontentsredrawonsetneedsdisplay) | 这是推荐使用的策略。采用这种策略时，视图的几何属性变化不会自动导致视图更新其图层的内容。取而代之的是，图层现有的内容会被拉伸和处理以适应几何属性的变化。要强制视图重绘自身并更新图层的内容，你必须显式调用视图的 [setNeedsDisplay:](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay) 方法。  该策略最贴近 Core Animation 图层的标准行为。不过，它并不是默认策略，必须显式设置。 |
| [NSViewLayerContentsRedrawDuringViewResize](https://developer.apple.com/documentation/appkit/nsview/layercontentsredrawpolicy/duringviewresize) | 这是默认的重绘策略。该策略通过在视图的几何属性发生变化时重新缓存图层的内容，最大限度地保持与传统 AppKit 绘制方式的兼容性。这种行为会导致在调整大小的操作过程中，视图的 `drawRect:` 方法在应用的主线程上被多次调用。 |
| [NSViewLayerContentsRedrawBeforeViewResize](https://developer.apple.com/documentation/appkit/nsview/layercontentsredrawpolicy/beforeviewresize) | 采用这种策略时，AppKit 会在任何调整大小的操作之前，先以图层的最终尺寸进行绘制，并缓存该位图。调整大小的操作会以缓存的位图作为起始图像，将其缩放以适配旧的 bounds 矩形，然后再将该位图动画过渡到其最终尺寸。这种行为可能会导致视图的内容在动画开始时显得被拉伸或变形，在初始外观不重要或不明显的场景下，这种策略表现更好。 |
| [NSViewLayerContentsRedrawNever](https://developer.apple.com/documentation/appkit/nsviewlayercontentsredrawpolicy/nsviewlayercontentsredrawnever) | 采用这种策略时，即使你调用了 [setNeedsDisplay:](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay) 方法，AppKit 也完全不会更新图层。这种策略最适合内容从不改变、且视图尺寸即便会变化也十分罕见的视图。例如，你可以将其用于显示固定尺寸内容或背景元素的视图。 |

视图重绘策略减轻了为提升绘制性能而使用独立子图层的需要。在引入视图重绘策略之前，有些图层支撑视图会以超出实际需要的频率进行绘制，从而导致性能问题。当时对这类性能问题的解决方案，是使用子图层来呈现视图内容中不需要经常重绘的那些部分。随着重绘策略在 OS X v10.6 中的引入，现在推荐的做法是为图层支撑视图的重绘策略设置一个适当的值，而不是显式创建子图层层级结构。

[CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation) 和 [CALayer](https://developer.apple.com/documentation/quartzcore/calayer) 类扩展了键值编码（key-value coding）约定，以支持自定义属性。你可以利用这一行为向图层添加数据，并使用你自定义的键来获取这些数据。你甚至可以为自定义属性关联动作（action），这样当你更改该属性时，就会执行相应的动画。

关于如何设置和获取自定义属性的信息，请参阅 [Key-Value Coding Compliant Container Classes](Key-Value%20Coding%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjsfvjvomy)。关于如何为图层对象添加动作的信息，请参阅 [Changing a Layer’s Default Behavior](Changing%20a%20Layer%E2%80%99s%20Default%20Behavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqnznknltc)。

在打印过程中，图层会按需重绘其内容，以适应打印环境。虽然 Core Animation 在渲染到屏幕时通常依赖缓存的位图，但在打印时它会重新绘制该内容。具体来说，如果某个图层支撑视图使用 `drawRect:` 方法来提供图层内容，Core Animation 会在打印期间再次调用 `drawRect:`，以生成用于打印的图层内容。

[下一页](Animating%20Layer%20Content.md)[上一页](Core%20Animation%20Basics.md)

