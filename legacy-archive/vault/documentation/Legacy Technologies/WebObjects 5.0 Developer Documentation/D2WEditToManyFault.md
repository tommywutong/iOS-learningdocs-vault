---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WEditToManyFault.html
archived_at: '2026-07-15T08:12:43.857341Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WEditToManyFault__

__Package__: com.webobjects.directtoweb

__Inherits from__:[D2WComponent](D2WComponent.md)See Also:
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component displays a hyperlink representing a to-many relationship. The hyperlink navigates to an edit-relationship page that allows the user to change which objects are in the relationship. This component does not traverse the relationship (unlike D2WEditToManyRelationship) making it appropriate for relationships that contain many objects.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to edit a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WEditToManyFault()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxuimsxivsgs5cun5gwc3tzizqxk3duf5cdev2fmruxivdpjvqw46kgmf2wy5bpfauq)

---

- [browserList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxwe4tpo5zwk4smnfzxil2oknaxe4tbpexsqki)
- [browserListDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxwe4tpo5zwk4smnfzxirdfonrxe2lqoruw63rpkn2he2lom4xsqki)
- [browserStringForItem](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxwe4tpo5zwk4storzgs3thizxxeslumvws6u3uojuw4zzpfauq)

Private Methods

- [editValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxwkzdjorlgc3dvmvzs6v2pinxw24dpnzsw45bpfauq)
- [helpString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxwqzlmobjxi4tjnzts6u3uojuw4zzpfauq)
- [ivarNameForBrowserItem](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxws5tbojhgc3lfizxxeqtsn53xgzlsjf2gk3jpkn2he2lom4xsqki)
- [methodNameBrowserListDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxw2zlunbxwittbnvsue4tpo5zwk4smnfzxirdfonrxe2lqoruw63rpkn2he2lom4xsqki)
- [methodNameForEditValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxw2zlunbxwittbnvsum33sivsgs5cwmfwhkzltf5jxi4tjnzts6kbj)
- [methodNameListDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxw2zlunbxwittbnvsuy2ltorcgk43dojuxa5djn5xc6u3uojuw4zzpfauq)
- [plurifiedStrings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxxa3dvojuwm2lfmrjxi4tjnztxgl2torzgs3thf4ucs)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfdgc5lmoqxxezlqnrqwgzlnmvxhiqltonxwg2lboruw63sgn5zec43tn5rwsylunfxw4l2xj5axg43pmnuwc5djn5xc6kcxj5axg43pmnuwc5djn5xcyu3uojuw4zzmirkfovdfnvygyylumuwfot2dn5xhizlyoquq)

---

__Constructors__

---

__D2WEditToManyFault__

public D2WEditToManyFault()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Methods__

__browserList__

public NSArray browserList()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__browserListDescription__

public String browserListDescription()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__browserStringForItem__

public String browserStringForItem()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__editValues__

public WOComponent editValues()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__helpString__

public String helpString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__ivarNameForBrowserItem__

public String ivarNameForBrowserItem()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameBrowserListDescription__

public String methodNameBrowserListDescription()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameForEditValues__

public String methodNameForEditValues()

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

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
