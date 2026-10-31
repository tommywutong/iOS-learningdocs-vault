---
title: 'panel:shouldShowFilename:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/panel:shouldshowfilename:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/panel:shouldshowfilename:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/panel%3Ashouldshowfilename%3A.json'
content_hash: 'sha256:0cd1caeef68558f9'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# panel:shouldShowFilename:

<sub>实例方法</sub>

让委托有机会过滤其不希望用户选择的项目。

> [!warning] 已废弃
> 请使用 [panel(_:shouldEnable:)](<../../appkit/nsopensavepaneldelegate/panel(__shouldenable_).md>)（[NSOpenSavePanelDelegate](../../appkit/nsopensavepaneldelegate.md)）。

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) panel:(id) sender shouldShowFilename:(NSString *) filename;
```

## 参数

- `sender` — 正在查询是否应显示某个文件的面板。

- `filename` — 表示要在浏览器中加载的文件名的字符串。

## 返回值

若 `filename` 应可选则为 [YES](../yes.md)；若保存面板应禁用该文件或目录则为 [NO](../no.md)。

## 讨论

`NSSavePanel` 对象 `sender` 会对其即将在浏览器中加载的每个文件或目录（文件名）向面板的委托发送此消息。

## 另请参阅

### 相关文档

- [panel(_:shouldEnable:)](<../../appkit/nsopensavepaneldelegate/panel(__shouldenable_).md>) — 询问委托指定 URL 是否应在打开面板中启用。
