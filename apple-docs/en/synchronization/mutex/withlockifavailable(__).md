---
title: 'withLockIfAvailable(_:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/mutex/withlockifavailable(_:)'
source_url: 'https://developer.apple.com/documentation/synchronization/mutex/withlockifavailable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/mutex/withlockifavailable%28_%3A%29.json'
content_hash: 'sha256:4bc70f29023f703f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Mutex](../mutex.md)

# withLockIfAvailable(_:)

<sub>Instance Method</sub>

Attempts to acquire the lock and then calls the given closure if successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
borrowing func withLockIfAvailable<Result, E>(_ body: (inout sending Value) throws(E) -> sending Result) throws(E) -> sending Result? where E : Error, Result : ~Copyable
```

## Parameters

- `body` — A closure with a parameter of `Value` that has exclusive access to the value being stored within this mutex. This closure is considered the critical section as it will only be executed if the calling thread acquires the lock.

## Return Value

The return value, if any, of the `body` closure parameter or `nil` if the lock couldn’t be acquired.

## Discussion

If the calling thread was successful in acquiring the lock, the closure will be executed and then immediately after it will release ownership of the lock. If we were unable to acquire the lock, this will return `nil`.

This method is equivalent to the following sequence of code:

```swift
guard mutex.tryLock() else {
  return nil
}
defer {
  mutex.unlock()
}
return try body(&value)
```

> [!note] Note
> This function cannot spuriously fail to acquire the lock. The behavior of similar functions in other languages (such as C’s `mtx_trylock()`) is platform-dependent and may differ from Swift’s behavior.
