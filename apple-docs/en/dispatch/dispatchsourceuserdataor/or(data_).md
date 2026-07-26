---
title: 'or(data:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsourceuserdataor/or(data:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceuserdataor/or(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceuserdataor/or%28data%3A%29.json'
content_hash: 'sha256:ee160423efe3846b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceUserDataOr](../dispatchsourceuserdataor.md)

# or(data:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func or(data: UInt)
```

## Parameters

- `data` — The value you want to merge with the existing data in the dispatch source. The dispatch source ORs this value with the currently pending data.

## Discussion

After you call this method, the dispatch source submits its event handler to its target queue to process the data. If you specify `0` for the data parameter, the dispatch source does not submit its event hander for execution.
