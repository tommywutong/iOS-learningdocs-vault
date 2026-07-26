---
title: 'init(_:schema:isStoredInMemoryOnly:allowsSave:groupContainer:cloudKitDatabase:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelconfiguration/init(_:schema:isstoredinmemoryonly:allowssave:groupcontainer:cloudkitdatabase:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelconfiguration/init(_:schema:isstoredinmemoryonly:allowssave:groupcontainer:cloudkitdatabase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelconfiguration/init%28_%3Aschema%3Aisstoredinmemoryonly%3Aallowssave%3Agroupcontainer%3Acloudkitdatabase%3A%29.json'
content_hash: 'sha256:66d55af67aa6bd6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelConfiguration](../modelconfiguration.md)

# init(_:schema:isStoredInMemoryOnly:allowsSave:groupContainer:cloudKitDatabase:)

<sub>Initializer</sub>

Creates a named model configuration for the specified schema.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ name: String? = nil, schema: Schema? = nil, isStoredInMemoryOnly: Bool = false, allowsSave: Bool = true, groupContainer: ModelConfiguration.GroupContainer = .automatic, cloudKitDatabase: ModelConfiguration.CloudKitDatabase = .automatic)
```

## Parameters

- `name` — An optional name for the model configuration.

- `schema` — A schema that maps model classes to the associated data in the persistent storage. For more information, see [Schema](../schema.md).

- `isStoredInMemoryOnly` — A Boolean value that determines whether the associated persistent storage is ephemeral and exists only in memory. The default value is `false`.

- `allowsSave` — A Boolean value that determines whether the associated persistent storage is writable. The default value is `true`.

- `groupContainer` — The option to use for detecting the configuration’s group container. For possible values, see [GroupContainer](groupcontainer-swift.struct.md).

- `cloudKitDatabase` — The option to use for detecting the configuration’s CloudKit database. For possible values, see [CloudKitDatabase](cloudkitdatabase-swift.struct.md).

## See Also

### Creating a model configuration

- [init(isStoredInMemoryOnly:)](<init(isstoredinmemoryonly_).md>) — Creates a basic model configuration.
- [init(for:isStoredInMemoryOnly:)](<init(for_isstoredinmemoryonly_).md>) — Creates a model configuration for the specified model types.
- [init(_:schema:url:allowsSave:cloudKitDatabase:)](<init(__schema_url_allowssave_cloudkitdatabase_).md>) — Creates a named model configuration that specifies the on-disk location of the schema’s persistent storage.
