---
title: Building a faster Messenger
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2013/11/13/android/building-a-faster-messenger/'
original_language: en
published: 2013-11-13
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4d352dee27258369'
translated: false
---

> 原文：[Building a faster Messenger](https://engineering.fb.com/2013/11/13/android/building-a-faster-messenger/)　·　Meta Engineering — iOS

A little over two years ago we launched Messenger to give people passionate about messaging a simpler and faster way to communicate with their friends. As features have been well received by our Messenger users we’ve brought them over to our core Facebook apps. As a result, the Messenger and messaging experience across Facebook became very similar.

But we wanted to bring Messenger back to its roots as a dedicated app for people who are passionate about messaging and want to be reachable at all times. When we started working on the new Messenger, we needed to create a fast and reliable mobile-to-mobile messaging experience. We focused on improving two key areas — startup time and overall speed and performance of Messenger on Android and iOS.

## Improving Startup Time

We took a step back and looked at everything running during startup that didn’t have to. For a truly mobile-to-mobile experience, you need to be able to message your contacts immediately. So our goal was to eliminate any code that wasn’t fundamental to Messenger’s startup functionality.

On iOS, we needed a tracing utility that would tell us where we were spending the most time on startup. Facebook iOS Engineer, Ben Gertzfield, wrote a wall-clock tracing system called FBTracer to identify the biggest offenders making startup slow (reading from Keychain, talking to the disk, etc.), added reporting and built dashboards to measure our performance improvements. Once we had a clear picture of everything running on the backend, we removed all the unused features or moved them to background threads, so they wouldn’t affect startup time. We also did a complete pass of all the shared code between the main Facebook app and Messenger, making sure that only what was needed for messaging was in the Messenger binary. This cleanup process was essential in improving start up time and reducing binary size.

On Android, we wrote some quick scripts that would tell us where we were spending the most time on startup but we also had some additional performance challenges to deal with that didn’t exist on iOS. We have a dependency injection framework, which (after some investigation) we found was slowing down startup time by 30%. The dependency injection framework has been a huge resource. It has allowed us to test our code at scale, and detect problems with each diff. But the cost of doing this wasn’t efficient. Facebook engineer, Michael Marucheck, had the idea to actually edit the Java byte code after compilation. We used ASM to improve our dependency injection system by detecting bindings that are safe to remove, adding static methods that instantiate a bound type, and rewriting calls to the injector to instead call the appropriate static method. By improving this process, we were able to have a well-crafted dependency injection system that lets us test at scale, but still with the 30% gain in speed.

## Performance Updates

It’s not just about startup though. We wanted to make sure the entire app was quick and lightweight. On iOS, we realized that initializing the conversation view controller was inefficient, so we started reusing the same view controller for different conversations and resetting just the relevant state. We instantiated the object while the app was idle in the inbox view so that it was ready as soon as the user selected a thread. After discovering that AVAudioPlayer::play could block the main thread as we were sending/receiving messages, we moved the sound playing to a background thread. We also spent a lot of time looking at the network requests the app was making and reducing unnecessary data-fetching. On Android, we noticed that the people page was taking too long to start up, so we optimized the contacts schema and queries for Messenger to make contact loading as fast as possible.

Regressions are inevitable, but the trick is to catch them right away. To do this, Messenger Engineer, Luiz Scheidegger, hooked up a gingerbread device and an ICS device to a Mac mini and had it run startup-timing tests on every diff, so we can catch changes in performance right away. It runs start up 40 times and gives us an average on time. We can now detect changes in startup time down to 100ms. It was good we set that up, because two days after having this running, we ran into a performance gain that we couldn’t explain. Digging into it, it turned out to be an unrelated change to our logging that caused a 400ms gain. We merged that diff into our release branch immediately and were able to see the performance gains in our release version.

## What’s Next

This is just the beginning for the new and improved Messenger. Now that we have the tooling in place to track regressions we can make sure that future features are just as fast as the new experience. We will continue to run tests on our core systems to improve speed and performance — as well as feature tests that will help guide the future of how we develop in Messenger.
