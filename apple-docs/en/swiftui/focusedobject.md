---
title: FocusedObject
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusedobject
source_url: 'https://developer.apple.com/documentation/swiftui/focusedobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedobject.json'
content_hash: 'sha256:983cec58e6baa0c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FocusedObject

<sub>Structure</sub>

A property wrapper type for an observable object supplied by the focused view or one of its ancestors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @frozen @propertyWrapper @preconcurrency struct FocusedObject<ObjectType> where ObjectType : ObservableObject
```

## Overview

Focused objects invalidate the current view whenever the observable object changes. If multiple views publish a focused object using the same key, the wrapped property will reflect the object that’s closest to the focused view.

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md)

## Topics

### Creating the focused object

- [init()](<focusedobject/init().md>) — Creates a focused object.

### Getting the value

- [projectedValue](focusedobject/projectedvalue.md) — A projection of the focused object that creates bindings to its properties using dynamic member lookup.
- [wrappedValue](focusedobject/wrappedvalue.md) — The underlying value referenced by the focused object.
- [Wrapper](focusedobject/wrapper.md) — A wrapper around the underlying focused object that can create bindings to its properties using dynamic member lookup.

## See Also

### Exposing reference types to focused views

- [focusedObject(_:)](<view/focusedobject(__).md>) — Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [focusedSceneObject(_:)](<view/focusedsceneobject(__).md>) — Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
