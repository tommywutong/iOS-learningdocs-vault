---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WDisplayToManyBrowser.html
archived_at: '2026-07-15T08:12:43.599492Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WDisplayToManyBrowser__

__Package__: com.webobjects.directtoweb

__Inherits from__:[D2WDisplayToMany](D2WDisplayToMany.md)See Also:
[D2WDisplayToManyFault](D2WDisplayToManyFault.md)
[D2WCustomComponent](D2WCustomComponent.md)

---

__Class Description__

---

This property-level component displays the objects of a to-many relationship in a browser. You can specify whether the browser is collapsible or not. Since the component fetches all of the objects in the relationship, it is slower than the D2WDisplayToManyFault component, especially when the relationship has many objects.

Property-level components are not accessed programmatically. Instead, you use the Web Assistant to choose the property-level component that Direct to Web uses to display a property on a particular entity and task page. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information.

If you want to create property-level component to display a property, use D2WCustomComponent.

__Method Types__

---

Constructors

- [public D2WDisplayToManyBrowser()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kcojxxo43foixuimsxiruxg4dmmf4vi32nmfxhsqtsn53xgzlsf5cdev2enfzxa3dbpfkg6tlbnz4ue4tpo5zwk4rpfauq)

---

Fields

- [browserItem](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfordjonygyylzkrxu2ylopfbhe33xonsxel3cojxxo43fojexizln)

---

Private Methods

- [browserStringForItem](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kcojxxo43foixwe4tpo5zwk4storzgs3thizxxeslumvws6u3uojuw4zzpfauq)
- [ivarNameForBrowserItem](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kcojxxo43foixws5tbojhgc3lfizxxeqtsn53xgzlsjf2gk3jpkn2he2lom4xsqki)
- [methodNameForBrowserStringForItem](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kcojxxo43foixw2zlunbxwittbnvsum33sijzg653tmvzfg5dsnfxgortpojexizlnf5jxi4tjnzts6kbj)
- [methodNameInspectArrayAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kcojxxo43foixw2zlunbxwittbnvsus3ttobswg5cbojzgc6kbmn2gs33of5jxi4tjnzts6kbj)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cgs43qnrqxsvdpjvqw46kcojxxo43foixxezlqnrqwgzlnmvxhiqltonxwg2lboruw63sgn5zec43tn5rwsylunfxw4l2xj5axg43pmnuwc5djn5xc6kcxj5axg43pmnuwc5djn5xcyu3uojuw4zzmirkfovdfnvygyylumuwfot2dn5xhizlyoquq)

---

__Constructors__

---

__D2WDisplayToManyBrowser__

public D2WDisplayToManyBrowser()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Fields__

---

__browserItem__
com.webobjects.eocontrol.EOEnterpriseObject

This constant is intentionally undocumented.

---

__Methods__

__browserStringForItem__

public String browserStringForItem()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__ivarNameForBrowserItem__

public String ivarNameForBrowserItem()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__methodNameForBrowserStringForItem__

public String methodNameForBrowserStringForItem()

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
