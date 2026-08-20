---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/Settings.html
archived_at: '2026-07-15T08:11:31.020935Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__Settings__

__Package__:
com.apple.client.directtoweb.common

__Inherits from__:java.lang.Object__Implements__:

- [D2WKeyValueArchiving](D2WKeyValueArchiving.md)

__Subclasses__:

- [ServerSideSettings](ServerSideSettings.md)

---

__Class Description__

---

This class is used internally by other classes in WebObjects and should be considered private. It should not be used, subclassed, or replaced.

__Method Types__

---

Constructors

- [public Settings()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxvgzluoruw4z3tf5jwk5dunfxgo4zpfauq)

---

Static Constants

- [allMarker](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3bnrwe2ylsnnsxe)
- [areCurrentSettingsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3bojsug5lsojsw45ctmv2hi2lom5zuwzlz)
- [componentsInApplicationWrapperKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3dn5wxa33omvxhi42jnzaxa4dmnfrwc5djn5xfo4tbobygk4slmv4q)
- [dataTypesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3emf2gcvdzobsxgs3fpe)
- [dirtyReadOnlyEntitiesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3enfzhi6ksmvqwit3onr4uk3tunf2gszltjnsxs)
- [dynamicPageKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3epfxgc3ljmnigcz3fjnsxs)
- [dynamicPageNamesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3epfxgc3ljmnigcz3fjzqw2zltjnsxs)
- [entityKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3fnz2gs5dzjnsxs)
- [framesActiveKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3gojqw2zltifrxi2lwmvfwk6i)
- [lookKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3mn5xwws3fpe)
- [noneMarker](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3on5xgktlbojvwk4q)
- [pageConfigurationKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3qmftwkq3pnztgsz3vojqxi2lpnzfwk6i)
- [propertiesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3qojxxazlsoruwk42lmv4q)
- [readOnlyEntityNamesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3smvqwit3onr4uk3tunf2hsttbnvsxgs3fpe)
- [serverDirtyKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3tmvzhmzlsiruxe5dzjnsxs)
- [startupEntityKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3torqxe5dvobcw45djor4uwzlz)
- [startupTaskKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3torqxe5dvobkgc43ljnsxs)
- [taskKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3umfzwws3fpe)
- [visibleEntityNamesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3wnfzwsytmmvcw45djor4u4ylnmvzuwzlz)

---

Fields

- [areCurrentSettings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3bojsug5lsojsw45ctmv2hi2lom5zq)
- [dirtyReadOnlyEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3enfzhi6ksmvqwit3onr4uk3tunf2gszlt)
- [dynamicPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3epfxgc3ljmnigcz3f)
- [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3fnz2gs5dz)
- [framesActive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3gojqw2zltifrxi2lwmu)
- [look](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3mn5xww)
- [pageConfiguration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3qmftwkq3pnztgsz3vojqxi2lpny)
- [serverDirty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3tmvzhmzlsiruxe5dz)
- [startupEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3torqxe5dvobcw45djor4q)
- [startupTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3torqxe5dvobkgc43l)
- [task](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpknsxi5djnztxgl3umfzww)

---

Private Methods

- [addProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwczdekbzg64dfoj2hsl3wn5uwilzikbzg64dfoj2hski)
- [addReadOnlyEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwczdekjswczcpnzwhsrlooruxi6komfwwkl3wn5uwilzikn2he2lom4uq)
- [addVisibleEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwczdekzuxg2lcnrsuk3tunf2hsttbnvss65tpnfsc6kctorzgs3thfe)
- [componentsInApplicationWrapper](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwg33nobxw4zloorzus3sbobygy2ldmf2gs33ok5zgc4dqmvzc6vtfmn2g64rpfauq)
- [dataTypes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwiylumfkhs4dfomxvmzldorxxelzife)
- [decodeWithD2WKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwizldn5sgkv3jorueimsxjnsxsvtbnr2wkvlomfzgg2djozsxel3wn5uwilziiqzfos3fpflgc3dvmvkw4ylsmnugs5tfoiuq)
- [encodeWithD2WKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwk3tdn5sgkv3jorueimsxjnsxsvtbnr2wkqlsmnugs5tfoixxm33jmqxsqrbsk5fwk6kwmfwhkzkbojrwq2lwmvzcs)
- [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwk4lvmfwhgl3cn5xwyzlbnyxsqt3cnjswg5bj)
- [forADynamicPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwm33sifchs3tbnvuwgudbm5ss6ytpn5wgkylof4ucs)
- [forAllEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwm33sifwgyrlooruxi2lfomxwe33pnrswc3rpfauq)
- [forAllTasks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxwm33sifwgyvdbonvxgl3cn5xwyzlbnyxsqki)
- [properties](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxxa4tpobsxe5djmvzs6vtfmn2g64rpfauq)
- [propertyForName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxxa4tpobsxe5dzizxxettbnvss6udsn5ygk4tupexsqu3uojuw4zzj)
- [readOnlyEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxxezlbmrhw43dzivxhi2lupfhgc3lfomxvmzldorxxelzife)
- [setComponentsInApplicationWrapper](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxxgzluinxw24dpnzsw45dtjfxec4dqnruwgylunfxw4v3smfyhazlsf53g62lef4ufmzldorxxeki)
- [setDataTypes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxxgzluirqxiykupfygk4zpozxwszbpfblgky3un5zcs)
- [setReadOnlyEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxxgzlukjswczcpnzwhsrlooruxi6komfwwk4zpozxwszbpfblgky3un5zcs)
- [setVisibleEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxxgzlukzuxg2lcnrsuk3tunf2hsttbnvsxgl3wn5uwilzikzswg5dpoiuq)
- [toShortString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxxi32tnbxxe5ctorzgs3thf5jxi4tjnzts6kbj)
- [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxxi32torzgs3thf5jxi4tjnzts6kbj)
- [visibleEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3for2gs3thomxxm2ltnfrgyzkfnz2gs5dzjzqw2zltf5lgky3un5zc6kbj)

---

__Constructors__

---

__com.apple.client.directtoweb.common.Settings__

public Settings()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Static Constants__

---

__allMarker__
java.lang.String

This constant is intentionally undocumented.

---

__areCurrentSettingsKey__
java.lang.String

This constant is intentionally undocumented.

---

__componentsInApplicationWrapperKey__
java.lang.String

This constant is intentionally undocumented.

---

__dataTypesKey__
java.lang.String

This constant is intentionally undocumented.

---

__dirtyReadOnlyEntitiesKey__
java.lang.String

This constant is intentionally undocumented.

---

__dynamicPageKey__
java.lang.String

This constant is intentionally undocumented.

---

__dynamicPageNamesKey__
java.lang.String

This constant is intentionally undocumented.

---

__entityKey__
java.lang.String

This constant is intentionally undocumented.

---

__framesActiveKey__
java.lang.String

This constant is intentionally undocumented.

---

__lookKey__
java.lang.String

This constant is intentionally undocumented.

---

__noneMarker__
java.lang.String

This constant is intentionally undocumented.

---

__pageConfigurationKey__
java.lang.String

This constant is intentionally undocumented.

---

__propertiesKey__
java.lang.String

This constant is intentionally undocumented.

---

__readOnlyEntityNamesKey__
java.lang.String

This constant is intentionally undocumented.

---

__serverDirtyKey__
java.lang.String

This constant is intentionally undocumented.

---

__startupEntityKey__
java.lang.String

This constant is intentionally undocumented.

---

__startupTaskKey__
java.lang.String

This constant is intentionally undocumented.

---

__taskKey__
java.lang.String

This constant is intentionally undocumented.

---

__visibleEntityNamesKey__
java.lang.String

This constant is intentionally undocumented.

---

__Fields__

---

__areCurrentSettings__
boolean

This constant is intentionally undocumented.

---

__dirtyReadOnlyEntities__
boolean

This constant is intentionally undocumented.

---

__dynamicPage__
java.lang.String

This constant is intentionally undocumented.

---

__entity__
java.lang.String

This constant is intentionally undocumented.

---

__framesActive__
boolean

This constant is intentionally undocumented.

---

__look__
java.lang.String

This constant is intentionally undocumented.

---

__pageConfiguration__
com.apple.client.directtoweb.common.PageConfiguration

This constant is intentionally undocumented.

---

__serverDirty__
boolean

This constant is intentionally undocumented.

---

__startupEntity__
java.lang.String

This constant is intentionally undocumented.

---

__startupTask__
java.lang.String

This constant is intentionally undocumented.

---

__task__
java.lang.String

This constant is intentionally undocumented.

---

__Methods__

__addProperty__

public void addProperty(Property aProperty)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__addReadOnlyEntityName__

public void addReadOnlyEntityName(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__addVisibleEntityName__

public void addVisibleEntityName(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__componentsInApplicationWrapper__

public Vector componentsInApplicationWrapper()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__dataTypes__

public Vector dataTypes()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__decodeWithD2WKeyValueUnarchiver__

public void decodeWithD2WKeyValueUnarchiver(D2WKeyValueUnarchiver unarchiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__encodeWithD2WKeyValueArchiver__

public void encodeWithD2WKeyValueArchiver(D2WKeyValueArchiver archiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__equals__

public boolean equals(Object anObject)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__forADynamicPage__

public boolean forADynamicPage()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__forAllEntities__

public boolean forAllEntities()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__forAllTasks__

public boolean forAllTasks()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__properties__

public Vector properties()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__propertyForName__

public Property propertyForName(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__readOnlyEntityNames__

public Vector readOnlyEntityNames()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setComponentsInApplicationWrapper__

public void setComponentsInApplicationWrapper(Vector aVector)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setDataTypes__

public void setDataTypes(Vector aVector)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setReadOnlyEntityNames__

public void setReadOnlyEntityNames(Vector aVector)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setVisibleEntityNames__

public void setVisibleEntityNames(Vector aVector)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__toShortString__

public String toShortString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__toString__

public String toString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__visibleEntityNames__

public Vector visibleEntityNames()

This method is intentionally undocumented. You should never have to invoke or customize it.

---
