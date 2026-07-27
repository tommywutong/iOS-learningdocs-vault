---
title: 配置你的 Xcode 项目以使用源代码管理
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-your-xcode-project-to-use-source-control
source_url: 'https://developer.apple.com/documentation/xcode/configuring-your-xcode-project-to-use-source-control'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-your-xcode-project-to-use-source-control.json'
content_hash: 'sha256:a4aaa1da86189846'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Source control management](source-control-management.md)

# 配置你的 Xcode 项目以使用源代码管理

<sub>文章</sub>

通过将你的 Xcode 项目设置为使用 Git 源代码管理，在团队成员和开发用的电脑之间同步代码更改。

## 概述

当你与团队一起开发 App，或者独自使用多台 Mac 电脑开发时，可以借助 Xcode 对 Git 源代码管理的支持，在团队成员和电脑之间共享更改。

Xcode 使用 Git 命令来管理你的_源代码管理仓库_，用它来追踪项目文件更改的历史记录。如果你使用远程仓库，Git 会在其他设备之间同步这些更改。你可以通过创建新的本地仓库，或将其连接到已有的远程仓库，来设置你的 Xcode 项目使用 Git。

有关源代码管理设置的更多信息，请参阅[在 Xcode 中配置源代码管理](configuring-source-control-in-xcode.md)。

### 自定你的作者姓名和电子邮件

在设置源代码管理仓库之前，先输入你想要的姓名和电子邮件地址，Xcode 会在你所有的项目中使用它们。

之后，当你对源代码进行更改并提交到仓库时，Xcode 会将你的姓名和电子邮件地址作为作者写入源代码管理历史记录。其他人可以按住 Control 点按某条历史记录来给作者发送邮件。

要更改用于源代码管理的姓名和电子邮件地址，请选择“Xcode” > “设置”，在边栏中点按“Source Control”，然后在右侧打开“Enable source control”。接着点按下方的“Git settings”，在随后出现的表单中，在对应的文本框内输入你的作者姓名和电子邮件地址。

![显示了 Git 设置的屏幕截图，其中显示了作者姓名和作者电子邮件文本框。](../../../attachments/096c7eeabc70a5164eac8de35233dc47/configuring-your-xcode-project-to-use-source-control-1@2x.png)

### 为新项目创建本地仓库

从模板创建新的 Xcode 项目时，你可以在最后一张表单中指定是否创建本地 Git 源代码仓库。选择“Create Git repository on my Mac”，然后点按“Create”。

![](../../../attachments/995764162c388923b6e5267ffb97a31e/configuring-your-xcode-project-to-use-source-control-2@2x.png)

<sub>从模板创建项目时最后一个对话框的屏幕截图，显示了“Create Git repository on my Mac”选项和“Create”按钮。</sub>

Xcode 会创建项目文件夹，初始化本地 Git 源代码管理仓库，并提交它为你项目创建的所有文件。更多信息请参阅[为 App 创建 Xcode 项目](creating-an-xcode-project-for-an-app.md)。

### 从远程仓库克隆项目

你还可以为一个已有的远程 Git 仓库创建本地副本，也就是_克隆_一份，然后用 Xcode 提交更改。

首先，在 Xcode 设置中输入账户信息以访问远程仓库。在“Xcode” > “设置” > “Source Control”面板中，点按“Add Account”。在对话框中，选择账户类型，然后点按“Continue”。例如，选择 Bitbucket Server 或 GitHub Enterprise。

![账户对话框的屏幕截图，显示已选中 Bitbucket Cloud 以及一个“Continue”按钮。](../../../attachments/52d98f7ec907f2691b065d5e2b895893/configuring-your-xcode-project-to-use-source-control-3@2x.png)

在随后出现的对话框中，根据账户类型输入你的凭据，然后点按“Sign In”。如果你需要令牌，请点按“Create a Token on [_账户类型_]”，然后按照浏览器中出现的、针对该账户类型的网页上的说明进行操作。

要在运行 Xcode 时克隆远程仓库，请选择“Integrate” > “Clone”，或在你首次启动 Xcode 时出现的“Welcome to Xcode”窗口中点按“Clone Git Repository”。你可以随时选择“Window” > “Welcome to Xcode”重新打开这个窗口，查看其他选项。

如果你添加了一个或多个源代码管理账户，Xcode 会在下一个窗口中显示你可以克隆的项目列表。在顶部的搜索栏中输入仓库名称即可快速找到它；如果它没有出现在列表中，也可以把整个仓库 URL 粘贴到搜索栏中。然后选择该仓库并点按“Clone”。

![克隆仓库窗口的屏幕截图，顶部有一个搜索栏，下方有一个“Clone”按钮。](../../../attachments/62aa559a925efd5a0084f4eac56ce023/configuring-your-xcode-project-to-use-source-control-4@2x.png)

如果远程仓库中包含 Xcode 项目，Xcode 会扫描该项目，并提供一个可供克隆的分支列表。从弹出式菜单中选择要克隆的分支，然后在随后出现的对话框中，为 Xcode 提供一个保存本地项目的位置。Xcode 会检出该分支并打开项目。

### 连接到远程仓库以同步更改

你还可以为已有的本地项目创建新的远程仓库，或者将本地项目连接到已有的远程仓库。例如，当你创建了本地仓库、之后又决定改用远程仓库时，或者当你从远程仓库下载项目而没有克隆它、之后又想创建新的远程仓库来存储你的更改时，都可以这样做。

在“Source Control”导航器中，点按“Repositories”标签页。如有需要，展开该仓库以显示“Remotes”文件夹。

- 要为已有项目创建新的远程仓库，请按住 Control 点按“Remotes”，然后从弹出式菜单中选择“New “[_项目名称_]” Remote”。在对话框中输入远程仓库的信息，然后点按“Create”。
- 要将本地项目连接到已有的远程仓库，请按住 Control 点按“Remotes”，然后从弹出式菜单中选择“Add Existing Remote”。输入远程仓库的名称和 URL，然后点按“Add”。

### 从远程仓库获取更改

选择“Integrate” > “Pull”，从远程仓库获取更改。在随后出现的对话框中，选择分支，然后点按“Pull”。

![](../../../attachments/b3b4001bff97bbaa11e7fbf3a9a1af0f/configuring-your-xcode-project-to-use-source-control-7@2x.png)

<sub>拉取更改对话框的屏幕截图，显示了一个用于选择分支的弹出式菜单、一个“将本地更改变基到上游更改上”的选项，以及一个“Pull”按钮。</sub>

如果你有想要保留的本地更改，请在点按“Pull”之前选择“Rebase local changes onto upstream changes”选项。否则，可能会出现一个对话框，询问你在拉取远程更改之前是否要贮藏你的本地更改。

或者，选择“Integrate” > “Fetch Changes”，从远程仓库下载更改，而不将其应用到你的本地副本。

例如，如果你在不同的电脑上提交更改，或者与团队成员在同一个分支上协作，请在进行本地更改之前先拉取远程更改，以避免冲突。

## 另请参阅

### 基础

- [Tracking code changes in a source control repository](tracking-code-changes-in-a-source-control-repository.md) — 使用提交并推送到远程仓库，为你的项目创建增量更改的历史记录。
