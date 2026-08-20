---
title: Interface Builder
apple_id: 10000179i
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: null
technology: InterfaceBuilderKit
published: '2007-04-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/IBTips/Articles/FreqAskedQuests.html
archived_at: '2026-07-15T07:24:36.334580Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interface Builder](Introduction%20to%20Interface%20Builder.md)


[Next](Document%20Revision%20History.md)[Previous](Making%20Connections%20in%20Cocoa%20Applications.md)

# Frequently Asked Questions

This article gives brief answers to a number of questions that developers have had about Interface Builder.

- What do the non-integral rectangle warnings mean and how do I get rid of them?

  Non-integral rects are frame definitions that contain float values. Although not critical, these can lead to performance problems and blurring. Interface Builder will discover and correct any non-integral rects it finds when you open a nib.
- How do I put widgets inside a container such as a box or tab view?

  Click on a category in the Palette toolbar. Drag a widget from the palette over your design window. A selection ring will appear around the deepest element that can accept the widget. Release the mouse button to drop it. Once an element is embedded in a container, it can only be removed by deleting or cutting it.
- How do I see the containment hierarchy of my document?

  To see a hierarchical list of all the objects within your document, click the outline-mode button located above the scrollbar in the nib file window. You can use this view to select objects and widgets that are difficult to reach through the design window. You can also make connections from the outline view. To switch back to the icon view, click the icon-mode button immediately above the outline-mode button. The buttons are shown in Figure 1.

  __Figure 1__  Buttons for Outline and Icon View modes

  ![Buttons for Outline and Icon View modes](attachments/Articles/Art/icon_outln_buttons.gif)
- How do I switch tabs in a Tab view in the design window?

  Double click an area of the tab view free of embedded widgets to activate the tab view editor (a ring is drawn around the editor to show it is active). Then click once on the tab you would like to view, click the stepper control in the Info window, or press the Tab key to go to the next tab or Shift-Tab to go to the previous one.
- How do I edit tab titles?

  Double-click an area of the tab view free of embedded widgets to activate the tab view editor (a ring is drawn around the editor to show it is active). Double click the text of the tab you wish to change. Enter the new text and press Return.
- How do I add a tab to my tab view?

  Single-click the tab view to select it. Open the Attributes panel in the Info window. Add new tabs by increasing the number listed in that pane. Alternatively, you can double click the tab view to activate the tab view editor. Select the tab that is closest in design to what you want for the new one. Then copy and paste. You get a new tab that is a replica of the selected tab.
- How do I change the tab order of a tab view?

  Double click the tab view to open its editor. Select the tab you wish to reorder and press the arrow keys to reorder it. If this procedure doesn’t work, try using the stepper control in the Info window to select the tab you want to reorder before pressing the arrow key.
- How do I edit a widget’s properties?

  Select the widget in the design window. Open the Info window with the Tools > Show Info menu item. Make your changes using the various info panels.
- How do I add menus to the menu bar?

  To add individual items, drag an “Item” menu from the menu palette into your menu editor. To add a new submenu, drag a “Submenu” item from the menu palette into the menu editor. Double click these items in the menu editor to change their names. The other menu types in the menu palette represent various system menus.
- How do I add menus to a popup button?

  Double click the popup button. A menu editor will appear. Use the same techniques described above to add menu items to the editor.
- Can I create an interface without using Interface Builder?

  Interface Builder is a tool that manipulates Cocoa and Carbon interface elements. You could manipulate these same elements programmatically, but using Interface Builder is easier.
- Why is some text gray, and other text black?

  Gray elements represent items defined by system frameworks. Often, these elements can’t be deleted or changed. Files Owner, the NSApplicationIcon and the description for NSObject are examples of system defined elements.
- How can I turn off the Aqua guides?

  Use the Layout > Disable Aqua Guides menu item. You can hide any user guides you have created with the Layout > Hide Guides menu item. Hold down the Command key while you drag widgets to temporarily reverse your guide settings.
- How do I remove a user guide?

  User guides can be removed from the document by dragging them off the edge of the window.
- Does File Merge work with nibs?

  Yes. You can compare two nib files using File Merge to see what has changed, but you can’t merge to a new file. Behind the scenes, File Merge runs nibtool on the two nib files and diffs the textual output.
- Something is wrong with my Interface Builder preferences. How do I reset my preferences?

  Quit Interface Builder. Open a Terminal window and type the following: `defaults remove com.apple.InterfaceBuilder` The next time you launch Interface Builder, a new set of preferences will be created.
- How can I easily see the header for my classes?

  The “view in PB” button in the Attributes Info Panel is active while Xcode is running. Clicking the button opens the class’s header file for Cocoa objects and for custom classes if the source files for the class have been created.
- Can I add UI elements to closed containers

  A container does not have to be “open” (that is, you do not have to double-click it) before it will accept new UI elements or formatters. When you drag a UI element from the palette to a container, the deepest possible destination displays a ring. You can release the mouse to deposit the UI element in the container.
- Can I change the configuration of the tool bar in the Palette window?

  The control used to select the currently active palette is an NSToolbar. You can reorder the palette items and do anything that the NSToolbar allows you to do in the palette window. This allows you to move your most frequently used palettes closer together and allows easier loading of palettes.

- What kinds of images can I add to my Cocoa nib?

  You can add any image supported by NSImage. Any image you wish to use must have an extension understood by NSImage (.tiff, .jpeg, and so on). See the question “How do I get Interface Builder to display images from my project?” to learn how to use these images.
- Should I release top level objects at runtime?

  Usually, yes. The file’s owner is responsible for releasing any resources created by the nib. These include any top level objects such as formatters, custom views, extra windows, or extra menus. However, there are a few exceptions to this rule. Windows with the “Release on Close” flag set do not need to be released; they will release themselves when they close. Windows controlled by a window controller will also be released automatically.
- What does Instantiate do?

  A frequent misconception of nibs is that they are simply recipes for recreating user interfaces at runtime. In reality, nibs contain actual archived objects. Although most of these objects are in fact user interface elements, nibs can contain archived instances of other objects such as controllers and formatters. The “instantiate” command in the Classes pane causes the selected object to be created at runtime. It’s common to instantiate a window’s controller class alongside the actual window in the nib. When the nib is loaded, the window and controller are created and then any connections between them are established.
- How do I put widgets inside a scroll view?

  Select the widget(s) and use the menu item Layout > Make subviews of > Scroll view. If only one widget is selected, Interface Builder attempts to make it the NSScrollview’s document view. If more than one widget is selected, they are enclosed in an NSview and that is made the document view.
- How do I put widgets inside a split view?

  Select the widgets and use the menu item Layout > Make subviews of > Split view. If the widgets are arranged side to side, the split is vertical. Conversely, if they are arranged from top to bottom, the split is horizontal.
- How do I make a drawer?

  There are two ways of creating drawers in Interface Builder. To create a new window with a drawer, drag the composite drawer object off the window palette onto the desktop. The composite drawer object is the one that has a window with a drawer sticking off the left side of it. It’s NOT the object labeled “Drawer”. The composite drawer object contains a main window, a content view, and an NSDrawer object. These objects come pre-wired. All you have to do is connect a widget to the “toggle” action of the NSDrawer object. Double-click the content view icon in the Instances pane of the nib file window to open the content view so that you can add views to it. To add a drawer to an existing window, drag the NSDrawer object (the one labeled “Drawer”) into the nib file window and a custom view object (labeled CustomView) onto the design window. Use the custom view object as the content view for the drawer by connecting the NSDrawer’s `contentView` outlet to the custom view and its `parentWindow` outlet to the existing window.
- Why does my bottom or top drawer size itself improperly?

  There is a known problem in the underlying NSDrawer implementation that adversely affects proper drawer size calculations. Specifically, when a drawer’s preferred edge is left or right, the leading and trailing offsets are used to automatically calculate the height of the drawer. When a drawer’s preferred edge is top or bottom, the leading and trailing offsets should be used to automatically calculate the width of the drawer. However, these values are incorrectly applied to the height.
- What do File’s Owner and First Responder represent?

  File’s Owner and First Responder are proxies for objects that will exist at runtime. File’s Owner represents the object that will be passed in for owner in the method [NSBundle loadNibNamed: owner]. You can use the Custom Class Info Panel to specify what kind of object File’s Owner will be. Once you’ve indicated what File’s Owner is, you can make connections to it. First Responder is your portal to the responder chain. You can add actions to First Responder in the Classes pane of the nib file window. Then, connect buttons and menu items to First Responder so that they call the desired action. The first object in the responder chain that understands this action will be called. See the Cocoa documentation for more information about how the responder chain works.
- How do I set up the springs and struts so my views autosize?

  Views can be made to resize automatically when the window or split view that contains them is resized. You will probably need to set the springs and struts for every view in your window. The easiest way to see how they work is to assign a few views with different settings and then use File > Test Interface to see the results. To see how this works, bring up the Size info panel and select a square bevel button. There are two parts to Cocoa’s auto sizing: growing and anchoring. How the button grows is determined by the strut/spring setting shown inside the button picture in the info panel. If an axis (horizontal or vertical) is a spring, then the view can grow when its container is resized. If it’s not a spring, but rather a strut, the button will remain the same size. Click on the horizontal axis inside the mock button to turn it into a curly spring. Then use the menu item File > Test Interface to test the interface. Grow the window in various directions. The button gets longer, but never taller or shorter. Click the switch icon in the menu bar or press Command-Q to stop testing the interface. Repeat this process, but with the vertical axis set as a spring. Now it can get taller or shorter but never wider. The outer set of springs and struts represents how the view is to be anchored. If a segment is a strut, the view maintains a constant distance to the side of its container along that side. However, if it’s a spring the view allows the distance to vary. Select the sample square bevel button and click the left-most segment so that it turns into a spring. Because the segment at right is still a strut, the view maintains a constant distance to the edge of the window from the view’s right side, but allows a variable distance along the left side. Test the interface to see the effect.
- How do I add a contextual menu with Interface Builder?

  Select the Menu palette and drag the icon that looks like Figure 2 into your nib file window. A menu editor window opens for the new menu. Control-drag from the view for which you want a contextual menu to this menu icon to connect the `menu` outlet. You can use the menu editor window and the info panel to edit and add items to the contextual menu.

  __Figure 2__  Contextual menu icon

  ![Contextual menu icon](attachments/Articles/Art/menu_icon.gif)
- How do I use a formatter?

  There are two ways to add a formatter to a widget in Interface Builder. The easiest way is to drag it from the palette and drop it on the widget (providing that widget supports formatters). You can then select the widget and bring up the Formatter Info pane to set the formatter’s attributes. Alternatively, you can share a single instance of a formatter with several different widgets by dragging the formatter to the Nib file window and connecting the widget’s `formatter` outlet to the formatter in the Nib file window. As with any top level object, be sure to release it when you’re done.
- How do I make a matrix (rows and columns) of a widget?

  Any widget that has an NSCell counterpart can be made into a matrix. Hold down the Option key while you drag a selection handle. The farther you drag the handle, the more new rows and columns are appended to the matrix. Some other widgets, such as NSBrowser and NSForm, work the same way.
- How do I give a browser more than one column?

  Hold down the Option key while you drag one of the side selection handles. The farther you drag the handle, the more new columns are appended to the browser. To add or remove columns without changing the overall size of the browser, change the number in the Visible Columns field of the browser’s Attributes pane in the Info window.
- How do I add a table column?

  There are two ways to add columns to a table. The easiest way is to select the table and use the “#Colms” field in the table’s Attributes pane to add new columns. Another way is to open the table’s editor by double clicking it. Now select a table column. Copy and paste it to make new ones.
- How do I add a class definition?

  Switch to the Classes pane in the Nib file window. In this pane, you’ll see a listing of all the class types this nib understands. All of the Cocoa objects are predefined, but you’ll have to tell Interface Builder about your own classes before you can make connections to them. You can do this in either of two ways: If you have header files for your new classes, select the Classes > Read Files menu item and specify the header for the class you wish to describe. Interface Builder creates a new listing for this class under its superclass and fills it with any actions or outlets defined in the header. If you don’t have the header file, you can subclass one of the class descriptions already defined in the Classes pane. Select a class, such as NSObject, select the Classes > Subclass menu item, and name the subclass. Then select your subclass and bring up the Attributes pane of the Info window. Select the Objective-C or Java radio button, as appropriate for your class.
- How do I add outlets and actions to a class?

  You can add outlets only to a user defined subclass. Because of the protocol feature of Objective-C, however, you can add an action to any class, whether built in or user defined. Select the Classes pane in the Nib file window. Select the class definition to which you wish to add outlets and actions. The actions and outlets defined by the superclass are listed in gray in the Attributes pane of the Info window. Click the Add button to add actions and outlets to your subclass.
- After I’ve made class definitions in Interface Builder, how do I write them out?

  Select the class definition in the Classes pane and use the menu Classes > Create Files. If this nib is part of a loaded Xcode project, it may ask you if you would like to include the file(s) in a target. Depending on the type of class you’re creating, you’ll get a .m/.h set or a .java file.
- What are IBOutlet and IBAction doing in my code?

  To understand why they’re added to your code, you must understand how Interface Builder parses your code. When you choose Classes > Read Files, Interface Builder tries to find the outlets and actions you’ve declared in your header. You can use these signatures: for Outlets: `id someOutlet;` for Actions: `-(void)myAction:(id)sender` Some people prefer stronger typing of their outlets, so they would try: for Outlets: `NSTextField* someOutlet;` for Actions: `-(void)myAction:(MyApplication*)sender;` However, Interface Builder can’t tell the difference between these signatures and other non-outlet/non-action declarations, so it ignores them. To solve this dilemma, the no-op keywords IBOutlet and IBAction were introduced. Although the first set of signatures still works, Interface Builder also parses methods and fields containing these keywords: for Outlets: `IBOutlet NSTextField* someOutlet;` for Actions: `-(IBAction)myAction:(MyApplication*)sender;`
- How are outlets connected at runtime?

  The runtime code uses the list of outlets you generated in Interface Builder at design time. For example, if you specified an outlet called `foo`, Interface Builder first investigates the class containing the outlet to see if it responds to `setFoo:(id)`. If it does, that method is called with the contents for `foo`. If `setFoo:(id)` doesn’t exist, the instance variable `foo` itself is filled with the contents for `foo`.
- What is an object’s custom class?

  Many widgets have a Custom Class pane in the Info window. You can use this pane to specify that, at runtime, an object should be instantiated as a specific subclass. For example, you could make a subclass of NSApplication called MyApplication. To ensure that an instance of MyApplication is used at runtime, click the File’s Owner of your main nib file. Bring up the Custom Class pane and select MyApplication. Many controls can have custom classes. You could subclass NSSlider to add specific behavior. However, you can still use Interface Builder’s slider facilities. By setting the slider’s custom class, your custom slider is implemented at runtime, but a regular slider is used at design time.
- • How do I subclass a widget in Cocoa Java?

  To subclass a Cocoa Java widget, in addition to selecting your custom Java subclass in the Custom Class pane of the Info window, you must also create the .java file for the subclass and implement a special constructor that takes an NSCoder and a long. Here is an example: `protected MyButton(com.apple.cocoa.foundation.NSCoder decoder, long token) { super(decoder, token);` }
- Why does my application crash when I implement `initWithCoder` (or the above referenced Java Coder constructor) in my custom subclass of a Cocoa widget?

  If you have implemented a subclass of a Cocoa object and then specified it as the class of a widget with the Custom Class pane of the Info window, your custom subclass must not implement any decoding of its own if the nib file format uses non-keyed archiving (pre-10.2). This is because the class swapper that installs your subclass relies upon the coding signature of the real Cocoa widget's class rather than that of your actual subclass. Non-keyed archiving is very particular in such situations, and will crash if the coding signature is different. Note: even if it did not crash, such a scheme would not be useful since Interface Builder has no way of encoding anything useful to the subclass.
- How do I subclass NSTextview in Interface Builder?

  Select NSTextview in the Classes pane of the Nib file window and create a subclass for it. Drag an NSTextview widget from the palette into your design window, double-click the widget to edit it, and then select the desired subclass in the Custom Class pane of the Info window. Please note that the nib file format MUST be 10.2 or beyond for this feature to work, which means that the nib will not properly load on pre-10.2 systems.
- What is the difference between using a custom class and a custom object?

  A custom class is a subclass of one of the interface objects provided in an Interface Builder palette. For a custom class, you can set some properties of the object with the info panel in Interface Builder rather than having to do it all in your code.

  A custom view object is a subclass of NSView. You can define this view any way you like; it is more versatile than a custom class of an existing interface object. However, you must set all the properties programmatically. For more information, see [Cocoa Custom Views](Cocoa%20Custom%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgeydalkcifbesq2iindq).
- What is a dynamic palette and how do I make one?

  Dynamic palettes are custom palettes created by the user. Select the menu item Tools > Palettes > New Palette. A blank palette is created for you. You can now Option-drag widgets from the design window onto the palette. Option-drags containing multiple widgets come off the palette as one unit. Save the palette using the menu item Tools > Palettes > Save.
- How do I remove palettes?

  Palettes can be removed from the toolbar through the Tools > Palettes > Customize Toolbar menu item. Drag them off the toolbar after the customize sheet drops. To remove the palette from the list of available palettes, select the Palettes pane in Interface Builder Preferences. Remove the palette from the palette directory if you don’t want it to appear in this list. Built-in Interface Builder palettes cannot be removed.
- How do I make a UI element smaller than the smallest size allowed by Interface Builder?

  When resizing a UI element such as a button or group box, Interface Builder doesn’t let you resize it past the minimum size defined by the Aqua User Interface Guidelines. If you really need to resize it smaller, then first resize it to its smallest size and then resize again. Interface Builder will let you resize a UI element past its minimum size if the current size is the minimum size.
- I have an outlet named `rate` and in the same class a method named `-setRate:`. When my nib is loaded the `-setRate:` method is called. Why?

  The rule to set outlet connections is as follows: Given an outlet named `foo`, the loader first looks for a setter method named `-setFoo:`. If this method exists, the loader calls it, passing the value of the outlet as a parameter. If this method doesn’t exist, the loader then looks for an instance variable named `foo`. If this instance variable exists, it is set directly. If this instance variable doesn’t exist, the loader logs an error.
- I have a control in a container (for example, a tab view) and I want to move this control outside of the container. Cut and Paste break connections. How can I move a control between containers without breaking connections?

  This is a known limitation. The workaround is to Option-Drag the control to another window within the same nib file and then Option-drag it back to the original window (if you don’t have a second window in your nib, then create a temporary window). Using Option-drag between windows in the same nib doesn’t break connections.
- How do I change the data cell object of an NSTableColumn?

  To set a custom data cell (other than NSTextFieldCell) as the data cell for an NSTableColumn, drag a dataCell object from the Data Views palette and drop it on a column header. To inspect the data cell, select the table column first, and notice that the selected table column displays a small triangle in the corner of the header. Click that triangle once to inspect the data cell. Note that the Info window will let you set certain attributes that may not make sense for display in a table view, such as bezeled background.
- When I add more than 10K of text in an NSTextview in Interface Builder, it crashes.

  This is a known bug in the archiving mechanism in NSTextview. If you have added more than 10288 characters of text to an NSTextview, Interface Builder crashes immediately. The workaround is to set up the text view in Interface Builder, but use your `awakeFromNib` method to load the text programmatically into the text view.
- What are those little yellow badges that show up on the objects in the Instances pane?

  In the Instances pane of the Nib file window in Cocoa projects, a little yellow exclamation point (!) is displayed whenever the object, or a child of that object, is missing a connection. Hold the mouse over the (!) symbol for a tool tip that further defines what’s wrong. Switch to the Outline view to see which child of the object is causing problems. The symbol is displayed for any object that meets any of the following criteria:

  - The object is an instance of NSWindowController and you haven’t connected the window outlet.
  - The object follows the target/action paradigm and there is no target/action specified.
  - Not all of the outlets of a custom object are connected.
  - The delegate and data source of NSOutlineview and NSTableview are not connected.
  - The delegate of NSBrowser is not connected.
- What is the Document Info item in the File Menu?

  Choosing File > Document Info generates a sheet that tells the user almost everything that Interface Builder can ask Xcode about the current document and the project the nib is in.
- What is the Bindings pane and how does it work?

  Cocoa includes a feature that allows you to bind the value and behavioral elements of UI widgets to a controller object. Controller objects (such as NSUserDefaultsController, NSObjectController, and NSArrayController) establish and manage a relationship between UI elements and the data that drives them, significantly reducing or eliminating the need for custom code to manage a detailed user interface. For each object selected in Interface Builder, the Bindings pane of the Info window displays a list of possible bindings that can be bound to a controller object. For example, to bind the value of an NSTextField to an NSUserDefault value, you can use the following procedure:

  1. Drag an NSTextField to a window and select it.
  2. Open the Bindings pane of the Info window.
  3. Scroll to the “value” binding and click to display its details.
  4. Use the Shared User Defaults controller.
  5. Select the “value” model key.
  6. Enter a name for a key. This key is used to store the value in the Shared User Defaults controller.
  7. Do the same for a second NSTextField, using the same name for the key.
  8. Test the interface: changing the value in one text field should cause the other to change as well.
  9. Quit the interface test mode and then enter the interface test mode again. The fields should both contain the last value entered, preserved by the Shared User Defaults controller.
- How can I add a new controller to my nib for use in the Bindings inspector?

  Drag a controller of the type you want from the Controller palette to your Nib file window. If the Controller palette does not automatically show up in the palettes toolbar, it might be because you have a customized toolbar. Select > Tools > Palettes > Customize Toolbar to add the Controller palette to your palette toolbar.
- How do I specify and use a custom subclass of an NSController?

  Use the following procedure:

  1. Create an instance of NSController (or an NSController subclass) either by dragging one from the Controller palette to the Nib file window, or by instantiating NSController from the Classes pane of the Nib file window.
  2. Select the NSController class or subclass in the Classes pane of the Nib file window and use Classes > Subclass NSController to create your custom subclass.
  3. Select the instance of NSController in the Instances pane of the Nib file window and use the Custom Class pane of the Info window to set its class to your custom subclass.

  This method allows Interface Builder to use the concrete class and all of its facilities while you edit your nib, including displaying it in the Bindings pane of the Info window. Note that first creating a subclass of NSController and then instantiating the new subclass would not allow Interface Builder to use the class and display it in the Bindings pane. Therefore, for NSController and its subclasses, instantiation of subclasses is disabled.
- How do I use a WebView object in my nib?

  Drag a WebView object from the WebKit palette to you design window. WebView is a subclass of NSView, and thus behaves similarly in terms of size and auto-size behavior.

  The WebKit inspector has settings that allow you to tune its behavior. The Preferences ID is a way to allow multiple WebView instances to share the same settings across instances and nibs. If no ID is set, the default shared WebPreferences object is used.

  If the WebKit palette does not automatically show up in the palettes toolbar, it might be because you have a customized toolbar. Select > Tools > Palettes > Customize Toolbar to add the WebKit palette to your palette toolbar.

- Do nibs work on MacOS 8/9?

  Yes. IBCarbonRuntime.h has been a part of CarbonLib since version 1.1 (System 8.6). Because IBCarbonRuntime uses CFBundle, you need to package your application correctly.
- How do I load a nib in Carbon or CarbonLib?

  See the sample code in /Developer/Examples/InterfaceBuilder/IBCarbonExample. It uses the `CreateNibReference`, `CreateWindowFromNib`, and `SetMenuBarFromNib` functions to unarchive a Carbon nib. This example also shows how to register a simple Carbon event handler.
- How do I import a .rsrc file from Carbon?

  Interface Builder can import the following compiled resource types: DLOG, DITL, CNTL, MBAR, MENU, WIND, and tab#. DITL and CNTL resources are mapped directly to appearance-savvy controls. Be sure to select the correct text encoding before you import your resources. Interface Builder does not support rez files.
- What kinds of images can I add to my Carbon nib?

  Interface Builder currently understands the following Carbon resource types: ICON, icns, cicn, PICT, and Icon Ref. Tiffs and other NSImage types are not understood by Carbon nibs. See the question “How do I get Interface Builder to display images from my project?” to learn how to use these images.
- Why don’t my Carbon tab views switch at runtime or when I test the interface?

  The Carbon tab control does not automatically switch tab panes for you. Interface Builder does this for you as a convenience at design time. The example in /Developer/Examples/InterfaceBuilder/IBCarbonExample shows one way of switching tabs.
- Can I set up my custom controls in Interface Builder?

  Two types of custom controls are supported: CDEF Proc Pointer and event-based custom controls. In both cases, drag a Custom Control widget from the Other palette into your design window and use the Info panel to select a type of custom control. Look at the IBCarbonExample sample located in the /Developer/Examples/InterfaceBuilder folder for more details on how to use custom controls in your application.
- Does Interface Builder support MacApp?

  No. However, you can unarchive a Carbon nib and manipulate it with standard Carbon functions.

- How do I get Interface Builder to display images from my project?

  - For Carbon nibs:

    Make sure the project is open in Xcode. Add a compiled resource file containing your images to your Xcode project and open the nib. Carbon nibs look inside compiled resource files for PICT, icns, cicn, and ICON resources. These resource files must have the extension .rsrc.
  - For Cocoa nibs:

    Make sure the project is open in Xcode. Add your images to your Xcode project. Any images you add must have an extension understood by NSImage (.tiff, .jpeg, and so forth). Then open the nib.
  - General rules:

    Interface Builder only shows images it can guarantee will exist at runtime, so make sure your images or resources are included in the target that contains the nib. If a nib belongs to multiple targets, it will only show images contained within every one of those targets.
- My nib lost all of its images! Where did they go?

  Xcode must be running with your project open in order for Interface Builder to discover which images are available to you. If your project is open, but you still don’t see any images, or only see a subset of images, check your target settings. Interface Builder only shows images it can guarantee will exist at runtime, so make sure your images are included in the target that contains the nib. If a nib belongs to multiple targets, it only shows images contained within every one of these targets.
- Will Classes > Create Files overwrite my existing files?

  If the files Interface Builder is trying to write already exist, you are given the option to merge your changes through File Merge. You can also tell Interface Builder to stop, or overwrite the existing files.
- I tried to drag an image into Interface Builder and it said I should use Xcode, but I don’t want to.

  If you really want to store files within the nib, you can check the preference “Allow images to be stored inside the nib”. This is not a recommended practice, however.
- I have problems adding nib files to my CVS repository

  The easiest way to add a nib file to a CVS repository is to use the cvswrappers tool. Create a .cvswrappers symlink in your home directory that points to the cvswrappers file located in the /Developer/Tools directory: `ln -s /Developer/Tools/cvswrappers ~/.cvswrappers` You can now add nib files to a CVS repository the same way you do with regular files.

- Why doesn’t nibtool understand my objects.nib file?

  Don’t run nibtool against the object.nib file. Run it against the enclosing .nib directory. objects.nib, objects.xib, classes.nib, and info.nib are internal data structures packaged in a document wrapper.
- How can I localize my nib with nibtool?

  Use the following procedure:

  1. Generate the strings file for a particular nib file, using the following command: `nibtool -L myfile.nib > file.strings` file.strings will now contain entries such as “key” = “key” and be in Unicode (UTF-16) format.
  2. Give the resulting strings file to a translator and have it convert the second “key” entry to “key in other language”.
  3. Reprocess the foreign nibs using the converted strings file: `nibtool -d file.strings -w newLocalization.nib myfile.nib` nibtool will take the contents of file.strings and replace “key” in myfile.nib with “something in other language”.
- I have already translated my nib file and adjusted the sizes of my widgets so the text doesn’t clip. But now I have to add another widget to the development nib. When I translate this nib again, will I loose all of my size changes to the localized nib? How do I get the translation to maintain the size from the old nib file?

  In this example, let’s say we’re translating an English nib to an Italian localization. You need to get the file.strings file and the Italian.nib file and use nibtool to generate a newItalian nib file: `nibtool -d file.strings -I Italian.nib -w newItalian.nib English.nib` nibtool uses the file.strings file for the translation and Italian.nib for the size of objects. The resulting file newItalian.nib will have all of the objects’ size matching Italian.nib.

[Next](Document%20Revision%20History.md)[Previous](Making%20Connections%20in%20Cocoa%20Applications.md)

