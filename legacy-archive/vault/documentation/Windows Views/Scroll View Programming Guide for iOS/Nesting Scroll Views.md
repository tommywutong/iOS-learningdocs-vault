---
title: iOS Scroll View 编程指南
apple_id: TP40008179
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/UIScrollView_pg/NestedScrollViews/NestedScrollViews.html
archived_at: '2026-07-18T02:22:52.960707Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS Scroll View 编程指南](About%20Scroll%20View%20Programming.md)


[下一页](Document%20Revision%20History.md)[上一页](Scrolling%20Using%20Paging%20Mode.md)

# 嵌套 Scroll View

为了打造丰富的用户体验，你可能想在应用中嵌套 Scroll View。在 iOS 3.0 之前，这即便不是不可能，也相当困难。而在 iOS 3.0 中，这项功能已获得完整支持并可自动工作。

当一个 `UIScrollView` 是另一个 `UIScrollView` 的子视图，且二者朝同一方向滚动时，就是同向滚动。图 6-1 左侧的插图展示了这种情形。

__图 6-1__  同向滚动的 Scroll View 与交叉方向滚动的 Scroll View

!

交叉方向滚动指的是：作为另一个 Scroll View 子视图的 Scroll View，其滚动方向与外层相差 90 度，如图 6-1 右侧插图所示。

交叉方向滚动的一个例子可以在“股市”应用中找到。上方的视图是一个 Table View，而下方的视图是一个配置为分页模式的水平 Scroll View。它的三个子视图中有两个是自定义视图，第三个（包含新闻文章的那个）是一个 `UITableView`（`UIScrollView` 的子类），它是这个水平 Scroll View 的子视图。当你水平滚动到新闻视图之后，就可以再垂直滚动它的内容。

如前所述，你的应用不需要为支持嵌套滚动做任何事。它是默认就提供并支持的。

[下一页](Document%20Revision%20History.md)[上一页](Scrolling%20Using%20Paging%20Mode.md)

