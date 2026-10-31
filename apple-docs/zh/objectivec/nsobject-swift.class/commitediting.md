---
title: commitEditing
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/commitediting
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/commitediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/commitediting.json'
content_hash: 'sha256:40b84cb366d056cf'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# commitEditing

<sub>实例方法</sub>

返回接收者是否能够提交任何挂起的编辑。

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) commitEditing;
```

## 返回值

如果更改已成功应用到模型，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

如果接收者未能将更改应用到模型对象（可能由于验证错误），则提交会被拒绝。

## 另请参阅

### 相关文档

- [discardEditing](discardediting.md) — 使接收者丢弃任何更改，并恢复先前的值。 _(已废弃)_
