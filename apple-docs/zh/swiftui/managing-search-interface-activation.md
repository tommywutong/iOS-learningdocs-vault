---
title: 管理搜索界面的激活
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/managing-search-interface-activation
source_url: 'https://developer.apple.com/documentation/swiftui/managing-search-interface-activation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/managing-search-interface-activation.json'
content_hash: 'sha256:ecd76bd6e4ecca98'
translated: true
---

> 导航： [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [Search](search.md)

# 管理搜索界面的激活

<sub>文章</sub>

以编程方式检测和关闭搜索栏。

## 概述

人们通过轻点或点按来激活你 App 中的搜索栏，然后就可以输入搜索词。在许多情况下，你的 App 只需要响应搜索文本值的相应变化——界面会通过你提供的绑定来更新这些值，如[执行搜索操作](performing-a-search-operation.md)所述。

不过，SwiftUI 还提供了让你以编程方式管理搜索界面的控制。具体来说，你可以：

- 通过向 searchable 修饰符提供绑定来激活或停用界面。
- 通过读取环境值来检测界面是否处于活跃状态。
- 通过调用存储在环境中的操作来关闭界面。
- 等待搜索提交事件发生后再开始搜索。

### 通过绑定控制激活

你可以为 searchable 修饰符的 `isPresented` 参数提供一个指向布尔值的 [Binding](binding.md)，以编程方式控制搜索界面的激活。例如，要让一个表单在出现时搜索界面已处于活跃状态，可以创建一个初始值为 true 的绑定：

```swift
struct SheetView: View {
    @State private var isPresented = true
    @State private var text = ""
  
    var body: some View {
        NavigationStack {
            SheetContent()
                .searchable(text: $text, isPresented: $isPresented)
        }
    }
}   
```

在 iOS 和 macOS 上，SwiftUI 在呈现搜索时让搜索栏获得焦点，在关闭搜索时让搜索栏失去焦点。在搜索界面保持呈现的同时，搜索栏也可能失去焦点。例如，如果你的搜索界面包含一个文本栏列表，有人可能会把焦点移到其中一个文本栏上，而不关闭搜索界面。

### 检测搜索激活

如果你需要知道搜索界面何时处于活跃状态，可以使用 [Environment](environment.md) 属性包装器查询环境的 [isSearching](environmentvalues/issearching.md) 属性。下面的示例展示了一个根据该属性的状态更新所显示文本的视图：

```swift
struct SearchingExample: View {
    @State private var searchText = ""

    var body: some View {
        NavigationStack {
            SearchedView()
                .searchable(text: $searchText)
        }
    }
}

struct SearchedView: View {
    @Environment(\.isSearching) private var isSearching

    var body: some View {
        Text(isSearching ? "Searching" : "Not searching")
    }
}
```

当有人第一次轻点或点按搜索栏时，`isSearching` 属性变为 `true`。当他们取消搜索操作时，该属性变为 `false`。如果你以编程方式关闭界面（如下一节所述），该属性也会变为 `false`。

务必从被 [searchable(text:placement:prompt:)](<view/searchable(text_placement_prompt_).md>) 系列视图修饰符直接或间接包裹的视图内部读取该属性，例如上例中的 `SearchedView`。如果你从该上下文之外读取它（例如把它放在 `SearchingExample` 视图中），你将检测不到属性值的任何变化。

### 关闭搜索界面

你可以使用环境的 [dismissSearch](environmentvalues/dismisssearch.md) 操作以编程方式停用搜索界面。例如，考虑一个带有 [Button](button.md) 的视图，该按钮呈现关于集合中第一个匹配项的更多信息：

```swift
struct ContentView: View {
    @State private var searchText = ""

    var body: some View {
        NavigationStack {
            SearchedView(searchText: searchText)
                .searchable(text: $searchText)
        }
    }
}

private struct SearchedView: View {
    var searchText: String

    let items = ["a", "b", "c"]
    var filteredItems: [String] { items.filter { $0 == searchText.lowercased() } }

    @State private var isPresented = false
    @Environment(\.dismissSearch) private var dismissSearch

    var body: some View {
        if let item = filteredItems.first {
            Button("Details about \(item)") {
                isPresented = true
            }
            .sheet(isPresented: $isPresented) {
                NavigationStack {
                    DetailView(item: item, dismissSearch: dismissSearch)
                }
            }
        }
    }
}
```

只有当有人输入了能产生匹配的搜索文本后，这个按钮才会可见。按钮的操作会显示一个表单，提供关于该项目的更多信息，其中包含一个用于把该项目加入已存储项目列表的 Add 按钮：

```swift
private struct DetailView: View {
    var item: String
    var dismissSearch: DismissSearchAction

    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Text("Information about \(item).")
            .toolbar {
                Button("Add") {
                    // Store the item here...

                    dismiss()
                    dismissSearch()
                }
            }
    }
}
```

人们可以向下拖动来关闭这个表单，这实际上等于取消了操作，而保持进行中的搜索交互原样不变。或者，他们可以轻点 Add 按钮来存储该项目。由于此时人们很可能已经完成了详情视图和搜索交互，按钮的闭包使用 [dismiss](environmentvalues/dismiss.md) 属性关闭表单，并使用 [dismissSearch](environmentvalues/dismisssearch.md) 属性重置搜索栏。

与 `isSearching` 属性一样，务必只在 searchable 视图修饰符的层级结构内读取 `dismissSearch`。如果你在该上下文之外从环境中读取它，调用该操作不会产生任何效果。上面的示例从 `SearchedView` 中读取该操作，然后把它传入表单，因为表单有自己独立的环境。如果搜索界面未处于活跃状态，调用该操作同样没有效果。

### 响应搜索提交

要指定当有人提交搜索查询（按下回车键）时 SwiftUI 调用的操作，添加 [onSubmit(of:_:)](<view/onsubmit(of___).md>) 修饰符：

```swift
SearchedView()
    .searchable(text: $searchText)
    .onSubmit(of: .search) {
        submitCurrentSearchQuery()
    }
```

根据你的 App 结构，你可以用不同的方式利用搜索提交。例如，你可以借此机会在搜索查询字符串中查找可以转换成标记（token）的子字符串。又比如，对于一个非常缓慢的搜索操作（也许因为它需要网络访问），你可以等待提交事件发生后再执行搜索。

## 另请参阅

### 检测、激活和关闭搜索

- [isSearching](environmentvalues/issearching.md) — 一个布尔值，指示用户何时正在搜索。
- [dismissSearch](environmentvalues/dismisssearch.md) — 结束当前搜索交互的操作。
- [DismissSearchAction](dismisssearchaction.md) — 可以结束搜索交互的操作。
- [searchable(text:isPresented:placement:prompt:)](<view/searchable(text_ispresented_placement_prompt_).md>) — 将此视图标记为可搜索，并以编程方式呈现搜索栏。
- [searchable(text:tokens:isPresented:placement:prompt:token:)](<view/searchable(text_tokens_ispresented_placement_prompt_token_).md>) — 将此视图标记为可搜索，支持文本和标记，并支持以编程方式呈现。
- [searchable(text:editableTokens:isPresented:placement:prompt:token:)](<view/searchable(text_editabletokens_ispresented_placement_prompt_token_).md>) — 将此视图标记为可搜索，这会配置搜索栏的显示。
- [searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](<view/searchable(text_tokens_suggestedtokens_ispresented_placement_prompt_token_).md>) — 将此视图标记为可搜索，支持文本、标记和建议，并支持以编程方式呈现。
