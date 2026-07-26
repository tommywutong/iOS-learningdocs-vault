---
title: Environment values
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environment-values
source_url: 'https://developer.apple.com/documentation/swiftui/environment-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environment-values.json'
content_hash: 'sha256:369dbacb5d7b9a41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Environment values

<sub>API Collection</sub>

Share data throughout a view hierarchy using the environment.

## Overview

Views in SwiftUI can react to configuration information that they read from the environment using an [Environment](environment.md) property wrapper.

![](../../../attachments/c55679ce6979b83be86939cf3c9b5b65/environment-values-hero@2x.png)

A view inherits its environment from its container view, subject to explicit changes from an [environment(_:_:)](<view/environment(____).md>) view modifier, or by implicit changes from one of the many modifiers that operate on environment values. As a result, you can configure a entire hierarchy of views by modifying the environment of the group’s container.

You can find many built-in environment values in the [EnvironmentValues](environmentvalues.md) structure. You can also create a custom [EnvironmentValues](environmentvalues.md) property by defining a new property in an extension to the environment values structure and applying the [Entry()](<entry().md>) macro to the variable declaration.

## Topics

### Accessing environment values

- [Environment](environment.md) — A property wrapper that reads a value from a view’s environment.
- [EnvironmentValues](environmentvalues.md) — A collection of environment values propagated through a view hierarchy.

### Creating custom environment values

- [Entry()](<entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [EnvironmentKey](environmentkey.md) — A key for accessing values in the environment.

### Modifying the environment of a view

- [environment(_:)](<view/environment(__).md>) — Places an observable object in the view’s environment.
- [environment(_:_:)](<view/environment(____).md>) — Sets the environment value of the specified key path to the given value.
- [transformEnvironment(_:transform:)](<view/transformenvironment(__transform_).md>) — Transforms the environment value of the specified key path with the given function.

### Modifying the environment of a scene

- [environment(_:)](<scene/environment(__).md>) — Places an observable object in the scene’s environment.
- [environment(_:_:)](<scene/environment(____).md>) — Sets the environment value of the specified key path to the given value.
- [transformEnvironment(_:transform:)](<scene/transformenvironment(__transform_).md>) — Transforms the environment value of the specified key path with the given function.

## See Also

### Data and storage

- [Model data](model-data.md) — Manage the data that your app uses to drive its interface.
- [Preferences](preferences.md) — Indicate configuration preferences from views to their container views.
- [Persistent storage](persistent-storage.md) — Store data for use across sessions of your app.
