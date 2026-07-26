---
title: 'initializeCloudKitSchema(options:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcloudkitcontainer/initializecloudkitschema(options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/initializecloudkitschema(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/initializecloudkitschema%28options%3A%29.json'
content_hash: 'sha256:5e4a0c0b634c1647'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# initializeCloudKitSchema(options:)

<sub>Instance Method</sub>

Creates the CloudKit schema for all stores in the container that manage a CloudKit database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initializeCloudKitSchema(options: NSPersistentCloudKitContainerSchemaInitializationOptions = []) throws
```

## Parameters

- `options` — The options to use when creating the CloudKit schema.

## Discussion

To create the schema, this method creates a set of representative [CKRecord](../../cloudkit/ckrecord.md) instances for all stores in the container that use Core Data with CloudKit, and uploads them to CloudKit. These records have a representative value for every field Core Data might serialize for the specified managed object model. After successfully uploading the records, the schema is visible in the CloudKit Dashboard and the container deletes the representative records.

> [!note] Note
> This method also validates the managed object model in use for a store, so if the model isn’t valid for use with CloudKit, a validation error may return.

## See Also

### Promoting Your Schema

- [NSPersistentCloudKitContainerSchemaInitializationOptions](../nspersistentcloudkitcontainerschemainitializationoptions.md) — Options that control the behavior when promoting the container’s schema to CloudKit.
