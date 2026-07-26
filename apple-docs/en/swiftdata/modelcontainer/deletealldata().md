---
title: deleteAllData()
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, tvOS 17.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 10.0+（27.0 起废弃）, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swiftdata/modelcontainer/deletealldata()
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontainer/deletealldata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontainer/deletealldata%28%29.json'
content_hash: 'sha256:ce0dbb30c60480d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContainer](../modelcontainer.md)

# deleteAllData()

<sub>Instance Method</sub>

Removes all persisted model data from the app’s persistent storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deleteAllData()
```

## Discussion

> [!warning] Warning
> After you call this method, the container immediately deletes all data from the app’s persistent storage. This deletion is permanent and cannot be undone.
