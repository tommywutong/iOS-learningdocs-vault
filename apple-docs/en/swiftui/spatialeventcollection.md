---
title: SpatialEventCollection
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialeventcollection
source_url: 'https://developer.apple.com/documentation/swiftui/spatialeventcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialeventcollection.json'
content_hash: 'sha256:5fb27404af0a0a4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SpatialEventCollection

<sub>Structure</sub>

A collection of spatial input events that target a specific view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct SpatialEventCollection
```

## Overview

You receive a structure of this type as an input to the [onChanged(_:)](<gesture/onchanged(__).md>) or [onEnded(_:)](<gesture/onended(__).md>) method of a [SpatialEventGesture](spatialeventgesture.md). The structure contains a collection of [Event](spatialeventcollection/event.md) values that correspond to ongoing input events. You can look up a specific event in the collection by its [id](spatialeventcollection/event/id-swift.property.md) value or iterate over all events in the collection to apply logic depending on the event’s state.

## Relationships

- **Conforms To**: [Collection](../swift/collection.md), [Equatable](../swift/equatable.md), [Sequence](../swift/sequence.md)

## Topics

### Accessing the collection’s events

- [Event](spatialeventcollection/event.md) — A spatial event generated from an input like a touch or click that can drive gestures in the system.
- [subscript(_:)](<spatialeventcollection/subscript(__).md>) — Retrieves an event using its unique identifier.

### Iterating over events in the collection

- [makeIterator()](<spatialeventcollection/makeiterator().md>) — Makes an iterator over all events in the collection.
- [Iterator](spatialeventcollection/iterator.md) — An iterator over all events in the collection.

## See Also

### Recognizing spatial events

- [SpatialEventGesture](spatialeventgesture.md) — A gesture that provides information about ongoing spatial events like clicks and touches.
- [Chirality](chirality.md) — The chirality, or handedness, of a pose.
