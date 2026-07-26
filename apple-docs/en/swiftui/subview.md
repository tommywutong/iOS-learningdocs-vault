---
title: Subview
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/subview
source_url: 'https://developer.apple.com/documentation/swiftui/subview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/subview.json'
content_hash: 'sha256:8a8c484d3fe2550b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Subview

<sub>Structure</sub>

An opaque value representing a subview of another view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct Subview
```

## Overview

Access to a `Subview` can be obtained by using `ForEach(subviews:)` or `Group(subviews:)`.

Subviews are proxies to the resolved view they represent, meaning that modifiers applied to the original view will be applied before modifiers applied to the subview, and the view is resolved using the environment of its container, _not_ the environment of the its subview proxy. Additionally, because subviews must represent a single leaf view, or container, a subview may represent a view after the application of styles. As such, attempting to apply a style to it may have no affect.

## Relationships

- **Conforms To**: [Identifiable](../swift/identifiable.md), [View](view.md)

## Topics

### Structures

- [ID](subview/id-swift.struct.md) — A unique identifier for a subview.

### Instance Properties

- [containerValues](subview/containervalues.md) — The container values associated with the given subview.
- [id](subview/id-swift.property.md) — The unique identifier of the view.

### Enumerations

- [ContainerSizingOptions](subview/containersizingoptions.md) — Options on how all subviews should be sized when in a container.

## See Also

### Accessing a container’s subviews

- [SubviewsCollection](subviewscollection.md) — An opaque collection representing the subviews of view.
- [SubviewsCollectionSlice](subviewscollectionslice.md) — A slice of a SubviewsCollection.
- [containerValue(_:_:)](<view/containervalue(____).md>) — Sets a particular container value of a view.
- [ContainerValues](containervalues.md) — A collection of container values associated with a given view.
- [ContainerValueKey](containervaluekey.md) — A key for accessing container values.
