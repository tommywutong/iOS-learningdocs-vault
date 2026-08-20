---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.4.html
archived_at: '2026-07-15T07:52:54.752363Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.3.md)[Previous
Section](DirectToWeb.3.md) 

##  The Login Page

When you launch your application, your web browser displays the Direct to Web login screen:

##### 

!

The login page is the default implementation of your Main component, __Main.wo__
. It contains text fields to enter a name and password, as well as two submit buttons. To continue with the application, click one of the submit buttons. (You don't need to enter a name and password, because the default application provides no password-checking logic.) They both take you to the application's default first page. If you use the Login button, you won't have access to the WebAssistant.

You can modify this page to provide any behavior or appearance you like. For example, you can add your own password-checking logic if necessary. See [See Modifying Your Application's Code](DirectToWeb.c.md#apple-ge3tknbr)
for more information.

Besides the login page, there are four types of pages in a Direct to Web application:

- 

  A _query page_
  that allows the user to construct a query for a particular entity; see [See Query Pages](DirectToWeb.5.md#apple-gmztamjy)
  .
- 

  A _list page_
  that displays one or more records of a particular entity in tabular form; see [See List Pages](DirectToWeb.6.md#apple-gezdqmzt)
  . The result of a query is always a list page.
- 

  An _inspect page_
  that displays a single record of a given entity; see [See Inspect and Edit Pages](DirectToWeb.7.md#apple-gi3dqobt)
  .
- 

  An _edit page_
  that displays a single record of a given entity and also allows you to make changes to the record and save it to the database; see [See Inspect and Edit Pages](DirectToWeb.7.md#apple-gi3dqobt)
  .

When you click one of the login buttons, by default a query page for the first entity in your model is displayed.

All pages in your application contain the standard Direct to Web header (defined in __Header.wo__
) at the top of the page. This header provides a number of controls, described in the figure.

##### 

!

[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.5.md)[Next
Section](DirectToWeb.5.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
