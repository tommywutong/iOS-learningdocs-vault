---
title: NSUserAutomatorTask.CompletionHandler
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserautomatortask/completionhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsuserautomatortask/completionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserautomatortask/completionhandler.json'
content_hash: 'sha256:7a45fc5755f7d414'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserAutomatorTask](../nsuserautomatortask.md)

# NSUserAutomatorTask.CompletionHandler

<sub>Type Alias</sub>

Implement this block to retrieve the output of the Automator workflow executed by [- executeWithInput:completionHandler:](<execute(withinput_completionhandler_).md>).

<sub>macOS</sub>

```swift
typealias CompletionHandler = @Sendable (Any?, (any Error)?) -> Void
```
