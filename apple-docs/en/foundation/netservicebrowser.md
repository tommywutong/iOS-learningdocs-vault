---
title: NetServiceBrowser
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservicebrowser
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowser.json'
content_hash: 'sha256:58b17ca881c0b9b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NetServiceBrowser

<sub>Class</sub>

A network service browser that finds published services on a network using multicast DNS.

> [!warning] Deprecated
> Use nw_browser_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class NetServiceBrowser
```

## Overview

Services can range from standard services, such as HTTP and FTP, to custom services defined by other applications. You can use a network service browser in your code to obtain the list of accessible domains and then to obtain an [NetService](netservice.md) object for each discovered service. Each network service browser performs one search at a time, so if you want to perform multiple simultaneous searches, use multiple network service browsers.

A network service browser performs all searches asynchronously using the current run loop to execute the search in the background. Results from a search are returned through the associated delegate object, which your client application must provide. Searching proceeds in the background until the object receives a [- stop](<netservicebrowser/stop().md>) message.

To use an `NSNetServiceBrowser` object to search for services, allocate it, initialize it, and assign a delegate. (If you wish, you can also use the [- scheduleInRunLoop:forMode:](<netservicebrowser/schedule(in_formode_).md>) and [- removeFromRunLoop:forMode:](<netservicebrowser/remove(from_formode_).md>) methods to execute searches on a run loop other than the current one.) Once your object is ready, you begin by gathering the list of accessible domains using either the [- searchForRegistrationDomains](<netservicebrowser/searchforregistrationdomains().md>) or [- searchForBrowsableDomains](<netservicebrowser/searchforbrowsabledomains().md>) methods. From the list of returned domains, you can pick one and use the [- searchForServicesOfType:inDomain:](<netservicebrowser/searchforservices(oftype_indomain_).md>) method to search for services in that domain.

The `NSNetServiceBrowser` class provides two ways to search for domains. In most cases, your client should use the [- searchForRegistrationDomains](<netservicebrowser/searchforregistrationdomains().md>) method to search only for local domains to which the host machine has registration authority. This is the preferred method for accessing domains as it guarantees that the host machine can connect to services in the returned domains. Access to domains outside this list may be more limited.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Network Service Browsers

- [- init](<netservicebrowser/init().md>) — Initializes an allocated [NetServiceBrowser](netservicebrowser.md) object. _(deprecated)_

### Configuring Network Service Browsers

- [delegate](netservicebrowser/delegate.md) — The delegate object for this instance. _(deprecated)_
- [includesPeerToPeer](netservicebrowser/includespeertopeer.md) — Whether to browse over peer-to-peer Bluetooth and Wi-Fi, if available. _(deprecated)_

### Using Network Service Browsers

- [- searchForBrowsableDomains](<netservicebrowser/searchforbrowsabledomains().md>) — Initiates a search for domains visible to the host. This method returns immediately. _(deprecated)_
- [- searchForRegistrationDomains](<netservicebrowser/searchforregistrationdomains().md>) — Initiates a search for domains in which the host may register services. _(deprecated)_
- [- searchForServicesOfType:inDomain:](<netservicebrowser/searchforservices(oftype_indomain_).md>) — Starts a search for services of a particular type within a specific domain. _(deprecated)_
- [- stop](<netservicebrowser/stop().md>) — Halts a currently running search or resolution. _(deprecated)_

### Managing Run Loops

- [- scheduleInRunLoop:forMode:](<netservicebrowser/schedule(in_formode_).md>) — Adds the receiver to the specified run loop. _(deprecated)_
- [- removeFromRunLoop:forMode:](<netservicebrowser/remove(from_formode_).md>) — Removes the receiver from the specified run loop. _(deprecated)_

## See Also

### Service Discovery

- [NetServiceBrowserDelegate](netservicebrowserdelegate.md) — The interface a net service browser uses to inform a delegate about the state of service discovery.
