---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Reuse/Synchronize.html
archived_at: '2026-07-15T07:47:24.345510Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Reuse.book.md)
[!Previous Section](AlertPanelWithResponse.md)

# Synchronizing Parent and Child Components

WebObjects treats attribute bindings between parent and child components as potentially two-way communication paths and so synchronizes the values of the bound variables at strategic times during the request-response loop. This synchronization mechanism has some implications for how you design components.

For the sake of illustration, consider a page that displays a value in two different text fields--one provided by the parent component and one by the child:

!
 ____Figure 1.__  Synchronized Components__

Setting the value of either text field and submitting the change causes the new value to appear in both text fields.

The parent's declarations file reveals the binding between the two components:

```
CHILDCOMPONENT: ChildComponent {
    childValue=parentValue;
};
```

When a value is entered in a field and the change submitted, WebObjects will, if needed, synchronize the value in the parent (__parentValue__) and child (__childValue__) at each of the three stages of the request-response loop:

- Before and after the components receive the __takeValuesFromRequest:inContext:__ message.
- Before and after the components receive the __invokeAction:inContext:__ message.
- Before and after the components receive the __appendToResponse:inContext:__ message.

Synchronization is accomplished through key-value coding, a standard interface for accessing an object's properties either through methods designed for that purpose or directly through its instance variables. (The key-value coding mechanism is declared in the Enterprise Objects Framework, in __EOKeyValueCoding.h__. See the _Enterprise Objects Framework Developer's Guide_ for more information.) Key-value coding always first attempts to set properties through accessor methods, only reverting to accessing the instance variables directly if the required accessor method is missing.

Given that synchronization occurs several times during each cycle of the request-response loop and that key-value coding is used to accomplish this synchronization, how does this affect for the design of reusable component? It has these implications:

- You rarely need to implement accessor methods for your component's instance variables. For instance, it's sufficient in the example above to simply declare a __childValue__ instance variable in the child component and a __parentValue__ instance variable in the parent. You only need to implement accessor methods (such as __setChildValue:__ and __childValue__) if the component must do some calculation (say, determine how long the application has been running) before returning the value.
- If you do provide accessor methods, they should have no unwanted side effects and should be implemented as efficiently as possible since they will be invoked several times per transaction.
- If you bind a component's attribute to a method rather than to an instance variable, you must provide both accessor methods: one to set the value and one to return it. Let's say the parent component in the example above doesn't have a discrete __parentValue__ instance variable but instead stores the value in some other way (for example, as an entry in an NSDictionary object). In that case, the parent component must provide both a __parentValue__ method (to retrieve the value) AND a __setParentValue:__ method (to set it). During synchronization, WebObjects expects both methods to be present and will raise an exception if one is missing.

[!Table of Contents](Reuse.book.md)
[!Next Section](SearchPath.md)
