---
title: 'Emerge Tools Blog | Comparing the Performance of the Top 6 Analytics SDKs for iOS'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/comparing-top-analytics-sdks-for-ios'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:66248216bdb900af'
translated: false
---

> 原文：[Emerge Tools Blog | Comparing the Performance of the Top 6 Analytics SDKs for iOS](https://www.emergetools.com/blog/posts/comparing-top-analytics-sdks-for-ios)　·　Emerge Tools Blog

# Comparing the Performance of the Top 6 Analytics SDKs for iOS

October 4, 2023 by

Brian Capps

iOSPerformanceGuest post

![Comparing the Performance of the Top 6 Analytics SDKs for iOS](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner.b72becd1.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

_The following is a guest post from Brian Capps at [Lickability](https://lickability.com/?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post), a premier mobile software studio._

_"If you can't measure it, you can't manage it."   
- Peter Drucker_

Emerge Tools can measure a lot about your app — size, performance, UI changes, and more. However, only you can measure what success looks like for your product. Number of users, retention, conversion: these success metrics are often critical to your business and can be measured using analytics. But with a head-spinning number of analytics libraries available, which one should you choose for your app?

[appFigures](https://appfigures.com/top-sdks/analytics/all?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) has analyzed millions of apps in the App Store and provides a handy list of the most popular analytics libraries. It's easy to find a list of features for each library and why you might want to use it. But how does adding an SDK affect your app? What type of overhead do these libraries bring?

We can't choose an analytics library for you, but we can compare the size and performance implications of different SDKs to your app on iOS. Let's see how they all stack up!

## [The Comparison](https://www.emergetools.com/blog/posts/comparing-top-analytics-sdks-for-ios#the-comparison)

This post will compare the top 6 analytics SDKs on iOS. Every SDK will be measured against a newly created Xcode project with the default iOS app template (base app). This simple, single-view app is a mere 118.5kb in size with a clean startup path.

We'll add each library as a dependency through Swift Package Manager and initially configure it as directed (generally calling a setup method from the app delegate). Then we'll compare the size and startup performance to the base app.

Startup performance comparisons will be done using Emerge's [Performance Analysis](https://www.emergetools.com/product/performanceanalysis?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post). Some notes on how it works:

- Testing is done on physical devices (iPhone SE 2020)
- For this comparison, startup time is defined as process start to `didFinishLaunching` (Emerge users can customize markers)
- The primary metric is the relative change in startup time between the two builds. While we often think of startup in absolute time, the percentage change is more [apt for comparisons](https://docs.emergetools.com/docs/absolute-vs-relative-timing?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post)
- To come to a statistically significant conclusion, testing is done in a controlled environment and consists of numerous iterations of both the head and base builds (below image)
- You can refer to [our docs](https://docs.emergetools.com/docs/performance-testing?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) for full details on how testing is done

![Flame chart of app launch initializing Firebase](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Ffirebase-build-details.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Test iterations for Firebase. Iterations are run on a head and base build until a statistically significant conclusion can be reached

Links to our complete analysis are included for each SDK. The following are the 6 most popular analytics SDKs from most to least popular.

![Firebase logo](https://www.emergetools.com/images/blogs/blog18/firebase-logo.svg)

### Firebase

**Size Impact:**[+1.6 MB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-firebase)

|

**Startup Impact:**[+30.2% (27 ms)](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-firebase?buildContent=comparison)

Firebase from Google is by far the most popular analytics library in use on the App Store. This makes sense, with how many features Firebase offers as an all-service app development platform (database, push notifications, A/B testing, etc.). Our focus is testing the implications of only adding the `FirebaseAnalytics` product from the package. We are using the latest version, 10.14.0, and here are the results of the analyses:

![Flame chart of app launch initializing Firebase](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Ffirebase-flamechart.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Flame chart of app launch initializing Firebase

![Detailed size diff when adding the Firebase SDK](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Ftreemap-diff-firebase.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Detailed size diff when adding the Firebase SDK

Search

_Note: While appFigures lists Fabric and Google Analytics as popular SDKs, Google has rolled both products into Firebase Analytics, so they have not been included._

![Facebook Analytics logo](https://www.emergetools.com/images/blogs/blog18/meta-logo.svg)

### Facebook Analytics

**Size Impact:**[+1.4 MB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-facebook)

|

**Startup Impact:**[+18.7% (17 ms)](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-facebook?buildContent=comparison)

The next most popular SDK is Facebook Analytics. This popularity is also no surprise: Meta and Google are the largest companies on this list, and Facebook has long been a presence in the iOS community (anyone remember [Three20](https://github.com/facebookarchive/three20?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post)?). To set this up, we added the Facebook SDK version 14.1.0 with only the `FacebookCore` package product for analytics. Here's what we found:

![Flame chart of app launch initializing Facebook](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Ffb-flamechart.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Flame chart of app launch initializing Facebook

![Detailed size diff when adding the FB SDK](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Ftreemap-diff-fb.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Detailed size diff when adding the FB SDK

Search

Looking at the flame chart, we can see Facebook accessing the Keychain on the main thread. While these are quite fast, best practice is to put these calls in the background.

![Spans showing keychain access on the main thread](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Ffb-insight.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Keychain access on the main thread

![Flurry logo](https://www.emergetools.com/images/blogs/blog18/flurry-logo.svg)

### Flurry

**Size Impact:**[+1.0 MB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-flurry)

|

**Startup Impact:**[+10.8% (10 ms)](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-flurry?buildContent=comparison)

Like many of the top analytics SDKs, Flurry has been around for a long time. The configuration instructions show their age, referencing Objective-C code by default with no mention of SwiftUI or any newer technologies. After some initial trouble with website load issues, we installed version 12.4.0 and got to work on the comparison. You can see it below:

![Flame chart of app launch initializing Flurry](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Fflurry-flamechart.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Flame chart of app launch initializing Flurry

![Detailed size diff when adding the Flurry SDK](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Ftreemap-diff-flurry.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Detailed size diff when adding the Flurry SDK

Search

![Amplitude logo](https://www.emergetools.com/images/blogs/blog18/amplitude-logo.svg)

### Amplitude

**Size Impact:**[+468.5 kB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-amplitude)

|

**Startup Impact:**[+23.6% (21 ms)](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-amplitude?buildContent=comparison)

Amplitude is an analytics platform with detailed insight and experimentation capabilities. Founded in 2011, it's the newest company on the list. They offer several iOS SDK options, but for this comparison, we looked at the newer, [purely Swift beta iOS SDK](https://www.docs.developers.amplitude.com/data/sdks/ios-swift/?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post), version 0.4.14:

![Flame chart of app launch initializing Amplitude](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Famplitude-flamechart.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Flame chart of app launch initializing Amplitude

![Detailed size diff when adding the Amplitude SDK](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Ftreemap-diff-amplitude.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Detailed size diff when adding the Amplitude SDK

Search

![Segment logo](https://www.emergetools.com/images/blogs/blog18/segment-logo.svg)

### Segment

**Size Impact:**[+718.8 kB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-segment)

|

**Startup Impact:**[+14.6% (13 ms)](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-segment?buildContent=comparison)

Segment is another platform for analytics and customer data, with a focus on data insight. They were acquired in 2020 and are now a division of Twilio. They offer several iOS SDKs, but we chose their [Swift SDK](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) for this measurement. Here's what we saw on Analytics-Swift version 1.4.7:

![Flame chart of app launch initializing Segment](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Fsegment-flamechart.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Flame chart of app launch initializing Segment

![Detailed size diff when adding the Segment SDK](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Ftreemap-diff-segment.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Detailed size diff when adding the Segment SDK

Search

Part of Emerge's analysis identifies protocols without conformances — dead code. Of all the SDKs, Segment SDK had the most of this [type of dead code](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post), but not a significant amount.

![Screenshot of Emerge Insight showing protocols without conformances in Segment SDK](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Fsegment-dead-code.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Protocols without conformances in Segment SDK

![Mixpanel logo](https://www.emergetools.com/images/blogs/blog18/mixpanel-logo.svg)

### Mixpanel

**Size Impact:**[+422.2 kB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-mixpanel)

|

**Startup Impact:**[+31.0% (27 ms)](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-mixpanel?buildContent=comparison)

Finally, we have Mixpanel, our last (but certainly not least!) analytics provider. Mixpanel has been a staple of iOS analytics for quite a while, and they offer similar features to Segment and Amplitude. We selected the [Swift SDK](https://docs.mixpanel.com/docs/tracking/reference/swift?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) and tested the latest version, 4.1.4:

![Flame chart of app launch initializing Mixpanel](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Fmixpanel-flamechart.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Flame chart of app launch initializing Mixpanel

![Detailed size diff when adding the Mixpanel SDK](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog18%2Ftreemap-diff-mixpanel.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Detailed size diff when adding the Mixpanel SDK

Search

## [Results](https://www.emergetools.com/blog/posts/comparing-top-analytics-sdks-for-ios#results)

So how did they all do? Let’s see all the results in a table for easier comparison:

| SDK | App Size Increase | Startup Time Increase (Relative) |
|---|---|---|
| [Firebase Analytics](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-firebase) | [1.6 MB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-firebase) | [+30.2%](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-firebase?buildContent=comparison) |
| [Facebook Analytics](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-facebook) | [1.4 MB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-facebook) | [+18.7%](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-facebook?buildContent=comparison) |
| [Flurry](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-flurry) | [1.0 MB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-flurry) | [+10.8%](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-flurry?buildContent=comparison) |
| [Amplitude](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-amplitude) | [468.5 kB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-amplitude) | [+23.6%](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-amplitude?buildContent=comparison) |
| [Segment](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-segment) | [718.8 kB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-segment) | [+14.6%](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-segment?buildContent=comparison) |
| [Mixpanel](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-mixpanel) | [422.2 kB](https://www.emergetools.com/app/example/compare/ios-analytics-sdk-comparison-mixpanel) | [+31.0%](https://www.emergetools.com/app/example/ios/analytics-sdk-comparison-mixpanel?buildContent=comparison) |

As you can see, there are significant differences in app size and startup time between the SDKs. The most popular SDKs with some of the oldest repositories and many features add the most to your app size, while some of the more focused, less popular entrants are more compact and nimble. This may have been expected, but now we have the data to dig in more.

Firebase, with many years of development and shared core code with its myriad other features, tops the list as the most expensive in size and second in startup time. On the other end of the spectrum, Mixpanel's SDK is nearly 75% smaller than Firebase, while still adding just as much time to your app’s startup. All the others fall somewhere in between, with a few surprises like Flurry’s minimal impact on startup.

Increased size and runtime can affect your bottom line in many ways (and these SDKs will help you confirm that 😉). Aside from impacting the user, [**adding a megabyte**](https://www.emergetools.com/blog/posts/CostOfAByte?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) of app size can have the **equivalent CO2 emissions for 5 round-trip flights from London to LAX** for a globally-scaled app, so it's important to understand what's going into your app.

## [More than Metrics](https://www.emergetools.com/blog/posts/comparing-top-analytics-sdks-for-ios#more-than-metrics)

While these metrics provide helpful information, they can’t tell you everything. There may be features that your product team needs that only some SDKs offer, cost considerations, and many more factors. For example, Firebase has many other features that are incredibly useful for mobile developers (along with it being mostly free!), and that may be a much greater consideration than any app size or startup cost.

The analytics SDK you choose for your app will be personal for you and your business. Hopefully, these metrics provide helpful context for your team to decide. If you'd like to evaluate the performance implications of a specific SDK, you can create an [Emerge Tools account](https://www.emergetools.com/signup?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) to see our analysis!

_You can reach out to [Lickability](https://lickability.com/contact?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) for help implementing your Emerge Tools analysis recommendations!_
