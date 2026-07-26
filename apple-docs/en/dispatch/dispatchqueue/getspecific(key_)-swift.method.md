---
title: 'getSpecific(key:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/getspecific(key:)-swift.method'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/getspecific(key:)-swift.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/getspecific%28key%3A%29-swift.method.json'
content_hash: 'sha256:f2641a701bea869c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# getSpecific(key:)

<sub>Instance Method</sub>

Returns the value for the key associated with this dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func getSpecific<T>(key: DispatchSpecificKey<T>) -> T? where T : Sendable
```

## Parameters

- `key` — The key associated with the dispatch queue.

## See Also

### Getting and Setting Contextual Data

- [setSpecific(key:value:)](<setspecific(key_value_).md>) — Sets the key/value data for the specified dispatch queue.
- [getSpecific(key:)](<getspecific(key_)-swift.type.method.md>) — Returns the value for the key associated with the current execution context.
- [DispatchSpecificKey](../dispatchspecifickey.md) — A key associated with a specific contextual value on a dispatch queue.
