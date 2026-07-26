---
title: perform()
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchworkitem/perform()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitem/perform()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitem/perform%28%29.json'
content_hash: 'sha256:ccf4005939aa84b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItem](../dispatchworkitem.md)

# perform()

<sub>Instance Method</sub>

Executes the work item’s block synchronously on the current thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform()
```

## Discussion

This method executes the work item’s block immediately on the current thread.
