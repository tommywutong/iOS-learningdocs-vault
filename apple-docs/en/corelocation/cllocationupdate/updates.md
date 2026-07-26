---
title: CLLocationUpdate.Updates
framework: Core Location
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationupdate/updates
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationupdate/updates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationupdate/updates.json'
content_hash: 'sha256:0b44f491546e350b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationUpdate](../cllocationupdate.md)

# CLLocationUpdate.Updates

<sub>Structure</sub>

A structure that represents an asynchronous sequence of location updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Updates
```

## Overview

[CLLocationUpdate](../cllocationupdate.md) uses this structure to asynchronously deliver a stream of location updates to your app when you call [liveUpdates(_:)](<liveupdates(__).md>).

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Type aliases

- [Iterator](updates/iterator.md) — The type of the update’s iterator.

## See Also

### Receiving location updates

- [liveUpdates(_:)](<liveupdates(__).md>) — Tells Core Location to start delivering the location updates it produces for the configuration you specify.
- [LiveConfiguration](liveconfiguration.md) — Values for indicating the kind of updates the framework delivers.
