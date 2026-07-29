---
title: 学习通过启用 usbmuxd 的调试日志了解 iOS 设备如何通过 USB 同步
source: worthdoingbadly (Zhuowei Zhang)
source_key: worthdoingbadly
source_url: 'https://worthdoingbadly.com/usbmuxdebug/'
original_language: en
published: 2018-11-25
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:06a12a65c658ee05'
translated: true
---

> 原文：[Learn how iOS devices sync over USB by enabling usbmuxd’s debug logs](https://worthdoingbadly.com/usbmuxdebug/)　·　worthdoingbadly (Zhuowei Zhang)

# 学习通过启用 usbmuxd 的调试日志了解 iOS 设备如何通过 USB 同步

2018 年 11 月 25 日

为了了解 iTunes 和 Xcode 如何与 iPhone 同步，我启用了 macOS 的 `usbmuxd` 守护进程中的一个隐藏选项，该选项会记录 App 如何通过 USB 与 iOS 设备通信。

# 配置选项的作用

它会让 `usbmuxd` 记录哪些进程正在访问已连接的 iOS 设备。

[`usbmuxd`](https://www.theiphonewiki.com/wiki/Usbmux) 是 macOS 上的系统守护进程，负责处理通过 USB（或 Wi-Fi 同步，如果你已启用）与 iOS 设备的通信。

你可以打开“控制台”App 并过滤“usbmuxd”来查看日志：

![使用连接的 iOS 设备打开 Xcode 时的日志输出](https://worthdoingbadly.com/assets/blog/usbmuxdebug/usbmuxd_log_cropped.png)

在上面的日志中，我打开了 Xcode 的“设备”窗口，这触发了 Xcode 通过端口 62078 连接到我的 iPad 上的 Lockdownd，可能用于启动某种开发者服务。然后 Xcode 通过端口 59426 连接到新启动的服务。

# 如何启用

你需要一个 `/Library/Preferences/com.apple.usbmuxd.plist` 配置文件。

下载[这个 usbmuxd 配置文件](https://worthdoingbadly.com/assets/usbmuxddebug/com.apple.usbmuxd.plist)：

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>DebugLevel</key>
	<integer>7</integer>
</dict>
</plist>
```

并将其复制到你的 `/Library/Preferences/` 目录：

```
sudo cp ~/Downloads/com.apple.usbmuxd.plist /Library/Preferences
```

`usbmuxd` 应该会读取配置文件并向控制台打印一条消息：

```
usbmuxd	notice    log filter changed from 5 to 7
```

# 我是如何发现的

在我将 usbmuxd 加载到 IDA Free 后，我注意到它在调用 [`asl_set_filter`](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/asl_set_filter.3.html) 来过滤调试日志：

![调用 asl_set_filter 的函数](https://worthdoingbadly.com/assets/blog/usbmuxdebug/usbmuxd_set_filter.png)

这个函数被两个函数调用。

![asl_set_filter 的交叉引用](https://worthdoingbadly.com/assets/blog/usbmuxdebug/usbmuxd_xrefs.png)

`_start` 函数处理用于启用详细日志记录的命令行参数。

另一个函数 `sub_10000236E` 处理 `usbmuxd` 的配置文件：

![usbmuxd 的配置文件路径](https://worthdoingbadly.com/assets/blog/usbmuxdebug/usbmuxd_configpath.png)

usbmuxd 支持相当多的配置选项。其中看起来有希望的是 `DebugLevel`：

![usbmuxd 设置的名称](https://worthdoingbadly.com/assets/blog/usbmuxdebug/usbmuxd_settings_names.png)

我创建了 `/Library/Preferences/com.apple.usbmuxd.plist` 文件并提高了调试级别，直到调试消息开始出现。

# 其他资源

以下是我在研究过程中查阅的一些可能对你有用的资料：

- [Libimobiledevice](https://github.com/libimobiledevice/libimobiledevice) - 用于通过 USB 与 iOS 设备通信的开源工具
- iPhone Wiki 上的 [Usbmuxd 协议文档](https://www.theiphonewiki.com/wiki/Usbmux) - 记录了 usbmuxd 协议和 Lockdownd 协议（控制设备上的 USB 服务）
- [发现 iOS Instruments Server](https://github.com/troybowman/dtxmsg/blob/master/slides.pdf) - Troy Bowman 关于 Xcode 如何与 iOS 设备通信的演示文稿

# 我的收获

- macOS 上的系统守护进程存储其偏好设置的位置
- Apple 系统日志（Apple System Logger）框架中的日志级别
- 我**确实**能写一篇短文

[https://worthdoingbadly.com/usbmuxdebug/](https://worthdoingbadly.com/usbmuxdebug/)
