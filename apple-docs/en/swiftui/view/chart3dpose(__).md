---
title: 'chart3DPose(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chart3dpose(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chart3dpose(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chart3dpose%28_%3A%29.json'
content_hash: 'sha256:3da6f91954297f6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chart3DPose(_:)

<sub>Instance Method</sub>

Associates a binding to be updated when the 3D chart’s pose is changed by an interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func chart3DPose(_ pose: Binding<Chart3DPose>) -> some View

```

## Parameters

- `pose` — The 3D chart’s current pose.

## See Also

### 3D configuration

- [chart3DCameraProjection(_:)](<chart3dcameraprojection(__).md>)
- [chart3DRenderingStyle(_:)](<chart3drenderingstyle(__).md>)
