# 模块 5：UIKit、响应者链、渲染与列表性能

> 从事件传递到像素上屏，串起视图生命周期、渲染和列表性能。
> 对应仓库范围：UI 与渲染、RunLoop 与响应性、性能与调试。中文正文优先，随后列出未翻译资料。

- [返回暑期计划知识地图](../summer.md)
- [查看全库主题地图](../topics.md)

## 学习步骤

| 步骤 | 内容 | 产出 |
|---|---|---|
| 5.1 | 响应者链、事件传递链、hit-test，一个点击的完整过程 | 从触摸到 action 的完整时序图；自定义 hit-test 实验 |
| 5.2 | UIViewController 和 UIResponder；生命周期：创建、加载视图、出现/消失、布局、销毁 | 容器/模态切换真实日志，不背单一固定顺序 |
| 5.3 | frame、bounds、center、坐标转换，相对/绝对坐标 | 三个嵌套视图 + transform 实验 |
| 5.4 | UIView / CALayer 分工；model/presentation/render tree；布局、显示、合成 | “UIView 管交互与布局，CALayer 管可视内容”关系图 |
| 5.5 | 离屏渲染、混合、光栅化、圆角/阴影/mask 条件与代价 | Core Animation Instrument 对比 3 种圆角/阴影写法 |
| 5.6 | UITableView data source / delegate 调用时机；真正必需的两个 data source 方法 | 可运行表格 + 生命周期日志；纠正“必须实现 delegate” |
| 5.7 | cell 复用、预取、异步图片、主线程预算、高度计算、批量更新 | 列表卡顿 baseline；Time Profiler 和 Core Animation 证据 |
| 5.8 | NSDictionary / NSMutableArray 语义、class cluster、哈希/碰撞、扩容、可变数组存储策略 | API 语义、复杂度、源码版本差异三层作答 |

## 计划指定材料

- [使用响应者和响应者链处理事件](../../apple-docs/zh/uikit/using-responders-and-the-responder-chain-to-handle-events.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/uikit/using-responders-and-the-responder-chain-to-handle-events.md) — 本仓库资料
- [UIResponder](../../apple-docs/zh/uikit/uiresponder.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/uikit/uiresponder.md) — 本仓库资料
- [UIViewController](../../apple-docs/zh/uikit/uiviewcontroller.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/uikit/uiviewcontroller.md) — 本仓库资料
- [关于窗口与视图](../../legacy-archive/vault/documentation/Windows%20Views/View%20Programming%20Guide%20for%20iOS/About%20Windows%20and%20Views.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Windows%20Views/View%20Programming%20Guide%20for%20iOS/About%20Windows%20and%20Views.md) — Apple 旧归档
- [关于 Core Animation](../../legacy-archive/vault/documentation/Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md) — Apple 旧归档
- [Core Animation 基础](../../legacy-archive/vault/documentation/Cocoa/Core%20Animation%20Programming%20Guide/Core%20Animation%20Basics.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Core%20Animation%20Programming%20Guide/Core%20Animation%20Basics.md) — Apple 旧归档
- [设置图层对象](../../legacy-archive/vault/documentation/Cocoa/Core%20Animation%20Programming%20Guide/Setting%20Up%20Layer%20Objects.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Core%20Animation%20Programming%20Guide/Setting%20Up%20Layer%20Objects.md) — Apple 旧归档
- [用数据填充表格](../../apple-docs/zh/uikit/filling-a-table-with-data.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/uikit/filling-a-table-with-data.md) — 本仓库资料
- [UITableViewDataSource](../../apple-docs/zh/uikit/uitableviewdatasource.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/uikit/uitableviewdatasource.md) — 本仓库资料
- [UITableViewDelegate](../../apple-docs/zh/uikit/uitableviewdelegate.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/uikit/uitableviewdelegate.md) — 本仓库资料
- [提升 App 的性能](../../apple-docs/zh/xcode/improving-your-app-s-performance.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/xcode/improving-your-app-s-performance.md) — 本仓库资料
- [性能与指标](../../apple-docs/zh/xcode/performance-and-metrics.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/xcode/performance-and-metrics.md) — 本仓库资料
- [NSDictionary](../../apple-docs/zh/foundation/nsdictionary.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/nsdictionary.md) — 本仓库资料
- [NSMutableArray](../../apple-docs/zh/foundation/nsmutablearray.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/nsmutablearray.md) — 本仓库资料
- [计划材料](https://github.com/apple-oss-distributions/CF) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://swiftrocks.com/understanding-the-ios-responder-chain) — 第三方博客（未归档（swiftrocks.com））
- [计划材料](https://medium.com/ios-os-x-development/understanding-cocoa-and-cocoa-touch-responder-chain-12fe558ebe97) — 第三方博客（未归档（medium.com））
- [计划材料](https://www.cocoanetics.com/2012/09/the-amazing-responder-chain/) — 第三方博客（未归档（cocoanetics.com））
- [计划材料](https://bbs.huaweicloud.com/blogs/331365) — 第三方博客（未归档（bbs.huaweicloud.com））
- [计划材料](https://medium.com/@dhrumilraval212/mastering-the-uiviewcontroller-lifecycle-a-senior-developers-deep-dive-4cc8082cd3d6) — 第三方博客（未归档（medium.com））
- [计划材料](https://useyourloaf.com/blog/uikit-view-lifecycle-viewisappearing/) — 第三方博客（未归档（useyourloaf.com））
- [如何发现并修复 iOS 上视图控制器的过早加载](../../blogs/zh/jessesquires/how-to-find-and-fix-premature-view-controller-loading-on-ios.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/jessesquires/how-to-find-and-fix-premature-view-controller-loading-on-ios.md) — 本仓库资料
- [Animations Explained](../../blogs/en/objcio/animations-explained.md) · [原文网页](https://www.objc.io/issues/12-animations/animations-explained/) — 第三方博客
- [计划材料](https://joeshang.github.io/2014-12-19-understand-anchorpoint-position-frame/) — 第三方博客（未归档（joeshang.github.io））
- [计划材料](https://zhangbuhuai.com/post/layer-geometry-in-ios.html) — 第三方博客（未归档（zhangbuhuai.com））
- [计划材料](http://www.samirchen.com/graphic-transform-in-ios/) — 第三方博客（未归档（samirchen.com））
- [计划材料](https://www.jianshu.com/p/e1fec2f92c63) — 第三方博客（未归档（jianshu.com））
- [计划材料](https://www.objc.io/issue-3/moving-pixels-onto-the-screen.html) — 第三方博客（未归档（objc.io））
- [计划材料](https://www.hackingwithswift.com/articles/155/advanced-uiview-shadow-effects-using-shadowpath) — 第三方博客（未归档（hackingwithswift.com））
- [计划材料](http://angelolloqui.com/blog/30-iOS-Performance-tips-I-Drawing-shadows) — 第三方博客（未归档（angelolloqui.com））
- [计划材料](https://github.com/seedante/OptimizationForOffscreenRender) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://blog.fearcat.in/a?ID=01750-5926f776-644b-465e-8d4d-d6c7b854e533) — 第三方博客（未归档（blog.fearcat.in））
- [计划材料](https://www.jianshu.com/p/e6d44ca9c103) — 第三方博客（未归档（jianshu.com））
- [Clean Table View Code](../../blogs/en/objcio/clean-table-view-code.md) · [原文网页](https://www.objc.io/issues/1-view-controllers/table-views/) — 第三方博客
- [计划材料](https://medium.com/jike-engineering/asyncdisplaykit%E4%BB%8B%E7%BB%8D-%E4%B8%80-6b871d29e005) — 第三方博客（未归档（medium.com））
- [计划材料](https://www.swiftcafe.io/post/asdk) — 第三方博客（未归档（swiftcafe.io））
- [计划材料](https://medium.com/@iosengineering/better-uitableviews-pt-1-performance-a76dcd76d772) — 第三方博客（未归档（medium.com））
- [计划材料](https://blog.aberlt.com/2017/12/30/UITableView-%E6%B5%81%E7%95%85%E5%BA%A6%E4%BC%98%E5%8C%96%E5%AE%9E%E8%B7%B5/) — 第三方博客（未归档（blog.aberlt.com））
- [揭示 NSMutableArray](../../blogs/zh/ciechanowski/exposing-nsmutablearray-bartosz-ciechanowski.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/ciechanowski/exposing-nsmutablearray-bartosz-ciechanowski.md) — 本仓库资料
- [揭开 NSDictionary 的面纱](../../blogs/zh/ciechanowski/exposing-nsdictionary-bartosz-ciechanowski.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/ciechanowski/exposing-nsdictionary-bartosz-ciechanowski.md) — 本仓库资料
- [计划材料](http://blog.joyingx.me/2015/05/03/NSMutableArray%20%E5%8E%9F%E7%90%86%E6%8F%AD%E9%9C%B2/) — 第三方博客（未归档（blog.joyingx.me））
- [计划材料](https://zhuanlan.zhihu.com/p/25063245) — 第三方博客（未归档（zhuanlan.zhihu.com））
- [计划材料](https://www.laoqingcai.com/ios-nsmutablearray/) — 第三方博客（未归档（laoqingcai.com））

## 中文资料

共 109 份。包含译文和原生中文文章。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [[iOS] CALayer与UIView（以及离屏渲染浅谈）](../../blogs/snapshots/jianshu.com/ios-calayer%E4%B8%8Euiview-%E4%BB%A5%E5%8F%8A%E7%A6%BB%E5%B1%8F%E6%B8%B2%E6%9F%93%E6%B5%85%E8%B0%88.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/jianshu.com/ios-calayer%E4%B8%8Euiview-%E4%BB%A5%E5%8F%8A%E7%A6%BB%E5%B1%8F%E6%B8%B2%E6%9F%93%E6%B5%85%E8%B0%88.md) | 原生中文 |
| 计划核心 | [iOS 响应者链：UIResponder、UIEvent、UIControl 及其用途](../../blogs/snapshots-zh/swiftrocks.com/ios-responder-chain-uiresponder-uievent-uicontrol-and-uses.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/swiftrocks.com/ios-responder-chain-uiresponder-uievent-uicontrol-and-uses.md) | 已翻译 |
| 计划核心 | [iOS 性能提示（一）：绘制阴影](../../blogs/snapshots-zh/angelolloqui.com/ios-performance-tips-i-drawing-shadows.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/angelolloqui.com/ios-performance-tips-i-drawing-shadows.md) | 已翻译 |
| 计划核心 | [iOS中的图形变换](../../blogs/snapshots/samirchen.com/ios%E4%B8%AD%E7%9A%84%E5%9B%BE%E5%BD%A2%E5%8F%98%E6%8D%A2.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/samirchen.com/ios%E4%B8%AD%E7%9A%84%E5%9B%BE%E5%BD%A2%E5%8F%98%E6%8D%A2.md) | 原生中文 |
| 计划核心 | [iOS之深入解析事件传递的响应链](../../blogs/snapshots/bbs.huaweicloud.com/ios%E4%B9%8B%E6%B7%B1%E5%85%A5%E8%A7%A3%E6%9E%90%E4%BA%8B%E4%BB%B6%E4%BC%A0%E9%80%92%E7%9A%84%E5%93%8D%E5%BA%94%E9%93%BE.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/bbs.huaweicloud.com/ios%E4%B9%8B%E6%B7%B1%E5%85%A5%E8%A7%A3%E6%9E%90%E4%BA%8B%E4%BB%B6%E4%BC%A0%E9%80%92%E7%9A%84%E5%93%8D%E5%BA%94%E9%93%BE.md) | 原生中文 |
| 计划核心 | [iOS：重识Transform和frame](../../blogs/snapshots/jianshu.com/ios-%E9%87%8D%E8%AF%86transform%E5%92%8Cframe.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/jianshu.com/ios-%E9%87%8D%E8%AF%86transform%E5%92%8Cframe.md) | 原生中文 |
| 计划核心 | [NSMutableArray原理揭露](../../blogs/snapshots/blog.joyingx.me/nsmutablearray%E5%8E%9F%E7%90%86%E6%8F%AD%E9%9C%B2.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.joyingx.me/nsmutablearray%E5%8E%9F%E7%90%86%E6%8F%AD%E9%9C%B2.md) | 原生中文 |
| 计划核心 | [UIKit 视图生命周期——viewIsAppearing](../../blogs/snapshots-zh/useyourloaf.com/uikit-view-lifecycle-viewisappearing.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/useyourloaf.com/uikit-view-lifecycle-viewisappearing.md) | 已翻译 |
| 计划核心 | [UITableView 流畅度优化实践](../../blogs/snapshots/blog.aberlt.com/uitableview-%E6%B5%81%E7%95%85%E5%BA%A6%E4%BC%98%E5%8C%96%E5%AE%9E%E8%B7%B5.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.aberlt.com/uitableview-%E6%B5%81%E7%95%85%E5%BA%A6%E4%BC%98%E5%8C%96%E5%AE%9E%E8%B7%B5.md) | 原生中文 |
| 计划核心 | [令人惊叹的响应者链](../../blogs/snapshots-zh/cocoanetics.com/the-amazing-responder-chain.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/cocoanetics.com/the-amazing-responder-chain.md) | 已翻译 |
| 计划核心 | [普通可变数组](../../blogs/snapshots/laoqingcai.com/%E6%99%AE%E9%80%9A%E5%8F%AF%E5%8F%98%E6%95%B0%E7%BB%84.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/laoqingcai.com/%E6%99%AE%E9%80%9A%E5%8F%AF%E5%8F%98%E6%95%B0%E7%BB%84.md) | 原生中文 |
| 计划核心 | [理解 anchorPoint，position，frame 的关系](../../blogs/snapshots/joeshang.github.io/%E7%90%86%E8%A7%A3-anchorpoint-position-frame-%E7%9A%84%E5%85%B3%E7%B3%BB.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/joeshang.github.io/%E7%90%86%E8%A7%A3-anchorpoint-position-frame-%E7%9A%84%E5%85%B3%E7%B3%BB.md) | 原生中文 |
| 官方资料 | [UIKit Catalog: 创建和自定视图与控制](../../apple-docs/zh/uikit/uikit-catalog-creating-and-customizing-views-and-controls.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/uikit-catalog-creating-and-customizing-views-and-controls.md) | 已翻译 |
| 官方资料 | [UIKit 函数](../../apple-docs/zh/uikit/uikit-functions.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/uikit-functions.md) | 已翻译 |
| 官方资料 | [UIKit 动力学](../../apple-docs/zh/uikit/uikit-dynamics.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/uikit-dynamics.md) | 已翻译 |
| 官方资料 | [UIKit 宏](../../apple-docs/zh/uikit/uikit-macros.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/uikit-macros.md) | 已翻译 |
| 官方资料 | [UIKit 常量](../../apple-docs/zh/uikit/uikit-constants.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/uikit-constants.md) | 已翻译 |
| 官方资料 | [UIKit 数据类型](../../apple-docs/zh/uikit/uikit-data-types.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/uikit-data-types.md) | 已翻译 |
| 官方资料 | [UIKit 枚举](../../apple-docs/zh/uikit/uikit-enumerations.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/uikit-enumerations.md) | 已翻译 |
| 官方资料 | [UIKit 的辅助功能](../../apple-docs/zh/uikit/accessibility-for-uikit.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/accessibility-for-uikit.md) | 已翻译 |
| 官方资料 | [丰富文本视图中的文本](../../apple-docs/zh/uikit/enriching-your-text-in-text-views.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/enriching-your-text-in-text-views.md) | 已翻译 |
| 官方资料 | [为 iOS 本地化自动调整视图大小](../../apple-docs/zh/xcode/autosizing-views-for-localization-in-ios.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/autosizing-views-for-localization-in-ios.md) | 已翻译 |
| 官方资料 | [为自定义 UIKit 视图添加 Writing Tools 支持](../../apple-docs/zh/uikit/adding-writing-tools-support-to-a-custom-uiview.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/adding-writing-tools-support-to-a-custom-uiview.md) | 已翻译 |
| 官方资料 | [为表格分区添加页眉和页脚](../../apple-docs/zh/uikit/adding-headers-and-footers-to-table-sections.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/adding-headers-and-footers-to-table-sections.md) | 已翻译 |
| 官方资料 | [为表格配置单元格](../../apple-docs/zh/uikit/configuring-the-cells-for-your-table.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/configuring-the-cells-for-your-table.md) | 已翻译 |
| 官方资料 | [以不同光栅化速率渲染](../../apple-docs/zh/metal/rendering-at-different-rasterization-rates.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/rendering-at-different-rasterization-rates.md) | 已翻译 |
| 官方资料 | [估算表格滚动区域的高度](../../apple-docs/zh/uikit/estimating-the-height-of-a-table-s-scrolling-area.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/estimating-the-height-of-a-table-s-scrolling-area.md) | 已翻译 |
| 官方资料 | [使用光线追踪实时渲染反射](../../apple-docs/zh/metal/rendering-reflections-in-real-time-using-ray-tracing.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/rendering-reflections-in-real-time-using-ray-tracing.md) | 已翻译 |
| 官方资料 | [使用可差分数据源更新集合视图](../../apple-docs/zh/uikit/updating-collection-views-using-diffable-data-sources.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/updating-collection-views-using-diffable-data-sources.md) | 已翻译 |
| 官方资料 | [使用响应者和响应者链处理事件](../../apple-docs/zh/uikit/using-responders-and-the-responder-chain-to-handle-events.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/using-responders-and-the-responder-chain-to-handle-events.md) | 已翻译 |
| 官方资料 | [使用瓦片着色器以前向+光照渲染场景](../../apple-docs/zh/metal/rendering-a-scene-with-forward-plus-lighting-using-tile-shaders.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/rendering-a-scene-with-forward-plus-lighting-using-tile-shaders.md) | 已翻译 |
| 官方资料 | [使用目标-动作模式响应基于控制的事件](../../apple-docs/zh/uikit/responding-to-control-based-events-using-target-action.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/responding-to-control-based-events-using-target-action.md) | 已翻译 |
| 官方资料 | [使用自定义特性向视图层级结构提供数据](../../apple-docs/zh/uikit/providing-data-to-the-view-hierarchy-with-custom-traits.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/providing-data-to-the-view-hierarchy-with-custom-traits.md) | 已翻译 |
| 官方资料 | [使用视图控制器显示和管理视图](../../apple-docs/zh/uikit/displaying-and-managing-views-with-a-view-controller.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/displaying-and-managing-views-with-a-view-controller.md) | 已翻译 |
| 官方资料 | [使用调用树视图分析 CPU 概况](../../apple-docs/zh/xcode/analyzing-cpu-profiles-with-call-tree-views.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/analyzing-cpu-profiles-with-call-tree-views.md) | 已翻译 |
| 官方资料 | [使用顶点放大提高渲染性能](../../apple-docs/zh/metal/improving-rendering-performance-with-vertex-amplification.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/improving-rendering-performance-with-vertex-amplification.md) | 已翻译 |
| 官方资料 | [关于使用 UIKit 进行 App 开发](../../apple-docs/zh/uikit/about-app-development-with-uikit.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/about-app-development-with-uikit.md) | 已翻译 |
| 官方资料 | [关于同步事件](../../apple-docs/zh/metal/about-synchronization-events.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/about-synchronization-events.md) | 已翻译 |
| 官方资料 | [创建自定大小的表格视图单元格](../../apple-docs/zh/uikit/creating-self-sizing-table-view-cells.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/creating-self-sizing-table-view-cells.md) | 已翻译 |
| 官方资料 | [创建自定容器视图控制器](../../apple-docs/zh/uikit/creating-a-custom-container-view-controller.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/creating-a-custom-container-view-controller.md) | 已翻译 |
| 官方资料 | [动画与触感反馈](../../apple-docs/zh/uikit/animation-and-haptics.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/animation-and-haptics.md) | 已翻译 |
| 官方资料 | [在 GPU 与 CPU 之间同步事件](../../apple-docs/zh/metal/synchronizing-events-between-a-gpu-and-the-cpu.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/synchronizing-events-between-a-gpu-and-the-cpu.md) | 已翻译 |
| 官方资料 | [在 Objective-C 中以延迟光照渲染场景](../../apple-docs/zh/metal/rendering-a-scene-with-deferred-lighting-in-objective-c.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/rendering-a-scene-with-deferred-lighting-in-objective-c.md) | 已翻译 |
| 官方资料 | [在 Swift 中以延迟光照渲染场景](../../apple-docs/zh/metal/rendering-a-scene-with-deferred-lighting-in-swift.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/rendering-a-scene-with-deferred-lighting-in-swift.md) | 已翻译 |
| 官方资料 | [在 UIKit 中使用观察跟踪自动更新视图](../../apple-docs/zh/uikit/updating-views-automatically-with-observation-tracking-in-uikit.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/updating-views-automatically-with-observation-tracking-in-uikit.md) | 已翻译 |
| 官方资料 | [在 UIKit 中向属性字符串添加表格](../../apple-docs/zh/uikit/adding-tables-to-attributed-strings.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/adding-tables-to-attributed-strings.md) | 已翻译 |
| 官方资料 | [在 UIKit 中自定义与调整 sheet 的大小](../../apple-docs/zh/uikit/customizing-and-resizing-sheets-in-uikit.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/customizing-and-resizing-sheets-in-uikit.md) | 已翻译 |
| 官方资料 | [在光线追踪场景中渲染曲线图元](../../apple-docs/zh/metal/rendering-a-curve-primitive-in-a-ray-tracing-scene.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/rendering-a-curve-primitive-in-a-ray-tracing-scene.md) | 已翻译 |
| 官方资料 | [在单个设备内同步事件](../../apple-docs/zh/metal/synchronizing-events-within-a-single-device.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/synchronizing-events-within-a-single-device.md) | 已翻译 |
| 官方资料 | [在自定义文本视图中采用系统选择 UI](../../apple-docs/zh/uikit/adopting-system-selection-ui-in-custom-text-views.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/adopting-system-selection-ui-in-custom-text-views.md) | 已翻译 |
| 官方资料 | [在自定义视图中采用拖放](../../apple-docs/zh/uikit/adopting-drag-and-drop-in-a-custom-view.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/adopting-drag-and-drop-in-a-custom-view.md) | 已翻译 |
| 官方资料 | [在表格视图中采用拖放](../../apple-docs/zh/uikit/adopting-drag-and-drop-in-a-table-view.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/adopting-drag-and-drop-in-a-table-view.md) | 已翻译 |
| 官方资料 | [在视图中处理触摸](../../apple-docs/zh/uikit/handling-touches-in-your-view.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/handling-touches-in-your-view.md) | 已翻译 |
| 官方资料 | [处理表格视图中的行选择](../../apple-docs/zh/uikit/handling-row-selection-in-a-table-view.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/handling-row-selection-in-a-table-view.md) | 已翻译 |
| 官方资料 | [实现现代集合视图](../../apple-docs/zh/uikit/implementing-modern-collection-views.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/implementing-modern-collection-views.md) | 已翻译 |
| 官方资料 | [将 SwiftUI 与 UIKit 搭配使用](../../apple-docs/zh/uikit/using-swiftui-with-uikit.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/using-swiftui-with-uikit.md) | 已翻译 |
| 官方资料 | [将图像异步加载到表格视图和集合视图中](../../apple-docs/zh/uikit/asynchronously-loading-images-into-table-and-collection-views.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/asynchronously-loading-images-into-table-and-collection-views.md) | 已翻译 |
| 官方资料 | [将手势识别器附加到 UIKit 控制](../../apple-docs/zh/uikit/attaching-gesture-recognizers-to-uikit-controls.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/attaching-gesture-recognizers-to-uikit-controls.md) | 已翻译 |
| 官方资料 | [提升 App 的渲染效率](../../apple-docs/zh/xcode/improving-your-app-s-rendering-efficiency.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/improving-your-app-s-rendering-efficiency.md) | 已翻译 |
| 官方资料 | [支持表格视图中的拖放](../../apple-docs/zh/uikit/supporting-drag-and-drop-in-table-views.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/supporting-drag-and-drop-in-table-views.md) | 已翻译 |
| 官方资料 | [支持集合视图中的拖放](../../apple-docs/zh/uikit/supporting-drag-and-drop-in-collection-views.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/supporting-drag-and-drop-in-collection-views.md) | 已翻译 |
| 官方资料 | [显示与隐藏视图控制器](../../apple-docs/zh/uikit/showing-and-hiding-view-controllers.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/showing-and-hiding-view-controllers.md) | 已翻译 |
| 官方资料 | [构建高性能列表和集合视图](../../apple-docs/zh/uikit/building-high-performance-lists-and-collection-views.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/building-high-performance-lists-and-collection-views.md) | 已翻译 |
| 官方资料 | [流式布局附属视图](../../apple-docs/zh/uikit/flow-layout-supplementary-views.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/flow-layout-supplementary-views.md) | 已翻译 |
| 官方资料 | [渲染流程](../../apple-docs/zh/metal/render-passes.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/render-passes.md) | 已翻译 |
| 官方资料 | [渲染通道配置](../../apple-docs/zh/metal/render-pass-configuration.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/render-pass-configuration.md) | 已翻译 |
| 官方资料 | [滚动视图](../../apple-docs/zh/swiftui/scroll-views.md) | Apple 文档 | Apple · SwiftUI | [中文](../../apple-docs/zh/swiftui/scroll-views.md) | 已翻译 |
| 官方资料 | [理解可渲染颜色的像素格式大小](../../apple-docs/zh/metal/understanding-color-renderable-pixel-format-sizes.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/understanding-color-renderable-pixel-format-sizes.md) | 已翻译 |
| 官方资料 | [用 C++ 通过延迟光照渲染场景](../../apple-docs/zh/metal/rendering-a-scene-with-deferred-lighting-in-c%2B%2B.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/rendering-a-scene-with-deferred-lighting-in-c%2B%2B.md) | 已翻译 |
| 官方资料 | [用数据填充表格](../../apple-docs/zh/uikit/filling-a-table-with-data.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/filling-a-table-with-data.md) | 已翻译 |
| 官方资料 | [用更少的渲染流程渲染反射](../../apple-docs/zh/metal/rendering-reflections-with-fewer-render-passes.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/rendering-reflections-with-fewer-render-passes.md) | 已翻译 |
| 官方资料 | [自定义渲染通道设置](../../apple-docs/zh/metal/customizing-render-pass-setup.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/customizing-render-pass-setup.md) | 已翻译 |
| 官方资料 | [自定集合视图布局](../../apple-docs/zh/uikit/customizing-collection-view-layouts.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/customizing-collection-view-layouts.md) | 已翻译 |
| 官方资料 | [获取驱动视图显示的 GPU](../../apple-docs/zh/metal/getting-the-gpu-that-drives-a-views-display.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/getting-the-gpu-that-drives-a-views-display.md) | 已翻译 |
| 官方资料 | [表格视图](../../apple-docs/zh/uikit/table-views.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/table-views.md) | 已翻译 |
| 官方资料 | [视图控制器过渡](../../apple-docs/zh/uikit/view-controller-transitions.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/view-controller-transitions.md) | 已翻译 |
| 官方资料 | [训练一个神经网络以实时渲染辐照度](../../apple-docs/zh/metal/training-a-neural-network-to-render-irradiance-in-real-time.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/training-a-neural-network-to-render-irradiance-in-real-time.md) | 已翻译 |
| 官方资料 | [跨多个设备或进程同步事件](../../apple-docs/zh/metal/synchronizing-events-across-multiple-devices-or-processes.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/synchronizing-events-across-multiple-devices-or-processes.md) | 已翻译 |
| 官方资料 | [迁移到 UIKit 基于场景的生命周期](../../apple-docs/zh/uikit/transitioning-to-the-uikit-scene-based-life-cycle.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/transitioning-to-the-uikit-scene-based-life-cycle.md) | 已翻译 |
| 官方资料 | [针对 Apple GPU 和基于瓦片的延迟渲染定制你的 App](../../apple-docs/zh/metal/tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering.md) | 已翻译 |
| 官方资料 | [锁定 Storyboard 和 XIB 文件中的视图](../../apple-docs/zh/xcode/locking-views-in-storyboard-and-xib-files.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/locking-views-in-storyboard-and-xib-files.md) | 已翻译 |
| 官方资料 | [集合视图](../../apple-docs/zh/uikit/collection-views.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/collection-views.md) | 已翻译 |
| 官方资料 | [预取集合视图数据](../../apple-docs/zh/uikit/prefetching-collection-view-data.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/prefetching-collection-view-data.md) | 已翻译 |
| 官方资料 | [UIKit App 中面向协议与面向值的编程](../../wwdc/zh/wwdc2016/419-protocol-and-value-oriented-programming-in-uikit-apps.md) | WWDC | Apple · WWDC2016 | [中文](../../wwdc/zh/wwdc2016/419-protocol-and-value-oriented-programming-in-uikit-apps.md) | 已翻译 |
| 官方资料 | [使用 XCTest 消除动画卡顿](../../wwdc/zh/wwdc2020/10077-eliminate-animation-hitches-with-xctest.md) | WWDC | Apple · WWDC2020 | [中文](../../wwdc/zh/wwdc2020/10077-eliminate-animation-hitches-with-xctest.md) | 已翻译 |
| 官方资料 | [探索 UI 动画卡顿与渲染循环](../../wwdc/zh/tech-talks/10855-explore-ui-animation-hitches-and-the-render-loop.md) | WWDC | Apple · TECH-TALKS | [中文](../../wwdc/zh/tech-talks/10855-explore-ui-animation-hitches-and-the-render-loop.md) | 已翻译 |
| 官方资料 | [揭秘并消除渲染阶段中的卡顿](../../wwdc/zh/tech-talks/10857-demystify-and-eliminate-hitches-in-the-render-phase.md) | WWDC | Apple · TECH-TALKS | [中文](../../wwdc/zh/tech-talks/10857-demystify-and-eliminate-hitches-in-the-render-phase.md) | 已翻译 |
| 深度补充 | [Core Animation 中的参数化加速曲线](../../blogs/zh/cocoawithlove/parametric-acceleration-curves-in-core-animation-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/parametric-acceleration-curves-in-core-animation-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [Collection View 动画](../../blogs/zh/objccn/collection-view-%E5%8A%A8%E7%94%BB.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/collection-view-%E5%8A%A8%E7%94%BB.md) | 原生中文 |
| 深度补充 | [View Controller 容器](../../blogs/zh/objccn/view-controller-%E5%AE%B9%E5%99%A8.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/view-controller-%E5%AE%B9%E5%99%A8.md) | 原生中文 |
| 深度补充 | [View Controller 转场](../../blogs/zh/objccn/view-controller-%E8%BD%AC%E5%9C%BA.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/view-controller-%E8%BD%AC%E5%9C%BA.md) | 原生中文 |
| 深度补充 | [WWDC 2012 Session笔记——205 Introducing Collection Views](../../blogs/zh/onevcat/wwdc-2012-session%E7%AC%94%E8%AE%B0-205-introducing-collection-views.md) | 技术博客 | onevcat (王巍/喵神) | [中文](../../blogs/zh/onevcat/wwdc-2012-session%E7%AC%94%E8%AE%B0-205-introducing-collection-views.md) | 原生中文 |
| 深度补充 | [WWDC 2012 Session笔记——219 Advanced Collection Views and Building Custom Layouts](../../blogs/zh/onevcat/wwdc-2012-session%E7%AC%94%E8%AE%B0-219-advanced-collection-views-and-building-custom-layouts.md) | 技术博客 | onevcat (王巍/喵神) | [中文](../../blogs/zh/onevcat/wwdc-2012-session%E7%AC%94%E8%AE%B0-219-advanced-collection-views-and-building-custom-layouts.md) | 原生中文 |
| 深度补充 | [WWDC 2013 Session笔记 - UIKit Dynamics入门](../../blogs/zh/onevcat/wwdc-2013-session%E7%AC%94%E8%AE%B0-uikit-dynamics%E5%85%A5%E9%97%A8.md) | 技术博客 | onevcat (王巍/喵神) | [中文](../../blogs/zh/onevcat/wwdc-2013-session%E7%AC%94%E8%AE%B0-uikit-dynamics%E5%85%A5%E9%97%A8.md) | 原生中文 |
| 深度补充 | [从 UIKit 中学习](../../blogs/zh/objccn/view-layer-%E5%8D%8F%E4%BD%9C.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/view-layer-%E5%8D%8F%E4%BD%9C.md) | 原生中文 |
| 深度补充 | [从 UIKit 到 AppKit](../../blogs/zh/objccn/%E4%BB%8E-uikit-%E5%88%B0-appkit.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/%E4%BB%8E-uikit-%E5%88%B0-appkit.md) | 原生中文 |
| 深度补充 | [单向数据流动的函数式 View Controller](../../blogs/zh/onevcat/%E5%8D%95%E5%90%91%E6%95%B0%E6%8D%AE%E6%B5%81%E5%8A%A8%E7%9A%84%E5%87%BD%E6%95%B0%E5%BC%8F-view-controller.md) | 技术博客 | onevcat (王巍/喵神) | [中文](../../blogs/zh/onevcat/%E5%8D%95%E5%90%91%E6%95%B0%E6%8D%AE%E6%B5%81%E5%8A%A8%E7%9A%84%E5%87%BD%E6%95%B0%E5%BC%8F-view-controller.md) | 原生中文 |
| 深度补充 | [整洁的 Table View 代码](../../blogs/zh/objccn/%E6%95%B4%E6%B4%81%E7%9A%84-table-view-%E4%BB%A3%E7%A0%81.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/%E6%95%B4%E6%B4%81%E7%9A%84-table-view-%E4%BB%A3%E7%A0%81.md) | 原生中文 |
| 深度补充 | [测试 View Controllers](../../blogs/zh/objccn/%E6%B5%8B%E8%AF%95-view-controllers.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/%E6%B5%8B%E8%AF%95-view-controllers.md) | 原生中文 |
| 深度补充 | [理解 Scroll Views](../../blogs/zh/objccn/%E7%90%86%E8%A7%A3-scroll-views.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/%E7%90%86%E8%A7%A3-scroll-views.md) | 原生中文 |
| 深度补充 | [自定义 Collection View 布局](../../blogs/zh/objccn/%E8%87%AA%E5%AE%9A%E4%B9%89-collection-view-%E5%B8%83%E5%B1%80.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/%E8%87%AA%E5%AE%9A%E4%B9%89-collection-view-%E5%B8%83%E5%B1%80.md) | 原生中文 |
| 补充资料 | [UIKit DiffableDataSource API 与 Swift Concurrency 注解的不一致性解析](../../blogs/zh/jessesquires/uikit-diffabledatasource-api-inconsistencies-with-swift-concurrency-annotations-explained.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/uikit-diffabledatasource-api-inconsistencies-with-swift-concurrency-annotations-explained.md) | 已翻译 |
| 补充资料 | [UIKit: UIApearance](../../blogs/zh/southpeak/uikit-uiapearance.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/uikit-uiapearance.md) | 原生中文 |
| 补充资料 | [UIKit: UIControl](../../blogs/zh/southpeak/uikit-uicontrol.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/uikit-uicontrol.md) | 原生中文 |
| 补充资料 | [UIKit: UIImage](../../blogs/zh/southpeak/uikit-uiimage.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/uikit-uiimage.md) | 原生中文 |
| 补充资料 | [UIKit: UIResponder](../../blogs/zh/southpeak/uikit-uiresponder.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/uikit-uiresponder.md) | 原生中文 |
| 补充资料 | [如何发现并修复 iOS 上视图控制器过早加载的问题](../../blogs/zh/jessesquires/how-to-find-and-fix-premature-view-controller-loading-on-ios.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/how-to-find-and-fix-premature-view-controller-loading-on-ios.md) | 已翻译 |
| 补充资料 | [实现高滚动性能](../../blogs/zh/fbeng/delivering-high-scroll-performance.md) | 技术博客 | Meta Engineering — iOS | [中文](../../blogs/zh/fbeng/delivering-high-scroll-performance.md) | 已翻译 |
| 补充资料 | [将 SwiftUI 视图渲染为 HTML](../../blogs/zh/worthdoingbadly/rendering-swiftui-views-to-html.md) | 技术博客 | worthdoingbadly (Zhuowei Zhang) | [中文](../../blogs/zh/worthdoingbadly/rendering-swiftui-views-to-html.md) | 已翻译 |

## 未翻译资料

共 157 份。可能已有中文目录标题，但正文仍为英文。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [动画详解](../../blogs/en/objcio/animations-explained.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/animations-explained.md) | 仅标题中文，正文待翻译 |
| 计划核心 | [整洁的 Table View 代码](../../blogs/en/objcio/clean-table-view-code.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/clean-table-view-code.md) | 仅标题中文，正文待翻译 |
| 官方资料 | [Adding a background to your view](../../apple-docs/en/swiftui/adding-a-background-to-your-view.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/adding-a-background-to-your-view.md) | 待翻译 |
| 官方资料 | [Aligning views across stacks](../../apple-docs/en/swiftui/aligning-views-across-stacks.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/aligning-views-across-stacks.md) | 待翻译 |
| 官方资料 | [Aligning views within a stack](../../apple-docs/en/swiftui/aligning-views-within-a-stack.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/aligning-views-within-a-stack.md) | 待翻译 |
| 官方资料 | [Animations](../../apple-docs/en/technologyoverviews/animations.md) | Apple 文档 | Apple · Technology Overviews | [英文](../../apple-docs/en/technologyoverviews/animations.md) | 待翻译 |
| 官方资料 | [Animations](../../apple-docs/en/swiftui/animations.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/animations.md) | 待翻译 |
| 官方资料 | [AppEntityAnnotatable Implementations](../../apple-docs/en/uikit/uiview/appentityannotatable-implementations.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/uiview/appentityannotatable-implementations.md) | 待翻译 |
| 官方资料 | [Applying Liquid Glass to custom views](../../apple-docs/en/swiftui/applying-liquid-glass-to-custom-views.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/applying-liquid-glass-to-custom-views.md) | 待翻译 |
| 官方资料 | [Auxiliary view modifiers](../../apple-docs/en/swiftui/view-auxiliary-views.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/view-auxiliary-views.md) | 待翻译 |
| 官方资料 | [Building layouts with stack views](../../apple-docs/en/swiftui/building-layouts-with-stack-views.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/building-layouts-with-stack-views.md) | 待翻译 |
| 官方资料 | [Capturing thumbnail and preview images](../../apple-docs/en/avfoundation/capturing-thumbnail-and-preview-images.md) | Apple 文档 | Apple · AVFoundation | [英文](../../apple-docs/en/avfoundation/capturing-thumbnail-and-preview-images.md) | 待翻译 |
| 官方资料 | [CGPDFOperatorTable](../../apple-docs/en/coregraphics/cgpdfoperatortable.md) | Apple 文档 | Apple · Core Graphics | [英文](../../apple-docs/en/coregraphics/cgpdfoperatortable.md) | 待翻译 |
| 官方资料 | [Chart view modifiers](../../apple-docs/en/swiftui/view-chart-view.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/view-chart-view.md) | 待翻译 |
| 官方资料 | [Configuring views](../../apple-docs/en/swiftui/configuring-views.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/configuring-views.md) | 待翻译 |
| 官方资料 | [Controlling the timing and movements of your animations](../../apple-docs/en/swiftui/controlling-the-timing-and-movements-of-your-animations.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/controlling-the-timing-and-movements-of-your-animations.md) | 待翻译 |
| 官方资料 | [Core Animation](../../apple-docs/en/quartzcore.md) | Apple 文档 | Apple · Core Animation | [英文](../../apple-docs/en/quartzcore.md) | 待翻译 |
| 官方资料 | [Core Animation Constants](../../apple-docs/en/quartzcore/core-animation-constants.md) | Apple 文档 | Apple · Core Animation | [英文](../../apple-docs/en/quartzcore/core-animation-constants.md) | 待翻译 |
| 官方资料 | [Core Animation Data Types](../../apple-docs/en/quartzcore/core-animation-data-types.md) | Apple 文档 | Apple · Core Animation | [英文](../../apple-docs/en/quartzcore/core-animation-data-types.md) | 待翻译 |
| 官方资料 | [Core Animation Structures](../../apple-docs/en/quartzcore/core-animation-structures.md) | Apple 文档 | Apple · Core Animation | [英文](../../apple-docs/en/quartzcore/core-animation-structures.md) | 待翻译 |
| 官方资料 | [Creating a 3D application with hydra rendering](../../apple-docs/en/metal/creating-a-3d-application-with-hydra-rendering.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/creating-a-3d-application-with-hydra-rendering.md) | 待翻译 |
| 官方资料 | [Creating a custom Metal view](../../apple-docs/en/metal/creating-a-custom-metal-view.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/creating-a-custom-metal-view.md) | 待翻译 |
| 官方资料 | [Creating accessible views](../../apple-docs/en/swiftui/creating-accessible-views.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/creating-accessible-views.md) | 待翻译 |
| 官方资料 | [Creating custom container views](../../apple-docs/en/swiftui/creating-custom-container-views.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/creating-custom-container-views.md) | 待翻译 |
| 官方资料 | [Creating custom views for Live Activities](../../apple-docs/en/activitykit/creating-custom-views-for-live-activities.md) | Apple 文档 | Apple · ActivityKit | [英文](../../apple-docs/en/activitykit/creating-custom-views-for-live-activities.md) | 待翻译 |
| 官方资料 | [Creating performant scrollable stacks](../../apple-docs/en/swiftui/creating-performant-scrollable-stacks.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/creating-performant-scrollable-stacks.md) | 待翻译 |
| 官方资料 | [Creating views for widgets, Live Activities, and watch complications](../../apple-docs/en/widgetkit/creating-views-for-widgets-live-activities-and-watch-complications.md) | Apple 文档 | Apple · WidgetKit | [英文](../../apple-docs/en/widgetkit/creating-views-for-widgets-live-activities-and-watch-complications.md) | 待翻译 |
| 官方资料 | [Customizing Writing Tools behavior for UIKit views](../../apple-docs/en/uikit/customizing-writing-tools-behavior-for-system-views.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/customizing-writing-tools-behavior-for-system-views.md) | 待翻译 |
| 官方资料 | [Declaring a custom view](../../apple-docs/en/swiftui/declaring-a-custom-view.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/declaring-a-custom-view.md) | 待翻译 |
| 官方资料 | [Dismissing a view controller with an unwind segue](../../apple-docs/en/uikit/dismissing-a-view-controller-with-an-unwind-segue.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/dismissing-a-view-controller-with-an-unwind-segue.md) | 待翻译 |
| 官方资料 | [Emitter Render Order](../../apple-docs/en/quartzcore/emitter-render-order.md) | Apple 文档 | Apple · Core Animation | [英文](../../apple-docs/en/quartzcore/emitter-render-order.md) | 待翻译 |
| 官方资料 | [Emoji Rangers: Supporting Live Activities, interactivity, and animations](../../apple-docs/en/widgetkit/emoji-rangers-supporting-live-activities-interactivity-and-animations.md) | Apple 文档 | Apple · WidgetKit | [英文](../../apple-docs/en/widgetkit/emoji-rangers-supporting-live-activities-interactivity-and-animations.md) | 待翻译 |
| 官方资料 | [Enabling Password AutoFill on a text input view](../../apple-docs/en/security/enabling-password-autofill-on-a-text-input-view.md) | Apple 文档 | Apple · Security | [英文](../../apple-docs/en/security/enabling-password-autofill-on-a-text-input-view.md) | 待翻译 |
| 官方资料 | [Enhancing high dynamic range image rendering](../../apple-docs/en/coregraphics/adopting-advancements-in-hdr-image-rendering.md) | Apple 文档 | Apple · Core Graphics | [英文](../../apple-docs/en/coregraphics/adopting-advancements-in-hdr-image-rendering.md) | 待翻译 |
| 官方资料 | [Event Source Token](../../apple-docs/en/coregraphics/event-source-token.md) | Apple 文档 | Apple · Core Graphics | [英文](../../apple-docs/en/coregraphics/event-source-token.md) | 待翻译 |
| 官方资料 | [Event Type Mask](../../apple-docs/en/coregraphics/event-type-mask.md) | Apple 文档 | Apple · Core Graphics | [英文](../../apple-docs/en/coregraphics/event-type-mask.md) | 待翻译 |
| 官方资料 | [Font Table Index Values](../../apple-docs/en/coregraphics/font-table-index-values.md) | Apple 文档 | Apple · Core Graphics | [英文](../../apple-docs/en/coregraphics/font-table-index-values.md) | 待翻译 |
| 官方资料 | [Generating an animation with a Core Image Render Destination](../../apple-docs/en/coreimage/generating-an-animation-with-a-core-image-render-destination.md) | Apple 文档 | Apple · Core Image | [英文](../../apple-docs/en/coreimage/generating-an-animation-with-a-core-image-render-destination.md) | 待翻译 |
| 官方资料 | [Generating the signature to validate StoreKit-rendered ads](../../apple-docs/en/storekit/generating-the-signature-to-validate-storekit-rendered-ads.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/generating-the-signature-to-validate-storekit-rendered-ads.md) | 待翻译 |
| 官方资料 | [Generating the signature to validate view-through ads](../../apple-docs/en/storekit/generating-the-signature-to-validate-view-through-ads.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/generating-the-signature-to-validate-view-through-ads.md) | 待翻译 |
| 官方资料 | [Getting started with In-App Purchase using StoreKit views](../../apple-docs/en/storekit/getting-started-with-in-app-purchases-using-storekit-views.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/getting-started-with-in-app-purchases-using-storekit-views.md) | 待翻译 |
| 官方资料 | [Graphics and rendering modifiers](../../apple-docs/en/swiftui/view-graphics-and-rendering.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/view-graphics-and-rendering.md) | 待翻译 |
| 官方资料 | [Graphics, drawing, and animation](../../apple-docs/en/technologyoverviews/graphics-drawing-and-animation.md) | Apple 文档 | Apple · Technology Overviews | [英文](../../apple-docs/en/technologyoverviews/graphics-drawing-and-animation.md) | 待翻译 |
| 官方资料 | [Grouping data with lazy stack views](../../apple-docs/en/swiftui/grouping-data-with-lazy-stack-views.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/grouping-data-with-lazy-stack-views.md) | 待翻译 |
| 官方资料 | [Handling UIKit gestures](../../apple-docs/en/uikit/handling-uikit-gestures.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/handling-uikit-gestures.md) | 待翻译 |
| 官方资料 | [Implementing a multistage image filter using heaps and events](../../apple-docs/en/metal/implementing-a-multistage-image-filter-using-heaps-and-events.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/implementing-a-multistage-image-filter-using-heaps-and-events.md) | 待翻译 |
| 官方资料 | [Improving edge-rendering quality with multisample antialiasing (MSAA)](../../apple-docs/en/metal/improving-edge-rendering-quality-with-multisample-antialiasing-msaa.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/improving-edge-rendering-quality-with-multisample-antialiasing-msaa.md) | 待翻译 |
| 官方资料 | [Input and event modifiers](../../apple-docs/en/swiftui/view-input-and-events.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/view-input-and-events.md) | 待翻译 |
| 官方资料 | [Input events](../../apple-docs/en/swiftui/input-events.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/input-events.md) | 待翻译 |
| 官方资料 | [Inspecting view layout](../../apple-docs/en/swiftui/inspecting-view-layout.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/inspecting-view-layout.md) | 待翻译 |
| 官方资料 | [Landmarks: Extending horizontal scrolling under a sidebar or inspector](../../apple-docs/en/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector.md) | 待翻译 |
| 官方资料 | [Laying out a simple view](../../apple-docs/en/swiftui/laying-out-a-simple-view.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/laying-out-a-simple-view.md) | 待翻译 |
| 官方资料 | [Making a view into a drag source](../../apple-docs/en/uikit/making-a-view-into-a-drag-source.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/making-a-view-into-a-drag-source.md) | 待翻译 |
| 官方资料 | [Making a view into a drag source](../../apple-docs/en/swiftui/making-a-view-into-a-drag-source.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/making-a-view-into-a-drag-source.md) | 待翻译 |
| 官方资料 | [Making a view into a drop destination](../../apple-docs/en/uikit/making-a-view-into-a-drop-destination.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/making-a-view-into-a-drop-destination.md) | 待翻译 |
| 官方资料 | [Making fine adjustments to a view’s position](../../apple-docs/en/swiftui/making-fine-adjustments-to-a-view-s-position.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/making-fine-adjustments-to-a-view-s-position.md) | 待翻译 |
| 官方资料 | [Managing viewport layout and attachment reuse in text views](../../apple-docs/en/uikit/managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) | 待翻译 |
| 官方资料 | [MapKit for AppKit and UIKit](../../apple-docs/en/mapkit/mapkit-for-appkit-and-uikit.md) | Apple 文档 | Apple · MapKit | [英文](../../apple-docs/en/mapkit/mapkit-for-appkit-and-uikit.md) | 待翻译 |
| 官方资料 | [Mixing Metal and OpenGL rendering in a view](../../apple-docs/en/metal/mixing-metal-and-opengl-rendering-in-a-view.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/mixing-metal-and-opengl-rendering-in-a-view.md) | 待翻译 |
| 官方资料 | [Modern rendering with Metal](../../apple-docs/en/metal/modern-rendering-with-metal.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/modern-rendering-with-metal.md) | 待翻译 |
| 官方资料 | [Navigating Hierarchical Data Using Outline and Split Views](../../apple-docs/en/appkit/navigating-hierarchical-data-using-outline-and-split-views.md) | Apple 文档 | Apple · AppKit | [英文](../../apple-docs/en/appkit/navigating-hierarchical-data-using-outline-and-split-views.md) | 待翻译 |
| 官方资料 | [Obsolete Font Table Index Values](../../apple-docs/en/coregraphics/obsolete-font-table-index-values.md) | Apple 文档 | Apple · Core Graphics | [英文](../../apple-docs/en/coregraphics/obsolete-font-table-index-values.md) | 待翻译 |
| 官方资料 | [Optimizing your widget for accented rendering mode and Liquid Glass](../../apple-docs/en/widgetkit/optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md) | Apple 文档 | Apple · WidgetKit | [英文](../../apple-docs/en/widgetkit/optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md) | 待翻译 |
| 官方资料 | [Picking container views for your content](../../apple-docs/en/swiftui/picking-container-views-for-your-content.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/picking-container-views-for-your-content.md) | 待翻译 |
| 官方资料 | [Preparing views for localization](../../apple-docs/en/swiftui/preparing-views-for-localization.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/preparing-views-for-localization.md) | 待翻译 |
| 官方资料 | [Previews in Xcode](../../apple-docs/en/swiftui/previews-in-xcode.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/previews-in-xcode.md) | 待翻译 |
| 官方资料 | [Property-based animations](../../apple-docs/en/uikit/property-based-animations.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/property-based-animations.md) | 待翻译 |
| 官方资料 | [Providing an integrated view of your timeline when playing HLS interstitials](../../apple-docs/en/avfoundation/providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.md) | Apple 文档 | Apple · AVFoundation | [英文](../../apple-docs/en/avfoundation/providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.md) | 待翻译 |
| 官方资料 | [Quartz Event Services](../../apple-docs/en/coregraphics/quartz-event-services.md) | Apple 文档 | Apple · Core Graphics | [英文](../../apple-docs/en/coregraphics/quartz-event-services.md) | 待翻译 |
| 官方资料 | [Reducing view modifier maintenance](../../apple-docs/en/swiftui/reducing-view-modifier-maintenance.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/reducing-view-modifier-maintenance.md) | 待翻译 |
| 官方资料 | [Rendering terrain dynamically with argument buffers](../../apple-docs/en/metal/rendering-terrain-dynamically-with-argument-buffers.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/rendering-terrain-dynamically-with-argument-buffers.md) | 待翻译 |
| 官方资料 | [Rendering to multiple texture slices in a draw command](../../apple-docs/en/metal/rendering-to-multiple-texture-slices-in-a-draw-command.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/rendering-to-multiple-texture-slices-in-a-draw-command.md) | 待翻译 |
| 官方资料 | [Rendering to multiple viewports in a draw command](../../apple-docs/en/metal/rendering-to-multiple-viewports-in-a-draw-command.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/rendering-to-multiple-viewports-in-a-draw-command.md) | 待翻译 |
| 官方资料 | [Rendering with a rasterization rate map](../../apple-docs/en/metal/rendering-with-a-rasterization-rate-map.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/rendering-with-a-rasterization-rate-map.md) | 待翻译 |
| 官方资料 | [Scroll Modes](../../apple-docs/en/quartzcore/scroll-modes.md) | Apple 文档 | Apple · Core Animation | [英文](../../apple-docs/en/quartzcore/scroll-modes.md) | 待翻译 |
| 官方资料 | [Selecting device objects for graphics rendering](../../apple-docs/en/metal/selecting-device-objects-for-graphics-rendering.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/selecting-device-objects-for-graphics-rendering.md) | 待翻译 |
| 官方资料 | [Showing help tags for views and controls using tooltip interactions](../../apple-docs/en/uikit/showing-help-tags-for-views-and-controls-using-tooltip-interactions.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/showing-help-tags-for-views-and-controls-using-tooltip-interactions.md) | 待翻译 |
| 官方资料 | [StoreKit views](../../apple-docs/en/storekit/storekit-views.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/storekit-views.md) | 待翻译 |
| 官方资料 | [SwiftUI views for widgets](../../apple-docs/en/widgetkit/swiftui-views.md) | Apple 文档 | Apple · WidgetKit | [英文](../../apple-docs/en/widgetkit/swiftui-views.md) | 待翻译 |
| 官方资料 | [System events](../../apple-docs/en/swiftui/system-events.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/system-events.md) | 待翻译 |
| 官方资料 | [Tables](../../apple-docs/en/swiftui/tables.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/tables.md) | 待翻译 |
| 官方资料 | [Technology-specific views](../../apple-docs/en/swiftui/technology-specific-views.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/technology-specific-views.md) | 待翻译 |
| 官方资料 | [Tracking the force of 3D Touch events](../../apple-docs/en/uikit/tracking-the-force-of-3d-touch-events.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/tracking-the-force-of-3d-touch-events.md) | 待翻译 |
| 官方资料 | [UIDragPreview Implementations](../../apple-docs/en/uikit/uidragpreview/uidragpreview-implementations.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/uidragpreview/uidragpreview-implementations.md) | 待翻译 |
| 官方资料 | [UIKit](../../apple-docs/en/uikit.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit.md) | 待翻译 |
| 官方资料 | [UIKit and AppKit apps](../../apple-docs/en/technologyoverviews/uikit-appkit.md) | Apple 文档 | Apple · Technology Overviews | [英文](../../apple-docs/en/technologyoverviews/uikit-appkit.md) | 待翻译 |
| 官方资料 | [UIKit integration](../../apple-docs/en/swiftui/uikit-integration.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/uikit-integration.md) | 待翻译 |
| 官方资料 | [UIKit updates](../../apple-docs/en/updates/uikit.md) | Apple 文档 | Apple · Updates | [英文](../../apple-docs/en/updates/uikit.md) | 待翻译 |
| 官方资料 | [UITargetedDragPreview Implementations](../../apple-docs/en/uikit/uitargeteddragpreview/uitargeteddragpreview-implementations.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/uitargeteddragpreview/uitargeteddragpreview-implementations.md) | 待翻译 |
| 官方资料 | [Understanding the visionOS render pipeline](../../apple-docs/en/visionos/understanding-the-visionos-render-pipeline.md) | Apple 文档 | Apple · updates | [英文](../../apple-docs/en/visionos/understanding-the-visionos-render-pipeline.md) | 待翻译 |
| 官方资料 | [Unifying your app’s animations](../../apple-docs/en/swiftui/unifying-your-app-s-animations.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/unifying-your-app-s-animations.md) | 待翻译 |
| 官方资料 | [Using Metal to draw a view’s contents](../../apple-docs/en/metal/using-metal-to-draw-a-view%27s-contents.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/using-metal-to-draw-a-view%27s-contents.md) | 待翻译 |
| 官方资料 | [View configuration](../../apple-docs/en/swiftui/view-configuration.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/view-configuration.md) | 待翻译 |
| 官方资料 | [View controllers](../../apple-docs/en/uikit/view-controllers.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/view-controllers.md) | 待翻译 |
| 官方资料 | [View fundamentals](../../apple-docs/en/swiftui/view-fundamentals.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/view-fundamentals.md) | 待翻译 |
| 官方资料 | [View groupings](../../apple-docs/en/swiftui/view-groupings.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/view-groupings.md) | 待翻译 |
| 官方资料 | [View layout](../../apple-docs/en/uikit/view-layout.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/view-layout.md) | 待翻译 |
| 官方资料 | [View styles](../../apple-docs/en/swiftui/view-styles.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/view-styles.md) | 待翻译 |
| 官方资料 | [Views and controls](../../apple-docs/en/uikit/views-and-controls.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/views-and-controls.md) | 待翻译 |
| 官方资料 | [A Tour of UICollectionView](../../wwdc/en/wwdc2018/225-a-tour-of-uicollectionview.md) | WWDC | Apple · WWDC2018 | [英文](../../wwdc/en/wwdc2018/225-a-tour-of-uicollectionview.md) | 待翻译 |
| 官方资料 | [Advances in Collection View Layout](../../wwdc/en/wwdc2019/215-advances-in-collection-view-layout.md) | WWDC | Apple · WWDC2019 | [英文](../../wwdc/en/wwdc2019/215-advances-in-collection-view-layout.md) | 待翻译 |
| 官方资料 | [Advances in UICollectionView](../../wwdc/en/wwdc2020/10097-advances-in-uicollectionview.md) | WWDC | Apple · WWDC2020 | [英文](../../wwdc/en/wwdc2020/10097-advances-in-uicollectionview.md) | 待翻译 |
| 官方资料 | [Beyond scroll views](../../wwdc/en/wwdc2023/10159-beyond-scroll-views.md) | WWDC | Apple · WWDC2023 | [英文](../../wwdc/en/wwdc2023/10159-beyond-scroll-views.md) | 待翻译 |
| 官方资料 | [Dive into lazy stacks and scrolling with SwiftUI](../../wwdc/en/wwdc2026/321-dive-into-lazy-stacks-and-scrolling-with-swiftui.md) | WWDC | Apple · WWDC2026 | [英文](../../wwdc/en/wwdc2026/321-dive-into-lazy-stacks-and-scrolling-with-swiftui.md) | 待翻译 |
| 官方资料 | [Explore SwiftUI animation](../../wwdc/en/wwdc2023/10156-explore-swiftui-animation.md) | WWDC | Apple · WWDC2023 | [英文](../../wwdc/en/wwdc2023/10156-explore-swiftui-animation.md) | 待翻译 |
| 官方资料 | [Lists in UICollectionView](../../wwdc/en/wwdc2020/10026-lists-in-uicollectionview.md) | WWDC | Apple · WWDC2020 | [英文](../../wwdc/en/wwdc2020/10026-lists-in-uicollectionview.md) | 待翻译 |
| 官方资料 | [Make blazing fast lists and collection views](../../wwdc/en/wwdc2021/10252-make-blazing-fast-lists-and-collection-views.md) | WWDC | Apple · WWDC2021 | [英文](../../wwdc/en/wwdc2021/10252-make-blazing-fast-lists-and-collection-views.md) | 待翻译 |
| 官方资料 | [Unleash the UIKit trait system](../../wwdc/en/wwdc2023/10057-unleash-the-uikit-trait-system.md) | WWDC | Apple · WWDC2023 | [英文](../../wwdc/en/wwdc2023/10057-unleash-the-uikit-trait-system.md) | 待翻译 |
| 官方资料 | [What's new in TextKit and text views](../../wwdc/en/wwdc2022/10090-what-s-new-in-textkit-and-text-views.md) | WWDC | Apple · WWDC2022 | [英文](../../wwdc/en/wwdc2022/10090-what-s-new-in-textkit-and-text-views.md) | 待翻译 |
| 官方资料 | [What’s new in UIKit](../../wwdc/en/wwdc2023/10055-what-s-new-in-uikit.md) | WWDC | Apple · WWDC2023 | [英文](../../wwdc/en/wwdc2023/10055-what-s-new-in-uikit.md) | 待翻译 |
| 深度补充 | [Collection View 动画](../../blogs/en/objcio/animating-collection-views.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/animating-collection-views.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [macOS Catalina 和 Xcode 11 上的 SwiftUI 预览](../../blogs/en/nshipster/swiftui-previews-on-macos-catalina-and-xcode-11.md) | 技术博客 | NSHipster (Mattt) | [英文](../../blogs/en/nshipster/swiftui-previews-on-macos-catalina-and-xcode-11.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [UIActivityViewController](../../blogs/en/nshipster/uiactivityviewcontroller.md) | 技术博客 | NSHipster (Mattt) | [英文](../../blogs/en/nshipster/uiactivityviewcontroller.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [UICollectionView](../../blogs/en/nshipster/uicollectionview.md) | 技术博客 | NSHipster (Mattt) | [英文](../../blogs/en/nshipster/uicollectionview.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [UICollectionView + UIKit Dynamics](../../blogs/en/objcio/uicollectionview-uikit-dynamics.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/uicollectionview-uikit-dynamics.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [UISplitViewController](../../blogs/en/nshipster/uisplitviewcontroller.md) | 技术博客 | NSHipster (Mattt) | [英文](../../blogs/en/nshipster/uisplitviewcontroller.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [UIStackView](../../blogs/en/nshipster/uistackview.md) | 技术博客 | NSHipster (Mattt) | [英文](../../blogs/en/nshipster/uistackview.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [UITableViewHeaderFooterView](../../blogs/en/nshipster/uitableviewheaderfooterview.md) | 技术博客 | NSHipster (Mattt) | [英文](../../blogs/en/nshipster/uitableviewheaderfooterview.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [WKWebView](../../blogs/en/nshipster/wkwebview.md) | 技术博客 | NSHipster (Mattt) | [英文](../../blogs/en/nshipster/wkwebview.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [一种视图构建语法](../../blogs/en/cocoawithlove/a-view-construction-syntax-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/a-view-construction-syntax-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [交互式动画](../../blogs/en/objcio/interactive-animations.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/interactive-animations.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [仅用 2 个子视图在 UIScrollView 中实现多虚拟页面 \| Cocoa with Love](../../blogs/en/cocoawithlove/multiple-virtual-pages-in-a-uiscrollview-with-just-2-child-views-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/multiple-virtual-pages-in-a-uiscrollview-with-just-2-child-views-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [从 NIB 加载还是在代码中构造视图：哪个更快？ \| Cocoa with Love](../../blogs/en/cocoawithlove/load-from-nib-or-construct-views-in-code-which-is-faster-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/load-from-nib-or-construct-views-in-code-which-is-faster-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [优化 iPhone 上超大表格的加载 \| Cocoa with Love](../../blogs/en/cocoawithlove/optimizing-the-loading-of-a-very-large-table-on-the-iphone-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/optimizing-the-loading-of-a-very-large-table-on-the-iphone-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [使用 IBPlugins 在 Interface Builder 中创建自定义视图](../../blogs/en/cocoawithlove/custom-views-in-interface-builder-using-ibplugins-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/custom-views-in-interface-builder-using-ibplugins-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [受 React 启发的视图](../../blogs/en/objcio/react-inspired-views.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/react-inspired-views.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [声明式视图](../../blogs/en/cocoawithlove/declarative-views-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/declarative-views-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [字符串渲染](../../blogs/en/objcio/string-rendering.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/string-rendering.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [没有控制器的模型-视图-控制器 \| Cocoa with Love](../../blogs/en/cocoawithlove/model-view-controller-without-the-controller-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/model-view-controller-without-the-controller-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [浅析 Cocoa 中的模型-视图-控制器 \| Cocoa with Love](../../blogs/en/cocoawithlove/looking-at-model-view-controller-in-cocoa-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/looking-at-model-view-controller-in-cocoa-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [测试视图控制器](../../blogs/en/objcio/testing-view-controllers.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/testing-view-controllers.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [理解滚动视图](../../blogs/en/objcio/understanding-scroll-views.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/understanding-scroll-views.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [用绑定设计视图（Mac 上的 UITableView）](../../blogs/en/cocoawithlove/designing-a-view-with-bindings-uitableview-on-the-mac-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/designing-a-view-with-bindings-uitableview-on-the-mac-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [自定义容器视图控制器转场](../../blogs/en/objcio/custom-container-view-controller-transitions.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/custom-container-view-controller-transitions.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [自定义集合视图布局](../../blogs/en/objcio/custom-collection-view-layouts.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/custom-collection-view-layouts.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [视图与层的协同](../../blogs/en/objcio/view-layer-synergy.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/view-layer-synergy.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [视图控制器包含](../../blogs/en/objcio/view-controller-containment.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/view-controller-containment.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [视图控制器转场](../../blogs/en/objcio/view-controller-transitions.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/view-controller-transitions.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [视图状态驱动的应用程序 \| Cocoa with Love](../../blogs/en/cocoawithlove/view-state-driven-applications-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/view-state-driven-applications-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [面向 UIKit 开发者的 AppKit](../../blogs/en/objcio/appkit-for-uikit-developers.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/appkit-for-uikit-developers.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [2018 年 11 月 2 日 React Conf 回顾：Hooks、Suspense 和 Concurrent Rendering](../../blogs/en/fbeng/nov-02-2018-react-conf-recap-hooks-suspense-and-concurrent-rendering.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/nov-02-2018-react-conf-recap-hooks-suspense-and-concurrent-rendering.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [App Store 安全的翻页动画](../../blogs/en/oleb/app-store-safe-page-curl-animations.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/app-store-safe-page-curl-animations.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [iOS 6 中的远程视图控制器](../../blogs/en/oleb/remote-view-controllers-in-ios-6.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/remote-view-controllers-in-ios-6.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [iOS 9 中的 UIKit 变化](../../blogs/en/jessesquires/uikit-changes-in-ios-9.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/uikit-changes-in-ios-9.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Keyframes：向移动客户端交付可扩展的高质量动画](../../blogs/en/fbeng/keyframes-delivering-scalable-high-quality-animations-to-mobile-clients.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/keyframes-delivering-scalable-high-quality-animations-to-mobile-clients.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Swifty 视图控制器展示器](../../blogs/en/jessesquires/swifty-view-controller-presenters.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/swifty-view-controller-presenters.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [为 Instagram Stories 构建文字动画](../../blogs/en/fbeng/building-text-animations-for-instagram-stories.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/building-text-animations-for-instagram-stories.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [介绍 Pop：Paper 背后的动画引擎](../../blogs/en/fbeng/introducing-pop-the-animation-engine-behind-paper.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/introducing-pop-the-animation-engine-behind-paper.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [优化集合](../../blogs/en/oleb/optimizing-collections.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/optimizing-collections.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [在视图控制器之间传递数据](../../blogs/en/oleb/passing-data-between-view-controllers.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/passing-data-between-view-controllers.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [如何使用 VariadicView，SwiftUI 的私有 View API](../../blogs/en/emergetools/emerge-tools-blog-how-to-use-variadicview-swiftui-s-private-view-api.md) | 技术博客 | Emerge Tools Blog | [英文](../../blogs/en/emergetools/emerge-tools-blog-how-to-use-variadicview-swiftui-s-private-view-api.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [如何在 iOS 和 macOS 的文本视图中防止孤词](../../blogs/en/jessesquires/how-to-prevent-orphan-words-in-text-views-on-ios-and-macos.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/how-to-prevent-orphan-words-in-text-views-on-ios-and-macos.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [如何在 SwiftUI 中自定义 NavigationLink 辅助视图](../../blogs/en/jessesquires/how-to-customize-navigationlink-accessory-views-in-swiftui.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/how-to-customize-navigationlink-accessory-views-in-swiftui.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [更多关于远程视图控制器](../../blogs/en/oleb/more-on-remote-view-controllers.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/more-on-remote-view-controllers.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [滚动视图嵌套滚动视图](../../blogs/en/oleb/scroll-views-inside-scroll-views.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/scroll-views-inside-scroll-views.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [虚拟滚动：无延迟渲染数百万条消息 \| Kreya](../../blogs/en/kreya/virtual-scrolling-rendering-millions-of-messages-without-lag-kreya.md) | 技术博客 | Kreya Blog | [英文](../../blogs/en/kreya/virtual-scrolling-rendering-millions-of-messages-without-lag-kreya.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [远程视图控制器更新](../../blogs/en/oleb/update-on-remote-view-controllers.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/update-on-remote-view-controllers.md) | 仅标题中文，正文待翻译 |
