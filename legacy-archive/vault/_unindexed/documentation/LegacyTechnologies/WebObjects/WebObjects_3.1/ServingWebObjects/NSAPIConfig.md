---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/NSAPIConfig.html
archived_at: '2026-07-15T07:50:00.886476Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](LoadBalancing.md)

# Installing and Configuring NSAPI Adaptors

If you have a Netscape server, the NSAPI adaptor to use, and the procedure for configuring it, depends on the type of server. Adaptors are located in __NextLibrary/WOAdaptors/NSAPI__.

| If you have server... | use adaptor... |
| --- | --- |
| Netscape 1.1 (Communication/Commerce) | 1.1/WebObjects-NSAPI.dll or 1.1/WebObjects-NSAPI.so |
| Netscape 2.0 (FastTrack/Enterprise) | 2.0/WebObjects-NSAPI.dll or 2.0/WebObjects-NSAPI.so |
| Netscape 2.0.1 (FastTrack/Enterprise) | 2.0.1/WebObjects-NSAPI.dll or 2.0.1/WebObjects-NSAPI.so |

__Note__: There is no requirement for installing an adaptor anywhere other than its original location. If you wish, you can copy the adaptor to the server's executable or configuration directories, but ensure that the configuration specifications refer to its proper location. The following procedures assume the original installed locations. NSAPI configuration is applicable only to the WebObjects Enterprise product.

## __Configuring the 1.1 NSAPI Adaptor on Windows NT__

To configure the NSAPI adaptor for Netscape 1.1 servers on Windows NT, you must make a series of key-value entries in the NT registry. These instructions assume some familiarity with the registry editor. If you aren't sure how to use this program, refer to the appropriate documentation.

1. Run the registry editor REGEDT32.EXE. This executable is located in the system folder _D_:\WINNT\SYSTEM32 where _D_ is the drive letter.
2. Expand the registry folders in this order:

   ```
       HKEY_LOCAL_MACHINE\Software\Netscape\Http[d|s]-port\CurrentVersion
   ```

   The interior folder name represented by "Http[d|s]" is __Https__ if the server performs authentication and __Httpd__ if it doesn't; _port_ is either a port number or the server host name, depending on the server.
3. Select the Startup folder and create a key called "InitFunction11". Then create a series of named string values for this key:

| Name | Value |
| --- | --- |
| fn | load-modules |
| shlib | C:\NeXT\NextLibrary\WOAdaptors\NSAPI\1.1\WebObjects-NSAPI.dll |
| funcs | WONetscapeInterface,WONSInterfaceFindWebObjects |

   The value for "shlib" in the example takes _NEXT_ROOT_ to be __C:\NeXT__. Your _NEXT_ROOT_ might be different.
4. From the CurrentVersion folder, navigate to Objects\Object1. Check the Directive_n_ folders under this key until you find one with a value of "NameTrans" (_n_ indicates a number)
5. Create a key under the "NameTrans" Directive_n_ key called "Function09" (the "09" causes this key to precede the Function_n_ key for cgi-bin). Then create a series of named string values for this key:

| Name | Value |
| --- | --- |
| fn | WONSInterfaceFindWebObjects |
| from | /cgi-bin/WebObjects (assuming "cgi-bin" is the name given to the CGI executable directory) |
| name | webobjects |
6. From CurrentVersion, go to Objects and create a key named "Object12" (the "12" makes this the last Object key). Create the following named string value for this key:

| Name | Value |
| --- | --- |
| name | webobjects |
7. Add the key "Directive10" to Object12. For this key, create the following named string value:

| Name | Value |
| --- | --- |
| DirectiveName | Service |
8. Add the key "Function10" to the newly created Directive10 key. For this function key, create the following named string value:

| Name | Value |
| --- | --- |
| fn | WONetscapeInterface |
9. To have the changes take effect, restart the server from the Services control panel.

## __Other Adaptor Configurations__

To configure Netscape 1.1 NSAPI adaptors for the Solaris and HPUX platforms, and to configure Netscape 2.0 or 2.0.1 NSAPI adaptors for all platforms, complete the following procedure:

1. Locate the appropriate server configuration files for the platform:

| Server | Platform | Configuration Files to Modify |
| --- | --- | --- |
| 1.1 | Solaris | _cgi_bin_dir_\config\magnus.conf  _cgi_bin_dir_\config\obj.conf |
| 1.1 | HPUX | _cgi_bin_dir_\config\magnus.conf  _cgi_bin_dir_\config\obj.conf |
| 2.0/2.0.1 | all platforms | _cgi_bin_dir_\config\obj.conf |
2. Edit the configuration file to insert one an line similar to one of the following:

   ___2.0 and 2.0.1 Servers___:In the __obj.conf__ file insert the following:

   ```
       Init fn=load-modules shlib=c:/NeXT/NextLibrary/WOAdaptors/NSAPI/2.0/WebObjects-NSAPI.dll
       funcs="WONetscapeInterface,WONSInterfaceFindWebObjects"
   ```

   This example is specific to Windows NT and NSAPI 2.0; for Solaris and HPUX the name of the adaptor binary is __WebObjects-NSAPI.so__.

   ___1.1 Servers (HPUX/Solaris)___: In the __magnus.conf__ file insert the following:

   ```
       Init fn=load-modules shlib=c:/NeXT/NextLibrary/WOAdaptors/NSAPI/1.1/WebObjects-NSAPI.so
       funcs="WONetscapeInterface,WONSInterfaceFindWebObjects"
   ```
3. Locate the following line in __obj.conf__:

   ```
       NameTrans from="/cgi-bin" fn="pfx2dir" dir="cgi_bin_dir" name="cgi"
   ```

   Just before this line, insert the following line:

   ```
       NameTrans from="/cgi-bin/WebObjects" fn="WONSInterfaceFindWebObjects" name="webobjects"
   ```
4. At the end of __obj.conf__, add the following text, just as it appears here:

   ```
       <Object name="webobjects">
       Service fn="WONetscapeInterface"
       </Object>
   ```
5. Restart your server.

## __Notes__

On Windows NT, you can restart your server from the Services control panel by stopping and then starting it (clicking the Stop button, then clicking the Start button). However, it is better to use the browser interface provided for administration to restart the server. If there are errors, you can check the error activity log to find out what they are.

When you test an API-based adaptor to verify that it's properly configured, you should eliminate the CGI adaptor as a factor. To do this, rename __WebObjects__ (or __WebObjects.exe__) to something like "WebObjects_test" (or "WebObjects_test.exe") and test the API-based adaptor. If you wish later to restore the CGI adaptor, simply undo the changes you made previously.

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](ISAPIConfig.md)
