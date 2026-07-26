---
title: NamedCoordinateSpace
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/namedcoordinatespace
source_url: 'https://developer.apple.com/documentation/swiftui/namedcoordinatespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/namedcoordinatespace.json'
content_hash: 'sha256:fdca38fd0e3fdf84'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NamedCoordinateSpace

<sub>Structure</sub>

A named coordinate space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NamedCoordinateSpace
```

## Overview

Use the `coordinateSpace(_:)` modifier to assign a name to the local coordinate space of a  parent view. Child views can then refer to that coordinate space using `.named(_:)`.

## Relationships

- **Conforms To**: [CoordinateSpaceProtocol](coordinatespaceprotocol.md), [Equatable](../swift/equatable.md)

## See Also

### Supporting types

- [GlobalCoordinateSpace](globalcoordinatespace.md) — The global coordinate space at the root of the view hierarchy.
- [LocalCoordinateSpace](localcoordinatespace.md) — The local coordinate space of the current view.
