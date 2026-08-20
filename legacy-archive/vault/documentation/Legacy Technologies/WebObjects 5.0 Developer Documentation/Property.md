---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/Property.html
archived_at: '2026-07-15T08:12:45.341458Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__Property__

__Package__:
com.apple.client.directtoweb.common

__Inherits from__:java.lang.Object__Implements__:

- [D2WKeyValueArchiving](D2WKeyValueArchiving.md)

---

__Class Description__

---

This class is used internally by other classes in WebObjects and should be considered private. It should not be used, subclassed, or replaced.

__Method Types__

---

Constructors

- [public Property()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexva4tpobsxe5dzf5ihe33qmvzhi6jpfauq)
- [public Property(String string1, String string2, boolean aBoolean, int anInt, String string3, ComponentConfiguration aConfiguration, Vector aVector)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexva4tpobsxe5dzf5ihe33qmvzhi6jpfbjxi4tjnztsyu3uojuw4zzmmjxw63dfmfxcy2looqwfg5dsnfxgolcdn5wxa33omvxhiq3pnztgsz3vojqxi2lpnywfmzldorxxeki)

---

Static Constants

- [alternativeComponentsInFrameworkKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl3bnr2gk4tomf2gs5tfinxw24dpnzsw45dtjfxem4tbnvsxo33snnfwk6i)
- [ATTRIBUTE](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl2bkrkfeskckvkek)
- [componentConfigurationKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl3dn5wxa33omvxhiq3pnztgsz3vojqxi2lpnzfwk6i)
- [CUSTOM_KEY](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl2dkvjvit2nl5fukwi)
- [displayNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl3enfzxa3dbpfhgc3lfjnsxs)
- [hasChildrenKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl3imfzug2djnrshezlojnsxs)
- [KEYPATH](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl2livmvaqkuja)
- [propertyNameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl3qojxxazlsor4u4ylnmvfwk6i)
- [TO_MANY_RELATIONSHIP](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl2uj5pu2qkolfpverkmifkest2okneesua)
- [TO_ONE_RELATIONSHIP](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl2uj5pu6tsfl5jektcbkreu6tstjbeva)
- [typeKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl3upfygks3fpe)
- [valueTypeKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl3wmfwhkzkupfygks3fpe)
- [visibleKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbzg64dfoj2hsl3wnfzwsytmmvfwk6i)

---

Private Methods

- [alternativeComponentsInFramework](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexwc3dumvzg4ylunf3gkq3pnvyg63tfnz2hgsloizzgc3lfo5xxe2zpkzswg5dpoixsqki)
- [componentConfiguration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexwg33nobxw4zloorbw63tgnftxk4tboruw63rpinxw24dpnzsw45cdn5xgm2lhovzgc5djn5xc6kbj)
- [copyValuesFrom](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexwg33qpflgc3dvmvzum4tpnuxxm33jmqxsqudsn5ygk4tupeuq)
- [decodeWithD2WKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexwizldn5sgkv3jorueimsxjnsxsvtbnr2wkvlomfzgg2djozsxel3wn5uwilziiqzfos3fpflgc3dvmvkw4ylsmnugs5tfoiuq)
- [displayName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexwi2ltobwgc6komfwwkl2torzgs3thf4ucs)
- [encodeWithD2WKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexwk3tdn5sgkv3jorueimsxjnsxsvtbnr2wkqlsmnugs5tfoixxm33jmqxsqrbsk5fwk6kwmfwhkzkbojrwq2lwmvzcs)
- [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexwk4lvmfwhgl3cn5xwyzlbnyxsqt3cnjswg5bj)
- [hasChildren](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexwqyltinugs3deojsw4l3cn5xwyzlbnyxsqki)
- [isComplete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexws42dn5wxa3dforss6ytpn5wgkylof4ucs)
- [isEOModelProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexws42fj5gw6zdfnrihe33qmvzhi6jpmjxw63dfmfxc6kbj)
- [markIncomplete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexw2ylsnnew4y3pnvygyzlumuxxm33jmqxsqki)
- [propertyName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxa4tpobsxe5dzjzqw2zjpkn2he2lom4xsqki)
- [setAlternativeComponentsInFramework](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxgzluifwhizlsnzqxi2lwmvbw63lqn5xgk3tuonew4rtsmfwwk53pojvs65tpnfsc6kcwmvrxi33sfe)
- [setComponentConfiguration](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxgzluinxw24dpnzsw45cdn5xgm2lhovzgc5djn5xc65tpnfsc6kcdn5wxa33omvxhiq3pnztgsz3vojqxi2lpnyuq)
- [setDisplayName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxgzluiruxg4dmmf4u4ylnmuxxm33jmqxsqu3uojuw4zzj)
- [setHasChildren](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxgzlujbqxgq3infwgi4tfnyxxm33jmqxsqytpn5wgkylofe)
- [setPropertyName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxgzlukbzg64dfoj2hsttbnvss65tpnfsc6kctorzgs3thfe)
- [setType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxgzlukr4xazjpozxwszbpfbuw45bj)
- [setVisibility](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxgzlukzuxg2lcnfwgs5dzf53g62lef4uge33pnrswc3rj)
- [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxi32torzgs3thf5jxi4tjnzts6kbj)
- [type](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxi6lqmuxws3tuf4ucs)
- [valueType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxmylmovsvi6lqmuxvg5dsnfxgolzife)
- [visibility](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udsn5ygk4tupexxm2ltnfrgs3djor4s6ytpn5wgkylof4ucs)

---

__Constructors__

---

__com.apple.client.directtoweb.common.Property__

public Property()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__com.apple.client.directtoweb.common.Property__

public Property(String string1, String string2, boolean aBoolean, int anInt, String string3, ComponentConfiguration aConfiguration, Vector aVector)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Static Constants__

---

__alternativeComponentsInFrameworkKey__
java.lang.String

This constant is intentionally undocumented.

---

__ATTRIBUTE__
int

This constant is intentionally undocumented.

---

__componentConfigurationKey__
java.lang.String

This constant is intentionally undocumented.

---

__CUSTOM_KEY__
int

This constant is intentionally undocumented.

---

__displayNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__hasChildrenKey__
java.lang.String

This constant is intentionally undocumented.

---

__KEYPATH__
int

This constant is intentionally undocumented.

---

__propertyNameKey__
java.lang.String

This constant is intentionally undocumented.

---

__TO_MANY_RELATIONSHIP__
int

This constant is intentionally undocumented.

---

__TO_ONE_RELATIONSHIP__
int

This constant is intentionally undocumented.

---

__typeKey__
java.lang.String

This constant is intentionally undocumented.

---

__valueTypeKey__
java.lang.String

This constant is intentionally undocumented.

---

__visibleKey__
java.lang.String

This constant is intentionally undocumented.

---

__Methods__

__alternativeComponentsInFramework__

public Vector alternativeComponentsInFramework()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__componentConfiguration__

public ComponentConfiguration componentConfiguration()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__copyValuesFrom__

public void copyValuesFrom(Property aProperty)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__decodeWithD2WKeyValueUnarchiver__

public void decodeWithD2WKeyValueUnarchiver(D2WKeyValueUnarchiver unarchiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__displayName__

public String displayName()

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

__hasChildren__

public boolean hasChildren()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isComplete__

public boolean isComplete()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isEOModelProperty__

public boolean isEOModelProperty()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__markIncomplete__

public void markIncomplete()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__propertyName__

public String propertyName()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setAlternativeComponentsInFramework__

public void setAlternativeComponentsInFramework(Vector aVector)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setComponentConfiguration__

public void setComponentConfiguration(ComponentConfiguration aConfiguration)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setDisplayName__

public void setDisplayName(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setHasChildren__

public void setHasChildren(boolean aBoolean)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setPropertyName__

public void setPropertyName(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setType__

public void setType(int anInt)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setVisibility__

public void setVisibility(boolean aBoolean)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__toString__

public String toString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__type__

public int type()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__valueType__

public String valueType()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__visibility__

public boolean visibility()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
