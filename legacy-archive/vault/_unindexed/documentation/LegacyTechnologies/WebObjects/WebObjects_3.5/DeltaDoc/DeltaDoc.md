---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DeltaDoc/DeltaDoc.html
archived_at: '2026-07-15T07:51:07.994259Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


# WebObjects Release 3.5

__Changes from Release 3.0 and 3.1__

11/18/97

If you've used WebObjects 3.0 or 3.1, this document tells you what's new in WebObjects Release 3.5. The differences between Release 3.5 and 3.1 fall into these major areas:

- Improved development experience
- Improved deployment
- Improved Java support

This document only summarizes the changes. For more complete details, see the rest of the WebObjects documentation set (available online at [http://devworld.apple.com/techinfo/techdocs/enterprise/WebObjects](http://devworld.apple.com/techinfo/techdocs/enterprise/WebObjects)).

Release 3.5 is backwards-compatible with Release 3.0, meaning that you should be able to run your existing WebObjects 3.0 (and 3.1) applications without having to change source code. However, the way you use the tools has changed. In particular, the way that WebObjects application projects are organized has changed. You'll probably want to convert your projects as described later in [Converting Projects](#apple-inxw45tfoj2gs3thkbzg62tfmn2hg).

## Improved Development Experience

To improve the development experience, the following changes have been made:

- Direct to Web, a new feature that quickly creates applications from existing databases, has been added.
- WebObjects Builder has been completely redesigned and rewritten.
- Certain tasks, in particular project management and code editing tasks, have moved to Project Builder. You now use Project Builder for all projects, not just ones that contain compiled code.
- Launching WebObjects applications has been simplified.

Major changes to the tools are summarized here. For more information on how to use them, see the book [_Getting Started With WebObjects_](../GettingStarted/GettingStartedTOC.md) or the online book [_WebObjects Development: Tools and Techniques_](../WOTools/WOToolsTOC.md), which is available on the Apple website.

### Direct to Web

Direct to Web is a new feature in WebObjects 3.5 that helps you quickly build database applications. To use Direct to Web, create a new WebObjectsApplication project in Project Builder and choose Direct to Web as the type of assistance. All you need to do is point Direct to Web at an EOModeler model file, and your application is ready to run. Launch that application, and you'll be presented with a login panel in your web browser. If you click the "Login with Web Assistant" button, you can not only view the pages that Direct to Web created for you, you can customize them using the Web Assistant as well. (Just click the Customize button, which is at the top of every page.)

For more information on using Direct to Web, see the documentation on the Apple website.

### WebObjects Builder Changes

In Releases 3.0 and 3.1, WebObjects Builder was the central tool for WebObjects development; however, many preferred to use Component Editor. In Release 3.5, WebObjects Builder has been redesigned and rewritten so that it has become a much more useful tool for all WebObjects developers -- from the HTML and WOF novice to the expert.

__NOTE:__ Palettes created in WebObjects 3.1 or earlier are incompatible with WebObjects Builder 3.5 because the underlying mechanism that WebObjects builder uses to store the HTML and bindings has changed.

The major changes to WebObjects Builder are:

- Project management

  WebObjects Builder now only edits components, not the entire project. You use Project Builder to perform project management tasks, such as creating new projects and adding resource files.
- Script editing

  You use Project Builder to edit all source code files, including component script files. You use WebObjects Builder to create the component's interface (HTML) and to bind it to the variables and methods in the code. You can still use WebObjects Builder to add variables and methods to a component's source code, but when you want to implement a method, you now do so in Project Builder.
- HTML preservation
  - WebObjects Builder can now create components that represent page fragments (that is, components that do not contain <HTML> or <BODY> tags). To create a page fragment, go to the page inspector and choose "Page Fragment" in the pop-up list.
  - You can now edit a component's HTML and wod files in plain text form. The leftmost button on WebObjects Builder's toolbar allows you to choose between source ("raw") mode editing and graphical (WYSIWYG) mode editing. (You can also edit the HTML and wod files directly in Project Builder.)
- WYSIWYG editing
  - WebObjects Builder WYSIWYG HTML editing is faster and more accurate to the HTML 3.2 specification.
  - The basic HTML and WebObjects elements have been moved from the palette to the toolbar. Place the cursor where you want the element, and then click its toolbar button. You can also wrap an element around existing text by selecting the area you want to wrap and then clicking the element's toolbar button.
  - In the graphical display, dynamic elements are denoted with a blue triangle in the top left corner to distinguish them from their static HTML counterparts. In this way, you can easily differentiate between a static text element and a WOTextField dynamic element, for example.
  - Dynamic elements that can contain HTML or other WebObjects now have the ability to expand and contract. Double-clicking toggles between expanding and contracting the element.
- Bindings

  To bind an element, drag from the variable or method in the object browser to the element in the HTML view. This opens the inspector, from which you select the attribute that you want to bind to. (This method of binding is similar to making connections in Interface Builder.) You no longer double-click in the object browser to make bindings.
- Inspector

  The icon path in the inspector has been improved. There is now only one icon per element. You choose between the static or dynamic inspector using a pop-up list. You can also use the inspector to convert a dynamic element to its static counterpart or vice versa.
- Database Wizard

  The Database Wizard has moved from WebObjects Builder to Project Builder. When you create a new WebObjectsApplication project or a new component, you have the option of using the wizard.

### Project Builder Changes

WebObjects Release 3.5 replaces the OpenStep 4.2 version of Project Builder with a Project Builder that has been enhanced to improve the WebObjects development experience. This new Project Builder is more tightly integrated with WebObjects Builder.

__NOTE:__ In Release 3.0 and 3.1, you needed to load a bundle called __WebObjectsSupport.bundle__ into Project Builder. This bundle is no longer necessary. When you uninstall WebObjects, __WebObjectsSupport.bundle__ is removed from your system, and it is not added back by the WebObjects 3.5 installation. When you open Project Builder, you'll receive an error message to this effect. Go to the Bundles view in the Preferences panel and remove __WebObjectsSupport.bundle__.

In addition to tighter integration with WebObjects Builder, Project Builder has these other improvements:

- Building applications

  In WebObjects 3.0 and 3.1, WebObjects application project directories had a __.woa__ extension. No distinction was made between the project directory and the end-result WebObjects application directory. When you built a compiled WebObjects application in Project Builder, it put the executable file directly into the project directory.

  In WebObjects 3.5, there is a difference between the project directory and the application directory. You create a project in Project Builder and name it _ApplicationName_ with no extension. When you build the project, the result is a directory named _ApplicationName___.woa__ containing the application executable and all necessary resources. (This model is similar to how you create OpenStep applications.)

  You can see this change by looking at the WebObjects examples distributed with Release 3.5. Look in ___<DocRoot>_/WebObjects/Examples/WebScript__. (WebObjects example applications are now divided by language.) Each example is in a directory that has no extension (__HelloWorld__). If you look inside the directory, you see __HelloWorld.woa__, which contains the application executable.

  For more information on changes to the __.woa__ directory, see the section "[Improved Deployment Experience](#apple-jfwxa4tpozswirdfobwg66lnmvxhi)" in this document.
- More Wizards

  When you create a new WebObjects project or a new component inside of a WebObjects project, a wizard launches. This wizard makes it easy for you to specify the programming language, and if you're writing an application with database access, it launches the Database Wizard or Direct to Web to help you. (Direct to Web is a new feature in 3.5 and is described earlier in this document.)
- New "suitcases"

  WebObjectsApplication projects contain these new "suitcases:"

  **Web Components**
  : For components (__.wo__)

  **WebServer Resources**
  : For resources (such as GIFs) that must reside under the web server's document root
- Component Editing

  You can now navigate inside component directories and edit individual component files in Project Builder. Component files are now indexed, and project-wide search and replace operates on component files.

  For Java components, the __.java__ file now lives outside of the component directory. When you create a component, you are prompted to choose the source code language (Java, Objective-C, or WebScript). If you choose Java, the __.java__ file is added to the Classes suitcase. WebScript files still reside in the component directory.
- New project types

  Project Builder contains these new project types:

  **WebObjects Framework**
  : Used mainly to create a framework of shared components, as described later in "[Shared Components and Resources](#apple-knugc4tfmrbw63lqn5xgk3tuom)."

  **WebObjects Subproject**
  : Used within WebObjectsApplication and WebObjects Framework projects.

  **Java Wrapper**
  : Used to wrap Objective-C API in Java class files.

  **JavaPackage**
  : Used to create a Java package of classes.
- New Java subprojects

  Each WebObjects project comes with two subprojects named ClientSideJava and CommonJava. Use ClientSideJava to create client-side components. Use CommonJava to create Java classes for use both on the server and the client. These subprojects have appropriate settings for certain variables in __Makefile.preamble__ so that all client-side Java classes end up under the document root and all common (both server and client) Java classes end up in both the document root and in the application's directory.

  When you create a WebObjects project, the ClientSideJava and CommonJava subprojects are created and placed in the project directory, but they are not added to the project. If you want to use them, add them to the Subprojects suitcase of your project.

### Changes to Launching Applications

In WebObjects 3.0 and 3.1, launching an application was a two step process. First, you had to type a command line to launch the application itself. Then, you had to go to the web browser and type a URL.

WebObjects 3.5 has made launching an application much simpler:

- By default in WebObjects 3.5, launching an application automatically opens the application in the web browser. You no longer need to enter the URL.
- When you're debugging an application, you can launch it from Project Builder's launch panel. Just open the launch panel and click the launch button. Project Builder launches the application with the appropriate command and opens the web browser for you.
- On Windows NT, to launch a WebObjects application, simply navigate to its executable file in the File Explorer, and double-click its icon.
- On all other platforms, you can launch most applications by opening a command shell window, going to the application's directory, and typing the application command with no arguments. The document root and application path are now optional arguments.

  For example, to launch the DodgeDemo example on Mach in WebObjects 3.1, you had to type these commands:

  ```
  % cd /NextLibrary/WebServer/htdocs/WebObjects/Examples/DodgeDemo.woa
  % DodgeDemo -d /NextLibrary/WebServer/htdocs Examples/DodgeDemo
  ```

  In 3.5, you can shorten the command to this:

  ```
  % cd /NextLibrary/WebServer/htdocs/WebObjects/Examples/ObjectiveC/DodgeDemo/DodgeDemo.woa
  % DodgeDemo
  ```

#### Launching Applications in Symbolically Linked Directories

As stated previously, you can now launch most applications without specifying arguments. However, if the application is symbolically linked into the document root, instead of physically under the document root, you must supply an argument so that the application name can be determined correctly. Symbolic links resolve to a path that doesn't appear to be under the document root.
Your application may appear to operate normally, but images won't load because they won't be found.

For example, all example applications on Solaris and HP-UX have this problem because the examples directory is a symbolic link to __/NextLibrary/WODocumentRoot__. To launch the DodgeDemo example on Solaris or HP-UX, you must specify the application name, just like you did in WebObjects 3.0:

```shell
% cd /NextLibrary/WebServer/htdocs/WebObjects/Examples/ObjectiveC/DodgeDemo/DodgeDemo.woa
% DodgeDemo Examples/ObjectiveC/DodgeDemo
```

Note that you only have to give the path to the project directory, not the path to the __.woa__ directory inside of the project directory. For the reason behind this, see "[The Debugging Shortcut](#apple-irswe5lhm5uw4z2tnbxxe5ddov2a)."

### Converting Projects

Because of the changes made to Project Builder and WebObjects Builder, you need to convert existing projects to the 3.5 style of project. Project Builder does much of the conversion for you.

__NOTE:__ Before you begin, you probably want to remove the __.woa__ extension from the project directory and back up that directory.

#### Converting Existing 3.0 Projects to 3.5 Projects

After you install WebObjects 3.5, when you open an existing project in Project Builder, Project Builder automatically converts it to a 3.5 project for you. The conversion utility looks at the extension of each file in the project and moves the file to a new suitcase if necessary. If a file extension is not recognized, you'll be prompted to manually assign the file with that extension to the appropriate suitcase.

Here's a summary of what the conversion does:

**__WOProject.plist__**
: __WOProject.plist__ is obsolete, so it is deleted.

**Components (__.wo__ extension)**
: All __.wo__ components are moved from the Interfaces suitcase to the WebComponents suitcase. It was common to have components that your application needs in the project directory but not add them to the project itself because doing so was unnecessary. In WebObjects 3.5, it is necessary for all components to be part of the project so that they will be copied into the __.woa__ directory during project builds. For this reason, the conversion utility adds to the WebComponents suitcase all components that physically reside in the project directory but are not part of the project itself.

**Java files (__.java__ extension)**
: If any component has a __.java__ file in it, it is moved out of the __.wo__ directory to the __.wo__'s parent directory and is added to the Classes suitcase of the project (or subproject if the __.wo__ is in a subproject).

__NOTE:__ Because the physical location of the __.java__ file changed, your revision control system will most likely be affected.

**Java subprojects**
: If your project has Java files, you'll be asked if you want the ClientSideJava and CommonJava subprojects in your project. If you respond with Yes, you'll be able to add all client-side Java classes to the ClientSideJava subproject and all classes intended for both the client and the server to the CommonJava subproject.

**Resource files**
: The Other Resources suitcase is replaced with two suitcases: WebServer Resources and Resources. Images with known extensions are moved into the WebServer Resources suitcase. All other resource files are placed in the Resources suitcase.

**__Makefile.preamble__**
: Several new make variables have been added. These new variables are appended to your existing __Makefile.preamble__ with the default values assigned.

**Subprojects**
: Subprojects are recursively converted using the same conversions described above.

#### Converting WebScript-Only Projects to 3.5

The conversion described in the previous section only takes place for directories that contain a __PB.project__ file. In WebObjects 3.0 and 3.1, applications written entirely in WebScript did not require the use of Project Builder, and so they do not have a __PB.project__ file. In this case, you should create a new project in Project Builder of type WebObjectsApplication and add files to the project manually. Use the list above as a guide.

## Improved Deployment

To improve deployment, the following changes were made in WebObjects 3.5:

- The "split install" has been automated through Project Builder.
- Resource management has been improved.
- Monitor has become a supported application.
- You can set up applications so that they shut down (recycle) periodically.
- Application record/playback for scalability testing is supported.
- A new component, WOStats, displays application statistics while an application runs.

To learn more about deployment features, see the online book _[Serving WebObjects](../ServingWebObjects/ServingWebObjectsTOC.md)_.

### Installing a WebObjects Application

The directory _NeXT_ROOT___/NextLibrary/WOApps__ was introduced in WebObjects 3.0 as a secure place to store your WebObjects applications so that scripts weren't accessible through the document root. Installing an application in the __WOApps__ directory was a cumbersome process; you had to place the entire application directory in __WOApps__ and then you had to make a "sparse" copy of the directory in the web server's document root so that the web server would be able to find image files and other web server resources.

In WebObjects 3.5, this split install process is automated in Project Builder. To install a WebObjects application (including entirely scripted applications):

1. If your project contains web server resources, go to the __Makefile.preamble__ file under Supporting Files. Uncomment the line that defines this macro:

   `INSTALLDIR_WEBSERVER`
2. Open the Project Build panel.
3. Click the checkmark button to open the Build Options panel.
4. Choose __install__ as the build target.
5. Click the Build button.

Project Builder builds your application project and then installs it, placing the appropriate directories in _NeXT_ROOT___/NextLibrary/WOApps__ and in the document root. (For more details, read the next section.)

To get the proper format and placement of the __.woa__ directory, you should build even entirely scripted applications at least once. Scripted applications contain a file with a __main__ function identical to the __main__ in __WODefaultApp__. For this reason in WebObjects 3.5, scripted applications often have their own executable and don't need to rely on __WODefaultApp__.

### Resource Management Changes

A WebObjects application now contains standard directories to store application resources.
A deployed WebObjects application has the following directories:

```
NeXT_ROOT/NextLibrary/WOApps/MyApp.woa/
    MyApp[.exe]
    Resources/
    WebServerResources/

<DocRoot>/WebObjects/MyApp.woa/
    WebServerResources/
```

The __Resources__ directory contains the component directories, the application and session script files (if any), and any other resource files that an application might need access to (for example, plists or model files). The __WebServerResources__ directory contains resources that both the application and the HTTP server might need access to, such as image files that should be displayed in the browser. (In Project Builder, you place all web server resources in the WebServer Resources suitcase, and Project Builder places them in the __WebServerResources__ directory during a build.)

#### Shared Components and Resources

In WebObjects 3.0, to share a component or a resource file between applications, you had to copy that file into each application where you wanted to use it.

To improve sharing of components and resources, WebObjects 3.5 introduces the WebObjects Framework project type. WebObjects Framework builds a framework in which you can store components (or any other type of resource) to be shared across applications.

A WebObjects framework typically has the following directories:

```
NeXTROOT/NextLibrary/Frameworks/MyFramework.framework/
    Resources/
    WebServerResources/

<DocRoot>/WebObjects/Frameworks/MyFramework.framework/
    WebServerResources/
```

As with WebObjects applications, the __Resources__ directory contains the component directories and any other resource files that the framework needs to access. The __WebServerResources__ directory contains resources that both the framework and the HTTP server might need access to, such as image files that should be displayed in the browser.

#### The Debugging Shortcut

When you're in development mode, you typically do not have an application installed in _NeXT_ROOT___/NextLibrary/WOApps__. Instead you have a project directory under the document root, and the built __.woa__ directory is inside that project directory. As a convenience for debugging, WebObjects looks one level up from the __.woa__ directory to see if the directory is inside of a project directory. If it is, the components and resources from the project directory are used instead of the resources inside the __Resources__ and __WebServerResources__ directories of the __.woa__ directory. This way, you can edit scripts or replace images and other resource files in the project and not have to rebuild the application to see the changes.

#### Image File Location

In WebObjects 3.0, when you wanted a component to have access to an image, you placed the image file inside of the component directory. In WebObjects 3.5, this practice is supported for backwards compatibility, but its use is deprecated. Instead, you should place image files in the WebServer Resources suitcase in Project Builder.

Two new attributes have been added to certain dynamic elements (for example, WOImage and WOActiveImage) to support this new location for image files:

**__filename__**
: The image's file name including its extension. In reality, this is the path to the image relative to the application's __WebServerResources__ directory.

**__framework__**
: The __framework__ attribute supports shared images stored in a framework. If the image is in a framework, you set the __framework__ attribute to that framework's name (minus the __.framework__ extension).

You can also place components in a framework and have them access image files stored in the application. To do this, you set the WOImage's __framework__ attribute to __"app"__.

You only use this attribute if the component and the image are in two separate locations. For example, if both the component and the image are in the same framework, you don't need this attribute. However, if the component is in framework A and the image is in framework B, you would need this attribute (set as __framework = "B"__).

For more information, see the descriptions of WOImage and WOActiveImage in the _Dynamic Elements Reference_.

#### Accessing Resources Programmatically

You used to access resources using methods in WOApplication and WOComponent. These methods are still supported, but their use is discouraged. Instead, you retrieve resources using the new WOResourceManager class. For more information, see the WOResourceManager class specification in the _WebObjects Reference_.

### The Monitor Application

The Monitor application, which is used to deploy WebObjects applications and monitor their performance, was distributed as an example in WebObjects 3.0 and 3.1. It is now a fully supported application. This application makes it easy to maintain the __WebObjects.conf__ file, particularly if you are load-balancing applications.

The example version of Monitor came with a special subclass of WOApplication that you needed to use in all WebObjects applications you wanted to monitor. In Release 3.5, all of the API in Monitor's subclass of WOApplication has been added to WOApplication, so the recompile is no longer necessary. However, the 3.5 Monitor API is incompatible with the previous version. If you used the previous version of Monitor, you need to recompile all of your applications to use the 3.5 version of WOApplication.

For more information on using Monitor to deploy applications, see the online book _Serving WebObjects_.

### Automatic Application Shutdown

In WebObjects 3.5, applications can automatically shut themselves down. These new methods have been added to the WOApplication class:

**__terminateAfterTimeInterval:__

******
: The application shuts down after the specific time interval (in seconds) has elapsed. All currently active sessions are abruptly terminated.

**__setMinimumActiveSessionsCount:__

******
: Sets the minimum number of active sessions. If the number of active sessions falls below this minimum, the application may terminate.

**__refuseNewSessions:__**
: Sets whether the application should refuse any requests to create new sessions. If the application refuses to create new sessions and the active session count falls below the minimum, the application shuts itself down. In this way, you can gracefully shut the application down without affecting any of your users (or affecting the smallest possible number of users).

The Monitor application also contains UI that you can use to set the application to shut itself down either abruptly or by refusing new sessions. You can also schedule the application to shut itself down daily, weekly, or after a given number of hours.

In addition, Monitor contains an Autorecover button for each application instance. If this button is enabled, Monitor automatically restarts the application instance after it shuts down. Using a combination of __refuseNewSessions:__ and Autorecover, sets of application instances can periodically recycle themselves, thereby maintaining high performance even for applications with memory leaks.

### Scalability Testing

WebObjects 3.0 and 3.1 included a recording and playback example that could be used to perform scalability testing. In WebObjects 3.5, recording and playback scalability testing has become a supported feature. The recording adaptor is installed as __NextLibrary/WOAdaptors/CGI-Recording__. The playback tool is installed in __NextLibrary/Executables/WOPlayback__. For more information on how to use these tools, see the online book _Serving WebObjects_.

### Deployment Statistics

In WebObjects 3.5, all applications keep statistics about themselves, such as the number of active sessions, the total number of sessions created, the startup time, the number of transactions processed, and so on. You can access these statistics in a couple of different ways:

- Through the Monitor application
- Through the WOStats component

  WOStats is a new component shared among all WebObjects applications. It displays a table of application statistics. You access WOStats by typing in its URL:

  ```
      http://localhost/cgi-bin/WebObjects/MyApp.woa/-/WOStats
  ```
- Through the WOStatisticsStore object

  WOStatisticsStore is a new class in the WebObjects framework. It keeps track of all of the statistics you see on the WOStats page. You can use WOStatisticsStore if you want access to application statistics programmatically.

  In particular, you can use WOStatisticsStore to archive your application's statistics in Common Log File Format (CLFF). To do so, send the message __setLogFile:rotationFrequencyInDays:__ to the WOStatisticsStore object. When you do so, at the end of each request-response loop, the response component's __descriptionForResponse:inContext:__ method is invoked. By default, this method just records the name of the component, but you can override it if you want to provide more information. For example, you might want to record the values of component variables as well as the component name.

__NOTE:__ If you have overridden __createSession__ in any of your WebObjects applications, those applications will not have the WOStatistics or application shutdown features properly implemented. You'll need to change your implementation of __createSession__. For more information, see the WebObjects Release Notes available through [NeXTanswers #2455](http://enterprise.apple.com/NeXTanswers/HTMLFiles/2455.htmld/2455.html).

## Improved Java Support

In WebObjects 3.5, Java support improved in these ways:

- WebObjects 3.5 supports JDK 1.1.3, which is installed with WebObjects.
- More Objective-C API is available in Java. In particular, the entire Enterprise Objects access and control layers are available as Java classes and interfaces. In the WebObjects Framework, WOAssociation and WOAdaptor are now available in Java.
- When you build Java code in Project Builder, the top pane of the Build panel can now take you to the location of some errors, just as it can with Objective-C code.
- Project Builder contains the JavaWrapper and JavaPackage project types. You use JavaWrapper to wrap Objective-C classes in Java and JavaPackage to create a traditional package of Java classes.
- You can now mix Java, Objective-C, and WebScript more easily because the Java VM is automatically loaded by all WebObjects applications that need it. In particular, you can instantiate Java classes from WebScript code using a statement like this:

  ```
      id myVar = [MyJavaClass new];
  ```
- EOModeler can now generate template code for Java enterprise object classes.
- Java support is available on the Windows NT and Solaris platforms.

### Changes to Client-Side Java Components

WebObjects 3.5 supports Java archive (__.jar__) files through modifications to projects and to the WOApplet dynamic element. As stated previously, all WebObjects projects can include the subprojects ClientSideJava and CommonJava for client and server-side Java classes. When you build a project that has these subprojects, Project Builder creates a __.jar__ file suitable for downloading onto the client.
In addition, WOApplet has been modified to support __.jar__ files. It contains these new attributes:

**__archive__**
: Use this attribute for archive files that you have generated outside of a WebObjects application or framework. The value for this attribute is appended to the __archiveNames__ attribute value.

**__archiveNames__**
: Use this attribute for archive files that are built as part of a WebObjects application or framework project.

**__agcArchive__**
: The archive file containing the AppletGroupController class (similar to the __archive__ attribute).

**__agcArchiveNames__**
: Similar to __archiveNames__, but the archive contains the AppletGroupController class.

If you want to use these attributes, you should be aware of the following limitations:

- Only the latest browsers support __.jar__ files, so you should always specify both the __codebase__ attribute and the __archive__ attribute.
- At the time of this writing, most browsers only accept one archive file in the __archive__ attribute of the APPLET tag (which corresponds to the __archive__ attribute of WOApplet)
- In Netscape Navigator 4, when two applets on the same page are trying to communicate using an interface class (as is the case with client-side components), the interface class must be found in the same __.jar__ file on the client and the server.

Because of these limitations, the following is the recommended way to use __.jar__ files with client-side components:

1. Create one __.jar__ file, _X___.jar__, that contains:
   - Your Java client-side classes
   - The __next.wo.client__ package
   - Any third party packages you are using
2. Include the binding __archive="___X___.jar"__ in _all_ the WOApplets on the page.
3. Include the binding __agcArchive="___X___.jar"__ in _one_ of the WOApplets on the page.

This ensures that all the classes needed by both your applets and the AppletGroupController will be found in the __.jar__ file. Incidentally, this is also how you will get maximum performance out of __.jar__ files.

The prepackaged client-side component classes that were distributed with WebObjects 3.0 are now available as a __.jar__ file named __WOExtensions.jar__. This __.jar__ file is in the WOExtensions framework, which is described below.

## Other Major Changes

In addition to the improvements to development tools, deployment, and Java support, the following changes have been made in WebObjects 3.5.

### WOExtensions Framework

A new framework of dynamic elements and shared components, the WOExtensions framework, is distributed with WebObjects 3.5. This framework contains the client-side components distributed with WebObjects, the WOStats component described previously, plus other dynamic elements and components that are ready to use in your application. You can freely access all of these through palettes in WebObjects Builder. For more information, see the [_WOExtensions Reference_](../Reference/DynamicElements/WOExtensionsTOC.md).

### Enterprise Objects Framework Changes

An updated version of Enterprise Objects Framework is distributed with WebObjects 3.5 on all platforms. Enterprise Objects Framework contains these new features:

- The Enterprise Objects Framework access and control layers are available in Java.
- EOModeler can now generate template code for Java enterprise object classes.
- EOModeler reverse engineering incorporates more schema information from your database into newly created models.
- You can now create relationships in EOModeler's diagram view by Control-dragging similar to the way connections are made in Interface Builder.
- Dragging a to-many relationship from EOModeler to WebObjects Builder creates a detail display group.
- Enterprise Objects Framework now caches to-many array faults, which can greatly reduce faulting and thus improve performance.
- A new qualifier operator, __caseInsensitiveLike__, is supported for case-insensitive comparisons.

### WebObjects Framework Changes

In addition to the new classes WOResourceManager and WOStatisticsStore mentioned previously, the WebObjects framework in Release 3.5 contains these changes:

- WebScript is now "type-tolerant," meaning that you can specify the type of a variable, a method, or a method argument, and WebScript will not produce an error message:

  ```
  NSString *myString;
  - (MyEntity *)returnAnEntityMethodWithArgument:(NSNumber *)aNumber { ... }
  ```

  The purpose of this feature is to allow WebObjects Builder to make more intelligent assumptions when you bind variables and methods to a component. WebScript does not perform type checking; it just passes the information along to WebObjects Builder.
- The way you set up queries in WODisplayGroup has changed. API such as __executeQuery__ and __inputObjectForQualifier:__ is deprecated. Instead, you build a qualifier using three dictionaries: __queryMax__, __queryMin__, and __queryMatch__. WODisplayGroup also has master-detail support added to it. For more information, see the WODisplayGroup class specification.
- A new dynamic element, WOImageButton, has been added to provide image map support in a form. Instead of using WOActiveImage inside of a form, you use WOImageButton. The APIs are the same for both dynamic elements.

### New Documentation

All of the WebObjects documentation has been updated for 3.5. Most of the documentation is installed on your system when you install WebObjects. In particular, look for these noteworthy changes:

- The reference for the Enterprise Objects and Foundation frameworks is now distributed in HTML format instead of RTF or Windows Help. You can access this reference material both through the WebObjects Home Page and through Project Builder.
- The WebObjects class reference is now accessible through Project Builder as well as through the WebObjects Home Page.
- The _Post-Install Instructions_ now contain a troubleshooting guide to help you verify that your installation was successful.
- _Getting Started With WebObjects_ has been modified to show you how to write Java applications using Project Builder and WebObjects Builder, as well as how to write WebScript.
- Coverage of Java programming in the _WebObjects Developer's Guide_ has been improved. In addition, this book now contains a new chapter "Deployment and Performance" that describes how to put the finishing touches on a WebObjects application and how to improve performance.
- The online book _Serving WebObjects_ has been updated to include how to perform various tasks using the Monitor application. It also has a new section named "Improving Performance" that provides tips for non-programmatic ways of improving performance.

As stated previously, most 3.5 documentation is available on your system. However, the following pieces of documentation are currently being written. When they are completed, they will be made available through the Apple website. (You can click the "Updated Documentation at Apple" link in the left frame of the WebObjects Home Page to see if they are available.)

- Enterprise Objects Framework reference in Java
- Direct to Web documentation
- More complete documentation for WebObjects Builder and Project Builder (titled _WebObjects Tools and Techniques_)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
