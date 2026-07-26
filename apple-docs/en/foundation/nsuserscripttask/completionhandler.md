---
title: NSUserScriptTask.CompletionHandler
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserscripttask/completionhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsuserscripttask/completionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserscripttask/completionhandler.json'
content_hash: 'sha256:9e0c9b5f46390f00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserScriptTask](../nsuserscripttask.md)

# NSUserScriptTask.CompletionHandler

<sub>Type Alias</sub>

Implement this block to retrieve the error of the script executed by [- executeWithCompletionHandler:](<execute(completionhandler_).md>).

<sub>macOS</sub>

```swift
typealias CompletionHandler = @Sendable ((any Error)?) -> Void
```
