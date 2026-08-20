---
title: Interacting with the Operating System
apple_id: 10000058i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OperatingSystem/Concepts/host.html
archived_at: '2026-07-15T07:17:35.051881Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interacting with the Operating System](Introduction%20to%20Interacting%20with%20the%20Operating%20System.md)


[Next](Process%20Information.md)[Previous](Introduction%20to%20Interacting%20with%20the%20Operating%20System.md)

# Host Information

An `NSHost` object holds network name and address information for a host. You use this class to get the current host’s name and address and to look up other hosts by name or by address. The class uses available network administration services (such as NetInfo or the Domain Name Service) to discover all requested names and addresses for the host. It does not attempt to contact the host itself, however. This avoids untimely delays due to a host being unavailable, but it may result in incomplete information about the host.

An `NSHost` object contains all of the network addresses and names discovered for a given host by the network administration services. Each `NSHost` object typically contains one unique address, but it may have more than one name. If the host has more than one name, the additional names are usually variations on the same name—typically the basic host name plus the fully qualified domain name. For example, with a host name “`sales`” in the domain “`anycorp.com`”, an `NSHost` object can hold both the names “`sales`” and “`sales.anycorp.com`”.

The `NSHost` class maintains a cache of previously created instances so that requests for an existing `NSHost` object return that object instead of creating a new one. Use the `setHostCacheEnabled:` method to turn the cache off, forcing lookup of hosts as they’re requested. You can also use the `flushHostCache` method to clear the cache of its entries so that subsequent requests look up the host information and create new instances.

THe NSHost class is available in Objective-C only. Java developers can use the `java.net.InetAddress` class instead.

[Next](Process%20Information.md)[Previous](Introduction%20to%20Interacting%20with%20the%20Operating%20System.md)

