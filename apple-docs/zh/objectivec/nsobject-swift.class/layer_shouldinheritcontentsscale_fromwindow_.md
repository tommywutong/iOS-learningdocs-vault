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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# layer:shouldInheritContentsScale:fromWindow:

<sub>实例方法</sub>

当承载该图层的窗口发生分辨率更改时调用。

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) layer:(CALayer *) layer shouldInheritContentsScale:(CGFloat) newScale fromWindow:(NSWindow *) window;
```

## 参数

- `layer` — 其缩放和内容可能需要更新的图层。

- `newScale` — 窗口的新缩放比例。

- `window` — 承载该图层的窗口。

## 返回值

指定是否更改图层的 `contentsScale` 属性的布尔值。

## 讨论

当给定窗口发生分辨率更改时，系统会遍历该窗口中的图层树，以决定对每个图层采取何种操作（如有）。系统会查询图层的委托，以确定是否将图层的 `contentsScale` 属性更改为新的缩放比例（`2.0` 或 `1.0`）。

请注意，你无需管理 [NSImage](../../appkit/nsimage.md) 内容，并且对于内容为 [NSImage](../../appkit/nsimage.md) 对象的图层，不会对其委托调用此方法。

若委托返回 [YES](../yes.md)，则应根据分辨率更改对图层属性进行相应更改。例如，内容包含 CGImage 对象的图层需要确定是否有适用于新缩放因子的备用 CGImage 对象。若委托找到合适的 CGImage 对象，则除返回 [YES](../yes.md) 外，还应将该 CGImage 对象设置为图层的新内容。
