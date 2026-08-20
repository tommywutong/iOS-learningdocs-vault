---
title: Specifying Proxy Settings
apple_id: DTS10001400
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-04-24'
source_url: https://developer.apple.com/library/archive/qa/java/java25.html
archived_at: '2026-07-18T02:29:42.441456Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA25Specifying Proxy Settings |

|  |
| --- |
| ---   Q: I have a Java application that needs to use a proxy server for connections to the Internet. How do I specify these settings in my application?  A: Java networking classes use System properties to route network traffic through proxy servers. MRJ (version 2.2 or later) automatically uses the settings in the Internet Control panel to continually update the System properties. By far, the best thing to do is have the use the proxy information in the Internet Control panel.  You can set these properties using JBindery, MRJAppBuilder, or programmatically, but you run the risk that MRJ will overwrite them.  The image below illustrates how the Internet control panel settings map to those in JBindery: |

![Proxy](../What%20is%20JAR%20caching/attachments/images/java25_001.gif)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Here is a complete table of how these settings map:   |  |  |  | | --- | --- | --- | | __Internet Control Panel Setting__ | __JBindery Setting__ | __Java System Property__ | | Web Proxy (checkbox) | HTTP proxy (checkbox) | proxySet | | Web Proxy (text) | HTTP proxy (text) | proxyHost | | Web Port | HTTP Port | proxyPort | | FTP Proxy (checkbox) | FTP proxy (checkbox) | ftpProxySet | | FTP Proxy | FTP proxy | ftpProxyHost | | FTP Port | FTP Port | ftpProxyPort | |  | Firewall (checkbox) | firewallSet | |  | Firewall | firewallHost | |  | Firewall Port | firewallPort | | Bypass Proxy Servers |  | http.nonProxyHosts |   The Proxy settings in the Internet Control Panel are accessible from the Firewall page of the __Advanced__ tab. JBindery settings can be specified from the Security page.  If you wish to configure your proxy settings programmatically, you need to use Java's standard property mechanism.     |  | | --- | | ``` import java.util.*; class SystemProperties {     public static void main(String args[])     {         Properties systemproperties = System.getProperties();         systemproperties.put("firewallHost",                              "web.proxy.nl.com"); // firewall proxy server         systemproperties.put("firewallPort",                              "140");              // firewall port #         systemproperties.put("firewallSet","true");         systemproperties.put("proxyHost",                              "http.proxy.nl.com");// http proxy server         systemproperties.put("proxyPort",                              "180");              // http port #         systemproperties.put("proxySet","true");         systemproperties.put("ftpProxyHost",                              "ftp.proxy.nl.com"); // ftp proxy server         systemproperties.put("ftpProxyPort",                              "110");              // ftp port #         systemproperties.put("ftpProxySet","true");         systemproperties.put("http.nonProxyHosts",                              "apple.com|netscape.com");                                                   // proxy bypass sites         System.setProperties(systemproperties);     } } ``` |    To modify your proxy settings using MRJAppBuilder, add the settings directly in your properties file. Here's an example:   |  | | --- | | ``` proxySet = true proxyHost = http.proxy.nl.com ``` |   For more information on system properties in Java, please visit [Sun's web pages](http://java.sun.com/docs/books/tutorial/essential/system/properties.html).  For more information on MRJAppBuilder, see the document _About MRJAppBuilder_ that ships with the MRJ 2.2 SDK in Tools:Application Builders:MRJAppBuilder. For more information on JBindery, consult _About JBindery_ that ships with the MRJ 2.2 SDK (and earlier) in Tools:Application Builders:JBindery. [Apr 24 2000] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
