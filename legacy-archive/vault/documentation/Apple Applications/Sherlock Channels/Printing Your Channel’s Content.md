---
title: Sherlock Channels
apple_id: 10000121i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-04-09'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Sherlock/Tasks/Printing.html
archived_at: '2026-07-15T05:18:58.639387Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sherlock Channels](Introduction%20to%20Sherlock%20Channels.md)


[Next](Using%20Web%20Services.md)[Previous](Accessing%20Channels.md)

# Printing Your Channel’s Content

This article describes Sherlock’s printing support for channels. Sherlock provides both default and custom printing support for channels. With the default support, Sherlock sends a snapshot of your channel’s interface to the printer when the user selects the Print command. Default printing happens automatically and requires no effort on your part.

If you want to alter the appearance of your channel prior to printing, you must add code to implement custom printing. With custom printing, you can make minor changes to your channel’s existing interface or use a completely separate view to display your data.

This article covers the steps needed to support custom printing in your channel.

Custom printing lets you adjust the content and display of your channel prior to it being rendered for the printer. You do not need to implement custom printing support if you want to display the existing contents of your channel without modification. However, if you want to make modifications to content or use a different view for printing, you must enable custom printing.

To enable custom printing, you must tell Sherlock that your channel supports it. To do this, you assign a non-zero value to the `customPrint` path in the data store. You should do this in your channel’s initialization code, as shown in the following example:

```
<initialize language="JavaScript">
    DataStore.Set("customPrint", 1);
</initialize>
```

Assigning a value to `customPrint` tells Sherlock that your channel defines a trigger to handle printing. The trigger you define must respond to the `print` path, which Sherlock notifies when it receives a print request. In your trigger, you can adjust the content or print specific portions of your channel. For example, if you want to print the contents of only one subview, you can use your print trigger to reroute the print notification to that subview. The following example reroutes the print notification to the search results table of the channel to print only the search results.

```
<trigger language="JavaScript" path="print">
    /* Print only the results table. */
    DataStore.Notify(“MyChannel.ResultsTable.print");
</trigger>
```

If you plan to make significant changes to a channel’s printed content, or if you want to rearrange controls in your main view, do not try to use the print trigger alone. For significant printing changes, it is better to define a custom print view to handle printing. For information on custom print views, see [Using a Custom Print View](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dqljrgeydeojs).

If you want to present a different interface for printing than you do for general display, you can do it using a custom print view. A custom print view is another view you create using Interface Builder and store in your channel’s nib file. Sherlock loads this view with the rest of the nib file and calls your channel’s print trigger at print time to prepare the view for printing.

A custom print view must be an entirely separate view hierarchy from your channel’s main display view. Your print view should contain only those elements you want to be printed. You do not have to have a one-to-one correspondence between controls in your display view and print views. You can even use completely different controls in the two views as long as you know how to map information from one view to the other in your print trigger.

When you supply additional views in your nib file, such as a print view, you must tell Sherlock which view to use for displaying content. Sherlock loads all of the views in your nib file by default. If only one view is present, it uses that view for both display and printing. However, if multiple views are present, you must tell Sherlock which view is your main display view. You do this by setting the `mainViewIdentifier` path to the name of your display view during initialization, as shown in the following example:

```
<initialize language="JavaScript">
    /* Indicate which view is for display */
    DataStore.Set("mainViewIdentifier", "MyDisplayView");

    /* Enable printing */
    DataStore.Set("customPrint", 1);
</initialize>
```

In your print trigger, you can decide which view to use for printing. If you want to print from a custom view, your print trigger is responsible for populating that view with data prior to printing. When the print command is received, your channel’s main display view contains the current data to be printed. Transfer whatever data you need and then send the print notification to your custom view to begin printing.

The following example shows a complete print trigger from the Yellow Pages channel. In this example, the channel copies the selected address, driving directions, and map data over to the view named `PrintView`. Once all the data is set up, the trigger sends a notification to the path `PrintView.print` to begin printing.

```
 <trigger language="JavaScript" path="print">
/* set up the print view */
selectedData = DataStore.Get("YellowPages.data.SelectedRow");
if (selectedData == null)
{
    DataStore.Set("PrintView.name.stringValue", "");
    DataStore.Set("PrintView.address.stringValue", "");
    DataStore.Set("PrintView.phone.stringValue", "");
}
else
{
    DataStore.Set("PrintView.name.stringValue", selectedData.name);
    DataStore.Set("PrintView.address.stringValue", selectedData.address);
    DataStore.Set("PrintView.phone.stringValue", selectedData.phone);
}

mapImage = DataStore.Get("YellowPages.MapImage.data");
DataStore.Set("PrintView.MapImage.data", mapImage);

drivingDirections =
        DataStore.Get("YellowPages.DrivingDirectionsTable.dataValue");
DataStore.Set("PrintView.DrivingDirectionsTable.dataValue",
        drivingDirections);

/* print */
DataStore.Notify("PrintView.print");
</trigger>
```

[Next](Using%20Web%20Services.md)[Previous](Accessing%20Channels.md)

