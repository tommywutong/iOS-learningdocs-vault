---
title: 'controlTextDidEndEditing:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/controltextdidendediting:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/controltextdidendediting:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/controltextdidendediting%3A.json'
content_hash: 'sha256:f15bc55a2ed0bcdb'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# controlTextDidEndEditing:

<sub>实例方法</sub>

当带有可编辑文本的控件结束编辑会话时发送。

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) controlTextDidEndEditing:(NSNotification *) obj;
```

## 参数

- `obj` — 通知对象。通知名称始终为 [textDidEndEditingNotification](../../appkit/nscontrol/textdidendeditingnotification.md)。

## 讨论

当用户停止在文本字段或表单等控件中编辑文本时调用此方法。控件会发送 [textDidEndEditingNotification](../../appkit/nscontrol/textdidendeditingnotification.md) 通知，如果控件的委托实现了此方法，则会自动注册以接收该通知。使用键 `@"NSFieldEditor"` 从通知对象的 `userInfo` 字典中获取字段编辑器。

> [!warning] 警告
> 在某些情况下（例如在 `NSOutlineView` 实例中编辑时），可能会在未先调用 [controlTextDidBeginEditing:](controltextdidbeginediting_.md) 的情况下调用此方法。只有用户实际输入内容时，你才会收到 `controlTextDidBeginEditing:` 通知；但如果用户只是双击字段然后在字段外点按而未输入，你仍可能收到 `controlTextDidEndEditing:` 通知。
