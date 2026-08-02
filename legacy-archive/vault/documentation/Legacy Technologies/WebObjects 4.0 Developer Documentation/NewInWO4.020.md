---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.020.html
archived_at: '2026-07-15T07:58:31.664986Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.019.md)

### Suppressing Session IDs in a Direct Action URL

When you construct an HTML template that has some of its components bound to direct actions and some bound to component actions, depending on the placement of your direct action components their URLs may include session IDs. You can prevent the inclusion of a session ID in a direct action URL as shown in the following example:

```
MyLink:WOHyperlink {
    directActionName = "something";
    ?wosid = NO;
}
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.021.md)
