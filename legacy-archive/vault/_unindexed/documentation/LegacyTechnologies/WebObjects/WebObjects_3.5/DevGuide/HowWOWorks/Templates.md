---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/Templates.html
archived_at: '2026-07-15T07:51:57.305352Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](ComponentElement.md)

## Component Templates

The first step to generating a component's HTML page is to create a _template_ for the component. This template is not the same as the HTML template discussed in the chapter ["What Is a WebObjects Application?"](../WhatIsWOApp/WhatIsWOApp.md#apple-giydioa). In this context, a template is a graph of WOElement and WOComponent objects created by parsing and integrating the component's __.html__ and __.wod__ files (see [Figure 25](#apple-gyytcni)). The network of references corresponds to locations on the page and to parent-child relationships; for instance, a WOForm element would probably have WOTextField and WOSubmitButton children.

!Figure 25. An Object Graph for a Page's Template
The template is created at runtime when the component is first requested. The template is part of a larger _component definition_, which also includes information that allows instances of this component to share resources. Instances carry only the instance-variable values that are distinctive to them; the rest is stored in the component definition. You can, if you wish, enable caching of component definitions so that the component is parsed only once during an application's lifetime. To do so, send the application object a __setCachingEnabled:__ message in its initialization method.
For each request-handling message, WOComponent's default behavior is to forward the message to the objects in its template. To do so, it first retrieves the template from the component definition. The component definition returns the WOElement object at the root of the object graph. This root object, in turn, forwards the message to each of its child elements; if they have any children, these elements send the message to them. Thus, each element has, if appropriate, an opportunity to extract user data from the request, to invoke an action in the component, and to append its HTML representation to the response.
Each HTML element on a template has an element ID to identify it within the object graph. An element ID is implemented as an extension of the sender ID in the URL. You can request the current element ID from the WOContext object.

[!Table of Contents](HowWOWorks.md) [!Next Section](Associations.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
