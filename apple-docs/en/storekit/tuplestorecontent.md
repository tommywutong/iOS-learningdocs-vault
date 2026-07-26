---
title: TupleStoreContent
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/tuplestorecontent
source_url: 'https://developer.apple.com/documentation/storekit/tuplestorecontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/tuplestorecontent.json'
content_hash: 'sha256:e02a1efbb55a8a8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# TupleStoreContent

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct TupleStoreContent<each Content> where repeat each Content : StoreContent
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [StoreContent](storecontent.md)

## See Also

### Building store content

- [buildBlock(_:)](<storecontentbuilder/buildblock(__).md>)
- [buildEither(first:)](<storecontentbuilder/buildeither(first_).md>)
- [buildEither(second:)](<storecontentbuilder/buildeither(second_).md>)
- [buildExpression(_:)](<storecontentbuilder/buildexpression(__).md>)
- [buildIf(_:)](<storecontentbuilder/buildif(__).md>)
- [buildLimitedAvailability(_:)](<storecontentbuilder/buildlimitedavailability(__).md>)
