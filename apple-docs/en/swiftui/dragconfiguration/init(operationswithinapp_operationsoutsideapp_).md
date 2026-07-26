---
title: 'init(operationsWithinApp:operationsOutsideApp:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dragconfiguration/init(operationswithinapp:operationsoutsideapp:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dragconfiguration/init(operationswithinapp:operationsoutsideapp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dragconfiguration/init%28operationswithinapp%3Aoperationsoutsideapp%3A%29.json'
content_hash: 'sha256:dfa99705be0d019d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragConfiguration](../dragconfiguration.md)

# init(operationsWithinApp:operationsOutsideApp:)

<sub>Initializer</sub>

Creates a default drag configuration with operation `.copy` support for drags within the application and to other applications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(operationsWithinApp: DragConfiguration.OperationsWithinApp = .init(), operationsOutsideApp: DragConfiguration.OperationsOutsideApp = .init())
```
