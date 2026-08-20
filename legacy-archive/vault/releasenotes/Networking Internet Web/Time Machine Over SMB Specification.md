---
title: Time Machine Over SMB Specification
apple_id: TP40017496
resource_type: Release Note
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/NetworkingInternetWeb/Time_Machine_SMB_Spec/index.html
archived_at: '2026-07-18T02:59:00.958873Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Time Machine over SMB Specification

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Supporting the Timeout Field in SMB2_CREATE_DURABLE_HANDLE_REQUEST_V2 Requests](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnknltk)
- [Advertising Time Machine Availability Through Bonjour](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnknltc)
- [Validating the Time Machine Backup Destination](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Supporting the F_FULLFSYNC Extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnknlte)

### Introduction

Time Machine is a technology for backing up computers to local and network volumes. This document describes the requirements for SMB servers to support Time Machine backups. These requirements are as follows:

- SMB protocol version 3.x, including SMB 3.x signing
- Handling of `SMB2_CREATE_DURABLE_HANDLE_REQUEST_V2` requests, including the `Timeout` field. For more information, see the [Supporting the Timeout Field in SMB2_CREATE_DURABLE_HANDLE_REQUEST_V2 Requests](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnknltk) section below.
- Handling of `SMB2_CREATE_REQUEST_LEASE_V2` requests
- Handling of `SMB2_CREATE_DURABLE_HANDLE_RECONNECT_V2` requests
- Support for Bonjour discovery. For more information, see the [Advertising Time Machine Availabilty Through Bonjour](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnknltc) section below.
- Support for Apple’s `F_FULLFSYNC` extension to the `SMB2 FLUSH` command. For more information, see the [Supporting the F_FULLFSYNC Extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnknlte) section below.

### Supporting the Timeout Field in SMB2_CREATE_DURABLE_HANDLE_REQUEST_V2 Requests

The server must correctly honor the `Timeout` field of SMB2_CREATE_DURABLE_HANDLE_REQUEST_V2 requests. Time Machine clients may set timeouts as short as 30 seconds or less. The `Timeout` field in the server’s response must be set to indicate the amount of time the server will wait for a reconnect after a failover for this particular file.

### Advertising Time Machine Availability Through Bonjour

Bonjour, also known as zero-configuration networking, enables automatic discovery of devices and services on a local network using industry-standard IP protocols. SMB servers with a Time Machine share point must advertise themselves through Bonjour as supporting Time Machine backups over SMB. This is required for the server to show up automatically in Time Machine’s preference pane when a user clicks the Select Disk button.

Each network storage server must indicate that SMB share points are available on the server by registering and publishing an mDNS server record with type `_smb._tcp` and port 445. Each network storage server must also advertise that these SMB share points are available to clients for Time Machine backups by registering and publishing an mDNS service record with a type `_adisk._tcp`. The `_smb._tcp` and `_adisk._tcp` services must be advertised using the same service name.

The `_adisk._tcp` service includes a `TXT` record with entries that correspond to an exported volume available for sharing. The name portion of each entry is a unique key string. The value portion of each entry is a comma-separated list of subkey–subvalue pairs with the subkey and subvalue separated by an equal sign (`=`). Each subkey is a 4-character property code (for example, `adVN` for the name of the volume). The subvalue is the UTF-8 text associated with the specified property. Commas (`,`) and backslashes (`\`) are escaped with a backslash (for example, `\,` for a literal comma character).

The adVN and adVF property codes are required to advertise Time Machine availability through Bonjour.

__Table 1-1__ Property codes to advertise Time Machine availability

| Property code | Associated text |
| --- | --- |
| `adVN` | UTF-8 name for the volume. This is also the share name used for mounting the volume. |
| `adVF` | `AirDiskVolumeFlags` as a hex value string. |

Set the `AirDiskVolumeFlags` subvalue to 0x82 to indicate that Time Machine is supported on this SMB volume.

__Table 1-2__ AirDiskVolumeFlags for Time Machine support

| adVF value | Meaning |
| --- | --- |
| 0x0002 | SMB is supported on this volume. |
| 0x0080 | Time Machine should allow this SMB volume as a backup destination. |

The following is an example of a `TXT` record for a volume called Backups: `dk0=adVN=Backups,adVF=0x82`

### Validating the Time Machine Backup Destination

When a Time Machine client is configured to use an SMB share as a backup destination, it performs the following sequence of operations to ensure that the user has the appropriate access permissions to the share point as well as to ensure that the server has the necessary protocol support for Time Machine to function correctly.

1. An `SMB2 CREATE` request with an `“AAPL” Create Context` extension for the root of the share point is sent to validate that the `F_FULLFSYNC` extension is supported.
2. An `SMB2 CREATE` request for a file named `.com.apple.timemachine.supported` is attempted on the root of the selected share. This operation has the Create Contexts for `SMB2_CREATE_DURABLE_HANDLE_REQUEST_V2` and `SMB2_CREATE_REQUEST_LEASE_V2` to verify that the server supports these protocol features. This operation also verifies that the server supports SMB protocol version 3.x.
3. In the `SMB2_CREATE_DURABLE_HANDLE_REQUEST_V2` request, the `Timeout` field is set to 0 to enable discovery of the server’s default durable handle timeout in the response.
4. An `SMB2 CLOSE` request is sent to close the file.
5. An SMB2 compound request of `CREATE/SET_INFO/CLOSE` is sent to delete the file.
6. The client repeats steps 1-4 with a `Timeout` value of 30 seconds, and compares this value against the server’s response. If the values do not match, the client uses a series of timeout values ranging from 30-180 seconds to try to discover a value that is acceptable to the server, and validates that the server responded with the correct timeout.

### Supporting the F_FULLFSYNC Extension

The `F_FULLFSYNC` command is similar to a standard `SMB2 FLUSH` command, but ensures that all data is flushed to stable storage (which usually involves flushing the physical disk’s track cache) so that the data is not lost in the event of a power failure. This command is issued by the Time Machine client at periodic checkpoints to ensure that data corruption does not occur in the backup.

When the client needs to flush a file to stable storage, it issues an `SMB2 FLUSH` request with the `Reserved1` (16-bit) field set to `0xFFFF`. In response, the server must first process the `SMB2 FLUSH` command in the usual manner, and then must flush the data to stable storage (that is, flush the physical disk’s track cache) before responding to the client.

The server advertises this capability to the client by implementing the `“AAPL” Create Context` extension. The `“AAPL” Create Context` exchange is done early in the file system mount process, initiated by the client sending an `SMB2 CREATE` request containing an `“AAPL” Create Context` extension.

### Example Client Request

The following example shows an `SMB2 CREATE` request containing an `"AAPL" Create Context` extension, sent by the client to query server capabilities. The `CommandCode` value in this example is `kAAPL_SERVER_QUERY`.

```
---- SMB2 CREATE Request ---
StructureSize:           0x0039
SecurityFlags:           0x00
RequestedOplockLevel:    0x00
ImpersonationLevel:      0x00000002
CreateFlags:             0x0000000000000000
Reserved:                0x0000000000000000
DesiredAccess:           0x00100080
FileAttributes:          0x00000010
ShareAccess:             0x00000007
CreateDisposition:       0x00000001
CreateOptions            0x00000001
NameOffset:              0x00078
NameLength:              0x0000    // No filename provided
CreateContextsOffset:    0x00000080
CreateContextsLength:    0x00000030
--- AAPL Create Context (request) ---
Next:                    0x00000030
NameOffset:              0x0010
NameLength:              0x0004
Reserved:                0x0000
DataOffset:              0x0018
DataLength:              0x00000018
Name:                    0x4141504c  // "AAPL"
Padding:                 0x00000000  // pad to 8-byte boundary
CommandCode:             0x00000001  // 1 = kAAPL_SERVER_QUERY
Reserved:                0x00000000
RequestBitmap:           0x0000000000000007 // defined below
ClientCapabilities:      0x000000000000000f // defined below
```

The `AAPL Create Context` fields in a client request are defined in [Table 1-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnknltg).

__Table 1-3__ Client Request AAPL Create Context fields

| AAPL Create Context field | Meaning |
| --- | --- |
| `CommandCode` | This 32-bit field specifies the type of information the client is requesting. Possible values are:   - `kAAPL_SERVER_QUERY`  The client is requesting server information specified in the RequestBitmap field. - Other `CommandCode` values  These values are not required for support of the `F_FULLFSYNC` extension. |
| `RequestBitmap` | This 64-bit field allows the client to specify the type of information being requested. This field is present only in `kAAPL_SERVER_QUERY` requests. Possible values are:   - `kAAPL_SERVER_CAPS = 0x0000000000000001`  The client is requesting a bitmap of server capabilities. It is not necessary to respond with server capabilities to support the `F_FULLFSYNC` extension. - `kAAPL_VOLUME_CAPS = 0x0000000000000002`  The client is requesting a bitmap of the capabilities of the volume on which the share point is located (described in the `VolumeCapabilities` row of [Table 1-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnknlti)). - `kAAPL_MODEL_INFO = 0x0000000000000004`  This value is used to identify the specific Mac model. For non-Mac systems, there is no model information defined. The server should _not_ set the `kAAPL_MODEL_INFO` bit in the reply. |

### Example Server Response

```
---- SMB2 CREATE Response ----
StructureSize:           0x0059
OplockLevel:             0x00
Flags:                   0x00
CreateAction:            0x0000000000000001
CreateTime:              <64-bit timestamp>
LastAccessTime:          <64-bit timestamp>
LastWriteTime:           <64-bit timestamp>
ChangeTime:              <64-bit timestamp>
Allocation Size:         0x0000000000000000
End of File:             0x0000000000000000
FileAttributes:          0x00000010
Reserved:                0x00000000
File Id:                 <128-bit file id>
CreateContextsOffset:    0x00000098
CreateContextsLength:    0x00000080
--- AAPL Create Context (response) ---
Next:                    0x00000038
NameOffset:              0x0010
NameLength:              0x0004
Reserved:                0x0000
DataOffset:              0x0018
DataLength:              0x00000020
Name:                    0x4141504c  // "AAPL"
Pad1:                    0x00000000  // pad to 8-byte boundary
CommandCode:             0x00000001  // 1 = kAAPL_SERVER_QUERY
Reserved:                0x00000000
ReplyBitmap:             0x0000000000000003 // kAAPL_SERVER_CAPS | kAAPL_VOLUME_CAPS
ServerCapabilities:      0x0000000000000000 // No OS X specific capabilities reported by this server
VolumeCapabilities:      0x0000000000000004 // defined below
```

The `AAPL Create Context` fields in a server response are defined in [Table 1-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tiojwfvbuqmjnknlti).

__Table 1-4__ Server Response AAPL Create Context fields

| AAPL Create Context field | Meaning |
| --- | --- |
| `CommandCode` | The code that is defined in the client request. |
| `ReplyBitmap` | The bits are defined in the client request. Set the bits corresponding to the information being returned to the client. The server should _not_ include information that is not requested by the client. |
| `ServerCapabilities` | It is not necessary to implement this 64-bit field to support the `F_FULLFSYNC` extension. If the client requests it, respond with a `0` in this field. If the client does not request it, omit this field in the response. |
| `VolumeCapabilities` | This 64-bit field indicates the capabilities of the volume backing the share. Only one bit is required for support of the `F_FULLFSYNC` extension:  `kAAPL_SUPPORTS_FULL_SYNC = 0x0000000000000004`  When set, this value indicates that the volume supports `SMB2 FLUSH` with `F_FULLFSYNC`. |
