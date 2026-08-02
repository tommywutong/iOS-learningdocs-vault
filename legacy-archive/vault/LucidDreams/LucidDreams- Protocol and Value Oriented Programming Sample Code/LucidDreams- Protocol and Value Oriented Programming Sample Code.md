---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Introduction/Intro.html
archived_at: '2026-07-15T03:48:38.353133Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md)


[Next](LucidDreamsTests-LayoutTests.swift.md)

# LucidDreams: Protocol and Value Oriented Programming Sample Code

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2016-10-27 First release |
| __Build Requirements:__ | Xcode 8.0 or later; iOS 10.0 SDK or later |
| __Runtime Requirements:__ | iOS 10.0 SDK or later |

LucidDreams is a sample that accompanies the "Protocol and Value Oriented Programming in UIKit Apps" WWDC 2016 session (#419). It's recommended that you watch the talk before looking at this sample. The app lets users log their dreams with detailed content like effects that occurred during the dream, creatures that they saw, and more.

This application demonstrates how you can take advantage of value types and protocol oriented programming in Cocoa applications. We have examples of using these approaches in the model, view, and controller (MVC) layers. This is important because Cocoa apps are built using the MVC design pattern. We focus on the view and controller layers in this application more than the model layer because the view and controller layers are the least commonly thought of place to take advantage of these techniques. In this sample we show that value types are just as powerful in the view and controller layers as in the model layer.

\*\*note\*\* Some of these techniques may initially feel foreign. Don't worry——that's normal. It's a different way of thinking about how to solve certain kinds of problems.

Our goal for this sample is to make you think about how to architect the next solution to a problem you're having in code. If you're thinking about using classes with inheritance for customizing, think about using value types and composition instead. If your view controller has a lot of individual properties consider composing the properties into a value, i.e. your model and state properties, so that you can isolate the logic of that model into unit that can be tested and more easily reasoned about.

[Next](LucidDreamsTests-LayoutTests.swift.md)

