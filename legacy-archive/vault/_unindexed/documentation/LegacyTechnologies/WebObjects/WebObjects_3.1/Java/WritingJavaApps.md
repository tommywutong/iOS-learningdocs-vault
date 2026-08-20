---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Java/WritingJavaApps.html
archived_at: '2026-07-15T07:49:23.664133Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](TOC.md)

## Writing WebObjects Applications in Java

The major elements of a WebObjects application are the page creation and customization logic that binds WebObject page elements to real objects. The WebObjects Java Extensions allow those "real objects" to be pure Java objects that embody custom logic and compute results for HTML display.

With the Java Extensions, instead of scripting you create Java subclasses of __next.wo.WebSession__ and __next.wo.WebApplication__, and build pages with subclasses of __next.wo.Component__. (Note that for this release, Java subclasses of __next.wo.WebSession__ and __next.wo.WebApplication__ must be placed in the __.woa__ directory, while Java subclasses of __next.wo.Component__ must live in the __.wo__ directory with which they are associated.) To start your application, then, you simply point the Java Virtual Machine to your compiled Java subclass of Application; everything else will be loaded on demand.

Often you may find yourself building logic inside custom objects whose persistent storage is managed by the Enterprise Objects Framework. The Java classes that make up the __next.eo__ package provide access to EOF. Use the Framework to manage your Java subclasses of __next.eo.CustomObject__. You can use EOModeler in conjunction with your Java objects: to name the class of the resulting object: simply provide the Java subclass name where appropriate, qualified by its package name (using slashes).

The WebObjects Java Extensions includes a Java package corresponding to each of the three key WebObjects Frameworks: Foundation, Enterprise Objects, and WebObjects. These packages are __next.util__, __next.eo__, and __next.wo__, respectively. See ["The Java Packages"](Packages.md#apple-kjcumnbuge3tk) for information on the contents of these three packages.

### Using WebObjects Builder

WebObjects Builder has been enhanced so that it can write a component's logic in Java. To do this, you must set your language preference to Java before you create a new application. Go to the preferences panel, and choose "Java" in the Languages display. After your preference is set to Java, WebObjects Builder creates __.java__ files where it used to create __.wos__ files (for example, Application.java, Session.java, and Main.java). It also checks your Java syntax for you when you try to save the component.

For more information on using WebObjects Builder, refer to the _WebObjects Developer's Guide_.

### Using Project Builder

To construct a WebObjects application using Java, you'll need to use Project Builder to manage the project. Project Builder understands __.java__ files and will allow you to install them in the Classes suitcase. Also, the Project Builder makefiles have been augmented so that they know how to compile __.java__ files. Because of this, you can simply build your Java project just as you would any other. For more information on using Project Builder to construct WebObjects applications, refer to "Compiling and Debugging a WebObjects Application" in the _WebObjects Developer's Guide_.

__Note:__ when using Project Builder to create WebObjects applications in Java, you must have the WebObjectsSupport bundle loaded. To load this bundle, start Project Builder, select Preferences from the Tools menu, and select Bundles from the pull-down list at the top of the Preferences panel. Click Add, and in the Open panel browse to __NextDeveloper/PBBundles__ (relative to _NEXT_ROOT_). Select __WebObjectsSupport.bundle__, and click Open.

#### Building an Existing Project

The DodgeDemoJava example is a fairly substantial WebObjects application written entirely in Java, and serves as an excellent model of how you'd design a typical application. This demo uses custom logic, written in Java, to compute car leases. To build and run the example, follow these steps:

1. Using the Windows NT Explorer, traverse to the __WebObjects/Examples/DodgeDemoJava.woa__ directory beneath your web server's document root and double-click the __PB.project__ file located there. Project Builder will launch, and the DodgeDemoJava application will be loaded.
2. Click the build icon to bring up the Project Build window. In the Project Build window, click the build icon. DodgeDemoJava will build.
3. Make sure that your web server is running.
4. Start your web browser. If your browser is running on the same machine on which your server is running, enter the following URL:

   ```
   http://localhost/cgi-bin/WebObjects/Examples/DodgeDemoJava
   ```

   Otherwise, simply substitute your server name (__myserver.next.com__, for example) for __localhost__ in the above URL.

The Java application should automatically start and make itself accessable through your browser. In the event that it doesn't start automatically, you can
start it manually from a Bourne shell by changing to the Java application's ".woa" directory beneath your web server's document root (__WebObjects/Examples/DodgeDemoJava.woa__, in the above example)
and typing the following (substituting the name of your application for "DodgeDemoJava", and the full path to your web server's document root for
_DOC_ROOT_):

```
./DodgeDemoJava.exe -d DOC_ROOT/ Examples/DodgeDemoJava
```

After you've started your application manually, you should be able to access it from your web browser as detailed in step 4, above.

#### Creating a New Project

The creation of a new WebObjects project is a two-step process. First, you create a new project using WebObjects Builder. Then, launch Project Builder and create a new WebObjects Application, specifying the __.woa__ directory created in the previous step as the Project Path. From this point on, you work on your project using Project Builder and WebObjects Builder as you normally would. Making the resulting project will produce an executable that can be launched like any other WebObjects application.

### Browsing Java Classes

The WebObjects Java Extensions includes a tool that allows you to easily browse through the contents of various Java classes (including Objective-C classes that have Java "wrappers"). This tool is located in __NextDemos\JavaBrowser.app__ (relative to _`NEXT_ROOT`_), and can be started simply by clicking on __JavaBrowser.exe__. Upon startup, you'll be able to browse any packages found in your CLASSPATH. If your
CLASSPATH environment variable isn't set, you can specify an explicit path
by selecting Preferences from the Class Browser's Tools menu, and editing the
contents of the "Startup Paths" text view.

Double-click package names to display the contents of the package. Double-click the name of a class to display its fields and methods. By default, the main browser window shows the "Interface View," which displays the interface for the selected class. If source code is available for the selected class, clicking the Source button (located at the bottom of the browser display) will bring up that source. Otherwise, you can get some idea of the inner workings of the class by clicking Decompile: the selected class will be "decompiled" and the results will be displayed in the browser's main window.

### Using Symantec Cafe with WebObjects Builder

Symantec Cafe may be the development environment of choice for WebObjects Java developers for several reasons:

- You have previous experience with Symantec Cafe, and aren't interested in learning how to use a new set of tools.
- You have a significant amount of Java business logic already organized in Symantec projects that would have to be integrated into WebObjects Java applications.

For some people, there may be some advantages to using Symantec Cafe instead of Project Builder:

- Symantec Cafe was designed expressly for building Java applications, and includes some useful tools not supplied with the WebObjects Java Extensions.
- The Symantec compiler is extremely fast when compared to the Sun compiler (note that you have the option to use the Cafe compiler with Project Builder, if this is your primary complaint).
- Symantec Cafe provides a better integrated environment, including a powerful link between the compiler and the editor (similar to Project Builder when used with the Objective-C compiler).

Symantec Cafe isn't for everyone, though:

- For users accustomed to Project Builder, it's a new tool to learn.
- Using Symantec Cafe may give you a false sense of confidence regarding the level of integration of the products. As an example, WebObjects Builder assumes that you won't edit the Java code in components, while Cafe allows you to do so.
- The debugger in release 1.51 of Symantec Cafe can't be used with WebObjects Java applications, since Symantec modifies Sun's VM for its debugger hooks.
- Autostart isn't automatic; you need to take extra steps in order to enable it.

#### Creating HelloWorldJava

The following procedure shows you how to use Symantec Cafe to create the "HelloWorldJava" application (it assumes that you have Symantec Cafe release 1.51 installed):

1. Launch WebObjects Builder, and select Java in the Language Preferences. Create a new application named "HelloWorld.woa". Create a Main page, with a variable __visitorName__ and an action __sayHello__. Create a Hello Page with a variable __visitorName__. Save the project.
   You needn't quit WebObjects Builder at this stage, but when you go back to it later, make sure you do a Revert to Saved on the project. If you close all component windows at this time, you'll need to click on Revert To Saved only if you modify Application.java or Session.java in Symantec Cafe.
2. Copy the ".exe" file from any example into your __.woa__ directory. Rename the executable "HelloWorld.exe". This copy and rename enables both autostart and a simple shell start of your application.
3. Launch Symantec Cafe. Create a new project, using Project Express, as follows:
   1. In the "Name project" panel, create a __HelloWorld.prj__ project. Symantec differs from Project Builder here in that it allows you to keep the project files together in the same directory (Cafe/Projects), while the Java files can be located anywhere you want.
   2. In the "Set project type" panel, set the Target Type to "Application".
   3. In the "Add files to project" panel, browse to your HelloWorld.woa directory and add the Application.java, Session.java, Main.wo/Main.java and Hello.wo/Hello.java files.
   4. In the "Initial settings" panel, enter your Classpath.
4. Drag the project icon out of the tool bar to display the project window. Right-clicking on the project name gives you a menu which allows you to modify the project setting (to provide start-up arguments) or edit the project (to add new files), among other features.
5. Select Project Setting and enter the following in the Compiler Output Directory field:

   ```
   PATH-TO-THE-APP/HelloWorld.woa/Java
   ```

   click Yes in the alert panel, confirming that you wish to create a new directory.
6. Click on Application.java, and add an initializer:

   ```
   public Application() {
       super();
       System.out.println("Welcome to HelloWorld Java");
   }
   ```
7. Click on Main.java, and complete the __sayHello__ method:

   ```
   public Component sayHello() throws Exception {
       Hello nextPage = ((Application)application()).pageWithName("Hello");
       nextPage.setVisitorName(visitorName);
       return (Component)nextPage;
   }
   ```
8. Click on Hello.java, and add a __setVisitorName__ method:

   ```
   public void setVisitorName(String aName) {
       visitorName= aName;
   }
   ```
9. Click the compile icon. If the compile fails, click on the failure line and the editor will position you at the offending line.
   - If you want to modify the application UI, go back to WebObjects Builder and do a Revert to Saved on the project to force it to reload the files. The scripts, variable lists and method lists should all be updated. You can add methods, variables, and so on and then do a save.

     Again, you needn't quit WebObjects Builder at this stage, but when you go back to it later, make sure you do a Revert to Saved on the project. The Revert to Saved is required only if you have modified Application.java or Session.java. If you closed all Component windows before leaving WebObjects Builder the previous time, they'll be automatically updated from disk when you reopen them.
   - After making your changes, go back to Symantec Cafe. It will notice the changes and pop up a panel suggesting that you reload the modified files.
10. Once everything compiles without error, you can either start your application from a shell, or you can simply allow it to autostart from your browser. If you did not copy the ".exe" file as instructed earlier in this procedure, you'll need to start the application from a shell by changing to the __.woa__ directory and entering the following:

    ```
    java -classpath $CLASSPATH JavaMain -d  Examples/HelloWorld
    ```

As was mentioned previously, when debugging your applications you're on your own. The Symantec debugger will crash shortly after you start it on your application (this problem will be addressed once Sun's VM 1.1 is officially released). For now, your best bet is to use System.out.println().

[!Table of Contents](TOC.md)
[!Next Section](AccessingObjectiveC.md)
