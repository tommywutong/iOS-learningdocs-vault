---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WListPage.html
archived_at: '2026-07-15T08:11:30.265859Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WListPage__

__Package__:
com.apple.yellow.directtoweb

__Inherits from__:[D2WPage](D2WPage.md)__Implements__:

- [ListPageInterface](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Protocols/ListPageInterface.html)
- com.apple.yellow.webobjects.generation.DTWGeneration
- [SelectPageInterface](SelectPageInterface.md)

__Subclasses__:

- [D2WPlainListPage](D2WPlainListPage.md)
- [WOLListPage](WOLListPage.md)
- [NEUListPage](NEUListPage.md)
- [BASListPage](BASListPage.md)

---

__Class Description__

---

This class provides the behavior for the list page and select page Direct to Web templates, specifically BASListPage, NEUListPage, and WOLListPage. The classes for these components inherit directly from D2WListPage and define no additional methods or variables.

D2WPlainListPage also inherits from this class.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the Direct to Web template's bindings (`.wod`) file. If you create a Direct to Web template from a list page or a select page, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WListPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpiqzfotdjon2faylhmuxuimsxjruxg5cqmftwklzife)

---

Actions

- [backAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmjqwg22bmn2gs33of5lu6q3pnvyg63tfnz2c6kbj)
- [deleteObjectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmrswyzlumvhwe2tfmn2ecy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)
- [editObjectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmvsgs5cpmjvgky3uifrxi2lpnyxvot2dn5wxa33omvxhilzife)
- [inspectObjectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpnfxhg4dfmn2e6ytkmvrxiqldoruw63rpk5hug33nobxw4zlooqxsqki)
- [selectObjectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjponswyzldorhwe2tfmn2ecy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)

Key-Value Coding

- [displayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmruxg4dmmf4uo4tpovyc6v2piruxg4dmmf4uo4tpovyc6kbj)
- [isEntityReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpnfzuk3tunf2hsutfmfse63tmpexwe33pnrswc3rpfauq)
- [isListEmpty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpnfzuy2ltorcw24dupexwe33pnrswc3rpfauq)
- [isSelecting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpnfzvgzlmmvrxi2lom4xwe33pnrswc3rpfauq)
- [listSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpnruxg5ctnf5gkl3jnz2c6kbj)

Private Methods

- [alternatingColorForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmfwhizlsnzqxi2lom5bw63dpojdg64ssn53s6u3uojuw4zzpfauq)
- [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmfyhazlomrkg6utfonyg63ttmuxxm33jmqxsqv2pkjsxg4dpnzzwklcxj5bw63tumv4hiki)
- [backgroundColorForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmjqwg23hojxxk3teinxwy33sizxxeutpo4xvg5dsnfxgolzife)
- [backgroundColorForRowMethod](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmjqwg23hojxxk3teinxwy33sizxxeutpo5gwk5din5sc6u3uojuw4zzpfauq)
- [defaultSortKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmrswmylvnr2fg33sorfwk6jpkn2he2lom4xsqki)
- [editingContextDidSaveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmvsgs5djnztug33oorsxq5cenfsfgylwmvbwqylom5sxgl3wn5uwilzijzju433unftgsy3boruw63rj)
- [finalize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpmzuw4ylmnf5gkl3wn5uwilzife)
- [numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpnz2w2ytfojhwmt3cnjswg5dtkbsxeqtborrwql3jnz2c6kbj)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjpojsxa3dbmnsw2zlooraxg43pmnuwc5djn5xem33sifzxg33dnfqxi2lpnyxvot2bonzw6y3jmf2gs33of4ufot2bonzw6y3jmf2gs33ofrjxi4tjnztsyrcuk5kgk3lqnrqxizjmk5hug33oorsxq5bj)
- [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjponswyzldorswit3cnjswg5bpivhuk3tumvzha4tjonsu6ytkmvrxilzife)
- [setBackgroundColorForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjponsxiqtbmnvwo4tpovxgiq3pnrxxertpojjg65zpozxwszbpfbjxi4tjnztss)
- [setDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjponsxirdborqvg33vojrwkl3wn5uwilziivhuiylumfjw65lsmnsss)
- [setLocalContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjponsxitdpmnqwyq3pnz2gk6duf53g62lef4ueimsxinxw45dfpb2cs)
- [setSelectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ggs43ukbqwozjponsxiu3fnrswg5dfmrhwe2tfmn2c65tpnfsc6kcfj5cw45dfojyhe2ltmvhwe2tfmn2cs)

---

__Constructors__

---

__com.apple.yellow.directtoweb.D2WListPage__

public D2WListPage()

Standard Java no-argument constructor.

---

__Methods__

__alternatingColorForRow__

public String alternatingColorForRow()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__appendToResponse__

public void appendToResponse(WOResponse response, WOContext context)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__backAction__

public WOComponent backAction()

This action method is invoked when the user clicks Return in the list page. You can specify the component this action displays by overriding `nextPage`. You can also specify custom behavior for this action by overriding `nextPageDelegate`; in this case, `nextPage` is ignored.

__See Also:__[nextPage](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozjpk5hug33nobxw4zlooqxsqki) ([D2WPage](D2WPage.md))
[nextPageDelegate](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq) ([D2WPage](D2WPage.md))

---

__backgroundColorForRow__

public String backgroundColorForRow()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__backgroundColorForRowMethod__

public String backgroundColorForRowMethod()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__defaultSortKey__

public String defaultSortKey()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__deleteObjectAction__

public WOComponent deleteObjectAction()

This action method is invoked when the user clicks the delete button next to an object on the list page.

---

__displayGroup__

public WODisplayGroup displayGroup()

Returns the receiver's display group. This display group contains the objects listed on the page.

---

__editingContextDidSaveChanges__

public void editingContextDidSaveChanges(NSNotification notification)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__editObjectAction__

public WOComponent editObjectAction()

This action method is invoked when the user clicks the edit button next to an object on the list page. It creates and returns an inspect page (a WOComponent) for the object.

---

__finalize__

public void finalize()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__inspectObjectAction__

public WOComponent inspectObjectAction()

This action method is invoked when the user clicks the inspect button next to an object on the list page. It creates and returns an inspect page (a WOComponent) for the object.

---

__isEntityReadOnly__

public boolean isEntityReadOnly()

Returns whether the entity displayed on this list page can be modified or not.

---

__isListEmpty__

public boolean isListEmpty()

Returns whether the list displayed by this page contains no objects.

---

__isSelecting__

public boolean isSelecting()

Returns `true` if the receiver is a select page. Returns `false` if it is a list page.

---

__listSize__

public int listSize()

Returns the total number of objects in the list page's display group. This is not the number of objects shown on the page, which depends on the display group's batch size.

---

__numberOfObjectsPerBatch__

public int numberOfObjectsPerBatch()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__selectedObject__

public EOEnterpriseObject selectedObject()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__selectObjectAction__

public WOComponent selectObjectAction()

This action method is invoked when the user clicks Select next to one of the objects on the select page. You can specify custom behavior for this action by overriding `nextPageDelegate`.

__See Also:__[nextPageDelegate](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq) ([D2WPage](D2WPage.md))

---

__setBackgroundColorForRow__

public void setBackgroundColorForRow(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setDataSource__

public void setDataSource(EODataSource dataSource)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setLocalContext__

public void setLocalContext(D2WContext context)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setSelectedObject__

public void setSelectedObject(EOEnterpriseObject object)

This method is intentionally undocumented. You should never have to invoke or customize it.

---
