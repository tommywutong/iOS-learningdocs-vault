---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.062.html
archived_at: '2026-07-15T07:59:02.643204Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.061.md)

# Debugging

In WebObjects 4.0, you debug an application by launching it in the Project Builder launch panel. By default, the browser is launched automatically and shows the appropriate URL.
A new feature of WebObjects 4.0 allows you to debug applications on a machine that doesn't have a web server present. See ["Serverless" Applications](NewInWO4.011.md#apple-giytkmbr) for more information.

WOApplication, WOComponent, and WODirectAction define a method named __debugWithFormat:__ (__debugString__ in Java). This method is similar to __logWithFormat:__/__logString__ except that you can control whether it displays output with the __WODebuggingEnabled__ user default option. If __WODebuggingEnabled__ is YES, then the __debugWithFormat:__ messages display their output. If __WODebuggingEnabled__ is NO, the __debugWithFormat:__ messages don't display their output. WODirectAction also defines __logWithFormat:__.
All dynamic elements and components now have a __WODebug__ attribute that can be helpful when you are trying to locate unwanted behavior (and can also help you understand how non-synchronized components work). When __WODebug__ is set to YES, it turns on a "verbose mode" for all dynamic associations for the element. This results in logs like the following being generated:

```
[NestedList:WXNestedList] (item: {label = Alpha.2.1; value = A.2.1; })
==> currentItem
[NestedList:WXNestedList] (index: 0) ==> currentIndex
[NestedList:WXNestedList] sublist <== (currentItem.sublist: *nil*)
[NestedList:WXNestedList] (item: {isNew = 1; label = Alpha.2.2; value =
A.2.2; }) ==> currentItem
[NestedList:WXNestedList] (index: 1) ==> currentIndex
[NestedList:WXNestedList] sublist <== (currentItem.sublist: *nil*)
```


The format of these logs is controlled by two new methods on WOApplication that can be overridden to customize the log messages: __logTakeValueForDeclarationNamed:type:bindingNamed:associationDescription:value:__ (__logTakeValueForDeclarationNamed__ in Java), and __logSetValueForDeclarationNamed:type:bindingNamed:associationDescription:value:__ (__logSetValueForDeclarationNamed__ in Java).

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](Other%20Changes.md)
