---
title: 'makeWKInterfaceObject(context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/wkinterfaceobjectrepresentable/makewkinterfaceobject(context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/makewkinterfaceobject(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkinterfaceobjectrepresentable/makewkinterfaceobject%28context%3A%29.json'
content_hash: 'sha256:024ad26527190aae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKInterfaceObjectRepresentable](../wkinterfaceobjectrepresentable.md)

# makeWKInterfaceObject(context:)

<sub>Instance Method</sub>

Creates a WatchKit interface object and configures its initial state.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency func makeWKInterfaceObject(context: Self.Context) -> Self.WKInterfaceObjectType
```

## Parameters

- `context` — A context structure containing information about the current state of the system.

## Return Value

Your interface object configured with the provided information.

## Discussion

You must implement this method and use it to create your interface object. Configure the object using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your interface object for the first time. For all subsequent updates, the system calls the [updateWKInterfaceObject(_:context:)](<updatewkinterfaceobject(__context_).md>) method.

## See Also

### Creating and updating the interface object

- [updateWKInterfaceObject(_:context:)](<updatewkinterfaceobject(__context_).md>) — Updates the presented WatchKit interface object (and its coordinator) to the latest configuration.
- [Context](context.md)
