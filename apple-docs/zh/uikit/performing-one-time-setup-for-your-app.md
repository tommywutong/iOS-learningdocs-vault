---
title: 为你的 App 执行一次性设置
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/performing-one-time-setup-for-your-app
source_url: 'https://developer.apple.com/documentation/uikit/performing-one-time-setup-for-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/performing-one-time-setup-for-your-app.json'
content_hash: 'sha256:94eab4899f7adadf'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Responding to the launch of your app](responding-to-the-launch-of-your-app.md)

# 为你的 App 执行一次性设置

<sub>文章</sub>

确保你 App 环境的正确配置。

## 概述

当用户首次启动你的 App 时，你可能想通过执行一些一次性任务来准备好你的 App 环境。例如，你可能想要：

- 从你的服务器下载所需的数据。
- 把文稿模板或可修改的数据文件从你的 App bundle 复制到一个可写目录中。
- 为用户配置默认偏好设置。
- 设置用户账户或收集其他所需的数据。

请在你的 App 委托的 [- application:willFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) 或 [- application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) 方法中执行任何一次性任务。对于不需要用户输入的任务，切勿阻塞 App 的主线程。相反，应使用调度队列异步启动任务，让它们在你的 App 完成启动的同时在后台运行。对于需要用户输入的任务，请在 [- application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) 方法中对你的用户界面进行所有更改。

### 把文件安装在正确的位置

你的 App 有自己的容器目录用于存储文件，你应当始终把特定于该 App 的文件放在 `~/Library` 子目录下。具体来说，请把你的文件存放在下面这些 `~/Library` 子目录中：

- `~/Library/Application Support/` — 存放你希望随用户其他内容一起备份的、特定于该 App 的文件。（你可以按需在此创建自定的子目录。）把这个目录用于数据文件、配置文件、文稿模板等。
- `~/Library/Caches/` — 存放可以轻松重新生成或重新下载的临时数据文件。

要获取你 App 容器中某个目录的 URL，请使用 [FileManager](../foundation/filemanager.md) 的 [urls(for:in:)](<../foundation/filemanager/urls(for_in_).md>) 方法。

```swift
let appSupportURL = FileManager.default.urls(for: 
      .applicationSupportDirectory, in: .userDomainMask)

let cachesURL = FileManager.default.urls(for: 
      .cachesDirectory, in: .userDomainMask)
```

请把任何临时文件放在你 App 的 `tmp/` 目录中。临时文件可能包括你打算在其内容被提取并安装到别处之后就删除的压缩文件。使用 [FileManager](../foundation/filemanager.md) 的 [temporaryDirectory](../foundation/filemanager/temporarydirectory.md) 方法获取你 App 临时目录的 URL。

## 另请参阅

### Launch time

- [About the app launch sequence](about-the-app-launch-sequence.md) — 了解系统在 App 启动时执行你的代码的顺序。
- [Preserving your app's UI across launches](preserving-your-app-s-ui-across-launches.md) — 在系统终止你的 App 之后，让它恢复到之前的状态。
