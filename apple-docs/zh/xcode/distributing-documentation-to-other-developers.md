---
title: 向其他开发者分发文档
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/distributing-documentation-to-other-developers
source_url: 'https://developer.apple.com/documentation/xcode/distributing-documentation-to-other-developers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/distributing-documentation-to-other-developers.json'
content_hash: 'sha256:9c7e1ed00636f883'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Writing documentation](writing-documentation.md)

# 向其他开发者分发文档

<sub>文章</sub>

直接与 Xcode 用户共享你的文档，或将其托管在网络服务器上。

## 概述

一旦你在 Xcode 中创建了一个项目，DocC 就已经可以为你项目中的符号生成结构化文档。无论你只是在源文件中写有文档注释，还是精心制作了包含文章和教程的完整学习体验，Xcode 都提供了一种便捷的方式，让你能与其他开发者共享项目中的文档。

要共享你的文档，你需要创建一个 _文档归档_，这是一个包含你所需一切内容的自包含 bundle，其中包括：

- 从源码内注释、文章、教程和资源编译而成的文档
- 一个用于渲染文档的单页 Web App

分发你的文档涉及以下步骤：

1. 从 Xcode 的文档查看器导出你的文档，或使用 `xcodebuild` 命令行工具导出。
2. 共享你的文档，可以直接分享给在文档查看器中打开它的 Xcode 用户，也可以将其托管在一个网站上。

### 生成可发布的文档归档

要创建文档归档，你需要从文档查看器导出文档，或使用 `xcodebuild docbuild` 命令行工具。使用 `xcodebuild` 可以让你与持续集成（CI）工作流集成。

要从 Xcode 的文档查看器导出文档归档：

1. 将指针悬停在 Workspace Documentation 部分中已编译的文档目录上，以显示 More 按钮。
2. 点按 More 按钮并选择 Export 菜单项。或者，也可以在该文档目录项上调出上下文菜单以访问 Export 菜单。
3. 为该文档归档选择一个位置，然后点按 Export。

![Xcode 文档查看器的屏幕截图，显示了一个上下文菜单，其中 Export 菜单项处于选中状态。](../../../attachments/9d3e272f4b845ad6f3f1e062acacd3b3/distributing-documentation-to-other-developers-1@2x.png)

Xcode 导出的文档归档使用 `.doccarchive` 文件扩展名。

要从命令行导出文档归档，请在终端中运行 `xcodebuild docbuild`，然后从派生数据目录中复制生成的 `.doccarchive` bundle。根据你项目的配置，你可能需要传入额外的命令行选项。有关更多信息，请查阅 `xcodebuild` 的 man 手册页。

例如，要构建一个文档归档，可以使用类似下面的命令：

```shell
xcodebuild docbuild -scheme SlothCreator -derivedDataPath ~/Desktop/SlothCreatorBuild
```

> [!tip] 提示
> 虽然 `-derivedDataPath` 不是必需的选项，但包含它可以让自动化脚本更容易识别构建输出并找到生成的 `.doccarchive` bundle。

作为构建过程的一部分，`xcodebuild` 会在派生数据路径中生成许多文件。在构建输出中定位文档归档的一种方法是使用 `find` 命令。例如，使用以下命令定位上面 `xcodebuild` 命令生成的文档归档：

```shell
find ~/Desktop/SlothCreatorBuild -type d -name '*.doccarchive`
```

### 将文档归档直接发送给开发者

由于文档归档是一个自包含的 bundle，你可以轻松地与其他开发者共享它。例如，你可以像发送普通文稿一样通过电子邮件发送它，将它与产品的二进制分发版本一起提供，或者让它可以从某个网站下载。当接收者打开该文档归档时，Xcode 会将它添加到文档查看器的 Imported Documentation 部分。

![](../../../attachments/6be1f1854054fa26972a5aaf4b509773/distributing-documentation-to-other-developers-2@2x.png)

<sub>Xcode 文档查看器的屏幕截图，显示了 Imported Documentation 部分中一个 SlothCreator 项目的文档归档处于选中状态。</sub>

要移除一个已导入的文档归档，请将指针悬停在该项上以显示 More 按钮，然后选择 Remove。

### 在你的网站上托管文档归档

当 Xcode 导出文档归档时，它会在该 bundle 中包含一个单页 Web App。这个 Web App 会将文档内容渲染为 HTML，让你能够在网络服务器上托管该文档归档。

对于参考文档和文章，该 Web App 使用以 `/documentation` 开头的 URL 路径。对于教程，URL 路径以 `/tutorials` 开头。例如，如果某个项目包含一个名为 `SlothGenerator` 的协议，那么查看 `SlothGenerator` 文档的 URL 可能类似于以下内容：

```
https://www.example.com/documentation/SlothCreator/SlothGenerator
```

#### 使用文件服务器托管文档归档

你可以使用常规的文件服务器托管使用 Xcode 14.3 及更高版本创建的文档归档。默认情况下，服务器会在网站的根目录托管文档，就像上面的 SlothCreator 示例一样。要在特定的子路径托管文档，请在构建文档归档之前配置一个自定 [DocC Archive Hosting Base Path](build-settings-reference.md#DocC-Archive-Hosting-Base-Path)。

#### 使用自定路由托管文档归档

文件服务器是托管你的文档的推荐解决方案。但是，如果你需要对服务器如何托管你的内容有更多控制，你可以配置你的网络服务器的请求路由，使其用文档归档中的数据和资源来响应文档请求。

> [!note] 注意
> 以下各节以 Apache 作为示例。其他网络服务器安装方式也有类似的机制。有关执行类似配置的详细信息，请查阅你的服务器的文档。

要在你的网站上托管文档归档，请执行以下操作：

1. 将文档归档复制到你的网络服务器用于提供文件的目录中。在这个示例中，该文档归档是 `SlothCreator.doccarchive`。
2. 在服务器上添加一条规则，将以 `/documentation` 或 `/tutorial` 开头的传入 URL 重写为 `SlothCreator.doccarchive/index.html`。
3. 添加另一条针对传入请求的规则，以支持文档归档中打包的资源，例如 CSS 文件和图像资源。

以下示例 `.htaccess` 文件定义了适用于 Apache 的规则：

```shell
# 启用自定路由。
RewriteEngine On

# 路由文档和教程页面。
RewriteRule ^(documentation|tutorials)\/.*$ SlothCreator.doccarchive/index.html [L]

# 为文档归档路由文件和数据。
#
# 如果该文件路径在网站根目录下不存在……
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d

# ……则将该请求路由到文档归档中的该文件路径。
RewriteRule .* SlothCreator.doccarchive/$0 [L]
```

有了这些规则，网络服务器就能提供对文档归档内容的访问。

在配置好你的网络服务器以托管文档归档之后，请使用持续集成工作流保持其最新——该工作流使用 `xcodebuild docbuild` 构建文档归档，并将生成的 `.doccarchive` 复制到你的网络服务器。
