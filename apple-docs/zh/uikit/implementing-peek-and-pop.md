---
title: 实现 Peek 和 Pop
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 11.4+, iPadOS 11.4+, Mac Catalyst 11.4+, Xcode 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/implementing-peek-and-pop
source_url: 'https://developer.apple.com/documentation/uikit/implementing-peek-and-pop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/implementing-peek-and-pop.json'
content_hash: 'sha256:7433784f7eabab06'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Deprecated symbols](deprecated-symbols.md)

# 实现 Peek 和 Pop

<sub>示例代码</sub>

通过提供在详情视图控制器中预览内容的快捷方式，加速你 App 中的操作。

## 概述

这个示例项目演示了如何使用 Peek 和 Pop API 预览内容，并提供功能的快捷方式。这个 App 使用一个表格视图显示颜色列表，点按表格中的任意一行都会导览到显示该颜色的详情视图控制器。App 在表格视图的行上使用 3D Touch，让用户能够窥视（peek）内容，而不必将其放入导览堆栈。

颜色还可以被加星标或取消星标。已加星标的颜色在名称左侧会显示一个实心填色的星形图标，未加星标的颜色则显示一个空心星形。用户可以用两种方法之一切换某个颜色是否加星标：可以点按详情视图导航栏中的按钮，也可以使用 3D Touch 窥视内容。在 3D Touch 状态下向上滑动，用户就能使用 Peek 快速操作。

这个 App 使用一个标签页栏控制器来演示实现 Peek 和 Pop 的两种不同方法。第一个标签页包含 `ColorsViewControllerStoryboard` 视图控制器，它使用 `Main.storyboard` 中的转场配置 Peek 和 Pop。第二个标签页包含 `ColorsViewControllerCode` 视图控制器，以代码方式实现相同的功能。

`ColorsViewControllerStoryboard` 和 `ColorsViewControllerCode` 都是 `ColorsViewControllerBase` 的子类，后者包含了显示表格视图和处理标准转场所需的全部实现。

### 从 storyboard 中实现 Peek 和 Pop

该 storyboard 使用一个启用了 Peek 和 Pop 的 Show 转场，从 `ColorViewControllerStoryboard` 导览到 `ColorItemViewController`。具体做法是选中 Show 转场，然后在属性检查器中的 Peek & Pop 旁边打开「Preview & Commit Segues」。

在配置 `ColorItemViewController` 时，在属性检查器的「View Controller」部分启用「Use Preferred Explicit Size」选项。将「Content Size」设置为宽度 0、高度取适当值。宽度为 0 会将该视图控制器配置为在用户窥视内容时自动调整为设备宽度。

在实现 `ColorsViewControllerBase` 视图控制器时，请抵制在准备执行转场时使用 [indexPathForSelectedRow](uitableview/indexpathforselectedrow.md) 或 [indexPathsForSelectedRows](uitableview/indexpathsforselectedrows.md) 的诱惑。如果你使用默认的 Peek 和 Pop 实现来配置 storyboard，这些方法在转场执行时会返回 `nil`。应改为使用转场的 `sender` 属性来访问触发窥视的单元格。

```swift
override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
    guard let selectedTableViewCell = sender as? UITableViewCell,
        let indexPath = tableView.indexPath(for: selectedTableViewCell)
        else { preconditionFailure("Expected sender to be a valid table view cell") }

    guard let colorItemViewController = segue.destination as? ColorItemViewController
        else { preconditionFailure("Expected a ColorItemViewController") }

    // Pass over a reference to the ColorData object and the specific ColorItem being viewed.
    colorItemViewController.colorData = colorData
    colorItemViewController.colorItem = colorData.colors[indexPath.row]
}
```

### 以代码方式实现 Peek 和 Pop

`ColorsViewControllerCode` 视图控制器添加了代码，用于手动注册 Peek 和 Pop，而不是使用 storyboard 来自定转场。调用 [- registerForPreviewingWithDelegate:sourceView:](<uiviewcontroller/registerforpreviewing(with_sourceview_).md>) 来注册一个实现了 [UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md) 协议的类，然后传入一个能响应 3D Touch 的视图。

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    registerForPreviewing(with: self, sourceView: tableView)
}
```

该协议要求实现两个方法。当系统检测到 3D Touch 时，会调用 [- previewingContext:viewControllerForLocation:](<uiviewcontrollerpreviewingdelegate/previewingcontext(__viewcontrollerforlocation_).md>)，传入一个遵循 [UIViewControllerPreviewing](uiviewcontrollerpreviewing.md) 协议的 `previewingContext` 对象。使用这个方法来配置并回传用于窥视的视图控制器。

```swift
func previewingContext(_ previewingContext: UIViewControllerPreviewing, viewControllerForLocation location: CGPoint) -> UIViewController? {
    // First, get the index path and view for the previewed cell.
    guard let indexPath = tableView.indexPathForRow(at: location),
        let cell = tableView.cellForRow(at: indexPath)
        else { return nil }

    // Enable blurring of other UI elements and a zoom-in animation while peeking.
    previewingContext.sourceRect = cell.frame

    // Create and configure an instance of the color item view controller to show for the peek.
    guard let viewController = storyboard?.instantiateViewController(withIdentifier: "ColorItemViewController") as? ColorItemViewController
        else { preconditionFailure("Expected a ColorItemViewController") }

    // Pass over a reference to the ColorData object and the specific ColorItem being viewed.
    viewController.colorData = colorData
    viewController.colorItem = colorData.colors[indexPath.row]

    return viewController
}
```

当系统检测到 3D Touch 的压力足以弹出视图控制器时，会调用 [- previewingContext:commitViewController:](<uiviewcontrollerpreviewingdelegate/previewingcontext(__commit_).md>)。取得传入的视图控制器并将其呈现给用户。

```swift
func previewingContext(_ previewingContext: UIViewControllerPreviewing, commit viewControllerToCommit: UIViewController) {
    // Push the configured view controller onto the navigation stack.
    navigationController?.pushViewController(viewControllerToCommit, animated: true)
}
```

### 实现 Peek 快速操作

要为 `ColorItemViewController` 启用 Peek 快速操作，你必须重写 [previewActionItems](uiviewcontroller/previewactionitems.md) 属性的默认实现，使其返回一个 [UIPreviewAction](uipreviewaction.md) 或 [UIPreviewActionGroup](uipreviewactiongroup.md) 对象组成的数组。

以下代码将加星标/取消星标操作和删除操作都作为快速操作提供：

```swift
override var previewActionItems: [UIPreviewActionItem] {
    let starAction = UIPreviewAction(title: starButtonTitle(), style: .default, handler: { [unowned self] (_, _) in
        guard let colorItem = self.colorItem
            else { preconditionFailure("Expected a color item") }

        colorItem.starred.toggle()
    })

    let deleteAction = UIPreviewAction(title: "Delete", style: .destructive) { [unowned self] (_, _) in
        guard let colorData = self.colorData
            else { preconditionFailure("Expected a reference to the color data container") }

        guard let colorItem = self.colorItem
            else { preconditionFailure("Expected a color item") }

        colorData.delete(colorItem)
    }

    return [ starAction, deleteAction ]
}
```

加星标/取消星标操作以默认样式显示，删除操作则以破坏性样式显示。

请务必确保你 App 的功能在不支持 3D Touch 的设备上仍然可用。在这个示例中，加星标/取消星标以及删除功能仍然可以通过导览进入 `ColorItemViewController` 并点按导航栏中的按钮来使用。Peek 快速操作只是提供了一种更便捷的方式来访问该功能。

## 下载

- [ImplementingPeekAndPop.zip](https://docs-assets.developer.apple.com/published/22fe32e34c3a/ImplementingPeekAndPop.zip)
</content>
