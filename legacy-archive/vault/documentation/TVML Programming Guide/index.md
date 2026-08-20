---
title: TVML Programming Guide
apple_id: TP40016718
resource_type: Guide
platform: tvOS
topic: null
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/TVMLKitJS/Conceptual/TVMLProgrammingGuide/index.html
archived_at: '2026-07-27T06:57:10.283204Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)



## About TVML Apps

> [!IMPORTANT]

On your mobile devices and computers, you probably already use apps such as Netflix, Hulu, WatchESPN, and iTunes to watch TV shows. And that’s exactly where TV in the living room is headed. All of these apps have a look and feel that users immediately recognize. With the introduction of TVML apps, you can now create your own apps for Apple TV. Whether you are a blogger who wants a new way to share your podcasts or an independent film company that wants to stream the latest productions, template apps provide an easy way to distribute your product.

### Designing for Apple TV

TVML apps provide you with a way to create apps for Apple TV using TVMLKit JavaScript (TVMLKit JS), the Apple TV Markup Language (TVML), and the TVMLKit framework. Every template has a specific design that follows Apple style guidelines, allowing you to quickly create gorgeous looking apps. Each TVML app is created using a set of predefined TVML templates that are designed to address a specific need. You can modify each template to show off your content using different styles and attributes. As you become more comfortable with creating basic apps, you can customize your app using the TVMLKit framework to modify and create new elements, views, and view controllers.

At its most basic, a TVML app is made up of three main parts: An Xcode project that creates the binary app that links to TVMLKit and provides the TVMLKit JS environment, a TVMLKit JS file that controls your app flow and business logic, and a TVML template that display information on the screen.

The majority of TVML apps are client/server apps. The app stored on the Apple TV is the client. In a basic app, the client stores the URL that points to your initial TVMLKit JS file which is stored on a server.

### Programming TVML apps

When you create a TVML app, you combine three different frameworks: TVML, TVMLKit, and TVMLKit JS. Each framework interacts with the other frameworks to produce a client/server app.

### TVML

Apple’s Television Markup Language (TVML) is an XML based language that is used to display information on the screen. TVML templates define what elements can be used and in what order and are designed to display information in a specific way. For example, the `loadingTemplate` shows a spinner and a quick description of what is happening, while the `ratingTemplate` shows the rating for a product. You create a new TVML file that contains a single template for each page in a client/server app. Each template page occupies the entire TV screen. For more information, see _[Apple TV Markup Language Reference](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/ATV_Template_Guide/index.html#//apple_ref/doc/uid/TP40015064)_.

### TVMLKit JS

TVMLKit JS is a JavaScript API framework specifically designed to work with Apple TV and TVML. TVMLKit JS incorporates the basic functionality found in JavaScript along with specialized APIs designed for Apple TV. Using TVMLKit JS, you are able to load and display TVML templates, play media streams, load customized content, and control the flow of your app. For more information, see _[TVJS Framework Reference](https://developer.apple.com/documentation/tvmljs)_.

### TVMLKit

The TVMLKit framework provides access to the TVMLKit JS environment and TVML. TVMLKit also provides a way to combine TVML and UIKit to create your own layouts. You can create your own elements, views, and view controllers and use them to customize your app to better present your content. Using TVMLKit, you are able to bridge the gap between native and TVML apps. For more information, see _[TVMLKit Framework Reference](https://developer.apple.com/documentation/tvmlkit)_.

[Creating Your First TVML App](https://developer.apple.com/library/archive/documentation/TVMLKitJS/Conceptual/TVMLProgrammingGuide/CreatingYourFirstContentApp.html#//apple_ref/doc/uid/TP40016718-CH2-SW4)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2017-09-19](https://developer.apple.com/library/archive/documentation/TVMLKitJS/Conceptual/TVMLProgrammingGuide/RevisionHistory.html#//apple_ref/doc/uid/TP40016718-CH99-SW1)
