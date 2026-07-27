---
title: Xcode Cloud Webhook payload 参考
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/webhook-payload
source_url: 'https://developer.apple.com/documentation/xcode/webhook-payload'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/webhook-payload.json'
content_hash: 'sha256:7c2c5a0e586b4a0f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# Xcode Cloud Webhook payload 参考

<sub>文章</sub>

查看 Xcode Cloud 发送的 Webhook payload 的详细信息，包括与其关联的产品、工作流程、构建、操作、结果和 SCM 元数据。

### Webhook

- **`id`** — 唯一标识 Webhook 的字符串，例如 `12345678-abcd-1234-5678-a12345bc4567`。
- **`name`** — Webhook 的名称，例如 `Team Dashboard`。
- **`url`** — 接收并处理 Webhook 的 App 或服务的 URL。

### WebhookMetadata

- **`type`** — 常量值 `metadata`，表示 payload 的此部分包含 Webhook 的元数据。
- **`createdDate`** — Webhook 事件的创建日期。
- **`eventType`** — 与 Webhook 关联的事件类型，可以是 `BUILD_CREATED`、`BUILD_STARTED`、`BUILD_COMPLETED` 或 `UNRECOGNIZED`。

### App

- **`id`** — 唯一标识与 Webhook 关联的 App 的字符串，例如 `12345678-abcd-1234-5678-a12345bc4567`。
- **`type`** — 常量值 `apps`，表示 payload 的此部分包含事件的 App 信息。

### CIWorkflow

- **`id`** — 唯一标识与 Webhook 关联的工作流程的字符串，例如 `12345678-abcd-1234-5678-a12345bc4567`。
- **`type`** — 常量值 `ciWorkflows`，表示此数据结构代表一个工作流程。
- **`name`** — 与 Webhook 关联的工作流程名称。
- **`description`** — 工作流程编辑器中的工作流程描述。
- **`lastModifiedDate`** — 工作流程最近一次修改的日期。
- **`isEnabled`** — 一个布尔值，表示工作流程当前是否处于启用状态。
- **`isLockedForEditing`** — 一个布尔值，表示工作流程是否已锁定以禁止编辑，从而阻止任何修改。

### CIProduct

- **`id`** — 唯一标识与 Webhook 关联的产品的字符串，例如 `12345678-abcd-1234-5678-a12345bc4567`。
- **`type`** — 常量值 `ciProducts`，表示此数据结构代表一个产品。
- **`name`** — 与 Webhook 关联的产品名称。
- **`createdDate`** — 产品的创建日期。
- **`productType`** — 与 Webhook 关联的产品类型，例如 `APP` 或 `FRAMEWORK`。

### CIBuilds

- **`id`** — 唯一标识与 Webhook 关联的构建的字符串，例如 `12345678-abcd-1234-5678-a12345bc4567`。
- **`type`** — 常量值 `ciBuildRuns`，表示此数据结构代表一次构建。
- **`number`** — 当前构建的编号，例如 `42`。
- **`createdDate`** — 构建的创建日期或计划日期。
- **`startedDate`** — 构建开始执行的日期。
- **`finishedDate`** — 构建执行完成的日期。

**sourceCommit** - 构建的 `git` 提交和 SCM 详细信息。

- **`commitSha`** — 源提交的唯一 SHA-1 哈希。
- **`author`** — 源提交作者的显示名称。
- **`committer`** — 提交更改的人员的显示名称。
- **`htmlUrl`** — 指向 SCM 提供商网站上相应更改的 URL。

**destinationCommit** - 与构建关联的目标提交的可选详细信息。

- **`commitSha`** — 目标提交的唯一 SHA-1 哈希。
- **`author`** — 目标提交作者的显示名称。
- **`committer`** — 提交更改的人员的显示名称。
- **`htmlUrl`** — 指向 SCM 提供商网站上相应更改的 URL。
- **`isPullRequestBuild`** — 一个布尔值，表示该构建是否由拉取请求触发。
- **`executionProgress`** — 构建的当前进度，可以是 `PENDING`、`RUNNING` 或 `COMPLETE`。
- **`completionStatus`** — 构建的完成状态，可以是 `SUCCEEDED`、`FAILED`、`ERRORED`、`CANCELED` 或 `SKIPPED`。

### CIBuildActions

作为构建的一部分运行的每个构建操作的信息和元数据。

- **`id`** — 唯一标识构建操作列表的字符串。
- **`type`** — 常量值 `ciBuildActions`，表示此数据结构代表一个构建操作。
- **`name`** — 构建操作的名称。
- **`actionType`** — 构建操作的类型，可以是 `BUILD`、`ANALYZE`、`TEST` 或 `ARCHIVE`。
- **`startedDate`** — 构建操作开始执行的日期。
- **`finishedDate`** — 构建操作执行完成的日期。

**issueCounts**

- **`analyzerWarnings`** — 一个整数值，表示与构建关联的分析器警告数。
- **`errors`** — 一个整数值，表示与构建关联的错误数。
- **`testFailures`** — 一个整数值，表示与构建关联的测试失败数。
- **`warnings`** — 一个整数值，表示与构建关联的警告数。
- **`relationships`** — 构建关系的详细信息，包括平台类型。可能的平台类型有 `IOS`、`MAC_OS` 或 `TV_OS`。

**builds**

- **`id`** — 与构建操作关联的构建的唯一标识符。
- **`type`** — 常量值 `builds`，表示此数据结构代表一次构建。
- **`platform`** — 与构建关联的平台类型，例如 `IOS`、`MAC_OS` 或 `TV_OS`。

### ScmProvider

- **`type`** — 常量值 `scmProviders`，表示此数据结构代表一个 SCM 提供商。

**scmProviderType**

- **`scmProviderType`** — 表示 SCM 提供商类型的字符串值，例如 `GitHub` 或 `Bitbucket`。
- **`displayName`** — `ScmProviderType` 的字符串表示形式，例如 `GitHub` 或 `Bitbucket`。
- **`isOnPremise`** — 一个布尔值，表示 SCM 提供商是否为自托管。
- **`endpoint`** — SCM 提供商网站上仓库的 URL。

### ScmRepository

- **`id`** — 唯一标识 SCM 仓库的字符串。
- **`type`** — 常量值 `scmRepositories`，表示此数据结构代表一个 SCM 仓库。
- **`httpCloneUrl`** — 仓库的 HTTP 克隆 URL。
- **`sshCloneUrl`** — 仓库的可选 SSH 克隆 URL。
- **`ownerName`** — 仓库所有者个人或组织的名称。
- **`repositoryName`** — 与构建关联的仓库名称。

### ScmPullRequest

- **`id`** — 唯一标识拉取请求的字符串。
- **`type`** — 常量值 `scmPullRequests`，表示此数据结构代表一个 SCM 拉取请求。
- **`title`** — 拉取请求的标题。
- **`number`** — 当前拉取请求的编号，例如 `123`。
- **`htmlUrl`** — 拉取请求的 HTML URL，例如 `https://example.com/example/example-app/pull/123`。
- **`sourceRepositoryOwner`** — 源仓库的所有者。
- **`sourceRepositoryName`** — 源仓库的名称。
- **`sourceBranchName`** — 创建拉取请求的人员所在源仓库中的分支名称，例如 `annejohnson/new-features`。
- **`destinationRepositoryOwner`** — 目标仓库的所有者。
- **`destinationRepositoryName`** — 目标仓库的名称。
- **`destinationBranchName`** — 要将更改合并到的目标仓库分支名称。
- **`isClosed`** — 一个布尔值，表示拉取请求是否已关闭。
- **`isCrossRepository`** — 一个布尔值，表示拉取请求是否跨越由不同用户或组织拥有的仓库。

### ScmGitReference

- **`id`** — 唯一标识 Git 引用的字符串。
- **`type`** — 常量值 `scmGitReferences`，表示此数据结构代表一个 SCM Git 引用。
- **`name`** — Git 引用的易读名称。
- **`canonicalName`** — Git 引用的完全限定名称，例如 `refs/heads/bug-fix`。该名称唯一标识特定的分支、标签或其他引用。
- **`isDeleted`** — 一个布尔值，表示 Git 引用是否已删除。
- **`kind`** — Git 引用的类型，例如 `branch` 或 `tag`。

## 另请参阅

### 通知

- [在 Xcode Cloud 中配置 Webhook](configuring-webhooks-in-xcode-cloud.md) — 配置将 Xcode Cloud 连接到其他服务和工具的 Webhook。
- [将 Xcode Cloud 连接到 Slack](connecting-xcode-cloud-to-slack.md) — 将 Xcode Cloud 连接到 Slack，让团队及时了解最新的 Xcode Cloud 构建。
