---
title: init()
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+（9.0 起废弃）, iPadOS 3.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.11 起废弃）, tvOS（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nsmanagedobjectcontext/init()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/init%28%29.json'
content_hash: 'sha256:94a03433e469c50d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# init()

<sub>Initializer</sub>

> [!warning] Deprecated
> Use -initWithConcurrencyType: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init()
```

## See Also

### Deprecated instance methods

- [- initWithConcurrencyType:](<init(concurrencytype_).md>) — Creates a context that uses the specified concurrency type. _(deprecated)_
- [- lock](<lock().md>) — Attempts to acquire a lock on the context. _(deprecated)_
- [- tryLock](<trylock().md>) — Attempts to acquire a lock. _(deprecated)_
- [- unlock](<unlock().md>) — Relinquishes a previously acquired lock. _(deprecated)_
