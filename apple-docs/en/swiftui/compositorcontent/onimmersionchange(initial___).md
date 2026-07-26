---
title: 'onImmersionChange(initial:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/compositorcontent/onimmersionchange(initial:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontent/onimmersionchange(initial:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontent/onimmersionchange%28initial%3A_%3A%29.json'
content_hash: 'sha256:704c9c06851fd239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CompositorContent](../compositorcontent.md)

# onImmersionChange(initial:_:)

<sub>Instance Method</sub>

Performs an action when the immersion state of your app changes.

<sub>macOS, visionOS</sub>

```swift
nonisolated func onImmersionChange(initial: Bool = true, _ action: @escaping (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some CompositorContent

```

## Parameters

- `initial` — Whether the action should be run when this view initially appears.

- `action` — A closure to run when the immersion changes. - **oldValue** — The value representing the old state of immersion. - **newValue** — The value representing the current state of immersion.

## Discussion

Depending on the immersion style used for the Immersive Space in your app, the amount of immersion can be controlled by actions such as turning the Digital Crown. Use this modifier to define a closure that is run when the immersion state changes.
