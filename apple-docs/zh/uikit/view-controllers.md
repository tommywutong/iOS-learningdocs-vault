---
title: 视图控制器
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/view-controllers
source_url: 'https://developer.apple.com/documentation/uikit/view-controllers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/view-controllers.json'
content_hash: 'sha256:018e9b87c3456639'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# 视图控制器

<sub>API 集合</sub>

使用视图控制器管理你的界面，并促进在 App 内容各处之间的导览。

## 概述

你使用视图控制器来管理 UIKit App 的界面。一个视图控制器管理一个单一根视图，根视图本身可以包含任意数量的子视图。与该视图层级结构的用户交互由你的视图控制器处理，它会根据需要与 App 的其他对象协调。每个 App 都至少有一个视图控制器，其内容填满主窗口。如果你的 App 内容超出了一次能在屏幕上显示的量，可以使用多个视图控制器来管理内容的不同部分。

_容器视图控制器_会将其他视图控制器的内容嵌入到它自己的根视图中。容器视图控制器可以将自定视图与其所容纳的视图控制器的内容混合，以促进导览或创建独特的界面。例如，[UINavigationController](uinavigationcontroller.md) 对象管理一个导航栏和一叠视图控制器（一次只有一个可见），并提供用于在这叠视图控制器中添加和移除视图控制器的 API。

UIKit 为导览和管理特定类型的内容提供了几种标准视图控制器。包含你 App 自定内容的视图控制器由你自己定义。你也可以定义自定的容器视图控制器来实现新的导览方案。

## 主题

### 基础

- [管理 App 窗口中的内容](managing-content-in-your-app-s-windows.md) — 用视图控制器构建 App 的用户界面，并在你想要显示新内容时更改当前可见的视图控制器。
- [UIKit Catalog：创建和自定视图与控制](uikit-catalog-creating-and-customizing-views-and-controls.md) — 用视图和控制自定你的 App 用户界面。

### 内容视图控制器

- [用视图控制器显示和管理视图](displaying-and-managing-views-with-a-view-controller.md) — 在 storyboard 中构建视图控制器，用自定视图配置它，并用 App 的数据填充这些视图。
- [显示和隐藏视图控制器](showing-and-hiding-view-controllers.md) — 使用不同技巧显示视图控制器，并在过渡期间在它们之间传递数据。
- [UIViewController](uiviewcontroller.md) — 一个为你的 UIKit App 管理视图层级结构的对象。
- [UITableViewController](uitableviewcontroller.md) — 一个专门用于管理表格视图的视图控制器。
- [UICollectionViewController](uicollectionviewcontroller.md) — 一个专门用于管理集合视图的视图控制器。
- [UIContentContainer](uicontentcontainer.md) — 一组方法，用于让你的视图控制器的内容适应尺寸和特性变化。

### 容器视图控制器

- [创建自定容器视图控制器](creating-a-custom-container-view-controller.md) — 将一个或多个视图控制器的内容与其他自定视图组合，创建复合界面。
- [UISplitViewController](uisplitviewcontroller.md) — 一种实现层级界面的容器视图控制器。
- [UINavigationController](uinavigationcontroller.md) — 一种容器视图控制器，定义了导览层级内容的基于栈的方案。
- [UINavigationBar](uinavigationbar.md) — 沿屏幕顶部显示在栏中的导览控制，通常与导览控制器配合使用。
- [UINavigationItem](uinavigationitem.md) — 关联的视图控制器可见时导航栏所显示的项目。
- [UITabBarController](uitabbarcontroller.md) — 一种管理多选界面的容器视图控制器，所选内容决定显示哪个子视图控制器。
- [UITabBar](uitabbar.md) — 一种在标签页栏中显示一个或多个按钮的控制，用于在 App 的不同子任务、视图或模式之间进行选择。
- [UITabBarItem](uitabbaritem.md) — 一个描述标签页栏中项目的对象。
- [UITab](uitab.md) — 一个管理标签页栏中标签页的对象。
- [UITabAccessory](uitabaccessory.md)
- [UISearchTab](uisearchtab.md) — 一种表示系统搜索标签页的标签页子类。
- [UITabGroup](uitabgroup.md) — 一个管理一组标签页对象的集合的对象。
- [UIPageViewController](uipageviewcontroller.md) — 一种管理内容页面之间导览的容器视图控制器，每个页面由一个子视图控制器管理。

### 呈现管理

- [禁用表单的下滑手势](disabling-the-pull-down-gesture-for-a-sheet.md) — 在将视图控制器呈现为表单时确保良好的用户体验。
- [UIPresentationController](uipresentationcontroller.md) — 一个管理过渡动画以及视图控制器在屏幕上呈现的对象。
- [UISheetPresentationController](uisheetpresentationcontroller.md) — 一个管理表单外观和行为的呈现控制器。

### 搜索界面

- [UISearchContainerViewController](uisearchcontainerviewcontroller.md) — 一个在你的界面中管理搜索结果呈现的视图控制器。
- [UISearchController](uisearchcontroller.md) — 一个基于与搜索栏的交互来管理搜索结果显示的视图控制器。
- [UISearchBar](uisearchbar.md) — 一个专用于接收用户搜索相关信息的视图。
- [UISearchResultsUpdating](uisearchresultsupdating.md) — 一组方法，让你能够根据用户在搜索栏中输入的信息更新搜索结果。
- [使用搜索控制器显示可搜索的内容](displaying-searchable-content-by-using-a-search-controller.md) — 在表格视图中创建包含可搜索内容的用户界面。
- [在搜索控制器中使用建议搜索](using-suggested-searches-with-a-search-controller.md) — 创建一个带有建议搜索表格视图的搜索界面。

### 图像与视频

- [UIImagePickerController](uiimagepickercontroller.md) — 一个管理系统界面（用于拍照、录制影片以及从用户媒体库中选取项目）的视图控制器。
- [UIVideoEditorController](uivideoeditorcontroller.md) — 一个管理系统界面（用于修剪视频帧和对先前录制的影片进行编码）的视图控制器。

### 文稿与目录

- [自定基于文稿的 App 的启动体验](customizing-a-document-based-app-s-launch-experience.md) — 为 App 的文稿启动场景添加独特元素。
- [向你的 App 添加文稿浏览器](adding-a-document-browser-to-your-app.md) — 让人们能够在你的 App 内访问他们的本地或远程文稿。
- [提供对目录的访问](providing-access-to-directories.md) — 使用文稿选择器访问 App 容器之外目录的内容。
- [使用文稿浏览器构建 App](building-an-app-with-a-document-browser.md) — 通过向 App 添加文稿浏览器，提供对设备上和云中文件的访问。
- [为自定文件格式构建文稿浏览器 App](building-a-document-browser-app-for-custom-file-formats.md) — 实现自定文稿文件格式，以管理用户与不同云存储服务商文件的交互。
- [UIDocumentViewController](uidocumentviewcontroller.md) — 一个管理和呈现存储在本地或云中的文稿的视图控制器。
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md) — 一个用于浏览存储在本地和云中的文稿并对其执行操作的视图控制器。
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) — 一个提供对 App 沙盒之外的文稿或目的地的访问的视图控制器。
- [UIDocumentInteractionController](uidocumentinteractioncontroller.md) — 一个对 App 无法直接处理的文件格式的文件进行预览、打开或打印的视图控制器。

### iCloud 共享

- [UICloudSharingController](uicloudsharingcontroller.md) — 一个呈现标准界面的视图控制器，用于在 CloudKit 共享记录中添加和移除人员。

### 活动界面

- [协作并分享你的数据副本](collaborating-and-sharing-copies-of-your-data.md) — 从你的 App 与他人分享数据和协作。
- [UIActivityViewController](uiactivityviewcontroller.md) — 一个用于从你的 App 提供标准服务的视图控制器。
- [UIActivityItemProvider](uiactivityitemprovider.md) — 传递给活动视图控制器的数据的代理。
- [UIActivityItemSource](uiactivityitemsource.md) — 一组方法，活动视图控制器用它来获取要处理的数据项。
- [UIActivity](uiactivity.md) — 一个抽象类，通过派生子类来实现 App 专属服务。
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md) — 一个为可分享内容提供来源的接口，用于满足用户分享当前内容的请求。

### 字体选择器

- [UIFontPickerViewController](uifontpickerviewcontroller.md) — 一个管理选择字体（系统提供或用户安装）界面的视图控制器。
- [UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md) — 一组可选方法，用于接收关于用户与字体选择器交互的消息。
- [Configuration](uifontpickerviewcontroller/configuration-swift.class.md) — 字体选择器视图控制器用来设置字体选择器的筛选器和显示设置。

### 颜色选择器

- [UIColorPickerViewController](uicolorpickerviewcontroller.md) — 一个管理选择颜色界面的视图控制器。
- [UIColorPickerViewControllerDelegate](uicolorpickerviewcontrollerdelegate.md) — 用于告知颜色选择变化的委托协议。

### 单词查询

- [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md) — 一个显示标准界面的视图控制器，用于查询单词或术语的定义。

### 文本格式化

- [UITextFormattingViewController](uitextformattingviewcontroller.md) — 一个管理常用文本格式化选项界面的视图控制器。

### 打印机选择器

- [UIPrinterPickerController](uiprinterpickercontroller.md) — 一个显示用于选择打印机的标准界面的视图控制器。

### 界面方向

- [UIInterfaceOrientationIsPortrait](uiinterfaceorientation/isportrait.md) — 一个布尔值，指示用户界面当前是否以竖屏方向呈现。
- [UIInterfaceOrientationIsLandscape](uiinterfaceorientation/islandscape.md) — 一个布尔值，指示用户界面当前是否以横屏方向呈现。

### 界面恢复

- [恢复你的 App 的状态](restoring-your-app-s-state.md) — 通过保留当前活动来为用户提供连续性。
- [使用 SwiftUI 恢复你的 App 的状态](../swiftui/restoring-your-app-s-state-with-swiftui.md) — 通过保留用户的当前活动为用户提供 App 连续性。
- [在多次启动之间保留 App 的界面](preserving-your-app-s-ui-across-launches.md) — 在系统终止你的 App 后让它返回到之前的状态。
- [UIViewControllerRestoration](uiviewcontrollerrestoration.md) — 对象采用这些方法后，即可在状态恢复期间充当视图控制器的恢复类。
- [UIObjectRestoration](uiobjectrestoration.md) — 恢复类用来还原已保留对象的接口。
- [UIStateRestoring](uistaterestoring.md) — 用于将对象添加到状态恢复归档的方法。

## 另请参阅

### 用户界面

- [视图与控制](views-and-controls.md) — 在屏幕上呈现你的内容，并定义允许与该内容进行的交互。
- [视图布局](view-layout.md) — 使用叠放视图自动排布界面的视图。需要精确放置视图时请使用 Auto Layout。
- [外观自定](appearance-customization.md) — 将 Liquid Glass 应用到视图、在 App 中支持深色模式、自定各栏的外观，以及使用外观代理修改你的 UI。
- [动画与触感](animation-and-haptics.md) — 使用基于视图的动画和触感向用户提供反馈。
- [窗口与屏幕](windows-and-screens.md) — 为你的视图层级结构和其他内容提供一个容器。
