---
title: Apple Filing Protocol Programming Guide
apple_id: TP40000854
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/AFP/UsingVolumeCommands/UsingVolumeCommands.html
archived_at: '2026-07-15T08:18:10.291823Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Filing Protocol Programming Guide](Introduction.md)


[Next](Using%20Directory%20Commands.md)[Previous](AFP%20Client%20Caching.md)

# Using Volume Commands

AFP provides the following volume-level commands:

- `FPOpenVol`
- `FPCloseVol`
- `FPGetVolParms`
- `FPSetVolParms`
- `FPFlush`
- `FPCatSearch` and `FPCatSearchExt`

After obtaining the volume names through the `FPGetSrvrParms` command, the AFP client sends an `FPOpenVol` command for each volume to which it wants to gain access. If a volume has a password, it must be supplied at this time. The command returns the requested volume parameters, including the volume identifier, _VolumeID_.

The volume identifier is used in all subsequent commands to identify the volume for which the commands apply and remains valid until the session is terminated by calling `FPLogout` or the volume is closed by calling `FPVolClose`.

After obtaining the volume’s volume identifier, the AFP client can obtain the volume’s parameters by calling `FPGetVolParms`. The AFP client can also change the volume’s parameters by calling `FPSetVolParms`.

The `FPFlush` command requests that the server flush (write to disk) any data associated with a particular volume.

The `FPCatSearch` and `FPCatSearchExt` commands search a volume for files that match specified criteria. The `FPCatSearchExt` command differs from the `FPCatSearch` command in that `FPCatSearchExt` is prepared to handle the larger values that may be returned for searches on volumes greater than 4 GB in size.

[Next](Using%20Directory%20Commands.md)[Previous](AFP%20Client%20Caching.md)

