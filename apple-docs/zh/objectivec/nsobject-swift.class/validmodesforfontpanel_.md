---
title: 'validModesForFontPanel:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/validmodesforfontpanel:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validmodesforfontpanel:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/validmodesforfontpanel%3A.json'
content_hash: 'sha256:bf0a1743814f4abf'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# validModesForFontPanel:

<sub>实例方法</sub>

返回对应于预期字体面板模式的模式掩码。

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSFontPanelModeMask) validModesForFontPanel:(NSFontPanel *) fontPanel;
```

## 讨论

模式掩码在 [Mode Masks](../../appkit/mode-masks.md) 中定义。

字体面板可通过让目标响应 [validModesForFontPanel:](validmodesforfontpanel_.md) 来隐藏给定上下文中不适用的元素。若目标需要标准模式掩码以外的字体面板模式，则必须响应此方法。

此消息会沿响应者链向上发送，直至找到实现该方法的第一个响应者。理想情况下，该对象应是找到的同时实现 [changeFont:](changefont_.md) 的第一个响应者。
