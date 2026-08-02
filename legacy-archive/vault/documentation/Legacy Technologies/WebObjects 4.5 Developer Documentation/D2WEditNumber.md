---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WEditNumber.html
archived_at: '2026-07-15T08:11:30.024261Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WEditNumber__

__Package__:

__Inherits from__:[EditComponent](EditComponent.md)__Implements__:

- com.apple.yellow.webobjects.generation.DTWGeneration

See Also:
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component provides a text field for the user to enter a number. It also converts the entered text into a NSNumber object with the help of a formatter that you can specify.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to edit a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WEditNumber()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lujz2w2ytfoixuimsxivsgs5coovwwezlsf5cdev2fmruxittvnvrgk4rpfauq)

---

- [isDecimalNumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lujz2w2ytfoixws42emvrws3lbnrhhk3lcmvzc6ytpn5wgkylof4ucs)

Private Methods

- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lujz2w2ytfoixxezlqnrqwgzlnmvxhiqltonxwg2lboruw63sgn5zec43tn5rwsylunfxw4l2xj5axg43pmnuwc5djn5xc6kcxj5axg43pmnuwc5djn5xcyu3uojuw4zzmirkfovdfnvygyylumuwfot2dn5xhizlyoquq)

---

__Constructors__

---

__D2WEditNumber__

public D2WEditNumber()

Standard Java no-argument constructor.

---

__Methods__

__isDecimalNumber__

public boolean isDecimalNumber()

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---
