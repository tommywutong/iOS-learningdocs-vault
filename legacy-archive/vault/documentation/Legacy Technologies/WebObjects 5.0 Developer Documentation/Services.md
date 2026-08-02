---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/Services.html
archived_at: '2026-07-15T08:12:45.549184Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__Services__

__Package__:
com.webobjects.directtoweb

__Inherits from__:java.lang.Object

---

__Class Description__

---

This class is used internally by other classes in WebObjects and should be considered private. It should not be used, subclassed, or replaced.

__Method Types__

---

Constructors

- [public Services()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3foj3gsy3fomxvgzlsozuwgzltf5jwk4twnfrwk4zpfauq)

---

Private Methods

- [breakDown](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpmjzgkyllirxxo3rpkn2he2lom4xsqu3uojuw4zzmnfxhiki)
- [capitalize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpmnqxa2lumfwgs6tff5jxi4tjnzts6kctorzgs3thfe)
- [dictionaryFromFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpmruwg5djn5xgc4tzizzg63kgnfwgkl2okncgsy3unfxw4ylspexsqrtjnrsss)
- [flatten](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpmzwgc5dumvxc6tstifzheylzf4ue4u2bojzgc6jj)
- [formKeyForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpmzxxe3klmv4um33sjnsxsl2torzgs3thf4ufg5dsnfxgoki)
- [htmlify](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpnb2g23djmz4s6u3uojuw4zzpfbjxi4tjnztss)
- [htmlQuotify](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpnb2g23crovxxi2lgpexvg5dsnfxgolzikn2he2lom4uq)
- [mergeHashtableIntoHashtable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpnvsxez3fjbqxg2dumfrgyzkjnz2g6sdbonuhiylcnrss65tpnfsc6kcimfzwq5dbmjwgklcimfzwq5dbmjwgkki)
- [mergeVectorIntoVector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpnvsxez3fkzswg5dpojew45dpkzswg5dpoixxm33jmqxsqvtfmn2g64rmkzswg5dpoiuq)
- [mergeVectorIntoVectorWithoutDuplicates](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpnvsxez3fkzswg5dpojew45dpkzswg5dpojlws5din52xirdvobwgsy3borsxgl3wn5uwilzikzswg5dpoiwfmzldorxxeki)
- [objectFromPListFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpn5rguzldordhe33nkbggs43uizuwyzjpj5rguzldoqxsqrtjnrsss)
- [plurify](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpobwhk4tjmz4s6u3uojuw4zzpfbjxi4tjnztsy2looquq)
- [replace](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpojsxa3dbmnss6u3uojuw4zzpfbjxi4tjnztsyu3uojuw4zzmkn2he2lom4wgs3tufruw45bj)
- [replace](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpojsxa3dbmnss6u3uojuw4zzpfbjxi4tjnztsyu3uojuw4zzmkn2he2lom4uq)
- [replaceFileContents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpojsxa3dbmnsum2lmmvbw63tumvxhi4zpozxwszbpfbdgs3dffrjxi4tjnztss)
- [stringFromFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpon2he2lom5dhe33nizuwyzjpkn2he2lom4xsqrtjnrsss)
- [vectorFromImmutableVector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpozswg5dpojdhe33njfww25lumfrgyzkwmvrxi33sf5lgky3un5zc6kcoknaxe4tbpeuq)
- [writeDictionaryToFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jwk4twnfrwk4zpo5zgs5dfiruwg5djn5xgc4tzkrxum2lmmuxxm33jmqxsqtstiruwg5djn5xgc4tzfrdgs3dffe)

---

__Constructors__

---

__Services__

public Services()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Methods__

__breakDown__

static public String breakDown(String aString, int anInt)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__capitalize__

static public String capitalize(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__dictionaryFromFile__

public static NSDictionary dictionaryFromFile(File file)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__flatten__

public static NSArray flatten(NSArray anArray)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__formKeyForKey__

static public String formKeyForKey(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__htmlify__

static public String htmlify(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__htmlQuotify__

public static String htmlQuotify(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__mergeHashtableIntoHashtable__

static public void mergeHashtableIntoHashtable(Hashtable hashtable1, Hashtable hashtable2)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__mergeVectorIntoVector__

public static void mergeVectorIntoVector(Vector vector1, Vector vector2)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__mergeVectorIntoVectorWithoutDuplicates__

public static void mergeVectorIntoVectorWithoutDuplicates(Vector vector1, Vector vector2)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__objectFromPListFile__

static public Object objectFromPListFile(File file)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__plurify__

static public String plurify(String aString, int anInt)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replace__

public static String replace(String string1, String string2, String string3, int int1, int int2)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replace__

static public String replace(String string1, String string2, String string3)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__replaceFileContents__

static public void replaceFileContents(File file, String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__stringFromFile__

public static String stringFromFile(File file)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__vectorFromImmutableVector__

static public Vector vectorFromImmutableVector(NSArray anArray)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__writeDictionaryToFile__

static public void writeDictionaryToFile(NSDictionary aDictionary, File file)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
