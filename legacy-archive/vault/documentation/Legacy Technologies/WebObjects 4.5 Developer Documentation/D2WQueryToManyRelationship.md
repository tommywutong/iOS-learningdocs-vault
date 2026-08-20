---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WQueryToManyRelationship.html
archived_at: '2026-07-15T08:11:30.507315Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WQueryToManyRelationship__

__Package__:

__Inherits from__:[D2WQueryRelationship](D2WQueryRelationship.md)See Also:
[D2WQueryToManyField](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WQueryToManyField.html)
[D2WCustomQueryComponent](D2WCustomQueryComponent.md)

---

__Class Description__

---

This property-level component builds a query based on the value for a particular key of a destionation object of a to-many relationship. Since the component fetches all of the objects that can appear in the relationship, it is slower than the D2WQueryToManyField component.

You can specify whether the list is collapsible or not and whether the user interface is a browser or a table of checkboxes. You can also specify the size of the browser or the number of columns of checkboxes to display.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to query based on a property, use D2WCustomQueryComponent.

__Method Types__

---

Constructors

- [public D2WQueryToManyRelationship()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfkg6tlbnz4vezlmmf2gs33oonugs4bpiqzfoulvmvzhsvdpjvqw46ksmvwgc5djn5xhg2djoaxuimsxkf2wk4tzkrxu2ylopfjgk3dboruw63ttnbuxalzife)

---

---

__Constructors__

---

__D2WQueryToManyRelationship__

public D2WQueryToManyRelationship()

This method is intentionally undocumented. You should never have to invoke or customize it.

---
