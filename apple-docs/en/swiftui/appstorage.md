---
title: AppStorage
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/appstorage
source_url: 'https://developer.apple.com/documentation/swiftui/appstorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/appstorage.json'
content_hash: 'sha256:e3584daa4792747c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AppStorage

<sub>Structure</sub>

A property wrapper type that reflects a value from `UserDefaults` and invalidates a view on a change in value in that user default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen @propertyWrapper struct AppStorage<Value>
```

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Storing a value

- [init(wrappedValue:_:store:)](<appstorage/init(wrappedvalue___store_).md>) — Creates a property that can save and restore tab sidebar customizations.
- [init(_:store:)](<appstorage/init(__store_).md>) — Creates a property that can read and write an Optional boolean user default.

### Getting the value

- [wrappedValue](appstorage/wrappedvalue.md)
- [projectedValue](appstorage/projectedvalue.md)

## See Also

### Saving state across app launches

- [Restoring your app’s state with SwiftUI](restoring-your-app-s-state-with-swiftui.md) — Provide app continuity for users by preserving their current activities.
- [defaultAppStorage(_:)](<view/defaultappstorage(__).md>) — The default store used by `AppStorage` contained within the view.
- [SceneStorage](scenestorage.md) — A property wrapper type that reads and writes to persisted, per-scene storage.
