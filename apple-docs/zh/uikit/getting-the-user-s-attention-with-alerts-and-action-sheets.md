---
title: 使用提醒和操作表单吸引用户的注意
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/getting-the-user-s-attention-with-alerts-and-action-sheets
source_url: 'https://developer.apple.com/documentation/uikit/getting-the-user-s-attention-with-alerts-and-action-sheets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/getting-the-user-s-attention-with-alerts-and-action-sheets.json'
content_hash: 'sha256:63f3a103733f4a5f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [窗口与屏幕](windows-and-screens.md)

# 使用提醒和操作表单吸引用户的注意

<sub>文章</sub>

向用户呈现重要信息，或就重要选择向他们发出提示。

## 概述

当你的 App 需要用户提供额外信息或确认时，显示提醒或操作表单。提醒和操作表单会中断 App 的正常流程，向用户显示一条消息。下图展示了一个提醒，用户通过选择列出的选项之一来关闭它。

![](../../../attachments/1c688fcfd28582b45d9ae21668e5f617/getting-the-user-s-attention-with-alerts-and-action-sheets-1@2x.png)

<sub>一个提醒，标题为“A Short Title is Best”，消息为“A message needs to be a short, complete sentence.”，并带有“OK”和“Cancel”按钮。</sub>

下图展示了一个操作表单。用户通过选择列出的选项之一，或点按操作表单外部区域来关闭它。

![](../../../attachments/38460444831a172cb1a2d7283ddc3903/getting-the-user-s-attention-with-alerts-and-action-sheets-2@2x.png)

<sub>显示的操作表单，消息为“A message needs to be a short, complete sentence.”，并带有一个“Confirm”按钮。</sub>

> [!important] 重要
> 提醒和操作表单会打断用户当前的任务，因此要谨慎使用，只在绝对必要时才使用它们。关于何时使用它们的详细指导，请参阅[《人机界面指南》](https://developer.apple.com/design/human-interface-guidelines/presentation)中的“Action sheets”和“Alerts”。

### 呈现提醒

要显示提醒，请创建一个 [UIAlertController](uialertcontroller.md) 对象，对其进行配置，然后以该对象作为参数调用 [- presentViewController:animated:completion:](<uiviewcontroller/present(__animated_completion_).md>)，如下方代码所示。配置提醒控制器包括指定你希望用户看到的标题和消息，以及他们可以选择的操作。在呈现提醒控制器之前，至少要向其中添加一个操作 —— 由 [UIAlertAction](uialertaction.md) 对象表示。

```swift
@IBAction func agreeToTerms() {
   // Create the action buttons for the alert.
   let defaultAction = UIAlertAction(title: "Agree", 
                        style: .default) { (action) in
	// Respond to the person's selection of the action.
   }
   let cancelAction = UIAlertAction(title: "Disagree", 
                        style: .cancel) { (action) in
	// Respond to the person's selection of the action.
   }
   
   // Create and configure the alert controller.     
   let alert = UIAlertController(title: "Terms and Conditions",
         message: "Click Agree to accept the terms and conditions.",
         preferredStyle: .alert)
   alert.addAction(defaultAction)
   alert.addAction(cancelAction)
        
   self.present(alert, animated: true) {
      // The system presented the alert.
   }
}
```

### 呈现操作表单

在 iPhone 和 iPad 上，都在弹出窗口内显示操作表单。要在弹出窗口中显示你的操作表单，请使用提醒控制器的 [popoverPresentationController](uiviewcontroller/popoverpresentationcontroller.md) 属性指定弹出窗口的锚点。

```swift
@IBAction func deleteItem() {
   let destroyAction = UIAlertAction(title: "Delete", 
             style: .destructive) { (action) in
	// Respond to user selection of the action.
   }
   let cancelAction = UIAlertAction(title: "Cancel", 
             style: .cancel) { (action) in
	// Respond to user selection of the action.
   }
        
   let alert = UIAlertController(title: "Delete the image?", 
               message: "", 
               preferredStyle: .actionSheet)
   alert.addAction(destroyAction)
   alert.addAction(cancelAction)
        
   alert.popoverPresentationController?.sourceItem = 
               self.trashButton
        
   self.present(alert, animated: true) {
      // The system presented the alert.
   }
}
```

配置弹出窗口呈现控制器的 [sourceItem](uipopoverpresentationcontroller/sourceitem.md)，将弹出窗口锚定到某个 [UIBarButtonItem](uibarbuttonitem.md) 或 [NSToolbarItem](../appkit/nstoolbaritem.md)。当用户点按该按钮时，弹出窗口会从指定项目处以动画形式出现并替换它，直到用户选择某个操作项目或关闭弹出窗口为止。

或者，你也可以使用 [sourceView](uipopoverpresentationcontroller/sourceview.md) 和 [sourceRect](uipopoverpresentationcontroller/sourcerect.md) 属性来指定弹出窗口的锚点位置。

> [!note] 注意
> 如果你的操作集合中包含一个配置为 [UIAlertActionStyleCancel](uialertaction/style-swift.enum/cancel.md) 样式的按钮，当在弹出窗口中显示你的操作表单时，UIKit 会移除该按钮。点按弹出窗口外部的任意位置，效果与点按“Cancel”按钮相同，包括会调用你的操作处理程序。

## 另请参阅

### 提醒

- [UIAlertController](uialertcontroller.md) — 一个用于显示提醒消息的对象。
- [UIAlertAction](uialertaction.md) — 用户点按提醒中的按钮时可以执行的一项操作。
