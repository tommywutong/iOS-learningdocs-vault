---
title: safeAreaInsets
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/displayproxy/safeareainsets
source_url: 'https://developer.apple.com/documentation/swiftui/displayproxy/safeareainsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/displayproxy/safeareainsets.json'
content_hash: 'sha256:28011c72fceb1ae1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DisplayProxy](../displayproxy.md)

# safeAreaInsets

<sub>Instance Property</sub>

The safe area inset of this display.

<sub>macOS</sub>

```swift
let safeAreaInsets: EdgeInsets
```

## Discussion

On macOS, the safe area contains space occupied by the dock and menu bar, and is dependent on the current user settings. Additionally, on Macs that include a camera housing in the bezel, the safe area contains the vertical space occupied by the bezel.
