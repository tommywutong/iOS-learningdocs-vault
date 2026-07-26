---
title: View fundamentals
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-fundamentals
source_url: 'https://developer.apple.com/documentation/swiftui/view-fundamentals'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-fundamentals.json'
content_hash: 'sha256:36400a6bdb8e2e3a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# View fundamentals

<sub>API Collection</sub>

Define the visual elements of your app using a hierarchy of views.

## Overview

Views are the building blocks that you use to declare your app’s user interface. Each view contains a description of what to display for a given state. Every bit of your app that’s visible to the user derives from the description in a view, and any type that conforms to the [View](view.md) protocol can act as a view in your app.

![](../../../attachments/61676615099d97b5303fa180a5e1b8d1/view-fundamentals-hero@2x.png)

Compose a custom view by combining built-in views that SwiftUI provides with other custom views that you create in your view’s [body](view/body-8kl5o.md) computed property. Configure views using the view modifiers that SwiftUI provides, or by defining your own view modifiers using the [ViewModifier](viewmodifier.md) protocol and the [modifier(_:)](<view/modifier(__).md>) method.

## Topics

### Creating a view

- [Declaring a custom view](declaring-a-custom-view.md) — Define views and assemble them into a view hierarchy.
- [Wishlist: Planning travel in a SwiftUI app](wishlist-planning-travel-in-a-swiftui-app.md) — Build a travel planning app that organizes trips into collections and tracks activity completion.
- [View](view.md) — A type that represents part of your app’s user interface and provides modifiers that you use to configure views.
- [ContentBuilder](contentbuilder.md) — A custom parameter attribute that constructs views and other content types from closures.
- [ViewBuilder](viewbuilder.md) — A custom parameter attribute that constructs views from closures.

### Modifying a view

- [Configuring views](configuring-views.md) — Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md) — Bundle view modifiers that you regularly reuse into a custom view modifier.
- [modifier(_:)](<view/modifier(__).md>) — Applies a modifier to a view and returns a new view.
- [ViewModifier](viewmodifier.md) — A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [EmptyModifier](emptymodifier.md) — An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [ModifiedContent](modifiedcontent.md) — A value with a modifier applied to it.
- [EnvironmentalModifier](environmentalmodifier.md) — A modifier that must resolve to a concrete modifier in an environment before use.
- [ManipulableModifier](manipulablemodifier.md)
- [ManipulableResponderModifier](manipulablerespondermodifier.md)
- [ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
- [ManipulationGeometryModifier](manipulationgeometrymodifier.md)
- [ManipulationGestureModifier](manipulationgesturemodifier.md)
- [ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
- [Manipulable](manipulable.md) — A namespace for various manipulable related types.

### Responding to view life cycle updates

- [onAppear(perform:)](<view/onappear(perform_).md>) — Adds an action to perform before this view appears.
- [onDisappear(perform:)](<view/ondisappear(perform_).md>) — Adds an action to perform after this view disappears.

### Assigning tasks

- [task(id:name:executorPreference:priority:file:line:_:)](<view/task(id_name_executorpreference_priority_file_line___).md>) — Adds a task to perform before this view appears or when a specified value changes.
- [task(id:name:priority:file:line:_:)](<view/task(id_name_priority_file_line___).md>) — Adds a task to perform before this view appears or when a specified value changes.
- [task(name:executorPreference:priority:file:line:action:)](<view/task(name_executorpreference_priority_file_line_action_).md>) — Adds an asynchronous task to perform before this view appears.
- [task(name:priority:file:line:_:)](<view/task(name_priority_file_line___).md>) — Adds an asynchronous task to perform before this view appears.

### Managing the view hierarchy

- [id(_:)](<view/id(__).md>) — Binds a view’s identity to the given proxy value.
- [tag(_:includeOptional:)](<view/tag(__includeoptional_).md>) — Sets the unique tag value of this view.
- [equatable()](<view/equatable().md>) — Prevents the view from updating its child view when its new value is the same as its old value.

### Supporting content types

- [EmptyContent](emptycontent.md) — Content which contains nothing.
- [TupleContent](tuplecontent.md) — Content created from a tuple of content to be treated as siblings.

### Supporting view types

- [AnyView](anyview.md) — A type-erased view.
- [EmptyView](emptyview.md) — A view that doesn’t contain any content.
- [EquatableView](equatableview.md) — A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [SubscriptionView](subscriptionview.md) — A view that subscribes to a publisher with an action.
- [TupleView](tupleview.md) — A View created from a swift tuple of View values.

## See Also

### Views

- [View configuration](view-configuration.md) — Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md) — Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md) — Create smooth visual updates in response to state changes.
- [Text input and output](text-input-and-output.md) — Display formatted text and get text input from the user.
- [Images](images.md) — Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md) — Display values and get user selections.
- [Menus and commands](menus-and-commands.md) — Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md) — Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md) — Enhance your views with graphical effects and customized drawings.
