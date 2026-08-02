---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.019.html
archived_at: '2026-07-15T07:58:30.728404Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.018.md)

### Putting Values into a WORequest

WebObjects 4.0 allows you to set arguments for an action as follows:

```
myLink : WOHyperlink {
    directActionName = "display";
    queryDictionary = arguments;
    ?sku = currentProduct.sku;
}
```


The __queryDictionary__ attribute is set to an NSDictionary that contains arguments for the __displayAction__ method. The keys in this dictionary are variables in the action method. The __sku__ argument is an additional argument for the __displayAction__ method and is an alternate way of setting arguments for the action.
__Note:__  Although the above example uses a direct action, use of the __queryDictionary__ and the "?" binding aren't limited to direct actions: you can use them any time you need to put a value into a WORequest.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.020.md)
