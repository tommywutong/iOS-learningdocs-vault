---
title: Newsstand FAQ
apple_id: DTS40011215
resource_type: Technical Note
platform: iOS
topic: General
technology: null
published: '2012-01-19'
source_url: https://developer.apple.com/library/archive/technotes/tn2280/_index.html
archived_at: '2026-07-26T19:54:10.087641Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2280

# Newsstand FAQ

New in iOS 5.0, Newsstand provides a central place for users to read magazines and newspapers. Publishers who want to deliver their magazine and newspaper content through Newsstand can create their own iOS applications using the Newsstand Kit framework. This document intends to supplement the available technical documentation on the Newsstand Kit framework by answering frequently asked questions from Newsstand app developers.

[Newsstand App Icons](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvhekv2tknkectsel5avauc7jfbu6tst)[What are the size guidelines for Newsstand app icons?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvhekv2tknkectsel5avauc7jfbu6tstfvluqqkul5averk7kreekx2tjfnekx2hkveuirkmjfheku27izhvex2oivlvgu2uifheix2bkbif6skdj5hfgxy)[I've modified my Info.plist file to specify a new image for my Newsstand icon, and have styled it with a binding edge and binding type. Why isn't this styling shown on my app in the Newsstand view?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvhekv2tknkectsel5avauc7jfbu6tstfvev6vsfl5gu6rcjizeukrc7jvmv6skoizhv6ucmjfjvix2gjfgekx2uj5pvgucfineumwk7ifpu4rkxl5eu2qkhivpumt2sl5gvsx2oivlvgu2uifheix2jinhu4x27ifheix2iiflekx2tkrmuyrkel5evix2xjfkeqx2bl5bestsejfheox2firdukx2bjzcf6qsjjzcestshl5kfsucfl5pv6v2ilfpusu2ol5kf6vcijfjv6u2ulfgestshl5juqt2xjzpu6ts7jvmv6qkqkbpusts7kreekx2oivlvgu2uifheix2wjfcvoxy)[Selling Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvjuktcmjfheox2jknjvkrkt)[How should I sell issues of my publication within my Newsstand app?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvke4vcbi4za)[Users can browse Newsstand apps via a Store button in the Newsstand. Will my Newsstand app still be included in search results returned by the App Store app on iOS, and by iTunes on OS X?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvjuktcmjfheox2jknjvkrktfvkvgrksknpugqkol5bfet2xkncv6tsfk5jvgvcbjzcf6qkqkbjv6vsjifpucx2tkrhverk7ijkvivcpjzpusts7kreekx2oivlvgu2uifheix27l5lustcml5gvsx2oivlvgu2uifheix2bkbif6u2ujfgeyx2civpustsdjrkuirkel5eu4x2tivaveq2il5jeku2vjrkfgx2sivkfkusoivcf6qszl5keqrk7ififax2tkrhverk7ififax2pjzpust2tl5puctsel5bfsx2jkrku4rktl5hu4x2pknpvqxy)[Delivering Your Content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvcektcjkzcveskoi5pvst2vkjpugt2okrcu4va)[How is the push notification that initiates the Newsstand background download different from other push notifications? Will I have to change or modify my backend infrastructure?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvcektcjkzcveskoi5pvst2vkjpugt2okrcu4vbnjbhvox2jknpviscfl5ifku2il5he6vcjizeugqkujfhu4x2ujbavix2jjzeviskbkrcvgx2ujbcv6tsfk5jvgvcbjzcf6qsbinfuouspkvheix2ej5lu4tcpifcf6rcjizdekusfjzkf6rssj5gv6t2ujbcvex2qkvjuqx2oj5kesrsjinaviskpjzjv6x27k5euytc7jfpuqqkwivpvit27ineectshivpu6us7jvhuiskglfpu2wk7ijaugs2fjzcf6skoizjecu2ukjkugvcvkjcv6)[Can I initiate a background download with a push notification in a non-Newsstand app?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvcektcjkzcveskoi5pvst2vkjpugt2okrcu4vbninau4x2jl5eu4skujfavirk7ifpueqkdjndvet2vjzcf6rcpk5heyt2birpvoskujbpucx2qkvjuqx2oj5kesrsjinaviskpjzpusts7ifpu4t2ol5hekv2tknkectsel5avauc7)[Is my Newsstand app required to use Newsstand Kit's background downloading feature?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvcektcjkzcveskoi5pvst2vkjpugt2okrcu4vbnjfjv6tkzl5hekv2tknkectsel5avauc7kjcvcvkjkjcuix2uj5pvku2fl5hekv2tknkectsel5fusvc7knpueqkdjndvet2vjzcf6rcpk5heyt2bireu4r27izcucvcvkjcv6)[Can users disable background downloading?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvcektcjkzcveskoi5pvst2vkjpugt2okrcu4vbninau4x2vkncveu27irevgqkcjrcv6qsbinfuouspkvheix2ej5lu4tcpifcestshl4)[Once my app has received the notification, can I initiate the background download from a thread other than the main thread?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvcektcjkzcveskoi5pvst2vkjpugt2okrcu4vbnj5hegrk7jvmv6qkqkbpuqqktl5jekq2fjflekrc7kreekx2oj5kesrsjinaviskpjzpv6q2bjzpusx2jjzeviskbkrcv6vciivpueqkdjndvet2vjzcf6rcpk5heyt2birpumuspjvpucx2ujbjekqkel5hviscfkjpviscbjzpviscfl5gucskol5kequsfifcf6)[Should I package my issue for background download into one large file, or download each asset separately?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvcektcjkzcveskoi5pvst2vkjpugt2okrcu4vbnknee6vkmirpusx2qifbuwqkhivpu2wk7jfjvgvkfl5de6us7ijaugs2hkjhvktsel5ce6v2ojrhucrc7jfhfit27j5hekx2mifjeork7izeuyrk7l5hvex2ej5lu4tcpifcf6rkbinef6qktkncvix2tiviecusbkrcuywk7)[The content of my publication needs to be updated throughout the day. Can I initiate a Newsstand background download more than once in a 24-hour period?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvcektcjkzcveskoi5pvst2vkjpugt2okrcu4vbnkreekx2dj5hfirkokrpu6rs7jvmv6ucvijgesq2bkreu6ts7jzcukrctl5ke6x2civpvkuceifkekrc7krefet2vi5ee6vkul5keqrk7iravsx27l5bucts7jfpustsjkreucvcfl5av6tsfk5jvgvcbjzcf6qsbinfuouspkvheix2ej5lu4tcpifcf6tkpkjcv6vciifhf6t2oincv6skol5av6mrul5ee6vksl5iekusjj5cf6)[Managing Content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvguctsbi5eu4r27inhu4vcfjzka)[Will all of my issues be automatically stored on the user's device, indefinitely?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvguctsbi5eu4r27inhu4vcfjzkc2v2jjrgf6qkmjrpu6rs7jvmv6sktknkuku27ijcv6qkvkrhu2qkujfbuctcmlfpvgvcpkjcuix2pjzpviscfl5kvgrksl5jv6rcfkzeugrk7l5eu4rcfizeu4skuivgfsxy)[Can I move my issues out of the default Newsstand storage location once they're downloaded, or download issues to another location?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwugsbrfvguctsbi5eu4r27inhu4vcfjzkc2q2bjzpusx2nj5lekx2nlfpusu2tkvcvgx2pkvkf6t2gl5keqrk7ircumqkvjrkf6tsfk5jvgvcbjzcf6u2uj5jecr2fl5ge6q2bkreu6ts7j5hegrk7kreekwk7kjcv6rcpk5heyt2bircuix27j5jf6rcpk5heyt2birpusu2tkvcvgx2uj5puctspkreekus7jrhugqkujfhu4xy)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrrguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Newsstand App Icons

### What are the size guidelines for Newsstand app icons?

On iPhone, the length of the longest edge of your Newsstand app icon should be at least 90 pixels. On iPhone 4 retina display your icon dimensions should be doubled, meaning that the longest edge should be at least 180 pixels. On iPad the longest edge of your Newsstand app icon should be at least 126 pixels.

In all cases, the longest edge may be a horizontal or vertical edge. If the longest edge is horizontal, the aspect ratio should not exceed 2:1. If the longest edge is vertical, the aspect ratio should not be smaller than 1:2.

### I've modified my Info.plist file to specify a new image for my Newsstand icon, and have styled it with a binding edge and binding type. Why isn't this styling shown on my app in the Newsstand view?

If you specify a newspaper binding type with `UINewsstandBindingTypeNewspaper`, you'll see a subtle fold at the bottom of your icon in the Newsstand view. All other visual styling — magazine staples, magazine pages, and the stacked newspaper pages — is only shown in the iOS app switcher.

[Back to Top](#)

## Selling Issues

### How should I sell issues of my publication within my Newsstand app?

Your Newsstand app should always offer the option to purchase an auto-renewable subscription to your publication. Additionally you may sell single issues as individual non-consumable in-app purchase items.

### Users can browse Newsstand apps via a Store button in the Newsstand. Will my Newsstand app still be included in search results returned by the App Store app on iOS, and by iTunes on OS X?

Yes. Newsstand apps are included in search results returned within the App Store app on iOS, and within iTunes on OS X.

Users also may browse the iTunes Store by category. In iTunes Connect you may set the Primary Category on your Newsstand app to any of the available categories, such as Games, Lifestyle, or Business. The Secondary Category for Newsstand apps is automatically set to the Newsstand category.

[Back to Top](#)

## Delivering Your Content

### How is the push notification that initiates the Newsstand background download different from other push notifications? Will I have to change or modify my backend infrastructure?

The notification that initiates the Newsstand background download is the same as any other push notification, with two exceptions. The first difference is the payload — your Newsstand notification should include the `content-available` property (with a value of 1) in the JSON payload. Second, your app may only initiate a background download once every 24 hours. iOS will ignore notifications that try to initiate a background download more than once in a 24 hour period.

### Can I initiate a background download with a push notification in a non-Newsstand app?

No, this feature is only for Newsstand apps.

### Is my Newsstand app required to use Newsstand Kit's background downloading feature?

If you're delivering an issue to a user as part of a subscription, you must deliver it via background download.

In general, users will expect Newsstand apps to have content downloaded in the background, ready and available for offline viewing. If a user hasn't purchased a subscription for new issues, you may use Newsstand Kit's background downloading feature to deliver other content. Keep in mind that your Newsstand app should not deliver or manage content in a way that ends up consuming large amounts available storage space on a user's device.

### Can users disable background downloading?

Yes, users can disable Newsstand's push notification-initiated background downloading on a per-app basis in Settings. You can determine whether background downloading has been disabled for your app by looking for `UIRemoteNotificationTypeNewsstandContentAvailability` in the set of enabled types returned by UIApplication's `enabledRemoteNotificationTypes` property.

### Once my app has received the notification, can I initiate the background download from a thread other than the main thread?

In iOS 5.0, you should initiate the background download from the main thread.

### Should I package my issue for background download into one large file, or download each asset separately?

Packaging your issue assets into one compressed file is best for system performance, and it lets you determine the total download time for your issue.

Since your app has to be woken up and notified whenever a download finishes, downloading each issue asset individually is not the best approach for system performance. And, when you download each asset individually, it's impossible to calculate the total download time for your issue.

If you cannot deliver your issue in a single compressed file, then you should group your assets into sets of downloads that make sense for your app. For example, you might group the assets that are needed to show the first page of your issue into a single download.

### The content of my publication needs to be updated throughout the day. Can I initiate a Newsstand background download more than once in a 24-hour period?

Allowing multiple background downloads for multiple apps would drain system resources, so Newsstand apps are limited to one background download initiated by push notification each day. If you send additional notifications to a device that attempt to initiate a background download, those notifications will be delivered to the device but ignored by Newsstand Kit.

If you want your Newsstand app to deliver breaking news, consider sending an issue via background download and downloading a small amount of additional, up-to-the-minute content when the user launches your app.

For test purposes on development devices only, you can override the built-in limit and initiate more than one background download in a 24-hour period by setting the user default @"`NKDontThrottleNewsstandContentNotifications`". See Listing 1.

__Listing 1__  Setting the user default NKDontThrottleNewsstandContentNotifications

```
[[NSUserDefaults standardUserDefaults]setBool: YES forKey:@"NKDontThrottleNewsstandContentNotifications"];
```

__Note:__ A development device refers to a device which has been recognized in Xcode Organizer as having the "Use for Development" checkbox enabled.

[Back to Top](#)

## Managing Content

### Will all of my issues be automatically stored on the user's device, indefinitely?

Newsstand Kit provides a managed repository for your issues located at the `contentURL` for the `NKIssue`. This managed repository acts as a cache for the content you host on your servers, and like any cache is susceptible to eviction as system resources become low.

In such an event, the information you provide Newsstand Kit via the `currentlyReadingIssue` property and the `date` parameter in `addIssueWithName:date:` helps Newsstand Kit to prioritize which content is most critical for the user as it evicts elements from the cache. Your Newsstand app should be capable of re-downloading back issues at the user's request, should such resource constraints arise.

### Can I move my issues out of the default Newsstand storage location once they're downloaded, or download issues to another location?

You should not store or move your issues to a location other than the Newsstand managed repository, such as the Documents folder for your app. Doing so can result in a very long backup times, and a shortage of storage space.

Whether purchased as part of a subscription or as an individual non-consumable item, issues should always be stored in the default Newsstand storage location. This lets iOS manage the available storage space on a system-wide basis, delivering the best experience for users.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-01-19 | Added mention of the user default boolean key setting - NKDontThrottleNewsstandContentNotifications as a way to allow multiple downloads per day while testing in the sandbox only. |
| 2011-09-30 | Added detailed information about icon sizes for different devices, and categories. |
| 2011-09-08 | New document that answers frequently asked questions about Newsstand and the Newsstand Kit frameworks. |

