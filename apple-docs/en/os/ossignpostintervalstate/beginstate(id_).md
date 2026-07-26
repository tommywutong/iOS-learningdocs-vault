---
title: 'beginState(id:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignpostintervalstate/beginstate(id:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostintervalstate/beginstate(id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostintervalstate/beginstate%28id%3A%29.json'
content_hash: 'sha256:435bcb72f24f0665'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignpostIntervalState](../ossignpostintervalstate.md)

# beginState(id:)

<sub>Type Method</sub>

Recreates interval state from the specified signpost ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func beginState(id: OSSignpostID) -> OSSignpostIntervalState
```

## Parameters

- `id` — The signpost ID you use to begin the signposted interval.

## Return Value

The recreated interval state.

## Discussion

> [!important] Important
> Recreating interval state to end a signposted interval bypasses runtime assertions that check for consistency between the beginning and the end of the interval.
