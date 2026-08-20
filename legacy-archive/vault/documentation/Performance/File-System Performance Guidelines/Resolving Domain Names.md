---
title: File-System Performance Guidelines
apple_id: 10000161i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/FileSystem/Articles/ResolvingDomainNames.html
archived_at: '2026-07-18T01:48:44.470766Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File-System Performance Guidelines](Introduction%20to%20File-System%20Performance%20Guidelines.md)


[Next](Tracking%20File-System%20Changes.md)[Previous](Iterating%20Directory%20Contents.md)

# Resolving Domain Names

With the advent of IPv6, you may be tempted to use the `getaddrinfo` function to perform name or IP address resolution. However, use of this function can lead to extreme performance problems in some situations, such as large NetInfo networks. The `getaddrinfo` function is very general in nature and can cause multiple network operations to occur.

The CFNetwork family of routines provides a convenient way to do simple name-to-IP lookups. These routines support the fast lookup of host names and do so in a non-blocking fashion. More importantly, they retrieve precisely the information you need.

Beginning with OS X version 10.3, you can also use the CFHost family of routines to perform lookups. CFHost supports hostname lookup in both IPv4 and IPv6 automatically, so you do not need to rewrite your code to support both. As with the CFNetwork routines, CFHost routines are fast and non-blocking.

For more information on CFNetwork and CFHost, see the Core Foundation reference.

If you are performing a simple name-to-IP lookup, you can also use the BSD functions `getipnodebyname` and `getipnodebyaddr` instead of `getaddrinfo`. In OS X version 10.2 and later, these functions are threadsafe, reentrant, and take advantage of the networking subsystem’s IP address caching capabilities to improve performance. You can also use `getipnodebyname` to resolve domain names instead of `getipnodebyname`. For example, if you have code such as the following:

```
struct hostent * hostentry;

hostentry = gethostbyname(name);
    /* ...do something with the hostentry structure*/
```

You can replace it with the following IPv6-savvy code:

```
struct hostent * hostentry;

hostentry = getipnodebyname(name, AF_INET6, AI_DEFAULT, &error_num);
    /* ...do something with the hostentry structure*/
freehostent(hostentry);
```

The new code will handle both IPv4 and IPv6 addresses. Note that you must call the `freehostent` function to release the `hostent` data structure when you are finished with it.

[Next](Tracking%20File-System%20Changes.md)[Previous](Iterating%20Directory%20Contents.md)

