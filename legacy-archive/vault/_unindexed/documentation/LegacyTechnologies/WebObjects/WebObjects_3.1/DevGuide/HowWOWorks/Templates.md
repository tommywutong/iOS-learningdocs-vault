---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/Templates.html
archived_at: '2026-07-15T07:47:02.221243Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](ComponentElement.md)

# __Templates__

A template is a fixed and hierarchical network of elements and subcomponents shared by instances of a component. An application composes the template for a component at run time when the component is first requested. Template creation involves the parsing and integration of the component's ".html" and ".wod" files. This activity results in a _component definition_, which contains the template. A component definition captures essential information about a component and facilitates access to component resources. It makes it possible for component instances to share resources; instances need carry only the instance-variable values that are distinctive to them. If caching of component definitions is enabled, the application subsequently stores templates; in this case, parsing occurs only once during an application's lifetime.

When a component requests its template in a request-handling method, the WOElement object that is returned is the root object of an object graph. The root object can reference, directly or indirectly, every other element of the template. The network of reference corresponds to location on the page and to parent-child relationships; for instance, a WOForm would probably have WOTextField and WOSubmitButton children.

!

Figure 6: An Object Graph for a Page's Template

For each request-handling message, the default behavior of WOComponent is to forward the message to its template, which is represented by the root element. The root element, in turn, forwards the message to each of its child elements; if they have any children, these elements send it to them. Thus each element has an opportunity, if appropriate, to extract user data from the request, to invoke an action in the component, and to append its HTML representation to the response.

Each HTML element on a template has an element ID to identify it within the object graph. An element ID is implemented as an extension of the sender ID in the URL. You can request the current element ID from the WOContext object.

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](Associations.md)
