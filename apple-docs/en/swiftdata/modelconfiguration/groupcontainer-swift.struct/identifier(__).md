---
title: 'identifier(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct/identifier(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct/identifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct/identifier%28_%3A%29.json'
content_hash: 'sha256:a28bfbda7d7632a1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftData](../../../swiftdata.md) · [ModelConfiguration](../../modelconfiguration.md) · [GroupContainer](../groupcontainer-swift.struct.md)

# identifier(_:)

<sub>Type Method</sub>

Tells SwiftData to use the specified group container as the root location for the app’s persistent storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func identifier(_ groupName: String) -> ModelConfiguration.GroupContainer
```

## Parameters

- `groupName` — The identifier of the group container to use. You find these in the App Groups capabilities section of your Xcode project. For more information, see [Configuring app groups](../../../xcode/configuring-app-groups.md).

## See Also

### Getting discovery options

- [automatic](automatic.md) — Tells SwiftData to use the app’s primary group container as the root location for the persistent storage.
- [none](none.md) — Prevents SwiftData from using a group container as the root location for the app’s persistent storage.
