---
title: '@Scale 2014: Recap of Mobile Track'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2014/10/02/android/scale-2014-recap-of-mobile-track/'
original_language: en
published: 2014-10-02
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:93d467740edf81f5'
translated: false
---

> 原文：[@Scale 2014: Recap of Mobile Track](https://engineering.fb.com/2014/10/02/android/scale-2014-recap-of-mobile-track/)　·　Meta Engineering — iOS

It's never been a more exciting time to be a software developer. Two billion people — over a quarter of the entire human race — can access, with a single tap of a screen, software on smartphones, devices that would have been considered magic just a few decades ago.

However, with this new world comes new technical challenges. Consumers are demanding native experiences and are voting with their usage. Only 14% of time spent on mobile devices remains within the browser, according to mobile app analytics firm Flurry.

Writing these native applications is more challenging than their web-based predecessors. These apps are highly stateful, long-lived, multithreaded, and have a less flexible deployment model. We as engineers must build abstractions, tools, and methodologies to address this new post-Web world.

This technical challenge was the focus of the @Scale 2014 mobile track. Hearing from companies across the industry — Dropbox, Facebook, LinkedIn, Uber, and Microsoft — we learned about topics spanning from cross-platform native development, to addressing the needs of Android users in emerging markets, to using techniques like functional programming to make life easier for product developers in these increasingly complex applications.

## Presentation Summary and Videos

**Facebook’s iOS Architecture**

Adam Ernst and Ari Grant started the conference by discussing two novel aspects of the Facebook iOS architecture. Adam discussed the Facebook's initial adoption of Apple's Core Data, and then our need to replace it with a custom persistence layer more suited to Facebook's needs. Ari then took over and described a new view architecture, named Components, that uses declarative and functional programming principles. This system dramatically reduced the amount of code for the News Feed UI and presented a less error-prone programming model to Facebook's product developers.

**Practical Cross-Platform Mobile C++ Development**

Alex Allain of Dropbox discussed how the company has been able use C++ to build much of the Dropbox app to be cross-platform, while still preserving the native UI look and feel that customers demand. He also covered improvements in C++, C++ 11, and C++14, which are step function improvements in ease-of-use for engineers.

Andrew Twyman followed up with an in-depth look at networking and HTTP differences across platforms. He also introduced Djinni, an incredibly useful tool designed to ease the pain of bridging between shared C++, Objective-C, and Java, generating common interfaces using specific patterns and lifting the burden of writing laborious JNI code. This framework is open-sourced and available on [Github](https://github.com/dropbox/djinni).

**Unbundling and Its Impact on Mobile and Web Architectures**

LinkedIn’s Kiran Prasad explored the evolution of LinkedIn and its mobile app, which has been growing since 2010. He highlighted the transition from HTML5 to native languages; standardizing the company on Rest.li, a framework created for developing RESTful services at scale; process improvements such as regularized, timed releases; and other transitions required as the company grew from dozens to hundreds of engineers.

**Speeding Up Android Development with Exopackage**

David Reiss explained Facebook’s Android build tool, Buck, and its role in Android development, which allows programmers to build their app — whether it be large or small — more quickly and efficiently. Exopackage evolved from Buck and is able to deliver what most Android developers would consider the impossible: four-second build and install time for their app during development.

**Scaling a Mobile-Only Company**

Uber’s expansion can be summed up best by Paul Holden, mobile platform lead: “Treat every city like a startup.” He discussed the growth of Uber and how the mobile team was able to scale the app in more than 200 cities in over 20 countries. He then explored the changes the company took on for each city to maximize use and work within different legal systems.

**Microsoft Office Cross-Platform Architecture**

Igor Zaika, distinguished engineer for Microsoft Office, focused on how Microsoft uses C++ to deliver Office applications across Windows, Apple, Android and web platforms after 30 years of innovation. Office is one of the oldest and most complex software systems ever written, with innumerable features and code that has been live since 1983. This code, which initially targeted computers loaded with MS-DOS and 5 MHz processors, still lives and executes on your mobile devices 40 years later — a true engineering achievement. Igor vividly discussed this evolution and how this C++ lives on in the core of Office on every platform, with new native UX built on top of this shared core.

**Scaling Android Apps for Emerging Markets**

Building Android apps for emerging markets, where more than 10,000 different Android device models access Facebook regularly, is a unique technical challenge. Those user constraints are completely different from those of most software developers who work in the developed world. Chris Marra talked about how Facebook redesigned the Android app to work in this environment of fragmentation, poorly performing devices, small screens, and limited data plans.

Andrew Rogers then spoke about image download size, network quality detection and prefetching content, which allows Facebook users to get the best experience they can get with bytes they pay for. Tyler Kieft finished the session by talking about Instagram’s redesign for older phones, which simultaneously improved the design for Android and allowed for engineering improvements.
