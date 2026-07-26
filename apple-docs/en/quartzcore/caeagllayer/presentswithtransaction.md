---
title: presentsWithTransaction
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（12.0 起废弃）, iPadOS 9.0+（12.0 起废弃）, tvOS 9.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/quartzcore/caeagllayer/presentswithtransaction
source_url: 'https://developer.apple.com/documentation/quartzcore/caeagllayer/presentswithtransaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caeagllayer/presentswithtransaction.json'
content_hash: 'sha256:4389a388d5e8a6b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEAGLLayer](../caeagllayer.md)

# presentsWithTransaction

<sub>Instance Property</sub>

A Boolean value that determines whether the layer presents its content using a Core Animation transaction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var presentsWithTransaction: Bool { get set }
```

## Discussion

By default this value is [false](../../swift/false.md): [CAEAGLLayer](../caeagllayer.md) displays the output of a rendering pass to the display as quickly as possible and asynchronously to any Core Animation transactions. However, if your game or app combines OpenGL and Core Animation content, it’s not guaranteed that your OpenGL content will arrive in the same frame as your Core Animation content. This could be an issue if, for example, your app draws [UIKit](https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-6_1/index.html#//apple_ref/doc/uid/TP40012869-CH1-SW17) content (such as labels with a target position and time) over the top of your [CAEAGLLayer](../caeagllayer.md) and the two domains need to be synchronized.

Setting this value to [true](../../swift/true.md) changes this default behavior so that your [CAEAGLLayer](../caeagllayer.md) displays its drawable content synchronously, using whichever Core Animation transaction is current.

.

## See Also

### Accessing the Layer Properties

- [drawableProperties](../../opengles/eagldrawable/drawableproperties.md) — A dictionary of values that specify the desired characteristics of the drawable surface. _(deprecated)_
