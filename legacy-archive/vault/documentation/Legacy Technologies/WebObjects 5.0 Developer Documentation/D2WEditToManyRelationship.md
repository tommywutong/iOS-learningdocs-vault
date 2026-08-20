---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WEditToManyRelationship.html
archived_at: '2026-07-15T08:12:43.875180Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WEditToManyRelationship__

__Package__: com.webobjects.directtoweb

__Inherits from__:[EditRelationship](EditRelationship.md)See Also:
[D2WEditToManyFault](D2WEditToManyFault.md)
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component allows the user to choose which objects are in a to-many relationship. Since the component fetches all of the objects in the relationship, it is slower than the D2WEditToManyFault component, especially when the relationship has many objects.

You can specify whether the list is collapsible or not and whether the user interface is a a browser or a table of checkboxes. You can also specify the size of the browser or the number of columns of checkboxes to display.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to edit a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WEditToManyRelationship()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfjgk3dboruw63ttnbuxal2egjlukzdjorkg6tlbnz4vezlmmf2gs33oonugs4bpiqzforlenf2fi32nmfxhsutfnrqxi2lpnzzwq2lqf4ucs)

---

Private Methods

- [list](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfjgk3dboruw63ttnbuxal3mnfzxil2oknaxe4tbpexsqki)
- [methodNameToManyDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfjgk3dboruw63ttnbuxal3nmv2gq33ejzqw2zkun5gwc3tzirsxgy3snfyhi2lpnyxvg5dsnfxgolzife)
- [plurifiedStrings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfjgk3dboruw63ttnbuxal3qnr2xe2lgnfswiu3uojuw4z3tf5jxi4tjnzts6kbj)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfjgk3dboruw63ttnbuxal3smvygyyldmvwwk3tuifzxg33dnfqxi2lpnzdg64sbonzw6y3jmf2gs33of5lu6qltonxwg2lboruw63rpfblu6qltonxwg2lboruw63rmkn2he2lom4weivcxkrsw24dmmf2gklcxj5bw63tumv4hiki)
- [toManyDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu2ylopfjgk3dboruw63ttnbuxal3un5gwc3tzirsxgy3snfyhi2lpnyxvg5dsnfxgolzife)

---

__Constructors__

---

__D2WEditToManyRelationship__

public D2WEditToManyRelationship()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Methods__

__list__

public NSArray list()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameToManyDescription__

public String methodNameToManyDescription()

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

__toManyDescription__

public String toManyDescription()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
