---
title: CFNetwork Framework Release Notes
apple_id: TP40000990
resource_type: Release Note
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2008-06-05'
source_url: https://developer.apple.com/library/archive/releasenotes/Networking/RN-CFNetwork/index.html
archived_at: '2026-07-18T02:58:59.080344Z'
---
> 导航：[总目录](../README.md) · [releasenotes](../_indexes/releasenotes.md)



# CFNetwork Framework Release Notes for OS X v10.5 and v10.6

CFNetwork is a framework which provides C APIs for common Internet protocols such as HTTP, FTP, and others. These APIs are designed with portability, performance, and consistency in mind, and are available to Cocoa and Carbon applications. CFNetwork is part of the CoreServices umbrella framework. Simply linking with CoreServices will make the CFNetwork framework available for use.

This document describes the changes in CFNetwork since OS X v10.4, Tiger. Note that you may be able to find more information on many of these changes in Apple's developer documentation.

#### Contents:

- [CFError](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsojqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Changes in CFNetworkErrors.h for OS X v10.5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsojqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [New API available for OS X v10.5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsojqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [New API available for OS X v10.6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsojqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6oa)

### CFError

CFError is a new CFType introduced in CoreFoundation for reporting errors; see the _[Core Foundation Release Notes for OS X v10.9](https://developer.apple.com/library/archive/releasenotes/CoreFoundation/RN-CoreFoundation/index.html#//apple_ref/doc/uid/TP40000994)_ for more details on CFError. In Leopard, CFNetwork has adopted CFError. As such, CFNetwork provides its own error domains, error codes and user info entries in a new header file named CFNetworkErrors.h These new domains and error codes are listed below. Do reference the header file CFNetworkErrors.h for the most up to date information.

### Changes in CFNetworkErrors.h for OS X v10.5

|  |  |
| --- | --- |
| **Error domains:** | : `const CFStringRef kCFErrorDomainCFNetwork;` |
| **Error keys and codes that can be obtained from the CFError's userInfo dictionary:** | : When an error of kCFHostErrorUnknown is returned, this key's value is set to a CFNumber containing the raw error value returned by getaddrinfo()  `const CFStringRef kCFGetAddrInfoFailureKey;` |
| **When a SOCKS failure has occurred, this key's value is set to a CFString containing the status value returned by the SOCKS server.** | : `const CFStringRef kCFSOCKSStatusCodeKey;` |
| **When an error of kCFSOCKSErrorUnsupportedServerVersion is returned, this key's value is set to a CFString containing the version number requested by the server.** | : `const CFStringRef kCFSOCKSVersionKey;` |
| **When an error of kCFSOCKS5ErrorUnsupportedNegotiationMethod is returned, this key's value is set to a CFString containing the negotiation method requested by the server.** | : `const CFStringRef kCFSOCKSNegotiationMethodKey;` |
| **When an error of kCFNetServicesErrorDNSServiceFailure is returned, this key's value is set to a CFNumber containing the value returned from DNS; interret it using the values dns_sd.h** | : const CFStringRef kCFDNSServiceFailureKey; |
| **When an error of kCFFTPErrorUnexpectedStatusCode is returned, this key's value is set to a CFString containing the status code returned by the server.** | : `const CFStringRef kCFFTPStatusCodeKey;` |
| **When an error of kCFFTPErrorUnexpectedStatusCode is returned, this key's value is set to a CFString containing the status code returned by the server.** | : `const CFStringRef kCFFTPStatusCodeKey;` |

Please see [Reference Library > Core Foundation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000421) for more details on the CFError type.

### New API available for OS X v10.5

### CFNetServices.h

`SInt32 CFNetServiceGetPortNumber(CFNetServiceRef theService);`

Query a Network Service for its port number. The function parameter, "theService", is the Network Service instance to be queried and it must be non-NULL. It returns an SInt32 containing the port number in host byte order. On error, it returns -1 if the entity's port is not known (has not been resolved)

### CFProxySupport.h

`CFArrayRef CFNetworkCopyProxiesForURL(CFURLRef url, CFDictionaryRef proxySettings);`

Given an URL and a proxy dictionary, determines the ordered list of proxies that should be used to download the given URL. The parameter, "url", specifies which CFURLRef to find proxy information for. The "proxySettings" parameter is a dictionary describing the available proxy settings; the dictionary's format should match that described in and returned by SystemConfiguration.framework. This function returns an array of dictionaries; each dictionary describes a single proxy.

`CFArrayRef CFNetworkCopyProxiesForAutoConfigurationScript(CFStringRef proxyAutoConfigurationScript, CFURLRef targetURL);`

Thus function executes the script given in "proxyAutoConfigurationScript", using "targetURL" as input. It will return an array of proxies as returned by the script.

```
CFRunLoopSourceRefCFNetworkExecuteProxyAutoConfigurationURL(CFURLRef proxyAutoConfigURL,
                                         CFURLRef targetURL,
CFProxyAutoConfigurationResultCallback cb,
                                         CFStreamClientContext *clientContext);
```

Asynchronously downloads the autoconfiguration script from the given URL, then runs that script using "targetURL" as input. Once completed, the callback "cb" is called via the run loop, passing the proxy array returned by the script. Note that the caller must schedule the returned run loop source on a running run loop in order to receive the callback.

Proxy Type Keys - see CFProxySupport.h for more details

```
const CFStringRef kCFProxyTypeKey;
const CFStringRef kCFProxyTypeNone;
const CFStringRef kCFProxyTypeHTTP;
const CFStringRef kCFProxyTypeHTTPS;
const CFStringRef kCFProxyTypeSOCKS;
const CFStringRef kCFProxyTypeFTP;
const CFStringRef kCFProxyTypeAutoConfigurationURL;
```

Key for the proxy's hostname; value is a CFString. Note that this may be an IPv4 or IPv6 dotted-IP string.

`const CFStringRef kCFProxyHostNameKey;`

Key for the proxy's port number; value is a CFNumber specifying the port on which to contact the proxy.

`const CFStringRef kCFProxyPortNumberKey;`

Key for the proxy's PAC file location; this key is only present if the proxy's type is kCFProxyTypeAutoConfigurationURL. Value is a CFURL specifying the location of a proxy auto-configuration file.

`const CFStringRef kCFProxyAutoConfigurationURLKey;`

Key for the username to be used with the proxy; value is a CFString. Note that this key will only be present if the username could be extracted from the information passed in. No external credential stores (like the Keychain) are consulted.

`const CFStringRef kCFProxyUsernameKey;`

Key for the password to be used with the proxy; value is a CFString. Note that this key will only be present if the username could be extracted from the information passed in. No external credential stores (like the Keychain) are consulted.

`const CFStringRef kCFProxyPasswordKey;`

### CFHTTPStream.h

Stream property key, for copy operations. The value is the CFHTTPMessage transmitted by the stream, after all modifications (such as for authentication, connection policy, or redirection) have been made.

`const CFStringRef kCFStreamPropertyHTTPFinalRequest;`

### CFHTTPMessage.h

These two strings represent authentication methods that are supported in CFNetwork.

`const CFStringRef kCFHTTPAuthenticationSchemeNTLM;`

`const CFStringRef kCFHTTPAuthenticationSchemeNegotiate;`

### New API available for OS X v10.6

### CFProxySupport.h

In order to simply the programming model around using proxies with CFNetwork, we added support for getting the system stored internet proxy settings directly to CFNetwork. Prior to this, one had to use the SystemConfiguration framework to retrieve the proxies and CFNetwork to set the proxies on the stream.

```
CFDictionaryRef CFNetworkCopySystemProxySettings( void );
```

This function returns a dictionary containing key-value pairs that represent the current internet proxy settings. See below for definitions of the keys and values. Returns NULL if no proxy settings have been defined or if an error was encountered. The caller is responsible for releasing the returned dictionary.

> [!NOTE]
> 

```
const CFStringRef kCFNetworkProxiesExceptionsList
```

Key for the list of host name patterns that should bypass the proxy; value is a CFArray of CFStrings.

```
const CFStringRef kCFNetworkProxiesExcludeSimpleHostnames
```

Key whose value indicates if simple hostnames will be excluded; value is a CFNumber. Simple hostnames will be excluded if the key is present and has a non-zero value.

```
const CFStringRef kCFNetworkProxiesFTPEnable
```

Key for the enabled status of the ftp proxy; value is a CFNumber. The proxy is enabled if the key is present and has a non-zero value.

```
const CFStringRef kCFNetworkProxiesFTPPassive
```

Key for the state of passive mode for the ftp proxy; value is a CFNumber. A value of one indicates that passive mode is enabled, a value of zero indicates that passive mode is not enabled.

```
const CFStringRef kCFNetworkProxiesFTPPort
```

Key for the port number associated with the ftp proxy; value is a CFNumber which is the port number.

```
const CFStringRef kCFNetworkProxiesFTPProxy
```

Key for the host name associated with the ftp proxy; value is a CFString which is the proxy host name.

```
const CFStringRef kCFNetworkProxiesGopherEnable
```

Key for the enabled status of the gopher proxy; value is a CFNumber. The proxy is enabled if the key is present and has a non-zero value.

```
const CFStringRef kCFNetworkProxiesGopherPort
```

Key for the port number associated with the gopher proxy; value is a CFNumber which is the port number.

```
const CFStringRef kCFNetworkProxiesGopherProxy
```

Key for the host name associated with the gopher proxy; value is a CFString which is the proxy host name.

```
const CFStringRef kCFNetworkProxiesHTTPEnable
```

Key for the enabled status of the HTTP proxy; value is a CFNumber. The proxy is enabled if the key is present and has a non-zero value.

```
const CFStringRef kCFNetworkProxiesHTTPPort
```

Key for the port number associated with the HTTP proxy; value is a CFNumber which is the port number.

```
const CFStringRef kCFNetworkProxiesHTTPProxy
```

Key for the host name associated with the HTTP proxy; value is a CFString which is the proxy host name.

```
const CFStringRef kCFNetworkProxiesHTTPSEnable
```

Key for the enabled status of the HTTPS proxy; value is a CFNumber. The proxy is enabled if the key is present and has a non-zero value.

```
const CFStringRef kCFNetworkProxiesHTTPSPort
```

Key for the port number associated with the HTTPS proxy; value is a CFNumber which is the port number.

```
const CFStringRef kCFNetworkProxiesHTTPSProxy
```

Key for the host name associated with the HTTPS proxy; value is a CFString which is the proxy host name.

```
const CFStringRef kCFNetworkProxiesRTSPEnable
```

Key for the enabled status of the RTSP proxy; value is a CFNumber. The proxy is enabled if the key is present and has a non-zero value.

```
const CFStringRef kCFNetworkProxiesRTSPPort
```

Key for the port number associated with the RTSP proxy; value is a CFNumber which is the port number.

```
const CFStringRef kCFNetworkProxiesRTSPProxy
```

Key for the host name associated with the RTSP proxy; value is a CFString which is the proxy host name.

```
const CFStringRef kCFNetworkProxiesSOCKSEnable
```

Key for the enabled status of the SOCKS proxy; value is a CFNumber. The proxy is enabled if the key is present and has a non-zero value.

```
const CFStringRef kCFNetworkProxiesSOCKSPort
```

Key for the port number associated with the SOCKS proxy; value is a CFNumber which is the port number.

```
const CFStringRef kCFNetworkProxiesSOCKSProxy
```

Key for the host name associated with the SOCKS proxy; value is a CFString which is the proxy host name.

```
const CFStringRef kCFNetworkProxiesProxyAutoConfigEnable
```

Key for the enabled status ProxyAutoConfig (PAC); value is a CFNumber. ProxyAutoConfig is enabled if the key is present and has a non-zero value.

```
const CFStringRef kCFNetworkProxiesProxyAutoConfigURLString
```

Key for the url which indicates the location of the ProxyAutoConfig (PAC) file; value is a CFString which is url for the PAC file.

```
const CFStringRef kCFNetworkProxiesProxyAutoDiscoveryEnable
```

Key for the enabled status of proxy auto discovery; value is a CFNumber. Proxy auto discovery is enabled if the key is present and has a non-zero value.
