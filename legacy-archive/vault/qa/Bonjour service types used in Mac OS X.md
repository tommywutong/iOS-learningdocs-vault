---
title: Bonjour service types used in Mac OS X
apple_id: DTS10002382
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/qa/qa1312/_index.html
archived_at: '2026-07-18T02:30:22.601300Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1312

# Bonjour service types used in Mac OS X

## Q:  Is there a list of Bonjour service types being used by Mac OS X?

A: Is there a list of Bonjour service types being used by Mac OS X?

The following table lists the various Bonjour service types being used in Mac OS X. Bonjour service types are based on [IANA's list of protocol names and port numbers](http://www.iana.org/assignments/port-numbers). More information about registering a Bonjour service type is available at the [DNS-SD Web Site](http://www.dns-sd.org/ServiceTypes.html). For information on the format of a Bonjour service type, please see [QA1198](https://developer.apple.com/qa/qa2001/qa1198.html).

__Table 1__  Bonjour service types.

| Protocol Name | Service Type | Notes |
| AppleTalk Filing Protocol (AFP) | _afpovertcp._tcp | Used by Personal File Sharing in the Sharing preference panel starting in Mac OS X 10.2. The Finder browses for AFP servers starting in Mac OS X 10.2. |
| Network File System (NFS) | _nfs._tcp | The Finder browses for NFS servers starting in Mac OS X 10.2. |
| WebDAV File System (WEBDAV) | _webdav._tcp | The Finder browses for WebDAV servers but because of a bug (r. 3171023), double-clicking a discovered server fails to connect. |
| File Transfer Protocol (FTP) | _ftp._tcp | Used by FTP Access in the Sharing preference panel starting in Mac OS X 10.2.2. The Finder browses for FTP servers starting in Mac OS X 10.3. The Terminal application also browses for FTP servers starting in Mac OS X 10.3. |
| Secure Shell (SSH) | _ssh._tcp | Used by Remote Login in the Sharing preference panel starting in Mac OS X 10.3. The Terminal application browses for SSH servers starting in Mac OS X 10.3. |
| Remote AppleEvents | _eppc._tcp | Used by Remote AppleEvents in the Sharing preference panel starting in Mac OS X 10.2. |
| Hypertext Transfer Protocol (HTTP) | _http._tcp | Used by Personal Web Sharing in the Sharing preference panel to advertise the User's Sites folders starting in Mac OS X 10.2.4. Safari can be used to browse for web servers. |
| Remote Login (TELNET) | _telnet._tcp | If Telnet is enabled, xinetd will advertise it via Bonjour starting in Mac OS X 10.3. The Terminal application browses for Telnet servers starting in Mac OS X 10.3. |
| Line Printer Daemon (LPD/LPR) | _printer._tcp | Print Center browses for LPR printers starting in Mac OS X 10.2. For more information on creating a Bonjour printer, please see the Bonjour Printing Specification. |
| Internet Printing Protocol (IPP) | _ipp._tcp | Print Center browses for IPP printers starting in Mac OS X 10.2. For more information on creating a Bonjour printer, please see the Bonjour Printing Specification. |
| PDL Data Stream (Port 9100) | _pdl-datastream._tcp | Print Center browses for PDL Data Stream printers starting in Mac OS X 10.2. For more information on creating a Bonjour printer, please see the Bonjour Printing Specification. |
| Remote I/O USB Printer Protocol | _riousbprint._tcp | Used by the AirPort Extreme Base Station to share USB printers. Printer Setup Utility browses for AirPort Extreme shared USB printers which use the Remote I/O USB Printer Protocol starting in Mac OS X 10.3. |
| Digital Audio Access Protocol (DAAP) | _daap._tcp | Also known as iTunes Music Sharing. iTunes advertises and browses for DAAP servers starting in iTunes 4.0. |
| Digital Photo Access Protocol (DPAP) | _dpap._tcp | Also known as iPhoto Photo Sharing. iPhoto advertises and browses for DPAP servers starting in iPhoto 4.0. |
| iChat Instant Messaging Protocol | _ichat._tcp | Used by iChat 1.0 which shipped with Mac OS X 10.2. This service is now deprecated with the introduction of the "presence" service in iChat AV. See below. |
| iChat Instant Messaging Protocol | _presence._tcp | Used by iChat AV which shipped with Mac OS X 10.3. |
| Image Capture Sharing | _ica-networking._tcp | Used by the Image Capture application to share cameras in Mac OS X 10.3. |
| AirPort Base Station | _airport._tcp | Used by the AirPort Admin Utility starting in Mac OS X 10.2 in order to locate and configure the AirPort Base Station (Dual Ethernet) and the AirPort Extreme Base Station. |
| Xserve RAID | _xserveraid._tcp | Used by the Xserve RAID Admin Utility to locate and configure Xserve RAID hardware. |
| Distributed Compiler | _distcc._tcp | Used by Xcode in its Distributed Builds feature. |
| Apple Password Server | _apple-sasl._tcp | Used by Open Directory Password Server starting in Mac OS X Server 10.3. |
| Workgroup Manager | _workstation._tcp | Open Directory advertises this service starting in Mac OS X 10.2. Workgroup Manager browses for this service starting in Mac OS X Server 10.2. |
| Server Admin | _servermgr._tcp | Mac OS X Server machines advertise this service starting in Mac OS X 10.3. Server Admin browses for this service starting in Mac OS X Server 10.3. |
| Remote Audio Output Protocol (RAOP) | _raop._tcp | Also known as AirTunes. The AirPort Express Base Station advertises this service. iTunes browses for this service starting in iTunes 4.6. |

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-06-04 | Moved to Retired Documents Library. |
| 2004-07-14 | Added servermgr and raop. |
|  | New document that provides a list of common Bonjour service types used in Mac OS X. |

