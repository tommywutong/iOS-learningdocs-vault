---
title: iTunes Connect 的 Game Center 配置指南
apple_id: TP40014490
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide_SCh/Chapters/AccessAndEnable.html
archived_at: '2026-07-27T06:57:09.137108Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iTunes Connect 的 Game Center 配置指南](%E7%AE%80%E4%BB%8B.md)


[Next](%E6%8E%92%E8%A1%8C%E6%A6%9C%E5%92%8C%E6%8E%92%E8%A1%8C%E6%A6%9C%E9%9B%86%E5%90%88.md)[Previous](%E7%AE%80%E4%BB%8B.md)

# 访问和启用 Game Center 功能

Game Center 信息在 iTunes Connect 中的显示级别有两个：在 app 一级显示，您可以配置排行榜和成就的所有详细信息；在版本一级显示，您可以确定与该 app 版本相关联的排行榜和成就。本部分介绍了如何访问这两个配置级别。

__注意：__ 只有具有管理员、法律人员或技术人员角色的 iTunes Connect 用户才能使用 Game Center 功能。有关分配用户角色的信息，请参阅 创建 iTunes Connect 用户。

## 导航到 app 的 Game Center 页面

若要开始结合使用 app 和 Game Center，请导航到 app 的 Game Center 页面；如果您是首次在过程中这样做，请为 app 启用 Game Center。

![bullet](attachments/Resources/1282/Images/task_2x.png)在 iTunes Connect 中转到 app 的 Game Center 页面

1. 使用您的 Apple ID 用户名和密码登录 [iTunes Connect](https://itunesconnect.apple.com) 。
2. 点按“Manage Your Apps”（管理您的 app）。

   （原归档配图获取待重试：`gc_login_2x.png`）
3. 选择要管理的 app。

   如果该 app 未显示在近期有活动的 app 的列表中，请通过以下方式进行查找：

   - 点按“See All”（查看全部），显示包含组织内所有 app 的列表

     您可以点按列标题对列表进行排序，也可以使用页面控件在各页列表之间切换。

     （原归档配图获取待重试：`apps_see_all_list_2x.png`）
   - 在“Recent Activity”（近期活动）列表下，使用“Search”（搜索）部分中的字段

     （原归档配图获取待重试：`search_autocomplete_2x.png`）
4. 点按“Manage Game Center”（管理 Game Center）。

   （原归档配图获取待重试：`gc_manage_gc_2x.png`）
5. 如果您之前已为 app 启用 Game Center，则系统会打开 Game Center 页面。

   如果您是首次对此 app 进行 Game Center 配置，系统会提示您启用 Game Center。选择以下选项之一：

   - 如果您要配置此 app 专用的 Game Center 组件，请选择“Enable for Single Game”（为单个游戏启用）。
   - 如果您要配置可供多个 app 使用的 Game Center 组件，请选择“Enable for Group Games”（为组游戏启用）。

   此时，系统会打开相应的 Game Center 页面。

在此页面中，您可以配置 Game Center 组件： [排行榜和排行榜集合](%E6%8E%92%E8%A1%8C%E6%A6%9C%E5%92%8C%E6%8E%92%E8%A1%8C%E6%A6%9C%E9%9B%86%E5%90%88.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmrnknltc)、 [成就](%E6%88%90%E5%B0%B1.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmznknltc)和 [组](%E7%BB%84.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqnbnknltc)。

## 为您的 app 启用 Game Center

您可以在 iTunes Connect 中的两个位置为 app 启用 Game Center：

- “App Information”（app 信息）、Game Center 页面。通过点按“Manage Game Center”（管理 Game Center），从“App Summary”（app 摘要）页面打开 app 的 Game Center 页面。

  请参阅 [在 iTunes Connect 中转到 app 的 Game Center 页面](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmryfvjvooa)。

  在 Game Center 页面中，您可以配置 app 使用的所有 Game Center 组件。在此页面中启用 Game Center 可以允许该 app 与 Game Center 进行通信，并能将 Game Center 元数据（如 [Game Center 属性](Game%20Center%20%E5%B1%9E%E6%80%A7.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmrzfvjvomi)中所述）添加到 app 的 iTunes Connect 记录中。
- “App Version”（app 版本）、“Versions Details”（版本详细信息）页面。通过点按特定 app 版本的“Version Details”（版本详细信息），从“App Summary”（app 摘要）页面打开 app 的“Version Details”（版本详细信息）页面。

  请参阅 [为 app 版本启用 Game Center](%E5%8F%91%E5%B8%83%20Game%20Center%20app.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmrwfvjvomrq)。

  “Version Details”（版本详细信息）页面包含用于为此 app 版本启用 Game Center 配置的特定选项。请在完成测试并且准备提交 app 时设置这些选项。请参阅 [为 app 版本启用 Game Center](%E5%8F%91%E5%B8%83%20Game%20Center%20app.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmrwfvjvomrq)。

您必须在两个位置都启用 Game Center 才能允许 app 通过 Game Center 访问已配置的组件。

## 为 app 禁用 Game Center

在 app 版本获得批准之前，您可以为 app 禁用 Game Center。此操作会为所有版本 app 禁用 Game Center。若要为特定 app 版本禁用 Game Center，请参阅 [为 app 版本禁用 Game Center](%E5%8F%91%E5%B8%83%20Game%20Center%20app.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmrwfvjvomzy)。

![bullet](attachments/Resources/1282/Images/task_2x.png)为 app 禁用 Game Center

1. 转到 app 的 Game Center 页面，如 [导航到 app 的 Game Center 页面](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmryfvjvonrv)中所述。
2. 在“Game Center”部分中，点按禁用 Game Center 的开关。

[Next](%E6%8E%92%E8%A1%8C%E6%A6%9C%E5%92%8C%E6%8E%92%E8%A1%8C%E6%A6%9C%E9%9B%86%E5%90%88.md)[Previous](%E7%AE%80%E4%BB%8B.md)
