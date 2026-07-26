---
title: 'Emerge Tools Blog | Dogfooding Emerge Tools: Open-sourcing an Android Hacker News App'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:aaadafca6dec0503'
translated: false
---

> 原文：[Emerge Tools Blog | Dogfooding Emerge Tools: Open-sourcing an Android Hacker News App](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app)　·　Emerge Tools Blog

# Open-sourcing an Android Hacker News App

September 4, 2024 by

[Ryan Brooks](https://twitter.com/rbro112)

AndroidFeaturedOpen Source

![Open-sourcing Emerge Tools Hacker News App for Android](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.df7289b8.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Dogfooding | verb

_A company's use of its own product, as a way of testing and helping to improve it._

You might have heard the term "dogfooding" before. I first heard it in a famous [2013 post about Facebook](https://www.fastcompany.com/3012670/how-proper-dogfooding-might-have-saved-facebook-home). The term comes from "eating your own dog food", or using your own product as your real users would.

Emerge's team has a deep background in mobile apps. We bring years of experience from companies like Google, Apple, Airbnb, Amazon, Stripe, Uber & more. We know the pains of building for iOS and Android at scale.

In our first few years, we've already built a suite of tools to solve many mobile app developer headaches, from [Size Analysis](https://docs.emergetools.com/docs/what-is-app-size)to [Snapshots](https://docs.emergetools.com/docs/snapshot-testing) to our newest tool [Reaper](https://docs.emergetools.com/docs/reaper), which detects and deletes dead code. [Many of the best apps in the world are already built using our tooling.](https://www.emergetools.com/case-studies)

But we're a dev tool company, and other than our own individual experiences, our company hasn't had an actual app on any stores to test our products on... until now.

We're thrilled to **release Emerge's first app, [Hacker News](https://play.google.com/store/apps/details?id=com.emergetools.hackernews)** for Android 🎉

## [Introducing Hacker News for Android](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#introducing-hacker-news-for-android)

We partnered with [Supergooey](https://www.supergooey.dev/) to build **a free, open-source Hacker News client for Android.**

![Hacker News Android App Screenshots](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog24%2Fapp-store-screenshots.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

There are a few reasons we're building and maintaining Hacker News:

### [Dogfooding Emerge's suite of products](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#dogfooding-emerge-s-suite-of-products)

Hacker News lets us be users of Emerge. We can again personally experience the highs and lows of making and shipping an app to prod, connecting closer with the indie dev community, and using & improving Emerge along the way.

Hacker News was built using Emerge's products from the start. We were able to monitor every major change, like using Size Analysis to see the [impact of adding Sentry](https://github.com/EmergeTools/hackernews/pull/92/checks?check_run_id=28119115664), or easily reviewing [significant UI changes](https://github.com/EmergeTools/hackernews/pull/120/checks?check_run_id=28843413519) with Snapshots.

We used Reaper, our SDK to find dead code, during our internal testing and found an unexpected benefit. During the testing, we saw what classes had been used, as well as the classes that had never been touched. We saw certain code that never been tested and were able to quickly try it out. In one case this even helped us find a crash and report it 👀.

#### Testing New Products and Features

Dogfooding our existing products was valuable, but it may be even more helpful when testing brand new products and features. It allows us to experiment with ideas that would otherwise require a greater deal of polish.

As an example, we were able to try a brand new feature with Hacker News. We talk to all different types of mobile teams, from indie to enterprise. A common problem we kept hearing was the time and effort it took to create app store screenshots. In our mind, we want a tool that's:

- Minimally invasive
- Leverages existing code

Our Snapshots product already uses Compose Previews as the basis for snapshot testing. We added a [single-line annotation](https://github.com/EmergeTools/emerge-android/blob/main/snapshots/snapshots-annotations/src/main/kotlin/com/emergetools/snapshots/annotations/EmergeAppStoreSnapshot.kt) to mark a preview as an App Store screenshot.

```kotlin
@EmergeAppStoreSnapshot
@Composable
fun BookmarksScreenAppStorePreview() {
  ...
}
```

We then spun up a basic UI to create an app store screenshot: selecting the correct preview, manipulating on a canvas, choosing a background color, and adding markdown text.

This is exactly the type of testing that building and maintaining Hacker News allows us to do. While there are some rough edges in our earliest version, we found an idiomatic approach to app store screenshots helpful and are excited to build it out further. All screenshots for the app in the Play Store were made using this new tool, which we'll be rolling out for all our users soon.

In addition to testing out a potential new product, we were also able to test out new features, like our Network Monitoring for Performance Analysis.

![Network Monitoring in Performance Analysis for Hacker News' Network Calls](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog24%2Fperf-network.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

### [Building & shipping a high-quality native app](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#building-and-shipping-a-high-quality-native-app)

Our ultimate goal with Hacker News is simple: to build and maintain a top-tier native Android app.

We truly believe a native Android & iOS experience stands out compared to non-native approaches and we want to highlight that with HN.

We also want this app to serve as an example, in both code and design, for building and shipping a modern Android app.

### [Living Documentation](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#living-documentation)

How can you set up Emerge? What does a product look like when it's fully implemented? There's no replacement for a living example and Hacker News is that for Emerge.

## [Why Hacker News?](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#why-hacker-news)

The Hacker News community has been a huge part of our journey. We've hit the front page numerous times and that exposure has been tremendous in helping to bring eyes to our products.

By providing a high-quality, fully-featured Hacker News reader, we hope to give back to the users who've helped us grow, learn, and build.

By keeping the project open-source, we're opening the door for anyone to contribute & learn from the work we're doing. It won't be perfect, but we hope building in the open will help us share the journey of building a high-quality mobile app.

Not to mention, it's also just fun to have a nice Hacker News client. While we were submitting the app to the Play Store, Emerge made it to the front page of Hacker News for our [Twitter thread](https://x.com/emergetools/status/1828490449881047401) ([Unroll link](https://unrollnow.com/status/1828490449881047401)) on the Oral-B app. It was pretty cool to see us trending on Hacker News on our own Hacker News app 🤓

![Emerge Tools trending on Hacker News for the Oral-B app Twitter thread](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog24%2Fhn-top.png&w=640&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [Long term plans](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#long-term-plans)

Our plan isn't to just release an app and be done. We have some big plans for Hacker News.

### [Preview-driven testing](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#preview-driven-testing)

One focus of our development process is a paradigm we're piloting: _Preview-driven testing_.

We hope to cover a majority of app code & edge cases with native Compose Previews. This approach not only helps us test features early but also ensures that our UI remains consistent and high-quality across updates.

And combined with Emerge's snapshot testing tools, we also hope to add a rock-solid layer of UI and functional testing, without any other complicated testing methods.

We'll be sharing more about this philosophy in a future post.

![Snapshots status check for Hacker News](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog24%2Fsnapshots-check.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Snapshots status check for Hacker News

![Snapshots UI for Hacker News](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog24%2Fsnapshots-ui.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

### [Leveraging Reaper to build the most minimal app possible](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#leveraging-reaper-to-build-the-most-minimal-app-possible)

Reaper is an SDK for finding dead code using production data. As Emerge's newest product, we want to ensure the utmost quality, so Hacker News has Reaper fully integrated from day one.

![Reaper data for Hackernews](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog24%2Freaper.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

We plan to leverage the reaper reports to trim back unused code & resources, combined with our size tooling to validate those removals.

Our goal is to ship the most minimal app possible and share how we do so using Emerge's tooling.

### [Become the #1 Hacker News reader on the Play Store](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#become-the-best-example-android-project)

Like what [Apollo was to Reddit (RIP)](https://www.emergetools.com/deep-dives/apollo), we want Emerge's Hacker News for Android to become the go-to Hacker News reader for anyone who wants to read HN on mobile.

We're confident that we can reach that goal by focusing on quality, usability, and continuous improvement.

### [Be the best example Android project](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#be-the-best-example-android-project)

Here's my hot take: the Google-published [Now in Android example](https://github.com/android/nowinandroid) is a behemoth. Any new developer diving into that codebase could feel overwhelmed and deterred from Android development, not encouraged like we'd want them to be!

We want Hacker News for Android to be an example of how to build a high-quality Android app using modern tools and practices, without drowning in complexity.

## [How you can help](https://www.emergetools.com/blog/posts/open-sourcing-emerge-tools-hackernews-app#how-you-can-help)

Try it out, and let us know what you think! [Hacker News is available on the Play Store to download now](https://play.google.com/store/apps/details?id=com.emergetools.hackernews).

Got feature recommendations or ideas? Let us know by submitting your feedback [here](https://forms.gle/YYno9sUehE5xuKAq9).

And since Hacker News is completely open-source, check out [the repository](https://github.com/EmergeTools/hackernews) and feel free to open pull requests with new features.

And before you ask, we do have plans for iOS 😉 - more on that in the future.

🚀

If you want to use the tools we used to build Hacker News Android on your own app, Emerge Tools is free for open-source projects and has indie and enterprise [pricing tiers available](https://www.emergetools.com/pricing).
