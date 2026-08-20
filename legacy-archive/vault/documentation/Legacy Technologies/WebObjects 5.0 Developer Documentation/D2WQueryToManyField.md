---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WQueryToManyField.html
archived_at: '2026-07-15T08:12:44.665121Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WQueryToManyField__

__Package__: com.webobjects.directtoweb

__Inherits from__:[QueryComponent](QueryComponent.md)See Also:
[D2WCustomQueryComponent](D2WCustomQueryComponent.md)

---

__Class Description__

---

This property-level component builds a query based on the value for a particular key of a destination object of a to-many relationship. Since this component does not traverse the relationship (unlike D2WQueryToManyRelationship), it is appropriate when the relationship has many objects.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to query based on a property, use D2WCustomQueryComponent.

__Method Types__

---

Constructors

- [public D2WQueryToManyField()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfkg6tlbnz4um2lfnrsc6rbsk5ixkzlspfkg6tlbnz4um2lfnrsc6rbsk5ixkzlspfkg6tlbnz4um2lfnrsc6kbj)

---

Private Methods

- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfkg6tlbnz4um2lfnrsc64tfobwgcy3fnvsw45cbonzw6y3jmf2gs33oizxxeqltonxwg2lboruw63rpk5huc43tn5rwsylunfxw4lzik5huc43tn5rwsylunfxw4lctorzgs3thfrcfiv2umvwxa3dborssyv2pinxw45dfpb2cs)
- [reset](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfkg6tlbnz4um2lfnrsc64tfonsxil3wn5uwilzife)
- [setValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfkg6tlbnz4um2lfnrsc643forlgc3dvmuxxm33jmqxsqt3cnjswg5bj)
- [value](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfkg6tlbnz4um2lfnrsc65tbnr2wkl2pmjvgky3uf4ucs)

---

__Constructors__

---

__D2WQueryToManyField__

public D2WQueryToManyField()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Methods__

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__reset__

public void reset()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setValue__

public void setValue(Object anObject)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__value__

public Object value()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
