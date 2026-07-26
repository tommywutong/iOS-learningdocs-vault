---
title: 'Mobile @Scale — Tel Aviv recap'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2018/12/06/android/mobile-scale-tel-aviv/'
original_language: en
published: 2018-12-06
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bbfb09f7fadf0950'
translated: false
---

> 原文：[Mobile @Scale — Tel Aviv recap](https://engineering.fb.com/2018/12/06/android/mobile-scale-tel-aviv/)　·　Meta Engineering — iOS

Recently, we hosted [Mobile @Scale](https://atscaleconference.com/events/mobilescale-tel-aviv/), an invitation-only technical conference for engineers working on large-scale mobile applications. The first-ever @Scale event in Tel Aviv attracted more than 300 attendees to hear talks on topics such as the efficiency of tools and teams, and techniques for the challenges inherent in scaling apps. The conference featured technical deep dives from engineers at Automattic, Facebook, Gett, Google, and Houzz to share their hands-on experience dealing with these topics. Summaries and videos of some of the presentations are below.

If you’re interested in joining the next event, visit the [@Scale website](https://atscaleconference.com/) or join the [@Scale community](https://www.facebook.com/atscaleevents/).

## Learnings for scaling mobile dev at Facebook  
 Joey Simhon, Engineering Director, Facebook

As Facebook has scaled mobile development from HTML5 to native development, from dozens of engineers to thousands, from one app to a family of apps, and has grown to serve 2.5 billion people around the world, we’ve learned so much. In this talk Joey shares some of the key learnings around the importance of performance.

## Mobile development process automation  
 Felix Krause, Tech Lead for fastlane, Google

Felix talks about leveraging existing open source infrastructure to build powerful tools to automate your mobile development processes. This includes topics like accessing the new Apple and Google Play APIs, isolating development dependencies, optimizing your deployments, how to deal with localized screenshots, and code signing at scale.

## Building for emerging markets  
 Eli Ganim, Engineering Manager, Facebook

Emerging markets will account for over 90 percent of new mobile subscribers globally by 2020. If you’re not currently building your products with these users in mind, you’re missing out on a huge growth lever. In this talk, Eli describes the characteristics of these markets, the challenges his team faced when building Facebook Lite, and their biggest wins. You’ll hear about common assumptions that don’t hold in emerging markets and learn some dos and don’ts.

## Using mobile to help your business  
 Guy Shaviv, GM and Mobile Development Manager, Houzz Israel

Mobile technology offers many unique and interesting ways to help you advance your business goals. Learn how Houzz has used the capabilities that mobile offers to support its business, how Houzz thinks about mobile, what special mobile capabilities Houzz has used in the past, and the impact they’ve had on its business.

## Don’t miss the train: Shipping apps and beyond  
 Tal Kellner, Release TPM, Facebook

Each day, Facebook is updated with new features, bug fixes, and product improvements. Each day, Facebook also ships mobile apps to billions of mobile devices around the world. Coordinating thousands of engineers, hundreds of product changes, and billions of users seems like an impossible task. Over the years, we’ve developed tools and processes that help us step up to our mission of bringing the world closer together, without breaking people’s experience when we release new versions to them.

## YOLO releases considered harmful: Running an effective mobile engineering team  
 Cate Huston, Mobile Lead, Automattic

Organizations often worry about their mobile teams. Sometimes they are a bit separate. There’s often an inexplicable hostility toward mentions of React Native. Why do bug fixes take so long to get to production, and what are all these certificates for, anyway? Cate covers the realities of shipping compiled code, the woes of the app stores, and the infrastructure challenges we haven’t yet figured out. You’ll leave with a better understanding of the realities your mobile teams may be struggling with and some strategies for how to help them. And how to help your organization build an effective mobile team that ships regularly. And, yes, you’ll finally understand the React Native argument, too.

## Keeping Lite light: Techniques for keeping our APK as small as ~1MB  
 Dekel Naar, Software Engineer, Facebook Lite Performance Team, Facebook

Facebook Lite is a lightweight version of the Facebook app that’s targeted to emerging markets. We observed that as APK size grows, its install rates drop, especially in emerging markets where phone resources are low. Dekel covers some of our efforts to keep our APK as small as possible. Dekel discusses the way we approach the problem, projects that we delivered to achieve our goal, and more.

## Reactive extensions for mobile apps: Getting started  
 Shai Mishali, iOS Tech Lead, Gett

Reactive applications have been extremely popular in all fields of programming: web apps, back end, and, of course, mobile applications! In this talk, Shai covers the building blocks of reactive extensions and reactive programming, and how you can leverage these concepts and techniques in your own applications across platforms.

## Flipper: An extensible mobile app debugger  
 Daniel Buchele, Front End Engineer, Facebook

Flipper is an open source debugging tool that helps mobile developers get a better understanding of what is happening inside their apps. The built-in features allow inspecting and changing the layout hierarchy on the fly, debugging network requests, and much more. But where Flipper becomes really powerful is when building custom plugins to visualize the app’s business logic.

![Speakers at the first @Scale event in Tel Aviv.](https://engineering.fb.com/wp-content/uploads/2018/12/telaviv.jpg)
