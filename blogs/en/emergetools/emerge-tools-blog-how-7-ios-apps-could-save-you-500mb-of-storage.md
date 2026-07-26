---
title: 'Emerge Tools Blog | How 7 iOS Apps Could Save You 500MB of Storage'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/7AppsThatCouldSaveYou500MB'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:5bbafa5a860511aa'
translated: false
---

> 原文：[Emerge Tools Blog | How 7 iOS Apps Could Save You 500MB of Storage](https://www.emergetools.com/blog/posts/7AppsThatCouldSaveYou500MB)　·　Emerge Tools Blog

# How 7 iOS Apps Could Save You 500MB of Storage

January 14, 2021 by

[Noah Martin](https://twitter.com/sond813)

iOSApp size

![Treemap chart showing asset sizes in an app breakdown.](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog1.fbd041bc.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [Background](https://www.emergetools.com/blog/posts/7AppsThatCouldSaveYou500MB#background)

Many mobile developers can attest to the problems of app size increase.

Sometimes it's a quick feature release with an uncompressed image that adds 5%. Sometimes it's a slow, steady increase of 0.5% each week.

I worked on these issues as a software engineer at Airbnb for 4.5 years, and in my own apps with ThnkDev. Recently, I personally analyzed over 150 apps to try to solve the issue of app size once and for all. I wanted to share my findings about common mistakes with everyone so we can all build lighter and faster apps! 🚀

## [Why?](https://www.emergetools.com/blog/posts/7AppsThatCouldSaveYou500MB#why)

Knowing exactly what goes into your app is tricky for fast moving teams, that's why **automated testing and alerts around best practices** makes apps more efficient. [Emerge](https://www.emergetools.com/) aims to do this for your apps.

App quality is always top of mind for developers and one of the most important factors is what actually gets shipped to users. However, it's not easy to validate what goes into your final .app and bugs can often slip through unnoticed. Developers can easily get into situations where duplicate files need to be kept in sync, extra code delays app startup, or file fragmentation bloats the install size. Your app's size is a user's first impression of your app, longer download times can lead to missed users or failed installs. Not to mention, uninstall rate goes up as app size increases and users look for ways to free up space on their devices.

**Experiments indicate as much as a 0.5% drop in install conversions per megabyte added.**

## [What is app size anyway?](https://www.emergetools.com/blog/posts/7AppsThatCouldSaveYou500MB#what-is-app-size)

App size can be tricky to measure, there are many places that display size which can be contradicting and enough context isn't always provided. In general there are 2 measurements to know: install and download size.

![Screenshot showing the download size of Hopper is 81 megabytes.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog1%2F1.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Install and download size for Hopper

Users most often see install size. It's on the App Store page and shown in system settings. Install size is how much storage your app takes up on a user's phone. To keep things simple in the rest of this post when we refer to size, it's install size, because we care most about what users see. **You can read all about the different ways to measure size in the [Emerge documentation](https://docs.emergetools.com/docs/what-is-app-size)**.

## [Now let's get started!](https://www.emergetools.com/blog/posts/7AppsThatCouldSaveYou500MB#now-lets-get-started)

![Dropbox IOS app logo and title, with additional text showing the app size could be reduced by around 40%.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog1%2F2.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

[https://www.emergetools.com/app/example/dropbox](https://www.emergetools.com/app/example/dropbox)

Dropbox has the most savings of any app we've measured. Weighing in at 269 MB, our tool's analysis shows **potential size reductions of 40%**. Most of this extra size is coming from duplicate localization files. As you can see from their app breakdown, each app extension has the same copy of Localizable.strings as the main app bundle, for all 21 supported languages. In addition to duplicates, the Localizable.strings files contain comments used to provide context to translators. These aren't needed in the production app, stripping comments in production would save ~46mb. With the current setup, every new language will account for about 4mb. There are a few other things that could be improved, but let's go on to some other apps.

![Spark iOS app logo and title, with additional text showing the app size could be reduced by around 45%.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog1%2F3.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

[https://www.emergetools.com/app/example/spark](https://www.emergetools.com/app/example/spark)

The Spark app is almost 10% font files. Taking a closer look at the fonts you might notice some familiar names:

- SF-Pro-Text-Semibold.otf
- SF-Pro-Text-Light.otf
- SF-Pro-Text-Medium.otf
- SF-Pro-Text-Heavy.otf
- SF-Pro-Text-Bold.otf
- SF-Pro-Text-Regular.otf

Each of these font files appear twice in the app, once in the main app bundle and once in the sharing extension. These are the default fonts included in iOS, and can be downloaded [here](https://developer.apple.com/fonts/). According to the license agreement shown when installing these fonts:

> **IMPORTANT NOTE: THE APPLE SAN FRANCISCO FONT IS TO BE USED SOLELY FOR CREATING MOCK-UPS OF USER INTERFACES TO BE USED IN SOFTWARE PRODUCTS** **RUNNING ON APPLE'S iOS, iPadOS, macOS OR tvOS OPERATING SYSTEMS, AS APPLICABLE.**

They shouldn't need to be included in any app targeting iOS 11+, as they can all use the default system font. Removing them would reduce Spark's size by ~20mb.

** Edit: Some have pointed out that the SF fonts change even in later iOS versions. There still may be some license agreement violations for using these, and even if they are needed it doesn't change the total savings for Spark which is calculated assuming the duplicate copy of the font is removed and only one is kept. **

![eBay app logo and title, with additional text showing the app size could be reduced by around 50%.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog1%2F4.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

[https://www.emergetools.com/app/example/ebay](https://www.emergetools.com/app/example/ebay)

The Ebay app has an interesting architecture where the main app's executable is only ~150kb although 86% of the app size is executable files. This is because most of their app consists of frameworks, the biggest one (34mb) is EbayApp.framework. **Almost 100mb of these frameworks are unnecessary** swift symbols. When you build a swift framework, the binary contains a symbol table which you can read with the `nm` command.

```shell
nm -m eBayApp.framework/eBayApp
...
s7eBayApp28SettingsViewControllerLegacyC13viewDidAppearyySbFTo
```

Ebay has tens of thousands of these non-external symbols. After stripping them using the method described [here](https://docs.emergetools.com/docs/strip-binary-symbols) the size is greatly reduced.

![Twitch app logo and title, with additional text showing the app size could be reduced by almost 45%.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog1%2F5.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

[https://www.emergetools.com/app/example/twitch](https://www.emergetools.com/app/example/twitch)

Just like Ebay, Twitch has a lot of size attributed to non-external swift symbols in binaries. However, Twitch also has a very large main app binary. More than half of it is the LINKEDIT segment containing the symbol table. Since this binary isn't a dynamic framework, we can be more aggressive with symbol stripping and even remove the global symbols.

![Slack app logo and title, with additional text showing the app size could be reduced by around 30%](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog1%2F6.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

[https://www.emergetools.com/app/example/slack](https://www.emergetools.com/app/example/slack)

Slack could also greatly benefit from stripping Swift symbols. They have almost 10mb of images, but could drop 3mb by using some image compression techniques or new files formats such as HEIC.

![An unnamed app logo with additional text showing the app size could be reduced by around 35%](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog1%2F7.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

An unnamed (for legal reasons) vacation rental app shows a new kind of breakdown, 18% of the app is debugging symbols in .bcsymbolmap files. These are basically dSYMs for bitcode, so they should not be shipped to users in the final product. Taking a closer look shows the files belong to TwilioChatClient.framework which is a binary SDK distributed [here](https://www.twilio.com/docs/chat/sdk-download-install#ios-sdk). The [final step of their documentation](https://www.twilio.com/docs/chat/sdk-download-install#completing-framework-integration) instructs users to run a shell script that deletes all bcsymbolmap files for release builds. The documentation says this step isn't needed to be done manually for CocoaPods integration, but we found if you don't do this the extra 20mb of files get included in your production app.

![Lyft app logo and title, with additional text showing the app size could be reduced by around 20%.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog1%2F8.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

[https://www.emergetools.com/app/example/lyft](https://www.emergetools.com/app/example/lyft)

The Lyft app has hundreds of duplicate files, the largest consumer of space is a single asset catalog copied 73 times in separate bundles. Another asset catalog that is virtually identical except for the timestamp at which it was created is copied 67 times. Each of these contain nothing but 482 colors (colors can be stored in asset catalogs to simplify management of dark mode). With each one taking ~250kb these quickly eat up 35mb.

### [And this brings our total to 536mb!](https://www.emergetools.com/blog/posts/7AppsThatCouldSaveYou500MB#and-this-brings-our-total-to-536mb)

Hopefully these case studies provide insight into common setups that lead to bloated apps and how to easily fix them.

---

Disclaimer: These apps were analyzed by the Emerge Tools team for educational purposes, they do not represent customers or endorsements.
