---
title: 'buildBlock(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storecontentbuilder/buildblock(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/storecontentbuilder/buildblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storecontentbuilder/buildblock%28_%3A%29.json'
content_hash: 'sha256:34d8276cf70ad93d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreContentBuilder](../storecontentbuilder.md)

# buildBlock(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildBlock<each Content>(_ content: repeat each Content) -> TupleStoreContent<repeat each Content> where repeat each Content : StoreContent
```

## See Also

### Building store content

- [buildEither(first:)](<buildeither(first_).md>)
- [buildEither(second:)](<buildeither(second_).md>)
- [buildExpression(_:)](<buildexpression(__).md>)
- [buildIf(_:)](<buildif(__).md>)
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>)
- [TupleStoreContent](../tuplestorecontent.md)
