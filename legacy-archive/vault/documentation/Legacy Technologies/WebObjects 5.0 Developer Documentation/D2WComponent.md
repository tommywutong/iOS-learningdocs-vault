---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WComponent.html
archived_at: '2026-07-15T08:12:43.109344Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WComponent__

__Package__:
com.webobjects.directtoweb

__Inherits from__:com.webobjects.appserver.WOComponent__Subclasses__:

- [EditRelationship](EditRelationship.md)
- [D2WPage](D2WPage.md)
- [D2WStatelessComponent](D2WStatelessComponent.md)
- [D2WEditToManyFault](D2WEditToManyFault.md)
- [D2WCustomQueryComponent](D2WCustomQueryComponent.md)
- [D2WCompactInspectComponent](D2WCompactInspectComponent.md)
- [D2WDisplayToMany](D2WDisplayToMany.md)
- [D2WHead](D2WHead.md)
- [D2WKeyPathContainer](D2WKeyPathContainer.md)
- [D2WRemoteControl](D2WRemoteControl.md)
- [D2WCustomComponent](D2WCustomComponent.md)
- [D2WWebAssistantPage](D2WWebAssistantPage.md)
- [D2WWebAssistantFrame](D2WWebAssistantFrame.md)

---

__Class Description__

---

This class is the parent class for the Direct to Web templates and the property-level components. These components all access a Direct to Web context with the `d2wContext` method. The D2WComponent class also defines several keys that are used in the binding (`.wod`) files for the Direct to Web templates. In addition, D2WComponent defines an action method, `showWebAssistant`, that opens the Web Assistant in the user's browser.

__Method Types__

---

Constructors

- [public D2WComponent()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5cdev2dn5wxa33omvxhil2egjlug33nobxw4zlooqxsqki)

---

Static Constants

- [currentObjectKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpiqzfoq3pnvyg63tfnz2c6y3vojzgk3tuj5rguzldorfwk6i)

---

Actions

- [logout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5wg6z3pov2c6v2pinxw24dpnzsw45bpfauq)
- [showWebAssistant](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwq33xk5sweqltonuxg5dbnz2c6v2pinxw24dpnzsw45bpfauq)

Key-Value Coding

- [backgroundColorForHeaderRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5rgcy3lm5zg65lomrbw63dpojdg64simvqwizlskjxxol2torzgs3thf4ucs)
- [backgroundColorForTable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5rgcy3lm5zg65lomrbw63dpojdg64sumfrgyzjpkn2he2lom4xsqki)
- [d2wContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5sde52dn5xhizlyoqxuimsxinxw45dfpb2c6kbj)
- [d2wContextVisibleEntityNamesCountPlus1](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5sde52dn5xhizlyorlgs43jmjwgkrlooruxi6komfwwk42dn52w45cqnr2xgmjpkn2he2lom4xsqki)
- [defaultRowspan](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5sgkztbovwhiutpo5zxaylof5jxi4tjnzts6kbj)
- [displayNameForKeyWhenRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5sgs43qnrqxsttbnvsum33sjnsxsv3imvxfezlmmf2gs33oonugs4bpkn2he2lom4xsqki)
- [displayNameForProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5sgs43qnrqxsttbnvsum33skbzg64dfoj2hsl2torzgs3thf4ucs)
- [displayPropertyKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5sgs43qnrqxsudsn5ygk4tupffwk6ltf5hfgqlsojqxslzife)
- [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5sw45djor4s6rkpivxhi2lupexsqki)
- [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5sw45djor4u4ylnmuxvg5dsnfxgolzife)
- [hasEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5ugc42fnz2gs5dzf5rg633mmvqw4lzife)
- [homeHref](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5ug63lfjbzgkzrpkn2he2lom4xsqki)
- [isEntityReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5uxgrlooruxi6ksmvqwit3onr4s6ytpn5wgkylof4ucs)
- [isPropertyAnAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5uxgudsn5ygk4tupfaw4qluorzgsytvorss6ytpn5wgkylof4ucs)
- [keyWhenRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5vwk6kxnbsw4utfnrqxi2lpnzzwq2lqf5jxi4tjnzts6kbj)
- [object](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5xwe2tfmn2c6rkpivxhizlsobzgs43fj5rguzldoqxsqki)
- [objectPropertyValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5xwe2tfmn2fa4tpobsxe5dzkzqwy5lff5hwe2tfmn2c6kbj)
- [propertyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5yhe33qmvzhi6klmv4s6u3uojuw4zzpfauq)
- [propertyValueClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5yhe33qmvzhi6kwmfwhkzkdnrqxg42omfwwkl2torzgs3thf4ucs)
- [relationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zgk3dboruw63ttnbuxal2fj5jgk3dboruw63ttnbuxalzife)
- [setLocalContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5cmn5rwc3cdn5xhizlyoqxxm33jmqxsqrbsk5bw63tumv4hiki)
- [setObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5cpmjvgky3uf53g62lef4uekt2fnz2gk4tqojuxgzkpmjvgky3ufe)
- [showBanner](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwq33xijqw43tfoixwe33pnrswc3rpfauq)
- [submitActionName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zxkytnnf2ecy3unfxw4ttbnvss6u3uojuw4zzpfauq)
- [task](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf52gc43lf5jxi4tjnzts6kbj)
- [visibleEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf53gs43jmjwgkrlooruxi6komfwwk4zpjzjuc4tsmf4s6kbj)

Private Methods

- [allEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5qwy3cfnz2gs5djmvzs6u3uojuw4zzpfauq)
- [allowCollapsing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5qwy3dpo5bw63dmmfyhg2lom4xus3tumvtwk4rpfauq)
- [applicationPort](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5qxa4dmnfrwc5djn5xfa33soqxws3tuf4ucs)
- [assistantPort](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5qxg43jon2gc3tukbxxe5bpnfxhilzife)
- [attribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5qxi5dsnfrhk5dff5cu6qluorzgsytvorss6kbj)
- [backgroundColorForPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5rgcy3lm5zg65lomrbw63dpojdg64sqmftwkl2torzgs3thf4ucs)
- [backgroundColorForTableDark](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5rgcy3lm5zg65lomrbw63dpojdg64sumfrgyzkemfzgwl2torzgs3thf4ucs)
- [backgroundColorForTableLight](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5rgcy3lm5zg65lomrbw63dpojdg64sumfrgyzkmnftwq5bpkn2he2lom4xsqki)
- [color](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5rw63dpoixvg5dsnfxgolzife)
- [currentSettings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5rxk4tsmvxhiu3for2gs3thomxvg5dsnfxgolzife)
- [dynamicPages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5shs3tbnvuwgudbm5sxgl2torzgs3thf4ucs)
- [finalize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5tgs3tbnruxuzjpozxwszbpfauq)
- [formatter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5tg64tnmf2hizlsf5jxi4tjnzts6kbj)
- [generationReplacementFor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5twk3tfojqxi2lpnzjgk4dmmfrwk3lfnz2em33sf5jxi4tjnzts6kctorzgs3thfe)
- [hasCustomKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5ugc42dovzxi33njnsxsl3cn5xwyzlbnyxsqu3uojuw4zzj)
- [hasNoColor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5ugc42on5bw63dpoixwe33pnrswc3rpfauq)
- [homeClicked](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5ug63lfinwgsy3lmvsc6v2pinxw24dpnzsw45bpfauq)
- [isEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5uxgrlenf2gs3thf5rg633mmvqw4lzife)
- [isEntityReadOnly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5uxgrlooruxi6ksmvqwit3onr4s6ytpn5wgkylof4uekt2fnz2gs5dzfe)
- [isNotBoldAsBoolean](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5uxgttporbg63deifzue33pnrswc3rpmjxw63dfmfxc6kbj)
- [isNotItalicAsBoolean](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5uxgttporexiylmnfruc42cn5xwyzlbnyxwe33pnrswc3rpfauq)
- [isWebAssistantActive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5uxgv3fmjaxg43jon2gc3tuifrxi2lwmuxwe33pnrswc3rpfauq)
- [isWebAssistantConnected](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5uxgv3fmjaxg43jon2gc3tuinxw43tfmn2gkzbpmjxw63dfmfxc6kbj)
- [isWebAssistantEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5uxgv3fmjaxg43jon2gc3tuivxgcytmmvsc6ytpn5wgkylof4ucs)
- [keyForGenerationReplacementForVariableNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2dn5wxa33omvxhil3lmv4um33si5sw4zlsmf2gs33okjsxa3dbmnsw2zloordg64swmfzgsylcnrsu4ylnmvsc6u3uojuw4zzpfbjxi4tjnztss)
- [length](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5wgk3thoruc6u3uojuw4zzpfauq)
- [objectPropertyValueIsNonNull](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5xwe2tfmn2fa4tpobsxe5dzkzqwy5lfjfzu433ojz2wy3bpmjxw63dfmfxc6kbj)
- [pageTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5ygcz3fkruxi3dff5jxi4tjnzts6kbj)
- [property](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5yhe33qmvzhi6jpj5rguzldoqxsqki)
- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zgk4dmmfrwk3lfnz2ec43tn5rwsylunfxw4rtpojaxg43pmnuwc5djn5xc6v2pifzxg33dnfqxi2lpnyxsqv2pifzxg33dnfqxi2lpnywfg5dsnfxgolcekrlvizlnobwgc5dffrlu6q3pnz2gk6dufe)
- [resourcePathURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zgk43povzggzkqmf2gqvksjqxvg5dsnfxgolzife)
- [sessionID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk43tnfxw4skef5jxi4tjnzts6kbj)
- [setCurrentSettings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5cdovzhezloorjwk5dunfxgo4zpozxwszbpfbjxi4tjnztss)
- [setDynamicPages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5cepfxgc3ljmnigcz3fomxxm33jmqxsqu3uojuw4zzj)
- [setEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5cfnz2gs5djmvzs65tpnfsc6kctorzgs3thfe)
- [setEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5cfnz2gs5dzf53g62lef4uekt2fnz2gs5dzfe)
- [setEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5cfnz2gs5dzjzqw2zjpozxwszbpfbjxi4tjnztss)
- [setPropertyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5cqojxxazlsor4uwzlzf53g62lef4ufg5dsnfxgoki)
- [setResourcePathURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5csmvzw65lsmnsvaylunbkvetbpozxwszbpfbjxi4tjnztss)
- [setTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5cumfzwwl3wn5uwilzikn2he2lom4uq)
- [setTasks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf5zwk5cumfzww4zpozxwszbpfbjxi4tjnztss)
- [target](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf52gc4thmv2c6u3uojuw4zzpfauq)
- [tasks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63lqn5xgk3tuf52gc43lomxvg5dsnfxgolzife)

---

__Constructors__

---

__D2WComponent__

public D2WComponent()

Standard Java no-argument constructor.

---

__Static Constants__

---

__currentObjectKey__
java.lang.String

This constant is intentionally undocumented.

---

__Methods__

__allEntities__

public String allEntities()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__allowCollapsing__

public Integer allowCollapsing()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__applicationPort__

public int applicationPort()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__assistantPort__

protected int assistantPort()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__attribute__

public EOAttribute attribute()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__backgroundColorForHeaderRow__

public String backgroundColorForHeaderRow()

Returns the background color for the header rows of tables rendered by Direct to Web.

---

__backgroundColorForPage__

public String backgroundColorForPage()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__backgroundColorForTable__

public String backgroundColorForTable()

Returns the background color for tables rendered in this component. This key is resolved using the rule system.

---

__backgroundColorForTableDark__

public String backgroundColorForTableDark()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__backgroundColorForTableLight__

public String backgroundColorForTableLight()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__color__

public String color()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__currentSettings__

public String currentSettings()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__d2wContext__

public D2WContext d2wContext()

Returns the receiver's Direct to Web context (a D2WContext object).

---

__d2wContextVisibleEntityNamesCountPlus1__

public String d2wContextVisibleEntityNamesCountPlus1()

Returns a String containing the number of visible entities in the receiver's Direct to Web context incremented by one.

---

__defaultRowspan__

public String defaultRowspan()

Returns the number of HTML table rows spanned by the vertical rule in the page containing the Direct to Web context in which the receiver's rule fires. The query and inspect pages in the WebObjects look use this method.

---

__displayNameForKeyWhenRelationship__

public String displayNameForKeyWhenRelationship()

Returns a String containing the name of a property that represents the destination object of the current relationship in the receiver's Direct to Web context. Returns `null` if the current property in the component's Direct to Web context is not a relationship.

The name is derived from the key for one of the properties of the destination entity that can be used to represent that entity. For example, the representative key for `Studio` could be `name`. This method determines the key using the rule system. To convert the key to a user-presentable name, the method capitalizes lower case words and inserts spaces between words with mixed case (for example, "firstName" becomes "First Name").

---

__displayNameForProperty__

public String displayNameForProperty()

Returns a String containing a user-presentable name for the current property in the component's Direct to Web context. The method derives the name from the property's key by capitalizing lower case words and inserting spaces between words with mixed case (for example, "firstName" becomes "First Name").

---

__displayPropertyKeys__

public NSArray displayPropertyKeys()

Returns an NSArray containing the keys (Strings) for all visible properties of the current entity in the components Direct to Web context. The method determines the result using the rule system.

You can hide a property or make it visible with the Web Assistant.

---

__dynamicPages__

protected String dynamicPages()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__entity__

public EOEntity entity()

Returns the current entity (an EOEntity object) in the receiver's Direct to Web context. The EOEntity class is defined in the EOAccess Framework.

---

__entityName__

public String entityName()

Returns a String containing the name of the entity displayed by this component.

---

__finalize__

public void finalize()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__formatter__

public String formatter()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__generationReplacementFor__

protected String generationReplacementFor(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__hasCustomKey__

public boolean hasCustomKey(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__hasEntity__

public boolean hasEntity()

Returns whether the receiver's Direct to Web context has an entity or not.

---

__hasNoColor__

public boolean hasNoColor()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__homeClicked__

public WOComponent homeClicked()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__homeHref__

public String homeHref()

Returns a String containing the URL of the application's home page (the `Main` component).

---

__isEditing__

public boolean isEditing()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isEntityReadOnly__

public boolean isEntityReadOnly()

Returns whether the current entity in the receiver's Direct to Web context can be modified or not. You can specify if an entity can be modified using the Web Assistant.

---

__isEntityReadOnly__

public boolean isEntityReadOnly(EOEntity anEntity)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isLiveAssistantEnabled__

public boolean isLiveAssistantEnabled()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isNotBoldAsBoolean__

public boolean isNotBoldAsBoolean()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isNotItalicAsBoolean__

public boolean isNotItalicAsBoolean()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isPropertyAnAttribute__

public boolean isPropertyAnAttribute()

Returns `true` if the property in the receiver's Direct to Web context is an attribute (and not a relationship).

---

__isWebAssistantActive__

public boolean isWebAssistantActive()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isWebAssistantConnected__

public boolean isWebAssistantConnected()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isWebAssistantEnabled__

public boolean isWebAssistantEnabled()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__keyForGenerationReplacementForVariableNamed__

public static String keyForGenerationReplacementForVariableNamed(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__keyWhenRelationship__

public String keyWhenRelationship()

Returns a String containing the key for the property that represents the destination object of the current relationship in the receiver's Direct to Web context. Returns `null` if the current property in the Direct to Web is not a relationship.

The returned key is the key for one of the properties of the destination entity that can be used to represent the entity. For example, the representative key for `Studio` could be `name`. The method determines the result using the rule system.

---

__length__

public String length()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__localContext__

public D2WContext localContext()

This method is deprecated. Use `d2wContext` instead.

---

__logout__

public WOComponent logout()

This action method is invoked when the user clicks Logout in the menu bar. It terminates the current session and returns the application's home page WOComponent (`Main`).

---

__object__

public EOEnterpriseObject object()

Returns the EOEnterpriseObject (defined in the EOControl Framework) displayed by this component.

---

__objectPropertyValue__

public Object objectPropertyValue()

Returns the value of the current property for the object the receiver displays. For example, if the current entity in the component's Direct to Web context is "Movie" and the current property key is "title", this method returns the title of the movie displayed in this component.

---

__objectPropertyValueIsNonNull__

public boolean objectPropertyValueIsNonNull()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__pageTitle__

public String pageTitle()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__property__

public Object property()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__propertyKey__

public String propertyKey()

Returns the key corresponding to the current property in the receiver's Direct to Web context.

---

__propertyValueClassName__

public String propertyValueClassName()

Returns a String containing the name of the class for the current attribute's values ("NSString" for example). If the current property in the component's Direct to Web context is not an attribute, this method returns `null`.

---

__relationship__

public EORelationship relationship()

Returns the EORelationship (defined in the EOAccess Framework) for the current property in the receiver's Direct to Web context, or `null` if the property is not a relationship.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__resourcePathURL__

public String resourcePathURL()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__sessionID__

protected String sessionID()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setCurrentSettings__

public void setCurrentSettings(String settings)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setDynamicPages__

protected void setDynamicPages(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setEntities__

public void setEntities(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setEntity__

public void setEntity(EOEntity entity)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setEntityName__

public void setEntityName(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setLocalContext__

public void setLocalContext(D2WContext context)

Sets the Direct to Web context for this component to `context`.

---

__setObject__

public void setObject(EOEnterpriseObject object)

Sets the EOEnterpriseObject (defined in the EOControl Framework) the receiver manipulates to `object`.

---

__setPropertyKey__

public void setPropertyKey(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setResourcePathURL__

public void setResourcePathURL(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setTask__

protected void setTask(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setTasks__

protected void setTasks(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__showBanner__

public boolean showBanner()

Returns whether the banner should be shown in this component or not. If the component is an embedded component, the banner is not shown.

---

__showWebAssistant__

public WOComponent showWebAssistant()

This action method is invoked when the user clicks Customize in the menu bar. It displays the Web Assistant in the user's browser.

---

__submitActionName__

public String submitActionName()

The name of an action method that is called when the user clicks a submit button within the form. This action method is used in the tab panel components, that is, NEUTabInspectPage and WOLTabInspectPage to specify the WOTabPanel's `submitActionName` binding.

---

__target__

public String target()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__task__

protected String task()

Returns a String containing the current task in the receiver's Direct to Web context.

---

__tasks__

protected String tasks()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__visibleEntityNames__

public NSArray visibleEntityNames()

Returns an NSArray containing the entities that are visible within the application. You can choose which entities are visible using the Web Assistant.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
