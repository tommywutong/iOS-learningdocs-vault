---
title: 'init(initialState:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osallocatedunfairlock/init(initialstate:)'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/init(initialstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/init%28initialstate%3A%29.json'
content_hash: 'sha256:b8b1ea93a1581fde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# init(initialState:)

<sub>Initializer</sub>

Creates a lock object that maintains and protects state data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(initialState: State)
```

## Parameters

- `initialState` — The starting state of the operation.

## See Also

### Creating a lock object

- [init()](<init().md>) — Creates a lock object that doesn’t protect state data.
