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
doc_path: '/documentation/mapkit/map/init(position:bounds:interactionmodes:selection:scope:content:)-96bhq'
source_url: 'https://developer.apple.com/documentation/mapkit/map/init(position:bounds:interactionmodes:selection:scope:content:)-96bhq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/map/init%28position%3Abounds%3Ainteractionmodes%3Aselection%3Ascope%3Acontent%3A%29-96bhq.json'
content_hash: 'sha256:a8271ead4752e0d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Map](../map.md)

# init(position:bounds:interactionModes:selection:scope:content:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency init<SelectedValue, C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds? = nil, interactionModes: MapInteractionModes = .all, selection: Binding<SelectedValue?>, scope: Namespace.ID? = nil, @MapContentBuilder content: () -> C) where Content == MapSelectableContentView<SelectedValue, C>, SelectedValue : MapSelectable, C : MapContent
```
