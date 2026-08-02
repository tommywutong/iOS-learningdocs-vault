---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.b.html
archived_at: '2026-07-15T07:53:08.487236Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.a.md)[Previous
Section](DirectToWeb.a.md) 

#   Generating Components

When you have worked with the WebAssistant and customized your pages to your liking, you may still want to add more features to your application. To do so, you can "freeze" a page; that is, save it as a WebObjects component. When you do this, the component becomes part of your project and is no longer created "on the fly" by Direct to Web. This has several advantages:

- 

  You have complete control over the visual appearance of the page. You can add any static or dynamic HTML elements you like, using a tool such as WebObjects Builder.
- 

  You can add functionality to the page by editing the component's Java code, as well as by editing the bindings of the page's dynamic elements.
- 

  Your application's performance improves because Direct to Web doesn't have to go through the process of creating the page "on the fly."

The main disadvantage of generating components is that you lose the ability to modify settings with the WebAssistant. Therefore, you should try to get your settings as close as possible to what you want before generating the component.

To save a page as a component:

#####  1. Click Advanced Options at the top of the WebAssistant.

###### 

!

#####  2. Select the task and entity corresponding to the page you want to generate.

_Note:_
You can't select "\*all\*" to generate multiple components. You must generate the components one at a time.

#####  3. Click Generate.

The Freeze Component window appears. It contains a text field with a default name for your page (the page name followed by the entity name). You can edit the name if you choose.

###### 

!

#####  4. Click OK.

Direct to Web generates a component and adds it to your project. (You may have to wait a few moments for this process to complete.)

#####  5. Click Save to save the changes to disk.

If you don't click Save, the component will be generated, but Direct to Web won't automatically use the generated component the next time you run the project. To use the generated component, click Use Custom in the Advanced Options screen, then click Pick to choose the component.

To "un-freeze" a component, click Use Standard.

_Note:_
When you generate a page and click Update, the browser's current page doesn't reflect the changes. To use the new component, you must navigate to a new instance of the page. For example, if the current page is a Movie query page, and you use the WebAssistant to freeze it, you must navigate to a new instance of Movie query (by clicking Build Query); the new instance uses the frozen component.

You can edit your component graphically using WebObjects Builder.

###### 

!

You can also examine the new component in Project Builder.

###### 

!

Direct to Web generates Java code for your component. Each component implements an interface that is appropriate to the page: QueryPageInterface, ListPageInterface, InspectPageInterface, and EditPageInterface. For example, the _QueryMovieRole.java_
file shown below implements the QueryPageInterface. For example, it contains an action method called _queryClicked_
that returns a component when the Query DB button is clicked. (Note that the component's submit button is bound to _queryClicked_
in _QueryMovieRole.wod_
.)

You can modify the code in the generated routines if you choose.

###### 

!

To make use of the new component, you must rebuild and relaunch your application.

[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.c.md)[Next
Section](DirectToWeb.c.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
