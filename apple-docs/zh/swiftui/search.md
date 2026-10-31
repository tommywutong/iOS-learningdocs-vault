---
title: 搜索
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/search
source_url: 'https://developer.apple.com/documentation/swiftui/search'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/search.json'
content_hash: 'sha256:6784212488fcb51b'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 搜索

<sub>API 集合</sub>

让人们能够在你的 App 内搜索文本或其他内容。

## 概述

要在你的 App 中呈现搜索栏，请为搜索文本创建并管理存储，也可以选择为称为_令牌_（token）的离散搜索词创建存储。然后，通过将 searchable 视图修饰符应用到 App 中的某个视图，把存储绑定到搜索栏。

![](../../../attachments/366a90bfb4ab3aea60848d447e01a437/search-hero@2x.png)

当人们与搜索栏交互时，他们会隐式地修改底层存储，从而修改搜索参数。你的 App 会相应地更新其界面的其他部分。为了增强搜索交互，你还可以：

- 在搜索期间提供建议，包括针对文本和令牌的建议。
- 实现搜索范围，帮助人们缩小搜索空间。
- 检测人们何时激活搜索栏，并使用环境值以编程方式关闭搜索栏。

有关设计指引，请参阅《人机界面指南》中的[搜索](../design/human-interface-guidelines/searching.md)。

## 主题

### 搜索 App 的数据模型

- [为你的 App 添加搜索界面](adding-a-search-interface-to-your-app.md) — 呈现一个人们可以用来搜索你 App 内容的界面。
- [执行搜索操作](performing-a-search-operation.md) — 根据你存储的搜索文本和可选的令牌来更新搜索结果。
- [searchable(text:placement:prompt:)](<view/searchable(text_placement_prompt_).md>) — 将此视图标记为可搜索，这会配置一个搜索栏的显示。
- [searchable(text:tokens:placement:prompt:token:)](<view/searchable(text_tokens_placement_prompt_token_).md>) — 将此视图标记为支持文本和令牌的可搜索视图。
- [searchable(text:editableTokens:placement:prompt:token:)](<view/searchable(text_editabletokens_placement_prompt_token_).md>) — 将此视图标记为可搜索，这会配置一个搜索栏的显示。
- [SearchFieldPlacement](searchfieldplacement.md) — 搜索栏在视图层级结构中的位置。

### 制作搜索建议

- [建议搜索词](suggesting-search-terms.md) — 为在你的 App 中搜索内容的人们提供建议。
- [searchSuggestions(_:)](<view/searchsuggestions(__).md>) — 为此视图配置搜索建议。
- [searchSuggestions(_:for:)](<view/searchsuggestions(__for_).md>) — 配置在此视图内显示搜索建议的方式。
- [searchCompletion(_:)](<view/searchcompletion(__).md>) — 当此视图用作搜索建议时，将一个完整成形的字符串与其值关联。
- [searchable(text:tokens:suggestedTokens:placement:prompt:token:)](<view/searchable(text_tokens_suggestedtokens_placement_prompt_token_).md>) — 将此视图标记为支持文本、令牌和建议的可搜索视图。
- [SearchSuggestionsPlacement](searchsuggestionsplacement.md) — SwiftUI 显示搜索建议的方式。

### 限制搜索范围

- [为搜索操作划分范围](scoping-a-search-operation.md) — 把搜索空间划分为几个大类。
- [searchScopes(_:scopes:)](<view/searchscopes(__scopes_).md>) — 为此视图配置搜索范围。
- [searchScopes(_:activation:_:)](<view/searchscopes(__activation___).md>) — 使用指定的激活策略为此视图配置搜索范围。
- [SearchScopeActivation](searchscopeactivation.md) — searchable 修饰符显示或隐藏搜索范围的方式。

### 检测、激活和关闭搜索

- [管理搜索界面的激活](managing-search-interface-activation.md) — 以编程方式检测并关闭搜索栏。
- [isSearching](environmentvalues/issearching.md) — 一个布尔值，指示用户何时正在搜索。
- [dismissSearch](environmentvalues/dismisssearch.md) — 一个结束当前搜索交互的操作。
- [DismissSearchAction](dismisssearchaction.md) — 一个可以结束搜索交互的操作。
- [searchable(text:isPresented:placement:prompt:)](<view/searchable(text_ispresented_placement_prompt_).md>) — 将此视图标记为可搜索，并支持以编程方式呈现搜索栏。
- [searchable(text:tokens:isPresented:placement:prompt:token:)](<view/searchable(text_tokens_ispresented_placement_prompt_token_).md>) — 将此视图标记为支持文本和令牌的可搜索视图，并支持以编程方式呈现。
- [searchable(text:editableTokens:isPresented:placement:prompt:token:)](<view/searchable(text_editabletokens_ispresented_placement_prompt_token_).md>) — 将此视图标记为可搜索，这会配置一个搜索栏的显示。
- [searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](<view/searchable(text_tokens_suggestedtokens_ispresented_placement_prompt_token_).md>) — 将此视图标记为支持文本、令牌和建议的可搜索视图，并支持以编程方式呈现。

### 在搜索期间显示工具栏内容

- [searchPresentationToolbarBehavior(_:)](<view/searchpresentationtoolbarbehavior(__).md>) — 为此视图内的任何 searchable 修饰符配置搜索工具栏呈现行为。
- [SearchPresentationToolbarBehavior](searchpresentationtoolbarbehavior.md) — 一个类型，定义呈现搜索时工具栏的行为方式。

### 在视图中搜索文本

- [findNavigator(isPresented:)](<view/findnavigator(ispresented_).md>) — 以编程方式呈现文本编辑器视图的查找和替换界面。
- [findDisabled(_:)](<view/finddisabled(__).md>) — 阻止文本编辑器中的查找和替换操作。
- [replaceDisabled(_:)](<view/replacedisabled(__).md>) — 阻止文本编辑器中的替换操作。
- [FindContext](findcontext.md) — 支持文本编辑的视图的查找导航器状态。

## 另请参阅

### App 结构

- [App 组织](app-organization.md) — 定义 App 的入口点和顶层结构。
- [场景](scenes.md) — 声明构成 App 各部分的用户界面分组。
- [窗口](windows.md) — 在一个窗口或一组窗口中显示用户界面内容。
- [沉浸式空间](immersive-spaces.md) — 在用户的周围环境中显示无边界内容。
- [文稿](documents.md) — 让人们能够打开和管理文稿。
- [导览](navigation.md) — 让人们能够在场景内移动到你 App 视图层级结构的不同部分。
- [模态呈现方式](modal-presentations.md) — 在提供专注交互的独立视图中呈现内容。
- [工具栏](toolbars.md) — 提供对常用命令和控制的即时访问。
- [App 扩展](app-extensions.md) — 把你 App 的基础功能扩展到系统的其他部分，例如添加小组件。
