---
title: 通过流畅过渡增强你的 App
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/enhancing-your-app-with-fluid-transitions
source_url: 'https://developer.apple.com/documentation/uikit/enhancing-your-app-with-fluid-transitions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/enhancing-your-app-with-fluid-transitions.json'
content_hash: 'sha256:443aac466b1ca0f8'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Animation and haptics](animation-and-haptics.md) · [View controller transitions](view-controller-transitions.md)

# 通过流畅过渡增强你的 App

<sub>文章</sub>

使用流畅缩放过渡效果，为你的 App 提供持续可交互、响应灵敏的体验。

## 概述

iOS 18 引入了一种流畅、可持续交互的缩放过渡效果。当你的 App 从一个大的单元格或缩略图导览离开时，可以使用这种过渡效果来增强 App 中的连续感。用户随后可以在过渡开始时以及动画进行期间的任何时刻抓取、拖动并控制这个过渡。

![](../../../attachments/bd50d0379034d35e5c72efaca38e8530/media-4422984@2x.png)

例如，有人点按一个缩略图，你的 App 将相应的视图控制器推入导览栈。如果你使用的是缩放过渡效果，用户可以停止该过渡，或拖动它来放慢或反转过渡进程。App 的状态和过渡动画都会根据用户的手势无缝变化。

流畅缩放过渡效果适用于 iPhone 和 iPad，包括在 visionOS 中运行的 iPad App。该 API 在其他平台上也可用，但系统会根据当前上下文改用默认的过渡效果。

### 设置缩放过渡效果

要使用缩放过渡效果，请在新的视图控制器上将 [preferredTransition](uiviewcontroller/preferredtransition.md) 属性设为 [zoom(options:sourceViewProvider:)](<uiviewcontroller/transition/zoom(options_sourceviewprovider_).md>)，并传入一个返回你要从中缩放的视图的闭包。然后将该视图控制器推入导览栈。

```swift
// Create a detail view controller for the selected item.
let detailViewController = MyDetailViewController(itemID: itemID)

// Set the preferred transition to zoom.
detailViewController.preferredTransition = .zoom { [self] _ in
    
    // Return the thumbnail view for the selected item.
    return thumbnail(for: itemID)
}

// Push the detail view controller onto the navigation stack.
navigationController?.pushViewController(detailViewController, animated: true)
```

> [!important] 重要
> 由于该过渡效果在缩放放大和缩小时都会运行，请使用一个稳定的标识符来在闭包中查找视图，而不要捕获 [UIView](uiview.md) 或 [IndexPath](../foundation/indexpath.md) 实例。

如果你的 App 允许用户在不离开详情视图的情况下滑动切换不同的条目，那么你想要缩放回去的缩略图可能会发生变化。要查找正确的缩略图，请使用系统传给闭包的上下文。

```swift
// Create a detail view controller for the selected item.
let detailViewController = MyDetailViewController(itemID: itemID)

// Set the preferred transition to zoom.
detailViewController.preferredTransition = .zoom { context in
    
    // Use the context to determine the current item.
    guard let controller = context.zoomedViewController as? MyDetailViewController else {
        fatalError("Unable to access the current view controller.")
    }
    
    // Return the thumbnail for the current item.
    return self.thumbnail(for: controller.itemID)
}

// Push the detail view controller onto the navigation stack.
navigationController?.pushViewController(detailViewController, animated: true)
```

> [!note] 注意
> 你也可以将 `preferredTransition` 属性用于其他系统过渡效果，比如 [coverVertical](uiviewcontroller/transition/coververtical.md)、[flipHorizontal](uiviewcontroller/transition/fliphorizontal.md)、[crossDissolve](uiviewcontroller/transition/crossdissolve.md) 和 [partialCurl](uiviewcontroller/transition/partialcurl.md)。

### 处理状态变化和回调

在将视图控制器推入导览栈或从中弹出时，它们会经历多次状态变化。

![](../../../attachments/e97461b40b52ce1a5a9f78c0b8bfeed8/media-4414969@2x.png)

<sub>展示视图控制器状态、过渡和回调方法之间关系的示意图。该示意图有四种状态：已消失、正在出现、已出现和正在消失。从已消失过渡到正在出现时，系统调用 viewWillAppear，将视图添加到视图层级结构中，然后调用 viewIsAppearing。从正在出现过渡到已出现时，调用 viewDidAppear。从已出现过渡到正在消失时，调用 viewWillDisappear。最后，从正在消失过渡到已消失时，将视图从视图层级结构中移除，然后调用 viewDidDisappear。</sub>

当你将视图控制器推入导览栈时，该控制器最初处于 _disappeared_（已消失）状态。在它过渡到 _appeared_（已出现）状态的过程中，系统会执行以下步骤：

1. 调用 [- viewWillAppear:](<uiviewcontroller/viewwillappear(__).md>)。
2. 将控制器的视图添加到视图层级结构中。
3. 调用 [- viewIsAppearing:](<uiviewcontroller/viewisappearing(__).md>)。
4. 过渡到 _appearing_（正在出现）状态。
5. 调用 [- viewDidAppear:](<uiviewcontroller/viewdidappear(__).md>)。
6. 结束于已出现状态。

![](../../../attachments/c291f5d39a4710a35a376032ddc8a36a/media-4422525@2x.png)

<sub>展示视图控制器在推入过渡期间状态变化的示意图。它从已消失状态开始。系统调用 viewWillAppear，将视图添加到视图层级结构中，然后在控制器转入正在出现状态时调用 viewIsAppearing。随后系统在控制器转入已出现状态时调用 viewDidAppear。</sub>

当你将视图控制器从导览栈中弹出时，它从已出现状态开始。随后系统会执行以下步骤：

1. 调用 [- viewWillDisappear:](<uiviewcontroller/viewwilldisappear(__).md>)。
2. 过渡到 _disappearing_（正在消失）状态。
3. 将视图从视图层级结构中移除。
4. 调用 [- viewDidDisappear:](<uiviewcontroller/viewdiddisappear(__).md>)。
5. 结束于已消失状态。

![](../../../attachments/be3392ac981e83490758da2b05c8eadb/media-4422524@2x.png)

<sub>展示视图控制器在弹出过渡期间状态变化的示意图。它从已出现状态开始。系统在控制器转入正在消失状态时调用 viewWillDisappear。随后系统将视图从视图层级结构中移除，并在视图控制器转入已消失状态时调用 viewDidDisappear。</sub>

当有人中断流畅缩放过渡时，事件序列会发生变化。如果用户取消了一次导览弹出，系统会调用 [- viewWillDisappear:](<uiviewcontroller/viewwilldisappear(__).md>) 并过渡到正在消失状态。此时，系统会直接过渡到正在出现状态，并在结束于已出现状态之前调用 [- viewDidDisappear:](<uiviewcontroller/viewdiddisappear(__).md>)。这个过渡发生在运行循环的一个周期内，因此新事件无法打断它。

![](../../../attachments/bcf6a36e70e75b1a165c3369e2f40f16/media-4422527@2x.png)

<sub>展示当有人取消弹出过渡时视图控制器状态变化的示意图。视图控制器从已出现状态开始。系统在控制器转入正在消失状态时调用 viewWillDisappear。随后视图控制器直接转入正在出现状态。系统调用 viewDidAppear，视图控制器转入已出现状态。</sub>

然而，如果有人中断了一次导览推入，系统不会取消推入过渡。相反，系统会完成到已出现状态的过渡，并在运行循环的一个周期内开始导览弹出。随后弹出过渡会照常进行，要么运行至完成，要么再次被中断。

![](../../../attachments/46c46c5d95d188e3dc5d7c6d8e514a72/media-4422526@2x.png)

<sub>展示当有人中断推入过渡、将其转换为弹出过渡时视图控制器状态变化的示意图。推入过渡从已消失状态开始，即使在推入过渡被中断之后，仍会推进到已出现状态。随后它开始一次弹出过渡，从已出现状态转回已消失状态。系统在此周期内执行所有操作：调用 viewWillAppear，将视图添加到视图层级结构中，调用 viewIsAppearing，调用 viewDidAppear，调用 viewWillDisappear，将视图从视图层级结构中移除，并调用 viewDidDisappear。</sub>

> [!important] 重要
> 系统对推入和弹出过渡的处理方式不同。它不会取消推入操作——而是将其转换为弹出操作。这确保了视图控制器能到达已出现状态，并调用完整周期的出现和消失回调。

### 保持无缝过渡

在使用持续可交互的过渡效果时，你的 App 需要随时准备好让新的过渡开始或停止。请遵循以下准则，帮助你的过渡运行得无缝而流畅：

- 不要因为某个过渡当前正在运行就避免开始新的导览推入或弹出。让新的推入或弹出开始，系统会处理这些过渡。
- 将临时的过渡状态保持在最少，并避免让其他代码依赖于该状态。
- 实现你的回调方法时，要确保系统可以安全地多次调用它们。在调用任何使用或清理结果的代码之前，系统可能会不止一次地调用这些方法。
- 如果你需要在过渡期间跟踪某个状态，请在 [- viewDidAppear:](<uiviewcontroller/viewdidappear(__).md>) 或 [- viewDidDisappear:](<uiviewcontroller/viewdiddisappear(__).md>) 中清理它。系统会在过渡结束时调用这些方法。
- 如果你使用的是导览控制委托，可以使用 [- navigationController:willShowViewController:animated:](<uinavigationcontrollerdelegate/navigationcontroller(__willshow_animated_).md>) 和 [- navigationController:didShowViewController:animated:](<uinavigationcontrollerdelegate/navigationcontroller(__didshow_animated_).md>) 来进行清理，而不是使用视图控制器的回调方法。
