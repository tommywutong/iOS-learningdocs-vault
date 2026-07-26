---
title: 'init(content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapreader/init(content:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapreader/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapreader/init%28content%3A%29.json'
content_hash: 'sha256:4d157c37e458aaa7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapReader](../mapreader.md)

# init(content:)

<sub>Initializer</sub>

Creates an instance that allows view content to reference information about a contained map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(@ViewBuilder content: @escaping (MapProxy) -> Content)
```

## Parameters

- `content` — The content of the map reader uses to retrieve information about, it uses the first map the `content` contains.

## Return Value

Returns a [MapProxy](../mapproxy.md) that allows you to introspect the content of a map.
