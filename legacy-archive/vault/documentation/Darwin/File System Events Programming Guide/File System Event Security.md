---
title: File System Events Programming Guide
apple_id: TP40005289
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/FSEvents_ProgGuide/FileSystemEventSecurity/FileSystemEventSecurity.html
archived_at: '2026-07-15T07:23:04.129159Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Events Programming Guide](Introduction.md)


[Next](Kernel%20Queues-%20An%20Alternative%20to%20File%20System%20Events.md)[Previous](Using%20the%20File%20System%20Events%20API.md)

# File System Event Security

The file system events API poses an interesting challenge for security. Because it provides the file system path leading up to changed content, storing that information in a persistent database, it represents a new avenue for information leaks, albeit only of the names of directories.

The file system events API mediates this concern in two ways: permissions and prevention.

The most obvious security concern related to file system events is one of privacy. If Bob can see a list of events from changes to Alice’s home directory, Bob might see things that Alice does not want him to see. For example, Alice might have a directory name that coincides with the code name of an unreleased Apple product.

To prevent this potential security leak, users do not receive any events unless the user can reach the modified directory through standard file system permissions.

When files or directories are deleted, these events look just like any other file system event. This means that directory names will linger on your computer even after a file is deleted.

It is not possible to remove individual records programmatically. The only way to remove prior entries in the database is to purge all entries prior to a particular entry ID. You can do this by calling [FSEventsPurgeEventsForDeviceUpToEventId](https://developer.apple.com/documentation/coreservices/1447985-fseventspurgeeventsfordeviceupto) in your application.

While the gzipped data is stored in a series of files in the `.fseventsd` directory at the root level of each volume (accessible only by the root user), you should never work with the data directly, as the format of these files may change at any time.

In some cases, the contents of a volume are sufficiently secret that it is not appropriate to log them. To disable logging on a per-volume basis (for creating a backup volume, for example), you must do the following:

- Create a `.fseventsd` directory at the top level of the volume.
- Create an empty `no_log` file in that directory.

So if your volume is mounted at `/Volumes/MyDisk`, you would create an empty file called `/Volumes/MyDisk/.fseventsd/no_log`.

[Next](Kernel%20Queues-%20An%20Alternative%20to%20File%20System%20Events.md)[Previous](Using%20the%20File%20System%20Events%20API.md)

