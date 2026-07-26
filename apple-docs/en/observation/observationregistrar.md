---
title: ObservationRegistrar
framework: Observation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/observation/observationregistrar
source_url: 'https://developer.apple.com/documentation/observation/observationregistrar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observationregistrar.json'
content_hash: 'sha256:10d04b5d3eb57319'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Observation](../observation.md)

# ObservationRegistrar

<sub>Structure</sub>

Provides storage for tracking and access to data changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ObservationRegistrar
```

## Overview

You don’t need to create an instance of `ObservationRegistrar` when using the [Observable()](<observable().md>) macro to indicate observability of a type.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an observation registrar

- [init()](<observationregistrar/init().md>) — Creates an instance of the observation registrar.

### Receiving change notifications

- [willSet(_:keyPath:)](<observationregistrar/willset(__keypath_).md>) — A property observation called before setting the value of the subject.
- [didSet(_:keyPath:)](<observationregistrar/didset(__keypath_).md>) — A property observation called after setting the value of the subject.

### Identifying transactional access

- [access(_:keyPath:)](<observationregistrar/access(__keypath_).md>) — Registers access to a specific property for observation.
- [withMutation(of:keyPath:_:)](<observationregistrar/withmutation(of_keypath___).md>) — Identifies mutations to the transactions registered for observers.

## See Also

### Change tracking

- [withObservationTracking(_:onChange:)](<withobservationtracking(__onchange_).md>) — Tracks access to properties.
