---
title: 'animate(changes:completion:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uiviewrepresentablecontext/animate(changes:completion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewrepresentablecontext/animate(changes:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewrepresentablecontext/animate%28changes%3Acompletion%3A%29.json'
content_hash: 'sha256:624bd4c92435dd9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewRepresentableContext](../uiviewrepresentablecontext.md)

# animate(changes:completion:)

<sub>Instance Method</sub>

Animates changes using the animation in the current transaction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func animate(changes: () -> Void, completion: (() -> Void)? = nil)
```

## Parameters

- `changes` — A closure that changes animatable properties.

- `completion` — A closure to execute after the animation completes.

## Discussion

This combines doc://com.apple.documentation/documentation/UIKit/UIView/4429628-animate with the current transaction’s animation. When you start a SwiftUI animation using [withAnimation(_:_:)](<../withanimation(____).md>) and have a mutated SwiftUI state that causes the representable object to update, use this method to animate changes in the representable object using the same `Animation` timing.

```swift
struct ContentView: View {
    @State private var isCollapsed = false
    var body: some View {
        ZStack {
            MyDetailView(isCollapsed: isCollapsed)
            MyRepresentable(isCollapsed: $isCollapsed)
            Button("Collapse Content") {
                withAnimation(.bouncy) {
                    isCollapsed = true
                }
            }
        }
    }
}

struct MyRepresentable: UIViewRepresentable {
    @Binding var isCollapsed: Bool

    func updateUIView(_ uiView: UIViewType, context: Context) {
        if isCollapsed && !uiView.isCollapsed {
            context.animate {
                uiView.collapseSubview()
                uiView.layout()
            }
        }
    }
}
```
