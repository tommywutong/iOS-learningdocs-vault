---
title: 将数据上传到网站
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/uploading-data-to-a-website
source_url: 'https://developer.apple.com/documentation/foundation/uploading-data-to-a-website'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/uploading-data-to-a-website.json'
content_hash: 'sha256:2bc676e599c7da60'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md)

# 将数据上传到网站

<sub>文章</sub>

从你的 App 向服务器发布数据。

## 概述

许多 App 使用的服务器接受图像或文档等文件的上传，或使用接受 JSON 等结构化数据的 Web 服务 API 端点。要从你的 App 上传数据，你使用一个 [URLSession](urlsession.md) 实例来创建 [URLSessionUploadTask](urlsessionuploadtask.md) 实例。上传任务使用一个 [URLRequest](urlrequest.md) 实例，其中详细说明上传的执行方式。

### 准备要上传的数据

要上传的数据可以是文件内容、流或数据，如下例所示。

许多 Web 服务端点接受 JSON 格式的数据，你可以通过对数组、字典等 [Encodable](../swift/encodable.md) 类型使用 [JSONEncoder](jsonencoder.md) 类来创建这类数据。如下例所示，你可以声明一个符合 [Codable](../swift/codable.md) 的结构体，创建此类型的实例，并使用 [JSONEncoder](jsonencoder.md) 将该实例编码为要上传的 JSON 数据。

Preparing JSON data for upload

```swift
struct Order: Codable {
    let customerId: String
    let items: [String]
}

// ...

let order = Order(customerId: "12345",
                  items: ["Cheese pizza", "Diet soda"])
guard let uploadData = try? JSONEncoder().encode(order) else {
    return
}
```

还有许多其他方式可以创建数据实例，例如将图像编码为 JPEG 或 PNG 数据，或使用 UTF-8 等编码将字符串转换为数据。

### 配置上传请求

上传任务需要一个 [URLRequest](urlrequest.md) 实例。如下例所示，根据服务器支持和期望的情况，将请求的 [httpMethod](urlrequest/httpmethod.md) 属性设置为 `"``POST``"` 或 `"PUT"`。使用 [setValue(_:forHTTPHeaderField:)](<urlrequest/setvalue(__forhttpheaderfield_).md>) 方法设置你要提供的任何 HTTP 头部的值，但 `Content-Length` 头部除外。会话会根据你的数据大小自动算出内容长度。

配置 URL 请求

```swift
let url = URL(string: "https://example.com/post")!
var request = URLRequest(url: url)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
```

### 创建并启动上传任务

要开始上传，请在 [URLSession](urlsession.md) 实例上调用 [- uploadTaskWithRequest:fromData:completionHandler:](<urlsession/uploadtask(with_from_completionhandler_).md>) 创建一个上传用的 [URLSessionTask](urlsessiontask.md) 实例，传入你之前设置好的请求和数据实例。由于任务以挂起状态启动，你需要通过调用任务的 [- resume](<urlsessiontask/resume().md>) 来开始网络加载过程。下面的示例使用共享的 `URLSession` 实例，并在完成处理程序中接收结果。该处理程序在使用任何返回的数据之前，会先检查传输错误和服务器错误。

启动上传任务

```swift
let task = URLSession.shared.uploadTask(with: request, from: uploadData) { data, response, error in
    if let error = error {
        print ("error: \(error)")
        return
    }
    guard let response = response as? HTTPURLResponse,
        (200...299).contains(response.statusCode) else {
        print ("server error")
        return
    }
    if let mimeType = response.mimeType,
        mimeType == "application/json",
        let data = data,
        let dataString = String(data: data, encoding: .utf8) {
        print ("got data: \(dataString)")
    }
}
task.resume()
```

### 或者，通过设置委托来上传

作为完成处理程序方式的替代，你可以在自己配置的会话上设置委托，然后使用 [- uploadTaskWithRequest:fromData:](<urlsession/uploadtask(with_from_).md>) 创建上传任务。在这种情况下，你需要实现 [URLSessionDelegate](urlsessiondelegate.md) 和 [URLSessionTaskDelegate](urlsessiontaskdelegate.md) 协议中的方法。这些方法接收服务器响应以及任何数据或传输错误。

## 另请参阅

### 上传

- [Building a resumable upload server with SwiftNIO](building-a-resumable-upload-server-with-swiftnio.md) — 通过将可恢复上传转换为常规上传，在 SwiftNIO 中支持 HTTP 可恢复上传协议。
- [Uploading streams of data](uploading-streams-of-data.md) — 向服务器发送数据流。
- [Pausing and resuming uploads](pausing-and-resuming-uploads.md) — 暂停并恢复上传而无需重新开始，即使连接中断也不例外。
