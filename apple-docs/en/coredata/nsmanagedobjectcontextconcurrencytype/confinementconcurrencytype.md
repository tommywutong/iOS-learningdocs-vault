---
title: NSManagedObjectContextConcurrencyType.confinementConcurrencyType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 3.0+（9.0 起废弃）, iPadOS 3.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.11 起废弃）, tvOS（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype.json'
content_hash: 'sha256:bdd4f9956ef4956d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContextConcurrencyType](../nsmanagedobjectcontextconcurrencytype.md)

# NSManagedObjectContextConcurrencyType.confinementConcurrencyType

<sub>Case</sub>

Specifies that the context will use the thread confinement pattern.

> [!warning] Deprecated
> Use another NSManagedObjectContextConcurrencyType

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case confinementConcurrencyType
```

## See Also

### Concurrency Types

- [NSPrivateQueueConcurrencyType](privatequeueconcurrencytype.md) — Specifies that the context will be associated with a private dispatch queue.
- [NSMainQueueConcurrencyType](mainqueueconcurrencytype.md) — Specifies that the context will be associated with the main queue.
