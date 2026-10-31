---
title: 'changeColor:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/changecolor:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/changecolor:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/changecolor%3A.json'
content_hash: 'sha256:bb2d17131ae1e8fd'
translated: true
---
> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# changeColor:

<sub>实例方法</sub>

当用户在 `NSColorPanel` 对象中选择颜色时发送给第一响应者。

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) changeColor:(id) sender;
```

## 参数

- `sender` — 发送消息的 `NSColorPanel`。

## 讨论

当用户在 [NSColorPanel](../../appkit/nscolorpanel.md) 对象中选择颜色时，面板会尝试在第一响应者上调用此方法。你可以在任何需要响应颜色更改的响应者中重写此方法。
