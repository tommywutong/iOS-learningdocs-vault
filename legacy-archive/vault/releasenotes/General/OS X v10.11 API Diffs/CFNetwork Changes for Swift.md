---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CFNetwork.html
archived_at: '2026-07-18T02:53:21.480155Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CFNetwork Changes for Swift

### CFNetwork

Removed CFHostClientContext.init()Removed CFHostClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack, copyDescription: CFAllocatorCopyDescriptionCallBack)Removed CFNetServiceBrowserFlags.init(_: CFOptionFlags)Removed CFNetServiceClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack, copyDescription: CFAllocatorCopyDescriptionCallBack)Removed CFNetServiceRegisterFlags.init(_: CFOptionFlags)Added CFNetServiceClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack?, release: CFAllocatorReleaseCallBack?, copyDescription: CFAllocatorCopyDescriptionCallBack?)Added [CFNetworkErrors.CFURLErrorAppTransportSecurityRequiresSecureConnection](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorapptransportsecurityrequiressecureconnection)Added [kCFHTTPVersion2_0](https://developer.apple.com/documentation/cfnetwork/kcfhttpversion2_0)Added [kCFStreamPropertySocketExtendedBackgroundIdleMode](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertysocketextendedbackgroundidlemode)Modified [CFHostClientContext [struct]](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFHostClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack) } ``` |
| To | ``` struct CFHostClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack?     var release: CFAllocatorReleaseCallBack?     var copyDescription: CFAllocatorCopyDescriptionCallBack } ``` |

Modified [CFHostClientContext.release](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext/1426636-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack ``` |
| To | ``` var release: CFAllocatorReleaseCallBack? ``` |

Modified [CFHostClientContext.retain](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext/1426387-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack ``` |
| To | ``` var retain: CFAllocatorRetainCallBack? ``` |

Modified [CFHostInfoType [enum]](https://developer.apple.com/documentation/cfnetwork/cfhostinfotype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int32 |

Modified [CFNetDiagnosticStatusValues [enum]](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticstatusvalues)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int32 |

Modified [CFNetServiceBrowserFlags [struct]](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFNetServiceBrowserFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var MoreComing: CFNetServiceBrowserFlags { get }     static var IsDomain: CFNetServiceBrowserFlags { get }     static var IsDefault: CFNetServiceBrowserFlags { get }     static var IsRegistrationDomain: CFNetServiceBrowserFlags { get }     static var Remove: CFNetServiceBrowserFlags { get } } ``` | RawOptionSetType |
| To | ``` struct CFNetServiceBrowserFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var MoreComing: CFNetServiceBrowserFlags { get }     static var IsDomain: CFNetServiceBrowserFlags { get }     static var IsDefault: CFNetServiceBrowserFlags { get }     static var IsRegistrationDomain: CFNetServiceBrowserFlags { get }     static var Remove: CFNetServiceBrowserFlags { get } } ``` | OptionSetType |

Modified [CFNetServiceClientContext [struct]](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFNetServiceClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack) } ``` |
| To | ``` struct CFNetServiceClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack?     var release: CFAllocatorReleaseCallBack?     var copyDescription: CFAllocatorCopyDescriptionCallBack?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack?, release release: CFAllocatorReleaseCallBack?, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack?) } ``` |

Modified [CFNetServiceClientContext.copyDescription](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext/1426630-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack? ``` |

Modified [CFNetServiceClientContext.release](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext/1426897-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack ``` |
| To | ``` var release: CFAllocatorReleaseCallBack? ``` |

Modified [CFNetServiceClientContext.retain](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext/1426378-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack ``` |
| To | ``` var retain: CFAllocatorRetainCallBack? ``` |

Modified [CFNetServiceMonitorType [enum]](https://developer.apple.com/documentation/cfnetwork/cfnetservicemonitortype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int32 |

Modified [CFNetServiceRegisterFlags [struct]](https://developer.apple.com/documentation/cfnetwork/cfnetserviceregisterflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFNetServiceRegisterFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var FlagNoAutoRename: CFNetServiceRegisterFlags { get } } ``` | RawOptionSetType |
| To | ``` struct CFNetServiceRegisterFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var NoAutoRename: CFNetServiceRegisterFlags { get } } ``` | OptionSetType |

Modified [CFNetServiceRegisterFlags.NoAutoRename](https://developer.apple.com/documentation/cfnetwork/cfnetserviceregisterflags/1426637-noautorename)

|  | Declaration |
| --- | --- |
| From | ``` static var FlagNoAutoRename: CFNetServiceRegisterFlags { get } ``` |
| To | ``` static var NoAutoRename: CFNetServiceRegisterFlags { get } ``` |

Modified [CFNetServicesError [enum]](https://developer.apple.com/documentation/cfnetwork/cfnetserviceserror)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int32 |

Modified [CFNetworkErrors [enum]](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum CFNetworkErrors : Int32 {     case CFHostErrorHostNotFound     case CFHostErrorUnknown     case CFSOCKSErrorUnknownClientVersion     case CFSOCKSErrorUnsupportedServerVersion     case CFSOCKS4ErrorRequestFailed     case CFSOCKS4ErrorIdentdFailed     case CFSOCKS4ErrorIdConflict     case CFSOCKS4ErrorUnknownStatusCode     case CFSOCKS5ErrorBadState     case CFSOCKS5ErrorBadResponseAddr     case CFSOCKS5ErrorBadCredentials     case CFSOCKS5ErrorUnsupportedNegotiationMethod     case CFSOCKS5ErrorNoAcceptableMethod     case CFFTPErrorUnexpectedStatusCode     case CFErrorHTTPAuthenticationTypeUnsupported     case CFErrorHTTPBadCredentials     case CFErrorHTTPConnectionLost     case CFErrorHTTPParseFailure     case CFErrorHTTPRedirectionLoopDetected     case CFErrorHTTPBadURL     case CFErrorHTTPProxyConnectionFailure     case CFErrorHTTPBadProxyCredentials     case CFErrorPACFileError     case CFErrorPACFileAuth     case CFErrorHTTPSProxyConnectionFailure     case CFStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod     case CFURLErrorBackgroundSessionInUseByAnotherProcess     case CFURLErrorBackgroundSessionWasDisconnected     case CFURLErrorUnknown     case CFURLErrorCancelled     case CFURLErrorBadURL     case CFURLErrorTimedOut     case CFURLErrorUnsupportedURL     case CFURLErrorCannotFindHost     case CFURLErrorCannotConnectToHost     case CFURLErrorNetworkConnectionLost     case CFURLErrorDNSLookupFailed     case CFURLErrorHTTPTooManyRedirects     case CFURLErrorResourceUnavailable     case CFURLErrorNotConnectedToInternet     case CFURLErrorRedirectToNonExistentLocation     case CFURLErrorBadServerResponse     case CFURLErrorUserCancelledAuthentication     case CFURLErrorUserAuthenticationRequired     case CFURLErrorZeroByteResource     case CFURLErrorCannotDecodeRawData     case CFURLErrorCannotDecodeContentData     case CFURLErrorCannotParseResponse     case CFURLErrorInternationalRoamingOff     case CFURLErrorCallIsActive     case CFURLErrorDataNotAllowed     case CFURLErrorRequestBodyStreamExhausted     case CFURLErrorFileDoesNotExist     case CFURLErrorFileIsDirectory     case CFURLErrorNoPermissionsToReadFile     case CFURLErrorDataLengthExceedsMaximum     case CFURLErrorSecureConnectionFailed     case CFURLErrorServerCertificateHasBadDate     case CFURLErrorServerCertificateUntrusted     case CFURLErrorServerCertificateHasUnknownRoot     case CFURLErrorServerCertificateNotYetValid     case CFURLErrorClientCertificateRejected     case CFURLErrorClientCertificateRequired     case CFURLErrorCannotLoadFromNetwork     case CFURLErrorCannotCreateFile     case CFURLErrorCannotOpenFile     case CFURLErrorCannotCloseFile     case CFURLErrorCannotWriteToFile     case CFURLErrorCannotRemoveFile     case CFURLErrorCannotMoveFile     case CFURLErrorDownloadDecodingFailedMidStream     case CFURLErrorDownloadDecodingFailedToComplete     case CFHTTPCookieCannotParseCookieFile     case CFNetServiceErrorUnknown     case CFNetServiceErrorCollision     case CFNetServiceErrorNotFound     case CFNetServiceErrorInProgress     case CFNetServiceErrorBadArgument     case CFNetServiceErrorCancel     case CFNetServiceErrorInvalid     case CFNetServiceErrorTimeout     case CFNetServiceErrorDNSServiceFailure } ``` | -- |
| To | ``` enum CFNetworkErrors : Int32 {     case CFHostErrorHostNotFound     case CFHostErrorUnknown     case CFSOCKSErrorUnknownClientVersion     case CFSOCKSErrorUnsupportedServerVersion     case CFSOCKS4ErrorRequestFailed     case CFSOCKS4ErrorIdentdFailed     case CFSOCKS4ErrorIdConflict     case CFSOCKS4ErrorUnknownStatusCode     case CFSOCKS5ErrorBadState     case CFSOCKS5ErrorBadResponseAddr     case CFSOCKS5ErrorBadCredentials     case CFSOCKS5ErrorUnsupportedNegotiationMethod     case CFSOCKS5ErrorNoAcceptableMethod     case CFFTPErrorUnexpectedStatusCode     case CFErrorHTTPAuthenticationTypeUnsupported     case CFErrorHTTPBadCredentials     case CFErrorHTTPConnectionLost     case CFErrorHTTPParseFailure     case CFErrorHTTPRedirectionLoopDetected     case CFErrorHTTPBadURL     case CFErrorHTTPProxyConnectionFailure     case CFErrorHTTPBadProxyCredentials     case CFErrorPACFileError     case CFErrorPACFileAuth     case CFErrorHTTPSProxyConnectionFailure     case CFStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod     case CFURLErrorBackgroundSessionInUseByAnotherProcess     case CFURLErrorBackgroundSessionWasDisconnected     case CFURLErrorUnknown     case CFURLErrorCancelled     case CFURLErrorBadURL     case CFURLErrorTimedOut     case CFURLErrorUnsupportedURL     case CFURLErrorCannotFindHost     case CFURLErrorCannotConnectToHost     case CFURLErrorNetworkConnectionLost     case CFURLErrorDNSLookupFailed     case CFURLErrorHTTPTooManyRedirects     case CFURLErrorResourceUnavailable     case CFURLErrorNotConnectedToInternet     case CFURLErrorRedirectToNonExistentLocation     case CFURLErrorBadServerResponse     case CFURLErrorUserCancelledAuthentication     case CFURLErrorUserAuthenticationRequired     case CFURLErrorZeroByteResource     case CFURLErrorCannotDecodeRawData     case CFURLErrorCannotDecodeContentData     case CFURLErrorCannotParseResponse     case CFURLErrorInternationalRoamingOff     case CFURLErrorCallIsActive     case CFURLErrorDataNotAllowed     case CFURLErrorRequestBodyStreamExhausted     case CFURLErrorAppTransportSecurityRequiresSecureConnection     case CFURLErrorFileDoesNotExist     case CFURLErrorFileIsDirectory     case CFURLErrorNoPermissionsToReadFile     case CFURLErrorDataLengthExceedsMaximum     case CFURLErrorSecureConnectionFailed     case CFURLErrorServerCertificateHasBadDate     case CFURLErrorServerCertificateUntrusted     case CFURLErrorServerCertificateHasUnknownRoot     case CFURLErrorServerCertificateNotYetValid     case CFURLErrorClientCertificateRejected     case CFURLErrorClientCertificateRequired     case CFURLErrorCannotLoadFromNetwork     case CFURLErrorCannotCreateFile     case CFURLErrorCannotOpenFile     case CFURLErrorCannotCloseFile     case CFURLErrorCannotWriteToFile     case CFURLErrorCannotRemoveFile     case CFURLErrorCannotMoveFile     case CFURLErrorDownloadDecodingFailedMidStream     case CFURLErrorDownloadDecodingFailedToComplete     case CFHTTPCookieCannotParseCookieFile     case CFNetServiceErrorUnknown     case CFNetServiceErrorCollision     case CFNetServiceErrorNotFound     case CFNetServiceErrorInProgress     case CFNetServiceErrorBadArgument     case CFNetServiceErrorCancel     case CFNetServiceErrorInvalid     case CFNetServiceErrorTimeout     case CFNetServiceErrorDNSServiceFailure } ``` | Int32 |

Modified [CFStreamErrorHTTP [enum]](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttp)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int32 |

Modified [CFStreamErrorHTTPAuthentication [enum]](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttpauthentication)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int32 |

Modified [CFFTPCreateParsedResourceListing(_: CFAllocator?, _: UnsafePointer<UInt8>, _: CFIndex, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CFIndex](https://developer.apple.com/documentation/cfnetwork/1426546-cfftpcreateparsedresourcelisting)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func CFFTPCreateParsedResourceListing(_ alloc: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufferLength: CFIndex, _ parsed: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CFIndex ``` | -- |
| To | ``` func CFFTPCreateParsedResourceListing(_ alloc: CFAllocator?, _ buffer: UnsafePointer<UInt8>, _ bufferLength: CFIndex, _ parsed: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CFIndex ``` | OS X 10.11 |

Modified [CFHostCancelInfoResolution(_: CFHost, _: CFHostInfoType)](https://developer.apple.com/documentation/cfnetwork/1426691-cfhostcancelinforesolution)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostCancelInfoResolution(_ theHost: CFHost!, _ info: CFHostInfoType) ``` |
| To | ``` func CFHostCancelInfoResolution(_ theHost: CFHost, _ info: CFHostInfoType) ``` |

Modified [CFHostClientCallBack](https://developer.apple.com/documentation/cfnetwork/cfhostclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFHostClientCallBack = CFunctionPointer<((CFHost!, CFHostInfoType, UnsafePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFHostClientCallBack = (CFHost, CFHostInfoType, UnsafePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFHostCreateCopy(_: CFAllocator?, _: CFHost) -> Unmanaged<CFHost>](https://developer.apple.com/documentation/cfnetwork/1426854-cfhostcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostCreateCopy(_ alloc: CFAllocator!, _ host: CFHost!) -> Unmanaged<CFHost>! ``` |
| To | ``` func CFHostCreateCopy(_ alloc: CFAllocator?, _ host: CFHost) -> Unmanaged<CFHost> ``` |

Modified [CFHostCreateWithAddress(_: CFAllocator?, _: CFData) -> Unmanaged<CFHost>](https://developer.apple.com/documentation/cfnetwork/1426421-cfhostcreatewithaddress)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostCreateWithAddress(_ allocator: CFAllocator!, _ addr: CFData!) -> Unmanaged<CFHost>! ``` |
| To | ``` func CFHostCreateWithAddress(_ allocator: CFAllocator?, _ addr: CFData) -> Unmanaged<CFHost> ``` |

Modified [CFHostCreateWithName(_: CFAllocator?, _: CFString) -> Unmanaged<CFHost>](https://developer.apple.com/documentation/cfnetwork/1426488-cfhostcreatewithname)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostCreateWithName(_ allocator: CFAllocator!, _ hostname: CFString!) -> Unmanaged<CFHost>! ``` |
| To | ``` func CFHostCreateWithName(_ allocator: CFAllocator?, _ hostname: CFString) -> Unmanaged<CFHost> ``` |

Modified [CFHostGetAddressing(_: CFHost, _: UnsafeMutablePointer<DarwinBoolean>) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/cfnetwork/1426861-cfhostgetaddressing)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostGetAddressing(_ theHost: CFHost!, _ hasBeenResolved: UnsafeMutablePointer<Boolean>) -> Unmanaged<CFArray>! ``` |
| To | ``` func CFHostGetAddressing(_ theHost: CFHost, _ hasBeenResolved: UnsafeMutablePointer<DarwinBoolean>) -> Unmanaged<CFArray>? ``` |

Modified [CFHostGetNames(_: CFHost, _: UnsafeMutablePointer<DarwinBoolean>) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/cfnetwork/1426909-cfhostgetnames)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostGetNames(_ theHost: CFHost!, _ hasBeenResolved: UnsafeMutablePointer<Boolean>) -> Unmanaged<CFArray>! ``` |
| To | ``` func CFHostGetNames(_ theHost: CFHost, _ hasBeenResolved: UnsafeMutablePointer<DarwinBoolean>) -> Unmanaged<CFArray>? ``` |

Modified [CFHostGetReachability(_: CFHost, _: UnsafeMutablePointer<DarwinBoolean>) -> Unmanaged<CFData>?](https://developer.apple.com/documentation/cfnetwork/1426531-cfhostgetreachability)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostGetReachability(_ theHost: CFHost!, _ hasBeenResolved: UnsafeMutablePointer<Boolean>) -> Unmanaged<CFData>! ``` |
| To | ``` func CFHostGetReachability(_ theHost: CFHost, _ hasBeenResolved: UnsafeMutablePointer<DarwinBoolean>) -> Unmanaged<CFData>? ``` |

Modified [CFHostScheduleWithRunLoop(_: CFHost, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/cfnetwork/1426596-cfhostschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostScheduleWithRunLoop(_ theHost: CFHost!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFHostScheduleWithRunLoop(_ theHost: CFHost, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [CFHostSetClient(_: CFHost, _: CFHostClientCallBack?, _: UnsafeMutablePointer<CFHostClientContext>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426540-cfhostsetclient)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostSetClient(_ theHost: CFHost!, _ clientCB: CFHostClientCallBack, _ clientContext: UnsafeMutablePointer<CFHostClientContext>) -> Boolean ``` |
| To | ``` func CFHostSetClient(_ theHost: CFHost, _ clientCB: CFHostClientCallBack?, _ clientContext: UnsafeMutablePointer<CFHostClientContext>) -> Bool ``` |

Modified [CFHostStartInfoResolution(_: CFHost, _: CFHostInfoType, _: UnsafeMutablePointer<CFStreamError>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426672-cfhoststartinforesolution)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostStartInfoResolution(_ theHost: CFHost!, _ info: CFHostInfoType, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` |
| To | ``` func CFHostStartInfoResolution(_ theHost: CFHost, _ info: CFHostInfoType, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |

Modified [CFHostUnscheduleFromRunLoop(_: CFHost, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/cfnetwork/1426425-cfhostunschedulefromrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostUnscheduleFromRunLoop(_ theHost: CFHost!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFHostUnscheduleFromRunLoop(_ theHost: CFHost, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [CFHTTPAuthenticationAppliesToRequest(_: CFHTTPAuthentication, _: CFHTTPMessage) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426544-cfhttpauthenticationappliestoreq)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPAuthenticationAppliesToRequest(_ auth: CFHTTPAuthentication!, _ request: CFHTTPMessage!) -> Boolean ``` |
| To | ``` func CFHTTPAuthenticationAppliesToRequest(_ auth: CFHTTPAuthentication, _ request: CFHTTPMessage) -> Bool ``` |

Modified [CFHTTPAuthenticationCopyDomains(_: CFHTTPAuthentication) -> Unmanaged<CFArray>](https://developer.apple.com/documentation/cfnetwork/1426456-cfhttpauthenticationcopydomains)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPAuthenticationCopyDomains(_ auth: CFHTTPAuthentication!) -> Unmanaged<CFArray>! ``` |
| To | ``` func CFHTTPAuthenticationCopyDomains(_ auth: CFHTTPAuthentication) -> Unmanaged<CFArray> ``` |

Modified [CFHTTPAuthenticationCopyMethod(_: CFHTTPAuthentication) -> Unmanaged<CFString>](https://developer.apple.com/documentation/cfnetwork/1426688-cfhttpauthenticationcopymethod)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPAuthenticationCopyMethod(_ auth: CFHTTPAuthentication!) -> Unmanaged<CFString>! ``` |
| To | ``` func CFHTTPAuthenticationCopyMethod(_ auth: CFHTTPAuthentication) -> Unmanaged<CFString> ``` |

Modified [CFHTTPAuthenticationCopyRealm(_: CFHTTPAuthentication) -> Unmanaged<CFString>](https://developer.apple.com/documentation/cfnetwork/1426624-cfhttpauthenticationcopyrealm)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPAuthenticationCopyRealm(_ auth: CFHTTPAuthentication!) -> Unmanaged<CFString>! ``` |
| To | ``` func CFHTTPAuthenticationCopyRealm(_ auth: CFHTTPAuthentication) -> Unmanaged<CFString> ``` |

Modified [CFHTTPAuthenticationCreateFromResponse(_: CFAllocator?, _: CFHTTPMessage) -> Unmanaged<CFHTTPAuthentication>](https://developer.apple.com/documentation/cfnetwork/1426594-cfhttpauthenticationcreatefromre)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPAuthenticationCreateFromResponse(_ alloc: CFAllocator!, _ response: CFHTTPMessage!) -> Unmanaged<CFHTTPAuthentication>! ``` |
| To | ``` func CFHTTPAuthenticationCreateFromResponse(_ alloc: CFAllocator?, _ response: CFHTTPMessage) -> Unmanaged<CFHTTPAuthentication> ``` |

Modified [CFHTTPAuthenticationIsValid(_: CFHTTPAuthentication, _: UnsafeMutablePointer<CFStreamError>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426694-cfhttpauthenticationisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPAuthenticationIsValid(_ auth: CFHTTPAuthentication!, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` |
| To | ``` func CFHTTPAuthenticationIsValid(_ auth: CFHTTPAuthentication, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |

Modified [CFHTTPAuthenticationRequiresAccountDomain(_: CFHTTPAuthentication) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426760-cfhttpauthenticationrequiresacco)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPAuthenticationRequiresAccountDomain(_ auth: CFHTTPAuthentication!) -> Boolean ``` |
| To | ``` func CFHTTPAuthenticationRequiresAccountDomain(_ auth: CFHTTPAuthentication) -> Bool ``` |

Modified [CFHTTPAuthenticationRequiresOrderedRequests(_: CFHTTPAuthentication) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426505-cfhttpauthenticationrequiresorde)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPAuthenticationRequiresOrderedRequests(_ auth: CFHTTPAuthentication!) -> Boolean ``` |
| To | ``` func CFHTTPAuthenticationRequiresOrderedRequests(_ auth: CFHTTPAuthentication) -> Bool ``` |

Modified [CFHTTPAuthenticationRequiresUserNameAndPassword(_: CFHTTPAuthentication) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426849-cfhttpauthenticationrequiresuser)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPAuthenticationRequiresUserNameAndPassword(_ auth: CFHTTPAuthentication!) -> Boolean ``` |
| To | ``` func CFHTTPAuthenticationRequiresUserNameAndPassword(_ auth: CFHTTPAuthentication) -> Bool ``` |

Modified [CFHTTPMessageAddAuthentication(_: CFHTTPMessage, _: CFHTTPMessage?, _: CFString, _: CFString, _: CFString?, _: Bool) -> Bool](https://developer.apple.com/documentation/cfnetwork/1387294-cfhttpmessageaddauthentication)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageAddAuthentication(_ request: CFHTTPMessage!, _ authenticationFailureResponse: CFHTTPMessage!, _ username: CFString!, _ password: CFString!, _ authenticationScheme: CFString!, _ forProxy: Boolean) -> Boolean ``` |
| To | ``` func CFHTTPMessageAddAuthentication(_ request: CFHTTPMessage, _ authenticationFailureResponse: CFHTTPMessage?, _ username: CFString, _ password: CFString, _ authenticationScheme: CFString?, _ forProxy: Bool) -> Bool ``` |

Modified [CFHTTPMessageAppendBytes(_: CFHTTPMessage, _: UnsafePointer<UInt8>, _: CFIndex) -> Bool](https://developer.apple.com/documentation/cfnetwork/1387288-cfhttpmessageappendbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageAppendBytes(_ message: CFHTTPMessage!, _ newBytes: UnsafePointer<UInt8>, _ numBytes: CFIndex) -> Boolean ``` |
| To | ``` func CFHTTPMessageAppendBytes(_ message: CFHTTPMessage, _ newBytes: UnsafePointer<UInt8>, _ numBytes: CFIndex) -> Bool ``` |

Modified [CFHTTPMessageApplyCredentialDictionary(_: CFHTTPMessage, _: CFHTTPAuthentication, _: CFDictionary, _: UnsafeMutablePointer<CFStreamError>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426625-cfhttpmessageapplycredentialdict)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageApplyCredentialDictionary(_ request: CFHTTPMessage!, _ auth: CFHTTPAuthentication!, _ dict: CFDictionary!, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` |
| To | ``` func CFHTTPMessageApplyCredentialDictionary(_ request: CFHTTPMessage, _ auth: CFHTTPAuthentication, _ dict: CFDictionary, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |

Modified [CFHTTPMessageApplyCredentials(_: CFHTTPMessage, _: CFHTTPAuthentication, _: CFString?, _: CFString?, _: UnsafeMutablePointer<CFStreamError>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426525-cfhttpmessageapplycredentials)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageApplyCredentials(_ request: CFHTTPMessage!, _ auth: CFHTTPAuthentication!, _ username: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` |
| To | ``` func CFHTTPMessageApplyCredentials(_ request: CFHTTPMessage, _ auth: CFHTTPAuthentication, _ username: CFString?, _ password: CFString?, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |

Modified [CFHTTPMessageCopyAllHeaderFields(_: CFHTTPMessage) -> Unmanaged<CFDictionary>?](https://developer.apple.com/documentation/cfnetwork/1387311-cfhttpmessagecopyallheaderfields)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCopyAllHeaderFields(_ message: CFHTTPMessage!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CFHTTPMessageCopyAllHeaderFields(_ message: CFHTTPMessage) -> Unmanaged<CFDictionary>? ``` |

Modified [CFHTTPMessageCopyBody(_: CFHTTPMessage) -> Unmanaged<CFData>?](https://developer.apple.com/documentation/cfnetwork/1387262-cfhttpmessagecopybody)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCopyBody(_ message: CFHTTPMessage!) -> Unmanaged<CFData>! ``` |
| To | ``` func CFHTTPMessageCopyBody(_ message: CFHTTPMessage) -> Unmanaged<CFData>? ``` |

Modified [CFHTTPMessageCopyHeaderFieldValue(_: CFHTTPMessage, _: CFString) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/cfnetwork/1387300-cfhttpmessagecopyheaderfieldvalu)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCopyHeaderFieldValue(_ message: CFHTTPMessage!, _ headerField: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func CFHTTPMessageCopyHeaderFieldValue(_ message: CFHTTPMessage, _ headerField: CFString) -> Unmanaged<CFString>? ``` |

Modified [CFHTTPMessageCopyRequestMethod(_: CFHTTPMessage) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/cfnetwork/1387270-cfhttpmessagecopyrequestmethod)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCopyRequestMethod(_ request: CFHTTPMessage!) -> Unmanaged<CFString>! ``` |
| To | ``` func CFHTTPMessageCopyRequestMethod(_ request: CFHTTPMessage) -> Unmanaged<CFString>? ``` |

Modified [CFHTTPMessageCopyRequestURL(_: CFHTTPMessage) -> Unmanaged<CFURL>?](https://developer.apple.com/documentation/cfnetwork/1387280-cfhttpmessagecopyrequesturl)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCopyRequestURL(_ request: CFHTTPMessage!) -> Unmanaged<CFURL>! ``` |
| To | ``` func CFHTTPMessageCopyRequestURL(_ request: CFHTTPMessage) -> Unmanaged<CFURL>? ``` |

Modified [CFHTTPMessageCopyResponseStatusLine(_: CFHTTPMessage) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/cfnetwork/1387296-cfhttpmessagecopyresponsestatusl)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCopyResponseStatusLine(_ response: CFHTTPMessage!) -> Unmanaged<CFString>! ``` |
| To | ``` func CFHTTPMessageCopyResponseStatusLine(_ response: CFHTTPMessage) -> Unmanaged<CFString>? ``` |

Modified [CFHTTPMessageCopySerializedMessage(_: CFHTTPMessage) -> Unmanaged<CFData>?](https://developer.apple.com/documentation/cfnetwork/1387278-cfhttpmessagecopyserializedmessa)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCopySerializedMessage(_ message: CFHTTPMessage!) -> Unmanaged<CFData>! ``` |
| To | ``` func CFHTTPMessageCopySerializedMessage(_ message: CFHTTPMessage) -> Unmanaged<CFData>? ``` |

Modified [CFHTTPMessageCopyVersion(_: CFHTTPMessage) -> Unmanaged<CFString>](https://developer.apple.com/documentation/cfnetwork/1387273-cfhttpmessagecopyversion)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCopyVersion(_ message: CFHTTPMessage!) -> Unmanaged<CFString>! ``` |
| To | ``` func CFHTTPMessageCopyVersion(_ message: CFHTTPMessage) -> Unmanaged<CFString> ``` |

Modified [CFHTTPMessageCreateCopy(_: CFAllocator?, _: CFHTTPMessage) -> Unmanaged<CFHTTPMessage>](https://developer.apple.com/documentation/cfnetwork/1387266-cfhttpmessagecreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCreateCopy(_ alloc: CFAllocator!, _ message: CFHTTPMessage!) -> Unmanaged<CFHTTPMessage>! ``` |
| To | ``` func CFHTTPMessageCreateCopy(_ alloc: CFAllocator?, _ message: CFHTTPMessage) -> Unmanaged<CFHTTPMessage> ``` |

Modified [CFHTTPMessageCreateEmpty(_: CFAllocator?, _: Bool) -> Unmanaged<CFHTTPMessage>](https://developer.apple.com/documentation/cfnetwork/1387318-cfhttpmessagecreateempty)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCreateEmpty(_ alloc: CFAllocator!, _ isRequest: Boolean) -> Unmanaged<CFHTTPMessage>! ``` |
| To | ``` func CFHTTPMessageCreateEmpty(_ alloc: CFAllocator?, _ isRequest: Bool) -> Unmanaged<CFHTTPMessage> ``` |

Modified [CFHTTPMessageCreateRequest(_: CFAllocator?, _: CFString, _: CFURL, _: CFString) -> Unmanaged<CFHTTPMessage>](https://developer.apple.com/documentation/cfnetwork/1387314-cfhttpmessagecreaterequest)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCreateRequest(_ alloc: CFAllocator!, _ requestMethod: CFString!, _ url: CFURL!, _ httpVersion: CFString!) -> Unmanaged<CFHTTPMessage>! ``` |
| To | ``` func CFHTTPMessageCreateRequest(_ alloc: CFAllocator?, _ requestMethod: CFString, _ url: CFURL, _ httpVersion: CFString) -> Unmanaged<CFHTTPMessage> ``` |

Modified [CFHTTPMessageCreateResponse(_: CFAllocator?, _: CFIndex, _: CFString?, _: CFString) -> Unmanaged<CFHTTPMessage>](https://developer.apple.com/documentation/cfnetwork/1387272-cfhttpmessagecreateresponse)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageCreateResponse(_ alloc: CFAllocator!, _ statusCode: CFIndex, _ statusDescription: CFString!, _ httpVersion: CFString!) -> Unmanaged<CFHTTPMessage>! ``` |
| To | ``` func CFHTTPMessageCreateResponse(_ alloc: CFAllocator?, _ statusCode: CFIndex, _ statusDescription: CFString?, _ httpVersion: CFString) -> Unmanaged<CFHTTPMessage> ``` |

Modified [CFHTTPMessageGetResponseStatusCode(_: CFHTTPMessage) -> CFIndex](https://developer.apple.com/documentation/cfnetwork/1387284-cfhttpmessagegetresponsestatusco)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageGetResponseStatusCode(_ response: CFHTTPMessage!) -> CFIndex ``` |
| To | ``` func CFHTTPMessageGetResponseStatusCode(_ response: CFHTTPMessage) -> CFIndex ``` |

Modified [CFHTTPMessageIsHeaderComplete(_: CFHTTPMessage) -> Bool](https://developer.apple.com/documentation/cfnetwork/1387264-cfhttpmessageisheadercomplete)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageIsHeaderComplete(_ message: CFHTTPMessage!) -> Boolean ``` |
| To | ``` func CFHTTPMessageIsHeaderComplete(_ message: CFHTTPMessage) -> Bool ``` |

Modified [CFHTTPMessageIsRequest(_: CFHTTPMessage) -> Bool](https://developer.apple.com/documentation/cfnetwork/1387308-cfhttpmessageisrequest)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageIsRequest(_ message: CFHTTPMessage!) -> Boolean ``` |
| To | ``` func CFHTTPMessageIsRequest(_ message: CFHTTPMessage) -> Bool ``` |

Modified [CFHTTPMessageSetBody(_: CFHTTPMessage, _: CFData)](https://developer.apple.com/documentation/cfnetwork/1387302-cfhttpmessagesetbody)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageSetBody(_ message: CFHTTPMessage!, _ bodyData: CFData!) ``` |
| To | ``` func CFHTTPMessageSetBody(_ message: CFHTTPMessage, _ bodyData: CFData) ``` |

Modified [CFHTTPMessageSetHeaderFieldValue(_: CFHTTPMessage, _: CFString, _: CFString?)](https://developer.apple.com/documentation/cfnetwork/1387276-cfhttpmessagesetheaderfieldvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageSetHeaderFieldValue(_ message: CFHTTPMessage!, _ headerField: CFString!, _ value: CFString!) ``` |
| To | ``` func CFHTTPMessageSetHeaderFieldValue(_ message: CFHTTPMessage, _ headerField: CFString, _ value: CFString?) ``` |

Modified [CFNetDiagnosticCopyNetworkStatusPassively(_: CFNetDiagnostic, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFNetDiagnosticStatus](https://developer.apple.com/documentation/cfnetwork/1426472-cfnetdiagnosticcopynetworkstatus)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetDiagnosticCopyNetworkStatusPassively(_ details: CFNetDiagnostic!, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFNetDiagnosticStatus ``` |
| To | ``` func CFNetDiagnosticCopyNetworkStatusPassively(_ details: CFNetDiagnostic, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFNetDiagnosticStatus ``` |

Modified [CFNetDiagnosticCreateWithStreams(_: CFAllocator?, _: CFReadStream?, _: CFWriteStream?) -> Unmanaged<CFNetDiagnostic>](https://developer.apple.com/documentation/cfnetwork/1426752-cfnetdiagnosticcreatewithstreams)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetDiagnosticCreateWithStreams(_ alloc: CFAllocator!, _ readStream: CFReadStream!, _ writeStream: CFWriteStream!) -> Unmanaged<CFNetDiagnostic>! ``` |
| To | ``` func CFNetDiagnosticCreateWithStreams(_ alloc: CFAllocator?, _ readStream: CFReadStream?, _ writeStream: CFWriteStream?) -> Unmanaged<CFNetDiagnostic> ``` |

Modified [CFNetDiagnosticCreateWithURL(_: CFAllocator, _: CFURL) -> Unmanaged<CFNetDiagnostic>](https://developer.apple.com/documentation/cfnetwork/1426741-cfnetdiagnosticcreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetDiagnosticCreateWithURL(_ alloc: CFAllocator!, _ url: CFURL!) -> Unmanaged<CFNetDiagnostic>! ``` |
| To | ``` func CFNetDiagnosticCreateWithURL(_ alloc: CFAllocator, _ url: CFURL) -> Unmanaged<CFNetDiagnostic> ``` |

Modified [CFNetDiagnosticDiagnoseProblemInteractively(_: CFNetDiagnostic) -> CFNetDiagnosticStatus](https://developer.apple.com/documentation/cfnetwork/1426588-cfnetdiagnosticdiagnoseproblemin)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetDiagnosticDiagnoseProblemInteractively(_ details: CFNetDiagnostic!) -> CFNetDiagnosticStatus ``` |
| To | ``` func CFNetDiagnosticDiagnoseProblemInteractively(_ details: CFNetDiagnostic) -> CFNetDiagnosticStatus ``` |

Modified [CFNetDiagnosticSetName(_: CFNetDiagnostic, _: CFString)](https://developer.apple.com/documentation/cfnetwork/1426627-cfnetdiagnosticsetname)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetDiagnosticSetName(_ details: CFNetDiagnostic!, _ name: CFString!) ``` |
| To | ``` func CFNetDiagnosticSetName(_ details: CFNetDiagnostic, _ name: CFString) ``` |

Modified [CFNetServiceBrowserClientCallBack](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNetServiceBrowserClientCallBack = CFunctionPointer<((CFNetServiceBrowser!, CFOptionFlags, AnyObject!, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFNetServiceBrowserClientCallBack = (CFNetServiceBrowser, CFOptionFlags, AnyObject, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFNetServiceBrowserCreate(_: CFAllocator?, _: CFNetServiceBrowserClientCallBack, _: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>](https://developer.apple.com/documentation/cfnetwork/1426560-cfnetservicebrowsercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserCreate(_ alloc: CFAllocator!, _ clientCB: CFNetServiceBrowserClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>! ``` |
| To | ``` func CFNetServiceBrowserCreate(_ alloc: CFAllocator?, _ clientCB: CFNetServiceBrowserClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser> ``` |

Modified [CFNetServiceBrowserInvalidate(_: CFNetServiceBrowser)](https://developer.apple.com/documentation/cfnetwork/1426399-cfnetservicebrowserinvalidate)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserInvalidate(_ browser: CFNetServiceBrowser!) ``` |
| To | ``` func CFNetServiceBrowserInvalidate(_ browser: CFNetServiceBrowser) ``` |

Modified [CFNetServiceBrowserScheduleWithRunLoop(_: CFNetServiceBrowser, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/cfnetwork/1426904-cfnetservicebrowserschedulewithr)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserScheduleWithRunLoop(_ browser: CFNetServiceBrowser!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFNetServiceBrowserScheduleWithRunLoop(_ browser: CFNetServiceBrowser, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [CFNetServiceBrowserSearchForDomains(_: CFNetServiceBrowser, _: Bool, _: UnsafeMutablePointer<CFStreamError>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426893-cfnetservicebrowsersearchfordoma)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserSearchForDomains(_ browser: CFNetServiceBrowser!, _ registrationDomains: Boolean, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` |
| To | ``` func CFNetServiceBrowserSearchForDomains(_ browser: CFNetServiceBrowser, _ registrationDomains: Bool, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |

Modified [CFNetServiceBrowserSearchForServices(_: CFNetServiceBrowser, _: CFString, _: CFString, _: UnsafeMutablePointer<CFStreamError>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426405-cfnetservicebrowsersearchforserv)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserSearchForServices(_ browser: CFNetServiceBrowser!, _ domain: CFString!, _ serviceType: CFString!, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` |
| To | ``` func CFNetServiceBrowserSearchForServices(_ browser: CFNetServiceBrowser, _ domain: CFString, _ serviceType: CFString, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |

Modified [CFNetServiceBrowserStopSearch(_: CFNetServiceBrowser, _: UnsafeMutablePointer<CFStreamError>)](https://developer.apple.com/documentation/cfnetwork/1426523-cfnetservicebrowserstopsearch)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserStopSearch(_ browser: CFNetServiceBrowser!, _ error: UnsafeMutablePointer<CFStreamError>) ``` |
| To | ``` func CFNetServiceBrowserStopSearch(_ browser: CFNetServiceBrowser, _ error: UnsafeMutablePointer<CFStreamError>) ``` |

Modified [CFNetServiceBrowserUnscheduleFromRunLoop(_: CFNetServiceBrowser, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/cfnetwork/1426565-cfnetservicebrowserunschedulefro)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserUnscheduleFromRunLoop(_ browser: CFNetServiceBrowser!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFNetServiceBrowserUnscheduleFromRunLoop(_ browser: CFNetServiceBrowser, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [CFNetServiceCancel(_: CFNetService)](https://developer.apple.com/documentation/cfnetwork/1426533-cfnetservicecancel)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceCancel(_ theService: CFNetService!) ``` |
| To | ``` func CFNetServiceCancel(_ theService: CFNetService) ``` |

Modified [CFNetServiceClientCallBack](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNetServiceClientCallBack = CFunctionPointer<((CFNetService!, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFNetServiceClientCallBack = (CFNetService, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFNetServiceCreate(_: CFAllocator?, _: CFString, _: CFString, _: CFString, _: Int32) -> Unmanaged<CFNetService>](https://developer.apple.com/documentation/cfnetwork/1426628-cfnetservicecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceCreate(_ alloc: CFAllocator!, _ domain: CFString!, _ serviceType: CFString!, _ name: CFString!, _ port: Int32) -> Unmanaged<CFNetService>! ``` |
| To | ``` func CFNetServiceCreate(_ alloc: CFAllocator?, _ domain: CFString, _ serviceType: CFString, _ name: CFString, _ port: Int32) -> Unmanaged<CFNetService> ``` |

Modified [CFNetServiceCreateCopy(_: CFAllocator?, _: CFNetService) -> Unmanaged<CFNetService>](https://developer.apple.com/documentation/cfnetwork/1426654-cfnetservicecreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceCreateCopy(_ alloc: CFAllocator!, _ service: CFNetService!) -> Unmanaged<CFNetService>! ``` |
| To | ``` func CFNetServiceCreateCopy(_ alloc: CFAllocator?, _ service: CFNetService) -> Unmanaged<CFNetService> ``` |

Modified [CFNetServiceCreateDictionaryWithTXTData(_: CFAllocator?, _: CFData) -> Unmanaged<CFDictionary>?](https://developer.apple.com/documentation/cfnetwork/1426852-cfnetservicecreatedictionarywith)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceCreateDictionaryWithTXTData(_ alloc: CFAllocator!, _ txtRecord: CFData!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CFNetServiceCreateDictionaryWithTXTData(_ alloc: CFAllocator?, _ txtRecord: CFData) -> Unmanaged<CFDictionary>? ``` |

Modified [CFNetServiceCreateTXTDataWithDictionary(_: CFAllocator?, _: CFDictionary) -> Unmanaged<CFData>?](https://developer.apple.com/documentation/cfnetwork/1426572-cfnetservicecreatetxtdatawithdic)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceCreateTXTDataWithDictionary(_ alloc: CFAllocator!, _ keyValuePairs: CFDictionary!) -> Unmanaged<CFData>! ``` |
| To | ``` func CFNetServiceCreateTXTDataWithDictionary(_ alloc: CFAllocator?, _ keyValuePairs: CFDictionary) -> Unmanaged<CFData>? ``` |

Modified [CFNetServiceGetAddressing(_: CFNetService) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/cfnetwork/1426743-cfnetservicegetaddressing)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceGetAddressing(_ theService: CFNetService!) -> Unmanaged<CFArray>! ``` |
| To | ``` func CFNetServiceGetAddressing(_ theService: CFNetService) -> Unmanaged<CFArray>? ``` |

Modified [CFNetServiceGetDomain(_: CFNetService) -> Unmanaged<CFString>](https://developer.apple.com/documentation/cfnetwork/1426607-cfnetservicegetdomain)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceGetDomain(_ theService: CFNetService!) -> Unmanaged<CFString>! ``` |
| To | ``` func CFNetServiceGetDomain(_ theService: CFNetService) -> Unmanaged<CFString> ``` |

Modified [CFNetServiceGetName(_: CFNetService) -> Unmanaged<CFString>](https://developer.apple.com/documentation/cfnetwork/1426782-cfnetservicegetname)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceGetName(_ theService: CFNetService!) -> Unmanaged<CFString>! ``` |
| To | ``` func CFNetServiceGetName(_ theService: CFNetService) -> Unmanaged<CFString> ``` |

Modified [CFNetServiceGetPortNumber(_: CFNetService) -> Int32](https://developer.apple.com/documentation/cfnetwork/1426503-cfnetservicegetportnumber)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceGetPortNumber(_ theService: CFNetService!) -> Int32 ``` |
| To | ``` func CFNetServiceGetPortNumber(_ theService: CFNetService) -> Int32 ``` |

Modified [CFNetServiceGetTargetHost(_: CFNetService) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/cfnetwork/1426656-cfnetservicegettargethost)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceGetTargetHost(_ theService: CFNetService!) -> Unmanaged<CFString>! ``` |
| To | ``` func CFNetServiceGetTargetHost(_ theService: CFNetService) -> Unmanaged<CFString>? ``` |

Modified [CFNetServiceGetTXTData(_: CFNetService) -> Unmanaged<CFData>?](https://developer.apple.com/documentation/cfnetwork/1426664-cfnetservicegettxtdata)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceGetTXTData(_ theService: CFNetService!) -> Unmanaged<CFData>! ``` |
| To | ``` func CFNetServiceGetTXTData(_ theService: CFNetService) -> Unmanaged<CFData>? ``` |

Modified [CFNetServiceGetType(_: CFNetService) -> Unmanaged<CFString>](https://developer.apple.com/documentation/cfnetwork/1426806-cfnetservicegettype)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceGetType(_ theService: CFNetService!) -> Unmanaged<CFString>! ``` |
| To | ``` func CFNetServiceGetType(_ theService: CFNetService) -> Unmanaged<CFString> ``` |

Modified [CFNetServiceMonitorClientCallBack](https://developer.apple.com/documentation/cfnetwork/cfnetservicemonitorclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNetServiceMonitorClientCallBack = CFunctionPointer<((CFNetServiceMonitor!, CFNetService!, CFNetServiceMonitorType, CFData!, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CFNetServiceMonitorClientCallBack = (CFNetServiceMonitor, CFNetService, CFNetServiceMonitorType, CFData, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [CFNetServiceMonitorCreate(_: CFAllocator?, _: CFNetService, _: CFNetServiceMonitorClientCallBack, _: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>](https://developer.apple.com/documentation/cfnetwork/1426665-cfnetservicemonitorcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceMonitorCreate(_ alloc: CFAllocator!, _ theService: CFNetService!, _ clientCB: CFNetServiceMonitorClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>! ``` |
| To | ``` func CFNetServiceMonitorCreate(_ alloc: CFAllocator?, _ theService: CFNetService, _ clientCB: CFNetServiceMonitorClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor> ``` |

Modified [CFNetServiceMonitorInvalidate(_: CFNetServiceMonitor)](https://developer.apple.com/documentation/cfnetwork/1426906-cfnetservicemonitorinvalidate)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceMonitorInvalidate(_ monitor: CFNetServiceMonitor!) ``` |
| To | ``` func CFNetServiceMonitorInvalidate(_ monitor: CFNetServiceMonitor) ``` |

Modified [CFNetServiceMonitorScheduleWithRunLoop(_: CFNetServiceMonitor, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/cfnetwork/1426880-cfnetservicemonitorschedulewithr)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceMonitorScheduleWithRunLoop(_ monitor: CFNetServiceMonitor!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFNetServiceMonitorScheduleWithRunLoop(_ monitor: CFNetServiceMonitor, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [CFNetServiceMonitorStart(_: CFNetServiceMonitor, _: CFNetServiceMonitorType, _: UnsafeMutablePointer<CFStreamError>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426842-cfnetservicemonitorstart)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceMonitorStart(_ monitor: CFNetServiceMonitor!, _ recordType: CFNetServiceMonitorType, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` |
| To | ``` func CFNetServiceMonitorStart(_ monitor: CFNetServiceMonitor, _ recordType: CFNetServiceMonitorType, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |

Modified [CFNetServiceMonitorStop(_: CFNetServiceMonitor, _: UnsafeMutablePointer<CFStreamError>)](https://developer.apple.com/documentation/cfnetwork/1426696-cfnetservicemonitorstop)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceMonitorStop(_ monitor: CFNetServiceMonitor!, _ error: UnsafeMutablePointer<CFStreamError>) ``` |
| To | ``` func CFNetServiceMonitorStop(_ monitor: CFNetServiceMonitor, _ error: UnsafeMutablePointer<CFStreamError>) ``` |

Modified [CFNetServiceMonitorUnscheduleFromRunLoop(_: CFNetServiceMonitor, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/cfnetwork/1426400-cfnetservicemonitorunschedulefro)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceMonitorUnscheduleFromRunLoop(_ monitor: CFNetServiceMonitor!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFNetServiceMonitorUnscheduleFromRunLoop(_ monitor: CFNetServiceMonitor, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [CFNetServiceRegisterWithOptions(_: CFNetService, _: CFOptionFlags, _: UnsafeMutablePointer<CFStreamError>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426790-cfnetserviceregisterwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceRegisterWithOptions(_ theService: CFNetService!, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` |
| To | ``` func CFNetServiceRegisterWithOptions(_ theService: CFNetService, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |

Modified [CFNetServiceResolveWithTimeout(_: CFNetService, _: CFTimeInterval, _: UnsafeMutablePointer<CFStreamError>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426563-cfnetserviceresolvewithtimeout)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceResolveWithTimeout(_ theService: CFNetService!, _ timeout: CFTimeInterval, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` |
| To | ``` func CFNetServiceResolveWithTimeout(_ theService: CFNetService, _ timeout: CFTimeInterval, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |

Modified [CFNetServiceScheduleWithRunLoop(_: CFNetService, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/cfnetwork/1426730-cfnetserviceschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceScheduleWithRunLoop(_ theService: CFNetService!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFNetServiceScheduleWithRunLoop(_ theService: CFNetService, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [CFNetServiceSetClient(_: CFNetService, _: CFNetServiceClientCallBack?, _: UnsafeMutablePointer<CFNetServiceClientContext>) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426447-cfnetservicesetclient)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceSetClient(_ theService: CFNetService!, _ clientCB: CFNetServiceClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Boolean ``` |
| To | ``` func CFNetServiceSetClient(_ theService: CFNetService, _ clientCB: CFNetServiceClientCallBack?, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Bool ``` |

Modified [CFNetServiceSetTXTData(_: CFNetService, _: CFData) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426670-cfnetservicesettxtdata)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceSetTXTData(_ theService: CFNetService!, _ txtRecord: CFData!) -> Boolean ``` |
| To | ``` func CFNetServiceSetTXTData(_ theService: CFNetService, _ txtRecord: CFData) -> Bool ``` |

Modified [CFNetServiceUnscheduleFromRunLoop(_: CFNetService, _: CFRunLoop, _: CFString)](https://developer.apple.com/documentation/cfnetwork/1426679-cfnetserviceunschedulefromrunloo)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceUnscheduleFromRunLoop(_ theService: CFNetService!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func CFNetServiceUnscheduleFromRunLoop(_ theService: CFNetService, _ runLoop: CFRunLoop, _ runLoopMode: CFString) ``` |

Modified [CFNetworkCopyProxiesForAutoConfigurationScript(_: CFString, _: CFURL, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/cfnetwork/1426611-cfnetworkcopyproxiesforautoconfi)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetworkCopyProxiesForAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString!, _ targetURL: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func CFNetworkCopyProxiesForAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString, _ targetURL: CFURL, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>? ``` |

Modified [CFNetworkCopyProxiesForURL(_: CFURL, _: CFDictionary) -> Unmanaged<CFArray>](https://developer.apple.com/documentation/cfnetwork/1426639-cfnetworkcopyproxiesforurl)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetworkCopyProxiesForURL(_ url: CFURL!, _ proxySettings: CFDictionary!) -> Unmanaged<CFArray>! ``` |
| To | ``` func CFNetworkCopyProxiesForURL(_ url: CFURL, _ proxySettings: CFDictionary) -> Unmanaged<CFArray> ``` |

Modified [CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>?](https://developer.apple.com/documentation/cfnetwork/1426754-cfnetworkcopysystemproxysettings)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>? ``` |

Modified [CFNetworkExecuteProxyAutoConfigurationScript(_: CFString, _: CFURL, _: CFProxyAutoConfigurationResultCallback, _: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>](https://developer.apple.com/documentation/cfnetwork/1426362-cfnetworkexecuteproxyautoconfigu)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetworkExecuteProxyAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString!, _ targetURL: CFURL!, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>! ``` |
| To | ``` func CFNetworkExecuteProxyAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString, _ targetURL: CFURL, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource> ``` |

Modified [CFNetworkExecuteProxyAutoConfigurationURL(_: CFURL, _: CFURL, _: CFProxyAutoConfigurationResultCallback, _: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>](https://developer.apple.com/documentation/cfnetwork/1426392-cfnetworkexecuteproxyautoconfigu)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetworkExecuteProxyAutoConfigurationURL(_ proxyAutoConfigURL: CFURL!, _ targetURL: CFURL!, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>! ``` |
| To | ``` func CFNetworkExecuteProxyAutoConfigurationURL(_ proxyAutoConfigURL: CFURL, _ targetURL: CFURL, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource> ``` |

Modified [CFProxyAutoConfigurationResultCallback](https://developer.apple.com/documentation/cfnetwork/cfproxyautoconfigurationresultcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFProxyAutoConfigurationResultCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, CFArray!, CFError!) -> Void)> ``` |
| To | ``` typealias CFProxyAutoConfigurationResultCallback = (UnsafeMutablePointer<Void>, CFArray, CFError?) -> Void ``` |

Modified [CFReadStreamCreateForHTTPRequest(_: CFAllocator?, _: CFHTTPMessage) -> Unmanaged<CFReadStream>](https://developer.apple.com/documentation/cfnetwork/1426845-cfreadstreamcreateforhttprequest)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func CFReadStreamCreateForHTTPRequest(_ alloc: CFAllocator!, _ request: CFHTTPMessage!) -> Unmanaged<CFReadStream>! ``` | OS X 10.1 | -- |
| To | ``` func CFReadStreamCreateForHTTPRequest(_ alloc: CFAllocator?, _ request: CFHTTPMessage) -> Unmanaged<CFReadStream> ``` | OS X 10.2 | OS X 10.11 |

Modified [CFReadStreamCreateForStreamedHTTPRequest(_: CFAllocator?, _: CFHTTPMessage, _: CFReadStream) -> Unmanaged<CFReadStream>](https://developer.apple.com/documentation/cfnetwork/1426381-cfreadstreamcreateforstreamedhtt)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func CFReadStreamCreateForStreamedHTTPRequest(_ alloc: CFAllocator!, _ requestHeaders: CFHTTPMessage!, _ requestBody: CFReadStream!) -> Unmanaged<CFReadStream>! ``` | -- |
| To | ``` func CFReadStreamCreateForStreamedHTTPRequest(_ alloc: CFAllocator?, _ requestHeaders: CFHTTPMessage, _ requestBody: CFReadStream) -> Unmanaged<CFReadStream> ``` | OS X 10.11 |

Modified [CFReadStreamCreateWithFTPURL(_: CFAllocator?, _: CFURL) -> Unmanaged<CFReadStream>](https://developer.apple.com/documentation/cfnetwork/1426792-cfreadstreamcreatewithftpurl)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func CFReadStreamCreateWithFTPURL(_ alloc: CFAllocator!, _ ftpURL: CFURL!) -> Unmanaged<CFReadStream>! ``` | -- |
| To | ``` func CFReadStreamCreateWithFTPURL(_ alloc: CFAllocator?, _ ftpURL: CFURL) -> Unmanaged<CFReadStream> ``` | OS X 10.11 |

Modified [CFStreamCreatePairWithSocketToCFHost(_: CFAllocator?, _: CFHost, _: Int32, _: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>)](https://developer.apple.com/documentation/cfnetwork/1426831-cfstreamcreatepairwithsockettocf)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreatePairWithSocketToCFHost(_ alloc: CFAllocator!, _ host: CFHost!, _ port: Int32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |
| To | ``` func CFStreamCreatePairWithSocketToCFHost(_ alloc: CFAllocator?, _ host: CFHost, _ port: Int32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |

Modified [CFStreamCreatePairWithSocketToNetService(_: CFAllocator?, _: CFNetService, _: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>)](https://developer.apple.com/documentation/cfnetwork/1426794-cfstreamcreatepairwithsockettone)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreatePairWithSocketToNetService(_ alloc: CFAllocator!, _ service: CFNetService!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |
| To | ``` func CFStreamCreatePairWithSocketToNetService(_ alloc: CFAllocator?, _ service: CFNetService, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |

Modified [CFWriteStreamCreateWithFTPURL(_: CFAllocator?, _: CFURL) -> Unmanaged<CFWriteStream>](https://developer.apple.com/documentation/cfnetwork/1426626-cfwritestreamcreatewithftpurl)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func CFWriteStreamCreateWithFTPURL(_ alloc: CFAllocator!, _ ftpURL: CFURL!) -> Unmanaged<CFWriteStream>! ``` | -- |
| To | ``` func CFWriteStreamCreateWithFTPURL(_ alloc: CFAllocator?, _ ftpURL: CFURL) -> Unmanaged<CFWriteStream> ``` | OS X 10.11 |

Modified [kCFDNSServiceFailureKey](https://developer.apple.com/documentation/cfnetwork/kcfdnsservicefailurekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFDNSServiceFailureKey: CFString! ``` |
| To | ``` let kCFDNSServiceFailureKey: CFString ``` |

Modified [kCFErrorDomainCFNetwork](https://developer.apple.com/documentation/cfnetwork/kcferrordomaincfnetwork)

|  | Declaration |
| --- | --- |
| From | ``` let kCFErrorDomainCFNetwork: CFString! ``` |
| To | ``` let kCFErrorDomainCFNetwork: CFString ``` |

Modified [kCFErrorDomainWinSock](https://developer.apple.com/documentation/cfnetwork/kcferrordomainwinsock)

|  | Declaration |
| --- | --- |
| From | ``` let kCFErrorDomainWinSock: CFString! ``` |
| To | ``` let kCFErrorDomainWinSock: CFString ``` |

Modified [kCFFTPResourceGroup](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcegroup)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFFTPResourceGroup: CFString! ``` | -- |
| To | ``` let kCFFTPResourceGroup: CFString ``` | OS X 10.11 |

Modified [kCFFTPResourceLink](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcelink)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFFTPResourceLink: CFString! ``` | -- |
| To | ``` let kCFFTPResourceLink: CFString ``` | OS X 10.11 |

Modified [kCFFTPResourceModDate](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcemoddate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFFTPResourceModDate: CFString! ``` | -- |
| To | ``` let kCFFTPResourceModDate: CFString ``` | OS X 10.11 |

Modified [kCFFTPResourceMode](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcemode)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFFTPResourceMode: CFString! ``` | -- |
| To | ``` let kCFFTPResourceMode: CFString ``` | OS X 10.11 |

Modified [kCFFTPResourceName](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcename)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFFTPResourceName: CFString! ``` | -- |
| To | ``` let kCFFTPResourceName: CFString ``` | OS X 10.11 |

Modified [kCFFTPResourceOwner](https://developer.apple.com/documentation/cfnetwork/kcfftpresourceowner)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFFTPResourceOwner: CFString! ``` | -- |
| To | ``` let kCFFTPResourceOwner: CFString ``` | OS X 10.11 |

Modified [kCFFTPResourceSize](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcesize)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFFTPResourceSize: CFString! ``` | -- |
| To | ``` let kCFFTPResourceSize: CFString ``` | OS X 10.11 |

Modified [kCFFTPResourceType](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcetype)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFFTPResourceType: CFString! ``` | -- |
| To | ``` let kCFFTPResourceType: CFString ``` | OS X 10.11 |

Modified [kCFFTPStatusCodeKey](https://developer.apple.com/documentation/cfnetwork/kcfftpstatuscodekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFFTPStatusCodeKey: CFString! ``` |
| To | ``` let kCFFTPStatusCodeKey: CFString ``` |

Modified [kCFGetAddrInfoFailureKey](https://developer.apple.com/documentation/cfnetwork/kcfgetaddrinfofailurekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFGetAddrInfoFailureKey: CFString! ``` |
| To | ``` let kCFGetAddrInfoFailureKey: CFString ``` |

Modified [kCFHTTPAuthenticationAccountDomain](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationaccountdomain)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationAccountDomain: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationAccountDomain: CFString ``` |

Modified [kCFHTTPAuthenticationPassword](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationpassword)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationPassword: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationPassword: CFString ``` |

Modified [kCFHTTPAuthenticationSchemeBasic](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemebasic)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationSchemeBasic: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationSchemeBasic: CFString ``` |

Modified [kCFHTTPAuthenticationSchemeDigest](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemedigest)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationSchemeDigest: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationSchemeDigest: CFString ``` |

Modified [kCFHTTPAuthenticationSchemeKerberos](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemekerberos)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationSchemeKerberos: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationSchemeKerberos: CFString ``` |

Modified [kCFHTTPAuthenticationSchemeNegotiate](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemenegotiate)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationSchemeNegotiate: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationSchemeNegotiate: CFString ``` |

Modified [kCFHTTPAuthenticationSchemeNegotiate2](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemenegotiate2)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationSchemeNegotiate2: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationSchemeNegotiate2: CFString ``` |

Modified [kCFHTTPAuthenticationSchemeNTLM](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschementlm)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationSchemeNTLM: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationSchemeNTLM: CFString ``` |

Modified kCFHTTPAuthenticationSchemeOAuth1

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationSchemeOAuth1: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationSchemeOAuth1: CFString ``` |

Modified [kCFHTTPAuthenticationSchemeXMobileMeAuthToken](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemexmobilemeauthtoken)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationSchemeXMobileMeAuthToken: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationSchemeXMobileMeAuthToken: CFString ``` |

Modified [kCFHTTPAuthenticationUsername](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationusername)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPAuthenticationUsername: CFString! ``` |
| To | ``` let kCFHTTPAuthenticationUsername: CFString ``` |

Modified [kCFHTTPVersion1_0](https://developer.apple.com/documentation/cfnetwork/kcfhttpversion1_0)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPVersion1_0: CFString! ``` |
| To | ``` let kCFHTTPVersion1_0: CFString ``` |

Modified [kCFHTTPVersion1_1](https://developer.apple.com/documentation/cfnetwork/kcfhttpversion1_1)

|  | Declaration |
| --- | --- |
| From | ``` let kCFHTTPVersion1_1: CFString! ``` |
| To | ``` let kCFHTTPVersion1_1: CFString ``` |

Modified [kCFNetworkProxiesExceptionsList](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesexceptionslist)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesExceptionsList: CFString! ``` |
| To | ``` let kCFNetworkProxiesExceptionsList: CFString ``` |

Modified [kCFNetworkProxiesExcludeSimpleHostnames](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesexcludesimplehostnames)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesExcludeSimpleHostnames: CFString! ``` |
| To | ``` let kCFNetworkProxiesExcludeSimpleHostnames: CFString ``` |

Modified [kCFNetworkProxiesFTPEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesftpenable)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesFTPEnable: CFString! ``` |
| To | ``` let kCFNetworkProxiesFTPEnable: CFString ``` |

Modified [kCFNetworkProxiesFTPPassive](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesftppassive)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesFTPPassive: CFString! ``` |
| To | ``` let kCFNetworkProxiesFTPPassive: CFString ``` |

Modified [kCFNetworkProxiesFTPPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesftpport)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesFTPPort: CFString! ``` |
| To | ``` let kCFNetworkProxiesFTPPort: CFString ``` |

Modified [kCFNetworkProxiesFTPProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesftpproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesFTPProxy: CFString! ``` |
| To | ``` let kCFNetworkProxiesFTPProxy: CFString ``` |

Modified [kCFNetworkProxiesGopherEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesgopherenable)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesGopherEnable: CFString! ``` |
| To | ``` let kCFNetworkProxiesGopherEnable: CFString ``` |

Modified [kCFNetworkProxiesGopherPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesgopherport)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesGopherPort: CFString! ``` |
| To | ``` let kCFNetworkProxiesGopherPort: CFString ``` |

Modified [kCFNetworkProxiesGopherProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesgopherproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesGopherProxy: CFString! ``` |
| To | ``` let kCFNetworkProxiesGopherProxy: CFString ``` |

Modified [kCFNetworkProxiesHTTPEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpenable)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesHTTPEnable: CFString! ``` |
| To | ``` let kCFNetworkProxiesHTTPEnable: CFString ``` |

Modified [kCFNetworkProxiesHTTPPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpport)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesHTTPPort: CFString! ``` |
| To | ``` let kCFNetworkProxiesHTTPPort: CFString ``` |

Modified [kCFNetworkProxiesHTTPProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesHTTPProxy: CFString! ``` |
| To | ``` let kCFNetworkProxiesHTTPProxy: CFString ``` |

Modified [kCFNetworkProxiesHTTPSEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpsenable)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesHTTPSEnable: CFString! ``` |
| To | ``` let kCFNetworkProxiesHTTPSEnable: CFString ``` |

Modified [kCFNetworkProxiesHTTPSPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpsport)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesHTTPSPort: CFString! ``` |
| To | ``` let kCFNetworkProxiesHTTPSPort: CFString ``` |

Modified [kCFNetworkProxiesHTTPSProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpsproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesHTTPSProxy: CFString! ``` |
| To | ``` let kCFNetworkProxiesHTTPSProxy: CFString ``` |

Modified [kCFNetworkProxiesProxyAutoConfigEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesproxyautoconfigenable)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesProxyAutoConfigEnable: CFString! ``` |
| To | ``` let kCFNetworkProxiesProxyAutoConfigEnable: CFString ``` |

Modified [kCFNetworkProxiesProxyAutoConfigJavaScript](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesproxyautoconfigjavascript)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesProxyAutoConfigJavaScript: CFString! ``` |
| To | ``` let kCFNetworkProxiesProxyAutoConfigJavaScript: CFString ``` |

Modified [kCFNetworkProxiesProxyAutoConfigURLString](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesproxyautoconfigurlstring)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesProxyAutoConfigURLString: CFString! ``` |
| To | ``` let kCFNetworkProxiesProxyAutoConfigURLString: CFString ``` |

Modified [kCFNetworkProxiesProxyAutoDiscoveryEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesproxyautodiscoveryenable)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesProxyAutoDiscoveryEnable: CFString! ``` |
| To | ``` let kCFNetworkProxiesProxyAutoDiscoveryEnable: CFString ``` |

Modified [kCFNetworkProxiesRTSPEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesrtspenable)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesRTSPEnable: CFString! ``` |
| To | ``` let kCFNetworkProxiesRTSPEnable: CFString ``` |

Modified [kCFNetworkProxiesRTSPPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesrtspport)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesRTSPPort: CFString! ``` |
| To | ``` let kCFNetworkProxiesRTSPPort: CFString ``` |

Modified [kCFNetworkProxiesRTSPProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesrtspproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesRTSPProxy: CFString! ``` |
| To | ``` let kCFNetworkProxiesRTSPProxy: CFString ``` |

Modified [kCFNetworkProxiesSOCKSEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiessocksenable)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesSOCKSEnable: CFString! ``` |
| To | ``` let kCFNetworkProxiesSOCKSEnable: CFString ``` |

Modified [kCFNetworkProxiesSOCKSPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiessocksport)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesSOCKSPort: CFString! ``` |
| To | ``` let kCFNetworkProxiesSOCKSPort: CFString ``` |

Modified [kCFNetworkProxiesSOCKSProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiessocksproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kCFNetworkProxiesSOCKSProxy: CFString! ``` |
| To | ``` let kCFNetworkProxiesSOCKSProxy: CFString ``` |

Modified [kCFProxyAutoConfigurationHTTPResponseKey](https://developer.apple.com/documentation/cfnetwork/kcfproxyautoconfigurationhttpresponsekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyAutoConfigurationHTTPResponseKey: CFString! ``` |
| To | ``` let kCFProxyAutoConfigurationHTTPResponseKey: CFString ``` |

Modified [kCFProxyAutoConfigurationJavaScriptKey](https://developer.apple.com/documentation/cfnetwork/kcfproxyautoconfigurationjavascriptkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyAutoConfigurationJavaScriptKey: CFString! ``` |
| To | ``` let kCFProxyAutoConfigurationJavaScriptKey: CFString ``` |

Modified [kCFProxyAutoConfigurationURLKey](https://developer.apple.com/documentation/cfnetwork/kcfproxyautoconfigurationurlkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyAutoConfigurationURLKey: CFString! ``` |
| To | ``` let kCFProxyAutoConfigurationURLKey: CFString ``` |

Modified [kCFProxyHostNameKey](https://developer.apple.com/documentation/cfnetwork/kcfproxyhostnamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyHostNameKey: CFString! ``` |
| To | ``` let kCFProxyHostNameKey: CFString ``` |

Modified [kCFProxyPasswordKey](https://developer.apple.com/documentation/cfnetwork/kcfproxypasswordkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyPasswordKey: CFString! ``` |
| To | ``` let kCFProxyPasswordKey: CFString ``` |

Modified [kCFProxyPortNumberKey](https://developer.apple.com/documentation/cfnetwork/kcfproxyportnumberkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyPortNumberKey: CFString! ``` |
| To | ``` let kCFProxyPortNumberKey: CFString ``` |

Modified [kCFProxyTypeAutoConfigurationJavaScript](https://developer.apple.com/documentation/cfnetwork/kcfproxytypeautoconfigurationjavascript)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyTypeAutoConfigurationJavaScript: CFString! ``` |
| To | ``` let kCFProxyTypeAutoConfigurationJavaScript: CFString ``` |

Modified [kCFProxyTypeAutoConfigurationURL](https://developer.apple.com/documentation/cfnetwork/kcfproxytypeautoconfigurationurl)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyTypeAutoConfigurationURL: CFString! ``` |
| To | ``` let kCFProxyTypeAutoConfigurationURL: CFString ``` |

Modified [kCFProxyTypeFTP](https://developer.apple.com/documentation/cfnetwork/kcfproxytypeftp)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyTypeFTP: CFString! ``` |
| To | ``` let kCFProxyTypeFTP: CFString ``` |

Modified [kCFProxyTypeHTTP](https://developer.apple.com/documentation/cfnetwork/kcfproxytypehttp)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyTypeHTTP: CFString! ``` |
| To | ``` let kCFProxyTypeHTTP: CFString ``` |

Modified [kCFProxyTypeHTTPS](https://developer.apple.com/documentation/cfnetwork/kcfproxytypehttps)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyTypeHTTPS: CFString! ``` |
| To | ``` let kCFProxyTypeHTTPS: CFString ``` |

Modified [kCFProxyTypeKey](https://developer.apple.com/documentation/cfnetwork/kcfproxytypekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyTypeKey: CFString! ``` |
| To | ``` let kCFProxyTypeKey: CFString ``` |

Modified [kCFProxyTypeNone](https://developer.apple.com/documentation/cfnetwork/kcfproxytypenone)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyTypeNone: CFString! ``` |
| To | ``` let kCFProxyTypeNone: CFString ``` |

Modified [kCFProxyTypeSOCKS](https://developer.apple.com/documentation/cfnetwork/kcfproxytypesocks)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyTypeSOCKS: CFString! ``` |
| To | ``` let kCFProxyTypeSOCKS: CFString ``` |

Modified [kCFProxyUsernameKey](https://developer.apple.com/documentation/cfnetwork/kcfproxyusernamekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFProxyUsernameKey: CFString! ``` |
| To | ``` let kCFProxyUsernameKey: CFString ``` |

Modified [kCFSOCKSNegotiationMethodKey](https://developer.apple.com/documentation/cfnetwork/kcfsocksnegotiationmethodkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFSOCKSNegotiationMethodKey: CFString! ``` |
| To | ``` let kCFSOCKSNegotiationMethodKey: CFString ``` |

Modified [kCFSOCKSStatusCodeKey](https://developer.apple.com/documentation/cfnetwork/kcfsocksstatuscodekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFSOCKSStatusCodeKey: CFString! ``` |
| To | ``` let kCFSOCKSStatusCodeKey: CFString ``` |

Modified [kCFSOCKSVersionKey](https://developer.apple.com/documentation/cfnetwork/kcfsocksversionkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFSOCKSVersionKey: CFString! ``` |
| To | ``` let kCFSOCKSVersionKey: CFString ``` |

Modified [kCFStreamNetworkServiceType](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetype)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamNetworkServiceType: CFString! ``` |
| To | ``` let kCFStreamNetworkServiceType: CFString ``` |

Modified [kCFStreamNetworkServiceTypeBackground](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypebackground)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamNetworkServiceTypeBackground: CFString! ``` |
| To | ``` let kCFStreamNetworkServiceTypeBackground: CFString ``` |

Modified [kCFStreamNetworkServiceTypeVideo](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevideo)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamNetworkServiceTypeVideo: CFString! ``` |
| To | ``` let kCFStreamNetworkServiceTypeVideo: CFString ``` |

Modified [kCFStreamNetworkServiceTypeVoice](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevoice)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamNetworkServiceTypeVoice: CFString! ``` |
| To | ``` let kCFStreamNetworkServiceTypeVoice: CFString ``` |

Modified [kCFStreamNetworkServiceTypeVoIP](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevoip)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamNetworkServiceTypeVoIP: CFString! ``` | -- |
| To | ``` let kCFStreamNetworkServiceTypeVoIP: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyConnectionIsCellular](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyconnectioniscellular)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertyConnectionIsCellular: CFString! ``` |
| To | ``` let kCFStreamPropertyConnectionIsCellular: CFString ``` |

Modified [kCFStreamPropertyFTPAttemptPersistentConnection](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpattemptpersistentconnection)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPAttemptPersistentConnection: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPAttemptPersistentConnection: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPFetchResourceInfo](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpfetchresourceinfo)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPFetchResourceInfo: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPFetchResourceInfo: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPFileTransferOffset](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpfiletransferoffset)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPFileTransferOffset: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPFileTransferOffset: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPPassword](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftppassword)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPPassword: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPPassword: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPProxy](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxy)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPProxy: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPProxy: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPProxyHost](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxyhost)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPProxyHost: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPProxyHost: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPProxyPassword](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxypassword)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPProxyPassword: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPProxyPassword: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPProxyPort](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxyport)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPProxyPort: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPProxyPort: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPProxyUser](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxyuser)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPProxyUser: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPProxyUser: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPResourceSize](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpresourcesize)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPResourceSize: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPResourceSize: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPUsePassiveMode](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpusepassivemode)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPUsePassiveMode: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPUsePassiveMode: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyFTPUserName](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpusername)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyFTPUserName: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyFTPUserName: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPAttemptPersistentConnection](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpattemptpersistentconnection)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPAttemptPersistentConnection: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPAttemptPersistentConnection: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPFinalRequest](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpfinalrequest)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPFinalRequest: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPFinalRequest: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPFinalURL](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpfinalurl)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPFinalURL: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPFinalURL: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPProxy](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpproxy)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPProxy: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPProxy: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPProxyHost](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpproxyhost)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPProxyHost: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPProxyHost: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPProxyPort](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpproxyport)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPProxyPort: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPProxyPort: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPRequestBytesWrittenCount](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttprequestbyteswrittencount)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPRequestBytesWrittenCount: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPRequestBytesWrittenCount: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPResponseHeader](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpresponseheader)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPResponseHeader: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPResponseHeader: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPShouldAutoredirect](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpshouldautoredirect)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPShouldAutoredirect: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPShouldAutoredirect: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPSProxyHost](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpsproxyhost)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPSProxyHost: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPSProxyHost: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPSProxyPort](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpsproxyport)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` let kCFStreamPropertyHTTPSProxyPort: CFString! ``` | -- |
| To | ``` let kCFStreamPropertyHTTPSProxyPort: CFString ``` | OS X 10.11 |

Modified [kCFStreamPropertyNoCellular](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertynocellular)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertyNoCellular: CFString! ``` |
| To | ``` let kCFStreamPropertyNoCellular: CFString ``` |

Modified [kCFStreamPropertyProxyLocalBypass](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyproxylocalbypass)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertyProxyLocalBypass: CFString! ``` |
| To | ``` let kCFStreamPropertyProxyLocalBypass: CFString ``` |

Modified [kCFStreamPropertyShouldCloseNativeSocket](https://developer.apple.com/documentation/corefoundation/kcfstreampropertyshouldclosenativesocket)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertyShouldCloseNativeSocket: CFString! ``` |
| To | ``` let kCFStreamPropertyShouldCloseNativeSocket: CFString ``` |

Modified [kCFStreamPropertySocketRemoteHost](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertysocketremotehost)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySocketRemoteHost: CFString! ``` |
| To | ``` let kCFStreamPropertySocketRemoteHost: CFString ``` |

Modified [kCFStreamPropertySocketRemoteNetService](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertysocketremotenetservice)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySocketRemoteNetService: CFString! ``` |
| To | ``` let kCFStreamPropertySocketRemoteNetService: CFString ``` |

Modified [kCFStreamPropertySocketSecurityLevel](https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocketsecuritylevel)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySocketSecurityLevel: CFString! ``` |
| To | ``` let kCFStreamPropertySocketSecurityLevel: CFString ``` |

Modified [kCFStreamPropertySOCKSPassword](https://developer.apple.com/documentation/corefoundation/kcfstreampropertysockspassword)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySOCKSPassword: CFString! ``` |
| To | ``` let kCFStreamPropertySOCKSPassword: CFString ``` |

Modified [kCFStreamPropertySOCKSProxy](https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocksproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySOCKSProxy: CFString! ``` |
| To | ``` let kCFStreamPropertySOCKSProxy: CFString ``` |

Modified [kCFStreamPropertySOCKSProxyHost](https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocksproxyhost)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySOCKSProxyHost: CFString! ``` |
| To | ``` let kCFStreamPropertySOCKSProxyHost: CFString ``` |

Modified [kCFStreamPropertySOCKSProxyPort](https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocksproxyport)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySOCKSProxyPort: CFString! ``` |
| To | ``` let kCFStreamPropertySOCKSProxyPort: CFString ``` |

Modified [kCFStreamPropertySOCKSUser](https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocksuser)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySOCKSUser: CFString! ``` |
| To | ``` let kCFStreamPropertySOCKSUser: CFString ``` |

Modified [kCFStreamPropertySOCKSVersion](https://developer.apple.com/documentation/corefoundation/kcfstreampropertysocksversion)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySOCKSVersion: CFString! ``` |
| To | ``` let kCFStreamPropertySOCKSVersion: CFString ``` |

Modified [kCFStreamPropertySSLContext](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertysslcontext)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySSLContext: CFString! ``` |
| To | ``` let kCFStreamPropertySSLContext: CFString ``` |

Modified [kCFStreamPropertySSLPeerTrust](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertysslpeertrust)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySSLPeerTrust: CFString! ``` |
| To | ``` let kCFStreamPropertySSLPeerTrust: CFString ``` |

Modified [kCFStreamPropertySSLSettings](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertysslsettings)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamPropertySSLSettings: CFString! ``` |
| To | ``` let kCFStreamPropertySSLSettings: CFString ``` |

Modified [kCFStreamSocketSecurityLevelNegotiatedSSL](https://developer.apple.com/documentation/corefoundation/kcfstreamsocketsecuritylevelnegotiatedssl)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSocketSecurityLevelNegotiatedSSL: CFString! ``` |
| To | ``` let kCFStreamSocketSecurityLevelNegotiatedSSL: CFString ``` |

Modified [kCFStreamSocketSecurityLevelNone](https://developer.apple.com/documentation/corefoundation/kcfstreamsocketsecuritylevelnone)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSocketSecurityLevelNone: CFString! ``` |
| To | ``` let kCFStreamSocketSecurityLevelNone: CFString ``` |

Modified [kCFStreamSocketSecurityLevelSSLv2](https://developer.apple.com/documentation/corefoundation/kcfstreamsocketsecuritylevelsslv2)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSocketSecurityLevelSSLv2: CFString! ``` |
| To | ``` let kCFStreamSocketSecurityLevelSSLv2: CFString ``` |

Modified [kCFStreamSocketSecurityLevelSSLv3](https://developer.apple.com/documentation/corefoundation/kcfstreamsocketsecuritylevelsslv3)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSocketSecurityLevelSSLv3: CFString! ``` |
| To | ``` let kCFStreamSocketSecurityLevelSSLv3: CFString ``` |

Modified [kCFStreamSocketSecurityLevelTLSv1](https://developer.apple.com/documentation/corefoundation/kcfstreamsocketsecurityleveltlsv1)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSocketSecurityLevelTLSv1: CFString! ``` |
| To | ``` let kCFStreamSocketSecurityLevelTLSv1: CFString ``` |

Modified [kCFStreamSocketSOCKSVersion4](https://developer.apple.com/documentation/corefoundation/kcfstreamsocketsocksversion4)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSocketSOCKSVersion4: CFString! ``` |
| To | ``` let kCFStreamSocketSOCKSVersion4: CFString ``` |

Modified [kCFStreamSocketSOCKSVersion5](https://developer.apple.com/documentation/corefoundation/kcfstreamsocketsocksversion5)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSocketSOCKSVersion5: CFString! ``` |
| To | ``` let kCFStreamSocketSOCKSVersion5: CFString ``` |

Modified [kCFStreamSSLCertificates](https://developer.apple.com/documentation/cfnetwork/kcfstreamsslcertificates)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSSLCertificates: CFString! ``` |
| To | ``` let kCFStreamSSLCertificates: CFString ``` |

Modified [kCFStreamSSLIsServer](https://developer.apple.com/documentation/cfnetwork/kcfstreamsslisserver)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSSLIsServer: CFString! ``` |
| To | ``` let kCFStreamSSLIsServer: CFString ``` |

Modified [kCFStreamSSLLevel](https://developer.apple.com/documentation/cfnetwork/kcfstreamssllevel)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSSLLevel: CFString! ``` |
| To | ``` let kCFStreamSSLLevel: CFString ``` |

Modified [kCFStreamSSLPeerName](https://developer.apple.com/documentation/cfnetwork/kcfstreamsslpeername)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSSLPeerName: CFString! ``` |
| To | ``` let kCFStreamSSLPeerName: CFString ``` |

Modified [kCFStreamSSLValidatesCertificateChain](https://developer.apple.com/documentation/cfnetwork/kcfstreamsslvalidatescertificatechain)

|  | Declaration |
| --- | --- |
| From | ``` let kCFStreamSSLValidatesCertificateChain: CFString! ``` |
| To | ``` let kCFStreamSSLValidatesCertificateChain: CFString ``` |

Modified [kCFURLErrorFailingURLErrorKey](https://developer.apple.com/documentation/cfnetwork/kcfurlerrorfailingurlerrorkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFURLErrorFailingURLErrorKey: CFString! ``` |
| To | ``` let kCFURLErrorFailingURLErrorKey: CFString ``` |

Modified [kCFURLErrorFailingURLStringErrorKey](https://developer.apple.com/documentation/cfnetwork/kcfurlerrorfailingurlstringerrorkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCFURLErrorFailingURLStringErrorKey: CFString! ``` |
| To | ``` let kCFURLErrorFailingURLStringErrorKey: CFString ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
