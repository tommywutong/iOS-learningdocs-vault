---
title: SubviewsCollection
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/subviewscollection
source_url: 'https://developer.apple.com/documentation/swiftui/subviewscollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/subviewscollection.json'
content_hash: 'sha256:4f085b362df9422f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SubviewsCollection

<sub>Structure</sub>

An opaque collection representing the subviews of view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SubviewsCollection
```

## Overview

Subviews collection constructs subviews on demand, so only access the part of the collection you need to create the resulting content.

You can get access to a view’s subview collection by using the `Group/init(sectionsOf:transform:)` initializer.

The collection’s elements are the pieces that make up the given view, and the collection as a whole acts as a proxy for the original view.

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sequence](../swift/sequence.md), [View](view.md)

## See Also

### Accessing a container’s subviews

- [Subview](subview.md) — An opaque value representing a subview of another view.
- [SubviewsCollectionSlice](subviewscollectionslice.md) — A slice of a SubviewsCollection.
- [containerValue(_:_:)](<view/containervalue(____).md>) — Sets a particular container value of a view.
- [ContainerValues](containervalues.md) — A collection of container values associated with a given view.
- [ContainerValueKey](containervaluekey.md) — A key for accessing container values.
