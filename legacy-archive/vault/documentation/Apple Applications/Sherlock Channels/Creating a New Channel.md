---
title: Sherlock Channels
apple_id: 10000121i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-04-09'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Sherlock/Tasks/CreatingChannels.html
archived_at: '2026-07-15T05:18:57.143193Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sherlock Channels](Introduction%20to%20Sherlock%20Channels.md)


[Next](Accessing%20Channels.md)[Previous](Sherlock%20Reference.md)

# Creating a New Channel

This article takes you through the steps for creating a simple channel that displays an interface and responds to user input. The goal is to get the channel up and running quickly so that you can see how the user interface and underlying script code interact. The channel in this article does not attempt to connect to the Internet or gather information.

Before you can begin developing Sherlock channels, you must make sure your system has the proper tools. Sherlock requires the developer tools available for Mac OS X 10.2 or later. In particular, you must have the Interface Builder application to design your channel’s interface. You must also have the Sherlock palette before you can add path information to the views and controls of your channel.

Install the developer tools for your system using either the Developer Tools CD that came with Mac OS X 10.2 or by downloading the tools from the developer section of Apple’s website. Once you have these tools installed, download the Sherlock SDK from the developer section of Apple’s website and install it. This SDK installs a Sherlock palette, documentation, and channel templates for you to use in creating channels.

The Sherlock SDK installs a Project Builder template you can use to create new Sherlock channels. This template implements a simple Internet channel that lets the user enter a search string and retrieve the results. You should use this template as the starting point for any new channels you want to create.

1. Launch Project Builder.
2. Select New Project from the File menu.
3. From the New Project window, select Sherlock Channel from the Standard Apple Plug-ins section.
4. Click Next.
5. Enter the name and location of your project.
6. Click Finish.

Your new project includes a channel configuration file, a main code file, a default icon, and a nib file with a predefined window. The project also includes a Read Me file with the latest instructions on how to modify and debug your channel. You should read these instructions before deploying your channel for testing.

When you are ready to test your channel, you need to post it to a web server and tell Sherlock to load it. The simplest way to do this is to enable Personal Web Sharing on your local machine and place your channel files in the Sites directory of an active user. You can then load the channel from a browser address line.

The following steps show you how to load the default channel project. If you added any files to the project, you may need to copy those files to the Sites folder along with the standard channel files that came with the project:

1. In the Sharing System Preference, enable Personal Web Sharing on your test machine.
2. Copy the `SherlockChannel.xml` and `Channel.icns` files and the `Channel` directory to the `Sites` directory of your user home directory.
3. Launch Safari.
4. In the browser address bar, enter the path to the `SherlockChannel.xml` file of your channel. For example, if you put your channel in local user Steve’s `Sites` directory, your URL might look like the following:

```
sherlock://localhost/~steve/SherlockChannel.xml
```

Entering the URL for your channel configuration file launches Sherlock and tells it to load your channel. However, the icon for your channel does not appear in the toolbar until you explicitly add it, either programmatically or from the Sherlock application.

To add a channel to the toolbar from the Sherlock application, you would simply select the Add Channel to Toolbar command from the Channel menu. To add your test channel to the toolbar programmatically, you would use the following URL instead of the one in the preceding step:

```
sherlock://localhost/~steve/SherlockChannel.xml?action=add
```

For more information on loading channels using the `sherlock` scheme, see [Accessing Channels](Accessing%20Channels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dolkcineusrckirbq).

Apple provides several tools to aid you in debugging your trigger code.

Developers can add the Channel Development Tools subscription to Sherlock to access some special channels: an XQuery code tester, a JavaScript code tester, an HTML View tool, and a XPath Finder tool. The XQuery and JavaScript code testers let you execute trigger code in a Sherlock environment and view the results. The HTML View tool lets you load and view an HTML page. The XPath Finder tool gives you the XQuery path to a specific HTML tag in a document.

To subscribe to the developer channels, go to the following URL from your browser. This URL will load the developer channels and add them to your current subscription list:

```
sherlock://si.info.apple.com/sherlock3s/
                    developerChannels.xml?action=subscribe
```


Sherlock includes support for runtime debugging of your channel using the Sherlock Debug menu. You enable this feature by launching Sherlock from the Terminal application in the following way:

1. Launch the Terminal application.
2. In your shell, set the environment variable `DEBUG_SHERLOCK_CHANNELS` to the value 1. For example, in the `tcsh` shell, you would use the following command:

```
setenv DEBUG_SHERLOCK_CHANNELS 1
```
3. Launch Sherlock from the command-line. You can do this by navigating to the directory containing the Sherlock application bundle and executing the following command:

```
./Sherlock.app/Contents/MacOS/Sherlock
```

Another way to enable the Debug menu is to modify the `SherlockDebug` preference in the system defaults database. When set to `1`, Sherlock displays the Debug menu; when set to `0`, Sherlock hides it. The following example shows you how to enable the Debug menu from Terminal:

```
defaults write com.apple.Sherlock SherlockDebug 1
```

Launching Sherlock with either of these options adds a Debug menu to the end of the Sherlock menu bar. This menu contains commands for reloading the channel and for examining both the data store and the view hierarchy.

The Data Store command displays a browser window with which you can navigate the data store variable space. Following the path hierarchies, you can examine the data currently being managed by your channel at a specific path. You can use this tool to validate the integrity of your channel’s data.

The Examine View Hierarchy command displays a window with an outline view that shows the object hierarchy of your channel’s views. Each object is identified by its type and by the current address of the object itself. This information is read-only and cannot be permanently changed.

[Next](Accessing%20Channels.md)[Previous](Sherlock%20Reference.md)

