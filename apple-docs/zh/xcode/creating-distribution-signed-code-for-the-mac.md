---
title: 为 macOS 创建分发签名的代码
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-distribution-signed-code-for-the-mac
source_url: 'https://developer.apple.com/documentation/xcode/creating-distribution-signed-code-for-the-mac'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-distribution-signed-code-for-the-mac.json'
content_hash: 'sha256:da7a3289f2a19d80'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [分发](distribution.md)

# 为 macOS 创建分发签名的代码

<sub>文章</sub>

使用 Xcode 或命令行工具为要分发的 Mac 代码签名。

## 概述

在发布 Mac 软件产品之前，你需要先创建分发签名的代码——也就是你打包并提交到 Mac App Store 或公证服务的代码。具体做法取决于你的产品类型和构建方式：

- 如果你的产品是一个 Mac App bundle（可能包含 App 扩展等嵌套代码），并且你使用 Xcode 构建它，请用 Xcode 导出一个分发签名的 App。
- 如果你的产品不是 App，但你用 Xcode 构建它，请创建一个 Xcode 归档，然后手动从该归档导出分发签名的代码。
- 如果你使用外部构建系统（如 `make`）构建产品，请在构建系统中加入一个手动签名步骤。

拿到分发签名的代码后，将其打包以便分发。更多信息参见[打包用于分发的 Mac 软件](packaging-mac-software-for-distribution.md)。

> [!note] 注意
> 如果你使用第三方开发者工具构建 App，请查阅其文档以获得针对该工具的建议。

## 从 Xcode 导出 App

如果你的产品是用 Xcode 构建的独立 App，按以下步骤导出一个分发签名的 App：

1. 从你的项目构建一个 Xcode 归档。
2. 从该 Xcode 归档导出一个分发签名的 App。

每一步都可以在 Xcode App 中手动完成，也可以用 `xcodebuild` 自动化完成。

使用 Xcode App 创建分发签名的 App：

1. 选择你的 App 的 scheme。
2. 选取 Product \> Archive。
3. 在 Archives organizer 中，选择第 2 步创建的归档。
4. 点按 Distribute App。
5. 选择合适的分发方式。例如，要创建直接发送给客户的公证 App，选择 Direct Distribution。
6. 点按 Distribute。

> [!note] 注意
> 如果按钮显示的是 Distribute Content 而不是 Distribute App，说明你的归档在 `Products` 目录里有多个条目。要避免把某个 target 的产品拷进 `Products` 目录，请为该 target 设置 Skip Install（`SKIP_INSTALL`）构建设置。每个有输出嵌入你 App 的 target 都要这么做。更多信息参见 [TN3110: Resolving generic Xcode archive issue](../technotes/tn3110-resolving-generic-xcode-archive-issue.md)。

关于 Xcode 归档和 Archives organizer 的更多信息，参见[为 beta 测试和发布分发你的 App](distributing-your-app-for-beta-testing-and-releases.md)。

从命令行导出分发签名的 App：

1. 带 `archive` 动作运行 `xcodebuild`，构建并归档你的 App。
2. 带 `exportArchive` 动作运行 `xcodebuild`，从第 1 步创建的归档中导出分发签名的 App。

关于 `xcodebuild` 的更多信息，参见其联机手册（manual page）。如何阅读联机手册，参见[阅读 UNIX 联机手册](../os/reading-unix-manual-pages.md)。要了解导出选项属性列表支持的键，带 `-help` 参数运行 `xcodebuild`。

## 导出用 Xcode 构建的非 App 产品

要在 Xcode 中归档非 App 产品，请按上文"从 Xcode 导出 App"中的步骤操作。

从 Xcode 归档导出分发签名的产品：

1. 从归档中拷出相关组件。
2. 手动为这些组件签名。

你要用的命令取决于项目结构。例如，设想你的产品是一个守护进程（daemon），但它还有一个配套的配置 App。配置 App 带有一个 share extension 和一个嵌入式 framework，用于在 App 与扩展之间共享代码。这个产品在 Xcode 中的归档具有如下结构：

```
DaemonWithApp.xcarchive/
  Info.plist
  Products/
    usr/
      local/
        bin/
          Daemon
    Applications/
      ConfigApp.app/
        Contents/
          embedded.provisionprofile
          Frameworks/
            Core.framework/
              …
          PlugIns/
            Share.appex/
              Contents/
                embedded.provisionprofile
                …
          …
  …
```

`Products` 目录包含两项：守护进程本身（`Daemon`）和配置 App（`ConfigApp.app`）。要为这个产品签名，先把这些条目从归档中拷出来。

```
% mkdir "to-be-signed"
% ditto "DaemonWithApp.xcarchive/Products/usr/local/bin/Daemon" "to-be-signed/Daemon"
% ditto "DaemonWithApp.xcarchive/Products/Applications/ConfigApp.app" "to-be-signed/ConfigApp.app" 
```

> [!important] 重要
> 拷贝代码时请使用 `ditto` 而不是 `cp`，因为 `ditto` 会保留符号链接（symlink），而符号链接对 Mac framework 的结构至关重要。关于这一结构的更多信息，参见[将内容放入 bundle](../bundleresources/placing-content-in-a-bundle.md)。处理非标准代码结构时符号链接同样有用。更多细节参见[在包中嵌入非标准代码结构](embedding-nonstandard-code-structures-in-a-bundle.md)。

## 确定要签名的代码

要为产品签名，先确定你需要签名的每一个代码条目。例如，在 `DaemonWithApp` 产品中，有四个代码条目：`ConfigApp.app`、`Core.framework`、`Share.appex` 和 `Daemon`。

对每个代码条目，确定以下两点：

- 它是不是捆绑代码（bundled code）？
- 它是不是主可执行文件？

捆绑代码是 bundle 内的主要代码。例如，你有一个 App，内嵌一个辅助工具（helper tool），那就有两个代码条目：App 和辅助工具。App 属于捆绑代码，辅助工具则不是。

下表列出了 `DaemonWithApp` 产品中的代码条目，以及它们是否为捆绑代码或主可执行文件：

| 代码条目 | 捆绑代码？ | 主可执行文件？ |
|---|---|---|
| ConfigApp.app | 是 | 是 |
| Core.framework | 是 | 否 |
| Share.appex | 是 | 是 |
| Daemon | 否 | 是 |

有些情况下，代码条目是不是主可执行文件并不明显。要确认，运行 `file` 命令。主可执行文件会显示 `Mach-O … executable`，如下例所示：

```
% file "to-be-signed/ConfigApp.app/Contents/Frameworks/Core.framework/Versions/A/Core"
…
… Mach-O 64-bit dynamically linked shared library x86_64
…
% file "to-be-signed/ConfigApp.app/Contents/PlugIns/Share.appex/Contents/MacOS/Share"
…
… Mach-O 64-bit executable x86_64
…
```

`Core.framework` 不是主可执行文件，而 `Share.appex` 是。

## 确定签名顺序

签名要从内到外。也就是说，如果组件 `A` 依赖组件 `B`，先签 `B` 再签 `A`。以 `DaemonWithApp` 为例，按以下顺序为组件签名：

1. `Core.framework`
2. `Share.appex `
3. `ConfigApp.app`

App 和守护进程相互独立，所以二者的签名顺序可以随意。

## 配置你的 entitlements

代码签名可以包含 _entitlements_——授予可执行文件使用某项服务或技术的权限的键值对。macOS 运行一个进程时，会授予该进程其可执行文件的代码签名所声明的 entitlements。更多信息参见 [Entitlements](../bundleresources/entitlements.md)。

> [!important] 重要
> 不要给库代码套用 entitlements。它起不到任何有用作用，还可能妨碍你的代码运行。

entitlements 要套用在主可执行文件上。如果你的主可执行文件需要 entitlements，就创建一个 `.entitlements` 属性列表文件，加入该可执行文件所要声明的 entitlements 的键值对。

如果你用 Xcode 构建产品，也许可以直接使用 Xcode 在你的源代码里管理的那个 `.entitlements` 文件；如果没有，就自己创建 `.entitlements` 文件。

> [!important] 重要
> entitlements 文件必须是标准 XML 格式的属性列表，使用 LF 行尾，没有注释，也没有字节顺序标记（BOM）。如果不确定你的文件是否符合这些要求，用 `plutil` 把它转换成标准格式。具体步骤参见[解决常见的公证问题](../security/resolving-common-notarization-issues.md#3561456)。

如果你有程序的开发区签名版本，可以用 `codesign` 命令行工具打印它的 entitlements，并以此作为你的 entitlements 属性列表文件的基础，如下例所示：

```
% codesign -d --entitlements - --xml "to-be-signed/ConfigApp.app" | plutil -convert xml1 -o - -
…
<dict>
  <key>com.apple.application-identifier</key>
  <string>[Your Team ID].com.example.apple-samplecode.DaemonWithApp.App</string>
  <key>com.apple.developer.team-identifier</key>
  <string>[Your Team ID]</string>
  <key>com.apple.security.app-sandbox</key>
  <true/>
  <key>keychain-access-groups</key>
  <array>
    <string>[Your Team ID].com.example.apple-samplecode.DaemonWithApp.SharedKeychain</string>
  </array>
</dict>
</plist>
```

如果你用程序的开发区签名版本里的 entitlements 来创建分发签名代码的 entitlements 属性列表文件，请考虑对 entitlements 做以下改动：

- 把 [APS Environment (macOS) Entitlement](../bundleresources/entitlements/com.apple.developer.aps-environment.md) 的值从 `development` 改为 `production`。
- `com.apple.security.get-task-allow` entitlement 允许调试器附加到你的程序，所以你很少会对分发签名的程序套用它。更多信息参见[解决常见的公证问题](../security/resolving-common-notarization-issues.md#3087731)。

其他 entitlement 请在 [Entitlements](../bundleresources/entitlements.md) 中查阅各自的具体文档。

## 配置你的指定要求

代码签名包含一个指定要求（designated requirement，DR），macOS 用它来识别代码。例如，macOS 用 DR 来跟踪对麦克风这类受隐私保护资源的访问。更多信息参见 [TN3127: Inside Code Signing: Requirements](../technotes/tn3127-inside-code-signing-requirements.md)。

用 `codesign` 工具签名代码时，它会套用一个默认 DR。默认 DR 对大多数产品都适用，但有一个值得注意的例外：Mac App Store App 与 Developer ID 签名 App 的默认 DR 互不兼容。如果你的 App 分发两个变体——一个上架 Mac App Store，一个用 Developer ID 签名直接分发——那么默认情况下，这两个变体无法共享对受隐私保护资源的访问。

要让各变体共享对受隐私保护资源的访问，请用相互兼容的 DR 为变体签名。关于如何 crafting 这些 DR 的建议，参见 [TN3127: Inside Code Signing: Requirements](../technotes/tn3127-inside-code-signing-requirements.md)。

如果你决定使用自定义 DR，把它保存到一个 requirements 文件里。相互兼容的 DR 包含一个代码签名标识符。如果你的产品有多个代码条目，请为每个代码条目复制这个 requirements 文件，并把代码签名标识符更新为与该代码一致。

## 嵌入分发预配描述文件

出于安全考虑，大多数 entitlement 声明都需要预配描述文件（provisioning profile）的授权。例如，`keychain-access-groups` entitlement 就需要预配描述文件的授权。这可以防止其他开发者分发假冒你的 App 的 App 来访问其机密的钥匙串条目。

macOS 允许程序在无此授权的情况下声明某些 entitlement。这些不受限的 entitlement 包括：

- `com.apple.security.get-task-allow`
- `com.apple.security.application-groups`
- 启用并配置 [App Sandbox](../security/app-sandbox.md) 的 entitlement
- 配置 [Hardened Runtime](../security/hardened-runtime.md) 的 entitlement

如果你的程序声明了受限 entitlement，请按如下方式附上一个分发预配描述文件来为该声明授权：

1. 在开发者网站上创建描述文件。更多信息参见 [Developer Account Help](https://developer.apple.com/help/account/)。务必选择与你的分发渠道匹配的描述文件类型（Mac App Store 或 Developer ID）。
2. 把描述文件拷入你程序的 bundle。更多信息参见[将内容放入 bundle](../bundleresources/placing-content-in-a-bundle.md)。

如果你的产品包含一个使用受限 entitlement 的非捆绑可执行文件，请把这个可执行文件包装成类似 App 的结构。更多信息参见[使用受限 entitlement 为守护进程签名](signing-a-daemon-with-a-restricted-entitlement.md)。

在 `DaemonWithApp` 示例中，配置 App 及其 share extension 使用一个钥匙串访问组来共享机密。系统根据程序的 `keychain-access-groups` entitlement 声明授予它对该组的访问，而这种声明需要预配描述文件的授权。App 和 share extension 各有自己的描述文件。要分发这个 App，请用相应的分发预配描述文件更新 App 与 share extension 的 bundle。

```
% cp "ConfigApp-Dist.provisionprofile" "to-be-signed/ConfigApp.app/Contents/embedded.provisionprofile"
% cp "Share-Dist.provisionprofile" "to-be-signed/ConfigApp.app/Contents/PlugIns/Share.appex/Contents/embedded.provisionprofile"
```

以这种方式修改 App 会破坏其代码签名的封印。你在分发前要重新签名。

> [!important] 重要
> 如果你用 Xcode 构建产品，可能会发现 Xcode 在你的 bundle 里嵌入了一个预配描述文件。那是开发用预配描述文件，请替换成分发预配描述文件。

## 确认你的代码签名身份

你从 Xcode 归档中拷出的代码，通常是用开发用代码签名身份签名的。

```
% codesign -d -vv to-be-signed/Daemon
…
Authority=Apple Development: …
…
```

要发布你为开发而签名的产品，需要用合适的代码签名身份为分发重新签名。根据你的分发渠道选择以下身份之一：

- 要把 App 上架 Mac App Store，使用 Apple Distribution 代码签名身份。它的名称是 `Apple Distribution: <Team Name> (<Team ID>)`，其中 `<Team Name>` 和 `<Team ID>` 标识你的团队。
- 要独立分发产品，使用 Developer ID Application 代码签名身份。它的名称是 `Developer ID Application: <Team ID>`，其中 `<Team ID>` 标识你的团队。

关于如何设置这些代码签名身份，参见 [Developer Account Help](https://developer.apple.com/help/account/)。

要确认你的代码签名身份存在且正确，运行以下命令：

```
% security find-identity -p codesigning -v
  1) A06E7F3F8237330EE15CB91BE1A511C00B853358 "Apple Distribution: …"
  2) ADC03B244F4C1018384DCAFFC920F26136F6B59B "Developer ID Application: …"
     2 valid identities found
```

`-p codesigning` 参数筛选代码签名身份；`-v` 参数只筛选有效身份。如果你需要的代码签名身份没有列出，参见 [Developer Account Help](https://developer.apple.com/help/account/)。

每一行输出都包含一个唯一标识该身份的 SHA-1 哈希。如果你有多个同名身份，请用这个哈希而不是身份名称来签名。

## 为每个代码条目签名

对所有代码类型，基本的 `codesign` 命令如下：

```
% codesign -s <CodeSigningIdentity> <PathToExecutable>
```

把 `<CodeSigningIdentity>` 替换为要使用的代码签名身份的名称，把 `<PathToExecutable>` 替换为要签名的代码的路径。

`<CodeSigningIdentity>` 具体用哪个身份取决于你的分发渠道，如上文"确认你的代码签名身份"所述。

> [!note] 注意
> 如果你有多个同名身份，请提供该身份的 SHA-1 哈希来无歧义地指定它。如何获取这个哈希，参见上文"确认你的代码签名身份"。

如果你在重新签名——即要签的代码已有签名——请加上 `-f` 选项。

如果你签的主可执行文件需要 entitlements，加上 `--entitlements <entitlementsPath>` 选项，其中 `<entitlementsPath>` 是你为该可执行文件创建的 entitlements 文件的路径。

如果你是为 Developer ID 分发签名，加上 `--timestamp` 选项以包含安全时间戳。

如果你为 Developer ID 分发签名主可执行文件，加上 `-o runtime` 选项以启用强化运行时（Hardened Runtime）。关于强化运行时的更多信息，参见 [Hardened Runtime](../security/hardened-runtime.md)。

如果你签名的是非捆绑代码，加上 `-i <BundleID>` 选项设置代码签名标识符，其中 `<BundleID>` 是这段代码假如拥有 bundle ID 时会有的那个。例如，一个 App 的 bundle ID 是 `com.example.flying-animals`，内嵌一个名为 `pig-jato` 的命令行工具，你可以把 `com.example.flying-animals.pig-jato` 用作该命令行工具的 bundle ID。

> [!note] 注意
> 对捆绑代码，你无需提供代码签名标识符，因为 `codesign` 默认使用 bundle ID。

如果你使用自定义 DR，加上 `-r <ReqPath>` 选项，其中 `<ReqPath>` 是包含该代码条目 DR 的 requirements 文件的路径。

对产品中的每个代码条目，按你在上文"确定签名顺序"中建立的顺序重复这一签名步骤。如果你的产品复杂、要签名的代码条目很多，就写一个脚本把这一过程自动化。

下面的代码展示了为 Developer ID 分发给 `DaemonWithApp` 示例签名的完整命令序列：

```
% codesign -s "Developer ID Application" -f --timestamp "to-be-signed/ConfigApp.app/Contents/Frameworks/Core.framework"
to-be-signed/ConfigApp.app/Contents/Frameworks/Core.framework: replacing existing signature
% codesign -s "Developer ID Application" -f --timestamp -o runtime --entitlements "Share.entitlements" "to-be-signed/ConfigApp.app/Contents/PlugIns/Share.appex"
to-be-signed/ConfigApp.app/Contents/PlugIns/Share.appex: replacing existing signature
% codesign -s "Developer ID Application" -f --timestamp -o runtime --entitlements "ConfigApp.entitlements" "to-be-signed/ConfigApp.app"
to-be-signed/ConfigApp.app: replacing existing signature
% codesign -s "Developer ID Application" -f --timestamp -o runtime -i "com.example.apple-samplecode.DaemonWithApp.Daemon" "to-be-signed/Daemon"
to-be-signed/Daemon: replacing existing signature
```

> [!important] 重要
> 不要用 `sudo` 运行 `codesign`，因为 `codesign` 签名代码时依赖你的用户账户里的信息。用 `sudo` 之类的工具切换用户账户，会导致 `codesign` 访问这些信息时出问题。

## 避免深度签名

为代码签名时，不要给 `codesign` 传 `--deep` 选项。这个选项在某些特定情况下有用（例如验证代码签名时），但签名复杂产品时它会带来以下问题：

- `--deep` 选项对它签名的每个代码条目套用相同的代码签名选项。例如，你有一个带内嵌命令行工具的 App，App 与工具需要不同的 entitlements，而 `codesign --deep` 会给两者套用相同的 entitlements。
- 使用 `--deep` 选项时，`codesign` 只有在嵌套代码位于顶层 bundle 的特定位置时才会签名它。如果你把代码放在 `codesign` 认为放数据的地方，`codesign --deep` 就不会签它。关于嵌套代码在 bundle 中的正确组织方式，参见[将内容放入 bundle](../bundleresources/placing-content-in-a-bundle.md)。

## 另请参阅

### 代码签名

- [使用最新的代码签名格式](using-the-latest-code-signature-format.md) — 更新旧式 App 代码签名，让你的 App 能在当前系统版本上运行。
- [Notarizing macOS software before distribution](../security/notarizing-macos-software-before-distribution.md) — 把你的 macOS 软件提交给 Apple 公证，让用户更有信心。
- [使用受限 entitlement 为守护进程签名](signing-a-daemon-with-a-restricted-entitlement.md) — 把守护进程包装成类似 App 的结构，以使用需要预配描述文件授权的 entitlement。
- [将代码签名身份与开发者账户同步](sharing-your-teams-signing-certificates.md) — 确保你和其他团队成员能在 Xcode 中为你组织的代码和安装包签名。
- [TN3125: Inside Code Signing: Provisioning Profiles](../technotes/tn3125-inside-code-signing-provisioning-profiles.md) — 了解预配描述文件如何让第三方代码在 Apple 平台上运行。
