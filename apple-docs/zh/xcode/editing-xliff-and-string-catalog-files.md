---
title: 编辑 XLIFF 和字符串目录文件
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/editing-xliff-and-string-catalog-files
source_url: 'https://developer.apple.com/documentation/xcode/editing-xliff-and-string-catalog-files'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/editing-xliff-and-string-catalog-files.json'
content_hash: 'sha256:fc190493c56f6bb8'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [本地化](localization.md)

# 编辑 XLIFF 和字符串目录文件

<sub>文章</sub>

翻译或调整从项目导出的、针对某种语言和地区的可本地化文件。

## 概述

导出本地化后，你可以将 Xcode Localization Catalog 交给本地化人员翻译，也可以自行编辑 `Localized Contents` 文件夹中的 XLIFF 文件。

### 向 XLIFF 文件添加翻译

若要查找需要翻译的面向用户字符串（包括 App 名称），请在 XLIFF 文件中搜索 `<trans-unit>` 元素。若要插入字符串的译文，请向 `<trans-unit>` 元素添加包含本地化文本的 `<target>` 元素，如下所示：

```other
<trans-unit id="Hello, world!" xml:space="preserve">
        <source>Hello, world!</source>
        <target>Hallo, Welt!</target>
        <note>A friendly greeting.</note>
</trans-unit>
```

### 使用表对相关字符串分组

如果在对代码进行国际化时指定了表名称——也就是说，使用 `Text` 的 [init(_:tableName:bundle:comment:)](<../swiftui/text/init(__tablename_bundle_comment_).md>) 方法或 [NSLocalizedString(_:tableName:bundle:value:comment:)](<../foundation/nslocalizedstring(__tablename_bundle_value_comment_).md>) 函数并传入 `tableName` 参数——Xcode 会将字符串分组到单独的 `<file>` 元素中，并使用 `[table name].strings` 作为文件名。如果没有指定表名称，Xcode 会使用默认的 `Localizable.strings` 作为文件名。

导入本地化时，Xcode 会为每个本地化向项目添加一个字符串文件版本。在以下 SwiftUI 代码清单中，第一个 `Text` 字符串出现在默认的 `Localized.strings` 文件中，而指定了表名称的 Button 标签出现在 `Buttons.strings` 文件中：

```swift
VStack {
    Text("Hello, world!", comment:"A friendly greeting.")
        .font(.largeTitle)
        .padding()
    Button(action: pushMe){
        Text("Push Me", tableName:"Buttons", comment:"Push Me button label.")
    }
    .font(.title)
}
```

### 在 Xcode 中编辑字符串目录

导入本地化后，你可以编辑项目中的字符串目录文件。下次导出本地化时，Xcode 会将更改包含在 XLIFF 文件中。

有关在 Xcode 中编辑字符串目录的更多信息，请参阅[使用字符串目录本地化文本并提供变体](localizing-and-varying-text-with-a-string-catalog.md)。

## 另请参阅

### 翻译和调整

- [为本地化人员创建 App 屏幕截图](creating-screenshots-of-your-app-for-localizers.md) — 与本地化人员共享 App 屏幕截图，为翻译提供上下文。
- [导出本地化](exporting-localizations.md) — 向本地化人员提供项目中的可本地化文件。
- [导入本地化](importing-localizations.md) — 将你为某种语言和地区翻译或调整的文件导入项目。
- [锁定 storyboard 和 XIB 文件中的视图](locking-views-in-storyboard-and-xib-files.md) — 在本地化面向用户的字符串时，防止 Interface Builder 文件发生更改。
