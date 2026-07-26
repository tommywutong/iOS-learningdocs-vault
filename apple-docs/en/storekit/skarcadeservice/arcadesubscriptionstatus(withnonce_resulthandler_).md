---
title: 'arcadeSubscriptionStatus(withNonce:resultHandler:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skarcadeservice/arcadesubscriptionstatus(withnonce:resulthandler:)'
source_url: 'https://developer.apple.com/documentation/storekit/skarcadeservice/arcadesubscriptionstatus(withnonce:resulthandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skarcadeservice/arcadesubscriptionstatus%28withnonce%3Aresulthandler%3A%29.json'
content_hash: 'sha256:6ef669c7da768129'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKArcadeService](../skarcadeservice.md)

# arcadeSubscriptionStatus(withNonce:resultHandler:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func arcadeSubscriptionStatus(withNonce nonce: UInt64, resultHandler: @escaping (Data?, UInt32, Data?, UInt32, (any Error)?) -> Void)
```

## See Also

### Type Methods

- [+ registerArcadeAppWithRandomFromLib:randomFromLibLength:resultHandler:](<registerarcadeappwithrandom(fromlib_randomfromliblength_resulthandler_).md>)
- [+ repairArcadeApp](<repairarcadeapp().md>)
