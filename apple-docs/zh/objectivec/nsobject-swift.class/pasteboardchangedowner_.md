---
title: 'pasteboardChangedOwner:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/pasteboardchangedowner:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/pasteboardchangedowner:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/pasteboardchangedowner%3A.json'
content_hash: 'sha256:9dca6cd25de03cb3'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# pasteboardChangedOwner:

<sub>实例方法</sub>

通知指定剪贴板的先前所有者（以及剪贴板上表示形式的所有者）该剪贴板已更换所有者。

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) pasteboardChangedOwner:(NSPasteboard *) sender;
```

## 参数

- `sender` — 所有者已更改的剪贴板对象。

## 讨论

剪贴板所有者仅在需要知道何时失去所有权时才需实现此方法。

所有者在响应此方法时无法读取剪贴板内容。所有者应准备好随时接收此方法，甚至是在用于声明所有权的 [declareTypes(_:owner:)](<../../appkit/nspasteboard/declaretypes(__owner_).md>) 方法内部。

一旦所有者已为其声明的类型提供了全部数据，它将不会再收到 `pasteboardChangedOwner:` 消息。因此，如果你仅为惰性提供数据而维护某个对象，而不只依赖收到 `pasteboardChangedOwner:` 消息，则需要跟踪承诺了哪些类型以及已提供了哪些类型。当所有类型都已提供后，即可释放该所有者。

## 另请参阅

### 相关文档

- [changeCount](../../appkit/nspasteboard/changecount.md) — 接收者的更改计数。
- [declareTypes(_:owner:)](<../../appkit/nspasteboard/declaretypes(__owner_).md>) — 通过声明接收者将包含的新数据类型以及新所有者，为内容更改做好准备。
