---
title: 底层文件管理编程主题
apple_id: 10000055i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Introduction.html
archived_at: '2026-07-15T07:16:37.187464Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[下一页](File%20Management%20Classes.md)

# 底层文件管理编程主题简介

本文档介绍用于操作文件和目录（文件夹）的方法与函数。

你应该阅读本文档，以了解如何：

- 在 Cocoa 中表示文件路径
- 对文件和目录执行基本操作
- 在系统中查找标准目录

本文档包含以下文章：

- [文件管理类](File%20Management%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tanrzfvjvomi) 介绍用于文件系统操作的主要类。
- [创建路径与定位目录](Creating%20Paths%20and%20Locating%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tslkcineussccivcq) 说明如何构造文件系统操作中使用的路径。
- [文件管理](File%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44dalkcijbumrchizbq) 介绍如何执行许多通用的文件系统操作。
- [关于文件和卷宗的信息](Information%20about%20Files%20and%20Volumes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tanryfvjvomi) 介绍如何获取和设置有关文件和卷宗的信息。
- [使用 URL](Using%20URLs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tanjzfvjvomq) 介绍如何使用 `NSURL` 执行各种与文件相关的操作。
- [处理目录的内容](Working%20with%20the%20Contents%20of%20a%20Directory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44dglkciffemqsbifea) 介绍如何使用 `NSDirectoryEnumerator` 对象获取目录的内容。
- [解析替身](Resolving%20Aliases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge3dqlkcijbukrsfizfa) 介绍如何解析文件路径中的替身（alias）。
- [File Handle](File%20Handle.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44delkcijbumrchizbq) 介绍为访问打开的文件或通信通道提供封装的类。
- [HFS 文件类型](HFS%20File%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43tslkcijbumrchizbq) 介绍允许 Cocoa 应用程序获取和创建 HFS 类型代码与创建者代码的 API。

要了解如何使用文件封装器（以及 `NSFileWrapper` 类），请参阅 _[Application File Management](../Application%20File%20Management/Introduction%20to%20Application%20File%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tm2i)_。

[下一页](File%20Management%20Classes.md)
