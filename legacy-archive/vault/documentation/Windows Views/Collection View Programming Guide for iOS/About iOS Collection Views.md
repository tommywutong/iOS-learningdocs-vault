---
title: iOS Collection View 编程指南
apple_id: TP40012334
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/CollectionViewPGforIOS/Introduction/Introduction.html
archived_at: '2026-07-18T02:22:42.135503Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Collection%20View%20Basics.md)

# 关于 iOS Collection View

Collection view 是一种以灵活多变的布局来呈现一组有序数据项的方式。Collection view 最常见的用途是以网格形式排列各个项目，但 iOS 中的 collection view 能做的远不止行与列。借助 collection view，可视元素的精确布局可以通过子类化来定义，并且可以动态更改，因此你可以实现网格、堆叠、圆形布局、动态变化的布局，或任何你能想象到的排列方式。

Collection view 在被呈现的数据与用于呈现这些数据的可视元素之间保持着严格的分离。在大多数情况下，你的应用只负责管理数据。你的应用还需要提供用于呈现这些数据的视图对象。在此之后，collection view 会接手你的视图，完成把它们摆放到屏幕上的全部工作。它是与一个布局对象协作完成这项工作的——布局对象指定了各个视图的摆放位置和可视属性，并且可以通过子类化来精确满足你应用的需求。也就是说，你提供数据，布局对象提供位置信息，collection view 把两者合并起来，得到最终的外观。

iOS 标准的 collection view 类提供了实现简单网格所需的全部行为。你也可以扩展这些标准类，以支持自定义布局以及与这些布局的特定交互。

### Collection View 管理数据驱动视图的可视呈现

Collection view 负责协助呈现由你的应用提供的数据驱动视图。Collection view 唯一关心的事情就是接收你的视图并以特定的方式对它们进行布局。Collection view 只关注视图的呈现和排列，而不关注其内容。理解 collection view、其数据源、布局对象以及你的自定义对象之间的交互，对于在应用中使用 collection view 至关重要——尤其是要以聪明且高效的方式使用时。

### 流式布局支持网格及其他按行排列的呈现方式

流式布局（flow layout）对象是 UIKit 提供的一个具体布局对象。你通常用流式布局对象来实现网格——也就是项目的行与列——但流式布局支持任何类型的线性流动排列。正因为它并非只服务于网格，所以无论是否子类化，你都可以用流式布局为内容创建出有趣而灵活的排列。无需子类化，流式布局就支持不同尺寸的项目、可变的项目间距、自定义的页眉和页脚以及自定义边距。而通过子类化，你还可以进一步微调流式布局类的行为。

### 手势识别器可用于操作单元格与布局

与所有视图一样，你可以给 collection view 附加手势识别器来操作其内容。由于 collection view 涉及多个视图的协作，了解一些把手势识别器整合进 collection view 的基本技巧会很有帮助。你可以用手势识别器来调整布局属性，或者操作 collection view 中的项目。

### 自定义布局让你超越网格

你可以子类化基本的布局对象，为应用实现自定义布局。尽管设计自定义布局通常不需要大量代码，但你对布局的工作方式理解得越多，就越能把布局对象设计得高效。本指南的最后一章专注于一个包含自定义布局完整实现的示例项目。

在阅读本文档之前，你应该对视图在 iOS 应用中扮演的角色有扎实的理解。如果你刚接触 iOS 编程、还不熟悉 iOS 视图架构，请在阅读本书之前先阅读 _[View Programming Guide for iOS](../View%20Programming%20Guide%20for%20iOS/About%20Windows%20and%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbt)_。

Collection view 与 table view 有些相似，因为两者都向用户呈现有序数据。Table view 的实现与标准 collection view（即使用自带的流式布局的 collection view）类似，都使用索引路径、单元格和视图回收机制。不过，table view 的可视呈现围绕单列布局展开，而 collection view 可以支持多种不同的布局。有关 table view 的更多信息，请参阅 _[Table View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/TableView_iPhone/AboutTableViewsiPhone/AboutTableViewsiPhone.html#//apple_ref/doc/uid/TP40007451)_。

[下一页](Collection%20View%20Basics.md)

