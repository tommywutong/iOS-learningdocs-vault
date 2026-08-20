---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.7.html
archived_at: '2026-07-15T08:09:46.916624Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Obtain%20and%20Install%20Database%20Client%20Libraries.md) [!](Obtain%20and%20Install%20Database%20Client%20Libraries.md) [!](Informix.md)

---

#  Oracle

Phone: (800) 542-1170 or call your local sales representative

Ask for: Oracle 8 Client

The Oracle adaptor on NT requires the Oracle 8i, 8.0, 7.3, or 7.2 Client Library. It won't work with the 7.1 libraries.

On Windows NT, using the latest release of the Oracle client library requires you to use SQL\*Net v2, which requires a
tnsnames.ora
file.
tnsnames.ora
is a file that you put on client machines, generally in the directory
c:\Oracle\Net80\Admin\
. The file contains information needed to connect to a server over the network. Entries in tnsnames.ora are keyed off of a server ID alias, and they include information such as the server ID, the host machine name, and the network protocol used by the client library to resolve the server ID alias. An entry in
tnsnames.ora
might resemble the following:

myServerAlias = (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)

(HOST=myMachine) (PORT=1521))(CONNECT_DATA=(SID=eof)))

Oracle provides tools you can use to create
tnsnames.ora
files. Refer to your Oracle documentation for more information on
tnsnames.ora
files and the tools you can use to create them.

If you're using the 7.2 version of the Oracle client libraries on Windows NT, you can use either SQL\*Net v1 or SQL\*Net v2. To use SQL\*Net v1, you should set your adaptor's connectionDictionary serverId entry to

"T:<host-machine>:<server-name>".

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Obtain%20and%20Install%20Database%20Client%20Libraries.md) [!](Obtain%20and%20Install%20Database%20Client%20Libraries.md) [!](Informix.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
