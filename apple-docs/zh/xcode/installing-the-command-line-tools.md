---
title: 安装命令行工具
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/installing-the-command-line-tools
source_url: 'https://developer.apple.com/documentation/xcode/installing-the-command-line-tools'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/installing-the-command-line-tools.json'
content_hash: 'sha256:62fe7edc224b8ea8'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Command-line tools](command-line-tools.md)

# 安装命令行工具

<sub>文章</sub>

使用安装程序包或终端 App 为 Xcode 安装命令行工具。

## 概述

Xcode 附带了诸如 `clang`、`notarytool`、`xcodebuild` 和 `xcrun` 等命令行工具。如果你在 Mac 上安装了 Xcode，就不需要单独安装命令行工具。

Apple 提供了 Command Line Tools for Xcode 包，作为完整 Xcode 安装的替代方案。如果你在 Xcode 之外工作，或使用 UNIX 风格的命令来构建你的 App，这个包对于安装命令行工具会很有用。该包包含与 Xcode 附带的相同的 macOS SDK、man 页面和工具链二进制文件。你可以下载该包的特定版本，或从命令行为你的 Mac 安装其最新版本。系统会将该包安装在以下路径：`/Library/Developer/CommandLineTools`。

> [!important] 重要
> `xcodebuild` 和 `xctrace` 等命令仅随 Xcode 一起提供，并不包含在 Command Line Tools for Xcode 包中。要了解更多信息，请参阅 [Xcode command-line tool reference](xcode-command-line-tool-reference.md)。

### 选择 Command Line Tools for Xcode 包的版本

在安装 Command Line Tools for Xcode 包之前，请查阅 [Xcode Releases](https://developer.apple.com/support/xcode) 表格，以确定你可以在 macOS 计算机上安装并用于开发的命令行工具版本。你一次只能在 Mac 上安装该包的一个版本。

### 下载并安装 Command Line Tools for Xcode 包

[Apple Developer website](https://developer.apple.com/) 的 [More Downloads page](https://developer.apple.com/download/all/?q=command%20line%20tools) 列出了 Command Line Tools for Xcode 包的所有可下载版本。要安装命令行工具，请使用你的 Apple ID 登录，并搜索你想要用于开发的包。然后将其下载并安装到你的 Mac 上。例如，下图显示了「Command Line Tools for Xcode 26.1 beta」包：![](../../../attachments/e0155e2cecfc7ac98312087325742365/installing-the-command-line-tools-01@2x.png)

<sub>Apple Developer 网站的屏幕截图，显示了 More Downloads 页面，并按 Command Line Tools for Xcode 26.1 进行了筛选。</sub>

### 在终端中安装 Command Line Tools 包

你可以使用 `xcode-select` 命令，从命令行下载并安装 Command Line Tools for Xcode 包。在终端中，输入带有 `--install` 选项的 `xcode-select`，如下例所示：

```
% xcode-select --install 
xcode-select: note: install requested for command line developer tools
```

在出现的系统对话框中，点击安装，然后同意 Command Line Tools 许可协议。安装完成后，点击完成。

> [!note] 注意
> 在全新安装的 macOS 上，从命令行调用 Xcode 或命令行工具包中的任何命令（比如 `git`）都会提示你下载并安装 Command Line Tools for Xcode 包。

### 检查已安装的 Command Line Tools for Xcode 包的版本

安装 Command Line Tools for Xcode 包后，请验证其版本与你打算使用的版本是否一致。要检查 Command Line Tools for Xcode 包的版本，请在终端中运行带有 `--pkg-info` 选项的 `pkgutil` 命令：

```
% pkgutil --pkg-info=com.apple.pkg.CLTools_Executables
```

例如，以下命令列出了「Command Line Tools for Xcode 26.1 beta」包：

```
% pkgutil --pkg-info=com.apple.pkg.CLTools_Executables
package-id: com.apple.pkg.CLTools_Executables
version: 26.1.0.0.1.1760670222
volume: /
location: /
install-time: 1761350460
```

你可以在 `/Library/Developer/CommandLineTools/usr/bin` 找到该包所包含的命令行工具的完整列表。

### 让 Command Line Tools for Xcode 包保持最新

要更新 Command Line Tools for Xcode 包，请为当前 macOS 安装最新版本。更新会替换该包的旧版本。

要安装该包的新版本，请在系统设置中使用 [Software Update](https://support.apple.com/en-us/108382)，或使用 [softwareupdate](x-man-page://softwareupdate) 命令。「软件更新」和该命令会查找并显示与你的 macOS 兼容的该包更新。

> [!note] 注意
> macOS 升级后，请使用「软件更新」或 [`softwareupdate`](x-man-page://softwareupdate) 命令检查命令行工具包的新版本。已安装包的版本可能与新的 macOS 不兼容。

### 卸载 Command Line Tools for Xcode 包

要从你的 Mac 中移除该包，请在终端中运行带有 `-rf` 选项的 `sudo rm` 命令：

```
% sudo rm -rf /Library/Developer/CommandLineTools
```

> [!note] 注意
> `sudo` 命令需要管理员权限。当系统提示时，请输入你的管理员密码。

移除该包后，你的 Mac 仍会在「软件更新」中继续收到该包的新版本。删除包收据可以选择不再接收该包的软件更新。

要删除包收据，请在终端中运行带有 `--forget` 选项的 `sudo pkgutil` 命令：

```
% sudo pkgutil --forget com.apple.dt.commandlinetools
```

如果任务成功，`pkgutil` 会输出以下消息：

```
% sudo pkgutil --forget com.apple.dt.commandlinetools
No receipt for 'com.apple.dt.commandlinetools' found at '/'.
```

## 另请参阅

### 基础

- [Configuring command-line tools settings](configuring-command-line-tools-settings.md) — 在 Xcode 设置或终端中，选择你想要用于命令行工具的 Xcode 版本。
- [Xcode command-line tool reference](xcode-command-line-tool-reference.md) — 使用需要你安装 Xcode 并将该 App 设置为活跃开发者目录的命令行工具。
