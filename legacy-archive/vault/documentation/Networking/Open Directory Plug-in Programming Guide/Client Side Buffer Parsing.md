---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/ClientSideBufferParsing/ClientSideBufferParsing.html
archived_at: '2026-07-27T06:57:05.841100Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Configuring%20an%20Open%20Directory%20Plug-in.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Client Side Buffer Parsing

Open Directory provides standard data buffer parsing for a `tDataBuffer` returned by the plug-in serviced functions `dsGetRecordList`, `dsDoAttributeValueSearch`, and `dsDoAttributeValueSearchWithData` if and only if the buffer was built using the standard format, known as Client Side Buffer Parsing (CSBP) described in this section.

CSBP reduces round trip Mach and TCP message traffic between the client and the server that would otherwise require the passing of the entire `tDataBuffer`. Thus, CSBP leads to a considerable performance improvement in servicing calls to `dsGetRecordEntry`, `dsGetAttributeEntry`, and `dsGetAttributeValue`, which have to extract particular data points such as attribute values out of a `tDataBuffer`.

__Note:__ At this time, CSBP is not used on a `tDataBuffer` created by `dsGetDirNodeInfo` even though the `dsGetAttributeEntry` and `dsGetAttributeValue` functions are used to extract data from the buffer.

There are two CSBP standards: StdA and StdB. StdB was the first format and it is still supported. StdA allows for larger attributes and is the recommended format.

Table 12-1 lists the order of the overall data block holding _x_ number of records.

__Table 12-1__  Format of a StdA and StdB data block

| Number of Bytes | Description |
| 4 | ulong:: tag describing the data block; value is `STDA` or `STDB` |
| 4 | ulong:: count of records contained in this data block |
| 4 | ulong:: offset in bytes to the start of the first record block |
| 4 | ulong:: offset in bytes to the start of the second record block |
| ... |  |
| 4 | ulong:: offset in bytes to the start of the last record block |
| 4 | ulong:: tag describing end of offsets; value is `ENDT` |
| ... | empty space until the start of the last record block; that is, record blocks are packed into the buffer starting at the end of the data block |
| 4 | ulong:: length in bytes of last record block |
| # | last record block |
| ... |  |
| 4 | ulong:: length in bytes of first record block |
| # | first record block |

Table 12-2 lists the order of a StdA single record block holding _y_ complete attribute blocks.

__Table 12-2__  Format of a StdA single record block

| Number of Bytes | Description |
| 2 | ushort:: length of record type string |
| n | UTF-8[n]:: record type string |
| 2 | ushort:: length of record name string |
| m | UTF-8[m]:: record name string |
| 2 | ushort:: number of attributes in this record block |
| 4 | ulong:: length in bytes of first attribute block |
| # | first attribute block for this record block |
| .... |  |
| 4 | ulong:: length in bytes of last attribute block |
| # | last attribute block for this record block |

Table 12-3 lists the order of a StdA single attribute block holding _z_ values (that is, all of the attribute’s values).

__Table 12-3__  Format of a StdA single attribute block

| Number of Bytes | Description |
| 2 | ushort:: length of attribute name |
| r | UTF-8[r]:: attribute name string |
| 2 | ushort:: number of attribute values in this attribute block |
| 4 | ulong:: length of first attribute value |
| s | byte[s]:: first attribute value for this attribute type |
| .... |  |
| 4 | ulong:: length of last attribute value |
| t | byte[t]:: last attribute value for this attribute type |

Table 12-4 lists the order of a StdB single record block holding _y_ complete attribute blocks.

__Table 12-4__  Format of a StdB single record block

| Number of Bytes | Description |
| 2 | ushort:: length of record type string |
| n | UTF-8[n]:: record type string |
| 2 | ushort:: length of record name string |
| m | UTF-8[m]:: record name string |
| 2 | ushort:: number of attributes in this record block |
| 2 | ushort:: length in bytes of first attribute block |
| # | first attribute block for this record block |
| .... |  |
| 2 | ushort:: length in bytes of last attribute block |
| # | last attribute block for this record block |

Table 12-5 lists the order of a StdB single attribute block holding _z_ values (that is, all of the attribute’s values).

__Table 12-5__  Format of a StdB single attribute block

| Number of Bytes | Description |
| 2 | ushort:: length of attribute name |
| r | UTF-8[r]:: attribute name string |
| 2 | ushort:: number of attribute values in this attribute block |
| 2 | ushort:: length of first attribute value |
| s | byte[s]:: first attribute value for this attribute type |
| .... |  |
| 2 | ushort:: length of last attribute value |
| t | byte[t]:: last attribute value for this attribute type |

[Next](Document%20Revision%20History.md)[Previous](Configuring%20an%20Open%20Directory%20Plug-in.md)
