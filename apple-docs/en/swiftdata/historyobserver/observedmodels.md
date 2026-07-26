---
title: observedModels
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/historyobserver/observedmodels
source_url: 'https://developer.apple.com/documentation/swiftdata/historyobserver/observedmodels'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historyobserver/observedmodels.json'
content_hash: 'sha256:d8fd4d474e83993c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryObserver](../historyobserver.md)

# observedModels

<sub>Instance Property</sub>

The model types that the observer filters for when evaluating history transactions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final let observedModels: [any PersistentModel.Type]
```

## Discussion

When non-empty, the observer only reports changes whose transactions contain modifications to instances of these types. When empty, the observer treats any new transaction as relevant.

## See Also

### Accessing observer properties

- [eventCounter](eventcounter.md) — A counter that increments each time the observer detects relevant changes. _(beta)_
- [modelContainer](modelcontainer.md) — The model container whose data stores this observer monitors for changes. _(beta)_
- [authors](authors.md) — The transaction authors that the observer filters for when evaluating history transactions. _(beta)_
