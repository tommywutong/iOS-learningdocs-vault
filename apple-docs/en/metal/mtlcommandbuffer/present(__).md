---
title: 'present(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/present(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/present%28_%3A%29.json'
content_hash: 'sha256:6e82de4bd9285c08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# present(_:)

<sub>Instance Method</sub>

Presents a drawable as early as possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func present(_ drawable: any MTLDrawable)
```

## Parameters

- `drawable` — An [MTLDrawable](../mtldrawable.md) instance that contains a texture the system can show on a display.

## Discussion

This convenience method calls the drawable’s [- present](<../mtldrawable/present().md>) method after the command queue schedules the command buffer for execution. The command buffer does this by adding a completion handler by calling its own [- addScheduledHandler:](<addscheduledhandler(__).md>) method for you.

> [!important] Important
> You can only call this method before calling the command buffer’s [- commit](<commit().md>) method.

## Default Implementations

### MTLCommandBuffer Implementations

- [present(_:)](<present(__)-8nfpq.md>) — Presents a texture resource drawable as early as possible.

## See Also

### Presenting a drawable

- [- presentDrawable:atTime:](<present(__attime_).md>) — Presents a drawable at a specific time.
- [- presentDrawable:afterMinimumDuration:](<present(__afterminimumduration_).md>) — Presents a drawable after the system presents the previous drawable for an amount of time.
