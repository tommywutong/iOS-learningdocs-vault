---
title: 'replace(data:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsourceuserdatareplace/replace(data:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceuserdatareplace/replace(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceuserdatareplace/replace%28data%3A%29.json'
content_hash: 'sha256:eb16a9a36854bd24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceUserDataReplace](../dispatchsourceuserdatareplace.md)

# replace(data:)

<sub>Instance Method</sub>

Replaces the current pending data with the new value you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replace(data: UInt)
```

## Parameters

- `data` — The data that replaces the current pending value.

## Discussion

After you call this method, the dispatch source submits its event handler to its target queue to process the data. If you specify `0` for the data parameter, the dispatch source does not submit its event hander for execution.
