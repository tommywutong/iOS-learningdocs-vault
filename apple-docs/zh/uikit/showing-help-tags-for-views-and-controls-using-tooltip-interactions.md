---
title: 使用工具提示交互为视图和控件显示帮助标签
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/showing-help-tags-for-views-and-controls-using-tooltip-interactions
source_url: 'https://developer.apple.com/documentation/uikit/showing-help-tags-for-views-and-controls-using-tooltip-interactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/showing-help-tags-for-views-and-controls-using-tooltip-interactions.json'
content_hash: 'sha256:4d321aa6abb0414a'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# 使用工具提示交互为视图和控件显示帮助标签

<sub>示例代码</sub>

通过在指针悬停于元素上时显示工具提示，解释界面元素的用途。

## 概述

此示例展示如何显示工具提示（也称为 _帮助标签_），以解释界面元素（如视图或控件）的用途，或提供关于它的附加信息，而不会将人的焦点从主界面移开。当指针在视图或控件上悬停几秒钟时，工具提示会出现。工具提示会保持可见几秒钟，或直到指针离开该界面元素。

有关设计工具提示内容的指南，参见 macOS 《人机界面指南》的 [Help](https://developer.apple.com/design/human-interface-guidelines/macos/user-interaction/help/) 部分。

### 配置示例代码项目

在 macOS 12 或更高版本上运行时，示例 App 中会提供工具提示。要构建并运行示例 App：

1. 选择 Product \> Destination \> My Mac。
2. 点击 Product \> Run。

### 为视图添加工具提示

要在指针悬停于视图上时显示工具提示，示例会创建一个 [UIToolTipInteraction](uitooltipinteraction.md) 对象，并传入默认的工具提示文本。然后示例使用视图的 [- addInteraction:](<uiview/addinteraction(__).md>) 方法将该交互添加到 [UIView](uiview.md)。

```swift
lazy var viewWithDefaultTooltip: UIView = {
    let view = UIView()
    view.backgroundColor = UIColor.systemGreen
    view.addText("Hover the pointer over this view to see its default tooltip.")

    let tooltipInteraction = UIToolTipInteraction(defaultToolTip: "The default tooltip for the view.")
    view.addInteraction(tooltipInteraction)

    return view
}()
```

示例对其他类型的视图也使用相同的方法，例如为 [UILabel](uilabel.md) 的实例添加工具提示：

```swift
lazy var labelWithTooltip: UILabel = {
    let label = UILabel()
    label.text = "Hover the pointer over this label to see its tooltip."
    label.numberOfLines = 0
    
    let tooltipInteraction = UIToolTipInteraction(defaultToolTip: "The label's tooltip.")
    label.addInteraction(tooltipInteraction)
    
    return label
}()
```

### 为控件添加工具提示

对于派生自 [UIControl](uicontrol.md) 的界面元素，例如 [UIButton](uibutton.md)，示例使用 [toolTip](uicontrol/tooltip.md) 属性来设置工具提示中显示的默认文本，而不是向控件添加交互。

```swift
lazy var buttonWithTooltip: UIButton = {
    var configuration = UIButton.Configuration.filled()
    configuration.title = "Buy"
    configuration.subtitle = "Only $9.99"
    configuration.titleAlignment = .center
    
    let action = UIAction { _ in print("Thank you for your purchase.") }

    let button = UIButton(configuration: configuration, primaryAction: action)
    button.toolTip = "Click to buy this item. You'll have a chance to change your mind before confirming your purchase."
    button.preferredBehavioralStyle = .pad
    
    return button
}()
```

### 更改视图的工具提示文本

设置工具提示交互的 [defaultToolTip](uitooltipinteraction/defaulttooltip.md) 属性，以及设置控件的 [toolTip](uicontrol/tooltip.md) 属性，是显示在 App 运行期间不会更改的工具提示文本的便捷方式。然而，有时 App 需要根据 App 的状态或 App 特定的逻辑来决定工具提示的内容。例如，示例 App 会查找视图背景颜色的名称，并在指针悬停于该视图上时在工具提示中显示该名称。

要显示背景颜色名称的工具提示，示例会创建一个 [UIToolTipInteraction](uitooltipinteraction.md) 实例，并将其 [delegate](uitooltipinteraction/delegate.md) 属性设置为 `ViewWithBackgroundColorTooltip` 的实例，这是一个符合 [UIToolTipInteractionDelegate](uitooltipinteractiondelegate.md) 协议的自定义视图。然后示例将该交互添加到视图。

```swift
lazy var viewWithBackgroundColorTooltip: UIView = {
    let view = ViewWithBackgroundColorTooltip()
    view.backgroundColor = UIColor.systemYellow
    view.addText("Hover the pointer over this view to see the name of the view's background color.")

    let tooltipInteraction = UIToolTipInteraction()
    tooltipInteraction.delegate = view
    view.addInteraction(tooltipInteraction)
    
    return view
}()
```

接下来，`ViewWithBackgroundColorTooltip` 实现了 [- toolTipInteraction:configurationAtPoint:](<uitooltipinteractiondelegate/tooltipinteraction(__configurationat_).md>) 方法，并返回一个包含背景颜色名称作为工具提示文本的 [UIToolTipConfiguration](uitooltipconfiguration.md) 对象。如果颜色名称不可用，该方法返回 `nil`，从而阻止工具提示显示。

```swift
class ViewWithBackgroundColorTooltip: UIView, UIToolTipInteractionDelegate {
    
    func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration? {

        let configuration: UIToolTipConfiguration?
        if let accessibilityName = backgroundColor?.accessibilityName {
            configuration = UIToolTipConfiguration(toolTip: "The color is \(accessibilityName).")
        } else {
            configuration = nil
        }
        
        return configuration
    }

}
```

### 更改控件的工具提示文本

要更改像示例中的购物车按钮这类控件的工具提示文本，示例会像自定义视图那样提供一个工具提示交互 delegate。但这次它不创建工具提示交互，而是将按钮的 [toolTip](uicontrol/tooltip.md) 属性设置为默认文本。这会使控件创建一个 [UIToolTipInteraction](uitooltipinteraction.md) 对象，并将其赋给 [toolTipInteraction](uicontrol/tooltipinteraction.md) 属性。示例随后使用该属性为该交互分配一个 delegate。

```swift
lazy var shoppingCartButtonWithTooltip: UIButton = {
    var configuration = UIButton.Configuration.filled()
    configuration.title = "Add to Cart"
    configuration.image = UIImage(systemName: "cart.circle")
    configuration.imagePlacement = NSDirectionalRectEdge.leading
    configuration.imagePadding = 4
    
    let action = UIAction { [unowned self] _ in self.cartItemCount += 1 }
    
    let button = UIButton(configuration: configuration, primaryAction: action)
    button.toolTip = "Click to add the item to your cart. Your cart is empty."
    button.toolTipInteraction?.delegate = self
    
    return button
}()
```

示例还实现了 [- toolTipInteraction:configurationAtPoint:](<uitooltipinteractiondelegate/tooltipinteraction(__configurationat_).md>) delegate 方法，它返回一个包含描述按钮用途和购物车中商品数量的工具提示文本的 [UIToolTipConfiguration](uitooltipconfiguration.md) 对象。

```swift
func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration? {
    
    let text: String
    switch cartItemCount {
    case 0:
        text = "Click to add the item to your cart. Your cart is empty."
    case 1:
        text = "Click to add the item to your cart. Your cart contains \(cartItemCount) item."
    default:
        text = "Click to add the item to your cart. Your cart contains \(cartItemCount) items."
    }
    
    return UIToolTipConfiguration(toolTip: text)
}
```

### 指定悬停区域

除了在 [UIToolTipConfiguration](uitooltipconfiguration.md) 对象中设置工具提示文本外，delegate 还可以指定指针必须悬停的界面元素区域，以触发工具提示的显示。例如，示例 App 会显示一个视图，当指针悬停于该视图的顶部或底部区域时显示工具提示，但当指针悬停于中间区域时则不显示。

为了判断指针位置是否在视图的顶部或底部区域，示例使用 [- toolTipInteraction:configurationAtPoint:](<uitooltipinteractiondelegate/tooltipinteraction(__configurationat_).md>) 方法提供的 `point` 值。当指针位于这些区域之一时，delegate 方法会返回一个包含工具提示文本和源矩形的工具提示配置，该源矩形定义了指针必须悬停以触发工具提示显示的视图区域。

```swift
class ViewWithTooltipRegion: UIView, UIToolTipInteractionDelegate {

    func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration? {
        
        var topRect = self.bounds
        var bottomRect = self.bounds
        
        let partHeight = self.bounds.size.height / 3
        topRect.size.height = partHeight
        bottomRect.size.height = partHeight
        bottomRect.origin.y = partHeight * 2
        
        // Display the tooltip if the pointer is within the top or bottom rects.
        if topRect.contains(point) {
            return UIToolTipConfiguration(toolTip: "Top area of the view.", in: topRect)
        } else if bottomRect.contains(point) {
            return UIToolTipConfiguration(toolTip: "Bottom area of the view.", in: bottomRect)
        }
        
        // Pointer is in the middle of the view; don't display a tooltip.
        return nil
    }
    
}
```

在另一个示例中，示例使用工具提示配置的源矩形来指定文本视图中选定文本的区域。当指针悬停于选定文本上时，工具提示会出现；但当指针悬停于未选定文本上时，它不会出现。

```swift
class TextViewWithTooltip: UITextView, UIToolTipInteractionDelegate {
    
    func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration? {
        
        guard
            let selectedTextRange = self.selectedTextRange,
            selectedTextRange.isEmpty == false
        else {
            return nil
        }

        var unionedRect = firstRect(for: selectedTextRange)
        for selectionRect in selectionRects(for: selectedTextRange) {
            unionedRect = unionedRect.union(selectionRect.rect)
        }
        
        if let selectedText = text(in: selectedTextRange) {
            return UIToolTipConfiguration(toolTip: "Selected text: \(selectedText)", in: unionedRect)
        }
        
        return nil
    }
    
}
```

## 另请参阅

### Tooltips

- [UIToolTipInteraction](uitooltipinteraction.md) — 一种交互对象，使指针悬停于视图或控件上时能够显示工具提示。
- [UIToolTipInteractionDelegate](uitooltipinteractiondelegate.md) — 为交互提供工具提示设置的接口。

## 下载

- [ShowingHelpTagsForViewsAndControlsUsingTooltipInteractions.zip](https://docs-assets.developer.apple.com/published/199a44d512cb/ShowingHelpTagsForViewsAndControlsUsingTooltipInteractions.zip)
