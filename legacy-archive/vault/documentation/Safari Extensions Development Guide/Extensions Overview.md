---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/ExtensionsOverview/ExtensionsOverview.html
archived_at: '2026-07-27T06:57:07.572341Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Using%20Extension%20Builder.md)[Previous](About%20Safari%20Extensions.md)

# Extensions Overview

Extensions are a way for you, as a developer, to add features to Safari. You write them using HTML, CSS, and JavaScript. Safari exposes additional methods and properties to JavaScript for extensions to use, allowing your extension to do things that scripts normally can’t.

## Developer Certificates

In Safari 9.0 on OS X 10.10 and 10.11, you can develop a Safari extension without creating a certificate. However, to distribute extensions for Safari, you first need to sign up for the Apple Developer Program online at [https://developer.apple.com](https://developer.apple.com). After joining the program, you must obtain a certificate in order for your extension to work; the extension will not load until your certificate is installed. To request a certificate, follow the "Certificates, IDs & Profiles" link from [your developer account](https://developer.apple.com/account/).

Install your certificate with the Keychain Access application. Select the "login" keychain. Then select "Import Items..." from the File menu. Choose your certificate file, verify that the "Destination Keychain" is set to "login", and click Open.

One certificate supports all your extensions. You can use the same certificate on more than one computer, as long as you also export the corresponding private key from the originating computer and import it into the new keychain on each new computer.

__Important:__ The private key and the certificate must match to be valid.

When your certificate nears expiration, create and download a new one from the Apple Developer website. Because the two certificates carry the same developer ID, your existing extensions will recognize the new certificate.

## What Your Extension Can Do

Safari extensions let you add persistent items to Safari, such as controls, local or web-based content, and scripts that modify web-based content.

- You can add buttons to the Safari toolbar.
- You can add menus and submenus to extension-defined toolbar buttons.
- You can add custom toolbars (extension bars).
- You can add items to Safari’s contextual menus.
- You can display HTML content in an extension bar, in a popover, or in its own tab, or inject the content into webpages.
- You can detect the availability of the Safari article reader, enter it programmatically, and inject scripts and style sheets into it.
- Your extension can run invisibly in the background.
- You can modify and reformat web content by applying scripts and style sheets.

  Your scripts and style sheets can be applied either universally or selectively, using whitelists and blacklists of URL patterns to determine which webpages they should be applied to.
- You can post notifications to Notification Center, OS X’s systemwide notification system, as you would from a webpage using HTML5 notifications. Your extension does not need explicit permission from the user. For more information, see [Sending Notifications](../Apple%20Applications/WebKit%20DOM%20Programming%20Topics/SendingNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytiobtfvbuqmrt).
- You can communicate securely with a native companion application.

__Note:__ An extension should be limited to a single purpose or service. Don’t create extensions with multiple unrelated behaviors, such as both injecting product ratings and reviews into product websites and injecting advertisements into webpages.

To see examples of Safari Extensions, visit the Safari Extensions Gallery ([https://extensions.apple.com/](https://extensions.apple.com/)).

## The Extension Parts List

An extension starts as a folder. Depending on what you want your extension to do, you put some or all of the following items into the folder:

- __Global HTML page__—An HTML page containing JavaScript support code for your extension. This page is never displayed, but it can contain HTML elements that are used by other parts of your extension. The global HTML page is loaded once, when the app launches or your extension is installed or enabled, and has access to the Safari app API. This is the right place to code buttons for the Safari toolbar, extension menus, or contextual menu items.
- __Content files__—HTML, CSS, and JavaScript content to display in extension bars, popovers, full-page tabs, or to inject into webpages by creating an [iframe](../Apple%20Applications/Safari%20HTML%20Reference/Supported%20HTML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi3delljmzzgc3lf).

  Popovers and extension bars have access to the Safari app-level API and can also contain code for toolbar items or menu items.

  Content files for tabs can be hosted on remote web servers but it is recommended that they reside in your extension package. Content files for popovers or extension bars _must_ reside in your extension package.
- __Injected scripts__—JavaScript files to be injected into browser content. These scripts can read, modify, add to, or delete content, and can be applied selectively to webpages using URL patterns.
- __Injected style sheets__—User style sheets that can modify the display of web content by overriding or adding to the styles normally applied. These style sheets can also be applied selectively using URL patterns.
- __Icon__—The icon for your extension. Name the image file `Icon.png`. Every extension must have a custom icon, which should be at least 64 x 64 pixels in size; the icon image will be scaled up or down as needed. You can also supply additional images optimized for display at particular sizes.

  If you provide multiple icons for display at different sizes, name the 64 x 64 icon file `Icon-64.png`. For best results, include an `Icon-48.png` and `Icon-32.png` for optimized display at smaller sizes. To optimize the appearance of your icons on high-resolution displays, include an `Icon-96.png` and an `Icon-128.png` as well.
- __Other images and media__—Any other images or media your extension needs, such as images that appear in menus.

## Extension Architecture

You can think of extensions as being divided into two parts: a part that interacts with the Safari app, and a part that interacts with web content.

The part of an extension that interacts with the Safari app resides in any of your extension’s global HTML page, extension bar pages, or popover pages. The part that interacts with web content resides in JavaScript files or CSS style sheets that are injected into content pages.

The division between these parts is strict, but you can send messages between them using proxies. If the global HTML page or an extension bar page needs to act on web content, it sends a message via the webpage proxy, where an injected script can act on it.

Similarly, if an injected script needs to make use of code in the global HTML page or an extension bar, it can send a message via the tab proxy.

The extension architecture is illustrated in Figure 1-1.

__Figure 1-1__  The extension architecture

（原归档配图未能恢复：`extensionsdiagram.png`）

An extension does not necessarily need to have both of these parts—an extension can operate only on the Safari app or only on web content. For example, a toolbar button to close a window or insert a tab would interact only with the app, while a style sheet that reformats websites into black text on a white background would operate only on web content.

## The Safari Extensions JavaScript API

In addition to the usual JavaScript methods, extensions have access to a special JavaScript API that lets them access the Safari app and web content. The full API is documented in _[Safari Extensions Reference](https://developer.apple.com/documentation/safariextensions)_, but this section covers the main things you need to know.

### Classes and Properties

The Safari Extensions API includes several classes such as [SafariBrowserWindow](https://developer.apple.com/documentation/safariextensions/safaribrowserwindow), [SafariBrowserTab](https://developer.apple.com/documentation/safariextensions/safaribrowsertab), and [SafariWebPageProxy](https://developer.apple.com/documentation/safariextensions/safariwebpageproxy), representing, respectively, a window, a tab, and the webpage loaded in a tab. You rarely, if ever, use the actual class names in your code, however. Instead, your extension JavaScript uses the [SafariNamespace](https://developer.apple.com/documentation/safariextensions/safarinamespace) object, `safari`, followed by a chain of properties. For example:

- `safari.application.activeBrowserWindow` returns the active instance of `SafariBrowserWindow`.
- `safari.application.activeBrowserWindow.activeTab` returns an instance of [SafariBrowserTab](https://developer.apple.com/documentation/safariextensions/safaribrowsertab).
- `safari.application.activeBrowserWindow.activeTab.page` returns an instance of [SafariWebPageProxy](https://developer.apple.com/documentation/safariextensions/safariwebpageproxy).

As usual in JavaScript, there is more than one way to address a particular object and the chain of properties goes both ways—a browser window has a [tabs](https://developer.apple.com/documentation/safariextensions/safaribrowserwindow/1635518-tabs) property representing its tabs, for example, and each tab has a [browserWindow](https://developer.apple.com/documentation/safariextensions/safaribrowsertab/1635481-browserwindow) property representing its parent window.

### The Application and Extension Objects

The [SafariApplication](https://developer.apple.com/documentation/safariextensions/safariapplication) object allows you to work with windows and tabs, and to respond to commands from toolbar items and contextual menu items (also known as shortcut menu items). For example, you open a new browser window like this:

`safari.application.openBrowserWindow();`

The [SafariExtension](https://developer.apple.com/documentation/safariextensions/safariextension) object allows you to add and delete buttons, menu items, scripts, and style sheets from your extension. For example, the following code snippet adds a simple black-and-white style sheet to the injected contents of your extension:

```
var bw = "body { color:black !important; background:white !important }" ;
safari.extension.addContentStyleSheet(bw);
```

You can access the `SafariApplication` and `SafariExtension` classes from your extension’s global HTML page or from an extension bar or popover. The classes are accessed as `safari.application` and `safari.extension`.

### Web Content Interaction

Scripts that are injected into web content can access the DOM of webpages they are injected into, allowing them to read and modify the content. Injected scripts use the normal JavaScript API—`getElementsByTagName()`, `innerHTML`, and so on—but because they are injected into a webpage, they have the privileges of a script loaded from the same domain the content comes from. In other words, a script injected by an extension can do anything the website author’s own scripts can do.

You can also designate style sheets as injected content. Injected style sheets are treated as user style sheets, as defined by the W3C. This means that they can override styles applied by the webpage’s author if they are declared important. For example, to override the `body` element’s background color, you could declare:

`body { background: #ffffff !important }`

The style cascades in the following order:

1. Your injected style sheet’s normal declarations are applied.
2. The website author’s style sheet’s normal declarations are applied.
3. Styles declared as important in the website author’s style sheets are applied.
4. Styles declared as important in your injected style sheets are applied, overriding any previous definitions (you have the last say).

## How to Create Extensions

Extensions are created using Extension Builder. Enable the Develop menu in the Advanced pane of Safari preferences. Then choose Show Extension Builder in the Develop menu.

An extension consists of an extension package—a signed, compressed folder with the `.safariextz` extension, containing all your extension's files and a generated `plist` file that tells Safari how your extension is organized and what it does.

__Note:__ The Safari extension package is an OS X bundle. You don’t need to understand bundles to create extensions, but you may find it helpful. To learn more about bundles and the `plist`, see _[Bundle Programming Guide](../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.

To create an extension, first make an extension folder by clicking the + button in Extension Builder and choosing New Extension. Then create the HTML, CSS, JavaScript, and media files you need and put them in the folder. The folder has the `.safariextension` extension when it is created.

Use Extension Builder to specify details about the structure and behavior of your extension and to build an extension package. Clicking Build creates a compressed, installable version of your extension with the `.safariextz` extension. For details, see [Using Extension Builder](Using%20Extension%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrnknltc).

Here’s a more detailed description of the things you put into the extension folder:

### Global HTML Page

Your extension can have a global HTML page, but it is not mandatory. This page is loaded only when Safari first loads your extension, but it is never displayed. It exists as a container for JavaScript. You can add JavaScript to your global page inline, or include it in a separate file or files in your extension.

If you are adding items to the main Safari toolbar, it’s generally best to write a global HTML page to specify what the toolbar items do. But you can also specify what the items do in a extension bar file. For details, see [Adding Buttons to the Main Safari Toolbar](Adding%20Buttons%20to%20the%20Main%20Safari%20Toolbar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmznknltc). Toolbar buttons can also invoke extension menus or popovers. The logic for extension menus generally belongs in the global HTML file as well. The logic for popovers can reside in the global HTML file or the popover file itself. For details, see [Adding Extension Menus](Adding%20Extension%20Menus.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrqfvjvomi) and [Adding Popovers](Adding%20Popovers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrrfvjvomi).

If you are adding items to Safari contextual menus, it’s generally best to write a global HTML page and specify what the menu items are and what they do, but again, you can also specify contextual menu items and actions in an extension bar or popover file. For details, see [Adding Contextual Menu Items](Adding%20Contextual%20Menu%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnbnknltc).

Putting the code for toolbar items, pop-up menus, and contextual menu items in your global page is more efficient than putting it in an extension bar file. This is because extension bar files are reloaded every time a window is opened, whereas the global file is loaded only once during the app’s lifetime.

If your injected scripts use a large amount of code or data, it should be moved to the global HTML page, so time isn’t spent reloading large blocks of code or data each time the user opens a webpage. Injected scripts can’t call functions defined in your global page directly, but injected scripts can pass messages to the global page, and the message handler in the global page can call other functions. For details, see [Messages and Proxies](Messages%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvomi).

### Extension Bar Files

Extension bars are toolbar-sized strips added to the Safari frame—below the bookmarks bar and above the tab bar—and dedicated to a particular extension. There can be multiple extensions with bars installed, and multiple bars per extension. If more than one extension bar exists, they are stacked. An example of an extension bar is shown in [Figure 1-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjvfvjvomjy).

Each extension bar has a label that is listed in the View menu (the View menu is hidden by default in Windows, but can be accessed through the gear button) and the menu item can be toggled to show or conceal each bar in the stack.

__Figure 1-2__  Extension bar example

（原归档配图未能恢复：`emoji.png`）

You can use extension bars to add controls to Safari or to display other content, such as a stock ticker, weather forecast, flight information, or headlines. Extension bars are only 30 pixels tall, so content that needs a taller display space should be shown in a popover, in its own tab, or injected into the browser content instead.

Extension bar files can access the Safari app to do things like opening and closing windows and tabs, loading URLs, responding to Safari toolbar items, and responding to menu choices in extension menus or contextual menus. Extension bar files cannot access the content layer to manipulate content loaded in a browser tab directly, however; for that you need to use injected scripts or styles (see [About Safari Extensions](About%20Safari%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjnknltc)). Your extension bars can send messages to and receive messages from your injected scripts.

You create extension bars using HTML (also CSS, JavaScript, and any media files). You don’t need to do anything special in the HTML to have your content displayed in an extension bar—just tell Extension Builder which HTML files are sources for extension bars.

If your extension bar uses images or other media, they can be included in the extension package or loaded from the web at runtime. It is strongly recommended that you use local media whenever possible.

Extension bar files are loaded each time Safari opens a browser window, creating an instance of the bar in every window, so if your extension bar has code or data that needs to load only once, you should put that material in a global HTML page instead.

If you want to create an extension bar, see [Adding Extension Bars](Adding%20Extension%20Bars.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnjnknlte).

### Popover Files

If your extension needs more space to display content than fits comfortably in an extension bar, or if you want the content to appear only when the user summons it, you can create a popover—an HTML file that displays in a pop-up window, then disappears when the user changes focus (by clicking in another window, for example).

Popover files have the same access and permissions as extension bar files, but display as pop-up windows instead of persistent bars. A popover is displayed in response to the user clicking, or pressing and holding, a toolbar item defined by the extension.

An extension can have multiple popovers, but only one displays at a time. Each popover is an element in the `safari.extension.popovers` array. If popovers are specified in Extension Builder, each popover file loads once, when the extension launches. If a popover is created at runtime, the specified popover file is loaded then. There is only one instance of a popover, no matter how many windows are open.

For details, see [Adding Popovers](Adding%20Popovers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrrfvjvomi).

### Injected Scripts and Style Sheets

You can have Safari inject scripts or style sheets that you provide into the webpages Safari loads. These injected scripts and styles can read and modify browser content.

Scripts can be specified as End Scripts (interpreted when the page’s `onload` event occurs), or Start Scripts (interpreted before the page is parsed). Most scripts are End Scripts. Scripts that block unwanted content before it displays are the most common use for Start Scripts. You can have both Start Scripts and End Scripts.

Style sheets are applied as user style sheets, so normal declarations in them precede the webpage author’s declarations in the cascade, but `!important` declarations are applied after the author’s declarations, allowing user style sheets to override the webpage author’s styles.

You can use URL patterns to decide which webpages your scripts and style sheets are applied to. Use URL patterns when creating a blacklist or a whitelist for your extension. The blacklist contains URL patterns for webpages you don’t want to inject scripts or styles into. The whitelist contains URL patterns for webpages you do want your scripts and styles injected into. For details, see [The Extension Builder Interface](Using%20Extension%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrnknltk).

If you want to inject scripts into webpages, see [Injecting Scripts](Injecting%20Scripts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnrnknltc).

If you want to apply user style sheets to webpages, see [Injecting Styles](Injecting%20Styles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnznknltc).

### Companion App Extensions

Companion app extensions provide an easy and secure way to send messages from your Safari extension to your native OS X app. You create the companion app extension as part of your OS X app and then call this app extension from your Safari extension. Messages sent to the companion app extension are similar to the messages you use to pass information around between parts of your Safari extension. For more information, see [Communicating with your OS X App](Communicating%20with%20your%20OS%20X%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrtfvjvona).

### The plist Files

The `Info.plist` file contains your extension’s metadata. This includes the extension name, author, and version, as well as information about how your extension is organized—whether it has a global HTML page, extension bars, or injected scripts, and which files are used for what. If your extension has settings, they are also defined in a `plist` file—`Settings.plist`. `Settings.plist` is optional, but `Info.plist` is required. When someone talks about your extension’s `plist` file, they generally mean `Info.plist`.

The `plist` files are created for you using Extension Builder, so you shouldn’t need to do anything with them yourself. But to really understand how extensions work, you need to know the `plist` files exist. All the fields you fill out in the Extension Builder interface are stored in a `plist` file.

## Security

Because extensions have privileges that allow them to go beyond what ordinary scripts can do, you need to be security conscious when writing extensions. The first level of security is provided by the certificate. The certificate ensures that an extension comes from a known source (you) and prevents malicious extensions from masquerading as your extension. It is your responsibility to prevent your extension from being taken over by a malicious script, however. Follow the guidelines in the following sections to prevent security breaches.

### Don’t Insert Imported Text Using innerHTML or document.write

It can be tempting to display HTML imported from the web using the `innerHTML` property, but it is dangerous to do so. It is equally dangerous to insert imported text into your extension using the `document.write` method. A malicious website can include a script that, when loaded into the HTML of your extension, gains the privileges of your extension. Furthermore, if your extension obtains the imported HTML using HTTP (as opposed to HTTPS), a forged DNS server, such as a Wi-Fi hacker, can substitute a malicious script for the requested item.

If you are displaying imported text, insert it into one or more paragraph elements using the `innerText` property instead of using the `innerHTML` property or the `document.write` method.

If you are displaying imported HTML, sanitize it by removing any material enclosed by dangerous tags, such as scripts or HTTP requests, before inserting the HTML into your extension. Use a whitelist of allowed tags and attributes, and remove any HTML that does not match the whitelist. Insert the HTML into your extension using DOM methods such as `appendChild`, which inserts only safe elements.

### Don’t Use eval with Imported Text

Using the `eval` method to parse imported data allows the data to be executed as code, enabling malicious scripts to execute from within your extension. Use the `JSON.parse` method instead.

### Don’t Use HTTP to Add HTML, CSS, or Scripts

Include any scripts, HTML, and CSS that your extension uses directly within your extension, or obtain them from a trusted source using HTTPS. If you import items using HTTP, a person with network access, such as a Wi-Fi hacker, can insert malicious scripts in place of the requested items.

### Don’t Use Custom IPC Methods to Talk to Native OS X apps

When your Safari extension needs to communicate with your OS X app, use a companion app extension. Other methods, such as NPAPI plug-ins and WebSockets, do not provide any security protection and can be intercepted or modified by attackers.

### Private Browsing

Private Browsing mode prevents Safari from storing cookies, browsing history, search history, caches, and AutoFill information. Your extension should not store any information about the user’s actions when in Private Browsing mode.

You can check whether a particular tab is in Private Browsing mode by querying the tab object’s [private](https://developer.apple.com/documentation/safariextensions/safaribrowsertab/1635351-private) property (for example, `safari.application.activeBrowserWindow.activeTab.private`).

[Next](Using%20Extension%20Builder.md)[Previous](About%20Safari%20Extensions.md)
