---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WMasterDetailPage.html
archived_at: '2026-07-15T08:12:44.218420Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WMasterDetailPage__

__Package__:
com.webobjects.directtoweb

__Inherits from__:[D2WPage](D2WPage.md)__Implements__:

- [ListPageInterface](ListPageInterface.md)

__Subclasses__:

- [WOLMasterDetailPage](WOLMasterDetailPage.md)
- [BASMasterDetailPage](BASMasterDetailPage.md)
- [NEUMasterDetailPage](NEUMasterDetailPage.md)

---

__Class Description__

---

This class provides the behavior for the master-detail page Direct to Web tempaltes, specifically BASMasterDetailPage, NEUMasterDetailPage, and WOLMasterDetailPage. The classes for these pages inherit directly from D2WMasterDetailPage and define no additional methods or variables.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the Direct to Web template's bindings (`.wod`) file. If you create a Direct to Web template from a master-detail page, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WMasterDetailPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gwc43umvzeizlumfuwyudbm5ss6rbsk5gwc43umvzeizlumfuwyudbm5ss6rbsk5gwc43umvzeizlumfuwyudbm5ss6kbj)

---

Fields

- [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfotlbon2gk4semv2gc2lmkbqwozjponswyzldorswit3cnjswg5a)

---

Actions

- [listReturnAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gwc43umvzeizlumfuwyudbm5ss63djon2fezluovzg4qldoruw63rpk5hug33nobxw4zlooqxsqki)

Key-Value Coding

- [isObjectSelected](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gwc43umvzeizlumfuwyudbm5ss62ltj5rguzldorjwk3dfmn2gkzbpmjxw63dfmfxc6kbj)
- [masterDetailPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gwc43umvzeizlumfuwyudbm5ss63lbon2gk4semv2gc2lmkbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq)
- [selectPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gwc43umvzeizlumfuwyudbm5ss643fnrswg5cqmftwkrdfnrswoylumuxu4zlyorigcz3firswyzlhmf2gklzife)

Private Methods

- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gwc43umvzeizlumfuwyudbm5ss64tfobwgcy3fnvsw45cbonzw6y3jmf2gs33oizxxeqltonxwg2lboruw63rpk5huc43tn5rwsylunfxw4lzik5huc43tn5rwsylunfxw4lctorzgs3thfrcfiv2umvwxa3dborssyv2pinxw45dfpb2cs)
- [setEditPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gwc43umvzeizlumfuwyudbm5ss643forcwi2lukbqwozkemvwgkz3borss65tpnfsc6kcpmjvgky3ufe)
- [setSelectPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5gwc43umvzeizlumfuwyudbm5ss643forjwk3dfmn2faylhmvcgk3dfm5qxizjpozxwszbpfbhwe2tfmn2cs)

---

__Constructors__

---

__D2WMasterDetailPage__

public D2WMasterDetailPage()

Standard Java no-argument constructor.

---

__Fields__

---

__selectedObject__
com.webobjects.eocontrol.EOEnterpriseObject

The EOEnterpriseObject the user chooses in the select component of the page. The edit component edits this object.

---

__Methods__

__isObjectSelected__

public boolean isObjectSelected()

Returns whether the user has selected an object in the select component of the master-detail page. When this condition is true, the edit component appears in the lower half of the master-detail page.

---

__listReturnAction__

public WOComponent listReturnAction()

This action method is invoked when the user clicks Return in the master-detail page. You can specify the component this action displays by overriding `nextPage`. You can also specify custom behavior for this action by overriding `nextPageDelegate`; in this case, `nextPage` is ignored.

__See Also:__[nextPageDelegate](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq) ([D2WPage](D2WPage.md))
[nextPage](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozjpk5hug33nobxw4zlooqxsqki) ([D2WPage](D2WPage.md))

---

__masterDetailPageDelegate__

public NextPageDelegate masterDetailPageDelegate()

Returns the next page delegate for the edit component on the master-detail page. Direct to Web invokes the `nextPage method on this object when the user clicks Cancel in the edit component.

See Also:
[NextPageDelegate](NextPageDelegate.md)

---

replacementAssociationForAssociation

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

selectPageDelegate

public NextPageDelegate selectPageDelegate()

Returns the next page delegate (an object implementing the NextPageDelegate interface) for the select component on the master-detail page. Direct to Web invokes the nextPage method on this object when the user selects the record to edit.

See Also:
[NextPageDelegate](NextPageDelegate.md)

---

setEditPageDelegate

public void setEditPageDelegate(Object anObject)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

setSelectPageDelegate

public void setSelectPageDelegate(Object anObject)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)`
