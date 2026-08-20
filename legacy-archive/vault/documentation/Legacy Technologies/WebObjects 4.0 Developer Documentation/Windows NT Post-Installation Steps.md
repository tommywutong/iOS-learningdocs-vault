---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.2.html
archived_at: '2026-07-15T08:00:19.317313Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Post-Install Guide](About%20This%20Document.md)

[!Table of Contents](About%20This%20Document.md)

#   Windows NT Post-Installation Steps

After you've finished installing on Windows NT, you may want to perform one or more of the following steps:

- 

  [Install Yellow Box Services](#apple-gm4tqnrv)
- 

  [Install Monitor as a Service](#apple-gm3dsnjr)
- 

  [Microsoft IIS or PWS Post-Installation Steps](#apple-ge4tknjx)
- 

  [Obtain and Install Database Client Libraries](#apple-gm4tenzz)

##   Install Yellow Box Services

The Install Shield wizard installs __machd__
and __nmserver__
and properly configures them as services unless you've changed your _NEXT_ROOT_ environment variable to the root directory (which you must do if you're using a Microsoft server). These two services are required to run WebObjects Builder, Project Builder, and EOModeler.

To install these processes as services, open a Bourne shell window and enter the following commands:

> ```
> > cd $NEXT_ROOT/Library/System
> ```

> ```
> > ./machd.exe -install
> ```

> ```
> > ./nmserver.exe -install
> ```

##   Install Monitor as a Service

Monitor and MonitorProxy can be installed as services on Windows NT systems. To install Monitor as a service, open a Bourne shell window and enter the following commands:

> ```
> > cd $NEXT_ROOT/Library/WebObjects/Applications/Monitor.woa
> ```

> ```
> > ./MonitorDaemon.exe -InstallMonitor
> ```

To install MonitorProxy, use:

> ```
> > cd $NEXT_ROOT/Library/WebObjects/Applications/Monitor.woa
> ```

> ```
> > ./MonitorDaemon.exe -InstallMonitorProxy
> ```

To reverse these operations, "uninstalling" them as services, use:

> ```
> > cd $NEXT_ROOT/Library/WebObjects/Applications/Monitor.woa
> ```

> ```
> > ./MonitorDaemon.exe -UninstallMonitor
> ```

Or:

> ```
> > cd $NEXT_ROOT/Library/WebObjects/Applications/Monitor.woa
> ```

> ```
> > ./MonitorDaemon.exe -UninstallMonitorProxy
> ```

##   Microsoft IIS or PWS Post-Installation Steps

If you're using Microsoft IIS or PWS as your HTTP server, perform the following additional post-installation steps:

###  Grant Administrator Privileges to the CGI User

- 

  The CGI user must have Administrator privileges to access the NEXT_ROOT environment variable. This is necessary if you want to enable _load balancing_ (distributing the processing load among multiple instances of a WebObjects application). Load balancing is a performance feature that you'd use on a deployment site.

To grant Administrator privileges to the CGI user, do the following:

1. 

   Open the "User Manager for Domains" application under Administrative Tools.
2. 

   Double-click the entry with the full name "Internet Guest Account." (The user name usually starts with "IUSR_".)
3. 

   In the window that opens, click the Groups button.

You'll see two tables, one called "Member of" and one called "Not member of."

4. 

   Move the Administrators group from the "Not member of" table to the "Member of" table.
5. 

   Click the OK button.

##   Obtain and Install Database Client Libraries

To use Enterprise Objects Framework on Windows NT, you must have the appropriate database client libraries. The Sybase client libraries are provided on the WebObjects Developer 4.0 CD as an optional package. To install the Sybase client libraries, you must do a custom installation and explicitly specify that you want to install the package. To use Enterprise Objects Framework with Oracle or Informix, you must purchase the appropriate client libraries from your database vendor.

### Oracle

Phone: (800) 542-1170 or call your local sales representative

Ask for: Oracle 8 Client

The Oracle adaptor on NT requires the Oracle 8.0, 7.3, or 7.2 Client Library. It won't work with the 7.1 libraries.

On Windows NT, using the latest release of the Oracle client library (8.0) requires you to use SQL\*Net v2, which requires a __tnsnames.ora__ file. __tnsnames.ora__ is a file that you put on client machines, generally in the directory Orant/Network/Admin. The file contains information needed to connect to a server over the network. Entries in __tnsnames.ora__ are keyed off of a server ID alias, and they include information such as the server ID, the host machine name, and the network protocol used by the client library to resolve the server ID alias. An entry in __tnsnames.ora__ might resemble the following:

> ```
> myServerAlias = (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)
> (HOST=myMachine) (PORT=1521))(CONNECT_DATA=(SID=eof)))
> ```

Oracle provides tools you can use to create __tnsnames.ora__ files. Refer to your Oracle documentation for more information on __tnsnames.ora__ files and the tools you can use to create them.

If you're using the 7.2 version of the Oracle client libraries on Windows NT, you can use either SQL\*Net v1 or SQL\*Net v2. To use SQL\*Net v1, you should set your adaptor's connectionDictionary __serverId__ entry to

> ```
> T:<host-machine>:<server-name>
> ```

### Informix

Phone: (800) 331-1763 or call your local sales representative

Ask for: ESQL/C version 7.23.TC9 for Win32

If you get the error "INFORMIXSERVER not in sqlhosts file (25596)" but can connect to your database server using the Informix
__ilogin__ program, you may need to run SetNet32 to update the environment variables used by Informix.

The Informix client libraries appear to have redundant sources of server information. They use the
__sqlhosts__ file (__$INFORMIXDIR/etc/sqlhosts__) as well as a collection of environment variables managed by the Setnet32 program.

See your Informix documentation for more information on the __sqlhosts__ file and the Setnet32 program.

### Sybase

Phone: (800) 685-8225 or call your local sales representative

Ask for: OpenClient/C Version 11.1

[!Table of Contents](About%20This%20Document.md) [!Next Section](Solaris%20Post-Installation%20Steps.md)
