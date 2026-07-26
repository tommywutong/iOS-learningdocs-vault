---
title: 'dismantleWKInterfaceObject(_:coordinator:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/wkinterfaceobjectrepresentable/dismantlewkinterfaceobject(_:coordinator:)'
source_url: 'https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/dismantlewkinterfaceobject(_:coordinator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkinterfaceobjectrepresentable/dismantlewkinterfaceobject%28_%3Acoordinator%3A%29.json'
content_hash: 'sha256:00567d528808e5ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKInterfaceObjectRepresentable](../wkinterfaceobjectrepresentable.md)

# dismantleWKInterfaceObject(_:coordinator:)

<sub>Type Method</sub>

Cleans up the presented WatchKit interface object (and its coordinator) in anticipation of their removal.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency static func dismantleWKInterfaceObject(_ wkInterfaceObject: Self.WKInterfaceObjectType, coordinator: Self.Coordinator)
```

## Parameters

- `wkInterfaceObject` — Your custom interface object.

- `coordinator` — The custom coordinator instance you use to communicate changes back to SwiftUI. If you do not use a custom coordinator, the system provides a default instance.

## Discussion

Use this method to perform additional clean-up work related to your custom interface object. For example, you might use this method to remove observers or update other parts of your SwiftUI interface.

## Default Implementations

### WKInterfaceObjectRepresentable Implementations

- [dismantleWKInterfaceObject(_:coordinator:)](<dismantlewkinterfaceobject(__coordinator_)-qd0y.md>) — Cleans up the presented interface object (and coordinator) in anticipation of their removal.
