---
title: 撤销架构
apple_id: 10000010i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-06-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UndoArchitecture/Articles/SettingUndoNames.html
archived_at: '2026-07-15T07:20:59.814857Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [撤销架构](Introduction%20to%20Undo%20Architecture.md)


[下一页](Using%20Undo%20Notifications.md)[上一页](Clearing%20the%20Undo%20Stack.md)

# 设置动作名称

你可以用 `NSUndoManager` 的 [setActionName:](https://developer.apple.com/documentation/foundation/nsundomanager/1412915-setactionname) 方法来修饰“编辑”菜单中“撤销”和“重做”命令的标题。当_当前_撤销组位于撤销栈和重做栈的顶部时，你传入的字符串会被追加到菜单项的“撤销”和“重做”之后。由于名称是应用到当前操作上的，所以通常你应该在注册操作的同时设置名称，以确保二者保持一致。

```objc
- (void)setBookTitle:(NSString *)newTitle {
    [undoManager registerUndoWithTarget:self
                 selector:@selector(setBookTitle:)
                 object:[book title]];
    [book setTitle:newTitle];
    [undoManager setActionName:@"Title Change"];
}
```

举例来说，考虑一个绘图应用程序，它允许用户添加圆形、用颜色填充圆形以及删除圆形。借助 `setActionName:`，你可以把每个动作的名称分别设为“添加圆形”、“填充”和“删除”。每次执行相应动作后，“撤销”菜单项的标题就会分别变成“撤销添加圆形”、“撤销填充”和“撤销删除”。

`NSUndoManager` 会自动本地化命令标题中“撤销”和“重做”的部分，但它只是把动作名称追加在后面。动作名称需要你自己去本地化。如果你想进一步定制这些标题的本地化方式，可以创建 `NSUndoManager` 的子类并重写 [undoMenuTitleForUndoActionName:](https://developer.apple.com/documentation/foundation/nsundomanager/1413122-undomenutitleforundoactionname) 和 [redoMenuTitleForUndoActionName:](https://developer.apple.com/documentation/foundation/nsundomanager/1407438-redomenutitleforundoactionname)。

[下一页](Using%20Undo%20Notifications.md)[上一页](Clearing%20the%20Undo%20Stack.md)

