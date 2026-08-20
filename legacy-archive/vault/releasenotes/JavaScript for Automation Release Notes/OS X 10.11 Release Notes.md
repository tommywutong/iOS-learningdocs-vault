---
title: JavaScript for Automation Release Notes
apple_id: TP40014508
resource_type: Release Note
platform: macOS
topic: Interapplication Communication
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/Articles/OSX10-11.html
archived_at: '2026-07-18T02:58:39.849259Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md) · [JavaScript for Automation Release Notes](Introduction%20to%20JavaScript%20for%20Automation%20Release%20Notes.md)


[Next](OS%20X%2010.10%20Release%20Notes.md)[Previous](Introduction%20to%20JavaScript%20for%20Automation%20Release%20Notes.md)

# OS X 10.11 Release Notes

This article describes changes to JavaScript for Automation in OS X 10.11.

JavaScript for Automation now allows you to debug scripts with Safari's Web Inspector. This feature can be used by scripts run in Script Editor and by the Run JavaScript action in Automator.

To debug scripts, you must enable the Web Inspector in Safari and add debugger statements to your scripts.

To enable debugging with the Web Inspector, follow the steps described in the [Enabling Web Inspector](../../documentation/Apple%20Applications/Safari%20Web%20Inspector%20Guide/Get%20Oriented.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqmrnknlte) section of _[Safari Web Inspector Guide](../../documentation/Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_.

Once you've enabled the Web Inspector, you will find a submenu with your computer's name in Safari's Develop menu. In that submenu, make sure the menu item Automatically Show Web Inspector for JSContexts is selected.

__Figure 1__  Enabling the Safari Web Inspector for JSContexts

!

In Script Editor or the Run JavaScript action in Automator, create a script with a debugger statement in it. For example:

```
var x = false
debugger
if (x) {
    console.log("Why isn't this being called?")
}
```

Run the script. If Safari is running, an inspector window appears and pauses on the debugger line.

You must recompile a script before you can debug it again.

JavaScript for Automation has flags on `Application` objects that affect how strictly properties and commands are looked up, and whether parameter types are checked before sending commands. These are discussed in more detail in the OS X 10.10 JavaScript for Automation release notes (see [Strict Flags](OS%20X%2010.10%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbyfvbuqmjqhewvgvztgq)).

For OS X 10.11, all strict flags are now set to `false` by default. This means that any property or command listed in a scripting dictionary is valid to access or call on any object in the application. You can send any type of parameter to a command, regardless of what the scripting dictionary says.

JavaScript for Automation now exposes an `id` property and a `running` property on all `Application` objects. These properties return an application's bundle identifier and whether the application is running, respectively. Like getting an application's `name`, `version`, or `frontmost` property, these are called as functions.

Here’s an example that demonstrates how to retrieve Mail's bundle identifier and running status.

```
Mail = Application('Mail')
Mail.id()
Mail.running()
```


JavaScript for Automation includes some enhancements to the way script libraries work.

JavaScript for Automation now has two additional search mechanisms you can use when searching for script libraries:

- You can place script libraries in the `Contents/Library/Script Libraries` directory of any installed application bundle. This allows distribution of libraries associated with an application, or creating applications for the sole purpose of distributing libraries.
- Use the environment variable `OSA_LIBRARY_PATH` to add more locations to search for script libraries. This feature allows you to use a library without installing it in one of the standard locations. The variable’s value is a colon-separated list of absolute POSIX paths, such as `OSA_LIBRARY_PATH='/opt/local/Script Libraries:/usr/local/Script Libraries'`.

For additional details, see [Creating a Library](../../documentation/Apple%20Script/AppleScript%20Language%20Guide/Script%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wvgvzrgm) in _[AppleScript Language Guide](../../documentation/Apple%20Script/AppleScript%20Language%20Guide/Introduction%20to%20AppleScript%20Language%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobt)_.

Custom errors thrown from script libraries are now catchable by client scripts. Prior to OS X 10.11, all errors thrown by script libraries became generic `(-10000)` errors when caught by the client script.

[Next](OS%20X%2010.10%20Release%20Notes.md)[Previous](Introduction%20to%20JavaScript%20for%20Automation%20Release%20Notes.md)

