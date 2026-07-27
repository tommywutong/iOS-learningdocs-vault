---
title: 在后台下载文件
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/downloading-files-in-the-background
source_url: 'https://developer.apple.com/documentation/foundation/downloading-files-in-the-background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/downloading-files-in-the-background.json'
content_hash: 'sha256:595325cb2429daed'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL 加载系统](url-loading-system.md)

# 在后台下载文件

<sub>文章</sub>

创建在 App 非活跃时下载文件的任务。

## 概述

对于耗时较长且不紧急的传输，可以创建在后台运行的任务。即使 App 被挂起，这些任务也会继续运行，使 App 在恢复运行后可以访问下载的文件。

> [!note] 注意
> 并非所有后台网络活动都必须使用本文所述的后台会话来完成。声明了适当后台模式的 App 可以像在前台时一样使用默认 URL 会话和数据任务。

### 配置后台会话

要执行后台下载，请配置 [URLSession](urlsession.md) 以在后台运行。以下示例演示此过程。

1. 使用 [URLSession](urlsession.md) 的类方法 [+ backgroundSessionConfigurationWithIdentifier:](<urlsessionconfiguration/background(withidentifier_).md>) 创建后台 [URLSessionConfiguration](urlsessionconfiguration.md) 对象，并提供一个在 App 内唯一的会话标识符。由于大多数 App 只需要少量后台会话（通常是一个），因此可以为标识符使用固定字符串，而不必使用动态生成的标识符。该标识符不需要全局唯一。
2. 为了让任务完成且 App 位于后台时系统唤醒 App，请确保 [sessionSendsLaunchEvents](urlsessionconfiguration/sessionsendslaunchevents.md) 属性设为 `true`（默认值）。
3. 对于对时间不敏感的任务，请启用 [discretionary](urlsessionconfiguration/isdiscretionary.md) 属性，使系统可以等待最佳条件再执行传输，例如设备接通电源或连接到 Wi-Fi 时。
4. 使用 [URLSessionConfiguration](urlsessionconfiguration.md) 实例创建 [URLSession](urlsession.md) 实例。提供一个委托（delegate），以接收后台传输事件。

创建后台 URL 会话

```swift
private lazy var urlSession: URLSession = {
    let config = URLSessionConfiguration.background(withIdentifier: "MySession")
    config.isDiscretionary = true
    config.sessionSendsLaunchEvents = true
    return URLSession(configuration: config, delegate: self, delegateQueue: nil)
}()
```

> [!note] 注意
> 要更详细地了解系统如何调度和执行后台任务，请从错误报告的 [Profiles and Logs](https://developer.apple.com/bug-reporting/profiles-and-logs/) 页面下载 Background Networking Profile 并安装到 iOS 设备上。

### 创建并调度下载任务

可以通过接受 URL 的 [- downloadTaskWithURL:](<urlsession/downloadtask(with_)-1onj.md>) 方法，或接受 [URLRequest](urlrequest.md) 实例的 [- downloadTaskWithRequest:](<urlsession/downloadtask(with_)-3fb7s.md>) 方法，从会话创建下载任务。请设置此任务的属性，帮助系统优化其行为。

1. 如以下示例所示，使用 [- downloadTaskWithURL:](<urlsession/downloadtask(with_)-1onj.md>) 创建下载任务。
2. 可以选择设置 [earliestBeginDate](urlsessiontask/earliestbegindate.md) 属性，将下载安排在未来的特定时间点开始。系统不保证下载恰好在此时开始，但不会提前开始。
3. 为帮助系统高效调度网络活动，请设置 [countOfBytesClientExpectsToSend](urlsessiontask/countofbytesclientexpectstosend.md) 和 [countOfBytesClientExpectsToReceive](urlsessiontask/countofbytesclientexpectstoreceive.md) 属性。这些值是预期字节数的最佳估计上限，应同时计入标头和正文数据。
4. 调用 [- resume](<urlsessiontask/resume().md>) 以启动任务。

在以下示例中，任务被设为至少一小时后开始，并配置为发送约 200 字节的数据和接收约 500 KB 的数据。

从 URL 会话创建下载任务

```swift
let backgroundTask = urlSession.downloadTask(with: url)
backgroundTask.earliestBeginDate = Date().addingTimeInterval(60 * 60)
backgroundTask.countOfBytesClientExpectsToSend = 200
backgroundTask.countOfBytesClientExpectsToReceive = 500 * 1024
backgroundTask.resume()
```

### 处理 App 挂起

不同的 App 状态会影响 App 与后台下载的交互方式。在 iOS 中，App 可能位于前台、被挂起，甚至被系统终止。有关这些状态的更多信息，请参阅[管理 App 生命周期](../uikit/managing-your-app-s-life-cycle.md)。

如果 App 位于后台，系统可能会在另一个进程执行下载时挂起 App。在这种情况下，下载完成时，系统会恢复 App 并调用 [UIApplicationDelegate](../uikit/uiapplicationdelegate.md) 的 [application(_:handleEventsForBackgroundURLSession:completionHandler:)](<../uikit/uiapplicationdelegate/application(__handleeventsforbackgroundurlsession_completionhandler_).md>) 方法。此方法的第二个参数是你在 `Creating a background URL session` 中创建的会话标识符。

此委托方法还会在最后一个参数中接收完成处理程序（completion handler）。请立即将此处理程序存储在适合 App 的位置，例如 App 委托（app delegate）的属性中，或实现 [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md) 的类中。在以下示例中，此完成处理程序存储在 App 委托名为 `backgroundCompletionHandler` 的属性中。

存储发送给 App 委托的后台下载完成处理程序

```swift
func application(_ application: UIApplication,
                 handleEventsForBackgroundURLSession identifier: String,
                 completionHandler: @escaping () -> Void) {
        backgroundCompletionHandler = completionHandler
}
```

传递完所有事件后，系统会调用 [URLSessionDelegate](urlsessiondelegate.md) 的 [- URLSessionDidFinishEventsForBackgroundURLSession:](<urlsessiondelegate/urlsessiondidfinishevents(forbackgroundurlsession_).md>) 方法。此时，请获取上一个示例中由 App 委托存储的 `backgroundCompletionHandler` 并执行它。以下示例展示此过程。

请注意，由于 [- URLSessionDidFinishEventsForBackgroundURLSession:](<urlsessiondelegate/urlsessiondidfinishevents(forbackgroundurlsession_).md>) 可能在辅助队列上调用，因此需要显式在主队列上执行该处理程序（它接收自 UIKit 方法）。

在主队列上执行后台 URL 会话的完成处理程序

```swift
func urlSessionDidFinishEvents(forBackgroundURLSession session: URLSession) {
    DispatchQueue.main.async {
        guard let appDelegate = UIApplication.shared.delegate as? AppDelegate,
            let backgroundCompletionHandler =
            appDelegate.backgroundCompletionHandler else {
                return
        }
        backgroundCompletionHandler()
    }
}
```

### 访问文件或将其移到永久位置

恢复运行的 App 调用完成处理程序后，下载任务会完成其工作，并调用委托的 [- URLSession:downloadTask:didFinishDownloadingToURL:](<urlsessiondownloaddelegate/urlsession(__downloadtask_didfinishdownloadingto_).md>) 方法。此时文件已完全下载，并且在委托方法返回前一直可用。如果只需读取一次，可以立即在临时位置访问该文件。如果想保留文件，请按照[从网站下载文件](downloading-files-from-websites.md)中的说明，将其移到 `Documents` 目录等永久位置。

### 如果 App 被终止，请重新创建会话

如果系统在 App 挂起期间将其终止，系统会在后台重新启动 App。在启动设置过程中，使用与之前相同的会话标识符重新创建后台会话（请参阅 `Creating a background URL session`），使系统能够将后台下载任务重新关联到你的会话。这样，无论 App 是由用户还是系统启动，后台会话都已准备就绪。App 重新启动后，事件序列与 App 被挂起后恢复运行时相同，如前文[处理 App 挂起](downloading-files-in-the-background.md#Handle-app-suspension)所述。

> [!note] 注意
> 如果传输在 App 位于后台时发起，会话配置的 [discretionary](urlsessionconfiguration/isdiscretionary.md) 属性会被视为 [true](../swift/true.md)。

### 遵守后台传输限制

使用后台会话时，实际传输由独立于 App 进程的另一个进程执行。由于重新启动 App 进程的开销较大，部分功能不可用，因此存在以下限制：

- 会话*必须*提供委托来传递事件。（对于上传和下载，委托的行为与进程内传输相同。）
- 仅支持 HTTP 和 HTTPS 协议（不支持自定义协议）。
- 系统始终遵循重定向。因此，即使实现了 [- URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:](<urlsessiontaskdelegate/urlsession(__task_willperformhttpredirection_newrequest_completionhandler_).md>)，也*不会*调用它。
- 仅支持从文件创建的上传任务（从数据实例或流进行的上传会在 App 退出后失败）。

### 高效使用后台会话

系统恢复或重新启动 App 时，会使用速率限制器来防止滥用后台下载。App 在后台启动新下载任务时，该任务会等到延迟期结束后才开始。系统每次恢复或重新启动 App 时，延迟都会增加。

因此，如果 App 启动单个后台下载，在下载完成时恢复运行，然后再启动一个新下载，延迟将大幅增加。请改用少量后台会话（最好只有一个），并使用这些会话一次启动多个下载任务。这样，系统可以同时执行多项下载，并在它们完成后恢复 App。

不过，请记住每个任务都有自己的开销。如果发现需要启动数千个下载任务，请更改设计，改为执行数量更少、规模更大的传输。

> [!note] 注意
> 用户每次将 App 带到前台时，延迟都会重置为 0。如果延迟期已结束而系统未恢复或重新启动 App，延迟也会重置。

## 另请参阅

### 下载

- [从网站下载文件](downloading-files-from-websites.md) — 将文件直接下载到文件系统。
- [暂停和恢复下载](pausing-and-resuming-downloads.md) — 允许用户恢复下载，而不必从头开始。
