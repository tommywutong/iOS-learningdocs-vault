---
title: 'present(_:afterMinimumDuration:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/present(_:afterminimumduration:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:afterminimumduration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/present%28_%3Aafterminimumduration%3A%29.json'
content_hash: 'sha256:b7a92cc4e509b3cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# present(_:afterMinimumDuration:)

<sub>Instance Method</sub>

Presents a drawable after the system presents the previous drawable for an amount of time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func present(_ drawable: any MTLDrawable, afterMinimumDuration duration: CFTimeInterval)
```

## Parameters

- `drawable` — An [MTLDrawable](../mtldrawable.md) instance that contains a texture the system can show on a display.

- `duration` — The shortest display time you want the system to give to the previous drawable before presenting this one.

## Discussion

This convenience method calls the drawable’s [- presentAfterMinimumDuration:](<../mtldrawable/present(afterminimumduration_).md>) method after the command queue schedules the command buffer for execution. The command buffer does this by adding a completion handler by calling its own [- addScheduledHandler:](<addscheduledhandler(__).md>) method for you.

> [!important] Important
> You can only call this method before calling the command buffer’s [- commit](<commit().md>) method.

## See Also

### Presenting a drawable

- [- presentDrawable:](<present(__).md>) — Presents a drawable as early as possible.
- [- presentDrawable:atTime:](<present(__attime_).md>) — Presents a drawable at a specific time.
