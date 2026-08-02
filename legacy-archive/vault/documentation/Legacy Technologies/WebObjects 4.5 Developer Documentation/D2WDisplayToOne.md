---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WDisplayToOne.html
archived_at: '2026-07-15T08:11:29.959273Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WDisplayToOne__

__Package__:

__Inherits from__:[D2WStatelessComponent](D2WStatelessComponent.md)__Implements__:

- com.apple.yellow.webobjects.generation.DTWGeneration

__Subclasses__:

- [D2WEditToOneFault](D2WEditToOneFault.md)

See Also:
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component displays the destination object of a to-one relationship.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to display a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WDisplayToOne()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpj5xgkl2egjlui2ltobwgc6kun5hw4zjpiqzfordjonygyylzkrxu63tff4ucs)

---

Private Methods

- [methodNameForToOneAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpj5xgkl3nmv2gq33ejzqw2zkgn5zfi32pnzsucy3unfxw4l2torzgs3thf4ucs)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpj5xgkl3smvygyyldmvwwk3tuifzxg33dnfqxi2lpnzdg64sbonzw6y3jmf2gs33of5lu6qltonxwg2lboruw63rpfblu6qltonxwg2lboruw63rmkn2he2lom4weivcxkrsw24dmmf2gklcxj5bw63tumv4hiki)
- [toOneAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpj5xgkl3un5hw4zkbmn2gs33of5lu6q3pnvyg63tfnz2c6kbj)
- [toOneDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpj5xgkl3un5hw4zkemvzwg4tjob2gs33of5hwe2tfmn2c6kbj)

---

__Constructors__

---

__D2WDisplayToOne__

public D2WDisplayToOne()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Methods__

__methodNameForToOneAction__

public String methodNameForToOneAction()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__toOneAction__

public WOComponent toOneAction()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__toOneDescription__

public Object toOneDescription()

This method is intentionally undocumented. You should never have to invoke or customize it.

---
