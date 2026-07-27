---
title: 通过基于用户活动的建议提高 App 使用率
framework: Foundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, Xcode 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/increasing-app-usage-with-suggestions-based-on-user-activities
source_url: 'https://developer.apple.com/documentation/foundation/increasing-app-usage-with-suggestions-based-on-user-activities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/increasing-app-usage-with-suggestions-based-on-user-activities.json'
content_hash: 'sha256:63af3419a260ec6f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Task Management](task-management.md)

# 通过基于用户活动的建议提高 App 使用率

<sub>示例代码</sub>

通过从你的 App 中捕获信息，并将这些信息作为主动建议展示在整个系统中，来提供连续的用户体验。

## 概述

这个示例 App 会在表格视图中显示你当前位置附近的一份披萨店列表。从表格视图中选择一家餐厅，即可将其位置信息作为用户活动对象捐赠给系统。系统随后会主动展示已注册的位置信息作为建议，例如在与 Siri 快捷指令配合使用的搜索中。

当用户与某个主动建议进行交互时，系统会通过将该对象的活动类型与该示例 App 关联起来，来继续该活动。

在捐赠位置信息时，这个示例 App 还会验证之前捕获的信息，是否作为 QuickType 键盘建议出现在设备上安装的其他 App 中。

### 声明一个用户活动类型

要实现主动建议，你需要确定用户在你的 App 中可以执行的具体活动，并且你能够在之后重新创建这些活动的状态。这个示例 App 有一个用户活动 `view-location`，代表用户正在查看某个具体餐厅位置的详情。

在这个示例 App 中，目标将 `view-location` 活动作为一个条目包含在其 [Information Property List](../bundleresources/information-property-list.md) 文件中，键名为 。这个条目的类型是 `Array`，每个成员都是一个 `String`，以反向 DNS 表示法表示一个受支持的用户活动。

```
<key>NSUserActivityTypes</key>
<array>
<string>com.example.apple-samplecode.ProactiveToolbox.view-location</string>
</array>
```

### 管理用户活动

在运行时，你使用 [NSUserActivity](nsuseractivity.md) 对象来表示一个用户活动。你使用一个字符串标识符来初始化用户活动对象，这个标识符与之前在 `Info.plist` 文件中声明的相同。

在这个示例 App 中，`LocationViewController` 管理着一个代表 `view-location` 活动类型的 [NSUserActivity](nsuseractivity.md) 对象。当你选择一家餐厅时，视图控制器会将其 [userActivity](../uikit/uiresponder/useractivity.md) 属性设置为 `view-location` 活动——将该用户活动对象注册为当前活动，替换掉之前发送给 Siri 或系统的任何其他活动。

> [!important] 重要
> 当用户活动对象不包含在响应者链中时，你必须调用 [- becomeCurrent](<nsuseractivity/becomecurrent().md>) 方法，将该对象标记为当前活动，这同时也会向系统注册该对象。

视图控制器还会将 [needsSave](nsuseractivity/needssave.md) 设置为 `true`，表示该活动今后会随新数据一起更新，这最终会导致对 [updateUserActivityState(_:)](<../uikit/uiresponder/updateuseractivitystate(__).md>) 方法的回调。在 Siri 或系统接收该活动之前，这是 App 刷新活动对象 [userInfo](nsuseractivity/userinfo.md) 属性的机会，只需提供恢复 App 状态所需的最少信息。

```swift
/*
 在 `userInfo` 字典中提供恰好足够恢复状态的信息即可。
 字典越大，传递该负载并恢复活动所需的时间就越长。
 */
var userInfo = [String: Any]()
do {
    let data = try NSKeyedArchiver.archivedData(withRootObject: mapItem.placemark, requiringSecureCoding: true)
    userInfo["placemark"] = data
} catch {
    os_log("Could not encode placemark data", type: .error)
}

if let phoneNumber = mapItem.phoneNumber {
    userInfo["phoneNumber"] = phoneNumber
}

activity.addUserInfoEntries(from: userInfo)
```

### 提供改进搜索结果的支持

如果你的用户活动对象包含用户之后可能想要搜索的信息，你可以让「搜索」为这些对象建立索引，并在后续的设备端搜索中加以考虑。

要为用户活动对象启用「搜索」支持，将 [eligibleForSearch](nsuseractivity/iseligibleforsearch.md) 属性设置为 `true`。此外，你还可以通过将 [eligibleForPublicIndexing](nsuseractivity/iseligibleforpublicindexing.md) 属性设置为 `true`，让活动对象对所有 iOS 用户公开可访问。

```swift
// The following properties enable the activity to be indexed in Search.
activity.isEligibleForPublicIndexing = true
activity.isEligibleForSearch = true
activity.title = mapItem?.name
activity.keywords = ["pizza"]
```

通过配置 [contentAttributeSet](nsuseractivity/contentattributeset.md)、[keywords](nsuseractivity/keywords.md) 或 [webpageURL](nsuseractivity/webpageurl.md) 属性，为活动对象提供尽可能丰富的相关信息，以便系统能够为该对象建立索引。App 还必须对系统用于搜索结果的任何活动对象保持强引用。

```swift
// Provide additional searchable attributes.
activity.contentAttributeSet?.supportsNavigation = true
activity.contentAttributeSet?.supportsPhoneCall = true
activity.contentAttributeSet?.thumbnailData = #imageLiteral(resourceName: "pizza").pngData()
```

要了解「搜索」的更多信息，请参阅 [App Search Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch)。

### 提供对快捷指令的支持

Siri 通过你的 App 向 Siri 所做的捐赠，来了解你 App 可用的快捷指令。当某个操作涉及你 App 中的某个视图时，例如这个会显示附近餐厅列表的示例 App，你就可以从一个用户活动进行捐赠。

这个示例 App 通过将用户活动对象的 [eligibleForPrediction](nsuseractivity/iseligibleforprediction.md) 属性设置为 `true`，为其启用 Siri 快捷指令支持。App 通过为 [suggestedInvocationPhrase](nsuseractivity/suggestedinvocationphrase.md) 属性设置一个简短、易记的短语，来建议一个调用短语，该短语会在用户创建快捷指令时显示给用户。

```swift
// The following properties enable the activity to be used as a shortcut with Siri.
activity.isEligibleForPrediction = true
activity.suggestedInvocationPhrase = "Show my favorite pizzeria"
```

在开发期间，系统提供了开发者设置，用于修改快捷指令的显示行为，并强制将快捷指令从 iPhone 设备同步到 Apple Watch。前往 iPhone 设备上的「设置」\>「开发者」，测试 App 在 Siri 快捷指令方面的行为。

要了解更多信息，请参阅 [Donating Shortcuts](../sirikit/donating-shortcuts.md)。

### 提供对共享的支持

如果你的用户活动对象包含某个网页的信息，你的用户就可以通过 Siri 与他人共享该网页。例如，用户可以通过让 Siri「share this」（分享这个）来分享他们正在查看的披萨店，从而向另一位用户发送一条包含该网页 URL 的消息。Siri 会使用 App 存储在用户活动的 [webpageURL](nsuseractivity/webpageurl.md) 中的 URL。

```swift
// Enable sharing this location by telling Siri to "share this".
activity.webpageURL = mapItem?.url
```

### 处理活动

当用户与你 App 的某个主动建议进行交互时，例如通过 Siri 快捷指令，系统会将你的 App 恢复到前台，接收与其用户活动相关联的数据，并调用 [application(_:continue:restorationHandler:)](<../uikit/uiapplicationdelegate/application(__continue_restorationhandler_).md>)。

为了让 `SearchViewController` 有机会通过 [restoreUserActivityState(_:)](<../uikit/uiresponder/restoreuseractivitystate(__).md>) 执行其状态恢复操作，这个示例 App 会验证用户活动对象的活动类型，并将第一个标签页的视图控制器层级结构传递给 `restorationHandler` 代码块参数。

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    
    guard userActivity.activityType == "com.example.apple-samplecode.ProactiveToolbox.view-location",
        let tabBarController = window?.rootViewController as? UITabBarController,
        let navigationController = tabBarController.viewControllers?.first as? UINavigationController
        else { return false }
    
    tabBarController.selectedIndex = 0
    
    /*
     Calling the restoration handler is optional and is only needed
     when specific objects are capable of continuing the activity.
     */
    restorationHandler(navigationController.viewControllers)
    
    return true
}
```

这个示例 App 会验证用户活动，从 `userInfo` 字典中提取所需的任何信息，并更新其 UI，从用户上次离开的地方继续所请求的活动。

```swift
override func restoreUserActivityState(_ activity: NSUserActivity) {
    super.restoreUserActivityState(activity)
    
    do {
        guard let userInfo = activity.userInfo,
            let url = activity.webpageURL,
            let phoneNumber = userInfo["phoneNumber"] as? String,
            let placemarkData = userInfo["placemark"] as? Data,
            let placemark = try NSKeyedUnarchiver.unarchivedObject(ofClass: MKPlacemark.self, from: placemarkData)
            else { return }
        
        let mapItem = MKMapItem(placemark: placemark)
        mapItem.name = activity.title
        
        if navigationController?.visibleViewController == self {
            restoreMapItem(mapItem, url: url, phoneNumber: phoneNumber)
        } else if let modalController = navigationController?.visibleViewController as? LocationViewController {
            modalController.restoreMapItem(mapItem, url: url, phoneNumber: phoneNumber)
        }
    } catch {
        os_log("Could not convert user activity placemark data to placemark object", type: .error)
    }
}
```

### 验证 QuickType 键盘集成

文本栏通过 [textContentType](../uikit/uitextinputtraits/textcontenttype.md) 属性来描述输入数据的预期用途，比如某个地区的名称或邮政编码。如果设备上任何一个 App 最近捐赠了与预期文本内容类型相匹配的信息，当用户在该文本栏中输入时，该信息就会作为建议出现在 QuickType 键盘中。

例如，在这个示例 App 中，用户选择了一家披萨店，其地址就会在「信息」或 Apple 地图的搜索栏中被建议出来。

```swift
// These properties can also be set on the field in Interface Builder.
nameTextField.textContentType = .organizationName
streetAddressLine1TextField.textContentType = .streetAddressLine1
streetAddressLine2TextField.textContentType = .streetAddressLine2
cityTextField.textContentType = .addressCity
stateTextField.textContentType = .addressState
postalCodeTextField.textContentType = .postalCode
countryOrRegionTextField.textContentType = .countryName
```

要验证这一行为，请在 Apple 地图中选择一个兴趣点，然后返回这个示例 App，查看捐赠的信息是否已填充到 QuickType 键盘中。

## 另请参阅

### Activity Sharing

- [Creating a user activity object](creating-a-user-activity-object.md) — 确定关键的用户交互，并包含用于在之后恢复它们的信息。
- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md) — 直接创建、发送和接收用户活动。
- [Continuing User Activities with Handoff](continuing-user-activities-with-handoff.md) — 定义并管理你 App 的哪些活动可以在设备之间继续。
- [Supporting the creation of Quick Notes](supporting-the-creation-of-quick-notes.md) — 支持创建包含你 App 内容的备忘录。
- [NSUserActivity](nsuseractivity.md) — 你的 App 在某一时刻状态的表示形式。
- [NSUserActivityDelegate](nsuseractivitydelegate.md) — 用户活动实例通过其向委托通知更新的接口。

## 下载

- [IncreasingAppUsageWithSuggestionsBasedOnUserActivities.zip](https://docs-assets.developer.apple.com/published/b8d8e4357791/IncreasingAppUsageWithSuggestionsBasedOnUserActivities.zip)
</content>
