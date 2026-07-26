---
title: How Do Alarm Clock Apps Work on iOS?
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/02/alarm-clock-apps-ios/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:726c79e2ac4d307f'
translated: false
---

> 原文：[How Do Alarm Clock Apps Work on iOS?](https://oleb.net/blog/2014/02/alarm-clock-apps-ios/)　·　Ole Begemann

# How Do Alarm Clock Apps Work on iOS?

**Update June 6, 2019:** According to the [iOS 13 release notes](https://developer.apple.com/documentation/ios_ipados_release_notes/ios_ipados_13_beta_release_notes/), `UIApplicationExitsOnSuspend` is no longer supported in iOS 13, so the trick I describe in this article doesn’t work anymore.

---

Not surprisingly, there is a ton of alarm clock apps on the App Store. Did you ever wonder how they work under Apple’s strict [multitasking restrictions](https://developer.apple.com/library/ios/documentation/iphone/conceptual/iPhoneOSProgrammingGuide/ManagingYourApplicationsFlow/ManagingYourApplicationsFlow.html#//apple_ref/doc/uid/TP40007072-CH4-SW20)?

## Local Notifications Have Limitations

Yes, there are [Local Notifications](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/), allowing apps to play an alarm sound at a specified time. But other than that, local notifications are of very limited usefulness to a sophisticated alarm clock app:

- A local notification does not wake up the app unless the user interacts with it, giving the app no control when the alarm sounds.
- Alert sounds have a maximum duration of 30 seconds and there is no way to repeat them automatically. (An app could schedule multiple local notifications in pre-defined time intervals to simulate a repeating alert, though.)
- Local notifications cannot override the ring/silent switch or the device’s Do Not Disturb setting.
- Alert sounds must be located in the app bundle. Users cannot specify a song from their music library as their alert.
- Apps have no control over the volume of a local notification’s alert sound (for example, to slowly crank up the volume of the alarm).

Let’s take the beautifully designed [Rise app](http://www.simplebots.co/) as an example. Rise overcomes all these limitations, so how does it do it? A [silent push notification](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW22) could be used to wake up the app, but that would require a server infrastructure and a network connection. Do you want to risk that your alarm clock might stop working when the network goes down? Moreover, that feature was just introduced in iOS 7 and Rise did work on earlier OS versions.

## Opt out of Multitasking

Rise’s surprising solution is to [opt out of iOS multitasking](https://developer.apple.com/library/ios/documentation/iphone/conceptual/iPhoneOSProgrammingGuide/ManagingYourApplicationsFlow/ManagingYourApplicationsFlow.html#//apple_ref/doc/uid/TP40007072-CH4-SW5) altogether. What was presumably intended by Apple as a temporary option for apps when [multitasking was first introduced in iOS 4.0](https://developer.apple.com/library/ios/releasenotes/General/WhatsNewIniOS/Articles/iPhoneOS4.html#//apple_ref/doc/uid/TP40009559-SW5) is still available:

> If you do not want your app to run in the background at all, you can explicitly opt out of background by adding the `UIApplicationExitsOnSuspend` key (with the value `YES`) to your app’s `Info.plist` file. When an app opts out, it cycles between the not-running, inactive, and active states and never enters the background or suspended states.

You can observe this behavior in Rise when you leave the app and immediately reopen it: it relaunches from scratch, showing the launch image again, rather than just wake up from the background.

![Rise.app's Info.plist with the UIApplicationExitsOnSuspend key](https://oleb.net/media/rise-app-info-plist.png)

<sub>Rise.app's `Info.plist` with the `UIApplicationExitsOnSuspend` key.</sub>

Rise takes advantage of a subtle difference between the pre- and post-multitasking environments: unlike apps that support multitasking, which get suspended in the background when the device gets locked, an app that runs in the pre-multitasking compatibility mode _keeps running_ when the user locks the device while the app is in the foreground. All the app has to do is wait for the alarm time and execute its custom code.

Keep in mind that this trick only works if users launch the app and keep in the foreground before they go to bed (they can lock the device, though). If the app is not running, it has no choice but to fall back to local notifications with their limited features. So Apple’s own alarm clock app can still do a lot more than any third-party app.

## How Long Will it Last?

I wonder if (and when) Apple will ever deprecate and eventually remove the ability for apps to opt out of multitasking. Makers of alarm clock app would not like that move.

Thanks to [Jörg Jacobsen](http://www.joergjacobsen.com/) for helping me figure this out.
