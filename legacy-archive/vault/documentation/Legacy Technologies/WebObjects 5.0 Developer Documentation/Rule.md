---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/Rule.html
archived_at: '2026-07-15T08:12:45.417667Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__Rule__

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

- [public Rule(int anInt, EOQualifierEvaluation aQualifier, Assignment assignment)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6utvnrss6utvnrss6kdjnz2cyrkpkf2wc3djmzuwk4sfozqwy5lboruw63rmifzxg2lhnzwwk3tufe)
- [public Rule(EOKeyValueUnarchiver unarchiver)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6utvnrss6utvnrss6kcfj5fwk6kwmfwhkzkvnzqxey3inf3gk4rj)
- [public Rule()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6utvnrss6utvnrss6kbj)

---

Static Constants

- [authorKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjpmf2xi2dpojfwk6i)
- [D2W](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjpiqzfo)
- [lhsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjpnruhgs3fpe)
- [rhsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjpojuhgs3fpe)
- [traceRuleFiring](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjporzgcy3fkj2wyzkgnfzgs3th)
- [traceRuleFiringAsString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjporzgcy3fkj2wyzkgnfzgs3thifzvg5dsnfxgo)
- [traceRuleFiringKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjporzgcy3fkj2wyzkgnfzgs3thjnsxs)
- [traceRuleModifications](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjporzgcy3fkj2wyzknn5sgsztjmnqxi2lpnzzq)
- [traceRuleModificationsAsString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjporzgcy3fkj2wyzknn5sgsztjmnqxi2lpnzzuc42torzgs3th)
- [traceRuleModificationsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjporzgcy3fkj2wyzknn5sgsztjmnqxi2lpnzzuwzlz)
- [WEB_ASSISTANT](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjpk5cuex2bknjusu2uifhfi)
- [WEB_ASSISTANT_PAGE_AVAILABLE](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkj2wyzjpk5cuex2bknjusu2uifhfix2qifdukx2bkzaustcbijgek)

---

Private Methods

- [author](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6ylvorug64rpnfxhilzife)
- [canFireInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6y3bnzdgs4tfjfxeg33oorsxq5bpmjxw63dfmfxc6kcegjlug33oorsxq5bj)
- [compareRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6y3pnvygc4tfkj2wyzltf5uw45bpfbjhk3dffe)
- [createAssignment](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6y3smvqxizkbonzwsz3onvsw45bpifzxg2lhnzwwk3tuf4ufg5dsnfxgolctorzgs3thfe)
- [dataTypesInvolved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6zdborqvi6lqmvzus3twn5whmzlef5lgky3un5zc6kbj)
- [dynamicPagesInvolved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6zdznzqw22ldkbqwozltjfxhm33mozswil2wmvrxi33sf4ucs)
- [fire](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6ztjojss6t3cnjswg5bpfbcdev2dn5xhizlyoquq)
- [firstDynamicPageNameInvolved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6ztjojzxirdznzqw22ldkbqwozkomfwwksloozxwy5tfmqxvg5dsnfxgolzife)
- [firstEntityInvolved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6ztjojzxirlooruxi6kjnz3g63dwmvsc6u3uojuw4zzpfauq)
- [firstPropertyKeyInvolved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6ztjojzxiudsn5ygk4tupffwk6kjnz3g63dwmvsc6u3uojuw4zzpfauq)
- [firstTaskInvolved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss6ztjojzxivdbonvus3twn5whmzlef5jxi4tjnzts6kbj)
- [hasSameSettingsAs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss62dbonjwc3lfknsxi5djnztxgqltf5rg633mmvqw4lziknsxi5djnztxgldcn5xwyzlbnyuq)
- [isEntityPermissionRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss62ltivxhi2lupfigk4tnnfzxg2lpnzjhk3dff5rg633mmvqw4lzife)
- [isEntityRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss62ltivxhi2lupfjhk3dff5rg633mmvqw4lzife)
- [isLookRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss62ltjrxw622sovwgkl3cn5xwyzlbnyxsqki)
- [isStartupRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss62ltkn2gc4tuovyfe5lmmuxwe33pnrswc3rpfauq)
- [isTaskRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss62ltkrqxg22sovwgkl3cn5xwyzlbnyxsqki)
- [lhs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss63diomxukt2rovqwy2lgnfsxerlwmfwhkylunfxw4lzife)
- [priority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss64dsnfxxe2lupexws3tuf4ucs)
- [rhs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss64tiomxuc43tnftw43lfnz2c6kbj)
- [rhsKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss64tionfwk6kqmf2gql2torzgs3thf4ucs)
- [rhsKeyPathHash](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss64tionfwk6kqmf2gqsdbonuc62looqxsqki)
- [setLhs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss643forggq4zpozxwszbpfbcu6ulvmfwgsztjmvzek5tbnr2wc5djn5xcs)
- [setRhs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss643forjgq4zpozxwszbpfbaxg43jm5xg2zlooquq)
- [tasksInvolved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss65dbonvxgsloozxwy5tfmqxvmzldorxxelzife)
- [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6utvnrss65dpkn2he2lom4xvg5dsnfxgolzife)
- [traceRuleFiringEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jhk3dff52heyldmvjhk3dfizuxe2lom5cw4ylcnrswil3cn5xwyzlbnyxsqki)
- [traceRuleModificationsEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5jhk3dff52heyldmvjhk3dfjvxwi2lgnfrwc5djn5xhgrlomfrgyzlef5rg633mmvqw4lzife)

---

__Constructors__

---

__Rule__

public Rule(int anInt, EOQualifierEvaluation aQualifier, Assignment assignment)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Rule__

public Rule(EOKeyValueUnarchiver unarchiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Rule__

public Rule()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Static Constants__

---

__authorKey__
java.lang.String

This constant is intentionally undocumented.

---

__D2W__
int

This constant is intentionally undocumented.

---

__lhsKey__
java.lang.String

This constant is intentionally undocumented.

---

__rhsKey__
java.lang.String

This constant is intentionally undocumented.

---

__traceRuleFiring__
boolean

This constant is intentionally undocumented.

---

__traceRuleFiringAsString__
java.lang.String

This constant is intentionally undocumented.

---

__traceRuleFiringKey__
java.lang.String

This constant is intentionally undocumented.

---

__traceRuleModifications__
boolean

This constant is intentionally undocumented.

---

__traceRuleModificationsAsString__
java.lang.String

This constant is intentionally undocumented.

---

__traceRuleModificationsKey__
java.lang.String

This constant is intentionally undocumented.

---

__WEB_ASSISTANT__
int

This constant is intentionally undocumented.

---

__WEB_ASSISTANT_PAGE_AVAILABLE__
int

This constant is intentionally undocumented.

---

__Methods__

__author__

public int author()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__canFireInContext__

public boolean canFireInContext(D2WContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__compareRules__

public int compareRules(Rule aRule)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__createAssignment__

public Assignment createAssignment(String string1, String string2)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__dataTypesInvolved__

public Vector dataTypesInvolved()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__dynamicPagesInvolved__

public Vector dynamicPagesInvolved()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__fire__

public Object fire(D2WContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__firstDynamicPageNameInvolved__

public String firstDynamicPageNameInvolved()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__firstEntityInvolved__

public String firstEntityInvolved()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__firstPropertyKeyInvolved__

public String firstPropertyKeyInvolved()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__firstTaskInvolved__

public String firstTaskInvolved()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__hasSameSettingsAs__

public boolean hasSameSettingsAs(Settings settings, boolean aBoolean)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isEntityPermissionRule__

public boolean isEntityPermissionRule()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isEntityRule__

public boolean isEntityRule()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isLookRule__

public boolean isLookRule()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isStartupRule__

public boolean isStartupRule()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__isTaskRule__

public boolean isTaskRule()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__lhs__

public EOQualifierEvaluation lhs()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__priority__

public int priority()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__rhs__

public final Assignment rhs()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__rhsKeyPath__

public final String rhsKeyPath()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__rhsKeyPathHash__

public int rhsKeyPathHash()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setLhs__

public void setLhs(EOQualifierEvaluation newValue)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setRhs__

public void setRhs(Assignment assignment)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__tasksInvolved__

public Vector tasksInvolved()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__toString__

public String toString()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__traceRuleFiringEnabled__

static public boolean traceRuleFiringEnabled()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__traceRuleModificationsEnabled__

static public boolean traceRuleModificationsEnabled()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
