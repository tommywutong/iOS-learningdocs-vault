---
title: 'setSpecific(key:value:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/setspecific(key:value:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/setspecific(key:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/setspecific%28key%3Avalue%3A%29.json'
content_hash: 'sha256:21e63c4599bf3a09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# setSpecific(key:value:)

<sub>Instance Method</sub>

Sets the key/value data for the specified dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func setSpecific<T>(key: DispatchSpecificKey<T>, value: T?) where T : Sendable
```

## Parameters

- `key` — The key that you use to identify the data.

- `value` — The data you want to associate with the queue.

## See Also

### Getting and Setting Contextual Data

- [getSpecific(key:)](<getspecific(key_)-swift.method.md>) — Returns the value for the key associated with this dispatch queue.
- [getSpecific(key:)](<getspecific(key_)-swift.type.method.md>) — Returns the value for the key associated with the current execution context.
- [DispatchSpecificKey](../dispatchspecifickey.md) — A key associated with a specific contextual value on a dispatch queue.
