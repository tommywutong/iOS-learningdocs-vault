---
title: 'Under the Hood: Integrating standalone mobile app features into Facebook for iOS'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2012/11/09/ios/under-the-hood-integrating-standalone-mobile-app-features-into-facebook-for-ios/'
original_language: en
published: 2012-11-09
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4392006e16622b26'
translated: false
---

> 原文：[Under the Hood: Integrating standalone mobile app features into Facebook for iOS](https://engineering.fb.com/2012/11/09/ios/under-the-hood-integrating-standalone-mobile-app-features-into-facebook-for-ios/)　·　Meta Engineering — iOS

Earlier this week we rolled out an update to Facebook for iOS that more deeply integrates the best features from two of our standalone apps, Camera and Messenger, into the core app. With over 600 million people accessing Facebook on mobile devices every month, our engineers are dedicated to making the mobile Facebook experience as fast, reliable, and feature-rich as possible.

Having mobile apps designed for the most popular mobile activities allows us to take the best features from each and cross-pollinate with our core Facebook for iOS and Android apps. However, this also introduces the challenge of deciding which features make the most sense for the core apps and figuring out how to implement them.

By retooling our development process–from making every product team responsible for their experience across desktop and mobile, to switching to native code and timed release cycles–we’ve been able to make sure the best of each standalone app is represented in the core app experience.

## One product, one team across platforms

Facebook has historically had a small, nimble engineering team with separate groups dedicated to desktop and mobile experiences. In fact, the first core iOS app was originally built and maintained by one person, and later developed by a single small team.

Within the last year, our engineering teams have taken ownership of their product experiences across both desktop and our mobile apps. These teams know their product, features, and users better than anyone and are sensitive to the nuances of developing and adapting these experiences across multiple platforms.

As a part of this evolution, the photos and messaging teams have built standalone mobile apps in addition to incorporating their features into desktop and the core apps. These apps are built to offer fast access to features people use a lot on mobile and to offer deeper standalone photos and messaging experiences.

## Standalone apps

Last year the messaging team created Facebook Messenger, a fast, feature-rich messaging app for iOS, Android, and Blackberry that makes it easy to message friends directly to their mobile phones. Several months later, the photos team built Camera, an iOS photo app that makes it easy to share photos with your friends on Facebook and see all of their photos in one place.

Apps like Messenger and Camera let us push the envelope with specific features and allow us to get feedback from specific audiences like photo experts and hard core messaging users. The highly engaged users of these apps are a great proving ground for next-generation features that are refined and tweaked in the standalone apps before potentially making a debut in the core app.

Having a single team own the product experience in their standalone apps as well as the integrated experience in the core app means that we have more thoughtfully-executed experiences across platforms and applications.

We can do this kind of fast, adaptive sharing across apps because we’ve retooled our mobile development process with a focus on native code and timed release cycles.

## How we share

Several months ago we launched a [new native iOS app](https://www.facebook.com/notes/facebook-engineering/under-the-hood-rebuilding-facebook-for-ios/10151036091753920), which made it possible for our apps to share a codebase and integrate features from the standalone apps into the core apps. For example, in the latest release of the core iOS app, we’ve integrated two of our most successful standalone app features–left swipe access to chat from Messenger and the ability to select multiple photos to upload from Camera–into iOS 5.1.

We’ve also moved to a [timed release cycle](https://www.facebook.com/notes/facebook-engineering/timed-releases-for-mobile-apps/10151078442213920), where apps get more updates and features have the ability to launch sooner. For example, we launched our last Messenger for Android update and Facebook for Android update (which incorporated features from Messenger) on the same day.

Not every feature from the standalone apps makes sense for the core app, so as the Facebook for iOS PM, one of my jobs is to make sure that the features we share across apps result in the best user experience. So while the swipe gesture to reveal the camera roll works really well within the Camera app – we chose not to include this in the core app because the gesture doesn’t make sense with our persistent top navigation bar. To make it into the core app, a feature has to add significant value to the integrated experience, regardless of how critical it is in one of our standalone apps.

The core app is not just composed of features from standalone apps – there are many teams that own key portions of the core app and continue to iterate on them. Timeline, Groups and Events are sections that are completely owned and maintained by their respective teams.

As we continue to develop Facebook across platforms, we will continue to use our standalone apps to push the limits of each product and leverage new, battle-tested features to create the best possible core app experiences on every platform.
