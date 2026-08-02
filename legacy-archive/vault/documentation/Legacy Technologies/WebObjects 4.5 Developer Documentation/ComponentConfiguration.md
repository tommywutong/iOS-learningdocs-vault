---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/ComponentConfiguration.html
archived_at: '2026-07-15T08:11:28.485045Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__ComponentConfiguration__

__Package__:
com.apple.client.directtoweb.common

__Inherits from__:java.lang.Object__Implements__:

- [D2WKeyValueArchiving](D2WKeyValueArchiving.md)

__Subclasses__:

- [PageConfiguration](PageConfiguration.md)

---

__Class Description__

---

This class is used internally by other classes in WebObjects and should be considered private. It should not be used, subclassed, or replaced.

__Method Types__

---

Constructors

- [public ComponentConfiguration()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5bw63lqn5xgk3tuinxw4ztjm52xeylunfxw4l2dn5wxa33omvxhiq3pnztgsz3vojqxi2lpnyxsqki)

---

Static Constants

- [boldKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpinxw24dpnzsw45cdn5xgm2lhovzgc5djn5xc6ytpnrsewzlz)
- [choicesKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpinxw24dpnzsw45cdn5xgm2lhovzgc5djn5xc6y3in5uwgzltjnsxs)
- [colorKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpinxw24dpnzsw45cdn5xgm2lhovzgc5djn5xc6y3pnrxxes3fpe)
- [componentNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpinxw24dpnzsw45cdn5xgm2lhovzgc5djn5xc6y3pnvyg63tfnz2e4ylnmvfwk6i)
- [dataKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpinxw24dpnzsw45cdn5xgm2lhovzgc5djn5xc6zdborquwzlz)
- [italicKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpinxw24dpnzsw45cdn5xgm2lhovzgc5djn5xc62lumfwgsy2lmv4q)
- [keyWhenRelationshipKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpinxw24dpnzsw45cdn5xgm2lhovzgc5djn5xc623fpflwqzlokjswyylunfxw443infyewzlz)

---

Private Methods

- [addChoice](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5qwizcdnbxwsy3ff53g62lef4ue6ytkmvrxiki)
- [bold](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5rg63def5jxi4tjnzts6kbj)
- [choices](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5rwq33jmnsxgl2wmvrxi33sf4ucs)
- [color](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5rw63dpoixvg5dsnfxgolzife)
- [componentName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5rw63lqn5xgk3tujzqw2zjpkn2he2lom4xsqki)
- [decodeWithD2WKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5sgky3pmrsvo2lunbcdev2lmv4vmylmovsvk3tbojrwq2lwmvzc65tpnfsc6kcegjluwzlzkzqwy5lfkvxgc4tdnbuxmzlsfe)
- [encodeWithD2WKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5sw4y3pmrsvo2lunbcdev2lmv4vmylmovsuc4tdnbuxmzlsf53g62lef4ueimsxjnsxsvtbnr2wkqlsmnugs5tfoiuq)
- [italic](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5uxiylmnfrs6u3uojuw4zzpfauq)
- [keyWhenRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5vwk6kxnbsw4utfnrqxi2lpnzzwq2lqf5jxi4tjnzts6kbj)
- [setBold](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5zwk5ccn5wgil3wn5uwilzikn2he2lom4uq)
- [setChoices](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5zwk5cdnbxwsy3fomxxm33jmqxsqvtfmn2g64rj)
- [setColor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5zwk5cdn5wg64rpozxwszbpfbjxi4tjnztss)
- [setComponentName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5zwk5cdn5wxa33omvxhittbnvss65tpnfsc6kctorzgs3thfe)
- [setItalic](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5zwk5cjorqwy2ldf53g62lef4ufg5dsnfxgoki)
- [setKeyWhenRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of5zwk5clmv4vo2dfnzjgk3dboruw63ttnbuxal3wn5uwilzikn2he2lom4uq)
- [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of52gc23fkzqwy5lfizxxes3fpexxm33jmqxsqt3cnjswg5bmkn2he2lom4uq)
- [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6q3pnvyg63tfnz2eg33omzuwo5lsmf2gs33of53gc3dvmvdg64slmv4s6t3cnjswg5bpfbjxi4tjnztss)

---

__Constructors__

---

__com.apple.client.directtoweb.common.ComponentConfiguration__

public ComponentConfiguration()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Static Constants__

---

__boldKey__
java.lang.String

This constant is intentionally undocumented.

---

__choicesKey__
java.lang.String

This constant is intentionally undocumented.

---

__colorKey__
java.lang.String

This constant is intentionally undocumented.

---

__componentNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__dataKey__
java.lang.String

This constant is intentionally undocumented.

---

__italicKey__
java.lang.String

This constant is intentionally undocumented.

---

__keyWhenRelationshipKey__
java.lang.String

This constant is intentionally undocumented.

---

__Methods__

__addChoice__

public final void addChoice(Object anObject)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__bold__

final public String bold()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__choices__

final public Vector choices()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__color__

final public String color()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__componentName__

final public String componentName()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__decodeWithD2WKeyValueUnarchiver__

final public void decodeWithD2WKeyValueUnarchiver(D2WKeyValueUnarchiver unarchiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__encodeWithD2WKeyValueArchiver__

public final void encodeWithD2WKeyValueArchiver(D2WKeyValueArchiver archiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__italic__

final public String italic()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__keyWhenRelationship__

public final String keyWhenRelationship()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setBold__

public final void setBold(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setChoices__

public final void setChoices(Vector aVector)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setColor__

public final void setColor(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setComponentName__

public void setComponentName(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setItalic__

public final void setItalic(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setKeyWhenRelationship__

final public void setKeyWhenRelationship(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__takeValueForKey__

public final void takeValueForKey(Object anObject, String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__valueForKey__

public final Object valueForKey(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---
