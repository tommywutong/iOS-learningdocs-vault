---
title: 'view:stringForToolTip:point:userData:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/view:stringfortooltip:point:userdata:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/view:stringfortooltip:point:userdata:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/view%3Astringfortooltip%3Apoint%3Auserdata%3A.json'
content_hash: 'sha256:4884f49d9e02288c'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# view:stringForToolTip:point:userData:

<sub>实例方法</sub>

返回因光标在视图 `view` 中由 `tag` 标识的工具提示矩形内位置 `point` 处暂停而要显示的工具提示字符串。

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSString *) view:(NSView *) view stringForToolTip:(NSToolTipTag) tag point:(NSPoint) point userData:(void *) data;
```

## 讨论

`userData` 是工具提示矩形创建者提供的附加信息。

## 另请参阅

### 相关文档

- [Online Help](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OnlineHelp/OnlineHelp.html#//apple_ref/doc/uid/10000009i)
- [addToolTip(_:owner:userData:)](<../../appkit/nsview/addtooltip(__owner_userdata_).md>) — 为视图中的定义区域创建工具提示，并返回标识工具提示矩形的标记。
