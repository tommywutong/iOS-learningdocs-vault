---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/app/body-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/app/body-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/app/body-swift.property.json'
content_hash: 'sha256:923b7996295a7895'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [App](../app.md)

# body

<sub>Instance Property</sub>

The content and behavior of the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@SceneBuilder @MainActor @preconcurrency var body: Self.Body { get }
```

## Discussion

For any app that you create, provide a computed `body` property that defines your app’s scenes, which are instances that conform to the [Scene](../scene.md) protocol. For example, you can create a simple app with a single scene containing a single view:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            Text("Hello, world!")
        }
    }
}
```

Swift infers the app’s [Body](body-swift.associatedtype.md) associated type based on the scene provided by the `body` property.

## See Also

### Implementing an app

- [Body](body-swift.associatedtype.md) — The type of scene representing the content of the app.
