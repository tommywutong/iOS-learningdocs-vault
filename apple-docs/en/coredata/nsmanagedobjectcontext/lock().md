---
title: lock()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nsmanagedobjectcontext/lock()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/lock()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/lock%28%29.json'
content_hash: 'sha256:bcb9b215e946d400'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# lock()

<sub>Instance Method</sub>

Attempts to acquire a lock on the context.

> [!warning] Deprecated
> Use a queue style context and -performBlockAndWait: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func lock()
```

## Discussion

This method blocks a thread’s execution until the lock can be acquired. An application protects a critical section of code by requiring a thread to acquire a lock before executing the code. Once the critical section is past, the thread relinquishes the lock by invoking [- unlock](<unlock().md>).

Sending this message to a managed object context helps the framework to understand the scope of a transaction in a multi-threaded environment. It is preferable to use the `NSManagedObjectContext`’s implementation of `NSLocking` instead using of a separate mutex object.

If you lock (or successfully `tryLock`) a managed object context, the thread in which the lock call is made must keep a strong reference to the context until it invokes unlock, otherwise if the context is deallocated this will result in deadlock.

## See Also

### Deprecated instance methods

- [- initWithConcurrencyType:](<init(concurrencytype_).md>) — Creates a context that uses the specified concurrency type. _(deprecated)_
- [- init](<init().md>) _(deprecated)_
- [- tryLock](<trylock().md>) — Attempts to acquire a lock. _(deprecated)_
- [- unlock](<unlock().md>) — Relinquishes a previously acquired lock. _(deprecated)_
