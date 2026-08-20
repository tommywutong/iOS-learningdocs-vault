---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.07.html
archived_at: '2026-07-15T07:59:03.628957Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.06.md)

# File Location Changes

WebObjects 4.0 is the first release of WebObjects that runs on Mac OS X Server and Yellow Box for Windows NT instead of OpenStep 4.2. Because of this change, the locations of WebObjects files have changed.
On Mac OS X Server, most WebObjects files are installed in the __System__ folder (some can be found in __/Local__). On Windows NT, you still choose a folder in which to install the software, and the __NEXT_ROOT__ environment variable points to that folder. The default has changed to __C:\Apple__.
The following table lists new directory names relative to the __System__ folder or __NEXT_ROOT__ and what each directory contains.

|  Location |  Contains |
|  Developer/Applications |  Developer applications such as Interface Builder, EOModeler, Project Builder, and WebObjects Builder |
|  Developer/Examples/EnterpriseObjects |  EOModels and database installation scripts needed to run the WebObjects examples |
|  Developer/Examples/WebObjects |  WebObjects examples |
|  Developer/Examples/WebObjects/Java/ConversionScripts |  Conversion scripts for Java APIs |
|  Documentation/Developer |  Developer documentation for Mac OS X Server, Yellow Box, Enterprise Objects Framework, and WebObjects. |
|  Library/Frameworks |  Public frameworks such as WebObjects.framework, EOAccess.framework, and so on |
|  Library/Executables (Windows NT systems only) |  Framework DLLs |
|  Library/Java |  Java packages for Yellow Box, WebObjects, and Enterprise Objects Framework |
|  Library/WebObjects/Adaptors |  Executables for the various WebObjects adaptors |
|  Library/WebObjects/Applications |  The Monitor application and PlaybackManager |
|  Library/WebObjects/Configuration |  Configuration files |
|  Library/WebObjects/Executables |  WODefaultApp and WOPlayBack |

```
```


The following are new directories and files installed under the __Local__ directory. On Mac OS X Server, the __Local__ directory is at the root level. On Windows NT, it is under __NEXT_ROOT__.

|  Location |  Contains |
|  Local/Library/Frameworks |  Location where you install custom frameworks |
|  Local/Library/WebObjects/Applications |  Location where you install WebObjects applications (.__woa__ directories) |
|  Local/Library/Webserver/CGI-Executables |  The cgi-bin directory for the Apache web server (Mac OS X Server systems only). The WebObjects executable is installed here.  On Windows NT, you specify your web server's cgi-bin directory at install time. |
|  Local/Library/Webserver/Documents |  The document root for the Apache web server (Mac OS X Server systems only)  On Windows NT, you specify your web server's document root directory at install time. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](Running%20an%20Application%20on%20WebObjects%204.0.md)
