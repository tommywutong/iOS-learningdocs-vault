---
title: iTunes Connect 的 Game Center 配置指南
apple_id: TP40014490
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide_SCh/Chapters/TestingYourApp.html
archived_at: '2026-07-27T06:57:09.214303Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iTunes Connect 的 Game Center 配置指南](%E7%AE%80%E4%BB%8B.md)


[Next](%E5%8F%91%E5%B8%83%20Game%20Center%20app.md)[Previous](%E7%BB%84.md)

# 测试您的 app

Apple 提供了 Game Center 的非生产开发环境，您可以使用该环境测试 app 与 Game Center 之间的互动方式。要使用此环境，请在 iTunes Connect 中创建测试用户帐户，并使用该测试帐户登录开发环境中的游戏。即使您的 app 属于某个组，您也可以在不进行其他设置的情况下开始测试排行榜和成就。但是，测试多人游戏兼容性需要在 iTunes Connect 中进行某些配置。

有关测试 Game Center 功能的特定信息，请参阅 测试您的支持 Game Center 的游戏 中的 _“排行榜”_。

__重要事项：__ 您可以在开发环境中测试使用 iOS 和 OS X 种子软件版本的 app，但是无法将其提交到 App Store，直到传送了相应的 OS。

## 在您的 app 中测试 Game Center 功能

测试 Game Center 感知 app 涉及到以下步骤：

1. 为您的 app 配置 Game Center 组件，如此文档中所述。
2. 为准备提交的 app 版本启用特定的排行榜或成就，如 [为 app 版本启用 Game Center](%E5%8F%91%E5%B8%83%20Game%20Center%20app.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmrwfvjvomrz)。
3. 标识您希望能够与正在测试的 app 一起游戏的其他任何 app，如 [配置多人游戏兼容性测试](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmrvfvjvoni)。
4. 设置 iTunes Connect 测试用户，如 创建测试用户帐户。
5. 根据 测试您的支持 Game Center 的游戏 中的 _“排行榜”_。
6. 清除排行榜测试数据，如 [测试后清除](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmrvfvjvomq)。

## 配置多人游戏兼容性测试

多人游戏兼容性设置决定了哪些运行您的 app 的不同版本的用户可以同时在 Game Center 中查看结果。通过您的 app 的“Version Details”（版本详细信息）页面，可以访问多人游戏兼容性设置。

如果您要测试一起游戏的多个 app，转到“Version Details”（版本详细信息）页面，并将您想要测试的 app 添加到多人游戏兼容性列表。如果您要测试同一个 app 的多个版本，无需其他配置。

![bullet](attachments/Resources/1282/Images/task_2x.png)允许某个 app 与其他 app 相兼容以进行测试的步骤

1. 转到 app 的 Game Center 页面，如 [导航到 app 的 Game Center 页面](%E8%AE%BF%E9%97%AE%E5%92%8C%E5%90%AF%E7%94%A8%20Game%20Center%20%E5%8A%9F%E8%83%BD.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmryfvjvonrv)。
2. 点按您要测试的 app 版本的“View Details”（查看详细信息）。
3. 在 Game Center 部分，启用 Game Center（如果尚未启用）。

   如果未在“View Details”（查看详细信息）中看到 Game Center 部分，则表明尚未为此 app 启用 Game Center。请参阅 [访问和启用 Game Center 功能](%E8%AE%BF%E9%97%AE%E5%92%8C%E5%90%AF%E7%94%A8%20Game%20Center%20%E5%8A%9F%E8%83%BD.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmryfvjvomi)。
4. 在“Multiplayer Compatibility”（多方兼容性）部分中，点按“Edit”（编辑）。
5. 从位于 app 列表下方的添加弹出菜单 (+) 中选择您希望与此 app 相兼容的其他 app。

   （原归档配图获取待重试：`gc_mc_add_app_2x.png`）

   添加弹出菜单 (+) 显示您可以添加的每个 app 的名称和平台。（仅显示启用了 Game Center 的 app）。
6. 点按“Save”（保存）。

## 测试后清除

完成排行榜测试后，请务必删除排行榜测试数据，然后再提交该 app。

![bullet](attachments/Resources/1282/Images/task_2x.png)删除排行榜测试数据的步骤

1. 转到 app 的 Game Center 页面，如 [导航到 app 的 Game Center 页面](%E8%AE%BF%E9%97%AE%E5%92%8C%E5%90%AF%E7%94%A8%20Game%20Center%20%E5%8A%9F%E8%83%BD.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmryfvjvonrv)。
2. 在“排行榜”（排行榜）部分中，点按“Delete Test Data”（删除测试数据）。

   向 Apple 提交删除您的测试数据的请求。通常，请求会在一天内得到处理，并且无法恢复。

   （原归档配图获取待重试：`gc_lb_delete_data_2x.png`）

[Next](%E5%8F%91%E5%B8%83%20Game%20Center%20app.md)[Previous](%E7%BB%84.md)
