---
title: 'performBackgroundTask(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcontainer/performbackgroundtask(_:)-25nok'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/performbackgroundtask(_:)-25nok'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/performbackgroundtask%28_%3A%29-25nok.json'
content_hash: 'sha256:e53cd5e6e8d83e54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# performBackgroundTask(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performBackgroundTask<T>(_ block: @escaping (NSManagedObjectContext) throws -> T) async rethrows -> T
```

## See Also

### Performing Background Tasks

- [- performBackgroundTask:](<performbackgroundtask(__)-39sch.md>) — Executes a closure on a private queue using an ephemeral managed object context.
