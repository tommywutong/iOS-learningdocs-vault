---
title: 使用受限 entitlement 为守护进程签名
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/signing-a-daemon-with-a-restricted-entitlement
source_url: 'https://developer.apple.com/documentation/xcode/signing-a-daemon-with-a-restricted-entitlement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/signing-a-daemon-with-a-restricted-entitlement.json'
content_hash: 'sha256:52124e1779abe989'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Distribution](distribution.md)

# 使用受限 entitlement 为守护进程签名

<sub>文章</sub>

把守护进程包装成类似 App 的结构，以便使用需要由描述文件（provisioning profile）授权的 entitlement。

## 概述

有些 API 可以从守护进程中使用，但要求该守护进程声明一个需要由描述文件授权的受限 entitlement。例如，[Endpoint Security](../endpointsecurity.md) API 可以从守护进程中使用，但要求该守护进程拥有 [`com.apple.developer.endpoint-security.client`](../bundleresources/entitlements/com.apple.developer.endpoint-security.client.md) entitlement，并且该 entitlement 需要由描述文件授权。这就带来了问题，因为守护进程是一个独立的可执行文件，你无法在其中嵌入描述文件。要绕开这个限制，可以把你的守护进程包装成类似 App 的结构。

> [!important] 重要
> 如果你所使用的 API 支持系统扩展，那就把守护进程改成系统扩展，从而避开这个问题。系统扩展天然支持描述文件，在这种情况下 Xcode 会自动创建描述文件并将其嵌入。

### 创建一个最小化的守护进程项目

基本思路是创建一个 App target（而不是命令行工具 target），然后移除所有 App 专属的内容，替换成你的守护进程代码。首先，通过依次选择 File \> New \> Project，再选择 macOS \> App 模板，创建一个带有 App target 的新项目。将 Interface 弹出菜单设为 Storyboard，将 Life Cycle 弹出菜单（如果存在）设为 AppKit App Delegate，将 Language 弹出菜单设为 Swift。

> [!note] 注意
> 本示例使用 Swift，但如果你选择 Objective-C，这套方法同样适用。

在目标编辑器的 General 标签页中，确认 Bundle Identifier 字段的值正确无误。这一点很重要，因为你的描述文件与你的 App ID 相绑定，而 bundle identifier 正是该 App ID 的关键组成部分。

另外，清空 Deployment Info \> Main Interface 字段，并把 App Icons \> Source 弹出菜单设为 "Don't use asset catalogs"。

切换到 Signing & Capabilities 标签页，按下面的方式进行配置：

- 确保 "Automatically manage signing" 处于选中状态。
- 在 Team 弹出菜单中选择你的团队。
- 移除 App Sandbox 功能（如果存在）。顾名思义，App 沙盒化并不适用于守护进程。
- 添加 Hardened Runtime 功能，公证你的守护进程时会用到它。
- 添加 Custom Network Protocol 功能，它会启用 `com.apple.developer.networking.custom-protocol` entitlement，而该 entitlement 必须由描述文件授权。把它添加到你的 target 后，会触发 Xcode 的自动代码签名机制去注册你的 App ID、为该 App ID 创建描述文件，并将该描述文件嵌入构建产物中。

> [!important] 重要
> 如果你的最终目标是使用 [`com.apple.developer.endpoint-security.client`](../bundleresources/entitlements/com.apple.developer.endpoint-security.client.md) entitlement，请先添加 Custom Network Protocol 功能，以强制 Xcode 注册你的 App ID 并生成一份初始描述文件。然后按照[使用受管功能进行描述](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities)中的说明，把 Endpoint Security 附加功能添加到你的 App ID 中。最后，假设你的守护进程出于其他原因并不需要 Custom Network Protocol 功能，就把它移除。

切换到 Build Settings 标签页，移除 Enable App Sandbox（`ENABLE_APP_SANDBOX`）构建设置（如果存在）。

切换到 Info 标签页，删除所有 App 专属项目（[`NSPrincipalClass`](../bundleresources/information-property-list/nsprincipalclass.md)、[`NSMainStoryboardFile`](../bundleresources/information-property-list/nsmainstoryboardfile.md)、[`NSSupportsSuddenTermination`](../bundleresources/information-property-list/nssupportssuddentermination.md)、`NSSupportsAutomaticTermination` 和 [`CFBundleIconFile`](../bundleresources/information-property-list/cfbundleiconfile.md)）。根据你所使用的具体 Xcode 版本，其中一些项目可能并不存在。

在 Project navigator 中，移除 `AppDelegate.swift`、`ViewController.swift`、`Assets.xcassets` 和 `Main.storyboard` 文件。

添加一个 `main.swift` 文件，并在其中填入你的守护进程代码。对于最小化的守护进程，可以使用下面的代码：

```swift
import Foundation

/// A helper for calling the Security framework from Swift.

func secCall<Result>(_ body: (_ resultPtr: UnsafeMutablePointer<Result?>) -> OSStatus  ) throws -> Result {
    var result: Result? = nil
    let err = body(&result)
    guard err == errSecSuccess else {
        throw NSError(domain: NSOSStatusErrorDomain, code: Int(err), userInfo: nil)
    }
    return result!
}

func main() throws {
    let me = try secCall { SecCodeCopySelf([], $0) }
    let meStatic = try secCall { SecCodeCopyStaticCode(me, [], $0) }
    let infoCF = try secCall { SecCodeCopySigningInformation(meStatic, [], $0) }
    let info = infoCF as NSDictionary
    let entitlements = info[kSecCodeInfoEntitlementsDict] as? NSDictionary
    NSLog("entitlements: %@", entitlements ?? [:])
}

try! main()
```

这段代码会记录当前进程的 entitlements，这是确认你的设置是否正确的一个好方法。

在 Xcode 中构建并运行该守护进程。该程序会记录其 entitlements：

```
2021-08-04 16:24:10.979941+0100 DaemonInAppsClothing[50219:4886989] entitlements: {
    "com.apple.application-identifier" = "SKMME9E2Y8.com.example.apple-samplecode.DaemonInAppsClothing";
    "com.apple.developer.networking.custom-protocol" = 1;
    "com.apple.developer.team-identifier" = SKMME9E2Y8;
    "com.apple.security.get-task-allow" = 1;
}
```

你的守护进程的最终结构应该是这样：

```
DaemonInAppsClothing.app/
  Contents/
    Info.plist
    MacOS/
      DaemonInAppsClothing
    PkgInfo
    _CodeSignature/
      CodeResources
    embedded.provisionprofile
```

注意其中存在着一个嵌入式描述文件；正是这份描述文件授权你的守护进程使用 `com.apple.developer.networking.custom-protocol` entitlement。

### 测试你的守护进程

要正确测试你的守护进程，需要在守护进程的上下文中运行它。首先，把构建好的守护进程复制到一个安全的位置：

```
% sudo mkdir "/Library/Application Support/DaemonInAppsClothing"
% sudo cp -R "DaemonInAppsClothing.app" "/Library/Application Support/DaemonInAppsClothing/"
```

现在创建一个指向该守护进程主可执行文件的 `launchd` 属性列表文件：

```
% /usr/libexec/PlistBuddy -c "Add :Label string com.example.apple-samplecode.DaemonInAppsClothing" "com.example.apple-samplecode.DaemonInAppsClothing.plist"
File Doesn't Exist, Will Create: com.example.apple-samplecode.DaemonInAppsClothing.plist
% /usr/libexec/PlistBuddy -c 'Add :Program string "/Library/Application Support/DaemonInAppsClothing/DaemonInAppsClothing.app/Contents/MacOS/DaemonInAppsClothing"' "com.example.apple-samplecode.DaemonInAppsClothing.plist"
% cat com.example.apple-samplecode.DaemonInAppsClothing.plist 
…
<dict>
    <key>Label</key>
    <string>com.example.apple-samplecode.DaemonInAppsClothing</string>
    <key>Program</key>
    <string>/Library/Application Support/DaemonInAppsClothing/DaemonInAppsClothing.app/Contents/MacOS/DaemonInAppsClothing</string>
</dict>
</plist>
```

把它复制到 `/Library/LaunchDaemons`，然后加载并启动你的守护进程：

```
% sudo cp com.example.apple-samplecode.DaemonInAppsClothing.plist /Library/LaunchDaemons 
% sudo launchctl load /Library/LaunchDaemons/com.example.apple-samplecode.DaemonInAppsClothing.plist 
% sudo launchctl start com.example.apple-samplecode.DaemonInAppsClothing                      
```

运行 Console App，查看系统日志。在你启动该守护进程的那一刻，你会看到这样一条日志：

```
entitlements: {
    "com.apple.application-identifier" = "SKMME9E2Y8.com.example.apple-samplecode.DaemonInAppsClothing";
    "com.apple.developer.networking.custom-protocol" = 1;
    "com.apple.developer.team-identifier" = SKMME9E2Y8;
    "com.apple.security.get-task-allow" = 1;
}
```

如果错过了它，再次运行 `launchctl start` 命令来重新启动你的守护进程。

### 集成你的守护进程代码

现在你已经有了一个可正常工作的最小化守护进程，接下来该把你真正的守护进程代码集成到项目中了。像对待其他任何 Xcode 项目那样，把你的代码添加到项目中。如有需要，用 C、C++、Objective-C 或 Objective-C++ 的主入口点替换 `main.swift`。

或者，如果你使用的是替代构建系统（例如 makefile），请更新它，使其创建出与 Xcode 所创建结构相匹配的结构。

## 另请参阅

### Code signing

- [Creating distribution-signed code for macOS](creating-distribution-signed-code-for-the-mac.md) — 使用 Xcode 或命令行工具为 Mac 代码签署分发签名。
- [Using the latest code signature format](using-the-latest-code-signature-format.md) — 更新旧版 App 代码签名，让你的 App 能在当前的操作系统版本上运行。
- [Notarizing macOS software before distribution](../security/notarizing-macos-software-before-distribution.md) — 把你的 macOS 软件提交给 Apple 进行公证，让用户对它更加放心。
- [Synchronizing code signing identities with your developer account](sharing-your-teams-signing-certificates.md) — 确保你和其他团队成员都能在 Xcode 中签署你所在组织的代码和安装程序包。
- [TN3125: Inside Code Signing: Provisioning Profiles](../technotes/tn3125-inside-code-signing-provisioning-profiles.md) — 了解描述文件如何让第三方代码能够在 Apple 平台上运行。
