---
title: SMB Release Notes
apple_id: TP40007741
resource_type: Release Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/HardwareDrivers/RN-SMB/index.html
archived_at: '2026-07-18T02:58:39.525920Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Network File Services Release Notes (WWDC 2013)

#### Contents:

- [SMB 2.1 Supported for Client and File Server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonbrfvbuqmjnknlte)
- [Replace AFP with SMB 2.1 for Personal File Sharing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonbrfvbuqmjnknltg)

### SMB 2.1 Supported for Client and File Server

1) By default, SMB Client will always attempt multi protocol negotiate from SMB 1 to SMB 2.1

2) By default, SMB File Server will always offer multi protocol negotiate from SMB 1 to SMB 2.1

3) Improved reconnects using SMB 2.1 Durable Handles

4) Minimal Lease support is implemented to just support SMB 2.1 Durable Handles

5) Implemented Compounded Requests to improve performance

6) Larger Read/Write/Transaction I/O sizes are used to improve performance

7) Client will issue multiple read or write requests to improve performance

8) Added Server Side Copies (OS X SMB Client <-> OS X/Windows SMB File Server)

9) DFS, Spotlight and Printing are supported

10) SMB 2.1 Signing is supported which offers improved security compared to SMB 1

11) Specifying “cifs://” will force using only SMB 1. Specifying “smb://” will always try SMB 2.1 first and then fall back to SMB 1

12) Client will prefer using port 445 over port 139

### Replace AFP with SMB 2.1 for Personal File Sharing

1) Finder’s Shared Computers will always prefer SMB 2.1 File Servers over AFP File Servers

2) Uses Kerberos authentication when connecting from OS X to OS X

3) Turning on file sharing turns on both AFP and SMB file sharing

4) Client prefers to use File IDs from `FileInternalInformation` if the server supports them to improve support for OS X File Manager

5) Client supports `getdirentriesattr`, which will improve enumerations of large directories
