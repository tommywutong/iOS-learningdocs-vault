---
title: waitUntilCompleted()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/waituntilcompleted()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/waituntilcompleted()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/waituntilcompleted%28%29.json'
content_hash: 'sha256:4de0294b5af57769'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# waitUntilCompleted()

<sub>Instance Method</sub>

Blocks the current thread until the GPU finishes executing the command buffer and all of its completion handlers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func waitUntilCompleted()
```

## See Also

### Waiting for state changes

- [- waitUntilScheduled](<waituntilscheduled().md>) — Blocks the current thread until the command queue schedules the buffer.
