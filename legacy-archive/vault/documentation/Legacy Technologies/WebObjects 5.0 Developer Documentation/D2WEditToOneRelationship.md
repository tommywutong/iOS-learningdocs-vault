---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WEditToOneRelationship.html
archived_at: '2026-07-15T08:12:43.910495Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WEditToOneRelationship__

__Package__: com.webobjects.directtoweb

__Inherits from__:[EditRelationship](EditRelationship.md)See Also:
[D2WEditToOneFault](D2WEditToOneFault.md)
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component allows the user to choose the destination object of a to-one relationship. Since the component fetches all of the objects that can appear in the relationship, this component is slower than the D2WEditToOneFault component.

You can specify whether the user interface is a browser, pop-up list, or table of radio buttons. You can also specify the size of the browser or the number of columns of radio buttons to display.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to edit a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WEditToOneRelationship()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu63tfkjswyylunfxw443infyc6rbsk5cwi2lukrxu63tfkjswyylunfxw443infyc6rbsk5cwi2lukrxu63tfkjswyylunfxw443infyc6kbj)

---

- [generatedToOneDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu63tfkjswyylunfxw443infyc6z3fnzsxeylumvsfi32pnzsuizltmnzgs4dunfxw4l2torzgs3thf4ucs)
- [methodNameToOneDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu63tfkjswyylunfxw443infyc63lforug6zcomfwwkvdpj5xgkrdfonrxe2lqoruw63rpkn2he2lom4xsqki)
- [toOneDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu63tfkjswyylunfxw443infyc65dpj5xgkrdfonrxe2lqoruw63rpj5rguzldoqxsqki)

Private Methods

- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukrxu63tfkjswyylunfxw443infyc64tfobwgcy3fnvsw45cbonzw6y3jmf2gs33oizxxeqltonxwg2lboruw63rpk5huc43tn5rwsylunfxw4lzik5huc43tn5rwsylunfxw4lctorzgs3thfrcfiv2umvwxa3dborssyv2pinxw45dfpb2cs)

---

__Constructors__

---

__D2WEditToOneRelationship__

public D2WEditToOneRelationship()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Methods__

__generatedToOneDescription__

public String generatedToOneDescription()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameToOneDescription__

public String methodNameToOneDescription()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__toOneDescription__

public Object toOneDescription()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
