---
title: iOS Collection View 编程指南
apple_id: TP40012334
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/CollectionViewPGforIOS/CreatingCustomLayouts/CreatingCustomLayouts.html
archived_at: '2026-07-18T02:22:39.764609Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS Collection View 编程指南](About%20iOS%20Collection%20Views.md)


[下一页](Custom%20Layouts-%20A%20Worked%20Example.md)[上一页](Incorporating%20Gesture%20Support.md)

# 创建自定义布局

在着手构建自定义布局之前，先想清楚这么做是否真有必要。[UICollectionViewFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout) 类提供了大量已经过效率优化的行为，并且可以通过多种方式加以调整，实现许多不同类型的标准布局。只有在以下情形下，才值得考虑实现自定义布局：

- 你想要的布局完全不像网格，也不像基于行的断行布局（这类布局会不断把项目放进一行，直到该行放满，然后继续排到下一行，直至所有项目都被放置完毕），或者它必须支持在多个方向上滚动。
- 你需要频繁地改变所有单元格的位置，频繁到修改现有流式布局比创建一个自定义布局还费事。

好消息是，从 API 的角度看，实现自定义布局并不难。最难的部分是完成确定布局中各项目位置所需的计算。一旦你知道了这些项目的位置，把这些信息提供给 collection view 就很直接了。

要做自定义布局，你需要对 [UICollectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionviewlayout) 派生子类，它为你的设计提供了一个全新的起点。其中只有少数几个方法提供了布局对象的核心行为，是你的实现中必需的。其余方法则供你按需重写，用来微调布局行为。核心方法负责以下几项关键任务：

- 指定可滚动内容区域的尺寸。
- 为构成你布局的单元格和视图提供属性对象，以便 collection view 能够摆放每一个单元格和视图。

尽管只实现这些核心方法就能得到一个可用的布局对象，但如果你同时实现若干可选方法，你的布局往往会更吸引人。

布局对象利用数据源提供的信息来创建 collection view 的布局。你的布局通过调用 [collectionView](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617751-collectionview) 属性上的方法与数据源通信，该属性在布局的所有方法中都可以访问。请留意在布局过程中 collection view 知道什么、不知道什么。因为布局过程正在进行，collection view 无法跟踪视图的布局或位置。所以，尽管布局对象并不会阻止你调用 collection view 的任何方法，但除了计算布局所必需的数据之外，不要依赖 collection view 提供其他任何东西。

Collection view 会直接与你的自定义布局对象协作，管理整个布局过程。当 collection view 判定自己需要布局信息时，就会要求你的布局对象提供。例如，collection view 在首次显示或被调整大小时会索取布局信息。你也可以通过调用布局对象的 [invalidateLayout](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617728-invalidatelayout) 方法，显式地告诉 collection view 更新其布局。该方法会丢弃已有的布局信息，强制布局对象生成新的布局信息。

在布局过程中，collection view 会调用你布局对象的一些特定方法。这些方法就是你计算项目位置、并向 collection view 提供其所需主要信息的机会。其他方法也可能被调用，但下面这些方法在布局过程中总是按以下顺序被调用：

1. 用 [prepareLayout](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617752-preparelayout) 方法执行提供布局信息所需的前期计算。
2. 用 [collectionViewContentSize](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617796-collectionviewcontentsize) 方法，基于你的初步计算返回整个内容区域的总体尺寸。
3. 用 [layoutAttributesForElementsInRect:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617769-layoutattributesforelementsinrec) 方法返回位于指定矩形内的单元格和视图的属性。

图 5-1 说明了你可以如何用上述方法生成布局信息。

__图 5-1__  排布你的自定义内容

!!

`prepareLayout` 方法是你执行各种计算、确定布局中单元格和视图位置的机会。至少，你应该在这个方法中算出足够的信息，以便能够返回内容区域的总体尺寸——那正是第 2 步中要返回给 collection view 的东西。

Collection view 用这个内容尺寸来恰当地配置它的 scroll view。举例来说，如果你算出的内容尺寸在垂直和水平两个方向上都超出了当前设备屏幕的边界，scroll view 就会做出调整，允许同时在两个方向上滚动。与 `UICollectionViewFlowLayout` 不同，它默认不会为了只在一个方向上滚动而调整内容的布局。

接着，collection view 会根据当前的滚动位置调用你的 `layoutAttributesForElementsInRect:` 方法，索取某个特定矩形内单元格和视图的属性——这个矩形不一定就是可见矩形。返回这些信息之后，核心的布局过程就基本完成了。

布局结束之后，单元格和视图的属性会一直保持不变，直到你或 collection view 使布局失效为止。调用布局对象的 `invalidateLayout` 方法会让布局过程重新开始，从再次调用 `prepareLayout` 方法起步。Collection view 也可能在滚动期间自动使你的布局失效。如果用户滚动其内容，collection view 会调用布局对象的 [shouldInvalidateLayoutForBoundsChange:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617781-shouldinvalidatelayoutforboundsc) 方法，若该方法返回 `YES`，就使布局失效。

你的布局所负责的属性对象是 [UICollectionViewLayoutAttributes](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes) 类的实例。这些实例可以在你应用的多种方法中创建。当你的应用要处理的项目不到成千上万个时，在准备布局时创建这些实例是合理的，因为这样布局信息可以被缓存和引用，而不必临时计算。如果在你的应用中，预先计算全部属性的开销超过了缓存带来的好处，那么在属性被请求的当下再创建它们同样简单。

无论如何，当你创建 `UICollectionViewLayoutAttributes` 类的新实例时，请使用下列类方法之一：

- [layoutAttributesForCellWithIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617759-layoutattributesforcellwithindex)
- [layoutAttributesForSupplementaryViewOfKind:withIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617801-init)
- [layoutAttributesForDecorationViewOfKind:withIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617786-layoutattributesfordecorationvie)

你必须根据所显示视图的类型选用正确的类方法，因为 collection view 会依据这个信息向数据源对象请求相应类型的视图。用错方法会导致 collection view 在错误的位置创建错误的视图，你的布局也就不会呈现出预期的样子。

创建好每个属性对象之后，为对应的视图设置相关属性。至少要设置视图在布局中的尺寸和位置。如果你的布局中存在视图重叠的情况，请为 [zIndex](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617768-zindex) 属性赋值，以确保重叠视图之间有确定的次序。其他属性让你可以控制单元格或视图的可见性与外观，可按需修改。如果标准的属性类不能满足你应用的需要，你可以对它派生子类并加以扩展，以存储关于每个视图的其他信息。对布局属性派生子类时，你必须实现 [isEqual:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/isEqual:) 方法来比较你的自定义属性，因为 collection view 的某些操作会用到这个方法。

有关布局属性的更多信息，请参阅 _[UICollectionViewLayoutAttributes Class Reference](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes)_。

在布局周期开始时，布局对象会在正式进入布局过程之前调用 `prepareLayout`。这个方法是你计算各种信息、为之后的布局提供依据的机会。实现自定义布局并不要求必须实现 `prepareLayout` 方法，它只是在必要时提供一个做初步计算的机会。这个方法被调用之后，你的布局必须掌握足够的信息来计算 collection view 的内容尺寸——那是布局过程的下一步。不过，这里所说的「信息」可以少到只满足上述最低要求，也可以多到创建并存储你布局将要用到的全部布局属性对象。如何使用 `prepareLayout` 方法，取决于你应用的架构，以及哪些东西预先计算更合理、哪些东西按需计算更合理。有关 `prepareLayout` 方法大致长什么样的示例，请参阅[准备布局](Custom%20Layouts-%20A%20Worked%20Example.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqobnknltc)。

在布局过程的最后一步中，collection view 会调用你布局对象的 `layoutAttributesForElementsInRect:` 方法。这个方法的目的是为与指定矩形相交的每一个单元格、每一个补充视图或装饰视图提供布局属性。对于很大的可滚动内容区域，collection view 可能只索取该内容区域中当前可见部分内那些项目的属性。在图 5-2 中，当前可见、需要你的布局对象为之创建属性对象的内容是第 6 到第 20 个单元格以及第二个页眉视图。你必须做好准备，为 collection view 内容区域的任何部分提供布局属性。这些属性可能被用于辅助被插入或被删除项目的动画。

__图 5-2__  只排布可见的视图

!

由于 `layoutAttributesForElementsInRect:` 方法是在你布局对象的 `prepareLayout` 方法之后被调用的，你应该已经掌握了返回或创建所需属性的大部分信息。你的 `layoutAttributesForElementsInRect:` 方法实现遵循以下步骤：

1. 遍历 `prepareLayout` 方法生成的数据，从中取出已缓存的属性，或者创建新的属性。
2. 检查每个项目的 frame，看它是否与传给 `layoutAttributesForElementsInRect:` 方法的矩形相交。
3. 对每一个相交的项目，把对应的 `UICollectionViewLayoutAttributes` 对象添加到一个数组中。
4. 把这个布局属性数组返回给 collection view。

根据你管理布局信息的方式，你可以在 `prepareLayout` 方法中创建 `UICollectionViewLayoutAttributes` 对象，也可以等到 `layoutAttributesForElementsInRect:` 方法里再创建。在设计符合你应用需求的实现时，别忘了缓存布局信息带来的好处。反复为单元格计算新的布局属性是一项开销很大的操作，会对你应用的性能造成明显的负面影响。话虽如此，当你的 collection view 管理的项目数量很大时，在被请求时才创建布局属性可能（从性能上看）更合理。这纯粹是一个判断哪种策略最适合你应用的问题。

有关如何实现 `layoutAttributesForElementsInRect:` 的具体示例，请参阅[提供布局属性](Custom%20Layouts-%20A%20Worked%20Example.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqobnknlts)。

在正式的布局过程之外，collection view 还会不时要求你的布局对象为单个项目提供属性。例如，collection view 在为某个项目配置插入和删除动画时就会索取这类信息。你的布局对象必须做好准备，为它所支持的每一个单元格、补充视图和装饰视图提供布局属性。为此，你要重写以下方法：

- [layoutAttributesForItemAtIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617797-layoutattributesforitematindexpa)
- [layoutAttributesForSupplementaryViewOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617792-layoutattributesforsupplementary)
- [layoutAttributesForDecorationViewOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617809-layoutattributesfordecorationvie)

你对这些方法的实现应当取回给定单元格或视图的当前布局属性。每个自定义布局对象都应实现 `layoutAttributesForItemAtIndexPath:` 方法。如果你的布局不包含任何补充视图，就不需要重写 `layoutAttributesForSupplementaryViewOfKind:atIndexPath:` 方法。同样，如果它不包含装饰视图，也不需要重写 `layoutAttributesForDecorationViewOfKind:atIndexPath:` 方法。返回属性时，你不应该更新布局属性。如果你需要改变布局信息，请使布局对象失效，让它在随后的布局周期中更新这些数据。

把你的自定义布局关联到 collection view 有两种方式：通过代码，或者通过 storyboard。Collection view 通过一个可写的属性 [collectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionview/1618047-collectionviewlayout) 与它的布局关联。要把布局设为你的自定义实现，就把 collection view 的 layout 属性设为你自定义布局对象的一个实例。清单 5-1 展示了所需的那行代码。

__清单 5-1__  关联你的自定义布局

```objc
self.collectionView.collectionViewLayout = [[MyCustomLayout alloc] init];
```

另一种方式是，在你的 storyboard 中打开 Document Outline 面板并选中你的 collection view（它列在你的 controller 的下拉菜单中）。选中 collection view 后，打开 Utilities 面板中的 Attributes inspector，在标有 Collection View 的那一节下面，把 Layout 选项从 Flow 改为 Custom。它下面的选项会从 Scroll Direction 变成 Class，此时你就可以选择你的自定义布局类了。

在布局过程中为每个单元格和视图提供布局属性是必需的，但还有一些其他行为可以改善用户使用你自定义布局时的体验。实现这些行为是可选的，但建议实现。

补充视图独立于 collection view 的单元格之外，拥有自己的一套布局属性。和单元格一样，这些视图也由数据源对象提供，但它们的作用是衬托你应用的主要内容。例如，`UICollectionViewFlowLayout` 用补充视图来实现 section 页眉和页脚。另一个应用则可能用补充视图给每个单元格配一个文本标签，用来显示关于该单元格的信息。与 collection view 单元格一样，补充视图也会经历回收过程，以优化 collection view 所占用的资源量。因此，你应用中用到的所有补充视图都应当派生自 [UICollectionReusableView](https://developer.apple.com/documentation/uikit/uicollectionreusableview) 类。

为你的布局添加补充视图的步骤如下：

1. 用 [registerClass:forSupplementaryViewOfKind:withReuseIdentifier:](https://developer.apple.com/documentation/uikit/uicollectionview/1618103-register) 或 [registerNib:forSupplementaryViewOfKind:withReuseIdentifier:](https://developer.apple.com/documentation/uikit/uicollectionview/1618101-registernib) 方法把你的补充视图注册到 collection view 的布局对象上。
2. 在你的数据源中实现 [collectionView:viewForSupplementaryElementOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/1618037-collectionview)。由于这些视图是可复用的，请调用 [dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionview/1618068-dequeuereusablesupplementaryview) 取出（或创建）一个新的可复用视图，并在返回它之前设置好所有必要的数据。
3. 像为单元格创建布局属性对象那样，为你的补充视图创建布局属性对象。
4. 把这些布局属性对象包含进 `layoutAttributesForElementsInRect:` 方法所返回的属性数组中。
5. 实现 `layoutAttributesForSupplementaryViewOfKind:atIndexPath:` 方法，以便在被查询时返回指定补充视图的属性对象。

在自定义布局中为补充视图创建属性对象的过程与为单元格创建的过程几乎相同，区别在于：一个自定义布局可以有多种类型的补充视图，但只能有一种类型的单元格。这是因为补充视图的用途是衬托主要内容，因而是独立于主要内容之外的。一个应用的内容可以有许多种被衬托的方式，所以补充视图的每个方法都会指明当前处理的是哪一种视图，以便与其他种类区分开，让你的布局能够依据类型正确地计算其属性。注册补充视图以供使用时，你提供的字符串会被布局对象用来把该视图与其他视图区分开。有关把补充视图整合进自定义布局的示例，请参阅[加入补充视图](Custom%20Layouts-%20A%20Worked%20Example.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqobnknlte)。

装饰视图是用来增强 collection view 布局外观的视觉装饰。与单元格和补充视图不同，装饰视图只提供视觉内容，因此与数据源无关。你可以用它们提供自定义背景、填充单元格周围的空隙，甚至在你需要时遮挡单元格。装饰视图完全由布局对象定义和管理，不与 collection view 的数据源对象发生交互。

要为你的布局添加装饰视图，请执行以下操作：

1. 用 [registerClass:forDecorationViewOfKind:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617739-registerclass) 或 [registerNib:forDecorationViewOfKind:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617732-registernib) 方法把你的装饰视图注册到布局对象上。虽然这一做法与注册单元格和补充视图类似，但要记住，装饰视图是注册在布局对象里，而不是数据源里。
2. 在你布局对象的 `layoutAttributesForElementsInRect:` 方法中，像为单元格和补充视图那样为你的装饰视图创建属性。
3. 在你的布局对象中实现 [layoutAttributesForDecorationViewOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617809-layoutattributesfordecorationvie) 方法，在被询问时返回装饰视图的属性。
4. 可选地，实现 [initialLayoutAttributesForAppearingDecorationElementOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617726-initiallayoutattributesforappear) 和 [finalLayoutAttributesForDisappearingDecorationElementOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617762-finallayoutattributesfordisappea) 方法，以处理装饰视图出现和消失时的动画。更多信息请参阅[让插入和删除动画更有趣](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltcmy)

装饰视图的创建过程与单元格和补充视图的过程不同。你只需注册一个类或 nib 文件，就足以确保装饰视图在需要时被创建出来。由于它们纯粹是视觉性的，装饰视图除了所提供的 nib 文件中已完成的配置、或对象 [initWithFrame:](https://developer.apple.com/documentation/uikit/uiview/1622488-init) 方法中已完成的配置之外，不应再需要任何配置。正因如此，当需要某个装饰视图时，collection view 会替你创建它，并应用布局对象提供的属性。所有装饰视图仍应是 `UICollectionReusableView` 的子类，因为布局对象对它的装饰视图也采用了回收机制。

插入和删除单元格与视图给布局带来了一个有趣的难题。插入一个单元格可能导致其他单元格和视图的布局发生变化。尽管布局对象知道如何把已有的单元格和视图从当前位置动画移动到新位置，但对于正被插入的那个单元格，它并没有当前位置。Collection view 没有选择不带动画地插入新单元格，而是要求布局对象提供一组用于动画的初始属性。同样，当一个单元格被删除时，collection view 会要求布局对象提供一组最终属性，作为各种动画的终点。

要理解初始属性是怎么回事，看一个例子会很有帮助。起始布局（图 5-3）展示了一个最初只包含三个单元格的 collection view。当一个新单元格被插入时，collection view 会要求布局对象为这个正被插入的单元格提供初始属性。在这个例子中，布局对象把该单元格的初始位置设为 collection view 的中央，并把它的 alpha 值设为 0 使其隐藏。在动画过程中，这个新单元格看上去就会一边淡入，一边从 collection view 的中央移动到它在右下角的最终位置。

__图 5-3__  为一个即将出现在屏幕上的项目指定初始属性

!

清单 5-2 展示了你可以用来为图 5-3 中被插入单元格指定初始属性的代码。该方法把单元格的位置设为 collection view 的中心，并让它变透明。随后，布局对象会在常规布局过程中提供该单元格的最终位置和 alpha 值。

__清单 5-2__  为被插入的单元格指定初始属性

```objc
- (UICollectionViewLayoutAttributes *)initialLayoutAttributesForAppearingItemAtIndexPath:(NSIndexPath *)itemIndexPath {
   UICollectionViewLayoutAttributes* attributes = [self layoutAttributesForItemAtIndexPath:itemIndexPath];
   attributes.alpha = 0.0;

   CGSize size = [self collectionView].frame.size;
   attributes.center = CGPointMake(size.width / 2.0, size.height / 2.0);
   return attributes;
}
```

处理删除的过程与处理插入的过程完全相同，只不过你指定的是最终属性而不是初始属性。沿用前面的例子，如果你用与插入单元格时相同的属性，那么删除该单元格就会让它一边淡出、一边移向 collection view 的中央。`UICollectionViewLayout` 类中共有六个可用方法——为项目、补充视图和装饰视图各提供两个独立的方法（分别对应初始属性和最终属性）。

你的自定义布局对象可以影响 collection view 的滚动行为，从而带来更好的用户体验。当与滚动相关的触摸事件结束时，scroll view 会根据当前速度和生效的减速率来确定滚动内容的最终停靠位置。当 collection view 知道了这个位置，它会调用布局对象的 [targetContentOffsetForProposedContentOffset:withScrollingVelocity:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617729-targetcontentoffset) 方法，询问该位置是否应当被修改。由于它是在底层内容仍在移动时调用这个方法的，你的自定义布局便能影响滚动内容的最终停靠点。

图 5-4 演示了你可以如何用布局对象改变 collection view 的滚动行为。假设 collection view 的偏移量从 (0, 0) 开始，而用户向左滑动。Collection view 会算出滚动自然停止的位置，并把这个值作为「建议的」内容偏移量提供出来。你的布局对象可以修改这个建议值，以确保滚动停止时恰好有一个项目在 collection view 的可见边界内居中。这个新值就成了目标内容偏移量，也就是你要从 `targetContentOffsetForProposedContentOffset:withScrollingVelocity:` 方法中返回的值。

__图 5-4__  把建议的内容偏移量改成更合适的值

!

以下是实现自定义布局对象的一些提示和建议：

- 考虑用 `prepareLayout` 方法创建并存储你之后需要的 `UICollectionViewLayoutAttributes` 对象。Collection view 迟早会索取布局属性对象，所以在某些情况下预先创建并存储它们是合理的。如果你的项目数量相对较少（几百个），或者这些项目的实际布局属性很少变化，那就尤其如此。

  不过，如果你的布局需要管理成千上万个项目，你就要权衡缓存与重新计算孰优孰劣。对于尺寸可变、布局又很少变化的项目，缓存通常能省去定期重新计算复杂布局信息的必要。对于数量庞大的固定尺寸项目，按需计算属性可能反而更简单。而对于属性频繁变化的项目，你可能无论如何都要一直重新计算，所以缓存反而只会额外占用内存空间。
- 避免对 `UICollectionView` 派生子类。Collection view 自身几乎没有任何外观。相反，它从你的数据源对象获取全部视图，从布局对象获取全部与布局相关的信息。如果你想在三维空间中排布项目，正确的做法是实现一个自定义布局，为每个单元格和视图恰当地设置 3D 变换。
- 绝不要在你自定义布局对象的 `layoutAttributesForElementsInRect:` 方法中调用 `UICollectionView` 的 [visibleCells](https://developer.apple.com/documentation/uikit/uicollectionview/1618056-visiblecells) 方法。除了布局对象告诉它的之外，collection view 对项目位于何处一无所知。因此，向它索要可见单元格，只会把这个请求转发回你的布局对象。

  你的布局对象应当始终知道各项目在内容区域中的位置，并且能够随时返回这些项目的属性。在大多数情况下，它应该自行完成这件事。只有在少数情况下，布局对象才可能依赖数据源中的信息来摆放项目。例如，一个在地图上显示项目的布局，可能会从数据源取回每个项目的地图位置。

[下一页](Custom%20Layouts-%20A%20Worked%20Example.md)[上一页](Incorporating%20Gesture%20Support.md)

