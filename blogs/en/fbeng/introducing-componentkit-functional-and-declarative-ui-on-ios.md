---
title: 'Introducing ComponentKit: Functional and declarative UI on iOS'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2015/03/25/ios/introducing-componentkit-functional-and-declarative-ui-on-ios/'
original_language: en
published: 2015-03-25
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:266b35941ca69811'
translated: false
---

> 原文：[Introducing ComponentKit: Functional and declarative UI on iOS](https://engineering.fb.com/2015/03/25/ios/introducing-componentkit-functional-and-declarative-ui-on-ios/)　·　Meta Engineering — iOS

Building user interfaces for iOS requires lots of imperative code. As a developer, you create views, configure them, and add them to the hierarchy. You then have to implement callbacks to controllers, which in turn must change the state of your views. Implementing this two-way data flow, even for a simple UI, can be tedious and error prone.

At Facebook, we’re very familiar with this issue. News Feed on iOS is a complex list interface, made up of a variety of row types, with each row having unique layout and interactions. Keeping the infrastructure for this complex list both maintainable and performant quickly became a difficult task, especially under constant iteration.

To tackle this challenge, we wanted a better abstraction. We drew inspiration from [React](https://reactjs.org/) and its functional reactive programming model for building UI and made a native, Objective-C++ library called [ComponentKit](https://componentkit.org/) which is now used to render News Feed in the Facebook iOS app.

Today we’re very excited to announce that we are making ComponentKit open source!

## Introducing ComponentKit

ComponentKit takes a functional, declarative approach to building UI and emphasizes a one-way data flow from [immutable models](https://engineering.fb.com/posts/340384146140520/making-news-feed-nearly-50-faster-on-ios/) to immutable components that describe how views should be configured.

A hierarchy of components is a blueprint for how your UI should look. This blueprint is then taken by the infrastructure that renders it as a hierarchy of UIKit elements.

![](https://engineering.fb.com/wp-content/uploads/2015/03/GCy4qADHOmkdHW4BAFWxuGoAAAAAbj0JAAAD.png)

ComponentKit lets you focus on what your UI should look like, rather than on the steps necessary to build it, which is more common with traditional imperative approaches.

For example, in regular iOS development, to display a view with a header, text and a footer you would have to:

- Create a header view, a text view, a footer view and store them in three different instance variables
- Add these three views as subviews of their container
- Add constraints so that each view has the same width as their container
- And finally add more constraints so that the views are positioned correctly and stacked together.

ComponentKit is declarative; it asks you to describe *what you want* not _how it should be done_, like so: “I want a header component, a text component and a footer component stacked together vertically and stretched horizontally.”

![](https://engineering.fb.com/wp-content/uploads/2015/03/GM63qAC5lZVkdwECAOBVN1QAAAAAbj0JAAAD.png)

ComponentKit entirely abstracts the task of rendering UI on the screen away from the developer. This means optimizations can be performed in a single place to benefit all code that builds on ComponentKit. It performs layout on a background thread, creates the minimal view hierarchy to render the components on screen and has intelligent view reuse. This results in great scroll performance and a snappy system overall.

If you want to dive deeper into the details of how ComponentKit works you can check out [this article](http://www.objc.io/issue-22/facebook.html) from Adam Ernst or the second half of this [@Scale talk](https://www.youtube.com/watch?v=XhXC4SKOGfQ&t=24m40s) by Ari Grant.

## Migrating iOS News Feed to ComponentKit

ComponentKit gave us performance and reliability gains in News Feed UI Rendering and made the system easier to reason about. It allowed us to:

- Reduce the size of our rendering code by 70%. Manual and intricate layout code was completely removed as it was no longer needed.
- Significantly improve scroll performance. ComponentKit eliminated many superfluous container views and significantly flattened our view hierarchy. A flatter hierarchy means less time spent on the main thread to render UI.
- Improve test coverage. ComponentKit made it easy to build modular UI for which each piece can then be tested in isolation. We now have almost all of News Feed UI under test coverage using [snapshot tests](https://github.com/facebook/ios-snapshot-test-case).

With less code to maintain, fewer bugs to fix, and more tests, we get to spend more time building awesome things.

ComponentKit has been used in News Feed for over six months in production and we are excited to push it even further. Today, we’re open-sourcing ComponentKit to share with the iOS developer community the same productivity and performance gains we’ve had at Facebook. We are excited for you to use it and we look forward to hearing your feedback.

With ComponentKit we are rethinking how we build interfaces on iOS. We can’t wait to see what you build with it.

## Get Started

ComponentKit is available on [GitHub](https://github.com/facebook/componentkit). Check out [the guide](http://componentkit.org).
