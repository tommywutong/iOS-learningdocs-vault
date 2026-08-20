---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WDisplayToMany.html
archived_at: '2026-07-15T08:12:43.554896Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WDisplayToMany__

__Package__: com.webobjects.directtoweb

__Inherits from__:[D2WComponent](D2WComponent.md)__Implements__:

- com.webobjects.directtoweb.generation.DTWGeneration

__Subclasses__:

- [D2WDisplayToManyBrowser](D2WDisplayToManyBrowser.md)
- [D2WDisplayToMany2](D2WDisplayToMany2.md)
- [D2WDisplayToManyTable](D2WDisplayToManyTable.md)

See Also:
[D2WDisplayToManyFault](D2WDisplayToManyFault.md)
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component displays the first few objects of a to-many relationship in a list. You can specify whether the list is collapsible or not. Since the component fetches all of the objects in the relationship, it is slower than the D2WDisplayToManyFault component, especially when the relationship has many objects.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to display a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WDisplayToMany()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpiqzfordjonygyylzkrxu2ylopexuimsxiruxg4dmmf4vi32nmfxhslzife)

---

Private Methods

- [inspectArrayAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpnfxhg4dfmn2ec4tsmf4ucy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)
- [inspectArrayActionString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpnfxhg4dfmn2ec4tsmf4ucy3unfxw4u3uojuw4zzpkn2he2lom4xsqki)
- [ivarNameForBrowserItem](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpnf3gc4somfwwkrtpojbhe33xonsxeslumvws6u3uojuw4zzpfauq)
- [list](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpnruxg5bpjzjuc4tsmf4s6kbj)
- [listDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpnruxg5cemvzwg4tjob2gs33of5jxi4tjnzts6kbj)
- [methodNameForShouldDisplay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpnvsxi2dpmrhgc3lfizxxeu3in52wyzcenfzxa3dbpexvg5dsnfxgolzife)
- [methodNameInspectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpnvsxi2dpmrhgc3lfjfxhg4dfmn2ecy3unfxw4l2torzgs3thf4ucs)
- [methodNameInspectArrayAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpnvsxi2dpmrhgc3lfjfxhg4dfmn2ec4tsmf4ucy3unfxw4l2torzgs3thf4ucs)
- [methodNameListDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpnvsxi2dpmrhgc3lfjruxg5cemvzwg4tjob2gs33of5jxi4tjnzts6kbj)
- [plurifiedStrings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpobwhk4tjmzuwkzctorzgs3thomxvg5dsnfxgolzife)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jpojsxa3dbmnsw2zlooraxg43pmnuwc5djn5xem33sifzxg33dnfqxi2lpnyxvot2bonzw6y3jmf2gs33of4ufot2bonzw6y3jmf2gs33ofrjxi4tjnztsyrcuk5kgk3lqnrqxizjmk5hug33oorsxq5bj)
- [setInspectArrayAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jponsxisloonygky3uifzheylzifrxi2lpnyxxm33jmqxsqt3cnjswg5bj)
- [setList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jponsxitdjon2c65tpnfsc6kcpmjvgky3ufe)
- [shouldDisplay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46jponug65lmmrcgs43qnrqxsl3cn5xwyzlbnyxsqki)

---

__Constructors__

---

__D2WDisplayToMany__

public D2WDisplayToMany()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Methods__

__inspectArrayAction__

public WOComponent inspectArrayAction()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__inspectArrayActionString__

public String inspectArrayActionString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__ivarNameForBrowserItem__

public String ivarNameForBrowserItem()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__list__

public NSArray list()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__listDescription__

public String listDescription()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameForShouldDisplay__

public String methodNameForShouldDisplay()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameInspectAction__

public String methodNameInspectAction()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameInspectArrayAction__

public String methodNameInspectArrayAction()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameListDescription__

public String methodNameListDescription()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__plurifiedStrings__

public String plurifiedStrings()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setInspectArrayAction__

public void setInspectArrayAction(Object anObject)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setList__

public void setList(Object anObject)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__shouldDisplay__

public boolean shouldDisplay()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
