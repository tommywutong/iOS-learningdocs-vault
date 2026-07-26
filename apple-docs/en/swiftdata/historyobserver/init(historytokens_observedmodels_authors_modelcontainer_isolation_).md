---
title: 'init(historyTokens:observedModels:authors:modelContainer:isolation:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/historyobserver/init(historytokens:observedmodels:authors:modelcontainer:isolation:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/historyobserver/init(historytokens:observedmodels:authors:modelcontainer:isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historyobserver/init%28historytokens%3Aobservedmodels%3Aauthors%3Amodelcontainer%3Aisolation%3A%29.json'
content_hash: 'sha256:9c8f17a0d6492437'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [HistoryObserver](../historyobserver.md)

# init(historyTokens:observedModels:authors:modelContainer:isolation:)

<sub>Initializer</sub>

Creates a history observer that reports changes through its observable [eventCounter](eventcounter.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(historyTokens: [String : any HistoryToken]? = nil, observedModels: [any PersistentModel.Type] = [], authors: Set<String> = [], modelContainer: ModelContainer, isolation: isolated (any Actor)? = #isolation) throws
```

## Parameters

- `historyTokens` — The initial history tokens keyed by store identifier. When `nil`, the observer starts with an empty token set and captures tokens from the first notification for each store.

- `observedModels` — The model types to filter for. When empty (the default), the observer responds to changes for any model.

- `authors` — The transaction authors to filter for. When empty (the default), the observer responds to changes from any author.

- `modelContainer` — The model container to observe.

## Discussion

Use this initializer when you want to observe history changes via SwiftUI’s observation system or by reading [eventCounter](eventcounter.md) directly.

> [!danger] Throws
> An error if the observer fails to fetch the initial history tokens.
