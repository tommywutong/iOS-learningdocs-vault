---
title: 识别二进制依赖项
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/identifying-binary-dependencies
source_url: 'https://developer.apple.com/documentation/xcode/identifying-binary-dependencies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/identifying-binary-dependencies.json'
content_hash: 'sha256:d36175e232ebaf94'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Swift packages](swift-packages.md)

# 识别二进制依赖项

<sub>文章</sub>

查明某个 package 依赖项是否引用了二进制文件，并验证该二进制文件的真实性。

## 概述

当你为 App 添加基于源代码的 package 依赖项时，你可以检查其源代码、贡献错误修复，并在需要时重新编译源代码。然而，package 作者也可能选择以二进制形式分发其代码。例如，一家公司可能更倾向于分发二进制文件而非源文件，以保护知识产权。一般来说，引入依赖项总是需要仔细权衡，因为你是在为你的 App 添加代码；如果你要添加的是二进制依赖项，就更需要谨慎。因此，了解如何识别二进制依赖项非常重要。

### 审视二进制依赖项

请仔细考虑是否要添加二进制依赖项，因为这样做存在一些弊端。例如，二进制依赖项的可移植性较差，因为它只能支持其内含二进制文件所支持的平台，而且二进制依赖项仅适用于 Apple 平台。如果你可以在基于源代码的依赖项和二进制依赖项之间做选择，并且两者提供相同的功能，请使用基于源代码的依赖项。

### 识别二进制依赖项

要查明某个 package 依赖项本身是否为二进制依赖项，或者某个基于源代码的 package 是否依赖于二进制依赖项：

1. 在 Xcode 中打开你 App 的项目，并确保项目导览器可见。
2. 展开「Swift Package Dependencies」以及某个具体的 package 依赖项。
3. 查找名为「Referenced Binaries」的文件夹。如果存在，说明该 package 依赖项本身分发了二进制文件，或者依赖于某个二进制依赖项。
4. 要进一步检查所引用的二进制文件，按住 Control 键点按「Referenced Binaries」文件夹内的 XCFramework 包，并在「访达」中打开它。

下图展示了某个 App 已展开的 Swift package 依赖项，其中包括一个名为 SomeRemoteBinaryPackage 的、分发了二进制文件的 package 依赖项。

![显示项目导览器中含有二进制依赖项的截图。](../../../attachments/565c403a91000451d3400e59137cc614/identifying-binary-dependencies-1@2x.png)

> [!note] 注意
> 为帮助验证二进制依赖项的来源，其作者必须创建一个[校验和](../packagedescription/target/checksum.md)并将其包含在 package 清单中。当 Xcode 解析或更新 package 依赖项时，不允许二进制依赖项在不同时更改版本的情况下更改校验和。

## 另请参阅

### Package 依赖项

- [向你的 App 添加 package 依赖项](adding-package-dependencies-to-your-app.md) — 集成 package 依赖项以在项目之间共享代码，或利用其他开发者的代码。
- [将某个 package 依赖项作为本地 package 进行编辑](editing-a-package-dependency-as-a-local-package.md) — 通过将某个 package 依赖项添加为本地 package 来覆盖它并编辑其内容。
