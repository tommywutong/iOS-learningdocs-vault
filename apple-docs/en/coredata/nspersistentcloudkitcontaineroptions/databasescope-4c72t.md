---
title: databaseScope
framework: CoreData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontaineroptions/databasescope-4c72t
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontaineroptions/databasescope-4c72t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontaineroptions/databasescope-4c72t.json'
content_hash: 'sha256:d51dbc20941178e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainerOptions](../nspersistentcloudkitcontaineroptions.md)

# databaseScope

<sub>Instance Property</sub>

The database scope — public, private, or shared — to use for a specified store in a persistent CloudKit container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var databaseScope: CKDatabase.Scope { get set }
```

## See Also

### Creating Container Options

- [- initWithContainerIdentifier:](<init(containeridentifier_).md>) — Initializes container options using the given CloudKit container identifier.
- [containerIdentifier](containeridentifier.md) — The identifier of the CloudKit container associated with a given store description.
