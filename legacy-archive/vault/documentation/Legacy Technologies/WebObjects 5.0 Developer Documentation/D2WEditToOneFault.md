---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WEditToOneFault.html
archived_at: '2026-07-15T08:12:43.891156Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WEditToOneFault__

__Package__: com.webobjects.directtoweb

__Inherits from__:[D2WDisplayToOne](D2WDisplayToOne.md)__Implements__:

- com.webobjects.directtoweb.generation.DTWGeneration

See Also:
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component displays a hyperlink representing a to-one relationship. The hyperlink navigates to an edit-relationship page that allows the user to choose the destination object of the relationship.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to edit a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WEditToOneFault()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu63tfizqxk3duf5cdev2fmruxivdpj5xgkrtbovwhil2egjlukzdjorkg6t3omvdgc5lmoqxsqki)

---

Private Methods

- [editRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu63tfizqxk3duf5swi2lukjswyylunfxw443infyc6v2pinxw24dpnzsw45bpfauq)
- [helpString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu63tfizqxk3duf5ugk3dqkn2he2lom4xvg5dsnfxgolzife)
- [methodNameForEditRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu63tfizqxk3duf5wwk5din5se4ylnmvdg64sfmruxiutfnrqxi2lpnzzwq2lqf5jxi4tjnzts6kbj)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu63tfizqxk3duf5zgk4dmmfrwk3lfnz2ec43tn5rwsylunfxw4rtpojaxg43pmnuwc5djn5xc6v2pifzxg33dnfqxi2lpnyxsqv2pifzxg33dnfqxi2lpnywfg5dsnfxgolcekrlvizlnobwgc5dffrlu6q3pnz2gk6dufe)

---

__Constructors__

---

__D2WEditToOneFault__

public D2WEditToOneFault()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Methods__

__editRelationship__

public WOComponent editRelationship()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__helpString__

public String helpString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameForEditRelationship__

public String methodNameForEditRelationship()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
