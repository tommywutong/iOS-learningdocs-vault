---
title: tryLock()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nsmanagedobjectcontext/trylock()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/trylock()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/trylock%28%29.json'
content_hash: 'sha256:210417f4f5c2d15e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# tryLock()

<sub>Instance Method</sub>

Attempts to acquire a lock.

> [!warning] Deprecated
> Use a queue style context and -performBlock: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func tryLock() -> Bool
```

## Return Value

[true](../../swift/true.md) if a lock was acquired, [false](../../swift/false.md) otherwise.

## Discussion

This method returns immediately after the attempt to acquire a lock.

## See Also

### Deprecated instance methods

- [- initWithConcurrencyType:](<init(concurrencytype_).md>) — Creates a context that uses the specified concurrency type. _(deprecated)_
- [- init](<init().md>) _(deprecated)_
- [- lock](<lock().md>) — Attempts to acquire a lock on the context. _(deprecated)_
- [- unlock](<unlock().md>) — Relinquishes a previously acquired lock. _(deprecated)_
