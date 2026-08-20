---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2W.html
archived_at: '2026-07-15T08:11:28.498997Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2W__

__Package__:
com.apple.yellow.directtoweb

__Inherits from__:java.lang.Object

---

__Class Description__

---

The D2W class is responsible for creating Direct to Web pages. In each Direct to Web application, one instance of D2W creates all of the pages. This instance is called the Direct to Web factory and is accessed using the `factory` static method.

D2W defines several methods to create Direct to Web pages, for example, `listPageForEntityNamed`, `errorPage`, `pageForConfigurationNamed`, and `pageForTaskAndEntityNamed`. You invoke these methods on the Direct to Web factory. For example, to create a list page for Movies, use

`ListPageInterface lpi = D2W.factory().listPageForEntityNamed("Movie",session());`

If you want to customize the Direct to Web factory, you need to subclass D2W, create an instance of your subclass, and register it with Direct to Web using the `setFactory` method. See the "Customizing a Direct to Web Application" chapter in _Developing WebObjects Applications With Direct to Web_ for more information.

The D2W class also provides the `setWebAssistantEnabled` and `isWebAssistantEnabled` methods to manage the Web Assistant.
You can also change the keys with which Direct to Web caches rule firing results using `newSignificantKey`. See the "Direct to Web Architecture" chapter of _Developing WebObjects Applications With Direct to Web_ for more information about rule firing caching.

__Method Types__

---

Constructors

- [public D2W()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xuimsxf5cdevzpfauq)

---

Creating pages

- [confirmPageForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwg33omzuxe3kqmftwkrtpojcw45djor4u4ylnmvsc6q3pnztgs4tnkbqwozkjnz2gk4tgmfrwklzikn2he2lom4wfot2tmvzxg2lpnyuq)
- [defaultPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwizlgmf2wy5cqmftwkl2xj5bw63lqn5xgk3tuf4ufot2tmvzxg2lpnyuq)
- [editPageForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwkzdjorigcz3fizxxerlooruxi6komfwwkzbpivsgs5cqmftwksloorsxeztbmnss6kctorzgs3thfrlu6u3fonzws33ofe)
- [editPageForNewObjectWithConfigurationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwkzdjorigcz3fizxxettfo5hwe2tfmn2fo2lunbbw63tgnftxk4tboruw63somfwwkzbpivsgs5cqmftwksloorsxeztbmnss6kctorzgs3thfrlu6u3fonzws33ofe)
- [editPageForNewObjectWithEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwkzdjorigcz3fizxxettfo5hwe2tfmn2fo2lunbcw45djor4u4ylnmvsc6rlenf2faylhmvew45dfojtgcy3ff4ufg5dsnfxgolcxj5jwk43tnfxw4ki)
- [editRelationshipPageForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwkzdjorjgk3dboruw63ttnbuxaudbm5sum33sivxhi2lupfhgc3lfmqxukzdjorjgk3dboruw63ttnbuxaudbm5sus3tumvzgmyldmuxsqu3uojuw4zzmk5hvgzltonuw63rj)
- [errorPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwk4tsn5zfaylhmuxuk4tsn5zfaylhmvew45dfojtgcy3ff4ufot2dn5xhizlyoquq)
- [errorPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwk4tsn5zfaylhmuxuk4tsn5zfaylhmvew45dfojtgcy3ff4ufot2tmvzxg2lpnyuq)
- [inspectPageForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xws3ttobswg5cqmftwkrtpojcw45djor4u4ylnmvsc6sloonygky3ukbqwozkjnz2gk4tgmfrwklzikn2he2lom4wfot2tmvzxg2lpnyuq)
- [listPageForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwy2ltorigcz3fizxxerlooruxi6komfwwkzbpjruxg5cqmftwksloorsxeztbmnss6kctorzgs3thfrlu6u3fonzws33ofe)
- [pageForConfigurationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxaylhmvdg64sdn5xgm2lhovzgc5djn5xe4ylnmvsc6v2pinxw24dpnzsw45bpfbjxi4tjnztsyv2pknsxg43jn5xcs)
- [pageForTaskAndEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxaylhmvdg64sumfzwwqlomrcw45djor4u4ylnmvsc6v2pinxw24dpnzsw45bpfbjxi4tjnztsyu3uojuw4zzmk5hvgzltonuw63rj)
- [pageForTaskAndEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxaylhmvdg64sumfzwwqlomrcw45djor4u4ylnmvsc6v2pinxw24dpnzsw45bpfbjxi4tjnztsyu3uojuw4zzmk5hug33oorsxq5bj)
- [queryAllPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxc5lfoj4uc3dmkbqwozjpkf2wk4tzifwgyudbm5sus3tumvzgmyldmuxsqv2pknsxg43jn5xcs)
- [queryPageForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxc5lfoj4vaylhmvdg64sfnz2gs5dzjzqw2zlef5ixkzlspfigcz3fjfxhizlsmzqwgzjpfbjxi4tjnztsyv2pknsxg43jn5xcs)
- [selectPageForEntityNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxgzlmmvrxiudbm5sum33sivxhi2lupfhgc3lfmqxvgzlmmvrxiudbm5sus3tumvzgmyldmuxsqu3uojuw4zzmk5hvgzltonuw63rj)

Managing Rule Firing Caching

- [newSignificantKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xw4zlxknuwo3tjmzuwgyloorfwk6jpozxwszbpfbjxi4tjnztss)

Managing the Direct to Web factory

- [factory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdevzpmzqwg5dpoj4s6rbsk4xsqki)
- [setFactory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdevzponsxirtbmn2g64tzf53g62lef4ueimsxfe)

Managing the Web Assistant

- [isWebAssistantEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xws42xmvrec43tnfzxiyloorcw4ylcnrswil3cn5xwyzlbnyxsqki)
- [setWebAssistantEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxgzluk5sweqltonuxg5dbnz2ek3tbmjwgkzbpozxwszbpfbrg633mmvqw4ki)
- [webAssistantInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxozlcifzxg2ltorqw45cjnzbw63tumv4hil2xj5bw63lqn5xgk3tuf4ufot2dn5xhizlyoquq)

Obtaining Page Information

- [entityNameFromPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdevzpmvxhi2lupfhgc3lfizzg63kqmftwkl2torzgs3thf4ufot2dn5wxa33omvxhiki)
- [homeHrefInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwq33nmvehezlgjfxeg33oorsxq5bpkn2he2lom4xsqv2pinxw45dfpb2cs)
- [visibleEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxm2ltnfrgyzkfnz2gs5dzjzqw2zltf5hfgqlsojqxslzik5hvgzltonuw63rj)

Private Methods

- [activateWebAssistantServer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwcy3unf3gc5dfk5sweqltonuxg5dbnz2fgzlsozsxel3wn5uwilzife)
- [checkMultithreading](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwg2dfmnvu25lmoruxi2dsmvqwi2lom4xxm33jmqxsqtstjzxxi2lgnfrwc5djn5xcs)
- [init](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xws3tjoqxxm33jmqxsqki)
- [initializeD2W](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xws3tjoruwc3djpjsuimsxf53g62lef4ue4u2on52gsztjmnqxi2lpnyuq)
- [isDebugEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xws42emvrhkz2fnzqwe3dfmqxwe33pnrswc3rpfauq)
- [packetForPropertyAndSettingsWithPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxayldnnsxirtpojihe33qmvzhi6kbnzsfgzluoruw4z3tk5uxi2cqmftwkl2bonzws43umfxhiudbmnvwk5bpfbihe33qmvzhi6jmknsxi5djnztxglcxj5bw63lqn5xgk3tufe)
- [packetForSettingsWithPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxayldnnsxirtpojjwk5dunfxgo42xnf2gqudbm5ss6qltonuxg5dbnz2fayldnnsxilziknsxi5djnztxglcxj5bw63lqn5xgk3tufe)
- [requestWasHandled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxezlrovsxg5cxmfzuqylomrwgkzbpozxwszbpfblu6q3pnz2gk6dufe)
- [willCheckRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxo2lmnrbwqzldnnjhk3dfomxxm33jmqxsqtstjzxxi2lgnfrwc5djn5xcs)

---

__Constructors__

---

__com.apple.yellow.directtoweb.D2W__

public D2W()

Standard Java no argument constructor. If you subclass D2W, use the constructor to create an instance of your subclass and use `D2W.setFactory` to register it with Direct to Web.

---

__Methods__

__activateWebAssistantServer__

public void activateWebAssistantServer()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__checkMultithreading__

public void checkMultithreading(NSNotification notification)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__confirmPageForEntityNamed__

public ConfirmPageInterface confirmPageForEntityNamed(String entityName, WOSession session)

Returns a confirm page (a WOComponent object implementing the ConfirmPageInterface) for the entity identified by `entityName`. The `session` argument specifies the session in which the page should be created.

---

__defaultPage__

public WOComponent defaultPage(WOSession session)

Returns a default startup page (a WOComponent object), which is a query-all page unless you override the rule for the `startupTask` key. The `session` argument specifies the session in which the page should be created.

---

__editPageForEntityNamed__

public EditPageInterface editPageForEntityNamed(String entityName, WOSession session)

Returns an edit page (a WOComponent object implementing the EditPageInterface) for the entity identified by `entityName`. The `session` argument specifies the session in which the page should be created.

---

__editPageForNewObjectWithConfigurationNamed__

public EditPageInterface editPageForNewObjectWithConfigurationNamed(String configurationName, WOSession session)

Creates a new object and returns an edit page (a WOComponent object implementing the EditPageInterface. The object's class and the configuration of the page are determined from the named configuration identified by `configurationName`. The `session` argument specifies the session in which the page should be created.

---

__editPageForNewObjectWithEntityNamed__

public EditPageInterface editPageForNewObjectWithEntityNamed(String entityName, WOSession session)

Creates a new object and returns an edit page (a WOComponent object implementing the EditPageInterface. The object's class is determined from the EOEntity object identified by `entityName`. The `session` argument specifies the session in which the page should be created.

The EOEntity class is defined in the EOAccess Framework.

---

__editRelationshipPageForEntityNamed__

public EditRelationshipPageInterface editRelationshipPageForEntityNamed(String entityName, WOSession session)

Returns an edit-relationship page (a WOComponent object implementing the EditRelationshipPageInterface) for the entity identified by `entityName`. The `session` argument specifies the session in which the page should be created.

---

__entityNameFromPage__

public static String entityNameFromPage(WOComponent page)

Returns the name of the entity that the Direct to Web page `page` manipulates.

---

__errorPage__

public ErrorPageInterface errorPage(WOContext context)

Returns an error page (a WOComponent object implementing the ErrorPageInterface). The `context` argument specifies the WOContext containing the session in which the page should be created.

---

__errorPage__

public ErrorPageInterface errorPage(WOSession session)

Returns an error page (a WOComponent object implementing the ErrorPageInterface). The `session` argument specifies the session in which the page should be created.

---

__factory__

static public D2W factory()

Returns the Direct to Web factory, an instance of D2W that creates all of the Direct to Web pages in the application.

---

__homeHrefInContext__

public String homeHrefInContext(WOContext context)

Returns the URL for the login page for the session contained in the `context` WOContext object.

---

__init__

protected void init()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__initializeD2W__

public void initializeD2W(NSNotification notification)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__inspectPageForEntityNamed__

public InspectPageInterface inspectPageForEntityNamed(String entityName, WOSession session)

Returns an inspect page (a WOComponent object implementing the InspectPageInterface) for the entity identified by `entityName`. The `session` argument specifies the session in which the page should be created.

---

__isDebugEnabled__

public boolean isDebugEnabled()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isLiveAssistantEnabled__

public boolean isLiveAssistantEnabled()

Use `isWebAssistantEnabled` instead.

__See Also:__[isWebAssistantEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xws42xmvrec43tnfzxiyloorcw4ylcnrswil3cn5xwyzlbnyxsqki)

---

__isWebAssistantEnabled__

public boolean isWebAssistantEnabled()

Returns whether or not the Web Assistant is enabled. By default it is enabled.

---

__listPageForEntityNamed__

public ListPageInterface listPageForEntityNamed(String entityName, WOSession session)

Returns a list page (a WOComponent object implementing the ListPageInterface) for the entity identified by `entityName`. The `session` argument specifies the session in which the page should be created.

---

__newSignificantKey__

public void newSignificantKey(String key)

Adds `key` to the list of keys that the rule engine uses to cache the results of rule firing. See the "Direct to Web Architecture" chapter of _Developing WebObjects Applications With Direct to Web_ for more information about rule firing caching.

---

__packetForPropertyAndSettingsWithPage__

protected AssistantPacket packetForPropertyAndSettingsWithPage(Property aProperty, Settings settings, WOComponent aComponent)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__packetForSettingsWithPage__

protected AssistantPacket packetForSettingsWithPage(Settings settings, WOComponent aComponent)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__pageForConfigurationNamed__

public WOComponent pageForConfigurationNamed(String configurationName, WOSession session)

Returns a Direct to Web page (a WOComponent object) for a named configuration identified by `configurationName`. The `session` argument specifies the session in which the page should be created. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about named configurations.

---

__pageForTaskAndEntityNamed__

public WOComponent pageForTaskAndEntityNamed(String task, String entityName, WOSession session)

Returns a Direct to Web page (a WOComponent object) for the task identified by `task` and the entity identified by `entityName`. The `session` argument specifies the the session in which the page should be created.

---

__pageForTaskAndEntityNamed__

protected WOComponent pageForTaskAndEntityNamed(String task, String entityName, WOContext context)

Returns a Direct to Web page (a WOComponent object) for the task identified by `task` and the entity identified by `entityName`. The `context` argument specifies the context containing the session in which the page should be created.

---

__queryAllPage__

public QueryAllPageInterface queryAllPage(WOSession session)

Returns a query-all page (a WOComponent object implementing the QueryAllPageInterface). The `session` argument specifies the session in which the page should be created.

---

__queryPageForEntityNamed__

public QueryPageInterface queryPageForEntityNamed(String entityName, WOSession session)

Returns a query page (a WOComponent object implementing the QueryPageInterface) for the entity identified by `entityName`. The `session` argument specifies the session in which the page should be created.

---

__requestWasHandled__

public void requestWasHandled(WOContext context)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__selectPageForEntityNamed__

public SelectPageInterface selectPageForEntityNamed(String entityName, WOSession session)

Returns a select page (a WOComponent object implementing the SelectPageInterface) for the entity identified by `entityName`. The `session` argument specifies the session in which the page should be created.

---

__setFactory__

static public void setFactory(D2W factory)

Sets the Direct to Web factory, an instance of D2W that is used to create all of the application's Direct to Web pages. Use this method when you create a custom subclass of D2W.

---

__setLiveAssistantEnabled__

public void setLiveAssistantEnabled(boolean enabled)

Use `setWebAssistantEnabled` instead.

__See Also:__[setWebAssistantEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xxgzluk5sweqltonuxg5dbnz2ek3tbmjwgkzbpozxwszbpfbrg633mmvqw4ki)

---

__setWebAssistantEnabled__

public void setWebAssistantEnabled(boolean enabled)

Sets whether the Web Assistant is enabled or not. You should disable the Web Assistant when you deploy your application to prevent users from modifying the application's configuration.

---

__visibleEntityNames__

public NSArray visibleEntityNames()

This method is deprecated. Use `visibleEntityNames(WOSession session)` instead.

---

__visibleEntityNames__

public NSArray visibleEntityNames(WOSession session)

Returns an NSArray containing the names of the visible entities in `session`. You can hide entities using the Entities tab in the Web Assistant. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about hiding entities.

---

__webAssistantInContext__

public WOComponent webAssistantInContext(WOContext context)

This action method is invoked when the user clicks Customize in the menu bar. It activates the Web Assistant in the user's browser.

---

__willCheckRules__

public void willCheckRules(NSNotification notification)

This method is intentionally undocumented. You should never have to invoke or customize it.

---
