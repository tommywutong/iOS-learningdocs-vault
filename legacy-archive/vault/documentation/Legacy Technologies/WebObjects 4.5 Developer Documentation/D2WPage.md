---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WPage.html
archived_at: '2026-07-15T08:11:30.351323Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WPage__

__Package__:
com.apple.yellow.directtoweb

__Inherits from__:[D2WComponent](D2WComponent.md)__Subclasses__:

- [D2WMasterDetailPage](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WMasterDetailPage.html)
- [D2WQueryAllEntitiesPage](D2WQueryAllEntitiesPage.md)
- [D2WInspectPage](D2WInspectPage.md)
- [D2WListPage](D2WListPage.md)
- [D2WErrorPage](D2WErrorPage.md)
- [D2WQueryPage](D2WQueryPage.md)
- [D2WConfirmPage](D2WConfirmPage.md)
- [D2WEditRelationshipPage](D2WEditRelationshipPage.md)

---

__Class Description__

---

This class is the parent class for the Direct to Web templates. It provides support for the next page mechanism, which determines the behavior when the user leaves the page. It also provides other methods used by most or all of the Direct to Web templates, such as a data source, the page wrapper name, and a flag to indicate whether to show the cancel button or not.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the bindings (`.wod`) file of the Direct to Web templates. If you create your own Direct to Web template, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5cdev2qmftwkl2egjlvaylhmuxsqki)

---

Key-Value Coding

- [dataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5sgc5dbknxxk4tdmuxukt2emf2gcu3povzggzjpfauq)
- [pageWrapperName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5ygcz3fk5zgc4dqmvze4ylnmuxvg5dsnfxgolzife)
- [setDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5zwk5cemf2gcu3povzggzjpozxwszbpfbcu6rdborqvg33vojrwkki)
- [showCancel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5zwq33xinqw4y3fnqxwe33pnrswc3rpfauq)

Managing the Next Page Parameters

- [nextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozjpk5hug33nobxw4zlooqxsqki)
- [nextPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq)
- [setNextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5zwk5comv4hiudbm5ss65tpnfsc6kcxj5bw63lqn5xgk3tufe)
- [setNextPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5zwk5comv4hiudbm5suizlmmvtwc5dff53g62lef4ue4zlyorigcz3firswyzlhmf2gkki)

Private Methods

- [alternateRowColor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5qwy5dfojxgc5dfkjxxoq3pnrxxel3cn5xwyzlbnyxsqki)
- [descriptionForResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5sgk43dojuxa5djn5xem33skjsxg4dpnzzwkl2torzgs3thf4ufot2smvzxa33oonssyv2pinxw45dfpb2cs)
- [extraBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5sxq5dsmfbgs3tenfxgo4zpjzjui2ldoruw63tboj4s6kbj)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5zgk4dmmfrwk3lfnz2ec43tn5rwsylunfxw4rtpojaxg43pmnuwc5djn5xc6v2pifzxg33dnfqxi2lpnyxsqv2pifzxg33dnfqxi2lpnywfg5dsnfxgolcekrlvizlnobwgc5dffrlu6q3pnz2gk6dufe)
- [setExtraBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5zwk5cfpb2heykcnfxgi2lom5zs65tpnfsc6kcokngxk5dbmjwgkrdjmn2gs33omfzhski)

---

__Constructors__

---

__com.apple.yellow.directtoweb.D2WPage__

public D2WPage()

Standard Java no-argument constructor.

---

__Methods__

__alternateRowColor__

public boolean alternateRowColor()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__dataSource__

public EODataSource dataSource()

Returns the EODataSource (defined in the EOControl Framework) containing the objects displayed on the page (or the objects that match the query for the query page subclasses.)

---

__descriptionForResponse__

public String descriptionForResponse(WOResponse response, WOContext context)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__extraBindings__

public NSDictionary extraBindings()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__nextPage__

public WOComponent nextPage()

Returns the receiver's next page (a WOComponent) or `null`, if no next page has been specified. Typically, this method is invoked when the user leaves the page; the exact conditions under which it is invoked depends on the subclass of D2WPage that uses it. See the specification for the specific subclass for more information.

You can override this method to customize the D2WPage behavior when the user leaves the page.

---

__nextPageDelegate__

public NextPageDelegate nextPageDelegate()

Returns the receiver's next page delegate (an Object) or `null`, if no next page delegate has been specified. Typically, the `nextPage` method is invoked on the next page delegate (if it has been specified) when the user leaves the page; the exact conditions under which it is invoked depends on the subclass of D2WPage that uses it. See the specification for the specific subclass for more information.

If you do not specify a next page delegate, Direct to Web displays the WOComponent returned by the `nextPage` method.

You can override the `nextPageDelegate` method or use the `setNextPageDelegate` method to customize the D2WPage behavior when the user leaves the page.

__See Also:__[nextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozjpk5hug33nobxw4zlooqxsqki)
[setNextPageDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5zwk5comv4hiudbm5suizlmmvtwc5dff53g62lef4ue4zlyorigcz3firswyzlhmf2gkki)

---

__pageWrapperName__

public String pageWrapperName()

Returns the name of the page wrapper component that the receiver appears within. This key is resolved using the rule system.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setDataSource__

public void setDataSource(EODataSource dataSource)

Sets the EODataSource (defined in the EOControl Framework) containing the objects displayed on the page to `dataSource`.

---

__setExtraBindings__

public void setExtraBindings(NSMutableDictionary dictionary)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setNextPage__

public void setNextPage(WOComponent nextPage)

Sets the page that displayed when the user clicks Return in the page.

---

__setNextPageDelegate__

public void setNextPageDelegate(NextPageDelegate delegate)

Sets the receiver's next page delegate to `delegate`. Typically, the `nextPage` method is invoked on the next page delegate (if it has been specified) when the user leaves the page; the exact conditions under which it is invoked depends on the subclass of D2WPage that uses it. See the specification for the specific subclass for more information.

---

__showCancel__

public boolean showCancel()

Returns whether the Cancel button is displayed on the receiver's page or not.

---
