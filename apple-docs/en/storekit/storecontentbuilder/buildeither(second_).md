---
title: 'buildEither(second:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storecontentbuilder/buildeither(second:)'
source_url: 'https://developer.apple.com/documentation/storekit/storecontentbuilder/buildeither(second:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storecontentbuilder/buildeither%28second%3A%29.json'
content_hash: 'sha256:f206c726e114b9d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreContentBuilder](../storecontentbuilder.md)

# buildEither(second:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent> where TrueContent : StoreContent, FalseContent : StoreContent
```

## See Also

### Building store content

- [buildBlock(_:)](<buildblock(__).md>)
- [buildEither(first:)](<buildeither(first_).md>)
- [buildExpression(_:)](<buildexpression(__).md>)
- [buildIf(_:)](<buildif(__).md>)
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>)
- [TupleStoreContent](../tuplestorecontent.md)
