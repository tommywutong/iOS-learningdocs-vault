---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WCustomQueryComponent.html
archived_at: '2026-07-15T08:11:29.767135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WCustomQueryComponent__

__Package__:

__Inherits from__:[D2WComponent](D2WComponent.md)

---

__Class Description__

---

This component allows you to use a WebObjects reusable component as a property-level component that performs queries. D2WCustomQueryComponent passes two bindings to the reusable component: `displayGroup`, which specifies the display group that performs the query, and `key`, which specifies the key representing the objects in the display group.
The reusable component needs to set the display group's query dictionaries: `queryMatch`, `queryMax`, `queryMin`, and `queryOperator`. See the WODisplayGroup class specification in the _WebObjects Framework Reference_ for more information.

__Method Types__

---

Constructors

- [public D2WCustomQueryComponent()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bxk43un5wvc5lfoj4ug33nobxw4zlooqxuimsxin2xg5dpnvixkzlspfbw63lqn5xgk3tuf5cdev2dovzxi33nkf2wk4tzinxw24dpnzsw45bpfauq)

---

Fields

- [displayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfoq3von2g63krovsxe6kdn5wxa33omvxhil3enfzxa3dbpfdxe33voa)

---

---

__Constructors__

---

__D2WCustomQueryComponent__

public D2WCustomQueryComponent()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Fields__

---

__displayGroup__
com.apple.yellow.webobjects.WODisplayGroup

The display group that receives the values for the query keys.

---
