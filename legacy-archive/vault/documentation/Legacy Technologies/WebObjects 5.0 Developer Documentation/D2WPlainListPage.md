---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WPlainListPage.html
archived_at: '2026-07-15T08:12:44.359335Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WPlainListPage__

__Package__:
com.webobjects.directtoweb

__Inherits from__:[D2WListPage](D2WListPage.md)__Subclasses__:

- [BASPlainListPage](BASPlainListPage.md)
- [NEUPlainListPage](NEUPlainListPage.md)
- [WOLPlainListPage](WOLPlainListPage.md)

---

__Class Description__

---

This class provides the behavior for the plain-list page Direct to Web templates, specifically BASPlainListPage, NEUPlainListPage, and WOLPlainListPage. The classes for these components inherit directly from D2WPlainListPage and define no additional variables or methods.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the Direct to Web template's bindings (`.wod`) file. If you create a Direct to Web template from a plain-list page, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WPlainListPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igyyljnzggs43ukbqwozjpiqzfoudmmfuw4tdjon2faylhmuxuimsxkbwgc2lojruxg5cqmftwklzife)

---

Key-Value Coding

- [sortKeyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igyyljnzggs43ukbqwozjponxxe5clmv4uy2ltoqxu4u2bojzgc6jpfauq)

Private Methods

- [componentsForSortKeyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igyyljnzggs43ukbqwozjpmnxw24dpnzsw45dtizxxeu3poj2ewzlzjruxg5bpkn2he2lom4xsqki)
- [setLocalContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igyyljnzggs43ukbqwozjponsxitdpmnqwyq3pnz2gk6duf53g62lef4ueimsxinxw45dfpb2cs)

---

__Constructors__

---

__D2WPlainListPage__

public D2WPlainListPage()

Standard Java no-argument constructor.

---

__Methods__

__componentsForSortKeyList__

public String componentsForSortKeyList()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setLocalContext__

public void setLocalContext(D2WContext context)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__sortKeyList__

public NSArray sortKeyList()

Returns the list of property keys that can be used to sort the receiver's displayed objects.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
