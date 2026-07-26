---
title: tryCancel()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandbuffer/trycancel()
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/trycancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/trycancel%28%29.json'
content_hash: 'sha256:e81319f12b6eae13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# tryCancel()

<sub>Instance Method</sub>

Submits a request to abandon a command buffer the queue is currently running.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func tryCancel()
```

## Discussion

Check the command buffer’s [status](status.md) property after it completes, either after [- waitUntilCompleted](<waituntilcompleted().md>) or in one of your completion handlers (see [- addCompletedHandler:](<addcompletedhandler(__).md>)).
