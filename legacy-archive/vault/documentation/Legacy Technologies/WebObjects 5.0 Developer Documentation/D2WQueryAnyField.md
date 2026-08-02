---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WQueryAnyField.html
archived_at: '2026-07-15T08:12:44.419026Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WQueryAnyField__

__Package__: com.webobjects.directtoweb

__Inherits from__:[QueryComponent](QueryComponent.md)

---

__Class Description__

---

This property-level component builds a query based on the destination objects of a relationship. The user can specify the key for an attribute of the destination object and a value the attribute must have. This object does not traverse the relationship making it appropriate for relationships that contain many objects.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to query based on a property, use D2WCustomQueryComponent.

__Method Types__

---

Constructors

- [public D2WQueryAnyField()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfaw46kgnfswyzbpiqzfoulvmvzhsqlopfdgszlmmqxuimsxkf2wk4tzifxhsrtjmvwgilzife)

---

- [componentsForDisplayKeyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfaw46kgnfswyzbpmnxw24dpnzsw45dtizxxerdjonygyylzjnsxstdjon2c6u3uojuw4zzpfauq)
- [componentsForKeyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfaw46kgnfswyzbpmnxw24dpnzsw45dtizxxes3fpfggs43uf5jxi4tjnzts6kbj)
- [relationshipContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfaw46kgnfswyzbpojswyylunfxw443infyeg33oorsxq5bpiqzfoq3pnz2gk6duf4ucs)
- [relationshipContextDisplayAttributesKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfaw46kgnfswyzbpojswyylunfxw443infyeg33oorsxq5cenfzxa3dbpfaxi5dsnfrhk5dfonfwk6ltf5hfgqlsojqxslzife)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfaw46kgnfswyzbpojsxa3dbmnsw2zlooraxg43pmnuwc5djn5xem33sifzxg33dnfqxi2lpnyxvot2bonzw6y3jmf2gs33of4ufot2bonzw6y3jmf2gs33ofrjxi4tjnztsyrcuk5kgk3lqnrqxizjmk5hug33oorsxq5bj)
- [reset](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfaw46kgnfswyzbpojsxgzluf53g62lef4ucs)
- [selectedKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfaw46kgnfswyzbponswyzldorswis3fpexvg5dsnfxgolzife)
- [setSelectedKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfaw46kgnfswyzbponsxiu3fnrswg5dfmrfwk6jpozxwszbpfbjxi4tjnztss)
- [variableNameForKeyList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfaw46kgnfswyzbpozqxe2lbmjwgkttbnvsum33sjnsxstdjon2c6u3uojuw4zzpfauq)

---

__Constructors__

---

__D2WQueryAnyField__

public D2WQueryAnyField()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Methods__

__componentsForDisplayKeyList__

public String componentsForDisplayKeyList()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__componentsForKeyList__

public String componentsForKeyList()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__relationshipContext__

public D2WContext relationshipContext()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__relationshipContextDisplayAttributesKeys__

public NSArray relationshipContextDisplayAttributesKeys()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__reset__

public void reset()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__selectedKey__

public String selectedKey()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setSelectedKey__

public void setSelectedKey(String)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__variableNameForKeyList__

public String variableNameForKeyList()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
