---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.2.html
archived_at: '2026-07-15T07:52:50.762696Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.1.md)[Previous
Section](DirectToWeb.1.md) 

#  The Structure of a Direct to Web Project

A Direct to Web project has a similar structure to other WebObjects application projects. A newly created project contains three components:

###### 

!

- 

  __Main.wo__
  is the main component, representing the login page of the application.
- 

  __Header.wo__
  is a reusable component that is inserted at the beginning of each page in the application (other than Main). It contains some control buttons that are displayed at the top of each page. If you choose, you can add text or other elements to the Header component.
- 

  __Footer.wo__
  is a reusable component that is inserted at the end of each page in the application. By default, it is blank; you can add elements to it if you choose.

As you run your application, Direct to Web creates additional pages, using information in your model file and settings specified in the WebAssistant. These pages do not show up as components in your project. Rather, Direct to Web creates them dynamically using a set of reusable components in the Direct to Web framework. However, you have the option of saving any page as a component. When you do that, you are then able to modify the component just as you would with any other WebObjects component. See [See Generating Components](DirectToWeb.b.md#apple-geytgmjr)
for more information.

In your project's Classes suitcase, you'll see a Java file for each of the components, as well as the Session and Application objects. You can add code to any of these files to extend their functionality. See [See Modifying Your Application's Code](DirectToWeb.c.md#apple-ge3tknbr)
for more information on the Direct to Web API.

###### 

!

The Resources suitcase contains the model file you specified when you created the project (in this example, __Movies.eomodeld__
). It also contains __user.d2wmodel__
, which is used to store the preferences you have changed using the WebAssistant (you should never need to edit this file directly).

###### 

!

_Note:_
If your model references entities in another model, you must add the other model to your project manually. It doesn't get included automatically.

[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.3.md)[Next
Section](DirectToWeb.3.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
