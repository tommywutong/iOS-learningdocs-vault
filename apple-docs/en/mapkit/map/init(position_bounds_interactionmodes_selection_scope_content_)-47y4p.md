---
title: 'init(position:bounds:interactionModes:selection:scope:content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/map/init(position:bounds:interactionmodes:selection:scope:content:)-47y4p'
source_url: 'https://developer.apple.com/documentation/mapkit/map/init(position:bounds:interactionmodes:selection:scope:content:)-47y4p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/map/init%28position%3Abounds%3Ainteractionmodes%3Aselection%3Ascope%3Acontent%3A%29-47y4p.json'
content_hash: 'sha256:06f93e99a302d55d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Map](../map.md)

# init(position:bounds:interactionModes:selection:scope:content:)

<sub>Initializer</sub>

Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds? = nil, interactionModes: MapInteractionModes = .all, selection: Binding<MapFeature?>, scope: Namespace.ID? = nil, @MapContentBuilder content: () -> C) where Content == MapContentView<MapFeature, C>, C : MapContent
```

## Parameters

- `position` — The initial [MapCameraPosition](../mapcameraposition.md).

- `bounds` — The [MapCameraBounds](../mapcamerabounds.md) that define the camera’s view of the map.

- `interactionModes` — The [MapInteractionModes](../mapinteractionmodes.md) that describe ways a person can interact with the map.

- `selection` — A binding to a [MapFeature](../mapfeature.md) that represents a person’s selection.

- `scope` — The map’s [Namespace.ID](../../swiftui/namespace/id.md).

- `content` — A [MapContent](../mapcontent.md) content builder that supplies the map’s content.

## See Also

### Creating a map

- [init(bounds:interactionModes:scope:)](<init(bounds_interactionmodes_scope_).md>) — Creates a new, empty map with the bounds, interaction modes, and scope you provide.
- [init(bounds:interactionModes:scope:content:)](<init(bounds_interactionmodes_scope_content_).md>) — Creates a new map with the bounds, interaction modes, scope, and content you provide.
- [init(bounds:interactionModes:selection:scope:)](<init(bounds_interactionmodes_selection_scope_)-11lec.md>) — Creates a new, empty map with the bounds, interaction modes, a binding to a map feature, and scope you provide.
- [init(bounds:interactionModes:selection:scope:)](<init(bounds_interactionmodes_selection_scope_)-236di.md>) — Creates a new, empty map with the bounds, interaction modes, the selected map feature, and scope you provide.
- [init(bounds:interactionModes:selection:scope:content:)](<init(bounds_interactionmodes_selection_scope_content_)-28wns.md>) — Creates a new map with the bounds, interaction modes, selected map feature, scope, and map content you provide.
- [init(bounds:interactionModes:selection:scope:content:)](<init(bounds_interactionmodes_selection_scope_content_)-2tdbr.md>) — Creates a new map with the bounds, interaction modes, selected value, scope, and map content you provide.
- [init(initialPosition:bounds:interactionModes:scope:)](<init(initialposition_bounds_interactionmodes_scope_).md>) — Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init(initialPosition:bounds:interactionModes:scope:content:)](<init(initialposition_bounds_interactionmodes_scope_content_).md>) — Creates a new map with the initial camera position, bounds, interaction modes, scope, and map content you provide.
- [init(initialPosition:bounds:interactionModes:selection:scope:)](<init(initialposition_bounds_interactionmodes_selection_scope_).md>) — Creates a new, empty map with the initial camera position, bounds, interaction modes, selected map feature, and scope you provide.
- [init(initialPosition:bounds:interactionModes:selection:scope:content:)](<init(initialposition_bounds_interactionmodes_selection_scope_content_)-9feos.md>) — Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init(initialPosition:bounds:interactionModes:selection:scope:content:)](<init(initialposition_bounds_interactionmodes_selection_scope_content_)-451vp.md>) — Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init(position:bounds:interactionModes:scope:)](<init(position_bounds_interactionmodes_scope_).md>) — Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init(position:bounds:interactionModes:scope:content:)](<init(position_bounds_interactionmodes_scope_content_).md>) — Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init(position:bounds:interactionModes:selection:scope:)](<init(position_bounds_interactionmodes_selection_scope_).md>) — Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init(position:bounds:interactionModes:selection:scope:content:)](<init(position_bounds_interactionmodes_selection_scope_content_)-9xq1q.md>) — Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.
