---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Deprecated.html
archived_at: '2026-07-15T08:11:47.223115Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](WebObjectsTOC.md) 

## Deprecated API

This file enumerates those WebObjects Framework classes and
methods that have been deprecated and should no longer be used.
Wherever possible, notes have been included to indicate what API
should be used in place of the deprecated class or method.

## WOApplication

### context

`public WOContext context()`

Deprecated in WebObjects 4.0. Use WOComponent's [context](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Deprecated.html#//apple_ref/allLang/instm/Deprecated/context) method instead.

---

### createSession

`public WOSession createSession()`

Deprecated in WebObjects 4.0 Use [createSessionForRequest](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwg4tfmf2gku3fonzws33oizxxeutfof2wk43u) instead.

---

### handleException

`public WOResponse handleException(Throwable anException)`

Deprecated in WebObjects 4.0. Use [handleException](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkrlymnsxa5djn5xa) instead.

---

### handlePageRestorationError

`public WOResponse handlePageRestorationError()`

Deprecated in WebObjects 4.0. Use [handlePageRestorationErrorInContext](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkudbm5svezltorxxeylunfxw4rlsojxxesloinxw45dfpb2a) instead.

---

### handleRequest

`public WOResponse handleRequest(WORequest aRequest)`

Deprecated in WebObjects 4.0. Use [dispatchRequest](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwi2ltobqxiy3ikjsxc5lfon2a) instead.

---

### handleSessionCreationError

`public WOResponse handleSessionCreationError()`

Deprecated in WebObjects 4.0. Use [handleSessionCreationErrorInContext](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgku3fonzws33oinzgkylunfxw4rlsojxxesloinxw45dfpb2a) instead.

---

### handleSessionRestorationError

`public WOResponse handleSessionRestorationError()`

Deprecated in WebObjects 4.0. Use [handleSessionRestorationErrorInContext](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgku3fonzws33okjsxg5dpojqxi2lpnzcxe4tpojew4q3pnz2gk6du) instead.

---

### logToMonitorString

`public static void logToMonitorString(String aFormat)`

Deprecated in WebObjects 4.5. New features in
the Monitor application allow logging of information. The deprecated
API does nothing.

---

### pageWithName

`public WOComponent pageWithName(String aName)`

Deprecated in WebObjects 4.0. Use [pageWithName](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxaylhmvlws5dijzqw2zi) instead.

---

### pathForResourceNamed

`public String pathForResourceNamed(
String aName,
String anExtension)`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [pathForResourceNamed](WOResourceManager.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5ygc5diizxxeutfonxxk4tdmvhgc3lfmq) instead.

---

### requiresWOF35RequestHandling

`public boolean requiresWOF35RequestHandling()`

Deprecated in WebObjects 4.5. Apps should be
rewritten so that they don't require WebObjects 3.5 behavior.

---

### requiresWOF35TemplateParser

`public boolean requiresWOF35TemplateParser()`

Deprecated in WebObjects 4.5. Apps should be
rewritten so that they don't require WebObjects 3.5 behavior.

---

### restorePageForContextID

`public WOComponent restorePageForContextID(String contextID)`

Deprecated in WebObjects 4.0. Use WOSession's [restorePageForContextID](WOSession.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc64tfon2g64tfkbqwozkgn5zeg33oorsxq5cjiq) instead.

---

### restoreSession

`public WOSession restoreSession()`

Deprecated in WebObjects 4.0. Use [restoreSessionWithID](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezltorxxezktmvzxg2lpnzlws5dijfca) instead.

---

### savePage

`public void savePage(WOComponent aPage)`

Deprecated in WebObjects 4.0. Use WOSession's
implementation of [savePage](WOSession.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643bozsvaylhmu) instead.

---

### saveSession

`public void saveSession(WOSession aSession)`

Deprecated in WebObjects 4.0. Use [saveSessionForContext](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgylwmvjwk43tnfxw4rtpojbw63tumv4hi) instead.

---

### session

`public WOSession session()`

Deprecated in WebObjects 4.0 Use WOComponent's [session](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Deprecated.html#//apple_ref/allLang/instm/Deprecated/session) method instead.

---

### stringForKeyInTable

`public String stringForKeyInTable(
String aKey,
String aTableName,
String aDefaultValue)`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [stringForKey](WOResourceManager.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5zxi4tjnztum33sjnsxs) instead.

---

### urlForResourceNamed

`public String urlForResourceNamed(
String aName,
String anExtension)`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [urlForResourceNamed](WOResourceManager.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf52xe3cgn5zfezltn52xey3fjzqw2zle) instead.

---

## WOAssociation

### setValue

`public void setValue(Object aValue)`

Deprecated in WebObjects 4.0. Use [setValue](WOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxxgzlukzqwy5lf) instead.

---

### value

`public Object value()`

Deprecated in WebObjects 4.0. Use [valueInComponent](WOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxxmylmovsus3sdn5wxa33omvxhi) instead.

---

## WOComponent

### pathForResourceNamed

`public String pathForResourceNamed(
String aName,
String anExtension)`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [pathForResourceNamed](WOResourceManager.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5ygc5diizxxeutfonxxk4tdmvhgc3lfmq) instead.

---

### stringForKeyInTable

`public String stringForKeyInTable(
String aKey,
String aTableName,
String aDefaultValue)`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [stringForKey](WOResourceManager.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5zxi4tjnztum33sjnsxs) instead.

---

### urlForResourceNamed

`public String urlForResourceNamed(
String aResourceName,
String anExtension)`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [urlForResourceNamed](WOResourceManager.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf52xe3cgn5zfezltn52xey3fjzqw2zle) instead.

---

## WOContext

### application

`public WOApplication application()`

Deprecated in WebObjects 4.0. Use WOApplication's [application](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qlqobwgsy3boruw63rpmfyha3djmnqxi2lpny) method instead.

---

### isDistributionEnabled

`public boolean isDistributionEnabled()`

Deprecated in WebObjects 4.0. Use WOSession's
implementation of [isDistributionEnabled](WOSession.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62ltiruxg5dsnfrhk5djn5xek3tbmjwgkza) instead.

---

### setDistributionEnabled

`public void setDistributionEnabled(boolean flag)`

Deprecated in WebObjects 4.0. Use WOSession's
implementation of [setDistributionEnabled](WOSession.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forcgs43uojuwe5lunfxw4rlomfrgyzle) instead.

---

### url

`public String url()`

Deprecated in WebObjects 4.0. Use [componentActionURL](WOContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnvyg63tfnz2ecy3unfxw4vksjq) instead.

---

### urlSessionPrefix

`public String urlSessionPrefix()`

Deprecated in WebObjects 4.0. There is no alternative
since the URL session prefix doesn't mean anything in the current
URL format.

---

## WODisplayGroup

### setSortOrdering

`public void setSortOrdering(NSArray keySortOrderArray)`

Deprecated in WebObjects 4.0. Renamed to [setSortOrderings](WODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjw64tuj5zgizlsnfxgo4y).

---

### sortOrdering

`public NSArray sortOrdering()`

Deprecated in WebObjects 4.0. Renamed to [sortOrderings](WODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643poj2e64temvzgs3thom).

---

## WORequest

### applicationHost

`public String applicationHost()`

Deprecated in WebObjects 4.0. See java.net.InetAddress.

---

### contextID

`public String contextID()`

Deprecated in WebObjects 4.0. Use WOContext's
implementation of [contextID](WOContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnz2gk6dujfca) instead.

---

### pageName

`public String pageName()`

Deprecated in WebObjects 4.0. Use WOComponent's [name](WOComponent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnzqw2zi) method instead.

---

### senderID

`public String senderID()`

Deprecated in WebObjects 4.0. Use WOContext's
implementation of [senderID](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Deprecated.html#//apple_ref/allLang/instm/Deprecated/senderID) instead.

---

## WOResourceManager

### pathForResourceNamedInFramework

`public String pathForResourceNamedInFramework(
String aResourceName,
String aFrameworkName)`

Deprecated in WebObjects 4.0. Use [pathForResourceNamed](WOResourceManager.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5ygc5diizxxeutfonxxk4tdmvhgc3lfmq) instead.

---

### urlForResourceNamedInFramework

`public String urlForResourceNamedInFramework(
String aResourceName,
String aFrameworkName)`

Deprecated in WebObjects 4.0. Use [urlForResourceNamed](WOResourceManager.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf52xe3cgn5zfezltn52xey3fjzqw2zle) instead.

---

## WOSession

### application

`public WOApplication application()`

Deprecated in WebObjects 4.0. Use WOApplication's [application](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qlqobwgsy3boruw63rpmfyha3djmnqxi2lpny) method instead.

---

## WOSessionStore

### restoreSession

`public WOSession restoreSession()`

Deprecated in WebObjects 4.0. Use [restoreSessionWithID](WOSessionStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss64tfon2g64tfknsxg43jn5xfo2lunbeui) instead.

---

### saveSession

`public void saveSession(WOSession aSession)`

Deprecated in WebObjects 4.0. Use [saveSessionForContext](WOSessionStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss643bozsvgzltonuw63sgn5zeg33oorsxq5a) instead.

---

## WOStatisticsStore

### validateLogin

`public boolean validateLogin(String aString)`

Deprecated in WebObjects 4.0. Use [validateLogin](WOStatisticsStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff53gc3djmrqxizkmn5tws3q) instead.

---

[![Table of Contents](attachments/images/up.gif)](WebObjectsTOC.md)
