---
title: How to Debug an App That Was Launched by Push Notification or URL Handler
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/05/how-to-debug-app-launched-by-remote-event/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e4e0ab9c13fbc1d5'
translated: false
---

> 原文：[How to Debug an App That Was Launched by Push Notification or URL Handler](https://oleb.net/blog/2010/05/how-to-debug-app-launched-by-remote-event/)　·　Ole Begemann

# How to Debug an App That Was Launched by Push Notification or URL Handler

I’ve been fairly active on [Stack Overflow](http://stackoverflow.com/) lately. To date, I have [answered 315 questions](http://stackoverflow.com/users/116862/ole-begemann) there and while I haven’t asked any questions myself, I have profited immensely from the knowledge others have shared there. It is truly a great site, so much better than most programming forums. I think many questions that I have answered might also be interesting to you and so I thought I’d share some of the more interesting ones (and the answers, of course) here, perhaps with a little more detail than on SO.

Let’s start with this one: [How can I debug an app that was started by an external event such as a push notification or a URL handler?](http://stackoverflow.com/questions/454188/how-do-you-debug-your-application-if-they-got-started-using-a-custom-url-scheme/) You don’t click on Build and Debug in these cases, so how do we get the debugger to notice? You have two options here:

# 1. Use NSLog statements and inspect them in Console.app

The output of your `NSLog()` calls not only show up in the Debugger Console in Xcode but also in the system logs. To look up the logs for the simulator (useful for testing a custom URL scheme), open Console.app in OS X, select Console Messages in the left pane and then search for the name of your app in the Filter field. To see the Console messages on the device (e.g. to test how your app handles an incoming push notification), open the Organizer in Xcode, select your device and switch to the Console app before your app gets launched.

# 2. Ask the debugger to wait for your app to launch

Sometimes, `NSLog()` is just not enough and you want the full power of the debugger. No problem:

1. Set a breakpoint where you want it, for example in `application:didFinishLaunchingWithOptions:`.
2. Select Project \> Edit Active Executable. On the Debugging tab, select the Wait for next launch/push notification checkbox:

  ![Xcode Active Executable Settings: Debugging, wait for next launch](https://oleb.net/media/xcode-active-executable-debugging-wait-for-next-launch.png)
3. Build and Debug as you normally would. The Console will show you a message that the debugger is waiting for your app to launch.

  ![Xcode: Debugger waiting for app to launch](https://oleb.net/media/xcode-debugger-waiting-for-app-to-launch.png)
4. Launch your app by invoking your custom URL or sending a push notification. The debugger will automatically attach to your app’s process and stop at the breakpoint.
