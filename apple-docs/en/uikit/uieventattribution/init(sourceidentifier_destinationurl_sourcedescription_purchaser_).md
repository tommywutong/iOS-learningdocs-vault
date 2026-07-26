---
title: 'init(sourceIdentifier:destinationURL:sourceDescription:purchaser:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieventattribution/init(sourceidentifier:destinationurl:sourcedescription:purchaser:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieventattribution/init(sourceidentifier:destinationurl:sourcedescription:purchaser:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieventattribution/init%28sourceidentifier%3Adestinationurl%3Asourcedescription%3Apurchaser%3A%29.json'
content_hash: 'sha256:4cf25cf375e03c40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEventAttribution](../uieventattribution.md)

# init(sourceIdentifier:destinationURL:sourceDescription:purchaser:)

<sub>Initializer</sub>

Initializes a new event attribution object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(sourceIdentifier: UInt8, destinationURL: URL, sourceDescription: String, purchaser: String)
```

## Parameters

- `sourceIdentifier` — An 8-bit number that identifies the source of the click for attribution. Value must be between `0` and `255`.

- `destinationURL` — The destination URL of the attribution.

- `sourceDescription` — A description of the source of the attribution.

- `purchaser` — A string that describes the entity that purchased the attributed content.
