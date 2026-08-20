---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WInspectPage.html
archived_at: '2026-07-15T08:12:44.090449Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WInspectPage__

__Package__:
com.webobjects.directtoweb

__Inherits from__:[D2WPage](D2WPage.md)__Implements__:

- [InspectPageInterface](InspectPageInterface.md)
- com.webobjects.directtoweb.generation.DTWGeneration
- [EditPageInterface](EditPageInterface.md)

__Subclasses__:

- [D2WTabInspectPage](D2WTabInspectPage.md)
- [NEUInspectPage](NEUInspectPage.md)
- [BASInspectPage](BASInspectPage.md)
- [WOLInspectPage](WOLInspectPage.md)

---

__Class Description__

---

This class provides the behavior for the inspect page and edit page Direct to Web templates, specifically BASInspectPage, NEUInspectPage, and WOLInspectPage. The classes for these components inherit directly from D2WInspectPage and define no additional methods or variables.

D2WTabInspectPage also inherits from this class.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the Direct to Web template's bindings (`.wod`) file. If you create a Direct to Web template from an inspect page or an edit page, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WInspectPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss6rbsk5ew443qmvrxiudbm5ss6rbsk5ew443qmvrxiudbm5ss6kbj)

---

Fields

- [errorMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfosloonygky3ukbqwozjpmvzhe33sjvsxg43bm5sq)

---

Actions

- [cancelAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss6y3bnzrwk3cbmn2gs33of5lu6q3pnvyg63tfnz2c6kbj)
- [deleteAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss6zdfnrsxizkbmn2gs33of5lu6q3pnvyg63tfnz2c6kbj)
- [editAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss6zlenf2ecy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)
- [nextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss63tfpb2faylhmuxvot2dn5wxa33omvxhilzife)
- [submitAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss643vmjwws5cbmn2gs33of5lu6q3pnvyg63tfnz2c6kbj)

Key-Value Coding

- [object](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss633cnjswg5bpivhuk3tumvzha4tjonsu6ytkmvrxilzife)
- [setObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss643forhwe2tfmn2c65tpnfsc6kcfj5cw45dfojyhe2ltmvhwe2tfmn2cs)

Private Methods

- [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss6ylxmfvwkl3wn5uwilzife)
- [implementedInterface](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss62lnobwgk3lfnz2gkzcjnz2gk4tgmfrwkl2torzgs3thf4ucs)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss64tfobwgcy3fnvsw45cbonzw6y3jmf2gs33oizxxeqltonxwg2lboruw63rpk5huc43tn5rwsylunfxw4lzik5huc43tn5rwsylunfxw4lctorzgs3thfrcfiv2umvwxa3dborssyv2pinxw45dfpb2cs)
- [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss643forcwi2lunfxgoq3pnz2gk6duf53g62lef4uekt2fmruxi2lom5bw63tumv4hiki)
- [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss643mmvsxal3wn5uwilzife)
- [validationFailedWithException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ew443qmvrxiudbm5ss65tbnruwiylunfxw4rtbnfwgkzcxnf2gqrlymnsxa5djn5xc65tpnfsc6kcunbzg653bmjwgklcpmjvgky3ufrjxi4tjnztss)

---

__Constructors__

---

__D2WInspectPage__

public D2WInspectPage()

Standard Java no-argument constructor.

---

__Fields__

---

__errorMessage__
java.lang.String

Contains an error message displayed on the inspect page.

---

__Methods__

__awake__

public void awake()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__cancelAction__

public WOComponent cancelAction()

This action method is invoked when the user clicks Cancel. It discards the edits on the page. You can specify the component this action displays by overriding `nextPage`. You can also specify custom behavior for this action by overriding `nextPageDelegate`; in this case, `nextPage` is ignored.

__See Also:__[nextPage](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozjpk5hug33nobxw4zlooqxsqki) ([D2WPage](D2WPage.md))
[nextPageDelegate](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq) ([D2WPage](D2WPage.md))

---

__deleteAction__

public WOComponent deleteAction()

This action method is invoked when the user clicks Delete. It deletes the object that the page is inspecting or editing. You can specify the component this action displays by overriding `nextPage`. You can also specify custom behavior for this action by overriding `nextPageDelegate`; in this case, `nextPage` is ignored.

__See Also:__[nextPage](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozjpk5hug33nobxw4zlooqxsqki) ([D2WPage](D2WPage.md))
[nextPageDelegate](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq) ([D2WPage](D2WPage.md))

---

__editAction__

public WOComponent editAction()

This action method is invoked when the user clicks Edit in an inspect page. It creates an edit page for the inspected object.

---

__implementedInterface__

public String implementedInterface()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__nextPage__

public WOComponent nextPage()

This action method is invoked when the user clicks Return in an inspect page. You can specify the component this action displays by overriding this method. You can also specify custom behavior for this action by overriding `nextPageDelegate` instead.

__See Also:__[nextPageDelegate](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq) ([D2WPage](D2WPage.md))

---

__object__

public EOEnterpriseObject object()

Returns the Object displayed by the inspect or edit page.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setEditingContext__

public void setEditingContext(EOEditingContext editingContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setObject__

public void setObject(EOEnterpriseObject object)

Sets the object displayed by the inspect or edit page.

---

__sleep__

public void sleep()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__submitAction__

public WOComponent submitAction()

This action method executes when the user clicks Save on the edit page. It saves the edits to the database.

---

__validationFailedWithException__

public void validationFailedWithException(Throwable anExeception, Object anObject, String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
