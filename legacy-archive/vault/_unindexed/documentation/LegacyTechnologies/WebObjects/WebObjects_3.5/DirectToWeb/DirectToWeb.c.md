---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.c.html
archived_at: '2026-07-15T07:53:11.489411Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.b.md)[Previous
Section](DirectToWeb.b.md) 

#   Modifying Your Application's Code

You can modify your application's code just as you would in any other WebObjects application. In addition, there is an API for you to use specifically in Direct to Web applications. This consists of a set of methods defined in the D2WSession class.

You can use the following methods to return a specific component of a given class, given its name:

`QueryPageInterface queryPageForEntityNamed (String entity);`

`ListPageInterface listPageForEntityNamed (String entity);`

`EditPageInterface editPageForEntityNamed (String entity);`

`InspectPageInterface inspectPageForEntityNamed (String entity);`

There are three other methods provided by Direct to Web that you may want to override:

`public Component defaultPage();`

`public Component defaultPageWithAssistant();`

`public Component transitionToWebAssistant();`

These methods have the following functionality:

- 

  __defaultPage__
  returns the application's default page. Unless you override this method, the default page is the query page for the first entity in the model (alphabetically).
- 

  __defaultPageWithAssistant__
  returns the default page with the Customize button in the header, so that the WebAssistant is available.
- 

  __transitionToWebAssistant__
  returns a new page with two frames: the top frame contains the last page accessed, and the bottom frame contains the WebAssistant.

The following example shows how you can use these routines:

If you examine your application's Main component in WebObjects Builder, you'll notice that it contains a login form with text fields to enter a name and password, as well as two submit buttons.

###### 

!

The text fields are bound to the variables __username__
and __password__
(declared in __Main.java__
). The Login button is bound to __session.defaultPage__
, and LoginWithWebAssistant is bound to __session.defaultPageWithAssistant__
. You can override these methods to change the behavior of the buttons. For example, you may wish to add password-checking code (the default implementation doesn't have any). You also might want to begin with an entity that's not the first one in the list.

The following code in __Session.java__
overrides __session.defaultPage__
to change the default page to the query page for the Movie entity. It also changes the application's default timeout value.

###### 

!

_Note:_
When you override __defaultPage__
, this also takes care of the case where you use the LoginWithWebAssistant button, because the implementation of __defaultPageWithAssistant__
calls __defaultPage__
, which is now overridden by your code.

[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
