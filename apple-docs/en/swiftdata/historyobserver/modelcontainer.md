---
title: modelContainer
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/historyobserver/modelcontainer
source_url: 'https://developer.apple.com/documentation/swiftdata/historyobserver/modelcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historyobserver/modelcontainer.json'
content_hash: 'sha256:d076b992ed799166'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryObserver](../historyobserver.md)

# modelContainer

<sub>Instance Property</sub>

The model container whose data stores this observer monitors for changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final let modelContainer: ModelContainer
```

## See Also

### Accessing observer properties

- [eventCounter](eventcounter.md) — A counter that increments each time the observer detects relevant changes. _(beta)_
- [observedModels](observedmodels.md) — The model types that the observer filters for when evaluating history transactions. _(beta)_
- [authors](authors.md) — The transaction authors that the observer filters for when evaluating history transactions. _(beta)_
