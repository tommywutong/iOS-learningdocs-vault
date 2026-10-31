---
title: 禁用表单的下拉手势
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

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md)

# 禁用表单的下拉手势

<sub>示例代码</sub>

在以表单方式呈现视图控制器时确保良好的用户体验。

## 概述

默认情况下，用户可以使用下拉手势来关闭以表单方式呈现的视图控制器。UIKit 允许你在使用该手势可能导致用户丢失数据或最近更改的情况下禁用下拉手势。也可以通过呈现 [UIAlertController](uialertcontroller.md) 的实例来解释用户为何无法关闭视图控制器的呈现。

### 禁用关闭呈现的能力

要禁用关闭视图控制器的呈现，请把 [modalInPresentation](uiviewcontroller/ismodalinpresentation.md) 设为 `true`。

```swift
// If there are unsaved changes, enable the Save button and disable the ability to
// dismiss using the pull-down gesture.
saveButton.isEnabled = hasChanges
isModalInPresentation = hasChanges
```

也可以从呈现委托的 [- presentationControllerShouldDismiss:](<uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(__).md>) 方法返回 `false`。然而，如果 [modalInPresentation](uiviewcontroller/ismodalinpresentation.md) 为 `true` 或以编程方式关闭呈现时，系统不会调用此方法。

### 解释用户为何无法关闭呈现

要在用户尝试关闭已禁用关闭的呈现时执行动作，请按下面的代码设置呈现的委托：

```swift
// Set the editViewController to be the delegate of the presentationController for this presentation.
// editViewController can then respond to attempted dismissals.
navigationController.presentationController?.delegate = editViewController
```

设置委托后，实现 [- presentationControllerDidAttemptToDismiss:](<uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss(__).md>) 并执行动作。下面的示例展示呈现 [UIAlertController](uialertcontroller.md) 实例：

```swift
func presentationControllerDidAttemptToDismiss(_ presentationController: UIPresentationController) {
    // The system calls this delegate method whenever the user attempts to pull
    // down to dismiss and `isModalInPresentation` is false.
    // Clarify the user's intent by asking whether they want to cancel or save.
    confirmCancel(showingSave: true)
}

// MARK: - Cancellation Confirmation

func confirmCancel(showingSave: Bool) {
    // Present a UIAlertController as an action sheet to have the user confirm losing any
    // recent changes.
    let alert = UIAlertController(title: nil, message: nil, preferredStyle: .actionSheet)
    
    // Only ask if the user wants to save if they attempt to pull to dismiss, not if they tap Cancel.
    if showingSave {
        alert.addAction(UIAlertAction(title: "Save", style: .default) { _ in
            self.delegate?.editViewControllerDidFinish(self)
        })
    }
    
    alert.addAction(UIAlertAction(title: "Discard Changes", style: .destructive) { _ in
        self.delegate?.editViewControllerDidCancel(self)
    })
    
    alert.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler: nil))
    
    // If presenting the alert controller as a popover, point the popover at the Cancel button.
    alert.popoverPresentationController?.barButtonItem = cancelButton
    
    present(alert, animated: true, completion: nil)
}
```

## 另请参阅

### 呈现管理

- [UIPresentationController](uipresentationcontroller.md) — 一个管理过渡动画以及在屏幕上呈现视图控制器的对象。
- [UISheetPresentationController](uisheetpresentationcontroller.md) — 一个管理表单外观与行为的呈现控制器。

## 下载

- [DisablingThePullDownGestureForASheet.zip](https://docs-assets.developer.apple.com/published/2afc84a1a7e9/DisablingThePullDownGestureForASheet.zip)
