---
title: iOS Collection View 编程指南
apple_id: TP40012334
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/CollectionViewPGforIOS/UsingtheFlowLayout/UsingtheFlowLayout.html
archived_at: '2026-07-18T02:22:42.222091Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS Collection View 编程指南](About%20iOS%20Collection%20Views.md)


[下一页](Incorporating%20Gesture%20Support.md)[上一页](Designing%20Your%20Data%20Source%20and%20Delegate.md)

# 使用流式布局

你可以使用一个具体的布局对象——[UICollectionViewFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout) 类——来排列 collection view 中的项目。流式布局（flow layout）实现的是一种基于行的断行布局，也就是说，布局对象把单元格沿一条线性路径摆放，并在这条线上尽可能多地容纳单元格。当布局对象在当前行上放不下时，它就另起一行，并在新行上继续布局过程。图 3-1 展示了一个垂直滚动的流式布局是什么样子。在这种情况下，各行水平排布，每一新行位于前一行的下方。单个 section 中的单元格还可以选择性地由 section 页眉视图和 section 页脚视图包围起来。

__图 3-1__  使用流式布局排布 section 和单元格

!

你可以用流式布局来实现网格，但它能做的远不止于此。线性布局这一思路可以应用到许多不同的设计中。例如，你可以不做成项目的网格，而是调整间距，让项目沿滚动方向排成单独的一行。项目也可以有不同的尺寸，从而得到比传统网格更不对称、但仍带有线性流动感的排列。可能性有很多。

你既可以通过代码配置流式布局，也可以在 Xcode 中使用 Interface Builder 来配置。配置流式布局的步骤如下：

1. 创建一个流式布局对象，并把它指派给你的 collection view。
2. 配置单元格的宽度和高度。
3. （按需）设置行与项目的间距选项。
4. 如果你需要 section 页眉或 section 页脚，指定它们的尺寸。
5. 设置布局的滚动方向。

流式布局对象暴露了若干属性，用于配置你的内容的外观。设置这些属性后，它们会被同等地应用到布局中的所有项目上。例如，用流式布局对象的 [itemSize](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617711-itemsize) 属性设置单元格尺寸，会让所有单元格具有相同的尺寸。

如果你想动态改变项目的间距或尺寸，可以使用 [UICollectionViewDelegateFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout) [协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)中的方法来实现。你在指派给 collection view 本身的那个[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)上实现这些方法。如果某个方法存在，流式布局对象就会调用该方法，而不再使用它自己持有的固定值。这时，你的实现必须为 collection view 中的所有项目返回合适的值。

如果 collection view 中的所有项目尺寸相同，就把合适的宽度和高度值赋给流式布局对象的 [itemSize](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617711-itemsize) 属性。（项目尺寸始终以点（point）为单位指定。）对于尺寸不变的内容来说，这是配置布局对象最快的方式。

如果你想为单元格指定不同的尺寸，就必须在 collection view 的委托上实现 [collectionView:layout:sizeForItemAtIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617708-collectionview) 方法。你可以利用传入的索引路径信息返回对应项目的尺寸。在布局过程中，流式布局对象会把同一行上的项目在垂直方向上居中对齐，如图 3-2 所示。该行整体的高度或宽度则由这一维度上最大的那个项目决定。

__图 3-2__  流式布局中尺寸各异的项目

!

使用流式布局时，你可以指定同一行上项目之间的最小间距，以及相邻两行之间的最小间距。要记住，你提供的间距只是最小间距。由于流式布局对象自身的内容排布方式，它可能会把项目之间的间距增大到超过你所指定的值。当被布局的项目尺寸各异时，布局对象同样可能增大实际的行间距。

在布局过程中，流式布局对象会不断向当前行添加项目，直到剩余空间不足以容纳一个完整的项目为止。如果这一行的宽度刚好能整齐地容纳若干个项目、没有多余空间，那么项目之间的间距就等于最小间距。如果行末还有多余空间，布局对象就会增大项目间距，直到这些项目在行的边界内均匀分布为止，如图 3-3 所示。增大间距能改善这些项目的整体观感，并避免每行末尾出现大片空白。

__图 3-3__  项目之间的实际间距可能大于最小值

!

对于行间距，流式布局对象采用了与项目间距相同的处理方式。如果所有项目尺寸相同，流式布局就能严格遵守最小行间距值，一行中的所有项目看上去都与下一行的项目保持均匀的间隔。如果项目尺寸各异，各个项目之间的实际间距就可能有所不同。

图 3-4 演示了当项目尺寸各异时，最小行间距会发生什么情况。当项目尺寸不同时，流式布局对象会从每一行中挑出在滚动方向上尺寸最大的那个项目。例如，在垂直滚动的布局中，它会在每一行中找出高度最大的项目。然后把这些项目之间的间距设为最小值。如果这些项目位于行内的不同位置（如图所示），实际看到的行间距就会大于最小值。

__图 3-4__  项目尺寸不同时行间距会有变化

!

与流式布局的其他属性一样，你既可以使用固定的间距值，也可以动态改变这些值。行间距和项目间距是按 section 逐个处理的。因此，给定 section 内所有项目的行间距和项目间距都相同，但不同 section 之间可以不同。你可以通过流式布局对象的 [minimumLineSpacing](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617717-minimumlinespacing) 和 [minimumInteritemSpacing](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/1617706-minimuminteritemspacing) 属性静态地设置间距，也可以通过 collection view 委托的 [collectionView:layout:minimumLineSpacingForSectionAtIndex:](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617705-collectionview) 和 [collectionView:layout:minimumInteritemSpacingForSectionAtIndex:](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/1617696-collectionview) 方法来设置。

Section 边距（inset）是一种调整单元格可用布局空间的方式。你可以用边距在某个 section 的页眉视图之后、页脚视图之前插入空白。你也可以用边距在内容的四周插入空白。图 3-5 演示了在垂直滚动的流式布局中，边距是如何影响内容的。

__图 3-5__  Section 边距改变了排布单元格的可用空间

!

由于边距减少了可用于排布单元格的空间，你可以用它来限制某一行中单元格的数量。在非滚动方向上指定边距，就是一种收窄每行空间的办法。如果再配合恰当的单元格尺寸，你就能控制每行中单元格的数量。

尽管你不做子类化也能非常高效地使用流式布局，但仍有一些时候你需要通过子类化来获得所需的行为。表 3-1 列出了一些必须对 [UICollectionViewFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout) 派生子类才能达到预期效果的场景。

__表 3-1__  需要对 `UICollectionViewFlowLayout` 派生子类的场景

| 场景 | 子类化要点 |
| --- | --- |
| 你想为布局添加新的补充视图或装饰视图 | 标准的流式布局类只支持 section 页眉视图和 section 页脚视图，不支持装饰视图。要支持额外的补充视图和装饰视图，你至少需要重写以下方法：   - [layoutAttributesForElementsInRect:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617769-layoutattributesforelementsinrec)（必需） - [layoutAttributesForItemAtIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617797-layoutattributesforitematindexpa)（必需） - [layoutAttributesForSupplementaryViewOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617792-layoutattributesforsupplementary)（用于支持新的补充视图） - [layoutAttributesForDecorationViewOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617809-layoutattributesfordecorationvie)（用于支持新的装饰视图）   在你的 `layoutAttributesForElementsInRect:` 方法中，可以先调用 `super` 拿到单元格的布局属性，然后再补上位于指定矩形内的任何新补充视图或装饰视图的属性。其余方法则用于按需提供属性。  有关在布局过程中为视图提供属性的信息，请参阅[创建布局属性](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltemi)和[为给定矩形内的项目提供布局属性](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltm)。 |
| 你想微调流式布局返回的布局属性 | 重写 [layoutAttributesForElementsInRect:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617769-layoutattributesforelementsinrec) 方法以及任何返回布局属性的方法。你的方法实现应当调用 `super`，修改父类提供的属性，然后再把它们返回。  有关这些方法具体涉及什么的深入讨论，请参阅[创建布局属性](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltemi)和[为给定矩形内的项目提供布局属性](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltm)。 |
| 你想为单元格和视图添加新的布局属性 | 创建 [UICollectionViewLayoutAttributes](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes) 的自定义子类，并添加表示你自定义布局信息所需的任何属性。  对 [UICollectionViewFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout) 派生子类，并重写 [layoutAttributesClass](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617774-layoutattributesclass) 方法。在该方法的实现中返回你的自定义子类。  你还应该重写 [layoutAttributesForElementsInRect:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617769-layoutattributesforelementsinrec) 方法、[layoutAttributesForItemAtIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617797-layoutattributesforitematindexpa) 方法，以及任何其他返回布局属性的方法。在你的自定义实现中，应当为你所定义的所有自定义属性设置好取值。 |
| 你想为被插入或删除的项目指定初始位置或最终位置 | 默认情况下，被插入或删除的项目会得到一个简单的淡入淡出动画。要创建自定义动画，你必须重写以下方法中的部分或全部：   - [initialLayoutAttributesForAppearingItemAtIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617789-initiallayoutattributesforappear) - [initialLayoutAttributesForAppearingSupplementaryElementOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617737-initiallayoutattributesforappear) - [initialLayoutAttributesForAppearingDecorationElementOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617726-initiallayoutattributesforappear) - [finalLayoutAttributesForDisappearingItemAtIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617740-finallayoutattributesfordisappea) - [finalLayoutAttributesForDisappearingSupplementaryElementOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617742-finallayoutattributesfordisappea) - [finalLayoutAttributesForDisappearingDecorationElementOfKind:atIndexPath:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617762-finallayoutattributesfordisappea)   在这些方法的实现中，指定每个视图在被插入之前或被移除之后应具有的属性。流式布局对象会用你提供的这些属性来为插入和删除添加动画。  如果你重写了这些方法，还建议你重写 [prepareForCollectionViewUpdates:](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617784-prepareforcollectionviewupdates) 和 [finalizeCollectionViewUpdates](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/1617787-finalizecollectionviewupdates) 方法。你可以用这两个方法跟踪当前这一轮中有哪些项目正在被插入或删除。  有关插入和删除如何工作的更多信息，请参阅[让插入和删除动画更有趣](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltcmy)。 |

也有一些情况下，正确的做法是从零开始创建一个自定义布局。在决定这么做之前，请花点时间考虑它是否真有必要。流式布局提供了大量可自定义的行为，适用于许多不同类型的布局；而且因为它是系统提供给你的，所以既易于使用，又包含大量提升效率的优化。不过，这一切并不是说你永远不该创建自定义布局，因为确实有些情形下这么做完全合理。流式布局把滚动方向限制为单一方向，所以如果你的布局所包含的内容在两个方向上都超出屏幕边界，那么实现自定义布局就更合理。如果你的布局既不是网格、也不是上面所说的基于行的断行布局，或者布局内的项目变动过于频繁，以至于对流式布局派生子类比自己写一个还麻烦，那么创建自定义布局就是正确的选择。

有关创建自定义布局的更多内容，请参阅[创建自定义布局](Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltc)。

[下一页](Incorporating%20Gesture%20Support.md)[上一页](Designing%20Your%20Data%20Source%20and%20Delegate.md)

