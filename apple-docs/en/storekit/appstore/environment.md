---
title: AppStore.Environment
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/appstore/environment
source_url: 'https://developer.apple.com/documentation/storekit/appstore/environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore/environment.json'
content_hash: 'sha256:80c81c288f1eacef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppStore](../appstore.md)

# AppStore.Environment

<sub>Structure</sub>

Constants that represent the App Store server environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Environment
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the environment value

- [production](environment/production.md) — A value that indicates the production server environment.
- [sandbox](environment/sandbox.md) — A value that indicates the sandbox server environment.
- [xcode](environment/xcode.md) — A value that indicates the StoreKit Testing in Xcode environment.

## See Also

### Getting the environment

- [environment](../apptransaction/environment.md) — The server environment that signs the app transaction.
