---
title: 'animate(changes:completion:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsviewrepresentablecontext/animate(changes:completion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewrepresentablecontext/animate(changes:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewrepresentablecontext/animate%28changes%3Acompletion%3A%29.json'
content_hash: 'sha256:03a5e88418b823aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewRepresentableContext](../nsviewrepresentablecontext.md)

# animate(changes:completion:)

<sub>Instance Method</sub>

Animates changes using the animation in the current transaction.

<sub>macOS</sub>

```swift
@backDeployed(before: macOS 15.4)
@MainActor @preconcurrency func animate(changes: () -> Void, completion: (() -> Void)? = nil)
```

## Parameters

- `changes` — A closure that changes animatable properties.

- `completion` — A closure to execute after the animation completes.

## Discussion

This combines doc://com.apple.documentation/documentation/appkit/nsanimationcontext/4433144-animate with the current transaction’s animation. When you start a SwiftUI animation using [withAnimation(_:_:)](<../withanimation(____).md>) and have a mutated SwiftUI state that causes the representable object to update, use this method to animate changes in the representable object using the same `Animation` timing.

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

struct MyRepresentable: NSViewRepresentable {
    @Binding var isCollapsed: Bool

    func updateNSView(_ nsView: NSViewType, context: Context) {
        if isCollapsed && !nsView.isCollapsed {
            context.animate {
                nsView.collapseSubview()
                nsView.layoutSubtreeIfNeeded()
            }
        }
    }
}
```
