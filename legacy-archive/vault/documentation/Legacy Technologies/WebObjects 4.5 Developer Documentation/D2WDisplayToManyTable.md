---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WDisplayToManyTable.html
archived_at: '2026-07-15T08:11:29.946977Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WDisplayToManyTable__

__Package__:

__Inherits from__:[D2WDisplayToMany](D2WDisplayToMany.md)See Also:
[D2WDisplayToManyFault](D2WDisplayToManyFault.md)
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component displays the objects of a to-many relationship in a table. You can specify the number of columns in the table and whether the browser is collapsible or not. Since the component fetches all of the objects in the relationship, it is slower than the D2WDisplayToManyFault component, especially when the relationship has many objects.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to display a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WDisplayToManyTable()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kumfrgyzjpiqzfordjonygyylzkrxu2ylopfkgcytmmuxuimsxiruxg4dmmf4vi32nmfxhsvdbmjwgklzife)

---

Fields

- [item](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfordjonygyylzkrxu2ylopfkgcytmmuxws5dfnu)

---

Private Methods

- [inspectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kumfrgyzjpnfxhg4dfmn2ecy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kumfrgyzjpojsxa3dbmnsw2zlooraxg43pmnuwc5djn5xem33sifzxg33dnfqxi2lpnyxvot2bonzw6y3jmf2gs33of4ufot2bonzw6y3jmf2gs33ofrjxi4tjnztsyrcuk5kgk3lqnrqxizjmk5hug33oorsxq5bj)
- [stringForItem](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kumfrgyzjpon2he2lom5dg64sjorsw2l2pmjvgky3uf4ucs)

---

__Constructors__

---

__D2WDisplayToManyTable__

public D2WDisplayToManyTable()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Fields__

---

__item__
com.apple.yellow.eocontrol.EOEnterpriseObject

This constant is intentionally undocumented.

---

__Methods__

__inspectAction__

public WOComponent inspectAction()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__stringForItem__

public Object stringForItem()

This method is intentionally undocumented. You should never have to invoke or customize it.

---
