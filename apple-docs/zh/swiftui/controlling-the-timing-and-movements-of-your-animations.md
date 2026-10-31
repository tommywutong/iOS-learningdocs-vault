---
title: 控制动画的时序与移动
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlling-the-timing-and-movements-of-your-animations
source_url: 'https://developer.apple.com/documentation/swiftui/controlling-the-timing-and-movements-of-your-animations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlling-the-timing-and-movements-of-your-animations.json'
content_hash: 'sha256:c3ae0a75499474e4'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [动画](animations.md)

# 控制动画的时序与移动

<sub>示例代码</sub>

使用阶段动画器和关键帧动画器构建你可以完全掌控的复杂动画。

## 概述

SwiftUI 提供了一系列可在你的 App 中使用的实用动画。这些动画通过为视图和用户界面元素提供视觉过渡，帮助提升你 App 的用户体验。虽然这些标准动画为增强 App 的用户交互提供了极佳的方式，但有时你需要对视觉元素的时序和移动有更多的控制。[PhaseAnimator](phaseanimator.md) 和 [KeyframeAnimator](keyframeanimator.md) 可以给你这种控制。

阶段动画器让你可以把一个动画定义为一系列称为阶段的离散步骤。动画器在这些阶段之间循环，以创建视觉过渡。使用关键帧动画器时，你创建的关键帧会定义视觉过渡期间特定时刻的动画值。

## 创建简单的弹跳动画

为了更好地理解如何使用 [PhaseAnimator](phaseanimator.md) 或 [KeyframeAnimator](keyframeanimator.md) 创建动画，先从一个使用标准 SwiftUI 动画的简单示例开始。下面的代码通过把偏移量设为 `-40.0` 来向上移动一个 emoji。为了提供平滑的移动过渡，代码使用 [withAnimation(_:_:)](<withanimation(____).md>) 函数，在用户点按 emoji 后应用 [bouncy](animation/bouncy.md) 动画：

```swift
struct SimpleAnimationView: View {
    var emoji: String
    @State private var offset = 0.0

    var body: some View {
        EmojiView(emoji: emoji)
            .offset(y: offset)
            .onTapGesture {
                withAnimation(.bouncy) {
                    offset = -40.0
                }
            }
    }
}
```

这个动画只有一个离散步骤：向上移动 emoji。不过，一个动画可以包含多个步骤，例如先把 emoji 向上移动，再移回原位。例如，下面的代码先把偏移量设为 `-40.0` 向上移动 emoji，然后把偏移量设为 `0.0` 让 emoji 回到原来的位置：

```swift
struct SimpleAnimationView: View {
    var emoji: String
    @State private var offset = 0.0

    var body: some View {
        EmojiView(emoji: emoji)
            .offset(y: offset)
            .onTapGesture {
                withAnimation(.bouncy) {
                    offset = -40.0
                } completion: {
                    withAnimation {
                        offset = 0.0
                    }
                }
            }
    }
}
```

这段代码使用 [withAnimation(_:completionCriteria:_:completion:)](<withanimation(__completioncriteria___completion_).md>) 函数为视觉过渡的两个步骤添加动画。第一步发生在该函数的 `body` 闭包中，把偏移量设为 `-40.0`。第二步发生在 `completion` 闭包中，把偏移量设为 `0.0`。

[一段视频，展示一个心形 emoji 向上移动到最高点，然后返回原来的位置。](https://docs-assets.developer.apple.com/published/40a40ab47d93a0979b7449ba0a77f7ff/phase-keyframe-animation-01.mp4)

不过，`EmojiView` 实际上经历了三个步骤。第一步发生在视图第一次出现时，`EmojiView` 视图的偏移量为 `0.0`。当有人点按该视图时，偏移量变为 `-40.0`，这是第二步。当那个动画完成后，第三步把偏移量改回 `0.0`。但基于偏移量的取值（`0.0` 和 `-40.0`），只有两个离散步骤。

虽然这个实现确实能按预期工作，但使用 [PhaseAnimator](phaseanimator.md) 是把离散步骤定义为动画阶段的更便捷方式。

## 使用阶段动画器实现弹跳

[PhaseAnimator](phaseanimator.md) 会自动在一组给定的阶段之间推进，以创建动画过渡。使用 [phaseAnimator(_:content:animation:)](<view/phaseanimator(__content_animation_).md>) 修饰符为动画器提供用于更改动画值的阶段。例如，前面展示的 emoji 弹跳动画有两个阶段：向上移动和移回原位。你可以用布尔值 `true` 和 `false` 来表示这些阶段。当阶段为 `true` 时，emoji 向上移动到 `-40.0`。当阶段为 `false` 时，emoji 通过把偏移量设为 `0.0` 移回原位。

```swift
struct TwoPhaseAnimationView: View {
    var emoji: String
    
    var body: some View {
        EmojiView(emoji: emoji)
            .phaseAnimator([false, true]) { content, phase in
                content.offset(y: phase ? -40.0 : 0.0)
            }
    }
}
```

阶段动画器按照你提供给 [phaseAnimator(_:content:animation:)](<view/phaseanimator(__content_animation_).md>) 修饰符的顺序在阶段列表中循环。当视图第一次出现时，阶段动画器调用 `content` 闭包并传入第一个阶段。然后动画器以第二个阶段的值调用该闭包。动画器会继续为每个后续阶段调用 `content` 闭包。到达最后一个阶段后，动画器会以第一个阶段的值再调用一次 `content`。

这意味着在前面的代码中，当视图第一次出现时，阶段动画器以 `false` 的阶段值调用 `content`。这会把 emoji 的偏移量设为 `0.0`。随后阶段动画器以 `true` 阶段调用 `content`。这个阶段把偏移量设为 `-40.0`，使 emoji 向上移动。到达那个偏移位置后，动画器以 `false` 阶段调用 `content`。这会让 emoji 通过把偏移量设为 `0.0` 移回原位。

这个动画在视图出现时开始。要让动画基于某个事件开始，请使用 [phaseAnimator(_:trigger:content:animation:)](<view/phaseanimator(__trigger_content_animation_).md>) 修饰符，并提供一个供动画器观察变化的 `trigger` 值。当该值发生变化时，动画器就会开始动画。例如，下面的代码在每次有人点按 emoji 时递增状态变量 `likeCount`。代码把 `likeCount` 用作阶段动画器观察变化的值。现在，每当有人点按 emoji，它就会向上移动并返回原位。

```swift
struct TwoPhaseAnimationView: View {
    var emoji: String
    @State private var likeCount = 1
    
    var body: some View {
        EmojiView(emoji: emoji)
            .phaseAnimator([false, true], trigger: likeCount) { content, phase in
                content.offset(y: phase ? -40.0 : 0.0)
            }
            .onTapGesture {
                likeCount += 1
            }
    }
}
```

[一段视频，展示一个心形 emoji 向上移动到最高点，然后返回原来的位置。](https://docs-assets.developer.apple.com/published/ec64eab4da04dab0c3a7e2c28eede60b/phase-keyframe-animation-02.mp4)

到目前为止，阶段动画器使用[默认](animation/default.md)动画来移动 emoji。你可以通过为 `phaseAnimator` 修饰符提供一个动画闭包来改变这一行为。在这个闭包中，指定要为每个阶段应用的动画类型。例如，下面的代码在阶段为 `true` 时应用 [bouncy](animation/bouncy.md) 动画，否则应用[默认](animation/default.md)动画：

```swift
struct TwoPhaseAnimationView: View {
    var emoji: String
    @State private var likeCount = 1
    
    var body: some View {
        EmojiView(emoji: emoji)
            .phaseAnimator([false, true], trigger: likeCount) { content, phase in
                content.offset(y: phase ? -40.0 : 0.0)
            } animation: { phase in
                phase ? .bouncy : .default
            }
            .onTapGesture {
                likeCount += 1
            }
    }
}
```

[一段视频，展示一个心形 emoji 在向上移动之前先略微向下弹动。emoji 到达最高点后向下移动，回到原来的位置。](https://docs-assets.developer.apple.com/published/43854501d3908c17cd163953078cd131/phase-keyframe-animation-03.mp4)

## 为动画添加更多阶段

虽然这个弹跳效果已经不错，但你还可以为它增添更多趣味。例如，你可以让 emoji 在向上移动时逐渐变大，然后再缩回正常大小。为此，你需要给动画添加第三个阶段：缩放。

要定义这些阶段，创建一个列出可能阶段的自定义类型，例如：

```swift
private enum AnimationPhase: CaseIterable {
    case initial
    case move
    case scale
}
```

接下来，为了帮助简化逻辑、降低复杂度，定义一些返回要生成动画的值的计算属性。例如，为了设置移动 emoji 的垂直偏移量，创建一个基于当前阶段返回偏移量的计算属性：

```swift
private enum AnimationPhase: CaseIterable {
    case initial
    case move
    case scale
    
    var verticalOffset: Double {
        switch self {
        case .initial: 0
        case .move, .scale: -64
        }
    }
}
```

处于初始阶段时，偏移量为 `0`，即 emoji 在屏幕上的原始位置。而当阶段为 `move` 或 `scale` 时，偏移量为 `-64`。

你可以用同样的方法（创建计算属性）为缩放效果设置 emoji 的大小变化。emoji 一开始以原始大小出现，但在 `move` 和 `scale` 阶段会变大，如下所示：

```swift
private enum AnimationPhase: CaseIterable {
    case initial
    case move
    case scale
    
    var verticalOffset: Double {
        switch self {
        case .initial: 0
        case .move, .scale: -64
        }
    }
    
    var scaleEffect: Double {
        switch self {
        case .initial: 1
        case .move, .scale: 1.5
        }
    }
}
```

要为 emoji 添加动画，请将 [phaseAnimator(_:trigger:content:animation:)](<view/phaseanimator(__trigger_content_animation_).md>) 修饰符应用到 `EmojiView`。向动画器提供自定义 `AnimationPhase` 类型的全部 case。然后通过应用 [scaleEffect(_:anchor:)](<view/scaleeffect(__anchor_).md>) 和 [offset(x:y:)](<view/offset(x_y_).md>) 修饰符，根据阶段更改内容。传入这些修饰符的值来自那些计算属性，这有助于让视图代码更具可读性。

```swift
struct ThreePhaseAnimationView: View {
    var emoji: String
    @State private var likeCount = 1
    
    var body: some View {
        EmojiView(emoji: emoji)
            .phaseAnimator(AnimationPhase.allCases, trigger: likeCount) { content, phase in
                content
                    .scaleEffect(phase.scaleEffect)
                    .offset(y: phase.verticalOffset)
            } animation: { phase in
                switch phase {
                case .initial: .smooth
                case .move: .easeInOut(duration: 0.3)
                case .scale: .spring(duration: 0.3, bounce: 0.7)
                }
            }
            .onTapGesture {
                likeCount += 1
            }
    }
}
```

代码还在 `animation` 闭包中根据阶段应用了不同的动画类型，为整个动画带来了你所期待的那种活力。

[一段视频，展示一个心形 emoji 向上移动。emoji 向上移动时体积变大。emoji 到达最高点后，在恢复原始大小的同时向下移回原位。](https://docs-assets.developer.apple.com/published/54cd3f809790fd456c2b985c56821d66/phase-keyframe-animation-04.mp4)

> [!note] 注意
> 使用 Xcode 中的画布预览来帮助确定要为阶段动画应用的动画类型和值。修改代码后即可在画布预览中看到这些更改的效果。

[PhaseAnimator](phaseanimator.md) 让你可以基于离散阶段控制动画，这有助于为动画增添额外的精致感。但如果你发现自己需要对动画的时序和移动有更多控制，请使用 [KeyframeAnimator](keyframeanimator.md)。

## 使用关键帧动画器获得更多控制

你可以使用 [KeyframeAnimator](keyframeanimator.md) 定义复杂且相互协调的动画，并完全掌控时序和移动。这种动画器允许你创建在动画期间的特定时刻定义取值的关键帧。动画器使用这些值在每个动画帧之间生成插值。

阶段动画器需要你为分离的离散状态建模，关键帧动画器则不同：它会生成你所指定类型的插值。在动画进行过程中，动画器会在每一帧向你提供该类型的一个值，让你可以通过对视图应用修饰符来更新正在生成动画的视图。

你把这个类型定义为一个结构体，其中包含你想要独立生成动画的属性。例如，下面的代码定义了四个属性，分别决定 emoji 的缩放、拉伸、位置和角度：

```swift
private struct AnimationValues {
    var scale = 1.0
    var verticalStretch = 1.0
    var verticalOffset = 0.0
    var angle = Angle.zero
}
```

> [!note] 注意
> [KeyframeAnimator](keyframeanimator.md) 可以为任何符合 [Animatable](animatable.md) 协议的值生成动画。

要使用关键帧动画器创建动画，请将 [keyframeAnimator(initialValue:repeating:content:keyframes:)](<view/keyframeanimator(initialvalue_repeating_content_keyframes_).md>) 或 [keyframeAnimator(initialValue:trigger:content:keyframes:)](<view/keyframeanimator(initialvalue_trigger_content_keyframes_).md>) 修饰符应用到你想为其添加动画的视图。例如，下面的代码把第二个修饰符应用到 `EmojiView`。动画的初始值是一个新的 `AnimationValues` 实例，状态变量 `likeCount` 则是动画器观察其变化以触发动画的值，与前面的阶段动画示例中一样。

```swift
struct KeyframeAnimationView: View {
    var emoji: String
    @State private var likeCount = 1
    
    var body: some View {
        EmojiView(emoji: emoji)
            .keyframeAnimator(
                initialValue: AnimationValues(),
                trigger: likeCount
            ) { content, value in
                // ...
            } keyframes: { _ in
                // ...
            }
            .onTapGesture {
                likeCount += 1
            }
    }
}
```

要在动画期间对视图应用修饰符，请向关键帧动画器提供一个 `content` 闭包。这个闭包包含两个参数：

- **`content`** — 正在生成动画的视图。
- **`value`** — 当前的插值。

使用这些参数对 SwiftUI 正在生成动画的视图应用修饰符。例如，下面的代码使用这些参数来旋转、缩放、拉伸和移动一个 emoji：

```swift
struct KeyframeAnimationView: View {
    var emoji: String
    @State private var likeCount = 1
    
    var body: some View {
        EmojiView(emoji: emoji)
            .keyframeAnimator(
                initialValue: AnimationValues(),
                trigger: likeCount
            ) { content, value in
                content
                    .rotationEffect(value.angle)
                    .scaleEffect(value.scale)
                    .scaleEffect(y: value.verticalStretch)
                    .offset(y: value.verticalOffset)
            } keyframes: { _ in
                // ...
            }
            .onTapGesture {
                likeCount += 1
            }
    }
}
```

> [!important] 重要
> SwiftUI 会在动画的每一帧上调用关键帧动画器的 `content` 闭包，因此请避免直接在它内部执行任何开销较大的操作。

接下来，定义关键帧。关键帧让你可以为不同的属性使用不同的关键帧，从而构建复杂的动画。为了实现这一点，你需要把关键帧组织到轨道中。每条轨道控制你正在生成动画的类型的一个不同属性。在创建轨道时提供该属性的键路径，即可把属性关联到轨道。例如，下面的代码为 `scale` 属性添加了一条 [KeyframeTrack](keyframetrack.md)：

```swift
struct KeyframeAnimationView: View {
    var emoji: String
    @State private var likeCount = 1
    
    var body: some View {
        EmojiView(emoji: emoji)
            .keyframeAnimator(
                initialValue: AnimationValues(),
                trigger: likeCount
            ) { content, value in
                content
                    .rotationEffect(value.angle)
                    .scaleEffect(value.scale)
                    .scaleEffect(y: value.verticalStretch)
                    .offset(y: value.verticalOffset)
            } keyframes: { _ in
                KeyframeTrack(\.scale) {
                    // ...
                }
            }
            .onTapGesture {
                likeCount += 1
            }
    }
}
```

创建轨道时，你使用 SwiftUI 的声明式语法向轨道添加关键帧。关键帧有多种类型，例如 [CubicKeyframe](cubickeyframe.md)、[LinearKeyframe](linearkeyframe.md) 和 [SpringKeyframe](springkeyframe.md)。你可以在一条轨道内混用和搭配不同类型的关键帧。例如，下面的代码为 `scale` 属性添加了一条轨道，执行线性和弹簧动画的组合：

```swift
struct KeyframeAnimationView: View {
    var emoji: String
    @State private var likeCount = 1
    
    var body: some View {
        EmojiView(emoji: emoji)
            .keyframeAnimator(
                initialValue: AnimationValues(),
                trigger: likeCount
            ) { content, value in
                content
                    .rotationEffect(value.angle)
                    .scaleEffect(value.scale)
                    .scaleEffect(y: value.verticalStretch)
                    .offset(y: value.verticalOffset)
            } keyframes: { _ in
                KeyframeTrack(\.scale) {
                    LinearKeyframe(1.0, duration: 0.36)
                    SpringKeyframe(1.5, duration: 0.8,
                        spring: .bouncy)
                    SpringKeyframe(1.0, spring: .bouncy)
                }
            }
            .onTapGesture {
                likeCount += 1
            }
    }
}
```

每种关键帧类型都接收一个值。动画器使用这个值在帧之间生成插值，并在调用动画器的 content 闭包之前设置轨道键路径中指定的属性。例如，在上面的代码清单中，在线性关键帧期间 scale 值为 `1.0`，这使 emoji 保持原始大小。然后在第一个弹簧关键帧期间 scale 变为 `1.5`。这使 emoji 变大。最后一个弹簧关键帧把 scale 设为 `1.0`，让 emoji 恢复原始大小。

> [!note] 注意
> SwiftUI 会在一条轨道内的多个关键帧之间保留速度（即动画的速率），以实现连续运动。

在实现关键帧动画时，为每个想要生成动画的属性添加一条轨道。例如，`AnimationValues` 有四个属性：

- `scale`
- `verticalStretch`
- `verticalOffset`
- `angle`

要为全部四个属性生成动画，动画器需要四条关键帧轨道，如下面的代码所示：

```swift
struct KeyframeAnimationView: View {
    var emoji: String
    @State private var likeCount = 1
    
    var body: some View {
        EmojiView(emoji: emoji)
            .keyframeAnimator(
                initialValue: AnimationValues(),
                trigger: likeCount
            ) { content, value in
                content
                    .rotationEffect(value.angle)
                    .scaleEffect(value.scale)
                    .scaleEffect(y: value.verticalStretch)
                    .offset(y: value.verticalOffset)
            } keyframes: { _ in
                KeyframeTrack(\.scale) {
                    LinearKeyframe(1.0, duration: 0.36)
                    SpringKeyframe(1.5, duration: 0.8, spring: .bouncy)
                    SpringKeyframe(1.0, spring: .bouncy)
                }
                
                KeyframeTrack(\.verticalOffset) {
                    LinearKeyframe(0.0, duration: 0.1)
                    SpringKeyframe(20.0, duration: 0.15, spring: .bouncy)
                    SpringKeyframe(-60.0, duration: 1.0, spring: .bouncy)
                    SpringKeyframe(0.0, spring: .bouncy)
                }

                KeyframeTrack(\.verticalStretch) {
                    CubicKeyframe(1.0, duration: 0.1)
                    CubicKeyframe(0.6, duration: 0.15)
                    CubicKeyframe(1.5, duration: 0.1)
                    CubicKeyframe(1.05, duration: 0.15)
                    CubicKeyframe(1.0, duration: 0.88)
                    CubicKeyframe(0.8, duration: 0.1)
                    CubicKeyframe(1.04, duration: 0.4)
                    CubicKeyframe(1.0, duration: 0.22)
                }

                KeyframeTrack(\.angle) {
                    CubicKeyframe(.zero, duration: 0.58)
                    CubicKeyframe(.degrees(16), duration: 0.125)
                    CubicKeyframe(.degrees(-16), duration: 0.125)
                    CubicKeyframe(.degrees(16), duration: 0.125)
                    CubicKeyframe(.zero, duration: 0.125)
                }
            }
            .onTapGesture {
                likeCount += 1
            }
    }
}
```

这些关键帧轨道组合在一起，创建出一个先挤压和拉伸 emoji、再将它向上弹起的动画。emoji 向最高点移动时逐渐变大。到达最高点时，它会轻微扭动一下。随后 emoji 带着轻微的弹跳返回原位，逐渐稳定在初始位置。

[一段视频，展示一个心形 emoji 先被挤压和拉伸，然后向上弹起。emoji 向最高点移动时逐渐变大。到达最高点时，它以轻微的顺时针到逆时针旋转扭动。随后 emoji 向下移回原位，同时缩回原始大小。最后，emoji 在回到初始位置时轻微弹动了一下。](https://docs-assets.developer.apple.com/published/049c64d56826ecf9f384dfbfd0bdbce7/phase-keyframe-animation-05.mp4)

> [!note] 注意
> 与阶段动画一样，使用 Xcode 中的画布预览来帮助确定要为关键帧动画应用的动画类型和值。修改代码后即可在画布预览中看到这些更改的效果。

## 另请参阅

### 创建基于阶段的动画

- [phaseAnimator(_:content:animation:)](<view/phaseanimator(__content_animation_).md>) — 让你应用于视图的效果在一系列持续变化的阶段上生成动画。
- [phaseAnimator(_:trigger:content:animation:)](<view/phaseanimator(__trigger_content_animation_).md>) — 让你应用于视图的效果在一系列基于触发器变化的阶段上生成动画。
- [PhaseAnimator](phaseanimator.md) — 一个容器，通过在你提供的一组阶段中自动循环来为其内容生成动画，每个阶段定义动画中的一个离散步骤。

## 下载

- [PhaseAndKeyframeAnimationSample.zip](https://docs-assets.developer.apple.com/published/354a9f65c3b5/PhaseAndKeyframeAnimationSample.zip)
