---
title: NSManagedObjectContextConcurrencyType.mainQueueConcurrencyType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype.json'
content_hash: 'sha256:3aa4e535bb221b76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContextConcurrencyType](../nsmanagedobjectcontextconcurrencytype.md)

# NSManagedObjectContextConcurrencyType.mainQueueConcurrencyType

<sub>Case</sub>

Specifies that the context will be associated with the main queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case mainQueueConcurrencyType
```

## See Also

### Concurrency Types

- [NSPrivateQueueConcurrencyType](privatequeueconcurrencytype.md) — Specifies that the context will be associated with a private dispatch queue.
- [NSConfinementConcurrencyType](confinementconcurrencytype.md) — Specifies that the context will use the thread confinement pattern. _(deprecated)_
