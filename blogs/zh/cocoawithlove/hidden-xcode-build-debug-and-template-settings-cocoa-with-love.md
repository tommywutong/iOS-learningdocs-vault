---
title: '隐藏的 Xcode 构建设置、调试设置与模板设置 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/06/hidden-xcode-build-debug-and-template.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:9c3ed1dc77e5abf8'
translated: true
---

> 原文：[Hidden Xcode build, debug and template settings | Cocoa with Love](https://www.cocoawithlove.com/2008/06/hidden-xcode-build-debug-and-template.html)　·　Cocoa with Love (Matt Gallagher)

本文收集了 Xcode 中与构建、调试和文件模板相关的最实用却又不容易发现的隐藏设置。

这篇文章介绍的是 Xcode 中那些大多数程序员都离不开、却又很难找到的设置。写这个话题让我感觉有点奇怪，因为这里的大部分信息在别处都有文档。但我发现自己仍然会忘记并且需要重新发掘这些小技巧（尽管我已经使用 ProjectBuilder/Xcode 七年了，本该记住的），所以我觉得这些信息值得反复巩固。

我将介绍：

- [GCC 的自定义编译器标志](#compilersettings)
- [构建前和构建后的脚本](#buildscripts)
- [更改构建后程序的名称](#buildname)
- [替换文件模板中烦人的 "__MyCompanyName__" 占位符](#mycompanyname)
- [完全自定义文件模板](#filetemplates)
- [自定义、修改和添加自动补全的“文本宏”](#textmacros)
- [为调试配置环境变量和可执行文件参数](#environmentvariables)

## 自定义编译器设置

Xcode 项目中的默认编译器设置相当不错。即便如此，程序员的天职就是摆弄一切，而摆弄编译器设置正是编程项目的核心。

自定义编译设置在 Xcode 中藏得相当深。要访问自定义编译器设置，你必须：

1. 确保 Xcode 中置前的是项目窗口或项目包含的文档窗口。
2. 从菜单栏的“项目”菜单中选择“编辑项目设置”菜单项   
  **_或者_**  
   右键单击项目窗口中“组与文件”树状视图中的项目图标，然后从弹出菜单中选择“显示简介”（默认情况下，项目图标是一个蓝色的文档图标，位于此树状视图的最顶部）。
3. 在出现的项目信息窗口顶部选择“构建”标签页。
4. 从标签面板顶部的弹出菜单中将“配置”设置为“调试”、“发布”或“所有配置”（编译设置只会为你选择的配置更改）。
5. 向下滚动到名为“GCC 4.0 - 语言”的标题。
6. 这些复选框中的每一个都允许自定义构建设置。如果你想知道每个设置会影响什么，请点击该行并显示“研究助理”（Control-Command-?）。

可以使用“其他 C 标志”行（用于 C 和 Objective-C）或“其他 C++ 标志”（用于 C++）将完全自定义的命令行设置传递给编译器。

有关 Xcode 构建设置的更多信息，请参阅“[Xcode 构建设置参考](http://developer.apple.com/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/Introduction/Introduction.html)”。

## 构建后或构建前脚本

构建阶段是 Xcode 执行构建中不同步骤的方式。如果你展开项目窗口中“组与文件”树状视图的“目标”节点下的一个目标，就可以看到构建的不同步骤。对于一个普通的“Cocoa 应用程序”，步骤依次是“拷贝 Bundle 资源”、“编译源代码”和“将二进制文件与库链接”。

你可以通过右键单击目标，然后从弹出菜单的“添加”子菜单中选择想要的构建阶段，来向目标添加一个新的构建阶段。

你也可以从菜单栏“项目”菜单的“新建构建阶段”子菜单中选择一个选项，将构建阶段添加到当前目标。

要添加一个“脚本”构建阶段，请选择“新建运行脚本构建阶段”。这将在构建的最后一个阶段添加一个新脚本。如果你希望该脚本是一个“构建前”脚本，则必须将其拖拽到项目窗口中“组与文件”树状视图的“目标”节点下为该目标显示的构建阶段列表的顶部。通过将其拖拽到其他阶段之间的位置，也可以实现“构建中”脚本。

最后，你必须输入脚本本身。选择该构建阶段，然后从菜单栏的“文件”菜单中选择“显示简介”。选择“通用”标签页，然后你就可以在“脚本”字段中输入脚本。

你可以在脚本中使用的变量列表，请参考 Xcode 文档中的[运行脚本构建阶段](http://developer.apple.com/documentation/DeveloperTools/Conceptual/XcodeUserGuide/Contents/Resources/en.lproj/05_03_bs_build_phases/chapter_32_section_9.html)页面。

## 更改构建后程序的名称

这可能有点难找，因为构建后程序的名称（例如“MyProgram.app”）在 Xcode 中并非以完整形式存在。

1. 确保 Xcode 中置前的是项目窗口或项目包含的文档窗口，并且“活动目标”设置为你要重命名其产品的目标。
2. 从菜单栏的“项目”菜单中选择“编辑活动目标‘...’”菜单项   
  **_或者_**   
   右键单击项目窗口中“组与文件”树状视图中“目标”下的目标名称，然后从弹出菜单中选择“显示简介”。
3. 在出现的项目信息窗口顶部选择“构建”标签页。
4. 从标签面板顶部的弹出菜单中将“配置”设置为“调试”、“发布”或“所有配置”（编译设置只会为你选择的配置更改）。
5. 向下滚动到名为“打包”的标题。

应用程序的名称将由“可执行前缀”（通常为空）、“产品名称”（最初与项目名称相同）、“可执行后缀”和“包装器扩展名”（对于应用程序通常是“.app”）组合而成。

简而言之，大多数情况下你只需要更改“产品名称”字段。

## 在新文件模板中替换 \_\_MyCompanyName\_\_

在终端窗口中输入以下命令：

```objc
defaults write com.apple.Xcode PBXCustomTemplateMacroDefinitions '{ "ORGANIZATIONNAME" = "Your Company Name" ; }'
```

将“Your Company Name”替换为你选择的任何内容。

你也可以在“属性列表编辑器”中打开 ~/Library/Preferences/com.apple.Xcode 文件，并在字典“PBXCustomTemplateMacroDefinitions”下将你的公司名称作为字符串值插入键“ORGANIZATIONNAME”。如果“PBXCustomTemplateMacroDefinitions”尚不存在，你可能需要在顶层创建它。

## 更改新文件模板

Xcode 用于新文件的完整文件模板集可以在“/Developer/Library/Xcode/File Templates/”中找到，按 API 分类（我们最喜欢 Cocoa）。

你可以根据需要添加或修改它们，但建议在其他位置备份已更改的文件，因为如果你将帐户迁移到新电脑或重新安装 Xcode，“/Developer/Library/Xcode/File Templates/”可能会丢失。

## 文本宏

Xcode 中的“文本宏”可以节省大量时间。你可以在“编辑”菜单下的“插入文本宏”中找到它们，但当你知道它们的快捷键时它们才是最方便的。在 Xcode 中编辑文档时输入快捷键，按“F5”键进行自动补全，宏会展开为完整形式，并带有变量位置。

有关默认文本宏及其快捷键的完整列表，请访问 Apple 的“[Xcode 用户指南：重复代码](http://developer.apple.com/mac/library/documentation/DeveloperTools/Conceptual/XcodeWorkspace/100-The_Text_Editor/text_editor.html#//apple_ref/doc/uid/TP40002679-SW43)”。

自定义文本宏的第一种方法是在你的“com.apple.Xcode”偏好设置文件中的“XCCodeSenseFormattingOptions”字典里为“BlockSeparator”、“IndentedBlockSeparator”、“InExpressionsSpacing”、“PostBlockSeparator”和“PreExpressionsSpacing”创建条目。

和之前一样，你可以这样操作：

```objc
defaults write com.apple.Xcode XCCodeSenseFormattingOptions '{ "BlockSeparator" = "\n" ; }'
```

或者直接编辑“~/Library/Preferences/com.apple.Xcode”文件。

你可能还想添加全新的宏，或者进行超出这些变量允许范围的更多自定义。做到这一点最好的方法是将“TextMacros.xctxtmacro”目录从：

```objc
/Developer/Applications/Xcode/Contents/PlugIns
```

复制到：

```objc
~/Library/Application Support/Developer/Shared/Xcode/Specifications
```

然后修改或补充 Apple 提供的宏。

不建议直接编辑 Xcode.app 内部的原始“TextMacros.xctxtmacro”定义。我们将它们复制到自己的 Library 中，因为每次更新 Xcode 时，Xcode.app 中的版本都会在没有警告的情况下被替换。

> **注意**：此处要复制“TextMacros.xctxtmacro”的目标路径是正确的，但上面链接的 Apple 提供的“重复代码”文档中的路径是错误的（该文档目前省略了“Shared”和“Specifications”之间的“Xcode”目录）。

宏按编程语言分类。我将留给你去弄清楚宏的具体格式。我不清楚 xctxtmacro 文件格式有任何正式文档，但它是一种“属性列表”风格的纯文本，所以你应该不难理解。

## 环境变量和可执行文件参数

选择所需项目和目标后，从菜单栏的“项目”菜单中选择“编辑活动可执行文件...”。在“参数”标签页中可以设置环境变量和可执行文件参数。

当使用 Cocoa 编程时，以下环境变量尤为重要：

- NSDebugEnabled 设置为 YES — 在 Foundation 中开启额外的调试信息
- NSZombieEnabled 设置为 YES — 当消息被错误地发送到已释放的对象时发出通知，从而更好地调试此问题

更多调试环境变量，请查看 Apple 的“[技术说明 TN2124：Mac OS X 调试魔法](http://developer.apple.com/technotes/tn2004/tn2124.html#SECFOUNDATION)”页面。
