---
title: 禁用 sheet 的下拉手势
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 12.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/disabling-the-pull-down-gesture-for-a-sheet
source_url: 'https://developer.apple.com/documentation/uikit/disabling-the-pull-down-gesture-for-a-sheet'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/disabling-the-pull-down-gesture-for-a-sheet.json'
content_hash: 'sha256:c8d75233dd2ed370'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md)

# 禁用 sheet 的下拉手势

<sub>示例代码</sub>

在以 sheet 形式呈现视图控制器时，确保良好的用户体验。

## 概述

默认情况下，用户可以使用下拉手势来关闭以 sheet 形式呈现的视图控制器。在用户使用下拉手势可能会丢失数据或最近的更改的情况下，UIKit 允许你禁用这个手势。你还可以通过呈现一个 [UIAlertController](uialertcontroller.md) 实例，来解释用户为什么无法关闭这个视图控制器的呈现。

### 禁用关闭呈现的能力

要禁用关闭视图控制器的呈现，请将 [modalInPresentation](uiviewcontroller/ismodalinpresentation.md) 设为 `true`。

```swift
// 如果存在未保存的更改，则启用 Save 按钮，
// 并禁用通过下拉手势进行关闭的能力。
saveButton.isEnabled = hasChanges
isModalInPresentation = hasChanges
```

也可以从呈现委托（presentation delegate）的 [- presentationControllerShouldDismiss:](<uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(__).md>) 方法返回 `false`。不过，当 [modalInPresentation](uiviewcontroller/ismodalinpresentation.md) 为 `true` 时，或者以编程方式关闭呈现时，系统不会调用这个方法。

### 解释用户为何无法关闭呈现

要在用户尝试关闭一个已禁用关闭的呈现时执行某个操作，请按下方的代码所示设置该呈现的委托：

```swift
// 将 editViewController 设置为本次呈现的 presentationController 的委托。
// 这样 editViewController 就能响应尝试关闭的操作。
navigationController.presentationController?.delegate = editViewController
```

设置好委托后，实现 [- presentationControllerDidAttemptToDismiss:](<uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss(__).md>) 方法并执行相应操作。下面的示例展示了 [UIAlertController](uialertcontroller.md) 实例的呈现：

```swift
func presentationControllerDidAttemptToDismiss(_ presentationController: UIPresentationController) {
    // 每当用户尝试下拉关闭且 `isModalInPresentation` 为 false 时，
    // 系统都会调用这个委托方法。
    // 通过询问用户想要取消还是保存来明确用户的意图。
    confirmCancel(showingSave: true)
}

// MARK: - 取消确认

func confirmCancel(showingSave: Bool) {
    // 以操作表单（action sheet）的形式呈现 UIAlertController，让用户确认将丢失
    // 最近的任何更改。
    let alert = UIAlertController(title: nil, message: nil, preferredStyle: .actionSheet)
    
    // 只在用户尝试下拉关闭时才询问是否要保存；用户轻点 Cancel 时则不询问。
    if showingSave {
        alert.addAction(UIAlertAction(title: "Save", style: .default) { _ in
            self.delegate?.editViewControllerDidFinish(self)
        })
    }
    
    alert.addAction(UIAlertAction(title: "Discard Changes", style: .destructive) { _ in
        self.delegate?.editViewControllerDidCancel(self)
    })
    
    alert.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler: nil))
    
    // 如果把提醒控制器呈现为弹出窗口（popover），则让弹出窗口指向 Cancel 按钮。
    alert.popoverPresentationController?.barButtonItem = cancelButton
    
    present(alert, animated: true, completion: nil)
}
```

## 另请参阅

### 呈现管理

- [UIPresentationController](uipresentationcontroller.md) — 管理视图控制器在屏幕上的过渡动画和呈现的对象。
- [UISheetPresentationController](uisheetpresentationcontroller.md) — 管理 sheet 的外观和行为的呈现控制器。

## 下载

- [DisablingThePullDownGestureForASheet.zip](https://docs-assets.developer.apple.com/published/2afc84a1a7e9/DisablingThePullDownGestureForASheet.zip)
