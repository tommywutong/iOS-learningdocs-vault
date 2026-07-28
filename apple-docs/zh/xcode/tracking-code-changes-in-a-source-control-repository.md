---
title: 在源代码管理仓库中跟踪代码更改
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/tracking-code-changes-in-a-source-control-repository
source_url: 'https://developer.apple.com/documentation/xcode/tracking-code-changes-in-a-source-control-repository'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/tracking-code-changes-in-a-source-control-repository.json'
content_hash: 'sha256:52ca90575456949a'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [源代码管理](source-control-management.md)

# 在源代码管理仓库中跟踪代码更改

<sub>文章</sub>

使用提交（commit）并推送到远程仓库（remote repository）来创建项目增量更改的历史记录。

## 概述

当你使用源代码管理仓库（source control repository）管理 Xcode 项目时，可以将更改保存到仓库中，这些更改以增量状态的形式称为提交（commit）。*提交*包含项目在特定时间点的状态快照（snapshot）、描述上一状态到当前状态更改集的消息，以及额外的元数据，例如标识该提交的唯一哈希值。

![](../../../attachments/e531630d352ad4ce907bcbff40ded594/tracking-code-changes-in-a-source-control-repository-1@2x.png)

<sub>概念图，展示一行四个提交。最右侧的提交包含一个标签，描述了该提交的一些信息，包括提交哈希值、提交消息和作者姓名。</sub>

首先，暂存（stage）你要包含在提交中的项目文件更改。对于本地仓库，然后提交更改；对于远程仓库，你需要同时提交并远程推送更改。之后，你可以浏览提交历史、比较特定提交之间的更改，并快速将项目恢复到某个提交时的状态。

### 在项目导航器和源代码编辑器中查看更改

当你对项目文件进行更改时，Xcode 会跟踪这些更改，并在项目导航器（Project navigator）和源代码编辑器（source editor）中标记它们。

- 项目导航器使用 *A*（新文件）或 *M*（已修改文件）来标注自上次提交以来有更改的文件。
- 源代码编辑器会在装订线中显示更改条（change bar）。

如果悬停在更改条上，源代码编辑器会高亮显示你更改的行以及行中的文本。然后，使用更改条的弹出菜单来显示、暂存或丢弃你所做的更改。

![](../../../attachments/7affe3996ef78ab4b3cb48055ad070b0/tracking-code-changes-in-a-source-control-repository-2@2x.png)

<sub>项目编辑器（Project editor）的截图，显示项目导航器中标注了已修改的文件和一个新文件。源代码编辑器高亮显示了更改的文件行，并显示一个弹出菜单，该菜单在单击装订线中的更改条时出现。</sub>

### 在源代码编辑器中比较更改

要比较你对某个文件所做的更改，请在项目导航器中选择该文件，然后单击源代码编辑器右上角的“启用代码审核”（Enable Code Review）按钮（查看（View） > 显示代码审核）。源代码编辑器会切换到一个比较视图，高亮显示当前文件与最近一次提交之间的更改。

默认情况下，源代码编辑器会以内联方式比较更改。要在编辑器区域中以独立视图查看更改，请从“启用代码审核”按钮旁边的“调整编辑器选项”（Adjust Editor Options）按钮中选择“并排比较”（Side by Side Comparison）。

![](../../../attachments/905278a56760d5b8e09e91abea6c4d70/tracking-code-changes-in-a-source-control-repository-3@2x.png)

<sub>项目编辑器的截图，左侧显示项目导航器，右侧显示比较视图。该视图展示了并排比较，高亮显示了左侧当前本地版本与右侧上次提交之间的更改。</sub>

要直接在源代码编辑器中查看更改，请改为选择“内联比较”（Inline Comparison）。

然后，使用比较视图底部的控件来浏览文件中的更改，并选择其他提交与当前更改进行比较。

### 暂存要提交的更改

在将更改永久保存到源代码管理仓库之前，请先审查项目文件的所有更改。

选择“集成”（Integrate）>“提交”（Commit），Xcode 会打开源代码管理导航器（Source Control navigator），并选中“更改”（Changes）标签页。使用右侧详细信息区域中的控件来暂存你要包含在提交中的更改。

![](../../../attachments/041b3589acf83e56aa18c61230df6300/tracking-code-changes-in-a-source-control-repository-4@2x.png)

<sub>项目编辑器的截图，左侧显示源代码管理导航器并选中“更改”标签页，右侧高亮显示对所选文件的更改，上方有“暂存全部”（Stage All）按钮和提交消息文本字段。</sub>

滚动详细信息区域以查看对所有文件的更改，或在导航器中选择一个文件以跳转到特定文件的更改。

要包含提交中的所有更改，只需单击“暂存全部”按钮。否则，在详细信息区域中审阅更改时，挑选要包含的更改。你仍然可以在提交前从该编辑器修改看到的文件，例如删除无意中添加的更改。

使用工具栏控件，你可以执行以下操作：

- 要筛选文件，请单击“所有更改”（All Changes）、“未暂存”（Unstaged）或“已暂存”（Staged）标签页。
- 要切换是否暂存所有更改，请单击标签页右侧的“暂存全部”或“取消暂存全部”（Unstage All）按钮。

使用文件标题上显示的控件，你可以执行以下操作：

- 要隐藏或显示文件，请单击文件名左侧的展开三角形。
- 要仅显示更改或整个文件，请单击文件名右侧的“折叠/展开文件”（Collapse/Expand File）按钮。
- 要暂存或取消暂存某个文件的所有更改，请单击文件名最右侧的按钮，并从弹出菜单中选择“暂存更改”（Stage Changes）或“取消暂存更改”（Unstage Changes）。

对于文件的单个更改，请使用更改条弹出菜单执行以下操作：

- 要包含未暂存的更改，请选择“暂存更改”。
- 要删除未暂存的更改，请选择“丢弃更改”（Discard Change）。
- 要排除已暂存的更改，请选择“取消暂存更改”。

例如，如果你想提交大部分更改，请单击“暂存全部”按钮，然后使用文件控件或更改条弹出菜单取消暂存单个文件或文件的更改。

### 提交更改并推送到仓库

准备保存工作时，请选择“集成”>“提交”。单击“暂存全部”或使用以下控件选择要提交的更改。输入提交消息，并从“提交”弹出菜单中选择“提交”或“提交并推送”（Commit and Push）。

在出现的对话框中，选择分支，如果希望推送标签（tag），请选中“包含标签”（Include tags）选项，然后单击“推送”（Push）。对于本地仓库，你不会看到推送更改的选项，因为你只需提交更改。

使用远程仓库时，你可以分别进行一次或多次提交，然后单独推送。例如，将功能更改分离到不同的提交中，然后将它们一起推送。对于每组已暂存的更改，单击“提交”而不是选择“提交并推送”。然后，单击“推送”，或选择“集成”>“推送”，以上传所有待处理的提交。

### 查看项目提交历史

Xcode 允许你查看源代码管理仓库中所有分支的完整提交历史。

1. 打开源代码管理导航器，然后单击“仓库”（Repositories）标签页。
2. 展开你的仓库和“分支”（Branches）文件夹。
3. 选择一个分支，以在编辑器区域中显示提交列表。
4. 双击列表中的某个提交，以在下方或右侧显示详细信息，具体取决于你的布局。

![](../../../attachments/ac211ffed7f14e793563747f5f8ac47e/tracking-code-changes-in-a-source-control-repository-5@2x.png)

<sub>项目编辑器的截图，左侧仓库导航器中选中了主要分支，中间提交列表中选中了一个提交，右侧显示了所选提交的详细信息。</sub>

使用提交列表上方的标签页和“过滤”（Filter）字段来限制或扩展列表。与暂存更改类似，使用文件名旁边的展开三角形折叠或展开文件，并使用文件名右侧的“折叠/展开文件”按钮仅查看更改或整个文件。

### 将项目恢复到之前的状态

你可以通过签出（check out）特定提交，快速将代码恢复到源代码管理仓库中的先前状态。Xcode 会将你的项目文件恢复到你选择的提交所指定的状态。

在恢复代码的先前提交之前，请确保你没有任何未提交的更改。如果有，你可以丢弃这些更改（“集成”>“丢弃所有更改”）或通过贮藏（stash）它们来保存以便稍后应用（“集成”>“贮藏所有更改”）。

1. 打开源代码管理导航器。
2. 在仓库导航器中，展开你的仓库和“分支”文件夹。
3. 选择包含你要恢复的提交的分支。
4. 在详细信息视图中，按住 Control 键单击目标提交，然后选择“切换至 [_提交哈希_]”（Switch to "[_commit-hash_]"）。
5. 在对话框中，单击“切换”（Switch）。Xcode 会将你的项目状态恢复到早期提交。

要了解更多关于恢复已贮藏更改的信息，请参阅[使用源代码管理组织你的代码更改](organizing-your-code-changes-with-source-control.md)。

## 另请参阅

### 基础

- [配置你的 Xcode 项目以使用源代码管理](configuring-your-xcode-project-to-use-source-control.md) —— 通过设置 Xcode 项目以使用 Git 源代码管理，在团队成员和开发电脑之间同步代码更改。
