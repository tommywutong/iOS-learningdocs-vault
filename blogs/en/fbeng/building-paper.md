---
title: Building Paper
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2014/03/07/ios/building-paper/'
original_language: en
published: 2014-03-07
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:af98233f41cdc2f7'
translated: false
---

> 原文：[Building Paper](https://engineering.fb.com/2014/03/07/ios/building-paper/)　·　Meta Engineering — iOS

A few weeks ago we launched [Paper](http://www.facebook.com/paper), a new app to explore content from your friends and the world around you—with built-in access to all the core features of Facebook. Through the process of implementing the fresh design and creating about 20 new categories of content, the team has developed new frameworks and architectural approaches to address the toughest challenges we encountered. In a series of blog posts, tech talks, and open source releases, we hope to give a comprehensive overview of the key parts of Paper’s implementation and share some of our most valuable lessons learned while building this interaction-rich app on iOS.

In setting out to create Paper, our goal was not to pick apart past assumptions, but to start clean. We did establish one new assumption, however: the product should be designed and optimized for mobile devices at every level, from performance to user experience. The constraints and capabilities of smartphones with multitouch displays are quite unique, and it soon became apparent that fulfilling this charter would require not just a new set of interface designs–it would also demand rethinking the engineering approach in several major ways to successfully build out the vision.

## Constraints and capabilities

Perhaps the most obvious constraint of a mobile device is its limited display size. Wasting space with unnecessary indentation, tab bars, or bordering of elements crowds the content being presented and causes text to wrap sooner and images to be smaller. Paper addresses this by removing virtually all of the traditional navigation elements, ensuring that the screen is used edge-to-edge with useful and beautiful material. While Paper was developed in isolation from iOS 7, the system’s all-new design has broadly introduced similar underlying principles (both in first-party apps, and as a new set of design guidelines for third parties).

Recognizing visible area as a limitation, these displays have an important advantage compared to earlier generations of devices: multitouch sensing hardware. This input modality is extremely powerful, yet still in its early stages of utilization in the market. We can’t simply remove standard navigational elements like buttons, as their functionality must be replaced by another mechanism. This combination of facts led to an early decision that the app would be gesture-driven to a degree we had not built before, with nearly everything onscreen reacting to peoples’ touches. Disambiguating these gestures and allowing them to seamlessly interrupt in-flight animations became an important, unsolved engineering problem.

## Engineering a new level of interactivity

When we decided to minimize application chrome and replace it with large surfaces that respond to touch input, we observed an essential detail which seems to apply to gestures in general. They feel best when the force imparted to the device from a person’s finger behaves as though it is carried into the device—transcending the glass, and playing out in an action that is animated naturally by a physics simulation. In fact, the familiar inertial scrolling and edge bouncing effects seen when scrolling content on iOS are examples of these velocity-sensitive interactions, but surprisingly, it has been uncommon to see this successful paradigm extended further. Paper’s user interface is made more intuitive and realistic with consistent, pervasive use of these physics-simulating animations in new contexts, such as when interacting with photos and links, dragging elements in a list that follow your finger, etc.

The stories that follow will all be about how the team implemented the user interface of Paper, including discussion of the new techniques we came up with to enable our development, and how we confronted those limitations while maximizing use of the powerful frameworks already available (in the iOS SDK, and at Facebook). Here are some of the topics we’re planning to discuss:

- Building asynchronous user interfaces: How Paper keeps gestures and animations smooth
- Implementing physics-simulating animations: Going beyond Core Animation
- Advanced interactions on iOS: Coordinating animations with touch input
- Advanced techniques with asynchronous UI: Preloading content and GPU optimization

The first technical post will dive into how Paper’s architecture ensures that the application’s main thread is significantly less burdened than in a typical UIKit application, enabling high responsiveness and frame rates, especially for an app that makes heavy use of physics-simulating animations. We’re excited to explore other topics in the coming months!

## Sharing what we’ve learned

Facebook has a strong tradition of sharing our engineering work; examples I’m personally proud of include Open Compute’s innovative hardware designs, major open source projects like React and HHVM, and engineering events like hackathons and F8. The Paper team is eager to participate in the community by sharing our experiences across several mediums. In addition to our planned series of engineering blog posts, we’ve already open sourced two small components, [KVOController](https://github.com/facebook/KVOController) and [Shimmer](https://github.com/facebook/Shimmer), and are working on more. We’re also starting to plan some tech talks, and we look forward to posting some videos of them here on [code.facebook.com](https://engineering.fb.com) and the [Facebook Engineering Page](https://www.facebook.com/engineering). Each effort will be led by engineers from the Paper team, aimed at reflecting one of their personal specialties they developed while working on the project. We’ll be listening carefully to the community throughout, so please let us know which topics and formats are the most interesting and useful!

It was possible for the Paper team to focus so deeply on these challenges of interactivity and performance only because of the infrastructure we were able to build upon. iOS has a rich set of APIs that give us key functionality to use and extend with our own. Far more significantly, being situated inside Facebook, surrounded by people of consistently humbling intelligence and skill, gave us access to both client and server capabilities which proved essential for allowing our team to remain focused on the areas where we could contribute back new innovations. The Paper team is genuinely grateful for this opportunity, and we’re excited to share what we’ve learned with people both inside and out of Facebook.

_Thanks to all the engineers who put significant full-time effort into shipping Paper v1.0: Kimon Tsinteris, Tim Omernick, Brian Amerige, Jason Prado, Ben Cunningham, Grant Paul, Li Tan, Andrew Pouliot, Andrew Wang, Nadine Salter, and more!_
