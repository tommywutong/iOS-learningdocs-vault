---
title: 编写自定构建脚本
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/writing-custom-build-scripts
source_url: 'https://developer.apple.com/documentation/xcode/writing-custom-build-scripts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/writing-custom-build-scripts.json'
content_hash: 'sha256:dc7b65172484640a'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 编写自定构建脚本

<sub>文章</sub>

使用执行自定任务或安装其他工具的自定构建脚本，扩展 Xcode Cloud 工作流。

## 概述

Xcode Cloud 会利用项目中配置的方案，并提供用于创建高级工作流的设置。不过，Xcode Cloud 工作流还能提供更大的灵活性，以满足项目需求。例如，你可能需要安装其他第三方工具才能成功构建项目，将构建构件上传到私有存储空间，为每夜构建使用不同的 App 图标，等等。

如果 Xcode Cloud 工作流需要更大的灵活性，请创建一个_自定构建脚本（custom build script）_，在指定时间执行特定任务。Xcode Cloud 可以识别三种不同类型的脚本：

- Xcode Cloud 克隆 Git 仓库后运行的_克隆后脚本_。
- Xcode Cloud 运行 `xcodebuild` 前执行的_前置 `xcodebuild` 脚本_。
- Xcode Cloud 运行 `xcodebuild` 后执行的_后置 `xcodebuild` 脚本_。

要让 Xcode Cloud 识别自定构建脚本，需要将它们放在特定位置：`ci_scripts` 目录。Xcode Cloud 会从该目录运行自定构建脚本。此外，请按照下方列出的约定为脚本命名。开始新构建时，Xcode Cloud 会自动识别你的自定构建脚本，并为每个操作运行它们。

> [!important] 重要
> Xcode Cloud 使用 `zsh` 作为默认 Unix shell。最佳做法是始终在自定构建脚本的第一行加入 shebang，例如 `#!/bin/sh`。

有关自定构建脚本的更多信息，请参阅[自定高级 Xcode Cloud 工作流](https://developer.apple.com/videos/play/wwdc2021/10269)。有关安装第三方工具的更多信息，请参阅[使用自定构建脚本安装第三方依赖项或工具](making-dependencies-available-to-xcode-cloud.md#Use-a-custom-build-script-to-install-a-third-party-dependency-or-tool)。

### 创建 CI 脚本目录

自定构建脚本位于名为 `ci_scripts` 的目录中，该目录与 Xcode 项目或工作区位于同一目录下。Xcode Cloud 会以此目录作为根目录运行自定构建脚本。

要创建 `ci_scripts` 目录：

1. 在 Xcode 中打开项目或工作区，并导览到项目导航器。
2. 在项目导航器中，按住 Control 键点按项目，然后选择 New Group，以创建组及其对应目录。
3. 将新组命名为 `ci_scripts`。

### 创建自定构建脚本

Xcode Cloud 执行你添加到工作流的操作时，会执行一系列步骤。如果添加自定构建脚本，Xcode Cloud 会在这些步骤之间的特定时刻运行它。

自定脚本对应文件的名称决定 Xcode Cloud 何时运行该脚本；脚本只能使用以下文件名：

- **`ci_post_clone.sh`** — 克隆后脚本在 Xcode Cloud 克隆 Git 仓库后运行。你可以使用克隆后脚本安装其他工具，或向属性列表添加新条目。
- **`ci_pre_xcodebuild.sh`** — 前置 `xcodebuild` 脚本在 Xcode Cloud 运行 `xcodebuild` 命令前执行。你可以使用前置 `xcodebuild` 脚本编译其他依赖项。
- **`ci_post_xcodebuild.sh`** — 后置 `xcodebuild` 脚本在 Xcode Cloud 运行 `xcodebuild` 命令后执行，即使 `xcodebuild` 命令失败也会运行。你可以使用后置 `xcodebuild` 脚本将构件上传到存储空间或其他服务。

![](../../../attachments/6dc78b269a115b929a161d8daec31be0/Writing-Custom-Build-Scripts-1@2x.png)

<sub>一幅插图，从左到右展示 Xcode Cloud 执行操作时所完成的不同步骤，其中包括自定构建脚本。</sub>

要创建自定构建脚本：

1. 在 Xcode 中打开项目或工作区，并导览到项目导航器。
2. 按住 Control 键点按之前创建的 `ci_scripts` 组，然后选择 New File。
3. 选择 Shell Script 模板。
4. 将 shell 脚本命名为 `ci_post_clone.sh`、`ci_pre_xcodebuild.sh` 或 `ci_post_xcodebuild.sh`。
5. 创建文件，但不要将其添加到 target。
6. 在“终端”中运行 `chmod +x $filename.sh`，使 shell 脚本成为可执行文件。
7. 向自定构建脚本添加代码，包括在第一行加入 shebang（例如 `#!/bin/sh`），然后将其添加到 Git 仓库。Xcode Cloud 会在开始下一次构建时自动运行该脚本。

如果文件可执行，Xcode Cloud 会遵循 shebang。如果未在自定脚本的第一行加入 shebang，或忘记将文件设为可执行，Xcode Cloud 会以 `zsh $filename` 运行脚本；根据脚本内容，这可能会导致构建失败。

> [!note] 注意
> 你无法在自定构建脚本中使用 `sudo` 获取管理员权限。

通过自定构建脚本创建的文件无法供其他自定构建脚本使用，并且 Xcode Cloud 会删除自定构建脚本创建的所有文件。因此，可下载的 Xcode Cloud 构建构件不包含你使用自定构建脚本创建的文件。

### 向 CI 脚本目录添加资源

自定构建脚本在临时构建环境中运行，此时源代码可能不可用。因此，需要将自定脚本访问的所有资源放入 `ci_scripts` 目录。例如，将图稿或 `.plist` 文件放入该目录。

> [!note] 注意
> 使用 `ci_scripts` 目录中的子目录整理内容。不过，请务必将三个自定构建脚本 `ci_post_clone.sh`、`ci_pre_xcodebuild.sh` 和 `ci_post_xcodebuild.sh` 放在 `ci_scripts` 目录的顶层。

在某些情况下，自定构建脚本需要访问仓库中的文件，但将该文件放入 `ci_scripts` 目录并不实际。此时，请在 `ci_scripts` 目录中创建指向该文件的符号链接。Xcode Cloud 会检测该符号链接，并在运行操作的后续阶段使其可在 `ci_scripts` 目录中使用。

### 访问环境变量

环境变量是自定脚本的关键，因为它们让你可以编写具有高级控制流的灵活自定脚本。例如，以下代码片段会检查 `CI_PULL_REQUEST_NUMBER` 变量是否存在，使某条命令仅在 Xcode Cloud 将脚本作为拉取请求构建的一部分运行时执行：

```bash
#!/bin/sh

if [[ -n $CI_PULL_REQUEST_NUMBER ]];
then
    echo "This build started from a pull request."

    # 仅当构建从拉取请求开始时才执行操作。
fi
```

有关预定义环境变量的列表，请参阅[环境变量参考](environment-variable-reference.md)。

### 定义自定环境变量

除预定义环境变量外，你还可以在工作流的 Environment 部分中定义自定环境变量。要进一步了解如何配置自定环境变量，请参阅[自定环境变量](xcode-cloud-workflow-reference.md#Custom-environment-variables)

### 添加调试信息

自定构建脚本的输出会出现在构建报告的构建日志中。请记录在调试自定构建脚本时可能有帮助的信息。不过，除非使用 secret 自定环境变量，否则绝不要在 shell 脚本输出中记录 API 密钥或访问令牌等敏感信息。如果将自定环境变量标记为 secret，Xcode Cloud 会在构建日志中使用星号（`**********`）替换其值。

### 编写弹性脚本

自定构建脚本可以执行安装依赖项或将构建构件上传到存储空间等关键任务。请编写能够妥善处理错误的弹性代码；如果命令失败，则返回非零退出码。自定构建脚本返回非零退出码，可以让 Xcode Cloud 知道出现了问题，并使构建失败，从而通知你存在问题。

以下构建脚本会设置 `-e` 选项，在命令以非零退出码退出时停止脚本。此外，如果出现问题，也会返回非零退出码：

```bash
#!/bin/sh

# 设置 -e 标志，以便在命令返回非零退出码时
# 停止运行脚本。
set -e

# 命令或脚本已成功执行。
echo "A command or script was successful."
exit 0

...

# 出现了问题。
echo "Something went wrong. Include helpful information here."
exit 1
```

### 在复杂的自定构建脚本中使用辅助脚本

如果仓库包含多个项目，你很可能需要配置多个 Xcode Cloud 工作流。由于 Xcode Cloud 只能识别仓库中的一个 `ci_scripts` 目录，而且该目录只能包含三个自定构建脚本，因此需要添加_辅助脚本（helper script）_。辅助脚本是你放在 `ci_scripts` 目录中的 shell 脚本，可用于拆分默认构建脚本的任务。

你可以使用辅助脚本创建更灵活的构建环境，将希望 Xcode Cloud 在自定构建脚本中执行的大部分逻辑卸载到单独的 shell 脚本文件中。例如，你可以使用环境变量确定哪个 Xcode Cloud 工作流正在运行构建脚本、什么事件开始了构建、正在运行的构建针对哪个平台等，从而仅在适用时运行逻辑。

> [!note] 注意
> Xcode Cloud 使用 `zsh` 作为默认 Unix shell。请将脚本设为可执行，并在脚本开头添加 shebang 行，以免构建失败。例如，为使用 Python 编写、将构建构件上传到服务器的辅助脚本添加 `#!/usr/bin/env python3`。如果使用 Swift 编写辅助脚本，请使用 `#!/usr/bin/env swift`。

为辅助脚本命名时，请使用便于识别脚本用途的文件名。例如，你可以在辅助脚本前加上其目标平台的名称，并将以下脚本命名为 `platform-detect.sh`，因为它使用 `CI_PRODUCT_PLATFORM` 变量检测当前构建的平台：

```bash
#!/bin/sh

if [ $CI_PRODUCT_PLATFORM = 'macOS' ]
then
    ./macos_perform_example_task.sh
else
    ./iOS_perform_example_task.sh
fi
```

为使辅助脚本更容易识别，应避免使用 `ci_` 作为脚本名称的前缀。

## 另请参阅

### 自定构建脚本

- [环境变量参考](environment-variable-reference.md) — 查看在自定构建脚本中使用的预定义环境变量。
