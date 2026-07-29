---
title: 'Xcode 提示：过滤调试器输出'
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2023/03/02/xcode-tip-filter-console/'
original_language: en
published: 2023-03-02
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:be8ab5fbe84fa9ac'
translated: true
---

> 原文：[Xcode Tip: filtering debugger output](https://www.jessesquires.com/blog/2023/03/02/xcode-tip-filter-console/)　·　Jesse Squires

在 Xcode 中调试一个大型团队共同开发的大项目时，控制台（console）可能会变得非常繁忙。到处都是日志！要从这些杂乱信息中筛选出有用的内容相当困难，尤其在你配置了大量断点（breakpoint）来记录消息、执行调试器命令、并在评估后继续运行而非暂停时。

你可以在我[之前的文章](https://www.jessesquires.com/blog/2023/02/20/ios-view-controller-loading/)中找到一个很好的例子，我演示了如何使用符号断点（symbolic breakpoint）来调试视图控制器（view controller）加载。如果你能隐藏控制台中发生的所有其他日志，只专注于调试，那岂不是很好？你可以！在 Xcode 的调试控制台中，你可以选择左下角菜单中的“调试器输出（Debugger Output）”选项。选中后，控制台中你将只会看到来自断点的日志和输出，以及你手动执行的任何调试器命令。

![在 Xcode 中过滤调试器输出](https://www.jessesquires.com/img/blog/xcode-debug-filter.jpg)

<sub>在 Xcode 中过滤调试器输出</sub>
