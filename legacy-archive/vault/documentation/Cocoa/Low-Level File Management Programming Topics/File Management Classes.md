---
title: 底层文件管理编程主题
apple_id: 10000055i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/Classes.html
archived_at: '2026-07-15T07:16:32.994938Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [底层文件管理编程主题](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)


[下一页](Creating%20Paths%20and%20Locating%20Directories.md)[上一页](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)

# 文件管理类

本文介绍用于与文件、卷宗（volume）和 Finder 交互的主要类。

你可以使用 `NSFileManager` 对象执行许多通用的文件系统操作——例如你可以：

- 创建目录和文件。
- 提取文件的内容（作为 `NSData` 对象）。
- 更改你在文件系统中的当前工作位置。
- 复制、移动和链接文件与目录。
- 移除文件、链接和目录。
- 获取并（在适当的情况下）设置文件、目录或文件系统的属性。
- 确定目录的内容。
- 比较文件和目录是否相等。
- 创建和解析符号链接。

除了提供一系列有用的通用功能外，`NSFileManager` 类还将应用程序与底层文件系统隔离开来。这种隔离的一个重要方面是文件名的编码（例如 Unicode、ISO Latin1 和 ASCII）。文件系统有一个默认的 `NSFileManager` 对象；该对象响应所有请求对相关文件系统执行操作的消息。

作为 `NSFileManager` 方法参数指定的路径名可以是绝对路径，也可以是相对于当前目录的路径（当前目录可以用 [currentDirectoryPath](https://developer.apple.com/documentation/foundation/nsfilemanager/1410766-currentdirectorypath) 确定，用 [changeCurrentDirectoryPath:](https://developer.apple.com/documentation/foundation/nsfilemanager/1412020-changecurrentdirectorypath) 设置）。但是，路径名不能包含通配符。

你可以为文件管理器设置一个委托（delegate）；委托允许你在各种事件发生之后修改管理器的行为。例如，[fileManager:shouldProceedAfterError:removingItemAtURL:](https://developer.apple.com/documentation/foundation/nsfilemanagerdelegate/1408660-filemanager) 允许你的委托介入移除某个项目的过程。

你可以使用 `NSWorkspace` 来：

- 打开、操作文件和设备，并获取它们的信息。
- 跟踪文件系统、设备和用户数据库的变化。
- 获取和设置文件的 Finder 信息。
- 启动应用程序。

`NSURL` 类提供了一种操作 URL _及其所引用资源_的方式。你可以使用 `NSURL` 对象来引用文件，这也是首选的方式。特别是在 Mac OS X v10.6 及更高版本中，能够读写文件数据的对象通常都有接受 `NSURL` 对象（而非路径名）作为文件引用的方法。基于 URL 的操作通常比等效的基于路径的操作高效得多。

你可以使用 `NSString` 对象来表示路径。`NSString` 提供了许多工具方法供你操作路径，例如查找文件名或路径扩展名。在 Mac OS X v10.6 及更高版本中，你应该使用 `NSURL` 对象而不是字符串来表示路径——URL 通常要高效得多。

[下一页](Creating%20Paths%20and%20Locating%20Directories.md)[上一页](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)
