---
title: OS X Server Failover Messaging Architecture Guide
apple_id: TP40001804
resource_type: Guide
platform: macOS
topic: System Administration
technology: null
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/documentation/MacOSXServer/Conceptual/XServer_Failover_Msg/Preface/Preface.html
archived_at: '2026-07-15T08:16:40.460113Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Concepts.md)

# About This Manual

This manual describes new failover procedures for AFP, NFS, and SMB in OS X v10.4. The failover model consists of two nodes – a master node and a backup node – each running a daemon that monitors, announces, and synchronizes changes to file service settings. Third-party software can use the NSDistributedNotificationCenter to issue messages or to receive notifications of changes to configuration settings or of cluster events, such as refresh, failover, and terminate.

The `Letter Gothic` font is used to indicate text that you type or see displayed. This manual includes special text elements to highlight important or supplemental information:

For information about NSDistributedNotificationCenter, see [NSDistributedNotificationCenter](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter).

[Next](Concepts.md)

