---
title: 'buildExpression(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storecontentbuilder/buildexpression(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/storecontentbuilder/buildexpression(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storecontentbuilder/buildexpression%28_%3A%29.json'
content_hash: 'sha256:35784790ce4111f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreContentBuilder](../storecontentbuilder.md)

# buildExpression(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildExpression<Content>(_ content: Content) -> some StoreContent where Content : StoreContent

```

## See Also

### Building store content

- [buildBlock(_:)](<buildblock(__).md>)
- [buildEither(first:)](<buildeither(first_).md>)
- [buildEither(second:)](<buildeither(second_).md>)
- [buildIf(_:)](<buildif(__).md>)
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>)
- [TupleStoreContent](../tuplestorecontent.md)
