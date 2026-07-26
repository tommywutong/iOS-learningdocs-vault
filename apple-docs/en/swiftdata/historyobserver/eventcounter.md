---
title: eventCounter
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/historyobserver/eventcounter
source_url: 'https://developer.apple.com/documentation/swiftdata/historyobserver/eventcounter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historyobserver/eventcounter.json'
content_hash: 'sha256:04205912d7798ed9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryObserver](../historyobserver.md)

# eventCounter

<sub>Instance Property</sub>

A counter that increments each time the observer detects relevant changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var eventCounter: Int { get }
```

## Discussion

The observer increments this value when it processes a remote change notification that contains transactions matching its criteria. You can observe this property from a SwiftUI view to trigger a UI update.

## See Also

### Accessing observer properties

- [modelContainer](modelcontainer.md) — The model container whose data stores this observer monitors for changes. _(beta)_
- [observedModels](observedmodels.md) — The model types that the observer filters for when evaluating history transactions. _(beta)_
- [authors](authors.md) — The transaction authors that the observer filters for when evaluating history transactions. _(beta)_
