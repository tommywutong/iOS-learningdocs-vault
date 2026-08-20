---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.8.html
archived_at: '2026-07-15T08:00:24.262560Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Post-Install Guide](About%20This%20Document.md)

[!Table of Contents](About%20This%20Document.md) [!Previous Section](Verifying%20the%20Installation.md)

#   Troubleshooting

WebObjects operates on a number of hardware platforms, running various operating systems and supporting many different types of HTTP servers. Taking these variables together means that WebObjects finds itself in a large number of distinctly different environments, a situation that can lead to problems affecting the installation of WebObjects or the running of WebObjects applications.

This short guide will help you find solutions to the problems most commonly encountered. It's divided into these major sections:

- 

  [Checking the Installation](#apple-giztsmbt)

- 

  [Windows NT](#apple-g4ztamrv)
- 

  [Solaris or HP-UX](#apple-geztsobx)
- 

  [Mac OS X Server](#apple-ha4tomjw)

- 

  [Problems With Scripted Applications](Problems%20With%20Scripted%20Applications.md#apple-geztgojt)
- 

  [Problems With Compiled Applications](Problems%20With%20Compiled%20Applications.md#apple-gyydenru)

Start by reading the section for your operating system in "[Checking the Installation](#apple-giztsmbt)
." If you don't see the solution there, continue with "[Problems With Scripted Applications](Problems%20With%20Scripted%20Applications.md#apple-geztgojt)
" and then "[Problems With Compiled Applications](Problems%20With%20Compiled%20Applications.md#apple-gyydenru)
."

Remember that the WebObjects release notes, available online (on your disk and on Apple's web site), have the latest information about bugs and workarounds.

##   Checking the Installation

###   Windows NT

On Windows NT, these locations should contain the following files or directories:

- 

  In your server's _cgi-bin_ directory:

- 

  __WebObjects.exe__
  : The WebObjects adaptor
- 

  __WebObjects__
  : This file is simply a copy of the __WebObjects.exe__
  file above minus the __.exe__
  extension. Some HTTP servers disallow the extension.

- 

  Your server's _document root_ directory

- 

  __WebObjects__
  : This directory should contain __Documentation__
  and __Java__
  subdirectories, plus a Frameworks subdirectory that contains directories for WOExtensions and DirectToWeb.

- 

  _NEXT_ROOT_ directory

> 
>
> This is the location where you installed the WebObjects software. Check for these files and directories:

- 

  __Library\WebObjects\Executables__
  :
  Contains __WODefaultApp.exe__
  , the default application executable for scripted WebObjects applications
- 

  __Library\Frameworks\WebObjects.framework__
  : WebObjects library of classes, plus header files (Developer installations only)
- 

  __Library\Frameworks\WOExtensions.framework__
  : WebObjects Extensions framework, which contains extra dynamic elements and shared components
- 

  __Library\Java__
  : The Java interfaces to WebObjects classes.
- 

  __Library\WebObjects\Adaptors__
  : Contains WebObjects configuration files and adaptors.

####  Corrective actions:

If you are missing any of the files from your server's _cgi-bin_ directory, you can copy them from __Library\WebObjects\Adaptors\CGI__
to your HTTP server's _cgi-bin_ directory.

If you are missing any of the contents of your server's _document root_ directory copy them from where they were installed to the directory _<DocRoot>___\WebObjects__
. If the files were not installed, reinstall WebObjects.

If you are missing any of the contents of the __NEXT_ROOT__
directory, reinstall WebObjects.

###   Solaris or HP-UX

On Solaris and HP-UX, these locations should contain the following files or directories:

- 

  Your server's _cgi-bin_ directory.

- 

  __WebObjects__
  : The WebObjects adaptor

- 

  Your server's _document root_ directory

- 

  __WebObjects__
  : This directory should contain __Documentation__
  and __Java__
  subdirectories, plus a Frameworks subdirectory that contains directories for WOExtensions and DirectToWeb.

- 

  _NEXT_ROOT_ directory

> 
>
> This is the location where you installed the WebObjects software. Check for these files and directories:

- 

  __Library/WebObjects/Executables__
  :
  Contains __WODefaultApp__
  , the default application executable for scripted WebObjects applications
- 

  __Library/Frameworks/WebObjects.framework__
  : WebObjects library of classes, plus header files (Developer installations only)
- 

  __Library/Frameworks/WOExtensions.framework__
  : WebObjects Extensions framework, which contains extra dynamic elements and shared components
- 

  __Library/Java__
  : The Java interfaces to WebObjects classes. (Solaris only)
- 

  __Library/WebObjects/Adaptors__
  : Contains WebObjects configuration files and adaptors.

####  Corrective action:

If you are missing any of the files from your server's _cgi-bin_ directory, you can copy them from __/Library/WebObjects/Adaptors/CGI__
to your HTTP server's _cgi-bin_ directory.

If you are missing any of the contents of your server's _document root_ directory copy them from where they were installed to your server's _document root_ directory. If the files were not installed, reinstall WebObjects.

If you are missing any of the contents of the __NEXT_ROOT__
directory, reinstall WebObjects.

###   Mac OS X Server

On Mac OS X Server, these locations should contain the following files or directories:

- 

  Your Apache server's CGI_Executables directory (__/Local/Library/WebServer/CGI-Executables__
  ).

- 

  __WebObjects__
  : The WebObjects adaptor

- 

  Your server's _document root_ directory

- 

  __WebObjects__
  : This directory should contain __Documentation__
  and __Java__
  subdirectories, plus a Frameworks subdirectory that contains directories for WOExtensions and DirectToWeb.

- 

  __/System/Library__
  directory

> 
>
> Check for these files and directories:

- 

  __WebObjects/Executables__
  :
  Contains __WODefaultApp__
  , the default application executable for scripted WebObjects applications
- 

  __Frameworks/WebObjects.framework__
  : WebObjects library of classes, plus header files (Developer installations only)
- 

  __Frameworks/WOExtensions.framework__
  : WebObjects Extensions framework, which contains extra dynamic elements and shared components
- 

  __Java__
  :
  The Java interfaces to WebObjects classes.
- 

  __WebObjects/Adaptors__
  : Contains WebObjects configuration files and adaptors.

####  Corrective action:

If you are missing any of the files from your server's _cgi-bin_ directory, check to see that you have moved them from __/Local/Library/WebServer/CGI-Executables__
to your HTTP server's CGI-Executables directory.

Likewise, if you are missing any of the directories from your server's _document root_ directory, check to see that you have moved them from __/Local/Library/WebServer/Documents__
to your HTTP server's _document root_ directory.

If you are missing any of the contents of your __/System/Library__
directory, reinstall WebObjects.

## [Problems With Scripted Applications](Problems%20With%20Scripted%20Applications.md#apple-obtwmslehu4damzy)

## [Problems With Compiled Applications](Problems%20With%20Compiled%20Applications.md#apple-obtwmslehu4daobu)

[!Table of Contents](About%20This%20Document.md) [!Next Section](Problems%20With%20Scripted%20Applications.md)
