---
title: 'buildBlock(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontentbuilder/buildblock(_:)-5ewn9'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontentbuilder/buildblock(_:)-5ewn9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontentbuilder/buildblock%28_%3A%29-5ewn9.json'
content_hash: 'sha256:9549f4a64f515ba8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContentBuilder](../mapcontentbuilder.md)

# buildBlock(_:)

<sub>Type Method</sub>

Creates a map content block that contains a single content result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildBlock<C>(_ content: C) -> C where C : MapContent
```

## Parameters

- `content` — The view content to add to the block.

## Return Value

Returns the [MapContent](../mapcontent.md) with the single element you provided.

## See Also

### Map content builders

- [buildBlock()](<buildblock().md>) — Creates an empty map content block that contains no statements.
