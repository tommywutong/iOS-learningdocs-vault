---
title: NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.json'
content_hash: 'sha256:fd1529e1534eb89b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContextConcurrencyType](../nsmanagedobjectcontextconcurrencytype.md)

# NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType

<sub>Case</sub>

Specifies that the context will be associated with a private dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case privateQueueConcurrencyType
```

## See Also

### Concurrency Types

- [NSMainQueueConcurrencyType](mainqueueconcurrencytype.md) — Specifies that the context will be associated with the main queue.
- [NSConfinementConcurrencyType](confinementconcurrencytype.md) — Specifies that the context will use the thread confinement pattern. _(deprecated)_
