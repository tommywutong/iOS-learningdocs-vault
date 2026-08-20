---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/Direct_to_W_rganization.html
archived_at: '2026-07-15T08:12:22.034446Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Property_Level_Components.md)[![Next](attachments/DirectToWeb/Images/next.gif)](The_Direct_to_Web_Context.md)

## Direct to Web Component Organization

[Figure 3-1](#apple-ijauussijjduk) shows the components in
an edit page for the Movie entity in the Neutral look. The top-level component is
a Direct to Web template called `NEUInspectPage.wo`. It contains the
project's `PageWrapper.wo` component, which defines the overall layout
of the page. The `PageWrapper.wo` component contains the
`MenuHeader.wo` component, which defines the Direct to Web navigation
menu. See ["The Structure of a
Direct to Web Project"](../WalkThrough/The_Structu_Web_Project.md#apple-ijauesceivbuo) for more information about `PageWrapper.wo`
and `MenuHeader.wo`.

__Figure 3-1 Edit page component
organization__

![[image: ../Art/EditPageComponents.gif]](../Art/EditPageComponents.gif)

The `PageWrapper.wo` component content comes
from the NEUInspectPage Direct to Web template. This content includes HTML input
elements for the visible attributes of an entity. Each attribute appears in a
separate property-level component that depends on the attribute's type. The
`category` attribute displays using a D2WEditString component. The
`dateReleased` attribute displays using a D2WEditDate
component.

Pages with nested Direct to Web
templates contain Direct to Web reusable components. [Figure
3-2](#apple-ijauur2binbus) shows a master detail page in the Neutral look. The
`NEUMasterDetail.wo` Direct to Web template contains
`PageWrapper.wo` which in turn, contains `MenuHeader.wo`.
`NEUMasterDetail.wo` also contains two reusable components that act as
interfaces to the templates they display: a D2WSelect component and a D2WEdit
component. Each of these components is actually a WOSwitchComponent that displays
a template-the D2WSelect component displays a NEUListPage Direct to Web template
and the D2WEdit component displays a NEUInspectPage Direct to Web
template.

__Figure 3-2 Master-detail page component
organization__

![[image: ../Art/MasterDetailPageComponents.gif]](../Art/masterdetailpagecomponents.gif)

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Property_Level_Components.md)[![Next](attachments/DirectToWeb/Images/next.gif)](The_Direct_to_Web_Context.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
