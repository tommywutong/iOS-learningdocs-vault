---
title: 'Emerge Tools Blog | Announcing Emerge’s Android Performance Testing Suite'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/announcing-android-performance-testing'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:0ff168d13694b35c'
translated: false
---

> 原文：[Emerge Tools Blog | Announcing Emerge’s Android Performance Testing Suite](https://www.emergetools.com/blog/posts/announcing-android-performance-testing)　·　Emerge Tools Blog

# Announcing Emerge's Android Performance Testing Suite

February 1, 2023 by

Nathanael Silverman

AndroidPerformance

![Graphic logo announcing Emerge's Android Performance Testing Suite](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog13.785cce2f.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Useful performance testing is controllable, user-impacting, and reproducible. At Emerge, our cross-platform tooling has helped popular apps with millions of users [improve app launch](https://doordash.engineering/2023/01/31/how-we-reduced-our-ios-app-launch-time-by-60/) and fix regressions before ever reaching production. Here's a look at our Android performance tooling.

## [How it Works](https://www.emergetools.com/blog/posts/announcing-android-performance-testing#how-it-works)

One of the biggest challenges with performance testing is reaching statistical significance. The speed of critical application flows (like app launch) can be impacted by many factors: a device's thermal state, battery, network conditions, disk state, etc. This all contributes to a high degree of variance in testing, making it difficult to reach confident conclusions.

Emerge isolates each performance test on a dedicated, real device. Conditions like the CPU clock speed, battery, network and more are normalized. The same test is run up to a hundred times, alternating between app versions to detect differences.

![Chart showing values of 80 test iterations that make up the result of one Emerge's performance tests.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog13%2Fbuild-details.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Tests are run on a head and base build until a statistically significant conclusion can be reached

**The result is a 99% confidence interval about whether a specific code change has improved, regressed or had no impact on the flows being tested**. A [differential flame chart](https://docs.emergetools.com/docs/performance-visualizations#differential-flame-graph) is generated to easily pinpoint the functions that contributed to the change:

![Differential flame chart showing a regression between two builds](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog13%2Fflamechart-diff.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Differential flame chart showing a regression between two builds

This blog walks through the process of setting up Emerge performance testing on Firefox (open-source) and comparing flows across builds.

## [Adding Emerge to Firefox](https://www.emergetools.com/blog/posts/announcing-android-performance-testing#adding-emerge-to-firefox)

Our first step is to apply and configure the [Emerge Gradle plugin](https://docs.emergetools.com/docs/gradle-plugin):

```kotlin
1// Top-level build.gradle
2
3plugins {
4  id("io.gitlab.arturbosch.detekt").version("1.19.0")
5  id("com.emergetools.android").version("1.2.0")
6}
7
8emerge {
9  appProjectPath = ':app'
10  apiToken = System.getenv("EMERGE_API_KEY")
11}
12
```

With the Gradle plugin, we can use `./gradlew emergeUploadReleaseAab` to easily upload a build.

![Visualization of the Firefox build in Emerge](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog13%2Femerge-build.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Visualization of the Firefox build in Emerge

Now that we have a build let's run our first app launch test!

## [Comparing App Launch Across Builds](https://www.emergetools.com/blog/posts/announcing-android-performance-testing#comparing-app-launch-across-builds)

Emerge's Performance Analysis tooling centers around the ability to accurately compare performance flows for any two builds. Comparisons are used to:

- Highlight and quantify performance improvements
- Catch regressions prior to merging
- Trace issues to the change that introduced them

To demonstrate, we made a simple code change that adds an SDK to be initialized during application creation.

```kotlin
1open fun setupInMainProcessOnly() {
2  // …
3  setupLeakCanary()
4  startMetricsIfEnabled()
5  setupPush()
6  migrateTopicSpecificSearchEngines()
7  MockSdk.initialize()
8  // …
9}
10
```

Builds can be automatically compared in your CI workflow or you can use our Compare page to start an ad-hoc comparison between any two builds. By default, you can run an app launch test on any build using time to initial display as the marker (we'll walk through running custom tests later). In this case, we'll upload the new build of Firefox and kick off an App Launch comparison.

![Comparing two builds on Emerge](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog13%2Fcomparison.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Comparing two builds on Emerge

Every performance test will return

- An overall conclusion to show how the two builds compared
- A differential flame chart, showing where changes occurred (if any)

![Page faults during app launch for Robinhood iOS app](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog13%2Ftest-conclusions.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Example of an improved, regressed, or unchanged test conclusion.

For our differential flame charts, each frame in the head build is compared to the corresponding frame in the base build. The relative and absolute difference is calculated as the difference between each frame. Frames are colored red to indicate a regression and green for an improvement.

In the Firefox app launch comparison, we see the overall app launch duration increased by 25.5%. Diving into the flame chart, we can "follow the red" down the call stack to trace the regression to MockSdk.initialize.

![GIF tracing a regression in app launch to the newly added MockSdk.initialize()](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog13%2Fandroid-sdk-initialize.gif&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

GIF tracing a regression in app launch to the newly added MockSdk.initialize()

Maybe we initialize this new SDK asynchronously, or maybe it's important enough that it's worth slowing down the app launch. In any event, using Emerge can help ensure that important performance changes are always measured and intentional. This brings us to…

## [Custom Performance Tests](https://www.emergetools.com/blog/posts/announcing-android-performance-testing#custom-performance-tests)

App launch speed is very important but it's generally not the only flow that has an impact on UX. Let's write a custom performance test for another flow in the Firefox app: when a user taps the address bar, enters a URL and waits for it to load.

Let's create a new Gradle subproject for our tests. First, we'll choose a path for it:

```kotlin
1// Top-level build.gradle
2
3emerge {
4  appProjectPath = ':app'
5  // arbitrary name b/c project doesn't exist yet
6  performanceProjectPath = ':performance'
7  apiToken = System.getenv("EMERGE_API_KEY")
8}
```

Next we'll let the Emerge Gradle plugin generate the subproject for us:

```shell
./gradlew emergeGeneratePerformanceProject \
  --package org.mozilla.fenix.performance
```

This creates and configures the project for us, including an example test:

![Directory hierarchy generated by `emergeGeneratePerformanceProject` command](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog13%2Fperf-dir.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge subproject with an example performance test

Emerge uses 3 annotations, similar to JUnit, in order to configure custom performance tests: **@EmergeInit**, **@EmergeSetup** and **@EmergeTest**. The example test explains how they work in detail, but here's a quick overview:

### [@EmergeInit](https://www.emergetools.com/blog/posts/announcing-android-performance-testing#emergeinit)

@EmergeInit runs once per app install. Typically this is used to login in order to test flows for registered users. With Firefox we don't need to login in order to test loading a webpage so we can skip this function entirely.

### [@EmergeSetup](https://www.emergetools.com/blog/posts/announcing-android-performance-testing#emerge-setup)

@EmergeSetup runs once before each test iteration. This is meant to get the app in the right state before beginning the performance recording. In this case we want to measure the performance of loading a webpage, not launching the app and then loading a webpage, so we'll launch the app as part of the setup.

```kotlin
@EmergeSetup
fun setup() {
  val device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
  device.pressHome()
  device.wait(Until.hasObject(By.pkg(device.launcherPackageName).depth(0)), LAUNCH_TIMEOUT)
  val context = ApplicationProvider.getApplicationContext<Context>()
  val intent = 
      checkNotNull(context.packageManager.getLaunchIntentForPackage(APP_PACKAGE_NAME)) {
          "Could not get launch intent for package $APP_PACKAGE_NAME"
      }
  intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK)
  intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
  context.startActivity(intent)       
  device.wait(Until.hasObject(By.pkg(APP_PACKAGE_NAME).depth(0)), LAUNCH_TIMEOUT)
}
```

### [@EmergeTest](https://www.emergetools.com/blog/posts/announcing-android-performance-testing#emerge-test)

@EmergeTest defines the UI flow to be tested. @EmergeSetup runs prior to the test so when @EmergeTest starts we are already on the app's home screen. Our test will consist of:

- Clicking the address text field.
- Entering the address of a predetermined website.
- Pressing enter to start loading the page.
- Waiting for the progress bar to appear and disappear to indicate the page is done loading.

```kotlin
@EmergeTest
fun myPerformanceTest() {
  val device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
  device.findObject(UiSelector().text("Search or enter address")).apply {
      click()
      text = "https://www.emergetools.com"
  }
  device.pressEnter()
  device.findObject(UiSelector().className(ProgressBar::class.java)).apply {
      waitForExists(1_000)
      waitUntilGone(10_000)
  }
}
```

_Note:_ One constraint is that tests must be written with [UI Automator](https://www.emergetools.com/glossary/ui-automator), rather than frameworks like Espresso which can degrade performance during tests.

Let's try to run it locally:

![GIF the written performance test, which opens Firefox, taps the address text field, and navigates to a web page](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog13%2Ftest.gif&w=828&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

```kotlin
./gradlew emergeLocalReleaseTest
…

┌──────────────────────────────────────────────────────┐
│ org.mozilla.fenix.performance.ExamplePerformanceTest │
└──────────────────────────────────────────────────────┘
├─ No @EmergeInit method
├─ @EmergeSetup setup ✅
└─ @EmergeTest myPerformanceTest ✅
```

Running an Emerge test locally doesn't test performance, it simply ensures that performance tests can run as expected. Now that we know they do, we can test our custom flows whenever a new build is uploaded!

## [What's next?](https://www.emergetools.com/blog/posts/announcing-android-performance-testing#whats-next)

And that's it!

Our testing suite is built to control everything about the app's environment, so the only changes measured will be changes from within the uploaded app. We've abstracted away much of the difficulties of performance testing so developers can focus on maintaining meaningful tests.

There's much we didn't get to cover, like our [performance insights](https://docs.emergetools.com/docs/performance-insights), which automatically identifies and suggests performance improvements, and our [managed baseline profile](https://docs.emergetools.com/docs/baseline-profiles-android) offering.

If you'd like to learn more about Emerge's performance testing suite for your app you can get in touch with us or explore our documentation on our mobile products.
