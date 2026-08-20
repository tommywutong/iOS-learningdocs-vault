---
title: 偏好与设置编程指南
apple_id: 10000059i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/Introduction/Introduction.html
archived_at: '2026-07-15T07:21:01.849355Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](About%20the%20User%20Defaults%20System.md)

# 关于偏好设置与设置

偏好设置（preferences）是你持久化存储、用于配置应用的信息片段。应用通常会把偏好设置暴露给用户，让用户自定义应用的外观与行为。大多数偏好设置都存储在本地，使用的是 Cocoa 偏好设置系统——也就是所谓的 _用户默认设置系统（user defaults system）_。应用也可以使用键值存储把偏好设置保存到用户的 iCloud 账户中。

用户默认设置系统和键值存储都是为在属性列表中存储简单数据类型而设计的——字符串、数字、日期、布尔值、URL、数据对象等等。使用属性列表还意味着你可以用数组和字典类型来组织你的偏好设置数据。此外，只要先把其他对象编码成 `NSData` 对象，也可以把它们存进属性列表。

应用集成偏好设置的方式有好几种，包括在代码中的各个位置以编程方式使用，以及作为用户界面的一部分呈现。iOS 应用和 Mac 应用都支持偏好设置。

### 由你决定要暴露哪些偏好设置

每个应用的偏好设置都不一样，究竟把应用的哪些部分做成可配置的，取决于你。所谓配置，就是在代码中检查某个已存储偏好设置的值，并根据该值采取相应行动。因此，偏好设置的值本身应当始终保持简单，并具有由你的应用来实现的特定含义。

### 应用自行提供偏好设置界面

由于每个应用的偏好设置各不相同，应用自身要负责决定如何以最佳方式把这些偏好设置呈现给用户——如果确实需要呈现的话。iOS 和 OS X 都提供了一些标准位置供你放置偏好设置界面，但你仍然要负责设计该界面并在恰当的时机显示它。

### 应用通过用户默认设置对象访问偏好设置

应用通过用户默认设置对象来访问本地存储的偏好设置，该对象要么是 [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) 对象（iOS 和 OS X），要么是 [NSUserDefaultsController](https://developer.apple.com/documentation/appkit/nsuserdefaultscontroller) 对象（仅限 OS X）。除了读取偏好设置的值，应用还可以用这个对象为偏好设置注册默认值，以及管理偏好设置系统的其他方面。

### iCloud 存储共享的偏好设置与配置数据

支持 iCloud 的应用可以把一部分偏好设置数据放到用户的 iCloud 账户里，让运行在用户其他设备上的应用实例也能访问这些数据。你可以利用这一能力来补充（而不是取代）应用已有的偏好设置数据，从而在用户的多台设备之间提供更连贯的体验。例如，一个杂志应用可以存储用户最后阅读的页码和期号，这样运行在另一台设备上的该应用就能显示同一页内容。

### 在 OS X 中默认设置按域分组

OS X 的偏好设置是按域分组的，这样系统偏好设置就能与应用偏好设置区分开来。以这种方式拆分偏好设置，可以让用户在全局层面指定一些偏好设置，然后在某个应用内部覆盖其中的一项或多项。

### Settings bundle 管理 iOS 应用的偏好设置

在 iOS 中，应用可以在「设置」应用里显示自己的偏好设置，对于那些用户不需要频繁配置的偏好设置来说，这是个不错的去处。为了在「设置」应用中显示偏好设置，应用的 bundle 必须包含一种名为 _Settings bundle_ 的特殊资源，它定义了要显示哪些偏好设置、以何种方式显示，以及记录用户选择所需的信息。

关于属性列表的信息，请参阅 _[属性列表编程指南](../Property%20List%20Programming%20Guide/Introduction%20to%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2i)_。

关于使用 Core Foundation 管理偏好设置的进阶信息，请参阅 _[Core Foundation 偏好设置编程主题](../../Core%20Foundation/Preferences%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezds2i)_。

[下一页](About%20the%20User%20Defaults%20System.md)

