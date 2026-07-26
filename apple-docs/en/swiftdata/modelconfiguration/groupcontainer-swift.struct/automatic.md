---
title: automatic
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct/automatic
source_url: 'https://developer.apple.com/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct/automatic.json'
content_hash: 'sha256:11f5041c8b2612ba'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftData](../../../swiftdata.md) · [ModelConfiguration](../../modelconfiguration.md) · [GroupContainer](../groupcontainer-swift.struct.md)

# automatic

<sub>Type Property</sub>

Tells SwiftData to use the app’s primary group container as the root location for the persistent storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: ModelConfiguration.GroupContainer { get }
```

## See Also

### Getting discovery options

- [identifier(_:)](<identifier(__).md>) — Tells SwiftData to use the specified group container as the root location for the app’s persistent storage.
- [none](none.md) — Prevents SwiftData from using a group container as the root location for the app’s persistent storage.
