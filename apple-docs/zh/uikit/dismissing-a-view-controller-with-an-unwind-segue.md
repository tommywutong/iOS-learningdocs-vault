---
title: 使用展开 segue 关闭视图控制器
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/dismissing-a-view-controller-with-an-unwind-segue
source_url: 'https://developer.apple.com/documentation/uikit/dismissing-a-view-controller-with-an-unwind-segue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/dismissing-a-view-controller-with-an-unwind-segue.json'
content_hash: 'sha256:b0c04dcbbf019e23'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [资源管理](resource-management.md)

# 使用展开 segue 关闭视图控制器

<sub>文章</sub>

在你的 Storyboard 文件中配置展开 segue（unwind segue），让它动态选择接下来要显示的最合适的视图控制器。

## 概述

要处理视图控制器的关闭，可以创建一个展开 segue。与你用来呈现视图控制器的 segue 不同，展开 segue 只保证关闭当前的视图控制器，而不保证由此产生的转场有一个具体的目标。相反，UIKit 会在运行时以编程方式确定展开 segue 的目标。

由于 UIKit 在运行时才确定展开 segue 的目标，你在安排视图控制器层级结构（view controller hierarchy）时不受任何限制。考虑这样一个场景：两个视图控制器呈现同一个子视图控制器，如下图所示。你可以添加复杂的逻辑来确定接下来显示哪个视图控制器，但这样的解决方案扩展性不佳。相反，UIKit 提供了一个简单的编程式解决方案，只需极少的工作量就能扩展到任意数量的视图控制器。

![](../../../attachments/61b83c9a12a192275987cc892156d382/media-3375405@2x.png)

<sub>展示把展开 segue 连接到特定视图控制器这一问题的示意图。可能有多个目标可供选择。 </sub>

### 在父视图控制器上定义 unwind 操作

unwind segue 操作方法的存在会告诉 UIKit：某个视图控制器是展开 segue 的一个潜在目的地。在你的 Storyboard 中配置任何展开 segue 之前，请把这个操作方法添加到至少一个视图控制器上。如果没有任何视图控制器拥有 unwind 操作，Xcode 会阻止你创建展开 segue。这个操作方法采用以下格式：

**Swift**

```swift
@IBAction func myUnwindAction(unwindSegue: UIStoryboardSegue)
```

**Objective-C**

```objc
- (IBAction) myUnwindAction:(UIStoryboardSegue*)unwindSegue
```

你不需要在 unwind segue 操作方法里做任何事情。这个方法的存在本身就足以关闭当前的视图控制器。不过，你可以利用这个方法在关闭过程中执行相关任务。例如，你可以把数据从被关闭的视图控制器传回呈现它的父视图控制器。如果这样做，你可以使用所提供的 [UIStoryboardSegue](uistoryboardsegue.md) 对象来获取起始和结束的视图控制器。

### 将触发对象连接到 Exit 控制

在你的 Storyboard 中，右键点按一个触发对象并拖到视图控制器场景（scene）顶部的 Exit 控制（Exit control），即可创建一个展开 segue。你可以从任何支持目标-动作（target-action）设计模式的对象触发 segue，例如某个控制或附加到你视图控制器上的手势识别器。

![展示如何把按钮连接到视图控制器的 Exit 控制以创建展开 segue 的示意图。](../../../attachments/b11e5fc6be5212414fff10f0d5774de5/media-3376048@2x.png)

当你把一个对象连接到 Exit 控制时，UIKit 会呈现一个已知操作方法的列表。选择其中一个操作方法即可完成这个展开 segue。你选择的只是操作方法，而不是某个具体的视图控制器。要在关闭后被显示，父视图控制器必须实现你所选择的方法。

当用户触发关闭操作时，UIKit 会在当前的视图控制器层级结构中搜索实现了指定操作方法的视图控制器。它从直接父级开始寻找最近的视图控制器，并沿着视图控制器层级结构逐级向上，直到找到合适的目标。如果找不到实现了该方法的视图控制器，展开 segue 会静默失败，而当前的视图控制器仍留在屏幕上。

## 另请参阅

### Storyboard

- [自定基于 segue 的呈现的行为](customizing-the-behavior-of-segue-based-presentations.md) — 在 segue 期间在视图控制器之间传递数据，并以编程方式控制 segue 何时发生。
- [UIStoryboard](uistoryboard.md) — 对 Interface Builder storyboard 资源文件中所表示的设计时视图控制器关系图的封装。
- [UIStoryboardSegue](uistoryboardsegue.md) — 为两个视图控制器之间的可视化转场做准备并执行该转场的对象。
- [UIStoryboardUnwindSegueSource](uistoryboardunwindseguesource.md) — 对展开 segue 相关信息的封装。
