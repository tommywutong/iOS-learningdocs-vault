---
title: Extending your app’s background execution time
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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Scenes](scenes.md) · [Preparing your UI to run in the background](preparing-your-ui-to-run-in-the-background.md)

# Extending your app’s background execution time

<sub>Article</sub>

Ensure that critical tasks finish when your app moves to the background.

## Overview

Extending your app’s background execution time ensures that you have adequate time to perform critical tasks. For tasks that require more background time, use [Background Tasks](../backgroundtasks.md).

When your app moves to the background, the system calls your app delegate’s [- applicationDidEnterBackground:](<uiapplicationdelegate/applicationdidenterbackground(__).md>) method. That method has five seconds to perform any tasks and return. Shortly after that method returns, the system puts your app into the suspended state. For most apps, five seconds is enough to perform any crucial tasks, but if you need more time, you can ask UIKit to extend your app’s runtime.

You extend your app’s runtime by calling the [- beginBackgroundTaskWithName:expirationHandler:](<uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) method. Calling this method gives you extra time to perform important tasks. (You can find out the maximum background time available using the [backgroundTimeRemaining](uiapplication/backgroundtimeremaining.md) property.) When you finish your tasks, call the [- endBackgroundTask:](<uiapplication/endbackgroundtask(__).md>) method right away to let the system know that you’re done. If you don’t end your tasks in a timely manner, the system terminates your app.

> [!note] Note
> Don’t wait until your app moves to the background to call the [- beginBackgroundTaskWithName:expirationHandler:](<uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) method. Call the method before performing any long-running task.

The following code shows an example that configures a background task so that the app may save data to its server, which could take longer than five seconds. The [- beginBackgroundTaskWithName:expirationHandler:](<uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) method returns an identifier that you must save and pass to the [- endBackgroundTask:](<uiapplication/endbackgroundtask(__).md>) method.

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

> [!note] Note
> The [- beginBackgroundTaskWithName:expirationHandler:](<uiapplication/beginbackgroundtask(withname_expirationhandler_).md>) method can’t be called from an app extension. To request extra execution time from your app extension, call the [performExpiringActivity(withReason:using:)](<../foundation/processinfo/performexpiringactivity(withreason_using_).md>) method of [ProcessInfo](../foundation/processinfo.md) instead.

## See Also

### Background execution

- [Using background tasks to update your app](using-background-tasks-to-update-your-app.md) — Configure your app to perform tasks in the background to make efficient use of processing time and power.
- [About the background execution sequence](about-the-background-execution-sequence.md) — Learn the order in which your custom code is executed when your app moves to the background.
