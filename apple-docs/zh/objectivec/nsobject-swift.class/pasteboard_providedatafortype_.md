---
title: 'pasteboard:provideDataForType:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/pasteboard:providedatafortype:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/pasteboard:providedatafortype:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/pasteboard%3Aprovidedatafortype%3A.json'
content_hash: 'sha256:f77690d29f013d66'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# pasteboard:provideDataForType:

<sub>实例方法</sub>

由所有者对象实现，用于提供承诺的数据。

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) pasteboard:(NSPasteboard *) sender provideDataForType:(NSPasteboardType) type;
```

## 参数

- `sender` — 粘贴操作所需指定数据的剪贴板。

- `type` — 所有者对象必须提供的数据类型。

## 讨论

接收者先前应已在 [declareTypes(_:owner:)](<../../appkit/nspasteboard/declaretypes(__owner_).md>) 消息中声明。

应使用 [setData(_:forType:)](<../../appkit/nspasteboard/setdata(__fortype_).md>)、[setPropertyList(_:forType:)](<../../appkit/nspasteboard/setpropertylist(__fortype_).md>) 或 [setString(_:forType:)](<../../appkit/nspasteboard/setstring(__fortype_).md>) 方法将请求的数据写入 `sender`。当通过应用程序的 [terminate(_:)](<../../appkit/nsapplication/terminate(__).md>) 方法关闭应用时，也可能向所有者发送 [pasteboard:provideDataForType:](pasteboard_providedatafortype_.md) 消息。这是响应“退出”命令时调用的方法。因此，用户可以将内容拷贝到剪贴板、退出应用，并且仍能粘贴已拷贝的数据。仅当指定类型的数据尚未提供给剪贴板时，才会发送 [pasteboard:provideDataForType:](pasteboard_providedatafortype_.md) 消息。应用可以选择在剪切或拷贝操作完成时不写入所有数据类型，而是实现此方法，仅在请求某些类型时提供数据。

若应用在剪切或拷贝操作时以最丰富（因此也是最优先）的类型将数据写入剪贴板，则其 [pasteboard:provideDataForType:](pasteboard_providedatafortype_.md) 方法可以简单地从剪贴板读取该数据，转换为请求的类型，再作为新类型写回剪贴板。

## 另请参阅

### 相关文档

- [Pasteboard Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PasteboardGuide106/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008099)
