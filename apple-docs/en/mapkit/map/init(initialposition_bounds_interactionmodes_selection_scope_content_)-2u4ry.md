---
title: 'init(initialPosition:bounds:interactionModes:selection:scope:content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/map/init(initialposition:bounds:interactionmodes:selection:scope:content:)-2u4ry'
source_url: 'https://developer.apple.com/documentation/mapkit/map/init(initialposition:bounds:interactionmodes:selection:scope:content:)-2u4ry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/map/init%28initialposition%3Abounds%3Ainteractionmodes%3Aselection%3Ascope%3Acontent%3A%29-2u4ry.json'
content_hash: 'sha256:3d5aed9f3eeb241e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Map](../map.md)

# init(initialPosition:bounds:interactionModes:selection:scope:content:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency init<SelectedValue, C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds? = nil, interactionModes: MapInteractionModes = .all, selection: Binding<SelectedValue?>, scope: Namespace.ID? = nil, @MapContentBuilder content: () -> C) where Content == MapSelectableContentView<SelectedValue, C>, SelectedValue : MapSelectable, C : MapContent
```
