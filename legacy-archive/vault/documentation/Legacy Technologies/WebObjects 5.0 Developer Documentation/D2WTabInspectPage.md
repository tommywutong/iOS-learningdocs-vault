---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WTabInspectPage.html
archived_at: '2026-07-15T08:12:44.867035Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WTabInspectPage__

__Package__:
com.webobjects.directtoweb

__Inherits from__:[D2WInspectPage](D2WInspectPage.md)__Subclasses__:

- [NEUTabInspectPage](NEUTabInspectPage.md)
- [WOLTabInspectPage](WOLTabInspectPage.md)

---

__Class Description__

---

This class provides the behavior for the tab-inspect page Direct to Web templates, specifically NEUTabInspectPage and WOLTabInspectPage. The classes for these components inherit directly from D2WTabInspectPage and define no additional variables or methods.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the Direct to Web template's bindings (`.wod`) file. If you create a Direct to Web template from a tab-inspect page, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WTabInspectPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kgcysjnzzxazldorigcz3ff5cdev2umfres3ttobswg5cqmftwkl2egjlviylcjfxhg4dfmn2faylhmuxsqki)

---

Key-Value Coding

- [defaultRowspan](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kgcysjnzzxazldorigcz3ff5sgkztbovwhiutpo5zxaylof5jxi4tjnzts6kbj)
- [displayedTabName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kgcysjnzzxazldorigcz3ff5sgs43qnrqxszlekrqwettbnvss6u3uojuw4zzpfauq)
- [isPropertyInHeader](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kgcysjnzzxazldorigcz3ff5uxgudsn5ygk4tupfew4sdfmfsgk4rpmjxw63dfmfxc6kbj)
- [setDisplayedTabName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kgcysjnzzxazldorigcz3ff5zwk5cenfzxa3dbpfswivdbmjhgc3lff53g62lef4ufg5dsnfxgoki)
- [tabs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kgcysjnzzxazldorigcz3ff52gcyttf5hfgqlsojqxslzife)

Private Methods

- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kgcysjnzzxazldorigcz3ff5zgk4dmmfrwk3lfnz2ec43tn5rwsylunfxw4rtpojaxg43pmnuwc5djn5xc6v2pifzxg33dnfqxi2lpnyxsqv2pifzxg33dnfqxi2lpnywfg5dsnfxgolcekrlvizlnobwgc5dffrlu6q3pnz2gk6dufe)
- [tabContents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kgcysjnzzxazldorigcz3ff52gcysdn5xhizloorzs6tstiruwg5djn5xgc4tzf4ucs)
- [tabNameIsInHeader](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kgcysjnzzxazldorigcz3ff52gcysomfwwksltjfxeqzlbmrsxel3cn5xwyzlbnyxsqu3uojuw4zzj)
- [tabsAsString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kgcysjnzzxazldorigcz3ff52gcyttifzvg5dsnfxgol2torzgs3thf4ucs)

---

__Constructors__

---

__D2WTabInspectPage__

public D2WTabInspectPage()

Standard Java no-argument constructor.

---

__Methods__

__defaultRowspan__

public String defaultRowspan()

Returns a String containing the number of HTML table rows spanned by the vertical rule within the current tab panel in the tab inspect page.

---

__displayedTabName__

public String displayedTabName()

Returns the name of the tab that is being displayed.

---

__isPropertyInHeader__

public boolean isPropertyInHeader()

Returns whether the current property in the receiver's Direct to Web context is outside the tab panel (and consequently in the header) or not.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setDisplayedTabName__

public void setDisplayedTabName(String tabName)

Sets the displayed tab to the one with the name `tabName`.

---

__tabContents__

public NSDictionary tabContents()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__tabNameIsInHeader__

public boolean tabNameIsInHeader(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__tabs__

public NSArray tabs()

Returns an array (an NSArray object) containing the names of the tabs displayed in the tab inspect page. This key is resolved using the rule system.

---

__tabsAsString__

public String tabsAsString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
