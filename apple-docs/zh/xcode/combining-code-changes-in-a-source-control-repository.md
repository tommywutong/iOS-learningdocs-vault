---
title: 在源代码管理仓库中合并代码更改
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/combining-code-changes-in-a-source-control-repository
source_url: 'https://developer.apple.com/documentation/xcode/combining-code-changes-in-a-source-control-repository'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/combining-code-changes-in-a-source-control-repository.json'
content_hash: 'sha256:9ce704ebe52852e6'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [源代码管理](source-control-management.md)

# 在源代码管理仓库中合并代码更改

<sub>文章</sub>

使用 Xcode 中的源代码管理工具，整合来自多个来源的代码更改并解决代码不同版本之间的冲突（conflict）。

## 概述

如果你使用源代码管理与协作者一同处理代码，或者为不同的发布管理 Xcode 项目的多个版本，那么最终你需要同步各版本之间的代码更改。Git 源代码管理提供了一种机制，通过将这些更改合并在一起，来组合多组代码更改，而 Xcode 则提供了一个用于执行 _合并_ 的可视化界面。

![](../../../attachments/357f965f3904cf401c393b515a8084dd/combining-code-changes-in-a-source-control-repository-1@2x.png)

<sub>概念示意图，显示两行提交，每行代表一个分支。下面一行最右边的提交合并到上面一行，以说明两次提交合并在一起。</sub>

### 合并代码更改

在完成某个功能或 Bug 修复分支的工作后，你需要将更改合并到主开发分支或生产分支中。或者，你也可以将主开发分支或生产分支中的其他更新合并到你的功能或 Bug 修复分支中，以解决冲突，或使你的工作与最新更新同步，并确保所有内容在合并回主开发分支或生产分支之前都能正常运行。

1. 打开源代码管理导航器（Source Control navigator），然后选择“仓库”（Repositories）。
2. 在仓库导航器（Repositories navigator）中，展开你的仓库以及“分支”（Branches）或“远程”（Remotes）文件夹。
3. 若要将你想合并到的分支设为当前分支，请按住 Control 键单击该分支，然后选择“切换”（Switch）。
4. 按住 Control 键单击你要从中合并的分支，然后选择“将 [来源分支] 合并到 [目标分支]”（Merge [_from branch_] into [_to branch_]）。

如果没有冲突，Xcode 会完成合并。

### 解决与其他代码的冲突

在源代码管理仓库中，当两次提交存在不兼容的更改，且 Git 无法自动合并这些更改时，就会发生冲突。例如，当两名开发者在同一源文件的同一行进行了修改时，就可能发生冲突。

如果你在 Xcode 中尝试合并更改时遇到冲突，Xcode 会显示一个比较视图，供你审查并解决冲突。

![](../../../attachments/e0ce932cdaeac8afdbeb8d36974c762e/combining-code-changes-in-a-source-control-repository-2@2x.png)

<sub>Xcode 合并冲突视图，显示要合并的文件列表，并高亮显示存在冲突的文件。该视图显示了冲突内容，以及你用于选择冲突解决方式的按钮。该视图还高亮显示了用于在文件的冲突之间进行导航的选项。</sub>

要解决冲突，请点击该冲突的问号 (?)，该问号出现在文件左侧和右侧版本之间的装订线中，然后选择要用于解决冲突的选项：

- 选择左侧（Choose Left）
- 选择右侧（Choose Right）
- 先选左侧再选右侧（Choose Left Then Right）
- 先选右侧再选左侧（Choose Right Then Left）

在你为每个冲突选择了解决方式后，Xcode 会启用“合并”（Merge）按钮。点击“合并”按钮可完成合并，或点击“取消”（Cancel）按钮可中止合并并恢复你的分支，以便你在合并前进行更多更改。

## 另请参阅

### Git

- [使用源代码管理组织代码更改](organizing-your-code-changes-with-source-control.md) — 使用 Git 分支和标签来简化协作并管理功能和发布。
- [在 Xcode 中配置源代码管理](configuring-source-control-in-xcode.md) — 自定义默认的 Xcode 设置，以连接到 Git 仓库、应用代码更改以及配置源代码管理的更多选项。
