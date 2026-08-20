---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/InjectingScripts/InjectingScripts.html
archived_at: '2026-07-27T06:57:07.710581Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Injecting%20Styles.md)[Previous](Adding%20Contextual%20Menu%20Items.md)

# Injecting Scripts

You can inject `.js` files into webpages (a `.js` file is a text file with the `.js` extension, containing JavaScript functions and commands). The scripts in these files have access to the DOM of the webpages they are injected into. Injected scripts have the same access privileges as scripts executed from the webpage’s host.

## About Injected Scripts

Injected scripts are loaded each time an extension-accessible webpage is loaded, so you should keep them lightweight. If your script requires large blocks of code or data, you should move them to the global HTML page. For details, see [Example: Calling a Function from an Injected Script](Messages%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvomq).

An injected script is injected into every webpage whose URL meets the access limitations for your extension. For details, see [Access and Permissions](Access%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqobnknltc).

Scripts are injected into the top-level page and any children with HTML sources, such as iframes. Do not assume that there is only one instance of your script per browser tab. If you want your injected script not to execute inside of iframes, preface your high-level functions with a test, such as this:

```
if (window.top === window) {
   // The parent frame is the top-level frame, not an iframe.
   // All non-iframe code goes before the closing brace.
```

Injected scripts have an implied namespace—you don’t have to worry about your variable or function names conflicting with those of the website author, nor can a website author call functions in your extension. In other words, injected scripts and scripts included in the webpage run in isolated worlds, with no access to each other’s functions or data.

Injected scripts do not have access to the `safari.application` object. Nor can you call functions defined in an extension bar or global HTML page directly from an injected script. If your script needs to access the Safari app or operate on the extension—to insert a tab or add a contextual menu item, for example—you can send a message to the global HTML page or an extension bar. For details, see [Messages and Proxies](Messages%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvomi).

__Important:__ When you use `safari.extension` from within an injected script, you are not addressing the `SafariExtension` class. You are addressing the `SafariContentExtension` class.

Your injected scripts can access resources—images, HTML, and other scripts, for example—within your extension folder. Relative URLs are relative to the webpage your script is injected into, however. If you need to access local resources, use `safari.extension.baseURI +` "relative path and filename". You cannot access resources on the user’s hard drive outside of the extensions folder.

To add content to a webpage, use DOM insertion functions, as illustrated in Listing 10-1.

__Listing 10-1__  Modifying a webpage using DOM insertion

```
// create a para and insert it at the top of the body
var newElement = document.createElement("p");
newElement.textContent = "New Element!";
newElement.style.color = "red";
newElement.style.float = "right";
document.body.insertBefore(newElement, document.body.firstChild);
```

__Note:__ DOM modification should take place in an End Script; in a Start Script, `document.body` may be undefined.

## Adding a Script

To add an injected script, follow these steps:

1. Create an extension folder—open Extension Builder, click +, choose New Extension, give it a name and location.
2. Drag your script file into the extension folder.
3. Click New Script under Injected Extension Content in Extension Builder, as illustrated in Figure 10-1.

   __Figure 10-1__  Specifying injected content

   （原归档配图获取待重试：`injectedContent.jpg`）

   You can choose to inject your script as a Start Script or an End Script. An End Script executes when the DOM is fully loaded—at the time the `onload` attribute of a `body` element would normally fire. Most scripts should be injected as End Scripts.

   A Start Script executes when the document has been created but before the webpage has been parsed. If your script blocks unwanted content it should be a Start Script, so it executes before the page displays.
4. Choose your script file from the pop-up menu.

You can have both Start and End Scripts. You can have more than one script of each type.

In order for your scripts to be injected, you must specify either Some or All website access for your extension. You can have your script apply to a single webpage, all webpages, or only certain webpages—pages from certain domains, for example. For details, see the description of whitelists and blacklists in [Access and Permissions](Access%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqobnknltc).

[Next](Injecting%20Styles.md)[Previous](Adding%20Contextual%20Menu%20Items.md)
