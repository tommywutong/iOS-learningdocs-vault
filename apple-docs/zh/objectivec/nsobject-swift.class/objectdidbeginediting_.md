---
title: 'objectDidBeginEditing:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/objectdidbeginediting:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/objectdidbeginediting:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/objectdidbeginediting%3A.json'
content_hash: 'sha256:98e7bf0d999cc173'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# objectDidBeginEditing:

<sub>实例方法</sub>

当 `editor` 有可能影响接收者的未提交更改时，应向接收者发送此消息。

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) objectDidBeginEditing:(id<NSEditor>) editor;
```

## 另请参阅

### 相关文档

- [Cocoa Bindings Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i)
- [objectDidEndEditing:](objectdidendediting_.md) — 当 `editor` 完成编辑属于接收者的属性时，应向接收者发送此消息。 _(已废弃)_
