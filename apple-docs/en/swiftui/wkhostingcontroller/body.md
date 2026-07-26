---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wkhostingcontroller/body
source_url: 'https://developer.apple.com/documentation/swiftui/wkhostingcontroller/body'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkhostingcontroller/body.json'
content_hash: 'sha256:26d1f0e0e3500169'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKHostingController](../wkhostingcontroller.md)

# body

<sub>Instance Property</sub>

The root view of the view hierarchy to display for your interface controller.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency var body: Body { get }
```

## Discussion

Override this property and return the root view of your SwiftUI view hierarchy from your implementation. If you don’t override this property, accessing the default implementation triggers an exception.
