---
title: 已废弃的初始化方法
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textfield-deprecated
source_url: 'https://developer.apple.com/documentation/swiftui/textfield-deprecated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield-deprecated.json'
content_hash: 'sha256:67e114a5e1e4481f'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [文本输入与输出](text-input-and-output.md) · [TextField](textfield.md)

# 已废弃的初始化方法

<sub>API 集合</sub>

查阅已废弃的文本栏初始化方法。

## 概述

在替换这些初始化方法时，请使用视图修饰符来指定文本栏的更改和提交行为。使用 [onSubmit(of:_:)](<view/onsubmit(of___).md>) 视图修饰符来获得 `onCommit` 参数所提供的行为。使用 [focused(_:equals:)](<view/focused(__equals_).md>) 和 [FocusState](focusstate.md) 来获得 `onEditingChanged` 参数所提供的行为。

## 主题

### 使用字符串创建文本栏

- [init(_:text:onEditingChanged:onCommit:)](<textfield/init(__text_oneditingchanged_oncommit_).md>) — 创建一个文本栏，其文本标签由本地化的标题字符串生成。 _(已废弃)_
- [init(_:text:onCommit:)](<textfield/init(__text_oncommit_).md>) — 创建一个文本栏，其文本标签由本地化的标题字符串生成。 _(已废弃)_
- [init(_:text:onEditingChanged:)](<textfield/init(__text_oneditingchanged_).md>) — 创建一个文本栏，其文本标签由本地化的标题字符串生成。 _(已废弃)_

### 使用值创建文本栏

- [init(_:value:formatter:onEditingChanged:onCommit:)](<textfield/init(__value_formatter_oneditingchanged_oncommit_).md>) — 创建一个绑定到任意类型 `V` 的实例。 _(已废弃)_
- [init(_:value:formatter:onCommit:)](<textfield/init(__value_formatter_oncommit_).md>) — 创建一个绑定到任意类型 `V` 的实例。 _(已废弃)_
- [init(_:value:formatter:onEditingChanged:)](<textfield/init(__value_formatter_oneditingchanged_).md>) — 创建一个绑定到任意类型 `V` 的实例。 _(已废弃)_
