---
title: 将指针交互集成到你的 iPad App
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, Xcode 12.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/integrating-pointer-interactions-into-your-ipad-app
source_url: 'https://developer.apple.com/documentation/uikit/integrating-pointer-interactions-into-your-ipad-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/integrating-pointer-interactions-into-your-ipad-app.json'
content_hash: 'sha256:26e056d7dd7b0360'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Pointer interactions](pointer-interactions.md)

# 将指针交互集成到你的 iPad App

<sub>示例代码</sub>

通过向视图添加指针交互，支持你的 iPad App 中的触摸交互。

## 概述

此示例代码项目展示了如何使用 [UIPointerInteraction](uipointerinteraction.md) 类。指针交互支持为视图添加效果，并自定义指针在 App 某个区域内的外观。它增强了鼠标和触控板设备的用户体验，并减少了用户在硬件键盘和 iPad 触摸屏之间移动手的需要。示例在 App 的 `ViewController` 的画布中放置了四个形状视图，每个都可以移动。这些形状视图是矩形、椭圆、圆角矩形和三角形。当用户在它们上方移动光标时，每个都会呈现不同的指针效果。此外，示例还展示了一个自定义 [UIControl](uicontrol.md) 子类，以说明控件如何采用指针交互。

### 为按钮添加指针交互

示例向 [UIButton](uibutton.md) 添加指针交互。自定义指针交互需要一个 [UIButtonPointerStyleProvider](uibuttonpointerstyleprovider.md) 函数。在应用样式提供函数时，UIKit 会向 App 传递一个指针效果和该按钮区域内的指针形状；App 随后为该特定按钮返回一个指针样式。开发者可以选择和使用系统推荐的效果和形状、替换其中一个，或创建完全自定义的样式。示例为其按钮应用了四种不同的指针效果：automatic、highlight、lift 和 hover。对于第五个按钮，应用了自定义的指针悬停效果，因此其效果在悬停时保持相同大小，并使用自定义 [UIPointerShape](uipointershape-swift.enum.md)。

### 为指针交互提供自定义视图

示例实现了形状视图，它们是名为 `ShapeView` 的 [UIView](uiview.md) 子类。它们通过设备的触摸屏和触控板与触摸事件交互。为了在视觉上与形状视图交互，会为其分配一个 [UIPointerInteraction](uipointerinteraction.md) 对象。视图控制器采用 [UIPointerInteractionDelegate](uipointerinteractiondelegate.md) 来帮助描述该指针交互如何操作。

### 为视图添加指针交互

指针交互由指针样式或视觉表示来描述。指针样式由带有 [UITargetedPreview](uitargetedpreview.md) 的 [UIPointerEffect](uipointereffect-swift.enum.md) 以及 [UIPointerShape](uipointershape-swift.enum.md) 组成。指针效果常用的形状是圆角矩形。指针形状或 `UIPointerShape` 需要一个 [UIBezierPath](uibezierpath.md)，用于描述该形状。示例通过像这样添加一个指针交互，将其与形状视图关联：

```swift
shapeView.addInteraction(UIPointerInteraction(delegate: self))
```

### 为指针交互创建 targeted preview

为了让形状视图在指针交互期间描述其外观，它必须提供 [UITargetedPreview](uitargetedpreview.md)。`UITargetedPreview` 为 UIKit 提供一个视图，用于在指针交互期间应用效果：

```swift
func targetedPreview() -> UITargetedPreview? {
    let parameters = UIPreviewParameters()
    
    // Use the entire view's shape for the preview.
    let visiblePath = viewPath
    parameters.visiblePath = visiblePath
    
    return UITargetedPreview(view: self, parameters: parameters)
}
```

当用户在形状视图内移动点时，指针交互会显示此 targeted preview。注意，targeted preview 也通过 [UIContextMenuConfiguration](uicontextmenuconfiguration.md) 与上下文菜单一起使用。在示例中，形状视图具有上下文菜单。

### 为指针交互创建指针效果

指针交互需要一个视觉效果来描述它如何渲染形状视图的 targeted preview。例如，椭圆形状视图使用 [UIPointerLiftEffect](uipointerlifteffect.md)，它会略微抬起 targeted preview，并在指针在椭圆形状内移动时滑动它。其他形状视图有各自的指针效果。矩形视图使用 [UIPointerEffect](uipointereffect-swift.enum.md)，圆角矩形视图使用 [UIPointerHighlightEffect](uipointerhighlighteffect.md)，三角形视图使用 [UIPointerHoverEffect](uipointerhovereffect.md)，它允许其 [UIPointerShape](uipointershape-swift.enum.md) 以三角形形式显示。

### 为指针交互创建形状

示例为其每个形状视图创建一个区域或形状，以便指针交互检测在哪里交互。示例还实现了 [UIPointerInteractionDelegate](uipointerinteractiondelegate.md) 的 [- pointerInteraction:regionForRequest:defaultRegion:](<uipointerinteractiondelegate/pointerinteraction(__regionfor_defaultregion_).md>)。当指针在指针交互的视图内移动时，UIKit 会调用此 delegate。返回要在其中应用指针样式的 [UIPointerRegion](uipointerregion.md)，或返回 `nil`，表示此交互不对当前位置自定义指针。

```swift
func pointerInteraction(_ interaction: UIPointerInteraction,
                        regionFor request: UIPointerRegionRequest,
                        defaultRegion: UIPointerRegion) -> UIPointerRegion? {
    var pointerRegion: UIPointerRegion? = nil
    
    if let view = interaction.view as? ShapeView {
        // Pointer has entered one of the shape views.
 
        // Check for modifiers keys pressed while inside the view path.
        if request.modifiers.contains(.command) && request.modifiers.contains(.alternate) {
            // Command + Option were both pressed, dim the view.
            view.alpha = 0.50
        } else {
            if view.alpha != 1.0 { view.alpha = 1.0 }
        }
        
        // The user interacted with the inner path region.
        pointerRegion =
            UIPointerRegion(rect: view.innerPath.bounds,
                            identifier: ShapeView.regionIdentifier)
    } else if let view = interaction.view as? AlphaControl {
        // Pointer has entered the alpha control.
        if view.bounds.contains(request.location) {
            pointerRegion =
                UIPointerRegion(rect: view.bounds,
                                identifier: AlphaControl.regionIdentifier)
        }
    }
  
    return pointerRegion
}
```

例如，椭圆形状视图会从其椭圆形 [UIBezierPath](uibezierpath.md) 内部与指针交互。

### 使用手势识别器与视图交互

为了使形状视图更具交互性，并提供由鼠标或触控板驱动的自定义行为，示例向每个形状视图附加了四种不同的手势识别器，与它们的指针交互协同工作。

[UIPanGestureRecognizer](uipangesturerecognizer.md) 移动形状视图，并在 pan 手势期间按住 command 键时，框架颜色变为橙色。

[UIPinchGestureRecognizer](uipinchgesturerecognizer.md) 通过双指捏合手势更改形状的大小。

[UITapGestureRecognizer](uitapgesturerecognizer.md) 将被轻点的形状视图带到前面。

[UIHoverGestureRecognizer](uihovergesturerecognizer.md) 当光标位于形状视图上方时，将其框架颜色更改为蓝色。如果用户在悬停时按住 command 键，框架颜色会切换为粉色。

下面是将 [UIHoverGestureRecognizer](uihovergesturerecognizer.md) 处理到 `ShapeView` 的示例：

```swift
func hoverShape(_ gestureRecognizer: UIHoverGestureRecognizer) {
    guard let shapeViewToUse = gestureRecognizer.view as? ShapeView else { return }

    switch gestureRecognizer.state {
    case .began, .changed:
        // User hovered within the view's path, change the view's border color.
        var pathViewColor = UIColor.systemTeal
        if gestureRecognizer.modifierFlags.contains(.command) {
            // If the command key is pressed while hovering change frame color to pink.
            pathViewColor = UIColor.systemPink
        }
        shapeViewToUse.viewPathColor = pathViewColor
        shapeViewToUse.setNeedsDisplay()

    case .ended, .cancelled:
        // User left the view, restore the border color.
        shapeViewToUse.restoreOuterFrameColor()

    default:
        break
    }
}
```

### 为连续滚动创建手势识别器

[UIPanGestureRecognizer](uipangesturerecognizer.md) 识别来自触控板等设备的连续滚动。示例向自定义 [UIControl](uicontrol.md) 子类 `AlphaControl` 添加 pan 手势识别器，识别双指滚动手势以更改给定颜色的 alpha 值。将 [allowedScrollTypesMask](uipangesturerecognizer/allowedscrolltypesmask.md) 设置为 [UIScrollTypeMaskContinuous](uiscrolltypemask/continuous.md)，App 就能识别连续滚动。控件的颜色样本会随着用户执行 pan 滚动手势或通过直接触摸而变化。

## 另请参阅

### 基础

- [UIPointerInteraction](uipointerinteraction.md) — 一种交互，支持在视图上添加效果，或自定义指针在 App 某个区域内的外观。
- [UIPointerInteractionDelegate](uipointerinteractiondelegate.md) — 处理交互视图内指针移动的接口。
- [Enhancing your iPad app with pointer interactions](enhancing-your-ipad-app-with-pointer-interactions.md) — 通过结合指针内容效果和形状自定义，为指点设备提供出色的用户体验。

## 下载

- [IntegratingPointerInteractionsIntoYourIPadApp.zip](https://docs-assets.developer.apple.com/published/dd68adc3cd24/IntegratingPointerInteractionsIntoYourIPadApp.zip)
