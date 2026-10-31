---
title: 'panel:isValidFilename:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/panel:isvalidfilename:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/panel:isvalidfilename:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/panel%3Aisvalidfilename%3A.json'
content_hash: 'sha256:eaf2ce3f5a1bf498'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# panel:isValidFilename:

<sub>实例方法</sub>

让委托有机会验证所选项目。

> [!warning] 已废弃
> 请改用 [panel(_:validate:)](<../../appkit/nsopensavepaneldelegate/panel(__validate_).md>)（[NSOpenSavePanelDelegate](../../appkit/nsopensavepaneldelegate.md)）。若两个方法都实现，将调用 URL 版本。

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) panel:(id) sender isValidFilename:(NSString *) filename;
```

## 参数

- `sender` — 请求文件名验证的面板。

- `filename` — 表示要验证的文件名的字符串。

## 返回值

若文件名有效则为 [YES](../yes.md)；若保存面板应停留在其模态循环中并等待用户输入或选择其他文件名，则为 [NO](../no.md)。

## 讨论

`NSSavePanel` 对象 `sender` 会在模态会话结束前，对显示或选择的每个文件名（包括多重选择中的文件名）发送此消息。若委托拒绝多重选择中的某个文件名，该文件名将被取消选择，其余文件名将保留选中状态，且对话框保持打开。

## 另请参阅

### 相关文档

- [panel(_:validate:)](<../../appkit/nsopensavepaneldelegate/panel(__validate_).md>) — 请委托验证用户所选文件的 URL。
