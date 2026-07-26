---
title: 延长你的 App 的后台运行时间
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/extending-your-app-s-background-execution-time
source_url: 'https://developer.apple.com/documentation/uikit/extending-your-app-s-background-execution-time'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/extending-your-app-s-background-execution-time.json'
content_hash: 'sha256:79432873e44000fa'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Scenes](scenes.md) · [Preparing your UI to run in the background](preparing-your-ui-to-run-in-the-background.md)

# 延长你的 App 的后台运行时间

<sub>文章</sub>

确保关键任务在你的 App 进入后台时完成。

## 概述

延长 App 的后台运行时间可以确保你有足够的时间执行关键任务。对于需要更多后台时间的任务，请使用[后台任务](../backgroundtasks.md)。

当你的 App 进入后台时，系统会调用你的 App 委托的 [- applicationDidEnterBackground:](<uiapplicationdelegate/applicationdidenterbackground(__).md>) 方法。该方法有五秒钟的时间来执行任何任务并返回。该方法返回后不久，系统会将你的 App 置于挂起状态。对于大多数 App 来说，五秒钟足以执行任何关键任务，但如果你需要更多时间，可以请求 UIKit 延长 App 的运行时间。

你可以通过调用 [- beginBackgroundTaskWithName:expirationHandler:](<uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) 方法来延长 App 的运行时间。调用此方法可以为你提供额外的时间来执行重要任务。（你可以使用 [backgroundTimeRemaining](uiapplication/backgroundtimeremaining.md) 属性获知可用的最长后台时间。）任务完成后，请立即调用 [- endBackgroundTask:](<uiapplication/endbackgroundtask(__).md>) 方法，让系统知道你已经完成。如果你没有及时结束任务，系统会终止你的 App。

> [!note] 注意
> 不要等到你的 App 进入后台才调用 [- beginBackgroundTaskWithName:expirationHandler:](<uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) 方法。请在执行任何长时间运行的任务之前调用该方法。

以下代码展示了一个示例，它配置了一个后台任务，以便 App 可以将数据保存到其服务器，这可能耗时超过五秒。[- beginBackgroundTaskWithName:expirationHandler:](<uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) 方法会返回一个标识符，你必须保存该标识符并将其传给 [- endBackgroundTask:](<uiapplication/endbackgroundtask(__).md>) 方法。

```swift
func sendDataToServer(data: NSData) {
   // Perform the task on a background queue.
   DispatchQueue.global().async {
      // Request the task assertion and save the ID.
      self.backgroundTaskID = UIApplication.shared.
                 beginBackgroundTask(withName: "Finish Network Tasks") {
         // End the task if time expires.
         UIApplication.shared.endBackgroundTask(self.backgroundTaskID!)
         self.backgroundTaskID = UIBackgroundTaskInvalid
      }
            
      // Send the data synchronously.
      self.sendAppDataToServer(data: data)
            
      // End the task assertion.
      UIApplication.shared.endBackgroundTask(self.backgroundTaskID!)
      self.backgroundTaskID = UIBackgroundTaskInvalid
   }
}
```

> [!note] 注意
> [- beginBackgroundTaskWithName:expirationHandler:](<uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) 方法不能从 App 扩展中调用。要从你的 App 扩展请求额外的执行时间，请改为调用 [ProcessInfo](../foundation/processinfo.md) 的 [performExpiringActivity(withReason:using:)](<../foundation/processinfo/performexpiringactivity(withreason_using_).md>) 方法。

## 另请参阅

### 后台执行

- [使用后台任务更新你的 App](using-background-tasks-to-update-your-app.md) — 配置你的 App 在后台执行任务，以有效利用处理时间和电量。
- [关于后台执行序列](about-the-background-execution-sequence.md) — 了解你 App 进入后台时，自定义代码的执行顺序。
