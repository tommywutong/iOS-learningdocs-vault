---
title: 使用搜索控制器显示可搜索内容
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, Xcode 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/displaying-searchable-content-by-using-a-search-controller
source_url: 'https://developer.apple.com/documentation/uikit/displaying-searchable-content-by-using-a-search-controller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/displaying-searchable-content-by-using-a-search-controller.json'
content_hash: 'sha256:1ae17da3e2112711'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md)

# 使用搜索控制器显示可搜索内容

<sub>示例代码</sub>

创建一个在表格视图（table view）中包含可搜索内容的用户界面。

## 概述

此示例演示如何创建表格视图控制器（table view controller）和搜索控制器，以管理可搜索内容的显示。它还会创建另一个自定义表格视图控制器来显示搜索结果。这个表格视图控制器也充当呈现者，或为搜索结果提供上下文，使搜索结果在自己的上下文中呈现。

此示例包含可选但推荐使用的 [UIStateRestoring](uistaterestoring.md) 协议。你可以在视图控制器类中采用此协议，以存储搜索栏的活跃状态、第一响应者（first responder）状态和搜索栏文本，并在 App 重新启动时恢复它们。

### 创建搜索控制器

使用 [UITableViewController](uitableviewcontroller.md) 的子类 `MainTableViewController` 创建搜索控制器。搜索控制器会搜索并筛选一组 `Product` 对象，并将它们显示在名为 `ResultsTableController` 的表格中。用户输入搜索字符串时会显示此表格控制器，搜索完成时则将其关闭。

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    let nib = UINib(nibName: "TableCell", bundle: nil)
    tableView.register(nib, forCellReuseIdentifier: tableViewCellIdentifier)
    
    resultsTableController =
        self.storyboard?.instantiateViewController(withIdentifier: "ResultsTableController") as? ResultsTableController
    // 此视图控制器关注表格视图中的行选择。
    resultsTableController.tableView.delegate = self
    
    searchController = UISearchController(searchResultsController: resultsTableController)
    searchController.delegate = self
    searchController.searchResultsUpdater = self
    searchController.searchBar.autocapitalizationType = .none
    searchController.searchBar.delegate = self // 监视搜索按钮何时被轻点。
    
    searchController.searchBar.scopeButtonTitles = [Product.productTypeName(forType: .all),
                                                    Product.productTypeName(forType: .birthdays),
                                                    Product.productTypeName(forType: .weddings),
                                                    Product.productTypeName(forType: .funerals)]

    // 将搜索栏放在导航栏中。
    navigationItem.searchController = searchController
    
    // 让搜索栏始终可见。
    navigationItem.hidesSearchBarWhenScrolling = false
    
    /** 搜索通过应用常规视图控制器呈现语义来呈现视图控制器。
        这意味着呈现过程会沿视图控制器层次结构向上移动，直到找到根
        视图控制器或定义了呈现上下文的视图控制器。
    */
    
    /** 指定此视图控制器决定搜索控制器的呈现方式。
        搜索控制器应以模态方式呈现，并与此视图控制器的实际大小相匹配。
    */
    definesPresentationContext = true
    
    setupDataSource()
}
```

### 更新搜索结果

此示例使用 [UISearchResultsUpdating](uisearchresultsupdating.md) 协议以及 [NSComparisonPredicate](../foundation/nscomparisonpredicate.md)，从可用产品组中筛选搜索结果。`NSComparisonPredicate` 是一个 Foundation 类，用于指定如何使用搜索条件提取或筛选数据。搜索条件基于用户在搜索栏中输入的内容，可以是产品标题、推出年份和价格的组合。

为搜索做准备时，会先从搜索栏内容中移除所有前导和尾随空格字符。随后将搜索字符串传递给 `findMatches` 函数，该函数返回搜索中使用的 `NSComparisonPredicate`。产品列表结果会以筛选列表的形式应用到搜索结果表格。

```swift
func updateSearchResults(for searchController: UISearchController) {
       // 根据搜索文本更新筛选后的数组。
       let searchResults = products

       // 移除所有前导和尾随空格。
       let whitespaceCharacterSet = CharacterSet.whitespaces
       let strippedString =
           searchController.searchBar.text!.trimmingCharacters(in: whitespaceCharacterSet)
       let searchItems = strippedString.components(separatedBy: " ") as [String]

       // 为 searchString 中的每个值构建所有“AND”表达式。
       let andMatchPredicates: [NSPredicate] = searchItems.map { searchString in
           findMatches(searchString: searchString)
       }

       // 匹配 Product 对象的字段。
       let finalCompoundPredicate =
           NSCompoundPredicate(andPredicateWithSubpredicates: andMatchPredicates)

       let filteredResults = searchResults.filter { finalCompoundPredicate.evaluate(with: $0) }

       // 将筛选后的结果应用到搜索结果表格。
       if let resultsController = searchController.searchResultsController as? ResultsTableController {
           resultsController.filteredProducts = filteredResults
           resultsController.tableView.reloadData()

           resultsController.resultsLabel.text = resultsController.filteredProducts.isEmpty ?
               NSLocalizedString("NoItemsFoundTitle", comment: "") :
               String(format: NSLocalizedString("Items found: %ld", comment: ""),
                      resultsController.filteredProducts.count)
       }
   }
```

## 另请参阅

### 搜索界面

- [UISearchContainerViewController](uisearchcontainerviewcontroller.md) — 管理搜索结果在界面中呈现方式的视图控制器。
- [UISearchController](uisearchcontroller.md) — 根据用户与搜索栏的交互来管理搜索结果显示的视图控制器。
- [UISearchBar](uisearchbar.md) — 用于接收用户搜索相关信息的专用视图。
- [UISearchResultsUpdating](uisearchresultsupdating.md) — 一组方法，可让你根据用户在搜索栏中输入的信息更新搜索结果。
- [通过搜索控制器使用建议搜索](using-suggested-searches-with-a-search-controller.md) — 创建带有建议搜索表格视图的搜索界面。

## 下载

- [DisplayingSearchableContentByUsingASearchController.zip](https://docs-assets.developer.apple.com/published/b3eaa845da50/DisplayingSearchableContentByUsingASearchController.zip)
