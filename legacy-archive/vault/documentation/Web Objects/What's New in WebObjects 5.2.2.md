---
title: What's New in WebObjects 5.2.2
apple_id: TP40000967
resource_type: Guide
platform: macOS
topic: null
technology: WebObjects
published: '2003-10-16'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/WhatsNew/WhatsNew/WhatsNewIn522.html
archived_at: '2026-07-18T02:22:15.158750Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)



# What’s New in WebObjects 5.2.2

This document describes the major new features of WebObjects 5.2.2 and explains the most significant changes made to the product.

This release includes support for Mac OS X v 10.3 and Xcode, the new development tools for Mac OS X. This release also fully supports Java 1.4.1 and deployment of WebObjects applications using the JBoss application server. Some problems were fixed in this release but mostly the API was changed in support of servlet/J2EE containers. You can now optionally build your WebObjects applications and frameworks as true JAR files. In support of this, all String path-based API was deprecated and replaced with URL-based API.

Refer to these sections for more details:

- [Support for Mac OS X v 10.3 and Xcode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrxfvkfamzqgaydambsgqwueqsdizfeurkc)
- [Support for Java 1.4.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrxfvkfamzqgaydambsgqwugscejjbeirkb)
- [Support for JBoss Application Server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrxfvkfamzqgaydambsgqwugsceivceeq2g)
- [Resolved Problems](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrxfvkfamzqgaydambsgqwugsceivauqr2g)
- [Summary of API Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrxfvkfamzqgaydambsgqwugsceirbeoqkj)

WebObjects applications can now be developed using Xcode on Mac OS X v 10.3. Xcode is Apple's new integrated development environment (IDE) for Mac OS X. It is designed to fully support all of the major platform initiatives of Mac OS X, such as the Carbon and Cocoa frameworks, Java, and new application packaging mechanisms. For more information on Xcode see [A Quick Tour of Xcode](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/A_Tour_of_Xcode/000-Introduction/qt_intro.html#//apple_ref/doc/uid/TP30000890-CH204).

WebObjects 5.2.2 now fully supports Java 1.4.1 (earlier versions of Java are not supported). Both the Java 1.4.1 Update 1 and the Mac OS X v 10.3 release for Java 1.4.1 provide bug fixes and enhancements, especially for graphics functionality. These updates and changes are all discussed in detail in the release notes for Java 1.4.1, the Java 1.4.1 Update 1, and for Mac OS X v 10.3 at [http://developer.apple.com/releasenotes/Java/index.html](https://developer.apple.com/releasenotes/Java/index.html).

WebObjects applications can now be hosted by any servlet/J2EE container including the JBoss application server available on Mac OS X v 10.3. JBoss is configured to use Tomcat (using the AJP connector) as its web server and servlet container. This differs from the standard configuration, which uses Jetty. In addition, HTTP and HTTPS (through port 8443) are enabled by default. For more information on JBoss and Mac OS X, see Mac OS X Java Application Server Administration and other related documents at [www.apple.com/server/documentation](http://www.apple.com/server/documentation).

Several fixes were made to the Enterprise Object Frameworks runtime and miscellaneous classes such as WOFileUpload. See the WebObjects 5.2.2 release notes for details on the problems fixed in this release, and remaining problems that will be fixed in future releases.

There were many miscellaneous changes to the WebObjects API across all frameworks. In general, the API changes were made in support of hosting WebObjects applications on any servlet/J2EE container including the JBoss application server. For example, all String path-based API was replaced with URL-based API.

Now when you create a servlet/J2EE container application you can choose the True WAR option. To build a True WAR servlet, all of your frameworks must be in the NSJarBundle format, and located in the `/Library/WebObjects/lib/` directory. When you choose the True WAR option, all your application and framework code is bundled together into a single file—the WAR archive. Deploying a WAR archive does not require that the WebObjects runtime be installed on the deployment host. WAR archives are intended for use in Servlet Containers such as JBoss.

Typically, WebObjects applications and frameworks exist in a directory format. Applications can now optionally be built as correct WAR files, instead of stubbed WAR or SSDD, and frameworks can be built as JARs implemented by the NSJarBundle class. To build an NSJarBundle from a framework, set the `BUNDLE_AS_JAR` build property to `YES`.

However, to use this option, you have to avoid using file and directory paths in your code. In general, it is recommended that WebObjects developers use URLs instead of String paths. Therefore, in WebObjects 5.2.2, all API that takes a String path as an argument has been deprecated, and replaced with API that takes a URL as an argument. Although all the WebObjects frameworks have been modified to use URLs, third party frameworks might still use file paths and therefore, may not work in the NSJarBundle format.

Also, in support of servlet management tools, `getProperty()` was added to NSProperties. Use this method instead of `System.getProperty()` to get system properties. This new method will nicely fall back to JNDI lookups if there are no relevant properties, which makes the properties easy to modify or inspect from servlet management tools.

See `/Developer/Documentation/WebObjects/Reference/changes.html` for details on the API changes made in WebObjects 5.2.2.

