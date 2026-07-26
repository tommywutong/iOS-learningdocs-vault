---
title: 'present(_:atTime:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/present(_:attime:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:attime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/present%28_%3Aattime%3A%29.json'
content_hash: 'sha256:c51799fa6cc6a0f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# present(_:atTime:)

<sub>Instance Method</sub>

Presents a drawable at a specific time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func present(_ drawable: any MTLDrawable, atTime presentationTime: CFTimeInterval)
```

## Parameters

- `drawable` — An [MTLDrawable](../mtldrawable.md) instance that contains a texture the system can show on a display.

- `presentationTime` — The Mach absolute time, in seconds, that you want to present the drawable.

## Discussion

This convenience method calls the drawable’s [- presentAtTime:](<../mtldrawable/present(at_).md>) method after the command queue schedules the command buffer for execution. The command buffer does this by adding a completion handler by calling its own [- addScheduledHandler:](<addscheduledhandler(__).md>) method for you.

> [!important] Important
> You can only call this method before calling the command buffer’s [- commit](<commit().md>) method.

## See Also

### Presenting a drawable

- [- presentDrawable:](<present(__).md>) — Presents a drawable as early as possible.
- [- presentDrawable:afterMinimumDuration:](<present(__afterminimumduration_).md>) — Presents a drawable after the system presents the previous drawable for an amount of time.
