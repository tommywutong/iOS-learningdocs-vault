---
title: databaseScope
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontaineroptions/databasescope-2784h
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontaineroptions/databasescope-2784h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontaineroptions/databasescope-2784h.json'
content_hash: 'sha256:1fdad697641fa045'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainerOptions](../nspersistentcloudkitcontaineroptions.md)

# databaseScope

<sub>Instance Property</sub>

The database scope — public, private, or shared — to use for a specified store in a persistent CloudKit container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CKDatabaseScope databaseScope;
```

## See Also

### Creating Container Options

- [- initWithContainerIdentifier:](<init(containeridentifier_).md>) — Initializes container options using the given CloudKit container identifier.
- [containerIdentifier](containeridentifier.md) — The identifier of the CloudKit container associated with a given store description.
