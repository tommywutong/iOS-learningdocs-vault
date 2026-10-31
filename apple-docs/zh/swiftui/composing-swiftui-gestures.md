---
title: 组合 SwiftUI 手势
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/composing-swiftui-gestures
source_url: 'https://developer.apple.com/documentation/swiftui/composing-swiftui-gestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/composing-swiftui-gestures.json'
content_hash: 'sha256:15313e70d6ab75db'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [手势](gestures.md)

# 组合 SwiftUI 手势

<sub>文章</sub>

组合手势以创建复杂的交互。

## 概述

当你向 App 的视图层级结构添加多个手势时，需要决定这些手势之间如何交互。你使用手势组合来定义 SwiftUI 识别手势的顺序。有三种手势组合类型：

- 同时（Simultaneous）
- 顺序（Sequenced）
- 互斥（Exclusive）

当你同时组合手势修饰符时，SwiftUI 必须同时识别所有子手势模式，才能识别组合后的手势。当你按先后顺序串接手势修饰符时，SwiftUI 必须按顺序识别每个子手势。最后，当你以互斥方式组合手势时，SwiftUI 只识别其中一个子手势而无法识别其他子手势时，就会识别整个手势模式。

### 将一个手势串接在另一个之后

当你把一个手势串接在另一个之后时，SwiftUI 会先识别第一个手势，再识别第二个手势。例如，要要求用户先长按才能拖动视图，你可以把一个 [DragGesture](draggesture.md) 串接在 [LongPressGesture](longpressgesture.md) 之后。

#### 为顺序手势的状态建模

为了更容易跟踪复杂的状态，使用一个枚举来捕获配置视图所需的全部状态。在下面的示例中，有三个重要的状态：无交互（`inactive`）、长按进行中（`pressing`）和拖动中（`dragging`）。

```swift
struct DraggableCircle: View {

    enum DragState {
        case inactive
        case pressing
        case dragging(translation: CGSize)
        
        var translation: CGSize {
            switch self {
            case .inactive, .pressing:
                return .zero
            case .dragging(let translation):
                return translation
            }
        }
        
        var isActive: Bool {
            switch self {
            case .inactive:
                return false
            case .pressing, .dragging:
                return true
            }
        }
        
        var isDragging: Bool {
            switch self {
            case .inactive, .pressing:
                return false
            case .dragging:
                return true
            }
        }
    }
    
    @GestureState private var dragState = DragState.inactive
    @State private var viewState = CGSize.zero
```

#### 创建手势并更新 UI 状态

当你串接两个手势时，回调会捕获两个手势的状态。在更新回调中，新的 `value` 使用一个枚举来表示各种可能手势状态的组合。下面的代码把底层的手势状态转换为上文定义的高层 `DragState` 枚举。

```swift
var body: some View {
        let minimumLongPressDuration = 0.5
        let longPressDrag = LongPressGesture(minimumDuration: minimumLongPressDuration)
            .sequenced(before: DragGesture())
            .updating($dragState) { value, state, transaction in
                switch value {
                // Long press begins.
                case .first(true):
                    state = .pressing
                // Long press confirmed, dragging may begin.
                case .second(true, let drag):
                    state = .dragging(translation: drag?.translation ?? .zero)
                // Dragging ended or the long press cancelled.
                default:
                    state = .inactive
                }
            }
            .onEnded { value in
                guard case .second(true, let drag?) = value else { return }
                self.viewState.width += drag.translation.width
                self.viewState.height += drag.translation.height
            }
```

当用户开始按压视图时，拖动状态变为 `pressing`，一个阴影会在形状下方生成动画。当用户完成长按、拖动状态变为 `dragging` 后，形状周围会出现一个边框，表示用户可以开始移动该视图。

```swift
        return Circle()
            .fill(Color.blue)
            .overlay(dragState.isDragging ? Circle().stroke(Color.white, lineWidth: 2) : nil)
            .frame(width: 100, height: 100, alignment: .center)
            .offset(
                x: viewState.width + dragState.translation.width,
                y: viewState.height + dragState.translation.height
            )
            .animation(nil)
            .shadow(radius: dragState.isActive ? 8 : 0)
            .animation(.linear(duration: minimumLongPressDuration))
            .gesture(longPressDrag)
    }
}
```

## 另请参阅

### 组合手势

- [simultaneousGesture(_:including:)](<view/simultaneousgesture(__including_).md>) — 将一个手势附加到视图上，与视图定义的手势同时处理。
- [simultaneousGesture(_:isEnabled:)](<view/simultaneousgesture(__isenabled_).md>) — 将一个手势附加到视图上，与视图定义的手势同时处理。
- [simultaneousGesture(_:name:isEnabled:)](<view/simultaneousgesture(__name_isenabled_).md>) — 将一个手势附加到视图上，与视图定义的手势同时处理。
- [SequenceGesture](sequencegesture.md) — 一个由两个手势按顺序组成的手势。
- [SimultaneousGesture](simultaneousgesture.md) — 一个包含两个可同时发生、且互不先后顺序的手势的手势。
- [ExclusiveGesture](exclusivegesture.md) — 一个由两个手势组成、但只有一个能成功的手势。
