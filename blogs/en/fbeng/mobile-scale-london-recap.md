---
title: 'Mobile @Scale London recap'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2016/03/29/android/mobile-scale-london-recap/'
original_language: en
published: 2016-03-29
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c9cc3daca257cb5a'
translated: false
---

> 原文：[Mobile @Scale London recap](https://engineering.fb.com/2016/03/29/android/mobile-scale-london-recap/)　·　Meta Engineering — iOS

Less than three years ago, engineers from Twitter, LinkedIn, Dropbox, Pinterest, and Facebook — including two from the then brand-new Facebook London office — met at Mobile @Scale in Menlo Park to talk about the challenges of building mobile software at large scale. Last Wednesday, the first Mobile @Scale London showed how far mobile development at scale has come in only a few short years.

In 2013, a lot of the conversation was about how to adapt approaches to testing, optimising, developing, and deploying software that had worked well on the web to the new mobile platforms.

Fast-forward to 2016 — you can imagine a musical montage showing lots of hacking — and instead of the conversation being about adapting to new mobile platforms, it is now about improving mobile platforms themselves.

The nature of the conversation has also changed. In 2013, the takeaways were lessons learned. In 2016, they are tools, frameworks, and platforms that can be downloaded, installed, forked, built upon, and deployed.

Mobile @Scale London was about crossing boundaries, improving platforms, and sharing code between organisations, but as Henna Kermani highlighted in her talk about using Facebook’s open source Fresco library at Twitter, each of those collaborations started with a conversation between engineers.

After a day of listening to conversations between 300 of the smartest mobile developers, I’m excited to see what the next three years holds.

Videos of the Mobile @Scale London talks are posted below. If you are interested in joining the next event, please check out and follow the [@Scale Facebook page](https://www.facebook.com/atscaleevents).

## Scaling iOS @ Google

Michele Aiello immediately set the “crossing boundaries” theme by talking about Google building with Material Design, protocol buffers, C++, and Java on iOS: a journey which started with just one app and then scaled to more than 60.

## When mobile IDEs need to scale

James Pearce and Al Sutton talked about two very different solutions used to overcome the problems inherent in building large mobile applications. For iOS and web developers, Facebook added [Buck](http://buckbuild.com/), Babel, Chrome Tools, Flow, and Clang to the open source Atom editor running in Chromium to create Nuclide as a scalable alternative to XCode. The open source nature of IntelliJ allows Facebook to contribute to that project to optimise the IDE for Facebook, allowing Android engineers to continue to use the tool they are familiar with as Android Studio.

## 6 lessons learned scaling mobile at SoundCloud

After a delicious lunch, Jamie and Matej shared six lessons learned scaling mobile at SoundCloud, including the perils of blindly following accepted industry practice, strategies for dealing with technical debt, and a real-world example of React Native allowing developers to move between platforms to build SoundCloud Pulse.

## Backend-driven native UIs

“What if we changed this list to a grid?” It sounds like a simple question, but in practice it’s not. John Sundell and Diego Cristina Capelo from Spotify showed us how to use backend-driven native UIs to make answering this question and many others faster and easier.

## Infer: Moving fast with static analysis

Traditionally, static analysis tools have required code to be annotated with contracts and taken hours to perform full program analysis to find deep bugs, or they’ve run quickly but found only trivial linting errors. Dulma Churchill explained how [Infer](http://fbinfer.com/) is able to automatically find and cache contracts, allowing it to find deep bugs at diff time, and showed examples of the important classes of bugs that Infer is helping eradicate on mobile at Facebook and now Spotify.

## 3,000 images per second

Twitter creates approximately 3,000 unique images and transfers approximately 200 GB of images per second. After a short break for coffee and @Scale cupcakes, Henna Kermani described how Twitter’s image read and write paths evolved to handle this scale and how Facebook’s [Fresco](http://frescolib.org/) image library is now an important part of that pipeline on Android.

## React Native: Bringing the best of web development to native

Moving to native made Facebook better for people around the world but not always better for Facebook developers. Pieter De Baets talked about the challenges of building across multiple platforms and how React Native is poised to bring the best of the web to native.

## Don’t forget the web

Despite the progress made over the last few years, it is easy to conclude that the web still hasn’t caught up to the native platforms. In a fascinating final talk, Jeremy Keith explained why that comparison doesn’t make sense.
