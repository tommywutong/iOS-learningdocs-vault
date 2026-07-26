---
title: 'init(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/schema/relationship/init(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/relationship/init(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/relationship/init%28_%3Adeleterule%3Aminimummodelcount%3Amaximummodelcount%3Aoriginalname%3Ainverse%3Ahashmodifier%3A%29.json'
content_hash: 'sha256:349ade232210acd9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftData](../../../swiftdata.md) · [Schema](../../schema.md) · [Relationship](../relationship.md)

# init(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ options: Schema.Relationship.Option..., deleteRule: Schema.Relationship.DeleteRule = .nullify, minimumModelCount: Int? = 0, maximumModelCount: Int? = 0, originalName: String? = nil, inverse: AnyKeyPath? = nil, hashModifier: String? = nil)
```
