---
title: 设置代码智能
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/setting-up-coding-intelligence
source_url: 'https://developer.apple.com/documentation/xcode/setting-up-coding-intelligence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/setting-up-coding-intelligence.json'
content_hash: 'sha256:0ec693e15cb7f475'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [代码智能](coding-intelligence.md)

# 设置代码智能

<sub>文章</sub>

启用你希望在 Xcode 中使用的智能工具。

## 概述

要在 Xcode 中使用代码智能，请前往“智能”设置，开启你希望使用的 Agent 和聊天产品。选择 Xcode >“设置”，然后在边栏中选择“智能”。在可用处，你可以在 Xcode 中开启 Claude 或 ChatGPT。你还可以使用来自其他提供商的编码工具。

![](../../../attachments/034ce543aae8389cd0788990db7b0064/intelligence-settings@2x.png)

<sub>“智能”设置的截图，显示了“关于 Xcode 中的智能与隐私”链接，以及“Agent”、“模型上下文协议（Model Context Protocol）”和“聊天”设置部分。</sub>

在“智能”设置中启用 Agent 或聊天提供商后，你可以在编码助手中输入提示词。当你输入提示词时，你在“智能”设置中设置的 Agent 或模型在处理你的请求时，可能会访问你的项目文件和其他信息。关于如何将项目文件共享给 Agent 和模型的更多信息，请在“智能”设置中点击“关于 Xcode 中的智能与隐私…”。

借助你和 Xcode 提供的额外指导和工具，帮助 Agent 更快地达到你的目标。你来控制 Agent 代表你执行任务时使用哪些命令、工具和技能。有关更多信息，请参阅[扩展和自定义 Agent](extending-and-customizing-agents.md)。

要让你在 Xcode 外部使用的 Agent 也能访问你的项目和 Xcode 功能，请参阅[为外部 Agent 授予 Xcode 访问权限](giving-external-agents-access-to-xcode.md)。

## 启用 Agent

当你在编码助手中选择一个 Agent 时，它会自动获得 Xcode 功能的访问权限，例如构建和测试你的 App。要启用 Agent：

1. 在“智能”设置中，点击“Agent”下你想要启用的 Agent 旁边的“获取”。
2. 在出现的对话框中，点击“安装”。

如果你有账户，请登录：

1. 在 Agent 设置中，点击“账户”行中的“更多”按钮（…）。
2. 在接下来的表单（sheet）中，以及（如果出现）浏览器窗口中，按照说明登录并输入你的凭据。

![Claude Agent 设置的截图，显示了“模型”和“账户”行。](../../../attachments/9277eb4e201667fa271a9f7d5f3fbbbf/intelligence-settings-claude-agent@2x.png)

关于 Agent 的更多信息，请点击 Agent 设置底部显示的隐私政策和服务条款链接。

要启用一个未显示在“智能”设置中但支持 Agent 客户端协议（ACP）的 Agent，请在“Agent”下点击“添加 Agent”，在接下来的表单中输入信息，然后点击“添加”。

![“添加 ACP Agent”表单的截图，下方是 Agent 设置和“添加”按钮。](../../../attachments/73c89c50f2b7d7d7db19f782a1cb1152/intelligence-settings-add-agent@2x.png)

下载 Agent 后，Xcode 会在可能的情况下自动更新下载内容。要管理 Agent 下载，请参阅[下载和安装其他 Xcode 组件](downloading-and-installing-additional-xcode-components.md)。

## 在 Xcode 中启用 ChatGPT

要在 Xcode 中使用 ChatGPT（无论是否有账户）：

1. 在“智能”设置中，点击“聊天”下的“ChatGPT in Xcode（在 Xcode 中使用 ChatGPT）”行中的“开启”。
2. 在出现的对话框中，点击“下一步”，然后点击“开启 ChatGPT”。

要登录免费 ChatGPT 账户或具有更高限制的付费账户：

1. 在“ChatGPT in Xcode”设置中，将“ChatGPT in Xcode”切换为开启。
2. 在“ChatGPT”行中，点击“登录”，然后在下一个对话框中再次点击“登录”。
3. 在出现的浏览器窗口中，按照说明输入你的凭据。

要将你的免费 ChatGPT 账户升级为付费账户，请点击“ChatGPT in Xcode”设置底部的“升级到 ChatGPT Plus”。

对于某些模型，你可以选择模型在生成回复时使用的推理级别。在与模型对话的“逐字稿”面板中，从消息文本字段底部出现的“推理”弹出菜单中选择推理级别。

关于 OpenAI 产品的更多信息，请点击“ChatGPT in Xcode”设置底部的“OpenAI 服务条款…”。

要关闭在 Xcode 中使用 ChatGPT，请在“ChatGPT in Xcode”设置中将“ChatGPT in Xcode”切换为关闭。

## 启用 Claude Sonnet & Opus

要使用 Claude Sonnet & Opus：

1. 在“智能”设置中，点击“聊天”下的“Claude Sonnet & Opus”。
2. 在“Claude”行中，点击“登录”。
3. 在出现的浏览器窗口中，按照说明输入你的凭据。

关于 Anthropic 产品的更多信息，请点击“Claude”设置底部的“Anthropic 服务条款…”。

## 使用其他聊天提供商

要使用其他聊天提供商，请点击“聊天”下的“添加聊天提供商”按钮。要添加托管在互联网上的提供商，请选择“互联网托管”，输入 URL 和其他详细信息，然后在出现的对话框中点击“添加”。要添加本地托管在你的 Mac 上的提供商，请选择“本地托管”，然后输入端口和可选的描述。

如果你添加其他提供商，它需要支持 Chat Completions API。此外，Xcode 期望提供商支持以下列出模型和执行补全的端点：

- `{模型提供商的 URL}/v1/models`
- `{模型提供商的 URL}/v1/chat/completions`

## 配置受管理设备

要为受管理设备关闭编码助手，请在移动设备管理（MDM）描述文件中将 `CodingAssistantAllowExternalIntegrations` 键设置为 `false`。有关更多信息，请参阅[Mac 电脑的设备管理限制](https://support.apple.com/guide/deployment/restrictions-for-mac-depba790e53/web)。

## 另请参阅

### 基础

- [在 Xcode 中使用智能编写代码](writing-code-with-intelligence-in-xcode.md) — 在 Xcode 中与 Agent 或模型开始对话，以生成代码、导览不熟悉的代码库，以及修复或重构现有代码。
- [在源代码编辑器中使用代码智能](using-coding-intelligence-in-the-source-editor.md) — 在你希望修改代码的同一位置提交提示词。
