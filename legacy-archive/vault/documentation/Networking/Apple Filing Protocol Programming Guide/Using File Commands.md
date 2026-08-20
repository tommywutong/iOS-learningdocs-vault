---
title: Apple Filing Protocol Programming Guide
apple_id: TP40000854
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/AFP/UsingFileCommands/UsingFileCommands.html
archived_at: '2026-07-15T08:18:10.266828Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Filing Protocol Programming Guide](Introduction.md)


[Next](Using%20Combined%20Directory%20and%20File%20Commands.md)[Previous](Using%20Directory%20Commands.md)

# Using File Commands

AFP provides these commands for working on files:

- `FPSetFileDirParms`
- `FPCreateFile`
- `FPCopyFile`
- `FPCreateID` (deprecated)
- `FPDeleteID` (deprecated)

- `FPResolveID`

- `FPExchangeFiles`

The AFP client uses the `FPSetFileParms` command to modify a specified file’s parameters, the `FPCreateFile` command to create a file, and the `FPCopyFile` command to copy a file that exists on a volume managed by a server to any other volume managed by that server. To obtain a specified file’s parameters, the AFP client uses the `FPGetFileDirParms` command, discussed in the next section.

The `FPCreateID` command creates a unique File ID for an existing file, and `FPDeleteID` removes a File ID.

The `FPResolveID` command uses a File ID to retrieve information about a file.

The `FPExchangeFiles` command preserves existing file IDs when an application performs a Save or a Save As operation.

[Next](Using%20Combined%20Directory%20and%20File%20Commands.md)[Previous](Using%20Directory%20Commands.md)

