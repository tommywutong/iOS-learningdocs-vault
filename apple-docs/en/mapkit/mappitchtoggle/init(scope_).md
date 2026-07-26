---
title: 'init(scope:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mappitchtoggle/init(scope:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mappitchtoggle/init(scope:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mappitchtoggle/init%28scope%3A%29.json'
content_hash: 'sha256:40b3ff904b37e803'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapPitchToggle](../mappitchtoggle.md)

# init(scope:)

<sub>Initializer</sub>

Creates a new map pitch toggle control with the provided scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency init(scope: Namespace.ID? = nil)
```

## Parameters

- `scope` — The namespace the framework passes to the associated [Map](../map.md) and `MapPitchToggle/mapScope(_:)`.
