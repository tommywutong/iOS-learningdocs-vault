---
title: 资源编程指南
apple_id: 10000051i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html
archived_at: '2026-07-15T07:16:32.541988Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Nib%20Files.md)

# 关于资源

在计算机程序中，资源是伴随程序可执行代码一同存在的数据文件。资源把复杂数据集合或图形内容的创建工作从代码中移出，交给更合适的工具去完成，从而简化了你必须编写的代码。例如，与其用代码逐个像素地创建图像，不如在图像编辑器中创建它们，那样效率高得多（也实际得多）。要用上一个资源，你的代码只需在运行时加载它并使用它。

除了简化代码之外，资源也是所有应用国际化过程中密不可分的一环。与其把字符串和其他用户可见的内容硬编码到应用里，不如把这些内容放到外部的资源文件中。这样一来，本地化你的应用就变成了一件简单的事：为每种支持的语言各创建一份资源文件的新版本即可。OS X 和 iOS 共同使用的 [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) 机制提供了一种组织本地化资源的方式，并简化了加载与用户首选语言相匹配的资源文件的过程。

本文档介绍 OS X 和 iOS 支持的资源类型，以及如何在代码中使用这些资源。本文档不讨论资源的创建过程。大多数资源都是用第三方应用，或者用 `/Developer/Applications` 目录中提供的开发者工具创建的。此外，虽然本文档谈的是在应用中使用资源，但这些内容同样适用于其他类型的打包可执行文件，包括[框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)和插件。

在阅读本文档之前，你应当熟悉应用 bundle 所规定的组织结构。理解这一结构能让你更容易地组织和查找应用所使用的资源文件。有关 bundle 结构的信息，请参阅 _[Bundle 编程指南](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_。

应用可以包含许多类型的资源，但其中有几种是 iOS 和 OS X 直接支持的。

### nib 文件存储应用用户界面中的对象

nib 文件是创建 iOS 和 Mac 应用时最典型的资源类型。_nib 文件_ 是一种数据归档，本质上包含一组被“冻结”起来、等待在运行时重新创建的对象。nib 文件最常用于存储预先配置好的窗口、视图以及其他面向视觉的对象，但它们也可以存储控制器这类非可视对象。

你在 Xcode 中通过 Interface Builder 编辑 nib 文件，它提供了一个用于组装对象的图形化编辑器。当你随后把一个 nib 文件加载到应用中时，nib 加载代码会实例化文件中的每个对象，并把它恢复成你在 Interface Builder 中指定的状态。因此，你在 Interface Builder 中看到的，正是应用运行时你所得到的。

### 包含可本地化文本的字符串资源

文本是大多数用户界面的重要组成部分，同时也是受本地化改动影响最大的资源。iOS 和 OS X 不主张把文本硬编码进代码，而是支持把用户可见的文本存放在 _strings 文件_ 中——这是一种人类可读的文本文件（采用 UTF-16 编码），其中包含一个应用所用的一组字符串资源。（这里刻意使用复数形式“strings”，因为这类文件使用的是 `.strings` 文件扩展名。）strings 文件让你只需编写一次代码，然后从可以轻松更改的资源文件中加载相应的本地化文本，从而极大地简化了国际化和本地化的过程。

Core Foundation 和 Foundation 框架提供了从 strings 文件加载文本的功能。使用这些功能的应用还可以借助 Xcode 附带的工具，在整个开发过程中生成和维护这些资源文件。

### 图像、声音和影片代表预先渲染好的内容

图像、声音和影片资源在 iOS 和 Mac 应用中扮演着重要角色。图像负责营造每个操作系统独有的视觉风格；它们还有助于简化你为复杂视觉元素编写的绘图代码。类似地，声音和影片文件既能提升应用的整体用户体验，又能简化实现这种体验所需的代码。这两个操作系统都为在应用中加载和呈现这类资源提供了广泛的支持。

### 属性列表和数据文件把数据与代码分离

属性列表文件是一种结构化文件，用于存储字符串、数字、布尔值、日期和原始数据值。文件中的数据项使用数组和字典结构来组织，大多数数据项都关联着一个唯一的键。系统使用属性列表来存储简单的数据集。例如，几乎每个应用中都能找到的 `Info.plist` 文件就是属性列表文件的一个例子。你也可以用属性列表文件来满足简单的数据存储需求。

除属性列表之外，OS X 还支持一些用于特定用途的特殊结构化文件。例如，AppleScript 数据和用户帮助就是用特殊格式的数据文件来存储的。你也可以创建自己的自定义数据文件。

### iOS 支持设备专属资源

在 iOS 4.0 及更高版本中，可以把单个资源文件标记为只在特定类型的设备上使用。这一能力简化了你为通用（Universal）应用所要编写的代码。你不必再创建各自独立的代码路径，为 iPhone 加载资源文件的一个版本、为 iPad 加载该文件的另一个版本，而是可以让 bundle 加载例程去挑选正确的文件。你要做的只是给资源文件起一个合适的名字。

要把资源文件与特定设备关联起来，你需要在它的文件名中加上一个自定义修饰字符串。加入这个修饰字符串后，文件名格式如下：

_<basename>__<device>_`.`_<filename_extension>_

_<basename>_ 字符串代表资源文件的原始名称，也是你在代码中访问该文件时使用的名称。同样，_<filename_extension>_ 字符串就是用于标识文件类型的标准文件扩展名。_<device>_ 字符串区分大小写，可以是下列值之一：

- `~ipad` - 该资源只应在 iPad 设备上加载。
- `~iphone` - 该资源只应在 iPhone 或 iPod touch 设备上加载。

你可以对任何类型的资源文件应用设备修饰符。例如，假设你有一张名为 `MyImage.png` 的图像。要为 iPad 和 iPhone 指定不同版本的图像，你需要创建名为 `MyImage~ipad.png` 和 `MyImage~iphone.png` 的资源文件，并把它们都包含进 bundle 中。加载这张图像时，你在代码中仍然按 `MyImage.png` 来引用该资源，让系统去选择合适的版本，如下所示：

```objc
UIImage* anImage = [UIImage imageNamed:@"MyImage.png"];
```

在 iPhone 或 iPod touch 设备上，系统会加载 `MyImage~iphone.png` 资源文件；而在 iPad 上，它会加载 `MyImage~ipad.png` 资源文件。如果找不到某个资源的设备专属版本，系统就会回过头去查找使用原始文件名的资源，在前面这个例子中也就是名为 `MyImage.png` 的图像。

下列 Apple 开发者文档在概念上与 _资源编程指南_ 相关：

- _[Bundle 编程指南](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_ 描述了应用用来存储可执行代码和资源的 bundle 结构。
- _[国际化与本地化指南](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_ 描述了为把应用（及其资源）翻译成其他语言而做准备的过程。
- _[Xcode 概述](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/index.html#//apple_ref/doc/uid/TP40010215)_ 中的 Build a User Interface 一章介绍了用于编辑 nib 文件资源的工具。
- _[属性列表编程指南](../Property%20List%20Programming%20Guide/Introduction%20to%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2i)_ 描述了把属性列表资源文件加载到 Cocoa 应用中所用的机制。
- _[Core Foundation 属性列表编程主题](../../Core%20Foundation/Property%20List%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezta2i)_ 描述了把属性列表资源文件加载到基于 C 的应用中所用的机制。
[下一页](Nib%20Files.md)

