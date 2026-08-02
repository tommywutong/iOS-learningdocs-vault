---
title: Apple Filing Protocol Programming Guide
apple_id: TP40000854
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/AFP/UsingCombinedDirectoryandFileCommands/UsingCombinedDirectoryandFileCommands.html
archived_at: '2026-07-15T08:18:10.220459Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Filing Protocol Programming Guide](Introduction.md)


[Next](Using%20Fork%20Commands.md)[Previous](Using%20File%20Commands.md)

# Using Combined Directory and File Commands

AFP provides five commands that operate on both files and directories:

- `FPGetFileDirParms`
- `FPSetFileDirParms`
- `FPRename`
- `FPDelete`
- `FPMoveAndRename`

The AFP client uses the `FPGetFileDirParms` command to retrieve the parameters associated with a given file or directory. When it uses this command, the AFP client does not need specify whether the CNode is a file or directory; the file server indicates the CNode’s type in response to this command.

The `FPSetFileDirParms` command is used to set the parameters of a file or directory. When the AFP client uses this command, it need not specify whether the object is a file or directory. This command allows the AFP client to set only those parameters that are common to both types of CNodes.

The `FPRename` command is used to rename files and directories.

The `FPDelete` command is used to delete a file or directory. A file can be deleted only if it is not open; a directory can be deleted only if it is empty.

The `FPMoveandRename` command is used to move a file or a directory from one parent directory to another on the same volume. The moved CNode can renamed at the same time.

[Next](Using%20Fork%20Commands.md)[Previous](Using%20File%20Commands.md)

