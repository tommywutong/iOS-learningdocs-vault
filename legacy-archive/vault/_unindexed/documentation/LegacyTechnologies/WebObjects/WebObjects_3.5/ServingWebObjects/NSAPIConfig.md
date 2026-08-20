---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/NSAPIConfig.html
archived_at: '2026-07-15T07:56:03.235964Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](ListenQueue.md)

## Installing and Configuring NSAPI Adaptors

If you have a Netscape server, use one of the NSAPI adaptors. Which NSAPI adaptor to use, and the procedure for configuring it, depends on the type of server you have. Adaptors are located in __NextLibrary/WOAdaptors/NSAPI__.

| __ If you have server...__ | __ use adaptor...__ |
|  Netscape 2.0   (FastTrack/Enterprise) |  2.0/WebObjects-NSAPI.[dll|so] |
|  Netscape 2.0.1   (FastTrack/Enterprise) |  2.0.1/WebObjects-NSAPI.[dll|so] |
|  Netscape 3.0   (FastTrack/Enterprise) |  3.0/WebObjects-NSAPI.[dll|so] |

```
```


__Note:__  There is no requirement for installing an adaptor anywhere other than its original location. If you wish, you can copy the adaptor to the server's executable or configuration directories, but ensure that the configuration specifications refer to its proper location. The following procedures assume the original installed locations.
To configure Netscape 2.0, 2.0.1, or 3.0NSAPI adaptors for all platforms, complete the following procedure:

- Locate the server configuration file in the directory _cgi-bin___/config/obj.conf__ where _cgi-bin_ is the server's cgi-bin directory.
- Edit the configuration file to insert one an line similar to one of the following:

In the __obj.conf__ file insert the following:

`Init fn=load-modules shlib=c:/NeXT/NextLibrary/WOAdaptors/NSAPI/2.0/WebObjects-NSAPI.dll funcs="WONetscapeInterface,WONSInterfaceFindWebObjects"`

This example is specific to Windows NT and NSAPI 2.0; for Solaris and HPUX the name of the adaptor executable is __WebObjects-NSAPI.so__.

- Locate the following line in __obj.conf__:

`NameTrans from="/cgi-bin" fn="pfx2dir" dir=`__"___cgi_bin_dir_" `name="cgi"`

Just before this line, insert the following line:

`NameTrans from="/cgi-bin/WebObjects" fn="WONSInterfaceFindWebObjects" name="webobjects"`

- At the end of __obj.conf__, add the following text, just as it appears here:

`<Object name="webobjects">
Service fn="WONetscapeInterface"
</Object>`

- Restart your server.

### Notes

On Windows NT, you can restart your server from the Services control panel by stopping and then starting it (clicking the Stop button, then clicking the Start button). However, it is better to use the browser interface provided for administration to restart the server. If there are errors, you can check the error activity log to find out what they are.
When you test an API-based adaptor to verify that it's properly configured, you should eliminate the CGI adaptor as a factor. To do this, rename __WebObjects__ (or __WebObjects.exe__) to something like "WebObjects_test" (or "WebObjects_test.exe") and test the API-based adaptor. If you wish later to restore the CGI adaptor, simply undo the changes you made previously.

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](ISAPIConfig.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
