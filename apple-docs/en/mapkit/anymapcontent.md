---
title: AnyMapContent
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, tvOS 17.5+, visionOS 1.2+, watchOS 10.5+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/anymapcontent
source_url: 'https://developer.apple.com/documentation/mapkit/anymapcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/anymapcontent.json'
content_hash: 'sha256:b55f8ae4d0924575'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# AnyMapContent

<sub>Structure</sub>

A type-erased map content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct AnyMapContent
```

## Overview

An `AnyMapContent` allows changing the type of content used in a given map view.

## Relationships

- **Conforms To**: [MapContent](mapcontent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<anymapcontent/init(__).md>) — Create an instance that type-erases `base`.
