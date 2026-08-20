---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/DefaultHeader.html
archived_at: '2026-07-15T08:11:30.662422Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__DefaultHeader__

__Package__:
com.apple.yellow.directtoweb

__Inherits from__:com.apple.yellow.webobjects.WOComponent__Subclasses__:

- [WOLHeader](WOLHeader.md)
- [BASSideHeader](BASSideHeader.md)
- [BASDefaultHeader](BASDefaultHeader.md)

---

__Class Description__

---

This class defines the behavior of the menu header in a Direct to Web application. The source code for this class is copied into the MenuHeader.java file in the application's project.

__Method Types__

---

Constructors

- [public DefaultHeader()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixuizlgmf2wy5cimvqwizlsf5cgkztbovwhisdfmfsgk4rpfauq)

---

Fields

- [entityNameInList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpirswmylvnr2eqzlbmrsxel3fnz2gs5dzjzqw2zkjnzggs43u)

---

Actions

- [findEntityAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixwm2lomrcw45djor4ucy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)
- [homeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixwq33nmvawg5djn5xc6v2pinxw24dpnzsw45bpfauq)
- [logout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixwy33hn52xil2xj5bw63lqn5xgk3tuf4ucs)
- [newObjectAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixw4zlxj5rguzldorawg5djn5xc6v2pinxw24dpnzsw45bpfauq)
- [showWebAssistant](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixxg2dpo5lwkysbonzws43umfxhil2xj5bw63lqn5xgk3tuf4ucs)

Key-Value Coding

- [isWebAssistantEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixws42xmvrec43tnfzxiyloorcw4ylcnrswil3cn5xwyzlbnyxsqki)
- [manipulatedEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixw2ylonfyhk3dborswirlooruxi6komfwwkl2torzgs3thf4ucs)
- [setManipulatedEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixxgzlujvqw42lqovwgc5dfmrcw45djor4u4ylnmuxxm33jmqxsqu3uojuw4zzj)
- [visibleEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixxm2ltnfrgyzkfnz2gs5dzjzqw2zltf5hfgqlsojqxslzife)

---

__Constructors__

---

__com.apple.yellow.directtoweb.DefaultHeader__

public DefaultHeader()

Standard Java no-argument constructor.

---

__Fields__

---

__entityNameInList__
java.lang.String

This instance variable is used as a temporary variable by the Entities WOPopupButton.

---

__Methods__

__findEntityAction__

public WOComponent findEntityAction()

This method is invoked when the user clicks Search in the menu bar. It creates and displays a query page (a WOComponent object) for the selected entity.

---

__homeAction__

public WOComponent homeAction()

This method is invoked when the user clicks Home in the menu bar. It displays the startup task page.

---

__isWebAssistantEnabled__

public boolean isWebAssistantEnabled()

Returns whether or not the Web Assistant is enabled. By default it is enabled.

---

__logout__

public WOComponent logout()

This method is invoked when the user clicks Logout in the menu bar. It terminates the current session and returns the application's home page WOComponent (`Main`).

__See Also:__[homeHrefInContext](D2W.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk4xwq33nmvehezlgjfxeg33oorsxq5bpkn2he2lom4xsqv2pinxw45dfpb2cs) ([D2W](D2W.md))

---

__manipulatedEntityName__

public String manipulatedEntityName()

Returns the entity name the user chooses in the Entities pop-up list in the menu bar.

---

__newObjectAction__

public WOComponent newObjectAction()

This action method is invoked when the user clicks New in the menu bar. It creates an instance of the manipulated entity and displays an edit page for it.

__See Also:__[manipulatedEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rdfmzqxk3dujbswczdfoixw2ylonfyhk3dborswirlooruxi6komfwwkl2torzgs3thf4ucs)

---

__setManipulatedEntityName__

public void setManipulatedEntityName(String entityName)

Sets the entity name the use chooses from the pop-up list in the menu bar.

---

__showWebAssistant__

public WOComponent showWebAssistant()

This action method is invoked when the user clicks Customize in the menu bar. It displays the Web Assistant in the user's browser.

---

__visibleEntityNames__

public NSArray visibleEntityNames()

Returns an NSArray containing the names of the visible entities in the `session` WOSession. You can hide entities using the Entities tab in the Web Assistant. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about hiding entities.

---
