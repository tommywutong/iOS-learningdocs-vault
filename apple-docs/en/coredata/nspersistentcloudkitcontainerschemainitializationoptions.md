---
title: NSPersistentCloudKitContainerSchemaInitializationOptions
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainerschemainitializationoptions
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainerschemainitializationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainerschemainitializationoptions.json'
content_hash: 'sha256:e0892ec696b64667'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentCloudKitContainerSchemaInitializationOptions

<sub>Structure</sub>

Options that control the behavior when promoting the container’s schema to CloudKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSPersistentCloudKitContainerSchemaInitializationOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [NSPersistentCloudKitContainerSchemaInitializationOptionsDryRun](nspersistentcloudkitcontainerschemainitializationoptions/dryrun.md) — A flag that indicates the container validates the model and generates the records, but doesn’t upload them to CloudKit.
- [NSPersistentCloudKitContainerSchemaInitializationOptionsPrintSchema](nspersistentcloudkitcontainerschemainitializationoptions/printschema.md) — Prints the generated records to the console.

### Initializers

- [init(rawValue:)](<nspersistentcloudkitcontainerschemainitializationoptions/init(rawvalue_).md>) — Creates the schema initialization options using the specified raw value.

## See Also

### Promoting Your Schema

- [- initializeCloudKitSchemaWithOptions:error:](<nspersistentcloudkitcontainer/initializecloudkitschema(options_).md>) — Creates the CloudKit schema for all stores in the container that manage a CloudKit database.
