---
title: 'present(at:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldrawable/present(at:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldrawable/present(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldrawable/present%28at%3A%29.json'
content_hash: 'sha256:85c86b693bfd0ff4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDrawable](../mtldrawable.md)

# present(at:)

<sub>Instance Method</sub>

Presents the drawable onscreen at a specific host time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func present(at presentationTime: CFTimeInterval)
```

## Parameters

- `presentationTime` — The Mach absolute time at which the drawable should be presented, in seconds.

## Discussion

When a command queue schedules a command buffer for execution, it tracks whether any commands in that command buffer need to render or write to the drawable object. When you call this method, the drawable waits until all render and write requests for that drawable are complete. If they complete prior to the specified time, the drawable presents the content at that time. If the commands complete after the presentation time, the drawable presents its contents as soon as possible.

> [!note] Note
> To avoid presenting a drawable before any work is scheduled, or to avoid holding on to a drawable longer than necessary, call a command buffer’s [- presentDrawable:atTime:](<../mtlcommandbuffer/present(__attime_).md>) method instead of a drawable’s [- presentAtTime:](<present(at_).md>) method. The [- presentDrawable:atTime:](<../mtlcommandbuffer/present(__attime_).md>) method is a convenience method that calls the given drawable’s [- presentAtTime:](<present(at_).md>) method after the command queue schedules that command buffer for execution.

## See Also

### Presenting the drawable

- [- present](<present().md>) — Presents the drawable onscreen as soon as possible.
- [- presentAfterMinimumDuration:](<present(afterminimumduration_).md>) — Presents the drawable onscreen as soon as possible after a previous drawable is visible for the specified duration.
