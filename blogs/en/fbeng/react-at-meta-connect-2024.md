---
title: React at Meta Connect 2024
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2024/10/02/android/react-at-meta-connect-2024/'
original_language: en
published: 2024-10-02
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3d10b02b69665ecc'
translated: false
---

> 原文：[React at Meta Connect 2024](https://engineering.fb.com/2024/10/02/android/react-at-meta-connect-2024/)　·　Meta Engineering — iOS

At Meta, [React](https://react.dev/) and [React Native](https://reactnative.dev/) are more than just tools; they are integral to our product development and innovation. With over five thousand people at Meta building products and experiences with React every month, these technologies are fundamental to our engineering culture and our ability to quickly build and ship high quality products. In this post, we will dive into the development experiences of some of the product teams who leveraged React and React Native to deliver exciting projects showcased at Meta Connect 2024.

## Instagram and Facebook For Meta Quest

[https://engineering.fb.com/wp-content/uploads/2024/10/RNBlogDemo-compressed.mp4](https://engineering.fb.com/wp-content/uploads/2024/10/RNBlogDemo-compressed.mp4)

At Connect, Mark Zuckerberg shared that we have re-built Instagram and Facebook for mixed reality (MR) on Meta Quest. Our goal was to bring our flagship social experiences to the Meta Quest headset, letting people catch up with their friends and watch Stories and Reels, all while showcasing new possibilities enabled only through MR.

Building Meta’s social apps from scratch in MR required our teams to thoughtfully leverage the platform capabilities offered by Meta Quest while keeping a tremendously high bar for quality. The teams first had to decide how to build them: reusing the existing Android apps, writing a new native Android app, or using React Native to build from scratch. We wanted to offer a hero experience that looked and felt at home on Meta Quest, taking advantage of the additional input types, gestures, and larger visual surface area. Instead of simply porting our mobile social apps, we chose React Native as it enabled our teams to iterate and build quickly with robust animation capabilities, great performance, and a shared platform that powers most of the 2D Meta Quest system apps.

On Instagram, React Native enabled our teams to build rich animations and novel interactions that embody the brand’s deep focus on quality and delight. For this new app, we introduced seamless transitions of video posts from feed into a full screen view side by side with comments, without dropping a single frame. We enabled the ability to swipe through stacks of photos with the controller joystick or pinching your hands. We also introduced a unique hover animation over interactive elements that smoothly follows your controller movements.

When building Facebook for Meta Quest, our teams took advantage of the mature code and infrastructure that supports our [Facebook.com desktop experience](http://facebook.com). We leveraged code sharing technologies to reuse some of the most complex and robust features from Facebook.com like Newsfeed and commenting. Some of these code sharing technologies include our Meta open source projects like [StyleX](https://stylexjs.com/) and [React Strict DOM](https://github.com/facebook/react-strict-dom). By sharing code, our teams could spend less time on repetitive business logic and focus more on adding Meta Quest specific interactions and experiences.

## Meta Horizon mobile app

![](https://engineering.fb.com/wp-content/uploads/2024/10/Meta-Horizon-React-Connect-2024-compressed.jpg?w=1024)

This year, we also [rolled out the new Meta Horizon mobile app](https://www.meta.com/blog/quest/horizon-mobile-app/) – a new look and a new name. We expanded the app to make it easier to socialize and express yourself both in and out of the headset. We added a dedicated tab to easily customize your avatar and express your mood, right from your phone. People can also visit Horizon Worlds and complete quests from the app to unlock exclusive avatar styles, items, and emotes.

We’ve also continued to improve app performance. At Meta, our teams typically look to Facebook Marketplace as a React Native performance benchmark. However, the Meta Horizon app is a standalone app with React Native in the initialization path of the app’s cold start, compared to the Facebook app which initializes React Native when you visit your first React Native surface and not on app start. The performance results our teams delivered with React Native exceeded our original expectations and are on par with Meta’s mobile social apps.

Our Meta Horizon team worked closely with our React team to profile our application and find opportunities for improvement using Android Systrace, React DevTools, and the new [React Native DevTools](https://www.youtube.com/live/b48Lax2-jOQ?si=OgqKzyw-AAnIUefZ&t=4290). The most impactful improvement that our teams made was initiating network queries earlier. Instead of initiating network requests when a component of the product surface was rendered, [Relay](https://relay.dev/), our GraphQL library, made it easy for our teams to move that network fetch to start when the navigation button from the previous surface was clicked.

## Meta Horizon Store

![](https://engineering.fb.com/wp-content/uploads/2024/10/Meta-Horizon-Store-Quest-React-Connect-2024-crop-compressed.jpg?w=1024)

We also announced that the Meta Horizon Store is now open for all developers to publish apps, [including 2D apps](https://developers.meta.com/horizon/blog/building-2d-apps-on-the-meta-horizon-store). To support this change, we made major changes to the Horizon Store; changes to our navigation to support significantly more categories, better ranking and categorization of apps, and a new “Early Access” section.

The Meta Horizon Store includes the surfaces that let you discover and acquire applications and games for Meta Quest, as well as explore Worlds you can travel to in Horizon. Since we have a centralized team that maintains the Store across four platforms (Android, iOS, Horizon OS, Web) and we need feature parity across these interfaces, the team has benefited tremendously from being able to use React and React Native even though these are primarily separate implementations today. These technologies have enabled the team to roll out new features and experiments much faster with a smaller team.

Just like the new Instagram and Facebook apps, and everything else using React at Meta, our teams use the bleeding edge of React infra like the React Compiler and the New React Native Architecture. The React team partnered with multiple teams over the last few years to build out infrastructure and capabilities to enable cross platform code sharing, which the Meta Horizon Store team has started to take advantage of. For example, the Meta Horizon Store’s navigation and routing infrastructure was originally quite different between platforms. The team is now reusing Meta’s internal router for React apps that was [originally built for Facebook.com](https://www.youtube.com/watch?v=KT3XKDBZW7M) which now also works with React Native. We also converted the Meta Horizon Store on the web from using pure CSS to using [StyleX](https://stylexjs.com/), which in combination with [React Strict DOM](https://github.com/facebook/react-strict-dom), has enabled them to reuse the Spotlight section of the Meta Horizon Store across web and mixed reality. This enabled us to more quickly support internationalized text rendering and light/dark mode for banners, and accelerated future enhancements for our merchandising team.

## Meta Spatial Editor

[https://engineering.fb.com/wp-content/uploads/2024/10/spatial-compressed.mp4](https://engineering.fb.com/wp-content/uploads/2024/10/spatial-compressed.mp4)

We announced the [Meta Spatial SDK](https://developers.meta.com/horizon/develop/spatial-sdk) and Meta Spatial Editor to enable mobile developers to create immersive experiences for Meta Horizon OS using familiar Android languages, libraries, and tools, along with unique Meta Quest capabilities, such as physics, MR, and 3D. Creating great 3D experiences always requires being able to visualize and edit your scenes directly. The Meta Spatial Editor is a new desktop app that lets you import, organize, and transform your assets into visual compositions and export them, using the glTF standard, into Meta Spatial SDK.

Our teams built the app with [React Native for Desktop](https://microsoft.github.io/react-native-windows/), providing users with native Windows and macOS apps and providing our teams with the incredible developer experience of React. One of the key factors in the teams’ decision to use React Native for Desktop instead of other web-based desktop solutions is that React Native enables the team to utilize native integrations when needed. The main 3D scene in the app is powered by a custom 3D rendering engine, requiring a custom React Native Native Component integration. The React Native panels on the scene let users modify all sorts of properties which then communicate with the 3D renderer via C++, enabling us to update the UI at 60fps.

The Meta Spatial Editor team had many engineers who primarily had a C++ background and were used to building with Qt. These team members were initially skeptical of JavaScript but ended up loving the developer experience provided by React Native, such as Fast Refresh. Web developers take for granted that code changes can be seen on file-save, but it is still extremely uncommon for native engineers. This developer experience enabled our teams to build much more quickly with React Native.

## This is how Meta builds React

Over a decade ago, Meta introduced React to the industry through open source. Our React team at Meta is so proud of these experiences that were announced at Meta Connect 2024. These products showcase the power, expressivity, and flexibility of what’s possible with React: delightful interactions, deeply complex integrations, and incredibly responsive interfaces. And of course, they all render natively on their respective platforms to match user expectations.

Over the past decade, the React team has partnered deeply with both teams at Meta as well as members of the open source community to enable these types of product and developer experiences. Engineers at Meta use React on every platform where we ship user interfaces: web, mobile, desktop, and new platforms such as MR. Each time the React team has added support for a new platform, the team has invested in deeply understanding the idioms and expectations for user experiences on that platform, then adapting and optimizing React accordingly. We’ve consistently found that improving React for one platform benefits others as well — an approach the React teams described in their [Many Platform Vision](https://reactnative.dev/blog/2021/08/26/many-platform-vision).

This pattern has continued as the teams expanded support to the constraints and opportunities of mixed reality devices. Our teams have improved startup and application responsiveness, improved efficiency to reduce battery drain, and taken major steps to enable code sharing across web and native platforms — with platform-specific customizations. These wins have consistently benefited our apps on other platforms, with user experience improvements in products such as Facebook.com and Facebook Marketplace.

Our engineers invest in these improvements knowing that they will benefit not only products created by Meta, but all React products in the world. Meta continues to share these improvements with the open source community whenever we have built our confidence that they are stable enough for broader adoption. We’ve previously shared some of these technologies with the open source community, including [React Compiler](https://youtu.be/lyEKhv8-3n0?si=sg-gbtEMtUCxFqOs&t=2269), [React 19](https://react.dev/blog/2024/04/25/react-19), React Native’s [New Architecture](https://youtu.be/Q5SMmKb7qVI?si=i5K0pUmYCYOeBbKu&t=766), [StyleX](https://stylexjs.com/), [React Strict DOM](https://github.com/facebook/react-strict-dom), and performance improvements [to Hermes](https://www.youtube.com/watch?v=rElD4RaR3gk). These innovations and more are currently under development, and our teams look forward to sharing them with the open source community in the future!

_Stranger Things ™/© Netflix. Used with permission._
