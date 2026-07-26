---
title: Dive into React Native performance
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2016/03/28/android/dive-into-react-native-performance/'
original_language: en
published: 2016-03-28
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:02e86a03bb803c79'
translated: false
---

> 原文：[Dive into React Native performance](https://engineering.fb.com/2016/03/28/android/dive-into-react-native-performance/)　·　Meta Engineering — iOS

[React Native](https://facebook.github.io/react-native/) allows you to build iOS and Android apps in JavaScript using [React](https://facebook.github.io/react/) and [Relay](https://facebook.github.io/relay/)‘s declarative programming model. This leads to more concise, easier-to-understand code; fast iteration without a compile cycle; and easy sharing of code across multiple platforms. You can ship faster and focus on details that really matter, making your app look and feel fantastic. Optimizing performance is a big part of this. Here is the story of how we made React Native app startup twice as fast.

## Why the hurry?

With an app that runs faster, content loads quickly, which means people get more time to interact with it, and smooth animations make the app enjoyable to use. In emerging markets, where [2011 class phones](https://engineering.fb.com/posts/952628711437136/classes-performance-and-network-segmentation-on-android/) on [2G networks](https://newsroom.fb.com/news/2015/10/news-feed-fyi-building-for-all-connectivity/) are the majority, a focus on performance can make the difference between an app that is usable and one that isn’t.

Since releasing React Native on [iOS](https://facebook.github.io/react/blog/2015/03/26/introducing-react-native.html) and on [Android](https://engineering.fb.com/posts/1189117404435352/react-native-for-android-how-we-built-the-first-cross-platform-react-native-app/), we have been improving list view scrolling performance, memory efficiency, UI responsiveness, and app startup time. Startup sets the first impression of an app and stresses all parts of the framework, so it is the most rewarding and challenging problem to tackle.

## Always be measuring

We converted the Events Dashboard feature in the [Facebook for iOS](https://itunes.apple.com/app/facebook/id284882215) app to React Native (navigate to the **More** tab in the app and tap **Events** to see it). This was the perfect candidate for testing performance because the native product was already highly optimized and provided a typical “interactive list of items” experience.

![](https://engineering.fb.com/wp-content/uploads/2016/03/GBZ5wQDCizZf8yYEAEM_gjcAAAAAbj0JAAAB.jpg)

<sub>Fig. 1: The Events Dashboard screen</sub>

Next, we set up an automated [CT-Scan](https://engineering.fb.com/posts/924676474230092/mobile-performance-tooling-infrastructure-at-facebook/) performance test that helped us navigate to the rightmost tab, which then opens and closes the Events Dashboard 50 times. During each of these iterations, we are able to measure the time it takes from tapping the Events button to events being visible on the screen. We also added more detailed performance markers to give us a good idea of which steps in the startup process were slow and taking up CPU time.

Here is an overview of some of the steps we are measuring:

1. **Native Initialization:** Initialize the JavaScript virtual machine and all the [native modules](https://facebook.github.io/react-native/docs/native-modules-ios.html) (disk cache, network, UI manager, etc.).
2. **JS Init + Require:** Read the minified JavaScript bundle file from disk and load it into the JavaScript virtual machine, which will parse it and generate bytecode as it requires the initial modules (mostly [React](https://facebook.github.io/react/), [Relay](https://facebook.github.io/relay/), and their dependencies).
3. **Before Fetch:** Load and execute the Events Dashboard application code, build the [Relay](https://facebook.github.io/relay/) query, and kick off reading from the on-disk cache.
4. **Fetch:** Fetch data from the on-disk cache.
5. **JS Render:** Instantiate all the React components and send them to the native UI manager module for display.
6. **Native Render:** Calculate view sizes by computing the [FlexBox](https://facebook.github.io/react-native/docs/flexbox.html) layout on the shadow thread; create and position the views on the main thread.

![](https://engineering.fb.com/wp-content/uploads/2016/03/GEF5wQCX-cXZUeEAADQ_6S4AAAAAbj0JAAAB.jpg)

<sub>Fig. 2: Events Dashboard startup performance</sub>

Our golden rule from then on: Never regress the test. We run it continuously to track performance improvements and regressions, and developers can run it on a specific commit to get a detailed performance analysis before pushing the change. Other tests have been set up to measure scroll performance and memory usage in the same way.

## What happens on startup

With automated performance tracking in place, we needed a tool that could give us more details on what exactly needed improvement during startup. We added detailed start/stop performance markers throughout our frameworks, collected the data, and used the [catapult viewer](https://github.com/catapult-project/catapult/tree/master/tracing) to identify hot spots and blocking interactions across threads. You can trigger profiling on your app from the [developer menu](https://facebook.github.io/react-native/docs/debugging.html).

With React Native, your code is executed on the JavaScript thread. Whenever you want to write data to the disk, make a network request, or access any other native resource (like the camera), your code needs to call a native module. When you render your components with React, they will be forwarded to the UI manager native module, which will then perform layout and create the resulting views on the main thread. The [bridge](http://tadeuzagallo.com/blog/react-native-bridge/) will forward your call to the module and call back to your code, if needed. In React Native, all native calls have to be asynchronous to avoid blocking the main thread or the JS thread.

In the below Events Dashboard startup visualization, we can see that the app, which is running on the JS queue, triggers a cache read for the events to be displayed, which is triggered on the async local storage queue. Once it gets the cached data back, the app renders the events cells on the JS queue with React, which then passes it on to the shadow queue for layout and finally to the main queue for view creation. This example shows multiple cache reads (using one common read operation may be faster) and a few React render operations on the JS thread that might be consolidated.

![](https://engineering.fb.com/wp-content/uploads/2016/03/GCefvQD26BsmvqsAAFRTmREAAAAAbj0JAAAB.jpg)

<sub>Fig. 3: Events Dashboard startup visualization</sub>

## Performance improvements

Here are a few of the most significant efficiency and scheduling improvements we have made to reach our results, with links to the relevant commits.

### Doing less

[Cleanup Require/Babel helpers](https://github.com/facebook/react-native/commit/b90fe8e2e8fd173498c268abf39a21b665e019ed) (high impact): Removes helper code executed during require() that was specific to our website and not needed for React Native.

[Avoid copying and decoding strings when loading the bundle](https://github.com/facebook/react-native/commit/f5670f8ab5cd045402ed037ade372c182902d19e) (medium impact): Passing a UTF-8 string to the [JavaScriptCore](http://trac.webkit.org/wiki/JavaScriptCore) virtual machine will cause it to trigger a slower conversion to UCS-2 format. Encoding it in ASCII format instead will avoid the conversion. Getting rid of the [intermediate NSString representation](https://github.com/facebook/react-native/commit/4a3857ef1dc073f4a58274b77e7f775ca81b39dd) also improves performance by avoiding one more conversion. We discovered these improvements through extensive benchmarking of the bundle loading step.

[Stripping DEV-only modules](https://github.com/facebook/react-native/commit/7a794cc72bf5c2ea6da4dbda3a452bafc2997885) (low impact): Unlike compiled code, JavaScript doesn’t have a preprocessor that can strip debugging features in release mode. Using a [Babel](https://babeljs.io/) transform, we were able to remove code living behind ` __DEV__` statements, effectively reducing bundle size, which improves JavaScript parse time.

**Generate event descriptions on the server** (low impact): Instead of fetching data to generate a sentence describing which friends are coming to an event, generate it on the server, which reduces the data we have to receive and parse, and avoid all the client-side processing to generate the sentence.

### Scheduling

[Lazy requires](https://github.com/facebook/react-native/commit/d088750163bd45cb60c4c6796ed97624fb6f91bf) (low impact): Instead of executing all JavaScript module require calls up front, trigger a require call only the first time we need it. This optimization effectively avoids requiring modules that are never used, and [it has also proved to be successful on the web](https://www.youtube.com/watch?v=SnAq9tbeRm4).

[Relay incremental cache read](https://github.com/facebook/relay/commit/cc7c0e5b16999e045937a5f75a4ef0fe05b4695e) (high impact): Relay was initially written for the web and had only an in-memory response cache. The first on-disk response cache was reading the entire cache from the disk. By reading only the content required to fulfill a particular query, we significantly reduced the I/O overhead and native-to-JS bridge traffic.

[De-batching bridge calls, batch Relay calls](https://github.com/facebook/react-native/commit/31f9a690f3b3524adf08aa9d8c01843e8524453e) (high impact): We initially thought that sending JS calls to native in batches would reduce the overhead of calling over the native-to-JS bridge, but performance analysis showed the overhead of JS calls to native was not a bottleneck: In fact, delaying UI or cache read calls to batch them with later calls also delayed work on the native thread, which harmed performance. In other cases, like the Relay cache read fetching data for multiple keys, [batching](https://github.com/facebook/react-native/commit/a64ee7d8c5b717051f0659bf25ec38a8bd583d54) proved to be a significant improvement.

[Early UI flushing](https://github.com/facebook/react-native/commit/c25c98c00c8c195f85c9fb17eae3cb0c36b465f5) (low impact): We also batched UI updates to enforce consistency, but sending layout commands as soon as they are ready proved to be more efficient because the native UI manager can work in parallel with the JavaScript thread.

[Lazy native modules loading](https://github.com/facebook/react-native/commit/060664fd3d9331f062696e68179bac9cd4544a06) (low impact): Initialize a native module only the first time we use it, which avoids initializing the modules we do not need.

[Lazy touch bindings on text components](https://github.com/facebook/react-native/commit/4ce03582a0013e60417dedbf2f760d00e687e540) (low impact): Binding touch event callbacks takes a significant amount of time. Instead of doing all that work up front, we are now only binding the touch down event (when you first touch a target) and bind all the other callbacks only when you start touching the element.

**Defer popular events query** (medium impact): The first screen of information is populated by the events query, and we will then show popular events after these. Deferring that query reduces contention when populating the screen with events.

## Prepare for light-speed

A few months ago, Events Dashboard startup took two seconds on the iPhone 5. After a lot of work from the React Native Performance, React Native, React, and Relay teams in [London](https://www.facebook.com/careers/locations/london/), [Menlo Park](https://www.facebook.com/careers/locations/menlo-park/), and [New York](https://www.facebook.com/careers/locations/newyork/), Events Dashboard startup is now twice as fast. Most of the improvements we made were done at the framework level, which means your React Native app will automatically benefit when migrating to the latest version of React Native.

These improvements are just the beginning: We continue to work on making every part of the stack faster, from JavaScript parse time to data-fetching performance. And [you can contribute](https://github.com/facebook/react-native), learn how to [make your apps faster](https://www.youtube.com/watch?v=0MlT74erp60), and ask any questions you may have in our [community](https://www.facebook.com/groups/react.native.community/)!
