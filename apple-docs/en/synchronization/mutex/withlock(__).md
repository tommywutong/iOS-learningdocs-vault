---
title: 'withLock(_:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/mutex/withlock(_:)'
source_url: 'https://developer.apple.com/documentation/synchronization/mutex/withlock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/mutex/withlock%28_%3A%29.json'
content_hash: 'sha256:594825c46a333aba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Mutex](../mutex.md)

# withLock(_:)

<sub>Instance Method</sub>

Calls the given closure after acquiring the lock and then releases ownership.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
borrowing func withLock<Result, E>(_ body: (inout sending Value) throws(E) -> sending Result) throws(E) -> sending Result where E : Error, Result : ~Copyable
```

## Parameters

- `body` — A closure with a parameter of `Value` that has exclusive access to the value being stored within this mutex. This closure is considered the critical section as it will only be executed once the calling thread has acquired the lock.

## Return Value

The return value, if any, of the `body` closure parameter.

## Discussion

This method is equivalent to the following sequence of code:

```swift
mutex.lock()
defer {
  mutex.unlock()
}
return try body(&value)
```

> [!warning] Warning
> Recursive calls to `withLock` within the closure parameter has behavior that is platform dependent. Some platforms may choose to panic the process, deadlock, or leave this behavior unspecified. This will never reacquire the lock however.
