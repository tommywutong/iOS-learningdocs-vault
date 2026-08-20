---
title: Core Animation 编程指南
apple_id: TP40004514
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/CoreAnimationBasics/CoreAnimationBasics.html
archived_at: '2026-07-15T07:13:57.323562Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Core Animation 编程指南](About%20Core%20Animation.md)


[下一页](Setting%20Up%20Layer%20Objects.md)[上一页](About%20Core%20Animation.md)

# Core Animation 基础

Core Animation 提供了一套通用系统，用来为 app 的视图和其他可视元素添加动画。Core Animation 并不是要取代 app 的视图，而是一种与视图集成的技术，用来为视图内容的动画提供更好的性能和支持。它实现这一效果的方式是把视图的内容缓存为位图，让图形硬件可以直接对其进行操作。在某些情况下，这种缓存行为可能需要你重新思考如何呈现和管理 app 的内容，但大多数时候你使用 Core Animation 时根本感觉不到它的存在。除了缓存视图内容之外，Core Animation 还定义了一种方式，让你能够指定任意的可视内容、把这些内容与视图集成起来，并像其他内容一样为其添加动画。

你使用 Core Animation 为 app 的视图和可视对象的变化添加动画。大多数变化都与修改可视对象的属性有关。例如，你可能会用 Core Animation 为视图 position、大小或不透明度的变化添加动画。当你做出这类改变时，Core Animation 会在该属性的当前值和你指定的新值之间产生动画过渡。你通常不会用 Core Animation 以每秒 60 次的频率替换视图的内容（就像卡通动画那样）。相反，你会用 Core Animation 在屏幕上移动视图的内容、让内容淡入淡出、对视图应用任意的图形变换，或者改变视图的其他视觉属性。

_图层对象_是组织在 3D 空间中的 2D 表面，是你用 Core Animation 所做一切事情的核心。和视图一样，图层也管理着关于其表面的几何属性、内容和视觉属性的信息。但与视图不同的是，图层并不定义自己的外观。图层仅仅管理着围绕一张位图的状态信息。这张位图本身可能是某个视图自行绘制的结果，也可能是你指定的一张固定图像。正因如此，你在 app 中用到的主要图层被视为模型对象，因为它们主要负责管理数据。记住这一点很重要，因为它会影响动画的行为方式。

大多数图层在你的 app 中并不进行任何实际的绘制。相反，图层会捕获 app 提供的内容，并将其缓存到一张位图中，这张位图有时被称为_后备存储（backing store）_。当你随后修改图层的某个属性时，你实际上只是在修改与该图层对象关联的状态信息。当某次变化触发了一个动画时，Core Animation 会把图层的位图和状态信息传递给图形硬件，由图形硬件根据新的信息完成位图的渲染工作，如图 1-1 所示。在硬件中操作位图，比用软件实现要快得多。

__图 1-1__  Core Animation 如何绘制内容

!!

由于图层操作的是静态位图，基于图层的绘制方式与更传统的基于视图的绘制技术有很大不同。在基于视图的绘制方式中，视图本身的变化通常会导致调用视图的 `drawRect:` 方法，用新参数重新绘制内容。但这种绘制方式代价高昂，因为它是在主线程上用 CPU 完成的。Core Animation 尽可能地避免了这种开销，做法是在硬件中操作缓存的位图，以达到相同或类似的效果。

尽管 Core Animation 会尽可能地使用已缓存的内容，但你的 app 仍然必须提供初始内容，并不时对其进行更新。app 为图层对象提供内容有几种方式，详见[提供图层的内容](Setting%20Up%20Layer%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjtfvjvona)。

图层对象的数据和状态信息，与该图层内容在屏幕上的视觉呈现是相互解耦的。这种解耦让 Core Animation 有机会介入其中，为从旧状态值到新状态值的变化添加动画。例如，改变图层的 position 属性会让 Core Animation 把图层从当前 position 移动到新指定的 position。对其他属性做类似的改动，也会触发相应的动画。图 1-2 展示了几种你可以在图层上执行的动画类型。关于会触发动画的图层属性列表，请参阅[可添加动画的属性](Animatable%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomi)。

__图 1-2__  你可以对图层执行的动画示例

!

在动画进行的过程中，Core Animation 会替你在硬件中完成所有逐帧的绘制工作。你所要做的只是指定动画的起点和终点，剩下的交给 Core Animation 处理。你也可以按需指定自定义的时间信息和动画参数；不过，如果你不指定，Core Animation 也会提供合适的默认值。

关于如何发起动画和配置动画参数的更多信息，请参阅[为图层内容添加动画](Animating%20Layer%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmznknltc)。

图层的职责之一，是管理其内容的可视几何属性。可视几何属性包括内容 bounds 的信息、内容在屏幕上的 position，以及图层是否被旋转、缩放或以某种方式做了变换。和视图一样，图层也有 frame 和 bounds 矩形，你可以用它们来定位图层及其内容。图层还拥有视图所没有的其他属性，比如锚点（anchor point），它定义了各种操作围绕其发生的那个点。指定图层几何属性某些方面的方式，也与指定视图相应信息的方式不同。

图层同时使用_基于点的坐标系统_和_单位坐标系统_来指定内容的位置。使用哪一种坐标系统，取决于所传达信息的类型。当指定的值直接映射到屏幕坐标，或者必须相对于另一个图层来指定时（例如图层的 `position` 属性），就使用基于点的坐标。当某个值不应该与屏幕坐标绑定、而是相对于其他某个值时，就使用单位坐标。例如，图层的 [anchorPoint](https://developer.apple.com/documentation/quartzcore/calayer/1410817-anchorpoint) 属性指定的就是一个相对于图层自身 bounds 的点，而这个 bounds 是可以变化的。

基于点的坐标最常见的用途之一，就是指定图层的大小和 position，你可以通过图层的 [bounds](https://developer.apple.com/documentation/quartzcore/calayer/1410915-bounds) 和 [position](https://developer.apple.com/documentation/quartzcore/calayer/1410791-position) 属性来做到这一点。`bounds` 定义了图层自身的坐标系统，并涵盖了图层在屏幕上的大小。`position` 属性定义的是图层相对于其父图层坐标系统的位置。虽然图层也有一个 `frame` 属性，但该属性实际上是由 `bounds` 和 `position` 属性的值派生出来的，使用频率较低。

图层的 `bounds` 和 `frame` 矩形的朝向，始终与底层平台的默认朝向一致。图 1-3 展示了 bounds 矩形在 iOS 和 OS X 上的默认朝向。在 iOS 中，bounds 矩形的原点默认位于图层的左上角，而在 OS X 中则位于左下角。如果你在 app 的 iOS 版本和 OS X 版本之间共享 Core Animation 代码，就必须考虑到这些差异。

__图 1-3__  iOS 和 OS X 上默认的图层几何结构

!

[图 1-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmrnknlte) 中值得注意的一点是，`position` 属性位于图层的正中央。该属性正是几个会随着图层 [anchorPoint](https://developer.apple.com/documentation/quartzcore/calayer/1410817-anchorpoint) 属性值变化而改变含义的属性之一。锚点表示某些坐标的起算点，[锚点如何影响几何操作](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmrnknltcny)中有更详细的说明。

锚点是你用单位坐标系统指定的几个属性之一。Core Animation 用单位坐标来表示那些值可能随图层大小变化而变化的属性。你可以把单位坐标理解为总可能值的百分比。单位坐标空间中的每个坐标的取值范围都是 `0.0` 到 `1.0`。例如，沿 x 轴，左边缘的坐标为 `0.0`，右边缘的坐标为 `1.0`。沿 y 轴，单位坐标值的朝向会因平台而异，如图 1-4 所示。

__图 1-4__  iOS 和 OS X 上默认的单位坐标系

!

无论是点坐标还是单位坐标，所有坐标值都以浮点数的形式指定。使用浮点数让你能够指定精确的位置，这些位置可能落在常规坐标值之间。使用浮点值很方便，尤其是在打印时，或者在向 Retina 显示屏绘制、一个点可能由多个像素表示的情况下。浮点值让你可以不必考虑底层设备的分辨率，只需按你需要的精度指定数值即可。

图层的几何相关操作，都是相对于该图层的锚点发生的，你可以通过图层的 [anchorPoint](https://developer.apple.com/documentation/quartzcore/calayer/1410817-anchorpoint) 属性来访问锚点。锚点的影响在操作图层的 `position` 或 [transform](https://developer.apple.com/documentation/quartzcore/calayer/1410836-transform) 属性时最为明显。position 属性总是相对于图层的锚点来指定的，你对图层应用的任何变换，也同样是相对于锚点发生的。

图 1-5 演示了把锚点从默认值改为其他值时，会如何影响图层的 `position` 属性。即使图层在其父图层的 bounds 内并没有移动，把锚点从图层的中心移动到图层 bounds 的原点，也会改变 `position` 属性的值。

__图 1-5__  锚点如何影响图层的 position 属性

!

图 1-6 展示了改变锚点会如何影响应用到图层上的变换。当你对图层应用旋转变换时，旋转是围绕锚点发生的。由于锚点默认设置在图层的正中央，这通常会产生你所预期的那种旋转行为。但是，如果你改变了锚点，旋转的结果就会不同。

__图 1-6__  锚点如何影响图层变换

!

每个图层都有两个变换矩阵，你可以用它们来操作图层及其内容。`CALayer` 的 [transform](https://developer.apple.com/documentation/quartzcore/calayer/1410836-transform) 属性指定的是你想同时应用到图层本身及其内嵌子图层上的变换。通常，当你想修改图层本身时，会使用这个属性。例如，你可以用这个属性来缩放或旋转图层，或临时改变它的 position。[sublayerTransform](https://developer.apple.com/documentation/quartzcore/calayer/1410888-sublayertransform) 属性定义的是仅应用于子图层的额外变换，最常用于给场景内容添加透视的视觉效果。

变换的工作原理是把坐标值与一个数字矩阵相乘，得到代表原始点变换后版本的新坐标。由于 Core Animation 的数值可以用三维方式指定，每个坐标点都有四个值，必须与一个四行四列的矩阵相乘，如图 1-7 所示。在 Core Animation 中，该图中的变换用 [CATransform3D](https://developer.apple.com/documentation/quartzcore/catransform3d) 类型表示。幸运的是，你不必直接修改这个结构体的字段来执行标准变换。Core Animation 提供了一整套用于创建缩放、平移和旋转矩阵的函数，也提供了用于比较矩阵的函数。除了用函数操作变换之外，Core Animation 还扩展了键值编码支持，让你可以使用键路径来修改变换。关于可以修改的键路径列表，请参阅 [CATransform3D 键路径](Key-Value%20Coding%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjsfvjvomi)。

__图 1-7__  使用矩阵运算转换坐标

!

图 1-8 展示了一些常见变换对应的矩阵配置。任意坐标乘以单位变换，得到的结果都与原坐标完全相同。对于其他变换，坐标被如何修改完全取决于你改变了哪些矩阵分量。例如，若只想沿 x 轴平移，你需要为平移矩阵的 `tx` 分量提供一个非零值，同时把 `ty` 和 `tz` 保持为 0。对于旋转，你需要提供目标旋转角度对应的正弦值和余弦值。

__图 1-8__  常见变换的矩阵配置

!

关于用来创建和操作变换的函数，请参阅 _Core Animation Function Reference_。

一个使用 Core Animation 的 app 拥有三组图层对象。每一组图层对象在让 app 内容显示到屏幕上的过程中，都扮演着不同的角色：

- _模型图层树（model layer tree）_（或简称为"图层树"）中的对象，是你的 app 打交道最多的对象。这棵树中的对象是模型对象，存储着任何动画的目标值。每当你修改某个图层的属性时，你使用的都是这些对象之一。
- _呈现树（presentation tree）_中的对象，包含任何正在运行的动画的中间值。图层树中的对象包含的是动画的目标值，而呈现树中的对象反映的则是这些值在屏幕上呈现时的当前值。你永远不应该修改这棵树中的对象。相反，你应该使用这些对象来读取当前的动画值，比如以这些值为起点创建一个新的动画。
- _渲染树（render tree）_中的对象负责执行实际的动画，它们是 Core Animation 私有的。

每一组图层对象都像 app 中的视图一样被组织成层级结构。事实上，对于一个为所有视图都启用了图层支持的 app 来说，每棵树的初始结构都与视图层级结构完全一致。不过，app 可以按需向图层层级结构中添加额外的图层对象——也就是不与任何视图关联的图层。你可能会在需要为那些不需要视图全部开销的内容优化 app 性能时这样做。图 1-9 展示了一个简单 iOS app 中图层的构成情况。示例中的窗口包含一个内容视图，该内容视图本身又包含一个按钮视图和两个独立的图层对象。每个视图都有一个对应的图层对象，构成图层层级结构的一部分。

__图 1-9__  与窗口关联的图层

!!

对于图层树中的每一个对象，在呈现树和渲染树中都有一个与之对应的对象，如图 1-10 所示。如前所述，app 主要是与图层树中的对象打交道，但有时也可能需要访问呈现树中的对象。具体来说，访问图层树中某个对象的 [presentationLayer](https://developer.apple.com/documentation/quartzcore/calayer/1410744-presentation) 属性，会返回呈现树中与之对应的那个对象。你可能想要访问该对象，来读取某个正处于动画过程中的属性的当前值。

__图 1-10__  某个窗口的图层树

!!

图层并不能取代 app 的视图——也就是说，你不能仅凭图层对象来构建可视界面。图层是为你的视图提供基础设施的。具体来说，图层让绘制和为视图内容添加动画变得更加容易和高效，同时还能在此过程中保持较高的帧率。然而，图层无法做到很多事情。图层不处理事件、不进行内容绘制、不参与响应者链，也做不了许多其他事情。正因如此，每个 app 仍然必须拥有一个或多个视图来处理这些交互。

在 iOS 中，每个视图都由一个对应的图层对象支持，但在 OS X 中，你需要自行决定哪些视图应该拥有图层。在 OS X v10.8 及更高版本中，为所有视图都添加图层可能是合理的做法。不过，你并非必须这样做，在图层带来的开销并非必要的情况下，你仍然可以禁用图层。图层确实会在一定程度上增加 app 的内存开销，但它们带来的好处往往超过这一劣势，所以在禁用图层支持之前，最好先测试一下 app 的性能表现。

当你为某个视图启用图层支持时，你创建的就是所谓的_由图层支持的视图（layer-backed view）_。在由图层支持的视图中，系统负责创建底层的图层对象，并负责让该图层与视图保持同步。所有 iOS 视图都是由图层支持的，OS X 中的大多数视图也是如此。不过，在 OS X 中，你还可以创建一种_承载图层的视图（layer-hosting view）_，即由你自己提供图层对象的视图。对于承载图层的视图，AppKit 对图层的管理采取甩手不管的方式，不会因视图的变化而修改该图层。

除了与视图关联的图层之外，你也可以创建没有对应视图的图层对象。你可以把这些独立的图层对象嵌入到 app 中任何其他图层对象内部，包括那些与视图关联的图层对象。你通常会把独立的图层对象用作某种特定优化手段的一部分。例如，如果你想在多个地方使用同一张图像，可以只加载一次该图像，然后把它关联到多个独立的图层对象上，再把这些对象加入图层树。这样一来，每个图层引用的都是同一份源图像，而不必在内存中为每个图层各自创建一份图像副本。

关于如何为 app 的视图启用图层支持的信息，请参阅[在你的 app 中启用 Core Animation 支持](Setting%20Up%20Layer%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjtfvjvoni)。关于如何创建图层对象层级结构，以及何时应该这样做的建议，请参阅[构建图层层级结构](Building%20a%20Layer%20Hierarchy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqnrnknlte)。

[下一页](Setting%20Up%20Layer%20Objects.md)[上一页](About%20Core%20Animation.md)

