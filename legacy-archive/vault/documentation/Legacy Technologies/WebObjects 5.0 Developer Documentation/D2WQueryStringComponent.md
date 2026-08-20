---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WQueryStringComponent.html
archived_at: '2026-07-15T08:12:44.609727Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WQueryStringComponent__

__Package__: com.webobjects.directtoweb

__Inherits from__:[QueryComponent](QueryComponent.md)See Also:
[D2WCustomQueryComponent](D2WCustomQueryComponent.md)

---

__Class Description__

---

This property-level component builds a query based on a string using WODisplayGroup's default values for `stringMatchFormat` (`#@*`) and `stringMatchOperator` (`caseInsensitiveLike`). In other words, the attribute must start with the query string (case is ignored).

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to query based on a property, use D2WCustomQueryComponent.

__Method Types__

---

Constructors

- [public D2WQueryStringComponent()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfjxi4tjnztug33nobxw4zlooqxuimsxkf2wk4tzkn2he2lom5bw63lqn5xgk3tuf5cdev2rovsxe6ktorzgs3thinxw24dpnzsw45bpfauq)

---

---

__Constructors__

---

__D2WQueryStringComponent__

public D2WQueryStringComponent()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
