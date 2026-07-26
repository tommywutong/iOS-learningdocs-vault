---
title: 'buildIf(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storecontentbuilder/buildif(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/storecontentbuilder/buildif(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storecontentbuilder/buildif%28_%3A%29.json'
content_hash: 'sha256:2b1e1aba71ae75d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreContentBuilder](../storecontentbuilder.md)

# buildIf(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildIf<Content>(_ section: Content?) -> Content? where Content : StoreContent
```

## See Also

### Building store content

- [buildBlock(_:)](<buildblock(__).md>)
- [buildEither(first:)](<buildeither(first_).md>)
- [buildEither(second:)](<buildeither(second_).md>)
- [buildExpression(_:)](<buildexpression(__).md>)
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>)
- [TupleStoreContent](../tuplestorecontent.md)
