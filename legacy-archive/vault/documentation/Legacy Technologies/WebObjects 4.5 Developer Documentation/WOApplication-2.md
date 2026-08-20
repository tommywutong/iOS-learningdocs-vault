---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOApplication.html
archived_at: '2026-07-15T08:11:47.343159Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOApplication

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOApplication.h

---

## Class Description

---

The primary role of the WOApplication class is to coordinate
the handling of HTTP requests. Each application must have exactly
one WOApplication object (or, simply, application object). The application
object receives client requests from an HTTP server adaptor, manages
the processing that generates a response, and returns that response-typically
an object representing a web page-to the adaptor. The adaptor,
in turn, forwards the response in a suitable form to the HTTP server
that originated the request.

In handling requests, an application object creates and manages
one or more sessions; a session (represented by a WOSession object)
dedicates resources to a period of access by a single user and stores
persistent state during that period. Conceptually, each cycle of
the request-response loop (or transaction) takes place within a
session.

Besides acting as a facilitator between the adaptor and the
rest of the application during request handling, WOApplication performs
many secondary functions. It returns pages based on component name,
caches page instances and component definitions, provides some facilities
for error handling and script debugging, coordinates the different
levels of multi-threaded execution, and furnishes a variety of data.

Typical deployment schemes balance the processing load by
having multiple application instances per server adaptor. A single
application, in turn, can interact with multiple adaptors; for example,
an application can simultaneously communicate with secure-socket
and Distributed Object adaptors as well as HTTP adaptors.

You can instantiate ready-made application objects from the
WOApplication class or you can obtain the application object from
a custom subclass of WOApplication. Custom WOApplication subclasses
are common in WebObjects applications since there is often a need
to override the [awake](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxoyllmu), [sleep](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwyzlfoa), [init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uw42lu), and request-handling methods.
Compiled WOApplication subclasses can take any name, but if the
name is anything other than "Application" you must implement
your own __main__ function to instantiate the application
object from this class. However, if the class name is "Application,"
you don't need to modify __main__. In scripted
applications, the code in the __Application.wos__ file
becomes the implementation logic of a WOApplication subclass automatically
created at run time; the application object is instantiated from
this subclass.

## Adopted Protocols

---

> NSLocking: - lock
> : - unlock

## Method Types

---

> **Creating**
> : [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uw42lu)
> : [+ application](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bobygy2ldmf2gs33o)
>
> **Obtaining attributes**
> : [- adaptorsDispatchRequestsConcurrently](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwiylqorxxe42enfzxaylumnufezlrovsxg5dtinxw4y3vojzgk3tunr4q)
> : [- allowsConcurrentRequestHandling](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwy3dpo5zug33omn2xe4tfnz2fezlrovsxg5cimfxgi3djnztq)
> : [- isConcurrentRequestHandlingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgq3pnzrxk4tsmvxhiutfof2wk43ujbqw4zdmnfxgorlomfrgyzle)
> : [- baseURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5rgc43fkvjey)
> : [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5xgc3lf)
> : [- number](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5xhk3lcmvza)
> : [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygc5di)
>
> **Locking**
> : [- lock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5wg6y3l)
> : [- unlock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52w43dpmnvq)
> : [- lockRequestHandling](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5wg6y3lkjsxc5lfon2eqylomrwgs3th)
> : [- unlockRequestHandling](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52w43dpmnvvezlrovsxg5cimfxgi3djnztq)
>
> **Managing adaptors**
> : [- adaptorWithName:arguments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwiylqorxxev3jorue4ylnmu5gc4thovwwk3tuom5a)
> : [- adaptors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwiylqorxxe4y)
>
> **Managing cache**
> : [- setCachingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cdmfrwq2lom5cw4ylcnrswioq)
> : [- isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgq3bmnugs3thivxgcytmmvsa)
>
> **Managing sessions**
> : [- setSessionStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5ctmvzxg2lpnzjxi33smu5a)
> : [- sessionStore](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk43tnfxw4u3un5zgk)
> : [- saveSessionForContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwc5tfknsxg43jn5xem33sinxw45dfpb2du)
> : [- restoreSessionWithID:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk43un5zgku3fonzws33ok5uxi2cjiq5gs3sdn5xhizlyoq5a)
> : [- createSessionForRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5rxezlborsvgzltonuw63sgn5zfezlrovsxg5b2)
>
> **Managing pages**
> : [- setPageCacheSize:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cqmftwkq3bmnugku3jpjstu)
> : [- pageCacheSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygcz3finqwg2dfknuxuzi)
> : [- permanentPageCacheSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygk4tnmfxgk3tukbqwozkdmfrwqzktnf5gk)
> : [- setPermanentPageCacheSize:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cqmvzg2ylomvxhiudbm5sugyldnbsvg2l2mu5a)
> : [- setPageRefreshOnBacktrackEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cqmftwkutfmzzgk43ij5xeeyldnn2heyldnncw4ylcnrswioq)
> : [- isPageRefreshOnBacktrackEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgudbm5svezlgojsxg2cpnzbgcy3lorzgcy3livxgcytmmvsa)
> : [- pageWithName:forRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygcz3fk5uxi2comfwwkotgn5zfezlrovsxg5b2)
> : [- pageWithName:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygcz3fk5uxi2comfwwkotjnzbw63tumv4hioq)
>
> **Creating elements**
> : [- dynamicElementWithName:associations:template:languages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5shs3tbnvuwgrlmmvwwk3tuk5uxi2comfwwkotbonzw6y3jmf2gs33oom5hizlnobwgc5dfhjwgc3thovqwozlthi)
>
> **Running**
> : [- runLoop](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zhk3smn5xxa)
> : [- run](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zhk3q)
> : [- setTimeOut:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cunfwwkt3voq5a)
> : [- timeOut](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gs3lfj52xi)
> : [- defaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkztbovwhiutfof2wk43ujbqw4zdmmvza)
> : [- terminate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gk4tnnfxgc5df)
> : [- terminateAfterTimeInterval:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gk4tnnfxgc5dfifthizlskruw2zkjnz2gk4twmfwdu)
>
> **Handling requests**
> : [- appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxa4dfnzsfi32smvzxa33oonstu2loinxw45dfpb2du)
> : [- awake](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxoyllmu)
> : [- createContextForRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5rxezlborsug33oorsxq5cgn5zfezlrovsxg5b2)
> : [- createSessionForRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5rxezlborsvgzltonuw63sgn5zfezlrovsxg5b2)
> : [- defaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkztbovwhiutfof2wk43ujbqw4zdmmvza)
> : [- defaultRequestHandlerClassName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkztbovwhiutfof2wk43ujbqw4zdmmvzeg3dbonzu4ylnmu)
> : [- dispatchRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgs43qmf2gg2csmvyxkzltoq5a)
> : [- handlerForRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsxertpojjgk4lvmvzxioq)
> : [- invokeActionForRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uw45tpnnsucy3unfxw4rtpojjgk4lvmvzxiotjnzbw63tumv4hioq)
> : [- registeredRequestHandlerKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkz3jon2gk4tfmrjgk4lvmvzxisdbnzsgyzlsjnsxs4y)
> : [- registerRequestHandler:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkz3jon2gk4ssmvyxkzltoregc3tenrsxeotgn5zewzlzhi)
> : [- removeRequestHandlerForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk3lpozsvezlrovsxg5cimfxgi3dfojdg64slmv4tu)
> : [- requestHandlerForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk4lvmvzxisdbnzsgyzlsizxxes3fpe5a)
> : [- setDefaultRequestHandler:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cemvtgc5lmorjgk4lvmvzxisdbnzsgyzlshi)
> : [- sleep](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwyzlfoa)
> : [- takeValuesFromRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gc23fkzqwy5lfondhe33nkjsxc5lfon2du2loinxw45dfpb2du)
>
> **Handling errors**
> : [- handleSessionCreationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvgzltonuw63sdojswc5djn5xek4tsn5zes3sdn5xhizlyoq5a)
> : [- handlePageRestorationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvaylhmvjgk43un5zgc5djn5xek4tsn5zes3sdn5xhizlyoq5a)
> : [- handleSessionRestorationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvgzltonuw63ssmvzxi33smf2gs33oivzhe33sjfxeg33oorsxq5b2)
> : [- handleException:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsuk6ddmvyhi2lpny5gs3sdn5xhizlyoq5a)
>
> **Backward compatibility**
> : [- requiresWOF35RequestHandling](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk4lvnfzgk42xj5ddgnksmvyxkzltoregc3tenruw4zy)
> : [- requiresWOF35TemplateParser](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk4lvnfzgk42xj5ddgnkumvwxa3dborsvaylsonsxe)
>
> **Scripted class support**
> : [- scriptedClassWithPath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwg4tjob2gkzcdnrqxg42xnf2gqudborudu)
> : [- scriptedClassWithPath:encoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwg4tjob2gkzcdnrqxg42xnf2gqudboruduzlomnxwi2lom4)
>
> **Script debugging**
> : [- logWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5wg6z2xnf2gqrtpojwwc5b2)
> : [- debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkytvm5lws5diizxxe3lboq5a)
> : [- printsHTMLParserDiagnostics](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5yhe2loorzuqvcnjrigc4ttmvzei2lbm5xg643unfrxg)
> : [- setPrintsHTMLParserDiagnostics:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cqojuw45dtjbke2tcqmfzhgzlsiruwcz3on5zxi2ldom5a)
> : [- traceAll:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvawy3b2)
>
> **Statistics report**
> : [- setStatisticsStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5ctorqxi2ltoruwg42torxxezj2)
> : [- statisticsStore](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zxiylunfzxi2ldonjxi33smu)
> : [- statistics](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zxiylunfzxi2ldom)
>
> **Monitor support**
> : [- monitoringEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ww63tjorxxe2lom5cw4ylcnrswi)
> : [- activeSessionsCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwg5djozsvgzltonuw63ttinxxk3tu)
> : [- refuseNewSessions:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkztvonsu4zlxknsxg43jn5xhgoq)
> : [- isRefusingNewSessions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgutfmz2xg2lom5hgk52tmvzxg2lpnzzq)
> : [- setMinimumActiveSessionsCount:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cnnfxgs3lvnvawg5djozsvgzltonuw63ttinxxk3tuhi)
> : [- minimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5wws3tjnv2w2qldoruxmzktmvzxg2lpnzzug33vnz2a)
> : [- terminateAfterTimeInterval:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gk4tnnfxgc5dfifthizlskruw2zkjnz2gk4twmfwdu)
>
> **Resource manager support**
> : [- setResourceManager:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5csmvzw65lsmnsu2ylomftwk4r2)
> : [- resourceManager](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk43povzggzknmfxgcz3foi)
>
> **User defaults**
> : [+ loadFrameworks](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3mn5qwirtsmfwwk53pojvxg)
> : [+ setLoadFrameworks:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2ey33bmrdheylnmv3w64tlom5a)
> : [+ isDebuggingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3joncgkytvm5tws3thivxgcytmmvsa)
> : [+ setDebuggingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2eizlcovtwo2lom5cw4ylcnrswioq)
> : [+ autoOpenInBrowser](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bov2g6t3qmvxes3scojxxo43foi)
> : [+ setAutoOpenInBrowser:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2ec5lun5hxazlojfxee4tpo5zwk4r2)
> : [+ isDirectConnectEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3joncgs4tfmn2eg33onzswg5cfnzqwe3dfmq)
> : [+ setDirectConnectEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2ei2lsmvrxiq3pnzxgky3uivxgcytmmvsdu)
> : [+ cgiAdaptorURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3dm5uuczdbob2g64svkjga)
> : [+ setCGIAdaptorURL:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2egr2jifsgc4dun5zfkusmhi)
> : [+ isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jonbwcy3infxgorlomfrgyzle)
> : [+ setCachingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2egyldnbuw4z2fnzqwe3dfmq5a)
> : [+ applicationBaseURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bobygy2ldmf2gs33oijqxgzkvkjga)
> : [+ setApplicationBaseURL:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2ec4dqnruwgylunfxw4qtbonsvkusmhi)
> : [+ frameworksBaseURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3gojqw2zlxn5zgw42cmfzwkvksjq)
> : [+ setFrameworksBaseURL:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2em4tbnvsxo33snnzueyltmvkvetb2)
> : [+ recordingPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3smvrw64tenfxgoudborua)
> : [+ setRecordingPath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fezldn5zgi2lom5igc5dihi)
> : [+ projectSearchPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3qojxwuzldorjwkylsmnufayluna)
> : [+ setProjectSearchPath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fa4tpnjswg5ctmvqxey3ikbqxi2b2)
> : [+ isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jongw63tjorxxerlomfrgyzle)
> : [+ setMonitorEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2e233onf2g64sfnzqwe3dfmq5a)
> : [+ monitorHost](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3nn5xgs5dpojeg643u)
> : [+ setMonitorHost:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2e233onf2g64sin5zxioq)
> : [+ SMTPHost](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l2tjvkfasdpon2a)
> : [+ setSMTPHost:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fgtkukbeg643uhi)
> : [+ adaptor](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bmrqxa5dpoi)
> : [+ setAdaptor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2eczdbob2g64r2)
> : [+ port](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3qn5zhi)
> : [+ setPort:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fa33soq5a)
> : [+ listenQueueSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3mnfzxizlokf2wk5lfknuxuzi)
> : [+ setListenQueueSize:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2ey2ltorsw4ulvmv2wku3jpjstu)
> : [+ workerThreadCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3xn5zgwzlskruhezlbmrbw65looq)
> : [+ setWorkerThreadCount:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fo33snnsxevdiojswczcdn52w45b2)
> : [+ additionalAdaptors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bmrsgs5djn5xgc3cbmrqxa5dpojzq)
> : [+ setAdditionalAdaptors:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2eczdenf2gs33omfweczdbob2g64tthi)
> : [+ includeCommentsInResponses](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jnzrwy5lemvbw63lnmvxhi42jnzjgk43qn5xhgzlt)
> : [+ setIncludeCommentsInResponses:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2es3tdnr2wizkdn5ww2zloorzus3ssmvzxa33oonsxgoq)
> : [+ componentRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3dn5wxa33omvxhiutfof2wk43ujbqw4zdmmvzewzlz)
> : [+ setComponentRequestHandlerKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2eg33nobxw4zloorjgk4lvmvzxisdbnzsgyzlsjnsxsoq)
> : [+ directActionRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3enfzgky3uifrxi2lpnzjgk4lvmvzxisdbnzsgyzlsjnsxs)
> : [+ setDirectActionRequestHandlerKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2ei2lsmvrxiqldoruw63ssmvyxkzltoregc3tenrsxes3fpe5a)
> : [+ resourceRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3smvzw65lsmnsvezlrovsxg5cimfxgi3dfojfwk6i)
> : [+ setResourceRequestHandlerKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fezltn52xey3fkjsxc5lfon2eqylomrwgk4slmv4tu)
> : [+ sessionTimeout](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmvzxg2lpnzkgs3lfn52xi)
> : [+ setSessionTimeOut:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fgzltonuw63sunfwwkt3voq5a)
>
> **Convenience Methods**
> : [- sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwqylsmvsekzdjoruw4z2dn5xhizlyoq)

## Class Methods

---

### adaptor

`+ (NSString *)adaptor`

Returns the class name of the primary adaptor.
This is the cover method for the user default WOAdaptor.

__See
Also:__  [+ setAdaptor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2eczdbob2g64r2)

---

### additionalAdaptors

`+ (NSArray *)additionalAdaptors`

Returns an array of adaptor description dictionaries.
This is the cover method for the user default WOAdditionalAdaptors.

__See
Also:__  [+ setAdditionalAdaptors:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2eczdenf2gs33omfweczdbob2g64tthi)

---

### application

`+ (WOApplication *)application`

Initializes and returns a WOApplication object. This
initializes application attributes and initializes the adaptor or
adaptors specified on the command line. If no adaptor is specified,
WODefaultAdaptor is made the default adaptor. Some of the more interesting
attribute initializations are:

- Session store
  is in the server.
- Page cache size is 30 pages.
- Client caching of pages is enabled ( [isPageRefreshOnBacktrackEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgudbm5svezlgojsxg2cpnzbgcy3lorzgcy3livxgcytmmvsa) returns
  NO).
- Component-definition caching is disabled ( [isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jonbwcy3infxgorlomfrgyzle) returns
  NO).

A exception is raised if initialization
does not succeed.

You may call this method, but do
not override it.

---

### applicationBaseURL

`+ (NSString *)applicationBaseURL`

Returns a path to where the current application
may be found under the document root (either the project or the __.woa__ wrapper).
This is the cover method for the user default WOApplicationBaseURL.

__See
Also:__  [+ setApplicationBaseURL:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2ec4dqnruwgylunfxw4qtbonsvkusmhi)

---

### autoOpenInBrowser

`+ (BOOL)autoOpenInBrowser`

Returns whether automatic browser launching
is enabled. By default, automatic browser launching is enabled.

---

### cgiAdaptorURL

`+ (NSString *)cgiAdaptorURL`

Returns the URL for the web server including
the path to the WebObjects CGI adaptor (for example, __http://localhost/cgi-bin/WebObjects__).
This URL is used by the direct connect feature only. This is the cover
for the user default WOCGIAdaptorURL.

__See
Also:__  [+ setCGIAdaptorURL:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2egr2jifsgc4dun5zfkusmhi)

---

### componentRequestHandlerKey

`+ (NSString *)componentRequestHandlerKey`

Returns the key which identifies URLs directed
at component-action-based requests. By default, this method returns
the string "wo".

---

### directActionRequestHandlerKey

`+ (NSString *)directActionRequestHandlerKey`

Returns the key which identifies URLs directed
at component-based requests. By default, this method returns the
string "wa".

---

### frameworksBaseURL

`+ (NSString *)frameworksBaseURL`

Returns a path to where all frameworks may be
found under the document root. This value is used to determine URLs
that should be generated to reference Web Server Resources in those
frameworks. This is the cover method for the user default WOFrameworksBaseURL.

__See
Also:__  [+ setFrameworksBaseURL:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2em4tbnvsxo33snnzueyltmvkvetb2)

---

### includeCommentsInResponses

`+ (BOOL)includeCommentsInResponses`

Returns whether or not HTML comments are appended
to the response. This is the cover method for the user default
WOIncludeCommentsInResponses.

__See Also:__  [+ setIncludeCommentsInResponses:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2es3tdnr2wizkdn5ww2zloorzus3ssmvzxa33oonsxgoq)

---

### isCachingEnabled

`+ (BOOL)isCachingEnabled`

Returns whether or not component caching is
enabled. If this is enabled, changes to a component will be reparsed
after being saved (assuming the project is under the NSProjectSearchPath).
Note that this has no effect on page caching. This is the cover
method for the user default WOCachingEnabled.

__See
Also:__  [+ setCachingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2egyldnbuw4z2fnzqwe3dfmq5a), [- pageCacheSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygcz3finqwg2dfknuxuzi), [- isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgq3bmnugs3thivxgcytmmvsa)

---

### isDebuggingEnabled

`+ (BOOL)isDebuggingEnabled`

Returns whether or not debugging is enabled.
If YES, [- debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkytvm5lws5diizxxe3lboq5a) prints
out. Most startup-time status message are supressed if this method
returns NO. By default, debugging is enabled. This is the cover
method for the user default WODebuggingEnabled.

__See
Also:__  [- setDebuggingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2eizlcovtwo2lom5cw4ylcnrswioq), [- debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkytvm5lws5diizxxe3lboq5a)

---

### isDirectConnectEnabled

`+ (BOOL)isDirectConnectEnabled`

Returns whether or not direct connect is enabled.
By default it is enabled. For more information, see [setDirectConnectEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2ei2lsmvrxiq3pnzxgky3uivxgcytmmvsdu).

__See
Also:__  [+ cgiAdaptorURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3dm5uuczdbob2g64svkjga)

---

### isMonitorEnabled

`+ (BOOL)isMonitorEnabled`

Returns whether or not the application can communicate
with a Monitor application. It returns YES if the application can
contact Monitor upon startup and subsequently let Monitor gather
statistics. It returns NO if no comunication with Monitor can take
place. By default, it can communicate with a Monitor application.
'This is a cover method for the user default WOMonitorEnabled.

__See
Also:__  [+ setMonitorEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2e233onf2g64sfnzqwe3dfmq5a), [+ monitorHost](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3nn5xgs5dpojeg643u), [+ setMonitorHost:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2e233onf2g64sin5zxioq)

---

### listenQueueSize

`+ (NSNumber *)listenQueueSize`

Returns the size of the listen queue which will
created by the primary adaptor (usually WODefaultAdaptor). This
is the cover method for the user default WOListenQueueSize.

__See
Also:__  [+ setListenQueueSize:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2ey2ltorsw4ulvmv2wku3jpjstu)

---

### loadFrameworks

`+ (NSArray *)loadFrameworks`

Returns the array of frameworks to be loaded
during application initialization.

__See Also:__  [+ setLoadFrameworks:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2ey33bmrdheylnmv3w64tlom5a)

---

### monitorHost

`+ (NSString *)monitorHost`

Returns the host on which Monitor is assumed
to be running. This value is used during initialization if [isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jongw63tjorxxerlomfrgyzle) returns YES.
This is a cover for the user default WOMonitorHost.

__See
Also:__  [+ setMonitorHost:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2e233onf2g64sin5zxioq), [+ isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jongw63tjorxxerlomfrgyzle)

---

### port

`+ (NSNumber *)port`

Returns the port number on which the primary
adaptor will listen (usually WODefaultAdaptor). This is the cover
method for the user default WOPort.

__See Also:__  [+ setPort:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fa33soq5a)

---

### projectSearchPath

`+ (NSArray *)projectSearchPath`

Returns an array of file system paths which
are searched for projects for rapid turnaround mode. This is the
cover method for the user default NSProjectSearchPath.

__See
Also:__  [+ setProjectSearchPath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fa4tpnjswg5ctmvqxey3ikbqxi2b2)

---

### recordingPath

`+ (NSString *)recordingPath`

Returns a file system path which is where the
recording information should be saved. By default, this method returns nil.

If
this method returns a path, all requests and responses are recorded
in the HTTP format in numbered files (__0000-request__, __0000-response__, __0001-request__, __0001-response__,
and so on), and saved under the recording path specified. This directory
is then used by the Playback tool to test the application. You will
most likely set this as a command line argument (-WORecordingPath
pathname), exercise your application to record a scenario you would
like to test, and then stop the application. Afterward you can restart
the application without the WORecordingPath argument, and point
Playback to the recording directory just created to replay your
sequence of requests and compare the responses received with the
ones recorded.

__See Also:__  [+ setRecordingPath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fezldn5zgi2lom5igc5dihi)

---

### resourceRequestHandlerKey

`+ (NSString *)resourceRequestHandlerKey`

Returns the key which identifies URLs directed
through the resource request handler. Resource requests are only
used during development of an application when the application is
being run without an HTTP server.

__See Also:__  [+ setResourceRequestHandlerKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fezltn52xey3fkjsxc5lfon2eqylomrwgk4slmv4tu)

---

### sessionTimeout

`+ (NSNumber*)sessionTimeOut`

Returns the number (of seconds) which will be
used as the default timeout for each newly created session. You
may either override this method, change the user default WOSessionTimeOut,
or set the session timeout in your session's __init__ method.

__See
Also:__  [+ setSessionTimeOut:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fgzltonuw63sunfwwkt3voq5a)

---

### setAdaptor:

`+ (void)setAdaptor:(NSString
*)anAdaptorName`

Sets the the class name of the primary adaptor
to _anAdaptorName_.

__See
Also:__  [+ adaptor](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bmrqxa5dpoi)

---

### setAdditionalAdaptors:

`+ (void)setAdditionalAdaptors:(NSArray
*)anAdaptorPlist`

Sets the array of adaptor description dictionaries
to _anAdaptorPlist_. Each adaptor
description dictionary must have "WOAdaptor" defined, which
is the name of the adaptor class. Other attributes such as WOPort
may also be specified, but are adaptor specific. For example WOWorkerThreadCount is
specific to the WODefaultAdaptor class and may not apply for all
adaptors.

__See Also:__  [+ additionalAdaptors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bmrsgs5djn5xgc3cbmrqxa5dpojzq)

---

### setApplicationBaseURL:

`+ (void)setApplicationBaseURL:(NSString
*)aBaseURL`

Sets to _aBaseURL_ the
path to which the current application may be found under the document
root (either the project or the __.woa__ wrapper).

__See
Also:__  [+ applicationBaseURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bobygy2ldmf2gs33oijqxgzkvkjga)

---

### setAutoOpenInBrowser:

`+ (void)setAutoOpenInBrowser:(BOOL)isEnabled`

Controls whether starting up this application
also launches a web browser. If isEnabled is YES, the application
launches the web browser. If NO, the application does not launch
the browser. Browser launching is enabled by default as long as
there is a WOAdaptorURL key in the file __NeXT_ROOT/NextLibrary/WOAdaptors/Configuration/WebServerConfig.plist__.

To
disable web browser launching, you must send this message in the
init method of your application subclass (or application script).

__See
Also:__  [+ autoOpenInBrowser](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bov2g6t3qmvxes3scojxxo43foi)

---

### setCGIAdaptorURL:

`+ (void)setCGIAdaptorURL:(NSString
*)aURL`

Sets the URL for the web server to _aURL_.
The URL must include the path to the WebObjects CGI adaptor (for
example, __http://localhost/cgi-bin/WebObjects__).
This URL is used by the direct connect feature only..

__See
Also:__  [+ cgiAdaptorURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3dm5uuczdbob2g64svkjga)

---

### setCachingEnabled:

`+ (void)setCachingEnabled:(BOOL)flag`

Sets whether or not component caching is enabled.
If this is enabled, changes to a component will be reparsed after
being saved (assuming the project is under the NSProjectSearchPath).
Note that this has no effect on page caching.

__See
Also:__  [+ isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jonbwcy3infxgorlomfrgyzle), [- pageCacheSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygcz3finqwg2dfknuxuzi), [- setCachingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cdmfrwq2lom5cw4ylcnrswioq)

---

### setComponentRequestHandlerKey:

`+ (void)setComponentRequestHandlerKey:(NSString
*)key`

Sets the component request handler key. This
affects all URLs generated during [appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxa4dfnzsfi32smvzxa33oonstu2loinxw45dfpb2du): of component-based
actions.

__See Also:__  [+ componentRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3dn5wxa33omvxhiutfof2wk43ujbqw4zdmmvzewzlz)

---

### setDebuggingEnabled:

`+ (void)setDebuggingEnabled:(BOOL)flag`

Sets whether or not debugging is enabled. If YES, [- debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkytvm5lws5diizxxe3lboq5a) prints
out. Most startup-time status message are supressed if this method
returns NO. By default, debugging is enabled.

__See
Also:__  [+ isDebuggingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3joncgkytvm5tws3thivxgcytmmvsa), [- debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkytvm5lws5diizxxe3lboq5a)

---

### setDirectActionRequestHandlerKey:

`+ (void)setDirectActionRequestHandlerKey:(NSString
*)key`

Sets the Direct Action request handler key.
This affects all URLs generated during [appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxa4dfnzsfi32smvzxa33oonstu2loinxw45dfpb2du): of direct
actions.

__See Also:__  [+ directActionRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3enfzgky3uifrxi2lpnzjgk4lvmvzxisdbnzsgyzlsjnsxs)

---

### setDirectConnectEnabled:

`+ (void)setDirectConnectEnabled:(BOOL)flag`

Sets whether or not direct connect is enabled.
By default it is enabled.

Direct connect actually transforms
your application in a simple web server of its own. In particular,
it is then able to find and return its images and resources as if
it were a web server. It is very useful in development mode: You
don't need a web server. Just point your URL to the port where
your application is listening, and the application will handle all
urls.

If this flag is YES, the following happens:

- When using [autoOpenInBrowser](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3bov2g6t3qmvxes3scojxxo43foi),
  a direct connect URL will be used.
- When using [WOMailDelivery](WOMailDelivery-2.md#apple-k5huczdbob2g64q) to mail pages with
  dynamic links in them, these links will be generated with a complete
  direct connect URL format. People receiving these mails will be
  able to access the application with direct connect.
- All files on the system are accessible through the resource
  request handler. On the other hand, if this flag is NO, the resource
  request handler can be used to retrieve data objects from memory
  only, and no more reading in the file system is permitted (secure
  mode for deployment).

__See
Also:__  [+ isDirectConnectEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3joncgs4tfmn2eg33onzswg5cfnzqwe3dfmq), [+ cgiAdaptorURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3dm5uuczdbob2g64svkjga)

---

### setFrameworksBaseURL:

`+ (void)setFrameworksBaseURL:(NSString
*)aString`

Sets to _aString_ the
path to where all frameworks may be found under the document root.
This value is used to determine URLs that should be generated to
reference Web Server Resources in those frameworks.

__See
Also:__  [+ frameworksBaseURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3gojqw2zlxn5zgw42cmfzwkvksjq)

---

### setIncludeCommentsInResponses:

`+ (void)setIncludeCommentsInResponses:(BOOL)flag`

Sets whether or not HTML comments are appended
to the response.

__See Also:__  [+ includeCommentsInResponses](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jnzrwy5lemvbw63lnmvxhi42jnzjgk43qn5xhgzlt)

---

### setListenQueueSize:

`+ (void)setListenQueueSize:(NSNumber
*)aListenQueueSize`

Sets the size of the listen queue which will
created by the primary adaptor (usually WODefaultAdaptor).

__See
Also:__  [+ listenQueueSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3mnfzxizlokf2wk5lfknuxuzi)

---

### setLoadFrameworks:

`+ (void)setLoadFrameworks:(NSArray
*)frameworkList`

Sets the array of frameworks to be loaded during
application initialization.

__See Also:__  [+ loadFrameworks](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3mn5qwirtsmfwwk53pojvxg)

---

### setMonitorEnabled:

`+ (void)setMonitorEnabled:(BOOL)flag`

Sets whether or not the application will communicate
with a Monitor application. If _flag_ is YES,
the application can contact Monitor upon startup and subsequently
let Monitor gather statistics. If _flag_ is NO,
no comunication with Monitor can take place. By default, it can
communicate with a Monitor application.

__See
Also:__  [+ isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jongw63tjorxxerlomfrgyzle)

---

### setMonitorHost:

`+ (void)setMonitorHost:(NSString
*)hostName`

Sets the host on which Monitor is assumed to
be running. This value is used during initialization if [isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jongw63tjorxxerlomfrgyzle) returns YES.

__See
Also:__  [+ monitorHost](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3nn5xgs5dpojeg643u), [+ isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jongw63tjorxxerlomfrgyzle)

---

### setPort:

`+ (void)setPort:(NSNumber
*)port`

Sets the port number on which the primary adaptor
will listen (usually WODefaultAdaptor).

__See
Also:__  [+ port](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3qn5zhi)

---

### setProjectSearchPath:

`+ (void)setProjectSearchPath:(NSArray)searchPath`

Sets the array of file system paths which are
searched for projects for rapid turnaround mode.

__See
Also:__  [+ projectSearchPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3qojxwuzldorjwkylsmnufayluna)

---

### setRecordingPath:

`+ (void)setRecordingPath:(NSString
*)path`

Sets the file system path where the recording
information should be saved. Use nil as the path if you don't
want to save recording information. By default, recording information
is not saved.

If you save recording information, all requests
and responses are recorded in the HTTP format in numbered files
(__0000-request__, __0000-response__, __0001-request__, __0001-response__,
and so on), and saved under the recording path specified. This directory
is then used by the Playback tool to test the application. You will
most likely set this as a command line argument (-WORecordingPath
pathname), exercise your application to record a scenario you would
like to test, and then stop the application. Afterward you can restart
the application without the WORecordingPath argument, and point Playback
to the recording directory just created to replay your sequence
of requests and compare the responses received with the ones recorded.

__See
Also:__  [+ recordingPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3smvrw64tenfxgoudborua)

---

### setResourceRequestHandlerKey:

`+ (void)setResourceRequestHandlerKey:(NSString
*)key`

Sets the resource request handler key. This
affects all URLs generated during [appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxa4dfnzsfi32smvzxa33oonstu2loinxw45dfpb2du) of resources.

__See
Also:__  [+ resourceRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3smvzw65lsmnsvezlrovsxg5cimfxgi3dfojfwk6i)

---

### setSessionTimeOut:

`+ (void)setSessionTimeOut:(NSNumber*)aTimeOut`

Accessor to set the default session timeOut.

__See
Also:__  [+ sessionTimeout](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmvzxg2lpnzkgs3lfn52xi)

---

### setSMTPHost:

`+ (void)setSMTPHost:(NSString
*)hostName`

Sets the name of the host that will be used
to send e-mail messages created by [WOMailDelivery](WOMailDelivery-2.md#apple-k5huczdbob2g64q).

__See
Also:__  [+ SMTPHost](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l2tjvkfasdpon2a)

---

### setWorkerThreadCount:

`+ (void)setWorkerThreadCount:(NSNumber
*)aWorkerThreadCount`

SEts the count of worker threads which will
created by the primary adaptor (usually WODefaultAdaptor). A worker
thread count of 0 implies single-threaded mode.

__See
Also:__  [+ workerThreadCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3xn5zgwzlskruhezlbmrbw65looq)

---

### SMTPHost

`+ (NSString *)SMTPHost`

Returns the name of the host that will be used
to send e-mail messages created by [WOMailDelivery](WOMailDelivery-2.md#apple-k5huczdbob2g64q). This is the cover
method for the user default WOSMTPHost.

__See
Also:__  [+ setSMTPHost:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fgtkukbeg643uhi)

---

### workerThreadCount

`+ (NSNumber *)workerThreadCount`

Returns the count of worker threads which will
created by the primary adaptor (usually WODefaultAdaptor). A worker
thread count of 0 implies single-threaded mode. This is the cover method
for the user default WOWorkerThreadCount.

__See
Also:__  [+ setWorkerThreadCount:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2fo33snnsxevdiojswczcdn52w45b2)

---

## Instance Methods

---

### activeSessionsCount

`- (int)activeSessionsCount`

Returns the number of sessions that are currently
active. (A session is active if it has not yet timed out.)

The
number returned here is only accurate if the application stores
state in memory in the server, which is the default. If you use
a custom state-storage strategy, there may be no way to tell how
many sessions are active for a given application instance.

__See
Also:__  [- minimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5wws3tjnv2w2qldoruxmzktmvzxg2lpnzzug33vnz2a), [- setMinimumActiveSessionsCount:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cnnfxgs3lvnvawg5djozsvgzltonuw63ttinxxk3tuhi)

---

### adaptorWithName:arguments:

`- (WOAdaptor *)adaptorWithName:(NSString
*)aName
arguments:(NSDictionary *)someArguments`

Invoked during the [init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uw42lu) method to create an adaptor.
If you subclass WOAdaptor, you specify the WOAdaptor subclass you
want the application to use with the __-a__ option
on the application's command line. When WOApplication encounters
the __-a__ option, it invokes this method.
This method looks for a subclass of WOAdaptor with the name aName
(which was supplied as the __-a__ option's
argument), and if such a class exists, a new instance is initialized
using the WOAdaptor method __initWithName:arguments:__.
The someArguments array is populated with any adaptor-specific options
(such as __-p__ or __-q__)
that follow the adaptor name on the command line. See the [WOAdaptor](WOAdaptor-2.md#apple-k5huczdbob2g64q) class for more information.

__See
Also:__  [- adaptors](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwiylqorxxe4y)

---

### adaptors

`- (NSArray *)adaptors`

Returns the current list of application adaptors.
A WOApplication can have multiple adaptors. (To associate the WOApplication
with multiple adaptors, you specify each adaptor on the application's command
line using the __-a__ option.) This allows
you to design an application that can not only listen to a socket
for incoming HTTP requests (using the WODefaultAdaptor), but can
also receive remote request messages using more advanced RPC mechanisms
such as DO, CORBA, and DCOM.

---

### adaptorsDispatchRequestsConcurrently

`- (BOOL)adaptorsDispatchRequestsConcurrently`

Returns YES if at least one adaptor contains
multiple threads and will attempt to concurrently invoke the request
handlers.

---

### allowsConcurrentRequestHandling

`- (BOOL)allowsConcurrentRequestHandling`

Override to return YES if concurrent request
handling is allowed.

__See Also:__  [- isConcurrentRequestHandlingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgq3pnzrxk4tsmvxhiutfof2wk43ujbqw4zdmnfxgorlomfrgyzle)

---

### appendToResponse:inContext:

`- (void)appendToResponse:(WOResponse
*)aResponse
inContext:(WOContext *)aContext`

The WOApplication object sends this message
to itself to initiate the last phase of request handling. This occurs
right after the __invokeActionForRequest:inContext:__ method
has completed, typically with the return a response page. In the
append-to-response phase, the application objects (particularly
the response component itself) generate the HTML content of the
page. WOApplication's default implementation of this method forwards
the message to the session object.

__See Also:__  [- invokeActionForRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uw45tpnnsucy3unfxw4rtpojjgk4lvmvzxiotjnzbw63tumv4hioq)

---

### awake

`- (void)awake`

Invoked at the beginning of each cycle of the
request-response loop, affording the opportunity to perform initializations
with application-wide scope. Since the default implementation does
nothing, overridden implementations do not have to call __super__.

__See
Also:__  [- sleep](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwyzlfoa)

---

### baseURL

`- (NSString *)baseURL`

Returns the application URL relative to the
server's document root, for example:
> ```
> WebObjects/Examples/HelloWorld.woa.
> ```

__See
Also:__  [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5xgc3lf), [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygc5di)

---

### createContextForRequest:

`- (WOContext *)createContextForRequest:(WORequest
*)aRequest`

Creates a new context object for a given request.
Override this method if you need to provide your own subclass of WOContext.
If you override it, your implementation need not call __super__.

---

### createSessionForRequest:

`- (WOSession *)createSessionForRequest:(WORequest
*)aRequest`

Creates and returns a WOSession object to manage
a session for the application. The method goes through several steps
to locate the class to use for instantiating this object:

1. First it looks for a compiled class of name "Session"
   that is a subclass of WOSession.
2. If such a class does not exist, it looks for a "__.wos__"
   script with the name of "Session" in the application wrapper
   ("__.woa__" directory).
3. If the __Session.wos__ script exists,
   the method parses the script and dynamically adds a scripted-class subclass
   of WOSession to the runtime.

The method
then returns an allocated and initialized (using the default WOSession initializer)
session instance of the selected class. It raises an exception if
it is unable to create a new session.

|  |
| --- |
| An implication of the foregoing description is that the names of compiled WOSession subclasses should be "Session"; if not, you will have to override this method to use the proper class to create the session object. |

__See Also:__  [- restoreSessionWithID:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk43un5zgku3fonzws33ok5uxi2cjiq5gs3sdn5xhizlyoq5a), [- saveSessionForContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwc5tfknsxg43jn5xem33sinxw45dfpb2du)

---

### debugWithFormat:

`- (void)debugWithFormat:(NSString
*)aFormatString,...`

Prints a message to the standard error device
(stderr), if __WODebuggingEnabled__ is YES.
The message can include formatted variable data using printf-style
conversion specifiers. Note that in WebScript, all variables are
objects, so the only conversion specifier allowed is %@. In compiled
Objective-C code, all printf conversion specifiers are allowed.

You
control whether this method displays output with the __WODebuggingEnabled__ user
default option. If __WODebuggingEnabled__ is YES,
then the __debugWithFormat:__ messages display
their output. If __WODebuggingEnabled__ is NO,
the __debugWithFormat:__ messages don't display
their output.

---

### defaultRequestHandler

`- (WORequestHandler *)defaultRequestHandler`

Returns the request handler to be used when
no request handler key was found in the URL or WORequest. This method
returns the WOComponent request handler by default. When an application is
contacted for the first time it is usually via a URL like the following:
> ```
> http://somehost/cgi-bin/WebObjects/AppName.woa
> ```

The
way that URLs of that type are handled is determined by the default
request handler.

---

### defaultRequestHandlerClassName

`- (NSString *)defaultRequestHandlerClassName`

The default implementation of this method returns @"WOComponentRequestHandler",
which is the default request handler. Override this method to return @"WODirectActionRequestHandler"
to make the direct action request handler the default.

---

### dispatchRequest:

`- (WOResponse *)dispatchRequest:(WORequest
*)aRequest`

The main entry point for any given interaction.
Invoked by the adaptor.

---

### dynamicElementWithName:associations:template:languages:

`- (WODynamicElement *)dynamicElementWithName:(NSString
*)aName
associations:(NSDictionary *)someAssociations
template:(WOElement *)anElement
languages:(NSArray *)languages`

Creates and returns a WODynamicElement object
based on the element's name, a dictionary of associations, and
a template of elements. This method is invoked automatically to
provide a WODynamicElement object that represents a WEBOBJECT element
in the HTML template. You don't ordinarily invoke __dynamicElementWithName:associations:template:languages:__,
but you might override it to substitute your own WODynamicElement
or reusable component for one of the built-in WODynamicElements.

The
arguments aName and someAssociations are derived from a corresponding
line in the declarations file. aName is an NSString that identifies
the kind of element to create. Generally aName specifies a built-in
WODynamicElement such as WOString, but it may also identify a reusable
component. (For more information, see the chapter "Using Reusable
Components" in the WebObjects Developer's Guide.) For example,
in the __dynamicElementWithName:associations:template:languages:__ message
for the following declaration:

> ```
> APP_STRING: WOString {value = applicationString;};
> ```

_aName_ contains
the string "WOString".

The someAssociations dictionary
contains an entry for each attribute specified in the corresponding declaration.
For the declaration above, someAssociations contains a single entry
for WOString's value attribute. The keys of someAssociations are
the attribute names and the values are WOAssociation objects.

WOApplication's
implementation of __dynamicElementWithName:associations:template:languages:__ first searches
for a WODynamicElement named _aName_.
If a WODynamicElement is found, the method creates an instance using
the method [initWithName:associations:template:](WODynamicElement-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2epfxgc3ljmncwyzlnmvxhil3jnzuxiv3jorue4ylnmu5gc43tn5rwsylunfxw44z2orsw24dmmf2gkoq) and
returns it. Otherwise, it searches for a component-either scripted
or compiled-to return instead. If neither are found, this method
returns nil.

---

### handleException:inContext:

`- (WOResponse *)handleException:(NSException
*)anException
inContext:(WOContext *)aContext`

Invoked when an exception occurs within the
request-response loop. The default behavior displays a page with
debugging information. You can override this method to catch exceptions
and display a "friendlier" error page. For example, the following
code replaces the standard error page with a component named ErrorPage.wo.
> ```
> - (WOResponse *)handleException:(NSException *)anException {
>     WOResponse *response = [[WOResponse alloc] init];
>     WORequest *request = [[self context] request];
>     WOString newURL = [NSString stringWithFormat:@"http://%@%@/%@.woa/-/ErrorPage.wo",
>         [request applicationHost],
>         [request adaptorPrefix],
>         [request applicationName]];
>
>     [response setHeader:newURL forKey:@"location"];
>     [response setHeader:@"text/html" forKey:@"content-type"];
>     [response setHeader:@"0" forKey:@"content-length"];
>     [response setStatus:302];
>     return response;
> }
> ```

__See
Also:__  [- handleSessionCreationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvgzltonuw63sdojswc5djn5xek4tsn5zes3sdn5xhizlyoq5a), [- handleSessionRestorationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvgzltonuw63ssmvzxi33smf2gs33oivzhe33sjfxeg33oorsxq5b2)

---

### handlePageRestorationErrorInContext:

`- (WOResponse *)handlePageRestorationErrorInContext:(WOContext
*)aContext`

Invoked when a page (WOComponent) instance cannot
be restored, which typically happens when a user backtracks too
far. Specifically, this method is invoked when the following occurs:
the request is not the first of a session, page restoration by context
ID fails, and page re-creation is disabled. The default behavior
displays a page with debugging information. You can override this
method to display a "friendlier" error page.

__See
Also:__  [- handleException:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsuk6ddmvyhi2lpny5gs3sdn5xhizlyoq5a), [- handleSessionCreationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvgzltonuw63sdojswc5djn5xek4tsn5zes3sdn5xhizlyoq5a), [- handleSessionRestorationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvgzltonuw63ssmvzxi33smf2gs33oivzhe33sjfxeg33oorsxq5b2)

---

### handleSessionCreationErrorInContext:

`- (WOResponse *)handleSessionCreationErrorInContext:(WOContext
*)aContext`

Invoked when a session (WOSession) instance
cannot be created. The default behavior displays a page with debugging
information. You can override this method to display a "friendlier"
error page.

__See Also:__  [- handleException:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsuk6ddmvyhi2lpny5gs3sdn5xhizlyoq5a), [- handlePageRestorationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvaylhmvjgk43un5zgc5djn5xek4tsn5zes3sdn5xhizlyoq5a), [- handleSessionRestorationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvgzltonuw63ssmvzxi33smf2gs33oivzhe33sjfxeg33oorsxq5b2)

---

### handleSessionRestorationErrorInContext:

`- (WOResponse *)handleSessionRestorationErrorInContext:(WOContext
*)aContext`

Invoked when a session (WOSession) instance
cannot be restored, which typically happens when the session times
out. The default behavior displays a page with debugging information.
You can override this method to display a "friendlier" error
page.

__See Also:__  [- handleException:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsuk6ddmvyhi2lpny5gs3sdn5xhizlyoq5a), [- handlePageRestorationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvaylhmvjgk43un5zgc5djn5xek4tsn5zes3sdn5xhizlyoq5a), [- handleSessionCreationErrorInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsvgzltonuw63sdojswc5djn5xek4tsn5zes3sdn5xhizlyoq5a)

---

### handlerForRequest:

`- (WORequestHandler *)handlerForRequest:(WORequest
*)aRequest`

Returns the request handler used to handle a
given request.

__See Also:__  [- registerRequestHandler:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkz3jon2gk4ssmvyxkzltoregc3tenrsxeotgn5zewzlzhi), [- registeredRequestHandlerKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkz3jon2gk4tfmrjgk4lvmvzxisdbnzsgyzlsjnsxs4y), [- requestHandlerForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk4lvmvzxisdbnzsgyzlsizxxes3fpe5a)

---

### init

`- (id)init`

Initializes application attributes and initializes
the adaptor or adaptors specified on the command line. If no adaptor
is specified, WODefaultAdaptor is made the default adaptor. Some
of the more interesting attribute initializations are:

- Session store is in the server.
- Page cache size is 30 pages.
- Client caching of pages is enabled ( [isPageRefreshOnBacktrackEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgudbm5svezlgojsxg2cpnzbgcy3lorzgcy3livxgcytmmvsa) returns
  NO).
- Component-definition caching is disabled ( [isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3jonbwcy3infxgorlomfrgyzle) returns
  NO).

A exception is raised if initialization
does not succeed.

|  |
| --- |
| The global variable "WOApp" is initialized in this method. Your subclasses of [WOApplication](#apple-k5huc4dqnruwgylunfxw4) (including Application.wos) should be sure to call __super__'s [init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uw42lu) method as their first line of code. |

---

### invokeActionForRequest:inContext:

`- (WOElement *)invokeActionForRequest:(WORequest
*)aRequest
inContext:(WOContext *)aContext`

The WOApplication object sends this message
to itself to initiate the middle phase of request handling. In this
phase, the message is propagated through the objects of the application
until the dynamic element that has received the user action (for
instance, a click on a button) responds to the message by triggering
the method in the request component that is bound to the action.
The default WOApplication implementation of this method forwards
the message to the session object.

__See Also:__  [- appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxa4dfnzsfi32smvzxa33oonstu2loinxw45dfpb2du)

---

### isCachingEnabled

`- (BOOL)isCachingEnabled`

Returns whether component-definition caching
is enabled. The default is NO.

__See Also:__  [- setCachingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cdmfrwq2lom5cw4ylcnrswioq)

---

### isConcurrentRequestHandlingEnabled

`- (BOOL)isConcurrentRequestHandlingEnabled`

Returns YES if adaptors dispatch requests concurrently
and [allowsConcurrentRequestHandling](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwy3dpo5zug33omn2xe4tfnz2fezlrovsxg5cimfxgi3djnztq) has
been overridden to allow concurrent request handling.

__See
Also:__  [- allowsConcurrentRequestHandling](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwy3dpo5zug33omn2xe4tfnz2fezlrovsxg5cimfxgi3djnztq)

---

### isPageRefreshOnBacktrackEnabled

`- (BOOL)isPageRefreshOnBacktrackEnabled`

Returns whether caching of pages is disabled
in the client. If so, the client does not restore request pages from
its cache but re-creates them "from scratch" by resending the
URL to the server. This flag is set to NO by default.

__See
Also:__  [- setPageRefreshOnBacktrackEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cqmftwkutfmzzgk43ij5xeeyldnn2heyldnncw4ylcnrswioq)

---

### isRefusingNewSessions

`- (BOOL)isRefusingNewSessions`

Returns YES if the application instance is refusing
new sessions, and NO otherwise. When the application instance refuses
new sessions, the WebObjects adaptor tries to start the session
in another instance of the same application. If no other instance
is running and accepting new sessions, the user receives an error
message.

---

### isTerminating

`- (BOOL)isTerminating`

Returns whether the application will terminate
at the end of the current request-response loop.

__See
Also:__  [- setTimeOut:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cunfwwkt3voq5a), [- defaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkztbovwhiutfof2wk43ujbqw4zdmmvza), [- terminateAfterTimeInterval:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gk4tnnfxgc5dfifthizlskruw2zkjnz2gk4twmfwdu), [- timeOut](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gs3lfj52xi)

---

### lock

`- (void)lock`

Locks the application object.

---

### lockRequestHandling

`- (void)lockRequestHandling`

Serializes request handler access if concurrent
request handling isn't enabled.

---

### logSetValueForDeclarationNamed:type:bindingNamed:associationDescription:value:

`- (void)logSetValueForDeclarationNamed:(NSString*)aDeclarationName
type:(NSString*)aDeclarationType
bindingNamed:(NSString*)aBindingName
associationDescription:(NSString*)anAssociationDescription
value:(id)aValue`

Formats and logs a message anytime a value is
set through a WOAssociation, when WODebug is set to YES for the
declaration in which the association appears. (Setting a value means
the child component/element is setting a value in the parent).
See [logTakeValueForDeclarationNamed:type:bindingNamed:associationDescription:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5wg6z2umfvwkvtbnr2wkrtpojcgky3mmfzgc5djn5xe4ylnmvsdu5dzobstuytjnzsgs3thjzqw2zlehjqxg43pmnuwc5djn5xeizltmnzgs4dunfxw4otwmfwhkzj2) for
a description of each of the arguments to this method.

---

### logTakeValueForDeclarationNamed:type:bindingNamed:associationDescription:value:

`- (void)logTakeValueForDeclarationNamed:(NSString*)aDeclarationName
type:(NSString*)aDeclarationType
bindingNamed:(NSString*)aBindingName
associationDescription:(NSString*)anAssociationDescription
value:(id)aValue`

Formats and logs a message anytime a value is
"taken" through a WOAssociation , when WODebug is set to YES for
the declaration in which the association appears. (Taking a value
means the child component/element is taking a value from the parent).
Override this method to alter the format of the log message. The
arguments of this method are defined in the following example of
a WebObjects declaration.
> ```
> aDeclarationName : aDeclarationType {
>     aBindingName = anAssociationDescription;
> }
> ```

Also, _aValue_ is
the value which is being pushed to or pulled from the child to the
parent.

---

### logWithFormat:

`- (void)logWithFormat:(NSString
*)aFormat,...`

Prints a message to the standard error device
(stderr). The message can include formatted variable data using
printf-style conversion specifiers, for example:
> ```
> id i = 500;
> id f = 2.045;
> [self logWithFormat:@"Amount = %@, Rate = %@, Total = %@", i, f, i*f];
> ```

Note
that in WebScript, all variables are objects, so the only conversion
specifier allowed is __%@__ as shown above.
In compiled Objective-C code, all __printf__ conversion
specifiers are allowed. The equivalent method in Java is __logString__.

---

### minimumActiveSessionsCount

`- (int)minimumActiveSessionsCount`

Returns the minimum number of active sessions
allowed. If the number of active sessions is less than or equal
to this number and [isRefusingNewSessions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgutfmz2xg2lom5hgk52tmvzxg2lpnzzq) is YES,
the application instance terminates. The default is 0.

__See
Also:__  [- activeSessionsCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwg5djozsvgzltonuw63ttinxxk3tu), [- refuseNewSessions:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkztvonsu4zlxknsxg43jn5xhgoq), [- setMinimumActiveSessionsCount:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cnnfxgs3lvnvawg5djozsvgzltonuw63ttinxxk3tuhi)

---

### monitoringEnabled

`- (BOOL)monitoringEnabled`

Returns YES if the application is "monitorable"
by the Monitor application, and NO otherwise. An application is
"monitorable" if it was able to find a running Monitor upon
startup and it is able to successfully communicate with that Monitor.

By
default, all applications are monitorable if the Monitor application
is running on the same machine as the application. You can specifically
disable monitoring using the -WOMonitorEnabled NO option on the
application command line. If you want the application to be monitorable
and the Monitor is running on another host, you can start up the
application through Monitor, or you can specify Monitor's host
on the application command line this way:

> ```
> MyApp.exe -WOMonitorEnabled YES -WOMonitorHost monitorHost ...
> ```

---

### name

`- (NSString *)name`

Returns the name of the application, which is
the name of the executable (without the .exe extension).

__See
Also:__  [- baseURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5rgc43fkvjey), [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygc5di)

---

### number

`- (NSString *)number`

Returns @"-1". This is provided for
backwards compatibility only.

---

### pageCacheSize

`- (unsigned int)pageCacheSize`

Returns the size of the internal cache for page
instances. The default size is 30 instances.

__See
Also:__  [- setPageCacheSize:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cqmftwkq3bmnugku3jpjstu)

---

### pageWithName:forRequest:

`- (WOComponent *)pageWithName:(NSString
*)aName
forRequest:(WORequest *)aRequest`

Returns a new page instance (a WOComponent object)
identified by aName. If aName is nil, the "Main" component is
assumed. If the method cannot create a valid page instance, it raises an
exception.

As part of its implementation, this method creates
a context with _aRequest_ and calls [pageWithName:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygcz3fk5uxi2comfwwkotjnzbw63tumv4hioq).

__See
Also:__  [- restorePageForContextID:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxxezltorxxezkqmftwkrtpojbw63tumv4hiskehi) (WOSession), [- savePage:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxxgylwmvigcz3fhi) (WOSession)

---

### pageWithName:inContext:

`- (WOComponent *)pageWithName:(NSString
*)aName
inContext:(WOContext *)aContext`

Returns a new page instance (a WOComponent object)
identified by aName. If aName is nil, the "Main" component is
assumed. If the method cannot create a valid page instance, it raises an
exception.

__See Also:__  [pageWithName:forRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygcz3fk5uxi2comfwwkotgn5zfezlrovsxg5b2), [- restorePageForContextID:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxxezltorxxezkqmftwkrtpojbw63tumv4hiskehi) (WOSession), [- savePage:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxxgylwmvigcz3fhi) (WOSession)

---

### path

`- (NSString *)path`

Returns the filesystem path of the application,
which is an absolute path and includes the "__.woa__" extension;
for example "__C:/NETSCAPE/ns-home/docs/WebObjects/Examples/HelloWorld.woa__"
is a typical application path.

__See Also:__  [- baseURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5rgc43fkvjey), [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5xgc3lf)

---

### permanentPageCacheSize

`- (unsigned int)permanentPageCacheSize`

Returns the permanent page cache size. The default
is 30. The permanent page cache holds pages which should not fall
out of the regular page cache. For example, a control page in a
frameset should exist for the duration of a session.

__See
Also:__  [savePageInPermanentCache:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxxgylwmvigcz3fjfxfazlsnvqw4zloorbwcy3imu5a) ( [WOApplication](#apple-k5huc4dqnruwgylunfxw4))

---

### printsHTMLParserDiagnostics

`- (BOOL)printsHTMLParserDiagnostics`

Returns whether the HTML parser prints
diagnostic information to stdout when it encounters unbalanced HTML
containers or other syntactically incorrect HTML. This method returns NO by default.

__See
Also:__  [+ isDebuggingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3joncgkytvm5tws3thivxgcytmmvsa), [- debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkytvm5lws5diizxxe3lboq5a)

---

### refuseNewSessions:

`- (void)refuseNewSessions:(BOOL)flag`

Controls whether this application instance will
create a session when it receives an HTTP request from a new user.
If _flag_ is YES, the application does
not create new sessions; when it receives a request from a new user,
it refuses that request, and the adaptor must try to find another
application instance that can process the request. If _flag_ is NO,
the application creates new sessions. NO is the default.

You
use this method with __setMinimumActiveSessionsCount:__ to
gracefully shut down application instances. Use __setMinimumActiveSessionsCount:__ to
set the active session minimum to a certain number. When number
of active sessions reaches the number you set and __isRefusingNewSessions__ returns YES, the
application terminates.

__See Also:__  [- activeSessionsCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwg5djozsvgzltonuw63ttinxxk3tu), [- isRefusingNewSessions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgutfmz2xg2lom5hgk52tmvzxg2lpnzzq), [- minimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5wws3tjnv2w2qldoruxmzktmvzxg2lpnzzug33vnz2a), [- setMinimumActiveSessionsCount:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cnnfxgs3lvnvawg5djozsvgzltonuw63ttinxxk3tuhi)

---

### registerRequestHandler:forKey:

`- (void)registerRequestHandler:(WORequestHandler
*)aHandler
forKey:(NSString *)aKey`

Registers a new request handler. _aKey_ must
specify a key which can be found in the URLs following the instance
number or application name.

__See Also:__  [- removeRequestHandlerForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk3lpozsvezlrovsxg5cimfxgi3dfojdg64slmv4tu), [- registeredRequestHandlerKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkz3jon2gk4tfmrjgk4lvmvzxisdbnzsgyzlsjnsxs4y), [- requestHandlerForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk4lvmvzxisdbnzsgyzlsizxxes3fpe5a)

---

### registeredRequestHandlerKeys

`- (NSArray *)registeredRequestHandlerKeys`

Returns an array of strings containing the keys
of all of the registered request handlers.

__See
Also:__  [- handlerForRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsxertpojjgk4lvmvzxioq), [- requestHandlerForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk4lvmvzxisdbnzsgyzlsizxxes3fpe5a)

---

### removeRequestHandlerForKey:

`- (WORequestHandler *)removeRequestHandlerForKey:(NSString
*)aRequestHandlerKey`

Removes the specified request handler from the
application.

__See Also:__  [- registerRequestHandler:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkz3jon2gk4ssmvyxkzltoregc3tenrsxeotgn5zewzlzhi), [- requestHandlerForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk4lvmvzxisdbnzsgyzlsizxxes3fpe5a)

---

### requestHandlerForKey:

`- (WORequestHandler *)requestHandlerForKey:(NSString
*)key`

Returns the request handler used to handle requests
containing the specified key.

__See Also:__  [- handlerForRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ugc3tenrsxertpojjgk4lvmvzxioq), [- registerRequestHandler:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkz3jon2gk4ssmvyxkzltoregc3tenrsxeotgn5zewzlzhi), [- registeredRequestHandlerKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkz3jon2gk4tfmrjgk4lvmvzxisdbnzsgyzlsjnsxs4y)

---

### requiresWOF35RequestHandling

`- (BOOL)requiresWOF35RequestHandling`

For backward compatibility, if your project
depends upon features or side effects of the old request handling,
you will want to override this method and return YES. By default,
it returns NO.

---

### requiresWOF35TemplateParser

`- (BOOL)requiresWOF35TemplateParser`

For backward compatibility, if your project
depends upon features or side effects removed from the new, 4.0
template parser, you will want to override this method and return YES.
By default, it returns NO.

---

### resourceManager

`- (WOResourceManager *)resourceManager`

Returns the WOResourceManager object that the
application uses to manage resources.

__See
Also:__  [- setResourceManager:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5csmvzw65lsmnsu2ylomftwk4r2)

---

### restoreSessionWithID:inContext:

`- (WOSession *)restoreSessionWithID:(NSString
*)aSessionID
inContext:(WOContext *)aContext`

Restores the WOSession object representing a
session. In normal request handling, this method is invoked at the
start of a cycle of the request-response loop. The default implementation
simply invokes WOSessionStore's [checkOutSessionWithID:request:](WOSessionStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnzjxi33smuxwg2dfmnvu65luknsxg43jn5xfo2lunbeuiotsmvyxkzltoq5a) method,
but raises an exception if the WOSessionStore object is missing.

__See
Also:__  [- createSessionForRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5rxezlborsvgzltonuw63sgn5zfezlrovsxg5b2), [- saveSessionForContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwc5tfknsxg43jn5xem33sinxw45dfpb2du)

---

### run

`- (void)run`

Runs the application in a near-indefinite run
loop in the default run-loop mode. Before starting the run loop,
the method sends [registerForEvents](WOAdaptor-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bmrqxa5dpoixxezlhnfzxizlsizxxerlwmvxhi4y) to
the application's adaptors so that they can begin receiving run-loop
events. Normally, [run](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zhk3q) is
invoked in the main function.

__See Also:__  [- setTimeOut:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cunfwwkt3voq5a), [- defaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkztbovwhiutfof2wk43ujbqw4zdmmvza), [- terminateAfterTimeInterval:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gk4tnnfxgc5dfifthizlskruw2zkjnz2gk4twmfwdu)

---

### runLoop

`- (NSRunLoop *)runLoop`

Returns the application's run loop. Use this
method when you need a run loop for such things as registering timers.

---

### saveSessionForContext:

`- (void)saveSessionForContext:(WOContext
*)aContext`

Called at the end of the request handling loop,
when the current session object needs to be saved. The default implementation
simply invokes WOSessionStore's [checkInSessionForContext:](WOSessionStore-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnzjxi33smuxwg2dfmnvus3stmvzxg2lpnzdg64sdn5xhizlyoq5a) method,
but raises an exception if the WOSessionStore object is missing.

__See
Also:__  [- restoreSessionWithID:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk43un5zgku3fonzws33ok5uxi2cjiq5gs3sdn5xhizlyoq5a)

---

### scriptedClassWithPath:

`- (Class)scriptedClassWithPath:(NSString
*)aPath`

Loads a Webscript-based class with the pathname _aPath_ into
the application. The specified script is parsed assuming the default
string encoding, and the class and categories found in the script
file are dynamically added to the runtime.

---

### scriptedClassWithPath:encoding

`- (Class)scriptedClassWithPath:(NSString
*)aPath
encoding:(NSStringEncoding)anEncoding`

Loads a scripted class with the pathname _aPath_ using
the encoding _anEncoding_. The class
and categories found in the script file are dynamically added to
the runtime. The script must use the @interface/@implementation
syntax.

---

### sessionStore

`- (WOSessionStore *)sessionStore`

Returns the application's current WOSessionStore
object (which, by default, stores state in the server).

__See
Also:__  [- setSessionStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5ctmvzxg2lpnzjxi33smu5a)

---

### setCachingEnabled:

`- (void)setCachingEnabled:(BOOL)flag`

Enables or disables the caching of component
definitions. Component definitions contain templates and other information
about pages and subcomponents, and are used to generate instances
of those components. When this flag is enabled, the application
parses the script (or implementation) file, the HTML, and the declaration
(".wod") file of a component once and then stores the resulting
component definition. By default, this kind of caching is disabled
so that you can edit a scripted component without having to relaunch
the application every time to check the results. You should always
enable component-definition caching when you deploy an application
since performance improves significantly.

Do not confuse this
type of caching with page-instance caching (see setPageCacheSize:).
Caching Strategies in the class description provides further details.

__See
Also:__  [- isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgq3bmnugs3thivxgcytmmvsa)

---

### setDefaultRequestHandler:

`- (void)setDefaultRequestHandler:(WORequestHandler
*)aHandler`

Sets the default request handler. If,
for instance, you want the default request handler to use direct actions,
write something like the following:

> ```
> aHandler = [self requestHandlerForKey:@"wa"]; [self setDefaultRequestHandler:aHandler];
> ```

__See
Also:__  [- defaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkztbovwhiutfof2wk43ujbqw4zdmmvza)

---

### setMinimumActiveSessionsCount:

`- (void)setMinimumActiveSessionsCount:(int)anInt`

Sets the minimum number of active sessions to _anInt_.
The default is 0.

You use this method to gracefully shut down
application instances. If the active sessions count reaches this
number and isRefusingNewSessions returns YES, the application terminates.
You might want to terminate application instances periodically for
performance reasons; some applications leak a certain amount of
memory per transaction, and shutting down and restarting instances
of those applications can free up that memory.

__See
Also:__  [- activeSessionsCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qwg5djozsvgzltonuw63ttinxxk3tu), [- isRefusingNewSessions](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgutfmz2xg2lom5hgk52tmvzxg2lpnzzq), [- minimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5wws3tjnv2w2qldoruxmzktmvzxg2lpnzzug33vnz2a), [- refuseNewSessions:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgkztvonsu4zlxknsxg43jn5xhgoq)

---

### setPageCacheSize:

`- (void)setPageCacheSize:(unsigned
int)anInt`

Sets whether caching of page instances will
occur and the number of pages the cache will hold. When page-instance
caching is enabled, the application stores the WOComponent instance
corresponding to the response page in the session. When the page
is backtracked to, it restores it from the session and makes it
the request page. The state of the page is retained. By default,
page-instance caching is enabled, with a cache limit of 30 pages.

You
turn page-instance caching off by invoking this method with an argument
of zero. In this case, when the user backtracks to a page, the page
is not stored in the session and so must be re-created "from scratch." Do
not confuse this type of caching with component-definition caching
(see [setCachingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2egyldnbuw4z2fnzqwe3dfmq5a)).

__See
Also:__  [- pageCacheSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygcz3finqwg2dfknuxuzi)

---

### setPageRefreshOnBacktrackEnabled:

`- (void)setPageRefreshOnBacktrackEnabled:(BOOL)flag`

When _flag_ is YES,
disables caching of pages by the client by setting the page's
expiration-time header to the current date and time. (By default,
this attribute is set to NO.) Disabling of client caching affects what
happens during backtracking. With client caching turned off, the
browser resends the URL to the server for the page requested by
backtracking. The application must return a new page to the browser (corresponding
to a new WOComponent instance). This behavior is desirable when
you do not want the user to backtrack to a page that might be obsolete
because of changes that have occurred in the session.

When
this flag is turned on and a request corresponding to a client backtrack
occurs, the retrieved page will only be asked to regenerate its
response. The first two phases of a normal request-response loop (value
extraction from the request and action invocation) do not occur.

See
Caching Strategies in the class description for further details.

__See
Also:__  [- isPageRefreshOnBacktrackEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgudbm5svezlgojsxg2cpnzbgcy3lorzgcy3livxgcytmmvsa)

---

### setPermanentPageCacheSize:

`- (void)setPermanentPageCacheSize:(unsigned
int)aSize`

Sets the permanentPageCacheSize to aSize

__See
Also:__  [- permanentPageCacheSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5ygk4tnmfxgk3tukbqwozkdmfrwqzktnf5gk)

---

### setPrintsHTMLParserDiagnostics:

`- (void)printsHTMLParserDiagnostics:(BOOL)flag`

Sets whether the HTML parser prints diagnostic
information to stdout when it encounters unbalanced HTML containers
or other syntactically incorrect HTML. This diagnostic information
is not printed by default.

__See Also:__  [+ setDebuggingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5huc4dqnruwgylunfxw4l3tmv2eizlcovtwo2lom5cw4ylcnrswioq), [- debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5sgkytvm5lws5diizxxe3lboq5a)

---

### setResourceManager:

`- (void)setResourceManager:(WOResourceManager
*)aResourceManager`

Sets the WOResourceManager object to _aResourceManager_.
WOResourceManager objects search for and retrieve resources from
the application directory and from shared framework directories.

__See
Also:__  [- resourceManager](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk43povzggzknmfxgcz3foi)

---

### setSessionStore:

`- (void)setSessionStore:(WOSessionStore
*)aSessionStore`

Set the session-store object for the application.
By default, an object that stores session state in process memory
(that is, in the server) is used. The session-store object specifies
the state storage strategy for the whole application. This object
is responsible for making session objects persistent. You should
set the session store object when the application starts up, before
the first request is handled.

__See Also:__  [- sessionStore](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk43tnfxw4u3un5zgk)

---

### setStatisticsStore:

`- (void)setStatisticsStore:(WOStatisticsStore
*)aStatisticsStore`

Sets the WOStatisticsStore object to _aStatisticsStore_.
WOStatisticsStore objects record application statistics while the
application runs.

__See Also:__  [- statisticsStore](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zxiylunfzxi2ldonjxi33smu)

---

### setTimeOut:

`- (void)setTimeOut:(NSTimeInterval)aTimeInterval`

Sets the number of seconds the application can
experience inactivity (no HTTP requests) before it terminates execution.

This
method differs from [terminateAfterTimeInterval:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gk4tnnfxgc5dfifthizlskruw2zkjnz2gk4twmfwdu) in
that with this method, the application must be idle for _aTimeInterval_ seconds
for the application to terminate. [terminateAfterTimeInterval:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gk4tnnfxgc5dfifthizlskruw2zkjnz2gk4twmfwdu) terminates
the application whether it is active or not.

__See
Also:__  [- timeOut](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52gs3lfj52xi)

---

### sharedEditingContext

`- (EOSharedEditingContext *)sharedEditingContext`

This is a convenience method that returns
the default shared editing context.

__See
Also:__  EOSharedEditingContext class description in
the EOControl Framework

---

### sleep

`- (void)sleep`

Invoked at the conclusion of a request-handling
cycle to give an application the opportunity for deallocating objects
created and initialized in its awake method. The default implementation
does nothing.

---

### statistics

`- (bycopyNSDictionary *)statistics`

Returns a copy of the dictionary containing
the application statistics maintained by WOStatisticsStore. This
method is used by the Monitor application to retrieve application
statistics. If you need to access the statistics internally, use
this message instead:
> ```
> [[[WOApplication application] statisticsStore] statistics]
> ```

---

### statisticsStore

`- (WOStatisticsStore *)statisticsStore`

Returns the WOStatisticsStore object, which
records statistics while the application runs.

__See
Also:__  [- setStatisticsStore:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5ctorqxi2ltoruwg42torxxezj2)

---

### takeValuesFromRequest:inContext:

`- (void)takeValuesFromRequest:(WORequest
*)aRequest
inContext:(WOContext *)aContext`

The component action request handler sends this
message to the WOApplication to start the first phase of request
handling. In this phase, the message is propagated to the session
and component objects involved in the request as well as the request
page's dynamic elements. Each dynamic element acquires any entered
data or changed state (such as a check in a check box) associated
with an attribute and assigns the value to the variable bound to
the attribute. The default WOApplication implementation of this
method forwards the message to the session object.

__See
Also:__  [- appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxa4dfnzsfi32smvzxa33oonstu2loinxw45dfpb2du), [- invokeActionForRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uw45tpnnsucy3unfxw4rtpojjgk4lvmvzxiotjnzbw63tumv4hioq)

---

### terminate

`- (oneway void)terminate`

Terminates the application process. Termination
does not take place until the handling of the current request has
completed.

__See Also:__  [- isTerminating](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5uxgvdfojwws3tboruw4zy), [- setTimeOut:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cunfwwkt3voq5a)

---

### terminateAfterTimeInterval:

`- (void)terminateAfterTimeInterval:(NSTimeInterval)aTimeInterval`

Sets the application to terminate itself after
aTimeInterval seconds has elapsed. After the specified time interval
has elapsed, the application immediately stops all current processing.
If any sessions are active, users may lose information.

This
method differs from [setTimeOut:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cunfwwkt3voq5a) in
that it does not set idle time; __terminateAfterTimeInterval:__ shuts
down the application regardless of whether it is idle.

---

### timeOut

`- (NSTimeInterval)timeOut`

Returns the application's time-out interval:
a period (in seconds) of inactivity before the application terminates
execution. The default application time-out interval is a very large
number.

__See Also:__  [- setTimeOut:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zwk5cunfwwkt3voq5a)

---

### trace:

`- (void)trace:(BOOL)flag`

If flag is YES, prints all trace messages (messages
for scripted messages, compiled messages, and all statements in
the application) to the standard error device. If flag is NO, stops
printing all trace messages.

__See Also:__  [- traceAssignments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvaxg43jm5xg2zloorztu), [- traceObjectiveCMessages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvhwe2tfmn2gs5tfingwk43tmftwk4z2), [- traceScriptedMessages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvjwg4tjob2gkzcnmvzxgylhmvztu), [- traceStatements:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvjxiylumvwwk3tuom5a)

---

### traceAll:

`- (void)traceAll:(BOOL)flag`

If flag is YES, prints all trace messages (messages
for scripted messages, compiled messages, and all statements in
the application) to the standard error device. If flag is NO, stops
printing all trace messages.

__See Also:__  [- traceAssignments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvaxg43jm5xg2zloorztu), [- traceObjectiveCMessages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvhwe2tfmn2gs5tfingwk43tmftwk4z2), [- traceScriptedMessages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvjwg4tjob2gkzcnmvzxgylhmvztu), [- traceStatements:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvjxiylumvwwk3tuom5a)

---

### traceAssignments:

`- (void)traceAssignments:(BOOL)flag`

If flag is YES, prints a message to the standard
error device every time an assignment statement is executed. If
flag is NO, stops printing trace assignment messages.

__See
Also:__  [- trace:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmu5a), [- traceObjectiveCMessages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvhwe2tfmn2gs5tfingwk43tmftwk4z2), [- traceScriptedMessages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvjwg4tjob2gkzcnmvzxgylhmvztu), [- traceStatements:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvjxiylumvwwk3tuom5a)

---

### traceObjectiveCMessages:

`- (void)traceObjectiveCMessages:(BOOL)flag`

If flag is YES, prints a message to the standard
error device every time a message is sent to a compiled class from
Webscript. If flag is NO, stops printing these messages.

__See
Also:__  [- trace:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmu5a), [- traceAssignments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvaxg43jm5xg2zloorztu), [- traceScriptedMessages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvjwg4tjob2gkzcnmvzxgylhmvztu), [- traceStatements:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvjxiylumvwwk3tuom5a)

---

### traceScriptedMessages:

`- (void)traceScriptedMessages:(BOOL)flag`

If flag is YES, prints a message to the standard
error device every time a message is sent to a scripted class from
Webscript. If flag is NO, stops printing trace scripted method messages.

__See
Also:__  [- trace:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmu5a), [- traceAssignments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvaxg43jm5xg2zloorztu), [- traceObjectiveCMessages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvhwe2tfmn2gs5tfingwk43tmftwk4z2), [- traceStatements:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvjxiylumvwwk3tuom5a)

---

### traceStatements:

`- (void)traceStatements:(BOOL)flag`

If flag is YES, prints a message to the standard
error device every time a statement in the application is executed
from Webscript. If flag is NO, stops printing trace statement messages.

__See
Also:__  [- trace:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmu5a), [- traceAssignments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvaxg43jm5xg2zloorztu), [- traceObjectiveCMessages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvhwe2tfmn2gs5tfingwk43tmftwk4z2), [- traceScriptedMessages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of52heyldmvjwg4tjob2gkzcnmvzxgylhmvztu)

---

### unlock

`- (void)unlock`

Unlocks the application object.

---

### unlockRequestHandling

`- (void)unlockRequestHandling`

Disables serialized request handler access if
concurrent request handling isn't enabled.

---

## Notifications

---

### WOApplicationDidFinishLaunchingNotification

Posted just before the application
begins waiting for requests. The notification contains the application instance.

The
notification contains the application instance.

### WOApplicationWillFinishLaunchingNotification

Posted when an application has finished
its __init__ method. Register to receive this
notification if you have an object that wishes to set various setting
in the application. For example, if you have a WORequestHandler
implemented in a framework and you want to register it with the
WOApplication, you would register to receive this notification and
then implement a method that register your WORequestHandler with
the application.

The notification contains the application
instance.

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
