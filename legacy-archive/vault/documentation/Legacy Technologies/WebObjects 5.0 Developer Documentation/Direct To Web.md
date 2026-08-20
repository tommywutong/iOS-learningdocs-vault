---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Introduction.html
archived_at: '2026-07-15T08:12:45.933077Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](DirectToWebTOC.md)

# Direct To Web

> **__Packages:__**
> : com.webobjects.directtoweb
> : com.apple.client.directtoweb

---

## Introduction

The Direct to Web class hierarchy has two roots. Most of the classes descend from the WebObjects WOComponent class. The remaining objects descend from the Java Object class. Some [classes](Direct%20to%20Web%20API%20Reference.md#apple-obzgs5tborsug3dbonzwk4y) and [interfaces](Direct%20to%20Web%20API%20Reference.md#apple-obzgs5tborsus3tumvzgmyldmvzq) in this framework are private but are declared public and appear in the Java Browser. You should not use, subclass, or replace them.

The public classes within the Direct to Web framework
can be grouped as follows:

- Application Level Classes. [D2W](D2W.md) creates Direct to Web pages and manages application-level settings.
- Component Superclasses. [D2WComponent](D2WComponent.md) is the superclass of every Direct to Web component that resolves keys using a Direct to Web context, including the Direct to Web pages and the property-level components. D2WPage is the superclass of every Direct to Web page, specifically the Direct to Web template implementation classes.
- Direct to Web Context Class. [D2WContext](D2WContext.md) resolves the keys, often with the help of the rule system, for Direct to Web template components and property-level components.
- Direct to Web Template Implementation Classes. [D2WConfirmPage](D2WConfirmPage.md), [D2WErrorPage](D2WErrorPage.md), [D2WInspectPage](D2WInspectPage.md), [D2WListPage](D2WListPage.md), [D2WMasterDetailPage](D2WMasterDetailPage.md), [D2WPlainListPage](D2WPlainListPage.md), [D2WQueryAllEntitiesPage](D2WQueryAllEntitiesPage.md), [D2WQueryPage](D2WQueryPage.md), and [D2WTabInspectPage](D2WTabInspectPage.md), implement the behaviors of the respective Direct to Web templates. Note that the [Direct to Web template classes](Direct%20to%20Web%20API%20Reference.md#apple-iqzfovdfnvygyylumvzq) inherit directly from the implementation classes and define no additional variables or methods.
- Miscellaneous Components. [D2WHead](D2WHead.md) contains the HTML between the <HEAD> and </HEAD> tags that is generated for every Direct to Web page. [DefaultHeader](DefaultHeader.md) defines the behavior of the application's menu header. You can also find this code in your project's `MenuHeader.java` file.

The public interfaces can be grouped as follows:

- Page Creation Interfaces. [ConfirmPageInterface](ConfirmPageInterface.md), [EditPageInterface](EditPageInterface.md), [EditRelationshipPageInterface](EditRelationshipPageInterface.md),
  [ErrorPageInterface](ErrorPageInterface.md), [InspectPageInterface](InspectPageInterface.md), [ListPageInterface](ListPageInterface.md), [QueryAllPageInterface](QueryAllPageInterface.md), [QueryPageInterface](QueryPageInterface.md), and [SelectPageInterface](SelectPageInterface.md) allow you to initialize newly-created Direct to Web pages.
- Next Page Delegate Interface. [NextPageDelegate](NextPageDelegate.md) provides a way to provide customized behavior when a the user exits a Direct to Web page.

In addition to the specifications to the public classes, this reference provides:

- Direct to Web Reusable Component binding specifications. [D2WEdit](D2WEdit.md), [D2WInspect](D2WInspect.md), [D2WList](D2WList.md), [D2WQuery](D2WQuery.md), and [D2WSelect](D2WSelect.md) can be embedded in a WebObjects component to display a Direct to Web page. An [introduction](Direct%20to%20Web%20Reusable%20Component%20Specifications.md) is also included. You never need to use the classes directly.
- Property-Level Components class descriptions. The [property-level components](Direct%20to%20Web%20API%20Reference.md#apple-obzg64dfoj2hstdfozswyq3pnvyg63tfnz2hg) display, edit, or query for a single property of an entity. Although you never use the classes directly, you can use the Web Assistant to configure your Direct to Web pages to use particular property-level components.

For more information about using the Direct to Web framework, refer to _Developing WebObjects Applications With Direct to Web_.

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](DirectToWebTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
