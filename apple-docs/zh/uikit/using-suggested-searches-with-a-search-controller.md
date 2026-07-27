---
title: 通过搜索控制器使用建议搜索
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.2+, iPadOS 13.2+, Mac Catalyst 13.2+, Xcode 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/using-suggested-searches-with-a-search-controller
source_url: 'https://developer.apple.com/documentation/uikit/using-suggested-searches-with-a-search-controller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/using-suggested-searches-with-a-search-controller.json'
content_hash: 'sha256:b894674ea5fa1152'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md)

# 通过搜索控制器使用建议搜索

<sub>示例代码</sub>

创建带有建议搜索表格视图（table view）的搜索界面。

## 概述

此示例项目演示如何在 App 中实现 [UISearchController](uisearchcontroller.md)。`UISearchController` 是一种视图控制器（view controller），它根据用户与搜索栏的交互来管理搜索结果的显示。

该示例列出了花卉产品。用户可以按标题、价格、年份和颜色进行搜索。用户轻点搜索栏后，搜索控制器会立即显示建议搜索列表。每项建议搜索表示一种特定颜色：红色、蓝色或绿色。选择建议的颜色时，搜索控制器会按颜色筛选花卉产品列表。此行为与 Mail App 一致。

此示例还演示了使用 [UISceneDelegate](uiscenedelegate.md) 的基于场景（scene）的架构。它包含推荐使用的 [UIUserActivityRestoring](uiuseractivityrestoring.md) 协议，用于存储和恢复搜索结果。采用此协议可存储搜索栏的活跃状态、第一响应者（first responder）状态、搜索栏文本和令牌，并在 App 重新启动时恢复它们。

### 创建搜索控制器

[UITableViewController](uitableviewcontroller.md) 的子类 `MainTableViewController` 会创建搜索控制器。搜索控制器的搜索栏有助于筛选一组 `Product` 对象，并在表格视图中显示结果。示例将搜索控制器放在 `MainTableViewController` 的导航栏中：

```swift
searchController = UISearchController(searchResultsController: resultsTableController)
searchController.searchResultsUpdater = self
searchController.searchBar.autocapitalizationType = .none
searchController.searchBar.searchTextField.placeholder = NSLocalizedString("Enter a search term", comment: "")
searchController.searchBar.returnKeyType = .done

// 将搜索栏放在导航栏中。
navigationItem.searchController = searchController
    
// 让搜索栏始终可见。
navigationItem.hidesSearchBarWhenScrolling = false

// 监视搜索控制器何时呈现和关闭。
searchController.delegate = self

// 监视搜索按钮何时被轻点，并开始或结束编辑。
searchController.searchBar.delegate = self
```

`ResultsTableController` 同时显示筛选后的花卉产品列表和建议搜索颜色列表。用户在搜索栏中输入文本时，花卉产品列表会匹配输入内容。如果用户未输入任何文本，搜索控制器会显示建议搜索颜色列表。每项建议搜索代表一个用于查找特定产品颜色的查询。

### 创建建议搜索

轻点搜索栏后，结果控制器会显示建议搜索列表：

```swift
   func presentSearchController(_ searchController: UISearchController) {
       searchController.showsSearchResultsController = true
       setToSuggestedSearches()
}
```

用户首次轻点搜索栏时，搜索结果控制器会显示建议搜索。用户选择一项建议搜索，然后在搜索栏中输入其他搜索条件。每项建议搜索表示一个 [UISearchToken](uisearchtoken.md)，即搜索查询的视觉表示。轻点建议搜索会为特定颜色创建搜索令牌，搜索控制器会将其放入搜索栏的文本栏中。此文本栏由 [UISearchTextField](uisearchtextfield.md) 表示，支持对搜索令牌进行剪切、拷贝、粘贴和拖放。令牌始终位于文本之前，用户可以选择并删除令牌。

示例按如下方式创建 `UISearchToken`：

```swift
class func searchToken(tokenValue: Int) -> UISearchToken {
    let tokenColor = ResultsTableController.suggestedColor(fromIndex: tokenValue)
    let image =
        UIImage(systemName: "circle.fill")?.withTintColor(tokenColor, renderingMode: .alwaysOriginal)
    let searchToken = UISearchToken(icon: image, text: suggestedTitle(fromIndex: tokenValue))
    
    // 将颜色种类编号设为令牌值。
    let color = ResultsTableController.colorKind(fromIndex: tokenValue).rawValue
    searchToken.representedObject = NSNumber(value: color)
    
    return searchToken
}
```

此示例按如下方式将搜索令牌插入搜索栏的搜索文本栏：

```swift
if let searchField = navigationItem.searchController?.searchBar.searchTextField {
    searchField.insertToken(token, at: 0)
    
    // 现在已有令牌，隐藏建议搜索。
    resultsTableController.showSuggestedSearches = false
    
    // 使用新插入的令牌更新搜索查询。
    updateSearchResults(for: searchController)
}
```

## 另请参阅

### 搜索界面

- [UISearchContainerViewController](uisearchcontainerviewcontroller.md) — 管理搜索结果在界面中呈现方式的视图控制器。
- [UISearchController](uisearchcontroller.md) — 根据用户与搜索栏的交互来管理搜索结果显示的视图控制器。
- [UISearchBar](uisearchbar.md) — 用于接收用户搜索相关信息的专用视图。
- [UISearchResultsUpdating](uisearchresultsupdating.md) — 一组方法，可让你根据用户在搜索栏中输入的信息更新搜索结果。
- [使用搜索控制器显示可搜索内容](displaying-searchable-content-by-using-a-search-controller.md) — 创建一个在表格视图中包含可搜索内容的用户界面。

## 下载

- [UsingSuggestedSearchesWithASearchController.zip](https://docs-assets.developer.apple.com/published/eef0fcbecc3e/UsingSuggestedSearchesWithASearchController.zip)
