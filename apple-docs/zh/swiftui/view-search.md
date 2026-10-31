---
title: 搜索修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-search
source_url: 'https://developer.apple.com/documentation/swiftui/view-search'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-search.json'
content_hash: 'sha256:522a4f51a18a93d3'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 搜索修饰符

<sub>API 集合</sub>

让人们能够在你的 App 中搜索内容。

## 概述

使用搜索视图修饰符为你的 App 添加搜索功能。更多信息，请参阅[搜索](search.md)。

## 主题

### 显示搜索界面

- [searchable(text:placement:prompt:)](<view/searchable(text_placement_prompt_).md>) — 将此视图标记为可搜索，这会配置一个搜索栏的显示。
- [searchable(text:isPresented:placement:prompt:)](<view/searchable(text_ispresented_placement_prompt_).md>) — 将此视图标记为可搜索，并支持以编程方式呈现搜索栏。
- [searchPresentationToolbarBehavior(_:)](<view/searchpresentationtoolbarbehavior(__).md>) — 为此视图内的任何 searchable 修饰符配置搜索工具栏呈现行为。
- [searchToolbarBehavior(_:)](<view/searchtoolbarbehavior(__).md>) — 配置工具栏中搜索的行为。
- [searchSelection(_:)](<view/searchselection(__).md>) — 将与最近的 searchable 修饰符关联的搜索栏的选择绑定到给定的 [TextSelection](textselection.md) 值。

### 使用令牌搜索

- [searchable(text:tokens:placement:prompt:token:)](<view/searchable(text_tokens_placement_prompt_token_).md>) — 将此视图标记为支持文本和令牌的可搜索视图。
- [searchable(text:tokens:isPresented:placement:prompt:token:)](<view/searchable(text_tokens_ispresented_placement_prompt_token_).md>) — 将此视图标记为支持文本和令牌的可搜索视图，并支持以编程方式呈现。

### 使用可编辑令牌搜索

- [searchable(text:editableTokens:isPresented:placement:prompt:token:)](<view/searchable(text_editabletokens_ispresented_placement_prompt_token_).md>) — 将此视图标记为可搜索，这会配置一个搜索栏的显示。
- [searchable(text:editableTokens:placement:prompt:token:)](<view/searchable(text_editabletokens_placement_prompt_token_).md>) — 将此视图标记为可搜索，这会配置一个搜索栏的显示。

### 制作搜索建议

- [searchSuggestions(_:)](<view/searchsuggestions(__).md>) — 为此视图配置搜索建议。
- [searchSuggestions(_:for:)](<view/searchsuggestions(__for_).md>) — 配置在此视图内显示搜索建议的方式。
- [searchCompletion(_:)](<view/searchcompletion(__).md>) — 当此视图用作搜索建议时，将一个完整成形的字符串与其值关联。
- [searchable(text:tokens:suggestedTokens:placement:prompt:token:)](<view/searchable(text_tokens_suggestedtokens_placement_prompt_token_).md>) — 将此视图标记为支持文本、令牌和建议的可搜索视图。
- [searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](<view/searchable(text_tokens_suggestedtokens_ispresented_placement_prompt_token_).md>) — 将此视图标记为支持文本、令牌和建议的可搜索视图，并支持以编程方式呈现。

### 限制搜索范围

- [searchScopes(_:scopes:)](<view/searchscopes(__scopes_).md>) — 为此视图配置搜索范围。
- [searchScopes(_:activation:_:)](<view/searchscopes(__activation___).md>) — 使用指定的激活策略为此视图配置搜索范围。

### 通过听写搜索

- [searchDictationBehavior(_:)](<view/searchdictationbehavior(__).md>) — 为 searchable 修饰符配置的任何搜索栏配置听写行为。

## 另请参阅

### 提供交互性

- [Input and event modifiers](view-input-and-events.md) — 为视图提供响应于用户输入和系统事件而执行的操作。
- [Presentation modifiers](view-presentation.md) — 为视图定义额外要在指定条件下呈现的视图。
- [State modifiers](view-state.md) — 访问存储，并为子视图提供配置数据。
