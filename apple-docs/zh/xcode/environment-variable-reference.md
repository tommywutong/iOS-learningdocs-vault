---
title: 环境变量参考
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/environment-variable-reference
source_url: 'https://developer.apple.com/documentation/xcode/environment-variable-reference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/environment-variable-reference.json'
content_hash: 'sha256:1481ea199b650311'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 环境变量参考

<sub>文章</sub>

查看在自定义构建脚本中使用的预定义环境变量。

## 概述

通过自定义工作流程，你可以根据需要定制 Xcode Cloud。创建自定义工作流程时，你可以配置 Xcode Cloud 使用的临时构建环境、启动条件、操作以及其他设置。但是，你可能需要执行自定义任务，例如安装第三方工具或将构建产物上传到你的服务器。为实现这一点，Xcode Cloud 支持运行自定义 shell 脚本，称为 _自定义构建脚本（custom build script）_。

Xcode Cloud 包含一组预定义的环境变量，你可以使用它们编写灵活的自定义构建脚本，实现高级控制流程。例如，在脚本中访问 `CI_XCODEBUILD_ACTION` 变量，以确定正在运行的操作，并使用此信息运行特定命令。你还可以利用某个变量的缺失来改变自定义构建脚本的控制流程。

> [!tip] 提示
> 除了预定义的环境变量，你还可以在工作流程的“环境”部分设置自定义环境变量，并在自定义构建脚本或测试操作中访问它们。

有关使用自定义构建脚本和访问环境变量的更多信息，请参阅[编写自定义构建脚本](writing-custom-build-scripts.md)。

### 始终可用的变量

无论你为工作流程配置了哪些操作或启动条件，以下环境变量在 Xcode Cloud 每次启动构建时都可用：

- **`CI`** — 一个布尔值，当自定义构建脚本在 Xcode Cloud 中运行时，其值为 `TRUE`。使用它仅当 Xcode Cloud 构建你的项目或工作区时才运行构建脚本。另请参阅 `CI_XCODE_CLOUD`。
- **`CI_BUILD_ID`** — 唯一标识当前构建的字符串，例如 `12345678-ABCD-DEFG-1234-012345ABCDEF`。
- **`CI_BUILD_NUMBER`** — 当前构建的编号，例如 `42`。
- **`CI_BUILD_URL`** — App Store Connect 中 Xcode Cloud 构建的 URL。
- **`CI_BUNDLE_ID`** — 产品的 Bundle ID，例如 `com.example.appname`。
- **`CI_COMMIT`** — Xcode Cloud 用于当前构建的 Git 提交哈希值。
- **`CI_DERIVED_DATA_PATH`** — 包含项目派生数据的目录路径。
- **`CI_PRIMARY_REPOSITORY_PATH`** — 临时构建环境中从工作流程指定的主仓库克隆的源代码位置，例如 `/Volumes/workspace/repository`。
- **`CI_PRODUCT`** — 工作流程的产品名称。
- **`CI_PRODUCT_ID`** — 唯一标识产品的字符串，例如 `12345678-ABCD-DEFG-1234-012345ABCDEF`。用于区分同一项目或工作区中的产品。
- **`CI_PRODUCT_PLATFORM`** — 当前操作的平台（`iOS`、`macOS`、`tvOS` 或 `watchOS`）。
- **`CI_PROJECT_FILE_PATH`** — 临时构建环境中 Xcode 项目或工作区的路径。
- **`CI_START_CONDITION`** — 启动构建的启动条件。可用值为 `manual`、`manual_rebuild`、`push`、`pr_open`、`pr_update` 和 `schedule`。
- **`CI_TEAM_ID`** — 你 Apple Development 团队的 ID，例如 `ABCDE12345`。
- **`CI_WORKFLOW`** — 工作流程的名称，例如 `Default Workflow`。使用此变量仅对特定工作流程运行命令。
- **`CI_WORKFLOW_ID`** — 唯一标识工作流程的字符串，例如 `12345678-ABCD-DEFG-1234-012345ABCDEF`。
- **`CI_WORKSPACE_PATH`** — 用于克隆源代码和存储构建产物的工作区位置，例如 `/Volumes/workspace`。
- **`CI_XCODE_CLOUD`** — 一个布尔值，当自定义构建脚本在 Xcode Cloud 中运行时，其值为 `TRUE`。使用它仅当 Xcode Cloud 构建你的项目或工作区时才运行脚本内容。
- **`CI_XCODE_PROJECT`** — Xcode 项目或工作区的名称。
- **`CI_XCODE_SCHEME`** — 当前操作使用的 scheme。
- **`CI_XCODEBUILD_ACTION`** — Xcode Cloud 即将执行的 `xcodebuild` 命令。可能的值为 `analyze`、`archive`、`build`、`build-for-testing` 和 `test-without-building`。
- **`CI_XCODEBUILD_EXIT_CODE`** — `xcodebuild` 命令的退出码。此变量在 Xcode Cloud 运行完操作对应的 `xcodebuild` 命令后可用。退出码 `0` 表示 `xcodebuild` 命令执行成功。

> [!note] 注意
> Xcode Cloud 在使用 HTTP 代理的临时构建环境中构建你的项目，并提供标准的 `HTTP_PROXY` 和 `HTTPS_PROXY` 环境变量。许多工具会读取这些变量并使用它们更改其设置。

### 特定启动条件的变量

以下环境变量的可用性取决于你配置的工作流程启动条件。例如，`CI_PULL_REQUEST_NUMBER` 变量仅在“拉取请求更改”启动条件启动构建时才可用。

#### 分支更改的变量

- **`CI_BRANCH`** — Xcode Cloud 为当前构建检出的源分支的名称，例如 `main`。

#### 标签更改的变量

- **`CI_TAG`** — Xcode Cloud 为当前构建检出的标签的名称，例如 `release-1.1`。

#### 分支更改和标签更改的变量

- **`CI_GIT_REF`** — 包含 `CI_COMMIT` 的标准 Git 引用，例如，来自 `bug-fix` 分支的构建为 `refs/heads/bug-fix`，来自 `release-1.0` 标签的构建为 `refs/tags/release-1.0`。

#### 拉取请求更改的变量

- **`CI_PULL_REQUEST_HTML_URL`** — 拉取请求网页的 URL。
- **`CI_PULL_REQUEST_NUMBER`** — 拉取请求的编号，例如 `42`。
- **`CI_PULL_REQUEST_SOURCE_BRANCH`** — 拉取请求的源分支，例如 `feature/feature-12345`。
- **`CI_PULL_REQUEST_SOURCE_COMMIT`** — 拉取请求源的 Git 提交哈希值。与 `CI_COMMIT` 值相同。
- **`CI_PULL_REQUEST_SOURCE_REPO`** — 拉取请求源仓库的全名，例如 `example/fork-of-example-framework`。如果拉取请求只涉及一个仓库，则该变量的值与 `CI_PULL_REQUEST_TARGET_REPO` 相同。
- **`CI_PULL_REQUEST_TARGET_BRANCH`** — 拉取请求的目标分支，例如 `main`。
- **`CI_PULL_REQUEST_TARGET_COMMIT`** — 拉取请求目标分支的最新 Git 提交哈希值。CI 服务会针对 `CI_PULL_REQUEST_TARGET_COMMIT` 和 `CI_PULL_REQUEST_SOURCE_COMMIT` 的合并来测试你的更改。
- **`CI_PULL_REQUEST_TARGET_REPO`** — 拉取请求目标仓库的全名，例如 `example/original-repository-of-example-framework`。如果拉取请求只涉及一个仓库，则该变量的值与 `CI_PULL_REQUEST_SOURCE_REPO` 相同。

### 特定操作的变量

以下环境变量的可用性取决于 Xcode Cloud 执行的操作。例如，`CI_ARCHIVE_PATH` 变量仅在 Xcode Cloud 执行归档操作时可用。

#### 测试操作的变量

- **`CI_RESULT_BUNDLE_PATH`** — 测试操作结果包（`.xcresult`）的路径。
- **`CI_TEST_DESTINATION_DEVICE_TYPE`** — 你选择作为测试操作目标的模拟设备的设备类型，例如 `iPhone 11`。
- **`CI_TEST_DESTINATION_RUNTIME`** — 你选择作为测试操作目标的模拟设备的 OS 版本，例如 `iOS 13.0`。
- **`CI_TEST_DESTINATION_UDID`** — 唯一标识你选择作为测试操作目标的模拟设备的字符串。
- **`CI_TEST_PLAN`** — 测试操作使用的测试计划的名称。仅在使用测试计划时此变量才可用。
- **`CI_TEST_PRODUCTS_PATH`** — 包含 Xcode Cloud 创建的项目测试产品的目录路径。

> [!note] 注意
> Xcode Cloud 将测试操作的所有环境变量提供给执行测试的进程（称为 _测试运行器（test runner）_）。这包括系统设置的环境变量，以及你在工作流程的“环境”部分设置的任何自定义环境变量。执行测试操作时，Xcode Cloud 会在每个变量名称前添加前缀 `TEST_RUNNER_`，这是 `xcodebuild` 为测试运行器进程按原始名称访问每个变量所必需的。有关在运行 `xcodebuild` 时在环境变量上使用 `TEST_RUNNER_` 前缀的更多信息，请参阅 `xcodebuild` 手册页的“环境变量”部分：[x-man-page://1/xcodebuild](x-man-page://1/xcodebuild)。

#### 归档操作的变量

- **`CI_AD_HOC_SIGNED_APP_PATH`** — 已针对 Ad Hoc 分发进行代码签名的已导出归档的路径。
- **`CI_APP_STORE_SIGNED_APP_PATH`** — 已针对 TestFlight 分发进行代码签名并符合 App Store 发布条件的已导出归档的路径。
- **`CI_ARCHIVE_PATH`** — Xcode Cloud 在运行归档操作时创建的已导出 App 归档的路径。
- **`CI_DEVELOPMENT_SIGNED_APP_PATH`** — 已针对开发分发进行代码签名的已导出 App 归档的路径。
- **`CI_DEVELOPER_ID_SIGNED_APP_PATH`** — 使用 Developer ID 证书进行代码签名的已导出 App 归档的路径。仅对在 Mac App Store 之外分发的 Mac App 使用 Developer ID 签名。有关更多信息，请参阅 [Developer ID](https://developer.apple.com/developer-id/)。

## 另请参阅

### 自定义构建脚本

- [编写自定义构建脚本](writing-custom-build-scripts.md) — 使用自定义构建脚本扩展你的 Xcode Cloud 工作流程，以执行自定义任务或安装其他工具。
