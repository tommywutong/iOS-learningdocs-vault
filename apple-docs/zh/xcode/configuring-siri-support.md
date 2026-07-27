---
title: 配置 Siri 支持
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-siri-support
source_url: 'https://developer.apple.com/documentation/xcode/configuring-siri-support'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-siri-support.json'
content_hash: 'sha256:ef3c78005e4cd436'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Capabilities](capabilities.md)

# 配置 Siri 支持

<sub>文章</sub>

让你的 App 及其 Intents 扩展能够解析、确认并处理用户发起的针对你的 App 服务的 Siri 请求。

## 概述

要处理源自 Siri 的用户请求，首先要将 Siri 功能添加到你的 App 的 target 中。这会告知系统，你的 App 已准备好解析、确认并处理 SiriKit intent，通常是通过其 Intents 扩展来完成；在 iOS 14 及更高版本中，你可以选择在 App 内部完成这些步骤中的每一步。

在配置好你的 App 以处理 SiriKit intent 后，向你的 App 委托（app delegate）或 Intents 扩展添加代码，将传入的 intent 路由到你的自定处理程序。有关更多信息，请参阅 [Dispatching intents to handlers](../sirikit/dispatching-intents-to-handlers.md)。

> [!note] 注意
> watchOS 并不支持所有 intent 类型。例如，watchOS App 无法发起视频通话，也无法处理 CarPlay 领域中的 intent。请查看某个 intent 的可用性信息，以确定你能否在 watchOS 上使用它。

### 将 Siri 功能添加到你的 target

按照 [Add a capability](adding-capabilities-to-your-app.md#Add-a-capability) 中的步骤，将该功能添加到你的 App 的 target，确保从 Xcode 的 Capabilities 库中选择 Siri 功能。对于带有独立 WatchKit 扩展的 watchOS App，你必须将该功能添加到 WatchKit Extension target。该功能不适用于 macOS。

![](../../../attachments/9627343970c7b20046c3823a96824a19/siri@2x.png)

<sub>Xcode 的 Capabilities 库截图，左侧是可用功能列表，右侧是信息面板。列表显示了从 Near Field Communication Tag Reading 到 Wireless Access Configuration 等一系列功能，Siri 功能处于选中状态。信息面板上的文字说明 Siri 功能可让你的应用程序处理 Siri 请求。</sub>

添加 Siri 功能后，Xcode 会自动更新你的 target 的 entitlements 文件，加入 [Siri Entitlement](../bundleresources/entitlements/com.apple.developer.siri.md)。对于任何包含处理非快捷指令 Siri 请求的 Intents 扩展的 App，App Store 都要求具备此 entitlement。

### 在 Intents 扩展中处理 SiriKit intent

使用 Intents 扩展可以快速响应用户从 Siri 发出的请求，而不必承担将整个 App 加载到内存中的性能开销。要使用扩展，你必须先完成若干额外的配置步骤，例如向你的 App 的 target 添加一个或多个 Intents 扩展，并指定这些扩展支持的 intent 类型。有关更多信息，请参阅 [Add an Intents App Extension to Your Project](https://developer.apple.com/documentation/sirikit/intent_handling_infrastructure/creating_an_intents_app_extension#2864127)。

### 直接在你的 App 中处理 SiriKit intent

在 iOS 14 及更高版本中，你可以选择不使用 Intents 扩展，而是直接从你的 iOS App 内部响应用户的请求。为此，请在你的 App 委托中重写 [application(_:handlerFor:)](<../uikit/uiapplicationdelegate/application(__handlerfor_).md>) 方法，并使用它将传入的 intent 映射到能够处理这些 intent 的对象。

与配置 Intents 扩展的方式相同，你必须指定你的 iOS App 支持的 intent 类型。有关更多信息，请参阅 [Specify the Intents Your Extension Supports](https://developer.apple.com/documentation/sirikit/intent_handling_infrastructure/creating_an_intents_app_extension#2864128)。

## 另请参阅

### App execution

- [Configuring background execution modes](configuring-background-execution-modes.md) — 说明你的 App 需要哪些后台服务才能在 iOS、iPadOS、tvOS、visionOS 和 watchOS 中继续在后台执行。
- [Configuring custom fonts](configuring-custom-fonts.md) — 将你的 App 注册为系统范围自定字体的提供方或使用方。
- [Configuring game controllers](configuring-game-controllers.md) — 通过启用对实体游戏控制器的发现、配置和使用，增强游戏输入体验。
- [Configuring Maps support](configuring-maps-support.md) — 注册你的 iOS 路线规划 App，以向地图和其他 App 提供点对点路线指引。
