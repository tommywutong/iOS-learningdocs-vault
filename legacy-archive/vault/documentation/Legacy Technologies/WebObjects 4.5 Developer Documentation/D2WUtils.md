---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/D2WUtils.html
archived_at: '2026-07-15T08:11:30.622252Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__D2WUtils__

__Package__:
com.apple.yellow.directtoweb

__Inherits from__:java.lang.Object

---

__Class Description__

---

This class is used internally by other classes in WebObjects and should be considered private. It should not be used, subclassed, or replaced.

__Method Types__

---

Constructors

- [public D2WUtils()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5kxi2lmomxuimsxkv2gs3dtf5cdev2voruwy4zpfauq)

---

Private Methods

- [allEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpmfwgyrlooruxi2lfomxu4u2bojzgc6jpfauq)
- [appletViewerCommand](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpmfyha3dforlgszlxmvzeg33nnvqw4zbpkn2he2lom4xsqki)
- [applicationPort](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpmfyha3djmnqxi2lpnzig64tuf5uw45bpfauq)
- [availableKeysForInterfaceAndKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpmf3gc2lmmfrgyzklmv4xgrtpojew45dfojtgcy3fifxgis3fpfigc5dif5hfgqlsojqxslzik5bes3tumvzgmyldmvcgk43dojuxa5dpoiwe4u2bojzgc6jj)
- [darker](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpmrqxe23foixvg5dsnfxgolzikn2he2lom4uq)
- [dataTypeForCustomKeyAndEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpmrqxiykupfygkrtpojbxk43un5wuwzlzifxgirlooruxi6jpinwgc43tf4ufg5dsnfxgolcfj5cw45djor4ss)
- [flushCaches](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpmzwhk43iinqwg2dfomxxm33jmqxsqki)
- [forName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpmzxxettbnvss6q3mmfzxglzikn2he2lom4uq)
- [homeHrefInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpnbxw2zkiojswmsloinxw45dfpb2c6u3uojuw4zzpfblu6q3pnz2gk6dufe)
- [keyDescriptorForInterfaceAndKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpnnsxsrdfonrxe2lqorxxertpojew45dfojtgcy3fifxgis3fpfigc5dif5lues3fpfcgk43dojuxa5dpoixsqv2cjfxhizlsmzqwgzkemvzwg4tjob2g64rmjzjuc4tsmf4ss)
- [lighter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpnruwo2dumvzc6u3uojuw4zzpfbjxi4tjnztss)
- [makeSubContextForDynamicPageNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpnvqwwzktovreg33oorsxq5cgn5zei6lomfwwsy2qmftwkttbnvswil2egjlug33oorsxq5bpfbjxi4tjnztsyv2pknsxg43jn5xcs)
- [makeSubContextForTaskAndEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpnvqwwzktovreg33oorsxq5cgn5zfiyltnnaw4zcfnz2gs5dzf5cdev2dn5xhizlyoqxsqu3uojuw4zzmivhuk3tunf2hslcxj5jwk43tnfxw4ki)
- [propertyKeyDescriptorsFromEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpobzg64dfoj2hss3fpfcgk43dojuxa5dpojzum4tpnvcw45djor4s6tstifzheylzf4uekt2fnz2gs5dzfe)
- [readableDateFormatDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpojswczdbmjwgkrdborsum33snvqxirdfonrxe2lqoruw63rpkn2he2lom4xsqu3uojuw4zzj)
- [readOnlyEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpojswczcpnzwhsrlooruxi6komfwwk4zpjzjuc4tsmf4s6kcegjlug33oorsxq5bj)
- [safeEquals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zponqwmzkfof2wc3dtf5rg633mmvqw4lzij5rguzldoqwe6ytkmvrxiki)
- [smartDefaultEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zponwwc4tuirswmylvnr2ek3tunf2hsttbnvsxgl2oknaxe4tbpexsqki)
- [smartDefaultKeyForEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zponwwc4tuirswmylvnr2ewzlzizxxerlooruxi6jpkn2he2lom4xsqrkpivxhi2lupeuq)
- [urlFromUrlAndFormValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpovzgyrtsn5wvk4tmifxgirtpojwvmylmovsxgl2torzgs3thf4ufg5dsnfxgolcokncgsy3unfxw4ylspeuq)
- [userDefaultsValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpovzwk4semvtgc5lmorzvmylmovsum33sjnsxsl2torzgs3thf4ufg5dsnfxgoki)
- [visibleEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cdev2voruwy4zpozuxg2lcnrsuk3tunf2hsttbnvsxgl2oknaxe4tbpexsqrbsk5bw63tumv4hiki)

---

__Constructors__

---

__com.apple.yellow.directtoweb.D2WUtils__

public D2WUtils()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Methods__

__allEntities__

static public NSArray allEntities()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__appletViewerCommand__

static public String appletViewerCommand()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__applicationPort__

public static int applicationPort()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__availableKeysForInterfaceAndKeyPath__

static public NSArray availableKeysForInterfaceAndKeyPath(WBInterfaceDescriptor descriptor, NSArray anArray)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__darker__

static public String darker(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__dataTypeForCustomKeyAndEntity__

public static final Class dataTypeForCustomKeyAndEntity(String aString, EOEntity anEntity)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__flushCaches__

static protected void flushCaches()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__forName__

static public Class forName(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__homeHrefInContext__

static public String homeHrefInContext(WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__keyDescriptorForInterfaceAndKeyPath__

public static WBKeyDescriptor keyDescriptorForInterfaceAndKeyPath(WBInterfaceDescriptor descriptor, NSArray anArray)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__lighter__

public static String lighter(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__makeSubContextForDynamicPageNamed__

static public D2WContext makeSubContextForDynamicPageNamed(String aString, WOSession session)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__makeSubContextForTaskAndEntity__

public static D2WContext makeSubContextForTaskAndEntity(String aString, EOEntity anEntity, WOSession session)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__propertyKeyDescriptorsFromEntity__

static public NSArray propertyKeyDescriptorsFromEntity(EOEntity anEntity)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__readableDateFormatDescription__

public static String readableDateFormatDescription(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__readOnlyEntityNames__

static public NSArray readOnlyEntityNames(D2WContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__safeEquals__

static public boolean safeEquals(Object object1, Object object2)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__smartDefaultEntityNames__

public static NSArray smartDefaultEntityNames()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__smartDefaultKeyForEntity__

public static String smartDefaultKeyForEntity(EOEntity anEntity)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__urlFromUrlAndFormValues__

public static String urlFromUrlAndFormValues(String aString, NSDictionary aDictionary)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__userDefaultsValueForKey__

static public String userDefaultsValueForKey(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__visibleEntityNames__

public static NSArray visibleEntityNames(D2WContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---
