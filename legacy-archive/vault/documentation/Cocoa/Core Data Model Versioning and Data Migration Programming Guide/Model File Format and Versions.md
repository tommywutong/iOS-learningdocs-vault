---
title: Core Data 模型版本管理与数据迁移编程指南
apple_id: TP40004399
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/vmModelFormat.html
archived_at: '2026-07-15T07:14:29.257550Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 模型版本管理与数据迁移编程指南](Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md)


[下一页](Lightweight%20Migration.md)[上一页](Understanding%20Versions.md)

# 模型文件格式与版本

一个支持版本管理的托管对象模型，在文件系统中以 `.xcdatamodeld` 文档的形式表示。`.xcdatamodeld` 文档是一个文件包（参见 [Document Packages](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/DocumentPackages/DocumentPackages.html#//apple_ref/doc/uid/10000123i-CH106)），其中汇集了该模型的各个版本，每个版本由一个独立的 `.xcdatamodel` 文件表示，此外还有一个包含版本信息的 `Info.plist` 文件。

该模型会被编译为运行时格式——一个扩展名为 `.momd` 的文件包，其中包含各个独立编译好的、扩展名为 `.mom` 的模型文件。你可以使用 `NSManagedObjectModel` 的 [initWithContentsOfURL:](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506225-init) 来加载 `.momd` 模型包。

要为模型添加一个版本，可以从类似图 2-1 所示的模型开始。

__图 2-1__  Core Recipes 模型的初始版本

!

要添加一个版本，选择 Editor > Add Model Version。在弹出的表单中，输入新模型版本的名称，并选择该版本所基于的模型。

要将新模型设置为该模型的当前版本，在项目导航器中选中 `.xcdatamodeld` 文档，然后在属性检查器（Attributes Inspector）的 Versioned Core Data Model 区域的弹出菜单中选择新模型（见图 2-2）。

__图 2-2__  Core Recipes 模型的第 2 版

!!
[下一页](Lightweight%20Migration.md)[上一页](Understanding%20Versions.md)
