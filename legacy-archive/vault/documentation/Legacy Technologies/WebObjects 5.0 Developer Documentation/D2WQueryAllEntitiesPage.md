---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WQueryAllEntitiesPage.html
archived_at: '2026-07-15T08:12:44.398075Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WQueryAllEntitiesPage__

__Package__:
com.webobjects.directtoweb

__Inherits from__:[D2WPage](D2WPage.md)__Implements__:

- com.webobjects.directtoweb.generation.DTWGeneration
- [QueryAllPageInterface](QueryAllPageInterface.md)

__Subclasses__:

- [WOLQueryAllPage](WOLQueryAllPage.md)
- [BASQueryAllEntitiesPage](BASQueryAllEntitiesPage.md)
- [NEUQueryAllPage](NEUQueryAllPage.md)

---

__Class Description__

---

This class provides the behavior for the query-all page Direct to Web templates, specifically BASQueryAllEntitesPage, NEUQueryAllPage, and WOLQueryAllPage. The classes for these components inherit directly from D2WQueryAllEntitiesPage and define no additional variables or methods.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the Direct to Web template's bindings (`.wod`) file. If you create a Direct to Web template from a query-all page, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WQueryAllEntitiesPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfawy3cfnz2gs5djmvzvaylhmuxuimsxkf2wk4tzifwgyrlooruxi2lfonigcz3ff5cdev2rovsxe6kbnrwek3tunf2gszltkbqwozjpfauq)

---

Fields

- [displayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfoulvmvzhsqlmnrcw45djoruwk42qmftwkl3enfzxa3dbpfdxe33voa)

---

Actions

- [queryAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfawy3cfnz2gs5djmvzvaylhmuxxc5lfoj4ucy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)
- [showRegularQueryAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfawy3cfnz2gs5djmvzvaylhmuxxg2dpo5jgkz3vnrqxeulvmvzhsqldoruw63rpk5hug33nobxw4zlooqxsqki)

Private Methods

- [queryDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfawy3cfnz2gs5djmvzvaylhmuxxc5lfoj4uiylumfjw65lsmnss6rkpirqxiyktn52xey3ff4ucs)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfawy3cfnz2gs5djmvzvaylhmuxxezlqnrqwgzlnmvxhiqltonxwg2lboruw63sgn5zec43tn5rwsylunfxw4l2xj5axg43pmnuwc5djn5xc6kcxj5axg43pmnuwc5djn5xcyu3uojuw4zzmirkfovdfnvygyylumuwfot2dn5xhizlyoquq)

---

__Constructors__

---

__D2WQueryAllEntitiesPage__

public D2WQueryAllEntitiesPage()

Standard Java no-argument constructor.

---

__Fields__

---

__displayGroup__
com.webobjects.appserver.WODisplayGroup

The WODisplayGroup object that performs the query.

---

__Methods__

__queryAction__

public WOComponent queryAction()

This action method is invoked when the user clicks the search button next to an entity in the query-all page. It returns a list page (a WOComponent) displaying the objects that match the query.

---

__queryDataSource__

public EODataSource queryDataSource()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__showRegularQueryAction__

public WOComponent showRegularQueryAction()

This action method is invoked when the user clicks the More Options button next to an entity. It returns a query page (a WOComponent for the entity.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
