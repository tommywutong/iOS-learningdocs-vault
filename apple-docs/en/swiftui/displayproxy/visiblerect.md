---
title: visibleRect
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/displayproxy/visiblerect
source_url: 'https://developer.apple.com/documentation/swiftui/displayproxy/visiblerect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/displayproxy/visiblerect.json'
content_hash: 'sha256:66c333bb21c88e1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DisplayProxy](../displayproxy.md)

# visibleRect

<sub>Instance Property</sub>

The portion of the display where it is safe to place windows.

<sub>macOS</sub>

```swift
let visibleRect: CGRect
```

## Discussion

On macOS, this area does not contain the space occupied by the dock and menu bar. Additionally, on Macs that include a camera housing in the bezel this rectangle does not include the bezel or visible areas to each side of the bezel.
