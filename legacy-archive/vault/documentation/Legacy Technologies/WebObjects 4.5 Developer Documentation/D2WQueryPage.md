---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WQueryPage.html
archived_at: '2026-07-15T08:11:30.449038Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WQueryPage__

__Package__:
com.apple.yellow.directtoweb

__Inherits from__:[D2WPage](D2WPage.md)__Implements__:

- [QueryPageInterface](QueryPageInterface.md)
- com.apple.yellow.webobjects.generation.DTWGeneration

__Subclasses__:

- [WOLQueryPage](WOLQueryPage.md)
- [NEUQueryPage](NEUQueryPage.md)
- [BASQueryPage](BASQueryPage.md)

---

__Class Description__

---

This class provides the behavior for the query-page Direct to Web templates, specifically BASQueryPage, NEUQueryPage, and WOLQueryPage. The classes for these components inherit directly from D2WQueryPage and define no additional variables or methods.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the Direct to Web template's bindings (`.wod`) file. If you create a Direct to Web template from a query page, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WQueryPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5cdev2rovsxe6kqmftwkl2egjlvc5lfoj4vaylhmuxsqki)

---

Fields

- [displayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfoulvmvzhsudbm5ss6zdjonygyylzi5zg65lq)

---

Actions

- [queryAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5yxkzlspfawg5djn5xc6v2pinxw24dpnzsw45bpfauq)

Managing the Fetch Specification

- [fetchLimit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5tgk5ddnbggs3ljoqxws3tuf4ucs)
- [fetchSpecOptions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5tgk5ddnbjxazldj5yhi2lpnzzs6u3uojuw4zzpfauq)
- [isDeep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5uxgrdfmvyc6ytpn5wgkylof4ucs)
- [refreshRefetchedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5zgkztsmvzwqutfmzsxiy3imvse6ytkmvrxi4zpmjxw63dfmfxc6kbj)
- [usesDistinct](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff52xgzltiruxg5djnzrxil3cn5xwyzlbnyxsqki)

Private Methods

- [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5yxkylmnftgszlsf5cu6ulvmfwgsztjmvzc6kbj)
- [queryDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5yxkzlspfcgc5dbknxxk4tdmuxukt2emf2gcu3povzggzjpfauq)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5zgk4dmmfrwk3lfnz2ec43tn5rwsylunfxw4rtpojaxg43pmnuwc5djn5xc6v2pifzxg33dnfqxi2lpnyxsqv2pifzxg33dnfqxi2lpnywfg5dsnfxgolcekrlvizlnobwgc5dffrlu6q3pnz2gk6dufe)
- [setQueryDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5zwk5crovsxe6kemf2gcu3povzggzjpozxwszbpfbcu6rdborqvg33vojrwkki)

---

__Constructors__

---

__com.apple.yellow.directtoweb.D2WQueryPage__

public D2WQueryPage()

Standard Java no-argument constructor.

---

__Fields__

---

__displayGroup__
com.apple.yellow.webobjects.WODisplayGroup

The WODisplayGroup object that performs the query.

---

__Methods__

__fetchLimit__

public int fetchLimit()

The maximum number of objects matching the query that the receiver's display group fetches. The fetch limit is used by the receiver's fetch specification.

---

__fetchSpecOptions__

public String fetchSpecOptions()

Returns a String containing the state of the receiver's fetch specification options. These options are: `isDeep`, `usesDistinct`, `refreshesRefetchedObjects`, and `fetchLimit`.

__See Also:__[isDeep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5uxgrdfmvyc6ytpn5wgkylof4ucs)
[usesDistinct](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff52xgzltiruxg5djnzrxil3cn5xwyzlbnyxsqki)
[refreshRefetchedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5zgkztsmvzwqutfmzsxiy3imvse6ytkmvrxi4zpmjxw63dfmfxc6kbj)
[fetchLimit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5ixkzlspfigcz3ff5tgk5ddnbggs3ljoqxws3tuf4ucs)

---

__isDeep__

public boolean isDeep()

A flag indicating whether or not fetches should include sub-entities of the query fetch specification's entity. Defaults to `false`. This flag is used by the receiver's fetch specification.

---

__qualifier__

public EOQualifier qualifier()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__queryAction__

public WOComponent queryAction()

This action method is invoked when the user clicks Search in the query page. To specify the search behavior, override the `nextPageDelegate` method.

__See Also:__[nextPageDelegate](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq) ([D2WPage](D2WPage.md))

---

__queryDataSource__

public EODataSource queryDataSource()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__refreshRefetchedObjects__

public boolean refreshRefetchedObjects()

A flag indicating whether or not existing objects are overwritten with fetched values when they've been updated or changed. Defaults to `false`, that is, existing objects aren't touched when their data is refetched (the fetched data is simply discarded). This flag is used by the receiver's fetch specification.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setQueryDataSource__

public void setQueryDataSource(EODataSource dataSource)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__usesDistinct__

public boolean usesDistinct()

A flag indicating whether or not duplicate objects or records are removed after fetching. Defaults to `false`. This flag is used by the receiver's fetch specification.

---
