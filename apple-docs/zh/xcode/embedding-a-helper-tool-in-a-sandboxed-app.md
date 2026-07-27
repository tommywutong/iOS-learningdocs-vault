---
title: 在沙盒化 App 中嵌入命令行工具
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/embedding-a-helper-tool-in-a-sandboxed-app
source_url: 'https://developer.apple.com/documentation/xcode/embedding-a-helper-tool-in-a-sandboxed-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/embedding-a-helper-tool-in-a-sandboxed-app.json'
content_hash: 'sha256:0d0fb94ff33d28ea'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [项目与工作区](projects-and-workspaces.md)

# 在沙盒化 App 中嵌入命令行工具

<sub>文章</sub>

将命令行工具添加到沙盒化 App 的 Xcode 项目，使生成的 App 能够将它作为辅助工具运行。

## 概述

构建 Mac App 时，可以在 App 中嵌入命令行工具作为辅助工具。以下是可能适合这样做的一些情况：

- 你想在单独的进程中运行一些代码。许多情况下，XPC 服务是更好的选择，但有时嵌入命令行工具更加简单。
- 你想使用外部构建系统（例如 `make`）构建命令行工具，然后从 App 运行它。

在沙盒化 App 中嵌入命令行工具确实会带来一些独特挑战。最佳方法取决于你是使用 Xcode 构建工具，还是使用外部构建系统构建的工具。

> [!note] 注意
> 这些步骤假设你正在为 App Store 构建 App，因为 App Store 是沙盒化 App 最常见的分发目标。不过，使用 Developer ID 签名独立分发的 App 也可以采用相同的基本过程；只需在 Xcode Organizer 中选择不同的分发路径。

### 创建 App 项目

首先，从 macOS \> App 模板创建新项目。将其命名为 `AppWithTool`，从而生成类似 `com.example.apple-samplecode.AppWithTool` 的捆绑包 ID。

在项目编辑器中，将部署目标设置为 10.15。稍后你将配置工具目标，使其继承此部署目标，这有助于保持所有内容同步。

在 App 目标编辑器的 General 标签页中，将 App Category 设置为 Utilities。这样可以避免为分发进行构建时出现警告。

在 App 目标编辑器的 Signing & Capabilities 标签页中，确保选中“Automatically manage signing”，然后选择适当的团队。Signing Certificate 弹出式菜单应切换到 Development，这正是日常开发所需的设置。

添加 Hardened Runtime 功能。App Store App 并不要求此功能，但这是新代码的最佳实践。

选择 Product \> Archive，这会将 App 构建到 Xcode 归档中，并在 Xcode Organizer 中显示该归档。这里的目的是检查目前为止一切是否正常。

在 Organizer 中删除新归档，只是为了重置到原始状态。

### 创建辅助工具目标

App 目标已能在项目中正确构建，接下来创建辅助工具目标，以便将其产品嵌入 App。首先，从 macOS \> Command Line Tool 模板创建新目标。将其命名为 `ToolX`，其中 _X_ 表示_使用 Xcode 构建_。

在工具目标编辑器的 General 标签页中，清空 Deployment Target 字段。这会将工具目标配置为从项目继承部署目标（macOS 10.15）。

在工具目标编辑器的 Signing & Capabilities 标签页中，确保选中“Automatically manage signing”，然后选择适当的团队。同样，Signing Certificate 弹出式菜单会切换到 Development。

填写 Bundle Identifier 字段。App 的捆绑包 ID 是 `com.example.apple-samplecode.AppWithTool`，因此将其设置为 `com.example.apple-samplecode.AppWithTool.ToolX`。此值会成为辅助工具的代码签名标识符。请参阅下文有关 Other Code Signing Flags 构建设置的讨论。

添加 App Sandbox 和 Hardened Runtime 功能。同样，App Store App 不要求强化运行时，但这是新代码的最佳实践。

在 Build Settings 标签页中，启用 Skip Install（`SKIP_INSTALL`）构建设置。如果不启用此设置，Xcode 会在 Xcode 归档中放置一份独立的工具副本（此外还有嵌入 App 的副本）。尝试分发该归档时，这份工具副本会造成问题。

还要停用 Code Signing Inject Base Entitlements（`CODE_SIGN_INJECT_BASE_ENTITLEMENTS`）构建设置。如果保持启用，Xcode 会在工具的开发构建中包含 `com.apple.security.get-task-allow` entitlement。这样会有问题，因为该 entitlement 与 `com.apple.security.inherit` entitlement 不兼容。

> [!important] 重要
> 缺少 `com.apple.security.get-task-allow` entitlement 意味着你无法调试该工具。如果需要调试，请专门创建一个未沙盒化的新命令行工具目标。不过请注意，由于此目标不在沙盒中运行，其行为可能与正常工具目标不同。

将 Other Code Signing Flags（`OTHER_CODE_SIGN_FLAGS`）构建设置设为 `$(inherited) -i $(PRODUCT_BUNDLE_IDENTIFIER)`，确保工具的代码签名标识符与其捆绑包 ID 匹配。

在 Project navigator 中选择 `ToolX.entitlements`，并向其中添加布尔值为 `true` 的 `com.apple.security.inherit`。有关此 entitlement 的更多信息，请参阅[启用 App Sandbox 继承](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW15)。

选择 ToolX 方案并选择 Product \> Build，以确保工具能够正确构建。

现在切换回 App（`AppWithTool`）方案。

### 嵌入辅助工具

在 App 目标编辑器的 Build Phases 标签页中，将 ToolX 目标添加到 Dependencies 构建阶段。这样可以确保 Xcode 在构建 App 目标之前构建工具目标。

添加一个新的 Copy Files 构建阶段。连按构建阶段名称并将其更改为 `Embed Helper Tools`（确切名称并不重要，但最好选择描述性名称）。将 Destination 弹出式菜单设为 Executables。这会将辅助工具放入 App 的 `Contents/MacOS` 目录中，该目录是[在捆绑包中放置内容](../bundleresources/placing-content-in-a-bundle.md)所建议的位置之一。

将 `ToolX` 可执行文件添加到该构建阶段，并确保选中 Code Sign On Copy。

有关构建阶段的更多信息，请参阅[什么是构建阶段？](https://help.apple.com/xcode/mac/11.4/index.html#/dev50bab713d)

### 构建并验证

项目设置完毕后，应测试所有内容是否能正确构建。首先选择 Product \> Archive，这会先构建工具目标，再构建 App 目标，并将前者的结果嵌入后者。

在 Xcode Organizer 中，选择新创建的归档并点按 Distribute App。

> [!note] 注意
> 如果按钮显示 Distribute Content 而不是 Distribute App，请返回并检查是否已为工具目标启用 Skip Install 构建设置。

选择 App Store Connect 并点按 Next，然后选择 Export 并点按 Next。

完成导出工作流程的其余步骤。最终结果是一个名称类似 `AppWithTool 2021-05-17 14-07-21` 的目录。该目录中包含一个安装器包（扩展名为 `.pkg`）。解包该软件包。

> [!note] 注意
> 解包安装器包最简单的方法是安装它。如果不想安装，可以使用 `xar` 和 `cpio` 手动解包。有关更多信息，请阅读这些工具的手册页（参阅[阅读 UNIX 手册页](../os/reading-unix-manual-pages.md)）。

运行以下命令，确认 Xcode 正确构建了所有内容：

```
% codesign -d -vvv --entitlements :- AppWithTool.app 
…
Identifier=com.example.apple-samplecode.AppWithTool
Format=app bundle with Mach-O universal (x86_64 arm64)
CodeDirectory v=20500 size=822 flags=0x10000(runtime) hashes=14+7 location=embedded
…
Authority=Apple Distribution: …
…
TeamIdentifier=SKMME9E2Y8
…
<dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.files.user-selected.read-only</key>
    <true/>
</dict>
</plist>
% codesign -d -vvv --entitlements :- AppWithTool.app/Contents/MacOS/ToolX 
…
Identifier=com.example.apple-samplecode.AppWithTool.ToolX
Format=Mach-O universal (x86_64 arm64)
CodeDirectory v=20500 size=796 flags=0x10000(runtime) hashes=13+7 location=embedded
…
Authority=Apple Distribution: …
…
TeamIdentifier=SKMME9E2Y8
…
<dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.inherit</key>
    <true/>
</dict>
</plist>
```

检查以下内容：

- `Identifier` 字段是代码签名标识符。
- `Format` 字段显示可执行文件是通用二进制文件。
- `CodeDirectory` 字段中的 `runtime` 标志表明已启用强化运行时。
- `Authority` 字段表明代码由 Apple Distribution 签名身份签名，这正是提交到 App Store 时所预期的结果。
- `TeamIdentifier` 字段是你的 Team ID。
- App 的 entitlement 包含 `com.apple.security.app-sandbox`，以及适用于此 App 的所有其他 entitlement。
- 工具的 entitlement 仅包含 `com.apple.security.app-sandbox` 和 `com.apple.security.inherit`。

> [!important] 重要
> 向工具添加其他 entitlement 可能导致问题。如果 App 运行工具时，该工具立即因代码签名错误而崩溃，请检查工具是否仅使用以下两个 entitlement 签名：`com.apple.security.app-sandbox` 和 `com.apple.security.inherit`。

### 嵌入由外部构建的工具

App 和使用 Xcode 构建的辅助工具均可正常工作后，可以为使用外部构建系统构建的工具重复此过程。以下示例从命令行创建一个示例辅助工具，然后将其嵌入 AppWithTool App。在真实项目中，你会使用命令行工具的外部构建系统（例如 `make`）来构建要嵌入的工具。

### 构建工具

创建新目录并进入该目录：

```
% mkdir ToolC
% cd ToolC
```

这里的 _C_ 表示_使用 Clang 构建_。

在目录中创建如下所示的源文件：

```
% cat main.c 
#include <stdio.h>

int main(int argc, char ** argv) {
    printf("Hello Cruel World!\n");
    return 0;
}
```

使用 `clang` 构建该源文件两次，每种架构各一次，然后使用 `lipo` 将两者合并：

```
% clang -o ToolC-x86_64 -mmacosx-version-min=10.15 -arch x86_64 main.c
% clang -o ToolC-arm64 -mmacosx-version-min=11.0 -arch arm64 main.c
% lipo ToolC-x86_64 ToolC-arm64 -create -output ToolC 
```

`-mmacosx-version-min` 选项将部署目标设置为与 AppWithTool App 匹配。对于 Intel 架构，如上所述，此版本为 macOS 10.15。对于 Apple 芯片架构，此版本为 macOS 11.0，这是首个支持 Apple 芯片的 macOS 版本。

为工具创建 entitlement 文件：

```
% /usr/libexec/PlistBuddy -c "Add :com.apple.security.app-sandbox bool true" "ToolC.entitlements"
File Doesn't Exist, Will Create: ToolC.entitlements
% /usr/libexec/PlistBuddy -c "Add :com.apple.security.inherit bool true" ToolC.entitlements
% cat ToolC.entitlements 
…
<dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.inherit</key>
    <true/>
</dict>
</plist>
```

按如下方式为工具签名：

```
% codesign -s - -i com.example.apple-samplecode.AppWithTool.ToolC -o runtime --entitlements ToolC.entitlements -f ToolC
```

各参数的含义如下：

- `-s -` 参数应用临时签名（在 Xcode 术语中称为 Sign to Run Locally）。在此处设置代码签名至关重要。它建立了 Xcode 在将工具嵌入最终 App 时重新签名所使用的模式。只有签名身份不重要。嵌入过程中，Xcode 会使用产品的签名身份覆盖该身份，因此可以使用临时签名。
- `-i com.example.apple-samplecode.AppWithTool.ToolC` 选项设置代码签名标识符。
- `-o runtime` 选项启用强化运行时。同样，App Store 分发并不要求此功能，但这是新代码的最佳实践。
- `--entitlements ToolC.entitlements` 选项提供签名的 entitlement。
- `-f` 选项覆盖所有现有签名。严格来说并不需要此选项，但它可以避免对 `clang` 为 `arm64` 架构应用的现有临时签名产生混淆。Apple 芯片要求所有代码都经过签名，因此 `clang` 在为 Apple 芯片构建时会自动应用临时签名。

将 `ToolC` 可执行文件添加到 Xcode 项目。执行此操作时：

- 启用“Copy items if needed”。
- 选择“Create groups”，而不是“Create folder reference”。
- 取消选中“Add to targets”列表中的所有复选框。

在 App 目标编辑器的 Build Phases 标签页中，将 `ToolC` 添加到 Embed Helper Tools 构建阶段，并确保选中 Code Sign On Copy。

### 再次构建并验证

若要验证工作，请按照[构建并验证](embedding-a-helper-tool-in-a-sandboxed-app.md#Build-and-validate)中所述过程操作，并将所有 `ToolX` 替换为 `ToolC`。

## 另请参阅

### 项目配置

- [管理 App 的信息属性列表值](../bundleresources/managing-your-app-s-information-property-list.md) — 使用 Xcode 自定 App 的信息属性列表值。
- [向 App 添加软件包依赖项](adding-package-dependencies-to-your-app.md) — 集成软件包依赖项，以在项目之间共享代码或利用其他开发者的代码。
- [创建 iPad App 的 Mac 版本](../uikit/creating-a-mac-version-of-your-ipad-app.md) — 使用 Mac Catalyst 将 iPad App 带到 macOS。
- [设置 watchOS 项目](../watchos-apps/setting-up-a-watchos-project.md) — 创建新的 watchOS 项目，或向现有 iOS 项目添加 watch 目标。
