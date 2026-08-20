---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/UsingExtensionBuilder/UsingExtensionBuilder.html
archived_at: '2026-07-27T06:57:07.586060Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Accessing%20Resources%20Within%20Your%20Extension%20Folder.md)[Previous](Extensions%20Overview.md)

# Using Extension Builder

You can use Safari’s Extension Builder tool to build, install, reload, and uninstall extensions.

## Before You Begin

Before you can build and install an extension, you need to install a developer certificate. For more information, see [Developer Certificates](Extensions%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjvfvjvomrw).

## Opening Extension Builder

To access Extension Builder, first enable the Safari developer tools by clicking "Show Develop menu in menu bar" in the Advanced pane of Safari preferences, as shown in Figure 2-1. (To learn more about the Safari developer tools, see _[Safari Web Inspector Guide](../Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_).

__Figure 2-1__  Enabling the developer tools

（原归档配图未能恢复：`EnableDeveloperTools.png`）

Next, choose Show Extension Builder from the Develop menu. If no previous work has been done in Extension Builder, the Extension Builder window is largely empty except for the + button. Don’t worry; that’s normal.

## The Extension Builder Interface

Click the + button to create a new folder to hold your extension. You are prompted to either Add Extension (choose an existing extension folder) or create a New Extension. Choose New Extension. You’re prompted to give the folder a name and location. The folder is created with the `.safariextension` extension.

A generic extension icon is displayed with a label derived from your folder name. Add your extension’s HTML, CSS, JavaScript, and media files to this folder. If you include an `Icon.png` or `Icon-64.png` file, the icon changes to show it, otherwise the icon remains generic. Your certificate information is also displayed. The information is shown in the format: `Safari Developer: (Developer ID) email@address`.

Click your extension’s icon to bring up the main Extension Builder interface, as shown in Figure 2-2.

__Figure 2-2__  Extension Builder interface

（原归档配图未能恢复：`ExtensionBuilderInterface.png`）

At the top of the window is your extension’s icon, title, the name of the extension folder, and your developer ID. The following interactive fields are displayed below:

- Display Name—The visible name of your extension. _Required_.
- Author—Your name or your company name.
- Description—A brief description of what your extension does.
- Website—The website that users should visit for information and support.
- Bundle Identifier—The bundle identifier that identifies your Safari extension. OS X bundle identifiers are alphanumeric strings in reverse DNS format. Use your type of organization (com, gov, edu, org, and so on), your company name, and the extension name, separated by dots. For example, `com.MyCompany.myExtension`. _Required_.
- Companion Bundle Identifier—The bundle identifier that identifies an OS X app that your extension can communicate with. OS X bundle identifiers are alphanumeric strings in reverse DNS format. Use your type of organization (com, gov, edu, org, and so on), your company name, and the extension name, separated by dots. For example, `com.MyCompany.myCompanionExtension`. For more information, see [Communicating with your OS X App](Communicating%20with%20your%20OS%20X%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrtfvjvona).
- Update Manifest—The URL to use when checking for available updates. For more information, see [Updating Extensions](Updating%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjsfvjvomi).
- Display Version—The displayed version number for your extension. _Required_.
- Bundle Version—The internal version number used by the operating system. One or more digits with period separators, such as 1 or 4.1.1. This is the version number Safari uses when checking for updates. _Required_.
- Website Access Level—Use this field to restrict your extension’s access to external websites. Your choices are as follows:

  - None—Your extension cannot access webpages by injecting scripts or style sheets.
  - Some—Your extension has access to webpages specified in the Allowed Domains field. If this field is left blank, your extension has no website access.
  - All—Your extension can access webpages from any domain.

  If you choose Some or All, you can further choose to allow your extension access to secure sites (HTTPS URLs) or not, as shown in Figure 2-3.

  __Figure 2-3__  Access restrictions

  （原归档配图未能恢复：`AccessRestrictions.jpg`）

  When listing domains and pages your extension is allowed to access, you can use the asterisk as a wildcard character. For more information on access and permissions, see [Access and Permissions](Access%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqobnknltc).
- Content Blocker File—A file containing rules to block cookies, images, resources, pop-ups, and other content. For more information, see [Using Your Extension to Block Content](Using%20Your%20Extension%20to%20Block%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrufvjvona).
- Global Page File—A page loaded once, when Safari loads your extension. This page is not displayed. It is intended for JavaScript functions that handle response to commands, messages, and other events.
- Database Quota—The space you want to allocate for HTML5 client-side database storage for your extension. For more information, see [Settings and Local Storage](Settings%20and%20Local%20Storage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjrfvjvomi).
- Bars—An extension bar is space below the bookmarks bar and above the tab bar reserved for your extension. If you want to display persistent data in the browser frame, create an extension bar. Add an HTML file to your extension folder as the source for your extension bar and click New Bar, then choose the file from the pop-up menu. You are prompted to enter a label to identify your bar in the View menu. For more information, see [Adding Extension Bars](Adding%20Extension%20Bars.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnjnknlte).
- Context Menu Items—Items your extension adds to contextual menus. Click New Context Menu Item to add an item. The interface expands to allow you to enter a title, identifier, and command for each context menu item. For more information, see [Adding Contextual Menu Items](Adding%20Contextual%20Menu%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnbnknltc).
- Toolbar Items—Buttons you are adding to the main Safari toolbar (_not_ an extension bar). Click New Toolbar Item and you are prompted to enter a label, palette label, tooltip, image file, identifier, and command. The code that listens for the button click and executes the command goes in either your global HTML page or an extension bar. For details, see [Adding Buttons to the Main Safari Toolbar](Adding%20Buttons%20to%20the%20Main%20Safari%20Toolbar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmznknltc).
- Menus—Pop-up menus you associate with a toolbar item you have created.
- Popovers—Pop-up windows containing HTML content that you associate with a toolbar item you have created.
- Start Scripts—Scripts to execute before a webpage is interpreted, usually a script that blocks unwanted content.
- End Scripts—Scripts to execute when the page load event occurs (roughly when a function specified in the body `onload` attribute would execute). Most scripts are End Scripts.

  For more information, see [Injecting Scripts](Injecting%20Scripts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnrnknltc).
- Style Sheets—User style sheets to apply to browser content. For more information, see [Injecting Styles](Injecting%20Styles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnznknltc).
- Whitelist—When injecting scripts or style sheets, only URLs specified in the whitelist are affected. If no whitelist is specified, all URLs are on the whitelist.
- Blacklist—When injecting scripts or style sheets, any URLs specified on the blacklist are skipped (scripts and style sheets are not injected).

  Add URLs to the whitelist or blacklist by clicking New URL Pattern.

  A URL pattern can include the `*` character to match any string. The `*` character can be used in any part of the `Domain` or `Path`, but not the `Scheme`.

  Examples:

  - `http://*/*`—matches all HTTP URLs.
  - `http://*.apple.com/*`—matches all webpages from apple.com.
  - `http://developer.apple.com/*`—matches all webpages from developer.apple.com.
  - `https://secure.A_BankForExample.com/accounts/*`—matches all webpages from the accounts directory of secure.A_BankForExample.com that are delivered over HTTPS.
  - `http://www.example.com/thepath/thepage.html`—matches one webpage.

  For more information, see [Access and Permissions](Access%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqobnknltc).
- Extension Settings—Persistent settings for your extension. Click New Settings Item to add a setting. Hidden settings are not displayed to the user. All other settings appear in a pane for your extension in Safari preferences. Each setting has a key (identifier), a type (such as a checkbox or text field), and an optional default value. For details, see [Settings and Local Storage](Settings%20and%20Local%20Storage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjrfvjvomi).

## Building a Simple Extension

In order to create an extension, you need a minimum of two files:

1. An Apple Developer certificate. For more information, see [Developer Certificates](Extensions%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjvfvjvomrw).
2. A resource file, such as an HTML page, script, or CSS file. To create an extension bar, you need an HTML file.

   As the resource file for this example, create an HTML page that displays "Hello World" and save it as `helloworld.html`. An example is shown in Listing 2-1.

__Listing 2-1__  helloworld.html

```
<!DOCTYPE html>
<html>
<head>
<title>Hello World</title>
</head>
<body>Hello World!</body>
</html>
```

Follow these steps to create an extension bar that displays "Hello World".

1. Click the + button in Extension Builder and choose New Extension. Extension Builder creates an empty folder with the extension `.safariextension` and prompts you for a name and location. Name the new extension folder HelloWorld and have Extension Builder put it in your Documents folder. A generic icon is displayed with the name HelloWorld.

   This brings up the main Extension Builder interface, as shown in [Figure 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrnknlti).
2. Put the `helloworld.html` file in the `HelloWorld.safariextension` folder.

   (You don’t use Extension Builder for this step—just drag the file into the folder.)
3. Click New Bar in Extension Builder, enter a label such as `Hello World`, and choose `helloworld.html`from the pop-up menu. This tells Extension Builder to use `helloworld.html` as the source file for a new extension bar. The label appears in the View menu.
4. Click the Install button. Extension Builder creates a compressed folder with the extension `.safariextz`. This is your extension package. The package is installed, and a new extension bar is added to your browser window that displays "Hello World," as illustrated in [Figure 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrnknlts).

   __Figure 2-4__  Hello World

   （原归档配图未能恢复：`helloworld.jpg`）

Notice that you can toggle the bar’s visibility by name in the View menu, and disable or enable the extension itself in the Extensions pane of Safari preferences. You can edit and save `helloworld.html` to experiment with it. Click Reload in Extension Builder to build and install the modified version.

[Next](Accessing%20Resources%20Within%20Your%20Extension%20Folder.md)[Previous](Extensions%20Overview.md)
