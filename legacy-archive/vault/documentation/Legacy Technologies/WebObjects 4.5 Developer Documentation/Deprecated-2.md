---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Deprecated.html
archived_at: '2026-07-15T08:11:47.846327Z'
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

`- (WOContext *)context`

Deprecated in WebObjects 4.0. Use WOComponent's [context](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Deprecated.html#//apple_ref/allLang/instm/Deprecated/context) method instead.

---

### createSession

`- (WOSession *)createSession`

Deprecated in WebObjects 4.0 Use [createSessionForRequest:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5rxezlborsvgzltonuw63sgn5zfezlrovsxg5b2) instead.

---

### dynamicElementWithName:associations:template:

`- (WODynamicElement *)dynamicElementWithName:(NSString
*)aName
associations:(NSDictionary *)someAssociations
template:(WOElement *)anElement`

Deprecated in WebObjects 4.0. Use [dynamicElementWithName:associations:template:languages:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5shs3tbnvuwgrlmmvwwk3tuk5uxi2comfwwkotbonzw6y3jmf2gs33oom5hizlnobwgc5dfhjwgc3thovqwozlthi) instead.

---

### handleException:

`- (WOResponse *)handleException:(NSException
*)anException`

Deprecated in WebObjects 4.0. Use [handleException:inContext:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsuk6ddmvyhi2lpny5gs3sdn5xhizlyoq5a) instead.

---

### handlePageRestorationError

`- (WOResponse *)handlePageRestorationError`

Deprecated in WebObjects 4.0. Use [handlePageRestorationErrorInContext:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvaylhmvjgk43un5zgc5djn5xek4tsn5zes3sdn5xhizlyoq5a) instead.

---

### handleRequest:

`- (WOResponse *)handleRequest:(WORequest
*)aRequest`

Deprecated in WebObjects 4.0. Use [dispatchRequest:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgs43qmf2gg2csmvyxkzltoq5a) instead.

---

### handleSessionCreationError

`- (WOResponse *)handleSessionCreationError`

Deprecated in WebObjects 4.0. Use [handleSessionCreationErrorInContext:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvgzltonuw63sdojswc5djn5xek4tsn5zes3sdn5xhizlyoq5a) instead.

---

### handleSessionRestorationError

`- (WOResponse *)handleSessionRestorationError`

Deprecated in WebObjects 4.0. Use [handleSessionRestorationErrorInContext:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvgzltonuw63ssmvzxi33smf2gs33oivzhe33sjfxeg33oorsxq5b2) instead.

---

### logToMonitorWithFormat:

`- (void)logToMonitorWithFormat:(NSString
*)aFormat, ...`

Deprecated in WebObjects 4.5. New features in
the Monitor application allow logging of information. The deprecated
API does nothing.

---

### monitorHost

`+ (NSString *)monitorHost`

Deprecated in WebObjects 4.5. Returned the host
on which Monitor is assumed to be running. This value was used
during initialization if [isMonitorEnabled](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jongw63tjorxxerlomfrgyzle) is YES. This was
a cover for the deprecated user default WOMonitorHost. New Monitor
features eliminate the need for this method.

---

### pageWithName:

`- (WOComponent *)pageWithName:(NSString
*)aName`

Deprecated in WebObjects 4.0. Use [pageWithName:forRequest:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygcz3fk5uxi2comfwwkotgn5zfezlrovsxg5b2) instead.

---

### pathForResourceNamed:ofType:

`- (NSString *)pathForResourceNamed:(NSString
*)aName
ofType:(NSString *)anExtension`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [pathForResourceNamed:inFramework:languages:](WOResourceManager-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpobqxi2cgn5zfezltn52xey3fjzqw2zlehjuw4rtsmfwwk53pojvtu3dbnztxkylhmvztu) instead.

---

### requiresWOF35RequestHandling

`- (BOOL)requiresWOF35RequestHandling`

Deprecated in WebObjects 4.5. Apps should be
rewritten so that they don't require WebObjects 3.5 behavior.

---

### requiresWOF35Scripting

`- (BOOL)requiresWOF35Scripting`

Deprecated in WebObjects 4.5. Apps should be
rewritten so that they don't require WebObjects 3.5 behavior.

---

### requiresWOF35TemplateParser

`- (BOOL)requiresWOF35TemplateParser`

Deprecated in WebObjects 4.5. Apps should be
rewritten so that they don't require WebObjects 3.5 behavior.

---

### restorePageForContextID:

`- (WOComponent *)restorePageForContextID:(NSString
*)contextID`

Deprecated in WebObjects 4.0. Use WOSession's [restorePageForContextID:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxxezltorxxezkqmftwkrtpojbw63tumv4hiskehi) instead.

---

### restoreSession

`- (WOSession *)restoreSession`

Deprecated in WebObjects 4.0. Use [restoreSessionWithID:inContext:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk43un5zgku3fonzws33ok5uxi2cjiq5gs3sdn5xhizlyoq5a) instead.

---

### savePage:

`- (void)savePage:(WOComponent
*)aPage`

Deprecated in WebObjects 4.0. Use WOSession's
implementation of [savePage:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxxgylwmvigcz3fhi) instead.

---

### saveSession:

`- (void)saveSession:(WOSession
*)aSession`

Deprecated in WebObjects 4.0. Use [saveSessionForContext:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwc5tfknsxg43jn5xem33sinxw45dfpb2du) instead.

---

### session

`- (WOSession *)session`

Deprecated in WebObjects 4.0 Use WOComponent's [session](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Deprecated.html#//apple_ref/allLang/instm/Deprecated/session) method instead.

---

### setMonitorHost:

`+ (void)setMonitorHost:(NSString
*)aHostName`

Deprecated in WebObjects 4.5. This was an accessor
to set the monitorHost. New Monitor features eliminate the need
for this method.

---

### stringForKey:inTableNamed:withDefaultValue:

`- (NSString *)stringForKey:(NSString
*)aKey
inTableNamed:(NSString *)aTableName
withDefaultValue:(NSString *)aDefaultValue`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [stringForKey:inTableNamed:withDefaultValue:inFramework:languages:](WOResourceManager-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpon2he2lom5dg64slmv4tu2lokrqwe3dfjzqw2zlehj3ws5diirswmylvnr2fmylmovstu2loizzgc3lfo5xxe2z2nrqw4z3vmftwk4z2) instead.

---

### urlForResourceNamed:ofType:

`- (NSString *)urlForResourceNamed:(NSString
*)aName
ofType:(NSString *)anExtension`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [urlForResourceNamed:inFramework:languages:request:](WOResourceManager-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpovzgyrtpojjgk43povzggzkomfwwkzb2nfxem4tbnvsxo33snm5gyylom52wcz3fom5hezlrovsxg5b2) instead.

---

## WOAssociation

### setValue:

`- (void)setValue:(id)aValue`

Deprecated in WebObjects 4.0. Use [setValue:inComponent:](WOAssociation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2nfxeg33nobxw4zlooq5a) instead.

---

### value

`- (id)value`

Deprecated in WebObjects 4.0. Use [valueInComponent:](WOAssociation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bonzw6y3jmf2gs33of53gc3dvmvew4q3pnvyg63tfnz2du) instead.

---

## WOComponent

### pathForResourceNamed:ofType:

`- (NSString *)pathForResourceNamed:(NSString
*)aName
ofType:(NSString *)anExtension`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [pathForResourceNamed:inFramework:languages:](WOResourceManager-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpobqxi2cgn5zfezltn52xey3fjzqw2zlehjuw4rtsmfwwk53pojvtu3dbnztxkylhmvztu) instead.

---

### requiresWOF35RequestHandling

`- (BOOL)requiresWOF35RequestHandling`

Deprecated in WebObjects 4.5. Apps should be
rewritten so that they don't require WebObjects 3.5 behavior.

---

### stringForKey:inTableNamed:withDefaultValue:

`- (NSString *)stringForKey:(NSString
*)aKey
inTableNamed:(NSString *)aTableName
withDefaultValue:(NSString *)aDefaultValue`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [stringForKey:inTableNamed:withDefaultValue:inFramework:languages:](WOResourceManager-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpon2he2lom5dg64slmv4tu2lokrqwe3dfjzqw2zlehj3ws5diirswmylvnr2fmylmovstu2loizzgc3lfo5xxe2z2nrqw4z3vmftwk4z2) instead.

---

### templateWithHTMLString:declarationString:

`+ (WOElement *)templateWithHTMLString:(NSString
*)anHTMLString
declarationString:(NSString *)aDeclarationString`

Deprecated in WebObjects 4.0. Use templateWithHTMLString:declarationString:languages: instead.

---

### urlForResourceNamed:ofType:

`- (NSString *)urlForResourceNamed:(NSString
*)aResourceName
ofType:(NSString *)anExtension`

Deprecated in WebObjects 4.0. Use WOResourceManager's
implementation of [urlForResourceNamed:inFramework:languages:request:](WOResourceManager-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpovzgyrtpojjgk43povzggzkomfwwkzb2nfxem4tbnvsxo33snm5gyylom52wcz3fom5hezlrovsxg5b2) instead.

---

## WOContext

### application

`- (WOApplication *)application`

Deprecated in WebObjects 4.0. Use WOApplication's [application](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bobygy2ldmf2gs33o) method instead.

---

### isDistributionEnabled

`- (BOOL)isDistributionEnabled`

Deprecated in WebObjects 4.0. Use WOSession's
implementation of [isDistributionEnabled](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxws42enfzxi4tjmj2xi2lpnzcw4ylcnrswi) instead.

---

### setDistributionEnabled:

`- (void)setDistributionEnabled:(BOOL)flag`

Deprecated in WebObjects 4.0. Use WOSession's
implementation of [setDistributionEnabled:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxxgzluiruxg5dsnfrhk5djn5xek3tbmjwgkzb2) instead.

---

### url

`- (NSString *)url`

Deprecated in WebObjects 4.0. Use [componentActionURL](WOContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33nobxw4zloorawg5djn5xfkusm) instead.

---

### urlSessionPrefix

`- (NSString *)urlSessionPrefix`

Deprecated in WebObjects 4.0. There is no alternative
since the URL session prefix doesn't mean anything in the current
URL format.

---

## WODisplayGroup

### setSortOrdering:

`- (void)setSortOrdering:(NSArray
*)keySortOrderArray`

Deprecated in WebObjects 4.0. Renamed to [setSortOrderings:](WODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknxxe5cpojsgk4tjnztxgoq).

---

### sortOrdering

`- (NSArray *)sortOrdering`

Deprecated in WebObjects 4.0. Renamed to [sortOrderings](WODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxg33sorhxezdfojuw4z3t).

---

## WORequest

### applicationHost

`- (NSString *)applicationHost`

Deprecated in WebObjects 4.0. See NSProcessInfo
or NSHost.

---

### contextID

`- (NSString *)contextID`

Deprecated in WebObjects 4.0. Use WOContext's
implementation of [contextID](WOContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33oorsxq5cjiq) instead.

---

### pageName

`- (NSString *)pageName`

Deprecated in WebObjects 4.0. Use WOComponent's [name](WOComponent-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3omfwwk) method instead.

---

### senderID

`- (NSString *)senderID`

Deprecated in WebObjects 4.0. Use WOContext's
implementation of [senderID](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Deprecated.html#//apple_ref/allLang/instm/Deprecated/senderID) instead.

---

## WOResourceManager

### pathForResourceNamed:inFramework:

`- (NSString *)pathForResourceNamed:(NSString
*)aResourceName
inFramework:(NSString *)aFrameworkName`

Deprecated in WebObjects 4.0. Use [pathForResourceNamed:inFramework:languages:](WOResourceManager-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpobqxi2cgn5zfezltn52xey3fjzqw2zlehjuw4rtsmfwwk53pojvtu3dbnztxkylhmvztu) instead.

---

### urlForResourceNamed:inFramework:

`- (NSString *)urlForResourceNamed:(NSString
*)aResourceName
inFramework:(NSString *)aFrameworkName`

Deprecated in WebObjects 4.0. Use [urlForResourceNamed:inFramework:languages:request:](WOResourceManager-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpovzgyrtpojjgk43povzggzkomfwwkzb2nfxem4tbnvsxo33snm5gyylom52wcz3fom5hezlrovsxg5b2) instead.

---

## WOSession

### application

`- (WOApplication*)application`

Deprecated in WebObjects 4.0. Use WOApplication's [application](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bobygy2ldmf2gs33o) method instead.

---

## WOSessionStore

### restoreSession

`- (WOSession*)restoreSession`

Deprecated in WebObjects 4.0. Use [restoreSessionWithID:request:](WOSessionStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnzjxi33smuxxezltorxxezktmvzxg2lpnzlws5dijfcdu4tfof2wk43uhi) instead.

---

### saveSession:

`- (void)saveSession:(WOSession
*)aSession`

Deprecated in WebObjects 4.0. Use [saveSessionForContext:](WOSessionStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnzjxi33smuxxgylwmvjwk43tnfxw4rtpojbw63tumv4hioq) instead.

---

## WOStatisticsStore

### validateLogin:

`- (BOOL)validateLogin:(NSString
*)string`

Deprecated in WebObjects 4.0. Use [validateLogin:forSession:](WOStatisticsStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpozqwy2lemf2gktdpm5uw4otgn5zfgzltonuw63r2) instead.

---

[![Table of Contents](attachments/images/up.gif)](WebObjectsTOC.md)
