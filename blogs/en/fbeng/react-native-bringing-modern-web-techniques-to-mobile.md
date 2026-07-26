---
title: 'React Native: Bringing modern web techniques to mobile'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2015/03/26/android/react-native-bringing-modern-web-techniques-to-mobile/'
original_language: en
published: 2015-03-26
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1a3fd07f3907e6f1'
translated: false
---

> 原文：[React Native: Bringing modern web techniques to mobile](https://engineering.fb.com/2015/03/26/android/react-native-bringing-modern-web-techniques-to-mobile/)　·　Meta Engineering — iOS

_If you’re new to React, you can read more about it on the [React website](http://facebook.github.io/react/). You can also get started with [React Native for iOS](https://facebook.github.io/react-native/), which was released at F8 2015 on the [React Native website](http://native.reactjs.com/)._

## It started with React

We introduced [React](https://reactjs.org/) to the world two years ago, and since then it’s seen impressive growth, both inside and outside of Facebook. Today, even though no one is forced to use it, new web projects at Facebook are commonly built using React in one form or another, and it’s being broadly adopted across the industry. Engineers are choosing to use React every day because it enables them to spend more time focusing on their products and less time fighting with their framework. It wasn’t until we’d been building with React for a while, though, that we started to understand what makes it so powerful.

[React](https://reactjs.org/) forces us to break our applications down into discrete components, each representing a single view. These components make it easier to iterate on our products, since we don’t need to keep the entire system in our head in order to make changes to one part of it. More important, though, React wraps the DOM’s mutative, imperative API with a declarative one, which raises the level of abstraction and simplifies the programming model. What we’ve found is that when we build with React, our code is a lot more predictable. This predictability makes it so we can iterate more quickly with confidence, and our applications are a lot more reliable as a result. Additionally, it’s not only easier to scale our applications when they’re built with React, but we’ve found it’s also easier to scale the size of our teams themselves.

Together with the rapid iteration cycle of the web, we’ve been able to build some awesome products with React, including many components of Facebook.com. Additionally, we’ve built amazing frameworks in JavaScript on top of React, like [Relay](https://facebook.github.io/react/blog/2015/02/20/introducing-relay-and-graphql.html), which allows us to greatly simplify our data fetching at scale. Of course, web is only part of the story. Facebook also has widely used Android and iOS apps, which are built on top of disjointed, proprietary technology stacks. Having to build our apps on top of multiple platforms has bifurcated our engineering organization, but that’s only one of the things that makes native mobile application development hard.

## Why native is difficult

There are many reasons the native mobile environment is more difficult to work with than the web. For one thing, it’s harder to lay things out on the screen, and we often have to manually compute the size and position of all our views. We also don’t have access to React or Relay, which have made it easier to scale the process of developing websites and growing our engineering organization. One of the most painful things about our transition to mobile, though, is how much it’s slowed down our development velocity.

When building on the web, we can simply save our files and reload the browser to see the result of our changes. On native, however, we need to recompile after every change, even if we just want to shift text a few pixels over on the screen. As a result, engineers end up working a lot more slowly, especially in a large codebase where compilation is especially burdensome. Building on native also makes testing new functionality more difficult. At Facebook, we deliver a new version of the website twice a day, so we can get the results of an experiment back almost immediately. On mobile, we often need to wait weeks or months in order to get the results of an experiment or A/B test back, because new versions of our app are released far less often. “Move fast” is in Facebook’s DNA, but we can’t move as fast on mobile as we can on the web. So why make the switch away from web in the first place?

The reason we build native apps on these proprietary platforms is that right now, we can create better-feeling experiences that are more consistent with the rest of the platform than we can on the web.

![](https://engineering.fb.com/wp-content/uploads/2015/03/GNK3qAB-XhV_7T4CAHBkdUgAAAAAbj0JAAAB.jpg)

## Why native is necessary

Even though developing native mobile apps takes longer, there are many reasons why we can produce better experiences on the mobile platforms than we can on the web. For one thing, we have access to platform-specific UI components, like maps, date pickers, switches, and navigation stacks. It’s possible to reimplement these components on the web, but our reimplementations never feel exactly like their native counterparts, and they also don’t get updated automatically with changes to the platform. We also don’t have anything as sophisticated as the native mobile gesture recognizers on the web, and we don’t yet have the proper tooling or the developer discipline needed to build a system that gets this right.

On the web, we also don’t have a sophisticated threading model, so we can’t parallelize work onto multiple threads. We can try to make use of web workers to execute some of our application logic in the background, but we can’t yet perform highly numeric computation like image decoding or text measurement efficiently off the main thread in the browser. This is probably one of the biggest challenges of building high-performance and responsive web apps.

## Best of both worlds?

What we really want is the user experience of the native mobile platforms, combined with the developer experience we have when building with React on the web. There are a few ways we can probably achieve this:

1.   1. Using WebViews

One possibility is to use WebViews inside simple native wrapper applications. We tried this a few years back, and we actually think it’s a great idea. While our implementation didn’t give us the performance and scaling we wanted, this approach is remarkably flexible and comes with all the positives associated with the developer experience of the web, like the ability to take full advantage of React and the web’s rapid iteration cycle. Unfortunately, because all the rendering is done using web tech, we can’t produce a truly native user experience.

1.   1. Porting React to native

Porting React to native code is also a great idea, and in fact, we built this for iOS! This project is called [ComponentKit](http://componentkit.org/), and we just open sourced it yesterday at F8. With ComponentKit, we get all the benefits of React, especially declarative, predictable UIs, but we can also take advantage of the power of the native environment, with platform-specific components and sophisticated gesture handling, as well as asynchronous image decoding, text measurement, and rendering. Additionally, since ComponentKit uses [flexbox](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Flexible_boxes) for layout, you don’t need to manually position and size the views in your application, so your code ends up being more concise and easier to maintain.

There are a couple of minor downsides to this approach, though. First, it’s iOS-only, so if we want to take advantage of it on Android, we’d have to build a separate implementation, and teach engineers how to use it. Additionally, we don’t have access to any of the stuff we’ve built for the web on top of React, like Relay, which helps us solve real problems we’ve faced scaling our data fetching. Most important, though, is that we haven’t fundamentally improved our developer velocity challenge — we still need to recompile after every change.

1.   1. Scripting native

If we use JavaScript to call into native APIs, we should have access to all the power of the native environment but should also be able to iterate quickly and take advantage of some of our existing JavaScript infrastructure. Additionally, since it’s just JavaScript, we could probably make this stack work across platforms. It sounds like everything we want, and it’s no surprise that there are tons of frameworks out there doing this. But it’s actually not quite so straightforward.

## Scripting native is tricky

If we just synchronously call back and forth between the native environment and an interpreted environment, our UI thread could end up being blocked on JavaScript execution. To make this efficient, we know we want to execute our JavaScript off the main thread, but doing so is hard. The first reason it’s hard is resource contention. If our JavaScript code accesses something that might represent a resource on another thread — the dimensions of a rendered view, for example — the system has to lock, which can cause stalls in the UI. The second reason this is tough is that there’s some fixed amount of overhead associated with every round trip between the native environment and the JavaScript virtual machine. If we need to cross the thread boundary often, we’ll have to incur this overhead over and over again.

So if we don’t do this correctly, our app could end up feeling worse than if it were written entirely in either native code or in JavaScript. We can’t just reimplement synchronous, imperative user interface APIs in JavaScript and expect to get a responsive, native-feeling experience. We need to fundamentally change the programming model and ensure that our system always passes messages across the thread boundary asynchronously and that we can batch up as many of these messages per frame as possible, minimizing cross-thread communication overhead.

Luckily, React gives us the perfect programming model to do this correctly.

![](https://engineering.fb.com/wp-content/uploads/2015/03/GMCrnQAGRB6TtwUFALcgOwgAAAAAbj0JAAAB.jpg)

## Introducing React Native

Since React components are just pure, side-effect-free functions that return what our views look like at any point in time, we never need to read from our underlying rendered view implementation in order to write to it. In the browser environment, React is non-blocking with respect to the DOM, but the beauty of React is that it is abstract and not tightly coupled to the DOM. React can wrap any imperative view system, like UIKit on iOS, for example.

So this means with a bit of work, we can make it so the exact same React that’s on [GitHub](https://github.com/facebook/react) can power truly native mobile applications. The only difference in the mobile environment is that instead of running React in the browser and rendering to divs and spans, we run it in an embedded instance of JavaScriptCore inside our apps and render to higher-level platform-specific components.

One of the best parts about this approach is that we can adopt it incrementally, building new products on top of it or converting old products to use it whenever and wherever it makes sense. Just as we didn’t need to rewrite all of Facebook.com in order to start using React in some places, we don’t need to rebuild our entire mobile Facebook applications in order to start realizing the benefits of React Native.

## This is working

We’ve been using React Native in production at Facebook for some time now, and while there’s still a ton of work to do, it’s been working really well for us. It’s worth noting that we’re not chasing “write once, run anywhere.” Different platforms have different looks, feels, and capabilities, and as such, we should still be developing discrete apps for each platform, but the same set of engineers should be able to build applications for whatever platform they choose, without needing to learn a fundamentally different set of technologies for each. We call this approach “learn once, write anywhere.”

![](https://engineering.fb.com/wp-content/uploads/2015/03/GMu3qAAGS3wrbCYDAB1nKGcAAAAAbj0JAAAD.png)

If you have an iPhone, you can test out a few apps using React Native that are available from the App Store. [Facebook Groups](https://itunes.apple.com/us/app/facebook-groups/id931735837) is a hybrid application, consisting of views built both with native code and React Native JavaScript, and [Facebook Ads Manager](https://itunes.apple.com/app/id964397083) is built entirely using React Native.

## Open source

At Facebook, our mission is to make the world more open and connected, and we want to actively contribute to that mission via open source. React Native is no exception. We realize that the problems we face as an engineering organization are not unique to us, and accordingly, we want to develop in the open as much as possible, collaborating with others who are facing the same challenges.

Today, we’re excited to open-source React Native for iOS and make it available on [GitHub](https://github.com/facebook/react-native). Android support is coming soon, and we’re also continuing full steam ahead on React for the web, but we wanted to get this initial iOS support out as early as possible so we can get input from others who are also excited about this approach. Keep in mind that there are probably many things that are either broken or not implemented yet. We welcome your feedback and contributions, and we can’t wait to see what you’ll build!
