---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WQueryToOneRelationship.html
archived_at: '2026-07-15T08:12:44.716590Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WQueryToOneRelationship__

__Package__: com.webobjects.directtoweb

__Inherits from__:[D2WQueryRelationship](D2WQueryRelationship.md)See Also:
[D2WQueryToOneField](D2WQueryToOneField.md)
[D2WCustomQueryComponent](D2WCustomQueryComponent.md)

---

__Class Description__

---

This property-level component builds a query based on the value for a particular key of a destionation object of a to-one relationship. Since the component fetches all of the objects that can appear in the relationship, it is slower than the D2WQueryToOneField component.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to query based on a property, use D2WCustomQueryComponent.

__Method Types__

---

Constructors

- [public D2WQueryToOneRelationship()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfkg6t3omvjgk3dboruw63ttnbuxal2egjlvc5lfoj4vi32pnzsvezlmmf2gs33oonugs4bpiqzfoulvmvzhsvdpj5xgkutfnrqxi2lpnzzwq2lqf4ucs)

---

---

__Constructors__

---

__D2WQueryToOneRelationship__

public D2WQueryToOneRelationship()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
