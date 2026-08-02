---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOApplication.html
archived_at: '2026-07-15T08:15:15.205997Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOApplication

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSKeyValueCoding: NSKeyValueCoding.ErrorHandling: NSKeyValueCodingAdditions

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

The primary role of the WOApplication class is to coordinate the handling of HTTP requests. Each application must have exactly one WOApplication object (or, simply, application object). The application object receives client requests from an HTTP server adaptor, manages the processing that generates a response, and returns that response-typically an object representing a web page-to the adaptor. The adaptor, in turn, forwards the response in a suitable form to the HTTP server that originated the request.

In handling requests, an application object creates and manages one or more sessions; a session (represented by a WOSession object) dedicates resources to a period of access by a single user and stores persistent state during that period. Conceptually, each cycle of the request-response loop (or transaction) takes place within a session.

Besides acting as a facilitator between the adaptor and the rest of the application during request handling, WOApplication performs many secondary functions. It returns pages based on component name, caches page instances and component definitions, provides some facilities for error handling and script debugging, coordinates the different levels of multi-threaded execution, and furnishes a variety of data.

Typical deployment schemes balance the processing load by having multiple application instances per server adaptor. A single application, in turn, can interact with multiple adaptors; for example, an application can simultaneously communicate with secure-socket and Distributed Object adaptors as well as HTTP adaptors.

You can instantiate ready-made application objects from the WOApplication class or you can obtain the application object from a custom subclass of WOApplication. Custom WOApplication subclasses are common in WebObjects applications since there is often a need to override the [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc53bnnsq), [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxg3dfmvya), and request-handling methods. Compiled WOApplication subclasses can take any name, but if the name is anything other than "Application" you must implement your own __main__ function to instantiate the application object from this class. However, if the class name is "Application," you don't need to modify __main__. In scripted applications, the code in the __Application.wos__ file becomes the implementation logic of a WOApplication subclass automatically created at run time; the application object is instantiated from this subclass.

## Constants

---

WOApplication declares class variables:

|  |  |
| --- | --- |
| __Class Variable__ | __Description__ |
| ApplicationDidDispatchRequestNotification | This class variable contains a String that names the notification posted at the very beginning of WOApplication's __dispatchRequest(WORequest)__ method. |
| ApplicationDidFinishLaunchingNotification | This class variable contains a String that names the notification posted by WOApplication's __run()__ method after the application is launched. This notification is posted when the __run()__ method logs the "Waiting for requests..." message to the console. |
| ApplicationWillDispatchRequestNotification | This class variable contains a String that names the notification posted at the end of WOApplication's __dispatchRequest(WORequest)__ method. |
| ApplicationWillFinishLaunchingNotification | This class variable contains a String that names the notification posted at the very beginning of WOApplication's __run()__ method. |

## Interfaces Implemented

---

> : NSKeyValueCoding: [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxiyllmvlgc3dvmvdg64slmv4q): [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxmylmovsum33sjnsxs): : NSKeyValueCoding.ErrorHandling: [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkulvmvzhsv3jorufk3tcn52w4zclmv4q): [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkvdbnnsvmylmovsum33skvxge33vnzsewzlz): [unableToSetNullForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxk3tbmjwgkvdpknsxittvnrwem33sjnsxs): : NSKeyValueCodingAdditions: [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxiyllmvlgc3dvmvzum4tpnvjgk4lvmvzxi): [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxmylmovsum33sjnsxsudborua):

## Method Types

---

> **Creating**
> : [WOApplication](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxvot2bobygy2ldmf2gs33o)
>
> **Obtaining attributes**
> : [adaptorsDispatchRequestsConcurrently](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwczdbob2g64ttiruxg4dborrwqutfof2wk43uonbw63tdovzhezloorwhs): [allowsConcurrentRequestHandling](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc3dmn53xgq3pnzrxk4tsmvxhiutfof2wk43ujbqw4zdmnfxgo): [isConcurrentRequestHandlingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42dn5xgg5lsojsw45csmvyxkzltoregc3tenruw4z2fnzqwe3dfmq): [baseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxweyltmvkveta): [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw4ylnmu): [number](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw45lnmjsxe): [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxayluna)
>
> **Locking**
> : [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwy33dnm): [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxk3tmn5rww)
>
> **Managing adaptors**
> : [adaptorWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwczdbob2g64sxnf2gqttbnvsq): [adaptors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwczdbob2g64tt)
>
> **Managing sessions**
> : [setSessionStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluknsxg43jn5xfg5dpojsq): [sessionStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzltonuw63storxxezi): [saveSessionForContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgylwmvjwk43tnfxw4rtpojbw63tumv4hi): [restoreSessionWithID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezltorxxezktmvzxg2lpnzlws5dijfca): [createSessionForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwg4tfmf2gku3fonzws33oizxxeutfof2wk43u)
>
> **Managing pages**
> : [setPageCacheSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbqwozkdmfrwqzktnf5gk): [pageCacheSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxaylhmvbwcy3imvjws6tf): [permanentPageCacheSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxazlsnvqw4zloorigcz3finqwg2dfknuxuzi): [setPermanentPageCacheSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbsxe3lbnzsw45cqmftwkq3bmnugku3jpjsq): [setPageRefreshOnBacktrackEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbqwozksmvthezltnbhw4qtbmnvxi4tbmnvuk3tbmjwgkza): [isPageRefreshOnBacktrackEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42qmftwkutfmzzgk43ij5xeeyldnn2heyldnncw4ylcnrswi): [pageWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxaylhmvlws5dijzqw2zi): [pageWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxaylhmvlws5dijzqw2zi)
>
> **Creating elements**
> : [dynamicElementWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwi6lomfwwsy2fnrsw2zloorlws5dijzqw2zi)
>
> **Running**
> : [run](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxe5lo): [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukruw2zkpov2a): [timeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxi2lnmvhxk5a): [defaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlgmf2wy5csmvyxkzltoregc3tenrsxe): [terminate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxizlsnvuw4ylumu): [terminateAfterTimeInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxizlsnvuw4ylumvawm5dfojkgs3lfjfxhizlsozqwy)
>
> **Handling requests**
> : [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc4dqmvxgivdpkjsxg4dpnzzwk): [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc53bnnsq): [createContextForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwg4tfmf2gkq3pnz2gk6duizxxeutfof2wk43u): [createSessionForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwg4tfmf2gku3fonzws33oizxxeutfof2wk43u): [defaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlgmf2wy5csmvyxkzltoregc3tenrsxe): [defaultRequestHandlerClassName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlgmf2wy5csmvyxkzltoregc3tenrsxeq3mmfzxgttbnvsq): [dispatchRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwi2ltobqxiy3ikjsxc5lfon2a): [handlerForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgk4sgn5zfezlrovsxg5a): [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws3twn5vwkqldoruw63q): [registeredRequestHandlerKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlhnfzxizlsmvsfezlrovsxg5cimfxgi3dfojfwk6lt): [registerRequestHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlhnfzxizlskjsxc5lfon2eqylomrwgk4q): [removeRequestHandlerForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlnn53gkutfof2wk43ujbqw4zdmmvzem33sjnsxs): [requestHandlerForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlrovsxg5cimfxgi3dfojdg64slmv4q): [setDefaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluirswmylvnr2fezlrovsxg5cimfxgi3dfoi): [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxg3dfmvya): [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxiyllmvlgc3dvmvzum4tpnvjgk4lvmvzxi)
>
> **Handling errors**
> : [handleSessionCreationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgku3fonzws33oinzgkylunfxw4rlsojxxesloinxw45dfpb2a): [handlePageRestorationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkudbm5svezltorxxeylunfxw4rlsojxxesloinxw45dfpb2a): [handleSessionRestorationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgku3fonzws33okjsxg5dpojqxi2lpnzcxe4tpojew4q3pnz2gk6du): [handleException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkrlymnsxa5djn5xa)
>
> **Script debugging**
> : [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwy33hkn2he2lom4): [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlcovtvg5dsnfxgo): [printsHTMLParserDiagnostics](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxa4tjnz2hgscujvgfaylsonsxerdjmftw433toruwg4y): [setPrintsHTMLParserDiagnostics](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbzgs3tuonefitkmkbqxe43fojcgsylhnzxxg5djmnzq): [logTakeValueForDeclarationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwy33hkrqwwzkwmfwhkzkgn5zeizldnrqxeylunfxw4ttbnvswi): [logSetValueForDeclarationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwy33hknsxivtbnr2wkrtpojcgky3mmfzgc5djn5xe4ylnmvsa)
>
> **Statistics report**
> : [setStatisticsStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukn2gc5djon2gsy3tkn2g64tf): [statisticsStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxg5dboruxg5djmnzvg5dpojsq): [statistics](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxg5dboruxg5djmnzq)
>
> **Monitor support**
> : [monitorEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw233onf2g64sfnzqwe3dfmq): [monitoringEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw233onf2g64tjnztuk3tbmjwgkza): [activeSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwcy3unf3gku3fonzws33oonbw65looq): [refuseNewSessions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlgovzwkttfo5jwk43tnfxw44y): [isRefusingNewSessions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42smvthk43jnztu4zlxknsxg43jn5xhg): [setMinimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujvuw42lnovwucy3unf3gku3fonzws33oonbw65looq): [minimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw22lonfwxk3kbmn2gs5tfknsxg43jn5xhgq3povxhi): [terminateAfterTimeInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxizlsnvuw4ylumvawm5dfojkgs3lfjfxhizlsozqwy)
>
> **Resource manager support**
> : [setResourceManager](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukjsxg33vojrwktlbnzqwozls): [resourceManager](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezltn52xey3fjvqw4ylhmvza)
>
> **User defaults**
> : [loadFrameworks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwy33bmrdheylnmv3w64tlom): [setLoadFrameworks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujrxwczcgojqw2zlxn5zgw4y): [isDebuggingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42emvrhkz3hnfxgorlomfrgyzle): [autoOpenInBrowser](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc5lun5hxazlojfxee4tpo5zwk4q): [setAutoOpenInBrowser](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluif2xi32pobsw4sloijzg653tmvza): [isDirectConnectEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42enfzgky3uinxw43tfmn2ek3tbmjwgkza): [setDirectConnectEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluiruxezldorbw63tomvrxirlomfrgyzle): [cgiAdaptorURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwgz3jifsgc4dun5zfkusm): [setCGIAdaptorURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluindusqlemfyhi33skvjey): [isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42dmfrwq2lom5cw4ylcnrswi): [setCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluinqwg2djnztuk3tbmjwgkza): [applicationBaseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc4dqnruwgylunfxw4qtbonsvkusm): [setApplicationBaseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluifyha3djmnqxi2lpnzbgc43fkvjey): [frameworksBaseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwm4tbnvsxo33snnzueyltmvkveta): [setFrameworksBaseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluizzgc3lfo5xxe23tijqxgzkvkjga): [recordingPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezldn5zgi2lom5igc5di): [setRecordingPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukjswg33smruw4z2qmf2gq): [projectSearchPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxa4tpnjswg5ctmvqxey3ikbqxi2a): [setProjectSearchPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbzg62tfmn2fgzlbojrwqudborua): [isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42nn5xgs5dpojcw4ylcnrswi): [setMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujvxw42lun5zek3tbmjwgkza): [monitorHost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw233onf2g64sin5zxi): [setMonitorHost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujvxw42lun5zeq33toq): [SMTPHost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxvgtkukbeg643u): [setSMTPHost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukngviucin5zxi): [adaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwczdbob2g64q): [setAdaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluifsgc4dun5za): [port](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxa33soq): [setPort](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbxxe5a): [listenQueueSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwy2ltorsw4ulvmv2wku3jpjsq): [setListenQueueSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujruxg5dfnzixkzlvmvjws6tf): [workerThreadCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxo33snnsxevdiojswczcdn52w45a): [setWorkerThreadCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluk5xxe23fojkgq4tfmfseg33vnz2a): [additionalAdaptors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwczdenf2gs33omfweczdbob2g64tt): [setAdditionalAdaptors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluifsgi2lunfxw4ylmifsgc4dun5zhg): [includeCommentsInResponses](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws3tdnr2wizkdn5ww2zloorzus3ssmvzxa33oonsxg): [setIncludeCommentsInResponses](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujfxgg3dvmrsug33nnvsw45dtjfxfezltobxw443fom): [componentRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwg33nobxw4zloorjgk4lvmvzxisdbnzsgyzlsjnsxs): [setComponentRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluinxw24dpnzsw45csmvyxkzltoregc3tenrsxes3fpe): [directActionRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwi2lsmvrxiqldoruw63ssmvyxkzltoregc3tenrsxes3fpe): [setDirectActionRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluiruxezldorawg5djn5xfezlrovsxg5cimfxgi3dfojfwk6i): [resourceRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezltn52xey3fkjsxc5lfon2eqylomrwgk4slmv4q): [setResourceRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukjsxg33vojrwkutfof2wk43ujbqw4zdmmvzewzlz): [sessionTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzltonuw63sunfwwk33voq): [setSessionTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluknsxg43jn5xfi2lnmvhxk5a)
>
> **Convenience Methods**
> : [sharedEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxg2dbojswirlenf2gs3thinxw45dfpb2a)

## Constructors

---

### WOApplication

`public WOApplication()`

Creates and initializes application attributes and initializes the adaptor or adaptors specified on the command line. If no adaptor is specified, WODefaultAdaptor is made the default adaptor. Some of the more interesting attribute initializations are:

- Session store is in the server.
- Page cache size is 30 pages.
- Client caching of pages is enabled ( [isPageRefreshOnBacktrackEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42qmftwkutfmzzgk43ij5xeeyldnn2heyldnncw4ylcnrswi) returns false).

A exception is thrown if initialization does not succeed.

|  |
| --- |
| __Note:__ The global variable "WOApp" is initialized in this method. |

---

## Static Methods

---

### application

`public static WOApplication application()`

Returns a WOApplication object.

You may call this method, but do not override it.

---

### __licensedRequestLimit__

`public static final int licensedRequestLimit()`

This static final method returns an int that represents the request limit license value.

---

### __licensedRequestWindow__

`public static final long licensedRequestWindow()`

This static final method returns a long containing the license value of the request window, in milliseconds (this is the amount of time WebObjects pauses per request once the license limit has been hit).

---

### __licensingAllowsMultipleInstances__

`public static final boolean licensingAllowsMultipleInstances()`

This static final method returns a boolean indicating whether the license allows multiple instances of the application to run simultaneously.

---

### __licensingAllowsMultipleThreads__

`public static final boolean licensingAllowsMultipleThreads()`

This static final method returns a boolean that indicates whether the application is allowed to run in multithreaded mode.

---

### canAccessFieldsDirectly

`public static boolean canAccessFieldsDirectly()`

WOApplication's implementation of this static method returns `true`, indicating that key/value coding is allowed to access fields in this object if an appropriate method isn't present.

---

### __main__

`public static void main(String[] argv[])`

The WebObjects application's main method.

`public static void main(String[] argv[], Class applicationClass)`

An alternate main method for your WebObjects applications that allows you to specify a subclass of WOApplication to be instantiated and run instead of WOApplication.

---

## Instance Methods

---

### activeSessionsCount

`public synchronized int activeSessionsCount()`

Returns the number of sessions that are currently active. (A session is active if it has not yet timed out.)

The number returned here is only accurate if the application stores state in memory in the server, which is the default. If you use a custom state-storage strategy, there may be no way to tell how many sessions are active for a given application instance.

__See Also:__ [minimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw22lonfwxk3kbmn2gs5tfknsxg43jn5xhgq3povxhi), [setMinimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujvuw42lnovwucy3unf3gku3fonzws33oonbw65looq)

---

### adaptorWithName

`public WOAdaptor adaptorWithName( String aName, NSDictionary someArguments)`

Invoked during the constructor to create an adaptor. If you subclass WOAdaptor, you specify the WOAdaptor subclass you want the application to use with the __-a__ option on the application's command line. When WOApplication encounters the __-a__ option, it invokes this method. This method looks for a subclass of WOAdaptor with the name aName (which was supplied as the __-a__ option's argument), and if such a class exists, a new instance is created. The someArguments array is populated with any adaptor-specific options (such as __-p__ or __-q__) that follow the adaptor name on the command line. See the WOAdaptor class for more information.

__See Also:__ [adaptors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwczdbob2g64tt)

---

### adaptor

`public String adaptor()`

Returns the class name of the primary adaptor. This is the cover method for the user default WOAdaptor.

__See Also:__ [setAdaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluifsgc4dun5za)

---

### adaptors

`public NSArray adaptors()`

Returns the current list of application adaptors. A WOApplication can have multiple adaptors. (To associate the WOApplication with multiple adaptors, you specify each adaptor on the application's command line using the __-a__ option.) This allows you to design an application that can not only listen to a socket for incoming HTTP requests (using the WODefaultAdaptor), but can also receive remote request messages using more advanced RPC mechanisms such as DO, CORBA, and DCOM.

---

### adaptorsDispatchRequestsConcurrently

`public final boolean adaptorsDispatchRequestsConcurrently()`

Returns `true` if at least one adaptor contains multiple threads and will attempt to concurrently invoke the request handlers.

---

### additionalAdaptors

`public NSArray additionalAdaptors()`

Returns an array of adaptor description dictionaries. This is the cover method for the user default WOAdditionalAdaptors.

__See Also:__ [setAdditionalAdaptors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluifsgi2lunfxw4ylmifsgc4dun5zhg)

---

### allowsConcurrentRequestHandling

`public boolean allowsConcurrentRequestHandling()`

Override to return `true` if concurrent request handling is allowed.

__See Also:__ [isConcurrentRequestHandlingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42dn5xgg5lsojsw45csmvyxkzltoregc3tenruw4z2fnzqwe3dfmq)

---

### appendToResponse

`public void appendToResponse( WOResponse aResponse, WOContext aContext)`

The WOApplication object sends this message to itself to initiate the last phase of request handling. This occurs right after the __invokeAction__ method has completed, typically with the return a response page. In the append-to-response phase, the application objects (particularly the response component itself) generate the HTML content of the page. WOApplication's default implementation of this method forwards the message to the session object.

__See Also:__ [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws3twn5vwkqldoruw63q)

---

### applicationBaseURL

`public String applicationBaseURL()`

Returns a path to where the current application may be found under the document root (either the project or the __.woa__ wrapper). This is the cover method for the user default WOApplicationBaseURL.

__See Also:__ [setApplicationBaseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluifyha3djmnqxi2lpnzbgc43fkvjey)

---

### autoOpenInBrowser

`public boolean autoOpenInBrowser()`

Returns whether automatic browser launching is enabled. By default, automatic browser launching is enabled.

---

### awake

`public void awake()`

Invoked at the beginning of each cycle of the request-response loop, affording the opportunity to perform initializations with application-wide scope. Since the default implementation does nothing, overridden implementations do not have to call __super__. .

__See Also:__ [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxg3dfmvya)

---

### baseURL

`public String baseURL()`

Returns the application URL relative to the server's document root, for example:
> ```
> WebObjects/Examples/HelloWorld.woa.
> ```

__See Also:__ [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw4ylnmu), [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxayluna)

---

### cgiAdaptorURL

`public String cgiAdaptorURL()`

Returns the URL for the web server including the path to the WebObjects CGI adaptor (for example, __http://localhost/cgi-bin/WebObjects__). This URL is used by the direct connect feature only. This is the cover for the user default WOCGIAdaptorURL.

__See Also:__ [setCGIAdaptorURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluindusqlemfyhi33skvjey)

---

### componentRequestHandlerKey

`public String componentRequestHandlerKey()`

Returns the key which identifies URLs directed at component-action-based requests. By default, this method returns the string "wo".

---

### createContextForRequest

`public WOContext createContextForRequest(WORequestaRequest)`

Creates a new context object for a given request. Override this method if you need to provide your own subclass of WOContext. If you override it, your implementation need not call __super__.

---

### createRequest

`public WORequest createRequest( String aMethod, String aURL, String anHTTPVersion, NSDictionary someHeaders, NSData aContent, NSDictionary someInfo)`

Convenience method that instantiates and returns a new WORequest object.

---

### createResponseInContext

`public WOResponse createResponseInContext(WOContext aContext)`

Convenience method that instantiates and returns a new, empty WOResponse object.

---

### createSessionForRequest

`public WOSession createSessionForRequest(WORequest aRequest)`

Creates and returns a WOSession object to manage a session for the application. The method goes through several steps to locate the class to use for instantiating this object:

1. First it looks for a compiled class of name "Session" that is a subclass of WOSession.
2. If such a class does not exist, it looks for a "__.wos__" script with the name of "Session" in the application wrapper ("__.woa__" directory).
3. If the __Session.wos__ script exists, the method parses the script and dynamically adds a scripted-class subclass of WOSession to the runtime.

The method then returns an allocated and initialized (using the default WOSession constructor) session instance of the selected class. It throws an exception if it is unable to create a new session.

|  |
| --- |
| __Note:__ An implication of the foregoing description is that the names of compiled WOSession subclasses should be "Session"; if not, you will have to override this method to use the proper class to create the session object. |

__See Also:__ [restoreSessionWithID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezltorxxezktmvzxg2lpnzlws5dijfca), [saveSessionForContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgylwmvjwk43tnfxw4rtpojbw63tumv4hi)

---

### defaultRequestHandler

`public WORequestHandler defaultRequestHandler()`

Returns the request handler to be used when no request handler key was found in the URL or WORequest. This method returns the WOComponent request handler by default. When an application is contacted for the first time it is usually via a URL like the following:
> ```
> http://somehost/cgi-bin/WebObjects/AppName.woa
> ```

The way that URLs of that type are handled is determined by the default request handler.

---

### defaultRequestHandlerClassName

`public String defaultRequestHandlerClassName()`

The default implementation of this method returns "WOComponentRequestHandler", which is the default request handler. Override this method to return "WODirectActionRequestHandler" to make the direct action request handler the default.

---

### debugString

`public void debugString(String aFormatString)`

Prints a message to the standard error device (stderr), if __WODebuggingEnabled__ is true. The message can include formatted variable data using String's concatenation feature.

You control whether this method displays output with the __WODebuggingEnabled__ user default option. If __WODebuggingEnabled__ is true, then the __debugString__ messages display their output. If __WODebuggingEnabled__ is false, the __debugString__ messages don't display their output.

---

### directActionRequestHandlerKey

`public String directActionRequestHandlerKey()`

Returns the key which identifies URLs directed at component-based requests. By default, this method returns the string "wa".

---

### dispatchRequest

`public WOResponse dispatchRequest(WORequest aRequest)`

The main entry point for any given interaction. Invoked by the adaptor.

---

### dynamicElementWithName

`public WOElement dynamicElementWithName( String aName, NSDictionary someAssociations, WOElement anElement NSArray languages)`

Creates and returns a WOElement object based on the element's name, a dictionary of associations, and a template of elements. This method is invoked automatically to provide a WOElement object that represents a WEBOBJECT element in the HTML template. You don't ordinarily invoke __dynamicElementWithName__, but you might override it to substitute your own WOElement or reusable component for one of the built-in WOElements.

The arguments aName and someAssociations are derived from a corresponding line in the declarations file. aName is a String that identifies the kind of element to create. Generally aName specifies a built-in WOElement such as WOString, but it may also identify a reusable component. (For more information, see the chapter "Using Reusable Components" in the WebObjects Developer's Guide.) For example, in the __dynamicElementWithName__ message for the following declaration:

> ```
> APP_STRING: WOString {value = applicationString;};
> ```

_aName_ contains the string "WOString".

The someAssociations dictionary contains an entry for each attribute specified in the corresponding declaration. For the declaration above, someAssociations contains a single entry for WOString's value attribute. The keys of someAssociations are the attribute names and the values are WOAssociation objects.

WOApplication's implementation of __dynamicElementWithName__ first searches for a WOElement named _aName_. If a WOElement is found, the method creates an instance and returns it. Otherwise, it searches for a component-either scripted or compiled-to return instead. If neither are found, this method returns `null`.

---

### finalize

`protected void finalize() throws Throwable`

WOApplication's finalizer. This protected method frees up resources that are used internally by the WOApplication object.

---

### frameworksBaseURL

`public String frameworksBaseURL()`

Returns a path to where all frameworks may be found under the document root. This value is used to determine URLs that should be generated to reference Web Server Resources in those frameworks. This is the cover method for the user default WOFrameworksBaseURL.

__See Also:__ [setFrameworksBaseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluizzgc3lfo5xxe23tijqxgzkvkjga)

---

### handleException

`public WOResponse handleException( Exception anException, WOContext aContext)`

Invoked when an exception occurs within the request-response loop. The default behavior displays a page with debugging information. You can override this method to catch exceptions and display a "friendlier" error page.

__See Also:__ [handleSessionCreationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgku3fonzws33oinzgkylunfxw4rlsojxxesloinxw45dfpb2a), [handleSessionRestorationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgku3fonzws33okjsxg5dpojqxi2lpnzcxe4tpojew4q3pnz2gk6du)

---

### handlePageRestorationErrorInContext

`public WOResponse handlePageRestorationErrorInContext(WOContext aContext)`

Invoked when a page (WOComponent) instance cannot be restored, which typically happens when a user backtracks too far. Specifically, this method is invoked when the following occurs: the request is not the first of a session, page restoration by context ID fails, and page re-creation is disabled. The default behavior displays a page with debugging information. You can override this method to display a "friendlier" error page.

__See Also:__ [handleException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkrlymnsxa5djn5xa), [handleSessionCreationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgku3fonzws33oinzgkylunfxw4rlsojxxesloinxw45dfpb2a), [handleSessionRestorationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgku3fonzws33okjsxg5dpojqxi2lpnzcxe4tpojew4q3pnz2gk6du)

---

### handleQueryWithUnboundKey

`public Object handleQueryWithUnboundKey(String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### handleSessionCreationErrorInContext

`public WOResponse handleSessionCreationErrorInContext(WOContext aContext)`

Invoked when a session (WOSession) instance cannot be created. The default behavior displays a page with debugging information. You can override this method to display a "friendlier" error page.

__See Also:__ [handleException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkrlymnsxa5djn5xa), [handlePageRestorationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkudbm5svezltorxxeylunfxw4rlsojxxesloinxw45dfpb2a), [handleSessionRestorationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgku3fonzws33okjsxg5dpojqxi2lpnzcxe4tpojew4q3pnz2gk6du)

---

### handleSessionRestorationErrorInContext

`public WOResponse handleSessionRestorationErrorInContext(WOContext aContext)`

Invoked when a session (WOSession) instance cannot be restored, which typically happens when the session times out. The default behavior displays a page with debugging information. You can override this method to display a "friendlier" error page.

__See Also:__ [handleException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkrlymnsxa5djn5xa), [handlePageRestorationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgkudbm5svezltorxxeylunfxw4rlsojxxesloinxw45dfpb2a), [handleSessionCreationErrorInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgku3fonzws33oinzgkylunfxw4rlsojxxesloinxw45dfpb2a)

---

### handleTakeValueForUnboundKey

`public void handleTakeValueForUnboundKey(Object value, String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### handlerForRequest

`public WORequestHandler handlerForRequest(WORequest aRequest)`

Returns the request handler used to handle a given request.

__See Also:__ [registerRequestHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlhnfzxizlskjsxc5lfon2eqylomrwgk4q), [registeredRequestHandlerKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlhnfzxizlsmvsfezlrovsxg5cimfxgi3dfojfwk6lt), [requestHandlerForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlrovsxg5cimfxgi3dfojdg64slmv4q)

---

### includeCommentsInResponses

`public boolean includeCommentsInResponses()`

Returns whether or not HTML comments are appended to the response. This is the cover method for the user default WOIncludeCommentsInResponses.

__See Also:__ [setIncludeCommentsInResponses](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujfxgg3dvmrsug33nnvsw45dtjfxfezltobxw443fom)

---

### invokeAction

`public WOActionResults invokeAction( WORequest aRequest, WOContext aContext)`

The WOApplication object sends this message to itself to initiate the middle phase of request handling. In this phase, the message is propagated through the objects of the application until the dynamic element that has received the user action (for instance, a click on a button) responds to the message by triggering the method in the request component that is bound to the action. The default WOApplication implementation of this method forwards the message to the session object.

__See Also:__ [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc4dqmvxgivdpkjsxg4dpnzzwk)

---

### isCachingEnabled

`public boolean isCachingEnabled()`

Returns whether or not component caching is enabled. If this is enabled, changes to a component will be reparsed after being saved (assuming the project is under the NSProjectSearchPath). Note that this has no effect on page caching. This is the cover method for the user default WOCachingEnabled.

__See Also:__ [setCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluinqwg2djnztuk3tbmjwgkza), [pageCacheSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxaylhmvbwcy3imvjws6tf)

---

### isConcurrentRequestHandlingEnabled

`public final boolean isConcurrentRequestHandlingEnabled()`

Returns `true` if adaptors dispatch requests concurrently and [allowsConcurrentRequestHandling](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc3dmn53xgq3pnzrxk4tsmvxhiutfof2wk43ujbqw4zdmnfxgo) has been overridden to allow concurrent request handling.

__See Also:__ [allowsConcurrentRequestHandling](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc3dmn53xgq3pnzrxk4tsmvxhiutfof2wk43ujbqw4zdmnfxgo)

---

### isDebuggingEnabled

`public boolean isDebuggingEnabled()`

Returns whether or not debugging is enabled. If `true`, [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlcovtvg5dsnfxgo) prints out. Most startup-time status message are supressed if this method returns `false`. By default, debugging is enabled. This is the cover method for the user default WODebuggingEnabled.

__See Also:__ [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlcovtvg5dsnfxgo)

---

### isDirectConnectEnabled

`public boolean isDirectConnectEnabled()`

Returns whether or not direct connect is enabled. By default it is enabled. For more information, see [setDirectConnectEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluiruxezldorbw63tomvrxirlomfrgyzle).

__See Also:__ [cgiAdaptorURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwgz3jifsgc4dun5zfkusm)

---

### isMonitorEnabled

`public boolean isMonitorEnabled()`

Returns whether or not the application can communicate with a Monitor application. It returns `true` if the application can contact Monitor upon startup and subsequently let Monitor gather statistics. It returns `false` if no communication with Monitor can take place. By default, it can communicate with a Monitor application. 'This is a cover method for the user default WOMonitorEnabled.

__See Also:__ [setMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujvxw42lun5zek3tbmjwgkza), [monitorHost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw233onf2g64sin5zxi), [setMonitorHost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujvxw42lun5zeq33toq)

---

### isPageRefreshOnBacktrackEnabled

`public boolean isPageRefreshOnBacktrackEnabled()`

Returns whether caching of pages is disabled in the client. If so, the client does not restore request pages from its cache but re-creates them "from scratch" by resending the URL to the server. This flag is set to `false` by default.

__See Also:__ [setPageRefreshOnBacktrackEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbqwozksmvthezltnbhw4qtbmnvxi4tbmnvuk3tbmjwgkza)

---

### isRefusingNewSessions

`public boolean isRefusingNewSessions()`

Returns `true` if the application instance is refusing new sessions, and `false` otherwise. When the application instance refuses new sessions, the WebObjects adaptor tries to start the session in another instance of the same application. If no other instance is running and accepting new sessions, the user receives an error message.

---

### isTerminating

`public boolean isTerminating()`

Returns whether the application will terminate at the end of the current request-response loop.

__See Also:__ [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukruw2zkpov2a), [defaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlgmf2wy5csmvyxkzltoregc3tenrsxe), [terminateAfterTimeInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxizlsnvuw4ylumvawm5dfojkgs3lfjfxhizlsozqwy), [timeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxi2lnmvhxk5a)

---

### __lifebeatDestinationPort__

`public int lifebeatDestinationPort()`

Returns an int indicating the port to which application lifebeat signals are to be sent. This port value is controlled by the `WOLifebeatDestinationPort` key and by the __setLifebeatDestinationPort(int)__ method.

---

### lifebeatEnabled

`public boolean lifebeatEnabled()`

Description forthcoming.

---

### lifebeatInterval

`public int lifebeatInterval()`

Description forthcoming.

---

### listenQueueSize

`public Number listenQueueSize()`

Returns the size of the listen queue which will created by the primary adaptor (usually WODefaultAdaptor). This is the cover method for the user default WOListenQueueSize.

__See Also:__ [setListenQueueSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujruxg5dfnzixkzlvmvjws6tf)

---

### loadFrameworks

`public NSArray loadFrameworks()`

Returns the array of frameworks to be loaded during application initialization.

__See Also:__ [setLoadFrameworks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujrxwczcgojqw2zlxn5zgw4y)

---

### lock

`public void lock()`

Locks the application object.

---

### logSetValueForDeclarationNamed

`public void logSetValueForDeclarationNamed( String aDeclarationName, String aDeclarationType, String aBindingName, String anAssociationDescription, Object aValue)`

Formats and logs a message anytime a value is set through a WOAssociation, when WODebug is set to `true` for the declaration in which the association appears. (Setting a value means the child component/element is setting a value in the parent). See [logTakeValueForDeclarationNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwy33hkrqwwzkwmfwhkzkgn5zeizldnrqxeylunfxw4ttbnvswi) for a description of each of the arguments to this method.

---

### logString

`public void logString(String aString)`

Prints a message to the standard error device (stderr). The message can include formatted variable data using String's concatenation feature, for example:
> ```
> int i = 500;
> float f = 2.045;
> WOApplication.logString("Amount = " + i + ", Rate = " + f ", Total = " + i*f);
> ```

---

### logTakeValueForDeclarationNamed

`public void logTakeValueForDeclarationNamed( String aDeclarationName, String aDeclarationType, String aBindingName, String anAssociationDescription, Object aValue)`

Formats and logs a message anytime a value is "taken" through a WOAssociation , when WODebug is set to `true` for the declaration in which the association appears. (Taking a value means the child component/element is taking a value from the parent). Override this method to alter the format of the log message. The arguments of this method are defined in the following example of a WebObjects declaration.
> ```
> aDeclarationName : aDeclarationType {
>     aBindingName = anAssociationDescription;
> }
> ```

Also, _aValue_ is the value which is being pushed to or pulled from the child to the parent.

---

### __maxSocketIdleTime__

`public Number maxSocketIdleTime()`

Returns a Number indicating the maximum amount of time a socket is allowed to idle. This value is controlled by the `WOMaxSocketIdleTime` key and by the __setMaxSocketIdleTime(Number)__ method.

__See Also:__ [setMaxSocketIdleTime](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujvqxqu3pmnvwk5cjmrwgkvdjnvsq)

---

### minimumActiveSessionsCount

`public int minimumActiveSessionsCount()`

Returns the minimum number of active sessions allowed. If the number of active sessions is less than or equal to this number and [isRefusingNewSessions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42smvthk43jnztu4zlxknsxg43jn5xhg) is `true`, the application instance terminates. The default is 0.

__See Also:__ [activeSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwcy3unf3gku3fonzws33oonbw65looq), [refuseNewSessions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlgovzwkttfo5jwk43tnfxw44y), [setMinimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujvuw42lnovwucy3unf3gku3fonzws33oonbw65looq)

---

### monitorEnabled

`public boolean monitorEnabled()`

Description forthcoming.

---

### monitoringEnabled

`public boolean monitoringEnabled()`

Returns `true` if the application is "monitorable" by the Monitor application, and `false` otherwise. An application is "monitorable" if it was able to find a running Monitor upon startup and it is able to successfully communicate with that Monitor.

By default, all applications are monitorable if the Monitor application is running on the same machine as the application. You can specifically disable monitoring using the -WOMonitorEnabled NO option on the application command line. If you want the application to be monitorable and the Monitor is running on another host, you can start up the application through Monitor, or you can specify Monitor's host on the application command line this way:

> ```
> MyApp.exe -WOMonitorEnabled YES -WOMonitorHost monitorHost ...
> ```

---

### monitorHost

`public String monitorHost()`

Returns the host on which Monitor is assumed to be running. This value is used during initialization if [isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42nn5xgs5dpojcw4ylcnrswi) returns `true`. This is a cover for the user default WOMonitorHost.

__See Also:__ [setMonitorHost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujvxw42lun5zeq33toq), [isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42nn5xgs5dpojcw4ylcnrswi)

---

### name

`public String name()`

Returns the name of the application, which is the name of the executable (without the .exe extension).

__See Also:__ [baseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxweyltmvkveta), [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxayluna)

---

### number

`public String number()`

Returns "-1". This is provided for backwards compatibility only.

---

### outputPath

`public String outputPath()`

Description forthcoming.

---

### pageCacheSize

`public int pageCacheSize()`

Returns the size of the internal cache for page instances. The default size is 30 instances.

__See Also:__ [setPageCacheSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbqwozkdmfrwqzktnf5gk)

---

### pageWithName

`public WOComponent pageWithName( String aName, WORequest aRequest)`

Returns a new page instance (a WOComponent object) identified by aName. If aName is `null`, the "Main" component is assumed. If the method cannot create a valid page instance, it `throws` an exception.

As part of its implementation, this method creates a context with _aRequest_ and calls [pageWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxaylhmvlws5dijzqw2zi).

__See Also:__ restorePageForContextID (WOSession), savePage (WOSession)

---

### pageWithName

`public WOComponent pageWithName( String aName, WOContext aContext)`

Returns a new page instance (a WOComponent object) identified by aName. If aName is `null`, the "Main" component is assumed. If the method cannot create a valid page instance, it `throws` an exception.

__See Also:__ [pageWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxaylhmvlws5dijzqw2zi), restorePageForContextID (WOSession), savePage (WOSession)

---

### path

`public String path()`

Returns the file system path of the application, which is an absolute path and includes the "__.woa__" extension; for example "__C:/NETSCAPE/ns-home/docs/WebObjects/Examples/HelloWorld.woa__" is a typical application path.

__See Also:__ [baseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxweyltmvkveta), [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw4ylnmu)

---

### permanentPageCacheSize

`public int permanentPageCacheSize()`

Returns the permanent page cache size. The default is 30. The permanent page cache holds pages which should not fall out of the regular page cache. For example, a control page in a frameset should exist for the duration of a session.

__See Also:__ savePageInPermanentCache ( [WOApplication](#apple-k5huc4dqnruwgylunfxw4))

---

### port

`public Number port()`

Returns the port number on which the primary adaptor will listen (usually WODefaultAdaptor). This is the cover method for the user default WOPort.

__See Also:__ [setPort](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbxxe5a)

---

### printsHTMLParserDiagnostics

`public boolean printsHTMLParserDiagnostics()`

Returns whether the HTML parser prints diagnostic information to stdout when it encounters unbalanced HTML containers or other syntactically incorrect HTML. This method returns `false` by default.

__See Also:__ [isDebuggingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42emvrhkz3hnfxgorlomfrgyzle) [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlcovtvg5dsnfxgo)

---

### projectSearchPath

`public NSArray projectSearchPath()`

Returns an array of file system paths which are searched for projects for rapid turnaround mode. This is the cover method for the user default NSProjectSearchPath.

__See Also:__ [setProjectSearchPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbzg62tfmn2fgzlbojrwqudborua)

---

### recordingPath

`public String recordingPath()`

Returns a file system path which is where the recording information should be saved. By default, this method returns `null`.

If this method returns a path, all requests and responses are recorded in the HTTP format in numbered files (__0000-request__, __0000-response__, __0001-request__, __0001-response__, and so on), and saved under the recording path specified. This directory is then used by the Playback tool to test the application. You will most likely set this as a command line argument (-WORecordingPath pathname), exercise your application to record a scenario you would like to test, and then stop the application. Afterward you can restart the application without the WORecordingPath argument, and point Playback to the recording directory just created to replay your sequence of requests and compare the responses received with the ones recorded.

__See Also:__ [setRecordingPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukjswg33smruw4z2qmf2gq)

---

### refuseNewSessions

`public synchronized void refuseNewSessions(boolean flag)`

Controls whether this application instance will create a session when it receives an HTTP request from a new user. If _flag_ is `true`, the application does not create new sessions; when it receives a request from a new user, it refuses that request, and the adaptor must try to find another application instance that can process the request. If _flag_ is `false`, the application creates new sessions. `false` is the default.

You use this method with __setMinimumActiveSessionsCount__ to gracefully shut down application instances. Use __setMinimumActiveSessionsCount__ to set the active session minimum to a certain number. When number of active sessions reaches the number you set and __isRefusingNewSessions__ returns `true`, the application terminates.

__See Also:__ [activeSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwcy3unf3gku3fonzws33oonbw65looq), [isRefusingNewSessions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42smvthk43jnztu4zlxknsxg43jn5xhg), [minimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw22lonfwxk3kbmn2gs5tfknsxg43jn5xhgq3povxhi), [setMinimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlujvuw42lnovwucy3unf3gku3fonzws33oonbw65looq)

---

### registerRequestHandler

`public void registerRequestHandler( WORequestHandler aHandler, String aKey)`

Registers a new request handler. _aKey_ must specify a key which can be found in the URLs following the instance number or application name.

__See Also:__ [removeRequestHandlerForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlnn53gkutfof2wk43ujbqw4zdmmvzem33sjnsxs), [registeredRequestHandlerKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlhnfzxizlsmvsfezlrovsxg5cimfxgi3dfojfwk6lt), [requestHandlerForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlrovsxg5cimfxgi3dfojdg64slmv4q)

---

### registeredRequestHandlerKeys

`public NSArray registeredRequestHandlerKeys()`

Returns an array of strings containing the keys of all of the registered request handlers.

__See Also:__ [handlerForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgk4sgn5zfezlrovsxg5a), [requestHandlerForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlrovsxg5cimfxgi3dfojdg64slmv4q)

---

### removeRequestHandlerForKey

`public WORequestHandler removeRequestHandlerForKey(String aRequestHandlerKey)`

Removes the specified request handler from the application.

__See Also:__ [registerRequestHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlhnfzxizlskjsxc5lfon2eqylomrwgk4q), [requestHandlerForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlrovsxg5cimfxgi3dfojdg64slmv4q)

---

### requestHandlerForKey

`public WORequestHandler requestHandlerForKey(String key)`

Returns the request handler used to handle requests containing the specified key.

__See Also:__ [handlerForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwqylomrwgk4sgn5zfezlrovsxg5a), [registerRequestHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlhnfzxizlskjsxc5lfon2eqylomrwgk4q), [registeredRequestHandlerKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlhnfzxizlsmvsfezlrovsxg5cimfxgi3dfojfwk6lt)

---

### requestHandlingLock

`public Object requestHandlingLock()`

Returns an Object suitable for a synchronization lock, or `null` if the application isn't multithreaded.

---

### resourceManager

`public WOResourceManager resourceManager()`

Returns the WOResourceManager object that the application uses to manage resources.

__See Also:__ [setResourceManager](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukjsxg33vojrwktlbnzqwozls)

---

### resourceRequestHandlerKey

`public String resourceRequestHandlerKey()`

Returns the key which identifies URLs directed through the resource request handler. Resource requests are only used during development of an application when the application is being run without an HTTP server.

__See Also:__ [setResourceRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukjsxg33vojrwkutfof2wk43ujbqw4zdmmvzewzlz)

---

### restoreSessionWithID

`public WOSession restoreSessionWithID( String aSessionID, WOContext aContext)`

Restores the WOSession object representing a session. In normal request handling, this method is invoked at the start of a cycle of the request-response loop. The default implementation simply invokes WOSessionStore's checkOutSessionWithID method, but raises an exception if the WOSessionStore object is missing.

__See Also:__ [createSessionForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwg4tfmf2gku3fonzws33oizxxeutfof2wk43u), [saveSessionForContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgylwmvjwk43tnfxw4rtpojbw63tumv4hi)

---

### run

`public void run()`

Runs the application in a near-indefinite run loop in the default run-loop mode. Before starting the run loop, the method sends registerForEvents to the application's adaptors so that they can begin receiving run-loop events. Normally, [run](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxe5lo) is invoked in the main function.

__See Also:__ [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukruw2zkpov2a), [defaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlgmf2wy5csmvyxkzltoregc3tenrsxe), [terminateAfterTimeInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxizlsnvuw4ylumvawm5dfojkgs3lfjfxhizlsozqwy)

---

### saveSessionForContext

`public void saveSessionForContext(WOContext aContext)`

Called at the end of the request handling loop, when the current session object needs to be saved. The default implementation simply invokes WOSessionStore's checkInSessionForContext method, but throws an exception if the WOSessionStore object is missing.

__See Also:__ [restoreSessionWithID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezltorxxezktmvzxg2lpnzlws5dijfca)

---

### sessionStore

`public WOSessionStore sessionStore()`

Returns the application's current WOSessionStore object (which, by default, stores state in the server).

__See Also:__ [setSessionStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluknsxg43jn5xfg5dpojsq)

---

### __sessionStoreClassName__

`public String sessionStoreClassName()`

Returns, as a String, the value of the `WOSessionStoreClassName` key. The default value for this key is "WOServerSessionStore".

---

### sessionTimeout

`public Number sessionTimeOut()`

Returns the number (of seconds) which will be used as the default timeout for each newly created session. You may either override this method, change the user default WOSessionTimeOut, or set the session timeout in your session's __init__ method.

__See Also:__ [setSessionTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluknsxg43jn5xfi2lnmvhxk5a)

---

### setAdaptor

`public void setAdaptor(String anAdaptorName)`

Sets the the class name of the primary adaptor to _anAdaptorName_.

__See Also:__ [adaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwczdbob2g64q)

---

### setAdditionalAdaptors

`public void setAdditionalAdaptors(NSArray anAdaptorPlist)`

Sets the array of adaptor description dictionaries to _anAdaptorPlist_. Each adaptor description dictionary must have "WOAdaptor" defined, which is the name of the adaptor class. Other attributes such as WOPort may also be specified, but are adaptor specific. For example WOWorkerThreadCount is specific to the WODefaultAdaptor class and may not apply for all adaptors.

__See Also:__ [additionalAdaptors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwczdenf2gs33omfweczdbob2g64tt)

---

### setAllowsConcurrentRequestHandling

`public void setAllowsConcurrentRequestHandling(boolean aValue)`

Explicitly specifies whether concurrent request handling is allowed. If your code does not invoke this method, the value of the `WOAllowsConcurrentRequestHandling` (interpreted as a boolean) determines whether concurrent request handling is allowed.

---

### setApplicationBaseURL

`public void setApplicationBaseURL(String aBaseURL)`

Sets to _aBaseURL_ the path to which the current application may be found under the document root (either the project or the __.woa__ wrapper).

__See Also:__ [applicationBaseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc4dqnruwgylunfxw4qtbonsvkusm)

---

### setAutoOpenInBrowser

`public void setAutoOpenInBrowser(boolean isEnabled)`

Controls whether starting up this application also launches a web browser. If isEnabled is `true`, the application launches the web browser. If `false`, the application does not launch the browser. Browser launching is enabled by default as long as there is a WOAdaptorURL key in the file __NeXT_ROOT/NextLibrary/WOAdaptors/Configuration/WebServerConfig.plist__.

To disable web browser launching, you must send this message in your subclass's constructor.

__See Also:__ [autoOpenInBrowser](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc5lun5hxazlojfxee4tpo5zwk4q)

---

### setCachingEnabled

`public void setCachingEnabled(boolean flag)`

Sets whether or not component caching is enabled. If this is enabled, changes to a component will be reparsed after being saved (assuming the project is under the NSProjectSearchPath). Note that this has no effect on page caching.

__See Also:__ [isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42dmfrwq2lom5cw4ylcnrswi), [pageCacheSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxaylhmvbwcy3imvjws6tf)

---

### setCGIAdaptorURL

`public void setCGIAdaptorURL(String aURL)`

Sets the URL for the web server to _aURL_. The URL must include the path to the WebObjects CGI adaptor (for example, __http://localhost/cgi-bin/WebObjects__). This URL is used by the direct connect feature only..

__See Also:__ [cgiAdaptorURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwgz3jifsgc4dun5zfkusm)

---

### setComponentRequestHandlerKey

`public void setComponentRequestHandlerKey(String key)`

Sets the component request handler key. This affects all URLs generated during [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc4dqmvxgivdpkjsxg4dpnzzwk): of component-based actions.

__See Also:__ [componentRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwg33nobxw4zloorjgk4lvmvzxisdbnzsgyzlsjnsxs)

---

### setDefaultRequestHandler

`public void setDefaultRequestHandler(WORequestHandler aHandler)`

Sets the default request handler.

__See Also:__ [defaultRequestHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlgmf2wy5csmvyxkzltoregc3tenrsxe)

---

### setDirectActionRequestHandlerKey

`public void setDirectActionRequestHandlerKey(String key)`

Sets the Direct Action request handler key. This affects all URLs generated during [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc4dqmvxgivdpkjsxg4dpnzzwk): of direct actions.

__See Also:__ [directActionRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwi2lsmvrxiqldoruw63ssmvyxkzltoregc3tenrsxes3fpe)

---

### setDirectConnectEnabled

`public void setDirectConnectEnabled(boolean flag)`

Sets whether or not direct connect is enabled. By default it is enabled.

Direct connect actually transforms your application in a simple web server of its own. In particular, it is then able to find and return its images and resources as if it were a web server. It is very useful in development mode: You don't need a web server. Just point your URL to the port where your application is listening, and the application will handle all urls.

If this flag is `true`, the following happens:

- When using [autoOpenInBrowser](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc5lun5hxazlojfxee4tpo5zwk4q), a direct connect URL will be used.
- When using WOMailDelivery to mail pages with dynamic links in them, these links will be generated with a complete direct connect URL format. People receiving these mails will be able to access the application with direct connect.
- All files on the system are accessible through the resource request handler. On the other hand, if this flag is `false`, the resource request handler can be used to retrieve data objects from memory only, and no more reading in the file system is permitted (secure mode for deployment).

__See Also:__ [isDirectConnectEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42enfzgky3uinxw43tfmn2ek3tbmjwgkza), [cgiAdaptorURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwgz3jifsgc4dun5zfkusm)

---

### setFrameworksBaseURL

`public void setFrameworksBaseURL(String aString)`

Sets to _aString_ the path to where all frameworks may be found under the document root. This value is used to determine URLs that should be generated to reference Web Server Resources in those frameworks.

__See Also:__ [frameworksBaseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwm4tbnvsxo33snnzueyltmvkveta)

---

### setIncludeCommentsInResponses

`public void setIncludeCommentsInResponses(boolean flag)`

Sets whether or not HTML comments are appended to the response.

__See Also:__ [includeCommentsInResponses](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws3tdnr2wizkdn5ww2zloorzus3ssmvzxa33oonsxg)

---

### setListenQueueSize

`public void setListenQueueSize(Number aListenQueueSize)`

Sets the size of the listen queue which will created by the primary adaptor (usually WODefaultAdaptor).

__See Also:__ [listenQueueSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwy2ltorsw4ulvmv2wku3jpjsq)

---

### setLoadFrameworks

`public void setLoadFrameworks(NSArray frameworkList)`

Sets the array of frameworks to be loaded during application initialization.

__See Also:__ [loadFrameworks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwy33bmrdheylnmv3w64tlom)

---

### setMaxSocketIdleTime

`public void setMaxSocketIdleTime(Number maxSocketIdleTime)`

Specifies the maximum amount of time a socket should be allowed to idle. The value specified to this method takes precedence over the `WOMaxSocketIdleTime` key.

---

### setMinimumActiveSessionsCount

`public void setMinimumActiveSessionsCount(int anInt)`

Sets the minimum number of active sessions to _anInt_. The default is 0.

You use this method to gracefully shut down application instances. If the active sessions count reaches this number and__isRefusingNewSessions__ returns `true`, the application terminates. You might want to terminate application instances periodically for performance reasons; some applications leak a certain amount of memory per transaction, and shutting down and restarting instances of those applications can free up that memory.

__See Also:__ [activeSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwcy3unf3gku3fonzws33oonbw65looq), [isRefusingNewSessions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42smvthk43jnztu4zlxknsxg43jn5xhg), [minimumActiveSessionsCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw22lonfwxk3kbmn2gs5tfknsxg43jn5xhgq3povxhi), [refuseNewSessions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezlgovzwkttfo5jwk43tnfxw44y)

---

### setMonitorEnabled

`public void setMonitorEnabled(boolean flag)`

Sets whether or not the application will communicate with a Monitor application. If _flag_ is `true`, the application can contact Monitor upon startup and subsequently let Monitor gather statistics. If _flag_ is `false`, no comunication with Monitor can take place. By default, it can communicate with a Monitor application.

__See Also:__ [isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42nn5xgs5dpojcw4ylcnrswi)

---

### setMonitorHost

`public void setMonitorHost(String hostName)`

Sets the host on which Monitor is assumed to be running. This value is used during initialization if [isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42nn5xgs5dpojcw4ylcnrswi) returns `true`.

__See Also:__ [monitorHost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxw233onf2g64sin5zxi), [isMonitorEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42nn5xgs5dpojcw4ylcnrswi)

---

### setPageCacheSize

`public void setPageCacheSize(int anInt)`

Sets whether caching of page instances will occur and the number of pages the cache will hold. When page-instance caching is enabled, the application stores the WOComponent instance corresponding to the response page in the session. When the page is backtracked to, it restores it from the session and makes it the request page. The state of the page is retained. By default, page-instance caching is enabled, with a cache limit of 30 pages.

You turn page-instance caching off by invoking this method with an argument of zero. In this case, when the user backtracks to a page, the page is not stored in the session and so must be re-created "from scratch."

__See Also:__ [pageCacheSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxaylhmvbwcy3imvjws6tf)

---

### setPageRefreshOnBacktrackEnabled

`public void setPageRefreshOnBacktrackEnabled(boolean flag)`

When _flag_ is `true`, disables caching of pages by the client by setting the page's expiration-time header to the current date and time. (By default, this attribute is set to `false`.) Disabling of client caching affects what happens during backtracking. With client caching turned off, the browser resends the URL to the server for the page requested by backtracking. The application must return a new page to the browser (corresponding to a new WOComponent instance). This behavior is desirable when you do not want the user to backtrack to a page that might be obsolete because of changes that have occurred in the session.

When this flag is turned on and a request corresponding to a client backtrack occurs, the retrieved page will only be asked to regenerate its response. The first two phases of a normal request-response loop (value extraction from the request and action invocation) do not occur.

See Caching Strategies in the class description for further details.

__See Also:__ [isPageRefreshOnBacktrackEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42qmftwkutfmzzgk43ij5xeeyldnn2heyldnncw4ylcnrswi)

---

### setPermanentPageCacheSize

`public void setPermanentPageCacheSize(int aSize)`

Sets the permanentPageCacheSize to aSize

__See Also:__ [permanentPageCacheSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxazlsnvqw4zloorigcz3finqwg2dfknuxuzi)

---

### setPort

`public void setPort(Number port)`

Sets the port number on which the primary adaptor will listen (usually WODefaultAdaptor).

__See Also:__ [port](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxa33soq)

---

### setPrintsHTMLParserDiagnostics

`public void setPrintsHTMLParserDiagnostics(boolean flag)`

Sets whether the HTML parser prints diagnostic information to stdout when it encounters unbalanced HTML containers or other syntactically incorrect HTML. This diagnostic information is not printed by default.

__See Also:__ [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwizlcovtvg5dsnfxgo)

---

### setProjectSearchPath

`public void setProjectSearchPath(NSArray searchPath)`

Sets the array of file system paths which are searched for projects for rapid turnaround mode.

__See Also:__ [projectSearchPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxa4tpnjswg5ctmvqxey3ikbqxi2a)

---

### setRecordingPath

`public void setRecordingPath(String path)`

Sets the file system path where the recording information should be saved. Use `null` as the path if you don't want to save recording information. By default, recording information is not saved.

If you save recording information, all requests and responses are recorded in the HTTP format in numbered files (__0000-request__, __0000-response__, __0001-request__, __0001-response__, and so on), and saved under the recording path specified. This directory is then used by the Playback tool to test the application. You will most likely set this as a command line argument (-WORecordingPath pathname), exercise your application to record a scenario you would like to test, and then stop the application. Afterward you can restart the application without the WORecordingPath argument, and point Playback to the recording directory just created to replay your sequence of requests and compare the responses received with the ones recorded.

__See Also:__ [recordingPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezldn5zgi2lom5igc5di)

---

### setResourceManager

`public void setResourceManager(WOResourceManager aResourceManager)`

Sets the WOResourceManager object to _aResourceManager_. WOResourceManager objects search for and retrieve resources from the application directory and from shared framework directories.

__See Also:__ [resourceManager](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezltn52xey3fjvqw4ylhmvza)

---

### setResourceRequestHandlerKey

`public void setResourceRequestHandlerKey(String key)`

Sets the resource request handler key. This affects all URLs generated during [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc4dqmvxgivdpkjsxg4dpnzzwk) of resources.

__See Also:__ [resourceRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxezltn52xey3fkjsxc5lfon2eqylomrwgk4slmv4q)

---

### setSessionStore

`public void setSessionStore(WOSessionStore aSessionStore)`

Set the session-store object for the application. By default, an object that stores session state in process memory (that is, in the server) is used. The session-store object specifies the state storage strategy for the whole application. This object is responsible for making session objects persistent. You should set the session store object when the application starts up, before the first request is handled.

__See Also:__ [sessionStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzltonuw63storxxezi)

---

### setSessionStoreClassName

`public void setSessionStoreClassName(String aString)`

Sets the name of the session store class to the specified name. The value specified to this method takes precedence over the `WOSessionStoreClassName` key.

---

### setSessionTimeOut

`public void setSessionTimeOut(Number aTimeOut)`

Accessor to set the default session timeOut.

__See Also:__ [sessionTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzltonuw63sunfwwk33voq)

---

### setSMTPHost

`public void setSMTPHost(String hostName)`

Sets the name of the host that will be used to send e-mail messages created by WOMailDelivery.

__See Also:__ [SMTPHost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxvgtkukbeg643u)

---

### setSocketCacheSize

`public void setSocketCacheSize(Number socketCacheSize)`

Specifies the maximum number of sockets to retain in the socket cache. If you don't explicitly specify the number of sockets with this method, the socket cache size will be determined by the value of the `WOSocketCacheSize` key, which has a default value of 100.

---

### setSocketMonitorSleepTime

`public void setSocketMonitorSleepTime(Number socketMonitorSleepTime)`

Sets the length of time (in milliseconds) that the socket monitor will sleep in order to allow the worker threads to operate. If you don't invoke this method, the value of the `WOSocketMonitorSleepTime` key will be used (the default value for this key is 50 msec).

---

### setStatisticsStore

`public void setStatisticsStore(WOStatisticsStore aStatisticsStore)`

Sets the WOStatisticsStore object to _aStatisticsStore_. WOStatisticsStore objects record application statistics while the application runs.

__See Also:__ [statisticsStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxg5dboruxg5djmnzvg5dpojsq)

---

### setWorkerThreadCount

`public void setWorkerThreadCount(Number aWorkerThreadCount)`

SEts the count of worker threads which will created by the primary adaptor (usually WODefaultAdaptor). A worker thread count of 0 implies single-threaded mode.

__See Also:__ [workerThreadCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxo33snnsxevdiojswczcdn52w45a)

---

### setTimeOut

`public void setTimeOut(double aTimeInterval)`

Sets the number of seconds the application can experience inactivity (no HTTP requests) before it terminates execution.

This method differs from [terminateAfterTimeInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxizlsnvuw4ylumvawm5dfojkgs3lfjfxhizlsozqwy) in that with this method, the application must be idle for _aTimeInterval_ seconds for the application to terminate. [terminateAfterTimeInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxizlsnvuw4ylumvawm5dfojkgs3lfjfxhizlsozqwy) terminates the application whether it is active or not.

__See Also:__ [timeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxi2lnmvhxk5a)

---

### sharedEditingContext

`public com.webobjects.eocontrol.EOSharedEditingContext sharedEditingContext()`

This is a convenience method that returns the default shared editing context.

__See Also:__ EOSharedEditingContext class description in the EOControl Framework

---

### sleep

`public void sleep()`

Invoked at the conclusion of a request-handling cycle to give an application the opportunity for deallocating objects created and initialized in its awake method. The default implementation does nothing.

---

### SMTPHost

`public String SMTPHost()`

Returns the name of the host that will be used to send e-mail messages created by WOMailDelivery. This is the cover method for the user default WOSMTPHost.

__See Also:__ [setSMTPHost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukngviucin5zxi)

---

### __socketCacheSize__

`public Number socketCacheSize()`

Returns a Number indicating the maximum number of sockets that can be held in the socket cache. The default cache size is 100.

__See Also:__ [setSocketCacheSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluknxwg23forbwcy3imvjws6tf)

---

### __socketMonitorSleepTime__

`public Number socketMonitorSleepTime()`

Returns a Number indicating the length of time (in milliseconds) that the socket monitor will sleep in order to allow the worker threads to operate. The default is 50 milliseconds.

__See Also:__ [setSocketMonitorSleepTime](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluknxwg23forgw63tjorxxeu3mmvsxavdjnvsq)

---

### statistics

`public NSDictionary statistics()`

Returns a copy of the dictionary containing the application statistics maintained by WOStatisticsStore. This method is used by the Monitor application to retrieve application statistics. If you need to access the statistics internally, use this message instead:
> ```
> WOApplication.application().statisticsStore().statistics()
> ```

---

### statisticsStore

`public WOStatisticsStore statisticsStore()`

Returns the WOStatisticsStore object, which records statistics while the application runs.

__See Also:__ [setStatisticsStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukn2gc5djon2gsy3tkn2g64tf)

---

### takeValueForKey

`public void takeValueForKey(Object value, String key)`

Conformance to NSKeyValueCoding.

---

### takeValueForKeyPath

`public void takeValueForKeyPath(Object value, String keyPath)`

Conformance to NSKeyValueCodingAdditions.

---

### takeValuesFromRequest

`public void takeValuesFromRequest( WORequest aRequest, WOContext aContext)`

The component action request handler sends this message to the WOApplication to start the first phase of request handling. In this phase, the message is propagated to the session and component objects involved in the request as well as the request page's dynamic elements. Each dynamic element acquires any entered data or changed state (such as a check in a check box) associated with an attribute and assigns the value to the variable bound to the attribute. The default WOApplication implementation of this method forwards the message to the session object.

__See Also:__ [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxwc4dqmvxgivdpkjsxg4dpnzzwk), [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws3twn5vwkqldoruw63q)

---

### terminate

`public void terminate()`

Terminates the application process. Termination does not take place until the handling of the current request has completed.

__See Also:__ [isTerminating](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxws42umvzg22lomf2gs3th), [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukruw2zkpov2a)

---

### terminateAfterTimeInterval

`public void terminateAfterTimeInterval(double aTimeInterval)`

Sets the application to terminate itself after aTimeInterval seconds has elapsed. After the specified time interval has elapsed, the application immediately stops all current processing. If any sessions are active, users may lose information.

This method differs from [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukruw2zkpov2a) in that it does not set idle time; __terminateAfterTimeInterval__ shuts down the application regardless of whether it is idle.

---

### timeOut

`public double timeOut()`

Returns the application's time-out interval: a period (in seconds) of inactivity before the application terminates execution. The default application time-out interval is a very large number.

__See Also:__ [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukruw2zkpov2a)

---

### toString

`public String toString()`

Returns a String containing a string representation of the receiver.

---

### unableToSetNullForKey

`public void unableToSetNullForKey(String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### unlock

`public void unlock()`

Unlocks the application object.

---

### validationFailedWithException

`public synchronized void validationFailedWithException( Throwable exception, Object value, String keyPath, WOComponent aComponent, WOSession aSession)`

Description forthcoming.

---

### valueForKey

`public Object valueForKey(String key)`

Conformance to NSKeyValueCoding.

---

### valueForKeyPath

`public Object valueForKeyPath(String keyPath)`

Conformance to NSKeyValueCodingAdditions.

---

### workerThreadCount

`public Number workerThreadCount()`

Returns the count of worker threads which will created by the primary adaptor (usually WODefaultAdaptor). A worker thread count of 0 implies single-threaded mode. This is the cover method for the user default WOWorkerThreadCount.

__See Also:__ [setWorkerThreadCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzluk5xxe23fojkgq4tfmfseg33vnz2a)

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
