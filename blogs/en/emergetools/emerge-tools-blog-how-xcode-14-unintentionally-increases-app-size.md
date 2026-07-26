---
title: 'Emerge Tools Blog | How Xcode 14 unintentionally increases app size'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:40382a8543c7ec7e'
translated: false
---

> 原文：[Emerge Tools Blog | How Xcode 14 unintentionally increases app size](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size)　·　Emerge Tools Blog

# How Xcode 14 unintentionally increases app size

November 10, 2022 by

Max Topolsky & Josh Cohenzadeh

iOSApp sizeFeatured

![how-xcode14-unintentionally-increases-app-size](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog10.f51a5670.png&w=2048&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [Switching to Xcode 14](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#bitcode-symbol-stripping)

Xcode 14 released on September 12th with many new features and improvements. "The first thing you'll notice" is that Xcode is faster and 30% smaller.[^1](https://developer.apple.com/videos/play/wwdc2022/110427/)

Shortly after Xcode 14's release, a number of iOS apps saw significant size increases. We [first tweeted](https://twitter.com/emergetools/status/1575597900825915393) about observing a large spike in the Zillow iOS app. Zillow was not an isolated example.

Between mid-September and early-October:

- On October 8th, the Nike iOS app install size was 182.2 MB. A week later, it was 322.1 MB (+68%)
- American Airlines went from 182.2 MB to 389.1 MB — with Xcode 14 causing 76.2 MB (+42%) of the increase
- Chime increased from 162.8 MB to 212.8 MB (+31%)

![Chart with significant install size increase for Nike, American, Chime, and Zillow iOS Apps](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Finstall-size-2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Install size over time for Nike, American, Chime, and Zillow iOS apps

In each case, the size jump is due to these apps releasing with Xcode 14 for the first time. Among other features, Xcode 14 disabled bitcode by default.

_Xcode no longer builds bitcode by default... The capability to build with bitcode will be removed in a future Xcode release. IPAs that contain bitcode will have the bitcode stripped before being submitted to the App Store.   
 - [Xcode 14 Release Notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)_

What is bitcode?  
 Bitcode is an alternate way of packaging the app, which leaves part of the build process for Apple to complete after submitting it to the App Store. One of the things that Apple does is strip binary symbols.

And binary symbol stripping?  
Binary symbol stripping is where certain types of metadata that are unnecessary for running the app in production are removed from the binary. This is metadata that can be helpful prior to production, e.g. to generate dSYM files with, but only adds bloat to a user's phone in a production build.

The simple explanation is that bitcode optimizes production builds, partly by **stripping binary symbols**. Without bitcode turned on, Xcode build settings have to be changed to strip binary symbols.

This blog is not about whether deprecating bitcode is good or bad, but instead about highlighting a lesser known effect of releasing apps with Xcode 14. Below we'll:

- Compare app builds before and after Xcode 14
- Investigate which apps had a size regression due to Xcode 14
- And finally, show how any app can strip binary symbols

## [Comparing Nike before and after Xcode 14](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#size-increase-comparison)

With Xcode 14, any app that relied on bitcode is no longer necessarily stripping binary symbols from their production app. This means an app can get **much bigger** without adding any functionality.

Here is Emerge's Size Analysis X-Ray for version 22.35.0 (measured 10/8) of the Nike iOS app. In this version, frameworks make up 163.7 MB of the 191.7 MB install size. Try interacting with the treemap if you're on a larger screen to see granular size breakdowns.

![Emerge Size Analysis X-Ray for v22.35.0 of the Nike iOS App](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Fnike-treemap-1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Size Analysis X-Ray

Search

In version 22.36.1 (10/15), frameworks spike to 293.8 MB (+127.3 MB) of a total 322.1 MB. Notice the addition of the dark blue "String Table(s)" found in each framework.

![Emerge Size Analysis X-Ray for v22.36.1 of the Nike iOS App](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Fnike-treemap.gif&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Size Analysis X-Ray

Search

When we compare the two builds, we see that practically all of the 130 MB increase is coming from increases in [dyld](https://www.emergetools.com/glossary/dyld) String Tables. These String Tables are the unnecessary metadata that has now made it into production.

![Emerge Comparison table between two Nike builds](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Fnike-size-comp.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Size comparison between two Nike builds

Nike went from 213.9 KB of binary symbols (0.11% of total app size) to 127.5 **MB** of binary symbols — nearly 40% of the entire app.

![Binary symbol size in v22.35.0 (before Xcode 14)](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Finsight_comp1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Binary symbol size in v22.35.0 (before Xcode 14)

![Binary symbol size in v22.36.1 (after Xcode 14)](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Finsight_comp2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Binary symbol size in v22.36.1 (after Xcode 14)

Overall, the Nike iOS app increased by 130 MB, without any major changes.

![Bar chart of Nike iOS app size increase](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Fnike-size-chart.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [How many apps were affected](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#apps-affected)

Emerge Tools regularly downloads apps from the App Store for analysis, which let us detect these regressions and take a closer look. The below data represents all apps where:

- There are more than 2 MB of binary symbols
- More than 5% of the app is binary symbols
- The percent of the app that is binary symbols grew by at least 5% between builds

All apps are pulled directly from the App Store. Analysis provided is for educational purposes only and does not represent Emerge Tools customers.

Each of the above apps likely regressed due to releasing with Xcode 14. That said, there are many other apps that have significant savings from stripping binary symbols that aren't definitively attributable to Xcode 14.

Toyota (v2.0.9), the app tweeted about at the start of the blog, has an install size of 550.2 MB and could save 109.8 MB (20% of total app size) from stripping binary symbols. That was the first time Emerge Tools analyzed the Toyota app and we can't say if it had binary symbol bloat in previous builds.

There are also apps like TurboTax, which we've analyzed weekly since April 2022. TurboTax has over 100 MB of potential savings in every build we've measured. The three main Intuit iOS apps – [TurboTax](https://www.emergetools.com/app/example/ios/turbotax-xcode14), [Mint](https://www.emergetools.com/app/example/ios/mint-xcode14), and [Quickbooks](https://www.emergetools.com/app/example/ios/quickbooks-xcode14) – have a combined install size of 1.37 GB. They could save 578 MB (42% of size) just by stripping binary symbols.

The following is a list of apps where there are more than 15 MB of binary symbols, but we can't say for sure if it is related to switching to Xcode 14.

## [How to strip binary symbols without bitcode](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#stripping-symbols)

Luckily, stripping binary symbols from the final build product is straightforward. Here are two ways you can strip binary symbols.

### [Using Xcode build settings](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#xcode-build-settings)

You can do automatic stripping of builds during the Archive build action by setting:

- "Deployment Postprocessing" = "Yes"
- "Strip Linked Product" to "Yes"
- "Additional Strip Flags" to `-rSTx`
- All other stripping settings to their defaults

However, with this method, you have to be careful that settings are the same for all targets. Also, there can be pitfalls when used with package managers. For Cocoapods, here is a [discussion](https://github.com/CocoaPods/CocoaPods/issues/10277) of the issue which links to one possible [solution](https://github.com/home-assistant/iOS/pull/2234/files#diff-8f7d6adf31268a2d897ee34bd170592648d6e520aa237104395e4a4438af50cb) (make sure that the frameworks being stripped are all dynamic if you do this).

### [Using a Shell Script](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#shell-script)

One can also run the script below at the very end of the build process, right before signing. Note that for some package managers like Cocoapods, there may not be any point between the frameworks being copied in and being signed where a custom script can be run. In that case, signing must be done again manually after the stripping, because stripping will invalidate the signature.

Below is an example of a script you can use for binary stripping. Huge thanks to Filip Busic from Doordash for helping here!

In the build phases's settings, make sure that "Based on dependency analysis" is unchecked so that the script is run on every build. You can read more about this method [on our documentation](https://docs.emergetools.com/docs/strip-binary-symbols).

**Note:** binary stripping has to be done before codesigning the app or else the code signature will be invalidated.

## [Why this matters](https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size#conclusion)

As Apple said in their Xcode 14 video, app size is the first thing your user will notice. And users do pay attention, as a recent reviewer of the American Airlines iOS app puts it:

![Negative review of the American Airlines iOS app due to its install size](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Famerican-review.jpeg&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

App Store review of American Airlines iOS app

Google's Play Console documentation has a similar recommendation:

_App size is one of the biggest factors that can affect your app's install and uninstall metrics. It's important to regularly monitor and understand how you can reduce your app's download and install sizes.   
 - [Play Console Documentation](https://support.google.com/googleplay/android-developer/answer/9859372?hl=en)_

Ok ... size matters ... Assuming that's true, how could this regression have been avoided?

It's unrealistic to expect devs to stay on top of all the nuances in platform version changes. This is where continuous monitoring comes in. If measurement is manual, regressions won't consistently be caught before reaching production.

![Slack message to Emerge Tools about size increase due to Xcode 14](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog10%2Ffirst-message.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Above is a Slack from one of our customers asking about their app size increase after switching to Xcode 14. They caught the regression before their release with the help of Emerge's continuous integration tooling.

The bitcode deprecation that happened as part of Xcode 14 is certainly an extreme example of app size regression. However, we find that smaller regressions happen all the time, whether it be from an SDK update or a new feature. Over time these changes accumulate into a noticeably worse user experience, which is all the more reason to be proactive about your app size.
