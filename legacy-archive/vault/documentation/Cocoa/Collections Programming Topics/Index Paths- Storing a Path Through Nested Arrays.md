---
title: 集合编程主题
apple_id: 10000034i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/IndexPaths.html
archived_at: '2026-07-15T07:13:34.309076Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [集合编程主题](About%20Collections.md)


[下一页](Copying%20Collections.md)[上一页](Index%20Sets-%20Storing%20Indexes%20into%20an%20Array.md)

# 索引路径：在嵌套数组中存储路径

索引路径（index path）存储了穿过一组嵌套数组的路径，用于在更复杂的集合层次结构（例如树）中检索对象。例如，图 1 展示了一组嵌套数组，表示某个假想公司的组织层级结构。

__图 1__  嵌套数组与索引路径

!

以[图 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnrxfvjvona) 所示的这家假想公司的层级结构为例，根数组只包含 CEO 这一个条目。其下的数组由各位副总裁组成。每位副总裁下面是一个由各位总监组成的数组，依此类推。如果你想存储欧洲市场团队中某位特定员工的位置，仅凭一个简单的索引是不够的，而需要一条穿过这些嵌套数组的路径。在这个例子中，Bill T. 可以用索引路径 0.0.1.1.2 来表示。

你可以通过一个单一索引、或一个 C 风格的 `NSUInteger` 值数组来创建索引路径。清单 1 展示了如何创建指向 Bill T. 的索引路径。

__清单 1__  从数组创建索引路径

```objc
NSUInteger arrayLength = 5;
NSUInteger integerArray[] = {0,0,1,1,2};
NSIndexPath *aPath = [[NSIndexPath alloc] initWithIndexes:integerArray length:arrayLength];
```

你也可以从许多更复杂的层次结构集合类中自动创建索引路径。相关示例请参见 [NSTreeNode](https://developer.apple.com/documentation/appkit/nstreenode) 类的 [indexPath](https://developer.apple.com/documentation/appkit/nstreenode/1532255-indexpath) 方法。

`NSIndexPath` 提供了用于查询路径中各个元素的方法。例如，[indexAtPosition:](https://developer.apple.com/documentation/foundation/nsindexpath/1414179-index) 会返回索引路径中给定位置所存储的索引。你也可以通过添加一个新索引或移除最后一个索引来创建新的索引路径。有一些类会大量使用索引路径来管理其内容，`NSTreeController` 就是这样一个例子。关于 `NSTreeController` 和索引路径的更多信息，请参阅 _[Cocoa Bindings Programming Topics](../Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)_。

在 iOS 中，`UITableView` 及其[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)和数据源使用索引路径来管理其大部分内容，并处理用户交互。为了配合这一点，UIKit 为 `NSIndexPath` 添加了编程接口，将表视图的行和分区更充分地纳入索引路径中。更多信息请参阅 _NSIndexPath UIKit Additions_。例如，[tableView:didSelectRowAtIndexPath:](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614877-tableview) 委托方法就使用索引路径来指定用户所做的选择。

[下一页](Copying%20Collections.md)[上一页](Index%20Sets-%20Storing%20Indexes%20into%20an%20Array.md)
