---
title: 'init(value:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsemaphore/init(value:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsemaphore/init(value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsemaphore/init%28value%3A%29.json'
content_hash: 'sha256:75050ed9f9c9c5b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSemaphore](../dispatchsemaphore.md)

# init(value:)

<sub>Initializer</sub>

Creates new counting semaphore with an initial value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(value: Int)
```

## Parameters

- `value` — The starting value for the semaphore. Do not pass a value less than zero.

## Return Value

The newly created semaphore.

## Discussion

Passing zero for the value is useful for when two threads need to reconcile the completion of a particular event. Passing a value greater than zero is useful for managing a finite pool of resources, where the pool size is equal to the value.

> [!important] Important
> Calls to [signal()](<signal().md>) must be balanced with calls to [wait()](<wait().md>). Attempting to dispose of a semaphore with a count lower than `value` causes an `EXC_BAD_INSTRUCTION` exception.
