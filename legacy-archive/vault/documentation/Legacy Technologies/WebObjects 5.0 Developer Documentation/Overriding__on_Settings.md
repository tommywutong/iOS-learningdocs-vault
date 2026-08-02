---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/WebObjectsAdaptors/Overriding__on_Settings.html
archived_at: '2026-07-15T08:12:16.961436Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](The_WebObje_mation_Page.md)[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/index.html)

## Overriding Default Configuration Settings

For the most part, you shouldn't need to modify the default
values of settings in the configuration file. However, if you want
to change the way the HTTP adaptor obtains your site's state information,
for example, you'll need to perform some of the procedures explained
here.

These are the tasks explained in this section:

- ["Setting the Multicast Address and Port"](#apple-ijbegq2dizdes)
- ["Setting the Host List"](#apple-ijbegq2hirdec)
- ["Setting the HTTP Adaptor Configuration File"](#apple-ijbegq2fizdui)
- ["Setting Access to the WebObjects Adaptor Information Page"](#apple-ijbegqsfizeug)
- ["Setting an Alias for cgi-bin in the WebObjects URL"](#apple-ijbegqsiivdus)
- ["Setting the Document Root Path of the Web Server"](#apple-ijbegrsfircuq)

### Setting the Multicast Address and Port

The following list explains how to set the multicast address,
port, and configuration refresh interval (in seconds) in the supported
adaptors. The default values for each of these properties are `239.128.14.2`, `1085`,
and `10` respectively.
The adaptor uses the configuration interval to determine the amount
of time that passes between state discoveries on your site. The
host discovery process occurs 10 times less frequently than the
time indicated by the configuration refresh interval. With the configuration
refresh interval set to `10`,
the discovery process occurs every 100 seconds.

- __Apache__ Set
  the value of the `WebObjectsConfig` variable
  in the `apache.conf` file
  to the desired values, using the format shown below:

  ```
  WebObjectsConfig webobjects://<address>:<port> <configuration_interval>
  ```
- __ISAPI__ Add two keys to the Registry, `CONF_URL` and `CONF_INTERVAL`,
  choose `REG_SZ` as their
  data type, and set their values as follows:

  ```
  \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\CONF_URL  webobjects://<address>:<port>

  \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\CONF_INTERVAL  <configuration_interval>
  ```
- __NSAPI__ Add the following line to the `obj.conf` file:

  ```
  Init fn="WebObjects_init" root="/opt/ns-home/docs" config="webobjects:// <address>:<port> confinterval="<configuration_interval>"
  ```
- __CGI__ Set the `WO_CONFIG_URL` environment
  variable to `webobjects://<address>:<port>`. Make
  sure your Web server is configured to pass the variable to the adaptor
  (consult your Web server's documentation for instructions).

### Setting the Host List

The following list explains how to set a host list for a site
with two hosts, host1 and host2, in the supported adaptors with
a configuration interval of `10` (the
configuration interval cannot be set in the CGI adaptor).

- __Apache__ Set
  the `WebObjectsConfig` variable
  in the `apache.conf` file
  to the desired list of hosts. By default it's set to `http://localhost:1085
  10` (the 10 is the configuration refresh interval).
  Separate each host with a comma, as shown in the following example

  ```
  WebObjectsConfig http://host1:1085,http://host2:1085 10
  ```
- __ISAPI__ Add two keys to the Registry, `CONF_URL` and `CONF_INTERVAL`,
  choose `REG_SZ` as their
  data type, and set their values as follows

  ```
  \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\CONF_URL  http://host1:1085,http://host2:1085

  \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\CONF_INTERVAL  10
  ```
- __NSAPI__ Set the WebObjects_init function's
  arguments in the `obj.conf` file
  as follows

  ```
  Init fn="WebObjects_init" root="/opt/ns-home/docs" config="http:// host1:1085,http://host2:1085" confinterval="10"
  ```
- __CGI__ Set the `WO_CONFIG_URL` environment
  variable to `http://host1:1085,http://host:1085`.
  Make sure the Web server is configured to pass the variable to the
  adaptor (consult your Web server's documentation for instructions)

### Setting the HTTP Adaptor Configuration File

- __Apache__ Set
  the value of `WebObjectsConfig` variable
  in the `apache.conf` file
  to the path of the adaptor configuration file.

  ```
  WebObjectsConfig file://<path-to-an-xml-config-file> 10
  ```
- __ISAPI__ Add the `CONF_URL` key
  to the Registry, choose `REG_SZ` as
  its data type, and set the adaptor configuration file path as its
  value, as the following example shows:

  ```
  \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\CONF_URL  file://<path-to-an-xml-config-file>
  ```
- __NSAPI__ Set the arguments of the `WebObjects_init` function
  in the `obj.conf` file
  as follows:

  ```
  Init fn="WebObjects_init" root="/opt/ns-home/docs" config="file:// <path-to-an-xml-config-file>"
  ```
- __CGI__ Set the `WO_CONFIG_URL` environment
  variable to `file://<path-to-an-xml-config-file>`.
  Make sure the Web server is configured to pass the variable to the
  adaptor (consult your Web server's documentation for instructions).

### Setting Access to the WebObjects Adaptor Information Page

You can provide access to the WebObjects adaptor information
page to a specific user or to everyone. To provide access to a single
user, you set the values of the `username` and `password` attributes.
To provide public access, set the `username` attribute
to `public`. The following
list explains how to provide access to the information page to a
user named joe in the supported adaptors. For the changes to take
effect, you need to restart the Web server.

- __Apache__ Add
  the following lines to the apache.conf file,
  located in the /System/Library/WebObjects/Adaptor/Apache directory:

  ```
  WebObjectsAdminUsername joe
  WebObjectsAdminPassword secret
  ```
- __ISAPI__ Add two keys to the Registry, `WOUSERNAME` and `WOPASSWORD`,
  choose `REG_SZ` as their data
  type, and set their values as follows:

  ```
  \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\WOUSERNAME  joe

  \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\WOPASSWORD  secret
  ```
- __NSAPI__ Add the following line to `obj.conf`:

  ```
  Init fn="WebObjects_init" root="/opt/ns-home/docs" config="webobjects:// <address>:<port>" username="joe" password="secret"
  ```
- __CGI__ Set the `WO_ADAPTOR_INFO_USERNAME` and `WO_ADAPTOR_INFO_PASSWORD` environment variables
  to the appropriate values. Make sure the Web server is configured
  to pass the variables to the adaptor (consult your Web server's
  documentation for instructions).

### Setting an Alias for cgi-bin in the WebObjects URL

The following list explains how to change the `cgi-bin` part
of the URL used to connect to an application instance to `Store` in
the Apache, NSAPI, and CGI adaptors:

- __Apache__ In
  the `apache.conf` file,
  change the line

  ```
  WebObjectsAlias /cgi-bin/WebObjects
  ```

  to

  ```
  WebObjectsAlias /Store/WebObjects
  ```
- __NSAPI__ In the `obj.conf` file,
  change the lines

  ```
  NameTrans from="/cgi-bin/WebObjects" fn="WebObjectsNameTrans" name="webobjects"
  NameTrans from="/cgi-bin" fn="pfx2dir" dir="/opt/ns-home/cgi-bin" name="cgi"
  ```

  to

  ```
  NameTrans from="/Store/WebObjects" fn="WebObjectsNameTrans" name="webobjects"
  NameTrans from="/Store" fn="pfx2dir" dir="/opt/ns-home/cgi-bin" name="cgi"
  ```

### Setting the Document Root Path of the Web Server

- __Apache__ In
  the `apache.conf` file,
  change the line

  ```
  WebObjectsDocumentRoot /Library/WebServer/Documents
  ```

  to

  ```
  WebObjectsDocumentRoot <document-root-path>
  ```
- __ISAPI__ Add the following Registry entry:

  ```
  \\HKEY_LOCAL_MACHINE\\SOFTWARE\\Apple\\WebObjects\\Configuration\\DOCUMENT_ROOT  <document-root-path>
  ```
- __NSAPI__ In the `obj.conf` file,
  change the value of the `root` variable
  in every line that defines it to the desired path. For example,
  the line

  ```
  Init fn="WebObjects_init" root="/opt/ns-home/docs" config="http:// localhost:1085"
  ```

  needs
  to be changed to

  ```
  Init fn="WebObjects_init" root="<document-root-path>" config="http:// localhost:1085"
  ```
- __CGI__ Set the value of the `CGI_DOCUMENT_ROOT` environment
  variable to the desired path. Make sure that your Web server is
  configured to pass the variable to the adaptor (consult your Web
  server's documentation for instructions).

[!](The_WebObje_mation_Page.md)[!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/DeploymentElements/index.html)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
