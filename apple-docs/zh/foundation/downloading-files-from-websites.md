---
title: 从网站下载文件
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/downloading-files-from-websites
source_url: 'https://developer.apple.com/documentation/foundation/downloading-files-from-websites'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/downloading-files-from-websites.json'
content_hash: 'sha256:f4f3664515fedf8b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL 加载系统](url-loading-system.md)

# 从网站下载文件

<sub>文章</sub>

将文件直接下载到文件系统。

## 概述

对于已经以文件形式存储的网络资源（例如图像和文稿），可以使用下载任务将这些项目直接获取到本地文件系统。

> [!tip] 提示
> 你还可以配置下载任务，使其在 App 于后台挂起或终止时继续运行。有关详细信息，请参阅[在后台下载文件](downloading-files-in-the-background.md)。

### 对于简单下载，使用完成处理程序

要下载文件，请从 [URLSession](urlsession.md) 创建 [URLSessionDownloadTask](urlsessiondownloadtask.md)。如果不需要在下载期间接收进度更新或其他委托（delegate）回调，可以使用完成处理程序（completion handler）。无论下载成功结束还是下载失败，任务都会在下载结束时调用完成处理程序。

完成处理程序可能收到客户端错误，这表示存在无法连接网络等本地问题。如果没有客户端错误，你还会收到 [URLResponse](urlresponse.md)，应检查它是否表示服务器成功响应。

如果下载成功，完成处理程序会收到一个 URL，指明所下载文件在本地文件系统中的位置。此存储位置是临时的。如果想保留文件，返回完成处理程序之前*必须*从此位置复制或移动该文件。

以下示例展示如何创建带有完成处理程序的简单下载任务。如果未指明任何错误，完成处理程序会将下载的文件移到 App 的 `Documents` 目录。调用 [- resume](<urlsessiontask/resume().md>) 以启动任务。

创建带有完成处理程序的下载任务

```swift
let downloadTask = URLSession.shared.downloadTask(with: url) {
    urlOrNil, responseOrNil, errorOrNil in
    // 检查并处理错误：
    // * errorOrNil 应为 nil
    // * responseOrNil 应为 statusCode 在 200..<299 范围内的 HTTPURLResponse
    
    guard let fileURL = urlOrNil else { return }
    do {
        let documentsURL = try
            FileManager.default.url(for: .documentDirectory,
                                    in: .userDomainMask,
                                    appropriateFor: nil,
                                    create: false)
        let savedURL = documentsURL.appendingPathComponent(fileURL.lastPathComponent)
        try FileManager.default.moveItem(at: fileURL, to: savedURL)
    } catch {
        print ("file error: \(error)")
    }
}
downloadTask.resume()

```

> [!tip] 提示
> 上一个示例使用 [- downloadTaskWithURL:](<urlsession/downloadtask(with_)-1onj.md>) 创建下载任务，该方法只接受一个 [URL](url.md) 参数。如果需要自定义发送给服务器的请求，请使用 [- downloadTaskWithRequest:](<urlsession/downloadtask(with_)-3fb7s.md>) 创建任务，并传入自定义的 [URLRequest](urlrequest.md)。

### 要接收进度更新，请使用委托

如果想在下载进行时接收进度更新，必须使用委托。此时不会在完成处理程序中接收结果，而是通过你实现的 [URLSessionTaskDelegate](urlsessiontaskdelegate.md) 和 [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md) 协议方法接收回调。

创建自己的 [URLSession](urlsession.md) 实例，并设置其 `delegate` 属性。以下示例展示一个延迟实例化的 `urlSession` 属性，它将 `self` 设为自身的委托。

创建带有委托的 URL 会话

```swift
private lazy var urlSession = URLSession(configuration: .default,
                                         delegate: self,
                                         delegateQueue: nil)

```

要开始下载，请使用此 [URLSession](urlsession.md) 创建 [URLSessionDownloadTask](urlsessiondownloadtask.md)，然后调用 [- resume](<urlsessiontask/resume().md>) 启动任务，如以下示例所示。

创建并启动使用委托的下载任务

```swift
private func startDownload(url: URL) {
    let downloadTask = urlSession.downloadTask(with: url)
    downloadTask.resume()
    self.downloadTask = downloadTask
}

```

### 接收进度更新

下载开始后，你会在 [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md) 的 [- URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:](<urlsessiondownloaddelegate/urlsession(__downloadtask_didwritedata_totalbyteswritten_totalbytesexpectedtowrite_).md>) 方法中定期收到进度更新。可以使用此回调提供的字节数更新 App 中的进度 UI。

以下示例展示此回调方法的实现。该实现计算下载进度比例，并用它更新一个以百分比显示进度的标签。由于回调在未知的 Grand Central Dispatch 队列上执行，因此*必须*显式在主队列上执行 UI 更新。

使用委托方法更新 UI 中的下载进度

```swift
func urlSession(_ session: URLSession,
                downloadTask: URLSessionDownloadTask,
                didWriteData bytesWritten: Int64,
                totalBytesWritten: Int64,
                totalBytesExpectedToWrite: Int64) {
     if downloadTask == self.downloadTask {
        let calculatedProgress = Float(totalBytesWritten) / Float(totalBytesExpectedToWrite)
        DispatchQueue.main.async {
            self.progressLabel.text = self.percentFormatter.string(from:
                NSNumber(value: calculatedProgress))
        }
    }
}
```

> [!tip] 提示
> 如果下载期间唯一需要执行的 UI 更新是更新 [UIProgressView](../uikit/uiprogressview.md)，请使用任务的 [progress](urlsessiontask/progress.md) 属性，而不要自行计算进度。此属性是 [Progress](progress.md) 的实例；创建任务时，可以将它赋给 [UIProgressView](../uikit/uiprogressview.md) 的 [observedProgress](../uikit/uiprogressview/observedprogress.md) 属性，以自动更新进度视图。

### 在委托中处理下载完成或错误

使用委托而不是完成处理程序时，请通过实现 [- URLSession:downloadTask:didFinishDownloadingToURL:](<urlsessiondownloaddelegate/urlsession(__downloadtask_didfinishdownloadingto_).md>) 来处理下载完成。检查 `downloadTask` 的 [response](urlsessiontask/response.md) 属性，确保服务器响应表示成功。如果成功，`location` 参数会提供存储文件的本地 URL。此位置仅在回调结束前有效。这意味着从回调方法返回之前，*必须*立即读取文件，或将其移到 App 的 `Documents` 目录等其他位置。以下示例展示如何保留下载的文件。

在委托回调中存储下载的文件

```swift
func urlSession(_ session: URLSession,
                downloadTask: URLSessionDownloadTask,
                didFinishDownloadingTo location: URL) {
    // 检查并处理错误：
    // * downloadTask.response 应为 statusCode 在 200..<299 范围内的 HTTPURLResponse

    do {
        let documentsURL = try
            FileManager.default.url(for: .documentDirectory,
                                    in: .userDomainMask,
                                    appropriateFor: nil,
                                    create: false)
        let savedURL = documentsURL.appendingPathComponent(
            location.lastPathComponent)
        try FileManager.default.moveItem(at: location, to: savedURL)
    } catch {
        // 处理文件系统错误
    }
}

```

如果发生客户端错误，委托会在 [- URLSession:task:didCompleteWithError:](<urlsessiontaskdelegate/urlsession(__task_didcompletewitherror_).md>) 委托方法的回调中收到该错误。另一方面，如果下载成功完成，则会在 [- URLSession:downloadTask:didFinishDownloadingToURL:](<urlsessiondownloaddelegate/urlsession(__downloadtask_didfinishdownloadingto_).md>) 之后调用此方法，并且错误为 `nil`。

## 另请参阅

### 下载

- [暂停和恢复下载](pausing-and-resuming-downloads.md) — 允许用户恢复下载，而不必从头开始。
- [在后台下载文件](downloading-files-in-the-background.md) — 创建在 App 非活跃时下载文件的任务。
