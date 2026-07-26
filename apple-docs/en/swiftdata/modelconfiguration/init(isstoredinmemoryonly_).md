---
title: 'init(isStoredInMemoryOnly:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelconfiguration/init(isstoredinmemoryonly:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelconfiguration/init(isstoredinmemoryonly:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelconfiguration/init%28isstoredinmemoryonly%3A%29.json'
content_hash: 'sha256:e73e1d5c7c45ad8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelConfiguration](../modelconfiguration.md)

# init(isStoredInMemoryOnly:)

<sub>Initializer</sub>

Creates a basic model configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(isStoredInMemoryOnly: Bool = false)
```

## Parameters

- `isStoredInMemoryOnly` — A Boolean value that determines whether the associated persistent storage is ephemeral and exists only in memory. The default value is `false`.

## See Also

### Creating a model configuration

- [init(for:isStoredInMemoryOnly:)](<init(for_isstoredinmemoryonly_).md>) — Creates a model configuration for the specified model types.
- [init(_:schema:isStoredInMemoryOnly:allowsSave:groupContainer:cloudKitDatabase:)](<init(__schema_isstoredinmemoryonly_allowssave_groupcontainer_cloudkitdatabase_).md>) — Creates a named model configuration for the specified schema.
- [init(_:schema:url:allowsSave:cloudKitDatabase:)](<init(__schema_url_allowssave_cloudkitdatabase_).md>) — Creates a named model configuration that specifies the on-disk location of the schema’s persistent storage.
