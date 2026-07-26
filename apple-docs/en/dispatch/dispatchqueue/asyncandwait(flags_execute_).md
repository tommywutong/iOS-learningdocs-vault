---
title: 'asyncAndWait(flags:execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/asyncandwait(flags:execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncandwait(flags:execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/asyncandwait%28flags%3Aexecute%3A%29.json'
content_hash: 'sha256:5efe4d4175b56a84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# asyncAndWait(flags:execute:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func asyncAndWait<T>(flags: DispatchWorkItemFlags, execute work: () throws -> T) rethrows -> T
```
