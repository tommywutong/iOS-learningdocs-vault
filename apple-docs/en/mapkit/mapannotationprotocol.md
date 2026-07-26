---
title: MapAnnotationProtocol
framework: MapKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapannotationprotocol
source_url: 'https://developer.apple.com/documentation/mapkit/mapannotationprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapannotationprotocol.json'
content_hash: 'sha256:ae30788170b4a62e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapAnnotationProtocol

<sub>Protocol</sub>

A protocol that represents the possible return types of annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MapAnnotationProtocol
```

## Overview

Don’t create types conforming to this protocol. Instead, use one of the framework-provided types [MapAnnotation](mapannotation.md), [MapMarker](mapmarker.md), and [MapPin](mappin.md).

## Relationships

- **Conforming Types**: [MapAnnotation](mapannotation.md), [MapMarker](mapmarker.md), [MapPin](mappin.md)

## See Also

### Annotations in SwiftUI

- [MapMarker](mapmarker.md) — A balloon-shaped annotation used to indicate the location on a map. _(deprecated)_
- [MapPin](mappin.md) — A pin-shaped annotation used to indicate a location on a map. _(deprecated)_
- [MapAnnotation](mapannotation.md) — A customizable annotation that marks a map location. _(deprecated)_
