---
title: 'layer:shouldInheritContentsScale:fromWindow:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/layer:shouldinheritcontentsscale:fromwindow:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/layer:shouldinheritcontentsscale:fromwindow:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/layer%3Ashouldinheritcontentsscale%3Afromwindow%3A.json'
content_hash: 'sha256:c2154c5d7983804a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# layer:shouldInheritContentsScale:fromWindow:

<sub>Instance Method</sub>

Invoked when a resolution changes occurs for the window that hosts the layer.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) layer:(CALayer *) layer shouldInheritContentsScale:(CGFloat) newScale fromWindow:(NSWindow *) window;
```

## Parameters

- `layer` — The layer whose scale and content might need updating.

- `newScale` — The new scale of the window.

- `window` — The window that hosts the layer.

## Return Value

A Boolean value that specifies whether to change the layer’s `contentsScale` property.

## Discussion

When a resolution change occurs for a given window, the system traverses the layer trees in that window to decide what action, if any, to take for each layer. The system queries the layer’s delegate to determine whether to change the layer’s `contentsScale` property to the new scale (either `2.0` or `1.0`).

Note that you don’t need to manage [NSImage](../../appkit/nsimage.md) contents and that this method is not called on the delegate of a layer whose content is an [NSImage](../../appkit/nsimage.md) object.

If the delegate returns [YES](../yes.md), it should make any corresponding changes to the layer’s properties, as required by the resolution change. For example, a layer whose contents contain a CGImage object needs to determine whether an alternate CGImage object is available for the new scale factor. If the delegate finds a suitable CGImage object, then in addition to returning [YES](../yes.md), it should set the appropriate CGImage object as the layer’s new contents.
