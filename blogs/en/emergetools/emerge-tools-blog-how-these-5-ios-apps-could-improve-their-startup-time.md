---
title: 'Emerge Tools Blog | How these 5 iOS apps could improve their startup time'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/improve-popular-iOS-app-startup-times'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:50dd653b58a0e1f5'
translated: false
---

> 原文：[Emerge Tools Blog | How these 5 iOS apps could improve their startup time](https://www.emergetools.com/blog/posts/improve-popular-iOS-app-startup-times)　·　Emerge Tools Blog

# How 5 iOS apps could improve their startup time by an average of 28%

September 14, 2022 by

Michael Eisel

iOSPerformanceStartup time

![improve-popular-iOS-app-startup-times](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog9.54f9d326.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [Milliseconds matter](https://www.emergetools.com/blog/posts/improve-popular-iOS-app-startup-times#milliseconds-matter)

Startup time is a crucial app metric that should be continuously monitored and improved. A/B tests at top mobile app companies consistently show that adding just fractions of a second can significantly hurt core usage metrics, such as daily active users and time spent on the app per user per day.

Lyft reported a 5% increase in user sessions thanks to a [21% decrease](https://www.youtube.com/watch?v=nmeuLSM__10&t=8s) in startup time for their driver app. Apple has made startup time the subject of numerous WWDC presentations^[[1]](https://developer.apple.com/videos/play/wwdc2019/423/)[[2]](https://developer.apple.com/videos/play/wwdc2022/110362/)[[3]](https://developer.apple.com/videos/play/wwdc2022/110363/).

Instead of high level claims about avoiding common anti-patterns to improve startup time, this blog post will use Emerge's [Performance Analysis](https://www.emergetools.com/product/performanceanalysis) product to diagnose specific app startup issues and find improvements. This post will focus on iOS apps, however Emerge's tooling has full parity across both Android and iOS.

**These are real optimizations that apply to public App Store builds with no developer involvement.**

## [How we measured startup](https://www.emergetools.com/blog/posts/improve-popular-iOS-app-startup-times#how-we-measured-startup)

Since the apps analyzed here are taken from the App Store without any debug information or source code, we decided to simply define "startup time" as the earliest point of app launch until the end of `applicationDidBecomeActive(_:)`.

For mobile app teams working with Emerge, startup time definitions are [fully customizable by the developer](https://docs.emergetools.com/docs/ios-performance-testing). A common use case would be defining endpoints past `applicationDidBecomeActive(_:)` to measure the time to when the user can meaningfully interact with the app. This means that the startup time measurements shown below are likely conservative estimates compared to what a developer at the company might consider startup to be.

Because of the lack of any debug symbols, we're unable to fully de-obfuscate many of the function names. Apps that are part of an [Emerge CI integration](https://www.emergetools.com/app/example/ios/wikipedia?buildContent=comparison) with debug symbols included would result in a much [more detailed flamegraph](https://www.emergetools.com/app/example/ios/wikipedia?buildContent=comparison).

Emerge utilizes a state-of-the-art physical device farm to ensure that performance measurements are as accurate as possible. The following main thread measurements were conducted on an iPhone SE (2020) running iOS 15.4.1.

It's important to note that _a single_ measure of an app's startup time is exactly that and shouldn't necessarily be extrapolated to represent a larger sample size. Controlling variance is akin to taming a wild beast; everything from the app being logged in, recently launched, the device type, or even the temperature of the device can all drastically affect results.

Now let's see how 5 popular apps could improve their startup time...

![United Airlines app icon](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Funited.webp&w=128&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

United Airlines

View interactive startup time flamegraph

Total startup time: 2.05s

Possible savings: 40% (0.83s)

[![United app performance insight](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Funited-flamegraph.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)](https://www.emergetools.com/app/example/ios/united-performance-test?buildContent=flamegraph)

Featured Automated Insight

The United app has already been discussed at length by others due to [app size issues](https://telkins.dev/posts/how-i-shaved-187mb-off-uniteds-airlines-439mb-ios-app/#:~:text=Let's%20inspect%20the%20biggest%20framework%2C%20UALAppCore%20.&text=OK%2C%20so%20the%20vast%20majority,very%20large%20for%20a%20framework), but its startup time also has a lot of room for improvement. Three things immediately jump out:

- **Automated insight:** United spends 48ms in `JSONDecoder.decode()`, which should either be done in the background or sped up with a faster third-party JSON library like my own [ZippyJSON](https://github.com/michaeleisel/ZippyJSON).
- United spends 677ms in `-[NSPersistentContainer loadPersistentStoresWithCompletionHandler:]`. Core data work like this should be done off of the main thread. A delay this huge likely points to other anti-patterns being present.
- United spends 103ms in LPMessagingSDK, which calls `Bundle.init(identifier:)`. This method takes an identifier and returns the bundle that matches that ID (`CFBundleIdentifier` in the Info.plist). Although the method might seem innocuous, it has to load all the bundles from disk until it finds the one with the right bundle ID. This includes both user-supplied bundles, such as frameworks, as well as all of Apple's many bundles. When the bundles are first loaded, they become cached to some extent. Rerunning the app again immediately after sees a startup time reduction of 20ms, but for cold-start, this load cost must be paid. The app should be changed to delay the LPMessagingSDK initialization until the feature is actually needed (which is likely only when the user goes to a support page).

![Chipotle app icon](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fchipotle.webp&w=128&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Chipotle

View interactive startup time flamegraph

Total startup time: 0.57s

Possible savings: 33% (0.19s)

[![Chipotle app performance insight](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fchipotle-flamegraph.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)](https://www.emergetools.com/app/example/ios/chipotle-performance-test?buildContent=flamegraph)

Featured Automated Insight

- **Automated insight:** United's app isn't the only one to fall prey to issues with LPMessagingSDK. Chipotle's app spends 187ms of startup in LPMessagingSDK in `Bundle.init(identifier:)`, which, as discussed above, can be moved off the startup path.

![Curb app icon](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fcurb.webp&w=128&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Curb

View interactive startup time flamegraph

Total startup time: 0.8s

Possible savings: 22% (0.18s)

[![Curb app performance insight](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fcurb-flamegraph.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)](https://www.emergetools.com/app/example/ios/curb-performance-test?buildContent=flamegraph)

Featured Automated Insight

Curb is the only app we analyze here that uses the Salesforce Service Cloud SDK. This SDK provides APIs and UIs for customer relationship management tools, such as support chat. As with LPMessagingSDK, the Salesforce Service Cloud SDK does some very costly loading of bundles. Specifically, it spends 83ms in `Bundle.allFrameworks`, and then another 93ms in `NSArray.filtered(using:)` immediately after. These method calls are at the very beginning of startup (or at least the portion we can record), suggesting that they're initializers. Initializers are special functions that are implicitly run during early startup, such as during `NSObject.load()` methods.

[![Emerge Advanced Flamegraph Controls](https://www.emergetools.com/images/blogs/blog9/perf-gif.gif)](https://www.emergetools.com/app/example/ios/curb-performance-test?buildContent=flamegraph)

Emerge Advanced Flamegraph Controls

If we switch the ["Collapse system calls"](https://docs.emergetools.com/docs/performance-visualizations#remove-system-libraries) toggle in the UI, we can see they're indeed initializers that aren't being run by app code, but instead by `dyld4::Loader::findAndRunAllInitializers`. After decompiling that library with Hopper, we find that the subsequent function is calling `Bundle.allFrameworks` and doing essentially the following:

```shell
var frameworksList: [Bundle]?
...
func initializeFrameworkBundles() {
...
let allFrameworks = NSBundle.allFrameworks
let predicate = Predicate(format:"bundleIdentifier BEGINSWITH %@", "com.salesforce")
frameworksList = allFrameworks.filteredArray(predicate:predicate)
...
}
```

`NSBundle.allFrameworks` is expensive because it does some initial setup and/or fetching from cache for every single framework. This includes user-supplied frameworks as well as many Apple frameworks. The `NSArray.filteredArrayUsingPredicate(using:)` call is expensive for a similar reason: it calls `NSBundle.bundleIdentifier` for every single framework bundle. This means that on top of the initial setup done in `NSBundle.allFrameworks`, it now has to read the Info.plist for each framework and get the `CFBundleIdentifier` value. Although it can be faster on further runs due to caches being filled, it will still take a non-trivial amount of time, and cold start remains an important case.

Salesforce could avoid all of this by reducing its search to just the user-supplied frameworks in `*bundle path*/Frameworks`, or better yet searching for the frameworks by name that it knows could be Salesforce provided. For an app developer who uses Salesforce, it's tougher to work around. Unlike with LPMessagingSDK, where the developer could control when initialization occurs and move it completely off the startup path, the developer doesn't have that option for an initializer function that gets run automatically by the system.

To SDK developers: _please_ don't use initializer functions. They are much harder to measure the impact on startup and to prevent/delay from running. Not only can they hurt performance, but also stability as I think we all remember in the [Facebook SDK fiasco](https://www.theverge.com/2020/5/7/21250689/facebook-sdk-bug-ios-app-crash-apple-spotify-venmo-tiktok-tinder).

With this in mind, here are some mitigation approaches:

- For the adventurous, try not linking the Service Cloud frameworks, instead include them in the app bundle and use `Bundle.load()` to load them before calling the APIs (since oftentimes the SDK is only needed for very specific, less-commonly used screens, like customer support).
- Use the Service Cloud REST API directly, rather than via their libraries.
- Use an alternate service entirely.

Beyond the issues mentioned above, the Salesforce Service Cloud SDK spends 67ms running `class_conformsToProtocol` and `objc_copyClassList` (perhaps iterating over all classes to determine which ones conform to some protocol) in non-initializer setup. All of this setup can likely be moved out of startup.

As for other SDKs, we see NewRelic taking 4% of startup due to method swizzling, LeanPlum taking 3% due to method swizzling, and Realm taking 1% for `objc_copyClassList` (probably only 1% because Service Cloud SDK warmed up the caches by calling that function first). Although Realm might be fairly integral to the startup path, the other two SDKs seem like they can at least be delayed slightly to allow the startup screen to display before blocking the main thread.

![Walmart app icon](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fwalmart.webp&w=128&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Walmart

View interactive startup time flamegraph

Total startup time: 0.67s

Possible savings: 33% (0.22s)

[![Walmart app performance insight](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fwalmart-flamegraph.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)](https://www.emergetools.com/app/example/ios/walmart-performance-test?buildContent=flamegraph)

Featured Automated Insight

- **Automated insight:** Walmart spent 20ms on `print` statements, which should not be used in a production App Store app
- Walmart also spent 197ms of startup on `String.init(describing:)`. Generally, this is a sign that an app is trying to either use that string as a unique ID (in which case it should use `ObjectIdentifier` instead), or that it may be calling this method as part of logging, which can just be removed.

![Zoom app icon](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fzoom.webp&w=128&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Zoom

View interactive startup time flamegraph

Total startup time: 0.27s

Possible savings: 15% (0.04s)

[![Zoom app performance insight](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fzoom-flamegraph.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)](https://www.emergetools.com/app/example/ios/zoom-performance-test?buildContent=flamegraph)

Featured Automated Insight

- And lastly, my personal favorite. Zoom's app actually spends 41ms _sleeping_ on the main thread during startup.

---

## [Conclusion](https://www.emergetools.com/blog/posts/improve-popular-iOS-app-startup-times#conclusion)

Even at the largest scale, managing mobile app performance is extremely challenging. Startup time is one of the most common and accessible performance metrics, but achieving accurate measurement in the development process is a major hurdle.

Using Emerge’s Performance Analysis product, we were able to analyze and propose startup time improvements for five popular iOS apps downloaded directly from the App Store. Many of the insights proposed in this blog post are automated insights from Emerge’s Performance Analysis product which automatically identifies and suggests performance improvements.

Once integrated into CI, a developer can make changes and immediately see whether that feature regressed/improved app performance directly on their pull request.

Good luck to all those working on improving startup time and app performance out there and please let us know if you’ve got any questions!
