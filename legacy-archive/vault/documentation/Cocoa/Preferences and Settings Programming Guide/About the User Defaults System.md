---
title: 偏好与设置编程指南
apple_id: 10000059i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/AboutPreferenceDomains/AboutPreferenceDomains.html
archived_at: '2026-07-15T07:21:01.829819Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [偏好与设置编程指南](About%20Preferences%20and%20Settings.md)


[下一页](Accessing%20Preference%20Values.md)[上一页](About%20Preferences%20and%20Settings.md)

# 关于用户默认设置系统

用户默认设置（user defaults）系统负责管理每个用户的偏好设置存储。大多数偏好设置都是持久化存储的，因此不会在你的应用两次启动之间发生变化。应用使用偏好设置来跟踪由用户发起和由程序发起的配置变更。

在定义应用的偏好设置时，最好尽可能使用简单的值和数据类型。偏好设置系统是围绕属性列表数据类型（如字符串、数字和日期）构建的。虽然你可以用 [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 对象在偏好设置中存储任意对象，但在大多数情况下并不推荐这么做。

持久化存储对象意味着你的应用总要在某个时刻对该对象解码。就偏好设置而言，存储对象意味着每次访问该偏好设置时都要解码一次。这还意味着，你的应用的新版本必须确保自己能够解码由旧版本创建并写入磁盘的对象，而这很容易出错。

对于偏好设置，更好的做法是存储简单的字符串和值，并用它们来创建应用所需的对象。存储简单值意味着你的应用总能访问到该值。版本之间唯一发生变化的，是对这个简单值的解释以及应用据此创建的对象。

对于面向用户的偏好设置，表 1-1 列出了将其展示给用户的各种选项。从这张表可以看出，大多数选项都需要你创建自定义用户界面来管理和呈现偏好设置。如果你开发的是 iOS 应用，可以用 Settings bundle 来呈现偏好设置，但只应把那些用户很少更改的设置放在那里。

__表 1-1__  向用户展示偏好设置的选项

| 偏好设置 | iOS | OS X |
| --- | --- | --- |
| 频繁更改的偏好设置 | 自定义 UI | 自定义 UI |
| 不常更改的偏好设置 | Settings bundle | 自定义 UI |

Mac 应用的偏好设置应当可以通过应用菜单中的「偏好设置」菜单项访问。使用 Xcode 模板创建的 Cocoa 应用会自动为你提供这样一个菜单项。当用户选择该菜单项时，你要负责呈现合适的用户界面。你可以在应用委托（delegate）中定义一个显示自定义偏好设置窗口的[动作方法](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/TargetAction.html#//apple_ref/doc/uid/TP40009448-CH3)，并在 Interface Builder 中把该动作方法连接到菜单项上，从而提供这个界面。

在 iOS 应用内部显示自定义偏好设置并没有标准做法。你可以用许多方式来集成偏好设置，包括在标签栏界面中单独使用一个标签页，或者在应用的某个界面上放一个自定义按钮。偏好设置一般应当用一个独立的视图控制器来呈现，这样当用户关闭该视图控制器时就可以记录偏好设置的变更。

偏好设置被分组到各个域（domain）中，每个域都有一个名称和特定的用途。例如，有一个域用于存放应用专属的偏好设置，另一个域用于存放适用于所有应用的系统级偏好设置。所有偏好设置都是按用户逐一存储和访问的，不支持在不同用户之间共享偏好设置。

每一项偏好设置都有三个组成部分：

- 它所存储于的域
- 它的名称（用 `NSString` 对象指定）
- 它的值，可以是任意属性列表对象（`NSData`、`NSString`、`NSNumber`、`NSDate`、`NSArray` 或 `NSDictionary`）

一项偏好设置的生命期取决于你把它存放在哪个域里。有些域通过把偏好设置写入用户的默认设置数据库来持久化存储它们，这类偏好设置会从应用的一次启动一直保留到下一次启动。另一些域则以更易失的方式存储偏好设置，只在对应的用户默认设置对象存活期间保留其值。

查找某项偏好设置的值时，会依次遍历 [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) 对象搜索列表中的各个域。只有搜索列表中的域才会被搜索，并且按表 1-2 所示的顺序搜索，从 `NSArgumentDomain` 域开始。一旦找到具有指定名称的偏好设置，搜索就结束。如果多个域都包含同一项偏好设置，则取搜索列表中最靠前的那个域里的值。

__表 1-2__  域的搜索顺序

| 域 | 状态 |
| --- | --- |
| [NSArgumentDomain](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSArgumentDomain) | 易失 |
| 应用（由应用的标识符标识） | 持久 |
| [NSGlobalDomain](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSGlobalDomain) | 持久 |
| 语言（由语言名称标识） | 易失 |
| [NSRegistrationDomain](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSRegistrationDomain) | 易失 |

参数域包含从命令行参数设置的值（前提是你从命令行启动应用），由 [NSArgumentDomain](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSArgumentDomain) 常量标识。从命令行设置的值会由系统自动放入该域。要向这个域中添加一个值，请在命令行上指定偏好设置的名称（前面加一个连字符），后面跟上对应的值。例如，下面的命令会启动 Xcode 并把它的 `IndexOnOpen` 偏好设置的值设为 `NO`：

```bash
localhost> Xcode.app/Contents/MacOS/Xcode -IndexOnOpen NO
```

从命令行设置的偏好设置会临时覆盖用户默认设置数据库中已有的值。在前面的例子中，把 `IndexOnOpen` 偏好设置设为 `NO` 会阻止 Xcode 自动为项目建立索引，即便用户默认设置数据库中该偏好设置被设为 `YES` 也是如此。

应用域包含应用专属的偏好设置，它们存储在当前用户的默认设置数据库中。当你使用共享的 [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) 对象（或在 OS X 中使用 [NSUserDefaultsController](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller) 对象）写入偏好设置时，这些偏好设置会自动被放入该域。

由于这个域是应用专属的，域中的内容与你的应用的 bundle 标识符绑定。该域的内容存储在一个由系统管理的文件中。目前，这个文件位于 _$HOME_`/Library/Preferences/` 目录下，其中 _$HOME_ 要么是应用的主目录，要么是用户的主目录（取决于平台以及你的应用是否运行在沙盒中）。用户默认设置数据库文件的名称是 _<ApplicationBundleIdentifer>_`.plist`，其中 _<ApplicationBundleIdentifer>_ 是你的应用的 bundle 标识符。你不应该直接修改这个文件，但可以在调试期间查看它，以确认你的应用确实写入了预期的偏好设置值。

全局域包含适用于所有应用的偏好设置，由 [NSGlobalDomain](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSGlobalDomain) 常量标识。这个域通常由系统框架用来存储系统级的值，你的应用不应该用它来存储应用专属的值。如果你想更改全局域中某项偏好设置的值，请把同名偏好设置以新值写入应用域。

系统框架使用该域的一些例子：

- `NSRuleView` 类的实例把用户偏好的度量单位存储在 `AppleMeasurementUnits` 键下。使用这个存储位置可以让所有应用中的标尺视图都使用相同的单位。
- 系统使用 `AppleLanguages` 键，以字符串数组的形式存储用户偏好的语言。例如，用户可以指定英语为首选语言，其后依次是西班牙语、法语、德语、意大利语和瑞典语。

对于 `AppleLanguages` 偏好设置中的每一种语言，系统都会把与该语言相关的偏好设置值记录在一个以语言名称命名的域中。每个语言专属的域都包含对应区域设置的偏好设置。Foundation 框架中的许多类（例如 `NSDate`、`NSDateFormatter`、`NSTimeZone`、`NSString` 和 `NSScanner` 类）都会利用这些区域设置信息来调整自身行为。例如，当你请求某个 `NSCalendarDate` 对象的字符串表示时，该 `NSCalendarDate` 对象会利用区域设置信息，按用户的首选语言查找月份名和星期名。

注册域定义了一组默认值，当某项偏好设置在其他任何域中都没有被显式设置时就使用这些值。应用可以在启动时调用 `NSUserDefaults` 的 [registerDefaults:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/registerDefaults:) 方法，为重要的偏好设置指定一组默认值。应用首次启动时，大多数偏好设置还没有值，因此读取它们会得到未定义的结果。注册一组默认值可以确保你的应用始终有一组已知良好的值可用。

注册域的内容只能通过 [registerDefaults:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/registerDefaults:) 方法来设置。

在 OS X 中，`defaults` 命令行工具让你可以查看用户默认设置数据库的内容。在应用开发期间，你可以用这个工具来验证应用写入磁盘的偏好设置。为此，你可以在「终端」应用中使用如下形式的命令：

`defaults read` _<application-bundle-identifier>_

要读取全局域的内容，可以使用下面的命令：

`defaults read NSGlobalDomain`

关于使用 defaults 工具读写偏好设置值的更多信息，请参阅 `defaults` 手册页。

[下一页](Accessing%20Preference%20Values.md)[上一页](About%20Preferences%20and%20Settings.md)

