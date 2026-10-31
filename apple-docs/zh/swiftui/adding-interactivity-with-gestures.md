---
title: 使用手势添加交互性
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/adding-interactivity-with-gestures
source_url: 'https://developer.apple.com/documentation/swiftui/adding-interactivity-with-gestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/adding-interactivity-with-gestures.json'
content_hash: 'sha256:c1877cd1130c9e8b'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [手势](gestures.md)

# 使用手势添加交互性

<sub>文章</sub>

使用手势修饰符为你的 App 添加交互性。

## 概述

手势修饰符负责处理用户输入事件（例如触摸）所需的全部逻辑，并在这些事件匹配已知的手势模式（例如长按或旋转）时进行识别。识别到某个模式时，SwiftUI 会运行一个回调，你可以用它来更新视图的状态或执行某个操作。

### 向视图添加手势修饰符

你添加的每个手势都应用于视图层级结构中的特定视图。要在特定视图上识别手势事件，先创建并配置手势，然后使用 [gesture(_:including:)](<view/gesture(__including_).md>) 修饰符：

```swift
struct ShapeTapView: View {
    var body: some View {
        let tap = TapGesture()
            .onEnded { _ in
                print("View tapped!")
            }
        
        return Circle()
            .fill(Color.blue)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(tap)
    }
}
```

### 响应手势回调

根据你添加到手势修饰符上的回调，只要手势的状态发生变化，SwiftUI 就会向你的代码报告。手势修饰符提供三种接收更新的方式：[updating(_:body:)](<gesture/updating(__body_).md>)、[onChanged(_:)](<gesture/onchanged(__).md>) 和 [onEnded(_:)](<gesture/onended(__).md>)。

#### 更新瞬时 UI 状态

要在手势变化时更新视图，请向你的视图添加一个 [GestureState](gesturestate.md) 属性，并在 [updating(_:body:)](<gesture/updating(__body_).md>) 回调中更新它。SwiftUI 会在识别到手势的那一刻以及手势的值每次变化时调用 updating 回调。例如，当放大手势开始时 SwiftUI 会立即调用 updating 回调，并在放大值每次变化时再次调用。当用户结束或取消手势时，SwiftUI 不会调用 updating 回调。相反，手势状态属性会自动把其状态重置回初始值。

例如，要制作一个在用户执行长按期间改变颜色的视图，请添加一个手势状态属性并在 updating 回调中更新它。

```swift
struct CounterView: View {
    @GestureState private var isDetectingLongPress = false
    
    var body: some View {
        let press = LongPressGesture(minimumDuration: 1)
            .updating($isDetectingLongPress) { currentState, gestureState, transaction in
                gestureState = currentState
            }
        
        return Circle()
            .fill(isDetectingLongPress ? Color.yellow : Color.green)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(press)
    }
}
```

#### 在手势期间更新持久状态

要跟踪某个手势的更改，并且这些更改在手势结束后不应重置，请使用 [onChanged(_:)](<gesture/onchanged(__).md>) 回调。例如，要统计你的 App 识别到长按的次数，请添加一个 [onChanged(_:)](<gesture/onchanged(__).md>) 回调并递增计数器。

```swift
struct CounterView: View {
    @GestureState private var isDetectingLongPress = false
    @State private var totalNumberOfTaps = 0
    
    var body: some View {
        let press = LongPressGesture(minimumDuration: 1)
            .updating($isDetectingLongPress) { currentState, gestureState, transaction in
                gestureState = currentState
            }.onChanged { _ in
                self.totalNumberOfTaps += 1
            }
        
        return VStack {
            Text("\(totalNumberOfTaps)")
                .font(.largeTitle)
            
            Circle()
                .fill(isDetectingLongPress ? Color.yellow : Color.green)
                .frame(width: 100, height: 100, alignment: .center)
                .gesture(press)
        }
    }
}
```

#### 在手势结束时更新持久状态

要识别手势何时成功完成并获取手势的最终值，请使用 [onEnded(_:)](<gesture/onended(__).md>) 函数在回调中更新 App 的状态。SwiftUI 只在手势成功时才调用 [onEnded(_:)](<gesture/onended(__).md>) 回调。例如，在 [LongPressGesture](longpressgesture.md) 期间，如果用户在 [minimumDuration](longpressgesture/minimumduration.md) 秒尚未流逝前就停止触摸视图，或者手指移动超过 [maximumDistance](longpressgesture/maximumdistance.md) 点，SwiftUI 就不会调用 [onEnded(_:)](<gesture/onended(__).md>) 回调。

例如，要在用户完成一次长按后停止统计长按尝试，请添加一个 [onEnded(_:)](<gesture/onended(__).md>) 回调，并有条件地应用该手势修饰符。

```swift
struct CounterView: View {
    @GestureState private var isDetectingLongPress = false
    @State private var totalNumberOfTaps = 0
    @State private var doneCounting = false
    
    var body: some View {
        let press = LongPressGesture(minimumDuration: 1)
            .updating($isDetectingLongPress) { currentState, gestureState, transaction in
                gestureState = currentState
            }.onChanged { _ in
                self.totalNumberOfTaps += 1
            }
            .onEnded { _ in
                self.doneCounting = true
            }
        
        return VStack {
            Text("\(totalNumberOfTaps)")
                .font(.largeTitle)
            
            Circle()
                .fill(doneCounting ? Color.red : isDetectingLongPress ? Color.yellow : Color.green)
                .frame(width: 100, height: 100, alignment: .center)
                .gesture(doneCounting ? nil : press)
        }
    }
}
```
