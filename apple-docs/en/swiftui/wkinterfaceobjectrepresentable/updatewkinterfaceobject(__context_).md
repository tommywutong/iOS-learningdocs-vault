---
title: 'updateWKInterfaceObject(_:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/wkinterfaceobjectrepresentable/updatewkinterfaceobject(_:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentable/updatewkinterfaceobject(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkinterfaceobjectrepresentable/updatewkinterfaceobject%28_%3Acontext%3A%29.json'
content_hash: 'sha256:abe828c07073519f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKInterfaceObjectRepresentable](../wkinterfaceobjectrepresentable.md)

# updateWKInterfaceObject(_:context:)

<sub>Instance Method</sub>

Updates the presented WatchKit interface object (and its coordinator) to the latest configuration.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency func updateWKInterfaceObject(_ wkInterfaceObject: Self.WKInterfaceObjectType, context: Self.Context)
```

## Parameters

- `wkInterfaceObject` — Your custom interface object.

- `context` — A context structure containing information about the current state of the system.

## Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding interface object. Use this method to update the configuration of your object to match the new state information provided in the `context` parameter.

## See Also

### Creating and updating the interface object

- [makeWKInterfaceObject(context:)](<makewkinterfaceobject(context_).md>) — Creates a WatchKit interface object and configures its initial state.
- [Context](context.md)
