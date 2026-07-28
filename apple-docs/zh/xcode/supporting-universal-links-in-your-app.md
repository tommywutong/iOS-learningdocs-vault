---
title: 在你的 App 中支持通用链接
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/supporting-universal-links-in-your-app
source_url: 'https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/supporting-universal-links-in-your-app.json'
content_hash: 'sha256:0416740b689dd31f'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [项目与工作区](projects-and-workspaces.md) · [允许 App 与网站链接到你的内容](allowing-apps-and-websites-to-link-to-your-content.md)

# 在你的 App 中支持通用链接

<sub>文章</sub>

让你的 App 准备好响应传入的通用链接。

## 概述

当用户激活通用链接时，系统会启动你的 App 并向其发送一个 [NSUserActivity](../foundation/nsuseractivity.md) 对象。查询此对象以了解你的 App 如何启动，并决定要采取什么操作。

要支持你 App 中的通用链接：

1. 在 App 与网站之间建立双向关联，并指定你的 App 处理的 URL。请参阅[支持关联域名](supporting-associated-domains.md)。
2. 更新 App 的委托（delegate），使其在收到 [activityType](../foundation/nsuseractivity/activitytype.md) 设置为 [NSUserActivityTypeBrowsingWeb](../foundation/nsuseractivitytypebrowsingweb.md) 的 [NSUserActivity](../foundation/nsuseractivity.md) 对象时做出响应。

> [!warning] 警告
> 通用链接为你的 App 提供了一个潜在的攻击向量，因此请务必验证所有 URL 参数并丢弃格式错误的 URL。此外，应将可用操作限制为那些不会危及用户数据的操作。例如，不要允许通用链接直接删除内容或访问用户的敏感信息。在测试你的 URL 处理代码时，请确保测试用例包含格式不正确的 URL。

### 更新你的 App 委托以响应通用链接

当系统因通用链接打开你的 App 时，你的 App 会收到一个 [activityType](../foundation/nsuseractivity/activitytype.md) 值为 [NSUserActivityTypeBrowsingWeb](../foundation/nsuseractivitytypebrowsingweb.md) 的 [NSUserActivity](../foundation/nsuseractivity.md) 对象。该活动对象的 [webpageURL](../foundation/nsuseractivity/webpageurl.md) 属性（property）包含用户访问的 HTTP 或 HTTPS URL。使用 [NSURLComponents](../foundation/nsurlcomponents.md) API 来提取 URL 的组成部分。请参阅后面的示例。

以下示例代码展示了如何在 macOS 中处理通用链接：

```swift
func application(_ application: NSApplication,
                     continue userActivity: NSUserActivity,
                     restorationHandler: @escaping ([NSUserActivityRestoring]) -> Void) -> Bool
{
    // 从传入的用户活动中获取 URL 组件。
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let incomingURL = userActivity.webpageURL,
        let components = NSURLComponents(url: incomingURL, resolvingAgainstBaseURL: true) else {
        return false
    }

    // 检查你需要的特定 URL 组件。
    guard let path = components.path,
    let params = components.queryItems else {
        return false
    }    
    print("path = \(path)")

    if let albumName = params.first(where: { $0.name == "albumname" } )?.value,
        let photoIndex = params.first(where: { $0.name == "index" })?.value {            
        print("album = \(albumName)")
        print("photoIndex = \(photoIndex)")
        return true  

    } else {
        print("Either album name or photo index missing")
        return false
    }
}
```

以下示例代码展示了如何在 iOS 和 tvOS 中处理通用链接：

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool
{
    // 从传入的用户活动中获取 URL 组件。
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let incomingURL = userActivity.webpageURL,
        let components = NSURLComponents(url: incomingURL, resolvingAgainstBaseURL: true) else {
        return false
    }

    // 检查你需要的特定 URL 组件。
    guard let path = components.path,
    let params = components.queryItems else {
        return false
    }    
    print("path = \(path)")

    if let albumName = params.first(where: { $0.name == "albumname" } )?.value,
        let photoIndex = params.first(where: { $0.name == "index" })?.value {

        print("album = \(albumName)")
        print("photoIndex = \(photoIndex)")
        return true

    } else {
        print("Either album name or photo index missing")
        return false
    }
}
```

如果你的 App 已选择使用[场景](../uikit/scenes.md)，且 App 未在运行，系统会在启动后将通用链接传递给 [scene(_:willConnectTo:options:)](<../uikit/uiscenedelegate/scene(__willconnectto_options_).md>) 委托方法；当 App 正在运行或挂起在内存中时点击通用链接，系统会将其传递给 [scene(_:continue:)](<../uikit/uiscenedelegate/scene(__continue_).md>) 方法。

```swift
func scene(_ scene: UIScene, willConnectTo
           session: UISceneSession,
           options connectionOptions: UIScene.ConnectionOptions) {
    
    // 从传入的用户活动中获取 URL 组件。
    guard let userActivity = connectionOptions.userActivities.first,
        userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let incomingURL = userActivity.webpageURL,
        let components = NSURLComponents(url: incomingURL, resolvingAgainstBaseURL: true) else {
        return
    }

    // 检查你需要的特定 URL 组件。
    guard let path = components.path,
        let params = components.queryItems else {
        return
    }
    print("path = \(path)")

    if let albumName = params.first(where: { $0.name == "albumname" })?.value,
        let photoIndex = params.first(where: { $0.name == "index" })?.value {
        
        print("album = \(albumName)")
        print("photoIndex = \(photoIndex)")
    } else {
        print("Either album name or photo index missing")
    }
}
```

以下示例代码展示了如何在 watchOS 中处理通用链接：

```swift
func handle(_ userActivity: NSUserActivity)
{
    // 从传入的用户活动中获取 URL 组件。
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let incomingURL = userActivity.webpageURL,
        let components = NSURLComponents(url: incomingURL, resolvingAgainstBaseURL: true) else { return }

    // 检查你需要的特定 URL 组件。
    guard let path = components.path,
    let params = components.queryItems else { return }    
    print("path = \(path)")

    if let albumName = params.first(where: { $0.name == "albumname" } )?.value,
        let photoIndex = params.first(where: { $0.name == "index" })?.value {            
        print("album = \(albumName)")
        print("photoIndex = \(photoIndex)")
    } else {
        print("Either album name or photo index missing")
    }
}
```

> [!note] 注意
> 在 watchOS 中，类似 Safari 的界面可供“信息”和“邮件”等 App 使用。对于其他 App，当用户点击指向某个配套 App 中内容的通用链接，但用户并未安装该配套 App 时，系统会通知用户在 iPhone 上查看该 URL。
