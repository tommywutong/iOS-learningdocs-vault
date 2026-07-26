---
title: 允许 App 和网站链接到你的内容
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/allowing-apps-and-websites-to-link-to-your-content
source_url: 'https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content.json'
content_hash: 'sha256:61402b20e2b3c78c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Projects and workspaces](projects-and-workspaces.md)

# 允许 App 和网站链接到你的内容

使用通用链接直接链接到你 App 内部的内容，并安全地共享数据。

## 概述

你可以使用通用链接连接到 App 深处的内容。用户在指定的上下文中打开你的 App，从而能够高效地完成他们的目标。

当用户点按或点击一个通用链接时，系统会将该链接直接重定向到你的 App，而不经过用户的默认网页浏览器或你的网站。此外，由于通用链接是标准的 HTTP 或 HTTPS 链接，同一个 URL 既适用于你的网站，也适用于你的 App。如果用户没有安装你的 App，系统会在其默认网页浏览器中打开该 URL，交由你的网站来处理。

当有人安装你的 App 时，系统会检查存储在你的 Web 服务器上的一个文件，以验证你的网站是否允许你的 App 代表它打开 URL。只有你才能将此文件存储在你的服务器上，从而确保你的网站与你的 App 之间的关联是安全的。

### 支持通用链接

请执行以下步骤以支持通用链接：

1. 在你的 App 和网站之间创建双向关联，并指定你的 App 处理的 URL，如[支持关联域](supporting-associated-domains.md)中所述。
2. 更新你的 App 委托，以响应系统在通用链接路由到你的 App 时提供的用户活动对象，如[在你的 App 中支持通用链接](supporting-universal-links-in-your-app.md)中所述。

借助通用链接，当用户在浏览器 App 或 [WKWebView](../webkit/wkwebview.md) 中点击指向你网站的链接时，以及当他们点击的链接会导致调用以下方法时，用户就会打开你的 App：

- iOS 和 tvOS 中的 [open(_:options:completionHandler:)](<../uikit/uiapplication/open(__options_completionhandler_).md>)
- watchOS 中的 [openSystemURL(_:)](<../watchkit/wkextension/opensystemurl(__).md>)
- macOS 中的 [open(_:withApplicationAt:configuration:completionHandler:)](<../appkit/nsworkspace/open(__withapplicationat_configuration_completionhandler_).md>)
- SwiftUI 中的 [openURL](../swiftui/environmentvalues/openurl.md)

> [!note] 注意
> 如果你的 App 使用上述方法之一打开一个指向你网站的通用链接，该链接不会在你的 App 中打开。

当用户在 Safari 中浏览你的网站，并点按同一域名下的通用链接时，系统会在 Safari 中打开该链接，以尊重用户很可能想要留在浏览器中继续操作的意图。如果用户点按的是不同域名下的通用链接，系统会在你的 App 中打开该链接。

### 与其他 App 通信

App 之间可以通过通用链接进行通信。支持通用链接可以让其他 App 直接向你的 App 发送少量数据，而无需使用第三方服务器。

在 URL 查询字符串中定义你 App 处理的参数。以下是一款照片图库 App 的示例代码，其中指定的参数包括要显示的相册名称和照片索引。

```other
https://myphotoapp.example.com/albums?albumname=vacation&index=1
https://myphotoapp.example.com/albums?albumname=wedding&index=17
```

其他 App 会根据你的域名、路径和参数构造 URL，并通过调用以下方法请求你的 App 打开它们：

- iOS 和 tvOS 中 [UIApplication](../uikit/uiapplication.md) 的 [open(_:options:completionHandler:)](<../uikit/uiapplication/open(__options_completionhandler_).md>) 方法
- watchOS 中 [WKExtension](../watchkit/wkextension.md) 的 [openSystemURL(_:)](<../watchkit/wkextension/opensystemurl(__).md>) 方法
- macOS 中 [NSWorkspace](../appkit/nsworkspace.md) 的 [open(_:withApplicationAt:configuration:completionHandler:)](<../appkit/nsworkspace/open(__withapplicationat_configuration_completionhandler_).md>) 方法
- SwiftUI 中的 [openURL](../swiftui/environmentvalues/openurl.md) 环境值

发起调用的 App 可以请求系统在你的 App 打开该 URL 时通知它。

在以下示例代码中，一个 App 在 iOS 和 tvOS 中调用你的通用链接：

```swift
if let appURL = URL(string: "https://myphotoapp.example.com/albums?albumname=vacation&index=1") {
    UIApplication.shared.open(appURL) { success in
        if success {
            print("The URL was delivered successfully.")
        } else {
            print("The URL failed to open.")
        }
    }
} else {
    print("Invalid URL specified.")
}
```

在以下示例代码中，一个 App 在 watchOS 中调用你的通用链接：

```swift
if let appURL = URL(string: "https://myphotoapp.example.com/albums?albumname=vacation&index=1") {
    WKExtension.shared().openSystemURL(appURL)
} else {
    print("Invalid URL specified.")
}
```

在以下示例代码中，一个 App 在 macOS 中调用你的通用链接：

```swift
if let appURL = URL(string: "https://myphotoapp.example.com/albums?albumname=vacation&index=1") {
    let configuration = NSWorkspace.OpenConfiguration()
    NSWorkspace.shared.open(appURL, configuration: configuration) { (app, error) in
        guard error == nil else {
            print("The URL failed to open.")
            return
        }
        print("The URL was delivered successfully.")
    }
} else {
    print("Invalid URL specified.")
}
```

有关在你的 App 中处理链接的更多信息，请参阅[在你的 App 中支持通用链接](supporting-universal-links-in-your-app.md)。

## 主题

### 通用链接

- [在你的 App 中支持通用链接](supporting-universal-links-in-your-app.md) — 为你的 App 做好准备，以响应传入的通用链接。

### 关联域

- [支持关联域](supporting-associated-domains.md) — 将你的 App 和一个网站连接起来，同时提供原生 App 体验和浏览器体验。

### 自定义 URL

- [为你的 App 定义自定义 URL 方案](defining-a-custom-url-scheme-for-your-app.md) — 使用特殊格式的 URL 链接到你 App 内的内容。

### 默认 App

- [准备将你的 App 设为默认网页浏览器](preparing-your-app-to-be-the-default-browser.md) — 配置你的浏览器 App，以便用户可以将其设置为设备上的默认浏览器，取代 Safari。
