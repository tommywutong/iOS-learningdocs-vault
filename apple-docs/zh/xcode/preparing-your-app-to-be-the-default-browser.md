---
title: 准备你的 App 成为默认网页浏览器
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/preparing-your-app-to-be-the-default-browser
source_url: 'https://developer.apple.com/documentation/xcode/preparing-your-app-to-be-the-default-browser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/preparing-your-app-to-be-the-default-browser.json'
content_hash: 'sha256:cb9d3afb8f4ad9c4'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Projects and workspaces](projects-and-workspaces.md) · [Allowing apps and websites to link to your content](allowing-apps-and-websites-to-link-to-your-content.md)

# 准备你的 App 成为默认网页浏览器

<sub>文章</sub>

配置你的浏览器 App，让用户可以在其设备上将其设置为默认浏览器，而不是 Safari。

## 概述

在 iOS 14 及更高版本中，用户可以选择一个 App 作为其默认网页浏览器。要让你的 App 成为可选项，请先确认你的 App 满足下面的要求，然后申请一项受管理的 entitlement。

### 配置你的 App 成为默认浏览器

每当用户打开 HTTP 或 HTTPS 链接时，iOS 系统都会调用默认网页浏览器。因为这个 App 会成为用户访问互联网的主要入口，Apple 要求网页浏览类 App 满足特定的功能标准，以保护用户隐私并确保对互联网资源的正确访问。

App 通过使用 [com.apple.developer.web-browser](../bundleresources/entitlements/com.apple.developer.web-browser.md) 受管理 entitlement 来表明自己具备成为默认网页浏览器的能力。

> [!important] 重要
> 通过填写[默认浏览器 entitlement 申请表](https://developer.apple.com/contact/request/default-browser-entitlement/)来申请默认浏览器 entitlement。在该表单中，你还可以申请 [com.apple.developer.browser.app-installation](../bundleresources/entitlements/com.apple.developer.browser.app-installation.md) entitlement。如果你这样做，并且你的默认浏览器 entitlement 申请获得批准，你就会同时获得默认浏览器 entitlement 和你的浏览器 App 的 app-installation entitlement。

### 满足默认浏览器的要求

注册为默认网页浏览器选项的 App 必须满足以下标准：

- 你的 App 必须在其 `Info.plist` 文件中指定 HTTP 和 HTTPS scheme。
- 你的 App 不能使用 [UIWebView](../uikit/uiwebview.md)。
- 在启动时，App 必须提供一个用于输入 URL 的文本栏、用于在互联网上查找相关链接的搜索工具，或者精选的书签列表。

在其默认配置下打开 HTTP 或 HTTPS URL 时：

- App 必须直接导览到指定的目的地并渲染预期的网页内容。重定向到意外位置或渲染目的地源代码中未指定内容的 App，不满足默认网页浏览器的要求。
- 设计用于在家长控制或锁定模式下运行的 App，可以为符合这些目标而限制导览。
- 你的 App 可以对疑似钓鱼或存在其他问题的内容显示「安全浏览」或其他警告。
- 你的 App 可以为同时提供原生网页登录流程的网站提供原生身份验证界面。

### 使用默认浏览器功能

使用 [com.apple.developer.web-browser](../bundleresources/entitlements/com.apple.developer.web-browser.md) 受管理 entitlement 的 App 可以：

- 成为用户选择其默认浏览器的可选项之一。
- 以完整的脚本访问权限加载来自所有域的页面。
- 在 [WKWebView](../webkit/wkwebview.md) 实例中使用 Service Worker。
- 在创建 [UIActivityViewController](../uikit/uiactivityviewcontroller.md) 时，将当前的 [WKWebView](../webkit/wkwebview.md) 包含在 `activityItems` 数组中，从而在分享表单中提供「添加到主屏幕」操作。

### 遵守浏览器限制

拥有 [com.apple.developer.web-browser](../bundleresources/entitlements/com.apple.developer.web-browser.md) 受管理 entitlement 的 App，不得声称能响应特定域的通用链接。系统会忽略任何此类声明。拥有该 entitlement 的 App 仍然可以像往常一样打开通往其他 App 的通用链接。

由于浏览器 App 在用户网页浏览中占据特权地位，它们应避免不必要地访问个人数据。在使用 [com.apple.developer.web-browser](../bundleresources/entitlements/com.apple.developer.web-browser.md) 受管理 entitlement 的同时使用以下任何 `Info.plist` 键的 App 都会被拒绝：

- [NSPhotoLibraryUsageDescription](../bundleresources/information-property-list/nsphotolibraryusagedescription.md)——为了保存图像，你的 App 应仅指定 [NSPhotoLibraryAddUsageDescription](../bundleresources/information-property-list/nsphotolibraryaddusagedescription.md)。[WKWebView](../webkit/wkwebview.md) 仍然可以上传照片和文件，而无需你的 App 访问用户的整个照片图库。要访问单张照片，你的 App 应使用不需要 [NSPhotoLibraryUsageDescription](../bundleresources/information-property-list/nsphotolibraryusagedescription.md) 的 [PHPickerViewController](../photosui/phpickerviewcontroller.md)，而不是 [UIImagePickerController](../uikit/uiimagepickercontroller.md)。
- [NSLocationAlwaysUsageDescription](../bundleresources/information-property-list/nslocationalwaysusagedescription.md)、[NSLocationAlwaysAndWhenInUseUsageDescription](../bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription.md)——为了确定用户的位置，请改为请求「使用期间」授权（[NSLocationWhenInUseUsageDescription](../bundleresources/information-property-list/nslocationwheninuseusagedescription.md)）。浏览器不得始终访问位置信息。
- [NSHomeKitUsageDescription](../bundleresources/information-property-list/nshomekitusagedescription.md)——浏览器不能访问用户的 HomeKit 数据库。
- [NSBluetoothAlwaysUsageDescription](../bundleresources/information-property-list/nsbluetoothalwaysusagedescription.md)——浏览器不能在 App 处于后台时轮询蓝牙设备。浏览器应为蓝牙功能使用 `NSBluetoothWhileInUseUsageDescription`。
- [NSHealthShareUsageDescription](../bundleresources/information-property-list/nshealthshareusagedescription.md)、[NSHealthUpdateUsageDescription](../bundleresources/information-property-list/nshealthupdateusagedescription.md)——浏览器不能访问用户的健康数据库。

> [!note] 注意
> [NSLocationAlwaysUsageDescription](../bundleresources/information-property-list/nslocationalwaysusagedescription.md) 已在 iOS 10 中废弃。更多信息请参阅[选择要申请的位置服务授权](../bundleresources/choosing-the-location-services-authorization-to-request.md)。

### 检查你的 App 是否为默认浏览器

要测试用户是否已将你的 App 配置为 iOS 中的默认浏览器，请使用类别 [UIApplication.Category.webBrowser](../uikit/uiapplication/category/webbrowser.md) 调用 [isDefault(_:)](<../uikit/uiapplication/isdefault(__).md>)（Swift）或 [defaultStatusForCategory:error:](../uikit/uiapplication/defaultstatusforcategory_error_.md)（Objective-C）。

这个方法有速率限制：如果你的 App 调用得过于频繁，该方法会抛出错误。错误的用户信息字典中 [retryAvailableDateErrorKey](../uikit/uiapplication/categorydefaulterror/retryavailabledateerrorkey.md) 键对应的值，是你的 App 下次可以检查自己是否为默认浏览器的日期。

### 提供替代浏览器引擎

如果你的 iOS 浏览器 App 包含替代浏览器引擎——即使用操作系统提供的框架之外的其他版本 WebKit——你需要将你的浏览器设计为一个托管扩展的 App，用来访问系统资源并处理不可信数据。更多信息请参阅 [BrowserEngineKit](../browserenginekit.md)。
</content>
