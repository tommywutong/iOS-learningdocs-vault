---
title: 'validateDrop(info:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dropdelegate/validatedrop(info:)-1hqfh'
source_url: 'https://developer.apple.com/documentation/swiftui/dropdelegate/validatedrop(info:)-1hqfh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropdelegate/validatedrop%28info%3A%29-1hqfh.json'
content_hash: 'sha256:946284c76ca49a39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropDelegate](../dropdelegate.md)

# validateDrop(info:)

<sub>Instance Method</sub>

Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func validateDrop(info: DropInfo) -> Bool
```

## Discussion

Specify the expected types when you apply the drop modifier to the view. The default implementation returns `true`.
