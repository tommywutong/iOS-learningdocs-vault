---
title: Core Data 实用工具教程
apple_id: TP40001800
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataUtilityTutorial/Articles/02_creatingProj.html
archived_at: '2026-07-15T07:14:28.905189Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 实用工具教程](Introduction%20to%20Core%20Data%20Utility%20Tutorial.md)


[下一页](Creating%20the%20Managed%20Object%20Model.md)[上一页](Introduction%20to%20Core%20Data%20Utility%20Tutorial.md)

# 创建项目

本部分教程将引导你创建 CDCLI 项目。

Core Data 已集成到 [Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9)（以及 Cocoa Touch）[框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)中，因此任何 Cocoa 或 Foundation 应用程序都可以使用它。你将要构建的 CDCLI 程序是一个使用 Core Data 的 Foundation Tool。

请按照以下步骤创建初始项目：

1. 启动 Xcode。
2. [创建一个项目](https://developer.apple.com/library/archive/recipes/XcodeRecipes/Creating_a_Project/CreateProject.html#//apple_ref/doc/uid/TP40009043-CH10)，具备以下特征：

   - 平台：OS X
   - 模板类别：Application
   - 模板名称：Command Line Tool
   - 类型：Foundation
   - 使用 Automatic Reference Counting（自动引用计数）

   项目的名称并不重要。

1. 将 Core Data 框架[添加](https://developer.apple.com/library/archive/recipes/XcodeRecipes/Linking_to_Libraries_and_Frameworks/Linking_to_Libraries_and_Frameworks.html#//apple_ref/doc/uid/TP40009043-CH4)到项目的 target 中。（Foundation tool 并不会自动链接 Core Data 框架，所以你需要手动添加。）
2. 在主源文件中添加一条 import 语句：

```objc
#import <CoreData/CoreData.h>
```


至此，你创建了一个非常简单的 Foundation Tool 项目，并添加了 Core Data 框架。这强调了一点：你并不需要使用 Application Kit 或 UIKit 来构建图形用户界面。甚至也没有必要使用 Xcode 的数据建模工具——在下一章中，你将完全用代码创建模型。不过，使用建模工具确实能为你节省大量时间和精力。

[下一页](Creating%20the%20Managed%20Object%20Model.md)[上一页](Introduction%20to%20Core%20Data%20Utility%20Tutorial.md)

