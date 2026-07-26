---
title: EnvironmentObject
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentobject
source_url: 'https://developer.apple.com/documentation/swiftui/environmentobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentobject.json'
content_hash: 'sha256:f382f2d1d7ad70ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EnvironmentObject

<sub>Structure</sub>

A property wrapper type for an observable object that a parent or ancestor view supplies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @frozen @propertyWrapper @preconcurrency struct EnvironmentObject<ObjectType> where ObjectType : ObservableObject
```

## Overview

An environment object invalidates the current view whenever the observable object that conforms to [ObservableObject](../combine/observableobject.md) changes. If you declare a property as an environment object, be sure to set a corresponding model object on an ancestor view by calling its [environmentObject(_:)](<view/environmentobject(__).md>) modifier.

> [!note] Note
> If your observable object conforms to the [Observable](../observation/observable.md) protocol, use [Environment](environment.md) instead of `EnvironmentObject` and set the model object in an ancestor view by calling its [environment(_:)](<view/environment(__).md>) or [environment(_:_:)](<view/environment(____).md>) modifiers.

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an environment object

- [init()](<environmentobject/init().md>) — Creates an environment object.

### Getting the value

- [wrappedValue](environmentobject/wrappedvalue.md) — The underlying value referenced by the environment object.
- [projectedValue](environmentobject/projectedvalue.md) — A projection of the environment object that creates bindings to its properties using dynamic member lookup.
- [Wrapper](environmentobject/wrapper.md) — A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.

## See Also

### Distributing model data throughout your app

- [environmentObject(_:)](<view/environmentobject(__).md>) — Supplies an observable object to a view’s hierarchy.
- [environmentObject(_:)](<scene/environmentobject(__).md>) — Supplies an `ObservableObject` to a view subhierarchy.
