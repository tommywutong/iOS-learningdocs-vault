---
title: dryRun
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainerschemainitializationoptions/dryrun
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainerschemainitializationoptions/dryrun'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainerschemainitializationoptions/dryrun.json'
content_hash: 'sha256:69bbc1e3549d06a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainerSchemaInitializationOptions](../nspersistentcloudkitcontainerschemainitializationoptions.md)

# dryRun

<sub>Type Property</sub>

A flag that indicates the container validates the model and generates the records, but doesn’t upload them to CloudKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var dryRun: NSPersistentCloudKitContainerSchemaInitializationOptions { get }
```

## Discussion

This option is useful for unit testing to ensure your managed object model is valid for use with CloudKit.

## See Also

### Constants

- [NSPersistentCloudKitContainerSchemaInitializationOptionsPrintSchema](printschema.md) — Prints the generated records to the console.
