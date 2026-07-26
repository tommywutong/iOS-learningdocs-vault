---
title: 打包用于分发的 Mac 软件
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/packaging-mac-software-for-distribution
source_url: 'https://developer.apple.com/documentation/xcode/packaging-mac-software-for-distribution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/packaging-mac-software-for-distribution.json'
content_hash: 'sha256:cc63002f5853f449'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Distribution](distribution.md)

# 打包用于分发的 Mac 软件

<sub>文章</sub>

为分发你的 Mac 软件构建 zip 归档、磁盘映像或安装程序包。

## 概述

Xcode 为许多常见的 Mac 软件分发场景提供了处理方式，例如将你的 App 上传到 Mac App Store。有些你用 Xcode 或第三方开发者工具构建的产品在分发时需要其他步骤。这些产品包括：

- 不是 App 的产品
- 包含多个组件的产品，例如带有关联守护进程的 App
- 你直接分发的产品
- 你用第三方开发者工具构建的产品

如果你无法仅使用 Xcode 构建和分发产品，请选择一种容器格式并为分发打包你的产品。如果你直接分发产品（换句话说，通过 Mac App Store 以外的渠道），你需要为分发对代码签名并创建一个分发容器文件，然后对该容器文件进行公证。你可以考虑将这个过程自动化，以便对你 App 的每个版本重复执行。更多信息请参阅[为 macOS 创建分发签名代码](creating-distribution-signed-code-for-the-mac.md)。

> [!note] 注意
> 如果你使用第三方开发者工具构建你的 App，请查阅该工具的文档，获取针对该工具的具体建议。

## 决定容器格式

首先，决定你的容器格式。Mac 产品支持两种分发渠道：

- 你可以在 Mac App Store 中分发 App。
- 你可以使用 Developer ID 签名在 Mac App Store 之外直接分发 App 和其他产品。

要在 Mac App Store 中分发 App，你需要以安装程序包的形式提交该 App。对于直接分发，你可以选择各种容器格式，最常见的有：

- **Zip 归档（`.zip`）**——你无法对 zip 归档进行签名，因此其中未被你的代码签名覆盖的任何文件或文件夹都可能被攻击者篡改。收到你的 zip 归档的用户会在访达中打开它以解压内容，然后可以选择将其移动到自己偏好的位置。
- **磁盘映像（`.dmg`）**——你可以对磁盘映像进行签名，这样在签名后可以保护其中包含的所有文件和文件夹不被修改。收到你的磁盘映像的用户会在访达中打开它以访问其内容，他们可以选择直接从磁盘映像运行你的 App，或将其移动到自己偏好的位置。如果你的产品是单个文件或软件包，这种体验最为简便。
- **安装程序包（`.pkg`）**——你需要对安装程序包进行签名，这样在签名后可以保护其中包含的所有文件和文件夹不被修改。收到你的安装程序包的用户会在访达中打开它以启动「安装程序」App，该 App 会引导他们完成安装你的产品所需的步骤。如果你的产品包含多个组件、必须被复制到特定位置，或者你需要在安装过程中运行自定代码，安装程序包是最佳选择。

你可以嵌套这些容器。例如，你可能想在磁盘映像上的安装程序包中运送一个 App。要嵌套容器，请从最底层的容器开始逐级构建到最高层容器，并在每一步都遵循该容器的相应说明。

对你的代码签名，并对每个支持签名的嵌套容器签名。例如，如果你在磁盘映像上的安装程序包中运送一个 App，那么先对该 App 签名，创建安装程序包，对该包签名，创建磁盘映像，然后对磁盘映像签名。有关为分发对代码签名的更多信息，请参阅[为 macOS 创建分发签名代码](creating-distribution-signed-code-for-the-mac.md)。

## 构建 zip 归档

如果你选择以 zip 归档的形式分发你的产品，请使用 `ditto` 命令行工具创建该归档：

1. 创建一个目录，用于容纳你想要分发的所有内容。
2. 运行下面所示的 `ditto` 工具：

```
% ditto -c -k --keepParent <PathToDirectory> <PathToZip>
```

在这个示例命令中，`<PathToDirectory>` 是你在第 1 步中创建的目录的路径，`<PathToZip>` 是 `ditto` 应创建 zip 归档的位置。你无法对 zip 归档本身签名，但可以对其内容签名。

## 构建安装程序包

如果你选择以安装程序包的形式分发你的产品，首先要确定你的安装程序签名身份。为你的分发渠道选择正确的身份：

- 如果你要在 Mac App Store 上分发 App，请使用 Mac Installer Distribution 签名身份。它的名称为 `3rd Party Mac Developer Installer: <TeamID>`，其中 `<TeamID>` 标识你的团队。
- 如果你要独立分发产品，请使用 Developer ID Installer 签名身份。它的名称为 `Developer ID Installer: <TeamID>`，其中 `<TeamID>` 标识你的团队。

有关如何设置这些安装程序签名身份的信息，请参阅[开发者账户帮助](https://developer.apple.com/help/account/)。

运行以下命令以确认你的安装程序签名身份存在且正确：

```
% security find-identity -v               
  1) 6210ECCC616B6A72F238DE6FDDFDA1A06DEFF9FB "3rd Party Mac Developer Installer: …"
  2) C32E0E68CE92936D5532E21BAAD8CFF4A6D9BAA1 "Developer ID Installer: …"
     2 valid identities found
```

`-v` 参数仅筛选有效身份。如果你需要的安装程序签名身份未列出，请参阅[开发者账户帮助](https://developer.apple.com/help/account/)。

> [!important] 重要
> 不要使用 `-p codesigning` 选项来筛选代码签名身份。安装程序签名身份与代码签名身份不同，因此 `-p codesigning` 选项会把安装程序签名身份筛除。

如果你的产品仅由一个 App 组成，请使用 `productbuild` 工具为其创建一个简单的安装程序包。以下是 `productbuild` 最简单的用法，足以将你的 App 提交到 Mac App Store：

```
% productbuild --sign <Identity> --component <PathToApp> /Applications <PathToPackage>
```

对这条命令进行以下替换：

- **`<Identity>`**——你的安装程序签名身份。
- **`<PathToApp>`**——你的 App 的路径。
- **`<PathToPackage>`**——`productbuild` 创建安装程序包的路径。

如果你的产品更复杂，你就需要一个更复杂的安装程序包。有关如何使用安装程序包的更多详情，请参阅 `productbuild`、`productsign`、`pkgbuild` 和 `pkgutil` 的说明手册。有关如何阅读说明手册的说明，请参阅[阅读 UNIX 说明手册](../os/reading-unix-manual-pages.md)。

## 构建磁盘映像文件

如果你选择以磁盘映像文件（`.dmg`）的形式分发你的产品，请按照以下步骤操作：

1. 创建一个目录，作为磁盘映像卷根目录的来源。
2. 用你想要分发的项目填充该目录。如果你要创建脚本来自动执行此过程，请使用 `ditto` 而不是 `cp`，因为 `ditto` 会保留符号链接。
3. 使用以下 `hdiutil` 命令创建磁盘映像文件：

```
% hdiutil create -srcFolder <ProductDirectory> -o <DiskImageFile>
```

在这条命令中，`<ProductDirectory>` 是你在第 1 步中创建的目录，`<DiskImageFile>` 是 `hdiutil` 创建磁盘映像文件的路径。

1. 为这个磁盘映像决定一个代码签名标识符。如果你要签名的是打包好的代码，请以你代码的 bundle ID 作为前缀，加上一个唯一字符串来构建代码签名标识符。否则，请按照[为 macOS 创建分发签名代码](creating-distribution-signed-code-for-the-mac.md)中「对每个代码项签名」的步骤来构建前缀。使用一个与你其他产品（包括代码包标识符）都不同的唯一代码签名标识符。
2. 使用以下 `codesign` 命令对磁盘映像签名：

```
% codesign -s <CodeSigningIdentity> --timestamp -i <Identifier> <DiskImageFile>
```

在这条命令中，`<CodeSigningIdentity>` 是你的 Developer ID application 代码签名身份（例如 `Developer ID Application: <TeamID>`），`<Identifier>` 是你在第 4 步中选择的代码签名标识符，`<DiskImageFile>` 是你在第 3 步中创建的磁盘映像的路径。请使用代码签名身份，而不是安装程序签名身份。

有关代码签名身份的更多信息，请参阅[为 macOS 创建分发签名代码](creating-distribution-signed-code-for-the-mac.md)中的「确认你的代码签名身份」。

你可以使用第三方工具来配置用于分发的磁盘映像。例如，该工具可能会排布图标、设置背景图像，并添加一个指向「应用程序」文件夹的符号链接。如果你使用第三方工具，请确保生成的磁盘映像：

- 已使用你的 Developer ID Application 代码签名身份签名
- 是 UDIF 格式的只读 zip 压缩磁盘映像（类型为 `UDZO`）

## 将你的 App 提交到 Mac App Store

如果你正在为 Mac App Store 创建一个 App，请使用 `altool` 命令行工具或 Transporter App 提交你签名后的安装程序包。有关详细说明，请参阅 [App Store Connect 帮助 \> 参考 \> 上传工具](https://help.apple.com/app-store-connect/#/devb1c185036)。

## 对你的产品进行公证

如果你直接分发产品，请对你打算分发给用户的文件进行公证。更多信息请参阅[自定公证工作流程](../security/customizing-the-notarization-workflow.md)。跳过「导出用于公证的软件包」部分，因为你已经拥有想要提交的文件。

如果你使用嵌套容器分发产品，只需公证最外层的容器。例如，如果你有一个磁盘映像，其中包含一个安装程序包，安装程序包中又包含一个 App，那么请对 App 签名，对安装程序包签名，对磁盘映像签名，但只对磁盘映像进行公证。

如果你使用第三方安装程序工具，请参阅[自定公证工作流程](../security/customizing-the-notarization-workflow.md)。

## 为你的产品盖章

一旦你的产品完成公证，就把生成的票据盖章到你打算分发的文件上。有关如何为 zip 归档中的 App 执行此操作的信息，请参阅[自定公证工作流程](../security/customizing-the-notarization-workflow.md)中的「将票据盖章到你的分发文件上」。其他常见的容器格式，安装程序包和磁盘映像，都支持直接盖章。例如，要将票据盖章到磁盘映像上：

```
% xcrun stapler staple FlyingAnimals.dmg
```

如果你没有将票据盖章到分发文件上，当用户的 Mac 处于离线状态时，Gatekeeper 可能会阻止用户安装或使用你的产品。

## 测试你分发的产品

对于你直接分发的产品，请测试当你从创建的安装程序包、磁盘映像或 zip 文件使用该产品时，它能否正常工作。如果可能，请在与你开发软件所用的 Mac 不同的另一台 Mac 上进行测试，这样开发数据就不会影响测试结果。请考虑以下场景：

- 全新分发，在一台从未使用过你的产品的 Mac 上进行
- 升级分发，在一台已经使用过你产品旧版本的 Mac 上进行（同时考虑新版本替换旧版本，以及新版本安装在与旧版本不同位置这两种情况）
- 重复分发，在一台已经在不同位置包含相同版本产品的 Mac 上进行
- 使用你 App 的人在该 Mac 上登录的账户，与安装该 App 的人不同的分发情况

对于你以 zip 文件或磁盘映像文件形式分发的产品，请考虑以下附加场景：

- 用户在不将其移动到其他位置的情况下打开你的 App。在这种情况下，当用户首次打开你的 App 时，Gatekeeper 会随机化它从 [bundleURL](../foundation/bundle/bundleurl.md) 及其他 API 返回的路径。这项措施可以防止你的 App 使用相对路径访问其软件包之外（因此未被其代码签名封装）的资源，因为攻击者可能会控制这些资源来改变你 App 的行为。Gatekeeper 只在首次启动时执行这种 _转位_，因此也要在后续启动时测试这一行为。
- 用户将你的 App 移动到其他位置，然后启动它。在这种情况下，Gatekeeper 不会转位你 App 的路径。

## 另请参阅

### 分发与发布

- [为你的 App 分发测试版和发布版本](distributing-your-app-for-beta-testing-and-releases.md) — 将你的 App 发布给测试人员和用户。
- [向注册设备分发你的 App](distributing-your-app-to-registered-devices.md) — 在你的开发者账户中注册设备，并将你的 App 部署到这些设备上进行测试。
</content>
