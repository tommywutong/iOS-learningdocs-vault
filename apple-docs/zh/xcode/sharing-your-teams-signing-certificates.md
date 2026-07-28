---
title: 将代码签名身份与开发者账户同步
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/sharing-your-teams-signing-certificates
source_url: 'https://developer.apple.com/documentation/xcode/sharing-your-teams-signing-certificates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/sharing-your-teams-signing-certificates.json'
content_hash: 'sha256:05f9b7e4ae2075c7'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [分发](distribution.md)

# 将代码签名身份与开发者账户同步

<sub>文章</sub>

确保你和其他团队成员可以在 Xcode 中为组织的代码和安装程序软件包签名。

## 概述

为 App 签名可以向用户保证该 App 来自你的组织。对于许多常见工作流程，Xcode 会自动管理证书和代码签名身份。如果你需要自行管理代码签名身份（例如与外部构建系统集成），请使用 Xcode 设置创建代码签名身份和分发签名身份、与其他团队成员共享，并让本地身份与开发者账户保持同步。有关在开发者账户中创建、管理和撤销证书的信息，请参阅[开发者账户帮助](https://developer.apple.com/help/account/)。

## 创建新的代码签名身份

如果你需要为特定用途生成代码签名身份（例如与外部构建系统集成），请按以下步骤使用 Xcode 创建：

1. 打开 Xcode。
2. 选择 Xcode \> Settings。
3. 在工具栏中点按 Accounts。
4. 从账户列表中选择你的 Apple 账户。
5. 从 Apple 账户的团队列表中选择要为其创建代码签名身份的团队。
6. 点按 Manage Certificates。
7. 在签名证书表单左下角点按 Add 按钮（+），然后从弹出式菜单中选择证书类型。
8. 点按 Done。

![Xcode 中证书管理面板的屏幕截图。](../../../attachments/4bdd037af150a4780537dbe3ab1a8b77/certificate-management@2x.png)

## 导出签名身份以与团队成员共享

当其他团队成员需要使用某个身份且无法在 Xcode 中生成时，请导出该身份。例如，如果团队手动管理签名身份，请导出分发签名身份，与负责分发团队 App 的成员共享。Xcode 会在团队成员之间自动创建和共享云端管理的证书，因此无需手动导出这类证书。有关更多信息，请参阅[云端管理的证书](https://developer.apple.com/help/account/create-certificates/cloud-managed-certificates)。

任何获得导出签名身份访问权并知道（或猜出）密码的人，都可以分发经过签名的软件，而该软件在用户和操作系统看来来自你的 Apple Developer 账户。请为导出的签名身份使用强密码，核实与之共享身份的人员身份，并通过不同渠道分别共享导出的身份和密码。例如，与其发送一封附有导出身份且正文包含密码的电子邮件，不如通过电子邮件发送导出的身份，再通过 FaceTime 通话告知团队成员密码。

有关在 Apple Developer Program 中使用和保护代码签名身份的更多信息，请参阅[证书](https://developer.apple.com/support/certificates/)。

要将签名身份导出为受密码保护的 PKCS#12 文件：

1. 打开 Xcode。
2. 选择 Xcode \> Settings。
3. 在工具栏中点按 Accounts。
4. 从账户列表中选择你的 Apple 账户。
5. 从 Apple 账户的团队列表中选择团队。
6. 点按 Manage Certificates。
7. 在签名证书表单中，按住 Control 键点按与你要导出的签名身份相对应的证书，然后从弹出式菜单中选择 Export Certificate。![](../../../attachments/ec116498118c693759b4dbb5d05af8f0/sharing-certificates-1@2x.png)

  <sub>Xcode 中证书管理面板的屏幕截图。一个证书处于选中状态，快捷菜单中选中了“Export Certificate”。</sub>
8. 在出现的表单中，选择用于保存 PKCS#12 文件的位置。![Xcode 中用于导出代码签名身份的保存面板屏幕截图。](../../../attachments/28a238936e1ab3789ded4ce207f4e378/sharing-certificates-2@2x.png)
9. 输入文件名以及用于保护身份私钥的密码。
10. 点按 Save。

## 从其他团队成员处恢复缺失的私钥

如果你有证书但没有相应的私钥，就无法使用该证书进行代码签名或生成其他数字签名。必须拥有完整的数字身份才能为代码和其他数字对象签名。

如果需要从其他团队成员处获取 Xcode 证书管理器中某个证书的私钥，请按住 Control 键点按该证书并选择 Email Creator。此操作会打开一封发给数字身份创建者的新电子邮件。该人员随后可以按照上一节中的步骤，向你发送包含代码签名身份的 PKCS#12 文件。

团队成员向你发送导出的代码签名身份后，将其导入钥匙串：

1. 连按 `.p12` 文件。
2. “钥匙串访问”提示时，输入文件密码。

“钥匙串访问”会将代码签名身份导入你的登录钥匙串。

## 删除已撤销的证书

在证书管理面板中，按住 Control 键点按要删除的证书，然后选择“Delete Certificate”。Xcode 会提示你确认，并从钥匙串中移除证书及相应私钥。

你只能删除由你或团队成员在开发者账户中撤销的证书。有关撤销证书的更多信息，请参阅[撤销证书](https://developer.apple.com/help/account/create-certificates/revoke-a-certificate)。

## 另请参阅

### 代码签名

- [创建用于 macOS 分发的签名代码](creating-distribution-signed-code-for-the-mac.md) — 使用 Xcode 或命令行工具为要分发的 Mac 代码签名。
- [使用最新的代码签名格式](using-the-latest-code-signature-format.md) — 更新旧版 App 代码签名，使 App 能在当前操作系统版本上运行。
- [分发前对 macOS 软件进行公证](../security/notarizing-macos-software-before-distribution.md) — 将 macOS 软件提交给 Apple 进行公证，进一步增强用户信任。
- [使用受限 entitlement 为守护进程签名](signing-a-daemon-with-a-restricted-entitlement.md) — 将守护进程封装在类似 App 的结构中，以使用由预置描述文件授权的 entitlement。
- [TN3125：代码签名内幕：预置描述文件](../technotes/tn3125-inside-code-signing-provisioning-profiles.md) — 了解预置描述文件如何让第三方代码在 Apple 平台上运行。
