---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/PostInstall.html
archived_at: '2026-07-15T07:49:24.184493Z'
---
> 导航：[总目录](../../../../../README.md) · 未编入索引的页面


# WebObjects Release 3.1 Post-Installation Notes

---

This file contains:

- __[Using WebObjects with Your Web Server](#apple-k5humidxnf2gqicxmvrcau3foj3gk4q)__ describes the steps necessary to get WebObjects to work with your Web server.
- __[Customizing URLs](#apple-in2xg5dpnvuxu2lom5kvetdt)__ describes how you can improve the usability of the documentation on UNIX platforms. Not required for Windows NT installations.
- __[Uninstalling WebObjects for Windows NT](#apple-kvxgs3ttorqwy3bak5humicokq)__ tells you how remove WebObjects from your Windows NT machine.

---

# Using WebObjects with Your Web Server

At this point you should have installed WebObjects and rebooted your computer. The following topics tell how to get WebObjects working with your Web server.
> ## Windows NT
>
> The WebObjects installation program automatically sets up WebObjects to work with your Web server. No further steps are necessary.
>
> ## Mach
>
> The following instructions will help you make sure your Web server sees the WebObjects Adaptor and the examples.
>
> ### If you're using WebObjects with the Apache server
>
> You're done with installation. To start up the server, __su__ to root and
> give this command:
>
> ```
> /NextLibrary/WebServer/httpd -d /NextLibrary/WebServer > /dev/console
> ```
>
> ### If you're using WebObjects with any other Web server
>
> You'll need to move the contents of two directories. You may have to __su__ or log in as root before doing this.
>
> 1. Identify your Web server's _cgi-bin_ and _DocumentRoot_ directories.
>    - The _cgi-bin_ directory is commonly located as __/usr/local/etc/httpd/cgi-bin__.
>    - The _DocumentRoot_ is commonly located as __/usr/local/etc/httpd/htdocs__.
>    - If you don't know how to identify these important directories, see your system administrator.
> 2. Move files under __/NextLibrary/WebServer__ to your Web server's directories.
>    - Move the two files under __/NextLibrary/WebServer/cgi-bin__ to your Web server's _cgi-bin_ directory.
>    - Move the two directories under __/NextLibrary/WebServer/htdocs__ to your Web server's _DocumentRoot_ directory.
> 3. Make sure your Web server is running.
>
>
>
> ## Solaris and HP-UX
>
> ### If you're using WebObjects the Apache Web server
>
> To install the Apache Web server provided with the WebObjects release, follow these steps:
>
> 1. On Solaris, __cd__ to __WebServer-3.0/Solaris__ in the mount directory for the CD-ROM.
>
>    On HP-UX, __cd__ to __WebServer-3.0/HP-UX__ in the mount directory for the CD-ROM.
> 2. Start the install script with this command:
>
>    `sh WebServerInstall`
> 3. When the install script asks you to confirm that you want the Apache HTTP server software installed, type __"y"__ to proceed or __"n"__ to cancel the installation.
> 4. On HP-UX, there may be an incompatibility between the standard user and group ID numbers for nobody and those required by the Apache HTTP server. One work-around for this problem is to create a new user account to own the files on your web server. Create the user (using any name you wish) with the standard HP-UX utilities.
>
>    Then modify the __/NextLibrary/WebServer/conf/httpd.conf__ file by replacing "nobody" with the name of the new user in the following line
>
>    `User nobody`
> 5. To start the server, open a shell, __su__ to root, and give this command:
>
>    `/NextLibrary/WebServer/httpd -d /NextLibrary/WebServer > /dev/console`
>
> This completes the installation of the Apache server.
>
> ### If you're using WebObjects with any other Web server
>
> Follow these steps to move the contents of two directories. (You may need to __su__ to root before doing this.)
>
> 1. Identify your web server's _cgi-bin_ and _document root_ directories.
> 2. Move the files under __/NextLibrary/WebServer/cgi-bin__ to your web server's _cgi-bin_ directory.
> 3. Move the two directories under __/NextLibrary/WebServer/htdocs__ to your web server's _document root_ directory.

---

# Customizing URLs

In the WebObjects documentation, links from the documentation to example WebObjects applications are of the form:

```
    http://localhost/cgi-bin/WebObjects/Examples/ApplicationName

```

As long as you are accessing the documentation from the HTTP server machine (that is, __localhost__) and the HTTP server stores scripts in a directory named __cgi-bin__, these links work. If you are accessing the documentation over the network, or the HTTP server doesn't call its scripts directory "cgi-bin", the links will be broken.

We've provided a script, __curls.sh__, that modifies these URLs to use the name of the host and scripts directory specific to your installation. On Windows NT, this script runs automatically during the installation process. On UNIX platforms, you must run this script by hand. The script is in __$NEXT_ROOT/NextLibrary/Documentation/NextDev/WebObjects__.

Assuming your computer's hostname is "Mars" and its scripts directory is "Scripts", you could modify the URLs in the documentation by running these commands in a terminal window:

```
    cd $NEXT_ROOT/NextLibrary/Documentation/NextDev/WebObjects
    curls.sh -h Mars -c Scripts -F WOPages

```

(On a Mach machine, you'd __cd__ to __/NextLibrary/Documentation/NextDev/WebObjects__ before running the curls command.)

See the __curls.sh__ script itself for more information about its operation.

---

# Uninstalling WebObjects for Windows NT

OPENSTEP Enterprise includes an "uninstaller" that automatically removes
OPENSTEP Enterprise from your computer. However, this uninstaller
doesn't work on computers that have OPENSTEP for Windows 4.0 or D'OLE
(4.0 or earlier) installed. Versions 4.0 and earlier of OPENSTEP for
Windows and D'OLE must be uninstalled using the following procedure.

1. Terminate all running OPENSTEP for Windows and D'OLE programs by
   double-clicking each item in the NeXT Software program group. If
   you've double-clicked a running program, you get a dialog asking if
   you want to terminate it. If the program wasn't running, you just
   started it; double-click it again to terminate it.
2. Locate and delete the directory containing the OPENSTEP or D'OLE
   software, and all files and subdirectories contained within. If
   you're unsure which directory to delete, open the System control
   panel and look in the System Environment Variables section. The
   directory in question is identified by the __NEXT_ROOT__ environment
   variable.

   If you can't delete a file, that means it is still running. Double-click
   the file in Explorer to terminate it. Then delete the file.
3. Clean up your program groups. Use the appropriate procedure for your
   version of Windows NT:

   For Windows NT 3.51:

   - Select -- but do not open -- the NeXT Software program group icon
     in the
     Program Manager.
   - Press Delete, or choose Delete from the File menu. In the Delete
     confirmation dialog that appears, click Yes.
   - Double-click the Start-up group icon in the Program Manager.
   - If the Start-up group contains icons labeled MachD, Mach nmserver,
     WindowServer, or Pasteboard Server, select each icon and press
     Delete. In the Delete confirmation dialog that appears, click
     Yes.

   For Windows NT 4.0:

   - Click Start. Choose Settings, then Taskbar.
   - Click the Start Menu Programs tab in the Taskbar Properties
     dialog. In the Customize Start Menu section, click Remove.
   - In the Remove Shortcuts/Folders dialog, select the NeXT Software
     folder and click Remove to delete it.
   - Double-click the Start-up group folder to open it. If the Start-up
     group contains icons labeled MachD, Mach nmserver, WindowServer,
     or Pasteboard Server, select each icon and click Remove.
   - Click Close in the Remove Shortcuts/Folders dialog. Click OK in
     the Taskbar Properties dialog.
4. Clean up your system environment variables as follows:
   - If you're using Windows NT 3.51, go to the Windows NT Program
     Manager and open the Main program group. Double-click the Control
     Panel icon. If you're using Windows NT 4.0, click Start, select Settings,
     then select Control Panel.
   - Within the Control Panel window, double-click the System icon.
   - The System panel appears. On Windows NT, select the
     Environment tab. This panel is where you can alter the environment
     variable settings that Windows NT uses.
   - Select __NEXT_ROOT__ in the System Environment Variables section.
     Click Delete.
   - If developer software was installed, select the __lib__ (or Lib)
     system-environment variable definition. Highlight that portion of
     the definition that names directories removed in step 2, above,
     and press the Delete key (do not click Delete). Click Set to
     register the change.
   - Select the __Path__ system-environment variable definition. Highlight
     that portion of the definition that names directories removed in
     step 2, above, and press the Delete key (do not click Delete).
     Click Set to register the change.
   - Click OK in the System dialog.
5. Clean up the Windows NT Registry, using the appropriate procedure for
   your version of Windows NT. This step is not required.

   __Note:__ You must take great care when editing the Windows Registry;
   it's possible to alter your configuration so that your computer
   will no longer boot. If you aren't comfortable working with the
   Windows NT Registry, skip this step.

   For Windows NT 3.51:

   - Start the Windows Registry Editor. This program is named
     __REGEDIT.EXE__, and is typically found in your __WINNT35__ directory.
   - Select Find Key... from the View menu. In the Find What field,
     type __"NeXT"__.
   - Click Find Next in the Find panel to locate a key. Examine the
     key. If it appears to be one that was created for use with
     OPENSTEP or D'OLE, press the Delete key to delete it.
   - Repeat step c, above, until Find indicates that there are no keys
     that contain the string "NeXT". Close the Registry Editor.

   For Windows NT 4.0:

   - Start the Windows Registry Editor. This program is
     named __REGEDIT.EXE__, and is typically found in your __WINNT__
     directory.
   - Select Find from the Edit menu. In the Find What field, type
     __"NeXT"__. Click Find Next to locate the first key.
   - Examine the key. If it appears to be one that was created for use
     with OPENSTEP or D'OLE, press the Delete key to delete it. Press
     F3 to find the next key.
   - Repeat step c, above, until Find indicates that there are no keys
     that contain the string "NeXT". Close the Registry Editor.

Uninstallation is now complete.
