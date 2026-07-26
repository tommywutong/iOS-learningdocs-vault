---
title: 'onImmersionChange(initial:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onimmersionchange(initial:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onimmersionchange(initial:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onimmersionchange%28initial%3A_%3A%29.json'
content_hash: 'sha256:41d5da7060568172'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onImmersionChange(initial:_:)

<sub>Instance Method</sub>

Performs an action when the immersion state of your app changes.

<sub>visionOS</sub>

```swift
nonisolated func onImmersionChange(initial: Bool = true, _ action: @escaping (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View

```

## Parameters

- `initial` — Whether the action should be run when this view initially appears.

- `action` — A closure to run when the immersion changes.

## Discussion

Depending on the immersion style used for the Immersive Space in your app, the amount of immersion can be controlled by actions such as turning the Digital Crown. Use this modifier to define a closure that is run when the immersion state changes. The following example sets the value of a binding depending on the current amount of immersion:

```swift
struct ImmersiveView: View {
    @Binding var enableSoundEffects: Bool

    var body: some View {
        MyView()
            .onImmersionChange { _, newImmersion in
                guard let amount = newImmersion.amount else {
                    enableSoundEffects = false
                    return
                }
                // Enable some effects based on the updated
                // amount of immersion
                enableSoundEffects = amount > 0.5
            }
    }
}
```

## See Also

### Responding to immersion changes

- [ImmersionChangeContext](../immersionchangecontext.md) — A structure that represents a state of immersion of your app.
