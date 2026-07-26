---
title: HistoryObserver
framework: SwiftData
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/historyobserver
source_url: 'https://developer.apple.com/documentation/swiftdata/historyobserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historyobserver.json'
content_hash: 'sha256:b6a044091e6ad762'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# HistoryObserver

<sub>Class</sub>

Monitors a model container’s data stores for remote changes and notifies when new history transactions are available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class HistoryObserver
```

## Overview

`HistoryObserver` automatically listens for `ModelContainer/remoteChange` notifications and determines whether the incoming changes are relevant based on the models you specify at initialization. When relevant changes are detected, the observer updates its [eventCounter](historyobserver/eventcounter.md) property.

Use `HistoryObserver` as an `@Observable` object and react to changes in [eventCounter](historyobserver/eventcounter.md) from a SwiftUI view or other observer.

The observer tracks its position in each data store’s transaction history using `historyTokens`, enabling incremental processing of only new transactions since the last check.

You can scope the observer to specific model types using the `observedModels` parameter. When provided with a non-empty array, the observer filters incoming transactions to only those containing changes for the specified types (and optionally their related models). When the array is empty (the default), the observer responds to any history change in the container.

Example usage:

```swift
let observer = try HistoryObserver(
    observedModels: [Trip.self],
    modelContainer: container
)
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Observable](../observation/observable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a history observer

- [init(historyTokens:observedModels:authors:modelContainer:isolation:)](<historyobserver/init(historytokens_observedmodels_authors_modelcontainer_isolation_).md>) — Creates a history observer that reports changes through its observable [eventCounter](historyobserver/eventcounter.md) property. _(beta)_

### Accessing observer properties

- [eventCounter](historyobserver/eventcounter.md) — A counter that increments each time the observer detects relevant changes. _(beta)_
- [modelContainer](historyobserver/modelcontainer.md) — The model container whose data stores this observer monitors for changes. _(beta)_
- [observedModels](historyobserver/observedmodels.md) — The model types that the observer filters for when evaluating history transactions. _(beta)_
- [authors](historyobserver/authors.md) — The transaction authors that the observer filters for when evaluating history transactions. _(beta)_

## See Also

### Data store observation

- [ResultsObserver](resultsobserver.md) — Observes and tracks changes to a collection of persistent models in a model context. _(beta)_
