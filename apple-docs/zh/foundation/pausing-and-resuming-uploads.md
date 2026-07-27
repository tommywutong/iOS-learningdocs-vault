---
title: 暂停和恢复上传
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/pausing-and-resuming-uploads
source_url: 'https://developer.apple.com/documentation/foundation/pausing-and-resuming-uploads'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/pausing-and-resuming-uploads.json'
content_hash: 'sha256:02d5d72303edf53d'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [URL 加载系统](url-loading-system.md)

# 暂停和恢复上传

<sub>文章</sub>

无需从头开始即可暂停和恢复上传，即使连接中断也不例外。

## 概述

你的 App 或使用它的人可能需要取消正在进行的上传，并在稍后恢复。通过支持可恢复上传，你可以同时节省用户的时间和网络带宽。

从 iOS 17 及对应版本的操作系统开始，[URLSession](urlsession.md) 根据[最新的可恢复上传协议草案](https://www.ietf.org/archive/id/draft-ietf-httpbis-resumable-upload-01.txt)支持可恢复上传。该协议目前由 IETF 的 HTTP 工作组开发。要使用可恢复上传，你连接的服务器也必须支持此协议。

你可以使用此技术手动暂停和恢复上传，甚至恢复因连接暂时中断而失败的上传。在这两种情况下，[URLSession](urlsession.md) 都需要有关如何恢复上传的信息，这些信息存储在 `resumeData` 对象中。

### 暂停上传

你可以调用 [- cancelByProducingResumeData:](<urlsessiondownloadtask/cancel(byproducingresumedata_).md>) 来有效暂停 [URLSessionUploadTask](urlsessionuploadtask.md)。该方法会取消任务，并将 `resumeData` 参数传给其完成处理程序（completion handler）。如果 `resumeData` 不为 `nil`，你可以稍后使用此令牌恢复上传。下面的代码清单展示如何取消上传任务，并在 `resumeData` 存在时将其存入属性：

```swift
uploadTask.cancel { resumeData in
    guard let resumeData else { 
      // 上传无法恢复；必要时从 UI 中移除该上传。
      return
    }
    self.resumeData = resumeData
}
```

> [!important] 重要
> 并非所有上传都可以恢复。服务器必须支持 IETF 的 HTTP 工作组发布的[最新可恢复上传协议草案](https://www.ietf.org/archive/id/draft-ietf-httpbis-resumable-upload-01.txt)。此外，使用后台配置的上传会自动处理恢复，因此只有非后台上传才需要手动恢复。

### 恢复失败的上传

如果网络只发生短暂中断，但服务器仍可访问，[URLSession](urlsession.md) 会自动尝试为你恢复上传，无需额外代码。

对于更大范围的连接中断，你可以在任务错误中检查恢复数据，以恢复失败的上传。

上传失败时，会话会调用委托（delegate）的 [- URLSession:task:didCompleteWithError:](<urlsessiontaskdelegate/urlsession(__task_didcompletewitherror_).md>) 方法。如果 `error` 不为 `nil`，请在其 `userInfo` 字典中查找 [NSURLSessionUploadTaskResumeData](nsurlsessionuploadtaskresumedata.md) 键。如果该键存在，请保存其关联值，供稍后尝试恢复上传时使用。如果该键不存在，则无法恢复上传。

你可以使用 [URLError](urlerror.md) 的 [uploadTaskResumeData](urlerror/uploadtaskresumedata.md) 属性方便地访问恢复数据。

你也可以捕获 [upload(for:fromFile:)](<urlsession/upload(for_fromfile_).md>) 等异步 [URLSession](urlsession.md) 上传方法产生的错误。下面的代码清单展示了检查错误中恢复数据的一种错误处理实现：

```swift
do {
    let (data, response) = try await session.upload(for: request, fromFile: fileURL)
} catch let error as URLError {
    guard let resumeData = error.uploadTaskResumeData else {
        // 上传无法恢复。
        return
    }
    self.resumeData = resumeData
}
```

### 恢复上传

在适合恢复上传时，使用 [URLSession](urlsession.md) 的 [- uploadTaskWithResumeData:](<urlsession/uploadtask(withresumedata_).md>) 方法创建新的 [URLSessionUploadTask](urlsessionuploadtask.md)，并传入先前存储的 `resumeData` 对象。然后对该任务调用 [- resume](<urlsessiontask/resume().md>) 以恢复上传：

```swift
guard let resumeData = self.resumeData else {
    // 告知用户上传无法恢复。
    return
}

let uploadTask = session.uploadTask(withResumeData: resumeData)
uploadTask.resume()
self.uploadTask = uploadTask
```

## 另请参阅

### 上传

- [使用 SwiftNIO 构建可恢复上传服务器](building-a-resumable-upload-server-with-swiftnio.md) — 通过将可恢复上传转换为常规上传，在 SwiftNIO 中支持 HTTP 可恢复上传协议。
- [向网站上传数据](uploading-data-to-a-website.md) — 从你的 App 向服务器发布数据。
- [上传数据流](uploading-streams-of-data.md) — 向服务器发送数据流。
