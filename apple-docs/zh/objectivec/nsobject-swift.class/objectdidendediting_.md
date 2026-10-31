---
title: 'objectDidEndEditing:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/objectdidendediting:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/objectdidendediting:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/objectdidendediting%3A.json'
content_hash: 'sha256:7188aaff6b032c37'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# objectDidEndEditing:

<sub>实例方法</sub>

当 `editor` 完成编辑属于接收者的属性时，应向接收者发送此消息。

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) objectDidEndEditing:(id<NSEditor>) editor;
```

## 另请参阅

### 相关文档

- [objectDidBeginEditing:](objectdidbeginediting_.md) — This message should be sent to the receiver when `editor` has uncommitted changes that can affect the receiver. _(已废弃)_
