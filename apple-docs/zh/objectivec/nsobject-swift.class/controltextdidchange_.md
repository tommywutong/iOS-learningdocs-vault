---
title: 'controlTextDidChange:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/controltextdidchange:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/controltextdidchange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/controltextdidchange%3A.json'
content_hash: 'sha256:4eb14eb9168cc6b7'
translated: true
---
> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# controlTextDidChange:

<sub>实例方法</sub>

当接收控件中的文本更改时发送。

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) controlTextDidChange:(NSNotification *) obj;
```

## 参数

- `obj` — 通知对象。通知名称始终为 [textDidChangeNotification](../../appkit/nscontrol/textdidchangenotification.md)。

## 讨论

当文本字段或表单等控件中的文本更改时调用此方法。控件会发送 [textDidChangeNotification](../../appkit/nscontrol/textdidchangenotification.md) 通知，如果控件的委托实现了此方法，则会自动注册以接收该通知。使用键 `@"NSFieldEditor"` 从通知对象的 `userInfo` 字典中获取字段编辑器。
