---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSSocketUtilities.html
archived_at: '2026-07-15T08:13:56.555374Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

# NSSocketUtilities

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

This class provides an easy way to get a TCP socket with a connection timeout. The static methods in this class correspond to all of the java.net.Socket constructors. See Sun's documentation for the java.net.Socket class for more information.

Calling [getSocketWithTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3pmnvwk5cvoruwy2lunfsxgl3hmv2fg33dnnsxiv3jorufi2lnmvxxk5a) will either return a socket, or will throw an IOException if it times out (because a socket cannot be created). When a new socket is requested with [getSocketWithTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3pmnvwk5cvoruwy2lunfsxgl3hmv2fg33dnnsxiv3jorufi2lnmvxxk5a), the polling interval regulates how often that socket is requested. By default, the polling interval is 100 milliseconds, and can be changed using [setPollingInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3pmnvwk5cvoruwy2lunfsxgl3tmv2fa33mnruw4z2jnz2gk4twmfwa). A timeout argument is passed to [getSocketWithTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3pmnvwk5cvoruwy2lunfsxgl3hmv2fg33dnnsxiv3jorufi2lnmvxxk5a), and the socket request times out when a timer that keeps track of the total polling time exceeds the timeout value.

This class only contains static methods. It is never instantiated.

## Method Types

---

> **All methods**
>
> : [getSocketWithTimeout](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3pmnvwk5cvoruwy2lunfsxgl3hmv2fg33dnnsxiv3jorufi2lnmvxxk5a): [pollingInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3pmnvwk5cvoruwy2lunfsxgl3qn5wgy2lom5ew45dfoj3gc3a): [setPollingInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3pmnvwk5cvoruwy2lunfsxgl3tmv2fa33mnruw4z2jnz2gk4twmfwa)

## Static Methods

---

### getSocketWithTimeout

`public static java.net.Socket getSocketWithTimeout( String remoteHost, int remotePort, java.net.InetAddress localInetAddress, int localPort, int timeOut) throws java.net.UnknownHostException, java.io.IOException`

Creates a socket and connects it to the port specified by _remotePort_ at the host specified by _remoteHost_. Binds the socket to the local port specified by _localPort_ at the local host specified by _localInetAddress_ with a timeout specified by _timeout_. Throws an UnknownHostException if _remoteHost_ cannot be resolved. Throws an IOException if the socket can't be created.

`public static java.net.Socket getSocketWithTimeout( String remoteHost, int remotePort, int timeout) throws java.net.UnknownHostException, java.io.IOException`

Creates a socket and connects it to the port specified by _remotePort_ at the host specified by _remoteHost_ with a timeout specified by _timeout_. Throws an UnknownHostException if _remoteHost_ cannot be resolved. Throws an IOException if the socket can't be created.

`public static java.net.Socket getSocketWithTimeout( InetAddress remoteAddress, int remotePort, int timeout) throws java.io.IOException`

Creates a socket and connects it to the port specified by _remotePort_ at the host specified by _remoteAddress_ with a timeout specified by _timeout_. Throws an IOException if the socket can't be created.

`public static Socket getSocketWithTimeout( InetAddress remoteAddress, int remotePort, InetAddress localAddress, int localPort, int timeout) throws java.io.IOException`

Creates a socket and connects it to the port specified by _remotePort_ at the host specified by _remoteAddress_. Binds the socket to the local port specified by _localPort_ at the local host specified by _localAddress_ with a timeout specified by _timeout_. Throws an IOException if the socket can't be created.

---

### pollingInterval

`public static int pollingInterval()`

Returns the polling interval in milleseconds. The default polling interval is 100 milliseconds. It can be changed with [setPollingInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgu3pmnvwk5cvoruwy2lunfsxgl3tmv2fa33mnruw4z2jnz2gk4twmfwa). See the ["Class Description"](#apple-inauqskjjjdug) section for more information.

---

### setPollingInterval

`public static void setPollingInterval(int interval)`

Sets the polling interval to _interval_ provided _interval_ is greater than 0. See the ["Class Description"](#apple-inauqskjjjdug) section for more information.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
