---
title: 以 Swift 包的形式分发二进制框架
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/distributing-binary-frameworks-as-swift-packages
source_url: 'https://developer.apple.com/documentation/xcode/distributing-binary-frameworks-as-swift-packages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/distributing-binary-frameworks-as-swift-packages.json'
content_hash: 'sha256:275a6c826f8c9324'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Swift 包](swift-packages.md)

# 以 Swift 包的形式分发二进制框架

<sub>文章</sub>

通过创建包含一个或多个 XCFramework 的 Swift 包，让其他开发者可以使用你的二进制文件。

## 概述

创建 Swift 包来组织和共享代码，能让将 Swift 包用作包依赖（package dependency）的开发者获取源文件。但你可能需要以二进制形式提供代码，以保护你的知识产权——例如，当你开发专有的闭源库时。

请仔细考虑是否要以二进制形式分发代码，因为这样做存在一些缺点。例如，包含二进制的 Swift 包可移植性较差，因为它只能支持其所含二进制支持的平台。此外，二进制依赖仅适用于 Apple 平台，这限制了你的 Swift 包的受众范围。

> [!note] 注意
> Swift 包可以同时包含源文件和二进制文件。这种使用场景在包含封装闭源二进制文件的源代码的包中很常见。

### 以 XCFramework bundle 形式打包二进制文件

要以二进制形式通过 Swift 包分发代码，需要创建一个包含二进制文件的 XCFramework bundle（即*产物*）。然后，将该 bundle 放在本地或服务器上供人使用：

- 当你在服务器上托管二进制文件时，请创建一个 ZIP 归档文件，将 XCFramework 放在其根目录中，并公开提供该归档文件。
- 如果 XCFramework 在本地可用，并包含在包的 Git 仓库中，则无需创建压缩归档，可以直接引用该 XCFramework。

要了解更多关于创建 XCFramework bundle 的信息，请参阅[创建跨平台二进制框架 bundle](creating-a-multi-platform-binary-framework-bundle.md)。

### 在包清单中声明二进制目标

首先，按照[使用 Xcode 创建独立 Swift 包](creating-a-standalone-swift-package-with-xcode.md) 中描述的过程创建一个新的 Swift 包。接下来，在包清单中声明一个*二进制目标*，并将其设为产品的一部分——就像处理包含源文件的目标一样。确保包清单中二进制目标的名称与产物的模块名称匹配。

要声明一个远程的（即*基于 URL 的*）二进制目标，请使用 [binaryTarget(name:path:)](<../packagedescription/target/binarytarget(name_path_).md>)。要创建所需的[校验码](../packagedescription/target/checksum.md)，请打开“终端” App，导航至包的根目录，然后运行 `swift package compute-checksum path/to/MyFramework.zip`。Xcode 使用校验码来验证托管的归档文件是否与你声明在清单文件中的归档文件一致。当开发者将此包作为二进制依赖添加到他们的项目，且远程归档文件的校验码与包清单中的校验码不匹配时，Xcode 会显示错误。

要声明一个本地的（即*基于路径的*）二进制目标，请使用 [package(name:path:)](<../packagedescription/package/dependency/package(name_path_).md>) 并且无需生成校验码。相反，你需要将 `.xcframework` bundle 包含在包的 Git 仓库中。

以下针对 MyLibrary 包的清单文件声明了一个库产品，该产品包含两个二进制目标：`SomeRemoteBinaryPackage`（一个远程的、基于 URL 的二进制目标）和 `SomeLocalBinaryPackage`（一个本地的、基于路径的二进制目标）。

```swift
// swift-tools-version:5.3
import PackageDescription

let package = Package(
    name: "MyLibrary",
    platforms: [
        .macOS(.v10_14), .iOS(.v13), .tvOS(.v13)
    ],
    products: [
        // Products define the executables and libraries a package produces, and make them visible to other packages.
        .library(
            name: "MyLibrary",
            targets: ["MyLibrary", "SomeRemoteBinaryPackage", "SomeLocalBinaryPackage"])
    ],
    dependencies: [
        // Dependencies declare other packages that this package depends on.
    ],
    targets: [
        // Targets are the basic building blocks of a package. A target can define a module or a test suite.
        // Targets can depend on other targets in this package, and on products in packages this package depends on.
        .target(
            name: "MyLibrary"
        ),
        .binaryTarget(
            name: "SomeRemoteBinaryPackage",
            url: "https://url/to/some/remote/xcframework.zip",
            checksum: "The checksum of the ZIP archive that contains the XCFramework."
        ),
        .package(
            name: "SomeLocalBinaryPackage",
            path: "path/to/some.xcframework"
        )
        .testTarget(
            name: "MyLibraryTests",
            dependencies: ["MyLibrary"]),
    ]
)
```

## 另请参阅

### 包创建

- [使用 Xcode 创建独立 Swift 包](creating-a-standalone-swift-package-with-xcode.md) — 将可执行或可共享的代码打包成独立 Swift 包。
- [将资源与 Swift 包捆绑](bundling-resources-with-a-swift-package.md) — 向你的 Swift 包添加资源文件，并在代码中访问它们。
- [本地化包资源](localizing-package-resources.md) — 确保你的 Swift 包为多种语言区域提供本地化资源。
- [与 App 并行开发 Swift 包](developing-a-swift-package-in-tandem-with-an-app.md) — 将你已发布的 Swift 包作为本地包添加到你的 App 项目中，并行开发包与 App。
- [使用本地包组织代码](organizing-your-code-with-local-packages.md) — 通过将你的 App 代码组织到本地 Swift 包中，简化维护、促进模块化并鼓励复用。
- [PackageDescription](../packagedescription.md) — 创建可复用代码，以轻量方式组织，并在你的项目以及其他开发者之间共享。
