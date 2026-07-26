---
title: dispatch_data_get_size
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_data_get_size
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_data_get_size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_data_get_size.json'
content_hash: 'sha256:0f8a825b965c92a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_data_get_size

<sub>Function</sub>

Returns the logical size of the memory managed by a dispatch data object

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern size_t dispatch_data_get_size(dispatch_data_t data);
```

## Parameters

- `data` — The dispatch data object to query

## Return Value

The number of bytes represented by the data object.

## Discussion

For data objects that represent multiple noncontiguous memory regions, the size reported by this function is the sum of the sizes of the individual regions.
