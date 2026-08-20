---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb6.html
archived_at: '2026-07-18T01:25:10.164595Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb5.md)

## Dynamically Generated Pages

Besides the login page, there are nine types of dynamically-generated pages (or reusable components) in a Direct to Web application:

- A _query-all page_ that displays all entities that are currently exposed and lets users construct queries on the attributes (but not the relationships) of those entities; see ["Query Pages"](DirectToWeb7.md#apple-guytkni). This properties of this page cannot be customized.
- A _query page_ that allows the user to construct a query for a particular entity; see ["Query Pages"](DirectToWeb7.md#apple-guytkni).
- A _list page_ that displays one or more records of a particular entity in tabular form; see ["List Pages and Select Components"](Using%20Direct%20to%20Web%20in%20Other%20WebObjects%20Applications.md#apple-gezdqmzt). The result of a query is always a list page.
- An _inspect page_ that displays a single record of a given entity; see ["Inspect and Edit Pages"](DirectToWeb9.md#apple-guytmni).
- An _edit page_ that displays a single record of a given entity and also allows you to make changes to the record and save it to the database; see ["Inspect and Edit Pages"](DirectToWeb9.md#apple-guytmni).
- A _select component_ that lets users select a record from a list, thereby adding it to a to-many relationship or populating an edit component with it; see ["List Pages and Select Components"](Using%20Direct%20to%20Web%20in%20Other%20WebObjects%20Applications.md#apple-gezdqmzt).
- A _master-detail_ _page_ consists of a select component and an edit component; it allows you to select and edit a record without having to switch to another page. See ["Master-Detail Pages"](DirectToWeb11.md#apple-geydkobz).
- An _edit-relationship page_ is a multiple component page for removing and adding objects to a to-many relationship. See ["Edit-Relationship Pages"](DirectToWeb10.md#apple-geydkobr).
- An _error page_ for displaying information related to exceptions and other errors. This properties of this page cannot be customized.

All pages in your application contain the standard Direct to Web header (defined in __PageWrapper.wo__) at the top of the page. This header provides a number of controls, described in the following figure.

!

For best results when navigating through a Direct to Web application, don't use your web browser's backtrack buttons. Instead:

- To return to the previous page from an edit or inspect page, click Cancel.
- To return to a query page from a list page, select the entity in the Entities pop-up menu and click Build Query.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb7.md)
