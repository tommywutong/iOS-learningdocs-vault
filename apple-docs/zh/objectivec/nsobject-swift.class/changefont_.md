---
title: 'changeFont:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/changefont:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/changefont:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/changefont%3A.json'
content_hash: 'sha256:ba92094c82cb3a14'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# changeFont:

<sub>实例方法</sub>

Informs responders of a font change.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) changeFont:(id) sender;
```

## 参数

- `sender` — The object that sent the message.

## 讨论

通常，此更改是因为用户更改了富文本字段所选内容中的字体，或整个纯文本字段中的字体。任何包含用户可更改字体的对象都必须响应 [changeFont:](changefont_.md) 消息，方法是对所选内容中的每个字体向 `sender`（一个 NSFontManager 对象）发回 [convert(_:)](<../../appkit/nsfontmanager/convert(__).md>) 消息。有关更多信息，请参阅 Responding to Font Changes。

请注意，此时 [selectedFont](../../appkit/nsfontmanager/selectedfont.md) 可能返回不可预测的结果。此属性中的字体可能不是最后选择的字体，或者在调用 [changeFont:](changefont_.md) 时可能选择了多种字体。强烈不建议从 [changeFont:](changefont_.md) 内部使用 [selectedFont](../../appkit/nsfontmanager/selectedfont.md)。

## 另请参阅

### 相关文档

- [convert(_:toFamily:)](<../../appkit/nsfontmanager/convert(__tofamily_).md>) — 返回一个字体，其特性尽可能与给定字体相似，但字体系列更改为给定系列。
- [addFontTrait(_:)](<../../appkit/nsfontmanager/addfonttrait(__).md>) — 向字体添加特性。
- [convert(_:toSize:)](<../../appkit/nsfontmanager/convert(__tosize_).md>) — 返回一个字体对象，其特性与给定字体相同，但大小更改为给定大小。
- [convert(_:toHaveTrait:)](<../../appkit/nsfontmanager/convert(__tohavetrait_).md>) — 返回包含单个额外特性的字体对象的新版本。
- [modifyFont(_:)](<../../appkit/nsfontmanager/modifyfont(__).md>) — 修改字体的特性。
- [convert(_:toNotHaveTrait:)](<../../appkit/nsfontmanager/convert(__tonothavetrait_).md>) — 返回不包含指定特性的字体对象的新版本。
- [modifyFontViaPanel(_:)](<../../appkit/nsfontmanager/modifyfontviapanel(__).md>) — 使用来自“字体”面板的输入修改字体特性。
- [convertWeight(_:of:)](<../../appkit/nsfontmanager/convertweight(__of_).md>) — 返回字重大于或小于给定字体的字体对象。
- [convert(_:toFace:)](<../../appkit/nsfontmanager/convert(__toface_).md>) — 返回一个字体，其特性尽可能与给定字体相似，但字样更改为给定字样。
- [removeFontTrait(_:)](<../../appkit/nsfontmanager/removefonttrait(__).md>) — 从字体中移除特性。
