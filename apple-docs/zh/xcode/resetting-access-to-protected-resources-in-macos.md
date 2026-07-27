---
title: 在 macOS 中重置对受保护资源的访问权限
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/resetting-access-to-protected-resources-in-macos
source_url: 'https://developer.apple.com/documentation/xcode/resetting-access-to-protected-resources-in-macos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/resetting-access-to-protected-resources-in-macos.json'
content_hash: 'sha256:09c275010c6f290b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Command-line tools](command-line-tools.md)

# 在 macOS 中重置对受保护资源的访问权限

<sub>文章</sub>

在测试期间，使用「终端」移除你 App 对受保护资源的授权访问。

## 概述

当你的 App 首次尝试访问诸如「提醒事项」或麦克风等受保护资源时，系统会提示用户授权。在用户同意或拒绝你 App 的访问请求后，系统会记住他们的选择。更多信息，请参阅[请求访问受保护资源](../uikit/requesting-access-to-protected-resources.md)。

在开发过程中，你可能需要让系统再次提示用户授权——比如测试你 App 的用户引导体验、验证你的用途说明字符串在你所支持的每种语言中是否都能正确显示，或者复现一个只在用户授权之前才会出现的错误。要让系统再次提示用户，请在「终端」中使用 `tccutil reset` 命令。`tccutil reset` 命令需要一个服务，每种受保护资源都有一个服务名称。默认情况下，该命令只影响你当前的用户账户。要重置你 Mac 上所有用户账户的访问权限，请使用 `sudo` 运行该命令。要了解更多关于 `tccutil` 的信息，请在「终端」中输入 `man tccutil`。

## 重置访问权限

要为所有 App 重置对某个特定受保护资源的访问权限，请输入带有服务名称的 `tccutil reset`：

```shell
% tccutil reset <service>
```

例如，以下命令会为所有 App 重置对「日历」的访问权限：

```shell
% tccutil reset Calendar
```

下次任何 App 尝试访问「日历」时，系统都会提示用户授权。

要为单个 App 重置对某个特定受保护资源（此处以「日历」为例）的访问权限，请在命令中加上该 App 的包 ID：

```shell
% tccutil reset Calendar com.example.company
```

要一次性重置对所有资源的访问权限，请将 `All` 作为服务名称传入：

```shell
% tccutil reset All
```

下次任何 App 尝试访问任何受保护资源时，系统都会提示用户授权。

要为单个 App 重置对所有资源的访问权限，请加上该 App 的包 ID：

```shell
% tccutil reset All com.example.company
```

## 查找服务名称

`<service>` 参数接受以下值。在适用的情况下，每个条目都包含需要添加到你 App `Info.plist` 中的隐私用途说明键。

- **`All`** — 重置对下面列出的每一种受保护资源的访问权限。
- **`Accessibility`** — 重置对辅助功能特性的访问权限。
- **`AddressBook`** — 重置对「通讯录」的访问权限。隐私用途说明键：[NSContactsUsageDescription](../bundleresources/information-property-list/nscontactsusagedescription.md)。
- **`AppleEvents`** — 重置发送 Apple 事件的访问权限。隐私用途说明键：[NSAppleEventsUsageDescription](../bundleresources/information-property-list/nsappleeventsusagedescription.md)。
- **`AudioCapture`** — 重置采集系统音频的访问权限。隐私用途说明键：[NSAudioCaptureUsageDescription](../bundleresources/information-property-list/nsaudiocaptureusagedescription.md)。
- **`BluetoothAlways`** — 重置对蓝牙的访问权限。隐私用途说明键：[NSBluetoothAlwaysUsageDescription](../bundleresources/information-property-list/nsbluetoothalwaysusagedescription.md)。
- **`Calendar`** — 重置对「日历」的访问权限。隐私用途说明键：[NSCalendarsWriteOnlyAccessUsageDescription](../bundleresources/information-property-list/nscalendarswriteonlyaccessusagedescription.md) 与 [NSCalendarsFullAccessUsageDescription](../bundleresources/information-property-list/nscalendarsfullaccessusagedescription.md)。
- **`Camera`** — 重置对相机的访问权限。隐私用途说明键：[NSCameraUsageDescription](../bundleresources/information-property-list/nscamerausagedescription.md)。
- **`DeveloperTool`** — 重置对「开发者工具」的访问权限，该权限允许 App 运行未签名或不符合系统安全策略的代码。
- **`EnergyKitGuidance`** — 重置对 EnergyKit 的访问权限，用于能耗使用指导与监测。
- **`ExternalCameraMedia`** — 重置对外接相机设备及其媒体内容的访问权限。
- **`FileProviderDomain`** — 重置对文件提供方所管理文件的访问权限。隐私用途说明键：[NSFileProviderDomainUsageDescription](../bundleresources/information-property-list/nsfileproviderdomainusagedescription.md)。
- **`FileProviderPresence`** — 重置文件提供方判断用户正在访问哪些文件的访问权限。隐私用途说明键：[NSFileProviderPresenceUsageDescription](../bundleresources/information-property-list/nsfileproviderpresenceusagedescription.md)。
- **`FocusStatus`** — 重置对用户专注状态的访问权限。隐私用途说明键：[NSFocusStatusUsageDescription](../bundleresources/information-property-list/nsfocusstatususagedescription.md)。
- **`GameCenterFriends`** — 重置对 Game Center 好友列表的访问权限。隐私用途说明键：[NSGKFriendListUsageDescription](../bundleresources/information-property-list/nsgkfriendlistusagedescription.md)。
- **`HomeKit`** — 重置对 HomeKit 的访问权限。隐私用途说明键：[NSHomeKitUsageDescription](../bundleresources/information-property-list/nshomekitusagedescription.md)。
- **`ListenEvent`** — 重置对「输入监控」的访问权限。
- **`MediaLibrary`** — 重置对 Apple Music 资料库的访问权限。隐私用途说明键：[NSAppleMusicUsageDescription](../bundleresources/information-property-list/nsapplemusicusagedescription.md)。
- **`Microphone`** — 重置对麦克风的访问权限。隐私用途说明键：[NSMicrophoneUsageDescription](../bundleresources/information-property-list/nsmicrophoneusagedescription.md)。
- **`Motion`** — 重置对设备运动数据的访问权限。隐私用途说明键：[NSMotionUsageDescription](../bundleresources/information-property-list/nsmotionusagedescription.md)。
- **`Photos`** — 重置对「照片」的访问权限。隐私用途说明键：[NSPhotoLibraryUsageDescription](../bundleresources/information-property-list/nsphotolibraryusagedescription.md)。
- **`PhotosAdd`** — 重置向「照片」资料库添加照片的访问权限。隐私用途说明键：[NSPhotoLibraryAddUsageDescription](../bundleresources/information-property-list/nsphotolibraryaddusagedescription.md)。
- **`PostEvent`** — 重置发送按键的访问权限。
- **`Reminders`** — 重置对「提醒事项」的访问权限。隐私用途说明键：[NSRemindersFullAccessUsageDescription](../bundleresources/information-property-list/nsremindersfullaccessusagedescription.md)。
- **`RemoteDesktop`** — 重置对「远程桌面」的访问权限。
- **`ScreenCapture`** — 重置对「屏幕录制」的访问权限。
- **`Siri`** — 重置对 Siri 的访问权限。隐私用途说明键：[NSSiriUsageDescription](../bundleresources/information-property-list/nssiriusagedescription.md)。
- **`SpeechRecognition`** — 重置对「语音识别」的访问权限。隐私用途说明键：[NSSpeechRecognitionUsageDescription](../bundleresources/information-property-list/nsspeechrecognitionusagedescription.md)。
- **`SystemPolicyAllFiles`** — 重置对所有文件的访问权限（完全磁盘访问权限）。
- **`SystemPolicyAppBundles`** — 重置对 App 包的访问权限。隐私用途说明键：[NSAppBundlesUsageDescription](../bundleresources/information-property-list/nsappbundlesusagedescription.md)。
- **`SystemPolicyAppData`** — 重置对其他 App 沙盒容器中文件的访问权限。隐私用途说明键：[NSAppDataUsageDescription](../bundleresources/information-property-list/nsappdatausagedescription.md)。
- **`SystemPolicyDesktopFolder`** — 重置对用户「桌面」文件夹中文件的访问权限。隐私用途说明键：[NSDesktopFolderUsageDescription](../bundleresources/information-property-list/nsdesktopfolderusagedescription.md)。
- **`SystemPolicyDocumentsFolder`** — 重置对用户「文稿」文件夹中文件的访问权限。隐私用途说明键：[NSDocumentsFolderUsageDescription](../bundleresources/information-property-list/nsdocumentsfolderusagedescription.md)。
- **`SystemPolicyDownloadsFolder`** — 重置对用户「下载」文件夹中文件的访问权限。隐私用途说明键：[NSDownloadsFolderUsageDescription](../bundleresources/information-property-list/nsdownloadsfolderusagedescription.md)。
- **`SystemPolicyNetworkVolumes`** — 重置对网络宗卷上文件的访问权限。隐私用途说明键：[NSNetworkVolumesUsageDescription](../bundleresources/information-property-list/nsnetworkvolumesusagedescription.md)。
- **`SystemPolicyRemovableVolumes`** — 重置对可移动宗卷上文件的访问权限。隐私用途说明键：[NSRemovableVolumesUsageDescription](../bundleresources/information-property-list/nsremovablevolumesusagedescription.md)。
- **`SystemPolicySysAdminFiles`** — 重置对系统配置文件的访问权限。隐私用途说明键：[NSSystemAdministrationUsageDescription](../bundleresources/information-property-list/nssystemadministrationusagedescription.md)。
- **`UserTracking`** — 重置对用户或设备跟踪数据的访问权限。隐私用途说明键：[NSUserTrackingUsageDescription](../bundleresources/information-property-list/nsusertrackingusagedescription.md)。
- **`VirtualMachineNetworking`** — 重置虚拟机联网的访问权限。
- **`VoiceBanking`** — 重置对「个人声音」和声音储存的访问权限。
- **`WebBrowserPublicKeyCredential`** — 重置对网页浏览器中公钥凭证（通行密钥与 WebAuthn）的访问权限。
