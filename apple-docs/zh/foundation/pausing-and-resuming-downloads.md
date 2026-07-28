---
title: 暂停和恢复下载
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/pausing-and-resuming-downloads
source_url: 'https://developer.apple.com/documentation/foundation/pausing-and-resuming-downloads'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/pausing-and-resuming-downloads.json'
content_hash: 'sha256:3448b291af38a406'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [URL 加载系统](url-loading-system.md)

# 暂停和恢复下载

<sub>文章</sub>

让用户无需从头开始即可恢复下载。

## 概述

你的 App 或用户可能需要取消正在进行的下载，并在稍后恢复。通过支持可恢复下载，你可以同时节省用户的时间和网络带宽。

你还可以使用此技术来恢复因连接暂时中断而失败的下载。

### 取消下载时存储恢复数据对象

你可以调用 [- cancelByProducingResumeData:](<urlsessiondownloadtask/cancel(byproducingresumedata_).md>) 来取消 [URLSessionDownloadTask](urlsessiondownloadtask.md)。该方法接受一个完成处理程序（completion handler），并在取消完成后调用它。完成处理程序接收 `resumeData` 参数。如果该参数不为 `nil`，它就是你稍后用来恢复下载的令牌。以下示例展示如何取消下载任务，并在 `resumeData` 存在时将其存入属性。

取消下载时存储恢复数据

```swift
downloadTask.cancel { resumeDataOrNil in
    guard let resumeData = resumeDataOrNil else { 
      // 下载无法恢复；必要时将其从 UI 中移除
      return
    }
    self.resumeData = resumeData
}

```

> [!important] 重要
> 并非所有下载都可以恢复。有关下载可恢复所必须满足的条件列表，请参阅 [- cancelByProducingResumeData:](<urlsessiondownloadtask/cancel(byproducingresumedata_).md>) 中的讨论。此外，使用后台配置的下载会自动处理恢复，因此只有非后台下载才需要手动恢复。

### 下载失败时存储恢复数据对象

你也可以恢复因连接暂时中断而失败的下载，例如用户走出 Wi-Fi 覆盖范围时。

下载失败时，会话会调用委托（delegate）的 [- URLSession:task:didCompleteWithError:](<urlsessiontaskdelegate/urlsession(__task_didcompletewitherror_).md>) 方法。如果 `error` 不为 `nil`，请在其 `userInfo` 字典中查找 [NSURLSessionDownloadTaskResumeData](nsurlsessiondownloadtaskresumedata.md) 键。如果该键存在，请保存其关联值，供稍后尝试恢复下载时使用。如果该键不存在，则下载无法恢复。

以下示例展示了 [- URLSession:task:didCompleteWithError:](<urlsessiontaskdelegate/urlsession(__task_didcompletewitherror_).md>) 的一种实现，它会从错误中获取并保存 `resumeData` 对象（如果存在）。

```swift
func urlSession(_ session: URLSession, task: URLSessionTask, didCompleteWithError error: Error?) {
    guard let error = error else {
        // 处理成功情况。
        return
    }
    let userInfo = (error as NSError).userInfo
    if let resumeData = userInfo[NSURLSessionDownloadTaskResumeData] as? Data {
        self.resumeData = resumeData
    } 
    // 执行其他错误处理。
}

```

### 使用存储的恢复数据对象恢复下载

在适合恢复下载时，使用 [URLSession](urlsession.md) 的 [- downloadTaskWithResumeData:](<urlsession/downloadtask(withresumedata_).md>) 或 [- downloadTaskWithResumeData:completionHandler:](<urlsession/downloadtask(withresumedata_completionhandler_).md>) 方法创建新的 [URLSessionDownloadTask](urlsessiondownloadtask.md)，并传入先前存储的 `resumeData` 对象。然后对该任务调用 [- resume](<urlsessiontask/resume().md>) 以恢复下载。

根据恢复数据创建并启动下载任务

```swift
guard let resumeData = resumeData else {
    // 告知用户下载无法恢复
    return
}
let downloadTask = urlSession.downloadTask(withResumeData: resumeData)
downloadTask.resume()
self.downloadTask = downloadTask

```

如果下载成功恢复，任务会调用委托的 [- URLSession:downloadTask:didResumeAtOffset:expectedTotalBytes:](<urlsessiondownloaddelegate/urlsession(__downloadtask_didresumeatoffset_expectedtotalbytes_).md>) 方法。你可以使用偏移量和字节数参数告知用户下载已恢复，并保留了之前的进度。

## 另请参阅

### 下载

- [从网站下载文件](downloading-files-from-websites.md) — 将文件直接下载到文件系统。
- [在后台下载文件](downloading-files-in-the-background.md) — 创建在 App 不活跃时下载文件的任务。
