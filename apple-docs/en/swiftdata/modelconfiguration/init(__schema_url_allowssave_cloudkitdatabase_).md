---
title: 'init(_:schema:url:allowsSave:cloudKitDatabase:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelconfiguration/init(_:schema:url:allowssave:cloudkitdatabase:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelconfiguration/init(_:schema:url:allowssave:cloudkitdatabase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelconfiguration/init%28_%3Aschema%3Aurl%3Aallowssave%3Acloudkitdatabase%3A%29.json'
content_hash: 'sha256:29ae6d34b00a6649'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelConfiguration](../modelconfiguration.md)

# init(_:schema:url:allowsSave:cloudKitDatabase:)

<sub>Initializer</sub>

Creates a named model configuration that specifies the on-disk location of the schema’s persistent storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ name: String? = nil, schema: Schema? = nil, url: URL, allowsSave: Bool = true, cloudKitDatabase: ModelConfiguration.CloudKitDatabase = .automatic)
```

## Parameters

- `name` — An optional name for the model configuration.

- `schema` — A schema that maps model classes to the associated data in the persistent storage. For more information, see [Schema](../schema.md).

- `url` — The on-disk location of the schema’s persistent storage.

- `allowsSave` — A Boolean value that determines whether the associated persistent storage is writable. The default value is `true`.

- `cloudKitDatabase` — The option to use for detecting the configuration’s CloudKit database. For possible values, see [CloudKitDatabase](cloudkitdatabase-swift.struct.md).

## See Also

### Creating a model configuration

- [init(isStoredInMemoryOnly:)](<init(isstoredinmemoryonly_).md>) — Creates a basic model configuration.
- [init(for:isStoredInMemoryOnly:)](<init(for_isstoredinmemoryonly_).md>) — Creates a model configuration for the specified model types.
- [init(_:schema:isStoredInMemoryOnly:allowsSave:groupContainer:cloudKitDatabase:)](<init(__schema_isstoredinmemoryonly_allowssave_groupcontainer_cloudkitdatabase_).md>) — Creates a named model configuration for the specified schema.
