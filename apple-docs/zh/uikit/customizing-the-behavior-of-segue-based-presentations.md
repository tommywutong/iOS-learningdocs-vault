---
title: 自定义基于 segue 的呈现行为
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/customizing-the-behavior-of-segue-based-presentations
source_url: 'https://developer.apple.com/documentation/uikit/customizing-the-behavior-of-segue-based-presentations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/customizing-the-behavior-of-segue-based-presentations.json'
content_hash: 'sha256:eb68eda9a259a146'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [资源管理](resource-management.md)

# 自定义基于 segue 的呈现行为

<sub>文章</sub>

在 segue 期间在视图控制器之间传递数据，并以编程方式控制 segue 何时发生。

## 概述

当用户触发 segue 时，UIKit 会使用你的 storyboard 中设定的选项来呈现视图控制器。UIKit 也为你提供了动态修改 segue 过程的机会：既可以阻止 segue 发生，也可以在 segue 发生时做一些额外工作。

关于如何创建 segue 的信息，参见[在你的 storyboard 文件中以可视化方式指定呈现](showing-and-hiding-view-controllers.md#Specify-presentations-visually-in-your-storyboard-file)。

### 配置转场的呈现风格

segue 的类型决定了 UIKit 在呈现和关闭 segue 时使用哪种动画，如下表所示。类型在创建 segue 时指定，但你之后也可以在属性检查器（attributes inspector）中更改它。

| Segue 类型 | 行为 |
|---|---|
| Show (Push) | 以模态方式显示视图控制器，除非父视图控制器实现了 [- showViewController:sender:](<uiviewcontroller/show(__sender_).md>) 动作方法——那样就由该视图控制器定义呈现行为。例如，[UINavigationController](uinavigationcontroller.md) 会把新的视图控制器推入它的导览栈。 |
| Show Detail (Replace) | 以模态方式显示视图控制器，除非父视图控制器实现了 [- showDetailViewController:sender:](<uiviewcontroller/showdetailviewcontroller(__sender_).md>) 动作方法——那样就由该视图控制器定义呈现行为。例如，[UISplitViewController](uisplitviewcontroller.md) 会用新的视图控制器替换它的第二个子视图控制器（详情控制器）。 |
| Present Modally | 使用指定的呈现与转场样式，以模态方式显示视图控制器。 |
| Present as Popover | 在水平常规（horizontally regular）环境中，UIKit 以弹出窗口呈现视图控制器。在水平紧凑（horizontally compact）环境中，UIKit 以模态方式呈现视图控制器。 |

关于 UIKit 如何执行涉及 Show 与 Show Detail 呈现风格的 segue 的更多信息，参见[让当前上下文决定呈现技术](showing-and-hiding-view-controllers.md#Let-the-current-context-define-the-presentation-technique)。

### 根据动态条件阻止 segue

当你不想让用户离开当前视图控制器时，在源视图控制器的 [- shouldPerformSegueWithIdentifier:sender:](<uiviewcontroller/shouldperformsegue(withidentifier_sender_).md>) 方法中返回 false，告诉 UIKit 不要执行 segue。用这个方法执行所需的各项检查，判断 segue 能否继续。例如，如果视图控制器的内容无效、需要用户纠正，就返回 [false](../swift/false.md)。返回 true 让 segue 继续；返回 [false](../swift/false.md) 则会让 segue 无声地失败。

### 向被呈现的视图控制器传递数据

由于 UIKit 会在 segue 期间自动创建并呈现视图控制器，请使用 [- prepareForSegue:sender:](<uiviewcontroller/prepare(for_sender_).md>) 方法在 segue 发生之前把数据传给该视图控制器。在包含发起 segue 的对象的视图控制器上实现这个方法。从提供的 [UIStoryboardSegue](uistoryboardsegue.md) 对象中取出新的视图控制器，以及关于触发了哪个 segue 的信息。

在下面的代码示例中，当前视图控制器取得与所选表格行关联的图像，并把该图像传给新的视图控制器。

```swift
override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
  // Get the new view controller.
   if let imageVC = segue.destination as? ImageViewController {

      // Fetch the image for the selected row. 
      let image = getImageForSelectedRow()
      imageVC.currentImage = image
   }
}
```

使用委托设计模式把数据从被呈现的视图控制器传回发起它的视图控制器。在你的 [- prepareForSegue:sender:](<uiviewcontroller/prepare(for_sender_).md>) 方法中配置该委托关系。

### 理解 segue 期间的事件序列

虽然 UIKit 自动处理 segue，但仍有许多地方可供你执行与显示新视图控制器相关的工作。下图展示了从用户触发 segue 到整个过程完成之间的事件流。执行 segue 相关操作的主要位置是当前视图控制器的 [- prepareForSegue:sender:](<uiviewcontroller/prepare(for_sender_).md>) 方法，但你也可以在创建新视图控制器的过程中执行任务。

![](../../../attachments/edeaea13eae34394632d64f139802ad4/media-3379644@2x.png)

<sub>示意图：用户触发 segue 时的事件流。UIKit 会调用当前视图控制器的方法来修改 segue 的行为。 </sub>

## 另请参阅

### Storyboard

- [用展开 segue 关闭视图控制器](dismissing-a-view-controller-with-an-unwind-segue.md) — 在你的 storyboard 文件中配置一个展开 segue，动态选择接下来最合适的显示视图控制器。
- [UIStoryboard](uistoryboard.md) — 对 Interface Builder storyboard 资源文件中所表示的设计期视图控制器图的封装。
- [UIStoryboardSegue](uistoryboardsegue.md) — 为两个视图控制器之间的可视化转场做准备并执行转场的对象。
- [UIStoryboardUnwindSegueSource](uistoryboardunwindseguesource.md) — 对展开 segue 相关信息的封装。
