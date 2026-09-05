---
title: 协作与共享你的数据的副本
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/collaborating-and-sharing-copies-of-your-data
source_url: 'https://developer.apple.com/documentation/uikit/collaborating-and-sharing-copies-of-your-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/collaborating-and-sharing-copies-of-your-data.json'
content_hash: 'sha256:4aa8ad9a84560769'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md)

# 协作与共享你的数据的副本

<sub>文章</sub>

从你的 App 出发共享数据并与他人协作。

## 概述

你可以使用 [UIActivityViewController](uiactivityviewcontroller.md) 对象从 App 中共享数据。打包数据和实例化活动视图控制器有许多种方式。其中一种是为你想共享的数据创建一个或多个 [NSItemProvider](../foundation/nsitemprovider.md) 对象。用这些条目提供程序（item provider）创建一个 [UIActivityItemsConfiguration](uiactivityitemsconfiguration.md)，再用该配置创建你的活动视图控制器，然后呈现这个视图控制器。

```swift
// Create an item provider for your data.
let itemProvider = NSItemProvider(item: noteText.text as NSString,
                                  typeIdentifier: "public.utf8-plain-text")

// Create an activity item configuration from the item provider.
let configuration =
UIActivityItemsConfiguration(itemProviders: [itemProvider])

// Create the activity view controller from the configuration.
let shareSheet = UIActivityViewController(activityItemsConfiguration: configuration)

// Present the share sheet.
present(shareSheet, animated: true) {}
```

这会显示共享面板（share sheet），让用户可以把数据的一份副本共享给设备上的其他 App。共享面板中出现的选项取决于你共享的数据类型。上面的例子共享一个 UTF-8 字符串，所以共享面板显示能接受文本的 App，比如信息（Messages）、邮件（Mail）和备忘录（Notes）。

![iPhone 屏幕快照：显示纯 UTF-8 文本文件的共享面板。](../../../attachments/c3684ad96b4797af5d30687b5a174215/media-4403929@2x.png)

### 为 iCloud 文稿启用协作

上面的例子共享的是你的 App 数据的一份副本。你也可以启用协作，让接收者看到数据的最新视图，甚至在你的 App 的权限允许下自行做出修改。

要启用协作，你需要可共享的内容，例如：

- 指向 iCloud 文稿的 URL（参见 [url(forUbiquityContainerIdentifier:)](<../foundation/filemanager/url(forubiquitycontaineridentifier_).md>)）
- 存储在 [CloudKit](../cloudkit.md) 中的数据
- 支持通用链接（universal link）的自定义协作架构（参见 [Integrate your custom collaboration app in Messages](https://developer.apple.com/videos/play/wwdc2022/10093)）

例如，要为 iCloud 文稿启用协作，你需要一个指向你的 App 的 iCloud 容器中文件的 URL。创建一个 [NSItemProvider](../foundation/nsitemprovider.md) 对象，调用它的 [registerFileRepresentation(for:visibility:openInPlace:loadHandler:)](<../foundation/nsitemprovider/registerfilerepresentation(for_visibility_openinplace_loadhandler_).md>) 方法，把 URL 作为 `for:` 参数传入，并把 [true](../swift/true.md) 作为 `openInPlace:` 参数传入。

```swift
// Create an empty item provider.
let itemProvider = NSItemProvider()

// Add the URL to a file saved in the iCloud document container.
itemProvider
    .registerFileRepresentation(for: .utf8PlainText,
                                openInPlace: true) { completion in
    completion(url, true, nil)
    return nil
}
```

然后像第一个代码示例那样创建并显示活动视图控制器。这一次，共享面板会多出一个用于选择共享模式的弹出菜单。

![iPhone 屏幕快照：共享面板显示发送副本或协作的选项。](../../../attachments/682d707ab6b3aecbc599b65b4edf3bf6/media-4403933@2x.png)

### 启用 CloudKit 数据的拷贝与协作

由于 CloudKit 不以文件形式存储数据，共享副本与协作都需要不同的做法。要共享 CloudKit 数据的副本，你需要创建数据的一个可共享表示，然后用 [NSItemProvider](../foundation/nsitemprovider.md) 注册它。例如，如果你想把 App 的数据以 UTF-8 文本共享，可以用前面的例子为你的文本创建条目提供程序。

要启用协作，需在协作开始时创建一个 [CKShare](../cloudkit/ckshare.md)。你还需要你的 [CKContainer](../cloudkit/ckcontainer.md)，以及定义你授予协作者权限的 [CKAllowedSharingOptions](../cloudkit/ckallowedsharingoptions.md)。

```swift
// Create an item provider.
let itemProvider = NSItemProvider()

// Create and save a new share.
itemProvider.registerCKShare(container: container,
                             allowedSharingOptions: CKAllowedSharingOptions.standard) {
    
    // Create your share.
    let newShare = CKShare(rootRecord: recordToShare)
    
    // Configure the share, save it, and handle any errors here.
    
    // Return the newly saved share.
    return newShare
    
}
```

要邀请新的协作者加入已有共享，创建条目提供程序并注册该共享。

```swift
// Create an item provider.
let itemProvider = NSItemProvider()

// Register an existing share.
itemProvider
    .registerCKShare(
        savedShare,
        container: container,
        allowedSharingOptions: CKAllowedSharingOptions.standard
    )
```

关于 CloudKit 中协作的更多信息，参见 [Sharing CloudKit Data with Other iCloud Users](../cloudkit/sharing-cloudkit-data-with-other-icloud-users.md)。

### 限制共享模式

默认情况下，如果你的条目提供程序同时支持拷贝与协作，共享面板会显示一个弹出菜单，让用户选择共享模式。在 iOS 18 及更高版本中，你可以把共享限制为两者之一。

要限制共享模式，创建一个 [CollaborationModeRestriction](uiactivityviewcontroller/collaborationmoderestriction.md) 并赋给你的配置的元数据。可以通过配置的 [perItemMetadataProvider](uiactivityitemsconfiguration/peritemmetadataprovider.md) 属性访问该元数据。

```swift
// Iterate through the metadata keys.
configuration.perItemMetadataProvider = { _, key in
    switch key {
    case .collaborationModeRestrictions:
        // If it's the collaboration mode restriction key, return an array
        // containing a collaboration mode restriction object.
        let modeRestriction = UIActivityViewController.CollaborationModeRestriction(
            disabledMode: .collaborate
        )
        return [modeRestriction]
    default:
        return nil
    }
}
```

然后照旧创建并呈现共享面板。这样产生的共享面板只会显示被允许的共享模式。

![两张 iPhone 屏幕快照：左边是仅拷贝的共享面板，右边是仅协作的共享面板。](../../../attachments/cc4575a41189271b9024dab1a77f2fc3/media-4413126@2x.png)

另一种做法是同时显示两种共享选项，但在有人选择受限模式时显示警告框。警告框还可以包含恢复建议，帮助用户启用受限模式。

```swift
// Iterate through the metadata keys.
configuration.perItemMetadataProvider = { _, key in
    switch key {
    case .collaborationModeRestrictions:
        // Set the title and text for the alert. Optionally, you can set the title and provide
        // a launch URL for the recovery action.
        let modeRestriction = UIActivityViewController.CollaborationModeRestriction(
            disabledMode: .collaborate,
            alertTitle: "File Locked",
            alertMessage: "You need to unlock the file before you can share it for collaboration.",
            alertDismissButtonTitle: "Cancel",
            alertRecoverySuggestionButtonTitle: "Unlock",
            alertRecoverySuggestionButtonLaunch: unlockURL
        )
        return [modeRestriction]
    default:
        return nil
    }
}
```

这种情况下，共享面板显示弹出菜单，且已选中被允许的共享模式。当有人试图把共享模式改成受限模式时，系统会显示警告框。如果对方随后轻点恢复按钮，系统会调用你的场景委托的 [- scene:openURLContexts:](<uiscenedelegate/scene(__openurlcontexts_).md>) 方法，并传入你提供的 URL。关于使用启动 URL 的更多信息，参见[为你的 App 定义自定义 URL scheme](../xcode/defining-a-custom-url-scheme-for-your-app.md)。

### 指定共享对象

在 iOS 18 及更高版本中，你还可以为共享的数据指定接收者。为每个接收者创建一个 [INPerson](../intents/inperson.md) 实例，并把它们加到你的活动配置的元数据中。

```swift
// Gather data about the recipient.
var name = PersonNameComponents()
name.givenName = myBFF.givenName
name.familyName = myBFF.familyName

let displayName = myBFF.givenName
let email = myBFF.email
let image = INImage(imageData: myBFF.image)

// Create an `INPerson` instance for the recipient.
let recipient = INPerson(
    personHandle: .init(value: email, type: .emailAddress),
    nameComponents: name,
    displayName: displayName,
    image: image,
    contactIdentifier: nil,
    customIdentifier: nil)

// Iterate through the metadata keys.
configuration.perItemMetadataProvider = { _, key in
    switch key {
        // Set the share recipients to an array of `INPerson` instances.
    case .shareRecipients:
        return [recipient]
    default:
        return nil
    }
}
```

随后，共享面板会在接受接收者的 App（如邮件和信息）中自动填入接收者的数据。

![iPhone 屏幕快照：新邮件自动填入了接收者和内容。](../../../attachments/cdb4c2e0eb96422b41f468cb92dd3351/media-4413127@2x.png)

如果用户在共享面板中选择了另一个接收者，该选择会覆盖你指定的接收者。如果他们选择了不接受接收者的 App，系统会忽略你的接收者。

你还可以把活动视图控制器的 [excludedActivitySectionTypes](uiactivityviewcontroller/excludedactivitysectiontypes.md) 属性设为 [UIActivitySectionTypesPeopleSuggestions](uiactivitysectiontypes/peoplesuggestions.md)，从而在共享面板中隐藏其他建议的接收者。

```swift
// Hide the suggested recipients.
shareSheet.excludedActivitySectionTypes = .peopleSuggestions
```

## 另请参阅

### 活动界面

- [UIActivityViewController](uiactivityviewcontroller.md) — 用于从你的 App 提供标准服务的视图控制器。
- [UIActivityItemProvider](uiactivityitemprovider.md) — 传递给活动视图控制器的数据的代理。
- [UIActivityItemSource](uiactivityitemsource.md) — 活动视图控制器用来获取待处理数据条目的一组方法。
- [UIActivity](uiactivity.md) — 一个抽象类，通过子类化它来实现 App 专属的服务。
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md) — 为可共享内容提供来源的接口，用于满足用户共享当前内容的请求。
