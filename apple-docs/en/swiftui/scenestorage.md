---
title: SceneStorage
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenestorage
source_url: 'https://developer.apple.com/documentation/swiftui/scenestorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenestorage.json'
content_hash: 'sha256:b9f0160564e5c29c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SceneStorage

<sub>Structure</sub>

A property wrapper type that reads and writes to persisted, per-scene storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen @propertyWrapper struct SceneStorage<Value>
```

## Overview

You use `SceneStorage` when you need automatic state restoration of the value.  `SceneStorage` works very similar to `State`, except its initial value is restored by the system if it was previously saved, and the value is shared with other `SceneStorage` variables in the same scene.

The system manages the saving and restoring of `SceneStorage` on your behalf. The underlying data that backs `SceneStorage` is not available to you, so you must access it via the `SceneStorage` property wrapper. The system makes no guarantees as to when and how often the data will be persisted.

Each `Scene` has its own notion of `SceneStorage`, so data is not shared between scenes.

Ensure that the data you use with `SceneStorage` is lightweight. Data of a large size, such as model data, should not be stored in `SceneStorage`, as poor performance may result.

If the `Scene` is explicitly destroyed (e.g. the switcher snapshot is destroyed on iPadOS or the window is closed on macOS), the data is also destroyed. Do not use `SceneStorage` with sensitive data.

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Storing a value

- [init(wrappedValue:_:)](<scenestorage/init(wrappedvalue___).md>) — Creates a property that can save and restore an integer, transforming it to a `RawRepresentable` data type.
- [init(_:)](<scenestorage/init(__).md>) — Creates a property that can save and restore an Optional boolean.

### Getting the value

- [wrappedValue](scenestorage/wrappedvalue.md) — The underlying value referenced by the state variable.
- [projectedValue](scenestorage/projectedvalue.md) — A binding to the state value.

### Initializers

- [init(wrappedValue:_:store:)](<scenestorage/init(wrappedvalue___store_).md>) — Creates a property that can save and restore tab sidebar customizations.

## See Also

### Saving state across app launches

- [Restoring your app’s state with SwiftUI](restoring-your-app-s-state-with-swiftui.md) — Provide app continuity for users by preserving their current activities.
- [defaultAppStorage(_:)](<view/defaultappstorage(__).md>) — The default store used by `AppStorage` contained within the view.
- [AppStorage](appstorage.md) — A property wrapper type that reflects a value from `UserDefaults` and invalidates a view on a change in value in that user default.
