---
title: 资源编程指南
apple_id: 10000051i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/DataResourceFiles/DataResourceFiles.html
archived_at: '2026-07-15T07:16:32.526254Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [资源编程指南](About%20Resources.md)


[下一页](Document%20Revision%20History.md)[上一页](Image%2C%20Sound%2C%20and%20Video%20Resources.md)

# 数据资源文件

把应用的数据与代码分开，可以让你日后更容易修改应用。如果你把应用的配置数据存放在资源文件中，就可以在不重新编译应用的情况下改变这些配置。数据资源文件可以用来存储任何类型的信息。下面几节重点介绍 iOS 和 OS X 支持的一些数据资源类型。

属性列表文件是一种把自定义配置数据存放在应用代码之外的方式。OS X 和 iOS 大量使用属性列表来实现诸如用户偏好设置、bundle 的信息属性列表文件之类的特性。你同样可以用属性列表来存储应用的私有（或公开）配置数据。

属性列表文件本质上就是一组结构化的数据值。你可以通过编程方式创建和编辑属性列表，也可以使用 Property List Editor 应用（位于 `/Developer/Applications/Utilities`）来创建和编辑。自定义属性列表文件的结构完全由你决定。你可以用属性列表存储字符串、数字、布尔值、日期和原始数据值。默认情况下，属性列表把数据存放在单个字典结构中，但你也可以把额外的字典和数组作为值赋进去，从而构建层次更丰富的数据集。

有关使用属性列表的信息，请参阅 _[属性列表编程指南](../Property%20List%20Programming%20Guide/Introduction%20to%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2i)_ 和 _[Core Foundation 属性列表编程主题](../../Core%20Foundation/Property%20List%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezta2i)_。

表 4-1 列出了 Mac 应用中支持的另外一些资源文件类型。

__表 4-1__  其他资源类型

| 资源类型 | 说明 |
| --- | --- |
| AppleScript 文件 | 在 OS X 中，AppleScript 术语文件和套件文件包含着与应用可脚本化能力有关的信息。这些文件可以使用 `.sdef`、`.scriptSuite` 或 `.scriptTerminology` 文件扩展名。由于用于给应用编写脚本的实际 AppleScript 命令在用户脚本和 Script Editor 应用中是可见的，因此这些资源需要本地化。有关支持 AppleScript 的信息，请参阅 _[AppleScript 概述](../../Apple%20Script/AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_。 |
| 帮助文件 | 在 OS X 中，帮助内容通常由一组 HTML 文件构成，这些文件用标准的文本编辑程序创建，并注册到 Help Viewer 应用中。（有关如何向 Help Viewer 注册的信息，请参阅 _[Apple Help 编程指南](../../Carbon/Apple%20Help%20Programming%20Guide/Introduction%20to%20Apple%20Help%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbt)_。）你也可以把 PDF 文件、RTF 文件、HTML 文件或其他自定义文档嵌入到 bundle 中，并用 Preview、Safari 之类的外部应用来打开它们。有关如何打开文件的信息，请参阅 _[Launch Services 编程指南](../../Carbon/Launch%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojz)_。 |

[下一页](Document%20Revision%20History.md)[上一页](Image%2C%20Sound%2C%20and%20Video%20Resources.md)

