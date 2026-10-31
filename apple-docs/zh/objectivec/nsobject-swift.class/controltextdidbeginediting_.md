---
title: 'controlTextDidBeginEditing:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/controltextdidbeginediting:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/controltextdidbeginediting:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/controltextdidbeginediting%3A.json'
content_hash: 'sha256:e3b691380cd9052a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# controlTextDidBeginEditing:

<sub>实例方法</sub>

当带有可编辑文本的控件开始编辑会话时发送。

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) controlTextDidBeginEditing:(NSNotification *) obj;
```

## 参数

- `obj` — 通知对象。通知名称始终为 [textDidBeginEditingNotification](../../appkit/nscontrol/textdidbegineditingnotification.md)。

## 讨论

当用户开始在文本字段或表单字段等控件中编辑文本时调用此方法。控件会发送 [textDidBeginEditingNotification](../../appkit/nscontrol/textdidbegineditingnotification.md) 通知，如果控件的委托实现了此方法，则会自动注册以接收该通知。使用键 `@"NSFieldEditor"` 从通知对象的 `userInfo` 字典中获取字段编辑器。

有关为何不一定每次调用 [controlTextDidEndEditing:](controltextdidendediting_.md) 都会对应一次 [controlTextDidBeginEditing:](controltextdidbeginediting_.md) 调用的说明，请参阅 [controlTextDidEndEditing:](controltextdidendediting_.md)。
