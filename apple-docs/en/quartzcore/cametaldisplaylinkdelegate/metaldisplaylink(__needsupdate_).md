---
title: 'metalDisplayLink(_:needsUpdate:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/cametaldisplaylinkdelegate/metaldisplaylink(_:needsupdate:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldisplaylinkdelegate/metaldisplaylink(_:needsupdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldisplaylinkdelegate/metaldisplaylink%28_%3Aneedsupdate%3A%29.json'
content_hash: 'sha256:8872fb5ce2fa57fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalDisplayLinkDelegate](../cametaldisplaylinkdelegate.md)

# metalDisplayLink(_:needsUpdate:)

<sub>Instance Method</sub>

A method the system calls to notify your app when it plans to update the display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func metalDisplayLink(_ link: CAMetalDisplayLink, needsUpdate update: CAMetalDisplayLink.Update)
```

## Parameters

- `link` — A Metal display link instance the system notifies.

- `update` — An update instance that contains the time the system intends to update the display, a [CAMetalDrawable](../cametaldrawable.md) instance, and a deadline to call its [present()](<../../metal/mtldrawable/present().md>) method.

## Discussion

In this method’s implementation, perform your app’s rendering on the [layer](../cametaldrawable/layer.md) or [texture](../cametaldrawable/texture.md) of the `update` instance’s [drawable](../cametaldisplaylink/update/drawable.md) property. Before calling [present()](<../../metal/mtldrawable/present().md>), encode all your Metal commands to the `link` parameter’s [MTLDevice](../../metal/mtldevice.md). The GPU has additional time to complete running your commands before the frame displays on screen, determined by the value of the `link` parameter’s [preferredFrameLatency](../cametaldisplaylink/preferredframelatency.md) property.

> [!warning] Warning
> Using alternative methods to [present()](<../../metal/mtldrawable/present().md>) that target the presentation for a specific time cause an assert when used with a [CAMetalDisplayLink](../cametaldisplaylink.md).
