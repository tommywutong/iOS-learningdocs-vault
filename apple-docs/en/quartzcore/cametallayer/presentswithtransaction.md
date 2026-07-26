---
title: presentsWithTransaction
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/presentswithtransaction
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/presentswithtransaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/presentswithtransaction.json'
content_hash: 'sha256:b08b5b010b7da79f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# presentsWithTransaction

<sub>Instance Property</sub>

A Boolean value that determines whether the layer presents its content using a Core Animation transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var presentsWithTransaction: Bool { get set }
```

## Discussion

By default, this value is [false](../../swift/false.md); [CAMetalLayer](../cametallayer.md) displays the output of a rendering pass to the display as quickly as possible and asynchronously to any Core Animation transactions. Core Animation doesn’t guarantee that the Metal content arrives in the same frame as other Core Animation content. This behavior could be an issue if, for example, your app draws [UIKit](https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-6_1/index.html#//apple_ref/doc/uid/TP40012869-CH1-SW17) content over the top of your [CAMetalLayer](../cametallayer.md).

Setting this value to [true](../../swift/true.md) makes the layer draw its contents synchronously, using whichever Core Animation transaction is current at the time you call the drawable’s [present()](<../../metal/mtldrawable/present().md>) method. To ensure that a transaction is available when you schedule the drawable to be presented, first commit the command buffer containing your Metal rendering commands. Then, call its [waitUntilScheduled()](<../../metal/mtlcommandbuffer/waituntilscheduled().md>) method to synchronously wait until the command queue schedules the command buffer to execute on the GPU. Finally, call the drawable’s [present()](<../../metal/mtldrawable/present().md>) method.

> [!warning] Warning
> If you’re synchronizing presentation with a Core Animation transaction, don’t use the [present(_:)](<../../metal/mtlcommandbuffer/present(__).md>) method on the command buffer to schedule the drawable for presentation. This convenience method (and any variant of it on [MTLCommandBuffer](../../metal/mtlcommandbuffer.md)) doesn’t wait for a transaction to be available.

## See Also

### Configuring Presentation Behavior

- [displaySyncEnabled](displaysyncenabled.md) — A Boolean value that determines whether the layer synchronizes its updates to the display’s refresh rate.
