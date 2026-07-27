---
title: JavaScript 代码中访问项目的键
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/keys-for-items-accessed-in-javascript-code
source_url: 'https://developer.apple.com/documentation/foundation/keys-for-items-accessed-in-javascript-code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/keys-for-items-accessed-in-javascript-code.json'
content_hash: 'sha256:07de97cfb42c88fb'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [App Extension Support](app-extension-support.md) · [NSItemProvider](nsitemprovider.md)

# JavaScript 代码中访问项目的键

<sub>API 集合</sub>

系统在与 JavaScript 代码之间收发的属性列表项目中所使用的键。

## 主题

### 常量

- [NSExtensionJavaScriptPreprocessingResultsKey](nsextensionjavascriptpreprocessingresultskey.md) — 一个键，其值为类型 `kUTTypePropertyList` 的项目。该项目包含一个 `NSDictionary`，其中包含 JavaScript 代码返回给其完成函数的对象。
- [NSExtensionJavaScriptFinalizeArgumentKey](nsextensionjavascriptfinalizeargumentkey.md) — 一个键，其值为类型 `kUTTypePropertyList` 的项目。该项目包含一个 `NSDictionary`，其中包含要传递给 JavaScript 终结方法的参数。

## 另请参阅

### 常量

- [CompletionHandler](nsitemprovider/completionhandler.md) — 一个接收项目提供者数据的代码块。
- [LoadHandler](nsitemprovider/loadhandler.md) — 一个加载项目提供者数据并将其强制转换为指定类型的代码块。
- [Options Dictionary Key](options-dictionary-key.md) — 表示生成项目提供者数据时要使用的选项的键。
- [NSItemProviderErrorDomain](nsitemprovider/errordomain.md) — 与项目提供者关联的错误域。
- [NSItemProviderFileOptions](nsitemproviderfileoptions.md) — 声明如何处理项目的数据访问规范。
- [NSItemProviderReading](nsitemproviderreading.md) — 用于实现某个类的协议，使项目提供者能够创建该类的实例。
- [NSItemProviderWriting](nsitemproviderwriting.md) — 用于实现某个类的协议，使项目提供者能够从该类的实例中检索数据。
- [NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md) — 控制哪些类别的进程可以看到某个项目的规范。
- [ErrorCode](nsitemprovider/errorcode.md) — 描述从项目提供者获取数据时出现的问题的错误代码。
</content>
