---
title: 'present(afterMinimumDuration:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldrawable/present(afterminimumduration:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldrawable/present(afterminimumduration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldrawable/present%28afterminimumduration%3A%29.json'
content_hash: 'sha256:4b61a92e4df534fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDrawable](../mtldrawable.md)

# present(afterMinimumDuration:)

<sub>Instance Method</sub>

Presents the drawable onscreen as soon as possible after a previous drawable is visible for the specified duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func present(afterMinimumDuration duration: CFTimeInterval)
```

## Parameters

- `duration` — The previous drawable’s minimum display time, in seconds.

## Discussion

When a command queue schedules a command buffer for execution, it tracks whether any commands in that command buffer need to render or write to the drawable object. When you call this method, the drawable presents its contents at a future time when all render and write requests for that drawable are complete and a previous drawable has been visible onscreen for the specified duration. Use this method to schedule drawables at a regular interval.

> [!note] Note
> To avoid presenting a drawable before any work is scheduled, or to avoid holding on to a drawable longer than necessary, call a command buffer’s [- presentDrawable:afterMinimumDuration:](<../mtlcommandbuffer/present(__afterminimumduration_).md>) method instead. The [- presentDrawable:afterMinimumDuration:](<../mtlcommandbuffer/present(__afterminimumduration_).md>) method is a convenience method that calls the given drawable’s [- presentAfterMinimumDuration:](<present(afterminimumduration_).md>) method after the command queue schedules that command buffer for execution.

## See Also

### Presenting the drawable

- [- present](<present().md>) — Presents the drawable onscreen as soon as possible.
- [- presentAtTime:](<present(at_).md>) — Presents the drawable onscreen at a specific host time.
