---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/PageConfiguration.html
archived_at: '2026-07-15T08:11:30.854209Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__PageConfiguration__

__Package__:
com.apple.client.directtoweb.common

__Inherits from__:[ComponentConfiguration](ComponentConfiguration.md)__Implements__:

- [D2WKeyValueArchiving](D2WKeyValueArchiving.md)

---

__Class Description__

---

This class is used internally by other classes in WebObjects and should be considered private. It should not be used, subclassed, or replaced.

__Method Types__

---

Constructors

- [public PageConfiguration()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5igcz3finxw4ztjm52xeylunfxw4l2qmftwkq3pnztgsz3vojqxi2lpnyxsqki)

---

Static Constants

- [actionsKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbqwozkdn5xgm2lhovzgc5djn5xc6yldoruw63ttjnsxs)
- [alternativePagesInFrameworkKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbqwozkdn5xgm2lhovzgc5djn5xc6ylmorsxe3tboruxmzkqmftwk42jnzdheylnmv3w64tljnsxs)
- [backgroundColorForTableKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbqwozkdn5xgm2lhovzgc5djn5xc6ytbmnvwo4tpovxgiq3pnrxxertpojkgcytmmvfwk6i)
- [frameKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbqwozkdn5xgm2lhovzgc5djn5xc6ztsmfwwks3fpe)
- [staticPageAvailableInRuntimeKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbqwozkdn5xgm2lhovzgc5djn5xc643umf2gsy2qmftwkqlwmfuwyylcnrsus3ssovxhi2lnmvfwk6i)
- [staticPageKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbqwozkdn5xgm2lhovzgc5djn5xc643umf2gsy2qmftwks3fpe)
- [titleKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpkbqwozkdn5xgm2lhovzgc5djn5xc65djorwgks3fpe)

---

Private Methods

- [actions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5qwg5djn5xhgl2wmvrxi33sf4ucs)
- [alternativePagesInFramework](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5qwy5dfojxgc5djozsvaylhmvzus3sgojqw2zlxn5zgwl2wmvrxi33sf4ucs)
- [backgroundColorForTable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5rgcy3lm5zg65lomrbw63dpojdg64sumfrgyzjpkn2he2lom4xsqki)
- [frame](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5theylnmuxvg5dsnfxgolzife)
- [setActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5zwk5cbmn2gs33oomxxm33jmqxsqvtfmn2g64rj)
- [setAlternativePagesInFramework](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5zwk5cbnr2gk4tomf2gs5tfkbqwozltjfxem4tbnvsxo33snmxxm33jmqxsqvtfmn2g64rj)
- [setBackgroundColorForTable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5zwk5ccmfrwwz3sn52w4zcdn5wg64sgn5zfiylcnrss65tpnfsc6kctorzgs3thfe)
- [setFrame](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5zwk5cgojqw2zjpozxwszbpfbjxi4tjnztss)
- [setStaticPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5zwk5ctorqxi2ldkbqwozjpozxwszbpfbrg633mmvqw4ki)
- [setStaticPageAvailableInRuntime](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5zwk5ctorqxi2ldkbqwozkbozqws3dbmjwgkslokj2w45djnvss65tpnfsc6kdcn5xwyzlbnyuq)
- [setTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5zwk5cunf2gyzjpozxwszbpfbjxi4tjnztss)
- [staticPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5zxiylunfrvaylhmuxwe33pnrswc3rpfauq)
- [staticPageAvailableInRuntime](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of5zxiylunfrvaylhmvaxmyljnrqwe3dfjfxfe5looruw2zjpmjxw63dfmfxc6kbj)
- [title](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6udbm5sug33omzuwo5lsmf2gs33of52gs5dmmuxvg5dsnfxgolzife)

---

__Constructors__

---

__com.apple.client.directtoweb.common.PageConfiguration__

public PageConfiguration()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__Static Constants__

---

__actionsKey__
java.lang.String

This constant is intentionally undocumented.

---

__alternativePagesInFrameworkKey__
java.lang.String

This constant is intentionally undocumented.

---

__backgroundColorForTableKey__
java.lang.String

This constant is intentionally undocumented.

---

__frameKey__
java.lang.String

This constant is intentionally undocumented.

---

__staticPageAvailableInRuntimeKey__
java.lang.String

This constant is intentionally undocumented.

---

__staticPageKey__
java.lang.String

This constant is intentionally undocumented.

---

__titleKey__
java.lang.String

This constant is intentionally undocumented.

---

__Methods__

__actions__

public Vector actions()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__alternativePagesInFramework__

public Vector alternativePagesInFramework()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__backgroundColorForTable__

public String backgroundColorForTable()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__frame__

public String frame()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setActions__

public void setActions(Vector aVector)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setAlternativePagesInFramework__

public void setAlternativePagesInFramework(Vector aVector)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setBackgroundColorForTable__

public void setBackgroundColorForTable(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setFrame__

public void setFrame(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setStaticPage__

public void setStaticPage(boolean aBoolean)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setStaticPageAvailableInRuntime__

public void setStaticPageAvailableInRuntime(boolean aBoolean)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setTitle__

public void setTitle(String aString)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__staticPage__

public boolean staticPage()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__staticPageAvailableInRuntime__

public boolean staticPageAvailableInRuntime()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__title__

public String title()

This method is intentionally undocumented. You should never have to invoke or customize it.

---
