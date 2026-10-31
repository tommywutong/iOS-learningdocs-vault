---
title: 管理文本视图子类中的视口布局与附件重用
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass
source_url: 'https://developer.apple.com/documentation/uikit/managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.json'
content_hash: 'sha256:33a3176247b956cd'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md)

# 管理文本视图子类中的视口布局与附件重用

<sub>文章</sub>

在文本视图子类中自定布局并保留附件视图。

## 概述

如果你构建了一个包含丰富附件（如图像、视频或交互式控件）的文本编辑器，你可能会注意到，当某人滚动使附件离开视口，或在同一段落中输入时，附件视图会闪烁或丢失状态。这是因为文本视图在正常布局过程中会丢弃并重新创建附件视图。

[UITextView](uitextview.md) 与 [NSTextView](../appkit/nstextview.md) 遵循 [NSTextViewportLayoutControllerDelegate](nstextviewportlayoutcontrollerdelegate.md)，让你的子类可以直接访问布局过程。你可以重写委托方法来响应布局事件，并自定文本片段的显示方式。

你还可以注册重用策略，告诉文本视图在滚动与编辑过程中保留哪些附件视图，从而消除闪烁并保留焦点与播放位置等状态。

### 重写视口布局方法

[- layoutViewport](<nstextviewportlayoutcontroller/layoutviewport().md>) 包含视口布局过程。每次视口内的视觉状态发生变化时，TextKit 都会调用它。在每次视口布局过程中，[NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) 会在三个点调用文本视图的委托方法——开始之前、每个文本布局片段即将渲染之前，以及完成后。在 [UITextView](uitextview.md)（或 macOS 上的 [NSTextView](../appkit/nstextview.md)）子类中重写这些方法中的任意一个，以自定每个阶段发生的事情：

```swift
class CustomTextView: UITextView {

    override func textViewportLayoutControllerWillLayout(
        _ textViewportLayoutController: NSTextViewportLayoutController
    ) {
        super.textViewportLayoutControllerWillLayout(textViewportLayoutController)
        // Prepare any state before the layout pass begins.
    }

    override func textViewportLayoutController(
        _ textViewportLayoutController: NSTextViewportLayoutController,
        configureRenderingSurfaceFor textLayoutFragment: NSTextLayoutFragment
    ) {
        super.textViewportLayoutController(textViewportLayoutController, configureRenderingSurfaceFor: textLayoutFragment)
        // Inspect or customize each laid-out text fragment.
    }

    override func textViewportLayoutControllerDidLayout(
        _ textViewportLayoutController: NSTextViewportLayoutController
    ) {
        super.textViewportLayoutControllerDidLayout(textViewportLayoutController)
        // Finalize layout after all fragments are positioned.
    }
}
```

> [!important] 重要
> 所有视口布局委托方法的重写都必须调用 `super`，因为省略它会破坏布局。只能在 [- textViewportLayoutControllerDidLayout:](<uitextview/textviewportlayoutcontrollerdidlayout(__).md>) 中查询任何 [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) 状态；从其他委托方法查询它可能导致崩溃。

下表显示可用的重写点集合：

| 方法 | 调用时机 |
|---|---|
| [- textViewportLayoutControllerWillLayout:](<uitextview/textviewportlayoutcontrollerwilllayout(__).md>) | 每次布局过程开始之前 |
| [- textViewportLayoutController:configureRenderingSurfaceForTextLayoutFragment:](<uitextview/textviewportlayoutcontroller(__configurerenderingsurfacefor_).md>) | 每个已布局片段一次，附带其渲染表面 |
| [- textViewportLayoutControllerDidLayout:](<uitextview/textviewportlayoutcontrollerdidlayout(__).md>) | 每次布局过程完成后 |
| [- textViewportLayoutControllerReceivedSetNeedsLayout:](<uitextview/textviewportlayoutcontrollerreceivedsetneedslayout(__).md>) | 当视口请求布局失效时 |
| [- viewportBoundsForTextViewportLayoutController:](<uitextview/viewportbounds(for_).md>) | 查询当前视口边界时 |

### 注册重用策略

使用注册 API 在布局过程中保留附件视图。在设置期间调用一次 [- registerTextAttachmentViewProviderReusePolicy:forTextAttachmentViewProviderType:](<uitextview/register(__fortextattachmentviewprovidertype_).md>)，为每个提供者类型声明重用行为：

```swift
// Retain video attachment views across both scrolling and paragraph edits.
textView.register(
    [.onScrollingOutOfViewport, .onEditingInlineParagraphs],
    forTextAttachmentViewProviderType: VideoAttachmentViewProvider.self
)

// Retain drawing views only when they scroll out of view.
textView.register(
    [.onScrollingOutOfViewport],
    forTextAttachmentViewProviderType: DrawingAttachmentViewProvider.self
)
```

注册提供者类型后，当滚动使其离开视图或编辑更改周围段落时，文本视图会保留这些附件视图，并在它们回来时恢复它们。这会自动在滚动与段落编辑过程中保持视频播放位置与聚焦控件的完整性。

## 另请参阅

### 布局

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md) — 通过管理文本选择与插入自定文本元素来与文本交互。
- [Display text with a custom layout](display-text-with-a-custom-layout.md) — 在自定形状的容器中布局文本并应用字形替换。
- [NSTextLayoutManager](nstextlayoutmanager.md) — 用于管理文本布局与呈现以实现自定文本显示的主类。
- [NSTextContainer](nstextcontainer.md) — 文本布局发生的区域。
- [NSTextLayoutFragment](nstextlayoutfragment.md) — 一个表示布局片段的类，通常对应于渲染表面，如图层或视图子类。
- [NSTextLineFragment](nstextlinefragment.md) — 一个表示行片段的类，作为文本布局片段内的单个文本布局与渲染单位。
- [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) — 管理视口内布局过程并与委托交互。
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — 一个协议，将视图或图层标识为文本布局片段的可绘制元素。 _(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — 一个协议，允许你使用对象在存储或检索渲染表面时标识它。
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — 一组定义对象文本方向的方法。
