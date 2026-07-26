---
title: authors
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/historyobserver/authors
source_url: 'https://developer.apple.com/documentation/swiftdata/historyobserver/authors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historyobserver/authors.json'
content_hash: 'sha256:c8058e804085ae16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryObserver](../historyobserver.md)

# authors

<sub>Instance Property</sub>

The transaction authors that the observer filters for when evaluating history transactions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final let authors: Set<String>
```

## Discussion

When non-empty, the observer only reports changes whose transactions were written by one of the specified authors. When empty, the observer treats transactions from any author as relevant.

## See Also

### Accessing observer properties

- [eventCounter](eventcounter.md) — A counter that increments each time the observer detects relevant changes. _(beta)_
- [modelContainer](modelcontainer.md) — The model container whose data stores this observer monitors for changes. _(beta)_
- [observedModels](observedmodels.md) — The model types that the observer filters for when evaluating history transactions. _(beta)_
