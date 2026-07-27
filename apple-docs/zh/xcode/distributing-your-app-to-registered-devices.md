---
title: 将你的 App 分发到已注册的设备
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/distributing-your-app-to-registered-devices
source_url: 'https://developer.apple.com/documentation/xcode/distributing-your-app-to-registered-devices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/distributing-your-app-to-registered-devices.json'
content_hash: 'sha256:eafa72f57e98f1f5'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Distribution](distribution.md)

# 将你的 App 分发到已注册的设备

<sub>文章</sub>

在你的开发者账户中注册设备，并将你的 App 部署到这些设备上进行测试。

## 概述

在[为 beta 测试和发布分发你的 App](distributing-your-app-for-beta-testing-and-releases.md)之前，你可以将进度构建版本分发给已知设备上的有限一组用户，而无需经过 beta App 审核。要向这组用户分发，请在你的[开发者账户](https://developer.apple.com/programs/)中注册他们的设备。你可以注册有限数量的设备，每个产品系列每年一定数量，供你的团队用于开发和测试。

### 为你的构建版本做准备

要准备分发你的构建版本，你需要：

- 一个你在[开发者账户](https://developer.apple.com/programs/)中为你的 App 设置的 App ID。
- 一个带有公钥和私钥的签名证书。在 iOS、iPadOS、tvOS、visionOS 和 watchOS 上，你需要一个分发证书；在 macOS 上，你需要一个开发证书。有关签名证书的更多信息，请参阅 [Certificates](https://developer.apple.com/support/certificates/)。
- 在你的开发者账户中注册的测试设备列表。
- 你的 App 和测试设备列表对应的描述文件。在 iOS、iPadOS、tvOS、visionOS 和 watchOS 上，你需要一个分发描述文件；在 macOS 上，你需要一个开发描述文件。

如果你选择默认的自动签名，Xcode 会为你创建包含你所有已注册设备的描述文件；对于像大团队限制签名资源访问权限，或只想包含你已注册设备的一个子集这样更高级的情况，请手动准备你的描述文件资源。无论是自动还是手动配置描述文件，你都需要收集并将你的测试设备列表添加到你的开发者账户中。当你手动配置一个描述文件时，请在添加测试设备后更新你的描述文件。

每台 iOS、iPadOS、macOS、tvOS、visionOS 和 watchOS 设备都有一个持久的、唯一的标识符，称为设备 ID。当你使用自动签名时，Xcode 会为你注册设备。否则，你需要收集设备 ID 并在你的开发者账户中注册该设备。

### 在 Xcode 中自动注册设备

当你使用自动签名时，Xcode 会为你注册已连接的设备或 Mac。对于 iOS、iPadOS 或 tvOS，将你的设备连接到你的计算机，如果设备询问是否信任你的计算机，请选择信任。对于 watchOS，将与你的 watchOS 设备配对的手机连接到你的计算机。

在 Xcode 中，选择你已连接的设备作为运行目标，然后构建并运行你的 App。有关模拟 App 的更多信息，请参阅[在模拟设备或实体设备上运行你的 App](running-your-app-on-simulated-or-physical-devices.md)。如果你的设备需要注册，请点按 Xcode 显示的对话框中的 Register 按钮，Xcode 会注册该设备并将其添加到你的描述文件中。

### 收集设备标识符：iOS、iPadOS、tvOS、visionOS、watchOS

当你使用手动签名时，首先使用访达或 Xcode 收集你的 iOS、iPadOS、tvOS、visionOS 或 watchOS 设备的设备标识符。

用数据线将你的设备连接到你的 Mac，如果你的设备询问是否信任你的计算机，请选择信任。对于 watchOS，将与你的手表配对的手机连接到你的 Mac，并使用 Xcode 查找该标识符。

使用访达：

1. 在侧栏的 Locations 部分下找到你的设备。有关如果 Locations 部分不可见该怎么办的更多信息，请参阅 [Customize the Finder toolbar and sidebar on Mac](https://support.apple.com/guide/mac-help/customize-finder-toolbar-sidebar-mac-mchlp3011/mac)。
2. 选择你的设备，然后点按信息面板中设备名称下方的标签一次，以查看该设备的序列号、UDID 和型号。多次点按会依次显示其他设备信息，例如型号和存储空间，以及 IMEI 和 MEID。
3. 按住 Control 键点按该标签以复制设备 ID，界面中将其标记为 UDID。

使用 Xcode：

1. 选择 Windows ＞ Devices and Simulators，然后选择 Devices 标签页。
2. 在 Connected 列表下选择你的设备。
3. 高亮显示界面中标记为 Identifier 的设备 ID 以将其复制。

### 收集设备标识符：macOS

要查找你的 Mac 的设备 ID：

1. 选择 Apple 菜单 ＞ 关于本机。
2. 点按 System Report。
3. 选择 Hardware 以查看 Hardware Overview；界面会将设备 ID 显示为 Hardware UUID（在 macOS 10.15 及更早版本中）或 Provisioning UDID（在 macOS 11.0 及更高版本中）。
4. 高亮显示 Hardware UUID 或 Provisioning UDID 以将其复制。

### 在你的开发者账户中注册设备

在你收集了设备 ID 之后，你可以通过将设备名称和标识符放入一个文件来一次性注册它们全部。登录你的开发者账户，然后：

1. 选择 Certificates, Identifiers, and Profiles。
2. 选择 Devices。
3. 点按 Download Sample File 获取示例文件。
4. 用你具体的设备信息自定该示例文件。
5. 上传该设备文件。

有关多设备注册的更多信息，请参阅 [Register multiple devices](https://developer.apple.com/help/account/register-devices/register-multiple-devices)。

通过点按 Devices 标题旁的加号（+）按钮添加单个设备。指定该设备的标识符和名称。使用一个便于识别该设备的名称，例如将机主姓名和设备类型组合起来，如“Ravi Patel's iPhone 11”。

你可以禁用不再允许其使用你的 App 的设备：选择该设备并点按 Disable。代码签名在设备被禁用期间不会包含该设备，但在你的账户续订日期之前，该设备仍计入该产品系列的设备数量。禁用一台设备会使包含该设备的所有描述文件失效；自动签名会在你下次构建 App 时重新生成描述文件，如果你没有使用自动签名，也可以手动重新生成该描述文件。

### 更新你的描述文件

当你使用自动签名时，Xcode 会在你导出该 App 时自动更新描述文件。

要使用手动签名，请登录你的开发者账户，选择 Certificates, Identifiers, and Profiles，然后选择 Profiles。点按 Profiles 标题旁的加号以创建一个新的描述文件。然后：

1. 按类型和平台选择描述文件的类型。
2. 选择你的 App ID。
3. 选择签名证书。
4. 选择要包含在该描述文件中的一个或多个设备。
5. 为该描述文件提供一个名称。
6. 选择 Generate。

你可以编辑一个现有的描述文件并重新生成它以添加或移除设备。生成描述文件之后，下载它，然后将下载的描述文件拖到 Xcode 的程序坞图标上并放开以安装它。你也可以通过 Xcode ＞ Settings ＞ Accounts，在选择你的账户后使用 Download Manual Profiles 按钮来下载它。

### 配置代码签名

要让 Xcode 为你管理签名，请在项目编辑器的 Signing & Capabilities 标签页中切换 Automatically manage signing 复选框，并选择一个 Team。要手动为你的 App 签名，请从 Provisioning Profile 下拉菜单中选择要使用的描述文件。你也可以选择 Import profile 或 Download profile，以从你的账户添加额外的描述文件。

### 归档该 App

在你的 Xcode 项目的主窗口中，从 Scheme 工具栏菜单中选择一个目标和一个运行目标。如果你为运行目标选择了一个模拟器，Xcode 会构建一个与该模拟器对应的仅供构建的设备类型相匹配的归档。选择 Product ＞ Archive 来构建该目标，Xcode 会在 Archives 管理器中显示该归档。

> [!note] 注意
> 对于使用 Mac Catalyst 构建的 App，请为 iPad 版本和 Mac Catalyst 版本创建各自独立的归档。在为 Mac Catalyst 版本创建归档时，选择名称中包含 Mac Catalyst 的运行目标。对于使用 Designed for iPad 构建的 App，使用 iPad 作为运行目标，或使用任何名称中包含 Designed for iPad 的运行目标创建单个归档。这些运行目标会生成相同的归档。

### 导出该 App

从该归档中，导出一个用于分发给用户的 App 版本：

1. 在 Archives 管理器中，选择该归档，然后点按 Distribute App。
2. 选择 Debugging，为在你团队的设备上调试准备一个 App 版本。
3. 点按 Export 并选择一个位置来保存导出的 App。

有关解决代码签名问题的更多信息，请参阅 [Code Signing Resources](https://developer.apple.com/forums/thread/707080)。

### 在用户设备上安装该 App

当你保存导出的 App 时，Xcode 会创建一个包含若干文件的文件夹，其中包括 iOS App 文件，这是一个扩展名为 `.ipa` 的文件。将该文件分发给你的用户，以便他们可以使用 Xcode 或 Apple Configurator 2 将其安装到他们的设备上。

对于 macOS，双击该文件即可安装并运行它。

要使用 Xcode 安装 iOS、iPadOS、tvOS、visionOS 或 watchOS App：

1. 将设备连接到计算机，或者对于 watchOS 设备连接与之配对的手机。
2. 选择 Window ＞ Devices and Simulators，然后选择 Devices 标签页。
3. 选择已连接的设备。
4. 点按 Installed Apps 部分下方的添加按钮（+）。
5. 选择 iOS App 文件以安装该 App。

要使用 Apple Configurator 2 安装 iOS、iPadOS、tvOS、visionOS 或 watchOS App：

1. 将设备连接到你的 Mac，或者对于 watchOS 设备连接与之配对的手机。
2. 选择已连接的设备。
3. 点按 Add 按钮。
4. 选择 iOS App 文件以安装该 App。

> [!important] 重要
> 每次你在 iOS 或 watchOS 设备上运行基于 `.ipa` 的 App 时，你都需要在该设备上启用开发者模式。有关更多信息，请参阅[在设备上启用开发者模式](enabling-developer-mode-on-a-device.md)。

## 另请参阅

### 分发与发布

- [Distributing your app for beta testing and releases](distributing-your-app-for-beta-testing-and-releases.md) — 将你的 App 发布给 beta 测试者和用户。
- [Packaging Mac software for distribution](packaging-mac-software-for-distribution.md) — 构建一个 zip 归档、磁盘映像或安装程序包，以分发你的 Mac 软件。
