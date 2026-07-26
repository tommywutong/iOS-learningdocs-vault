---
title: NSError
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/nserror/'
original_language: en
published: 2013-10-14
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:0f3936eb6622a533'
translated: false
---

> 原文：[NSError](https://nshipster.com/nserror/)　·　NSHipster (Mattt)

# [NSError](https://nshipster.com/nserror/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  October 14^th, 2013

> To err is human. To `NSError` is Cocoa.

All programs on a Unix system are a child process of another process, forking all the way from the original process, the unmoved mover: `pid` 1 (which in the case of OS X is `launchd`). When the executable finishes, it communicates a status code between `0` and `255` to its parent, as a way to communicate why or how the process exited. `0` means “everything exited normally; nothing to report here”, while any non-zero value indicates something that the parent process should be aware of. Exit status codes may be used to indicate whether the process crashed, or terminated prematurely. By some conventions, the higher the return value, the more severe the cause of the error.

In an OO paradigm processes are, for the most part, abstracted away, leaving only objects and the messages they pass between one another. That distinction between success and failure (and between different varieties of failure) is still useful in object-oriented programming. But considering that methods are often wont to return values other than `BOOL`, this can create something of a predicament.

Languages more drama-prone and trigger-happy than Objective-C reconcile this by abusing the hell out of exceptions, raising at even the slightest breach in contract. To our good fortune as Cocoanauts, however, Objective-C takes a more civilized approach when it comes to giving us bad news, and that approach is `NSError`.

---

`NSError` is the unsung hero of the Foundation framework. Passed gallantly in and out of perilous method calls, it is the messenger by which we are able to contextualize our failures. No news is good news, when it comes to such matters, but passing a `nil` pointer to an `NSError **` isn’t going to do you any favors.

`NSError` is toll-free bridged with `CFError`, but it’s unlikely that you’ll ever find a reason to dip down to its Core Foundation counterpart.

Each `NSError` object encodes three critical pieces of information: a status `code`, corresponding to a particular error `domain`, as well as additional context provided by a `userInfo` dictionary.

## `code` & `domain`

Like exit status codes, an `NSError -code` signals the nature of the problem. These status codes are defined within a particular error `domain`, in order to avoid overlap and confusion. These status codes are generally defined by constants in an `enum`.

For example, in the `NSCocoaErrorDomain`, the status code for an error caused by `NSFileManager` attempting to access a non-existant file is `4`, as defined by `NSFileNoSuchFileError`. However, `4` in `NSPOSIXErrorDomain` refers to a [POSIX `EINTR`, or “interupted function” error](http://250bpm.com/blog:12).

Now, anyone coming from a systems programming background may have just had a vision of a `switch` statement with smatterings of `printf` to translate numeric constants into something human-readable. `NSError` is way ahead of you.

## `userInfo`

What gives `NSError` its particular charm is everyone’s favorite grab bag property: `userInfo`. As a convention throughout Cocoa, `userInfo` is a dictionary that contains arbitrary key-value pairs that, whether for reasons of subclassing or schematic sparsity, are not suited to full-fledged properties in and of themselves. In the case of `NSError`, there are several special keys that correspond to `readonly` properties.

Three are generally useful:

- `localizedDescription` (`NSLocalizedDescriptionKey`): A localized description of the error.
- `localizedRecoverySuggestion` (`NSLocalizedRecoverySuggestionErrorKey`): A localized recovery suggestion for the error.
- `localizedFailureReason` (`NSLocalizedFailureReasonErrorKey`): A localized explanation of the reason for the error.

…whereas three others are specific to OS X:

- `localizedRecoveryOptions` (`NSLocalizedRecoveryOptionsErrorKey`): An array containing the localized titles of buttons appropriate for displaying in an alert panel
- `recoveryAttempter` (`NSRecoveryAttempterErrorKey`)
- `helpAnchor` (`NSHelpAnchorErrorKey`): Used by an alert panel by a help anchor button.

Here’s how to construct `NSError` with a `userInfo` dictionary:

```
NSDictionary *userInfo = @{
  NSLocalizedDescriptionKey: NSLocalizedString(@"Operation was unsuccessful.", nil),
  NSLocalizedFailureReasonErrorKey: NSLocalizedString(@"The operation timed out.", nil),
  NSLocalizedRecoverySuggestionErrorKey: NSLocalizedString(@"Have you tried turning it off and on again?", nil)
                          };
NSError *error = [NSError errorWithDomain:NSHipsterErrorDomain
                                     code:-57
                                 userInfo:userInfo];
```

The advantage of encapsulating this information in an object like `NSError`, as opposed to, say, throwing exceptions willy-nilly, is that these error objects can be easily passed between different objects and contexts.

For example, a controller that calls a method that populates an `NSError **` (as discussed in the next section) might pass that error into an alert view:

```
[[[UIAlertView alloc] initWithTitle:error.localizedDescription
                            message:error.localizedRecoverySuggestion
                           delegate:nil
                  cancelButtonTitle:NSLocalizedString(@"OK", nil)
                  otherButtonTitles:nil, nil] show];
```

> As a brief non-sequitur: one clever hack used by C functions to communicate errors is to [encode 4-letter ASCII sequences in the 32 bit return type](https://github.com/mattt/Xcode-Snippets/blob/master/checkerror.m). It’s no `localizedDescription`, but it’s better than cross-referencing error codes from a table every time!

For sake of completeness: here is a list of the standard `NSError` `userInfo` keys:

- `NSLocalizedDescriptionKey`
- `NSLocalizedFailureReasonErrorKey`
- `NSLocalizedRecoverySuggestionErrorKey`
- `NSLocalizedRecoveryOptionsErrorKey`
- `NSFilePathErrorKey`
- `NSStringEncodingErrorKey`
- `NSUnderlyingErrorKey`
- `NSRecoveryAttempterErrorKey`
- `NSHelpAnchorErrorKey`

## Using `NSError`

There are two ways in which you will encounter `NSError`: as a consumer and as a producer.

### Consuming

As a consumer, you are primarily concerned with methods that have a final parameter of type `NSError **`. Again, this is to get around the single return value constraint of Objective-C; by passing a pointer to an uninitialized `NSError *` variable, that variable will be populated with any error the method encounters:

```
NSError *error = nil;
BOOL success = [[NSFileManager defaultManager] moveItemAtPath:@"/path/to/target"
                                                       toPath:@"/path/to/destination"
                                                        error:&error];
if (!success) {
    NSLog(@"%@", error);
}
```

> According to Cocoa conventions, methods returning `BOOL` to indicate success or failure are encouraged to have a final `NSError **` parameter if there are multiple failure conditions to distinguish between. A good guideline is whether you could imagine that `NSError` bubbling up, and being presented to the user.

Another way `NSError` objects are passed is the inclusion of an `NSError *` argument in `completionHandler` blocks. This gets around both a constraint on single value returns as well as one on that value being returned synchronously. This has become especially popular with newer Foundation APIs, like `NSURLSession`:

```
NSURL *URL = [NSURL URLWithString:@"http://example.com"];
NSURLRequest *request = [NSURLRequest requestWithURL:URL];
NSURLSession *session = [NSURLSession sessionWithConfiguration:[NSURLSessionConfiguration defaultSessionConfiguration]];
[[session dataTaskWithRequest:request
            completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
    if (!data) {
        NSLog(@"%@", error);
    } else {
        …
    }
}] resume];
```

### Producing

One would be well-advised to follow the same conventions for error handling as other Foundation classes. In situations where a custom method invokes a method with an `NSError **` parameter, it is usually a good idea to similarly pass that `NSError **` parameter into the signature of the custom method. More substantial apps or libraries are encouraged to define their own error domains and error code constants as suitable.

To pass an error to an `NSError **` parameter, do the following:

```
- (BOOL)validateObject:(id)object
                 error:(NSError * __autoreleasing *)outError
{
    // call another API, passing &error into its (NSError **) parameter
    NSError *error = nil;
    BOOL success = ...; 

    if (!success) {
        if (outError) {
            *outError = [NSError errorWithDomain:NSHipsterErrorDomain
                                            code:-42
                                        userInfo:@{NSUnderlyingErrorKey: error}];
        }
    }

    return success;
}
```

The root error, if one exists, should be returned as part of your custom error’s `userInfo` dictionary as the value for `NSUnderlyingErrorKey`.

## `NSURLErrorDomain` & `CFNetworkErrors`

The greatest source of failure in iOS apps is networking. Between radios, transport, data roaming policies, proxies, security, authentication, and any number of protocol-specific negotiation, there is a lot that can go wrong.

On the plus side, the Foundation URL Loading system is incredibly mature, and takes care of most of that for you. The only negative is that the documentation for all of the various things that can go wrong is scattered across different programming guides and headers. If you get a request failing with error `-1004`, it can be _surprisingly_ difficult to figure out exactly what that means.

As such, here is an exhaustive, well-formatted table at your disposal:

| Code | Description |
|---|---|
| -1 `NSURLErrorUnknown` |  |
| 1 `kCFHostErrorHostNotFound` | Indicates that the DNS lookup failed. |
| 2 `kCFHostErrorUnknown` | An unknown error occurred (a name server failure, for example). For additional information, query the kCFGetAddrInfoFailureKey to get the value returned from getaddrinfo; lookup in netdb.h |
| 100 `kCFSOCKSErrorUnknownClientVersion` | The SOCKS server rejected access because it does not support connections with the requested SOCKS version.Query kCFSOCKSStatusCodeKey to recover the status code returned by the server. |
| 101 `kCFSOCKSErrorUnsupportedServerVersion` | The version of SOCKS requested by the server is not supported. Query kCFSOCKSStatusCodeKey to recover the status code returned by the server. Query the kCFSOCKSVersionKey to find the version requested by the server. |

### SOCKS4 Errors

| Code | Description |
|---|---|
| 110 `kCFSOCKS4ErrorRequestFailed` | Request rejected or failed by the server. |
| 111 `kCFSOCKS4ErrorIdentdFailed` | Request rejected because SOCKS server cannot connect to identd on the client. |
| 112 `kCFSOCKS4ErrorIdConflict` | Request rejected because the client program and identd report different user-ids. |
| 113 `kCFSOCKS4ErrorUnknownStatusCode` | The status code returned by the server is unknown. |

### SOCKS5 Errors

| Code | Description |
|---|---|
| 120 `kCFSOCKS5ErrorBadState` | The stream is not in a state that allows the requested operation. |
| 121 `kCFSOCKS5ErrorBadResponseAddr` | The address type returned is not supported. |
| 122 `kCFSOCKS5ErrorBadCredentials` | The SOCKS server refused the client connection because of bad login credentials. |
| 123 `kCFSOCKS5ErrorUnsupportedNegotiationMethod` | The requested method is not supported. Query kCFSOCKSNegotiationMethodKey to find the method requested. |
| 124 `kCFSOCKS5ErrorNoAcceptableMethod` | The client and server could not find a mutually agreeable authentication method. |

### FTP Errors

| Code | Description |
|---|---|
| 200 `kCFFTPErrorUnexpectedStatusCode` | The server returned an unexpected status code. Query the kCFFTPStatusCodeKey to get the status code returned by the server |

### HTTP Errors

| Code | Description |
|---|---|
| 300 `kCFErrorHTTPAuthenticationTypeUnsupported` | The client and server could not agree on a supported authentication type. |
| 301 `kCFErrorHTTPBadCredentials` | The credentials provided for an authenticated connection were rejected by the server. |
| 302 `kCFErrorHTTPConnectionLost` | The connection to the server was dropped. This usually indicates a highly overloaded server. |
| 303 `kCFErrorHTTPParseFailure` | The HTTP server response could not be parsed. |
| 304 `kCFErrorHTTPRedirectionLoopDetected` | Too many HTTP redirects occurred before reaching a page that did not redirect the client to another page. This usually indicates a redirect loop. |
| 305 `kCFErrorHTTPBadURL` | The requested URL could not be retrieved. |
| 306 `kCFErrorHTTPProxyConnectionFailure` | A connection could not be established to the HTTP proxy. |
| 307 `kCFErrorHTTPBadProxyCredentials` | The authentication credentials provided for logging into the proxy were rejected. |
| 308 `kCFErrorPACFileError` | An error occurred with the proxy autoconfiguration file. |
| 309 `kCFErrorPACFileAuth` | The authentication credentials provided by the proxy autoconfiguration file were rejected. |
| 310 `kCFErrorHTTPSProxyConnectionFailure` | A connection could not be established to the HTTPS proxy. |
| 311 `kCFStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod` | The HTTPS proxy returned an unexpected status code, such as a 3xx redirect. |

### CFURLConnection & CFURLProtocol Errors

| Code | Description |
|---|---|
| -998 `kCFURLErrorUnknown` | An unknown error occurred. |
| -999 `kCFURLErrorCancelled` `NSURLErrorCancelled` | The connection was cancelled. |
| -1000 `kCFURLErrorBadURL` `NSURLErrorBadURL` | The connection failed due to a malformed URL. |
| -1001 `kCFURLErrorTimedOut` `NSURLErrorTimedOut` | The connection timed out. |
| -1002 `kCFURLErrorUnsupportedURL` `NSURLErrorUnsupportedURL` | The connection failed due to an unsupported URL scheme. |
| -1003 `kCFURLErrorCannotFindHost` `NSURLErrorCannotFindHost` | The connection failed because the host could not be found. |
| -1004 `kCFURLErrorCannotConnectToHost` `NSURLErrorCannotConnectToHost` | The connection failed because a connection cannot be made to the host. |
| -1005 `kCFURLErrorNetworkConnectionLost` `NSURLErrorNetworkConnectionLost` | The connection failed because the network connection was lost. |
| -1006 `kCFURLErrorDNSLookupFailed` `NSURLErrorDNSLookupFailed` | The connection failed because the DNS lookup failed. |
| -1007 `kCFURLErrorHTTPTooManyRedirects` `NSURLErrorHTTPTooManyRedirects` | The HTTP connection failed due to too many redirects. |
| -1008 `kCFURLErrorResourceUnavailable` `NSURLErrorResourceUnavailable` | The connection’s resource is unavailable. |
| -1009 `kCFURLErrorNotConnectedToInternet` `NSURLErrorNotConnectedToInternet` | The connection failed because the device is not connected to the internet. |
| -1010 `kCFURLErrorRedirectToNonExistentLocation` `NSURLErrorRedirectToNonExistentLocation` | The connection was redirected to a nonexistent location. |
| -1011 `kCFURLErrorBadServerResponse` `NSURLErrorBadServerResponse` | The connection received an invalid server response. |
| -1012 `kCFURLErrorUserCancelledAuthentication` `NSURLErrorUserCancelledAuthentication` | The connection failed because the user cancelled required authentication. |
| -1013 `kCFURLErrorUserAuthenticationRequired` `NSURLErrorUserAuthenticationRequired` | The connection failed because authentication is required. |
| -1014 `kCFURLErrorZeroByteResource` `NSURLErrorZeroByteResource` | The resource retrieved by the connection is zero bytes. |
| -1015 `kCFURLErrorCannotDecodeRawData` `NSURLErrorCannotDecodeRawData` | The connection cannot decode data encoded with a known content encoding. |
| -1016 `kCFURLErrorCannotDecodeContentData` `NSURLErrorCannotDecodeContentData` | The connection cannot decode data encoded with an unknown content encoding. |
| -1017 `kCFURLErrorCannotParseResponse` `NSURLErrorCannotParseResponse` | The connection cannot parse the server’s response. |
| -1018 `kCFURLErrorInternationalRoamingOff` | The connection failed because international roaming is disabled on the device. |
| -1019 `kCFURLErrorCallIsActive` | The connection failed because a call is active. |
| -1020 `kCFURLErrorDataNotAllowed` | The connection failed because data use is currently not allowed on the device. |
| -1021 `kCFURLErrorRequestBodyStreamExhausted` | The connection failed because its request’s body stream was exhausted. |

### File Errors

| Code | Description |
|---|---|
| -1100 `kCFURLErrorFileDoesNotExist` `NSURLErrorFileDoesNotExist` | The file operation failed because the file does not exist. |
| -1101 `kCFURLErrorFileIsDirectory` `NSURLErrorFileIsDirectory` | The file operation failed because the file is a directory. |
| -1102 `kCFURLErrorNoPermissionsToReadFile` `NSURLErrorNoPermissionsToReadFile` | The file operation failed because it does not have permission to read the file. |
| -1103 `kCFURLErrorDataLengthExceedsMaximum` `NSURLErrorDataLengthExceedsMaximum` | The file operation failed because the file is too large. |

### SSL Errors

| Code | Description |
|---|---|
| -1200 `kCFURLErrorSecureConnectionFailed` `NSURLErrorSecureConnectionFailed` | The secure connection failed for an unknown reason. |
| -1201 `kCFURLErrorServerCertificateHasBadDate` `NSURLErrorServerCertificateHasBadDate` | The secure connection failed because the server’s certificate has an invalid date. |
| -1202 `kCFURLErrorServerCertificateUntrusted` `NSURLErrorServerCertificateUntrusted` | The secure connection failed because the server’s certificate is not trusted. |
| -1203 `kCFURLErrorServerCertificateHasUnknownRoot` `NSURLErrorServerCertificateHasUnknownRoot` | The secure connection failed because the server’s certificate has an unknown root. |
| -1204 `kCFURLErrorServerCertificateNotYetValid` `NSURLErrorServerCertificateNotYetValid` | The secure connection failed because the server’s certificate is not yet valid. |
| -1205 `kCFURLErrorClientCertificateRejected` `NSURLErrorClientCertificateRejected` | The secure connection failed because the client’s certificate was rejected. |
| -1206 `kCFURLErrorClientCertificateRequired` `NSURLErrorClientCertificateRequired` | The secure connection failed because the server requires a client certificate. |

### Download and File I/O Errors

| Code | Description |
|---|---|
| -2000 `kCFURLErrorCannotLoadFromNetwork` `NSURLErrorCannotLoadFromNetwork` | The connection failed because it is being required to return a cached resource, but one is not available. |
| -3000 `kCFURLErrorCannotCreateFile` `NSURLErrorCannotCreateFile` | The file cannot be created. |
| -3001 `kCFURLErrorCannotOpenFile` `NSURLErrorCannotOpenFile` | The file cannot be opened. |
| -3002 `kCFURLErrorCannotCloseFile` `NSURLErrorCannotCloseFile` | The file cannot be closed. |
| -3003 `kCFURLErrorCannotWriteToFile` `NSURLErrorCannotWriteToFile` | The file cannot be written. |
| -3004 `kCFURLErrorCannotRemoveFile` `NSURLErrorCannotRemoveFile` | The file cannot be removed. |
| -3005 `kCFURLErrorCannotMoveFile` `NSURLErrorCannotMoveFile` | The file cannot be moved. |
| -3006 `kCFURLErrorDownloadDecodingFailedMidStream` `NSURLErrorDownloadDecodingFailedMidStream` | The download failed because decoding of the downloaded data failed mid-stream. |
| -3007 `kCFURLErrorDownloadDecodingFailedToComplete` `NSURLErrorDownloadDecodingFailedToComplete` | The download failed because decoding of the downloaded data failed to complete. |

### Cookie errors

| Code | Description |
|---|---|
| -4000 `kCFHTTPCookieCannotParseCookieFile` | The cookie file cannot be parsed. |

### CFNetServices Errors

| Code | Description |
|---|---|
| -72000L `kCFNetServiceErrorUnknown` | An unknown error occurred. |
| -72001L `kCFNetServiceErrorCollision` | An attempt was made to use a name that is already in use. |
| -72002L `kCFNetServiceErrorNotFound` | Not used. |
| -72003L `kCFNetServiceErrorInProgress` | A new search could not be started because a search is already in progress. |
| -72004L `kCFNetServiceErrorBadArgument` | A required argument was not provided or was not valid. |
| -72005L `kCFNetServiceErrorCancel` | The search or service was cancelled. |
| -72006L `kCFNetServiceErrorInvalid` | Invalid data was passed to a CFNetServices function. |
| -72007L `kCFNetServiceErrorTimeout` | A search failed because it timed out. |
| -73000L `kCFNetServiceErrorDNSServiceFailure` | An error from DNS discovery; look at kCFDNSServiceFailureKey to get the error number and interpret using dnssd.h |

---

Having scrolled down through that huge table, you might be expecting the usual NSHipster philosophical wrap-up. Not this week. Do you have any idea how long it took to compile that table? It’s all, like, `NSRepetitiveStrainInjury` up in here.

Such are the error of my ways.
