---
title: 'private(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelconfiguration/cloudkitdatabase-swift.struct/private(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelconfiguration/cloudkitdatabase-swift.struct/private(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelconfiguration/cloudkitdatabase-swift.struct/private%28_%3A%29.json'
content_hash: 'sha256:e1c62df9c14d4a66'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftData](../../../swiftdata.md) · [ModelConfiguration](../../modelconfiguration.md) · [CloudKitDatabase](../cloudkitdatabase-swift.struct.md)

# private(_:)

<sub>Type Method</sub>

Enables managed CloudKit sync using the specified ubiquity container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func `private`(_ privateDBName: String) -> ModelConfiguration.CloudKitDatabase
```

## Parameters

- `privateDBName` — The identifier of the iCloud ubiquity container to use. You find these in the iCloud capabilities section of your Xcode project. For more information, see [Configuring iCloud services](../../../xcode/configuring-icloud-services.md).

## See Also

### Getting discovery options

- [automatic](automatic.md) — Enables managed CloudKit sync using the primary ubiquity container from the app’s entitlements.
- [none](none.md) — Disables managed CloudKit sync.
