---
title: iTunes Connect 的 Game Center 配置指南
apple_id: TP40014490
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide_SCh/Chapters/DistributingGameCenterApps.html
archived_at: '2026-07-27T06:57:09.222209Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iTunes Connect 的 Game Center 配置指南](%E7%AE%80%E4%BB%8B.md)


[Next](Game%20Center%20%E5%B1%9E%E6%80%A7.md)[Previous](%E6%B5%8B%E8%AF%95%E6%82%A8%E7%9A%84%20app.md)

# 发布 Game Center app

如果您已准备好将 app 提交到 App Store 或 Mac App Store，请使用 iTunes Connect 中的“Version Details”（版本详细信息）页面。在此页面中，您可以为此版本的 app 启用 Game Center 功能，并指明支持哪些排行榜和成就。

## 为 app 版本启用 Game Center

在 app 的“Version Details”（版本详细信息）页面中，您可以启用 Game Center 功能，以应用到此版本的 app。

- 启用 Game Center。
- 选择此 app 版本支持的排行榜。
- 选择此 app 版本支持的成就。
- 选择与此 app 兼容的相应 app 和版本。

启用 Game Center 功能是 提交 app中介绍的 app 提交总过程中的一步。

![bullet](attachments/Resources/1282/Images/task_2x.png)为 app 版本启用 Game Center

1. 转到 app 的 Game Center 页面，如 [导航到 app 的 Game Center 页面](%E8%AE%BF%E9%97%AE%E5%92%8C%E5%90%AF%E7%94%A8%20Game%20Center%20%E5%8A%9F%E8%83%BD.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmryfvjvonrv)中所述。
2. 在“Versions”（版本）部分中，点按要为其启用 Game Center 的版本旁边的“View Details”（查看详细信息）。
3. 在“Game Center”部分中，点按启用 Game Center 的开关。
4. 如果 app 使用排行榜集合，且您有与此版本 app 一起提交的排行榜，请按照以下步骤编辑排行榜集合信息。

   1. 在“Leaderboard Sets”（排行榜集合）部分中，点按“Edit”（编辑）。
   2. 使用“Add”（添加）弹出式菜单 (+) 选取包含您希望提交的排行榜的排行榜集合。
   3. 在右面板中，从相应的集合中选择要提交的每个排行榜。

      （原归档配图获取待重试：`gc_app_version_lb_2x.png`）
   4. 点按“Save”（保存）。
5. 如果您有与此版本 app 一起提交的排行榜，请按照以下步骤编辑排行榜信息。

   如果 app 使用排行榜集合，且您已通过集合选择排行榜，则可以跳过此步骤。

   1. 在“Leaderboards”（排行榜）部分中，点按“Edit”（编辑）。
   2. 选择要提交的排行榜或排行榜集合。

      （原归档配图获取待重试：`gc_app_version_select_lb_2x.png`）
   3. 点按“Save”（保存）。
6. 如果您有与此版本 app 一起提交的成就，请按照以下步骤编辑“Achievements”（成就）部分。

   1. 在“Achievements”（成就）部分中，点按“Edit”（编辑）。
   2. 选择要提交的成就。
   3. 点按“Save”（保存）。
7. 如果 app 属于组，或者如果您希望此 app 与其他 app 兼容，请按照以下步骤编辑“Multiplayer Compatibility”（多方兼容性）部分。

   1. 在“Multiplayer Compatibility”（多方兼容性）部分中，点按“Edit”（编辑）。
   2. 在“Add”（添加）弹出式菜单 (+)（位于 app 列表下方）中，选取一个兼容 app。

      （原归档配图获取待重试：`gc_mc_edit_2x.png`）

      “Add”（添加）弹出式菜单 (+) 显示您可以添加的已启用 Game Center 的每个 app 的名称和平台。
   3. 选择与您要提交的 app 兼容的 app 版本。
   4. 点按“Save”（保存）。
8. 点按“Ready to Upload Binary”（准备上传二进制文件）。

## 在 app 中禁用 Game Center

如果您的 app 版本之前已获得批准，则您无法再为 app 的所有版本禁用 Game Center。但您必须在更新 app 时更改 app 新版本的 Game Center 属性。如果您为 app 版本禁用 Game Center，则需要更改多方兼容性设置，如 [为 app 版本启用 Game Center](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diojqfvbuqmrwfvjvomrz)中所述。

__注意：__ 即使您为 app 的当前版本禁用 Game Center，用户也仍可使用 Game Center 中的所有排行榜。

![bullet](attachments/Resources/1282/Images/task_2x.png)为 app 版本禁用 Game Center

1. 在“App Information”（app 信息）页面中，打开要编辑的 app 版本的“Version Details”（版本详细信息）。
2. 在“Game Center”部分中，点按“Enabled”（已启用）按钮禁用 Game Center。

[Next](Game%20Center%20%E5%B1%9E%E6%80%A7.md)[Previous](%E6%B5%8B%E8%AF%95%E6%82%A8%E7%9A%84%20app.md)
