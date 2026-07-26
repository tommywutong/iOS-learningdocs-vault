---
title: 'init(_:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, tvOS 17.5+, visionOS 1.2+, watchOS 10.5+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/anymapcontent/init(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/anymapcontent/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/anymapcontent/init%28_%3A%29.json'
content_hash: 'sha256:ce718688157a5da5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [AnyMapContent](../anymapcontent.md)

# init(_:)

<sub>Initializer</sub>

Create an instance that type-erases `base`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init<Content>(_ base: Content) where Content : MapContent
```
