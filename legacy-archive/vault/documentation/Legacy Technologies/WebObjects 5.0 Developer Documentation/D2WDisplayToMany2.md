---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WDisplayToMany2.html
archived_at: '2026-07-15T08:12:43.580318Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WDisplayToMany2__

__Package__: com.webobjects.directtoweb

__Inherits from__:[D2WDisplayToMany](D2WDisplayToMany.md)See Also:
[D2WDisplayToManyFault](D2WDisplayToManyFault.md)
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component displays the objects of a to-many relationship in a table. Since the component fetches all of the objects in the relationship, it is slower than the D2WDisplayToManyFault component, especially when the relationship has many objects.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to display a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WDisplayToMany2()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jsf5cdev2enfzxa3dbpfkg6tlbnz4tel2egjlui2ltobwgc6kun5gwc3tzgixsqki)

---

Fields

- [item](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfordjonygyylzkrxu2ylopezc62lumvwq)

---

Private Methods

- [inspectItemAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jsf5uw443qmvrxislumvwucy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jsf5zgk4dmmfrwk3lfnz2ec43tn5rwsylunfxw4rtpojaxg43pmnuwc5djn5xc6v2pifzxg33dnfqxi2lpnyxsqv2pifzxg33dnfqxi2lpnywfg5dsnfxgolcekrlvizlnobwgc5dffrlu6q3pnz2gk6dufe)

---

__Constructors__

---

__D2WDisplayToMany2__

public D2WDisplayToMany2()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Fields__

---

__item__
com.webobjects.eocontrol.EOEnterpriseObject

This constant is intentially undocumen

---

__Methods__

__inspectItemAction__

public WOComponent inspectItemAction()

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
