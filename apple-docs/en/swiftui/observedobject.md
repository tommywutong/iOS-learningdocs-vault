---
title: ObservedObject
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/observedobject
source_url: 'https://developer.apple.com/documentation/swiftui/observedobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/observedobject.json'
content_hash: 'sha256:50d4ef182183ec38'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ObservedObject

<sub>Structure</sub>

A property wrapper type that subscribes to an observable object and invalidates a view whenever the observable object changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @propertyWrapper @preconcurrency @frozen struct ObservedObject<ObjectType> where ObjectType : ObservableObject
```

## Overview

Add the `@ObservedObject` attribute to a parameter of a SwiftUI [View](view.md) when the input is an [ObservableObject](../combine/observableobject.md) and you want the view to update when the object’s published properties change. You typically do this to pass a [StateObject](stateobject.md) into a subview.

The following example defines a data model as an observable object, instantiates the model in a view as a state object, and then passes the instance to a subview as an observed object:

```swift
class DataModel: ObservableObject {
    @Published var name = "Some Name"
    @Published var isEnabled = false
}

struct MyView: View {
    @StateObject private var model = DataModel()

    var body: some View {
        Text(model.name)
        MySubView(model: model)
    }
}

struct MySubView: View {
    @ObservedObject var model: DataModel

    var body: some View {
        Toggle("Enabled", isOn: $model.isEnabled)
    }
}
```

When any published property of the observable object changes, SwiftUI updates any view that depends on the object. Subviews can also make updates to the model properties, like the [Toggle](toggle.md) in the above example, that propagate to other observers throughout the view hierarchy.

Don’t specify a default or initial value for the observed object. Use the attribute only for a property that acts as an input for a view, as in the above example.

> [!note] Note
> Don’t wrap objects conforming to the [Observable](../observation/observable.md) protocol with `@ObservedObject`. SwiftUI automatically tracks dependencies to `Observable` objects used within body and updates dependent views when their data changes. Attempting to wrap an `Observable` object with `@ObservedObject` may cause a compiler error, because it requires that its wrapped object to conform to the [ObservableObject](../combine/observableobject.md) protocol.
>
> If the view needs a binding to a property of an `Observable` object in its body, wrap the object with the [Bindable](bindable.md) property wrapper instead; for example, `@Bindable var model: DataModel`. For more information, see [Managing model data in your app](managing-model-data-in-your-app.md).

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an observed object

- [init(wrappedValue:)](<observedobject/init(wrappedvalue_).md>) — Creates an observed object with an initial wrapped value.
- [init(initialValue:)](<observedobject/init(initialvalue_).md>) — Creates an observed object with an initial value.

### Getting the value

- [wrappedValue](observedobject/wrappedvalue.md) — The underlying value that the observed object references.
- [projectedValue](observedobject/projectedvalue.md) — A projection of the observed object that creates bindings to its properties.
- [Wrapper](observedobject/wrapper.md) — A wrapper of the underlying observable object that can create bindings to its properties.

## See Also

### Creating model data

- [Managing model data in your app](managing-model-data-in-your-app.md) — Create connections between your app’s data model and views.
- [Migrating from the Observable Object protocol to the Observable macro](migrating-from-the-observable-object-protocol-to-the-observable-macro.md) — Update your existing app to leverage the benefits of Observation in Swift.
- [Observable()](<../observation/observable().md>) — Defines and implements conformance of the Observable protocol.
- [Monitoring data changes in your app](monitoring-model-data-changes-in-your-app.md) — Show changes to data in your app’s user interface by using observable objects.
- [StateObject](stateobject.md) — A property wrapper type that instantiates an observable object.
- [ObservableObject](../combine/observableobject.md) — A type of object with a publisher that emits before the object has changed.
