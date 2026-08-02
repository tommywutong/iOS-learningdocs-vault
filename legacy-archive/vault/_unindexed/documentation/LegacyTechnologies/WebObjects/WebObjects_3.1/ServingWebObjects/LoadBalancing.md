---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/LoadBalancing.html
archived_at: '2026-07-15T07:49:57.513765Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](Logging.md)

# Load Balancing

When you deploy a WebObjects application, you will probably want to improve performance by distributing the processing load among multiple instances of the application. This application processes can be running on the same machine as the server or on remote machines. The task that accomplishes this distribution is called load balancing.

You perform load balancing by creating a public configuration file named __WebObjects.conf__ and manually starting an application for each instance described in the file. When the adaptor receives an HTTP request for an application, it first (in its initial mode) checks __WebObjects.conf__ for an application instance that is accepting connections and forwards the request to it. The public configuration file can contain entries for instances of multiple applications and multiple instances of the same application running on different machines. The section "[HTTP Adaptors](HTTPAdaptors.md#apple-kjcummjtgyytm)" describes in some detail both the [public configuration file](ConfigFiles.md#apple-kjcummrwgq4dc) and the [adaptor modes](AdaptorModes.md#apple-kjcumnrxhe2ta) involved in load balancing.

__Note__: Load balancing is possible only with the WebObjects Enterprise product. The feature is not supported in the WebObjects Pro product.

## __Making the Public Configuration File__

The following steps describe the composition of a typical public configuration file using some WebObjects applications found in _DOCUMENT_ROOT___/WebObjects/Examples__.

1. Using a text editor (such as the TextEdit application), create an ASCII file named __WebObjects.conf__.
2. Insert the lines of configuration information in __WebObjects.conf__ needed by the adaptor to interact with application instances. Each line must conform to this format:

   _ApplicationDirectory___:__InstanceNumber__@__HostName _PortNumber_

   For example, say you want one instance of the HelloWorld application to run on host toga.acme.com. You might make this entry:

   ```
       Examples/HelloWorld:1@toga.acme.com 3001
   ```

   There are several things to note about the parts of a __WebObjects.conf__ entry:

   - _ApplicationDirectory_ is relative to _DOCUMENT_ROOT___/WebObjects__. This path must map to the URL used to access the application.
   - _InstanceNumber_ must be a unique positive integer per application per host. (However, for ease of identification, you could assign each instance a unique number regardless of host.)
   - _PortNumber_ must be a unique number over 1024 per host (numbers from zero to 1024 are reserved).

   You cannot omit any part of an entry.

   Of course, to be useful, the public configuration file should describe multiple instances of the same application and perhaps other applications as well. The following example shows load balancing among two hosts (togo.acme.com and tutu.acme.com) and two applications (HelloWorld and CyberWind).

   ```
       Examples/HelloWorld:1@toga.acme.com 3001
       Examples/HelloWorld:2@toga.acme.com 3002
       Examples/HelloWorld:3@toga.acme.com 3003
       Examples/HelloWorld:4@tutu.acme.com 3001
       Examples/HelloWorld:5@tutu.acme.com 3002
       Examples/CyberWind:1@toga.acme.com 4001
       Examples/CyberWind:2@tutu.acme.com 4001
   ```

   When the adaptor gets a request, it tries to resolve the request's URL against the entries in the public configuration file until it finds an application it can contact. Thus, if a user submits the following URL:

   ```
       http://toga.acme.com/cgi-bin/WebObjects/Examples/CyberWind
   ```

   and the CyberWind application instance on the server machine (toga.acme.com) is already processing a request, it will contact the application instance 2 of CyberWind on tutu.acme.com.
3. Save __WebObjects.conf__ in the location or locations appropriate to the platform and adaptors (specified directories are relative to the server root):

|  | Mach | Solaris | HPUX | Windows NT |
| --- | --- | --- | --- | --- |
| __CGI__ | cgi-bin | cgi-bin | cgi-bin | cgi-bin |
| __NSAPI__ | n/a | httpd-_port_/config or https-_port_/config | httpd-_port_/config or https-_port_/config | httpd-_port_/config or https-_port_/config |
| __NSAPI2__ | n/a | httpd-_port_/config or https-_port_/config | httpd-_port_/config or https-_port_/config | httpd-_port_/config or https-_port_/config |
| __ISAPI__ | n/a | n/a | n/a | _D_:\WINNT\ System32(_D_ = drive letter) |

   __Note:__ If you are using WebObjects Release 3.1, you can save the __WebObjects.conf__ file in the directory ___<NextRoot>_/NextLibrary/WOAdaptors/Configuration__ regardless of which adaptor you are using. WebObjects 3.1 is backwards compatible with WebObjects 3.0, so storing __WebObjects.conf__ under the server will still work.

## __Running the Applications__

You must manually start each application instance specified in __WebObjects.conf__ from a separate shell program window _on_ the host indicated by the __WebObjects.conf__ entry. For each instance, go to the appropriate machine and start a new shell (on Windows NT, use the Bourne Shell program provided in the WebObjects program group). When you give the command, make sure the command line names an adaptor class (WODefaultAdaptor is the default) and specifies port and instance-number arguments that match the entry in __WebObject.conf__. The following example---for a Netscape 1.1 server on Windows NT and using the default adaptor class---corresponds to the first entry in the example above. The command would be given from a shell on host toga.acme.com:

```
    C:\NeXT\NextLibrary\Executables\WODefaultApp -a WODefaultAdaptor -n 1 -p 3001
    -d C:/NETSCAPE/ns-home/docs Examples/HelloWorld
```

If the application directory (the last argument) is on a remote machine rather than on the same document root as the server, and you want load-balancing to be transparent, you'd specify the document root (the path after the __-d__ flag) of that remote WebObjects machine. Note that the remote document root doesn't have to mirror the document root on the server machine. The following would be an acceptable command:

```
    C:\NeXT\NextLibrary\Executables\WODefaultApp -a WODefaultAdaptor -n 1 -p 3001
    -d C:/WOApps Examples/HelloWorld
```

For this command to be valid, however, you'd have to create on the remote machine a subdirectory in __C:\WOApps__ called WebObjects and install the HelloWorld application in that subdirectory. Note that the Examples directory is unnecessary, but to get load balancing to work properly you'd have to modify the entry in __WebObjects.conf__ appropriately and move HelloWorld from the Examples directory up to _DOCUMENT_ROOT___/WebObjects__:

```
    HelloWorld:1@toga.acme.com 3001
```

See "[Manually Starting WebObjects Applications](ManualStarting.md#apple-kjcummjygi3ts)" for more about the arguments of this command.

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](NSAPIConfig.md)
