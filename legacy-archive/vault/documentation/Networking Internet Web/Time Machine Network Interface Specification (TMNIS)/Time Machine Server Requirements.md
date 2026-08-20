---
title: Time Machine Network Interface Specification (TMNIS)
apple_id: TP40008951
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2009-08-19'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/TimeMachineNetworkInterfaceSpecification/TimeMachineRequirements/TimeMachineRequirements.html
archived_at: '2026-07-18T01:36:10.856535Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Time Machine Network Interface Specification (TMNIS)](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction.md)

# Time Machine Server Requirements

Not all AFP servers support the functionality required for Time Machine backups. In order to support Time Machine, a server must implement the following:

- Lock stealing—when the client logs in, it sends the `FPGetSessionToken` command. Upon receiving this command, if the _Type_ field is set to `kLoginWithTimeAndID`, `kReconnWithTimeAndID`, `kRecon1Login`, or `kRecon1ReconnectLogin`, the server searches through any previous sessions. Previous sessions from the same user that contain a Time Machine sharepoint are destroyed, releasing all locks associated with those previous sessions. Due to the nature of lock stealing, it is recommended that sharepoints designated for Time Machine backups be used exclusively for Time Machine backups and not for general file sharing use.
- Client reconnect and state recovery—AFP 3.3 supports a replay cache for correct Time Machine behavior over AFP. Supporting and advertising this cache is required for all AFP Servers that want to support Time Machine. For more information, see [AFP Replay Cache](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/AFP/AFPReplayCache/AFPReplayCache.html#//apple_ref/doc/uid/TP40000854-CH227), [Reconnect](../../Networking/Apple%20Filing%20Protocol%20Programming%20Guide/AFP%20File%20Server%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df53xe2lumvzgszbpifdfax2smvrw63tomvrxix2vifgq), and [Reconnecting Sessions](../../Networking/Apple%20Filing%20Protocol%20Programming%20Guide/Apple%20Filing%20Protocol%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df53xe2lumvzgszbpifdfax2smvrw63tomvrxi2lom5pvgzltonuw63tt) in _[Apple Filing Protocol Programming Guide](../../Networking/Apple%20Filing%20Protocol%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnju)_.
- A compliant server must implement the deny modes of `FPOpenFork` as mandatory locks.
- A compliant server must set the `kSupportsTMLockSteal` bit in the response to the `FPGetVolParms` for AFP volumes designated to support Time Machine backups. See the `FPGetVolParms` documentation for more information.
- A compliant server must support the `FPSyncDir` and `FPSyncFork` (directory/fork data full sync and commit) AFP commands.
- Bonjour discovery—Time Capsule or OS X Server with a Time Machine sharepoint advertises itself through Bonjour as supporting Time Machine backups over AFP. This is required for the server to show up automatically in Time Machine’s preferences pane when you select "Change Disk...".

  Each network storage server with suitable AFP share points must register and publish an mDNS service record with a type of `"_adisk._tcp"`.

  This service includes a `TXT` record with entries that correspond to an exported volume available for sharing.

  The name portion of each entry is a unique key string. The value portion of the entry is a comma-separated list of subkey/subvalue pairs with the subkey and subvalue separated by an equal sign (`=`). Each subkey is a 4-character property code (for example, `adVN` for the name of the volume). The subvalue is the UTF-8 text associated with the specified property. Commas (`,`) and backslashes (`\`) are escaped with a backslash (for example, `\,` for a literal comma character).

  The following property codes are currently required for Time Machine discovery:

  **`adVN`**
  : UTF-8 name for the volume. This is also the share name used for mounting the volume.

  **`adVF`**
  : `AirDiskVolumeFlags` as a hex value string.

  The flags value should be set to `0x81` to indicate that Time Machine is supported on this AFP volume:

  **0x0001**
  : AFP is supported for this volume.

  **0x0080**
  : Time machine should allow this as a backup destination.

  The following is an example of a `TXT` record for the volume “Backups”:

```
dk0=adVN=Backups,adVF=0x81
```

For more information, see _[Bonjour Overview](../../Cocoa/Bonjour%20Overview/About%20Bonjour.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyts2i)_.

[Next](Document%20Revision%20History.md)[Previous](Introduction.md)

