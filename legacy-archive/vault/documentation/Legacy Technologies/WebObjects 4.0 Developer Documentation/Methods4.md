---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Methods4.html
archived_at: '2026-07-18T01:20:17.779132Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods3.md)

### Suppressing Session IDs in a Direct Action URL

When you construct an HTML template that has some of its components bound to direct actions and some bound to component actions, depending on the placement of your direct action components their URLs may include session IDs. You can prevent the inclusion of a session ID in a direct action URL as shown in the following example:

```
MyLink:WOHyperlink {
    directActionName = "something";
    ?wosid = NO;
}
```

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods5.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
