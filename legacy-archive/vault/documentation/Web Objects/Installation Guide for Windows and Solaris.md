---
title: Installation Guide for Windows and Solaris
apple_id: TP40000882
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-11-01'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/WO_Install_Win_Sol/WOOtherIG_Overview/WOOtherIG_Overview.html
archived_at: '2026-07-18T02:21:56.105756Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)



# Installation Guide for Windows and Solaris

WebObjects includes both a development environment and a deployment platform. Before installing WebObjects, you need to determine which to install. WebObjects Developer is supported on Windows 2000 Professional. WebObjects Deployment is supported on Windows 2000 Server and on Solaris. The deployment packages are included with WebObjects Developer so if you install WebObjects Developer, you do not need to install WebObjects Deployment.

WebObjects Developer provides the tools for you to build powerful and robust client-server applications for corporate intranets or the World Wide Web. The WebObjects development environment includes these applications:

- _Project Builder_ for managing and organizing your development projects, including code editing, compiling, and debugging in a variety of languages
- _Interface Builder_ for visual development of desktop and Java Client user interfaces
- _WebObjects Builder_ for viewing and editing HTML in either markup or preview mode
- _EOModeler_ for visual entity relationship mapping, forward and reverse engineering of database schemata, and integration of multiple data sources within a single model

WebObjects Deployment provides the architecture and tools to deploy your WebObjects applications on an intranet or the World Wide Web. It supplies the necessary Web server adaptors as well as WebObjects Monitor and `wotaskd` to allow you to remotely view server instances and generate statistical data on your deployed applications.

This guide describes how to install and remove both WebObjects Developer and WebObjects Deployment. The WebObjects 5.2 CD contains the software you need for both types of installation.

Additional WebObjects documentation is available online at [http://developer.apple.com/tools/webobjects/](https://developer.apple.com/tools/webobjects/). WebObjects Developer on Windows also provides the WebObjects Info Center for viewing WebObjects documentation.

- 100% Pentium-compatible computer
- Microsoft Windows 2000 Professional or Server
- 256 MB of RAM
- at least 1 GB of available hard disk space (except on a FAT file system where you’ll need considerably more space)

Before installing the WebObjects components you need to make sure that some other details are taken care of:

- If you have a previous version of WebObjects installed, it is important that you first remove the old version before installing WebObjects 5.2.

- WebObjects works in concert with your Web server software. If you haven’t installed the Web server software already, you should do so before installing WebObjects. The WebObjects installer will ask you for the location of your cgi-bin and document root directories; make sure to take note of these locations before proceeding.

- WebObjects Deployment requires the Java 2 Platform, Standard Edition version 1.3.1 Java Runtime Environment (JRE). WebObjects Developer requires the Java 2 Platform, Standard Edition version 1.3.1 Software Development Kit (SDK).

  If you plan to use the JNDI (Java Naming and Directory Interface) adaptor to access information in an LDAP (Lightweight Directory Access Protocol) data source you also need to install the Java Platform, Standard Edition version 1.1.8 Java Development Kit (JDK).

  Install the appropriate Java components (available at [http://java.sun.com](http://java.sun.com/)) before proceeding.

1. Log in to an account that has administrator privileges.
2. Insert the WebObjects CD in your computer’s CD-ROM drive and navigate to the Windows folder.
3. Open the Setup application. (Depending on your system settings, the name may be `Setup.exe` or just `Setup`.) The installer for WebObjects starts.
4. Click Next. Read the software license agreement. If you agree to its terms, click Yes to continue with the installation.
5. Follow the onscreen prompts to the Customer Information screen. You are asked for a serial number, which is included with your WebObjects CD.
6. Continue to the Setup Type screen. Apple recommends that you perform a Typical installation. Perform a Custom installation only in the following circumstances:

   - You need to install WebObjects in a location on the file system other than the default (`C:\Apple\`).
   - You are installing WebObjects Developer on a system running the Japanese version of Windows. In this case you need to install the IME Support package, which is part of the Extras component.
   - You are installing WebObjects Developer and need to install the GNU source code with Apple modifications (part of the Extras component).

   If you do a Custom installation follow these guidelines:

   - Do not install WebObjects into a system-related folder such as WinNT, directly to the root of a disk, or to any path or folder whose name contains spaces. If you do, the software may not work.
   - Make sure that the entire WebObjects root directory path (for example `C:\Apple\`) is no longer than twelve characters and does not include any spaces. If the root directory path is too long, the software may not work. WebObjects will resolve `NEXT_ROOT` to the location where you install WebObjects instead of the default, `C:\Apple\`.
   - Apple recommends that you do not deselect any of the default packages during a Custom installation.
7. Follow the onscreen prompts to complete the installation. You need to restart your computer to finish the WebObjects installation.

Once you have restarted, you can verify that the application server is running by connecting to [http://localhost:1085](http://localhost:1085/). You should see a page that displays the configuration information for `wotaskd`.

The installer puts the WebObjects CGI adaptor into the cgi-bin directory you specified during installation and configures WebObjects to use it. WebObjects also includes a number of Web server adaptors. To use another adaptor, see the adaptor installation instructions in `NEXT_ROOT\Library\WebObjects\Adaptors`.

These adaptors are provided in source form so that you can customize them for your needs. Instructions for rebuilding the WebObjects Web server adaptors accompany the source code in `NEXT_ROOT\Developer\Examples\WebObjects\Source\Adaptors\`.

WebObjects 5.2 includes some third-party JAR files that you need for applications that use Enterprise JavaBeans (EJB), JavaServer Pages (JSP), Java Servlet integration, Web services, or Java Database Connectivity (JDBC). These JAR files are provided in the `ThirdPartyJars` directory on your WebObjects 5.2 CD. The JDBC extensions and JTA JAR files should be put into the location specified in your `JavaConfig.plist`  along with any of the necessary JDBC drivers. (If you are installing WebObjects Development, install the Java 1.1.8 JDBC driver, not the Java 2 JDBC driver.) Any other JAR files you need should be put into `NEXT_ROOT\Local\Library\WebObjects\Extensions`.

You can remove WebObjects 5.2 using Add/Remove Programs in the Control Panel. This requires you to be logged in to an account with administrator privileges. You need to restart your computer to completely remove WebObjects. For information on removing previous versions of WebObjects, see the documentation that came with the version you wish to remove.

You may upgrade your WebObjects Developer license to a WebObjects Deployment license on a particular computer without reinstalling the software. Run the WebObjects 5 License Upgrader application (Start > Programs > WebObjects > WebObjects 5 License Upgrader) as a user with administrator privileges. This application prompts you for the license key obtained from Apple. This application is installed only with WebObjects Developer.

- Solaris 8
- 256 MB of RAM
- at least 1 GB of available hard disk space

Before installing WebObjects, you should remove any previously installed WebObjects components.

WebObjects Deployment needs the Java Runtime Environment (JRE) version 1.3.1. If you do not already have it installed, install the JRE available at `http://java.sun.com` before installing WebObjects.

WebObjects Deployment works in concert with your HTTP server software. If you haven’t installed an HTTP server already, do so before installing WebObjects Deployment.

Before installing, you need to determine if you are going to perform a full installation or install only the Web server adaptors. If you plan to install the WebObjects application server on another computer than the computer (or computers) running your Web server, do an adaptor-only installation on the computer running a Web server; perform a full installation on the computer that you will use as your WebObjects application server. The installer gives you this option.

During installation, you will be prompted to enter the paths to your HTTP server’s cgi-bin (or scripts) directory and document root directory. Although you can specify a temporary directory for the installed files, you may want to note the paths before beginning your installation. By default Apache uses `/var/apache/cgi-bin` and `/var/apache/htdocs` respectively. If you do not set these paths during the installation you will need to manually copy the appropriate files after installation:

- Copy `/opt/AppleNOAdaptor/Library/WebObjects/Adaptors/CGI/WebObjects` into your cgi-bin directory.
- Copy the /`opt/AppleNOAdaptor/Library/WebObjects/WODocumentRoot/WebObjects` directory into your Web server’s document root directory.

Make sure to have a valid license key handy.

1. Log in as the root user.
2. If necessary, mount the CD-ROM.
3. Navigate to `Deployment/SOLARIS/WebObjects/` in the mount directory of the CD-ROM.
4. Start the install script with this command:

```
./install.sh
```
5. Follow the onscreen prompts to complete the installation.

As the installer finishes, it mentions three installation details to finalize:

- Add the following line to your `httpd.conf` file:

  `Include /opt/Apple/Library/WebObjects/Adaptors/Apache/apache.conf`
- Enable WebObjects services to start when your computer starts (if you want this and did not choose that option when prompted) by typing:

  `/opt/Apple/Library/WebObjects/Executables/WOServices enable`
- Define the `NEXT_ROOT` environment variable in your shell startup script. Unless you have chosen a nonstandard location to install WebObjects, this should be defined as `/opt/Apple`.

With the completion of the installation process, all of the necessary files are copied to the target computer, the cgi-bin and document root directories are created (if necessary), an uninstall script is created, startup scripts for WebObjects services are created (if requested), and WebObjects services are started (if requested).

This completes the installation of WebObjects. If you did a full installation, you can verify a successful installation of WebObjects Deployment by connecting to port 1085 of your computer. You should see a page that displays the configuration information for `wotaskd`.

If you did an adaptors-only installation, you can verify that the adaptors are functioning properly or troubleshoot incorrect behavior using the following procedure:

1. Stop your Web server.
2. As the root user: `touch /tmp/logWebObjects`
3. Start your Web server.

This enables WebObjects logging. When your Web server starts, it creates a file in  `/tmp` named `WebObjects.log`. The existence of this file verifies that your adaptor is correctly installed.

If you specify a cgi-bin directory during installation, the installer puts WebObjects CGI adaptors into this directory and configures WebObjects to use them. WebObjects also includes a number of other Web server adaptors. To use one of these, see the online adaptor installation instructions in `NEXT_ROOT/Library/WebObjects/Adaptors/`. These adaptors are provided in source form and can be customized. For instructions on rebuilding these WebObjects Web server adaptors, see `NEXT_ROOT/Developer/Examples/WebObjects/Source/Adaptors/BuildingInstructions.html`.

WebObjects 5.2 includes third-party JAR files that you need for applications that use Enterprise JavaBeans (EJB), JavaServer Pages (JSP), Java Servlet integration, Web services, or Java Database Connectivity (JDBC). The JAR files you need are provided for you in the `ThirdPartyJars` directory on your WebObjects 5.2 CD. They should be copied into `NEXT_ROOT/Local/Library/WebObjects/Extensions`.

1. Stop your Web server.
2. Find and kill any WebObjects processes that may be running.

   `ps -ef | grep -i wo` will help you in finding running WebObjects processes.
3. From the root level of your directory structure (`/`), run `NEXT_ROOT/Library/Executables/uninstall.sh`.

To apply a deployment license to an existing deployment installation, you need only change the installed serial number. Using a text editor, edit `NEXT_ROOT/Library/Frameworks/WebObjects.framework/Resources/License.key` and replace the license key found there with the new license key obtained from Apple.

