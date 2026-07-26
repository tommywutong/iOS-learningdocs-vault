---
title: 'iOS Apps: Disable the Sleep Timer for Long-Running Tasks'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/02/ios-apps-disable-sleep-timer-long-running-tasks/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:958287a53d941ef1'
translated: false
---

> 原文：[iOS Apps: Disable the Sleep Timer for Long-Running Tasks](https://oleb.net/blog/2013/02/ios-apps-disable-sleep-timer-long-running-tasks/)　·　Ole Begemann

# iOS Apps: Disable the Sleep Timer for Long-Running Tasks

Here’s a UX idea that [I tweeted about a while ago](https://twitter.com/olebegemann/status/276840116373299200): iOS apps that perform potentially long-running tasks (10+ minutes) should give the user the option to disable the device’s sleep timer.

As an example, let’s look at a long list of downloads such as you might encounter in your favorite podcast app when it downloads new episodes. As soon as the download starts, an on-off switch should appear on the app’s download status screen to let the user choose to prevent the device from entering sleep mode (on) or set the standard behavior where the device goes to sleep after a few minutes (off).

By default, this switch should be in its on position, indicating that the device will not go to sleep during the download process. That way, the user can put the device aside and be sure that the download will finish without any further action on his part.

# UIBackgroundTask Limited To 10 Minutes

“Now isn’t this what [Apple’s background task API](http://developer.apple.com/library/ios/documentation/iphone/conceptual/iphoneosprogrammingguide/ManagingYourApplicationsFlow/ManagingYourApplicationsFlow.html#//apple_ref/doc/uid/TP40007072-CH4-SW28) is for?”, you might object. Well, not really. Of course, both background execution and this concept can be used to extend the time an app can run without user interaction, but they have different constraints. My idea does not replace background tasks, it complements them.

With the background task API, iOS allows apps to finish time-consuming tasks even though they have been sent to the background, where apps are normally suspended and cannot execute any code. The podcast app in our example can make use of the API to continue downloading after the device went to sleep. There is one important restriction, though. The operating system limits the maximum amount of time it gives to any app to finish their background tasks. Currently, this limit is 10 minutes. If the downloads are not finished by then, the app has no choice but to pause them and wait for the user to reactivate the app.

So background task execution is not a perfect option if a task can potentially take more than 10+ minutes to complete and it should be possible to finish when unattended (without any user interaction). In this situation, giving the user the contextual control over the sleep timer could be an option for your app.

# DocSets

As a demonstration of my idea, I implemented it in Ole Zorn’s awesome [DocSets app](https://github.com/omz/DocSets-for-iOS). The process of downloading and extracting doc sets can easily take longer than 10 minutes, especially if you are on a slow connection or if you want to download multiple sets at once.

![The DocSets app showing the switch to disable the sleep timer during a download](https://oleb.net/media/docsets-screenshot-idle-timer-toolbar.png)

<sub>The DocSets app showing the toolbar that lets the user disable the sleep timer when a long-running download is in progress.</sub>

Here’s how the feature works in detail:

- As soon you start a doc set download from the Downloads screen, the `DocSetDownloadManager` class disables the sleep timer by calling `[[UIApplication sharedApplication] setIdleTimerDisabled:YES]`. It also informs the `DownloadViewController` about this event by posting a notification.
- When the view controller receives the notification, it animates a toolbar into view. The toolbar contains the switch that allows the user to override the automatic sleep timer management. The user can now put the device aside and wait for the download process to finish.
- If the user toggles the switch because he does not want the device to override the sleep timer, the view controller informs the download manager, which in turn re-enables the timer. The operating system will also re-enable the default behavior when the user manually leaves the app to do something else. In both cases, DocSets uses the background task API to continue the download in the background.
- When all downloads have finished, the download manager re-enables the sleep timer and informs the view controller, which in turn animates the toolbar off screen.

# Even Better: No Exposure in the UI

**Update February 8, 2013:** Having thought about this feature even more (and having received [some feedback on Twitter](https://twitter.com/luka_bernardi/status/299608876943302656)), I am more and more in favor of not exposing it in the UI at all.

Apps should just silently disable the sleep timer when a long download process starts and re-enable it when it ends. Showing the user a control to disable this behavior can easily be more confusing than helpful. And if the user does want to get his device to sleep, he still has the option of locking it manually or pressing the home button, which will send the app to the background and re-enable the sleep timer automatically.

If an app wants to show anything to the user, a small message that the sleep timer has been disabled during the download should suffice. There is no need to give him control to re-enable it.
