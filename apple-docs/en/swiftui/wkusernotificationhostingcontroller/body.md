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
doc_path: /documentation/swiftui/wkusernotificationhostingcontroller/body
source_url: 'https://developer.apple.com/documentation/swiftui/wkusernotificationhostingcontroller/body'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkusernotificationhostingcontroller/body.json'
content_hash: 'sha256:e7936fa7ba9275c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKUserNotificationHostingController](../wkusernotificationhostingcontroller.md)

# body

<sub>Instance Property</sub>

The root view of the view hierarchy to display for your notification interface.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency var body: Body { get }
```

## Discussion

Override this property and return the root view of your SwiftUI view hierarchy from your implementation. If you don’t override this property, accessing the default implementation triggers an exception.
