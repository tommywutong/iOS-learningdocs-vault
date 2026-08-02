---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WDisplayToManyFault.html
archived_at: '2026-07-15T08:12:43.616553Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WDisplayToManyFault__

__Package__: com.webobjects.directtoweb

__Inherits from__:[D2WStatelessComponent](D2WStatelessComponent.md)__Implements__:

- com.webobjects.directtoweb.generation.DTWGeneration

See Also:
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component displays a hyperlink representing a to-many relationship. The hyperlink navigates to a list page that displays the objects in the relationship. This component does not traverse the relationship (unlike D2WDisplayToMany, D2WDisplayToMany2, D2WDisplayToManyBrowser, and D2WDisplayToManyTable) making it appropriate for relationships that contain many objects.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to display a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WDisplayToManyFault()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kgmf2wy5bpiqzfordjonygyylzkrxu2ylopfdgc5lmoqxuimsxiruxg4dmmf4vi32nmfxhsrtbovwhilzife)

---

Private Methods

- [helpString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kgmf2wy5bpnbswy4ctorzgs3thf5jxi4tjnzts6kbj)
- [inspectArrayAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kgmf2wy5bpnfxhg4dfmn2ec4tsmf4ucy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)
- [methodNameInspectArrayAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kgmf2wy5bpnvsxi2dpmrhgc3lfjfxhg4dfmn2ec4tsmf4ucy3unfxw4l2torzgs3thf4ucs)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kgmf2wy5bpojsxa3dbmnsw2zlooraxg43pmnuwc5djn5xem33sifzxg33dnfqxi2lpnyxvot2bonzw6y3jmf2gs33of4ufot2bonzw6y3jmf2gs33ofrjxi4tjnztsyrcuk5kgk3lqnrqxizjmk5hug33oorsxq5bj)

---

__Constructors__

---

__D2WDisplayToManyFault__

public D2WDisplayToManyFault()

Standard Java no-argument constructor.

---

__Methods__

__helpString__

public String helpString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__inspectArrayAction__

public WOComponent inspectArrayAction()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameInspectArrayAction__

public String methodNameInspectArrayAction()

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
