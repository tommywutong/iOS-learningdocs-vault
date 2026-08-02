---
title: Installation Guide for Mac OS X
apple_id: TP40000881
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-11-01'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/WO_OSX_Install/WOMacIG_Overview/WOMacIG_Overview.html
archived_at: '2026-07-18T02:21:56.174638Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)



# Installation Guide for Mac OS X

WebObjects includes both a development environment and a deployment platform. Before installing WebObjects, you need to determine which to install. WebObjects Developer is supported on the desktop version of Mac OS X. WebObjects Deployment is supported on Mac OS X Server. (The Xserve server ships with WebObjects Deployment, not WebObjects Development.) The deployment packages are included with WebObjects Developer so if you install WebObjects Developer, you do not need to install WebObjects Deployment.

WebObjects Developer provides the tools for you to build powerful and robust client-server applications for corporate intranets or the World Wide Web. In addition to introducing applications unique to WebObjects, it enhances the Project Builder and Interface Builder applications provided with the Mac OS X Developer Tools. The WebObjects development environment includes these applications:

- _Project Builder_ for managing and organizing your development projects, including code editing, compiling, and debugging in a variety of languages
- _Interface Builder_ for visual development of desktop and Java Client user interfaces
- _WebObjects Builder_ for viewing and editing HTML in either markup or preview mode
- _EOModeler_ for visual entity relationship mapping, forward and reverse engineering of database schemata, and integration of multiple data sources within a single model

WebObjects Deployment provides the architecture and tools to deploy your WebObjects applications on an intranet or the World Wide Web. It supplies the necessary Web server adaptors as well as WebObjects Monitor and `wotaskd` to allow you to remotely view server instances and generate statistical data on your deployed applications.

This guide describes how to install and remove both WebObjects Developer and WebObjects Deployment. The WebObjects 5.2 CD contains the software you need for both types of installation.

Additional WebObjects documentation is available online at [http://developer.apple.com/tools/webobjects/](https://developer.apple.com/tools/webobjects/) and, after installation, in `/Developer/Documentation/WebObjects`.

- a Macintosh with a PowerPC G3 or G4 processor
- Mac OS X version 10.2.2 or later for WebObjects Development, Mac OS X Server 10.2.2 or later for WebObjects Deployment (see [Before Installing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqobrfuys2qscincessciiy) before upgrading to Mac OS X version 10.2)
- at least 256 MB of RAM
- at least 1 GB of available hard disk space
- administrator access to the computer you are installing on

If you have a version of WebObjects earlier than 5.1, you must first remove the old version before installing WebObjects 5.2. If you are not already running Mac OS X version 10.2, remove the old version of WebObjects before upgrading to Mac OS X version 10.2.

If you have WebObjects 5.1 installed, you may upgrade to WebObjects 5.2 by running the WebObjects 5.2 installer. See [Removing WebObjects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqobrfuys2qscineuuqsfi4) for more information on how to remove WebObjects.

You must install WebObjects Developer locally by double-clicking the installer package. Although you can install WebObjects Deployment locally, you may also install it remotely using the command line.

To install locally:

1. Log in as a user with administrator privileges.
2. If you are installing WebObjects Developer, install the Mac OS X Developer Tools included with Mac OS X before proceeding.
3. Insert the WebObjects CD and navigate to either the Deployment or Developer folder depending on your installation choice.
4. Inside the folder you have chosen is the WebObjects installer. It is named either `WebObjects_X_Developer.mpkg` or `WebObjects_X_Deployment.mpkg`. Double-click the appropriate installer.
5. Follow the onscreen prompts to complete the installation. You will be prompted for your license key, which is included with your WebObjects CDs.

The installer prompts you to restart your computer. Once you have restarted, you can verify that the application server is running by connecting to [http://localhost:1085](http://localhost:1085/). You should see a page that displays the configuration information for `wotaskd`.

Remote installation of WebObjects Deployment is useful for headless servers like the Xserve.

To install remotely, `sshd` needs to be running on the computer you wish to install onto. For Mac OS X Server, it is running by default. If it is not running, go to the Sharing pane of System Preferences. Click the Services tab and turn on Remote Login. You also need to have the WebObjects 5.2 CD in the computer you wish to install WebObjects on. With `sshd` turned on and the WebObjects CD in the drive of the computer, follow these steps to install WebObjects from a remote computer:

1. Use `ssh` to log in to the target computer with an administrator login and password.
2. Navigate to the location of the appropriate installation folder on your WebObjects CD. For example:

   `cd /Volumes/WebObjects\ 5.2\ OSX/Deployment`
3. Run the installer with the `sudo` command. Use the `-pkg` and `-target` flags. If you want to see the progress of your install, you might also want to use the `-dumplog` flag. For example, a standard installation of WebObjects Deployment looks like this:

   `sudo installer -dumplog -pkg ./WebObjects_X_Deployment.mpkg -target /`
4. Once the installation is complete, you need to restart your computer. Use `sudo /sbin/reboot`.

Again, a simple test of this installation is to confirm that you can connect to your server on port 1085.

By default, the installer configures the Apache Web server to use the WebObjects Apache adaptor. WebObjects also includes a CGI adaptor. If you wish to use it, configuration instructions are in `/System/Library/WebObjects/Adaptors/CGI/InstallationInstructions.html`. The source code for both adaptors (and adaptors for other platforms) are provided so that you can customize them. Instructions on rebuilding the WebObjects HTTP server adaptors are available in `/Developer/Examples/WebObjects/Source/Adaptors/BuildingInstructions.html`.

WebObjects 5.2 includes third-party JAR files that you need for applications that use Enterprise JavaBeans (EJB), JavaServer Pages (JSP), Java Servlet integration, Web services, or Java Database Connectivity (JDBC). Some useful JAR files are provided for you in the `ThirdPartyJars` folder on your WebObjects 5.2 CD. The JDBC extensions and Java Transaction API (JTA) JAR files should be put into `/Library/Java/Extensions` along with the appropriate JDBC drivers. Any other JAR files you need should be put into `/Library/WebObjects/Extensions`.

By default, `wotaskd` starts up when your system boots. You can configure `JavaMonitor` to start automatically also, and specify which user both of these processes run as, by uncommenting the appropriate lines in `/System/Library/StartupItems/WebObjects/WebObjects`.

For an installation of WebObjects Deployment on Mac OS X Server it is recommended that you turn off the performance caching on the Web server.

Performance caching allows for greater server performance on sites with static html pages. Since WebObjects works with dynamically generated Web pages, it is important to turn this off so that your WebObjects generated Web pages behave as expected.

To turn off performance caching on Mac OS X Server:

1. Connect to your Web server with the Server Settings application.
2. Choose the Internet tab.
3. Click Web and choose Configure Web Service.
4. Choose the Sites tab.
5. Select the appropriate site and click Edit.
6. Choose the Options tab.
7. Deselect Enable performance cache.
8. Click Save.
9. In the dialog, choose the option to Restart Now.

The WebObjectsLicenseUpgrader installed in `/Applications/Utilities/` allows you to modify your WebObjects license without reinstalling the software. To run this application, you must be logged in as an administrator user. The application requires one of the license keys that came with your copy of WebObjects.

WebObjects 5.2 includes three applications to remove WebObjects from your system. Your particular needs will determine which one you should use.

- If you are using Mac OS X version 10.1 and need to remove WebObjects 4.5.1, 5.0, or 5.1, use the `WO451-51Uninstall.pkg` provided on your WebObjects CD. This application doesn’t work on other versions of Mac OS X. (If you need to remove WebObjects 5.1 from a system with Mac OS X version 10.2, first upgrade WebObjects to version 5.1.4 and then use the WO5Uninstall application in `/Applications/Utilities`.)
- If you need to remove WebObjects 5.2 and have an account for the root user enabled on your computer, use the WO52Uninstall application in `/Applications/Utilities`. Log in as the root user before using this application.
- If you need to remove WebObjects 5.2 and do not have a root account enabled, use the `WO52Uninstall.pkg` on your WebObjects CD.

This information is presented in [Table 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqobrfuys2qscindugssjiq) based on which version of WebObjects and Mac OS X you have installed.

__Table 1-1__   Removing WebObjects from Mac OS X

| If you have: | Mac OS X version 10.1 | Mac OS X version 10.2 |
| WebObjects 4.5.1 | Use the `WO451-51Uninstall.pkg` provided on your WebObjects CD. | Not supported. |
| WebObjects 5.0 | Use the `WO451-51Uninstall.pkg` provided on your WebObjects CD. | Not supported. |
| WebObjects 5.1 | Use the `WO451-51Uninstall.pkg` provided on your WebObjects CD. | Upgrade to WebObjects 5.1.4, then run the WO5Uninstall application in  `/Applications/Utilities`. |
| WebObjects 5.2 | Not supported. | If you have root access, log in as the root users and run WO52Uninstall (in  `/Applications/Utilities`). If you don’t have root access, but do have administrator access, use the `WO52Uninstall.pkg` provided on your WebObjects CD. |

If you run either of the two versions included on the CD, you are prompted for an administrator login and password, but you do not need to log in as the root user. These applications first launch the Installer application. The WO5Uninstall application is bootstrapped by the Installer application. This means that before removing WebObjects, you will be prompted to “Install.” After the removal process is complete, the Installer displays the message “The software was successfully installed.” Don’t worry, you have removed, not installed, WebObjects.

If you need to remove versions of WebObjects older than WebObjects 4.5.1, use the removal mechanism provided with the version of WebObjects that you wish to remove.

