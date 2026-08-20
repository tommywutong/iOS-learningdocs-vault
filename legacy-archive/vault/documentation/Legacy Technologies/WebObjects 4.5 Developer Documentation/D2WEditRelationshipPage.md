---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WEditRelationshipPage.html
archived_at: '2026-07-15T08:11:30.034919Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WEditRelationshipPage__

__Package__:

__Inherits from__:[D2WPage](D2WPage.md)__Implements__:

- [EditRelationshipPageInterface](EditRelationshipPageInterface.md)
- com.apple.yellow.webobjects.generation.DTWGeneration

__Subclasses__:

- [BASEditRelationshipPage](BASEditRelationshipPage.md)
- [NEUEditRelationshipPage](NEUEditRelationshipPage.md)
- [WOLEditRelationshipPage](WOLEditRelationshipPage.md)

---

__Class Description__

---

This class provides the behavior for the edit-relationship page Direct to Web templates, specifically BASEditRelationshipPage, NEUEditRelationshipPage, and WOLEditRelationshipPage. The classes for these components inherit directly from D2WEditRelationshipPage and define no additional methods or variables.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the Direct to Web template's bindings (`.wod`) file. If you create a Direct to Web template from an edit-relationship page, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WEditRelationshipPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxuimsxivsgs5csmvwgc5djn5xhg2djobigcz3ff5cdev2fmruxiutfnrqxi2lpnzzwq2lqkbqwozjpfauq)

---

Static Constants

- [LIST](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzforlenf2fezlmmf2gs33oonugs4cqmftwkl2mjfjvi)
- [NEW](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzforlenf2fezlmmf2gs33oonugs4cqmftwkl2oivlq)
- [QUERY](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzforlenf2fezlmmf2gs33oonugs4cqmftwkl2rkvcvewi)

---

Fields

- [browserItem](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzforlenf2fezlmmf2gs33oonugs4cqmftwkl3cojxxo43fojexizln)
- [browserSelections](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzforlenf2fezlmmf2gs33oonugs4cqmftwkl3cojxxo43fojjwk3dfmn2gs33oom)
- [isRelationshipToMany](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzforlenf2fezlmmf2gs33oonugs4cqmftwkl3jonjgk3dboruw63ttnbuxavdpjvqw46i)
- [relationshipDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzforlenf2fezlmmf2gs33oonugs4cqmftwkl3smvwgc5djn5xhg2djobcgs43qnrqxsr3sn52xa)
- [selectDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzforlenf2fezlmmf2gs33oonugs4cqmftwkl3tmvwgky3uirqxiyktn52xey3f)

---

Actions

- [displayQueryAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxwi2ltobwgc6krovsxe6kbmn2gs33of5lu6q3pnvyg63tfnz2c6kbj)
- [newObjectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxw4zlxj5rguzldorawg5djn5xc6v2pinxw24dpnzsw45bpfauq)
- [queryAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxc5lfoj4ucy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)
- [removeFromToManyRelationshipAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxezlnn53gkrtsn5wvi32nmfxhsutfnrqxi2lpnzzwq2lqifrxi2lpnyxvot2dn5wxa33omvxhilzife)
- [removeFromToOneRelationshipAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxezlnn53gkrtsn5wvi32pnzsvezlmmf2gs33oonugs4cbmn2gs33of5lu6q3pnvyg63tfnz2c6kbj)
- [returnAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxezluovzg4qldoruw63rpk5hug33nobxw4zlooqxsqki)
- [saveAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxgylwmvawg5djn5xc6v2pinxw24dpnzsw45bpfauq)
- [selectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxgzlmmvrxiqldoruw63rpk5hug33nobxw4zlooqxsqki)

Key-Value Coding

- [browserStringForItem](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxwe4tpo5zwk4storzgs3thizxxeslumvws6u3uojuw4zzpfauq)
- [displayList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxwi2ltobwgc6kmnfzxil3cn5xwyzlbnyxsqki)
- [displayNameForRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxwi2ltobwgc6komfwwkrtpojjgk3dboruw63ttnbuxas3fpexvg5dsnfxgolzife)
- [displayNew](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxwi2ltobwgc6komv3s6ytpn5wgkylof4ucs)
- [displayQuery](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxwi2ltobwgc6krovsxe6jpmjxw63dfmfxc6kbj)
- [newObjectInRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxw4zlxj5rguzldorew4utfnrqxi2lpnzzwq2lqf5cu6rloorsxe4dsnfzwkt3cnjswg5bpfauq)
- [objectToAddToRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxw6ytkmvrxivdpifsgivdpkjswyylunfxw443infyc6rkpivxhizlsobzgs43fj5rguzldoqxsqki)
- [setObjectToAddToRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxgzluj5rguzldorkg6qlemrkg6utfnrqxi2lpnzzwq2lqf53g62lef4uekt2fnz2gk4tqojuxgzkpmjvgky3ufe)
- [toOneDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxi32pnzsuizltmnzgs4dunfxw4l2torzgs3thf4ucs)

Private Methods

- [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxwc53bnnss65tpnfsc6kbj)
- [displayKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxwi2ltobwgc6klmv4s6u3uojuw4zzpfauq)
- [editingContextShouldValidateChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxwkzdjoruw4z2dn5xhizlyorjwq33vnrsfmylmnfsgc5dfinugc3thmvzs6ytpn5wgkylof4uekt2fmruxi2lom5bw63tumv4hiki)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxezlqnrqwgzlnmvxhiqltonxwg2lboruw63sgn5zec43tn5rwsylunfxw4l2xj5axg43pmnuwc5djn5xc6kcxj5axg43pmnuwc5djn5xcyu3uojuw4zzmirkfovdfnvygyylumuwfot2dn5xhizlyoquq)
- [setEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxgzluivsgs5djnztug33oorsxq5bpozxwszbpfbcu6rlenf2gs3thinxw45dfpb2cs)
- [setMasterObjectAndRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxgzlujvqxg5dfojhwe2tfmn2ec3tekjswyylunfxw443infyewzlzf53g62lef4uekt2fnz2gk4tqojuxgzkpmjvgky3ufrjxi4tjnztss)
- [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cwi2lukjswyylunfxw443infyfaylhmuxxg3dfmvyc65tpnfsc6kbj)

---

__Constructors__

---

__D2WEditRelationshipPage__

public D2WEditRelationshipPage()

Standard Java no-argument constructor.

---

__Static Constants__

---

__LIST__
int

This constant is intentionally undocumented.

---

__NEW__
int

This constant is intentionally undocumented.

---

__QUERY__
int

This constant is intentionally undocumented.

---

__Fields__

---

__browserItem__
com.apple.yellow.eocontrol.EOEnterpriseObject

The iteration variable bound to the `item` attribute of the WOBrowser on the edit-relationship page.

---

__browserSelections__
com.apple.yellow.foundation.NSArray

Contains the selections the user chooses with the WOBrowser on the edit-relationship page.

---

__isRelationshipToMany__
boolean

Contains `true` if the relationship is a to-many relationship or `false` if the relationship is a to-one relationship.

---

__relationshipDisplayGroup__
com.apple.yellow.webobjects.WODisplayGroup

Contains the display group (a WODisplayGroup) with the relationship's destination objects.

---

__selectDataSource__
com.apple.yellow.eocontrol.EODataSource

Contains the data source (an EODataSource) that holds the possible destination objects for the relationship.

---

__Methods__

__awake__

public void awake()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__browserStringForItem__

public String browserStringForItem()

Returns a String containing a user-presentable name corresponding to receiver's `browserItem` variable. This string appears in the edit-relationship page's WOBrowser.

---

__displayKey__

public String displayKey()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__displayList__

public boolean displayList()

Returns whether or not the select component appears in the lower half of the edit-relationship page. Recall that the select component is actually a list component.

---

__displayNameForRelationshipKey__

public String displayNameForRelationshipKey()

Returns a String containing a user-presentable name for the relationship edited by the receiver. The method derives the result by capitalizing the first character of the relationship's key.

---

__displayNew__

public boolean displayNew()

Returns whether or not the edit component appears in the lower half of the edit-relationship page. The edit component allows the user to enter properties for a new destination object for the relationship.

---

__displayQuery__

public boolean displayQuery()

Returns whether or not the query component appears in the lower half of the edit-relationship page. The query component allows the user to query for destination objects to add to the relationship.

---

__displayQueryAction__

public WOComponent displayQueryAction()

This action method is invoked when the user clicks Search. It returns an edit-relationship page (a WOComponent) with an embedded query component.

---

__editingContextShouldValidateChanges__

public boolean editingContextShouldValidateChanges(EOEditingContext editingContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__newObjectAction__

public WOComponent newObjectAction()

This action method is invoked when the user clicks New in the edit-relationship page. It returns an edit-relationship page (a WOComponent) with an embedded edit component.

---

__newObjectInRelationship__

public EOEnterpriseObject newObjectInRelationship()

Returns the EOEnterpriseObject (defined in the EOControl Framework) that is created when the user clicks New. The edit component of the edit-relationship page edits this object.

---

__objectToAddToRelationship__

public EOEnterpriseObject objectToAddToRelationship()

Returns the EOEnterpriseObject (defined in the EOControl Framework) that is added to the relationship edited by the receiver. This is also the object the user selects in the select component.

---

__queryAction__

public WOComponent queryAction()

This action method is invoked when the user clicks the Search button in the query component of the edit-relationship page. It returns an edit-relationship page (a WOComponent) with a select component.

---

__removeFromToManyRelationshipAction__

public WOComponent removeFromToManyRelationshipAction()

This action method is invoked when the user clicks Remove in an edit-relationship page for a to-many relationship.

---

__removeFromToOneRelationshipAction__

public WOComponent removeFromToOneRelationshipAction()

This action method is invoked when the user clicks Remove in an edit-relationship page for a to-one relationship.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__returnAction__

public WOComponent returnAction()

This action method is invoked when the user clicks Return. It saves the edited relationship to the database. You can specify the component this action displays by overriding `nextPage`. You can also specify custom behavior for this action by overriding `nextPageDelegate`; in this case, `nextPage` is ignored.

__See Also:__[nextPage](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozjpk5hug33nobxw4zlooqxsqki) ([D2WPage](D2WPage.md))
[nextPageDelegate](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq) ([D2WPage](D2WPage.md))

---

__saveAction__

public WOComponent saveAction()

This action method is invoked with the user clicks Save in the edit component of the edit-relationship page. The edit component appears in the page when the user creates a new destination object for the relationship.

---

__selectAction__

public WOComponent selectAction()

This action method is invoked when the user clicks the Select button next to an object in the select component. The select component appears in the edit-relationship page after the user performs a query.

---

__setEditingContext__

protected void setEditingContext(EOEditingContext anEditingContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setMasterObjectAndRelationshipKey__

public void setMasterObjectAndRelationshipKey(EOEnterpriseObject object, String key)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setObjectToAddToRelationship__

public void setObjectToAddToRelationship(EOEnterpriseObject objectToAdd)

Sets the object the object that is added to the relationship. This is also the object that the user selects in the edit-relationship page's select component.

---

__sleep__

public void sleep()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__toOneDescription__

public String toOneDescription()

Returns a String representing the destination object of the relationship edited by the receiver if the relationship is a to-one relationship. Otherwise returns `null`.

---
