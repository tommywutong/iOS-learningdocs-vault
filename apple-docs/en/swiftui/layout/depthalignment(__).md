---
title: 'depthAlignment(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layout/depthalignment(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/layout/depthalignment(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/depthalignment%28_%3A%29.json'
content_hash: 'sha256:2d09c21268a5f5f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# depthAlignment(_:)

<sub>Instance Method</sub>

Sets the depth alignment for this layout.

<sub>visionOS</sub>

```swift
func depthAlignment(_ alignment: DepthAlignment) -> some Layout

```

## Parameters

- `alignment` — A [DepthAlignment](../depthalignment.md) value to use for aligning layout’s subviews

## Discussion

Use `depthAlignment(_:)` to specify a depth guide for aligning subviews of this layout.

In the example below, the button to play the robot animation is aligned to the `.front` of the `HStack`.

```swift
   let depthStack = HStackLayout().depthAlignment(.front)
   depthStack {
       RobotModel()
       Button("Play animation") {
           playRobotAnimation()
       }
       .glassBackgroundEffect()
   }
```
