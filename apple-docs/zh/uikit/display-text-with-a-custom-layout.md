---
title: 使用自定布局显示文本
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/display-text-with-a-custom-layout
source_url: 'https://developer.apple.com/documentation/uikit/display-text-with-a-custom-layout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/display-text-with-a-custom-layout.json'
content_hash: 'sha256:0f8c391aa46ef494'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md)

# 使用自定布局显示文本

<sub>示例代码</sub>

在自定形状的容器中布局文本，并应用字形替换（glyph substitution）。

## 概述

某些 App（例如图书和杂志阅读器、文本编辑器及游戏）可能需要以更符合自身 App 风格的方式来布局文本。TextKit 为这些 App 提供了一组用于实现自定文本布局（custom text layout）的 API。此示例演示了如何使用这些 API 在圆形容器和双栏容器中显示文本、如何为文本容器（text container）设置排除区域，以及如何在不更改文本存储的情况下替换字形。

### 实现自定形状的文本容器

布局一行文本时，TextKit 会调用 [NSTextContainer](nstextcontainer.md) 的 [- lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:](<nstextcontainer/linefragmentrect(forproposedrect_at_writingdirection_remaining_).md>) 方法，以确定该行的位置和大小；TextKit 将其称为_行片段矩形_。通过创建 `NSTextContainer` 的子类，并在该方法中返回自定行片段矩形，App 可以实现自定形状的文本容器。

此示例使用 `CircleTextContainer` 类实现圆形文本容器。为了计算适合容器 bounds 内切圆的行片段矩形，该类会调用 `super` 的实现来检索默认矩形，然后根据当前行原点和容器大小调整其 `origin.x` 与 `width`。

```swift
override func lineFragmentRect(forProposedRect proposedRect: CGRect,
                               at characterIndex: Int,
                               writingDirection baseWritingDirection: NSWritingDirection,
                               remaining remainingRect: UnsafeMutablePointer<CGRect>?) -> CGRect {
    let rect = super.lineFragmentRect(forProposedRect: proposedRect,
                                      at: characterIndex,
                                      writingDirection: baseWritingDirection,
                                      remaining: remainingRect)
    let containerWidth = Float(size.width), containerHeight = Float(size.height)

    let diameter = fminf(containerWidth, containerHeight)
    let radius = diameter / 2.0
    
    // 从行中心到容器中心的垂直距离。
    let yDistance = fabsf(Float(rect.origin.y + rect.size.height / 2.0) - radius)
    // 新的行宽。
    let width = (yDistance < radius) ? 2.0 * sqrt(radius * radius - yDistance * yDistance) : 0.0
    // 从 rect.origin.x 到行起点的水平距离。
    let xOffset = (containerWidth > diameter) ? (containerWidth - diameter) / 2.0 : 0.0
    // 行的起始 x 坐标。
    let xPosition = CGFloat(xOffset + Float(rect.origin.x) + radius - width / 2.0)
    return CGRect(x: xPosition, y: CGFloat(rect.origin.y), width: CGFloat(width), height: rect.size.height)
}
```

### 使用自定文本容器布局文本

若要使用自定文本容器布局文本，App 只需使用该容器设置文本视图，其余工作交给 TextKit 即可。[UITextView](uitextview.md) 的 [- initWithFrame:textContainer:](<uitextview/init(frame_textcontainer_).md>) 方法可用于此目的，此示例用它创建具有圆形文本容器的 `UITextView` 实例。

```swift
let textContainer = CircleTextContainer(size: .zero)
textContainer.widthTracksTextView = true

let layoutManager = NSLayoutManager()
layoutManager.addTextContainer(textContainer)
textStorage.addLayoutManager(layoutManager)

textView = UITextView(frame: CGRect.zero, textContainer: textContainer)
```

采用此配置后，负责协调字符布局与显示的 TextKit 类 [NSLayoutManager](nslayoutmanager.md) 会自动使用 `CircleTextContainer` 返回的行片段矩形来布局文本。

`NSLayoutManager` 支持在多个文本容器中布局文本，因此实现双栏布局只需向布局管理器添加第二个文本容器，如以下代码所示：

```swift
let firstTextContainer = NSTextContainer()
firstTextContainer.widthTracksTextView = true
firstTextContainer.heightTracksTextView = true

let secondTextContainer = NSTextContainer()
secondTextContainer.widthTracksTextView = true
secondTextContainer.heightTracksTextView = true
secondTextContainer.lineBreakMode = .byTruncatingTail

let layoutManager = NSLayoutManager()
layoutManager.addTextContainer(firstTextContainer)
layoutManager.addTextContainer(secondTextContainer)

textStorage.addLayoutManager(layoutManager)

let firstTextView = UITextView(frame: .zero, textContainer: firstTextContainer)
firstTextView.isScrollEnabled = false
view.addSubview(firstTextView)

let secondTextView = UITextView(frame: .zero, textContainer: secondTextContainer)
secondTextView.isScrollEnabled = false
view.addSubview(secondTextView)
```

请注意，向布局管理器添加第二个文本容器后，文本视图会变为不可编辑且不可选择。

### 在文本容器中预留区域

为了创建美观的 UI，某些 App 可能希望文本环绕某种形状。它们可以使用 `NSTextContainer` 的 [exclusionPaths](nstextcontainer/exclusionpaths.md) 属性，在文本容器中为该形状预留排除区域。

此示例使用以下代码设置排除区域，其中 `translatedCirclePath` 是一个使用文本容器坐标系的 [UIBezierPath](uibezierpath.md) 实例。

```swift
textView.textContainer.exclusionPaths = [translatedCirclePath]
```

### 在不更改文本存储的情况下替换字形

当文本容器没有足够空间显示文本时，App 可能需要一种方式来表明容器中还有更多文本，也就是_溢出_文本。标准文本容器可以使用 `NSTextContainer` 的 [lineBreakMode](nstextcontainer/linebreakmode.md) 属性添加结尾省略号，以帮助处理这种情况，但该属性并不完全支持 `CircleTextContainer` 这样的自定形状容器。

为了在圆形文本容器中显示溢出指示符，同时演示 TextKit 的字形替换和布局调整能力，此示例会使用省略号替换容器末尾字符的字形，并使省略号成为容器中最后一个可见字形。

末尾字符是最后几个单词中的字符，它们的总宽度要大于省略号。字符必须更宽，文本容器才有足够空间显示省略号。然而，由于这些字符更宽，字形替换后文本容器中会出现额外空间，从而可能带入更多字符。为避免在省略号后显示文本，此示例执行第二次字形替换：选择容器最后一个单词旁的字符，并将其替换为使用 [NSControlCharacterActionWhitespace](nslayoutmanager/controlcharacteraction/whitespace.md) 操作的控制字形。通过此替换，该字符会变为宽度可变的空白。利用这个可变空白字符，示例可以填满额外空间，将额外字符推到下一行，然后将该行移出文本容器。

字形替换和布局调整的详细实现如下：

- 通过使末尾字符的字形和布局失效（invalidate）来开始字形替换。

```swift
layoutManager.invalidateGlyphs(forCharacterRange: endingWordsCharRange, changeInLength: 0,
                               actualCharacterRange: nil)
layoutManager.invalidateLayout(forCharacterRange: endingWordsCharRange,
                               actualCharacterRange: nil)
```

- 实现 [NSLayoutManagerDelegate](nslayoutmanagerdelegate.md) 的 [- layoutManager:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:](<nslayoutmanagerdelegate/layoutmanager(__shouldgenerateglyphs_properties_characterindexes_font_forglyphrange_).md>) 方法来替换字形。TextKit 会在存储字形之前调用此委托（delegate）方法，让 App 有机会更改字形及其属性。

```swift
let ellipsisStartIndex = ellipsisIntersection.location
for index in ellipsisStartIndex..<ellipsisStartIndex + ellipsisIntersection.length {
    if index == ellipsisGlyphRange!.location {
        finalGlyphs[index - glyphRange.location] = myGlyphs[0]
    } else {
        finalProps[index - glyphRange.location] = .controlCharacter
    }
}
let flexibleSpaceStartIndex = flexibleSpaceIntersection.location
for index in  flexibleSpaceStartIndex..<flexibleSpaceStartIndex + flexibleSpaceIntersection.length {
    finalProps[index - glyphRange.location] = .controlCharacter
}
```

- 实现 [- layoutManager:shouldUseAction:forControlCharacterAtIndex:](<nslayoutmanagerdelegate/layoutmanager(__shoulduse_forcontrolcharacterat_).md>) 方法，为可变空白字符返回 `NSLayoutManager.ControlCharacterAction.whitespace` 操作。

```swift
func layoutManager(_ layoutManager: NSLayoutManager, shouldUse action: NSLayoutManager.ControlCharacterAction,
                   forControlCharacterAt charIndex: Int) -> NSLayoutManager.ControlCharacterAction {
    if let flexibleSpaceGlyphRange = self.flexibleSpaceGlyphRange,
        flexibleSpaceGlyphRange.contains(layoutManager.glyphIndexForCharacter(at: charIndex)) {
        return .whitespace
    }
    return action
}
```

- 实现 [- layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:](<nslayoutmanagerdelegate/layoutmanager(__boundingboxforcontrolglyphat_for_proposedlinefragment_glyphposition_characterindex_).md>) 方法，返回能够填满当前行片段矩形的边界框。

```swift
func layoutManager(_ layoutManager: NSLayoutManager,
                   boundingBoxForControlGlyphAt glyphIndex: Int,
                   for textContainer: NSTextContainer,
                   proposedLineFragment proposedRect: CGRect,
                   glyphPosition: CGPoint,
                   characterIndex charIndex: Int) -> CGRect {
    guard let flexibleSpaceGlyphRange = self.flexibleSpaceGlyphRange,
        flexibleSpaceGlyphRange.contains(glyphIndex) else {
        return CGRect(x: glyphPosition.x, y: glyphPosition.y, width: 0, height: proposedRect.height)
    }
    let padding = textContainer.lineFragmentPadding * 2
    let width = proposedRect.width - (glyphPosition.x - proposedRect.minX) - padding
    let rect = CGRect(x: glyphPosition.x, y: glyphPosition.y, width: width, height: proposedRect.height)
    return rect
}
```

- 实现 [- layoutManager:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:inTextContainer:forGlyphRange:](<nslayoutmanagerdelegate/layoutmanager(__shouldsetlinefragmentrect_linefragmentusedrect_baselineoffset_in_forglyphrange_).md>) 方法，将额外的一行移出文本容器。

```swift
func layoutManager(_ layoutManager: NSLayoutManager,
                   shouldSetLineFragmentRect lineFragmentRect: UnsafeMutablePointer<CGRect>,
                   lineFragmentUsedRect: UnsafeMutablePointer<CGRect>,
                   baselineOffset: UnsafeMutablePointer<CGFloat>,
                   in textContainer: NSTextContainer,
                   forGlyphRange glyphRange: NSRange) -> Bool {
    guard let ellipsisGlyphRange = self.ellipsisGlyphRange,
        glyphRange.location > ellipsisGlyphRange.location else {
            return false
    }
    let originX = textContainer.size.width
    lineFragmentRect.pointee.origin = CGPoint(x: originX, y: lineFragmentRect.pointee.origin.y)
    return true
}
```

## 另请参阅

### 布局

- [使用 TextKit 2 与文本交互](using-textkit-2-to-interact-with-text.md) — 通过管理文本选择和插入自定文本元素来与文本交互。
- [在文本视图中管理视口布局和附件复用](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) — 在文本视图子类中自定布局并保留附件视图。
- [NSTextLayoutManager](nstextlayoutmanager.md) — 用于管理自定文本显示的文本布局与呈现的主要类。
- [NSTextContainer](nstextcontainer.md) — 进行文本布局的区域。
- [NSTextLayoutFragment](nstextlayoutfragment.md) — 表示布局片段的类，该片段通常对应于图层或视图子类等渲染表面。
- [NSTextLineFragment](nstextlinefragment.md) — 表示行片段的类；行片段是文本布局片段中的单个文本布局和渲染单元。
- [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) — 管理视口内与其委托交互的布局过程。
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — 将视图或图层标识为文本布局片段可绘制元素的协议。_(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — 允许你在存储或检索渲染表面时使用对象标识该表面的协议。
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — 定义对象文本方向的一组方法。

## 下载

- [DisplayTextWithACustomLayout.zip](https://docs-assets.developer.apple.com/published/c94cdd160e47/DisplayTextWithACustomLayout.zip)
