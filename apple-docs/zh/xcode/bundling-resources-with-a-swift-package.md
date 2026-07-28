---
title: 通过 Swift Package 打包资源
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/bundling-resources-with-a-swift-package
source_url: 'https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/bundling-resources-with-a-swift-package.json'
content_hash: 'sha256:5bf427be76b1aa39'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Swift Package](swift-packages.md)

# 通过 Swift Package 打包资源

<sub>文章</sub>

将资源文件添加到你的 Swift Package，并在代码中访问它们。

## 概述

如果在 Package 清单中声明了 Swift 工具版本 5.3 或更高版本，便可以将资源与源代码一起打包为 Swift Package。例如，Swift Package 可以包含 Asset Catalog、Storyboard 等。

### 添加资源文件

与源代码类似，Xcode 将资源的作用域限定到某个 Target。将资源文件放入与该资源所属 Target 对应的文件夹中。例如，`MyLibrary` Target 的所有资源都需要放在 `Sources/MyLibrary` 中。不过，可以考虑为资源使用子文件夹，以便将其与源文件区分开来。例如，将所有资源文件放入名为 `Resources` 的目录，这样所有资源文件都将位于 `Sources/MyLibrary/Resources` 中。

要向 Swift Package 添加资源，请执行以下任一操作：

- 将它们拖入 Xcode 的项目导航器。
- 在 Xcode 的“File”菜单中，选择“Add Files to _[packageName]_”。
- 使用“访达”或“终端”App。

将资源添加到 Swift Package 时，Xcode 会自动检测 Apple 平台的常见资源类型，并将其视为资源。例如，以下资源无需修改 Package 清单：

- Interface Builder 文件，例如 XIB 文件和 Storyboard
- Core Data 文件，例如 `xcdatamodeld` 文件
- Asset Catalog
- 用于提供本地化资源的 `.lproj` 文件夹

如果你添加了一个 Xcode 默认不视为资源的资源文件，则必须按照下一节的说明在 Package 清单中对其进行配置。

### 明确声明或排除资源

若要添加 Xcode 无法自动处理的资源，请在 Package 清单中将其明确声明为资源。以下示例假设 `text.txt` 位于 `Sources/MyLibrary` 中，并且你希望将其包含在 `MyLibrary` Target 中。为了将其明确声明为 Package 资源，需要在 Package 清单中将文件名传递给 Target 的初始化方法：

```swift
targets: [
    .target(
        name: "MyLibrary",
        resources: [
            .process("text.txt")]
    ),
]
```

请注意上述示例代码使用了 [process(_:localization:)](<../packagedescription/resource/process(__localization_).md>) 函数。当你明确声明一个资源时，必须选择以下规则之一来决定 Xcode 如何处理该资源文件：

- **Process 规则** — 对于大多数用例，使用 [process(_:localization:)](<../packagedescription/resource/process(__localization_).md>) 应用此规则，让 Xcode 根据构建 Package 的平台来处理资源。例如，Xcode 可能会针对支持此类优化的平台优化图像文件。如果将 process 规则应用于目录路径，Xcode 会递归地将该规则应用于目录内容。如果某个资源没有可用的特殊处理，Xcode 会将该资源复制到资源 Bundle 的顶级目录。
- **Copy 规则** — 某些 Swift Package 可能需要资源文件保持不变，或者为资源保留特定的目录结构。使用 [copy(_:)](<../packagedescription/resource/copy(__).md>) 函数应用此规则，让 Xcode 按原样将资源复制到资源 Bundle 的顶级目录。如果将目录路径传递给 copy 规则，Xcode 会保留该目录的结构。

如果文件位于 Target 的文件夹内，而你又不希望它成为 Package 资源，请将其传递给 Target 初始化方法的 `exclude` 参数。下一个示例假设 `instructions.md` 是一个包含文档的 Markdown 文件，位于 `Sources/MyLibrary` 中，并且不应成为 Package 资源 Bundle 的一部分。以下代码展示了如何通过将该文件添加到排除文件列表来将其从 Target 中排除：

```swift
targets: [
    .target(
        name: "MyLibrary",
        exclude:["instructions.md"]
    ),
]
```

通常，应避免将非资源文件放在 Target 的源文件夹中。如果无法做到，则应避免逐个排除每个文件，而是将所有要排除的文件放入一个目录，并将该目录的路径添加到排除文件数组中。

### 在代码中访问资源

当你构建 Swift Package 时，Xcode 会将每个 Target 视为一个 Swift 模块。如果某个 Target 包含资源，Xcode 会为该模块创建一个资源 Bundle 和一个内部静态扩展（extension），以便通过 [Bundle](../foundation/bundle.md) 访问该 Bundle。使用该扩展来定位 Package 资源。例如，使用以下代码检索随 Package 打包的属性列表（property list）的 URL：

`let settingsURL = Bundle.module.url(forResource: "settings", withExtension: "plist")`

> [!important] 重要
> 访问资源时始终使用 `Bundle.module`。Package 不应假设资源的精确位置。

如果希望让依赖于你 Swift Package 的 App 也能使用 Package 资源，请为其声明一个公开常量。例如，使用以下代码向使用你 Swift Package 的 App 公开一个属性列表文件：

`public let settingsURL = Bundle.module.url(forResource: "settings", withExtension: "plist")`

## 另请参阅

### 创建 Package

- [使用 Xcode 创建独立的 Swift Package](creating-a-standalone-swift-package-with-xcode.md) — 将可执行或可共享的代码打包到独立的 Swift Package 中。
- [本地化 Package 资源](localizing-package-resources.md) — 确保你的 Swift Package 为多种语言区域提供本地化资源。
- [以 Swift Package 形式分发二进制框架](distributing-binary-frameworks-as-swift-packages.md) — 通过创建包含一个或多个 XCFramework 的 Swift Package，让其他开发者能够使用你的二进制文件。
- [配合 App 同步开发 Swift Package](developing-a-swift-package-in-tandem-with-an-app.md) — 将你已发布的 Swift Package 作为本地 Package 添加到 App 项目中，并同步开发 Package 和 App。
- [使用本地 Package 组织代码](organizing-your-code-with-local-packages.md) — 通过将 App 代码组织到本地 Swift Package 中，简化维护、促进模块化并鼓励代码复用。
- [PackageDescription](../packagedescription.md) — 创建可复用的代码，以轻量化的方式组织代码，并在各项目及与其他开发者之间共享。
