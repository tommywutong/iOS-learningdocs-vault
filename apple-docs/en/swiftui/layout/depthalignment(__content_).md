---
title: 'depthAlignment(_:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layout/depthalignment(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/layout/depthalignment(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/depthalignment%28_%3Acontent%3A%29.json'
content_hash: 'sha256:5eee2ce832ce9dc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# depthAlignment(_:content:)

<sub>Instance Method</sub>

Creates a layout view with the specified depth alignment.

<sub>visionOS</sub>

```swift
nonisolated func depthAlignment<Content>(_ alignment: DepthAlignment, @ContentBuilder content: () -> Content) -> some View where Content : View

```

## Parameters

- `alignment` — A [DepthAlignment](../depthalignment.md) value to use for aligning layout’s subviews

## Discussion

Use `depthAlignment(_:content:)` to specify a depth guide for aligning subviews of this layout.

In the example below, the button to play the robot animation is aligned to the `.front` of the `HStack`.

```swift
   HStackLayout().depthAlignment(.front) {
       RobotModel()
       Button("Play animation") {
           playRobotAnimation()
       }
       .glassBackgroundEffect()
   }
```
