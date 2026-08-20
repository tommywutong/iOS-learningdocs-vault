---
title: Dashcode User Guide
apple_id: TP40004692
resource_type: Guide
platform: Safari|Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashcode_UserGuide/Contents/Resources/en.lproj/DebuggingSharing/DebuggingSharing.html
archived_at: '2026-07-15T05:17:37.954064Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashcode User Guide](Introduction%20to%20Dashcode%20User%20Guide.md)


[Next](Advanced%20Topics%20for%20Widgets.md)[Previous](Adding%20Source%20Code%20and%20Creating%20Bindings.md)

# Testing and Sharing

After you’ve written code for your widget or web application, test it to ensure that it works as you expect. Dashcode includes its own Dashboard environment so you can run and test a widget in Dashcode without having to open it in Dashboard. Similarly, Dashcode includes a simulator application that simulates Safari and Safari on iPhone, so you can easily test both products of a dual-product web application project.

In addition to running widgets and web applications, Dashcode also includes tools that help you debug and fix problems that may arise. This chapter includes information on how to trace events and inspect variable values while a widget or web application executes. It also includes information on sharing a widget and deploying a web application.

To run a widget or a web application in Dashcode, choose Debug > Run or click Run in the toolbar. Depending on your project type, this has a different effect:

- For widgets, this runs the widget in Dashcode without having to open it in Dashboard. The widget behaves here as it would in Dashboard.
- For web applications, this runs the web application in the appropriate simulator application without having to deploy it and run it in a device. The simulator allows your web application to behave as it would in Safari on iPhone or in Safari.

If you’ve installed the iOS SDK on your computer, you have two display options when testing a mobile Safari web application in Dashcode version 3.0 and later:

- Run with the Safari interface visible (that is, with the Safari toolbar and navigation bar visible). This simulates what users can see when they use Safari on iPhone to navigate to your web application.
- Run with the Safari interface hidden (that is, in full-screen mode). This simulates what users can see when they tap a Web Clip icon to open a mobile Safari web application that can run in full-screen mode.

You can access these options by clicking and holding the Run button in the Dashcode project window. From the menu that appears, choose “Run” or “Run Full-screen.” After you make your choice, clicking Run or choosing Debug > Run runs your web application in that mode until you change it.

In Dashcode version 3.0 and later you can simulate running a web application on the same server that hosts the application’s data sources. This allows the application to bypass the “same source” restriction imposed by web browsers and fetch data from an external server (see [Deploying a Web Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvony) for more information on this restriction). When you run the application in Dashcode for the first time, Dashcode displays a dialog that asks whether you want to simulate running on a remote server or on your local computer.

- Click Simulate to simulate running on the remote server you identified in the application attributes pane or in the URL field of a data source.

  Dashcode uses this remote server for simulation until you specify a different one, or until you deselect the Simulation checkbox in the Running section of the Run & Share pane. If you do either of these things, Dashcode displays a dialog asking for confirmation of your simulation choice the next time you run your web application.
- Click Continue to run the application on your local computer. Note that this can prevent the application from loading external resources.

When your widget or web application loads, test it out to see if it functions as you expect. When an error occurs, an _exception_ is thrown and, by default, execution pauses. When this happens, there are a number of tools at your disposal that help you see where the problem is and inspect variable values:

- The run log lists errors and other useful information. If you enable tracing, the run log notes the invocation of functions as well. See [The Run Log and Tracing Execution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvomi) for details.
- The Stackframe & Variables table shows you the value of any variable a widget or web application uses. See [Checking Values in Memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvomy) for details.
- Step-by-step execution enables walking through the execution line-by-line so you can see the effects of the code. See [Pausing and Step-by-Step Execution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvoni) for details.
- The Evaluator is a console where you enter individual lines of code to be executed immediately. See [The Code Evaluator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvona) for details.

To continue a paused widget or web application, choose Debug > Continue or click Continue in the toolbar. To turn off pausing when an exception occurs, deselect Debug > Break on Exceptions.

To pause a widget or web application at any time, choose Debug > Pause or click the pause button in the toolbar. While a widget or web application is paused, you can step through its code line-by-line as discussed in [Pausing and Step-by-Step Execution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvoni). You can also pause a widget or web application when execution reaches a specific line of code using a breakpoint, as discussed in [Breakpoints](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvonq).

To stop running a widget or web application in its testing environment, choose Debug > Stop or click Stop in the toolbar.

When you run a widget or web application in Dashcode, the canvas is replaced by the run log. Any errors that Dashcode encounters while running the widget or web application are reported here. For example, a call to a function that doesn’t exist appears in the run log as an “object that doesn’t allow calls.“

If the run log is replaced by another view, choose View > Run Log to show it. When possible, selecting a row in the run log reveals the associated line of code in the source code editor.

In addition to reporting errors, the run log can be used to trace execution of a widget or web application. Tracing means that an entry in the run log is made whenever a function starts and finishes. This is useful when you’re watching the flow of execution in a widget or web application.

When the run log is visible, you can filter the contents of the run log by typing a term into the search field in the toolbar.

At any time, you can pause the execution of a widget or web application. Pausing execution is useful if you want to inspect the values of variables. To pause, choose Debug > Pause or click Pause in the toolbar. When the widget or web application is paused, the run log is replaced with the Stackframe & Variables table.

When the execution of a widget or web application is paused, you can inspect the values of the variables within the scope of the current function and the global scope. Also, the line of code that is paused is highlighted in the source code editor. In the shortcuts under the source code editor, you can see a hierarchy of functions that leads to the currently executing function. If you click another function name in the shortcuts, the function’s variables are shown in the Stackframes & Variables table and its code is shown in the code editor. You can also search for a specific variable by typing its name into the search field in the toolbar.

When you’re finished examining variables, you can continue executing the widget or web application in a few different ways:

**_Continue_**
: Choose Debug > Continue or click Continue in the toolbar to continue execution with no interruption.

**_Step Into_**
: Choose Debug > Step Into or click Step Into in the toolbar to execute the next line of code and step into function calls so you can see the effect that line of code has.

**_Step Over_**
: Choose Debug > Step Over or click Step Over in the toolbar to execute the next line of code so you can see the effects that line of code has.

**_Step to End_**
: Choose Debug > Step to End or click Step to End in the toolbar to execute the rest of the current function; execution pauses when the function is finished so that you can inspect its variables before they are relinquished.

Also, execution pauses whenever an exception occurs. When an exception occurs, the execution of a web application or widget is paused and an entry in the run log explains what the problem is. If you click the entry, the line of code in which the exception occurred is highlighted. By default, this option is enabled. You can control this option by choosing Debug > Break on Exceptions.

The Stackframe & Variables table shows the value of the variables used in a widget or web application. When the widget or web application is running, its global variables are available for inspection. When you pause a widget or web application, as described in [Pausing and Step-by-Step Execution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvoni), the current function gets its own heading in the table with its variables listed underneath. If the function was called by another function, the second function’s variables are listed under the first, and so on.

Double-clicking a variable in the table adds the variable name to the code evaluator, as discussed in [The Code Evaluator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvona).

In addition to pausing the execution of a widget or web application using the Pause option, you can set places in your code for execution to pause, called breakpoints. You can add a breakpoint in two ways. One way is to click in the gutter of the source code editor. If the gutter is not showing, go to Editing preferences and select the Show Gutter option.

A blue arrow in the gutter means that before that line of code is executed, execution will halt. To temporarily disable the breakpoint, click it; it turns from blue to gray to indicate that it’s disabled. To remove the breakpoint, drag it outside of the gutter.

The other way to set a breakpoint is to use the Breakpoints window. To show the Breakpoints window choose Debug > Show Breakpoints Window or double-click in the gutter. In the Breakpoints window, click the plus (+) button and specify either a filename and line number or a function name to break on. For instance, if you wanted to break in `Untitled.js` on line 42, you enter `Untitled.js:42`. Alternatively, you can supply the name of the function you want to break on (for instance, `showFront` in a widget).

In addition to the breakpoint, you can set a condition for the breakpoint. A condition is a JavaScript statement that evaluates to either `true` or `false`. If the condition evaluates to `true` when execution passes the breakpoint, execution pauses.

In the Breakpoints Window, you can remove a breakpoint by selecting a breakpoint from the table and clicking the minus (-) button or you can disable it by deselecting the checkbox next to a breakpoint’s item in the table.

While you run a widget or a web application, it can be useful to execute just one line of code. The code evaluator lets you do this. To show the code evaluator, choose View > Evaluator or choose Evaluator from the View menu in the toolbar. In the evaluator, you enter arbitrary code and press the Return key to execute the code immediately.

If you double-click a value in the Stackframes & Variables table, its name is automatically entered into the code evaluator. Also, if your cursor is at the prompt and you press the up arrow key, you cycle through the history of entries in the code evaluator.

When you’re finished developing a widget, you can share it with others. There are two commands for deploying a widget, and both export the widget from the project as a `.wdgt` bundle, ready to run in Dashboard. Click Run & Share in the navigator to see a pane that gives you the choice of deploying the widget for use in OS X v10.4.3 or later or for use in all versions of OS X v10.4. In most cases, deploying a widget for use in OS X v10.4.3 or later is advisable, because it results in a smaller widget.

If you want to share your widget by, for example, sending it in an email, click Save to Disk in the Run & Share pane and choose a convenient save location. If you want to make sure the widget project is automatically saved to disk before deploying, select the “Save project to disk before deploying” checkbox. Note that this checkbox is available after you’ve saved the widget project for the first time.

If the widget is for your use only, choose File > Deploy Widget to install it on your computer.

When you’re ready to deploy your web application, you choose where you want Dashcode to place your application’s code and resource files and how they should be saved. These files include the HTML, CSS, and JavaScript files, image files, and your application’s Web Clip icon or favicon. (Note that, during deployment, Dashcode removes some Dashcode-specific content from the HTML file.)

By default Dashcode deploys these files to a folder in your `~/Sites` folder. You can modify this behavior by making choices in the Run & Share pane (click Run & Share in the navigator to open this pane).

Dashcode gives you three deployment options:

- __Deploy to a local destination__. Dashcode places your web application files in a folder you specify for the default local destination or a local destination you create.
- __Deploy to a remote server__. Dashcode uses WebDAV, FTP, or MobileMe to upload your web application files to a server you specify.
- __Save to disk__. Dashcode saves your web application files in a folder whose name and location you supply.

If you want to save a copy of your web application files in a folder on disk, click Save to Disk at the bottom of the Run & Share pane and supply a folder name and location. If you want to deploy the application to a local or remote server, you can customize the deployment behavior in the Deploy section of the Run & Share pane:

- Use the Destination pop-up menu if you want to select a destination other than the default. (Unless you’ve already changed the default destination, this is the localhost account.)

  To add a new destination, select “Add destination” in the pop-up menu to open Dashcode’s Destinations preferences and set up a new destination.

  In Destinations preferences, you can specify an additional local destination or a WebDAV, FTP, or MobileMe destination. You can also set whether Dashcode should use the new destination as the default destination for new projects.
- Use the Application Path field to supply a name for the application folder (otherwise, Dashcode creates a folder called Untitled). Dashcode creates this folder in the path specified by the currently selected destination.

In the Options section of the Run & Share pane, you can determine the save behavior and the deployment notification:

- Select the “Save behavior” checkbox if you want your web application project to be saved before every deployment (this checkbox is available after you’ve saved the project for the first time).
- Select the Compression checkbox if you want Dashcode to compress the JavaScript code in the parts files. This can reduce network latency during multiple file requests. Note that selecting this checkbox does not compress `main.js` or any JavaScript code you supply.
- Select the Notification checkbox if you want Dashcode to send an email message containing a link to your application every time you deploy it. Use the field below the Notification checkbox to supply the recipient’s email address (or multiple email addresses, separated by commas).

After you finish making your selections, click Deploy at the bottom of the Run & Share pane, or choose File > Deploy, to deploy your web application. To view your web application, navigate to the `index.html` file on the designated server (for example, `http://myserver.com/myapp/index.html`). Your web application automatically detects the identity of the browser and opens a mobile Safari web application in Safari on iPhone and a Safari web application in Safari.

[Next](Advanced%20Topics%20for%20Widgets.md)[Previous](Adding%20Source%20Code%20and%20Creating%20Bindings.md)

