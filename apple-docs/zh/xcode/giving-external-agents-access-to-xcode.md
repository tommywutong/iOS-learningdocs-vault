---
title: 让外部智能体访问 Xcode
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/giving-external-agents-access-to-xcode
source_url: 'https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/giving-external-agents-access-to-xcode.json'
content_hash: 'sha256:35283711803fb62f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Coding intelligence](coding-intelligence.md)

# 让外部智能体访问 Xcode

<sub>文章</sub>

借助 Model Context Protocol 让智能体访问你的项目和 Xcode 功能。

## 概述

你可以为在 Xcode 之外启动的外部智能体授予权限，让它们修改你的 Xcode 项目并执行诸如构建你的 App 之类的操作。

如果你使用外部智能体进行开发：

1. 在「智能」设置中允许该智能体访问 Xcode。
2. 配置该智能体，使其通过 Xcode 提供的 Model Context Protocol (MCP) 服务器来访问 Xcode 功能。
3. 在 Xcode 中打开你的项目，然后开始向使用 Xcode 的外部智能体发出提示。

当外部智能体连接到 Xcode 以及处于活跃状态时，Xcode 会提醒你。

### 更新「智能」设置以让外部智能体访问 Xcode

在「智能」设置中，允许外部智能体通过其 MCP 服务器与 Xcode 建立连接：

1. 选择「Xcode」\> 「设置」，并在侧边栏中选择「智能」。
2. 在「Model Context Protocol」下，打开「允许外部智能体使用 Xcode 工具」。

![](../../../attachments/034ce543aae8389cd0788990db7b0064/intelligence-settings@2x.png)

<sub>一张「智能」设置的截图，显示了「Model Context Protocol」下的「允许外部智能体使用 Xcode 工具」开关。</sub>

### 配置外部智能体以使用 MCP 服务器

在「终端」中，使用 `xcrun mcpbridge` 命令来配置外部智能体以使用 Xcode 工具。例如，在「终端」中运行以下命令，可让 Claude Code 访问你打开的项目和 Xcode 功能：

```
claude mcp add --transport stdio xcode -- xcrun mcpbridge
```

对于 Codex，运行：

```
codex mcp add xcode -- xcrun mcpbridge
```

要验证配置，在「终端」中输入 `claude mcp list` 或 `codex mcp list`。

你也可以选择在外部智能体所使用的位置下，向配置文件（例如 `AGENTS.md` 或 `CLAUDE.md` 文件）中添加关于 Xcode 和你的项目的提示信息。有关配置在 Xcode 内运行的智能体的更多信息，请参阅[自定智能体环境](extending-and-customizing-agents.md#Customize-agent-environments)。

在向外部智能体（Xcode 之外的）发出提示之前，请确保已在 Xcode 中打开你的项目。

## 另请参阅

### 智能体配置

- [扩展和自定智能体](extending-and-customizing-agents.md) — 针对你的具体需求和应用领域扩展智能体功能。
