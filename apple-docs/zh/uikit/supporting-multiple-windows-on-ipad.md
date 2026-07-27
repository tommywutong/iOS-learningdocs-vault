---
title: 在 iPad 上支持多个窗口
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 13.3+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/supporting-multiple-windows-on-ipad
source_url: 'https://developer.apple.com/documentation/uikit/supporting-multiple-windows-on-ipad'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/supporting-multiple-windows-on-ipad.json'
content_hash: 'sha256:527c9ecf7aa64c8e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md) · [iPad、Mac 和 Apple Vision Pro 上的多任务处理](multitasking-on-ipad-mac-and-apple-vision-pro.md)

# 在 iPad 上支持多个窗口

<sub>示例代码</sub>

支持并排显示你 App 界面的多个实例，并创建新窗口。

## 概述

此示例展示了如何创建多个窗口，让用户能够创建 App 中内容相似或不同的独立部分。窗口由场景（scene）或 [UISceneSession](uiscenesession.md) 类管理。你的 App 使用 [UISceneDelegate](uiscenedelegate.md) 和 [UISceneConfiguration](uisceneconfiguration.md) 管理窗口的生命周期。场景拥有自己的专属生命周期，并与 [UIApplication](uiapplication.md) 分开管理。

采用多窗口架构时，管理 App 的 [UIApplicationDelegate](uiapplicationdelegate.md) 类会管理新创建的场景。随后，`UISceneDelegate` 会取代 `UIApplicationDelegate` 的委托（delegate）函数中的代码。

UIKit 提供了专门帮助管理窗口的 `UISceneDelegate` 子类 [UIWindowSceneDelegate](uiwindowscenedelegate.md)。在运行于 iOS 12 或更低版本的现有 App 中采用多窗口架构时，需要将更多职责从 `UIApplicationDelegate` 移交给 `UIWindowSceneDelegate`。

有关 iPadOS App 中多个窗口的更多信息，请参阅 [iOS 人机界面指南](https://developer.apple.com/design/human-interface-guidelines/ios/system-capabilities/multiple-windows/)。

> [!note] 注意
> 此示例代码项目在 WWDC 2019 场次 212：[iPad 上的多窗口简介](https://developer.apple.com/videos/play/wwdc2019/212)中进行了讨论和演示。

### 配置示例代码项目

在 Xcode 中，通过 iOS 目标的 Signing & Capabilities 标签页选择你的开发团队。

### 添加多场景支持

为支持多个窗口，App 的 `Info.plist` 需要包含清单或 [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md)，其中含有 App 对基于场景的生命周期支持的相关信息。存在此键表示 App 支持场景，并且不使用 App 委托（app delegate）对象来管理进入和离开前台或后台的过渡。请包含键 [`UIApplicationSupportsMultipleScenes`](../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md)，并将其布尔值设为 `true`，以表明 App 同时支持两个或更多场景。

### 添加场景委托

此示例提供了一个名为 `SceneDelegate` 的 `UIWindowScene` 子类，用于管理 App 的主窗口场景。[- scene:willConnectToSession:options:](<uiscenedelegate/scene(__willconnectto_options_).md>) 委托函数负责设置窗口和内容。

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
    if let userActivity = connectionOptions.userActivities.first ?? session.stateRestorationActivity {
        if !configure(window: window, with: userActivity) {
            Swift.debugPrint("Failed to restore from \(userActivity)")
        }
    }
    // 'window' 属性会自动加载 Storyboard 的初始视图控制器。
    
    // 设置作用于 'targetContentIdentifier' 的激活谓词。
    let conditions = scene.activationConditions
    let prefsPredicate = NSPredicate(format: "self == %@", mainSceneTargetContentIdentifier)
    // 主谓词，用于向系统说明场景能够显示哪种内容。
    conditions.canActivateForTargetContentIdentifierPredicate = prefsPredicate
    // 次谓词，用于向系统说明此场景对某类特定内容特别感兴趣。
    conditions.prefersToActivateForTargetContentIdentifierPredicate = prefsPredicate
}
```

通过在 `Info.plist` 场景清单中使用 [`UISceneConfigurations`](../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations.md) 键，该示例的此场景窗口会自动配置，并从 Storyboard 加载根视图控制器。

### 恢复场景

需要恢复场景时，iOS 会调用委托的 `scene(_:willConnectTo:options:)`。示例 App 使用 [`NSUserActivity`](../foundation/nsuseractivity.md) 将场景恢复到先前状态。

```swift
func configure(window: UIWindow?, with activity: NSUserActivity) -> Bool {
    var configured = false

    guard activity.activityType == UserActivity.GalleryOpenDetailActivityType else { return configured }
    guard let navigationController = window?.rootViewController as? UINavigationController else { return configured }
        
    if let photoID = activity.userInfo?[UserActivity.GalleryOpenDetailPhotoAssetKey] as? String,
        let photoTitle = activity.userInfo?[UserActivity.GalleryOpenDetailPhotoTitleKey] as? String {
        // 使用 'photoID' 和 'photoTitle' 恢复视图控制器。
        if let photoDetailViewController = PhotoDetailViewController.loadFromStoryboard() {
            photoDetailViewController.photo = Photo(assetName: photoID, title: photoTitle)

            navigationController.pushViewController(photoDetailViewController, animated: false)
            configured = true
        }
    }
    return configured
}
```

### 通过拖放（drag and drop）创建多个窗口

当用户将图像从集合视图拖到 iPad 屏幕的左侧或右侧时，此示例会创建一个单独窗口。示例通过实现 `UICollectionViewDragDelegate` 函数 [- collectionView:itemsForBeginningDragSession:atIndexPath:](<uicollectionviewdragdelegate/collectionview(__itemsforbeginning_at_).md>)，并提供带有关联 [`NSItemProvider`](../foundation/nsitemprovider.md) 的 [UIDragItem](uidragitem.md) 来创建新窗口。然后，示例使用已注册的 `NSUserActivity` 将照片数据传递给新窗口场景。

```swift
func collectionView(_ collectionView: UICollectionView, itemsForBeginning session: UIDragSession, at indexPath: IndexPath) -> [UIDragItem] {
    var dragItems = [UIDragItem]()
    let selectedPhoto = photos[indexPath.row]
    if let imageToDrag = UIImage(named: selectedPhoto.assetName) {
        let userActivity = selectedPhoto.detailUserActivity
        let itemProvider = NSItemProvider(object: imageToDrag)
        itemProvider.registerObject(userActivity, visibility: .all)

        let dragItem = UIDragItem(itemProvider: itemProvider)
        dragItem.localObject = selectedPhoto
        dragItems.append(dragItem)
    }
    return dragItems
}
```

`NSUserActivity` 的 [`activityType`](../foundation/nsuseractivity/activitytype.md) 必须包含在 App `Info.plist` 的 [`NSUserActivityTypes`](../bundleresources/information-property-list/nsuseractivitytypes.md) 数组中。如果没有它，将照片拖到设备边缘时就不会创建单独窗口。

```swift
    <key>NSUserActivityTypes</key>
    <array>
        <string>com.apple.gallery.openDetail</string>
    </array>
```

### 以编程方式创建多个窗口

此示例还会通过响应用户操作，以编程方式创建单独的窗口场景：

- **iPadOS**：轻触并按住一张照片，然后选择菜单项 Inspect。这样会创建一个包含该照片的表单样式窗口（form sheet window）。随后可以将该窗口拖到 iPad 屏幕的左侧或右侧，将 App 界面一分为二。
- **macOS**：选择一张照片。点按工具栏的 Info 按钮，或按住 Command 键点按照片并选择 Inspect。这两种方式都会创建一个包含该照片的新窗口。

这两种方式都使用以下代码创建新窗口场景。

```swift
class func openInspectorSceneSessionForPhoto(_ photo: Photo, requestingScene: UIWindowScene, errorHandler: ((Error) -> Void)? = nil) {
    let options = UIWindowScene.ActivationRequestOptions()
    options.preferredPresentationStyle = .prominent
    options.requestingScene = requestingScene // 请求激活另一场景的场景对象。
    
    // 将此场景作为独立于主窗口的次要窗口呈现。
    //
    // 查找与照片匹配且已经打开的窗口场景会话。
    if let foundSceneSession = InspectorSceneDelegate.activeInspectorSceneSessionForPhoto(photo.assetName) {
        // 检查器场景会话已打开，因此将其激活。
        UIApplication.shared.requestSceneSessionActivation(foundSceneSession, // 激活找到的场景会话。
                                                           userActivity: nil, // 已打开的会话无需传递活动。
                                                           options: options,
                                                           errorHandler: errorHandler)
    } else {
        // 未找到检查器场景会话，因此创建一个新会话。
        let userActivity = photo.inspectorUserActivity

        UIApplication.shared.requestSceneSessionActivation(nil, // 传入 nil 表示创建新会话。
                                                           userActivity: userActivity,
                                                           options: options,
                                                           errorHandler: errorHandler)
    }
}
```

通过使用唯一的 `NSUserActivity` [`activityType`](../foundation/nsuseractivity/activitytype.md)，App 可以在 [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>) 中区分要创建哪种新场景：

```swift
func application(_ application: UIApplication,
                 configurationForConnecting connectingSceneSession: UISceneSession,
                 options: UIScene.ConnectionOptions) -> UISceneConfiguration {
    // 每个 UISceneConfiguration 必须具有唯一的配置名称。
    var configurationName: String!

    switch options.userActivities.first?.activityType {
    case UserActivity.GalleryOpenInspectorActivityType:
        configurationName = "Inspector Configuration" // 创建照片检查器窗口场景。
    default:
        configurationName = "Default Configuration" // 创建默认照片图库窗口场景。
    }
    
    return UISceneConfiguration(name: configurationName, sessionRole: connectingSceneSession.role)
}
```

## 另请参阅

### 场景管理

- [场景](scenes.md) — 同时管理你 App UI 的多个实例，并将资源定向到适当的 UI 实例。

## 下载

- [SupportingMultipleWindowsOnIPad.zip](https://docs-assets.developer.apple.com/published/70ff427f711f/SupportingMultipleWindowsOnIPad.zip)
