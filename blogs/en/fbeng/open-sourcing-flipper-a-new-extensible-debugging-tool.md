---
title: 'Open-sourcing Flipper: a new extensible debugging tool'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2018/06/11/android/flipper/'
original_language: en
published: 2018-06-11
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0836e21239f5c4c5'
translated: false
---

> 原文：[Open-sourcing Flipper: a new extensible debugging tool](https://engineering.fb.com/2018/06/11/android/flipper/)　·　Meta Engineering — iOS

One challenge that comes from having many engineers working collaboratively on larger apps is that typically no single person knows how every module works. This segmentation of knowledge and expertise can make it difficult to develop new features, investigate bugs, or optimize performance. To help engineers at Facebook manage this complexity, we built Flipper, an extensible cross-platform debugging tool. Flipper gives us a surface where framework experts and developers can convey important information to framework users. Now we are adding functionality and [sharing Flipper as an open source project](https://fbflipper.com/) to help others accelerate the app development process. With Flipper, engineers have a highly flexible, intuitive way to inspect and understand the structure and behavior of their iOS and Android applications. We believe Flipper improves on current tools by providing a more visual and interactive experience that is extensible to fit engineers’ specific needs.

This initiative started more than three years ago with the release of Stetho, an Android debugging bridge built on Chrome’s developer tools. With Flipper, we wanted to build upon what we’ve learned with Stetho to design a tool that was more extensible to new features, had a richer user experience, and worked across both iOS and Android. With [today’s release of Flippper](https://github.com/facebook/flipper), we are sharing that work with the open source community. For most use cases going forward, we recommend using Fipper in place of Stetho. When engineers need a specific feature that has not been implemented in Flipper (for example, command-line tools based on dumpers), they can continue to use Stetho.

## Extensions in Flipper

Flipper has enabled Facebook engineers to more easily inspect the behavior of our applications. It has been used in many projects, but sample use cases include:

- Providing our engineers with access to a view hierarchy that more accurately resembles the features and functionality they are working with, by showing Litho and ComponentKit components.
- Surfacing a stream of GraphQL requests, as opposed to raw network events.
- Tracking performance markers in real time, allowing developers to more easily investigate performance problems.

Flipper was designed with extensibility as its focus, and, as a result, engineers have built a wide range of plugins for both generic and Facebook-specific use cases. Together with the Flipper platform, we are open-sourcing the plugins that we think will be most broadly useful to the open source community. With today’s release, engineers will be able to inspect the layout of their apps, whether the apps were built with standard Android/iOS views or Litho/ComponentKit components, and also inspect network traffic and system logs coming from their applications.

By working closely with framework and product developers inside Facebook from the start, we were able to ensure that our plugin APIs were powerful enough to build a wide range of tools. In fact, all the tools included in Flipper are themselves plugins; the core of Flipper only provides a set of UI components and manages the connection between devices. This means anyone can build equally powerful tools as custom plugins.

## An open source architecture

Flipper is made up of two parts: a desktop client and a mobile SDK. Flipper users interact with the desktop client. The mobile SDK is installed within the Android or iOS application that engineers want to debug, and it then transmits data to the Flipper desktop client. The desktop client is built on top of Electron and Facebook open source projects, including React.js, Flow, Metro, RSocket, and Yarn. The mobile SDK also makes heavy use of Facebook open source projects such as Folly and RSocket.

To extend Flipper with a plugin, an engineer writes a desktop client plugin to render the UI and a mobile SDK plugin to expose the data. For the desktop client plugin, the engineer just needs to create a React component extending the client’s base plugin class. This React component is in charge of communicating with the mobile SDK plugin and rendering any data it delivers. The desktop client plugin is also able to send commands back to the mobile SDK plugin. A mobile SDK plugin is developed in the language native to the platform on which it will run, whether Swift/Objective-C on iOS or Java/Kotlin on Android. The mobile SDK plugin registers a set of handlers and defines responses for them, similar to how engineers typically build a server application handling client requests.

With this bidirectional socket connection and React-based UI, we have been able to create a wide variety of tools to empower Facebook’s engineers. The image below shows the layout inspector in action. The property inspector appears on the right-hand side, where View properties can be edited on the fly to test different designs and configurations quickly and without needing to recompile. The layout inspector is itself extensible, and the Litho team has used it to bring the same live-update capabilities to Litho components inspected with Flipper.

![](https://scontent.xx.fbcdn.net/v/t39.2365-6/34181549_194884184473295_2201517085362749440_n.png?_nc_cat=0&_nc_log=1&oh=82a07d0dca365dd1faf1c31075f65f7e&oe=5BB21209)

## A tool for the open source community

We hope that open-sourcing Flipper and the accompanying plugins will provide a useful tool for other engineers working on mobile applications. These plugins can be easily integrated into existing apps using Flipper’s SDK with [just a few lines of code](https://l.facebook.com/l.php?u=https%3A%2F%2Ffbsonar.com%2Fdocs%2Fgetting-started.html%23setup&h=ATN-sZH2Q8W99l7w7IoUVOY5SRSf1uM3Dyll9DdfwFQo8498nBSe1Wj3BhhqvK_D4BCziQyt6XMaPF-_LcI2F5ETm5z0ef1c8RcIdrMa4qvrhDPcOYKQJhlUs_KZx8bU74gHNA).

As we’ve already seen Flipper prove useful internally at Facebook, we think Flipper’s APIs will help other engineers build great new experiences to improve their workflows. We look forward to seeing what the community will create, and over the coming months, we will continue working to improve the core of Flipper and expand the range of APIs available to plugin developers.

## UPDATE:

**As of July 31, 2018, we have changed the name of our open-sourced extensible debugging tool from Sonar to Flipper.**
