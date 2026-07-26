---
title: present()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldrawable/present()
source_url: 'https://developer.apple.com/documentation/metal/mtldrawable/present()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldrawable/present%28%29.json'
content_hash: 'sha256:d572436f41cbb91c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDrawable](../mtldrawable.md)

# present()

<sub>Instance Method</sub>

Presents the drawable onscreen as soon as possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func present()
```

## Discussion

When a command queue schedules a command buffer for execution, it tracks whether any commands in that command buffer need to render or write to the drawable object. When you call this method, the drawable presents its contents as soon as possible after all scheduled render or write requests for that drawable are complete.

> [!note] Note
> To avoid presenting a drawable before any work is scheduled, or to avoid holding on to a drawable longer than necessary, call a command buffer’s [- presentDrawable:](<../mtlcommandbuffer/present(__).md>) method instead of this method. The [- presentDrawable:](<../mtlcommandbuffer/present(__).md>) method is a convenience method that calls the drawable’s [- present](<present().md>) method after the command queue schedules that command buffer for execution.

## See Also

### Presenting the drawable

- [- presentAfterMinimumDuration:](<present(afterminimumduration_).md>) — Presents the drawable onscreen as soon as possible after a previous drawable is visible for the specified duration.
- [- presentAtTime:](<present(at_).md>) — Presents the drawable onscreen at a specific host time.
