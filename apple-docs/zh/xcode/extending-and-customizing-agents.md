---
title: 扩展和自定义智能代理
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/extending-and-customizing-agents
source_url: 'https://developer.apple.com/documentation/xcode/extending-and-customizing-agents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/extending-and-customizing-agents.json'
content_hash: 'sha256:90eece0f7789f616'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [编码智能](coding-intelligence.md)

# 扩展和自定义智能代理

<sub>文章</sub>

根据你的特定需求和应用程序领域扩展智能代理的能力。

## 概述

你可以赋予智能代理更多指导和专业知识，使其高效工作、能够自我验证，并在你的任务中以更少的干预自主运行。为此，需授予智能代理使用系统命令和工具的权限，要求智能代理使用内置技能，添加代理特定的配置文件，并安装可增加更多功能的外部插件。

## 控制对外部命令和工具的访问权限

如果你希望在智能代理执行任务时对其使用的命令和工具进行更精细的控制，可以在“智能”（Intelligence）设置中授予或拒绝访问权限。

要管理这些权限，请在 Xcode 的“代理”（Agents）下点击“权限”（Permissions）行。你之前在编码助手中授予访问权限的任何命令或工具都会显示在此处。

要允许访问你在“终端”（Terminal）中运行的命令行工具，请点击“允许的命令”（Allowed Commands）下的“添加”按钮（+）。在出现的文本字段中输入命令，然后按 Return 键。要移除一个命令行工具，请选中它并点击“允许的命令”下的“移除”按钮（-）。

要移除对某个工具的访问权限，请选中该工具并点击“允许的工具”（Allowed Tools）下的“移除”按钮（-）。

## 发现智能代理的技能和能力

Xcode 包含内置的专业知识，可以指导智能代理为高级任务使用最佳 API 和工作流程。Xcode 会根据你输入的提示自动利用这些知识。

例如，当你输入的提示中包含翻译 App 的某部分时，Xcode 会执行本地化步骤并启用翻译子代理。当你输入的提示中包含规划请求时，Xcode 会自动进入计划模式（plan mode），以便在不修改代码的情况下探索想法。

或者，使用斜杠命令显式调用技能，例如 `/plan` 进入计划模式。要发现 Xcode 中所有可用的技能，请在消息文本字段中输入斜杠（`/`）字符，然后在弹出菜单中滚动浏览列表。要退出作为工作流技能的计划模式，请键入 `/exit`，然后从弹出菜单中选择 `/exit-plan`。

## 自定义智能代理环境

通过特定产品的配置文件，你可以对智能代理进行超出“智能”设置和编码助手中可用选项的自定义。例如，你可以设置默认模型、添加额外的模型上下文协议（MCP）服务器，以及创建自己的技能。

将配置文件放置在 Xcode 专门使用的 `~/Library/Developer/Xcode/CodingAssistant` 文件夹中的代理特定子文件夹中。例如，将 Claude Agent、Codex 和 Gemini 的配置文件放置在以下文件夹中：

- `~/Library/Developer/Xcode/CodingAssistant/ClaudeAgentConfig`
- `~/Library/Developer/Xcode/CodingAssistant/codex`
- `~/Library/Developer/Xcode/CodingAssistant/gemini`

> [!note] 注意
> 这些配置仅在你在 Xcode 中启动智能代理时才会影响它们。

## 安装智能代理编码插件

你可以安装包含附加子代理、模型上下文协议（MCP）服务器以及智能代理可以使用的技能的插件。要管理插件，请打开“智能”设置，然后在 Xcode 的“代理”下点击“插件”（Plug-ins）行。

要添加插件，请点击“添加插件”（Add Plug-in）按钮。在表单（sheet）中，选择一个导入选项，然后点击“继续”（Continue）。在下一个表单中，输入信息（例如，如果你选择“从 URL 添加”，则输入 URL），然后点击“继续”。在最后的表单中，选择要安装的组件，然后点击“安装”（Install）。

## 另请参阅

### 代理配置

- [授予外部代理访问 Xcode 的权限](giving-external-agents-access-to-xcode.md) — 让代理使用模型上下文协议访问你的项目和 Xcode 功能。
