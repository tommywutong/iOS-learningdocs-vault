---
title: MapInteractionModes
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapinteractionmodes
source_url: 'https://developer.apple.com/documentation/mapkit/mapinteractionmodes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapinteractionmodes.json'
content_hash: 'sha256:6451260136be8dbd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapInteractionModes

<sub>Structure</sub>

Options that indicate the user interactions that the map responds to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapInteractionModes
```

## Overview

A person can’t interact with a map if the option set is empty.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Declared interaction modes

- [all](mapinteractionmodes/all.md) — The map allows all interaction modes.
- [pan](mapinteractionmodes/pan.md) — The map allows a person to pan around to different areas of the map.
- [zoom](mapinteractionmodes/zoom.md) — The map allows people to zoom in or out on map locations.
- [pitch](mapinteractionmodes/pitch.md) — The map allows people to set the map’s pitch to view the map from different angles.
- [rotate](mapinteractionmodes/rotate.md) — The map allows people to rotate the map.

## See Also

### Creating a map

- [init(bounds:interactionModes:scope:)](<map/init(bounds_interactionmodes_scope_).md>) — Creates a new, empty map with the bounds, interaction modes, and scope you provide.
- [init(bounds:interactionModes:scope:content:)](<map/init(bounds_interactionmodes_scope_content_).md>) — Creates a new map with the bounds, interaction modes, scope, and content you provide.
- [init(bounds:interactionModes:selection:scope:)](<map/init(bounds_interactionmodes_selection_scope_)-11lec.md>) — Creates a new, empty map with the bounds, interaction modes, a binding to a map feature, and scope you provide.
- [init(bounds:interactionModes:selection:scope:)](<map/init(bounds_interactionmodes_selection_scope_)-236di.md>) — Creates a new, empty map with the bounds, interaction modes, the selected map feature, and scope you provide.
- [init(bounds:interactionModes:selection:scope:content:)](<map/init(bounds_interactionmodes_selection_scope_content_)-28wns.md>) — Creates a new map with the bounds, interaction modes, selected map feature, scope, and map content you provide.
- [init(bounds:interactionModes:selection:scope:content:)](<map/init(bounds_interactionmodes_selection_scope_content_)-2tdbr.md>) — Creates a new map with the bounds, interaction modes, selected value, scope, and map content you provide.
- [init(initialPosition:bounds:interactionModes:scope:)](<map/init(initialposition_bounds_interactionmodes_scope_).md>) — Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init(initialPosition:bounds:interactionModes:scope:content:)](<map/init(initialposition_bounds_interactionmodes_scope_content_).md>) — Creates a new map with the initial camera position, bounds, interaction modes, scope, and map content you provide.
- [init(initialPosition:bounds:interactionModes:selection:scope:)](<map/init(initialposition_bounds_interactionmodes_selection_scope_).md>) — Creates a new, empty map with the initial camera position, bounds, interaction modes, selected map feature, and scope you provide.
- [init(initialPosition:bounds:interactionModes:selection:scope:content:)](<map/init(initialposition_bounds_interactionmodes_selection_scope_content_)-9feos.md>) — Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init(initialPosition:bounds:interactionModes:selection:scope:content:)](<map/init(initialposition_bounds_interactionmodes_selection_scope_content_)-451vp.md>) — Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init(position:bounds:interactionModes:scope:)](<map/init(position_bounds_interactionmodes_scope_).md>) — Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init(position:bounds:interactionModes:scope:content:)](<map/init(position_bounds_interactionmodes_scope_content_).md>) — Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init(position:bounds:interactionModes:selection:scope:)](<map/init(position_bounds_interactionmodes_selection_scope_).md>) — Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init(position:bounds:interactionModes:selection:scope:content:)](<map/init(position_bounds_interactionmodes_selection_scope_content_)-47y4p.md>) — Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.
