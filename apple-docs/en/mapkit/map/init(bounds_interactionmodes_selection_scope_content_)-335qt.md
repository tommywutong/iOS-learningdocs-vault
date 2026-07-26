---
title: 'init(bounds:interactionModes:selection:scope:content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/map/init(bounds:interactionmodes:selection:scope:content:)-335qt'
source_url: 'https://developer.apple.com/documentation/mapkit/map/init(bounds:interactionmodes:selection:scope:content:)-335qt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/map/init%28bounds%3Ainteractionmodes%3Aselection%3Ascope%3Acontent%3A%29-335qt.json'
content_hash: 'sha256:bf9a4839932f872b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Map](../map.md)

# init(bounds:interactionModes:selection:scope:content:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency init<SelectedValue, C>(bounds: MapCameraBounds? = nil, interactionModes: MapInteractionModes = .all, selection: Binding<SelectedValue?>, scope: Namespace.ID? = nil, @MapContentBuilder content: () -> C) where Content == MapSelectableContentView<SelectedValue, C>, SelectedValue : MapSelectable, C : MapContent
```
