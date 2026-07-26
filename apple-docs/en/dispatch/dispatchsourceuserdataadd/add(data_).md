---
title: 'add(data:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsourceuserdataadd/add(data:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceuserdataadd/add(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceuserdataadd/add%28data%3A%29.json'
content_hash: 'sha256:49a6ab8ecd538db4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceUserDataAdd](../dispatchsourceuserdataadd.md)

# add(data:)

<sub>Instance Method</sub>

Adds the value to the current pending data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func add(data: UInt)
```

## Parameters

- `data` — The value you want to add the dispatch source.

## Discussion

After you call this method, the dispatch source submits its event handler to its target queue to process the data. If you specify `0` for the data parameter, the dispatch source does not submit its event hander for execution.
