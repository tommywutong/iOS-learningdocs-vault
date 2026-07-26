---
title: NSUserAppleScriptTask.CompletionHandler
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuserapplescripttask/completionhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsuserapplescripttask/completionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserapplescripttask/completionhandler.json'
content_hash: 'sha256:59bac78fa01e6276'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserAppleScriptTask](../nsuserapplescripttask.md)

# NSUserAppleScriptTask.CompletionHandler

<sub>Type Alias</sub>

Implement this block to retrieve the result of the AppleScript executed by [- executeWithAppleEvent:completionHandler:](<execute(withappleevent_completionhandler_).md>).

<sub>macOS</sub>

```swift
typealias CompletionHandler = @Sendable (NSAppleEventDescriptor?, (any Error)?) -> Void
```
