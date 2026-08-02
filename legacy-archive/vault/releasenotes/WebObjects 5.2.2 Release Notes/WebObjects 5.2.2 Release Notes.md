---
title: WebObjects 5.2.2 Release Notes
apple_id: TP40008112
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2008-12-01'
source_url: http://docs.info.apple.com/article.html?artnum=107649
archived_at: '2026-07-27T07:15:44.185185Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



- [Apple](http://www.apple.com)
- [Store](http://www.apple.com/store/)
- [Mac](http://www.apple.com/mac/)
- [iPod + iTunes](http://www.apple.com/itunes/)
- [iPhone](http://www.apple.com/iphone/)
- [Downloads](http://www.apple.com/downloads/)
- [Support](http://www.apple.com/support/)

Search
You are invited to take part in a short survey to help us improve your
 Apple Support online experience. Please click Yes if you would like to participate.[Yes](javascript:yes();) [No](javascript:closeit();)

Ask a question [Help](http://www.apple.com/support/help/search/)

## [Browse Support](http://www.apple.com/support/)

All Products...
AirPort Extreme & AirPort Express
Aperture
Apple Cinema + Studio Displays
Apple Remote Desktop
Apple TV
AppleWorks
Bluetooth
Bonjour
Boot Camp
Cinema Tools
Color
Compressor
.Mac
DVD Studio Pro
Earlier Macintosh Servers
Earlier Mac models
Earlier Operating Systems
Earlier Power Macintosh
Earlier PowerBooks
eMac
Final Cut Express
Final Cut Pro
Final Cut Studio
GarageBand
iBook
iCal
iChat AV
iDVD
iLife
iMac G3 (CRT)
iMac G4 (Flat-Panel)
iMac G5 + G5 (iSight)
iMovie
Intel-based iMac
iPhone
iPhoto
iPod classic
Earlier iPod models
iPod Hi-Fi
iPod mini
iPod nano (3rd gen)
Earlier iPod nano models
iPod shuffle
iPod touch
iSight
iSync
iTunes
iTunes Store
iWeb
iWork
Keynote
LiveType
Logic Express
Logic Pro
Logic Studio
Mac mini
Mac OS 9
Mac OS X Server v10.5 Leopard
Mac OS X Server v10.4 Tiger
Mac OS X v10.2 and earlier
Mac OS X v10.5 Leopard
Mac OS X v10.3 Panther
Mac OS X v10.4 Tiger
Mac Pro
MacBook
MacBook Air
MacBook Pro
Mail
MainStage
Motion
Nike + iPod
Numbers
Pages
Power Mac G4
Power Mac G4 Cube
Power Mac G5
Power Macintosh G3
PowerBook G3
PowerBook G4
Qmaster
QuickTime Player & QuickTime Pro
Safari
Shake
Soundtrack
Soundtrack Pro
WaveBurner
WebObjects
Wireless Keyboard & Mouse
Xsan
Xserve
Xserve RAID

## Languages

- [English](http://docs.info.apple.com/article.html?artnum=107649-en)
- [日本語](http://docs.info.apple.com/article.html?artnum=107649-ja)

# WebObjects 5.2.2: About the WebObjects 5.2.2 Update

- __Last Modified on:__ June 01, 2007

- __Article:__ 107649
This document contains an overview and download information for Apple's WebObjects 5.2.2 Update. WebObjects 5.2 users who plan to develop their WO applications on Mac OS X 10.3 Panther or who use the Xcode development tool suite or plan to deploy their WO 5.2.2 applications on Mac OS X Server 10.3, Windows or Solaris should install this update.

 Technical document 70037, "[__WebObjects Current Patch List__](http://www.info.apple.com/kbnum/n70037)", contains information on all available patches and updates for all versions of WebObjects. Read this document if you're not sure which update you need on your system.

This update addresses the issues and adds support for the features listed below:

- Incompatibilities between WebObjects 5.2 development tools and Xcode 1.0- Incompatibilities between WebObjects 5.2 and Java 1.4.1 for Mac OS X- Incompatibilities between WebObjects 5.2 and Mac OS X 10.3- Fixes for the Enterprise Object Frameworks runtime- Fixes for WOFileUpload- Provide tighter integration between WebObjects 5.2 and the new JBoss features on Mac OS X 10.3 Server

__Important:__ WebObjects 5.2.2 requires Java 1.4.1. Java 1.3.1 is no longer supported.

__Important:__ You will not be able to use legacy ProjectBuilder to develop WebObjects applications after installing this update.

The [__WebObjects Current Patch List__](http://www.info.apple.com/kbnum/n70037) contains information on all available patches and updates for all versions of WebObjects. Read this document if you're not sure which update you need on your system.

__WebObjects 5.2.2 Developer for Mac OS X 10.3__

__Important:__ Support for developing WebObjects applications using legacy Project Builder and JDK 1.3.1 have been dropped in WebObjects 5.2.2 update.

This update is available through the Software Update feature of Mac OS X. If you use this method, only the proper update for the software which you have installed on your system is visible and available for download. If you prefer to download and install the package manually, follow the instructions below.

__Note:__ WebObjects 5.2.2 Developer requires:

- Mac OS X 10.3 or later- JDK 1.4.1- Xcode 1.0 Developer Tools

If you have not yet updated to the correct version of Mac OS X or Developer Tools, you must do so before installing WebObjects 5.2.2.

If you are creating a new Mac OS X WebObjects 5.2 development system, you should install the software in the following order:

1. Mac OS X 10.3
2. Xcode 1.0 Developer Tools
3. WebObjects 5.2 Developer
4. WebObjects 5.2.2 Developer

__Manually Installing WebObjects 5.2.2 Developer on Mac OS X 10.3__

These instructions are for manually downloading and installing WebObjects 5.2.2 Developer. If you are installing using Software Update, see the previous section of this document, WebObjects 5.2.2 for Mac OS X 10.3.

__Note:__ WebObjects 5.2.2 Developer requires:

- Mac OS X 10.3 or later- JDK 1.4.1- Xcode 1.0 Developer Tools

If you have not yet updated to the correct version of Mac OS X, Java, or Developer Tools, you must do so before installing WebObjects 5.2.2.

1. Download WO522Developer.pkg.tar, the update package for Mac OS X 10.3. The update is available from:

[http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/MultiCountry/Enterprise/webobjects/patches/5.2/WO522Developer.dmg](http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/MultiCountry/Enterprise/webobjects/patches/5.2/WO522Developer.dmg)

The disk image should expand when double clicked in the finder, leaving WO522Developer.pkg.

2. Open WO522Developer.pkg.

The Authenticate panel opens.

__Important:__ Only an administrator can install the update.

3. Type the proper administrator name and password to authenticate.

4. Click OK to proceed. The Introduction panel appears.

5. Click Continue. The Software License Agreement appears.

6. Read the software license agreement, then click Continue.

7. Click Agree to agree to the license agreement and continue the installation.

8. Select the volume containing Mac OS X and WebObjects 5.2 Developer.

9. Click Continue.

10. Make sure that there are no WebObjects or EOF applications running.

11. Click Install to proceed with installation. The Installer window displays information about the progress of the installation, which may take several minutes.

12. Restart your computer.

__WebObjects 5.2.2 Deployment for Mac OS X 10.3 Server__

WebObjects 5.2.2 deployment now comes pre-installed on Panther Server only. To install WebObjects 5.2.2. Deployment, install or upgrade to Mac OS X 10.3 Server.

Configuration tasks:

1. wotaskd is not configured to autostart by default. Open the file /System/Library/StartupItems/WebObjects/WebObjects and uncomment the following line:

#/usr/bin/su appserver -c "$WOSERVICE -appPath $WOTASKD" >/var/log/webobjects.log 2>&1 &

2. If you are planning to use Apache, you will need to update the httpd.config file. Add the following to the end of the file /etc/httpd/httpd.config:

# Including WebObjects Configs
Include /System/Library/WebObjects/Adaptors/Apache/apache.conf

__Installing WebObjects 5.2.2 on Windows 2000__

__Notes__

1. During the installation, if you see panels indicating that certain files being replaced by the update are "locked", click Reboot to continue the installation. The files will be replaced upon restarting.
2. This update cannot be uninstalled alone. Once you have upgraded to WebObjects 5.2.2 you cannot revert to WebObjects 5.2. However, the entire WebObjects 5.2.2 installation can be uninstalled using the Add/Remove Programs control panel.

__Steps__

1. Install JDK 1.4.1 if not yet installed (available from [http://java.sun.com](http://java.sun.com)). This version is required.

2. Download WO522.exe, the self-extracting update installer for Windows 2000.

The update is available from:

[http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/MultiCountry/Enterprise/webobjects/patches/5.2/WO522.exe](http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/MultiCountry/Enterprise/webobjects/patches/5.2/WO522.exe)

3. Log in as a user with Administrator privileges.

4. Make sure that there are no WebObjects or EOF applications running.

5. Double-click on the update installer, WO522.exe, to start the installation process. A screen appears with some information about this update.

6. After you have read the information screen, click Next to continue. The license agreement for this update appears.

7. To agree to the license and continue the installation, click Yes. The update will be installed on your system and you will be asked if you want to restart.

8. Select "Yes, I want to restart my computer now" to restart Windows.

The WinZip self-extractor automatically quits and removes its temporary files in about 20 seconds.

__Installing WebObjects 5.2.2 on Solaris__

1. Install JDK 1.4.1, if not yet installed (available from [http://java.sun.com](http://java.sun.com)). This version is required.

2. Download WO522Solaris.TAR.Z, the update installer for Solaris.

__Note:__ You will also need to download the update installation script, patcher.sh.

The update is available from:

[http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/MultiCountry/Enterprise/webobjects/patches/5.2/WO522Solaris.tar.gzip](http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/MultiCountry/Enterprise/webobjects/patches/5.2/WO522Solaris.tar.gzip)

The installation script is available at:

[http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/MultiCountry/Enterprise/scripts/patcher.sh](http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/MultiCountry/Enterprise/scripts/patcher.sh)

After you have downloaded the files, the patcher.sh script needs its executable bit set. At the command prompt enter:

chmod 511 patcher.sh

3. Log in as root.

4. Make sure that there are no WebObjects or EOF applications running, including Monitor.

5. If a web server is running on the computer on which you are installing the update, stop it.

6. Stop WebObjects services ( wotaskd and woservice ) using the WOServices script. At the command prompt enter:

cd $NEXT_ROOT/Library/WebObjects/Executables ./WOServices stop

These services will restart when you restart the computer after installing the update.

7. To Install the update, cd to the directory containing the update and the patcher.sh installation script. Then at the command prompt enter:

patcher.sh -install WO522Solaris.TAR.Z

For more information on using patcher.sh, at the command prompt enter:

patcher.sh -help

8. Copy the updated WODocument root to your web server's document root.

cp -r $NEXT_ROOT/Library/WebObjects/WODocumentRoot/WebObjects <webserver doc root>/WebObjects

9. Restart your computer.

__Issues resolved in WebObjects 5.2.2__

__EOBeanBuilder does not handle entities with relationships properly.__

Apple Reference 3012075

ISSUE:

EOBeanBuilder does not handle entities with relationships properly.

RESOLUTION:

This issue has been resolved and support for Container Managed Persistence 2.0 (CMP) in Enterprise Java Beans (EJBs) have been added.

__WOFileUpload is improperly setting filePath when no file is uploaded.__

Apple Reference 3078140

ISSUE:

Sometimes the filePath binding was munged after repeated uploads.

RESOLUTION:

If the user submits a file upload without a filepath binding, the filePath string will be set to "".

__EOModeler does not support double quotes in building qualifiers.__

Apple Reference 3081517

ISSUE:

When double quotes are used in building qualifiers, an extra space is added to the end of the qualifiers. For example, (title like "A\*") would be treated as (title like A\* ), which breaks the data browsing and filtering functionality.

RESOLUTION:

This issue has been resolved.

__wotaskd does not launch upon start up after specifying it to launch using a non-root user.__

Apple Reference 3088811

ISSUE:

A few double quotes are misplaced in the startup script /System/Library/StartupItems/WebObjects.

RESOLUTION:

This issue has been resolved.

__The class EOAttribute throws the exception ClassCastException when illegal arguments are encountered under certain situations.__

Apple Reference 3101631

ISSUE:

The method adaptorValueByConvertingAttributeValue() defined in the class EOAttribute throws the exception ClassCastException when illegal arguments are encountered.

RESOLUTION:

The exception IllegalArgumentException is thrown upon encountering illegal arguments.

__Content encoding related exceptions are thrown when WebObjects encounters Chinese/Japanese characters.__

Apple Reference 3135465

ISSUE:

WebObjects determines the content encoding based on HTTP headers only and ignores other encoding information in XML content.

RESOLUTION:

This issue has been resolved.

__Checked boxes generated by WOCheckedboxMatrix do not align correctly in some cases.__

Apple Reference 3148863

ISSUE:

If the text to the right of the checked boxes takes more than one line and if it wraps, the checked boxes are aligned between the lines instead of aligning at the first line.

RESOLUTION:

This issue has been resolved.

__Accesses to EOObjectStore are blocked after calling EODatabaseDataSource.qualifyWithRelationshipKey() in some cases.__

Apple Reference 3177592

ISSUE:

The lock acquired by calling EODatabaseDataSource.qualifierForRelationshipKey() never gets released.

RESOLUTION:

This issue has been resolved.

__The name "shared" cannot be used as an attribute name for an entity in WebObjects 5.2, but it can in WebObjects 5.0.__

Apple Reference 3179807

ISSUE:

Some private methods introduced to EOCustomObject in WebObjects 5.2 conflict with users specified property names.

RESOLUTION:

This issue has been resolved.

__The Object Inspector of WebObjects Builder does not handle binding values started with the character "^" correctly.__

Apple Reference 3179819

ISSUE:

Whenever a value started with "^" get assigned to a binding using Object Inspector, the binding value get double-quoted undesirable

RESOLUTION:

This issue has been resolved.

__WebObjects Builder does not handle binding value starting with the character "-" correctly.__

Apple Reference 3180520

ISSUE:

Whenever WebObjects Builder encounters a binding value starting with the character "-", it interprets it as an incorrect declaration.

RESOLUTION:

This issue has been resolved.

__The binding "overwrite" in the WOFileUpload example shipped in WebObjects 5.2 is not being respected.__

Apple Reference 3188888

ISSUE:

There are some issues with files renaming in some cases, which causes overwriting to fail.

RESOLUTION:

This issue has been resolved.

__JDBCContext does not respect the value returned by EOAdaptorContext.Delegate.adaptorContextShouldCommit()__

Apple Reference 3190939

ISSUE:

Even if EOAdaptorContext.Delegate.adaptorContextShouldCommit() returns true, JDBCContext always does the commit instead of delegating the responsibility to the delegate.

RESOLUTION:

This issue has been resolved.

__False warnings about missing locks are issued in some cases inside the method EOEditingContext._undoManagerCheckpoint() .__

Apple Reference 3192337

ISSUE:

Certain assertion checks in EOEditingContext are invalid.

RESOLUTION:

This issue has been resolved.

__NullPointerException is thrown in EOAttribute.adaptorValueType() upon generating an error message.__

Apple Reference 3192384

ISSUE:

If an illegal internal type presents in the definition of a stored procedure, EOAttribute.adaptorValueType() would throw an NullPointerException upon generating an error message.

RESOLUTION:

This issue has been resolved.

__NSTimeZone.timeZoneWithName() returns null in some cases, when handling certain names and abbreviations of some well-known time zones in JVM 1.4.1.__

Apple Reference 3203985

ISSUE:

Some new names/abbreviations for well-known time zones was introduced in Java Virtual Machine (JVM) ver. 1.4.1. NSTimeZone.timeZoneWithName() could not handle those names/abbreviations.

RESOLUTION:

This issue has been resolved.

__willRead() will throw a NullPointerException when an EO is in an invalid state.__

Apple Reference 3223265

ISSUE:

EOCustomObject can throw an NullPointerException in willRead() if the EO is either not inserted in an EOEditingContext or is somehow a zombie.

RESOLUTION:

It now throws an IllegalStateException instead.

__The width of some JComboBoxes in Direct to Java Client applications is not scaled according to the list of selectable values.__

Apple Reference 3252950

ISSUE:

In some cases JComboBox.getPerferredSize() returns less than optimal dimension in Java Virtual Machine ver. 1.4.1.

RESOLUTION:

This issue has been resolved.

__EOEditingContext throws NullPointerException in some cases.__

Apple Reference 3252964

ISSUE:

In some cases notifications are sent to an already disposed nested EOEditingContext.

RESOLUTION:

This issue has been resolved.

__There is an extra non-black space in the closedLabel attribute of the WOCollapsibleComponentContent.__

Apple Reference 3252969

ISSUE:

The closedLabel attribute of the WOCollapsibleComponentContent contains an extra non-blank space.

RESOLUTION:

This issue has been resolved.

__An error message is returned to Safari by Apache Web Server upon calling session.terminate().__

Apple Reference 3253004

ISSUE:

Cookies expiration is not being handled correctly, which causes issues with Safari and Apache Web Server.

RESOLUTION:

This issue has been resolved.

__The binding codebase of WOApplet is being ignored.__

Apple Reference 3255852

ISSUE:

The binding code base of WOApplet is not being respected.

RESOLUTION:

This issue has been resolved.

__Interface Builder crashes upon opening the MainMenu.nib file of a Cocoa Enterprise Objects Application project.__

Apple Reference 3319422

ISSUE:

When a Cocoa Enterprise Object Application project was created, a MainMenu.nib file was created by default. Upon opening such nib file, Interface Builder crashes.

RESOLUTION:

This issue has been resolved.

__An alter panel was displayed when launching Interface Builder on a system with Java Virtual Machine (JVM) ver. 1.4.1 installed as default JVM.__

Apple Reference 3319683

ISSUE:

Although the system default JVM was 1.4.1. Interface Builder still uses JVM 1.3.1 in some cases, which causes an error java.lang.UnsupportedClassVersionError.

RESOLUTION:

This issue has been resolved.

__Upon disposing an editing context, NSDelayedCallbackCenter throws an IllegalArguementException in some cases.__

Apple Reference 3323451

ISSUE:

Upon disposing an editing context, an IllegalArgumentException was thrown in NSDelayedCallbackCenter._cancelAllActionsWithTarget()
due to encountering an array out of bound issue.

RESOLUTION:

This issue has been resolved.

__Troubleshooting:__

__1. My application is throwing the exception "com.webobjects.foundation.NSForwardException for java.lang.NoClassDefFoundError: javax/servlet/ServletContext"__

For some reason, the necessary packages are not in your classpath. Debug your classpath to make sure the javax.servlet.\* classes are there. If the classes are not found, the resolution is to download the servlet.jar and put it into /Library/Java/Extensions or in your classpath. The servlet.jar can be found with many open source distributions (e.g tomcat).

__2. How do I convert my legacy WebObjects application to build as a true war bundle?__

1. In Xcode, configure your build settings to the following:

SERVLET_SINGLE_DIR_DEPLOY = NO
SERVLET_STUB_WAR = NO
SERVLET_TRUE_WAR = YES
SERVLET_DEPLOY_LICENSE = <your deployment license>
SERVLET_WEBAPPS_DIR = /Library/JBoss/3.2/deploy

2. add the JavaWOJSPServlet.framework to your project

3. You should also verify that all of your custom frameworks are being built as jar files and are installed or linked into /Library/WebObjects/lib.

__Keywords:__

ktech kobjects kmosx kwindows kwinxp__Did this article help you?__

__[It solved my issue...](http://docs.info.apple.com/survey/index.html?v=1&artnum=107649)__

Tell us what works for you.

__[It's good, but...](http://docs.info.apple.com/survey/index.html?v=2&artnum=107649)__

Report typos, inaccuracies, etc.

__[It wasn't helpful...](http://docs.info.apple.com/survey/index.html?v=3&artnum=107649)__

Tell us what would have helped.

[Home](http://www.apple.com)
>
[Support](http://www.apple.com/support/)

Visit the Apple Store [online](http://www.apple.com/store/) (1-800-MY-APPLE), visit a [retail](http://www.apple.com/retail/) location, or find a [reseller](http://www.apple.com/buy/locator/).

[Site Map](http://www.apple.com/sitemap/) | [Hot News](http://www.apple.com/hotnews/) | [RSS Feeds](http://www.apple.com/rss/) | [Contact Us](http://www.apple.com/contact/)

Copyright © 2008 Apple Inc. All rights reserved. [Terms of Use](http://www.apple.com/legal/terms/site.html) | [Privacy Policy](http://www.apple.com/legal/privacy/)
