---
title: 在构建期间运行自定脚本
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/running-custom-scripts-during-a-build
source_url: 'https://developer.apple.com/documentation/xcode/running-custom-scripts-during-a-build'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/running-custom-scripts-during-a-build.json'
content_hash: 'sha256:04f3b0a0653f4cea'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Build system](build-system.md)

# 在构建期间运行自定脚本

<sub>文章</sub>

在构建过程中执行自定 Shell 脚本，并运行你项目所需的工具或其他命令。

## 概述

Xcode 提供了许多工具，用于将代码和资源转变为成品，但有时你需要为你的产品运行自定工具。例如，你可能想把部分资源打包成经过优化的格式，以加快运行时的访问速度。对于这类任务，你可以使用自定 Shell 脚本，在构建过程中执行所需的代码和工具。

> [!note] 注意
> 如果你的脚本会将一个或多个输入文件编译或转换为另一种格式，可以考虑改为为你的文件创建一条构建规则。更多信息，请参阅[为自定文件类型创建构建规则](creating-build-rules-for-custom-file-types.md)。

### 为你的目标添加运行脚本构建阶段

要在构建时执行自定脚本，请为你的目标添加一个「Run Script」构建阶段。这个构建阶段与目标的其他构建阶段（例如编译和链接构建阶段）分开运行。你可以为目标添加多个与脚本相关的构建阶段，以便在构建的不同阶段执行脚本。

要为目标添加「Run Script」构建阶段：

1. 在「项目」导航器中，选择你的项目。
2. 选择你想要修改的目标。
3. 点按「Build Phases」选项卡。
4. 点按添加按钮（+），然后从弹出菜单中选择「New Run Script Phase」。
5. 点按新添加的「Run Script」阶段的显示三角形。
6. 在「Shell」文本栏中，输入你的脚本代码。

![用于指定自定 Shell 脚本内容的编辑器面板。](../../../attachments/7702f841567fd1ffa65e3506dcd46fbd/build-run-script-phase@2x.png)

如果你已有一个现成的 Shell 脚本文件，可以将其拖到「Shell」文本栏中，将脚本复制到那里。你可以使用任何可用的 Shell 环境来执行脚本，并且可以通过更改脚本代码上方的 Shell 命令来更改执行所用的 Shell。

> [!note] 注意
> 要重命名脚本阶段，请双击「Run Script」标题以编辑它。

### 为你的脚本指定输入和输出文件

「Run Script」构建阶段提供了一个位置，供你输入脚本的任何输入和输出文件。使用输入和输出文件可以自定脚本的行为，并帮助构建系统了解何时执行你的脚本。输入文件包含你希望脚本处理的数据。例如，你可能会将一个或多个图像文件传给脚本。输出文件包含脚本生成的任何数据。

可以通过以下两种方式之一指定输入和输出文件：

- 将单个文件指定为路径字符串。通常，只有当你事先知道输入或输出文件、并确定它们不会改变时，才使用路径字符串。
- 在文件列表中指定文件，文件列表是一个扩展名为 `.xcfilelist` 的文本文件。文件列表能让编辑文件集合变得更容易，如果你经常更改文件列表，或者想要用注释为列表添加说明，文件列表会特别有用。

要将文件或文件列表添加到脚本中，请在「Run Script」构建阶段相应部分点按添加按钮。对于每个条目，请指定该文件或文件列表的路径，路径中可以包含构建变量。例如，字符串 `$(PROJECT_DIR)/myFileList` 指定了当前项目根目录中的一个文件列表。

如果你会定期更改输入或输出文件的集合，请使用文件列表来指定它们。文件列表包含一组以换行符分隔的路径字符串。每个路径字符串代表脚本的一个输入或输出文件。路径字符串可以包含诸如 `$(PROJECT_DIR)` 之类的构建变量。

> [!note] 注意
> Xcode 需要知道你脚本所访问的输入和输出文件集合，以便告知构建过程。这样做既能确保正确性——按正确的顺序运行脚本和其他并发执行的构建任务——又能通过仅在必要时才运行你的脚本来优化构建时间。如果你不指定这些文件，Xcode 会在每次构建目标时都运行你的脚本，这可能会导致不正确的构建行为。更多信息，请参阅[提升增量构建的速度](improving-the-speed-of-incremental-builds.md)。

### 通过环境变量访问与脚本相关的文件

Xcode 会为你的脚本配置执行环境，并让你的脚本能够访问与目标相同的构建设置和环境变量。Xcode 还会专门为你的脚本创建以下环境变量。

| 变量 | 描述 |
|---|---|
| `SCRIPT_INPUT_FILE_COUNT` | 作为脚本输入的可用文件总数。 |
| `SCRIPT_INPUT_FILE_[#]` | 包含脚本输入文件路径的环境变量。Xcode 会为每个输入文件创建一个环境变量，从 `SCRIPT_INPUT_FILE_0` 开始，并为后续每个文件依次递增数值。 |
| `SCRIPT_INPUT_FILE_LIST_COUNT` | 作为脚本输入的可用文件列表总数。 |
| `SCRIPT_INPUT_FILE_LIST_[#]` | 包含脚本输入文件列表路径的环境变量。Xcode 会为每个输入文件列表创建一个环境变量，从 `SCRIPT_INPUT_FILE_LIST_0` 开始，并为后续每个文件列表依次递增数值。 |
| `SCRIPT_OUTPUT_FILE_COUNT` | 被描述为脚本输出的文件总数。 |
| `SCRIPT_OUTPUT_FILE_[#]` | 包含脚本输出文件路径的环境变量。Xcode 会为每个输出文件创建一个环境变量，从 `SCRIPT_OUTPUT_FILE_0` 开始，并为后续每个文件依次递增数值。 |
| `SCRIPT_OUTPUT_FILE_LIST_COUNT` | 被描述为脚本输出的文件列表总数。 |
| `SCRIPT_OUTPUT_FILE_LIST_[#]` | 包含脚本输出文件列表路径的环境变量。Xcode 会为每个输出文件列表创建一个环境变量，从 `SCRIPT_OUTPUT_FILE_LIST_0` 开始，并为后续每个文件列表依次递增数值。 |

使用构建设置和脚本专属的环境变量来自定脚本的行为。例如，你可能会将脚本的输出文件写入 `BUILT_PRODUCTS_DIR` 构建设置所指定的目录中。有关构建设置的完整列表，请参阅[构建设置参考](build-settings-reference.md)。

### 从脚本中记录错误和警告

在脚本执行期间，你可以向 Xcode 构建系统报告错误、警告和一般说明。使用这些消息来诊断问题或跟踪脚本的进度。要写入消息，请使用 echo 命令，并按以下格式设置你的消息：

```
[filename]:[linenumber]: error | warning | note : [message]
```

如果存在 `error:`、`warning:` 或 `note:` 字符串，Xcode 会将你的消息添加到构建日志中。如果问题发生在某个特定文件中，请以绝对路径的形式包含该文件名。如果问题发生在文件的某一特定行，也请包含行号。文件名和行号都是可选的。

以下是一些错误和警告的示例：

```
echo "error: An expected input file was missing."
echo "warning: Skipping a file of an unknown type."
```

### 触发构建失败

当你的脚本失败且无法恢复时，请让脚本返回一个非零退出代码。Xcode 会将非零退出值视为构建失败，并将相应信息添加到日志中。

以下示例将一条错误消息记录到标准输出，并触发构建失败。

```
echo "error: A fatal error occurred in the script."
exit 1
```

## 另请参阅

### 构建自定

- [自定项目的构建 Scheme](customizing-the-build-schemes-for-a-project.md) — 指定要构建哪些目标，并自定 Xcode 用于构建、运行、测试和分析这些目标的设置。
- [自定目标的构建阶段](customizing-the-build-phases-of-a-target.md) — 指定在构建过程中要执行的任务，包括要编译的源文件、要运行的脚本，以及要包含在最终产品中的资源。
- [为自定文件类型创建构建规则](creating-build-rules-for-custom-file-types.md) — 告诉 Xcode 如何构建你项目中的自定文件类型，并提供依赖信息，以针对每个文件优化构建过程。
- [在特定平台或操作系统版本上运行代码](running-code-on-a-specific-version.md) — 在需要特定设备系列或最低操作系统版本才能运行的代码周围添加条件编译标记。
