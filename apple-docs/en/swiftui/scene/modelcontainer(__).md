---
title: 'modelContainer(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/modelcontainer(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/modelcontainer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/modelcontainer%28_%3A%29.json'
content_hash: 'sha256:9fbb27311c09b9f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# modelContainer(_:)

<sub>Instance Method</sub>

Sets the model container and associated model context in this scene’s environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func modelContainer(_ container: ModelContainer) -> some Scene

```

## Parameters

- `container` — The model container to use for this scene.

## Discussion

In this example, `RecipesApp` sets a shared model container to use for all of its windows:

```swift
@main
struct RecipesApp: App {
    @State private var container = ModelContainer(...)

    var body: some Scene {
        WindowGroup {
            RecipesList()
        }
        .modelContainer(container)
    }
}
```

The environment’s [modelContext](../environmentvalues/modelcontext.md) property will be assigned a new context associated with this container. All implicit model context operations in this scene, such as `Query` properties, will use the environment’s context.

## See Also

### Configuring a data model

- [modelContext(_:)](<modelcontext(__).md>) — Sets the model context in this scene’s environment.
- [modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)](<modelcontainer(for_inmemory_isautosaveenabled_isundoenabled_onsetup_).md>) — Sets the model container in this scene for storing the provided model type, creating a new container if necessary, and also sets a model context for that container in this scene’s environment.
