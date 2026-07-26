---
title: State modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-state
source_url: 'https://developer.apple.com/documentation/swiftui/view-state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-state.json'
content_hash: 'sha256:6365e8efde84ca72'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# State modifiers

<sub>API Collection</sub>

Access storage and provide child views with configuration data.

## Overview

SwiftUI provides tools for managing data in your app. For example, you can store values and objects in an environment that’s shared among the views in a view hierarchy. Any view that shares the environment — typically all the descendant views of the view that stores the item — can then access the stored item.

For more information about the types that SwiftUI provides to help manage data in your app, see [Model data](model-data.md).

## Topics

### Identity

- [tag(_:includeOptional:)](<view/tag(__includeoptional_).md>) — Sets the unique tag value of this view.
- [id(_:)](<view/id(__).md>) — Binds a view’s identity to the given proxy value.
- [equatable()](<view/equatable().md>) — Prevents the view from updating its child view when its new value is the same as its old value.

### Environment values

- [environment(_:)](<view/environment(__).md>) — Places an observable object in the view’s environment.
- [environment(_:_:)](<view/environment(____).md>) — Sets the environment value of the specified key path to the given value.
- [environmentObject(_:)](<view/environmentobject(__).md>) — Supplies an observable object to a view’s hierarchy.
- [transformEnvironment(_:transform:)](<view/transformenvironment(__transform_).md>) — Transforms the environment value of the specified key path with the given function.

### Preferences

- [preference(key:value:)](<view/preference(key_value_).md>) — Sets a value for the given preference.
- [transformPreference(_:_:)](<view/transformpreference(____).md>) — Applies a transformation to a preference value.
- [anchorPreference(key:value:transform:)](<view/anchorpreference(key_value_transform_).md>) — Sets a value for the specified preference key, the value is a function of a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [transformAnchorPreference(key:value:transform:)](<view/transformanchorpreference(key_value_transform_).md>) — Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [onPreferenceChange(_:perform:)](<view/onpreferencechange(__perform_).md>) — Adds an action to perform when the specified preference key’s value changes.
- [backgroundPreferenceValue(_:_:)](<view/backgroundpreferencevalue(____).md>) — Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [backgroundPreferenceValue(_:alignment:_:)](<view/backgroundpreferencevalue(__alignment___).md>) — Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [overlayPreferenceValue(_:_:)](<view/overlaypreferencevalue(____).md>) — Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [overlayPreferenceValue(_:alignment:_:)](<view/overlaypreferencevalue(__alignment___).md>) — Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.

### Default storage

- [defaultAppStorage(_:)](<view/defaultappstorage(__).md>) — The default store used by `AppStorage` contained within the view.

### Configuring a model

- [modelContext(_:)](<view/modelcontext(__).md>) — Sets the model context in this view’s environment.
- [modelContainer(_:)](<view/modelcontainer(__).md>) — Sets the model container and associated model context in this view’s environment.
- [modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)](<view/modelcontainer(for_inmemory_isautosaveenabled_isundoenabled_onsetup_).md>) — Sets the model container in this view for storing the provided model type, creating a new container if necessary, and also sets a model context for that container in this view’s environment.

## See Also

### Providing interactivity

- [Input and event modifiers](view-input-and-events.md) — Supply actions for a view to perform in response to user input and system events.
- [Search modifiers](view-search.md) — Enable people to search for content in your app.
- [Presentation modifiers](view-presentation.md) — Define additional views for the view to present under specified conditions.
