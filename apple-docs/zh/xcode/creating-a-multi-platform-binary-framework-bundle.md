---
title: 创建多平台二进制框架捆绑包
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-a-multi-platform-binary-framework-bundle
source_url: 'https://developer.apple.com/documentation/xcode/creating-a-multi-platform-binary-framework-bundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-a-multi-platform-binary-framework-bundle.json'
content_hash: 'sha256:b3fc1fb175923ff6'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [捆绑包与框架](bundles-and-frameworks.md)

# 创建多平台二进制框架捆绑包

<sub>文章</sub>

将二进制框架或库的变体组合成一个支持多平台的 XCFramework 捆绑包。

## 概述

XCFramework 捆绑包（或称*产物*）是由 Xcode 创建的二进制软件包，包含为多个平台（iOS、iPadOS、macOS、tvOS、visionOS、watchOS 和 DriverKit，含模拟器构建版本）构建所必需的框架和库。框架可静态也可动态，并且也包含头文件。

将 XCFramework 捆绑包包含在 Swift Package 中，以二进制形式分发代码，供其他项目使用。有关更多信息，请参阅[将二进制框架作为 Swift 软件包分发](distributing-binary-frameworks-as-swift-packages.md)。

> [!note] WWDC19 相关讲座
> 讲座 417：[Swift 中的二进制框架](https://developer.apple.com/videos/play/wwdc2019/416)

### 设置项目

若要为创建 XCFramework 而设置项目，请确保你的 Xcode 项目有一个 scheme，仅构建框架 target 及其依赖项。

在你的 target 上配置这些 build settings（构建设置）：

- 将 [Build Libraries for Distribution](build-settings-reference.md#Build-Libraries-for-Distribution) 构建设置设为“是”。对于 Swift，这会启用对库演变（Library Evolution）的支持并生成模块接口文件。
- 将 [Skip Install](build-settings-reference.md#Skip-Install) 构建设置设为“否”。如果启用，构建产物将不会包含在归档中。
- 保持 [Architectures](build-settings-reference.md#Architectures) 构建设置为未设置状态。预定义值会将 target 配置为目标平台可能使用的所有架构构建通用二进制文件。

有关更多信息，请参阅[自定义项目的构建方案](customizing-the-build-schemes-for-a-project.md)和[配置 target 的构建设置](configuring-the-build-settings-of-a-target.md)。

### 为框架或库创建归档

在“终端”中使用 `archive` 构建操作运行 `xcodebuild`，为你希望支持的每个平台创建框架或库的归档。

以下命令为 iOS 平台归档框架：

```
xcodebuild archive 
    -project MyFramework.xcodeproj
    -scheme MyFramework
    -destination "generic/platform=iOS"
    -archivePath "archives/MyFramework"
```

如上例所示，使用 `-destination` 标志运行命令时，系统会根据构建设置确定架构和 SDK。使用此标志而非 `-arch` 和 `-sdk` 可以避免常见错误。

若要为其他平台构建归档，请调整 `-destination` 的值。将此值替换为 `"generic/platform=iOS Simulator"` 可为模拟器创建归档。

XCFramework 可以包含为 macOS（含与不含 Mac Catalyst）构建的框架版本。若要为 Mac Catalyst 变体生成归档，请使用 `"generic/platform=macOS,variant=Mac Catalyst"`，将变体类型添加到 `-destination` 值中。

若要查看所有命令选项的详尽列表，请使用 `-help` 标志执行 `xcodebuild`。

> [!note] 注意
> XCFramework 的使用方需要它支持该平台使用的所有可能架构。随着平台逐步采用新架构（例如 macOS 和 iOS Simulator 采用 Apple 芯片），请通过重新构建框架和库以包含新架构，来保持 XCFramework 中包含的二进制文件是最新的。若要确定二进制文件支持的架构，请参阅[确定二进制文件支持的架构](creating-a-multi-platform-binary-framework-bundle.md#Determine-the-architectures-a-binary-supports)。

### 生成 XCFramework 捆绑包

若要将给定框架或库的已构建内容，针对多个平台和变体打包为单个 XCFramework 捆绑包，请执行带有 `-create-xcframework` 选项的 `xcodebuild`。

以下命令创建包含 iOS、iOS Simulator、macOS 和 Mac Catalyst 变体的 XCFramework：

```
xcodebuild -create-xcframework
    -archive archives/MyFramework-iOS.xcarchive -framework MyFramework.framework
    -archive archives/MyFramework-iOS_Simulator.xcarchive -framework MyFramework.framework
    -archive archives/MyFramework-macOS.xcarchive -framework MyFramework.framework
    -archive archives/MyFramework-Mac_Catalyst.xcarchive -framework MyFramework.framework
    -output xcframeworks/MyFramework.xcframework
```

若要包含静态库文件（`.a` 文件），请在上面的命令中将 `-framework` 替换为 `-library`。

如果希望包含的内容存在于归档之外，请为 `-framework` 或 `-library` 的实例提供路径，并使用额外的 `-headers` 标志指定头文件路径。

```
xcodebuild -create-xcframework
    -library products/iOS/usr/local/lib/libMyLibrary.a -headers products/iOS/usr/local/include
    -library products/iOS_Simulator/usr/local/lib/libMyLibrary.a -headers products/iOS/usr/local/include
    -library products/macOS/usr/local/lib/libMyLibrary.a -headers products/macOS/usr/local/include
    -library products/Mac\ Catalyst/usr/local/lib/libMyLibrary.a -headers products/Mac\ Catalyst/usr/local/include
    -output xcframeworks/MyLibrary.xcframework
```

若要查看 XCFramework 实用工具支持的所有选项，请执行：

```
xcodebuild -create-xcframework -help
```

### 对 XCFramework 捆绑包进行签名

使用你的代码签名身份对 XCFramework 进行签名，可以告知使用你框架的开发者该框架来自你，并且在添加签名后未被篡改。若要对框架进行签名，请运行以下命令：

```
% codesign --timestamp -s <identity> xcframeworks/MyLibrary.xcframework
```

若要为作为 Apple Developer Program 成员分发而签名框架，你的代码签名身份应为 Apple Distribution 或 Apple Development 身份。若要为作为 Enterprise Program 成员分发而签名框架，请使用 iOS Distribution 或 iOS App Development 身份。你不需要在 `-s` 选项后面提供代码签名身份的全名。使用一个能在你用来签名 XCFramework 的钥匙串中唯一标识该代码签名身份的字符串。有关 `codesign` 工具的更多信息，请参阅 `codesign` 的 UNIX 手册页面。

> [!important] 重要
> 如果你吊销了用于签名分发框架的代码签名身份的证书，请使用另一个未被吊销的代码签名身份对框架进行签名，并将该版本分发给使用你框架的开发者。当 Xcode 构建系统遇到包含已吊销证书的代码签名的框架时，将失败并报错。

### 避免使用替代构建系统时出现问题

当使用替代构建系统时（这在开源项目中很常见），请遵循类似的过程将源代码编译为静态库文件，每个平台（即 *destination*）使用一个二进制文件。使用这些文件创建 XCFramework。

- 对于每个库和每个平台，构建一个二进制静态库文件（`.a` 文件），该文件包含该平台可能使用的所有架构切片。
- 在对 `xcodebuild -create-xcframework` 的调用中指定你创建的每个二进制文件的路径，以生成 XCFramework。

避免将静态库包装在 `.framework` 捆绑包中并省略 `.a` 扩展名。使用 `-library` 标志创建包含静态库的 XCFramework；请参阅上面[生成 XCFramework 捆绑包](creating-a-multi-platform-binary-framework-bundle.md#Generate-the-XCFramework-bundle)下的示例。

避免使用诸如 `lipo` 之类的工具将构建于 iOS 和 iOS Simulator 的架构切片合并到一个二进制文件中。iOS 和 iOS Simulator 的静态库文件必须保持分离。对于一个支持 iOS 和 iOS Simulator 的 XCFramework，你至少需要提供两个二进制静态库文件。iOS 设备使用的二进制文件是为 ARM64 构建的。模拟器的通用二进制文件包含用于 Apple 芯片的 x86_64 和 ARM64 切片。

避免使用动态库文件（`.dylib` 文件）进行动态链接。XCFramework 可以包含动态库文件，但只有 macOS 支持这些库进行动态链接。iOS、iPadOS、tvOS、visionOS 和 watchOS 上的动态链接要求 XCFramework 包含 `.framework` 捆绑包。

如果你对如何编译库以满足这些目标有进一步疑问，请咨询库供应商的支持团队。

### 确定二进制文件支持的架构

链接到你的 XCFramework 的项目需要它包含覆盖每个平台所构建架构的通用二进制文件。

若要确定现有二进制文件包含的架构，请在“终端”中执行 `file` 并提供二进制文件的路径。

```
file <PathToFramework>/<FrameworkName>.framework/<FrameworkName>
```

```
file <PathToLibrary>/libMyLibrary.a
```

## 另请参阅

### 框架

- [创建静态框架](creating-a-static-framework.md) — 配置你的项目以构建一个新的静态框架。
- [识别并解决框架模块问题](identifying-and-addressing-framework-module-issues.md) — 使用模块验证器检测并修复框架模块中的常见问题。
