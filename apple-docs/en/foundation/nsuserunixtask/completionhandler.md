---
title: NSUserUnixTask.CompletionHandler
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserunixtask/completionhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsuserunixtask/completionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserunixtask/completionhandler.json'
content_hash: 'sha256:6adae4f5ea4e3ea3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserUnixTask](../nsuserunixtask.md)

# NSUserUnixTask.CompletionHandler

<sub>Type Alias</sub>

Implement this block to retrieve an error from the Unix scripted executed by [- executeWithArguments:completionHandler:](<execute(witharguments_completionhandler_).md>).

<sub>macOS</sub>

```swift
typealias CompletionHandler = @Sendable ((any Error)?) -> Void
```
