---
title: 'replacing(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 2.0+（2.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/windowplacement/position/replacing(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowplacement/position/replacing(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowplacement/position/replacing%28_%3A%29.json'
content_hash: 'sha256:7ee736f0795a6f0b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [WindowPlacement](../../windowplacement.md) · [Position](../position.md)

# replacing(_:)

<sub>Type Method</sub>

Positions the window in the same spot as an existing window, hiding the old window in the process.

> [!warning] Deprecated
> Use PushWindowAction instead.

<sub>visionOS</sub>

```swift
static func replacing(_ relativeWindow: WindowProxy) -> WindowPlacement.Position
```

## Parameters

- `relativeWindow` — The existing window that the new window will replace.

## Discussion

This will position the new window in the same location as the specified existing window, and hide the old window. Closing the new window will then result in the original window being shown again.
