---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/CFNetwork.html
archived_at: '2026-07-18T02:51:02.680577Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CFNetwork Changes for Swift

### CFNetwork

Removed CFNetServiceClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack?, release: CFAllocatorReleaseCallBack?, copyDescription: CFAllocatorCopyDescriptionCallBack?)Added [CFHostClientContext.init()](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext/1645047-init)Added [CFHostClientContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: CoreFoundation.CFAllocatorRetainCallBack?, release: CoreFoundation.CFAllocatorReleaseCallBack?, copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack?)](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext/1645048-init)Added [CFNetServiceClientContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: CoreFoundation.CFAllocatorRetainCallBack?, release: CoreFoundation.CFAllocatorReleaseCallBack?, copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack?)](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext/1778249-init)Added [kCFStreamNetworkServiceTypeCallSignaling](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypecallsignaling)Modified [CFHostClientContext [struct]](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFHostClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack?     var release: CFAllocatorReleaseCallBack?     var copyDescription: CFAllocatorCopyDescriptionCallBack } ``` |
| To | ``` struct CFHostClientContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: CoreFoundation.CFAllocatorRetainCallBack?     var release: CoreFoundation.CFAllocatorReleaseCallBack?     var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: CoreFoundation.CFAllocatorRetainCallBack?, release release: CoreFoundation.CFAllocatorReleaseCallBack?, copyDescription copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack?) } ``` |

Modified [CFHostClientContext.copyDescription](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext/1426856-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack ``` |
| To | ``` var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack? ``` |

Modified [CFHostClientContext.info](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext/1426669-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer? ``` |

Modified [CFHostClientContext.release](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext/1426636-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack? ``` |
| To | ``` var release: CoreFoundation.CFAllocatorReleaseCallBack? ``` |

Modified [CFHostClientContext.retain](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext/1426387-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack? ``` |
| To | ``` var retain: CoreFoundation.CFAllocatorRetainCallBack? ``` |

Modified [CFHostInfoType [enum]](https://developer.apple.com/documentation/cfnetwork/cfhostinfotype)

|  | Declaration |
| --- | --- |
| From | ``` enum CFHostInfoType : Int32 {     case Addresses     case Names     case Reachability } ``` |
| To | ``` enum CFHostInfoType : Int32 {     case addresses     case names     case reachability } ``` |

Modified [CFHostInfoType.addresses](https://developer.apple.com/documentation/cfnetwork/cfhostinfotype/addresses)

|  | Declaration |
| --- | --- |
| From | ``` case Addresses ``` |
| To | ``` case addresses ``` |

Modified [CFHostInfoType.names](https://developer.apple.com/documentation/cfnetwork/cfhostinfotype/names)

|  | Declaration |
| --- | --- |
| From | ``` case Names ``` |
| To | ``` case names ``` |

Modified [CFHostInfoType.reachability](https://developer.apple.com/documentation/cfnetwork/cfhostinfotype/kcfhostreachability)

|  | Declaration |
| --- | --- |
| From | ``` case Reachability ``` |
| To | ``` case reachability ``` |

Modified [CFNetDiagnosticStatusValues [enum]](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticstatusvalues)

|  | Declaration |
| --- | --- |
| From | ``` enum CFNetDiagnosticStatusValues : Int32 {     case NoErr     case Err     case ConnectionUp     case ConnectionIndeterminate     case ConnectionDown } ``` |
| To | ``` enum CFNetDiagnosticStatusValues : Int32 {     case noErr     case err     case connectionUp     case connectionIndeterminate     case connectionDown } ``` |

Modified [CFNetDiagnosticStatusValues.connectionDown](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticstatusvalues/connectiondown)

|  | Declaration |
| --- | --- |
| From | ``` case ConnectionDown ``` |
| To | ``` case connectionDown ``` |

Modified [CFNetDiagnosticStatusValues.connectionIndeterminate](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticstatusvalues/kcfnetdiagnosticconnectionindeterminate)

|  | Declaration |
| --- | --- |
| From | ``` case ConnectionIndeterminate ``` |
| To | ``` case connectionIndeterminate ``` |

Modified [CFNetDiagnosticStatusValues.connectionUp](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticstatusvalues/connectionup)

|  | Declaration |
| --- | --- |
| From | ``` case ConnectionUp ``` |
| To | ``` case connectionUp ``` |

Modified [CFNetDiagnosticStatusValues.err](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticstatusvalues/kcfnetdiagnosticerr)

|  | Declaration |
| --- | --- |
| From | ``` case Err ``` |
| To | ``` case err ``` |

Modified [CFNetDiagnosticStatusValues.noErr](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticstatusvalues/kcfnetdiagnosticnoerr)

|  | Declaration |
| --- | --- |
| From | ``` case NoErr ``` |
| To | ``` case noErr ``` |

Modified [CFNetServiceBrowserFlags [struct]](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFNetServiceBrowserFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var MoreComing: CFNetServiceBrowserFlags { get }     static var IsDomain: CFNetServiceBrowserFlags { get }     static var IsDefault: CFNetServiceBrowserFlags { get }     static var IsRegistrationDomain: CFNetServiceBrowserFlags { get }     static var Remove: CFNetServiceBrowserFlags { get } } ``` | OptionSetType |
| To | ``` struct CFNetServiceBrowserFlags : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var moreComing: CFNetServiceBrowserFlags { get }     static var isDomain: CFNetServiceBrowserFlags { get }     static var isDefault: CFNetServiceBrowserFlags { get }     static var isRegistrationDomain: CFNetServiceBrowserFlags { get }     static var remove: CFNetServiceBrowserFlags { get }     func intersect(_ other: CFNetServiceBrowserFlags) -> CFNetServiceBrowserFlags     func exclusiveOr(_ other: CFNetServiceBrowserFlags) -> CFNetServiceBrowserFlags     mutating func unionInPlace(_ other: CFNetServiceBrowserFlags)     mutating func intersectInPlace(_ other: CFNetServiceBrowserFlags)     mutating func exclusiveOrInPlace(_ other: CFNetServiceBrowserFlags)     func isSubsetOf(_ other: CFNetServiceBrowserFlags) -> Bool     func isDisjointWith(_ other: CFNetServiceBrowserFlags) -> Bool     func isSupersetOf(_ other: CFNetServiceBrowserFlags) -> Bool     mutating func subtractInPlace(_ other: CFNetServiceBrowserFlags)     func isStrictSupersetOf(_ other: CFNetServiceBrowserFlags) -> Bool     func isStrictSubsetOf(_ other: CFNetServiceBrowserFlags) -> Bool } extension CFNetServiceBrowserFlags {     func union(_ other: CFNetServiceBrowserFlags) -> CFNetServiceBrowserFlags     func intersection(_ other: CFNetServiceBrowserFlags) -> CFNetServiceBrowserFlags     func symmetricDifference(_ other: CFNetServiceBrowserFlags) -> CFNetServiceBrowserFlags } extension CFNetServiceBrowserFlags {     func contains(_ member: CFNetServiceBrowserFlags) -> Bool     mutating func insert(_ newMember: CFNetServiceBrowserFlags) -> (inserted: Bool, memberAfterInsert: CFNetServiceBrowserFlags)     mutating func remove(_ member: CFNetServiceBrowserFlags) -> CFNetServiceBrowserFlags?     mutating func update(with newMember: CFNetServiceBrowserFlags) -> CFNetServiceBrowserFlags? } extension CFNetServiceBrowserFlags {     convenience init()     mutating func formUnion(_ other: CFNetServiceBrowserFlags)     mutating func formIntersection(_ other: CFNetServiceBrowserFlags)     mutating func formSymmetricDifference(_ other: CFNetServiceBrowserFlags) } extension CFNetServiceBrowserFlags {     convenience init<S : Sequence where S.Iterator.Element == CFNetServiceBrowserFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFNetServiceBrowserFlags...)     mutating func subtract(_ other: CFNetServiceBrowserFlags)     func isSubset(of other: CFNetServiceBrowserFlags) -> Bool     func isSuperset(of other: CFNetServiceBrowserFlags) -> Bool     func isDisjoint(with other: CFNetServiceBrowserFlags) -> Bool     func subtracting(_ other: CFNetServiceBrowserFlags) -> CFNetServiceBrowserFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFNetServiceBrowserFlags) -> Bool     func isStrictSubset(of other: CFNetServiceBrowserFlags) -> Bool } ``` | OptionSet |

Modified [CFNetServiceBrowserFlags.isDefault](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags/1426568-isdefault)

|  | Declaration |
| --- | --- |
| From | ``` static var IsDefault: CFNetServiceBrowserFlags { get } ``` |
| To | ``` static var isDefault: CFNetServiceBrowserFlags { get } ``` |

Modified [CFNetServiceBrowserFlags.isDomain](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags/kcfnetserviceflagisdomain)

|  | Declaration |
| --- | --- |
| From | ``` static var IsDomain: CFNetServiceBrowserFlags { get } ``` |
| To | ``` static var isDomain: CFNetServiceBrowserFlags { get } ``` |

Modified [CFNetServiceBrowserFlags.moreComing](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags/1426467-morecoming)

|  | Declaration |
| --- | --- |
| From | ``` static var MoreComing: CFNetServiceBrowserFlags { get } ``` |
| To | ``` static var moreComing: CFNetServiceBrowserFlags { get } ``` |

Modified [CFNetServiceBrowserFlags.remove](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserflags/1426869-remove)

|  | Declaration |
| --- | --- |
| From | ``` static var Remove: CFNetServiceBrowserFlags { get } ``` |
| To | ``` static var remove: CFNetServiceBrowserFlags { get } ``` |

Modified [CFNetServiceClientContext [struct]](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext)

|  | Declaration |
| --- | --- |
| From | ``` struct CFNetServiceClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack?     var release: CFAllocatorReleaseCallBack?     var copyDescription: CFAllocatorCopyDescriptionCallBack?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack?, release release: CFAllocatorReleaseCallBack?, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack?) } ``` |
| To | ``` struct CFNetServiceClientContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: CoreFoundation.CFAllocatorRetainCallBack?     var release: CoreFoundation.CFAllocatorReleaseCallBack?     var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: CoreFoundation.CFAllocatorRetainCallBack?, release release: CoreFoundation.CFAllocatorReleaseCallBack?, copyDescription copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack?) } ``` |

Modified [CFNetServiceClientContext.copyDescription](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext/1426630-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFAllocatorCopyDescriptionCallBack? ``` |
| To | ``` var copyDescription: CoreFoundation.CFAllocatorCopyDescriptionCallBack? ``` |

Modified [CFNetServiceClientContext.info](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext/1426558-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer? ``` |

Modified [CFNetServiceClientContext.release](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext/1426897-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFAllocatorReleaseCallBack? ``` |
| To | ``` var release: CoreFoundation.CFAllocatorReleaseCallBack? ``` |

Modified [CFNetServiceClientContext.retain](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcontext/1426378-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFAllocatorRetainCallBack? ``` |
| To | ``` var retain: CoreFoundation.CFAllocatorRetainCallBack? ``` |

Modified [CFNetServiceRegisterFlags [struct]](https://developer.apple.com/documentation/cfnetwork/cfnetserviceregisterflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFNetServiceRegisterFlags : OptionSetType {     init(rawValue rawValue: CFOptionFlags)     static var NoAutoRename: CFNetServiceRegisterFlags { get } } ``` | OptionSetType |
| To | ``` struct CFNetServiceRegisterFlags : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var noAutoRename: CFNetServiceRegisterFlags { get }     func intersect(_ other: CFNetServiceRegisterFlags) -> CFNetServiceRegisterFlags     func exclusiveOr(_ other: CFNetServiceRegisterFlags) -> CFNetServiceRegisterFlags     mutating func unionInPlace(_ other: CFNetServiceRegisterFlags)     mutating func intersectInPlace(_ other: CFNetServiceRegisterFlags)     mutating func exclusiveOrInPlace(_ other: CFNetServiceRegisterFlags)     func isSubsetOf(_ other: CFNetServiceRegisterFlags) -> Bool     func isDisjointWith(_ other: CFNetServiceRegisterFlags) -> Bool     func isSupersetOf(_ other: CFNetServiceRegisterFlags) -> Bool     mutating func subtractInPlace(_ other: CFNetServiceRegisterFlags)     func isStrictSupersetOf(_ other: CFNetServiceRegisterFlags) -> Bool     func isStrictSubsetOf(_ other: CFNetServiceRegisterFlags) -> Bool } extension CFNetServiceRegisterFlags {     func union(_ other: CFNetServiceRegisterFlags) -> CFNetServiceRegisterFlags     func intersection(_ other: CFNetServiceRegisterFlags) -> CFNetServiceRegisterFlags     func symmetricDifference(_ other: CFNetServiceRegisterFlags) -> CFNetServiceRegisterFlags } extension CFNetServiceRegisterFlags {     func contains(_ member: CFNetServiceRegisterFlags) -> Bool     mutating func insert(_ newMember: CFNetServiceRegisterFlags) -> (inserted: Bool, memberAfterInsert: CFNetServiceRegisterFlags)     mutating func remove(_ member: CFNetServiceRegisterFlags) -> CFNetServiceRegisterFlags?     mutating func update(with newMember: CFNetServiceRegisterFlags) -> CFNetServiceRegisterFlags? } extension CFNetServiceRegisterFlags {     convenience init()     mutating func formUnion(_ other: CFNetServiceRegisterFlags)     mutating func formIntersection(_ other: CFNetServiceRegisterFlags)     mutating func formSymmetricDifference(_ other: CFNetServiceRegisterFlags) } extension CFNetServiceRegisterFlags {     convenience init<S : Sequence where S.Iterator.Element == CFNetServiceRegisterFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CFNetServiceRegisterFlags...)     mutating func subtract(_ other: CFNetServiceRegisterFlags)     func isSubset(of other: CFNetServiceRegisterFlags) -> Bool     func isSuperset(of other: CFNetServiceRegisterFlags) -> Bool     func isDisjoint(with other: CFNetServiceRegisterFlags) -> Bool     func subtracting(_ other: CFNetServiceRegisterFlags) -> CFNetServiceRegisterFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: CFNetServiceRegisterFlags) -> Bool     func isStrictSubset(of other: CFNetServiceRegisterFlags) -> Bool } ``` | OptionSet |

Modified [CFNetServiceRegisterFlags.noAutoRename](https://developer.apple.com/documentation/cfnetwork/cfnetserviceregisterflags/1426637-noautorename)

|  | Declaration |
| --- | --- |
| From | ``` static var NoAutoRename: CFNetServiceRegisterFlags { get } ``` |
| To | ``` static var noAutoRename: CFNetServiceRegisterFlags { get } ``` |

Modified [CFNetServicesError [enum]](https://developer.apple.com/documentation/cfnetwork/cfnetserviceserror)

|  | Declaration |
| --- | --- |
| From | ``` enum CFNetServicesError : Int32 {     case Unknown     case Collision     case NotFound     case InProgress     case BadArgument     case Cancel     case Invalid     case Timeout } ``` |
| To | ``` enum CFNetServicesError : Int32 {     case unknown     case collision     case notFound     case inProgress     case badArgument     case cancel     case invalid     case timeout } ``` |

Modified [CFNetServicesError.badArgument](https://developer.apple.com/documentation/cfnetwork/cfnetserviceserror/badargument)

|  | Declaration |
| --- | --- |
| From | ``` case BadArgument ``` |
| To | ``` case badArgument ``` |

Modified [CFNetServicesError.cancel](https://developer.apple.com/documentation/cfnetwork/cfnetserviceserror/kcfnetserviceserrorcancel)

|  | Declaration |
| --- | --- |
| From | ``` case Cancel ``` |
| To | ``` case cancel ``` |

Modified [CFNetServicesError.collision](https://developer.apple.com/documentation/cfnetwork/cfnetserviceserror/collision)

|  | Declaration |
| --- | --- |
| From | ``` case Collision ``` |
| To | ``` case collision ``` |

Modified [CFNetServicesError.inProgress](https://developer.apple.com/documentation/cfnetwork/cfnetserviceserror/kcfnetserviceserrorinprogress)

|  | Declaration |
| --- | --- |
| From | ``` case InProgress ``` |
| To | ``` case inProgress ``` |

Modified [CFNetServicesError.invalid](https://developer.apple.com/documentation/cfnetwork/cfnetserviceserror/invalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [CFNetServicesError.notFound](https://developer.apple.com/documentation/cfnetwork/cfnetserviceserror/notfound)

|  | Declaration |
| --- | --- |
| From | ``` case NotFound ``` |
| To | ``` case notFound ``` |

Modified [CFNetServicesError.timeout](https://developer.apple.com/documentation/cfnetwork/cfnetserviceserror/kcfnetserviceserrortimeout)

|  | Declaration |
| --- | --- |
| From | ``` case Timeout ``` |
| To | ``` case timeout ``` |

Modified [CFNetServicesError.unknown](https://developer.apple.com/documentation/cfnetwork/cfnetserviceserror/kcfnetserviceserrorunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CFNetworkErrors [enum]](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors)

|  | Declaration |
| --- | --- |
| From | ``` enum CFNetworkErrors : Int32 {     case CFHostErrorHostNotFound     case CFHostErrorUnknown     case CFSOCKSErrorUnknownClientVersion     case CFSOCKSErrorUnsupportedServerVersion     case CFSOCKS4ErrorRequestFailed     case CFSOCKS4ErrorIdentdFailed     case CFSOCKS4ErrorIdConflict     case CFSOCKS4ErrorUnknownStatusCode     case CFSOCKS5ErrorBadState     case CFSOCKS5ErrorBadResponseAddr     case CFSOCKS5ErrorBadCredentials     case CFSOCKS5ErrorUnsupportedNegotiationMethod     case CFSOCKS5ErrorNoAcceptableMethod     case CFFTPErrorUnexpectedStatusCode     case CFErrorHTTPAuthenticationTypeUnsupported     case CFErrorHTTPBadCredentials     case CFErrorHTTPConnectionLost     case CFErrorHTTPParseFailure     case CFErrorHTTPRedirectionLoopDetected     case CFErrorHTTPBadURL     case CFErrorHTTPProxyConnectionFailure     case CFErrorHTTPBadProxyCredentials     case CFErrorPACFileError     case CFErrorPACFileAuth     case CFErrorHTTPSProxyConnectionFailure     case CFStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod     case CFURLErrorBackgroundSessionInUseByAnotherProcess     case CFURLErrorBackgroundSessionWasDisconnected     case CFURLErrorUnknown     case CFURLErrorCancelled     case CFURLErrorBadURL     case CFURLErrorTimedOut     case CFURLErrorUnsupportedURL     case CFURLErrorCannotFindHost     case CFURLErrorCannotConnectToHost     case CFURLErrorNetworkConnectionLost     case CFURLErrorDNSLookupFailed     case CFURLErrorHTTPTooManyRedirects     case CFURLErrorResourceUnavailable     case CFURLErrorNotConnectedToInternet     case CFURLErrorRedirectToNonExistentLocation     case CFURLErrorBadServerResponse     case CFURLErrorUserCancelledAuthentication     case CFURLErrorUserAuthenticationRequired     case CFURLErrorZeroByteResource     case CFURLErrorCannotDecodeRawData     case CFURLErrorCannotDecodeContentData     case CFURLErrorCannotParseResponse     case CFURLErrorInternationalRoamingOff     case CFURLErrorCallIsActive     case CFURLErrorDataNotAllowed     case CFURLErrorRequestBodyStreamExhausted     case CFURLErrorAppTransportSecurityRequiresSecureConnection     case CFURLErrorFileDoesNotExist     case CFURLErrorFileIsDirectory     case CFURLErrorNoPermissionsToReadFile     case CFURLErrorDataLengthExceedsMaximum     case CFURLErrorSecureConnectionFailed     case CFURLErrorServerCertificateHasBadDate     case CFURLErrorServerCertificateUntrusted     case CFURLErrorServerCertificateHasUnknownRoot     case CFURLErrorServerCertificateNotYetValid     case CFURLErrorClientCertificateRejected     case CFURLErrorClientCertificateRequired     case CFURLErrorCannotLoadFromNetwork     case CFURLErrorCannotCreateFile     case CFURLErrorCannotOpenFile     case CFURLErrorCannotCloseFile     case CFURLErrorCannotWriteToFile     case CFURLErrorCannotRemoveFile     case CFURLErrorCannotMoveFile     case CFURLErrorDownloadDecodingFailedMidStream     case CFURLErrorDownloadDecodingFailedToComplete     case CFHTTPCookieCannotParseCookieFile     case CFNetServiceErrorUnknown     case CFNetServiceErrorCollision     case CFNetServiceErrorNotFound     case CFNetServiceErrorInProgress     case CFNetServiceErrorBadArgument     case CFNetServiceErrorCancel     case CFNetServiceErrorInvalid     case CFNetServiceErrorTimeout     case CFNetServiceErrorDNSServiceFailure } ``` |
| To | ``` enum CFNetworkErrors : Int32 {     case cfHostErrorHostNotFound     case cfHostErrorUnknown     case cfsocksErrorUnknownClientVersion     case cfsocksErrorUnsupportedServerVersion     case cfsocks4ErrorRequestFailed     case cfsocks4ErrorIdentdFailed     case cfsocks4ErrorIdConflict     case cfsocks4ErrorUnknownStatusCode     case cfsocks5ErrorBadState     case cfsocks5ErrorBadResponseAddr     case cfsocks5ErrorBadCredentials     case cfsocks5ErrorUnsupportedNegotiationMethod     case cfsocks5ErrorNoAcceptableMethod     case cfftpErrorUnexpectedStatusCode     case cfErrorHTTPAuthenticationTypeUnsupported     case cfErrorHTTPBadCredentials     case cfErrorHTTPConnectionLost     case cfErrorHTTPParseFailure     case cfErrorHTTPRedirectionLoopDetected     case cfErrorHTTPBadURL     case cfErrorHTTPProxyConnectionFailure     case cfErrorHTTPBadProxyCredentials     case cfErrorPACFileError     case cfErrorPACFileAuth     case cfErrorHTTPSProxyConnectionFailure     case cfStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod     case cfurlErrorBackgroundSessionInUseByAnotherProcess     case cfurlErrorBackgroundSessionWasDisconnected     case cfurlErrorUnknown     case cfurlErrorCancelled     case cfurlErrorBadURL     case cfurlErrorTimedOut     case cfurlErrorUnsupportedURL     case cfurlErrorCannotFindHost     case cfurlErrorCannotConnectToHost     case cfurlErrorNetworkConnectionLost     case cfurlErrorDNSLookupFailed     case cfurlErrorHTTPTooManyRedirects     case cfurlErrorResourceUnavailable     case cfurlErrorNotConnectedToInternet     case cfurlErrorRedirectToNonExistentLocation     case cfurlErrorBadServerResponse     case cfurlErrorUserCancelledAuthentication     case cfurlErrorUserAuthenticationRequired     case cfurlErrorZeroByteResource     case cfurlErrorCannotDecodeRawData     case cfurlErrorCannotDecodeContentData     case cfurlErrorCannotParseResponse     case cfurlErrorInternationalRoamingOff     case cfurlErrorCallIsActive     case cfurlErrorDataNotAllowed     case cfurlErrorRequestBodyStreamExhausted     case cfurlErrorAppTransportSecurityRequiresSecureConnection     case cfurlErrorFileDoesNotExist     case cfurlErrorFileIsDirectory     case cfurlErrorNoPermissionsToReadFile     case cfurlErrorDataLengthExceedsMaximum     case cfurlErrorSecureConnectionFailed     case cfurlErrorServerCertificateHasBadDate     case cfurlErrorServerCertificateUntrusted     case cfurlErrorServerCertificateHasUnknownRoot     case cfurlErrorServerCertificateNotYetValid     case cfurlErrorClientCertificateRejected     case cfurlErrorClientCertificateRequired     case cfurlErrorCannotLoadFromNetwork     case cfurlErrorCannotCreateFile     case cfurlErrorCannotOpenFile     case cfurlErrorCannotCloseFile     case cfurlErrorCannotWriteToFile     case cfurlErrorCannotRemoveFile     case cfurlErrorCannotMoveFile     case cfurlErrorDownloadDecodingFailedMidStream     case cfurlErrorDownloadDecodingFailedToComplete     case cfhttpCookieCannotParseCookieFile     case cfNetServiceErrorUnknown     case cfNetServiceErrorCollision     case cfNetServiceErrorNotFound     case cfNetServiceErrorInProgress     case cfNetServiceErrorBadArgument     case cfNetServiceErrorCancel     case cfNetServiceErrorInvalid     case cfNetServiceErrorTimeout     case cfNetServiceErrorDNSServiceFailure } ``` |

Modified [CFNetworkErrors.cfErrorHTTPAuthenticationTypeUnsupported](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cferrorhttpauthenticationtypeunsupported)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorHTTPAuthenticationTypeUnsupported ``` |
| To | ``` case cfErrorHTTPAuthenticationTypeUnsupported ``` |

Modified [CFNetworkErrors.cfErrorHTTPBadCredentials](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cferrorhttpbadcredentials)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorHTTPBadCredentials ``` |
| To | ``` case cfErrorHTTPBadCredentials ``` |

Modified [CFNetworkErrors.cfErrorHTTPBadProxyCredentials](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcferrorhttpbadproxycredentials)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorHTTPBadProxyCredentials ``` |
| To | ``` case cfErrorHTTPBadProxyCredentials ``` |

Modified [CFNetworkErrors.cfErrorHTTPBadURL](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcferrorhttpbadurl)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorHTTPBadURL ``` |
| To | ``` case cfErrorHTTPBadURL ``` |

Modified [CFNetworkErrors.cfErrorHTTPConnectionLost](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcferrorhttpconnectionlost)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorHTTPConnectionLost ``` |
| To | ``` case cfErrorHTTPConnectionLost ``` |

Modified [CFNetworkErrors.cfErrorHTTPParseFailure](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cferrorhttpparsefailure)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorHTTPParseFailure ``` |
| To | ``` case cfErrorHTTPParseFailure ``` |

Modified [CFNetworkErrors.cfErrorHTTPProxyConnectionFailure](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcferrorhttpproxyconnectionfailure)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorHTTPProxyConnectionFailure ``` |
| To | ``` case cfErrorHTTPProxyConnectionFailure ``` |

Modified [CFNetworkErrors.cfErrorHTTPRedirectionLoopDetected](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cferrorhttpredirectionloopdetected)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorHTTPRedirectionLoopDetected ``` |
| To | ``` case cfErrorHTTPRedirectionLoopDetected ``` |

Modified [CFNetworkErrors.cfErrorHTTPSProxyConnectionFailure](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcferrorhttpsproxyconnectionfailure)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorHTTPSProxyConnectionFailure ``` |
| To | ``` case cfErrorHTTPSProxyConnectionFailure ``` |

Modified [CFNetworkErrors.cfErrorPACFileAuth](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcferrorpacfileauth)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorPACFileAuth ``` |
| To | ``` case cfErrorPACFileAuth ``` |

Modified [CFNetworkErrors.cfErrorPACFileError](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcferrorpacfileerror)

|  | Declaration |
| --- | --- |
| From | ``` case CFErrorPACFileError ``` |
| To | ``` case cfErrorPACFileError ``` |

Modified [CFNetworkErrors.cfftpErrorUnexpectedStatusCode](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfftperrorunexpectedstatuscode)

|  | Declaration |
| --- | --- |
| From | ``` case CFFTPErrorUnexpectedStatusCode ``` |
| To | ``` case cfftpErrorUnexpectedStatusCode ``` |

Modified [CFNetworkErrors.cfHostErrorHostNotFound](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfhosterrorhostnotfound)

|  | Declaration |
| --- | --- |
| From | ``` case CFHostErrorHostNotFound ``` |
| To | ``` case cfHostErrorHostNotFound ``` |

Modified [CFNetworkErrors.cfHostErrorUnknown](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfhosterrorunknown)

|  | Declaration |
| --- | --- |
| From | ``` case CFHostErrorUnknown ``` |
| To | ``` case cfHostErrorUnknown ``` |

Modified [CFNetworkErrors.cfhttpCookieCannotParseCookieFile](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfhttpcookiecannotparsecookiefile)

|  | Declaration |
| --- | --- |
| From | ``` case CFHTTPCookieCannotParseCookieFile ``` |
| To | ``` case cfhttpCookieCannotParseCookieFile ``` |

Modified [CFNetworkErrors.cfNetServiceErrorBadArgument](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfnetserviceerrorbadargument)

|  | Declaration |
| --- | --- |
| From | ``` case CFNetServiceErrorBadArgument ``` |
| To | ``` case cfNetServiceErrorBadArgument ``` |

Modified [CFNetworkErrors.cfNetServiceErrorCancel](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfnetserviceerrorcancel)

|  | Declaration |
| --- | --- |
| From | ``` case CFNetServiceErrorCancel ``` |
| To | ``` case cfNetServiceErrorCancel ``` |

Modified [CFNetworkErrors.cfNetServiceErrorCollision](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfnetserviceerrorcollision)

|  | Declaration |
| --- | --- |
| From | ``` case CFNetServiceErrorCollision ``` |
| To | ``` case cfNetServiceErrorCollision ``` |

Modified [CFNetworkErrors.cfNetServiceErrorDNSServiceFailure](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfnetserviceerrordnsservicefailure)

|  | Declaration |
| --- | --- |
| From | ``` case CFNetServiceErrorDNSServiceFailure ``` |
| To | ``` case cfNetServiceErrorDNSServiceFailure ``` |

Modified [CFNetworkErrors.cfNetServiceErrorInProgress](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfnetserviceerrorinprogress)

|  | Declaration |
| --- | --- |
| From | ``` case CFNetServiceErrorInProgress ``` |
| To | ``` case cfNetServiceErrorInProgress ``` |

Modified [CFNetworkErrors.cfNetServiceErrorInvalid](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfnetserviceerrorinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case CFNetServiceErrorInvalid ``` |
| To | ``` case cfNetServiceErrorInvalid ``` |

Modified [CFNetworkErrors.cfNetServiceErrorNotFound](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfnetserviceerrornotfound)

|  | Declaration |
| --- | --- |
| From | ``` case CFNetServiceErrorNotFound ``` |
| To | ``` case cfNetServiceErrorNotFound ``` |

Modified [CFNetworkErrors.cfNetServiceErrorTimeout](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfnetserviceerrortimeout)

|  | Declaration |
| --- | --- |
| From | ``` case CFNetServiceErrorTimeout ``` |
| To | ``` case cfNetServiceErrorTimeout ``` |

Modified [CFNetworkErrors.cfNetServiceErrorUnknown](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfnetserviceerrorunknown)

|  | Declaration |
| --- | --- |
| From | ``` case CFNetServiceErrorUnknown ``` |
| To | ``` case cfNetServiceErrorUnknown ``` |

Modified [CFNetworkErrors.cfsocks4ErrorIdConflict](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfsocks4erroridconflict)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKS4ErrorIdConflict ``` |
| To | ``` case cfsocks4ErrorIdConflict ``` |

Modified [CFNetworkErrors.cfsocks4ErrorIdentdFailed](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfsocks4erroridentdfailed)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKS4ErrorIdentdFailed ``` |
| To | ``` case cfsocks4ErrorIdentdFailed ``` |

Modified [CFNetworkErrors.cfsocks4ErrorRequestFailed](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfsocks4errorrequestfailed)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKS4ErrorRequestFailed ``` |
| To | ``` case cfsocks4ErrorRequestFailed ``` |

Modified [CFNetworkErrors.cfsocks4ErrorUnknownStatusCode](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfsocks4errorunknownstatuscode)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKS4ErrorUnknownStatusCode ``` |
| To | ``` case cfsocks4ErrorUnknownStatusCode ``` |

Modified [CFNetworkErrors.cfsocks5ErrorBadCredentials](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfsocks5errorbadcredentials)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKS5ErrorBadCredentials ``` |
| To | ``` case cfsocks5ErrorBadCredentials ``` |

Modified [CFNetworkErrors.cfsocks5ErrorBadResponseAddr](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfsocks5errorbadresponseaddr)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKS5ErrorBadResponseAddr ``` |
| To | ``` case cfsocks5ErrorBadResponseAddr ``` |

Modified [CFNetworkErrors.cfsocks5ErrorBadState](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfsocks5errorbadstate)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKS5ErrorBadState ``` |
| To | ``` case cfsocks5ErrorBadState ``` |

Modified [CFNetworkErrors.cfsocks5ErrorNoAcceptableMethod](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfsocks5errornoacceptablemethod)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKS5ErrorNoAcceptableMethod ``` |
| To | ``` case cfsocks5ErrorNoAcceptableMethod ``` |

Modified [CFNetworkErrors.cfsocks5ErrorUnsupportedNegotiationMethod](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfsocks5errorunsupportednegotiationmethod)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKS5ErrorUnsupportedNegotiationMethod ``` |
| To | ``` case cfsocks5ErrorUnsupportedNegotiationMethod ``` |

Modified [CFNetworkErrors.cfsocksErrorUnknownClientVersion](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfsockserrorunknownclientversion)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKSErrorUnknownClientVersion ``` |
| To | ``` case cfsocksErrorUnknownClientVersion ``` |

Modified [CFNetworkErrors.cfsocksErrorUnsupportedServerVersion](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfsockserrorunsupportedserverversion)

|  | Declaration |
| --- | --- |
| From | ``` case CFSOCKSErrorUnsupportedServerVersion ``` |
| To | ``` case cfsocksErrorUnsupportedServerVersion ``` |

Modified [CFNetworkErrors.cfStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfstreamerrorhttpsproxyfailureunexpectedresponsetoconnectmethod)

|  | Declaration |
| --- | --- |
| From | ``` case CFStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod ``` |
| To | ``` case cfStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod ``` |

Modified [CFNetworkErrors.cfurlErrorAppTransportSecurityRequiresSecureConnection](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorapptransportsecurityrequiressecureconnection)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorAppTransportSecurityRequiresSecureConnection ``` |
| To | ``` case cfurlErrorAppTransportSecurityRequiresSecureConnection ``` |

Modified [CFNetworkErrors.cfurlErrorBackgroundSessionInUseByAnotherProcess](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorbackgroundsessioninusebyanotherprocess)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorBackgroundSessionInUseByAnotherProcess ``` |
| To | ``` case cfurlErrorBackgroundSessionInUseByAnotherProcess ``` |

Modified [CFNetworkErrors.cfurlErrorBackgroundSessionWasDisconnected](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorbackgroundsessionwasdisconnected)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorBackgroundSessionWasDisconnected ``` |
| To | ``` case cfurlErrorBackgroundSessionWasDisconnected ``` |

Modified [CFNetworkErrors.cfurlErrorBadServerResponse](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorbadserverresponse)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorBadServerResponse ``` |
| To | ``` case cfurlErrorBadServerResponse ``` |

Modified [CFNetworkErrors.cfurlErrorBadURL](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorbadurl)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorBadURL ``` |
| To | ``` case cfurlErrorBadURL ``` |

Modified [CFNetworkErrors.cfurlErrorCallIsActive](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorcallisactive)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCallIsActive ``` |
| To | ``` case cfurlErrorCallIsActive ``` |

Modified [CFNetworkErrors.cfurlErrorCancelled](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorcancelled)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCancelled ``` |
| To | ``` case cfurlErrorCancelled ``` |

Modified [CFNetworkErrors.cfurlErrorCannotCloseFile](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorcannotclosefile)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotCloseFile ``` |
| To | ``` case cfurlErrorCannotCloseFile ``` |

Modified [CFNetworkErrors.cfurlErrorCannotConnectToHost](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorcannotconnecttohost)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotConnectToHost ``` |
| To | ``` case cfurlErrorCannotConnectToHost ``` |

Modified [CFNetworkErrors.cfurlErrorCannotCreateFile](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorcannotcreatefile)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotCreateFile ``` |
| To | ``` case cfurlErrorCannotCreateFile ``` |

Modified [CFNetworkErrors.cfurlErrorCannotDecodeContentData](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorcannotdecodecontentdata)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotDecodeContentData ``` |
| To | ``` case cfurlErrorCannotDecodeContentData ``` |

Modified [CFNetworkErrors.cfurlErrorCannotDecodeRawData](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorcannotdecoderawdata)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotDecodeRawData ``` |
| To | ``` case cfurlErrorCannotDecodeRawData ``` |

Modified [CFNetworkErrors.cfurlErrorCannotFindHost](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorcannotfindhost)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotFindHost ``` |
| To | ``` case cfurlErrorCannotFindHost ``` |

Modified [CFNetworkErrors.cfurlErrorCannotLoadFromNetwork](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorcannotloadfromnetwork)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotLoadFromNetwork ``` |
| To | ``` case cfurlErrorCannotLoadFromNetwork ``` |

Modified [CFNetworkErrors.cfurlErrorCannotMoveFile](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorcannotmovefile)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotMoveFile ``` |
| To | ``` case cfurlErrorCannotMoveFile ``` |

Modified [CFNetworkErrors.cfurlErrorCannotOpenFile](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorcannotopenfile)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotOpenFile ``` |
| To | ``` case cfurlErrorCannotOpenFile ``` |

Modified [CFNetworkErrors.cfurlErrorCannotParseResponse](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorcannotparseresponse)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotParseResponse ``` |
| To | ``` case cfurlErrorCannotParseResponse ``` |

Modified [CFNetworkErrors.cfurlErrorCannotRemoveFile](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorcannotremovefile)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotRemoveFile ``` |
| To | ``` case cfurlErrorCannotRemoveFile ``` |

Modified [CFNetworkErrors.cfurlErrorCannotWriteToFile](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorcannotwritetofile)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorCannotWriteToFile ``` |
| To | ``` case cfurlErrorCannotWriteToFile ``` |

Modified [CFNetworkErrors.cfurlErrorClientCertificateRejected](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorclientcertificaterejected)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorClientCertificateRejected ``` |
| To | ``` case cfurlErrorClientCertificateRejected ``` |

Modified [CFNetworkErrors.cfurlErrorClientCertificateRequired](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorclientcertificaterequired)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorClientCertificateRequired ``` |
| To | ``` case cfurlErrorClientCertificateRequired ``` |

Modified [CFNetworkErrors.cfurlErrorDataLengthExceedsMaximum](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrordatalengthexceedsmaximum)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorDataLengthExceedsMaximum ``` |
| To | ``` case cfurlErrorDataLengthExceedsMaximum ``` |

Modified [CFNetworkErrors.cfurlErrorDataNotAllowed](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrordatanotallowed)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorDataNotAllowed ``` |
| To | ``` case cfurlErrorDataNotAllowed ``` |

Modified [CFNetworkErrors.cfurlErrorDNSLookupFailed](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrordnslookupfailed)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorDNSLookupFailed ``` |
| To | ``` case cfurlErrorDNSLookupFailed ``` |

Modified [CFNetworkErrors.cfurlErrorDownloadDecodingFailedMidStream](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrordownloaddecodingfailedmidstream)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorDownloadDecodingFailedMidStream ``` |
| To | ``` case cfurlErrorDownloadDecodingFailedMidStream ``` |

Modified [CFNetworkErrors.cfurlErrorDownloadDecodingFailedToComplete](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrordownloaddecodingfailedtocomplete)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorDownloadDecodingFailedToComplete ``` |
| To | ``` case cfurlErrorDownloadDecodingFailedToComplete ``` |

Modified [CFNetworkErrors.cfurlErrorFileDoesNotExist](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorfiledoesnotexist)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorFileDoesNotExist ``` |
| To | ``` case cfurlErrorFileDoesNotExist ``` |

Modified [CFNetworkErrors.cfurlErrorFileIsDirectory](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorfileisdirectory)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorFileIsDirectory ``` |
| To | ``` case cfurlErrorFileIsDirectory ``` |

Modified [CFNetworkErrors.cfurlErrorHTTPTooManyRedirects](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorhttptoomanyredirects)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorHTTPTooManyRedirects ``` |
| To | ``` case cfurlErrorHTTPTooManyRedirects ``` |

Modified [CFNetworkErrors.cfurlErrorInternationalRoamingOff](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorinternationalroamingoff)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorInternationalRoamingOff ``` |
| To | ``` case cfurlErrorInternationalRoamingOff ``` |

Modified [CFNetworkErrors.cfurlErrorNetworkConnectionLost](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrornetworkconnectionlost)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorNetworkConnectionLost ``` |
| To | ``` case cfurlErrorNetworkConnectionLost ``` |

Modified [CFNetworkErrors.cfurlErrorNoPermissionsToReadFile](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrornopermissionstoreadfile)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorNoPermissionsToReadFile ``` |
| To | ``` case cfurlErrorNoPermissionsToReadFile ``` |

Modified [CFNetworkErrors.cfurlErrorNotConnectedToInternet](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrornotconnectedtointernet)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorNotConnectedToInternet ``` |
| To | ``` case cfurlErrorNotConnectedToInternet ``` |

Modified [CFNetworkErrors.cfurlErrorRedirectToNonExistentLocation](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorredirecttononexistentlocation)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorRedirectToNonExistentLocation ``` |
| To | ``` case cfurlErrorRedirectToNonExistentLocation ``` |

Modified [CFNetworkErrors.cfurlErrorRequestBodyStreamExhausted](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorrequestbodystreamexhausted)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorRequestBodyStreamExhausted ``` |
| To | ``` case cfurlErrorRequestBodyStreamExhausted ``` |

Modified [CFNetworkErrors.cfurlErrorResourceUnavailable](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorresourceunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorResourceUnavailable ``` |
| To | ``` case cfurlErrorResourceUnavailable ``` |

Modified [CFNetworkErrors.cfurlErrorSecureConnectionFailed](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorsecureconnectionfailed)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorSecureConnectionFailed ``` |
| To | ``` case cfurlErrorSecureConnectionFailed ``` |

Modified [CFNetworkErrors.cfurlErrorServerCertificateHasBadDate](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorservercertificatehasbaddate)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorServerCertificateHasBadDate ``` |
| To | ``` case cfurlErrorServerCertificateHasBadDate ``` |

Modified [CFNetworkErrors.cfurlErrorServerCertificateHasUnknownRoot](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorservercertificatehasunknownroot)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorServerCertificateHasUnknownRoot ``` |
| To | ``` case cfurlErrorServerCertificateHasUnknownRoot ``` |

Modified [CFNetworkErrors.cfurlErrorServerCertificateNotYetValid](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorservercertificatenotyetvalid)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorServerCertificateNotYetValid ``` |
| To | ``` case cfurlErrorServerCertificateNotYetValid ``` |

Modified [CFNetworkErrors.cfurlErrorServerCertificateUntrusted](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorservercertificateuntrusted)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorServerCertificateUntrusted ``` |
| To | ``` case cfurlErrorServerCertificateUntrusted ``` |

Modified [CFNetworkErrors.cfurlErrorTimedOut](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrortimedout)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorTimedOut ``` |
| To | ``` case cfurlErrorTimedOut ``` |

Modified [CFNetworkErrors.cfurlErrorUnknown](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorunknown)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorUnknown ``` |
| To | ``` case cfurlErrorUnknown ``` |

Modified [CFNetworkErrors.cfurlErrorUnsupportedURL](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorunsupportedurl)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorUnsupportedURL ``` |
| To | ``` case cfurlErrorUnsupportedURL ``` |

Modified [CFNetworkErrors.cfurlErrorUserAuthenticationRequired](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerroruserauthenticationrequired)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorUserAuthenticationRequired ``` |
| To | ``` case cfurlErrorUserAuthenticationRequired ``` |

Modified [CFNetworkErrors.cfurlErrorUserCancelledAuthentication](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cfurlerrorusercancelledauthentication)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorUserCancelledAuthentication ``` |
| To | ``` case cfurlErrorUserCancelledAuthentication ``` |

Modified [CFNetworkErrors.cfurlErrorZeroByteResource](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorzerobyteresource)

|  | Declaration |
| --- | --- |
| From | ``` case CFURLErrorZeroByteResource ``` |
| To | ``` case cfurlErrorZeroByteResource ``` |

Modified [CFStreamErrorHTTP [enum]](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttp)

|  | Declaration |
| --- | --- |
| From | ``` enum CFStreamErrorHTTP : Int32 {     case ParseFailure     case RedirectionLoop     case BadURL } ``` |
| To | ``` enum CFStreamErrorHTTP : Int32 {     case parseFailure     case redirectionLoop     case badURL } ``` |

Modified [CFStreamErrorHTTP.badURL](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttp/kcfstreamerrorhttpbadurl)

|  | Declaration |
| --- | --- |
| From | ``` case BadURL ``` |
| To | ``` case badURL ``` |

Modified [CFStreamErrorHTTP.parseFailure](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttp/kcfstreamerrorhttpparsefailure)

|  | Declaration |
| --- | --- |
| From | ``` case ParseFailure ``` |
| To | ``` case parseFailure ``` |

Modified [CFStreamErrorHTTP.redirectionLoop](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttp/redirectionloop)

|  | Declaration |
| --- | --- |
| From | ``` case RedirectionLoop ``` |
| To | ``` case redirectionLoop ``` |

Modified [CFStreamErrorHTTPAuthentication [enum]](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttpauthentication)

|  | Declaration |
| --- | --- |
| From | ``` enum CFStreamErrorHTTPAuthentication : Int32 {     case TypeUnsupported     case BadUserName     case BadPassword } ``` |
| To | ``` enum CFStreamErrorHTTPAuthentication : Int32 {     case typeUnsupported     case badUserName     case badPassword } ``` |

Modified [CFStreamErrorHTTPAuthentication.badPassword](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttpauthentication/badpassword)

|  | Declaration |
| --- | --- |
| From | ``` case BadPassword ``` |
| To | ``` case badPassword ``` |

Modified [CFStreamErrorHTTPAuthentication.badUserName](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttpauthentication/badusername)

|  | Declaration |
| --- | --- |
| From | ``` case BadUserName ``` |
| To | ``` case badUserName ``` |

Modified [CFStreamErrorHTTPAuthentication.typeUnsupported](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttpauthentication/kcfstreamerrorhttpauthenticationtypeunsupported)

|  | Declaration |
| --- | --- |
| From | ``` case TypeUnsupported ``` |
| To | ``` case typeUnsupported ``` |

Modified [CFFTPCreateParsedResourceListing(_: CFAllocator?, _: UnsafePointer<UInt8>, _: CFIndex, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>?) -> CFIndex](https://developer.apple.com/documentation/cfnetwork/1426546-cfftpcreateparsedresourcelisting)

|  | Declaration |
| --- | --- |
| From | ``` func CFFTPCreateParsedResourceListing(_ alloc: CFAllocator?, _ buffer: UnsafePointer<UInt8>, _ bufferLength: CFIndex, _ parsed: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CFIndex ``` |
| To | ``` func CFFTPCreateParsedResourceListing(_ alloc: CFAllocator?, _ buffer: UnsafePointer<UInt8>, _ bufferLength: CFIndex, _ parsed: UnsafeMutablePointer<Unmanaged<CFDictionary>?>?) -> CFIndex ``` |

Modified [CFHostClientCallBack](https://developer.apple.com/documentation/cfnetwork/cfhostclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFHostClientCallBack = (CFHost, CFHostInfoType, UnsafePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFHostClientCallBack = (CFHost, CFHostInfoType, UnsafePointer<CFStreamError>?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFHostGetAddressing(_: CFHost, _: UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/cfnetwork/1426861-cfhostgetaddressing)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostGetAddressing(_ theHost: CFHost, _ hasBeenResolved: UnsafeMutablePointer<DarwinBoolean>) -> Unmanaged<CFArray>? ``` |
| To | ``` func CFHostGetAddressing(_ theHost: CFHost, _ hasBeenResolved: UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>? ``` |

Modified [CFHostGetNames(_: CFHost, _: UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/cfnetwork/1426909-cfhostgetnames)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostGetNames(_ theHost: CFHost, _ hasBeenResolved: UnsafeMutablePointer<DarwinBoolean>) -> Unmanaged<CFArray>? ``` |
| To | ``` func CFHostGetNames(_ theHost: CFHost, _ hasBeenResolved: UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>? ``` |

Modified [CFHostGetReachability(_: CFHost, _: UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFData>?](https://developer.apple.com/documentation/cfnetwork/1426531-cfhostgetreachability)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostGetReachability(_ theHost: CFHost, _ hasBeenResolved: UnsafeMutablePointer<DarwinBoolean>) -> Unmanaged<CFData>? ``` |
| To | ``` func CFHostGetReachability(_ theHost: CFHost, _ hasBeenResolved: UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFData>? ``` |

Modified [CFHostSetClient(_: CFHost, _: CFNetwork.CFHostClientCallBack?, _: UnsafeMutablePointer<CFHostClientContext>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426540-cfhostsetclient)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostSetClient(_ theHost: CFHost, _ clientCB: CFHostClientCallBack?, _ clientContext: UnsafeMutablePointer<CFHostClientContext>) -> Bool ``` |
| To | ``` func CFHostSetClient(_ theHost: CFHost, _ clientCB: CFNetwork.CFHostClientCallBack?, _ clientContext: UnsafeMutablePointer<CFHostClientContext>?) -> Bool ``` |

Modified [CFHostStartInfoResolution(_: CFHost, _: CFHostInfoType, _: UnsafeMutablePointer<CFStreamError>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426672-cfhoststartinforesolution)

|  | Declaration |
| --- | --- |
| From | ``` func CFHostStartInfoResolution(_ theHost: CFHost, _ info: CFHostInfoType, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |
| To | ``` func CFHostStartInfoResolution(_ theHost: CFHost, _ info: CFHostInfoType, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool ``` |

Modified [CFHTTPAuthenticationIsValid(_: CFHTTPAuthentication, _: UnsafeMutablePointer<CFStreamError>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426694-cfhttpauthenticationisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPAuthenticationIsValid(_ auth: CFHTTPAuthentication, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |
| To | ``` func CFHTTPAuthenticationIsValid(_ auth: CFHTTPAuthentication, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool ``` |

Modified [CFHTTPMessageApplyCredentialDictionary(_: CFHTTPMessage, _: CFHTTPAuthentication, _: CFDictionary, _: UnsafeMutablePointer<CFStreamError>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426625-cfhttpmessageapplycredentialdict)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageApplyCredentialDictionary(_ request: CFHTTPMessage, _ auth: CFHTTPAuthentication, _ dict: CFDictionary, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |
| To | ``` func CFHTTPMessageApplyCredentialDictionary(_ request: CFHTTPMessage, _ auth: CFHTTPAuthentication, _ dict: CFDictionary, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool ``` |

Modified [CFHTTPMessageApplyCredentials(_: CFHTTPMessage, _: CFHTTPAuthentication, _: CFString?, _: CFString?, _: UnsafeMutablePointer<CFStreamError>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426525-cfhttpmessageapplycredentials)

|  | Declaration |
| --- | --- |
| From | ``` func CFHTTPMessageApplyCredentials(_ request: CFHTTPMessage, _ auth: CFHTTPAuthentication, _ username: CFString?, _ password: CFString?, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |
| To | ``` func CFHTTPMessageApplyCredentials(_ request: CFHTTPMessage, _ auth: CFHTTPAuthentication, _ username: CFString?, _ password: CFString?, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool ``` |

Modified [CFNetDiagnosticCopyNetworkStatusPassively(_: CFNetDiagnostic, _: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus](https://developer.apple.com/documentation/cfnetwork/1426472-cfnetdiagnosticcopynetworkstatus)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetDiagnosticCopyNetworkStatusPassively(_ details: CFNetDiagnostic, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFNetDiagnosticStatus ``` |
| To | ``` func CFNetDiagnosticCopyNetworkStatusPassively(_ details: CFNetDiagnostic, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus ``` |

Modified [CFNetServiceBrowserClientCallBack](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowserclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNetServiceBrowserClientCallBack = (CFNetServiceBrowser, CFOptionFlags, AnyObject, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFNetServiceBrowserClientCallBack = (CFNetServiceBrowser, CFOptionFlags, CFTypeRef?, UnsafeMutablePointer<CFStreamError>?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFNetServiceBrowserCreate(_: CFAllocator?, _: CFNetwork.CFNetServiceBrowserClientCallBack, _: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>](https://developer.apple.com/documentation/cfnetwork/1426560-cfnetservicebrowsercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserCreate(_ alloc: CFAllocator?, _ clientCB: CFNetServiceBrowserClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser> ``` |
| To | ``` func CFNetServiceBrowserCreate(_ alloc: CFAllocator?, _ clientCB: CFNetwork.CFNetServiceBrowserClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser> ``` |

Modified [CFNetServiceBrowserSearchForDomains(_: CFNetServiceBrowser, _: Bool, _: UnsafeMutablePointer<CFStreamError>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426893-cfnetservicebrowsersearchfordoma)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserSearchForDomains(_ browser: CFNetServiceBrowser, _ registrationDomains: Bool, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |
| To | ``` func CFNetServiceBrowserSearchForDomains(_ browser: CFNetServiceBrowser, _ registrationDomains: Bool, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool ``` |

Modified [CFNetServiceBrowserSearchForServices(_: CFNetServiceBrowser, _: CFString, _: CFString, _: UnsafeMutablePointer<CFStreamError>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426405-cfnetservicebrowsersearchforserv)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserSearchForServices(_ browser: CFNetServiceBrowser, _ domain: CFString, _ serviceType: CFString, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |
| To | ``` func CFNetServiceBrowserSearchForServices(_ browser: CFNetServiceBrowser, _ domain: CFString, _ serviceType: CFString, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool ``` |

Modified [CFNetServiceBrowserStopSearch(_: CFNetServiceBrowser, _: UnsafeMutablePointer<CFStreamError>?)](https://developer.apple.com/documentation/cfnetwork/1426523-cfnetservicebrowserstopsearch)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceBrowserStopSearch(_ browser: CFNetServiceBrowser, _ error: UnsafeMutablePointer<CFStreamError>) ``` |
| To | ``` func CFNetServiceBrowserStopSearch(_ browser: CFNetServiceBrowser, _ error: UnsafeMutablePointer<CFStreamError>?) ``` |

Modified [CFNetServiceClientCallBack](https://developer.apple.com/documentation/cfnetwork/cfnetserviceclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNetServiceClientCallBack = (CFNetService, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFNetServiceClientCallBack = (CFNetService, UnsafeMutablePointer<CFStreamError>?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFNetServiceMonitorClientCallBack](https://developer.apple.com/documentation/cfnetwork/cfnetservicemonitorclientcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNetServiceMonitorClientCallBack = (CFNetServiceMonitor, CFNetService, CFNetServiceMonitorType, CFData, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CFNetServiceMonitorClientCallBack = (CFNetServiceMonitor, CFNetService?, CFNetServiceMonitorType, CFData?, UnsafeMutablePointer<CFStreamError>?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CFNetServiceMonitorCreate(_: CFAllocator?, _: CFNetService, _: CFNetwork.CFNetServiceMonitorClientCallBack, _: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>](https://developer.apple.com/documentation/cfnetwork/1426665-cfnetservicemonitorcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceMonitorCreate(_ alloc: CFAllocator?, _ theService: CFNetService, _ clientCB: CFNetServiceMonitorClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor> ``` |
| To | ``` func CFNetServiceMonitorCreate(_ alloc: CFAllocator?, _ theService: CFNetService, _ clientCB: CFNetwork.CFNetServiceMonitorClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor> ``` |

Modified [CFNetServiceMonitorStart(_: CFNetServiceMonitor, _: CFNetServiceMonitorType, _: UnsafeMutablePointer<CFStreamError>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426842-cfnetservicemonitorstart)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceMonitorStart(_ monitor: CFNetServiceMonitor, _ recordType: CFNetServiceMonitorType, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |
| To | ``` func CFNetServiceMonitorStart(_ monitor: CFNetServiceMonitor, _ recordType: CFNetServiceMonitorType, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool ``` |

Modified [CFNetServiceMonitorStop(_: CFNetServiceMonitor, _: UnsafeMutablePointer<CFStreamError>?)](https://developer.apple.com/documentation/cfnetwork/1426696-cfnetservicemonitorstop)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceMonitorStop(_ monitor: CFNetServiceMonitor, _ error: UnsafeMutablePointer<CFStreamError>) ``` |
| To | ``` func CFNetServiceMonitorStop(_ monitor: CFNetServiceMonitor, _ error: UnsafeMutablePointer<CFStreamError>?) ``` |

Modified [CFNetServiceRegisterWithOptions(_: CFNetService, _: CFOptionFlags, _: UnsafeMutablePointer<CFStreamError>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426790-cfnetserviceregisterwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceRegisterWithOptions(_ theService: CFNetService, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |
| To | ``` func CFNetServiceRegisterWithOptions(_ theService: CFNetService, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool ``` |

Modified [CFNetServiceResolveWithTimeout(_: CFNetService, _: CFTimeInterval, _: UnsafeMutablePointer<CFStreamError>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426563-cfnetserviceresolvewithtimeout)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceResolveWithTimeout(_ theService: CFNetService, _ timeout: CFTimeInterval, _ error: UnsafeMutablePointer<CFStreamError>) -> Bool ``` |
| To | ``` func CFNetServiceResolveWithTimeout(_ theService: CFNetService, _ timeout: CFTimeInterval, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool ``` |

Modified [CFNetServiceSetClient(_: CFNetService, _: CFNetwork.CFNetServiceClientCallBack?, _: UnsafeMutablePointer<CFNetServiceClientContext>?) -> Bool](https://developer.apple.com/documentation/cfnetwork/1426447-cfnetservicesetclient)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetServiceSetClient(_ theService: CFNetService, _ clientCB: CFNetServiceClientCallBack?, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Bool ``` |
| To | ``` func CFNetServiceSetClient(_ theService: CFNetService, _ clientCB: CFNetwork.CFNetServiceClientCallBack?, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>?) -> Bool ``` |

Modified [CFNetworkCopyProxiesForAutoConfigurationScript(_: CFString, _: CFURL, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/cfnetwork/1426611-cfnetworkcopyproxiesforautoconfi)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetworkCopyProxiesForAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString, _ targetURL: CFURL, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>? ``` |
| To | ``` func CFNetworkCopyProxiesForAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString, _ targetURL: CFURL, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>? ``` |

Modified [CFNetworkExecuteProxyAutoConfigurationScript(_: CFString, _: CFURL, _: CFNetwork.CFProxyAutoConfigurationResultCallback, _: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>](https://developer.apple.com/documentation/cfnetwork/1426362-cfnetworkexecuteproxyautoconfigu)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetworkExecuteProxyAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString, _ targetURL: CFURL, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource> ``` |
| To | ``` func CFNetworkExecuteProxyAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString, _ targetURL: CFURL, _ cb: CFNetwork.CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource> ``` |

Modified [CFNetworkExecuteProxyAutoConfigurationURL(_: CFURL, _: CFURL, _: CFNetwork.CFProxyAutoConfigurationResultCallback, _: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>](https://developer.apple.com/documentation/cfnetwork/1426392-cfnetworkexecuteproxyautoconfigu)

|  | Declaration |
| --- | --- |
| From | ``` func CFNetworkExecuteProxyAutoConfigurationURL(_ proxyAutoConfigURL: CFURL, _ targetURL: CFURL, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource> ``` |
| To | ``` func CFNetworkExecuteProxyAutoConfigurationURL(_ proxyAutoConfigURL: CFURL, _ targetURL: CFURL, _ cb: CFNetwork.CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource> ``` |

Modified [CFProxyAutoConfigurationResultCallback](https://developer.apple.com/documentation/cfnetwork/cfproxyautoconfigurationresultcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CFProxyAutoConfigurationResultCallback = (UnsafeMutablePointer<Void>, CFArray, CFError?) -> Void ``` |
| To | ``` typealias CFProxyAutoConfigurationResultCallback = (UnsafeMutableRawPointer, CFArray, CFError?) -> Swift.Void ``` |

Modified [CFStreamCreatePairWithSocketToCFHost(_: CFAllocator?, _: CFHost, _: Int32, _: UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, _: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](https://developer.apple.com/documentation/cfnetwork/1426831-cfstreamcreatepairwithsockettocf)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreatePairWithSocketToCFHost(_ alloc: CFAllocator?, _ host: CFHost, _ port: Int32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |
| To | ``` func CFStreamCreatePairWithSocketToCFHost(_ alloc: CFAllocator?, _ host: CFHost, _ port: Int32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?) ``` |

Modified [CFStreamCreatePairWithSocketToNetService(_: CFAllocator?, _: CFNetService, _: UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, _: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](https://developer.apple.com/documentation/cfnetwork/1426794-cfstreamcreatepairwithsockettone)

|  | Declaration |
| --- | --- |
| From | ``` func CFStreamCreatePairWithSocketToNetService(_ alloc: CFAllocator?, _ service: CFNetService, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` |
| To | ``` func CFStreamCreatePairWithSocketToNetService(_ alloc: CFAllocator?, _ service: CFNetService, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?) ``` |

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
